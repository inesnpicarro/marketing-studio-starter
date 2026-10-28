"""Bundle every skill into one Markdown file, for AI tools that don't read skill folders.

Usage:
    python tools/build_single_file.py

Writes dist/marketing-studio.md. Upload it as a knowledge file (a ChatGPT custom GPT or
project, a Copilot instructions file, any assistant that accepts a document of instructions).
Run it again after editing house-rules so the bundle carries your rules.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
OUT = ROOT / "dist" / "marketing-studio.md"

# house-rules and start first; the rest in the order a piece of work meets them.
ORDER = [
    "house-rules", "start", "build-knowledge-base", "brand-system", "find-assets",
    "campaign-concept", "sme-interview", "meeting-source", "personas", "write-copy",
    "tailor", "brand-check", "timeline", "review-and-handoff", "project-setup",
]

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)

HEADER = """# Marketing Studio — single-file edition

You are a marketing content studio. The sections below are your skills. Each one starts with
when to use it. Always begin with **start** unless the person names a specific skill, and
always read **house-rules** before writing or checking anything.

Wherever a section says "the X skill", it means the section headed X in this file.

"""


def section(name: str) -> str:
    text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    description = ""
    if match:
        desc = re.search(r"^description:\s*(.+)$", match.group(1), re.M)
        description = desc.group(1).strip() if desc else ""
        text = text[match.end():]
    text = re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)  # owner comments
    text = re.sub(r"^(#+) ", lambda m: "#" + m.group(1) + " ", text, flags=re.M)  # demote headings
    return f"---\n\n# Skill: {name}\n\n**Use when:** {description}\n\n{text.strip()}\n"


def main() -> None:
    names = ORDER + sorted(p.name for p in SKILLS.iterdir() if p.is_dir() and p.name not in ORDER)
    body = HEADER + "\n".join(section(n) for n in names if (SKILLS / n / "SKILL.md").exists())
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(body, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} - {len(names)} skills, {len(body):,} characters")


if __name__ == "__main__":
    main()
