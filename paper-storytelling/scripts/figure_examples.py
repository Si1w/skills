# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib>=3.8,<4", "numpy>=1.26,<3"]
# ///
"""Recreate visual structures from Sophie Wang's paper-writing article.

All numerical data are synthetic. These examples demonstrate design, not
the paper's experimental results. See references/figures.md for provenance.
"""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import FancyArrowPatch, Patch, Rectangle
import numpy as np


# Approximate categorical colors, shared across the overview and teaser.
FILL = ["#a3a3a3", "#fbbf24", "#60a5fa", "#f87171", "#a78bfa"]
EDGE = ["#525252", "#b45309", "#2563eb", "#dc2626", "#7c3aed"]


def style_axes(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(length=3, color="#525252")
    ax.set_axisbelow(True)


def dot_grid(ax, xmax):
    x, y = np.meshgrid(np.arange(-0.35, xmax, 0.28), np.arange(0.1, 1.01, 0.1))
    ax.scatter(x, y, s=2, color="#d4d4d4", zorder=0, edgecolors="none")


def finish(fig, title, note="Synthetic data; design reference only."):
    fig.suptitle(title, x=0.055, y=0.98, ha="left", fontsize=17, weight="bold")
    fig.text(0.055, 0.025, note, fontsize=9, color="#525252")
    return fig


def overview():
    """Large primary result and four small supporting comparisons."""
    fig = plt.figure(figsize=(13.6, 5.4))
    grid = fig.add_gridspec(2, 4, width_ratios=[1.4, 1.4, 1, 1],
                           left=0.07, right=0.98, bottom=0.25, top=0.80,
                           wspace=0.65, hspace=0.6)
    axes = [fig.add_subplot(grid[:, :2])]
    axes += [fig.add_subplot(grid[row, col]) for row in range(2) for col in (2, 3)]
    positions = np.array([0, 1, 2, 3.5, 4.5, 5.5])
    values = np.array([[.38, .73, .71, .65, .84, .85],
                       [.43, .81, .66, .78, .92, .93],
                       [.29, .55, .60, .40, .69, .70],
                       [.12, .23, .36, .14, .30, .32],
                       [.47, .68, .66, .79, .76, .82]])
    # These magnitudes are invented, not confidence intervals or standard errors.
    errors = np.array([.025, .02, .018, .022, .015, .017])
    for index, (ax, row) in enumerate(zip(axes, values)):
        dot_grid(ax, 6.0)
        ax.bar(positions, row, width=.58, color=FILL[:3] * 2,
               edgecolor=EDGE[:3] * 2, linewidth=1.5, yerr=errors,
               error_kw={"elinewidth":1, "capsize":3}, zorder=2)
        ax.set(xlim=(-.6, 6.1), ylim=(0, 1.05))
        ax.set_yticks([0, .5, 1] if index else np.arange(0, 1.01, .2))
        style_axes(ax)
        if index == 0:
            ax.set_ylabel("Primary task accuracy")
            ax.set_xticks(positions, ["Base", "+ cue", "RL"] * 2)
            for x, value, color in zip(positions, row, EDGE[:3] * 2):
                ax.text(x, value + .05, f"{value:.2f}", ha="center", color=color, fontsize=14)
            for center, label in [(1, "Model A"), (4.5, "Model B")]:
                ax.text(center, 1.11, label, ha="center", fontsize=12,
                        bbox={"boxstyle":"square,pad=0.2", "fc":"white", "ec":"#737373"})
        else:
            ax.set_title(f"Task {index + 1}", loc="left", fontsize=11)
            ax.set_xticks([1, 4.5], ["A", "B"])
    legend = [Patch(facecolor=FILL[i], edgecolor=EDGE[i], label=label)
              for i, label in enumerate(["Base", "Base + cue", "After RL"])]
    fig.legend(handles=legend, loc="lower center", bbox_to_anchor=(.5, .09), ncol=3, frameon=False)
    return finish(fig, "One main comparison, supporting evidence alongside",
                  "Synthetic data; error bars are illustrative magnitudes, not estimated uncertainty.")


def spacing():
    """Reproduce the article's 3-by-4 empty-panel spacing demonstration."""
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.2))
    fig.subplots_adjust(left=.04, right=.96, bottom=.12, top=.78, wspace=.15)
    for ax, gap_x, gap_y, title in zip(axes, [.09, .40], [.40, .09],
                                       ["Read across rows", "Read down columns"]):
        for row in range(3):
            for col in range(4):
                ax.add_patch(Rectangle((col * (1 + gap_x), row * (1 + gap_y)),
                                       1, 1, facecolor="white", edgecolor="#262626", linewidth=1.6))
        # Common limits keep panel sizes identical; only spacing changes.
        ax.set(xlim=(-.12, 5.32), ylim=(-.12, 3.92), aspect="equal")
        ax.set_title(title, fontsize=13, pad=14)
        ax.axis("off")
    return finish(fig, "Spacing changes the grouping", "Schematic panels; only the gaps change.")


