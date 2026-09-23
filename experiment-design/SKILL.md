---
name: experiment-design
description: Design empirical software engineering studies using ACM/SIGSOFT standards, record decisions as ADRs, and map an agreed design to project code.
---

# Experiment Design

Produce a study whose research questions, evidence, analysis, and claims agree. Use the bundled empirical standards to identify design obligations and record material decisions in `docs/adr/`. For a focused revision, revisit the affected decisions rather than restarting the entire design.

## Establish the design

Extract the objective, research questions, contribution type, obtainable data, and compute, deadline, and ethics constraints from the request and project. Add hypotheses for confirmatory work. Resolve missing information that changes feasibility or scientific validity before depending on it.

Use [standards.md](references/standards.md) to select the relevant standards and supplements. Account for each applicable Essential attribute in an ADR, grouping attributes addressed by the same decision. Record justified non-applicability and unresolved gaps explicitly. Add Desirable attributes only when they materially support the intended claim, and check the selected standards' Antipatterns.

Typical decisions concern datasets and sampling, variables, baselines, metric validity, repetitions and seeds, timeouts, analysis, threats to validity, and replication or ethics. Set the confirmatory analysis before the main run, including applicable assumption checks, effect sizes, confidence intervals, and multiple-comparison handling. Label later exploratory analysis and deviations explicitly.

## Record decisions

Use the project's ADR template and decision workflow when present. Follow a one-question-at-a-time Grill workflow only if the project or user requests it. Reuse decisions and authorization already established in the conversation; ask for unresolved consequential choices with a recommendation and tradeoffs.

Each ADR should identify the RQs, cite the standard attributes it covers, explain the choice and meaningful alternatives, and record consequences. For implementation work, include the actual code or configuration locations. If no template exists, use these fields in `docs/adr/NNNN-title.md`.

Use `proposed` for unresolved decisions and `accepted` for decisions the user has agreed to, including agreement already given in the conversation. Do not require the user to edit status fields manually. Preserve accepted decisions; record a changed decision in a superseding ADR. Keep an index at `docs/adr/README.md` linking decisions, status, and covered standard attributes.

## Implement when requested

Map the agreed design to the existing project structure. For research-template projects, read [implementation.md](references/implementation.md); other projects keep their own layout. Do not make implementation contingent on unrelated unanswered decisions, but resolve any gap that would invalidate the affected experiment before running it.

Persist per-instance outputs and run metadata, use the same evaluation conditions for baselines, and record failures. Run a pilot within the agreed budget before the full experiment. Check that the implemented sampling, scoring, and analysis match the ADRs. Designing a study alone does not authorize a full compute run.

## Completion

A design is ready when the requested RQs have a feasible evidence and analysis plan, applicable Essential attributes are traceable to decisions, and unresolved limitations are explicit. Implementation is ready when its affected decisions map to working code and the pilot supports the planned execution. Report concrete remaining blockers without claiming guaranteed publication outcomes or generality the design cannot support.
