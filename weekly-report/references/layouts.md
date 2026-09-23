# Weekly report layouts

Use these layouts when composing or changing slides. The implementation in the project's `theme/layouts/` and `week/_template.md` is authoritative if it differs from this guide.

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

Helper classes on the default layout: `wr-card` (white row card with navy rule, for completed/in-progress items), `wr-figure` (framed figure box), `wr-finding` (gray box for one key result, written as `**Finding N:** ...`) and `wr-compare` (a flex row of white boxes for side-by-side comparison, e.g. one per condition in a case study; add `wr-good` / `wr-bad` on a box for a green or red top rule). Inline images under bullets are auto-capped at 40vh.
