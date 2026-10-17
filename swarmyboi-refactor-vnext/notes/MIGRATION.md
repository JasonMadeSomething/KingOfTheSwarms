# Migration notes

## Important limitation

This vNext pack is reconstructed from:

- the latest agent/playbook copies available in the ChatGPT file library;
- the model arrays that were present in those latest copies;
- the work-computer behavior observed in the current conversation;
- the design decisions made after those files were uploaded.

It is **not guaranteed to contain work-computer-only edits that were never uploaded back here**.

Do not blindly overwrite the work machine if those files contain additional changes you want to preserve. Diff the work copies against this pack first.

## Rename map

- SwarmyBoi agent -> Hank
- Mr.CC -> Gwen
- FunKiller -> Peggy
- SwarmyBoi remains the project/system name

Daria, Bobby, Beavis, Butthead, Nerd remain.

Librarian is new.

## Major behavioral changes incorporated

- Hank has no edit or execute privilege.
- Daria gains tightly constrained non-mutating execute for runtime/environment evidence.
- Beavis/Butthead may invoke Bobby or Daria for bounded epistemic support.
- Bobby may invoke Daria for a narrow factual question exposed by assumption analysis.
- Beavis/Butthead have intentionally different coding philosophies.
- `execute` is explicitly forbidden as a fallback source editor.
- Two failed repairs force `RESET REQUIRED` before a third attempt.
- Blocking specialist results must return before dependent planning decisions.
- Product edit scope is separated from permitted validation artifacts.
- Internal coordination files are forbidden unless explicitly requested.
- Peggy is strictly read-only even through execute and gains browser capability for QA.
- Librarian is added with conservative memory ownership.
- Bounded cognition/rationing is policy rather than an Accountant persona.
- Architecture, request interpretation, validation design, and browser testing move into skills.

## Suggested merge order

1. Save/copy the current work-machine agent files somewhere safe.
2. Diff the three renamed roles first (SwarmyBoi/Mr.CC/FunKiller -> Hank/Gwen/Peggy).
3. Merge Beavis/Butthead/Bobby changes next because their delegation/tool rules changed materially.
4. Add Librarian.
5. Replace/refactor the playbook.
6. Add skills under the supported personal skill path.
7. Run the static validator in `tests/`.
8. Run the integration campaign against a disposable workspace.

## Personal skill location

For current VS Code Copilot, personal skills can live under:

`~/.copilot/skills/<skill-name>/SKILL.md`

Keep the parent directory name identical to the skill `name` field.
