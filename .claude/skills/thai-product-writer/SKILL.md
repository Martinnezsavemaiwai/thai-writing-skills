---
name: thai-product-writer
description: |
  ตรวจและแก้ข้อความภาษาไทยใน "ซอฟต์แวร์โปรดักต์" ให้อ่านเป็นธรรมชาติ สื่อความหมาย
  ตรงกับต้นฉบับ ไม่ใช่แปลจากอังกฤษตรงตัวหรือฟังดูเป็น AI เขียน ใช้กับ UX copy
  (ปุ่ม, label, ฟอร์ม, ข้อความ validation/error, toast, notification, empty state,
  confirmation dialog, onboarding), code comment, git commit, pull request,
  requirement/acceptance criteria, business rule, เอกสารทางเทคนิค, README,
  release notes และข้อความสื่อสารกับลูกค้าหรือทีมงานภายใน "Product" ในที่นี้คือ
  ซอฟต์แวร์โปรดักต์ ไม่ใช่สินค้าขายของออนไลน์ งานเขียนคำโฆษณา/คำบรรยายสินค้า
  ขายของไม่อยู่ใน scope ของ skill นี้
license: MIT
metadata:
  version: "0.3.0"
---

# Thai Product Writer: เขียน/แก้ภาษาไทยสำหรับซอฟต์แวร์โปรดักต์ให้เป็นธรรมชาติ

skill นี้ช่วยให้ AI agent เขียนหรือแก้ข้อความภาษาไทยใน**ซอฟต์แวร์โปรดักต์และงาน engineering** ให้อ่านเป็นธรรมชาติเหมือนคนในทีมเขียนเอง ไม่ใช่แปลจากอังกฤษหรือมี pattern ที่ทำให้ดูเป็น AI เขียน โดยไม่เปลี่ยนความหมาย เงื่อนไข business rule หรือรายละเอียดทางเทคนิคของต้นฉบับ

**"Product" ในที่นี้คือ Software Product** หมายถึง UI, ฟีเจอร์, โค้ด, เอกสาร, และการสื่อสารรอบซอฟต์แวร์ **ไม่ใช่สินค้าขายของออนไลน์** งานเขียนคำโฆษณา คำบรรยายสินค้า แคปชันขายของ (Shopee/Lazada/TikTok Shop/Facebook/IG), framework การตลาด (FAB/AIDA/PAS) และการเช็กกฎหมายโฆษณาไทย (อย./สคบ.) **ไม่อยู่ใน scope ของ skill นี้**

ถ้าโจทย์คือปัญหาภาษาไทย**ในโค้ดเชิงเทคนิค** (slug/URL, ตัดคำ, วันที่ พ.ศ./ค.ศ., sort) ไม่ใช่การเขียนข้อความ ให้ใช้ skill [thai-i18n](../thai-i18n/SKILL.md) แทน เพราะคนละเรื่องกัน ไม่ใช่ core ของ skill นี้

skill นี้ต่อยอดจาก [thai-writer](../thai-writer/SKILL.md) ใช้หลักใน core/ และ review/ ของ thai-writer เสมอ (ภาษาไทยธรรมชาติ, เครื่องหมาย, การจัดรูปแบบ, AI-smell) แล้วเพิ่มบริบทของงานซอฟต์แวร์จากไฟล์ในนี้

## สถาปัตยกรรมหลัก: ตัดสินใจตามลำดับนี้เสมอ

```
Meaning > Context > Audience > Product Terminology > Tone > Natural Thai > Punctuation & Formatting > AI-Smell Review > จำเป็นต้องแก้ไหม (NO_CHANGE)

Meaning                   ความหมายและเจตนาของต้นฉบับ
Context                   ใช้ที่ไหน เช่น ปุ่ม, error, commit, README
Audience                  ผู้อ่านคือใคร: end user, dev, PM, ลูกค้า
Product Terminology       ศัพท์เฉพาะของโปรดักต์ต้องตรงกันทั้งระบบ
Tone                      ทางการหรือเป็นกันเองแค่ไหน ตัดสินจาก context กับ audience ไม่ใช่ความชอบ
Natural Thai              เรียบเรียงเป็นภาษาไทยที่คนอ่านจริง ไม่แปลคำต่อคำจากอังกฤษ
Punctuation & Formatting  เครื่องหมายและรูปแบบพอดีกับช่องทาง ไม่มี em dash หรือลูกศรในเนื้อความ
AI-Smell Review           ตรวจ pattern ที่ทำให้ดูเป็น AI เขียนก่อนส่ง
จำเป็นต้องแก้ไหม (NO_CHANGE)  ถ้าต้นฉบับผ่านทุกขั้นแล้ว ตอบว่าไม่ต้องแก้
```

