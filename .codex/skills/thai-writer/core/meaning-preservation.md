# Meaning Preservation

The first check, before any rewriting. Everything else in `core/` is about *how* to phrase something; this file is about what you're not allowed to change while phrasing it.

## What must never change

- **Business rules and conditions.** If the source says "the button disables when the cart is empty **or** the user isn't verified," the rewrite must preserve both conditions and the OR, without simplifying to one and without silently changing OR to AND.
- **Technical meaning.** Error causes, units, thresholds, API contract wording, field names referenced in code. These are load-bearing. A more natural-sounding sentence that drops "ภายใน 24 ชั่วโมง" or rounds "3 ครั้ง" to "หลายครั้ง" has broken the text even if it reads better.
- **Scope of a claim.** "บันทึกอัตโนมัติทุก 30 วินาที" and "บันทึกอัตโนมัติเป็นระยะ" are not interchangeable; the second is vaguer than the source, which is a meaning change even without adding anything false.
- **Facts in everyday writing.** The same rule holds outside software: numbers, dates, people's names, amounts of money, and conditions in an email or a message. `ส่งภายในวันศุกร์ที่ 14` cannot become `ส่งปลายสัปดาห์`, `คุณสมชาย` cannot become `ผู้ประสานงาน`, and `โอน 12,500 บาท ภายในสิ้นเดือน` keeps both the exact amount and the deadline. A friendlier rewrite that blurs any of these has changed what the sender committed to.

## What's safe to change

- Sentence structure, word order, which word carries the subject
- Splitting one long sentence into two, or merging two choppy ones
- Register/formality, as long as it matches the context (see the matching context file in `../contexts/` for general writing, or `../../thai-product-writer/contexts/` for software). That is not "meaning"
- Removing genuinely redundant restatement (see `conciseness.md`) as long as no unique information is lost

## When the source is ambiguous

Don't guess and don't silently pick an interpretation. If a validation message's condition is unclear, or a requirement doesn't say what happens on the edge case, ask. Guessing plausibly and writing confident Thai around a wrong guess is worse than a rewrite that keeps the ambiguity visible. An ambiguous sentence can be caught in review; a confident wrong one usually isn't.

## Self-check before delivering

1. List every fact, number, condition, and named entity in the source.
2. Confirm each one appears in the rewrite, unchanged in substance.
3. Confirm nothing was added that the source didn't say (no invented reassurance, no invented next step, no invented cause for an error).
