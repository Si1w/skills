# CREATE jobs

These tables preserve the locally recorded cluster configuration. They are a starting point, not a live inventory. Inspect `sinfo` and `scontrol show partition <name>` for the requested partition when preparing a submission; check project account access before using paid tiers.

## Partitions

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

Recorded scheduler limits (verify current policy before sizing a job):

| Item | Value |
|------|-------|
| Default resources | 1 core, 1GB memory |
| Default runtime | 24h batch, 4h interactive |
| Max runtime | 48h on `cpu` / `gpu`; 4h interactive |
| Max GPUs per job | 8 |
| Max concurrent per user | 700 cores, 8 A100 |
| long_cpu / long_gpu | 7 / 10 days, access by request to support@er.kcl.ac.uk |

Batch example for a project whose locked uv environment is already synced. Adapt resources and the entrypoint to the project; see [environment.md](environment.md) for setup.

```bash
#!/bin/bash
#SBATCH -J train
#SBATCH -p gpu
#SBATCH -t 24:00:00
#SBATCH -o %x_%j.out
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
