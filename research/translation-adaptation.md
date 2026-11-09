# English → Thai Adaptation

**Governing principle: preserve meaning and user intent, not English sentence structure.** Good Thai product writing is not a translation of an English string — it's Thai written from the same underlying fact/intent the English string was written from. This file catalogs common English software-writing structures and what Thai does instead, building on the calque patterns already in `thai-ai-smell-taxonomy.md` (`passive_calque`, `not_just_x_but_y_calque`) — cross-referenced below rather than duplicated.

Tags: `[SOURCE_BACKED]` / `[OBSERVED]` / `[PROJECT_DECISION]` / `[HYPOTHESIS]` / `[OPEN QUESTION]`.

## The eight structures

For each: what the literal-translation failure looks like, and what Thai does instead.

### "You can..."

- Literal: `คุณสามารถเปลี่ยนภาพโปรไฟล์ได้โดยการกดที่ไอคอนรูปภาพ`
- Natural: `กดไอคอนรูปภาพเพื่อเปลี่ยนโปรไฟล์`
- `[OBSERVED]`: English "you can X by Ying" is a permission-framing that Thai doesn't need for a straightforward instruction — Thai states the action directly as an imperative. **Adaptation: omit subject, restructure as direct instruction.** Reserve `คุณสามารถ...ได้` for when the point genuinely is optionality/capability (e.g. "you can also do X" when X is one of several valid choices), not for a single obvious instruction.

### "In order to..."

- Literal: `เพื่อที่จะดำเนินการต่อ กรุณายืนยันอีเมลของท่าน`
- Natural: `ยืนยันอีเมลก่อนดำเนินการต่อ` or simply `ยืนยันอีเมลเพื่อดำเนินการต่อ`
- `[OBSERVED]`: "in order to" is frequently just "to" in disguise — a padded purpose-clause opener. Thai's `เพื่อ` alone carries the same purpose relationship without the extra `ที่จะ`. **Adaptation: restructure**, drop the doubled purpose marker, and consider whether leading with the purpose or the action reads more naturally for the specific sentence (both orders are valid Thai; pick whichever puts the more important information first per `core/clarity.md`).

### "Please make sure..."

