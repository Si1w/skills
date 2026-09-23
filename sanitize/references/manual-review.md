# Review the sanitized copy

## Replacement policy

| Category | Action |
|----------|--------|
| AI assistant config (`CLAUDE.md`, `.claude/`, `.agents/`, `.cursorrules`, `AGENTS.md`) | delete |
| Secrets, logs, IDE settings, Slurm output | delete |
| Names, institutions, supervisor | replace with `ANONYMIZED` |
| Emails | replace with `anonymous@example.com` |
| Usernames (GitHub, HPC account) | replace with `anonymous` |
| Own repo URLs, own DOIs / arXiv IDs | replace with `URL-REMOVED` |
| Absolute path prefixes | rewrite to `./` so paths become relative |
| Jupyter notebooks | outputs and kernelspec cleared |
| Git history, untracked files | excluded by the default Git export; review explicit extras and non-Git input separately |

## Manual checklist

Inspect only files present in the export. For a `research-template` project the tracked files are `.agents/`, `AGENTS.md`, `configs/`, `eval/`, `scripts/`, `src/`, `LICENSE`, `README.md`, `pyproject.toml`. The first two are deleted by the script; the rest need the checks below.

- `LICENSE`: inspect identifying copyright lines. Preserve third-party notices and required licensing terms; do not delete or rewrite them as if they belonged to the submitting authors. Record any unresolved conflict with anonymity.
- `CITATION.cff`, `pyproject.toml`, `setup.py`, `package.json`, `Cargo.toml`: `authors`, `maintainers`, `homepage`, `repository` fields.
- `README`: the template's `Citation`, `Acknowledgments`, and `News` sections; funding, self-citations, "our previous work" phrasing, badges linking to CI or the original repo.
- `configs/*.yaml`: `dataset:` entries pointing at the user's own HuggingFace org or private datasets; add the org name to `identifiers.toml` under `urls`.
- Distinctive study settings may link submissions to prior work. Flag that risk, but preserve seeds, configurations, raw data, and results needed to reproduce the reported study.
- Dockerfile `LABEL`, `docker-compose` image names, CI workflows referencing the original org.
- Slurm scripts: `--account`, `--mail-user`, cluster-specific module names that identify the institution.
- Binary files listed in the report: figures with EXIF, PDFs with author metadata, pickled objects or checkpoints that embed paths.
- Dataset files that contain developer names, emails, or commit authors when the study mines real repositories. Decide with the user whether to pseudonymise or exclude.
- Paper draft or `paper/` directory: exclude entirely; the artifact should not contain the manuscript.

Keep the verification report outside the public artifact: its source path and matched identifiers can themselves identify the authors.
