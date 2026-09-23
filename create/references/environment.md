# CREATE Python environment

Use the project's `pyproject.toml`, lockfile, and documented runtime first. The versions below preserve a recorded project setup, not a cluster-wide requirement or a recommendation to upgrade or downgrade other projects. Check Python, CUDA, torch, and wheel compatibility together when changing dependencies.

## Project environment

- The recorded research project uses Python 3.12 (pinned via `requires-python = "==3.12.*"` in `pyproject.toml`).
- For this uv-managed setup, run `uv sync` on the login node, then `uv run --frozen --no-sync python ...` inside jobs. It does not need venv activation or module loading; follow the project's runtime requirements if it uses a different setup.
- For the recorded CUDA 12.8 / torch 2.8 environment, configure the cu128 index and matching flash-attn wheel in `pyproject.toml`:

```toml
[tool.uv.sources]
torch = { index = "pytorch-cu128" }

[[tool.uv.index]]
name = "pytorch-cu128"
url = "https://download.pytorch.org/whl/cu128"
explicit = true
```

- Software modules (`module avail`, `ml spider <pkg>`) are available for projects that need them.

## Common Libraries with versions

| Library | Version | Note |
|---------|---------|------|
| python | 3.12 | Required by the flash-attn wheel (cp312) |
| torch | 2.8.0 | https://download.pytorch.org/whl/cu128 |
| transformers | 4.57.6 | |
| datasets | 4.8.4 | |
| trl | 0.29.1 | |
| deepspeed | 0.18.9 | |
| flash-attn | 2.8.3 | https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.3/flash_attn-2.8.3+cu12torch2.8cxx11abiFALSE-cp312-cp312-linux_x86_64.whl |
| liger-kernel | 0.8.2 | |
| vllm | 0.11.0 | |
