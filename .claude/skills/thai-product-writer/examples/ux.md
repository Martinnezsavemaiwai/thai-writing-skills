# Examples: UX/UI

## Button

- Before: `ดำเนินการต่อไปยังขั้นตอนถัดไป`
- After: `ถัดไป`
- Why: `ดำเนินการ...ขั้นตอนถัดไป` pads a one-word action with formal/bureaucratic phrasing; a button reads at a glance.

## Validation message

- Before: `ข้อมูลที่ท่านกรอกไม่ถูกต้อง กรุณาตรวจสอบอีกครั้ง`
- After: `เบอร์โทรต้องมี 10 หลัก`
- Why: "not correct, please check again" is technically true and completely unhelpful. Say what's actually wrong.

## Error message (routine)

- Before: `ระบบไม่สามารถทำการบันทึกข้อมูลของท่านได้เนื่องจากเกิดข้อผิดพลาดขึ้น`
- After: `บันทึกไม่สำเร็จ ลองอีกครั้ง`
- Why: `ทำการบันทึก`, `ท่าน`, and `เนื่องจากเกิดข้อผิดพลาดขึ้น` (a cause with no actual information) all pad a message that a user reads for half a second before tapping retry.

## Error message (security/urgent: different register on purpose)

- Before: `เราตรวจพบว่าอาจมีความพยายามในการเข้าถึงบัญชีของคุณโดยไม่ได้รับอนุญาตค่ะ กรุณาดำเนินการเปลี่ยนรหัสผ่านของคุณโดยเร็วที่สุดนะคะ`
- After: `พบความพยายามเข้าสู่ระบบที่ผิดปกติ เปลี่ยนรหัสผ่านทันที`
- Why: this isn't just trimming: dropping the particles (ค่ะ/นะคะ) and going to a direct imperative is the *correct* register for a security warning, not a defect. See `../../thai-writer/core/anti-ai.md`.

## Confirmation dialog

- Before: title `ยืนยันการดำเนินการ`, buttons `ตกลง` / `ยกเลิก`
- After: title `ลบรายการนี้ใช่ไหม`, buttons `ลบ` / `ไม่ลบ`
- Why: the original title doesn't say what's being confirmed; the buttons don't answer the question they're attached to. The fix makes title and buttons a real question-and-answer pair.

## Empty state

- Before: `ขออภัย ขณะนี้ยังไม่มีข้อมูลรายการโปรดของท่านปรากฏอยู่ในระบบ ท่านสามารถเพิ่มรายการโปรดได้โดยการกดที่ไอคอนรูปหัวใจ`
- After: `ยังไม่มีรายการโปรด กดรูปหัวใจเพื่อเพิ่ม`
- Why: says the same two things (nothing here, here's how to add one) in a third of the words, no apology needed for an empty list.
