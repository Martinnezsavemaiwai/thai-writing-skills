# Conciseness

Cut what doesn't carry information. Don't cut what makes the text match its audience. Conciseness is not the same goal as casualness, and over-shortening a piece that needs to stay measured (a legal notice, a stakeholder update) is its own mistake. Check the matching context file (`../contexts/` for general writing, `../../thai-product-writer/contexts/` for software) for the target length/register before trimming.

## Redundant verb constructions

`ทำการ + verb` ("to carry out [verb]-ing") pads a sentence with a semantically empty helper verb.

- Padded: `ทำการบันทึกข้อมูล`
- Direct: `บันทึกข้อมูล`

Still valid in formal institutional announcements where the emphasis is genuinely on the act of undertaking something (`ธนาคารได้ทำการปรับปรุงระบบ`); check per case, don't strip mechanically.

## Redundant content, not just redundant words

Over-explanation is restating a consequence the reader already inferred. This is a content-level redundancy, distinct from wordy phrasing. Trimming words won't fix it; only removing the redundant sentence will.

- Over-explained: `ลบรายการนี้ไม่ได้เพราะมีการอ้างอิงอยู่ ดังนั้นกรุณาตรวจสอบการอ้างอิงก่อนทำการลบ`
- Trimmed: `ลบรายการนี้ไม่ได้เพราะมีการอ้างอิงอยู่`

## Repetitive sentence templates

Repeating the same sentence shape back-to-back (`X คือ... X ช่วยให้... X มี...`) reads as a list dressed as prose. Vary openers, or combine short related facts into one sentence instead of one-fact-per-sentence.

## Formal connectors as padding vs. as real logic

`ทั้งนี้`, `ดังนั้น`, `อย่างไรก็ตาม`, `กล่าวคือ`, `โดยเฉพาะอย่างยิ่ง` are not banned words (see `anti-ai.md`), but in short, casual, frequently-read surfaces (toasts, buttons, empty states) they're almost always padding rather than doing real logical work. Test: does removing the connector and using a space or nothing lose any actual logical relationship? If not, it was padding.

- Padded: `ทั้งนี้ กรุณากรอกอีเมลก่อนกดยืนยัน`
- Direct: `กรอกอีเมลก่อนกดยืนยัน`

## Politeness particles at natural rhythm, not on every clause

`ค่ะ`/`ครับ`/`นะคะ` etc. attached to every single sentence flattens rhythm in a way real speech and real customer copy don't. Use them at conversational beats, not mechanically. An established brand voice that intentionally uses the particle every sentence is an exception, so verify against the product's existing copy before flagging it.

## เปิดและปิดแบบแชทบอท

Chat-assistant openers and closers wrap the actual content in ceremony that carries no information. An acknowledgement on its own is not the problem: `ได้ครับ` and `ได้เลยครับ` are how Thai people normally answer a request in chat. The giveaway is the stock phrase wrapped around the content, such as an acknowledgement followed by a restatement of what is being handed over (`ได้เลยครับ นี่คือ...`), praise for the question (`คำถามที่ดีมาก`), or a closing wish tacked onto the end. As `anti-ai.md` says, one of these alone proves little; several in one short reply is the pattern.

Openers to cut:

- `แน่นอน!`
- `คำถามที่ดีมาก`
- `ได้เลยครับ นี่คือ...`

Closers to cut:

- `หวังว่าจะเป็นประโยชน์`
- `หากมีคำถามเพิ่มเติมสามารถสอบถามได้เลย`
- `โดยสรุปแล้ว...` when it only repeats what the previous paragraphs already said

The fix is to delete them and start with the answer. Rewording them into a different stock phrase is not a fix.

| Before | After |
|---|---|
| `ได้เลยครับ นี่คือสรุปยอดเดือนนี้ ยอดขายรวม 1.2 ล้านบาท หวังว่าจะเป็นประโยชน์นะครับ` | `ยอดขายเดือนนี้รวม 1.2 ล้านบาทครับ` |

Still valid: a short chat acknowledgement of a request (`ได้ครับ เดี๋ยวส่งให้`), and `แน่นอนครับ` when it is itself the answer to a yes/no question like `ทำได้ไหม` (see `formatting.md`, which asks for the yes or no first). Closers are still valid in customer service, where the reader really may need to follow up. Even then, replace the generic invitation with the actual channel: `สอบถามเพิ่มได้ที่ LINE @xxx` tells the customer where to go, while `หากมีคำถามเพิ่มเติมสามารถสอบถามได้เลย` does not. For how this looks in a chat answer, see `formatting.md`.