def hierarchy():
    """Hold the data and fit constant while changing their visual emphasis."""
    rng = np.random.default_rng(42)
    x = np.sort(rng.uniform(.15, 9.85, 85))
    y = 1.2 + .68 * x + 1.3 * np.sin((x - 1.3) / 2.3) + rng.normal(0, .45, len(x))
    line_x = np.linspace(0, 10, 100)
    line_y = np.polyval(np.polyfit(x, y, 1), line_x)
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.2), sharex=True, sharey=True)
    fig.subplots_adjust(left=.07, right=.97, bottom=.17, top=.78, wspace=.18)
    for ax, size, alpha, width, title in zip(axes, [58, 18], [1, .35], [1.5, 3.8],
                                           ["Samples emphasized", "Linear fit emphasized"]):
        ax.scatter(x, y, s=size, color=EDGE[2], alpha=alpha, edgecolors="white", linewidths=.5, zorder=3)
        ax.plot(line_x, line_y, color=EDGE[2], linewidth=width, alpha=.45 if width < 2 else 1)
        ax.set(title=title, xlim=(0, 10), ylim=(0, 10), xlabel="Predictor")
        style_axes(ax)
    axes[0].set_ylabel("Response")
    return finish(fig, "Visual weight changes what readers notice", "Synthetic data; both panels show identical samples, fitted line, and limits.")


def colormaps():
    """Show magnitude and signed deviation with appropriate normalization."""
    x, y = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 30))
    magnitude = np.exp(-((x - .5) ** 2 + (y + .2) ** 2))
    deviation = magnitude - np.exp(-((x + .5) ** 2 + (y - .2) ** 2))
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.2))
    fig.subplots_adjust(left=.07, right=.94, bottom=.18, top=.78, wspace=.38)
    for ax, data, cmap, norm, title, label in [
        (axes[0], magnitude, "viridis", plt.Normalize(0, 1), "Sequential: magnitude", "Magnitude"),
        (axes[1], deviation, "RdBu_r", TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1),
         "Diverging: change around zero", "Change from baseline")]:
        mesh = ax.pcolormesh(x, y, data, cmap=cmap, norm=norm, shading="auto", rasterized=False)
        ax.set(title=title, xlabel="Position x", ylabel="Position y", aspect="equal")
        colorbar = fig.colorbar(mesh, ax=ax, fraction=.046, pad=.04, label=label)
        colorbar.solids.set_rasterized(False)
    return finish(fig, "Match color semantics to the quantity")


