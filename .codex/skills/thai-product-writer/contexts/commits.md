```yaml
context: commits
purpose: describe what a commit changes and why, for teammates reading history/blame later
audience: Developer, Internal Team
desired_tone: Neutral-Technical, direct, imperative
desired_length: one-line subject; body only if the "why" needs more than the subject can carry
must_preserve: the actual scope of the change (don't broaden or narrow what the diff does)
common_mistakes: excessive_formal_connectors, over_explanation, redundant_verb_construction
```

`[Open question]`: whether a given team writes commits in Thai at all, vs. English (often via Conventional Commits), is a per-project choice, so don't assume Thai commits are the default. Apply this file only when the project's own convention is Thai commit messages.

## Structure

Same idea as English Conventional Commits (type + short imperative subject, body only for context the subject can't hold):

- `แก้: ตรวจสอบอีเมลซ้ำก่อนสมัครสมาชิก` (fix: check duplicate email before signup)
- `เพิ่ม: รองรับการชำระด้วย QR พร้อมเพย์` (feat: support PromptPay QR payment)

## Avoid formal throat-clearing

A commit subject doesn't need `ทำการ` or `ดำเนินการ`, since the imperative verb alone is the convention (`แก้`, `เพิ่ม`, `ลบ`, `ปรับปรุง`), matching the terseness of English imperative-mood commit subjects.

- Padded: `ทำการแก้ไขปัญหาการคำนวณราคาที่ผิดพลาด`
- Direct: `แก้: คำนวณราคาผิดตอนมีส่วนลดซ้อน`

## Body explains why, not what

The diff already shows what changed. If a body is needed at all, it's for context the diff can't carry: why this approach, what edge case prompted it, what it doesn't fix. Same principle as `code-comments.md`, applied to a different surface.
