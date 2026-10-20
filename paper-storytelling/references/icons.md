# Diagram Icons for Method Figures

`assets/icons/` holds hand-authored SVG icons that recur in method overviews and pipeline figures at CVPR, NeurIPS, ICLR, ICML, ACL, and EMNLP. Each file is named after what it draws, not after a single interpretation, so the same glyph can be reused wherever the visual convention fits. Browse [gallery.png](../assets/icons/gallery.png) for a contact sheet.

## Usage

Every icon is a 64 x 64 `viewBox` with a 2 px stroke and no external dependencies, so it scales cleanly in Inkscape, Illustrator, draw.io, PowerPoint, Keynote, Figma, or TikZ (`\includesvg` or after converting to PDF). Fills follow the palette in `scripts/figure_examples.py`: blue for frozen or encoder parts, amber for trainable parts, purple for decoder or probability outputs, green and red for positive and negative signals, grey for neutral containers.

Keep the convention consistent within a paper: pick one frozen marker (snowflake or padlock) and one trainable marker (flame or open padlock), state them once in a legend, and reuse them in every figure. Recolour by editing the `fill` and `stroke` attributes rather than rasterising. Operators and arrows are plain ink so they inherit the surrounding line weight.

## Index

### Parameter status

| File | Conventional meaning |
| --- | --- |
| `snowflake.svg` | Frozen parameters; the module is not updated during training. |
| `flame.svg` | Trainable parameters; the module is updated during training. |
| `padlock.svg` | Locked or frozen component; alternative to the snowflake. |
| `padlock-open.svg` | Unlocked or tunable component; alternative to the flame. |

### Operators

| File | Conventional meaning |
| --- | --- |
| `circle-plus.svg` | Element-wise addition; residual connection. |
| `circle-minus.svg` | Element-wise subtraction; difference or residual error. |
| `circle-times.svg` | Matrix multiplication; attention score product. |
| `circle-dot.svg` | Element-wise (Hadamard) product; gating. |
| `circle-c.svg` | Concatenation along the feature dimension. |
| `stop-gradient.svg` | Stop-gradient; forward pass only, no backpropagation through this edge. |
| `softmax-bars.svg` | Probability distribution; softmax output or logits. |
| `dice.svg` | Sampling; stochastic decoding or random draw. |
| `loop-arrows.svg` | Iterative loop; self-refinement, EM, or repeated rounds. |

### Model blocks

| File | Conventional meaning |
| --- | --- |
| `neural-network.svg` | Generic neural network or MLP head. |
| `stacked-layers.svg` | Stack of identical layers; N x block. |
| `transformer-block.svg` | Transformer layer: attention (blue), add and norm (grey), feed-forward (purple). |
| `encoder-trapezoid.svg` | Encoder; compresses input into a latent representation. |
| `decoder-trapezoid.svg` | Decoder; expands a latent representation into output. |
| `feature-map-stack.svg` | Convolutional feature maps; channel stack. |
| `tensor-cube.svg` | Tensor or 3D volume; latent grid. |
| `token-sequence.svg` | Token or patch embeddings; sequence input. |
| `masked-tokens.svg` | Masked tokens; masked language or image modelling. |
| `lora-adapter.svg` | Low-rank adapter (LoRA); parameter-efficient fine-tuning branch. |
| `attention-heatmap.svg` | Attention weights or similarity matrix. |
| `matrix-brackets.svg` | Weight matrix; learned parameters. |
| `noise-grid.svg` | Gaussian noise; diffusion forward process or noisy latent. |
| `robot-head.svg` | Language model or agent; LLM policy. |
| `chip.svg` | Model, processor, or hardware accelerator. |
| `server-rack.svg` | Compute cluster, GPU server, or deployment. |

### Data and inputs

| File | Conventional meaning |
| --- | --- |
| `database-cylinder.svg` | Dataset, corpus, memory bank, or knowledge store. |
| `image-frame.svg` | Image input or visual modality. |
| `film-strip.svg` | Video input or frame sequence. |
| `audio-waveform.svg` | Audio or speech input. |
| `text-document.svg` | Text document, passage, or report. |
| `speech-bubble.svg` | Prompt, instruction, or dialogue turn. |
| `code-brackets.svg` | Source code or program output. |
| `knowledge-graph.svg` | Knowledge graph, structured relations, or node set. |
| `user-person.svg` | Human user, annotator, or evaluator. |
| `globe.svg` | Web, environment, or external world. |
| `magnifier.svg` | Retrieval, search, or inspection. |
| `funnel.svg` | Filtering, data selection, or deduplication. |
| `eye.svg` | Observation, perception, or visual grounding. |

### Evaluation and signals

| File | Conventional meaning |
| --- | --- |
| `check-mark.svg` | Correct answer, positive pair, or accepted sample. |
| `cross-mark.svg` | Incorrect answer, negative pair, or rejected sample. |
| `thumbs-up.svg` | Preferred response; human feedback positive. |
| `thumbs-down.svg` | Dispreferred response; human feedback negative. |
| `trophy.svg` | Reward, win rate, or best result. |
| `star.svg` | Highlighted or best-performing item. |
| `loss-box.svg` | Loss or objective term. |
| `warning-triangle.svg` | Failure case, hallucination, or caution. |
| `question-mark.svg` | Unknown, query, or open question. |
| `lightbulb.svg` | Insight, reasoning step, or idea. |
| `clock.svg` | Time step, latency, or schedule. |
| `shield.svg` | Safety, robustness, or defense. |
| `scissors.svg` | Pruning, truncation, or cutting a connection. |
| `pencil.svg` | Editing, annotation, or rewriting. |

### Arrows and annotation

| File | Conventional meaning |
| --- | --- |
| `arrow-solid.svg` | Forward pass or data flow. |
| `arrow-dashed.svg` | Optional path, conceptual link, or inference-only route. |
| `arrow-backprop.svg` | Backward pass or gradient flow (red dashed, pointing back). |
| `arrow-double.svg` | Bidirectional interaction, alignment, or contrastive pairing. |
| `arrow-curved.svg` | Skip connection, feedback, or long-range link. |
| `curly-brace.svg` | Groups several elements under one label. |