def teaser():
    """Simplified adaptation of the article's concept-plus-evidence teaser."""
    fig = plt.figure(figsize=(13.6, 7.4))
    grid = fig.add_gridspec(2, 1, height_ratios=[2, 1], left=.07, right=.97,
                           top=.86, bottom=.16, hspace=.35)
    ax = fig.add_subplot(grid[0])
    ax.set(xlim=(0, 12), ylim=(0, 4))
    ax.axis("off")
    for x, label in [(2.4, "Opening cue"), (5.8, "Behavior"), (9.7, "Data association")]:
        ax.text(x, 3.85, label, fontsize=12, weight="bold")
    ax.text(.05, 2, "Prompt", fontsize=13, va="center",
            bbox={"boxstyle":"round,pad=.4", "fc":"#f5f5f5", "ec":EDGE[0]})
    ax.plot([1.1, 1.7], [2, 2], color=EDGE[0], linewidth=1.6)
    ax.plot([1.7, 1.7], [.85, 3.05], color=EDGE[0], linewidth=1.6)
    for y, cue, behavior, source, color_index in [
        (3.05, "Answer", "Concise response", "Short answers", 4),
        (1.95, "Okay", "Reasoning trace", "Worked examples", 1),
        (.85, "New cue", "Reasoning after edit", "Edited examples", 3)]:
        color = EDGE[color_index]
        ax.add_patch(FancyArrowPatch((1.7, y), (2.5, y),
                     arrowstyle="->", mutation_scale=12, lw=1.6, color=color))
        ax.text(3.2, y, cue, ha="center", va="center", fontfamily="DejaVu Sans Mono", fontsize=12,
                bbox={"boxstyle":"round,pad=.4", "fc":FILL[color_index], "ec":color, "alpha":.8})
        ax.annotate("", xy=(5.65, y), xytext=(3.95, y),
                    arrowprops={"arrowstyle":"->", "color":color, "lw":2})
        ax.text(5.8, y, behavior, va="center", fontsize=11, color=color)
        ax.plot([8.2, 9.5], [y, y], linestyle=(0, (3, 3)), color=color, linewidth=1.5)
        ax.text(9.7, y, source, va="center", fontsize=11,
                bbox={"boxstyle":"square,pad=.35", "fc":"white", "ec":color})
    ax.text(4.4, 2.25, "RL increases branch use", color=EDGE[2], ha="center", fontsize=9)
    ax.text(2.5, .15, "Data edits can alter cue associations", color=EDGE[3], fontsize=10)
    result_ax = fig.add_subplot(grid[1])
    values = [.39, .17, .72, .24, .70, .74]
    colors = [0, 4, 1, 3, 2, 3]
    labels = ["Base", "Base + Answer", "Base + Okay", "Base + new cue", "After RL", "Edit + new cue"]
    dot_grid(result_ax, 5.5)
    result_ax.bar(range(6), values, width=.55, color=[FILL[i] for i in colors],
                  edgecolor=[EDGE[i] for i in colors], linewidth=1.6, zorder=2)
    for i, value in enumerate(values):
        result_ax.text(i, value + .04, f"{value:.2f}", ha="center", color=EDGE[colors[i]])
    result_ax.set(xticks=range(6), xticklabels=labels, ylim=(0, 1), xlim=(-.5, 5.5), ylabel="Accuracy")
    style_axes(result_ax)
    return finish(fig, "Connect a conceptual explanation to observable comparisons",
                  "Synthetic data and simplified concept diagram; dashed links indicate associations, not causal estimates.")


EXAMPLES = {"overview": overview, "spacing": spacing, "hierarchy": hierarchy,
            "colormaps": colormaps, "teaser": teaser}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--figure", choices=["all", *EXAMPLES], default="all")
    parser.add_argument("--output", required=True, type=Path, help="Directory for PNG and SVG example outputs")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":10,
                         "svg.fonttype":"none", "svg.hashsalt":"paper-storytelling",
                         "axes.spines.top":False, "axes.spines.right":False,
                         "figure.facecolor":"white", "savefig.facecolor":"white"})
    names = list(EXAMPLES) if args.figure == "all" else [args.figure]
    for name in names:
        fig = EXAMPLES[name]()
        for extension in ("png", "svg"):
            path = args.output / f"{name}.{extension}"
            metadata = {"Description":"Synthetic teaching example; adapted from Sophie Wang's paper-writing article"}
            if extension == "svg":
                metadata["Date"] = None
            fig.savefig(path, dpi=170, metadata=metadata)
            print(path)
        plt.close(fig)
    if args.figure == "all":
        fig, axes = plt.subplots(3, 2, figsize=(16, 14), layout="constrained")
        for ax, name in zip(axes.flat, names):
            ax.imshow(plt.imread(args.output / f"{name}.png"))
            ax.axis("off")
        axes.flat[-1].axis("off")
        axes.flat[-1].text(.08, .65, "Python figure references", fontsize=21, weight="bold")
        axes.flat[-1].text(.08, .43, "Adapted from Sophie Wang's paper-writing article.\nSynthetic data, not reproduced experimental results.\nEditable SVG and PNG accompany each example.", fontsize=13, linespacing=1.8)
        fig.savefig(args.output / "gallery.png", dpi=130)
        plt.close(fig)
        print(args.output / "gallery.png")


if __name__ == "__main__":
    main()
