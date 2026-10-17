from __future__ import annotations

import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "agents"
SKILLS = ROOT / "skills"

EXPECTED_AGENTS = {
    "Hank", "Daria", "Bobby", "Beavis", "Butthead", "Gwen", "Peggy", "Nerd", "Librarian"
}
LEGACY_NAMES = {"Mr.CC", "FunKiller"}


def frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise AssertionError(f"{path}: unterminated YAML frontmatter")
    data: dict[str, object] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        key, sep, value = raw.partition(":")
        if not sep:
            continue
        value = value.strip()
        if value in {"true", "false"}:
            parsed: object = value == "true"
        elif value.startswith("["):
            parsed = ast.literal_eval(value)
        else:
            parsed = value.strip("'\"")
        data[key.strip()] = parsed
    return data


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    agent_files = sorted(AGENTS.glob("*.agent.md"))
    names: dict[str, tuple[Path, dict[str, object]]] = {}
    for path in agent_files:
        fm = frontmatter(path)
        name = fm.get("name")
        require(isinstance(name, str) and bool(name), f"{path.name}: missing name", errors)
        if isinstance(name, str):
            require(name not in names, f"duplicate agent name: {name}", errors)
            names[name] = (path, fm)
        require("model" in fm, f"{path.name}: model tag missing", errors)
        require("tools" in fm, f"{path.name}: tools missing", errors)
        require("swarmyboi-engineering-playbook.md" in path.read_text(encoding="utf-8"),
                f"{path.name}: does not reference canonical playbook", errors)

    require(set(names) == EXPECTED_AGENTS,
            f"agent set mismatch: expected {sorted(EXPECTED_AGENTS)}, got {sorted(names)}", errors)

    if "Hank" in names:
        tools = set(names["Hank"][1].get("tools", []))
        require("edit" not in tools and "execute" not in tools,
                "Hank must not have edit/execute", errors)

    if "Peggy" in names:
        tools = set(names["Peggy"][1].get("tools", []))
        require("edit" not in tools, "Peggy must not have edit", errors)
        require("browser" in tools, "Peggy should have browser tool set", errors)

    if "Gwen" in names:
        tools = set(names["Gwen"][1].get("tools", []))
        require("edit" not in tools and "execute" not in tools,
                "Gwen must remain mechanically read-only", errors)

    if "Bobby" in names:
        require(names["Bobby"][1].get("agents") == ["Daria"],
                "Bobby may delegate only to Daria", errors)

    for engineer in ("Beavis", "Butthead"):
        if engineer in names:
            require(set(names[engineer][1].get("agents", [])) == {"Bobby", "Daria"},
                    f"{engineer} may delegate only to Bobby/Daria", errors)

    for name, (path, _fm) in names.items():
        text = path.read_text(encoding="utf-8")
        for legacy in LEGACY_NAMES:
            require(legacy not in text, f"{path.name}: contains legacy role name {legacy}", errors)

    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        skill = skill_dir / "SKILL.md"
        require(skill.exists(), f"{skill_dir.name}: missing SKILL.md", errors)
        if skill.exists():
            fm = frontmatter(skill)
            require(fm.get("name") == skill_dir.name,
                    f"{skill}: skill name must match parent directory", errors)
            require(bool(fm.get("description")), f"{skill}: description missing", errors)

    playbook = (ROOT / "swarmyboi-engineering-playbook.md").read_text(encoding="utf-8")
    for legacy in LEGACY_NAMES:
        require(legacy not in playbook, f"playbook contains legacy role name {legacy}", errors)

    if errors:
        print("FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    print("PASS")
    print(f"- {len(agent_files)} agents")
    print(f"- {len([p for p in SKILLS.iterdir() if p.is_dir()])} skills")
    print("- coordinator/reviewer/delegation invariants satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
