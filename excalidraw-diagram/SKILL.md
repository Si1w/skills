---
name: excalidraw-diagram
description: Use when the user wants a flowchart, process or decision diagram, architecture diagram, or tree/graph diagram, or asks to draw, sketch, or visualize a flow, pipeline, or system. Produces an editable .excalidraw file plus a PNG. Keywords flowchart, flow chart, diagram, excalidraw, 流程图, 架构图.
---

# Excalidraw Diagram

Turn a node-and-edge description into an editable `.excalidraw` file and a PNG. You never compute coordinates. You describe the graph; `build.py` lays it out.

Covers any directed-graph diagram: flowchart, decision flow, architecture, tree. Not for sequence diagrams (different layout model).

## Workflow

1. Settle the graph with the user: nodes, edges, direction, formality.
2. Write a graph JSON file (schema below).
3. Build: `uvsk scripts/build.py graph.json -o out.excalidraw`
4. Export PNG: `node scripts/export_png.mjs out.excalidraw out.png [scale]`
5. Report both file paths.

`build.py` is standard-library only; the PNG step needs puppeteer (`npm install -g puppeteer`, once).

## Graph JSON

The example uses the formal settings (`roughness` 0, `font` 2), not the defaults.

```json
{
  "direction": "TB",
  "roughness": 0,
  "font": 2,
  "nodes": [
    {"id": "a", "label": "Start", "shape": "ellipse"},
    {"id": "b", "label": "Process step", "shape": "rectangle"},
    {"id": "c", "label": "Valid?", "shape": "diamond"},
    {"id": "d", "label": "Postgres", "image": "https://.../postgresql.svg"}
  ],
  "edges": [
    {"from": "a", "to": "b"},
    {"from": "c", "to": "b", "label": "yes"}
  ]
}
```

| Field | Values | Meaning |
|-------|--------|---------|
| `direction` | `TB` (default), `LR` | flow top-to-bottom or left-to-right |
| `roughness` | `0`, `1`, `2` | 0 clean and formal, 1 light sketch, 2 sketchy |
| `font` | `1`, `2`, `3` | 1 hand-drawn, 2 normal (formal), 3 code |
| `shape` | `rectangle`, `diamond`, `ellipse` | step, decision, start/end |
| `image` | local path or URL (`.svg`/`.png`) | draw the node as this picture with `label` as a caption; replaces `shape` |

A node uses `shape` or `image`, not both. To place pictures freely, add a top-level `images` array: `[{"src": "...", "x": 400, "y": 40, "width": 60}]`. See `references/svg-images.md`.

Defaults: `direction` TB, `roughness` 1, `font` 1. For formal output set `roughness` 0 and `font` 2.

## Rules

- Shapes carry meaning: `ellipse` for start/end, `diamond` for a decision (its out-edges should have labels like yes/no), `rectangle` for every other step.
- Give each node a unique `id`. Edges reference ids, not labels.
- Keep labels short; long labels widen nodes and stretch the layout.
- Cycles (loops back) are allowed; a back-edge between two adjacent nodes may overlap the forward edge, so pull it apart in the editor if it matters.

## Anti-patterns

- Do not hand-write `.excalidraw` JSON or any x/y coordinate. Always go through `build.py`. Hand-placed elements overlap and arrow bindings break.
- Do not invent shapes or fields beyond the table above.
- Do not skip the PNG step when the user wants an image; report both paths.

## Reference

`references/excalidraw-format.md` documents the `.excalidraw` element schema. Read it only to debug a build or extend the layout, not for normal use.

`references/svg-images.md` covers using SVG/PNG pictures as nodes or free-placed images, and where to get tech-logo SVGs (Devicon, Simple Icons).
