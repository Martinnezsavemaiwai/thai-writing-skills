# Natural Thai

Structural habits that make Thai read as translated or model-generated, and what a native writer does instead. Sourced from `../../../../research/thai-writing-principles.md`; see that file for citations and confidence tags. For common English software-writing phrases specifically ("You can...", "Successfully saved...", "Are you sure...") and what to do with each, see `../../../../research/translation-adaptation.md`. It builds directly on the patterns below rather than duplicating them.

## Subjects: Thai drops them, English can't

Thai freely omits a subject once it's recoverable from context. Carrying over English's requirement for an explicit subject in every sentence is one of the most common tells.

- Translated: `ระบบจะทำการบันทึกข้อมูลของคุณโดยอัตโนมัติ`
- Natural: `บันทึกข้อมูลอัตโนมัติ`

Keep the subject explicit only when it's doing real work, such as distinguishing "the system did this" from "you need to do this," or when ambiguity would actually confuse the reader. `[Open question: needs native-speaker validation]`: exactly how far to push subject omission in second-person UX copy without losing the "talking to you" feel; see `tone.md`.

## Passive voice: `ถูก`/`โดน` is not a default translation of English passive

`ถูก` is grammatical Thai, but native usage skews toward agentless or adversative situations (`ถูกไล่ออก`, `ถูกปฏิเสธ`). Using it to translate every English passive ("is designed to," "was created for") produces a sentence a Thai speaker wouldn't construct that way.

- Translated: `กระเป๋าใบนี้ถูกออกแบบมาเพื่อรองรับการใช้งานในชีวิตประจำวัน`
- Natural: `กระเป๋าใบนี้ออกแบบมาให้ใช้งานง่ายในชีวิตประจำวัน`

Passive is still correct when the agent is genuinely unknown/irrelevant (incident reports: "the request was rejected") or where passive is the established convention (legal/technical rule statements).

## Rhetorical calques

"Not just X, but also Y" (`ไม่ใช่แค่...แต่ยังเป็น...`) is a borrowed English rhetorical frame, not a natural Thai way to state two facts. Prefer stating both facts plainly and letting the reader draw the connection.

- Translated: `โลชั่นตัวนี้ไม่ใช่แค่บำรุงผิว แต่ยังเป็นตัวช่วยให้คุณมั่นใจในทุกวัน`
- Natural: `โลชั่นตัวนี้บำรุงผิวให้ชุ่มชื้น ใช้แล้วมั่นใจได้ทั้งวัน`

## One long sentence vs. several short ones

AI-generated Thai tends to chain clauses with subordinators the way English chains them with commas and relative pronouns, producing one long sentence where a native writer uses two or three short ones, especially in UI and docs, which favor short single-clause sentences (see `technical-writing-research.md`).

- Chained: `ระบบจะทำการตรวจสอบข้อมูลที่ผู้ใช้กรอกก่อนที่จะทำการบันทึกลงในฐานข้อมูลซึ่งหากพบข้อผิดพลาดจะแสดงข้อความแจ้งเตือนให้ผู้ใช้ทราบ`
- Split: `ระบบตรวจข้อมูลก่อนบันทึก ถ้าพบข้อผิดพลาดจะแจ้งเตือนทันที`

## English mid-sentence: don't carry over Title Case

An English word or brand/feature name inside a Thai sentence is normal; capitalizing it as if it were an English heading is not, because Thai has no capitalization system to begin with, so the Title Case is a visible seam from an English template.

- Seamed: `ให้ Perfect Skin ของคุณด้วย Premium Quality Serum ตัวนี้`
- Natural: `เซรั่มสูตรพรีเมียม ช่วยให้ผิวคุณดูดีขึ้น`

Actual proper nouns (brand names, a feature literally named "Smart Mode" in the UI) are exempt because they're identifiers, not descriptive adjectives.

## Nominalization: turning a verb into an abstract noun it doesn't need to be

`มีการ` + `การ-`/`ความ-` prefix turns a plain verb into an abstract-noun construction, adding length without adding precision. It is a related but distinct mechanism from `ทำการ` padding (that one keeps the verb and adds a helper; this one converts the verb into a noun phrase).

- Padded: `มีการดำเนินการตรวจสอบข้อมูลก่อนบันทึก`
- Direct: `ตรวจสอบข้อมูลก่อนบันทึก`

Still valid when the process itself, not its result, is genuinely the topic of the sentence (a formal report literally about "the conducting of an audit" as a subject, rather than about what the audit found).

## Classifiers (ลักษณนาม)

Thai counting constructions require a noun-specific classifier. Wrong or missing classifiers are one of the strongest "not written by a Thai speaker" signals, closer to a correctness bug than a style choice. `[Source-backed]`: Iwasaki & Ingkaphirom, *A Reference Grammar of Thai* (Cambridge University Press); see `../../../../research/thai-ai-smell-taxonomy.md`.

- Wrong: `เสื้อยืด 3 ชิ้น รองเท้า 2 ชิ้น`
- Correct: `เสื้อยืด 3 ตัว รองเท้า 2 คู่`

For emerging software-specific nouns (counting "devices," "accounts," "sessions") where classifier convention is contested or unsettled, match whatever the existing product copy already uses rather than guessing.

## ประโยคแบบ "ไม่ใช่ X แต่คือ Y"

A close relative of the calque above. The sentence denies something nobody claimed, only so it can announce something bigger. It sounds weighty but says less than a plain statement of what actually happens.

- Inflated: `นี่ไม่ใช่แค่การประชุม แต่คือจุดเริ่มต้นของการเปลี่ยนแปลง`
- Plain: `ประชุมครั้งนี้จะตัดสินแผนปีหน้า`

Still valid when it corrects a misunderstanding that really exists. If the team thinks the event was cancelled, `ไม่ได้ยกเลิก แค่เลื่อน` is exactly the right sentence: the denial answers something the reader already believes.

## คำคุณศัพท์สามคำ

Three adjectives in a row, usually ending with `และ...`, is a rhythm habit carried over from English. Each word is vague, and together they tell the reader nothing they could check.

- Padded: `รวดเร็ว ง่ายดาย และมีประสิทธิภาพ`
- Concrete: `สมัครเสร็จใน 2 นาที`

The fix is one measurable fact instead of three claims. Still valid when the text really backs all three words, for example a comparison where speed, ease, and cost are each shown with their own numbers.
