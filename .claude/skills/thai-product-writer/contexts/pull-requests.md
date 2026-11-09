```yaml
context: pull-requests
purpose: describe a proposed change for a reviewer, and give a stakeholder/QA reader enough to test it
audience: Developer, QA, Internal Team
desired_tone: Neutral-Conversational, direct
desired_length: short: a paragraph for why, a list for what changed, a checklist for how to test
must_preserve: the actual scope and any known limitation/caveat the author flagged
common_mistakes: excessive_formal_connectors, over_explanation
```

`[Project decision, derived]`: no single external style guide covers PR-description phrasing directly; this combines the "why not what" comment principle with Microsoft/Google's "lead with the point" guidance; see `../../../../research/technical-writing-research.md`.

## Lead with why, not what

The diff already shows what changed. A PR description that opens with "ใน PR นี้จะทำการปรับปรุง..." (in this PR, we will proceeze to improve...) delays the one thing the reviewer actually needs: why does this change exist.

- Throat-clearing: `ใน PR นี้จะทำการปรับปรุงฟังก์ชันการคำนวณราคาให้ถูกต้องมากขึ้น`
- Direct: `แก้บั๊กราคาคำนวณผิดเมื่อมีส่วนลดซ้อนกันสองรายการ`

## Structure that serves the reviewer

- **Why**: the problem or goal, one or two sentences
- **What changed**: a short list if it touches multiple things, prose if it's one change
- **How to test**: concrete steps or a checklist, especially for QA readers who won't read the diff

## Known limitations belong in the description, not buried in a comment thread

If the author knows the PR doesn't handle an edge case, say so directly, because this is a meaning-preservation issue (`../../thai-writer/core/meaning-preservation.md`) as much as a writing one: omitting a known caveat changes what the reviewer believes they're approving.
