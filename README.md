# thai-writing-skills

ชุด Agent Skill สำหรับเขียนและแก้ภาษาไทยให้อ่านเป็นธรรมชาติ สื่อความหมายตรงกับต้นฉบับ ไม่ใช่แปลจากอังกฤษตรงตัวหรือฟังดูเป็น AI เขียน repo นี้มี 3 skill

- `thai-writer` ใช้กับภาษาไทยทุกงาน ตั้งแต่อีเมล แชท บทความ รายงาน หนังสือราชการ ไปจนถึงสไลด์
- `thai-product-writer` เป็นส่วนเสริมสำหรับงานซอฟต์แวร์โปรดักต์และงาน engineering ต้องติดตั้งคู่กับ `thai-writer`
- `thai-i18n` แก้ปัญหาภาษาไทยในโค้ด เช่น slug, ตัดคำ, วันที่ พ.ศ. และการเรียงลำดับ ใช้แยกได้

**"Product" คือ Software Product ไม่ใช่สินค้าขายของออนไลน์** skill `thai-product-writer` ไม่ครอบคลุมคำโฆษณา คำบรรยายสินค้า แคปชันขายของ (Shopee/Lazada/TikTok Shop/Facebook/IG) framework การตลาด (FAB/AIDA/PAS) หรือการเช็กกฎหมายโฆษณาไทย (อย./สคบ.) งานเหล่านั้นเป็นคนละโดเมน

ใช้ได้ทั้ง [Claude Code](https://claude.com/claude-code) และ [Codex CLI](https://github.com/openai/codex) เพราะเขียนตาม [Agent Skills spec](https://github.com/anthropics/skills) เดียวกัน

## ครอบคลุมอะไรบ้าง

### thai-writer

งานเขียนภาษาไทยทั่วไป ได้แก่ อีเมล แชท LINE/Slack คำตอบในแชท บทความ บล็อก โพสต์โซเชียล รายงาน หนังสือราชการ งานวิชาการ คู่มือ สรุปประชุม และสไลด์นำเสนอ (รวม speaker notes และการตัดบรรทัดภาษาไทย) มีกฎเรื่องเครื่องหมายและรูปแบบที่ทำให้ข้อความดูเหมือน AI เขียน เช่น em dash ลูกศรในประโยค ป้ายตัวหนาตามด้วย colon emoji นำบรรทัด และ Markdown เกินเนื้อหา

### thai-product-writer

งานในซอฟต์แวร์ ได้แก่ UX/UI copy (ปุ่ม, label, ฟอร์ม, validation/error, toast, notification, empty state, confirmation dialog, onboarding) code comment, git commit, pull request, requirement/acceptance criteria, business rule, เอกสารทางเทคนิค, README, release notes และข้อความถึงลูกค้าหรือทีมงาน

## สถาปัตยกรรม

```
Meaning > Context > Audience > Tone > Natural Thai > Punctuation & Formatting > AI-Smell Review > NO_CHANGE
```

นี่คือลำดับของ `thai-writer` ส่วน `thai-product-writer` เพิ่มขั้น Product Terminology ระหว่าง Audience กับ Tone

Context-first คือตัดสินใจเรื่อง context และ audience ก่อนเสมอ แล้วค่อยเลือกคำ ไม่ใช่ "ตัวจับ AI-Thai" ที่ทำงานแบบ context-blind และ**ไม่มี blacklist คำต้องห้าม** ทุก pattern ประเมินจากบริบท ความถี่ ความซ้ำซ้อน ระดับภาษา และผู้อ่าน ไม่ใช่จากตัวคำ

## โครงสร้างโปรเจกต์

```
.claude/skills/thai-writer/           skill ภาษาไทยทุกงาน (SKILL.md + core/ + contexts/ + review/ + examples/)
.claude/skills/thai-product-writer/   ส่วนเสริมงานซอฟต์แวร์ (SKILL.md + audiences.md + contexts/ + terminology/ + examples/)
.codex/skills/                        mirror ของทั้งสอง skill สำหรับ Codex CLI
research/                             งานวิจัยที่ skill อิงอยู่ ทุก claim แท็ก source-backed/observed/decision/open-question
benchmark/                            evaluation rubric (7 มิติ) + case ตั้งต้น (ดูเป้าหมาย 100 case ในไฟล์)
scripts/check_skills.py               ตัวตรวจโครงสร้าง skill และลิงก์ในไฟล์
```

รายละเอียดไฟล์ในสกิลดูที่ [`.claude/skills/thai-writer/SKILL.md`](.claude/skills/thai-writer/SKILL.md) และ [`.claude/skills/thai-product-writer/SKILL.md`](.claude/skills/thai-product-writer/SKILL.md) งานวิจัยพื้นฐานดูที่ [`research/README.md`](research/README.md)

### [`thai-i18n`](.claude/skills/thai-i18n/SKILL.md)

คนละเรื่อง นี่คือปัญหาภาษาไทย**ในโค้ดเชิงเทคนิค** (slug/URL แบบ RTGS, ตัดคำสำหรับ line-wrap/search, วันที่ พ.ศ./ค.ศ. ตาม CLDR, sort) ไม่ใช่การเขียนข้อความ ไม่ใช่ core ของ `thai-product-writer`

## ติดตั้ง

Clone repo ก่อน

```bash
git clone https://github.com/Martinnezsavemaiwai/thai-writing-skills.git
cd thai-writing-skills
```

### Claude Code

คัดลอก skill ไปไว้ในโฟลเดอร์ skill ส่วนตัว แล้วใช้ได้ทุกโปรเจกต์

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/thai-writer .claude/skills/thai-product-writer .claude/skills/thai-i18n ~/.claude/skills/
```

ถ้าอยากใช้เฉพาะโปรเจกต์เดียว ให้คัดลอกไปที่ `.claude/skills/` ของโปรเจกต์นั้นแทน

### Codex CLI

```bash
mkdir -p ~/.codex/skills
cp -r .codex/skills/thai-writer .codex/skills/thai-product-writer .codex/skills/thai-i18n ~/.codex/skills/
```

**สำคัญ:** `thai-product-writer` อ้างไฟล์ของ `thai-writer` ผ่าน path แบบ `../thai-writer/` สองโฟลเดอร์นี้จึงต้องอยู่ในโฟลเดอร์ skill เดียวกันเสมอ

บน Windows ใช้คำสั่งข้างบนใน Git Bash ได้เลย

## ตรวจ repo

```
python scripts/check_skills.py
```

## สถานะ

งานวิจัยพื้นฐาน (`research/`) มาจาก web research จริง (ไม่ใช่เดา) แต่ **ยังไม่ผ่านการตรวจกับ native speaker reviewer อย่างเป็นระบบ** และ benchmark มี 46 case ยังไม่ครบ 100 case ตามเป้า ดู open questions เต็มใน [`research/README.md`](research/README.md) ก่อนยึดกฎใดเป็นกฎตายตัว

## License

MIT ดู [LICENSE](LICENSE)