- Literal: `กรุณาตรวจสอบให้แน่ใจว่าท่านได้กรอกข้อมูลครบถ้วนก่อนกดส่ง`
- Natural: `กรอกข้อมูลให้ครบก่อนกดส่ง`
- `[OBSERVED]`: "please make sure X" is an English hedge-politeness pattern around a direct instruction (the instruction is just "do X"). Reserve `กรุณา` for situations where the user is genuinely being asked to do something inconvenient or where the register calls for service-context politeness (see `ux-writing-research.md`'s กรุณา-vs-ลอง register note) — a routine form-completion reminder doesn't need it. **Adaptation: remove unnecessary politeness, state the requirement directly.**

### "We were unable to..."

- Literal: `เราไม่สามารถทำการประมวลผลคำขอของท่านได้ในขณะนี้`
- Natural: `ประมวลผลคำขอไม่สำเร็จ`
- `[OBSERVED]`: English error messages often frame the system/company as the grammatical subject ("we were unable to..."). Thai error messages more naturally state the result directly without a "we" actor — this is the same subject-omission principle as `core/natural-thai.md`'s general guidance, applied specifically to the common English error-message opener. **Adaptation: omit subject, state the result directly.** Also strips the `ทำการ` redundant-verb padding (`taxonomy:redundant_verb_construction`) that tends to accumulate around this pattern.

### "Something went wrong..."

- Literal: `มีบางอย่างผิดพลาดเกิดขึ้น`
- Natural (when no more specific cause is known): `เกิดข้อผิดพลาด` — or, per `error-writing-research.md`, name the actual specific problem if one is known rather than defaulting to this generic phrase at all
- `[PROJECT_DECISION, ties to error-writing-research.md]`: "something went wrong" is already a content-free filler in English — translating it well doesn't fix that it says nothing. **Adaptation: state the result directly**, and treat this English phrase as a signal to look for a more specific underlying cause before translating, not just to translate faithfully.

### "Are you sure you want to..."

- Literal: `คุณแน่ใจหรือไม่ว่าต้องการที่จะลบรายการนี้`
- Natural: `ลบรายการนี้ใช่ไหม` (routine) or, for destructive actions, name the consequence instead: `ลบบัญชีนี้ถาวร ข้อมูลทั้งหมดจะหายไปและกู้คืนไม่ได้` (see `contexts/ux-writing.md#destructive-actions`, sourced from NN/g's "state the outcome, not a generic confirmation" finding)
- `[OBSERVED]`: this English confirmation-dialog template translates into grammatical but stiff Thai (`แน่ใจหรือไม่ว่าต้องการที่จะ`), and — more importantly, per the destructive-actions research already in `ux-writing-research.md` — a generic "are you sure" confirms nothing about what will actually happen, so translating it well still leaves the underlying UX problem. **Adaptation: restructure**, and for destructive actions, replace the question with the actual consequence rather than translating the question at all.

### "Successfully completed..." / "Successfully saved..."

- Literal: `การบันทึกข้อมูลของท่านเสร็จสมบูรณ์เรียบร้อยแล้วอย่างสำเร็จ` (a genuinely awkward but representative over-literal rendering, stacking three success-markers)
- Natural: `บันทึกแล้ว`
- `[OBSERVED]`: English "successfully X-ed" redundantly states both the action and its success in one adverb; Thai's simple past-completive `แล้ว` already implies success for an action that doesn't have a partial/failure state worth distinguishing. **Adaptation: state the result directly**, drop the success-adverb entirely for routine confirmations. Reserve a more explicit "completed successfully" framing for cases where failure was a real, salient possibility the user was watching for (e.g. a long-running export/import job) — there, `เสร็จสมบูรณ์` earns its place because it's confirming something that could plausibly not have completed.

### "Your changes have been saved."

- Literal: `การเปลี่ยนแปลงของท่านได้ถูกบันทึกแล้ว`
- Natural: `บันทึกการเปลี่ยนแปลงแล้ว`
- `[OBSERVED]`: textbook `passive_calque` (see `thai-ai-smell-taxonomy.md`) — "have been saved" translated with `ถูก...แล้ว` when Thai defaults to active/topic-fronted phrasing for a routine, non-adversative confirmation. **Adaptation: retire the passive, state the result directly**; this is the same mechanism as the taxonomy's `passive_calque` entry, not a separate pattern — included here because it's one of the single most common English UI strings that gets literally translated this way.

## When to retain, translate, or transliterate the underlying terminology

Not covered per-phrase above but relevant to all eight: whichever adaptation is chosen, the *terminology* inside it (e.g. "save," "delete," "account") follows `terminology/terminology.md`, not this file — this file is about sentence-structure adaptation, term choice is a separate, per-product decision. Don't let a well-adapted sentence structure quietly introduce a term that conflicts with the product's existing glossary.

## Cross-references, not duplicated here

- Passive-voice calque mechanism in general: `thai-ai-smell-taxonomy.md`'s `passive_calque` entry, `core/natural-thai.md`
- "Not just X but also Y" rhetorical calque: `thai-ai-smell-taxonomy.md`'s `not_just_x_but_y_calque` entry
- Subject omission generally: `core/natural-thai.md`, `core/tone.md`'s "second person without over-using คุณ" section
- Politeness-particle register (กรุณา/ลอง): `ux-writing-research.md`'s Thai-specific baseline section

## Sources

This file is primarily `[OBSERVED]`/`[PROJECT_DECISION]` synthesis of patterns already sourced elsewhere in `research/` (see cross-references above) applied to eight specific, commonly-seen English source strings named in the task brief, rather than new external citations — no additional sources were fetched for this file specifically.
