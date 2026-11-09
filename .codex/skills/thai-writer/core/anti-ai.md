# Anti-AI: Detect Patterns, Not Words

This is the file that keeps the whole skill from collapsing into a blacklist. Read it before treating anything as "AI-sounding."

## The hard rule

**No word is banned.** The only exception is two symbols, `—` and `→`, in Thai prose (see `punctuation.md`). They are punctuation marks, not words, and Thai has no job for them that a space or a connecting word can't already do. Words like `ดำเนินการ`, `อย่างไรก็ตาม`, `ดังกล่าว`, `ในกรณีที่`, `ทั้งนี้` are not "AI words." Each is completely normal, expected, and correct in the right register (formal documents, B2B/legal text, requirements, government-adjacent process descriptions). Flagging them by string match, independent of context, is exactly the mistake this skill exists to avoid.

Evaluate every candidate "smell" on these axes, together, not any single one alone:

- **Register**: does the surrounding text's formality level call for this construction?
- **Frequency**: once in a long document is fine; three times in one short paragraph is not.
- **Redundancy**: does it add logical/legal precision, or just length?
- **Sentence structure**: is it holding together a genuinely complex conditional, or padding a simple statement?
- **Audience**: a government/finance/legal-adjacent audience expects a different register than a consumer app's end users (see `tone.md`).

## Worked example: the same word, two verdicts

`ในกรณีที่` ("in the case that"):

- **Fine**: requirements/acceptance criteria explicitly enumerating a condition, such as `ในกรณีที่ผู้ใช้ยังไม่ยืนยันอีเมล ระบบจะ...`. This is exactly the register a requirements doc wants.
- **Suspicious**: a plain error message such as `ในกรณีที่พบปัญหา กรุณาติดต่อฝ่ายสนับสนุน`. `ถ้า` is shorter, equally precise, and matches a UI's expected register.

Same word. The verdict depends entirely on where it appears, not on the word.

## Formality is not a fixed brand voice, it scales with context

A directly-verified real-product data point (AIS's fraud-SMS security alert; see `../../../../research/real-product-observations.md`) drops politeness particles (ค่ะ/ครับ/กรุณา) entirely and switches to short direct imperatives specifically because the message is urgent. That's a deliberate register shift, not sloppiness. Don't treat "drop the particles" as a defect in a high-severity warning, and don't treat "keep the particles" as required everywhere else, either. Match the moment.

## Full pattern list

The complete taxonomy (28 patterns, each with a `when_it_is_valid` list and a confidence rating) lives in `../review/thai-ai-smells.md` for applied use. Full sourcing and confidence detail for the original 20 is in `../../../../research/thai-ai-smell-taxonomy.md`; the 8 punctuation, formatting, and chatbot-framing patterns added later (plus two folded into existing rows) have their own file, `../../../../research/punctuation-formatting-research.md`. None of these patterns have been validated against a native-speaker review panel yet, so treat confidence ratings as "how much to trust this," not proof.

## สัญญาณเดียวไม่พอ

An AI smell is judged from several signals appearing together, not from one. A single word or structure seen once is not enough to call something a problem: one `อย่างไรก็ตาม`, one bolded label, or one three-item list can each be a normal human choice. What gives text away is the cluster, for example a chatbot opener, bold labels on every line, a triple of adjectives, and a summary that repeats the paragraph above, all in one short reply. `[Source-backed]` Wikipedia's "Signs of AI writing" makes the same point about its own catalogue: the signs are indicators to weigh together, not proof on their own (see `../../../../research/punctuation-formatting-research.md`).

When you do fix a cluster, rewrite the sentences. Swapping words or punctuation mechanically (`—` to `,`, `อย่างไรก็ตาม` to `แต่` everywhere) leaves the same English skeleton under new surface marks, and the text still reads as generated. See `punctuation.md` for the punctuation version of this rule.

## Before you flag anything, ask

1. Would this exact construction look normal in a comparable real document/UI of this same register and audience?
2. Am I flagging a word, or a mismatch between register and context?
3. Have I checked the frequency: is this one instance in a long piece, or three in one paragraph?
4. Am I about to recommend a blanket rule ("never use X") instead of a contextual judgment?

If the answer to #4 is yes, stop and rewrite the finding as a context-dependent observation instead.
