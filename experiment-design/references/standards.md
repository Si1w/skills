# Selecting empirical standards

Use the [general standard](general/general-standard.md) for all studies, then load the standards that match the actual methods. A mixed study may need several; an incidental keyword does not make every standard applicable.

| Study method | Reference |
|---|---|
| Propose and evaluate an artifact | [Engineering research](general/engineering-research.md) |
| Combine collection or analysis approaches | [Mixed methods](general/mixed-methods.md) |
| Controlled study with human participants | [Experiment](quantitative/experiment.md) |
| ML or computational analysis of SE artifacts | [Data science](quantitative/data-science.md) |
| Mine software repositories | [Repository mining](quantitative/repository-mining.md) |
| Quantitative questionnaire | [Questionnaire survey](quantitative/questionnaire-survey.md) |
| Compare systems on a benchmark | [Benchmarking](quantitative/benchmarking.md) |
| Observe changes over time | [Longitudinal](quantitative/longitudinal.md) |
| Evaluate an optimization method | [Optimization study](quantitative/optimization-study.md) |
| Quantitative simulation | [Quantitative simulation](quantitative/quantitative-simulation.md) |
| Study a bounded case in context | [Case study](qualitative/case-study.md) |
| Develop theory from qualitative data | [Grounded theory](qualitative/grounded-theory.md) |
| Intervene and study change collaboratively | [Action research](qualitative/action-research.md) |
| Qualitative survey | [Qualitative survey](qualitative/qualitative-survey.md) |
| Systematic literature review | [Systematic review](literature-review/systematic-review.md) |
| Synthesize cases | [Case survey](literature-review/case-survey.md) |
| Replicate an earlier study | [Replication](other/replication.md) |
| Study research practice itself | [Meta-science](other/meta-science.md) |

A typical LLM-for-SE artifact evaluation uses engineering research and benchmarking, with data science when its methods apply.

## Supplements

- [Open science](supplements/OpenScience.md): reproducibility and release planning for every study, documenting justified restrictions.
- [Sampling](supplements/Sampling.md): when selecting a subset of data, benchmarks, or participants.
- [Human participant ethics](supplements/EthicsHumanParticipants.md): when people participate.
- [Secondary data ethics](supplements/EthicsSecondaryData.md): when reusing data.
- [Engineering ethics](supplements/EthicsEngineering.md): when engineering artifacts creates ethical implications.
- [Inter-rater reliability](supplements/InterRaterReliabilityAndAgreement.md): when multiple raters label or judge observations.
- [Visualization](supplements/InformationVisualization.md): when designing research plots.
- [Registered reports](supplements/RegisteredReports.md): when targeting a registered-report process.

Consult the [glossary](general/glossary.md) when describing validity. Cite the actual standard and attribute wording in ADRs; do not invent attribute identifiers that the source does not define.
