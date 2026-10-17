# SwarmyBoi customization map

The refactor treats VS Code's customization mechanisms as separate architectural layers instead of making every concern another agent prompt.

## 1. Instructions — always-on invariants

Use for rules that should apply regardless of role:

- epistemic discipline;
- preserve user work;
- no shell-as-editor when a dedicated edit tool exists;
- read-only means no indirect mutation;
- orchestration state is not product output.

File: `copilot-instructions.md`

## 2. Custom agents — cognitive roles and authority

Use an agent when the system needs a recurring **kind of judgment**, a distinctive authority boundary, or a restricted tool/delegation surface.

Current cast:

- Hank — executive synthesis / decisions
- Daria — facts
- Bobby — assumptions
- Beavis — simplicity-first implementation
- Butthead — robustness-first implementation
- Gwen — trajectory / scope
- Peggy — technical review / QA
- Nerd — human reporting
- Librarian — knowledge/provenance

Avoid adding agents for procedures that can be skills.

## 3. Skills — learned procedures

Use skills when multiple roles may need the same professional method without creating another persona.

Current skills:

- `request-interpretation`
- `architecture`
- `validation-design`
- `webapp-testing`

Good future candidates if repeated behavior justifies them:

- root-cause-debugging
- API-contract-review
- generated-artifact-tracing
- migration-parity-analysis
- incident-triage
- deployment-validation

Do not create these preemptively. Promote repeated, useful workflows into skills after observing them.

## 4. Tools — concrete power

A role's tools should express what it is physically capable of doing.

Examples:

- Hank has delegation/context tools but no edit/execute.
- Daria has non-mutating execute because environment/runtime facts sometimes require commands.
- Implementers have edit + execute.
- Peggy has execute + browser but no edit and is semantically read-only.
- Librarian has memory but no engineering mutation tools.

Tool availability varies by harness; unavailable tools may be ignored. Review the effective tool list in the target environment.

## 5. Tool sets — reusable capability bundles

Worth exploring once the individual tool lists stabilize.

Potential bundles:

- `swarm-reader`
- `swarm-research`
- `swarm-implementer`
- `swarm-review-browser`

This would reduce repeated tool lists and make capability review easier. Do not introduce it until exact tool names are confirmed on both home and work harnesses.

## 6. Memory — emerging knowledge, not shared law

Librarian is the natural owner of memory use.

- session memory: in-flight ledger;
- repository memory: validated codebase facts that should survive conversations but are not yet shared project rules;
- user memory: only truly cross-workspace personal preferences.

Stable team rules belong in source-controlled documentation/customizations, not memory.

## 7. Hooks — deterministic enforcement

Hooks are interesting for rules that should not depend on model obedience:

- log subagent start/stop for acceptance tests;
- reject suspicious shell-based source rewriting by read-only roles;
- capture touched-file lists after edits;
- run a static validation command after certain lifecycle events.

Important: current VS Code agent-scoped hooks are a Local-harness feature. Treat hooks as a local/testing enhancement rather than the portable core until work-harness support is verified.

## 8. MCP / extension tools — external capability

Use only when SwarmyBoi needs a capability VS Code does not already expose:

- observability queries;
- CMDB/service metadata;
- internal deployment state;
- issue trackers;
- databases/APIs.

MCP is not needed just to make agents talk to each other.

## 9. Plugins — packaging

Once the system stabilizes, a plugin is a plausible distribution unit for related agents, skills, hooks, and MCP configuration.

Do not package instability yet.

## Heuristic

When adding something new, ask:

- Is this **who should think?** -> agent
- Is this **how to perform a recurring procedure?** -> skill
- Is this **what power is available?** -> tool/tool set/MCP
- Is this **a rule everyone must obey?** -> instructions/playbook
- Is this **what we learned?** -> Librarian/memory
- Is this **an action that must happen deterministically?** -> hook
