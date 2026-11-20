---
name: isambard
description: Set up and troubleshoot Isambard-AI HPC access through AIRR, including portal onboarding, Clifton SSH certificates, and project SSH connections.
---

# Isambard

The user accesses Isambard-AI through AIRR and is not a University of Bristol student. Use the AIRR onboarding route. Do not assume a Bristol account, the Bristol/GW4 allocation route, or CREATE credentials apply.

Keep personal HPC identifiers, account names, and project aliases out of skill files. Resolve them from the current conversation or local Clifton configuration when needed.

For first access, missing Clifton, or portal problems, read [Access setup](references/access.md). For an existing setup, inspect the relevant SSH profile and certificate before changing anything. Never assume an alias named `isambard` exists or guess the project code.

## How login works

Clifton is not a login command. Version 0.3 has two subcommands: `clifton auth` obtains a signed SSH certificate (currently valid for 12 hours) after browser or QR authentication, and `clifton ssh-config` prints or writes the OpenSSH configuration that pairs each project alias with the jump host, the access host, the identity key, and the certificate. The connection itself is always plain `ssh ALIAS`; OpenSSH reads the Clifton include and presents the certificate. So "log in with Clifton" means: check the certificate, run `clifton auth` only when it is missing or expired, then `ssh ALIAS`. Do not look for a Clifton connect command.

The jump host `ai.login.isambard.ac.uk` intermittently times out at TCP connect or during banner exchange even while the service status page shows no incident. One or two retries with `-o ConnectTimeout=90` normally succeed; a persistent failure is a different problem (see below).

## Connect and renew

1. Locate Clifton with `command -v clifton`. Inspect Isambard entries in `~/.ssh/config` and `~/.ssh/config_clifton`, including relevant `Include` files. Use `ssh -G ALIAS` to resolve the chosen profile. Read configuration and public certificate metadata only, never private key contents.
2. Check the configured certificate with `ssh-keygen -L -f CERTIFICATE_PATH`. If it is missing or expired, run `clifton auth`; for a custom key, use `clifton auth --identity KEY_PATH`. The user completes browser authentication and MFA with the same identity used for onboarding. Clifton supports browser or QR authentication. See the [Clifton documentation](https://github.com/isambard-sc/clifton).
3. For initial configuration or changed project membership, use `clifton ssh-config` to preview, then `clifton ssh-config write` to generate the SSH configuration. Preserve unrelated profiles. Select the actual project alias from its output, asking which project only when the intended choice remains ambiguous.
4. Connect using `ssh ALIAS`. The documented Isambard-AI example is `PROJECT.aip2.isambard`, but generated aliases determine the target. Certificates currently last 12 hours; renew with Clifton when needed. Check unfamiliar host fingerprints against the [official login guide](https://docs.isambard.ac.uk/user-documentation/guides/login/#host-fingerprints). Do not disable host verification.

For a reviewed connection check, use `ssh -o ConnectTimeout=15 ALIAS 'hostname; whoami; pwd'`. Report the selected project, observed result, and any remaining authentication step. Do not claim success from configuration generation alone.

## Diagnose the observed failure

- Missing alias or unexpected destination: inspect `ssh -G ALIAS` and the Clifton include before rewriting configuration.
- Public-key rejection: check certificate validity, identity/certificate pairing, and project membership. Renew only when indicated; do not assume every failure is MFA.
- Portal rejection or missing UNIX username: follow [Access setup](references/access.md).
- Timeout or connection refusal: retry once or twice first, since the jump host is flaky; then inspect the configured endpoint and [service status](https://docs.isambard.ac.uk/service-status/). Do not transplant CREATE VPN instructions. The Bristol VPN note in the login guide concerns BlueCrystal 5.
- If a targeted correction fails, retain the error and investigate that cause instead of repeatedly authenticating or overwriting SSH files. Redact identifiers and authentication URLs when sharing logs.

## Session boundaries

Keep the agent local. Present remote commands for user review before execution and use existing approval when it covers those commands. Do not establish persistent agent connections, run agents on login nodes, or extend access past certificate expiry with background sessions. These constraints follow the [Isambard agent guide](https://docs.isambard.ac.uk/user-documentation/guides/using_ai_agents/).

Keep substantial computation on Slurm compute nodes. Login assistance alone does not request a job submission. Each login session runs in a cgroup of 4 GiB memory and 1 CPU, so large downloads, transfers, and source builds belong in jobs; compute nodes have outbound HTTPS.

## Jobs, storage, and porting

Read [System reference](references/system.md) before writing Slurm scripts, choosing storage paths, installing Python packages, or porting a workflow from CREATE. It records the verified hardware (aarch64 GH200 nodes), the single `workq` partition and its QOS limits, the `--gpus` request convention with per-GPU CPU and memory defaults, storage quotas and variables, container and Python notes, file transfer commands, and a CREATE to Isambard difference table. Confirm live values with the commands listed there rather than copying CREATE partitions or paths.

Documentation checked on 2026-11-03. Recheck official guidance when commands, endpoints, or authentication behavior differ.
