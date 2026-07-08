---
name: md2gdoc
description: Use when the user wants to sync a local Markdown file with Google Docs; push a .md up to a Google Doc, or pull a Google Doc back into Markdown for local editing. Keywords google doc, gdoc, google docs, push, pull, md2gdoc.
---

# md2gdoc

Sync one Markdown file with one Google Doc, both directions, via pandoc docx conversion. Push renders the Markdown body to .docx against a standard reference template, then uploads it as a Google Doc; pull exports the Doc as .docx and pandoc converts it back to Markdown. The Doc id lives in the file's frontmatter, so the same file always maps to the same Doc.

## Setup (once)

- pandoc ships as a Python dependency (`pypandoc-binary`), installed by `uv sync`; no brew install needed. A system pandoc on PATH is used as fallback.
- A Google Cloud project and OAuth credentials. Walk the user through `references/gcp-setup.md`, then put the downloaded `credentials.json` at `~/.config/gdrive/credentials.json` (override the directory with `GDRIVE_HOME`). This credential is shared with the weekly-report skill. Skip this if `credentials.json` already exists.

## Workflow

First run opens a browser for one-time consent.

- Push (create on first run, update the same Doc after): `uvsk scripts/md2gdoc.py push <file.md>`
- Push with citations: add `--bib refs.bib` (and optionally `--csl style.csl`) to render `[@key]` citations via `--citeproc`.
- Pull (export the Doc back, frontmatter kept): `uvsk scripts/md2gdoc.py pull <file.md>`

On push, horizontal rules (`---`) are stripped and images are embedded without rendering their alt text as a caption.

## Template

`template/reference.docx` is the standard reference template that controls Doc styling (fonts, heading styles, margins); pandoc only reads its styles, not its body content. It is currently a Google Docs export, so pushed Docs match that house style. To restyle, edit its styles in Word/LibreOffice, export a styled Google Doc as .docx over it, or pass a different file with `--template`. Reset to the pandoc default with `pandoc -o template/reference.docx --print-default-data-file reference.docx`.

## References

| Reference | Description |
|---|---|
| `references/gcp-setup.md` | How to set up a Google Cloud project and OAuth credentials for this skill (once per machine) |
