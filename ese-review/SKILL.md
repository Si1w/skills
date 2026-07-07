---
name: ese-review
description: Review a paper against ACM/SIGSOFT Empirical Standards. Treat background and related work as interchangeable section names.
---

# Empirical Software Engineering Review

Close-reading review of the uploaded paper (PDF/tex) against the empirical standards in `references/`. Every section, every claim matters: do not skim, do not give the benefit of the doubt. The default disposition is skeptical but calibrated, never reflexive. Default output destination is chat; write a file only when the user explicitly asks to save or export.

## Review Process

### Step 1: Classify the paper

Match the paper's type(s) to a standard in `references/`. If it mixes methods (e.g. mining + experiment), evaluate against all applicable standards, weighted by each method's role in the study.

- `general/` general-standard (always), engineering-research (invents and evaluates a technological artifact), mixed-methods (combines 2+ data collection/analysis approaches)
- `quantitative/` experiment (intervention under controlled conditions), data-science (analyzes SE artifacts via ML or computation), repository-mining (quantitative analysis of platform-hosted data), questionnaire-survey (structured-question sample), benchmarking (competitive evaluation with a standard tool), longitudinal (change or evolution over time), optimization-study (SE problem framed as search), quantitative-simulation (mathematical model of system behavior)
- `qualitative/` case-study (in-depth inquiry of a phenomenon in its real-world context, including ethnography), grounded-theory (iterative collection + analysis yielding patterns), action-research (how an intervention affects a real-life context), qualitative-survey (semi-structured or open-ended interviews)
- `literature-review/` systematic-review (appraises and synthesizes literature), case-survey (converts qualitative case descriptions into quantitative data)
- `other/` replication (deliberately repeats a prior study), meta-science (analyzes methodology or makes methodological recommendations)

### Step 2: Load the standards and review aids

Read `general/general-standard.md` (always) plus the matched specific standard(s). Two general aids:
- `general/scoring-rubric.md` turns attribute satisfaction into a recommendation and a 1-5 score
- `general/glossary.md` precise definitions of recurring terms (validity types, recoverability, rigor, anonymization) to ground the terminology checks

When the paper raises a cross-cutting concern, also consult the matching file in `supplements/` (official guidance, not method standards; load only what the paper actually triggers): ethics (`EthicsHumanParticipants`, `EthicsSecondaryData`, `EthicsEngineering`), `Sampling`, `InterRaterReliabilityAndAgreement`, `OpenScience`, `RegisteredReports`, `InformationVisualization`, `ReviewerMisconduct`.

### Step 3: Close reading, section by section

Read end-to-end, paragraph by paragraph.

For each section, record:
- **Claims**: is each assertion backed by evidence, or hand-waving?
- **Logic gaps**: non sequiturs, cross-section contradictions (X increases here, decreases there).
- **Vague language**: "significantly improves", "generally outperforms", "reasonable results" with no numbers. Quote and locate.
- **Missing details**: anything a reader needs to reproduce or evaluate the work.
- **Inconsistencies**: text vs tables/figures, intro vs conclusion, method vs what was evaluated.
- **Terminology drift**: a concept silently renamed mid-paper (e.g. "fault localization" to "bug detection").
- **Serious grammar**: structural errors or Chinglish that make meaning ambiguous (skip stylistic preferences).

Section-specific focus:
- **Title & Abstract**: does the title reflect the contribution? Does the abstract overstate or include claims absent from the body?
- **Introduction**: is the problem motivated and the gap explicit (not implied)? Are the contributions actually novel?
- **Background / Related Work**: comprehensive, current, honest positioning, or strawmanning competitors?
- **Methodology**: enough detail to replicate? Threats addressed where they arise, not just in a token section?
- **Results**: all RQs answered with data? Tests appropriate? Effect sizes, not just p-values? Honest visualizations?
- **Discussion**: beyond restating results? Implications grounded, limitations honest?
- **Threats to Validity**: substantive and specific, or a copy-paste checklist?

### Step 4: Build or load the checklist

