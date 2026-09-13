---
name: sanitize
description: Use when preparing a repository for anonymous (double-blind) artifact submission. Copies the repo, strips identifying content, verifies the copy, and prepares it for Anonymous GitHub or Zenodo.
---

# Sanitize

Never modify the original repository. All work happens on an exported copy; the git history is the largest leak and is never carried over.

## Procedure

1. Check that `identifiers.toml` next to this file lists the user's own name, emails, usernames, institution, supervisor, own URLs, and absolute path prefixes.
2. Before running, grep the source repo for anything that should be added to the list, and update `identifiers.toml` if needed:
   ```bash
   git -C <repo> log --format='%an %ae' | sort -u        # author identities used in history
   grep -rIoh -E '[[:alnum:]._+-]+@[[:alnum:].-]+' <repo> | sort -u
   grep -rIoh -E '/(users|home|Users|scratch)/[^/ ]+' <repo> | sort -u
   ```
3. Run the script. The output directory must not exist yet.
   ```bash
   uv run --python 3.12 ~/.claude/skills/sanitize/scripts/sanitize.py <repo> <out_dir> [--extra data]
   ```
   It exports tracked files only (`git archive HEAD`), copies any `--extra` paths in, deletes everything under `[remove]` plus dangling symlinks, clears Jupyter outputs, applies the replacement rules, then scans the copy again and writes `<out_dir>.sanitize-report.md`. Exit code 1 means the verification pass still found hits.
   - Projects created from `research-template` git-ignore `data/` and `paper/`. Results the artifact must ship need `--extra data` (or a narrower path such as `--extra data/<benchmark>/results`); never pass `--extra paper`.
4. Read the report with the user. Every entry under "Remaining hits" must be either fixed (extend `identifiers.toml` and rerun into a fresh directory) or explicitly accepted as a false positive (third-party emails in dependency metadata, upstream GitHub URLs).
5. Walk the manual checklist below; the script cannot cover these.
6. Package for hosting (see Hosting).

## Replacement policy

| Category | Action |
|----------|--------|
| AI assistant config (`CLAUDE.md`, `.claude/`, `.cursorrules`, `AGENTS.md`) | delete |
| Secrets, logs, IDE settings, Slurm output | delete |
| Names, institutions, supervisor | replace with `ANONYMIZED` |
| Emails | replace with `anonymous@example.com` |
| Usernames (GitHub, HPC account) | replace with `anonymous` |
| Own repo URLs, own DOIs / arXiv IDs | replace with `URL-REMOVED` |
| Absolute path prefixes | rewrite to `./` so paths become relative |
| Jupyter notebooks | outputs and kernelspec cleared |
| Git history, untracked files | not exported |

## Manual checklist

For a `research-template` project the tracked files are `.claude/`, `AGENTS.md` (symlink into `.claude/`), `configs/`, `eval/`, `scripts/`, `src/`, `LICENSE`, `README.md`, `pyproject.toml`. The first two are deleted by the script; the rest need the checks below.

- `LICENSE`: copyright holder line. Replace with `Copyright (c) <year> Anonymous Authors` or drop the license until camera-ready.
- `CITATION.cff`, `pyproject.toml`, `setup.py`, `package.json`, `Cargo.toml`: `authors`, `maintainers`, `homepage`, `repository` fields.
- `README`: the template's `Citation`, `Acknowledgments`, and `News` sections; funding, self-citations, "our previous work" phrasing, badges linking to CI or the original repo.
- `configs/*.yaml`: `dataset:` entries pointing at the user's own HuggingFace org or private datasets; add the org name to `identifiers.toml` under `urls`.
- Distinctive constants reused across the user's papers (e.g. a personal default seed) link submissions to each other; consider changing them for the artifact only if a prior paper already exposes them.
- Dockerfile `LABEL`, `docker-compose` image names, CI workflows referencing the original org.
- Slurm scripts: `--account`, `--mail-user`, cluster-specific module names that identify the institution.
- Binary files listed in the report: figures with EXIF, PDFs with author metadata (`exiftool -all= <file>`), pickled objects or checkpoints that embed paths.
- Dataset files that contain developer names, emails, or commit authors when the study mines real repositories. Decide with the user whether to pseudonymise or exclude.
- Paper draft or `paper/` directory: exclude entirely; the artifact should not contain the manuscript.

## Hosting

Datasets and model weights:
- Artifacts produced by this work (a new benchmark, fine-tuned checkpoints, collected traces) go to HuggingFace under a fresh anonymous organisation created for the submission, not under the user's account. Set the dataset card / model card author to `Anonymous`, keep the repo public or gated, and reference it from the artifact README. Do not use `--extra data` to ship them inside the code artifact; large files belong on HuggingFace.
- Datasets and models reused from prior work are only cited by their original HuggingFace or paper reference; nothing needs re-uploading.
- After acceptance, transfer the HuggingFace repos to the real organisation (Settings > Transfer) so the existing links keep resolving.

Anonymous GitHub (https://anonymous.4open.science) proxies a real GitHub repository, so the sanitized copy must first be pushed to GitHub:
1. Initialise a fresh history in the copy with an anonymous identity; never push the original repository's history.
   ```bash
   cd <out_dir>
   git init -q && git add -A
   git -c user.name=Anonymous -c user.email=anonymous@example.com commit -qm "chore: init"
   ```
2. Create a new private repository on GitHub with a neutral name (no project codename that appears in prior talks or preprints), then push:
   ```bash
   git remote add origin git@github.com:<account>/<neutral-name>.git
   git push -u origin main
   ```
   Anonymous GitHub hides the source URL from reviewers, so the user's own account is acceptable, but a secondary account removes the risk entirely.
3. On anonymous.4open.science, sign in with the account that owns the repo, choose the repository, add the same terms as `identifiers.toml` to its keyword list as a second layer, and set an expiration date after the notification deadline.
4. Put the resulting `anonymous.4open.science/r/<id>` link in the paper. Later fixes go through the same path: rerun the sanitizer into a fresh directory, copy the result over the pushed working tree, commit, push; Anonymous GitHub picks up the new commit.

Zenodo:
- Zip the sanitized directory (`zip -r artifact.zip <out_dir> -x '*.DS_Store'`).
- Create the record with author `Anonymous` and no ORCID or affiliation; leave the record unpublished and share the restricted-access or review link, or publish only when the venue requires a DOI at submission time.
- Zenodo records are permanent once published; prefer keeping the record in draft until acceptance.

After acceptance, replace the anonymous artifact with the real repository and update the paper link; do not de-anonymize the anonymous copy in place.
