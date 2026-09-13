# se-research-skills

A collection of Agent skills for software engineering research and development workflows.

## Skills

| Skill | Description |
|-------|-------------|
| [commit](commit/) | Create git commits following the Conventional Commits format with a review-then-stage procedure |
| [create](create/) | Guidelines for the KCL CREATE HPC cluster: login, partitions, Slurm jobs, storage, cache, and pinned library versions |
| [improve-code-arch](improve-code-arch/) | Scan a codebase for module-deepening opportunities, pick one, then grill through the refactor decisions |
| [weekly-report](weekly-report/) | Compose and present the weekly report slides with Slidev |

## Setup

Symlink or copy this directory to `~/.claude/skills/` so the skills are discovered by Claude Code.

```bash
ln -sfn "$(pwd)" ~/.claude/skills
```
