# Optimization Studies in SE (including Search-Based Software Engineering)

Research studies that focus on the formulation of software engineering problems as search problems, and apply optimization techniques to solve such problems1.

## Application

This standard applies to empirical studies that meet the following criteria:

- Formulates a software engineering task2 as an optimization problem, with one or more specified fitness functions3 used to judge success in this task.
- Applies one or more approaches that generate solutions to the problem in an attempt to maximize or minimize the specified fitness functions.

## Specific Attributes

We stress that the use of optimization in SE is still a rapidly evolving field. Hence, the following criteria are approximate and there may exist many exceptions to them. Reviewers should reward sound and novel work and, where possible, support a diverse range of studies.

### Essential Attributes

- explains why the problem cannot be optimized manually or by brute force within a reasonable timeframe4

- EITHER: describes prior state of the art in this area
    OR: carefully motivates and defines the problem tackled and the solution proposed
- describes the search space (e.g., constraints, independent variables choices)
- uses realistic and limited simplifications and constraints for the optimization problem; simplifications and constraints do not reduce the search to one where all solutions could be enumerated through brute force
- justifies the choice of algorithm5 underlying the approach6
- compares approaches to a justified and appropriate baseline7
- explictly defines the solution formulation, including a description of what a solution represents8, how it is represented9, and how it is manipulated
- explicitly defines all fitness functions, including the type of goals that are optimized and the equations for calculating fitness values
- explicitly defines evaluated approaches, including the techniques, specific heuristics, and the parameters and their values10
- EITHER: clearly describes (and follows) a sound process to collect and prepare the datasets used to run and to evaluate the optimization approach
    OR: if the subjects are taken from previous work, fully reference the original source and explain whether any transformation or cleaning was applied to the datasets
- EITHER: makes data publicly available OR: explains why this is not possible11
- identifies and explains all possible sources of stochasticity12
- EITHER: executes stochastic approaches or elements multiple times
    OR: explains why this is not possible13

### Desirable Attributes

- provides a replication package that conforms to SIGSOFT standards for artifacts14.
- motivates the novelty and soundness of the proposed approach15
- explains whether the study explores a new problem type (or a new area within an existing problem space), or how it reproduces, replicates, or improves upon prior work
- explains in detail how subjects or datasets were collected/chosen to mitigate selection bias and improve the generalization of findings
- describes the main features of the subjects used to run and evaluate the optimization approach(es) and discuss what characterizes the different instances in terms of "hardness"
- justifies the use of synthetic data (if any); explain why real-world data cannot be used; discusses the extent to which the proposed approach and the findings can apply to the real world
- (if data cannot be shared) provides a sample dataset that can be shared to illustrate the approach
- selects a realistic option space for formulating a solution; any values set for attributes should reflect one that might be chosen in a "real-world" solution, and not generated from an arbitrary distribution
- justifies the parameter values used when executing the evaluated approaches (and note that experiments trying a wide range of different parameter values would be extraordinary, see below)
- samples from data multiple times in a controlled manner (where appropriate and possible)
- performs multiple trials either as a cross-validation (multiple independent executions) or temporally (multiple applications as part of a timed sequence), depending on the problem at hand
- provides random data splits (e.g., those used in data-driven approaches) or ensures splits are reproducibile.
- compares distributions (rather than means) of results using appropriate statistics
- compares solutions using an appropriate meta-evaluation criteria16; justifies the chosen criteria
- clearly distinguishes evidence-based results from interpretations and speculation17

### Extraordinary Attributes

- analyzes different parameter choices to the algorithm, indicating how the final parameters were selected18
- analyzes the fitness landscape for one or more of the chosen fitness functions

## General Quality Criteria

The most valuable quality criteria for optimization studies in SE include reliability, replicability, reproducibility, rigor, and usefulness (see Glossary).

## Examples of Acceptable Deviations

- The number of trials can be constrained by available time or experimental resources (e.g. where experiments are time-consuming to repeat or have human elements). In such cases, multiple trials are still ideal, but a limited number of trials can be justified as long as the limitations are disclosed and the possible effects of stochasticity are discussed.
- The use of industrial case studies is important in demonstrating the real-world application of a proposed technique, but industrial data generally cannot be shared. In such cases, it is recommended that a small open-source example be prepared and distributed as part of a replication package to demonstrate how the approach can be applied.

## Antipatterns

- Reporting significance tests (e.g., Mann-Whitney Wilcoxon test) without effect size tests (see Notes)
- Conducting multiple trials but failing to disclose or discuss the variation between trials; for instance reporting a measure of central (e.g. median) without any indication of variance (e.g., a boxplot).

## Invalid Criticisms

- The paper is unimportant. Be cautious of rejecting papers that seem "unimportant" (in the eyes of a reviewer). Research is exploratory and it is about taking risks. Clealy-motivated research and speculative exploration are both important and should be rewarded.
- The paper just uses older algorithms with no reference to recent work. Using older (and widely understood algorithms) may be valid when they are used, e.g., (1) as part of a larger set that compares many approaches; e.g. (2) to offer a "straw man" method that defines the "floor" of the performance (that everything else needs to beat); or (3), as a workbench within which one thing is changed (e.g., the fitness function) but everything else remains constant.
- That an approach is not benchmarked against an inappropriate or unavailable baseline. If a state-of-the-art approach lacks an available and functional implementation, it is not reasonable to expect the author to recreate that approach for benchmarking purposes.
- That a multi-objective approach is not compared to a single-objective approach by evaluating each objective separately. This is not a meaningful comparison because, in a multi-objective problem, the trade-off between the objectives is a major factor in result quality. It is more important to consider the Pareto frontiers and quality indicators.
- That one or very few subjects are used, as long as the paper offers a reasonable justification for why this was the case.
