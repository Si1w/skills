# Experiments (with Human Participants)

A study in which an intervention is deliberately introduced to observe its effects on some aspects of reality under controlled conditions

## Application

This standard applies to controlled experiments and quasi-experiments that meet all of the following conditions:

- manipulates one or more independent variables
- controls many extraneous variables
- applies each treatment independently to several experimental units
- involves human participants

In true experiments, experimental units are randomly allocated across treatments; quasi-experiments lack random assignment. Experiments include between-subjects, within-subjects and repeated measures designs. For experiments without human participants, see the Exploratory Data Science Standard or the Engineering Research Standard.

## Specific Attributes
### Essential Attributes

- states formal hypotheses
- uses two-sided hypotheses OR justifies use of one-sided hypotheses based on face validity or previous work
- describes the dependent variable(s) and justifies how they are measured (including units, instruments)
- describes the independent variable(s) and how they are manipulated or measured
- describes extraneous variables and how they are controlled: physically, statistically, or not at all
- justifies sample size (e.g. using power analysis)
- describes how characteristics of the phenomenon under investigation relate to experimental constructs
- describes the research design and protocol including treatments, materials, tasks, design (e.g. 2x2 factorial), participant allocation, period and sequences (for crossover designs), and logistics
- EITHER: uses random assignment and explains logistics (e.g. how random numbers were generated)
- OR: provides compelling justification for not using random assignment and explains how unequal groups threat to validity is mitigated (e.g. using pre-test/post-test and matched subjects design)
- describes experimental objects (e.g. real or toy system) and their characteristics (e.g. size, type)
- justifies selection of experimental objects; acknowledges object-treatment confounds, if any1
- design and protocol appropriate (not optimal) for stated research questions and hypotheses

- confirms no incentives for participation were offered or describes financial or non-financial incentives2
- describes participants (e.g. age, gender, education, relevant experience or preferences)
- reports distribution-appropriate descriptive and inferential statistics; justifies tests used

- reports effects sizes with confidence intervals (if using frequentist approach)
- discusses construct, conclusion, internal, and external validity
- discusses alternative interpretations of results

### Desirable Attributes

- provides supplementary material such as complete, algorithmic research protocol; task materials; raw, de-identified dataset; analysis scripts
- justifies hypotheses and Bayesian priors (if applicable) based on previous studies and theory
- discusses alternative experimental designs and why they were not used (e.g. validity trade-offs)
- includes visualizations of data distributions
- cites statistics research to support any nuanced issues or unusual approaches
- explains deviations between design and execution, and their implications3
- named experiment design (e.g. simple 2-group, 2x2 factorial, randomized block)
- analyzes construct validity of dependent variable
- reports manipulation checks
- pre-registration of hypotheses and design (where venue allows)
- clearly distinguishes evidence-based results from interpretations and speculation4

### Extraordinary Attributes

- reports multiple experiments or replications in different cultures or regions
- uses multiple methods of data collection; data triangulation
- longitudinal data collection with appropriate time-series analysis (see the Longitudinal Studies Standard)
- uses (internally and externally valid) payoff function(s) for financial incentives

## Examples of Acceptable Deviations

- Sample size is not justified by power analysis a priori because the study is conducted in a classroom in which the number of available participants is fixed.

## General Quality Criteria

Conclusion validity, construct validity, internal validity, reliability, objectivity, reproducibility

## Antipatterns

- using bad proxies for dependent variables (e.g. task completion time as a proxy for task complexity)
- quasi-experiments without a good reason5
- treatments or response variables are poorly described
- inappropriate design for the conditions under which the experiment took place
- data analysis technique used does not correspond to the design chosen or data characteristics (e.g. using an independent samples t-test on paired data)
- validity threats are simply listed without linking them to results

## Invalid Criticisms

- participants are students—appropriateness of participant characteristics should be judged based on the context, desired level of control, trade-off choices between internal and external validity, and the specifics of the technology (i.e. method, technique, tool, process, etc.) under evaluation; the choice must be explained in the paper
- low external validity
- the experiment is a replication
- the reviewer would have investigated the topic in any other way than an experiment
- not enough participants (unless supported by power analysis)
- not employing an incentivization scheme
