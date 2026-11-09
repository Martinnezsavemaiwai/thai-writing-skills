# Audience and Tone

Two pipeline stages (`Audience`, `Tone` in SKILL.md) collapsed into one file because tone is a direct function of audience + context, so there's no independent "tone" decision to make once you know who's reading and where.

## Audience model

| Audience | ตัวอย่างงาน | ระดับภาษาที่มักใช้ |
|---|---|---|
| เพื่อน/คนสนิท | แชท, โพสต์ส่วนตัว | กันเอง |
| เพื่อนร่วมงาน | อีเมลภายใน, Slack, สรุปประชุม | กลาง ถึง กันเอง |
| หัวหน้า/ผู้บริหาร | รายงาน, อีเมลขออนุมัติ, สไลด์นำเสนอ | สุภาพ ตรงประเด็น |
| ลูกค้า/คนนอกองค์กร | อีเมลตอบลูกค้า, ใบเสนอราคา | สุภาพ เป็นทางการพอประมาณ |
| ผู้อ่านทั่วไป | บทความ, บล็อก, โพสต์เพจ | กลาง อ่านง่าย |
| หน่วยงานราชการ/งานวิชาการ | หนังสือราชการ, รายงานวิจัย | ทางการ |

**ทางการไม่เท่ากับมืออาชีพ** ข้อความถึงหัวหน้าหรือเพื่อนร่วมงานสุภาพและตรงประเด็นได้โดยไม่ต้องใช้ภาษาราชการ ความผิดพลาดที่พบบ่อยคือเหมาว่าทุกงานธุรกิจต้องทางการสุดทุกครั้ง ไม่ดูว่าใครเป็นคนอ่านจริงๆ

## Tone spectrum

The scale runs from Formal through Professional, Neutral and Conversational to Friendly, plus two register-locked variants: Technical (precision over personality, e.g. API docs and error codes) and Executive (concise, outcome-first).

ระดับภาษาเลือกจากบริบทและผู้อ่าน ไม่ใช่จากความชอบส่วนตัว

งานซอฟต์แวร์ใช้ตาราง audience ใน [thai-product-writer/audiences.md](../../thai-product-writer/audiences.md)

## Second person without over-using "คุณ"

English UX-writing guidance says "always address the user directly, second person, active voice" (Microsoft, Material Design; see `../../../../research/ux-writing-research.md`). The intent (make the user the actor) transfers to Thai. The literal mechanism doesn't: Thai naturally omits a recoverable subject, and forcing `คุณ` into every sentence to satisfy the English rule produces the over-explicit-subject smell (see `../review/thai-ai-smells.md`). Apply the intent, not the pronoun count. `[Open question: needs native-speaker validation]`: exactly how sparse subject use can go before a piece stops feeling like it's addressed to the reader at all.

## Directness is a separate axis from formality

`[Source-backed principle, Thai-specific]` Thailand is documented in intercultural-communication research as a high-context culture where a direct "no" or direct disagreement is uncommon, and "เกรงใจ" (kreng jai: regard for others' feelings, avoiding imposition) is repeatedly identified as shaping Thai workplace communication, especially disagreement and feedback to a superior. Treat this as a real, repeatedly-observed factor, not a settled quantified finding; see `../../../../research/business-writing-research.md` for the caveat on how rigorous this literature actually is.

This means a Thai internal message that reads as "too blunt" may not be a formality problem, it may be a **directness** problem, and those are different axes. `[PROJECT DECISION]`: this distinction matters differently depending on what's being written:

- **Requirements, business rules, acceptance criteria, error messages**: directness is a correctness requirement, full stop. `ยกเลิกออเดอร์ได้เฉพาะภายใน 24 ชั่วโมง` shouldn't get softened into `ปกติแล้วมักจะยกเลิกได้ถ้าเวลายังไม่เกิน 24 ชั่วโมง` (a hedge that makes a firm rule sound optional) just because indirectness feels more natural; see `../../thai-product-writer/contexts/requirements.md`, `clarity.md`.
- **Interpersonal content** (code review feedback to a peer, disagreement with a proposal, delivering bad news to a stakeholder) is exactly where some cultural softening is expected and appropriate; flattening it to blunt directness "for clarity" can read as needlessly harsh to a Thai reader in a way it wouldn't in English.
- **Everyday writing** splits the same way. A firm deadline in an email to a supplier stays firm: `ขอรับของภายในวันพุธที่ 20 ค่ะ ถ้าช้ากว่านี้จะไม่ทันงาน`, not `ถ้าเป็นไปได้อยากได้ประมาณกลางสัปดาห์ค่ะ`. Disagreeing with your boss's plan is where softening belongs: `แผนนี้น่าสนใจครับ แต่ผมยังห่วงเรื่องงบอยู่ ขอลองเสนออีกทางได้ไหมครับ` reads as respectful, while `แผนนี้งบเกิน` reads as abrupt.

`[Open question: needs native-speaker judgment]`: exactly where the line sits between these two cases in an ambiguous piece of text isn't something this research can settle from outside; when unsure which side a piece of text falls on, default to keeping rules/conditions direct and treat interpersonal framing around them as the part that can flex.

## When formality should NOT flex

Legal/compliance text, contracts, and regulated-industry customer correspondence (banking, insurance) keep a consistently formal register regardless of audience friendliness elsewhere in the product, because the formal register itself is doing legal work there, not just signaling politeness. Don't "conversationalize" this content just because the rest of the product is friendly.
