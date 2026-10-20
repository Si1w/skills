# Figure Narrative and Python References

Use the comparison the reader needs to make to choose the plot and panel order. Give each panel a clear job; group panels that jointly support a claim. For a teaser, connect the central conceptual explanation to the evidence without implying an untested mechanism is established.

Keep condition colors consistent across figures. Use spacing to reinforce the intended comparison and visual weight to emphasize the relevant evidence. Choose sequential color for ordered magnitude and diverging color for a meaningful midpoint. Preserve readable labels and vector geometry where possible.

## Runnable examples

[figure_examples.py](../scripts/figure_examples.py) recreates selected visual structures from Sophie Wang's paper-writing article using Matplotlib. These are teaching adaptations, not pixel-exact copies or reproductions of the paper's experiments. Every numerical example uses synthetic data and says so in the image. Error bars in the overview are illustrative magnitudes, not estimated confidence intervals. DejaVu fonts substitute for the original fonts; colors are an approximate palette.

From the repository root, run with `uv` (dependencies are declared in the script):

```bash
uv run paper-storytelling/scripts/figure_examples.py --output /tmp/paper-figures
uv run paper-storytelling/scripts/figure_examples.py --figure hierarchy --output /tmp/paper-hierarchy
```

Alternatively, use Python 3.10+ with NumPy and Matplotlib installed. The script writes PNG and SVG files to the supplied directory, replacing same-named example outputs. `--figure all` also writes `gallery.png`. SVG keeps text editable and requires the viewer to have the selected fonts.

| Selection | Reference in the article | What to adapt |
| --- | --- | --- |
| `overview` | Final Figure 2 | One large comparison beside four supporting panels; shared condition colors, outlined bars, dotted background, direct values. |
| `spacing` | Rows and columns | The same 3-by-4 grid grouped through horizontal versus vertical gaps. |
| `hierarchy` | Samples and fit | Identical samples, fit, and axis limits with different marker and line weights. Neither view changes the evidence. |
| `colormaps` | Sequential and diverging | Extends the original gradient strips into magnitude and signed-deviation heatmaps, with explicit scales and a zero-centered diverging normalization. |
| `teaser` | Final teaser | A simplified branch diagram, behavior and data-source links, and a result strip. Dashed links are conceptual, not causal estimates. |

Browse the bundled [gallery](../assets/examples/gallery.png), then inspect the matching function when adapting a design. Each example has a PNG preview and an SVG in `assets/examples/`.

## Adapting to research data

Replace the synthetic arrays and generic labels with the project's measured data and definitions. Compute uncertainty from the actual sampling procedure and describe it in the caption; do not carry over the demonstration error bars. Preserve inconvenient observations and report selection criteria for any omitted results.

For method overviews and pipeline diagrams, reuse the icons listed in [icons.md](icons.md) (frozen and trainable markers, operators, module blocks, data sources, arrows) so that notation stays consistent across figures.

Check the figure at its intended publication size. Confirm units, axis limits, labels, uncertainty, and text agree with the analysis. Use direct labels, marker shapes, or patterns where color alone would make conditions difficult to distinguish. Palette and typography should follow the paper's existing design when there is one.
