---
name: weekly-report
description: Use when the user wants to review the project progress and compose the weekly report slides (Slidev), or present/export an existing week.
---

# Weekly Report

The deck lives in `~/Desktop/weekly-report`, a Slidev project. Each week is one folder: `week/YYYY-MM-DD/YYYY-MM-DD.md`, with that week's figures in the same folder. Shared styling is the local addon in `theme/`; do not edit it for routine reports.

## Commands

`slidev` is installed globally (`npm i -g @slidev/cli`); the project's `node_modules/` must exist for the local addon and theme (run `npm install` once if missing). Replace `<date>` with the week folder name; the latest week is the last entry of `ls week | sort`.

```bash
cd ~/Desktop/weekly-report
slidev week/<date>/<date>.md --open                                   # present a week
slidev export week/<date>/<date>.md --output week/<date>/<date>.pdf   # export to PDF (into its week folder)
```

## Writing a new week

1. **Gather content**: completed tasks, in-progress work, results and figures, blockers, plans. Read last week's `week/<date>/<date>.md` to write the recap. Figures must be image files; render data to PNG first if needed, and place them in the week folder (reference as `./name.png`).

2. **Create the file**: copy `week/_template.md` to `week/YYYY-MM-DD/YYYY-MM-DD.md`. In the frontmatter, set `title` (the project name), `researcher`, and `date`; keep `theme: default` and `addons: [weekly-report]`. The "Weekly Research Update" cover heading is a constant in the addon layout.

3. **Compose slides** using these layouts (from `theme/layouts/`):

   | layout | purpose |
   |---|---|
   | `cover` | Navy cover, filled from frontmatter. Always the first slide. |
   | (default) | Cream page, navy title (`#`), arrow bullets; nested list items render as dash sub-bullets. Markdown tables get the navy-header style. |
   | `cards` | Completed / In Progress / Content pages: title higher up, then `wr-card` rows; set `icon: check` (completed) or `icon: spin` (in progress / agenda) in the slide frontmatter. |
   | `results` | Figure review: text column left (default slot), framed figure right via `::figure::` slot. |
   | `recap` | Project overview and last week's recap as two cards, via `::left::` / `::right::` slots. |
   | `blockers` | Navy support-needed page; wrap three `<div>`s in `<div class="wr-3col">`. |
   | `plans` | Timeline; wrap four `<div>`s (Next Week / This Month / Milestone / Target DDL) in `<div class="wr-timeline">`. |
   | `section` | Navy divider page with green title (e.g. closing "Plan for the Next Week"). |

   Helper classes on the default layout: `wr-card` (white row card with navy rule, for completed/in-progress items) and `wr-figure` (framed figure box). Inline images under bullets are auto-capped at 40vh.

   Include only slides with real content; never leave template placeholder text.

4. **Preview**: run the export command above, then inspect every PDF page yourself (text overflow, image fit, leftover placeholders) before showing the user. Delete the preview PDF afterwards unless the user wants it.
