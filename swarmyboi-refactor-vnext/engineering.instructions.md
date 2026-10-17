# SwarmyBoi baseline engineering instructions

Optimize for correctness, semantic understanding, and engineer time before token thrift.

These rules are general engineering constraints. Role-specific behavior belongs in agent files; repeatable procedures belong in skills; orchestration belongs in the SwarmyBoi playbook.

- Read known relevant files directly before broad search. Use search for discovery, references, usages, generated artifacts, and genuinely unknown locations.
- Prefer actual source, configuration, runtime output, tests, and authoritative documentation over inference from names.
- Distinguish established facts, inferences, assumptions, and unresolved claims when the distinction matters. Confidence must not increase merely because information was summarized or handed off.
- A file, service, setting, error, or artifact mentioned in a prompt, log, prior environment, or another agent's report is not automatically present in the current workspace. "Not found here" means only that it was not found in the searched location.
- Preserve user work. Inspect existing changes before broad edits and avoid unrelated cleanup.
- Prefer the smallest coherent change that satisfies the requested behavior and fits nearby repository patterns.
- Treat errors as evidence. Diagnose before patching. Two unsuccessful repairs against the same underlying problem require a reset rather than a third opportunistic patch.
- Use dedicated edit tools for ordinary source/configuration/test/documentation changes. `execute` or shell commands are not fallback editing mechanisms.
- A role that is read-only remains read-only even if it has `execute`: it must not mutate source indirectly through PowerShell, shell redirection, inline scripts, formatters, generators, or similar mechanisms.
- Internal coordination state is not a repository artifact. Do not create `TASK_ANCHOR.md`, `PLAN.md`, `SWARM_MEMORY.md`, review notes, or similar files merely to coordinate agents unless the user explicitly requests them or the repository defines that convention.
- Validate semantics, not merely compilation or disappearance of an error. Use the strongest practical evidence available.
- Keep trivial work trivial. Do not invoke specialists or workflows merely because they exist.

When Hank is selected, follow `swarmyboi-engineering-playbook.md` for orchestration and role boundaries.
