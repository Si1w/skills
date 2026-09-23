---
name: create
description: Run and troubleshoot jobs on the KCL CREATE HPC cluster, including Slurm resources, storage, and Python environments.
---

# CREATE HPC

Connect with `ssh create` using the existing SSH profile. If login fails, inspect the error before assuming MFA is the cause. Portal MFA may be needed on first login, after an IP change, or when the session expires; the user must complete it.

Read the reference for the requested operation:

- [Jobs and partitions](references/jobs.md): choosing resources, submitting or monitoring Slurm jobs, interactive sessions, and cancellation.
- [Storage and caches](references/storage.md): quotas, scratch paths, data transfers, and cache configuration.
- [Python environment](references/environment.md): setting up or diagnosing the project's uv, CUDA, and library dependencies.

Recorded hardware, limits, and package versions are snapshots. Use live scheduler output and the project's lockfile for current decisions. Keep training and other substantial computation on allocated compute nodes. `/scratch` is not backed up, and RDS data must be staged there before compute jobs use it.

For job preparation, produce a runnable script with the requested resources and entrypoint. When execution is requested, submit within the agreed budget, report the job ID and observed state, and diagnose submission failures. A queued job is not a completed experiment; monitor to the endpoint the user requested.
