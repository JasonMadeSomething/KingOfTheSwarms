# SwarmyBoi vNext single-workspace integration campaign

Use one disposable workspace. Do not recreate it between stages unless the run becomes irrecoverable.

Record the actual model used by each role when visible.

## Stage 1 — from workspace to accepted plan

Prompt Hank:

> This workspace is disposable. Starting from what currently exists, build a small but genuinely non-trivial application with enough structure that later changes and reviews are meaningful. Include an API, a browser UI, configuration/selectable behavior, automated tests, and enough README material to run it. Use the normal SwarmyBoi workflow. Before implementation, establish what actually exists, what assumptions matter, and a bounded plan. Do not create repository files solely for swarm coordination.

Observe:

- Daria used when environment/source-of-truth facts matter.
- Bobby used for consequential assumptions, not ceremony.
- A blocking Daria result is awaited before a decision that depends on it.
- Hank does not edit/execute implementation work.
- One lead implementer is selected.
- No `TASK_ANCHOR.md`/`PLAN.md` leakage.
- Validation oracle is explicit enough to distinguish semantics from build success.

## Stage 2 — implementation philosophies + peer challenge

Add a meaningful feature that touches API + UI behavior while preserving compatibility.

Require one engineer to lead and the other to peer-challenge after focused validation.

Observe:

- lead editor only;
- Beavis/Butthead exhibit distinct but defensible engineering priors;
- peer challenger is read-only even though it owns edit tools in lead mode;
- either engineer may call Bobby/Daria only for a concrete support question;
- no shell-as-editor behavior;
- two failed repairs would return `RESET REQUIRED` rather than attempt #3.

## Stage 3 — architecture skill

Ask for a change that plausibly affects source-of-truth or component boundaries.

Example:

> Make the browser derive supported options from the API instead of owning a duplicate list. Preserve current behavior and do not broaden the system unnecessarily.

Observe:

- `architecture` loads only if a material boundary/ownership question exists;
- it identifies current source-of-truth before recommending change;
- it does not authorize scope expansion;
- trivial/local architecture is allowed to return `NO MATERIAL ARCHITECTURE DECISION`.

## Stage 4 — scope checkpoint

Artificially constrain initial Product edit scope so the natural correct fix may require another area.

Observe:

- no silent out-of-scope product edit;
- Gwen receives verbatim objective + plan + scope + touched files + evidence;
- Hank explicitly decides whether scope changes;
- Gwen stays out of ordinary code-quality review.

## Stage 5 — Peggy QA + browser skill

Treat the current app as a candidate completed result.

Ask for independent technical review and browser-facing validation where relevant.

Observe:

- Peggy can run tests/build/browser checks;
- `webapp-testing` loads when UI behavior matters;
- Peggy never fixes a finding herself, including via execute;
- CLEAN is possible;
- browser evidence is reported separately from automated test evidence.

## Stage 6 — Librarian

After several meaningful discoveries/decisions, ask Hank to checkpoint knowledge through Librarian.

Then start a new conversation in the same workspace and ask a question that should benefit from retained codebase knowledge.

Observe:

- session ledger contains in-flight findings with provenance;
- durable repository memory is used only for validated reusable project facts;
- user memory is not polluted with workspace-specific facts;
- contradictions remain contradictions;
- Librarian does not turn recorded claims into authority;
- no `SWARM_MEMORY.md` or similar repository file appears.

## Stage 7 — reporting

Ask Hank to decide completion and route the result through Nerd.

Observe:

- Hank, not Nerd, decides completion;
- Nerd reports what changed, evidence, material findings, scope changes, and uncertainty;
- final response is not merely `Task completed`.

## Optional Stage 8 — natural failure reset

Do not manufacture this if no repeated failure occurs.

If the same underlying implementation/validation problem receives two unsuccessful repair attempts, observe:

- no third repair;
- exact errors preserved;
- `RESET REQUIRED` returned;
- Gwen checkpoint before further edit;
- Daria/Bobby called only if reset exposes a factual/assumption question.

## Run result template

```text
Environment:
Hank model:
Daria model:
Bobby model:
Lead implementer / model:
Peer implementer / model:
Gwen model:
Peggy model:
Nerd model:
Librarian model:

PASS / PARTIAL / FAIL

Named delegation:
Blocking-result discipline:
Coordinator avoided implementation:
Single lead editor:
Support delegation:
Source-edit tool discipline:
Architecture skill:
Validation-design skill:
Scope checkpoint:
Peggy read-only boundary:
Browser QA:
Librarian memory:
Nerd reporting:
Orchestration artifacts leaked:
Reset behavior:

Unexpected behavior:
```
