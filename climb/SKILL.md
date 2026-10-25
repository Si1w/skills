---
name: climb
description: Map project files and their relationships when asked for comprehensive project exploration or task-focused file discovery.
---

# Climb

Produce an evidence-backed map of the current project's relevant files so the user can understand how the project works or where a task belongs.

## Scope

Use the active project and conversation to determine the scope. Without a specific question, cover the major components, entry points, and workflows. With a specific question, trace the relevant files and cross-component dependencies. A focused lookup does not require a whole-project map.

Exploration alone produces findings. When it supports an already requested change, carry those findings into the remaining work.

## Coverage

Choose searches and reading depth to fit the project. Comprehensive coverage means accounting for relevant components and relationships, not reading every file. Documentation and manifests are useful where they resolve project structure or task-specific questions.

Follow relationships beyond keyword matches: callers and consumers can reveal dependencies that filenames miss. Include configuration, tests, and documentation where they explain or constrain the behavior. In research projects, relevant chains may connect experiment settings, analysis scripts, figures, and manuscripts.

Account for search blind spots when they affect the result, particularly hidden configuration, ignore rules, generated inputs, and unavailable submodules. Inspect those locations selectively. Distinguish files actually read from candidates merely located, and confirmed relationships from inferred ones.

Continue until the main components or relevant dependency chain are accounted for and material open leads are resolved or identified as gaps. Further searching is useful when it could change the answer; repeated scans are not a completion requirement.

## Result

Give a navigable explanation of the findings, with file links and line references supporting specific claims. Highlight responsibilities, important relationships, and the best starting points for the user's task. Surface documentation conflicts or coverage gaps that affect the conclusion.

Choose a concise structure appropriate to the findings rather than listing every discovered file. Return the map in the conversation unless a saved artifact is requested or belongs to the established workflow.
