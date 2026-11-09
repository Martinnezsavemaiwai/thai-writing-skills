# Examples: Engineering

## Code comment: restates what, should be deleted or rewritten

- Before: `// เพิ่มค่า count ขึ้นทีละ 1 หน่วย` above `count++;`
- After: (delete the comment)
- Why: no rewrite makes this earn its place; the code says everything the comment says.

## Code comment: restates what, has a real "why" underneath

- Before: `// ตรวจสอบว่ามีข้อมูลหรือไม่เพื่อดำเนินการในขั้นตอนถัดไป` above `if (!order) return null;`
- After: `// ไม่มี Order ก็ไม่ต้องแสดงตาราง`
- Why: the original narrates the visible code; the fix states the actual reason (why returning null here is correct), which the code alone can't convey.

## Git commit

- Before: `ทำการแก้ไขปัญหาเกี่ยวกับการคำนวณราคาสินค้าที่ไม่ถูกต้องเมื่อมีการใช้ส่วนลดหลายรายการพร้อมกัน`
- After: `แก้: คำนวณราคาผิดเมื่อใช้ส่วนลดซ้อนกันหลายรายการ`
- Why: same information, imperative mood, no `ทำการ` padding, and matches the terseness of a normal commit subject line.

## Pull request description

- Before: `ใน PR นี้จะทำการปรับปรุงฟังก์ชันการค้นหาสินค้าให้มีประสิทธิภาพมากยิ่งขึ้น โดยได้ทำการเปลี่ยนแปลง query ที่ใช้ในการดึงข้อมูลจากฐานข้อมูล`
- After: `ค้นหาสินค้าช้าเพราะ query เดิมสแกนทั้งตาราง เปลี่ยนไปใช้ index ที่มีอยู่แล้วแทน\n\nวิธีทดสอบ: ค้นหาคำที่มีผลลัพธ์เกิน 1000 รายการ เทียบเวลาก่อน/หลัง`
- Why: leads with *why* (search was slow, and the actual cause) instead of announcing that improvements will be made; adds a concrete test step the diff alone doesn't provide.

## Requirement / acceptance criterion

- Before: `ระบบต้องสามารถจัดการกับกรณีที่ผู้ใช้ยังไม่ได้ยืนยันอีเมลของตนเองในขณะที่พยายามเข้าสู่ระบบได้อย่างเหมาะสม`
- After:
  ```
  Given ผู้ใช้ยังไม่ยืนยันอีเมล
  When ผู้ใช้พยายามเข้าสู่ระบบ
  Then ระบบแสดงข้อความให้ยืนยันอีเมลก่อน
  ```
- Why: "handle appropriately" isn't testable; the Given/When/Then version names the exact precondition, trigger, and expected behavior; see `../contexts/requirements.md` on keeping the labels in English.
