# Benchmarking (of Software Systems)

A study in which a software system is assessed using a standard tool (i.e. a benchmark) for competitively evaluating and comparing methods, techniques or systems "according to specific characteristics such as performance, dependability, or security" (Kistowski et al. 2015).

## Application

This standard applies to empirical research that meets the following conditions.

- investigates software systems within a defined context with an automated, repeatable procedure
- studies the software system's quality of service under a specific workload or usage profile

If the benchmark experiments primarily study software systems, use this standard. For experiments with human participants, see the Experiments (with Human Participants) Standard. For simulation of models of the software systems, see the Simulation (Quantitative) Standard. If the study is conducted within a real-world context, see the Case Study and Ethnography Standard. Benchmarking is often used with Engineering Research (see the Engineering Research (AKA Design Science) Standard)

## Specific Attributes
### Essential Attributes

- EITHER: justifies the selection of an existing, publicly available or standard benchmark (in terms of relevance, timeliness, etc.)
- OR: defines a new benchmark, including:
    - (i) the quality to be benchmarked (e.g., performance, availability, scalability, security),
    - (ii) the metric(s) to quantify the quality,
    - (iii) the measurement method(s) for the metric (if not obvious),
    - (iv) the workload, usage profile and/or task sample the system under test is subject to (i.e. what the system is doing when the measures are taken) AND justifies the design of the benchmark (in terms of relevance, timeliness, etc.) AND reuses existing benchmark design components from established benchmarks or justifies new components
- describes the experimental setup for the benchmark in sufficient detail to support independent replication (or refers to such a description in supplementary materials)
- specifies the workload or usage profile in sufficient detail to support independent replication (or refers to such a description in supplementary materials)
- allows different configurations of a system under test to compete on their merits without artificial limitations

- assesses stability or reliability using sufficient experiment repetitions and execution duration
- discusses the construct validity of the benchmark; that is, does the benchmark measure what it is supposed to measure?

### Desirable Attributes

- provides supplementary materials including datasets, analysis scripts and (for novel benchmarks) extended documentation
- provides benchmark(s) in a usable form that facillitates independent replication
- reports on independent replication of the benchmark results
- reports on a large community that uses the benchmark
- reports on an independent organization that maintains the benchmark
- uses or creates open source benchmarks
- transparently reports on problems with executing benchmark runs, if any

### Extraordinary Attributes

- provides empirical evidence for the relevance of a benchmark, e.g., using a Systematic Review
- provides empirical evidence for the usability of a benchmark, e.g., using Action Research or Case Studies

## General Quality Criteria

Fairness of measurements, reproducibility of results across experiment repetitions, benchmarking the right aspects, using a realistic benchmark with a representative workload

## Examples of Acceptable Deviations

- the nature of the benchmark requires specialized hardware (e.g. a quantum computer) so it not easy to replicate
- in a study that replicates published existing work, the description of the experimental setup could be quite brief
- the study only employs one (or a few) runs because prior work has shown that a single run is sufficient

## Antipatterns

- Tailoring the benchmark for a specific method, technique or tool, which is evaluated with the benchmark.
- Using benchmarking experiments that are irrelevant for the problem studied to obfuscate weaknesses in the proposed approach
- Insufficient repetitions or duration to assess stability of results
- Collecting aggregated measurements instead of persisting all raw results and running an offline analysis

## Invalid Criticisms

- The benchmark is not widely used. It is sufficient to start developing a new benchmark with a small group of researchers as an offer to a larger scientific community. Such a proto-benchmark (Sim et al. 2003) can act as a template to further the discussion of the topic and to initialize the consensus process.
- No independent replication of the benchmark results is reported.
- There is no independent organization that maintains the benchmark.
