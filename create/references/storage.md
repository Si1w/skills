# CREATE storage and caches

Recorded locations and quotas below are local guidance. Check the account's current quota before large transfers.

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
