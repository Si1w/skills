---
name: experiment-design
description: Use when asked to design a research experiment or to set up the code for one in a research-template project. Derives the required design decisions from the ACM/SIGSOFT Empirical Standards, resolves them one at a time (Grill), records each as an ADR under docs/adr/, then maps every ADR to the project code layout before implementation.
---

# Experiment Design

Design first, code second. The standards a reviewer will apply later (`references/`) are applied here up front: every Essential attribute of the matched standard must be covered by an accepted ADR, and every ADR must name the code that implements it. Follow the project's own workflow from `AGENTS.md`: Grill until a decision converges, write the ADR, then implement one step at a time.

## Procedure

### Step 1: Pin down the study

Extract from the user's notes, or ask, until each item is one unambiguous sentence:

- **Problem / objective**: what gap, why it matters now.
- **Research questions**: numbered RQ1..n. For confirmatory work add formal hypotheses (two-sided unless justified).
- **Contribution type**: new artifact (tool, model, prompt strategy), empirical finding about existing artifacts, replication, or a mix.
- **Constraints**: compute budget (GPU type, hours), deadline, data that is or is not obtainable, ethics constraints.

Stop and ask if the RQs cannot be answered with data the user can actually obtain.

### Step 2: Classify and load the standards

Match the study to one or more standards in `references/`. Mixed designs load every applicable standard.

- `general/` general-standard (always), engineering-research (proposes and evaluates an artifact), mixed-methods (2+ collection or analysis approaches)
- `quantitative/` experiment (human participants under controlled conditions), data-science (ML or computational analysis of SE artifacts), repository-mining, questionnaire-survey, benchmarking (competitive evaluation of systems on a benchmark), longitudinal, optimization-study, quantitative-simulation
- `qualitative/` case-study, grounded-theory, action-research, qualitative-survey
- `literature-review/` systematic-review, case-survey
- `other/` replication, meta-science

Typical LLM-for-SE study: engineering-research + benchmarking, often + data-science. Load `supplements/Sampling.md` whenever a subset of a dataset, benchmark, or population is selected; `supplements/OpenScience.md` always; the others only when triggered (human participants, secondary data, multiple raters, plots). Read `general/glossary.md` before writing about validity.

### Step 3: Build the decision list

Walk every Essential attribute of every loaded standard and turn it into a decision the project must make. Group attributes that are settled by the same decision. Desirable attributes are opt-in: add them only when they change what the paper can claim.

Decisions that almost always appear:

- **Benchmark / dataset and sampling**: source, selection and filtering steps, final size, argument for representativeness if generalization is claimed (Sampling supplement).
- **Variables**: independent (model, prompt, technique, config), dependent (metrics with units and measurement method), controlled (seed, versions, hardware, temperature), uncontrolled (declared).
- **Baselines**: state-of-the-art alternatives that are actually available and runnable, or the rationale for not comparing.
- **Metrics**: definition, why each measures the construct, known failure modes.
- **Protocol**: repetitions and seeds, timeouts, run order, pilot size (`--num_samples`). Enough repetitions to assess stability.
- **Analysis plan**: descriptive statistics with distributional information, inferential tests with assumption checks, effect sizes with confidence intervals, multiple-comparison correction. Decided before any data exists.
- **Threats to validity**: construct, internal, external, conclusion; each with the mitigation built into the design and the residual risk.
- **Replication package and ethics**: what is released, license, archive; which ethics supplement applies.

Check each standard's **Antipatterns** section and confirm no decision commits one.

### Step 4: Grill, then write one ADR per decision

Resolve the decision list in dependency order (dataset before metrics, metrics before analysis plan) following the Grill rules in `AGENTS.md`: one question at a time, recommended answer included, codebase explored instead of asked when possible.

When a decision converges, copy `docs/adr/template.md` to `docs/adr/{NNNN}-{kebab-case-title}.md` and fill every section, keeping it under half a page. Requirements specific to this skill:

