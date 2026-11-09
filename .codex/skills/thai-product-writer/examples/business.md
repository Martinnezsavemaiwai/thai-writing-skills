# Examples: Business / Product

## Business rule: rationale mixed into the rule

- Before: `ยกเลิกออเดอร์ไม่ได้หลัง 24 ชั่วโมงเพราะระบบคลังสินค้าตัดสต๊อกไปแล้วและการคืนสต๊อกทำได้ยากในทางปฏิบัติ`
- After:
  - Rule: `ยกเลิกออเดอร์ได้เฉพาะภายใน 24 ชั่วโมงหลังสั่งซื้อ`
  - Note (separate field): เหตุผล: ระบบคลังตัดสต๊อกอัตโนมัติหลัง 24 ชั่วโมง
- Why: the rule itself needs to stay a stable, grep-able conditional; folding the justification into the same sentence makes both harder to maintain independently.

## Internal stakeholder update: over-formalized for the actual audience

- Before: `เรียนท่านผู้บริหาร ทางทีมพัฒนาใคร่ขอเรียนให้ทราบว่าในขณะนี้ได้ดำเนินการแก้ไขปัญหาที่ท่านได้แจ้งมาเรียบร้อยแล้ว ทั้งนี้ ระบบสามารถใช้งานได้ตามปกติแล้วในขณะนี้`
- After: `แก้บั๊กที่แจ้งไว้เรียบร้อยแล้ว ระบบใช้งานได้ปกติ`
- Why: this is an internal status update to a PM/stakeholder the team works with regularly, not a formal external letter, and "professional" here doesn't mean maximum formality (see `../../thai-writer/core/tone.md`).

## Executive summary: needs to stay measured, not casual

- Before (over-casualized): `เดือนนี้เราแก้บั๊กไปเยอะมาก ระบบเสถียรขึ้นเยอะเลย ลูกค้าน่าจะแฮปปี้`
- After: `เดือนนี้ปิดบั๊กสำคัญ 12 รายการ อัตราการเกิดข้อผิดพลาดของระบบลดลง 40%`
- Why: an executive summary needs concrete outcomes, not a casual impression. This is the opposite failure mode from the stakeholder-update example above, and both are wrong for the same reason: not matching audience/context (see `../../thai-writer/core/tone.md`).

## Terminology inconsistency across a product

- Before: home screen says "รายการสั่งซื้อ", order history says "คำสั่งซื้อ", push notification says "ออเดอร์", all referring to the same entity.
- After: pick one (e.g. "รายการสั่งซื้อ"), record it in the glossary (`../terminology/glossary.example.yaml`), use it everywhere.
- Why: each term is individually fine; the inconsistency itself is the defect. It breaks the user's mental model of the product.
