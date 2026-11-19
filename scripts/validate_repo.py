#!/usr/bin/env python3
"""Lightweight repo validation for ai-from-zero CI."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    "ai-sources",
    "ai-for-my-job",
    "prompt-coach",
    "setup-doctor",
    "first-build",
    "skill-maker",
]
BANNED = ["元宝", "CodeBuddy"]
# Whitelist path spelling for WorkBuddy project skills directory.
WHITELIST_PATTERNS = [
    re.compile(r"\.codebuddy/"),
]


def strip_whitelisted(text: str) -> str:
    out = text
    for pat in WHITELIST_PATTERNS:
        out = pat.sub("", out)
    return out


def fail(msg: str) -> None:
    print(f"❌ {msg}")
    raise SystemExit(1)


def warn(msg: str) -> None:
    print(f"⚠️  {msg}")


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        fail(f"{path}: must start with YAML frontmatter")
    parts = content.split("---", 2)
    if len(parts) < 3:
        fail(f"{path}: invalid frontmatter")
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        fail(f"{path}: YAML error: {exc}")
    if not isinstance(data, dict):
        fail(f"{path}: frontmatter must be a mapping")
    return data, content


def validate_skill(name: str) -> None:
    skill_dir = ROOT / name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"missing {skill_md}")

    fm, content = parse_frontmatter(skill_md)
    if fm.get("name") != name:
        fail(f"{skill_md}: name '{fm.get('name')}' must equal folder '{name}'")
    if "description" not in fm:
        fail(f"{skill_md}: missing description")
    desc = fm["description"]
    if not isinstance(desc, str) or not desc.strip():
        fail(f"{skill_md}: description must be a non-empty string")
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name):
        fail(f"{name}: folder/name must be kebab-case")
    if len(desc) > 1024:
        fail(f"{skill_md}: description length {len(desc)} exceeds 1024")
    if len(desc) > 500:
        warn(f"{skill_md}: description length {len(desc)} > 500 (recommended)")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        fail(f"missing {openai_yaml}")
    try:
        cfg = yaml.safe_load(openai_yaml.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"{openai_yaml}: YAML error: {exc}")
    interface = (cfg or {}).get("interface")
    if not isinstance(interface, dict):
        fail(f"{openai_yaml}: missing interface")
    for key in ("display_name", "short_description", "default_prompt"):
        if key not in interface or not str(interface[key]).strip():
            fail(f"{openai_yaml}: missing interface.{key}")

    examples = skill_dir / "examples"
    if examples.exists():
        for path in sorted(examples.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".html", ".txt"}:
                text = path.read_text(encoding="utf-8", errors="ignore")
                if "虚构示例" not in text:
                    fail(f"{path}: examples must contain「虚构示例」")

    triggers = ROOT / "tests" / "triggers" / f"{name}.md"
    if not triggers.exists():
        fail(f"missing trigger list {triggers}")
    ttext = triggers.read_text(encoding="utf-8")
    should = len(re.findall(r"(?m)^\|?\s*\d+\s*\|[^|]*应该触发|^\|\s*\d+\s*\|", ttext))
    # Prefer explicit markers
    should_n = len(re.findall(r"(?m)^-\s*\[should\]\s+", ttext))
    should_not_n = len(re.findall(r"(?m)^-\s*\[should-not\]\s+", ttext))
    if should_n != 10 or should_not_n != 10:
        fail(
            f"{triggers}: need exactly 10 [should] and 10 [should-not] lines "
            f"(found {should_n}/{should_not_n})"
        )

    print(f"✅ {name}")


def validate_banned_words() -> None:
    bad: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "dist", "node_modules", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".yml", ".yaml", ".sh", ".py", ".html", ".txt"}:
            continue
        # Allow this validator and CI workflow to mention the ban list itself.
        if path.name in {"validate_repo.py", "ci.yml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        check = strip_whitelisted(text)
        for word in BANNED:
            if word in check:
                bad.append(f"{path.relative_to(ROOT)}: contains banned word「{word}」")
    if bad:
        fail("banned-word check failed:\n  - " + "\n  - ".join(bad))
    print("✅ banned-word check (whitelist: .codebuddy/)")


def validate_setup_doctor_errors() -> None:
    errors_dir = ROOT / "setup-doctor" / "errors"
    if not errors_dir.exists():
        fail("missing setup-doctor/errors")
    files = sorted(errors_dir.glob("*.md"))
    if len(files) < 20:
        fail(f"setup-doctor/errors needs >= 20 entries, found {len(files)}")
    for path in files:
        text = path.read_text(encoding="utf-8")
        if "出处" not in text:
            fail(f"{path}: missing「出处」field")
        # Require a non-empty 出处 value on a dedicated line or table cell.
        m = re.search(r"(?m)^(?:-\s*)?\*{0,2}出处\*{0,2}\s*[:：]\s*(\S.+)$", text)
        m2 = re.search(r"(?m)^\|\s*出处\s*\|\s*(\S.+?)\s*\|", text)
        value = (m.group(1).strip() if m else "") or (m2.group(1).strip() if m2 else "")
        if not value or value in {"待核实", "TBD", "-", "无"}:
            fail(f"{path}: 出处 must be non-empty official source (not 待核实)")
    print(f"✅ setup-doctor errors ({len(files)} files with 出处)")


def main() -> None:
    print("Validating ai-from-zero …")
    for name in SKILLS:
        validate_skill(name)
    validate_banned_words()
    validate_setup_doctor_errors()
    print("All checks passed.")


if __name__ == "__main__":
    main()
