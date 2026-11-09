# Clarity

Text the reader understands on first pass, without re-reading. This is a different failure mode from "unnatural" (core/natural-thai.md). A sentence can be grammatically perfect, idiomatic Thai and still be unclear because it's vague, front-loads the wrong information, or hides the actionable part.

## Lead with what the reader needs first

Don't preface with scene-setting before the actual point. This applies to a single UI string and to a whole document opening.

- Buried: `ถ้าต้องการเปลี่ยนภาพพื้นหลัง ให้ไปที่เมนูการตั้งค่าแล้วเลือกธีม`
- Direct: `เลือกธีมในการตั้งค่าเพื่อเปลี่ยนภาพพื้นหลัง`
- Buried (doc opening): `ในยุคที่ทุกอย่างเปลี่ยนเร็ว การวางแผนการเงินจึงสำคัญมากขึ้น บทความนี้จะ...`
- Direct: state what the text is about and why it matters, first sentence.

*(Source-backed: Microsoft Windows apps writing style says "don't preface"; see `../../../../research/ux-writing-research.md`.)*

## Say what's wrong and what to do, not just that something's wrong

A validation or error message that names the problem without enough detail to fix it isn't clear, even if every word in it is natural Thai.

- Vague: `ข้อมูลไม่ถูกต้อง`
- Actionable: `รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร`
- Vague (email reporting a problem): `เอกสารมีปัญหานิดหน่อยค่ะ`
- Clear: `ใบเสนอราคาหน้า 2 ยอดรวมยังไม่รวม VAT ค่ะ รบกวนแก้แล้วส่งใหม่ภายในวันศุกร์`

## Concrete over abstract when a concrete word exists

Abstract nouns that require the reader to infer the concrete referent slow comprehension. Prefer naming the actual thing.

- Abstract: `ดำเนินการที่จำเป็น` (the necessary action)
- Concrete: name the actual action, such as `กดยืนยันอีเมล`

## One idea per sentence in dense contexts

Requirements, acceptance criteria, and business rules should not pack multiple conditions into one sentence with implicit precedence. Split into separate, explicitly-scoped statements (see `../../thai-product-writer/contexts/requirements.md`).

## Consistent verbs for the same action

Using different Thai verbs for the same action across a product (`ลบ` vs `เอาออก` vs `นำออก` all meaning "delete" on different screens) breaks the reader's mental model even though each individual sentence is clear on its own. This is a terminology-consistency issue. See `../../thai-product-writer/terminology/terminology.md`.
