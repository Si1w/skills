---
name: commit
description: Use when creating git commits. Enforces the Conventional Commits format below and a review-then-stage procedure.
---

# Commit

## Procedure

1. Run `git status` and `git diff` (plus `git diff --cached`) to review every change before committing.
2. Stage files by name with `git add <file>`. Do not use `git add .` or `git add -A`; never stage secrets, credentials, `.env` files, or large binaries.
3. One logical change per commit. Split unrelated changes into separate commits.
4. Write the message in the format below. Always use this convention, even if the repository's existing history follows a different style.
5. Do not use `--amend` on pushed commits and do not use `--no-verify`.

```
git commit -m "<type>(<optional scope>): <description>" \
  -m "<optional body>" \
  -m "<optional footer>"
```

## Commit Message Formats

### General Commit
```
<type>(<optional scope>): <description>

<optional body>

<optional footer>
```

### Initial Commit
```
chore: init
```

### Merge Commit
```
Merge branch '<branch name>'
```
Follows the default git merge message.

### Revert Commit
```
Revert "<reverted commit subject line>"
```
Follows the default git revert message.

### Types
- Changes relevant to the API or UI:
    - `feat` Commits that add, adjust or remove a feature to/of/from the API or UI
    - `fix` Commits that fix an API or UI bug of a preceding `feat` commit
- `refactor` Commits that rewrite or restructure code without altering API or UI behavior
    - `perf` Commits are a special type of `refactor` commit that specifically improves performance
- `style` Commits that address code style (e.g., white-space, formatting, missing semi-colons) and do not affect application behavior
- `test` Commits that add missing tests or correct existing ones
- `docs` Commits that exclusively affect documentation
- `build` Commits that affect build-related components such as build tools, dependencies, project version, ...
- `ops` Commits that affect operational aspects like infrastructure (IaC), deployment scripts, CI/CD pipelines, backups, monitoring, or recovery procedures, ...
- `chore` Commits that represent tasks like initial commit, modifying `.gitignore`, ...

### Scopes
The `scope` provides additional contextual information.
- The scope is an **optional** part
- Use kebab-case (e.g., `shopping-cart`), typically a module or directory name defined by the project
- **Do not** use issue identifiers as scopes

### Breaking Changes Indicator
- A commit that introduces breaking changes **must** be indicated by an `!` before the `:` in the subject line, e.g. `feat(api)!: remove status endpoint`
- Breaking changes **should** be described in the [footer](#footer) if the [description](#description) is not sufficiently informative

### Description
The `description` contains a concise description of the change.
- The description is a **mandatory** part
- Use the imperative, present tense: "change" not "changed" nor "changes"
  - Think of `This commit will...` or `This commit should...`
- **Do not** capitalize the first letter
- **Do not** end the description with a period (`.`)
- In case of breaking changes also see [breaking changes indicator](#breaking-changes-indicator)

### Body
The `body` should include the motivation for the change and contrast this with previous behavior.
- The body is an **optional** part
- Use the imperative, present tense: "change" not "changed" nor "changes"

### Footer
The `footer` should contain issue references and information about **Breaking Changes**.
- The footer is an **optional** part, except if the commit introduces breaking changes
- *Optionally* reference issue identifiers (e.g., `Closes #123`, `Fixes JIRA-456`)
- **Breaking Changes** **must** start with the words `BREAKING CHANGE:`
  - For a single line description just add a space after `BREAKING CHANGE:`
  - For a multi line description add two new lines after `BREAKING CHANGE:`

### Trailers
- **Do not** add any trailer or signature at the end of the message, such as `Co-Authored-By:`, `Signed-off-by:`, or `Generated with ...`

### Examples
- ```
  feat: add email notifications on new direct messages
  ```
- ```
  feat(shopping-cart): add the amazing button
  ```
- ```
  feat!: remove ticket list endpoint

  refers to JIRA-1337

  BREAKING CHANGE: ticket endpoints no longer supports list all entities.
  ```
- ```
  fix(shopping-cart): prevent order an empty shopping cart
  ```
- ```
  fix(api): fix wrong calculation of request body checksum
  ```
- ```
  fix: add missing parameter to service call

  The error occurred due to <reasons>.
  ```
- ```
  perf: decrease memory footprint for determine unique visitors by using HyperLogLog
  ```
- ```
  build: update dependencies
  ```
- ```
  build(release): bump version to 1.0.0
  ```
- ```
  refactor: implement fibonacci number calculation as recursion
  ```
- ```
  style: remove empty line
  ```
