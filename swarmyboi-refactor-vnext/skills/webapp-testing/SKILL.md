---
name: webapp-testing
description: Perform focused browser-facing validation of a local web application using VS Code browser tools when UI/runtime behavior matters. Exercise observable acceptance criteria, capture evidence, inspect console/runtime behavior, and respect the caller's mutation authority.
argument-hint: "[user flow or acceptance criteria]"
---

# Web application testing

Use this skill when browser-visible behavior is part of the requested semantics.

The goal is independent observable evidence, not merely source inspection.

## Authority follows the caller

This skill never grants editing authority.

- If the caller is a read-only reviewer such as Peggy, **report defects; do not fix them**.
- If the caller is an authorized lead implementer, fixes may be made only inside the accepted plan/scope, followed by revalidation.
- Do not mutate external/production state merely because browser tools can reach it.

## Procedure

1. Identify the relevant acceptance criteria and user journey.
2. Establish how to start or locate the application without inventing setup steps.
3. Open an agent-controlled isolated browser page when possible.
4. Exercise the smallest flow that directly tests the requested behavior.
5. Check observable page behavior, relevant accessible text/elements, and console/runtime errors.
6. Exercise meaningful edge cases named by the requirement.
7. Capture screenshots only when visual evidence materially helps.
8. Record exact observed results and any unverified areas.

## Evidence discipline

- Browser smoke testing complements automated tests; it does not replace regression coverage when repeatable tests are appropriate.
- Do not claim a workflow was tested if the browser could not actually reach or exercise it.
- Distinguish UI behavior from API/server behavior unless both were observed.
- Do not wander through unrelated screens looking for defects.

## Output

### Flow exercised
### Expected behavior
### Observed behavior
### Console/runtime observations
### Edge cases exercised
### Result — PASS / FAIL / PARTIAL
### Remaining unverified
