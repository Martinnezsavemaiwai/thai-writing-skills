# Benchmark

Evaluates whether `thai-writer` and `thai-product-writer` actually improve Thai writing, general and software-product alike, and, just as importantly, whether they correctly leave already-good text alone. See `../research/README.md` for the research this benchmark is built on; this directory is the applied evaluation layer.

## Files

- **`cases.yaml`** — test cases. Schema per case: `id`, `context` (matches a `contexts/*.md` file), `audience`, `input`, `expected_characteristics`, `bad_examples`, `good_examples`, `evaluation_notes`.
- **`rubric.md`** — the 7-dimension scoring rubric (Meaning Preservation, Naturalness, Context Fit, Audience Fit, Terminology Consistency, Conciseness, AI-Smell), 1-5 each.

## `NO_CHANGE` is a first-class, correct output

A case's `good_examples` sometimes equals its `input` verbatim, or is explicitly noted as "(no change — already correct)." **This is not a missing test case — it's the point.** A skill that always finds something to rewrite fails these cases regardless of how good its rewrites are elsewhere. See `control-001`, `control-002`, `biz-004`, `biz-015`, `doc-010`, `doc-014`, `punct-005`, `punct-006`, `format-004`, `formal-001` (control cases in the corpus and benchmark) and `../.claude/skills/thai-writer/core/anti-ai.md`.

## What the adversarial cases test

Beyond straightforward "bad → good" pairs, several cases are deliberately adversarial — they test *decisions*, not just rewrites:

| Trap | What it catches | Example case(s) |
|---|---|---|
| Text is already correct | Skill that always rewrites something | `control-001`, `control-002` |
| Formal register is the right register | Skill that "humanizes" everything, including ToS/legal clauses | `register-001`, `formal-001` |
| A concise rewrite silently drops a condition or number | Grading conciseness/naturalness without checking meaning | `meaning-001`, `meaning-002` |
| A situation needs MORE detail, not less | Grading conciseness independent of severity/recoverability | `error-detail-001` |
| An English technical term should stay in English | Reflexively translating every English word | `tech-term-001` |
| A product's own terminology choice should win over generic preference | "Correcting" a valid house-style term to a different, also-valid one | `term-002` |
| Same string, different rendering across surfaces | Judging each string in isolation, missing the cross-surface defect | `term-001` |
| สัญลักษณ์ที่ถูกต้อง (ช่วงตัวเลข, โค้ด) | Flagging every dash or arrow without checking whether it marks a range or sits in code | `punct-005`, `punct-006` |
| emoji ที่เป็นน้ำเสียงจริง | Stripping emoji the author chose as part of their own voice | `format-004` |
| สลับเครื่องหมายแต่ไม่แก้โครงสร้าง | Swapping `—` for a comma or colon and calling the English two-half sentence fixed | `punct-004` |

If a case's `good_examples` looks *worse* at first glance than an obvious alternative, read `evaluation_notes` before assuming the case is wrong — several are deliberately testing that the "obvious" rewrite is the failure.

## Evidence status

Every case here is model-constructed and reasoned, not yet reviewed by a native Thai speaker — see `../research/native-speaker-validation.md` for the (currently unrun) methodology that would eventually validate these. Do not describe this benchmark as "validated."

## Adding a case

1. Pick the `context` it belongs to and check that context's file for what "correct" means there: `../.claude/skills/thai-writer/contexts/` for general writing, `../.claude/skills/thai-product-writer/contexts/` for software-product text.
2. Write `evaluation_notes` explaining *what specifically* the case tests — a case with no clear failure mode it's checking for is padding, not coverage (see section 9 of the Evidence Hardening research phase: "do not merely increase the number of cases").
3. If the case is adversarial (testing a decision, not just a rewrite), say so explicitly in `evaluation_notes` and add a row to the table above.
4. Cross-check against `../research/thai-ai-smell-taxonomy.md` if the case involves a specific pattern — cite the pattern `id`.
5. Run `python scripts/check_skills.py` from the repo root. It checks that every case has all 8 fields, a unique `id`, and a `context` that matches an existing `contexts/*.md` file.
