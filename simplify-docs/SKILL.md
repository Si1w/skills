---
name: simplify-docs
description: Simplify existing documentation, including README files, guides, AGENTS.md, and SKILL.md, when asked to reduce redundancy or unnecessary instructions while preserving meaning.
---

# Simplify Docs

Make the requested documents easier to use and maintain without losing information readers need. Edit the specified files unless the user asks only for an audit or suggestions. Preserve the intended audience, language, and scope; do not turn a simplification request into a repository-wide rewrite.

## Decide what earns its place

Read the target documents and consult related material only where needed to resolve meaning, dependencies, or factual uncertainty. Keep content that changes a reader's decision, explains a non-obvious constraint, or enables a necessary action.

Remove repetition, filler, empty sections, and examples that add no distinct information. Merge overlapping explanations and make wording direct. Delete obsolete guidance only when the available evidence establishes that it is obsolete; flag unresolved contradictions instead of guessing. Do not pursue a word-count reduction at the expense of usefulness. Leave already concise material alone.

For human-facing documentation, retain the context and examples its audience needs. An expert's familiarity is not evidence that a beginner's explanation is redundant. Preserve technical facts, prerequisites, command semantics, qualifications, citations, and required warnings. Keep normative distinctions such as "must" versus "may" intact.

## When simplifying agent instructions

For `AGENTS.md`, `SKILL.md`, and reusable prompts:

- Keep skill descriptions concise and specific to their activation conditions. Avoid broad keyword triggers that pull unrelated tasks into the workflow.
- Retain project-specific knowledge and real operational constraints. Remove generic coaching that adds no useful decision guidance.
- Prefer an outcome and completion criteria over a rigid itinerary where several approaches are valid. Preserve exact sequences when order matters for correctness.
- Make reference-reading conditional on the task. Split substantial, independently useful guidance into linked references only when that reduces irrelevant reading; do not fragment a short document.
- Distinguish actual authorization boundaries from unnecessary repeated confirmation. Do not weaken explicit restrictions or invent permission because a model is more capable.

## Finish the edit

Review the diff for lost meaning and accidental scope changes. If headings or files move, check affected links and references; preserve required metadata and machine-consumed structure. Use relevant documentation checks when available. Do not execute documented commands merely to validate prose, particularly commands with external effects.

Finish when the requested scope is simplified and relevant checks are complete, or explain a concrete blocker. Briefly report what changed, what was verified, and any unresolved factual questions. For an audit-only request, provide findings and proposed edits without changing files.
