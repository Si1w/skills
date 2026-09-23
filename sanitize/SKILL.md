---
name: sanitize
description: Prepare and verify an anonymous repository copy for double-blind artifact submission, with optional hosting preparation.
---

# Sanitize

Produce an anonymous artifact without changing the source repository or carrying over its Git history. Work in a new destination outside the source tree. Keep the local verification report outside the artifact because it can contain original identifiers.

## Export and verify

1. Review [identifiers.toml](identifiers.toml) and source metadata for the submitting authors' names, emails, accounts, institutions, own URLs, and path prefixes. Distinguish these from third-party attribution. Check `git status` and note that Git exports use `HEAD`, excluding uncommitted work; resolve a requested working-tree export before running.
2. Inspect source and extra-path symlinks before export. The script can follow live symlinks during rewriting; do not run it on links that could escape the output copy. Extra paths must be relative paths inside the source, without `..`, and must not introduce history, secrets, or the manuscript.
3. Run the bundled [script](scripts/sanitize.py) using its resolved location, not a hard-coded assistant installation path:

   ```bash
   uv run --python 3.12 <skill-dir>/scripts/sanitize.py <repo> <new-out-dir> [--extra data/<benchmark>/results]
   ```

   Replace `<skill-dir>` with the directory containing this `SKILL.md`. The default configuration is `identifiers.toml` beside it; `--config <path>` selects a project-specific copy. The destination must not exist. For a Git repository, the script exports `HEAD`; for a non-Git directory, it copies files except `.git`, so inspect that directory's contents first.
4. Read `<new-out-dir>.sanitize-report.md`. Exit code 1 indicates remaining matches. Fix author-identifying matches and rerun into a fresh directory; document evidence for third-party false positives. Ask only when ownership or a substantive data change is unclear. An unchanged finding requires diagnosis, not another identical run.
5. Apply [manual-review.md](references/manual-review.md) to metadata, notebooks, binary assets, licenses, and research data. Automated text scanning alone does not establish anonymity.

For research-template projects, `data/` and `paper/` are normally ignored. Include only necessary result files with `--extra`; exclude `paper/`. Keep large datasets and weights separate from the code package.

## Deliver or host

A preparation request is complete with the sanitized copy, verification findings, and any unresolved anonymity limitations. Do not describe the artifact as ready while identifying hits or relevant binary checks remain unresolved.

Read [hosting.md](references/hosting.md) only when packaging or hosting is requested. Local preparation can continue independently of publishing. Use existing authorization for a specified upload; if the destination or publication scope is missing, prepare the artifact before asking for that choice.
