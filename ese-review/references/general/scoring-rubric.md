# Quality Assessment from Empirical Standards Attributes

The ACM SIGSOFT Empirical Standards define no numeric rubric. A paper is judged by attribute satisfaction, gated on trustworthiness. From the General Standard ("Good Review Practices"): "A paper that is trustworthy can be accepted even if it is not important. A paper that is not trustworthy cannot be accepted, even if it seems important."

This file turns that official logic into a recommendation and an optional 1-5 score. It is lexicographic, not a weighted average: Essential attributes are a hard gate; Desirable and Extraordinary only differentiate quality among papers that already clear the gate. Two rules from the standards constrain its use:
- Assess only against attributes appropriate to the paper's method (the matched specific standard plus the General Standard). "There are no universal quality criteria." Never score against non-applicable attributes.
- A single composite number applied rigidly is itself a Reviewing Antipattern ("mechanical, box-ticking or gotcha-like"). Use the score to communicate the verdict, not to mechanically decide it, and never let Desirable count offset an unmet Essential attribute.

## Step 1: Trustworthiness gate (Essential attributes)

Evaluate the applicable Essential attributes only.
- If every applicable Essential attribute is met, the paper is trustworthy and clears the gate. Go to Step 2.
- If any applicable Essential attribute is unmet, the paper is not trustworthy and stays in the reject range, no matter how many Desirable or Extraordinary attributes it satisfies:
  - the gap is fundamental or not fixable in revision: Reject (score 1).
  - the gap is narrow and fixable in revision: Weak Reject (score 2).

## Step 2: Quality and priority (Desirable + Extraordinary)

For papers that clear the Essential gate:
- few Desirable attributes met, no critical weaknesses: Borderline (score 3).
- most Desirable attributes met: Weak Accept (score 4).
- most Desirable met plus at least one Extraordinary attribute or clear significance: Accept (score 5).

## Mapping summary

| Applicable Essential | Desirable / Extraordinary | Recommendation | Score |
|----------------------|---------------------------|----------------|-------|
| any unmet, fundamental | (not reached) | Reject | 1 |
| any unmet, fixable | (not reached) | Weak Reject | 2 |
| all met | few Desirable | Borderline | 3 |
| all met | most Desirable | Weak Accept | 4 |
| all met | most Desirable + Extraordinary or significance | Accept | 5 |

## Guardrails (from the General Standard)

Honor the Invalid Criticisms and Reviewing Antipatterns when applying the gate. Do not reject for arbitrary minimum sample sizes, for negative or null results, for being a replication, or by cross-paradigmatic criticism (judging qualitative work by quantitative criteria or vice versa). Trustworthiness, not fashionable topic or polished writing, drives the score.
