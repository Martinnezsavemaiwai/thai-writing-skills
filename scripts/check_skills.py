"""Repo checks for the Thai writing skills. Run: python scripts/check_skills.py"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CLAUDE = ROOT / ".claude/skills"
CODEX = ROOT / ".codex/skills"
NO_DASH_SKILLS = ["thai-writer", "thai-product-writer"]
CASE_FIELDS = {"id", "context", "audience", "input", "expected_characteristics",
               "bad_examples", "good_examples", "evaluation_notes"}
FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")
MD_LINK = re.compile(r"\]\(([^)\s]+)\)")
TICK_PATH = re.compile(r"`(\.\.?/[^`\s]+?\.(?:md|yaml))`")
SKIP_DIRS = {".git", "node_modules", ".superpowers"}


def blank_code(text):
    """Remove code so only prose is checked; keep newlines so line numbers stay right."""
    text = FENCE.sub(lambda m: "\n" * m.group().count("\n"), text)
    return INLINE.sub("", text)


def md_files():
    for f in ROOT.rglob("*.md"):
        rel = f.relative_to(ROOT).parts
        if SKIP_DIRS & set(rel) or rel[:2] == ("docs", "superpowers"):
            continue
        yield f


def check_dashes(errors):
    for skill in NO_DASH_SKILLS:
        base = CLAUDE / skill
        if not base.is_dir():
            errors.append(f"{base.relative_to(ROOT)}: skill missing")
            continue
        for f in base.rglob("*.md"):
            for n, line in enumerate(blank_code(f.read_text(encoding="utf-8")).splitlines(), 1):
                for ch in "—→":
                    if ch in line:
                        errors.append(f"{f.relative_to(ROOT)}:{n}: '{ch}' in prose")


def check_links(errors):
    for f in md_files():
        text = f.read_text(encoding="utf-8")
        targets = MD_LINK.findall(text) + TICK_PATH.findall(text)
        for t in targets:
            if re.match(r"^[a-z]+:", t) or t.startswith("#"):
                continue
            path = t.split("#")[0]
            if path and not (f.parent / path).exists():
                errors.append(f"{f.relative_to(ROOT)}: broken link {t}")


def check_mirror(errors):
    for skill in sorted(p.name for p in CLAUDE.iterdir() if p.is_dir()):
        a, b = CLAUDE / skill, CODEX / skill
        fa = {p.relative_to(a) for p in a.rglob("*") if p.is_file()}
        fb = {p.relative_to(b) for p in b.rglob("*") if p.is_file()} if b.is_dir() else set()
        for rel in sorted(fa ^ fb):
            errors.append(f"mirror: {skill}/{rel.as_posix()} only on one side")
        for rel in sorted(fa & fb):
            if (a / rel).read_bytes() != (b / rel).read_bytes():
                errors.append(f"mirror: {skill}/{rel.as_posix()} differs")


def check_cases(errors):
    cases = yaml.safe_load((ROOT / "benchmark/cases.yaml").read_text(encoding="utf-8"))
    contexts = {p.stem for p in CLAUDE.glob("*/contexts/*.md")}
    seen = set()
    for c in cases:
        cid = c.get("id", "?")
        if missing := CASE_FIELDS - c.keys():
            errors.append(f"case {cid}: missing {sorted(missing)}")
        if cid in seen:
            errors.append(f"case {cid}: duplicate id")
        seen.add(cid)
        if c.get("context") not in contexts:
            errors.append(f"case {cid}: unknown context {c.get('context')!r}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    errors = []
    for check in (check_dashes, check_links, check_mirror, check_cases):
        check(errors)
    print("\n".join(errors) or "all checks passed")
    print(f"{len(errors)} problem(s)", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
