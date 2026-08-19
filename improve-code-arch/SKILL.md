---
name: improve-code-arch
description: Scan a codebase for deepening opportunities, present the candidates for you to pick one, then grill through it.
disable-model-invocation: true
---

# Improve Codebase Architecture

Surface architectural friction and propose **deepening opportunities**: refactors that turn shallow modules into deep ones. The aim is testability and AI-navigability.

This command is built on a shared design vocabulary: use the architecture vocabulary below exactly in every suggestion; don't drift into "component," "service," "API," or "boundary."

## Vocabulary

- **Module**: any unit with an interface and an implementation — a function, class, package, or process.
- **Interface**: everything a caller must know to use a module: signatures, ordering rules, error contracts, hidden coupling. *The interface is the test surface* — tests should exercise a module only through it.
- **Depth**: the ratio of implementation complexity hidden behind the interface. A **deep** module hides a lot behind a small interface; a **shallow** module's interface is nearly as complex as its implementation.
- **Seam**: a place where the codebase can be separated so the parts vary independently — the natural place for a test double or an alternative implementation.
- **Adapter**: a thin translation layer between a module and something concrete (a vendor API, a framework, a wire format). One adapter marks a *hypothetical* seam; two adapters make it *real*.
- **Leverage**: how much future change a refactor absorbs — high-leverage deepening makes many anticipated changes cheap.
- **Locality**: whether the code you must read to understand a behavior sits in one place. Extracting pure functions for testability *destroys* locality when the real bugs hide in how they're called.
- **Deletion test**: ask "if I deleted this module, would its complexity concentrate somewhere sensible, or just smear elsewhere?" A "yes, concentrates" marks a shallow module worth deepening.

## Process

### 1. Explore

**Scope before you scan: YAGNI.** Deepening a module pays off by making future changes to it easier, so put extra weight on the parts of the codebase that have recently changed. Decide *where* to look before you look:

- If the user named a direction (a module, a subsystem, a pain point), take it, and skip the inference below.
- Otherwise, walk back a good stretch of the commit history (`git log --oneline`) to find the codebase's hot spots, the files and areas that keep coming up, and let those paths pull your attention first. If the changes are scattered with no clear hot spot, widen the net.

Then spawn a sub-agent to walk the codebase. Don't follow rigid heuristics; explore organically and note where you experience friction:

- Where does understanding one concept require bouncing between many small modules?
- Where are modules **shallow**, with an interface nearly as complex as the implementation?
- Where have pure functions been extracted just for testability, but the real bugs hide in how they're called (no **locality**)?
- Where do tightly-coupled modules leak across their seams?
- Which parts of the codebase are untested, or hard to test through their current interface?

Apply the **deletion test** to anything you suspect is shallow: would deleting it concentrate complexity, or just move it? A "yes, concentrates" is the signal you want.

### 2. Present candidates and let the user pick

Keep the strongest candidates — **at most 4** (AskUserQuestion's option limit). If you found more, fold the weaker ones into a short "also noticed, not worth grilling yet" list in the chat summary.

First, write up the candidates in the conversation as markdown. For each candidate:

- **Files**: which files/modules are involved
- **Problem**: why the current architecture is causing friction
- **Solution**: plain English description of what would change
- **Benefits**: explained in terms of locality and leverage, and how tests would improve
- **Before / After**: a compact ASCII or Mermaid sketch, side by side where it fits, illustrating the shallowness and the deepening
- **Recommendation strength**: one of `Strong`, `Worth exploring`, `Speculative`

End with a **Top recommendation**: which candidate you'd tackle first and why.

Then call **AskUserQuestion** with one single-select question ("Which candidate do you want to explore?"):

- Put your top recommendation first, its label suffixed with "(Recommended)".
- `label`: a short name for the candidate (the module/seam involved); `description`: one sentence of problem + strength.
- `preview`: the candidate's before/after ASCII sketch, so the user can compare options side by side.

**Use the codebase's own domain terms for the domain, and the Vocabulary section above for the architecture.** If the code calls it an "Order," talk about "the Order intake module," not "the FooBarHandler."

Do NOT propose interfaces yet — that happens after the user picks.

### 3. Grilling loop

Once the user picks a candidate, walk the decision tree with them through relentless questioning — one question at a time, waiting for the answer before continuing. Cover, in whatever order the conversation demands:

- **Constraints**: what must not change (public contracts, performance budgets, deploy shape, team ownership)?
- **Dependencies**: what does the module pull in today, and which of those belong behind the new seam?
- **Shape of the deepened module**: what is the smallest interface that still hides the messy parts? Name it in the codebase's domain terms.
- **Behind the seam**: what concrete things (vendor APIs, frameworks, storage) sit behind it, and does the seam deserve an adapter yet?
- **Tests**: which existing tests survive unchanged, which move to the new interface, which die?

When the answer to a question is unclear, don't assume — ask and wait.