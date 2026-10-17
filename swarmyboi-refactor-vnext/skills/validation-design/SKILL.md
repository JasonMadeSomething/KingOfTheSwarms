---
name: validation-design
description: Design a falsifiable validation oracle for an engineering change. Use when success could be confused with compilation, an error disappearing, a mock passing, or self-reported completion, or when preservation/compatibility behavior needs explicit evidence.
argument-hint: "[requested behavior and current plan]"
---

# Validation design

Define what observation distinguishes **the requested behavior is correct** from **the current failure merely stopped appearing**.

## Procedure

1. State the exact behavior/invariant that needs evidence.
2. Identify the strongest practical oracle already available.
3. If preservation matters, identify what should be characterized before editing.
4. Choose the narrowest experiment that can falsify an incorrect implementation.
5. Separate primary semantic evidence from supporting checks.
6. State what remains unverified even if the proposed checks pass.

## Evidence ladder

Prefer, when practical:

1. existing focused tests that directly cover the behavior;
2. new focused tests in an appropriate existing harness;
3. characterization tests for undocumented behavior that must be preserved;
4. temporary/local fixtures, sandboxes, fake dependencies, or controlled environments;
5. golden/snapshot/generated-output/before-after comparisons when artifacts are the behavior;
6. browser/runtime interaction for user-visible behavior;
7. compile/typecheck/lint/schema/static analysis as supporting evidence;
8. documented manual verification when stronger automation is impractical.

Compilation alone does not establish semantics.

A test that restates the implementation without distinguishing a wrong result is weak evidence.

## Validation artifacts

When proposing a new validation artifact, classify it:

- **temporary** — disposable local evidence;
- **persistent** — a legitimate ongoing test/fixture that belongs in the repository.

Do not silently expand product scope just to create validation machinery.

## Output

### Behavior to prove
### Primary oracle
### Supporting checks
### Pre-change characterization, if needed
### Validation artifact plan
### Failure observation that would falsify the implementation
### Remaining uncertainty
