# Repository Mining

A study that quantitatively analyzes a dataset extracted from a platform hosting of structured or semi-structured text (e.g a source code repository)

## Application

The standard applies to software engineering studies that: - use automated techniques to extract data from large-scale data repositories such as source code repositories, mailing list archives, bug tracking systems, Q&A forums and chat communication platforms - quantitatively analyze the contents mined from the repositories

If the study focuses on predictive modeling (e.g. machine learning) consider the Data Science Standard. If the subject systems are a few context-rich repositories, consider the Case Study Standard. If the analysis is predominately qualitative, refer to methodological guidelines for qualitative content analysis or discourse analysis (standard TBD).

## Specific Attributes

### Essential Attributes

- explains why repository mining is appropriate for the proposed research problem
- defines unit(s) of analysis or observation
- describes and justifies the data sources (e.g. GitHub, StackOverflow)
    - (if the selected data source(s) are obscure) explains in detail why they are appropriate for the goals of the study (e.g. consider number of repositories data quality, terms and conditions that may limit access to information)
- describes and justifies how the repositories are selected from the data sources (e.g. selection criteria, use of third-party tools, APIs, programming languages of choice)
- describes how the inclusion and exclusion criteria were validated (e.g., by manually inspecting the results of the automated search)
- describes the selected repositories
- describes the procedure for the acquisition (e.g., first selecting repositories and then downloading, or all completed together)
- if the data obtained is too large to be processed in its entirety
    - explains why (e.g., unfeasibility of a manual study, processing limitations, scope limitations)
    - explains the sampling strategy (see the Sampling Supplement)
- describes dataset characteristics including size of the selected repositories, and dataset attributes relevant to the study at hand (e.g., number of commit messages)
- describes data preprocessing steps
- if manual annotations are carried out:
    - uses multiple annotators; reports the number of annotators
    - describes the annotators (e.g. demographics, experience, training),
    - describes in detail the annotation procedure (e.g. what types of questions were asked to the annotators),
    - assesses inter-rater reliability (see the Inter-Rater Reliability Supplement)
- describes and justifies measures or metrics used

- uses previously validated measures, quantitatively assesses construct validity, or both

- if predictive modeling is used, complies with the Data Science Standard
- discusses threats to external validity (e.g. caused by selection of data source(s) and repositories, selection criteria, search strings)

### Desirable Attributes

- provides supplemental materials (e.g. complete dataset, tool(s) used to download, select, pre-process, and post-process the selected repositories)
- uses probability sampling (see the Sampling Supplement)
- suggests future work that validates or uses the same sample
- quantitatively assess construct validity (e.g. using factor analysis)
- triangulates across data sources, informants or researchers
- annotators reflect on their own possible biases
- qualitative analysis of scenarios where the data collection or analysis tools were ineffective
- performs testing (e.g., unit testing) to avoid bugs in the proposed tool
- builds, tests or extends theory
- tests formal hypotheses
- discusses ethical issues in mining of software repositories1 (e.g., data privacy)

### Extraordinary Attributes

- establishes causality, e.g. using longitidunal analyses

## General Quality Criteria

Internal validity, external validity, construct validity, reliability.

## Examples of Acceptable Deviations

- studies that focus on specific ecosystems (such as Apache) may choose specific repositories
- obfuscating some details of the dataset due to ethical concerns

## Antipatterns

- limiting a study to quantitative description; failing to test, build or extend theory
- unvalidated, uni-dimensional operationalizations of multidimensional constructs (e.g. using github stars as a proxy for popularity)
- using open-source repositories without any filtering criteria; i.e., convenience sampling2.
- in a study where all the commits of a project need to be analyzed, only the GitHub repository is considered; a GitHub repository does not necessarily contain all commits of a project3.
- conclusions must be derived in the context of the selected repositories; deriving generic conclusions applicable to the selected repositories but necessarily to a larger generic set is an antipattern
- insufficient details about the applied processing steps of the selected repositories

## Invalid Criticisms

- more data, sources, or repositories required without appropriate justification
- study doesn't use qualitative analysis or data
- a different source should have been used when the selected source(s) are justified
- complaining about intentional obfuscation of repository details to protect participant's identities
- in manual studies, requiring the disclosure of the time required for completion
