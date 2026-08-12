# se-research-skills

A collection of Agent skills for software engineering research and development workflows.

## Skills

### Research

| Skill | Description |
|-------|-------------|
| [ese-review](ese-review/) | Review a paper against ACM/SIGSOFT Empirical Standards |
| [mh-writing](mh-writing/) | Write and improve SE research papers paragraph by paragraph (Mark Harman's guidelines) |
| [grill-me](grill-me/) | Adversarially grill a paper or document to expose weaknesses |
| [excalidraw-diagram](excalidraw-diagram/) | Generate flowcharts and architecture diagrams as .excalidraw + PNG, with SVG icon support |

### Git Workflow

| Skill | Description |
|-------|-------------|
| [git-push](git-push/) | Push current branch to remote |

### Reporting

| Skill | Description |
|-------|-------------|
| [weekly-report](weekly-report/) | Compose and present the weekly report slides with Slidev |

### Documents

| Skill | Description |
|-------|-------------|
| [md2gdoc](md2gdoc/) | Sync a local Markdown file with a Google Doc, both directions |

## References

- [obra/superpowers](https://github.com/obra/superpowers) — The original skill collection that several skills in this repo were adapted from.
- [Draft Guidelines for My Students on Writing Software Engineering Research Papers](https://cragkhit.github.io/files/harman-writing-advice.pdf) — Mark Harman's writing guidelines, used as the basis for the [mh-writing](mh-writing/) skill.

## Setup

```bash
uv sync  # install Python dependencies
```

Script commands in the skills use the `uvsk` alias:

```bash
alias uvsk='uv run --project <path-to-this-repo>'
```