**กติกา:** อย่ากระโดดไปแก้คำที่ขั้นตอน "Natural Thai" หรือ "AI-Smell Review" ก่อนที่จะรู้ context/audience เพราะคำเดียวกันเป็นปัญหาในบริบทหนึ่งแต่ใช้ได้ปกติในอีกบริบทหนึ่ง (ดู [core/anti-ai.md](../thai-writer/core/anti-ai.md)) skill นี้เป็น **context-first** ไม่ใช่ "ตัวจับ AI-Thai" ที่ทำงานแบบ context-blind

## โครงสร้างไฟล์

| หมวด | ไฟล์ | ใช้เมื่อ |
|---|---|---|
| หลักการพื้นฐาน | [core/meaning-preservation.md](../thai-writer/core/meaning-preservation.md) | ทุกงาน เช็กก่อนว่าอะไรห้ามเปลี่ยน |
| | [core/natural-thai.md](../thai-writer/core/natural-thai.md) | โครงสร้างประโยค/คำที่ทำให้เป็นไทยธรรมชาติ |
| | [core/clarity.md](../thai-writer/core/clarity.md) | ทำให้อ่านแล้วเข้าใจทันที ไม่กำกวม |
| | [core/conciseness.md](../thai-writer/core/conciseness.md) | ตัดส่วนเกินโดยไม่กลายเป็นห้วน/กันเองเกินไป |
| | [core/anti-ai.md](../thai-writer/core/anti-ai.md) | วิธีตัดสินว่าอะไรคือ "AI-smell" แบบดูบริบท ไม่ใช่ blacklist |
| | [core/tone.md](../thai-writer/core/tone.md) | Audience ทั่วไป + Tone spectrum ใช้ตัดสินระดับภาษาตาม context×audience |
| | [audiences.md](audiences.md) | ตาราง 9 กลุ่มผู้อ่านสำหรับงานซอฟต์แวร์ และ context×audience |
| บริบทงาน | [contexts/ux-writing.md](contexts/ux-writing.md) | ปุ่ม, label, ฟอร์ม, validation/error, empty state, confirmation dialog, onboarding |
| | [contexts/notifications.md](contexts/notifications.md) | toast, push/email notification, system alert |
| | [contexts/code-comments.md](contexts/code-comments.md) | comment ในโค้ด |
| | [contexts/commits.md](contexts/commits.md) | ข้อความ git commit ภาษาไทย |
| | [contexts/pull-requests.md](contexts/pull-requests.md) | PR title/description |
| | [contexts/requirements.md](contexts/requirements.md) | requirement, acceptance criteria, business rule |
| | [contexts/documentation.md](contexts/documentation.md) | README, เอกสารเทคนิค, release notes |
| | [contexts/customer-facing.md](contexts/customer-facing.md) | ข้อความถึงลูกค้า/ผู้ใช้จริง (support, changelog สาธารณะ) |
| ศัพท์ | [terminology/terminology.md](terminology/terminology.md) | วิธีเลือก/รักษาความสม่ำเสมอของศัพท์เฉพาะโปรดักต์ |
| | [terminology/glossary.example.yaml](terminology/glossary.example.yaml) | ตัวอย่างโครง glossary ให้ทำสำเนาไปปรับใช้ต่อโปรเจกต์ |
| ตรวจก่อนส่ง | [review/review-checklist.md](../thai-writer/review/review-checklist.md) | checklist สุดท้ายก่อนส่งคำตอบ |
| | [review/thai-ai-smells.md](../thai-writer/review/thai-ai-smells.md) | รายการ pattern (ไม่ใช่ blacklist คำ) พร้อมตัวอย่างก่อน/หลัง |
| ตัวอย่าง | [examples/ux.md](examples/ux.md), [examples/engineering.md](examples/engineering.md), [examples/business.md](examples/business.md), [examples/documentation.md](examples/documentation.md) | ตัวอย่างจริงแยกตามหมวด |

