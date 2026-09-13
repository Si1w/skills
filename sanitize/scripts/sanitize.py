#!/usr/bin/env -S uv run --python 3.12 --script
"""Copy a repository, strip identifying content, and verify the result.

Usage: sanitize.py <src_repo> <out_dir> [--config identifiers.toml]
"""

import argparse
import fnmatch
import json
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Generic patterns checked in the verification pass regardless of the config.
GENERIC_PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "home path": re.compile(r"(?<![\w/])/(?:scratch/)?(?:users|home|Users)/[\w.-]+"),
    "github url": re.compile(r"github\.com/[\w.-]+"),
    "orcid": re.compile(r"\b\d{4}-\d{4}-\d{4}-\d{3}[\dX]\b"),
}


def load_config(path: Path) -> dict:
    with path.open("rb") as f:
        return tomllib.load(f)


def export_repo(src: Path, out: Path) -> None:
    """Export tracked files only (no .git, no untracked files)."""
    out.mkdir(parents=True)
    if (src / ".git").exists():
        archive = subprocess.run(
            ["git", "-C", str(src), "archive", "--format=tar", "HEAD"],
            check=True, capture_output=True,
        )
        subprocess.run(["tar", "-x", "-C", str(out)], input=archive.stdout, check=True)
    else:
        shutil.copytree(src, out, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git"))


def copy_extra(src: Path, out: Path, extras: list[str]) -> list[str]:
    """Copy git-ignored paths (e.g. data/) that the artifact must still ship."""
    copied = []
    for rel in extras:
        s, d = src / rel, out / rel
        if not s.exists():
            sys.exit(f"--extra path not found: {s}")
        shutil.copytree(s, d, dirs_exist_ok=True) if s.is_dir() else (d.parent.mkdir(parents=True, exist_ok=True), shutil.copy2(s, d))
        copied.append(rel)
    return copied


def remove_paths(out: Path, patterns: list[str]) -> list[str]:
    removed = []
    for p in sorted(out.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if not (p.exists() or p.is_symlink()):
            continue
        rel = p.relative_to(out).as_posix()
        matched = any(fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(p.name, pat) for pat in patterns)
        dangling = p.is_symlink() and not p.exists()
        if matched or dangling:
            shutil.rmtree(p) if p.is_dir() and not p.is_symlink() else p.unlink()
            removed.append(rel + (" (dangling symlink)" if dangling and not matched else ""))
    return sorted(removed)


def is_text(p: Path) -> bool:
    try:
        return b"\0" not in p.read_bytes()[:8192]
    except OSError:
        return False


def build_rules(cfg: dict) -> list[tuple[re.Pattern, str, str]]:
    """Return (pattern, replacement, label) tuples, longest literal first."""
    rules = []
    for prefix in cfg.get("paths", {}).get("prefixes", []):
        rules.append((re.compile(re.escape(prefix) + r"/?"), "./", f"path {prefix}"))
    placeholders = cfg.get("placeholders", {})
    for category, literals in cfg.get("identity", {}).items():
        repl = placeholders.get(category, "ANONYMIZED")
        for lit in literals:
            rules.append((re.compile(re.escape(lit), re.IGNORECASE), repl, f"{category} {lit}"))
    rules.sort(key=lambda r: len(r[2]), reverse=True)
    return rules


def clear_notebook(text: str) -> str:
    nb = json.loads(text)
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    nb.setdefault("metadata", {}).pop("kernelspec", None)
    return json.dumps(nb, indent=1, ensure_ascii=False) + "\n"


def rewrite(out: Path, rules) -> tuple[dict[str, int], list[str]]:
    changed: dict[str, int] = {}
    binaries: list[str] = []
    for p in out.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(out).as_posix()
        if not is_text(p):
            binaries.append(rel)
            continue
        text = p.read_text(encoding="utf-8", errors="surrogateescape")
        new = clear_notebook(text) if p.suffix == ".ipynb" else text
        hits = 0
        for pat, repl, _ in rules:
            new, n = pat.subn(repl, new)
            hits += n
        if new != text:
            p.write_text(new, encoding="utf-8", errors="surrogateescape")
            changed[rel] = hits
    return changed, sorted(binaries)


def verify(out: Path, cfg: dict) -> list[str]:
    literals = [lit for lits in cfg.get("identity", {}).values() for lit in lits]
    literals += cfg.get("paths", {}).get("prefixes", [])
    checks = [(f"identifier {lit}", re.compile(re.escape(lit), re.IGNORECASE)) for lit in literals]
    checks += list((k, v) for k, v in GENERIC_PATTERNS.items())
    placeholders = set(cfg.get("placeholders", {}).values())
    findings = []
    for p in out.rglob("*"):
        if not p.is_file() or not is_text(p):
            continue
        rel = p.relative_to(out).as_posix()
        for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for label, pat in checks:
                m = pat.search(line)
                if m and m.group(0) not in placeholders:
                    findings.append(f"{rel}:{i}: [{label}] {m.group(0)}")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--config", type=Path, default=HERE.parent / "identifiers.toml")
    ap.add_argument("--extra", action="append", default=[], metavar="PATH",
                    help="git-ignored path (relative to src) to copy in anyway, e.g. data/")
    args = ap.parse_args()

    if args.out.exists():
        sys.exit(f"refusing to overwrite existing {args.out}")
    if not args.config.exists():
        sys.exit(f"config not found: {args.config}")

    cfg = load_config(args.config)
    export_repo(args.src.resolve(), args.out)
    extras = copy_extra(args.src, args.out, args.extra)
    removed = remove_paths(args.out, cfg.get("remove", {}).get("paths", []))
    changed, binaries = rewrite(args.out, build_rules(cfg))
    findings = verify(args.out, cfg)

    report = args.out.parent / f"{args.out.name}.sanitize-report.md"
    lines = [f"# Sanitize report for {args.src}", ""]
    lines += ["## Extra paths copied (git-ignored)", ""] + [f"- {e}" for e in extras] + [""]
    lines += ["## Removed", ""] + [f"- {r}" for r in removed] + [""]
    lines += ["## Rewritten (replacements)", ""] + [f"- {k} ({v})" for k, v in sorted(changed.items())] + [""]
    lines += ["## Binary files (not checked, review manually)", ""] + [f"- {b}" for b in binaries] + [""]
    lines += ["## Remaining hits", ""] + ([f"- {f}" for f in findings] or ["- none"]) + [""]
    report.write_text("\n".join(lines))

    print(f"removed {len(removed)}, rewrote {len(changed)}, {len(binaries)} binaries, {len(findings)} remaining hits")
    print(f"report: {report}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
