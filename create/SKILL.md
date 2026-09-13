---
name: create
description: Use when writing sbatch/srun scripts, setting up Python environments, transferring data, or managing Slurm jobs on the KCL CREATE HPC cluster.
---

## Login

The connection profile has been stored in the `~/.ssh/config` file. Use the following command to connect to the CREATE cluster:

```bash
ssh create
```

Notes:
- MFA via the e-Research portal is required on first login, after an IP change, and weekly for static IPs. If `ssh create` hangs or is refused, ask user to complete MFA in the portal first.

## Device

GPU models by partition (from `sinfo`, constraints usable via `--constraint`):

| Partition | GPU models |
|-----------|------------|
| gpu | a100, a100_40g, h200, b200, l40s |
| interruptible_gpu | h100, a100_80g, a100_40g, a40, a30, l40s, rtx6000, rtx3070, rtx2080, titan_v, titan_rtx, titan_xp |
| tier1_gpu / tier1_charity_gpu | h200, b200 |
| tier2_gpu / tier2_charity_gpu | a100_40g, l40s |
| tier3_gpu / tier3_charity_gpu | a30 |
| nmes_gpu | a100_40g |

Note:
- `a100` is the same card as `a100_40g`; use `#SBATCH -C a100|a100_40g` to request either.
- a100_80g and h100 exist only in `interruptible_gpu`; jobs there are preemptible.
- Nodes carry 1–8 GPUs; check `sinfo -p gpu,interruptible_gpu -o "%P %n %G %f"` for current counts.
- `tier*_gpu` partitions are paid and need `--account <project_name>`.

CPU partitions:

| Partition | CPU features |
|-----------|--------------|
| cpu / paid_cpu | x86_64_v4, zen2, zen3 |
| interruptible_cpu | zen2, zen3, zen4, cascadelake, icelake, sapphirerapids |

## Jobs

Limits (from scheduler policy):

| Item | Value |
|------|-------|
| Default resources | 1 core, 1GB memory |
| Default runtime | 24h batch, 4h interactive |
| Max runtime | 48h on `cpu` / `gpu`; 4h interactive |
| Max GPUs per job | 8 |
| Max concurrent per user | 700 cores, 8 A100 |
| long_cpu / long_gpu | 7 / 10 days, access by request to support@er.kcl.ac.uk |

Batch template (project-style; run from the project root, no venv activation or `module load` needed):

```bash
#!/bin/bash
#SBATCH -J train
#SBATCH -p gpu
#SBATCH -t 24:00:00
#SBATCH -o %x_%j.out
#SBATCH --mail-user=<k-number>@kcl.ac.uk
#SBATCH --mail-type=FAIL,END
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 16
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH -C a100|a100_40g
set -euo pipefail

uv run --frozen --no-sync python -m src.train --step train
```

Interactive session (max 4h; use `interruptible_gpu` for quick tests on any GPU type):

```bash
srun -p interruptible_gpu --gres=gpu:1 --constraint=a40 --time=60 --pty /bin/bash -l
```

Monitoring:

```bash
squeue -u $USER        # my jobs
sacct -j <jobid>       # resource usage
seff <jobid>           # efficiency report
scancel <jobid>        # cancel
```

Useful variables inside a job: `$SLURM_JOB_ID`, `$SLURM_ARRAY_TASK_ID`, `$SLURM_NTASKS`. Use `--array=1-N` for task arrays and `--depend=afterok:<jobid>` for dependencies.

## Cache

The cache location is set to `/scratch/users/$USER/.cache` by default.

```bash
export XDG_CACHE_HOME="/scratch/users/$USER/.cache"
export HPC_CACHE="$XDG_CACHE_HOME"

export HF_HOME="$HPC_CACHE/huggingface"
export HF_HUB_CACHE="$HF_HOME/hub"
export HF_DATASETS_CACHE="$HF_HOME/datasets"
export VLLM_CACHE_ROOT="$HPC_CACHE/vllm"
export TORCH_HOME="$HPC_CACHE/torch"
export TRITON_CACHE_DIR="$HPC_CACHE/triton"
export CUDA_CACHE_PATH="$HPC_CACHE/nv"
export SINGULARITY_CACHEDIR="$HPC_CACHE/singularity"
export APPTAINER_CACHEDIR="$SINGULARITY_CACHEDIR"
export UV_CACHE_DIR="$HPC_CACHE/uv"
```

## Storage

| Path | Quota | Usage |
|------|-------|-------|
| /users/$USER | 50GiB | Code, configs, small files |
| /scratch/users/$USER | 200GiB | Job I/O, venvs, caches, checkpoints |
| /scratch/prj/<project> | 1TiB default, shared | Project data (need application) |
| /scratch/datasets/<id> | read-only | Shared datasets (need application) |

Notes:
- `/scratch` is not backed up.
- Check quota with `ceph_quota` or `rds_quota`. Exceeding the home quota can block login, so keep venvs and caches on `/scratch`.
- Transfer files with `scp`/`rsync` through the `create` host, e.g. `rsync -avP ./data create:/scratch/users/<k-number>/data`. Transfers over ~500GB should use `tmux`/`screen` on the login node or the data transfer node `erc-hpc-dm1`.
- RDS is not mounted on compute nodes; stage data to `/scratch` before submitting jobs.
- use `cd /scratch/users/$USER` or `cd /users/$USER` to access different storage locations.

## Environment

- Python 3.12 (pinned via `requires-python = "==3.12.*"` in `pyproject.toml`).
- `uv` manages the environment on local, login, and compute nodes; `uv sync` on the login node, then `uv run --frozen --no-sync python ...` inside jobs. Do not activate venvs or load modules in job scripts.
- Pin torch to the cu128 index and install flash-attn from the prebuilt wheel in `pyproject.toml`:

```toml
[tool.uv.sources]
torch = { index = "pytorch-cu128" }

[[tool.uv.index]]
name = "pytorch-cu128"
url = "https://download.pytorch.org/whl/cu128"
explicit = true
```

- Software modules (`module avail`, `ml spider <pkg>`) exist but are not used by project code.

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
| vllm | 0.11.0 | Last release pinned to torch 2.8.0; requires transformers>=4.55.2, pulls xformers 0.0.32.post1 |