- **Context** names the RQs it serves and cites the standard attributes it satisfies, e.g. `Satisfies: benchmarking/Essential "assesses stability using sufficient repetitions"; general/Essential "describes in detail how the data were analyzed"`.
- **Alternatives** lists what a reviewer would ask "why not X" about, with the reason X was rejected.
- **Consequences** ends with the code location(s) the decision lands in (see Step 5).
- Status starts as `proposed`; the user flips it to `accepted`. Accepted ADRs are never edited; a changed decision gets a new ADR that supersedes the old one, which is how deviations between design and execution get recorded.

Maintain `docs/adr/README.md` as the index with a Standards column so uncovered Essential attributes are visible:

```
| ID | Title | Status | Date | Standards |
|----|-------|--------|------|-----------|
| [0001](0001-....md) | ... | accepted | YYYY-MM-DD | benchmarking/E3, general/E6 |
```

Before implementation, every Essential attribute of every loaded standard maps to at least one ADR. Anything that cannot be satisfied is recorded in an ADR with status `proposed` and the reason, never silently dropped.

### Step 5: Map ADRs to the code layout

Layout and conventions come from the project's `AGENTS.md` and `.claude/spec/code-style.md`. Default mapping:

| Decision | Code location | Rule |
|----------|---------------|------|
| Dataset, models, controlled variables | `configs/{benchmark}.yaml` | Single source of truth. Seed, temperature, max_tokens, model IDs live here; nothing is hard-coded in `src/` or `eval/`. Baselines are entries in the same `models:` list. |
| Sampling | `eval/{benchmark}/main.py --step preprocess` | Selection and filtering are a script step, not a manual process. Log exclusion counts per step. |
| Protocol | `eval/{benchmark}/main.py --step inference` | One run = one (model, seed). Persist every per-instance raw output under `data/{benchmark}/results/{model_name}/`; never store only aggregates. Resumable. `--num_samples` for the pilot. |
| Metrics | `eval/{benchmark}/main.py --step score` | Pure functions from raw outputs to metric values, tested on hand-checked instances. |
| Analysis plan | `eval/{benchmark}/main.py --step analyze` | Reads raw results only. Implements exactly the tests, effect sizes, and CIs in the ADR. Writes `eval/tables-and-figures/rq{n}-{type}.csv/.png`. Committed before the full run. |
| Compute budget | `scripts/{benchmark}_vllm.sh`, `scripts/{benchmark}_api.sh` | One script per model type, `MODELS=()` array, template from code-style. See the `create` skill for partitions. |
| Replication package | `README.md`, `LICENSE`, `docs/adr/` | Commands to reproduce every table and figure from raw results. |

Coding rules derived from the standards' antipatterns:

- Raw before aggregate: persist all per-instance results, analyze offline (benchmarking).
- Preprocessing that changes distributions applies to training data only (data-science).
- No peeking: the analyze step is written before the main run; a change afterwards is a new ADR superseding the analysis-plan ADR.
- Baselines run through the same harness, data, metrics, and repetitions as the proposed method.
- Every run writes metadata: config hash, git commit, seed, hardware, library versions, wall time, failures. Failed runs are reported, not silently retried.

### Step 6: Implement and self-check

Implement following the four steps in `AGENTS.md` (domain interface, event flow, behavioral tests, logic), one step at a time. Run the pilot with `--num_samples` before any full job. Then re-read the ADR index and confirm each Consequences code location exists and behaves as the ADR states.

## Principles

1. **Standards are requirements, not review criteria.** An Essential attribute unmet at design time is a guaranteed Weak Reject later; fix it now when it is cheap.
2. **Pre-register the analysis.** Tests, effect sizes, and corrections are decided in an ADR before data exists.
3. **Everything reproducible from configs and scripts.** If a step needs a human to click or remember, it is not designed yet.
4. **Honest scope.** A single benchmark cannot support "general applicability"; write the claim the design can support and size the evaluation to the claim.
5. **YAGNI applies to design too.** Take a Desirable attribute only when it changes what the paper can claim; do not add experiments the RQs do not need.
