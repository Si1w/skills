# Longitudinal Studies

A study focusing on the changes in and evolution of a phenomenon over time

## Application

This standard applies to studies that involve repeated observations of the same variables (e.g., productivity or technical debt) over a period of time. Longitudinal studies include the analysis of datasets over time, such as the analysis of the evolution of the code. Longitudinal studies require to maintain identifiability of subjects (humans or artifacts) between data collection waves and to use at least two waves.

For cross-sectional analysis, consider the Exploratory Data Science Standard or the Experiments Standard (if variables are manipulated).

## Specific Attributes
### Essential Attributes

- determines the appropriate number of waves based on the natural oscillation of the research phenomenon1
- uses at least two data collection waves
- subjects (humans or artifacts) are identifiable between waves
- justifies the data analysis strategy2
- the data analysis strategy is appropriate for the interdependent nature of the data3
- discusses the critical alpha levels or justifies Bayesian priors4
- justifies sample size (e.g. using power analysis)5
- describes data loss throughout the different waves

- explains how missing data are handled

- describes the subjects (e.g., demographic information in the case of humans)6
- discusses the operationalization of the research model (i.e. construct validity)7

### Desirable Attributes

- provides supplementary materials including data sets, data collection scripts or instruments, analytical scripts, a description of how to reproduce the work and any other materials used
- either builds new theory or tests existing theory
- investigates causality using the longitudinal nature of the data to establish precedence and statistically controlling for third-variable explanations
- discusses potential confounding factors (for inferential analyses) that cannot be statistically controlled
- discusses data (in)consistency across waves (e.g. test-retest reliability)
- examines differences in distributions between waves (and uses an appropriate data analysis strategy)
- describes the cost of gathering data and any incentives used
- addresses survivorship bias8

### Extraordinary Attributes

- uses a multi-stage selection process to identify the study's subjects9
- follows subjects for an exceptionally long period (e.g. more than five years)

## General Quality Criteria

Reliability, internal validity, conclusion validity, construct validity, and external validity.

Longitudinal studies exploit the temporal nature of data to maximize internal validity. Other criteria are sometimes sacrificed to improve internal validity.

## Antipatterns

- subject loss between waves is too high, leading to a severely underpowered study
- the period between waves does not match the phenomenon's natural cycles
- treating longitudinal data as cross-sectional

## Variations

- Experience sampling provides a highly specific understanding of a phenomenon through multiple repeated measurements per day over a short period (typically one to three weeks). It emphasizes in-the-moment assessment rather than reflective assessment (van Berkel et al. 2017). This standard applies to experience sampling studies.
- Cohort studies are a type of analytical observational study where researchers investigate the relationship between an independent and dependent variable by observing subjects over time and comparing groups with different levels of exposure. Cohort studies follow more strict rules than presented here.10

## Invalid Criticisms

- Claiming that the time span between measurements is too short or too long.
- Claiming that the number of waves is inadequate without a reasoned explanation.
- Claiming that the sample size is too small without performing a post hoc power calculation.
- Claiming that the paper with a modest number of comparisons should have used more conservative alphas or adopted a Bayesian approach.
- Complaining about generalizability when the paper clearly acknowledges limitations to generalizability.
