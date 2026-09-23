---
name: weekly-report
description: Create, edit, present, or export weekly research slides in the local Slidev weekly-report project.
---

# Weekly Report

The project is `~/Desktop/weekly-report`. Each week uses `week/YYYY-MM-DD/YYYY-MM-DD.md`, with figures in the same folder. Shared styling lives in the local addon `theme/`; routine reports use its existing layouts.

## Compose or edit

Gather completed work, ongoing work, results, blockers, and plans from available project evidence and user notes. Read the previous week when writing a recap. Ask only for missing facts that affect the report; do not invent progress or results.

For a new week, copy `week/_template.md` into the dated folder without overwriting an existing report. Set `title`, `researcher`, and `date`; retain `theme: default` and `addons: [weekly-report]`. The addon supplies the cover heading.

Read [layouts.md](references/layouts.md) when authoring slides. Include only slides with real content. Place figure images in the week folder and reference them as `./name.png`; render data to an image when needed.

## Present or export

Use the requested date, or the latest ISO-dated folder under `week/` if no date is given. Run from the project root:

```bash
slidev week/<date>/<date>.md --open
slidev export week/<date>/<date>.md --output week/<date>/<date>.pdf
```

The project needs its local dependencies and the Slidev CLI. Use the existing package manager and lockfile to restore missing dependencies; check the local CLI before assuming a global installation is available.

For new or changed slides, export a preview and inspect every page for overflow, image fit, and template placeholders. Fix rendering problems before delivery. Use a temporary preview path when PDF is not requested, and remove only the preview created for this task. For export-only requests, inspect the resulting PDF and retain it at the requested destination. Report the source or export path and any rendering checks that could not be completed.
