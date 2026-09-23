---
name: commit
description: Create Git commits with Conventional Commits messages and selective staging. Use when the user asks to commit changes.
---

# Commit

Review the working tree and index with `git status`, `git diff`, and `git diff --cached`. Commit only changes within the user's requested scope. Preserve unrelated edits and staged changes; use hunk selection when a file mixes concerns.

Stage reviewed paths explicitly with `git add <file>`, not `git add .` or `git add -A`. Exclude secrets, credentials, `.env` files, and large binaries. Keep one logical change per commit. Do not amend pushed commits or bypass hooks with `--no-verify`.

## Message convention

Use `<type>(<optional-scope>): <description>`. Write a concise, lowercase imperative description without a trailing period. Scope is an optional module or directory in kebab-case, not an issue ID.

| Type | Change |
|---|---|
| `feat` | Add, change, or remove a feature |
| `fix` | Correct a bug |
| `refactor` | Restructure without changing behavior |
| `perf` | Improve performance |
| `style` | Formatting only |
| `test` | Add or correct tests |
| `docs` | Documentation only |
| `build` | Dependencies, build tools, or versions |
| `ops` | Infrastructure, deployment, or CI/CD |
| `chore` | Other maintenance |

Add a body only when motivation or behavior needs explanation. Put issue references in an optional footer. For a breaking change, add `!` before the colon and a `BREAKING CHANGE:` footer describing the impact and migration.

Use `chore: init` for initial commits; retain Git's default merge and revert subjects. Do not append attribution or signature trailers.

Examples: `fix(api): handle empty responses`, `docs: clarify setup steps`.

After committing, report the commit hash, subject, and any changes left uncommitted.