## ขั้นตอนการทำงาน

1. **หา context + audience ก่อนแก้คำใดๆ** ข้อความนี้อยู่ตรงไหนของ UI/โค้ด/เอกสาร ใครเป็นคนอ่าน (end user ทั่วไป, developer ในทีม, PM, ลูกค้า B2B) แล้วเปิดไฟล์ `contexts/*.md` ที่ตรงกับงาน
2. **เช็ก meaning-preservation ก่อนเรียบเรียงใหม่** ระบุว่าอะไรคือข้อเท็จจริง/เงื่อนไข/business rule ที่ห้ามเปลี่ยน (ดู [core/meaning-preservation.md](../thai-writer/core/meaning-preservation.md)) ถ้าข้อความกำกวมจนไม่รู้ความหมายจริง ให้ถามผู้ใช้แทนการเดา
3. **เช็กศัพท์เฉพาะ** ถ้าโปรเจกต์มี glossary ให้ยึดตามนั้น ถ้าไม่มีให้เสนอศัพท์ที่สอดคล้องกับที่เคยใช้ในโค้ด/UI เดิม (ดู [terminology/terminology.md](terminology/terminology.md))
4. **เลือกโทนจาก context×audience** ไม่ใช่ความชอบส่วนตัว (ดู [core/tone.md](../thai-writer/core/tone.md) และ [audiences.md](audiences.md)) ความเป็นทางการปรับตาม severity/context ได้ เช่น ข้อความเตือนความปลอดภัยตัดคำลงท้ายสุภาพออกได้โดยไม่ใช่ปัญหา
5. **เรียบเรียงตาม natural-thai + clarity + conciseness** เขียนใหม่ทั้งประโยค ไม่ใช่แทนคำทีละคำ
6. **ตรวจเครื่องหมายและรูปแบบ** ค้นหา `—` และ `→` แล้วดูว่ารูปแบบพอดีกับช่องทาง (ดู [core/punctuation.md](../thai-writer/core/punctuation.md) และ [core/formatting.md](../thai-writer/core/formatting.md))
7. **ตรวจ AI-smell ตามบริบท ไม่ใช่ตามรายการคำต้องห้าม** ไล่ตาม [review/thai-ai-smells.md](../thai-writer/review/thai-ai-smells.md) แล้วถามตัวเองว่า pattern นี้ผิดธรรมชาติ**ในบริบทนี้**จริงไหม ไม่ใช่ผิดเพราะเคยเห็นในข้อความ AI ที่อื่น
8. **ถามตัวเองก่อนว่าต้องแก้จริงไหม** ถ้าข้อความเดิมผ่านทุกข้อข้างบนอยู่แล้ว (ความหมายครบ, เข้ากับ context/audience, ศัพท์สอดคล้อง, โทนถูก, ภาษาธรรมชาติ, ไม่มี AI-smell ที่ผ่านการเช็กบริบทแล้ว) ให้ตอบว่า**ไม่ต้องแก้** แทนการแก้เพราะรู้สึกว่า "น่าจะต้องมีอะไรให้แก้บ้าง" เพราะ skill ที่แก้ทุกอย่างเสมอก็ทำงานผิดพลาดพอๆ กับ skill ที่ไม่แก้อะไรเลย (ดู [core/anti-ai.md](../thai-writer/core/anti-ai.md), [benchmark/README.md](../../../benchmark/README.md))
9. **ตรวจซ้ำด้วย [review/review-checklist.md](../thai-writer/review/review-checklist.md)** ก่อนส่งคำตอบ

## ตัวอย่างที่กำหนดพฤติกรรม: code comment ต้องอธิบาย "ทำไม" ไม่ใช่ "ทำอะไร"

โค้ดที่อ่านออกอยู่แล้วบอก "ทำอะไร" ได้เอง comment ที่ดีต้องเติมสิ่งที่โค้ดบอกไม่ได้ คือเหตุผล/บริบท/ข้อจำกัด

