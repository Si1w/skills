# Simulation (Quantitative)

A study that involves developing and using a mathematical model that imitates a real-world system's behavior, which often entails problem understanding, data collection, model development, verification, validation, design of experiments, data analysis, and implementation of results.

## Application

The standard applies to research studies that use simulation to understand, assess or improve a system or process and its behavior. Use this standard for in silico simulations, i.e., studies representing everything using computational models. For in virtuo simulations, i.e., human participants manipulating simulation models, use the Experiments (with human participants) Standard. For simulations used to assess a new or improved technological artifact, also consider the Engineering Research standard.

## Specific Attributes
### Essential Attributes

- justifies that simulation is a suitable method for investigating the problem (or research question, etc.)
- describes the simulation model (conceptual, implementation, or hybrid abstraction levels), including input parameters and response variables
- describes the underlying simulation approach1
- describes simulation packages or tools used to develop and run the simulation model, including version numbers, and computational environments
- describes the data used for model calibration, the calibration procedures, and contextual information
- describes how the simulation model was verified and validated at different abstraction levels2
- describes the study protocol, including independent variables, scenarios, number of runs per scenario (in case of using stochastic simulation), and steady-state or terminating conditions
- analyzes validity threats considering the supporting data and the simulation model3
- clearly explicates the assumptions of the simulation model

### Desirable Attributes

- provides supplementary materials including the raw data (for real data) or generation mechanism (for synthetic data) used for model calibration, all simulation models and source code, analysis scripts
- characterizes reference behaviors for the definition of simulation scenarios with representative and known values or probability distributions for input parameters4
- separates conceptual and implementation levels of the simulation model
- reports sensitivity analysis for input parameters or factors
- clearly distinguishes evidence-based results from interpretations and speculation5

### Extraordinary Attributes

- describes how stakeholders were involved in developing and validating the simulation model6
- provides a modular view of the simulation model, allowing reuse in different contexts7

## General Quality Criteria

Conclusion validity, construct validity, internal validity (if examining causal relationships), external validity, and reproducibility.

## Antipatterns

- Overfitting8 the simulation model to reproduce a reference behavior.
- Use of non-standard experimental designs9 without justification.
- Using a single run instead of multiple runs to experiment with stochastic models.

## Examples of Acceptable Deviations

- If insufficient data is available (or too costly to collect) to calibrate the model, assumptions can be used to implement parts of the model. These assumptions, however, must be explained and justified.
- When the translation from a conceptual to implementation model is straightforward, authors may present them together.
- If the simulation approach used is very common in software engineering (e.g. discrete-event simulation, system dynamics), it is sufficient to indicate which approach is used, citing appropriate references, rather than explaining in full how the approach works.

## Invalid Criticisms

- The mere presence of assumptions in the model is not a valid basis for criticism as long as the assumptions are documented and justified, and their implications for the validity of the simulation are sufficiently addressed. All models make assumptions.
- Claiming that the model is too abstact without explaining why the level of abstraction is inadequate for the purposes of the study.
- Claiming that the study is invalid because it uses generated data, secondary data or approximations based on expert opinion, when no appropriate primary data is available.
