# Research-template implementation

Read this when implementing a study in a research-template project. Use the project's `AGENTS.md` and `.agents/rules/code-style.md` when present. The mapping below is a default for that template, not a requirement to reorganize another project. Map each ADR to actual project paths before implementing it.

| Decision | Code location | Rule |
|----------|---------------|------|
| Dataset, models, controlled variables | `configs/{benchmark}.yaml` | Single source of truth. Seed, temperature, max_tokens, model IDs live here; nothing is hard-coded in `src/` or `eval/`. Baselines are entries in the same `models:` list. |
| Sampling | `eval/{benchmark}/main.py --step preprocess` | Selection and filtering are a script step, not a manual process. Log exclusion counts per step. |
| Protocol | `eval/{benchmark}/main.py --step inference` | One run = one (model, seed). Persist every per-instance raw output under `data/{benchmark}/results/{model_name}/`; never store only aggregates. Resumable. `--num_samples` for the pilot. |
| Metrics | `eval/{benchmark}/main.py --step score` | Pure functions from raw outputs to metric values, tested on hand-checked instances. |
| Analysis plan | `eval/{benchmark}/main.py --step analyze` | Reads raw results only. Implements exactly the tests, effect sizes, and CIs in the ADR. Writes `eval/tables-and-figures/rq{n}-{type}.csv/.png`. Committed before the full run. |
| Compute budget | `scripts/{benchmark}_vllm.sh`, `scripts/{benchmark}_api.sh` | One script per model type, `MODELS=()` array, template from code-style. Use the `create` skill for partitions only when running on KCL CREATE. |
| Replication package | `README.md`, `LICENSE`, `docs/adr/` | Commands to reproduce every table and figure from raw results. |

Coding rules derived from the standards' antipatterns:

- Raw before aggregate: persist all per-instance results, analyze offline (benchmarking).
- Preprocessing that changes distributions applies to training data only (data-science).
- No peeking: the analyze step is written before the main run; a change afterwards is a new ADR superseding the analysis-plan ADR.
- Baselines run through the same harness, data, metrics, and repetitions as the proposed method.
- Every run writes metadata: config hash, git commit, seed, hardware, library versions, wall time, failures. Failed runs are reported, not silently retried.

Run an affordable pilot before a full job and compare the implemented behavior with the ADRs. An authorized implementation request includes correcting pilot failures within the agreed design; ask only when a correction changes a material design decision or resource budget.
