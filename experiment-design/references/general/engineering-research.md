# Engineering Research (AKA Design Science)

Research that invents and evaluates technological artifacts

## Application

This standard applies to manuscripts that propose and evaluate technological artifacts, including algorithms, models, languages, methods, systems, tools, and other computer-based technologies. This standard is not appropriate for:

- evaluations of pre-existing engineering research approaches (consider the Experiments Standard)
- experience reports of applying pre-existing engineering research approaches

## Specific Attributes
### Essential Attributes

- describes the proposed artifact in adequate detail1
- justifies the need for, usefulness of, or relevance of the proposed artifact2

- conceptually evaluates the proposed artifact; discusses its strengths, weaknesses and limitations3
- empirically evaluates the proposed artifact using:
    - action research, in which the researchers intervene in a real organization using the artifact,
    - a case study in which the researchers observe a real organization using the artifact,
    - a controlled experiment in which human participants use the artifact,
    - a quantitative simulation in which the artifact is assessed (usually against a competing artifact) in an artificial environment,
    - a benchmarking study, in which the artifact is assessed using one or more benchmarks, or
    - another method for which a clear and convincing rationale is provided
- clearly indicates which of the above empirical methodology is used
- EITHER: discusses state-of-art alternatives (and their strengths, weaknesses and limitations)
    - OR: explains why no state-of-art alternatives exist
    - OR: provides compelling argument that direct comparisons are impractical

- EITHER: empirically compares the artifact to one or more state-of-the-art alternatives
    - OR: empirically compares the artifact to one or more state-of-the-art benchmarks
    - OR: provides a clear and convincing rationale for why comparative evaluation is impractical
- assumptions (if any) are explicit, plausible and do not contradict each other or the contribution’s goals
- uses notation consistently (if any notation is used)

### Desirable Attributes

- provides supplementary materials including source code (if the artifact is software) or a comprehensive description of the artifact (if not software), and any input datasets (if applicable)
- justifies any items missing from replication package based on practical or ethical grounds
- discusses the theoretical basis of the artifact
- provides correctness arguments for the key analytical and theoretical contributions (e.g. theorems, complexity analyses, mathematical proofs)
- includes one or more running examples to elucidate the artifact
- evaluates the artifact in an industry-relevant context (e.g. widely used open-source projects, professional programmers)

### Extraordinary Attributes

- contributes to our collective understanding of design practices or principles
- presents ground-breaking innovations with obvious real-world benefits

## General Quality Criteria

- Comprehensiveness of proposed artifact description
- Appropriateness of evaluation methods to the nature, goals, and assumptions of the contribution
- Relationship of innovativeness to rigorousness: less innovative artifacts require more rigorous evaluations

## Antipatterns

- overstates the novelty of the contribution
- omits details of key conceptual aspects while focusing exclusively on incidental implementation aspects
- evaluation consists only of eliciting users’ opinions of the artifact
- evaluation consists only of quantitative performance data that is not compared to established benchmarks or alternative solutions (see related point in “Invalid Criticism”)
- evaluation using a non-experimental (single group, non-repeated) design
- evaluation using toy examples (sometimes misrepresented as “case studies”)

## Invalid Criticisms

- The paper does not report as ambitious an empirical study as other predominately empirical papers. The more innovative the artifact and more comprehensive the conceptual evaluation, the less we should expect from the empirical study.
- “Too few experimental subjects” (e.g. the source code used to evaluate a static analysis technique) if few subjects are available in the contribution’s domain or the experimental evaluation is part of a more comprehensive validation strategy (e.g. formal arguments). Other criteria, such as the variety, realism, availability, and scale of the subjects, should also be considered.
- No replication package, if there are clear, convincing practical or ethical reasons preventing artifact disclosure.
- The artifact is not experimentally compared with related approaches that are not publicly available. In other words, before saying “you should have compared this against X,” make sure X is actually available and functional.
- This is not the first known solution to the identified problem. Proposed artifacts should outperform existing artifacts on some dimension(s); e.g. scalability, performance on specific classes of problems, applicability to realistic systems, theoretical guarantees.
- The paper does not explicitly define research question(s). Engineering papers often define a motivating “problem” or “objective” rather than a research questiion.
- The contribution is not technically complicated. What matters is that it works. Unnecessary complexity is undesirable.