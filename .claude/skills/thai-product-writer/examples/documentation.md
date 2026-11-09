# Examples: Documentation

## README opening: scene-setting before the point

- Before: `ในปัจจุบันการพัฒนาซอฟต์แวร์มีความสำคัญมากขึ้นเรื่อยๆ และการจัดการข้อมูลอย่างมีประสิทธิภาพก็เป็นสิ่งจำเป็น โปรเจกต์นี้จึงถูกสร้างขึ้นมาเพื่อช่วยแก้ปัญหาดังกล่าว`
- After: `โปรเจกต์นี้จัดการคิวงานพื้นหลังสำหรับระบบที่มี throughput สูง`
- Why: the first version takes two throat-clearing sentences to say nothing; the second says what the project does immediately.

## API doc: hedged instruction

- Before: `คุณอาจจะต้องพิจารณาตั้งค่า API key ของท่านในไฟล์ .env ก่อนที่จะเริ่มต้นใช้งาน`
- After: `ตั้งค่า API key ในไฟล์ .env ก่อนเริ่มใช้งาน`
- Why: API docs need literal, testable instructions: "you might want to consider" isn't an instruction.

## Public changelog: internal detail instead of user benefit

- Before: `ปรับปรุง indexing algorithm ของระบบค้นหาให้มีประสิทธิภาพมากขึ้น`
- After: `ค้นหาสินค้าได้เร็วขึ้น`
- Why: a customer-facing changelog entry (see `../contexts/customer-facing.md`) should lead with what the user experiences, not the internal implementation.

## Enterprise release note: needs a more measured register than a consumer changelog

- Before (too casual for this audience): `อัปเดตใหญ่มาแล้ว! เร็วขึ้นเยอะ บั๊กหายเพียบ`
- After: `เวอร์ชันนี้ปรับปรุงประสิทธิภาพการประมวลผลข้อมูลและแก้ไขข้อบกพร่อง 8 รายการที่รายงานโดยลูกค้า`
- Why: an enterprise B2B audience reading a release note expects a measured, specific register. It is the same "what changed and why it matters" content, calibrated differently than a consumer app's in-app "what's new" (see `../contexts/documentation.md`).