If `review-checklist.md` exists in the paper's folder, read it. Otherwise generate it from the loaded standards:

```
# Review Checklist
- Paper: [title]
- Type: [research type]
- Standards: [list]
- Date: [date]

## [Standard] - Essential / Desirable / Extraordinary Attributes
- [ ] item

## Antipatterns
- [ ] item (merged from all standards)

## Invalid Criticisms
- item (no checkboxes, for reference only)
```

### Step 5: Evaluate each checklist item

Zero tolerance. Mark `[x]` if satisfied; for `[ ]`, write a pointed annotation that quotes the deficiency. Never write "insufficient", write exactly what is missing and why it matters. Save to `review-checklist.md`.

- **Bad**: `- [ ] Validity discussion: insufficient`
- **Good**: `- [ ] Validity discussion: Section 6.2 mentions construct validity in one sentence ("We acknowledge potential threats to construct validity") but never identifies the actual threats. No discussion of mono-method bias despite relying solely on automated metrics. No discussion of data leakage between train/test splits.`

### Step 6: Produce the review output

Blunt, specific, unambiguous about what is wrong and why it matters. Default to chat; write a file only on explicit request.

Chat structure:
- **Summary** (2-3 sentences): what the paper does, method, claims. Factual, no praise.
- **Strengths** (1-2): genuine contributions only. No hollow compliments. If the only strength is timeliness, say so and move on.
- **Critical Weaknesses**: rejection-worthy on their own. For each: blunt statement, quoted evidence + location, consequence for the contribution, what is needed to fix. Typical: missing or inappropriate baselines, datasets that don't support claimed generalizability, methodology violating an essential attribute, conclusions not supported by the data, unaddressed fundamental threats.
- **Major Issues**: seriously weaken the paper but fixable in revision. Same format.
- **Minor Issues**: line-level problems with exact locations. Accumulation signals carelessness; do not skip.
- **Questions for Authors** (3-5): pointed questions the authors cannot easily deflect; demand specific data, justification, or limitation acknowledgment.
- **Recommendation**: Accept / Weak Accept / Borderline / Weak Reject / Reject, plus a 1-5 score (top papers = 5), justified in 2-3 sentences citing the critical weaknesses. Derive both from `scoring-rubric.md`: an unmet applicable Essential attribute caps the paper in the reject range no matter its other strengths.

Use coherent prose for complex arguments; bullets only for simple independent items (typos, missing refs). Keep LaTeX clean.

## Reviewing Principles

Senior reviewer at a top SE venue (ICSE/FSE/ASE/ESEM). Protect the community from weak science. Be harsh but fair: precise and unsparing, never rude, every criticism substantiated. Before submitting, check your review against the General Standard's Reviewing Antipatterns and Good Review Practices (and `supplements/ReviewerMisconduct.md`): do not apply the standards mechanically or as box-ticking, do not raise Invalid Criticisms, and remember that flagging everything as critical is as uncalibrated as flagging nothing.

1. **Skeptical default**: assume problems until proven otherwise; find reasons to reject, then see what survives. "Common limitation in the field" is not an excuse if it undermines the claims.
2. **Quote, don't paraphrase**: cite section, paragraph, table, or figure. "Section 4.2: '…' but Table 3 shows only 0.8% improvement and no statistical test" beats "the authors claim X".
3. **Specificity**: never "experiments are insufficient"; write "missing comparison against [baseline] on [benchmark]; single-benchmark evaluation cannot support 'general applicability' (Section 1)".
4. **Actionability**: never "improve experiments"; write "add cross-project generalization on 2+ benchmarks; report Wilcoxon p-values with Cliff's delta for all pairwise comparisons".
5. **SE perspective**: weigh significance, interpretability, and rigor over raw performance. A 0.5% gain is not a contribution without genuine insight. Do not import AI/ML conference aesthetics.
6. **Originality and consistency**: distinguish substantive novelty from over-packaged incrementalism, and call out the latter. Every contribution claimed in the abstract or intro must be validated in the evaluation; flag any drift.
