```yaml
context: code-comments
purpose: explain to a future reader of the code something the code itself can't say
audience: Developer
desired_tone: Technical, terse, no politeness particles, colleague-to-colleague
desired_length: one line where possible; a short paragraph only for a genuinely non-obvious constraint
must_preserve: the actual technical reason/constraint being documented
common_mistakes: over_explanation, unnecessary_subject_insertion, redundant_verb_construction
```

If the task is cleaning up **English** AI-generated comments, use the `code-comment-humanizer` skill instead. This file is specifically about the Thai-language layer on top of that same underlying principle.

## The governing rule: why, not what

A comment that restates what the next line visibly does is redundant regardless of how natural the Thai is. `[Source-backed principle]`, *Software Engineering at Google* ch. 8 / `google/eng-practices`; see `../../../../research/thai-ai-smell-taxonomy.md`.

```ts
// ไม่ดี: บอกซ้ำสิ่งที่โค้ดทำอยู่แล้ว
// ตรวจสอบว่ามีข้อมูลหรือไม่เพื่อดำเนินการในขั้นตอนถัดไป
if (!order) return null;

// ดีกว่า: บอกเหตุผลที่โค้ดไม่ได้บอกเอง
// ไม่มี Order ก็ไม่ต้องแสดงตาราง
if (!order) return null;
```

## Three valid outcomes, not two

Given a comment, the options are: **keep** it as-is (it already explains a real "why"), **rewrite** it (there's a real reason but the phrasing is padded/translated/over-formal), or **recommend deleting** it (the code is already self-explanatory, and no phrasing fix makes a redundant comment not-redundant). Don't default to "rewrite" out of habit; check whether the comment should exist at all first.

`[Source-backed, deepened this pass]`: triangulating Google against Robert C. Martin (*Clean Code*) and John Ousterhout (*A Philosophy of Software Design*) surfaces a fourth possibility this skill has no mandate to act on but should still flag (sources in `../../../../research/technical-writing-research.md`): sometimes a comment exists because the **code itself** isn't clear (bad naming, tangled logic), and the real fix is restructuring the code, not improving the Thai wording of the comment explaining it. If a comment reads as compensating for confusing code, say so as an observation alongside whatever text-level fix you give. Don't silently polish the Thai and leave the underlying code smell unmentioned.

**A "why" classification depends on the comment being paired with its actual code, not on the comment text alone.** The same sentence that correctly explains `if (!order) return null;` says nothing if attached to unrelated code, or shown with no code at all. Always evaluate a comment together with the line(s) it sits above; never judge comment text in isolation (validated against new test cases this pass; see `../../../../research/technical-writing-research.md`'s framework-validation section).

## What's actually different about Thai comments

Not a separate grammar: the structural "why not what" problem is language-independent. The Thai-specific things to watch:

- **Mixed Thai/English consistency.** Code comments in Thai codebases often mix in English technical terms (variable names, framework concepts). Keep that mixing consistent within one file/module rather than switching conventions comment to comment.
- **Register no higher than the surrounding code culture.** `ดำเนินการ`-style formal phrasing in a comment meant for a teammate reading fast is a register mismatch the same way it would be in a Slack message; see `../../thai-writer/core/anti-ai.md`.
- **Don't pad a one-line reason into a paragraph.** A comment justifying a workaround needs the constraint, not a lead-up to it.

## Worked example: a comment that should be deleted, not rewritten

```ts
// เพิ่มค่า count ขึ้น 1
count++;
```

No rewrite makes this comment earn its place; the code says everything the comment says. Recommend removing it.
