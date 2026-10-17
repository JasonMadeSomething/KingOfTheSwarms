---
name: architecture
description: Analyze system shape when a change materially affects boundaries, source-of-truth, ownership, contracts, dependency direction, lifecycle, persistence, deployment shape, or cross-cutting behavior. Prefer the smallest coherent design that fits the existing repository and accepted scope.
argument-hint: "[task or architectural question]"
---

# Architecture

Use this skill to reason about system shape, not to create an approval board.

## Use when

- source-of-truth or state ownership is changing;
- API/interface contracts may change;
- a change crosses components/layers/processes;
- lifecycle, persistence, synchronization, deployment, or failure propagation matters;
- a new abstraction is being considered;
- an implementation disagreement is actually about system structure.

Do not use this skill merely because the task involves code.

## Procedure

1. **Architectural pressure** — state the structural issue created or exposed by the request.
2. **Current shape** — inspect enough code/context to establish relevant owners, boundaries, contracts, dependencies, and lifecycle.
3. **Pressure points** — identify duplicate sources of truth, ownership changes, coupling, contract changes, lifecycle mismatches, or new failure propagation.
4. **Viable shapes** — only when there is more than one genuinely meaningful option, compare a small number by complexity, ownership clarity, coupling, compatibility, testability, operational impact, and fit with the repository.
5. **Recommendation** — prefer the smallest coherent direction supported by evidence.
6. **Keep unchanged** — name boundaries/contracts that should not move.
7. **Uncertainty** — route factual unknowns to Daria and hidden-premise questions to Bobby.
8. **Validation** — state what observation would show that the architectural intent was actually realized.

## Principles

- Existing architecture is evidence. Do not impose generic best practices that ignore the repository.
- Smallest does not mean fewest lines; coherence and clear ownership matter.
- Do not turn possible future needs into current requirements.
- Do not authorize scope expansion. Return required expansion to Hank.
- Distinguish established facts, inference, assumptions, and unresolved questions when relevant.
- A skill recommendation does not override the caller's role or authority.

## Output

### Architectural pressure
### Current shape
### Viable directions
### Recommendation
### Keep unchanged
### Assumptions / unresolved
### Validation

If no material architecture decision exists, return:

`NO MATERIAL ARCHITECTURE DECISION — this change fits the existing structure without altering ownership, boundaries, contracts, or lifecycle.`
