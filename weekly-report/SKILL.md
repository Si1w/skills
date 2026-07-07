---
name: weekly-report
description: Use when the user wants to review the project progress and render into a weekly report powerpoint template, or push/pull the weekly report to Google Slides.
---

# Weekly Report

Maintain one accumulating deck, `weekly-report/weekly-report.pptx`: each week's slides are built from `template/` and prepended, so the newest week is on top and past weeks stay below for recap.

All commands run from the repo root with `uv run python`.

## Workflow

1. **Gather content**: completed tasks, in-progress work, results and figures, blockers, plans. Figures must be image files on disk; render data to PNG first if needed. Use last week's slides in the deck to write the recap.

2. **Pick templates by id** from `scripts/schema.py`, where `TEMPLATES` defines each template's purpose and the meaning of every fillable shape id. Do not re-inspect the pptx (`build.py inspect` is for debugging the template only).

   | name | description |
   |------|-------------|
   | `title` | Cover: report title, project name, researcher, date. Always the first slide of a week; it separates weeks in the deck. |
   | `recap` | Project overview (motivation, purpose, venue, DDL) and last week's 1:1 recap. |
   | `completed` | Completed tasks: three `[Category] description` rows. |
   | `in-progress` | Ongoing work: three active-task rows with current status. |
   | `results` | One figure/table with explanation and takeaway. Repeat once per figure. |
   | `results-text` | Full-page explanation/takeaway card, for results without a figure. |
   | `results-big-figure` | Full-width large figure with caption; `images: {"figure": path}` fits and centers the image automatically. |
   | `blockers` | Support needed: technical, conceptual, resource columns. |
   | `plans` | Timeline: next week, this month, long-term milestone, target DDL. |
   | `next-week` | Closing divider. |

3. **Compose the manifest** (JSON, in the scratchpad): this week's slides in order, starting with `title`. Templates may be omitted, reordered, or repeated; include only slides with real content.

   ```json
   {
     "slides": [
       {"template": "title", "text": {"86": "Project: X", "87": "Researcher: K | Date: 2026-07-07"}},
       {"template": "results",
        "text": {"154": "How the figure was produced", "156": "The core insight."},
        "images": {"151": "/abs/path/fig1.png"},
        "delete": ["159"]}
     ]
   }
   ```

   - `text`: shape id -> text; `\n` starts a new line in the same style.
   - `images`: shape id -> image path. The image is stretched to the existing frame, so roughly match its aspect ratio (exception: the `figure` slot fits automatically).
   - `delete`: shape ids to remove (unused arrows, decorations, empty rows).
   - Fill or delete every placeholder on each included slide; never ship literal `[Placeholder ...]` text.
   - Pydantic validation rejects wrong template or shape ids and lists the valid options.

4. **Preview**: build to the scratchpad, render to PDF, and inspect every page yourself (text overflow, image fit, leftover placeholders) before showing the user. Iterate on the manifest here.

    ```bash
    uv run python weekly-report/scripts/build.py build <manifest.json> -o <scratchpad>/preview.pptx --fresh

    soffice --headless --convert-to pdf <scratchpad>/preview.pptx --outdir <scratchpad>
    ```

5. **Finalize**: once approved, build into the deck (prepends; creates the file if absent), then push.

    ```bash
    uv run python weekly-report/scripts/build.py build <manifest.json>
    ```

   Run this once per week: rerunning prepends a duplicate. `--fresh` discards all history; only on explicit request.

## Google Slides sync

One-time setup: OAuth client JSON at `~/.config/gdrive/credentials.json` (see `references/gcp-setup.md`); first run opens a browser for consent. The linked presentation id lives in `weekly-report/weekly-report.gslides.json`.

```bash
uv run python weekly-report/scripts/gslides.py push   # create/update the presentation, print URL

uv run python weekly-report/scripts/gslides.py pull   # overwrite local pptx with the online version
```

Push replaces the whole presentation with the local file, so pull first if the user edited the deck online.