```ts
// ไม่ดี: บอกซ้ำสิ่งที่โค้ดทำอยู่แล้ว
// ตรวจสอบว่ามีข้อมูลหรือไม่เพื่อดำเนินการในขั้นตอนถัดไป
if (!order) return null;

// ดีกว่า: บอกเหตุผลที่โค้ดไม่ได้บอกเอง
// ไม่มี Order ก็ไม่ต้องแสดงตาราง
if (!order) return null;
```

ถ้าโค้ดอ่านเข้าใจได้เองอยู่แล้วโดยไม่ต้องมี comment เลย ให้**เสนอลบ comment** แทนการเขียนใหม่ ดูรายละเอียดเพิ่มใน [contexts/code-comments.md](contexts/code-comments.md) (ถ้างานคือ "ทำความสะอาด comment ภาษาอังกฤษที่ AI เขียน" ไม่เกี่ยวกับภาษาไทย ให้ใช้ skill `code-comment-humanizer` แทน)

## กติกาการออกแบบที่ต้องยึด

- **ห้ามสร้าง blacklist คำต้องห้าม** คำอย่าง "ดำเนินการ", "อย่างไรก็ตาม", "ดังกล่าว", "ในกรณีที่", "ทั้งนี้" **ไม่ใช่ "คำ AI" โดยอัตโนมัติ** ต้องประเมินจากบริบท ความถี่ ความซ้ำซ้อน ระดับภาษา และโครงสร้างประโยครอบข้าง (รายละเอียดใน [core/anti-ai.md](../thai-writer/core/anti-ai.md))
- **ห้ามเปลี่ยน business rule/ความหมายทางเทคนิค** แม้จะทำให้อ่านลื่นขึ้นก็ตาม (ดู [core/meaning-preservation.md](../thai-writer/core/meaning-preservation.md))
- **กระชับได้ แต่ห้ามกันเองเกินบริบท** ตัดคำฟุ่มเฟือยได้ แต่ระดับภาษาต้องยังตรงกับ audience เดิม (ดู [core/conciseness.md](../thai-writer/core/conciseness.md))

## กฎที่ยังต้องการงานวิจัย/ตรวจสอบเพิ่ม

ทุกไฟล์ในนี้อิงงานวิจัยจริง (WebSearch/WebFetch ของแหล่งอ้างอิงจริง ไม่ใช่เดา) เก็บไว้ที่ [research/](../../../research/) ทุก claim ในนั้นแท็กเป็น `[Source-backed]` / `[Observed]` / `[Project decision]` / `[Open question]` / `[Hypothesis]` ไฟล์ในสกิลนี้ (core/contexts/review) เป็นเวอร์ชันที่เอาไปใช้จริง ส่วนที่มีข้อความ `[Open question]` หรือ "ยังไม่มีแหล่งอ้างอิง" หมายถึงยังเป็นสมมติฐาน **ไม่มี pattern ไหนผ่านการตรวจกับ native speaker reviewer อย่างเป็นระบบ** ดู [research/README.md](../../../research/README.md) สำหรับรายการ open question เต็ม

## วิธีส่งคำตอบ

1. **ข้อความที่แก้/เขียนใหม่** (เวอร์ชันสุดท้าย) หรือ **"ไม่ต้องแก้"** พร้อมเหตุผลสั้นๆ ถ้าข้อความเดิมถูกต้องอยู่แล้ว (ดูข้อ 8 ในขั้นตอนการทำงานด้านบน) นี่คือคำตอบที่ถูกต้องพอๆ กับการแก้ ไม่ใช่การหลบงาน
2. **สรุปการแก้แบบสั้น** แยกเป็น: (ก) แก้เพราะ meaning ต้นฉบับคลาดเคลื่อน (ข) แก้เพราะไม่เข้ากับ context/audience (ค) แก้เพราะ AI-smell โดยข้ามหมวดที่ไม่มีอะไรจะพูด
3. ถ้าผู้ใช้ขอแค่ "แก้ให้เลย" แบบสั้นๆ ให้ส่งแค่ข้อความที่แก้ ไม่ต้องแนบสรุป
