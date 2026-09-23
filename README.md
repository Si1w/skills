# se-research-skills

A collection of Agent skills for software engineering research and development workflows.

## Skills

| Skill | Description |
|-------|-------------|
| [commit](commit/) | Create git commits following the Conventional Commits format with a review-then-stage procedure |
| [create](create/) | Run and troubleshoot KCL CREATE jobs, with references for Slurm, storage, and project environments |
| [experiment-design](experiment-design/) | Design empirical SE studies using ACM/SIGSOFT standards, record ADRs, and map agreed decisions to project code |
| [sanitize](sanitize/) | Copy a repository, strip identifying content, and verify it for double-blind artifact submission |
| [weekly-report](weekly-report/) | Compose and present the weekly report slides with Slidev |

## Maintaining skills

Keep descriptions focused on the request that should select the skill. Keep essential constraints and completion criteria in `SKILL.md`; load operational references only for the relevant task. Preserve project-specific knowledge, and remove repeated generic advice or mandatory steps that do not change the outcome. These conventions follow [OpenAI's guidance on skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

The five skills above are maintained in this repository. `.system/`, `synced/`, and installed plugin caches have separate upstream sources; make durable changes at their source rather than relying on edits to managed copies.
