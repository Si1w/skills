# Isambard-AI Phase 2 system reference

Verified on the login node on 2026-11-03 against the official documentation. Recheck live values with the commands shown when behaviour differs. Placeholders: `PROJECT` is the project code, `USER` is the UNIX username, `ALIAS` is the Clifton-generated SSH host (`PROJECT.aip2.isambard`).

## Hardware

| Item | Value | Check |
|------|-------|-------|
| OS | SUSE Linux Enterprise Server 15 SP7 | `cat /etc/os-release` |
| CPU architecture | `aarch64` (NVIDIA Grace). No x86_64 binaries, wheels, or container images run. | `uname -m` |
| Compute node | 4 x GH200 superchip; 288 cores (4 x 72), 460 GB usable CPU memory (115 GB per superchip), 4 x H100 reported as `GH200 120GB` with 97,871 MiB usable | `scontrol show node nid010000` |
| Node features | `ARM,Compute,NVIDIA_GH200,GeneralCompute` (one node type, so `--constraint` is unnecessary) | `sinfo -o "%f %D"` |
| Login node | Grace CPU only, no GPU driver (`nvidia-smi` fails there by design). Each user session is confined to a cgroup of 4 GiB memory and 1 CPU (`/sys/fs/cgroup/user.slice/user-UID.slice`), and long transfers or downloads there get killed: run them in a job. | `cat /sys/fs/cgroup/user.slice/user-$(id -u).slice/memory.max` |
| Interconnect | Slingshot 11, 4 x 200 Gbps NICs per node; NVLink-C2C within a node | [specs](https://docs.isambard.ac.uk/specs/) |
| Scheduler | Slurm 26.05 | `sinfo --version` |

## Slurm

Source: [Slurm guide](https://docs.isambard.ac.uk/user-documentation/guides/slurm/), [advanced guide](https://docs.isambard.ac.uk/user-documentation/guides/slurm-advanced/), [job scheduling](https://docs.isambard.ac.uk/user-documentation/information/job-scheduling/).

- One partition, `workq` (default). There are no CPU-only partitions and no preemptible partitions; every job lands on a GH200 node.
- Request GPUs with `--gpus=N` and always add `--nodes=1` for single-node work. One GPU is one whole superchip and brings `DefCpuPerGPU=72` and `DefMemPerGPU=115000` (MB) automatically, so `-c` and `--mem` are optional and must not exceed 72 cores or 115 GB per GPU requested. `--gres=gpu:N` also works.
- CPU-only work: there is no CPU partition. Request `--gpus=1` (or omit GPUs and set `-c`/`--mem` explicitly; the job is still billed on a GH200 node). Prefer folding CPU-only steps into GPU jobs.
- Walltime: `MaxWall` is 24 h (`workq_qos`); partition default is 4 h. Always set `--time`. Chain longer work with `sbatch --parsable` and `--dependency=afterok:JOBID`.
- Limits (`workq_qos`): 256 running jobs and 512 submitted jobs per user; 32 GPUs allocated per project (`32gpu_qos`); 1000 tasks per array. Jobs over a limit are rejected at submission (`DenyOnLimit`), not queued.
- Account: `brics.PROJECT`, QOS `normal` on the association; the partition QOS applies the limits. Check with `sacctmgr show assoc user=$(whoami)` and `sacctmgr show qos workq_qos`.
- Interactive: `--reservation=interactive` with no `--partition`; default 30 min, max 8 h, max 4 nodes, 1 running and 1 queued job per user, billed at 1.5x. Example: `srun --nodes=1 --gpus=1 --time=00:15:00 --reservation=interactive --pty /bin/bash --login`.
- `--exclusive` bills all four superchips; avoid it.
- Multi-node: `--nodes=N --gpus-per-node=4 --ntasks-per-node=4 --cpus-per-task=72`; load `brics/nccl` and `brics/aws-ofi-nccl` modules for NCCL over Slingshot.
- `%x_%j.out`, `--mail-user`, `--mail-type`, job arrays, and `SLURM_RESTART_COUNT` behave as on any Slurm.

Minimal batch script:

```bash
#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --output=%x_%j.out
#SBATCH --nodes=1
#SBATCH --gpus=1
#SBATCH --time=04:00:00
hostname
nvidia-smi --list-gpus
```

## Storage

Source: [system storage](https://docs.isambard.ac.uk/user-documentation/information/system-storage/). Nothing is backed up; data is removed 30 days after project end.

| Path | Variable | Quota | Use |
|------|----------|-------|-----|
| `/home/PROJECT/USER.PROJECT` | `$HOME` | 100 GiB (NFS) | Config, scripts, job output. No caches or models. |
| `/scratch/PROJECT/USER.PROJECT` | `$SCRATCH`, `$SCRATCHDIR` | 5 TiB, 1 M files (Lustre `/lus/lfs1aip2`) | Repo checkout, uv cache, HF cache, SIF images, checkpoints. Personal, not shared with project members. |
| `/projects/PROJECT` | `$PROJECTDIR` | 200 TiB, 50 M files (Lustre) | Shared datasets, images, environments for the project. Only `public/` exists by default. |
| `/projects/public/PROJECT` | `$PROJECTDIR_PUBLIC` | counted in project quota | Readable by all users, writable by the project. Group-writable with setgid. |
| `/local/user/UID` | `$LOCALDIR`, `$APPTAINER_CACHEDIR` default | 512 GiB SSD on login; 48 GiB tmpfs on compute | Ephemeral: cleared at session or job end. Use for container tmp dirs. |

Check usage with `quota -s` (home, local) and `lfs quota -h -u $(whoami) /lus/lfs1aip2` (scratch). Shell startup files do not exist by default; create `~/.bashrc` for cache variables.

## Software

- Modules: Cray PE (`PrgEnv-gnu`, `cray-python/3.11.7`, `cuda/12.6`, `cudatoolkit`, `gcc-native/14.2`) plus `brics/*` (nccl, aws-ofi-nccl, openmpi, tmux, nano, emacs, apptainer-multi-node). System `python3` is 3.6; do not use it.
- Python: install uv with the official script into `~/.local/bin` (login node has outbound HTTPS). Set `UV_CACHE_DIR` and `UV_PYTHON_INSTALL_DIR` under `$SCRATCH` so managed interpreters and wheels stay off the 100 GiB home. Only `linux_aarch64` wheels install; packages shipping x86_64-only wheels need a source build or a replacement. Source builds of CUDA extensions need `module load gcc-native/13.2 cuda/12.6` (the system gcc is 7, which the PyTorch headers reject) and belong in a job.
- Outbound network: HTTPS to PyPI, Hugging Face, GitHub, Docker Hub works from login and compute nodes without a proxy (verified with `srun ... curl` on 2026-11-03). GitHub SSH is not authorized until a key is added. Download models and datasets inside a job, not on the login node.
- Containers: `apptainer` 1.5 on login and compute nodes, rootless (`--fakeroot`, `allow setuid = no`, `user bind control = yes`, `enable fusemount = yes`). Pull with `apptainer build image.sif docker://...` and run with `apptainer exec --nv image.sif ...` inside an allocation. Only `linux/arm64` images run. `podman-hpc` is also available: build or pull on the login node, `podman-hpc migrate NAME` to squashfs on `$SCRATCH`, then run on compute with `--gpu`.
- Agent policy: keep the agent local, submit commands over SSH for review, never run agents on login nodes ([agent guide](https://docs.isambard.ac.uk/user-documentation/guides/using_ai_agents/)).

## File transfer

Source: [file transfer](https://docs.isambard.ac.uk/user-documentation/guides/file_transfer/local/). All transfers go through the Clifton SSH alias and the jump host; there is no separate data transfer node.

```bash
rsync -avz --exclude .git --exclude data local_dir ALIAS:/scratch/PROJECT/USER.PROJECT/
tar c local_dir | ssh ALIAS 'cat > remote.tar'      # many small files
```

Install a current `rsync` with Homebrew on macOS; the bundled one is slow. Transient `Connection timed out during banner exchange` on the jump host is common; retry with `-o ConnectTimeout=40`.

## Porting a CREATE workflow

Differences from KCL CREATE that require script changes:

| CREATE | Isambard-AI |
|--------|-------------|
| x86_64, many GPU types, `-C a100` etc. | aarch64 GH200 only; drop `--constraint` and `--exclude` |
| `-p gpu`, `-p cpu`, `interruptible_*` | `workq` only; CPU jobs still occupy a GPU node |
| `--gres=gpu:N -c 16 --mem=64G` | `--gpus=N --nodes=1`; cores and memory default from the GPU count |
| `singularity` 4.3 on compute only | `apptainer` 1.5 on login and compute |
| `/scratch/prj/...` shared 1 TB | `$SCRATCH` 5 TiB personal, `$PROJECTDIR` 200 TiB shared |
| `/tmp` for container tmp | `$LOCALDIR` (`/local/user/UID`) |
| x86_64 PyTorch cu128 and flash-attn wheels | `manylinux_2_28_aarch64` wheels; flash-attn has no official aarch64 wheel for torch 2.8 (torch 2.9 and 2.10 only) |
| x86_64 SWE-bench images | arm64 images exist for only part of the benchmark: official `swebench/sweb.eval.arm64.<id with _1776_>` on Docker Hub, and best-effort `ghcr.io/epoch-research/swe-bench.eval.arm64.<original id>` from Epoch AI. Check per instance before planning an evaluation on Isambard. |
