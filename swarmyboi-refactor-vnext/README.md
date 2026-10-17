# SwarmyBoi vNext refactor draft

This is a reconstructed/refactored swarm pack for local/work testing.

It intentionally separates **roles**, **procedures**, **capabilities**, **orchestration policy**, and **memory** instead of letting every `.agent.md` file grow into its own miniature constitution.

## What changed conceptually

### Agents are roles

Agent files now answer:

- What kind of judgment does this role own?
- What authority does it have?
- What tools and nested delegation may it use?
- What temperament keeps its failure mode distinct?

They should not duplicate every workflow rule.

### Skills are procedures

Reusable methods moved into skills:

- `request-interpretation`
- `architecture`
- `validation-design`
- `webapp-testing`

This lets several agents share a professional procedure without inventing another persona.

### The playbook is constitutional policy

`swarmyboi-engineering-playbook.md` owns:

- task anchoring;
- epistemic handoff rules;
- delegation graph;
- blocking dependencies;
- rationing/bounded cognition;
- scope control;
- reset behavior;
- review independence;
- completion/reporting rules.

### Tools are power

Tool lists intentionally differ by role.

Notable boundaries:

- Hank has no `edit` or `execute`.
- Daria has `execute` only for non-mutating environment/runtime inspection.
- Beavis/Butthead can edit and run validation.
- Peggy can execute tests and use browser tools, but may not mutate source even indirectly.
- Librarian gets memory, not implementation tools.

## Current cast

| Role | Purpose |
| --- | --- |
| Hank | coordinator / final decision |
| Daria | facts / research |
| Bobby | assumption challenge |
| Beavis | simplicity-first implementation |
| Butthead | robustness-first implementation |
| Gwen | trajectory / scope / stale plan |
| Peggy | technical review / QA |
| Nerd | human-facing reporting |
| Librarian | knowledge / provenance / memory |

**SwarmyBoi remains the system/project name.**

## Important provenance note

The work-computer files were edited after the last full copies available here. This pack incorporates the behavior and changes observed in the conversation, but it cannot contain work-only text that was never uploaded.

Read `notes/MIGRATION.md` before overwriting the work machine.

## Suggested user-level layout

```text
~/.copilot/
  copilot-instructions.md
  swarmyboi-engineering-playbook.md
  agents/
    hank.agent.md
    daria.agent.md
    bobby.agent.md
    beavis.agent.md
    butthead.agent.md
    gwen.agent.md
    peggy.agent.md
    nerd.agent.md
    librarian.agent.md
  skills/
    architecture/
      SKILL.md
    request-interpretation/
      SKILL.md
    validation-design/
      SKILL.md
    webapp-testing/
      SKILL.md
```

Exact supported locations vary by harness. Current Copilot supports personal skills under `~/.copilot/skills/`.

## Static validation

From this pack directory:

```powershell
python .\tests\validate-pack.py
```

The script only checks structural invariants of the pack; it does not invoke VS Code/Copilot.

## Dynamic testing

Use `tests/INTEGRATION_CAMPAIGN.md` against one disposable workspace. It is intentionally an integration run rather than six clean-room fixtures.

## Next experiments

See `notes/CUSTOMIZATION_MAP.md`.

The highest-value likely next steps are:

1. test whether the skills are auto-loaded by the intended roles at sensible times;
2. see whether Beavis/Butthead's different coding philosophies produce meaningfully different solutions;
3. test Librarian session/repository memory behavior;
4. explore tool sets once effective tool names are stable on both machines;
5. explore Local hooks for deterministic telemetry/guardrails without making them part of the portable core.
