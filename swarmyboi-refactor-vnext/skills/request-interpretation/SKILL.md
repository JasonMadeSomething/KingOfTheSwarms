---
name: request-interpretation
description: Losslessly decompose a conversational, multi-message, ambiguous, or example-heavy user request into a derived engineering interpretation while preserving the user's exact wording as the authoritative raw channel. Use when examples, preferences, qualifiers, or implied context could otherwise be mistaken for hard requirements.
argument-hint: "[request or task context]"
user-invocable: false
---

# Request interpretation

This skill helps the caller understand the user's request without replacing it.

Maintain two channels:

## RAW

Preserve the exact user wording that defines the objective and material constraints. Do not rewrite it into cleaner engineering language and then discard the original.

## DERIVED

Extract only what is useful for planning:

- **Requested outcome**
- **Hard constraints** — explicit must/must-not requirements
- **Soft preferences** — desired but negotiable choices
- **Examples / illustrations** — examples are not automatically requirements
- **Relevant context** — only context materially needed for this task
- **Assumptions required to proceed**
- **Ambiguities that could change the result**
- **Things not to infer** — likely overreads the agents should avoid

## Rules

- Derived interpretation supplements RAW; it never replaces it.
- If RAW and DERIVED conflict, RAW wins.
- Anything not explicit must remain labeled as inference, assumption, or unresolved.
- Do not "improve" requirements, invent acceptance criteria, silently broaden scope, or convert preferences/examples into hard constraints.
- Preserve qualifiers such as "probably", "mostly", "if needed", and "don't make this a giant thing" when they materially affect how strongly a requirement should be treated.
- Ask the human only when an ambiguity materially blocks safe progress and cannot be resolved from available evidence.

## Output

### RAW
> Exact relevant request text

### DERIVED
- Requested outcome:
- Hard constraints:
- Soft preferences:
- Examples / non-binding illustrations:
- Assumptions:
- Ambiguities:
- Do not infer:
