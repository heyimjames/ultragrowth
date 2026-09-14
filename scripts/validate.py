#!/usr/bin/env python3
"""Check the skills are well formed before they go anywhere.

Every claim in this repo is a number somebody might act on, so the thing
worth checking mechanically is that the numbers carry sources and the
frontmatter is the shape the tools expect.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
fails: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        fails.append(msg)


for skill in sorted(SKILLS.iterdir()):
    if not skill.is_dir():
        continue
    md = skill / "SKILL.md"
    check(md.exists(), f"{skill.name}: no SKILL.md")
    if not md.exists():
        continue
    text = md.read_text()

    # Frontmatter, which is how every tool finds the thing.
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    check(fm is not None, f"{skill.name}: no frontmatter")
    if fm:
        body = fm.group(1)
        check("name:" in body, f"{skill.name}: frontmatter has no name")
        check("description:" in body, f"{skill.name}: frontmatter has no description")
        name = re.search(r"name:\s*(\S+)", body)
        check(name and name.group(1) == skill.name,
              f"{skill.name}: frontmatter name does not match the directory")
        desc = re.search(r"description:\s*(.+)", body)
        check(desc and len(desc.group(1)) > 60,
              f"{skill.name}: description is too short to route on")

    # Every reference the skill points at has to exist. A table of
    # contents pointing at nothing is worse than no table of contents.
    for ref in re.findall(r"`references/([a-z0-9-]+\.md)`", text):
        check((skill / "references" / ref).exists(),
              f"{skill.name}: references/{ref} is named but missing")

    check("## SOURCES" in text or "## Sources" in text,
          f"{skill.name}: no sources section, and this skill is all numbers")

    # Em dashes, which James does not use.
    for f in [md, *sorted((skill / "references").glob("*.md"))]:
        if "—" in f.read_text():
            fails.append(f"{f.relative_to(ROOT)}: contains an em dash")

if fails:
    print("FAILED")
    for f in fails:
        print("  " + f)
    sys.exit(1)

n = sum(1 for s in SKILLS.iterdir() if s.is_dir())
refs = len(list(SKILLS.glob("*/references/*.md")))
print(f"ok: {n} skill(s), {refs} reference file(s)")
