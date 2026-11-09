```yaml
context: requirements
purpose: specify what the product must do, testably, for developers and QA to build/verify against
audience: Product Manager, Developer, QA, Designer
desired_tone: Neutral-Technical, precise
desired_length: one condition per statement; as long as precision requires, no longer
must_preserve: every condition, every precondition, exact thresholds/values
common_mistakes: over_explanation (rule mixed with rationale), redundant_verb_construction
```

## Acceptance criteria: describe behavior, not implementation

`[Source-backed principle]` TestQuality, AltexSoft (see `../../../../research/business-writing-research.md`): criteria should name user-visible behavior ("เมื่อผู้ใช้ล็อกอินสำเร็จ" not "เมื่อ UserService คืนค่า JWT ที่ถูกต้อง"), be atomic (one scenario per criterion: split happy path from error/edge cases rather than branching inside one), and avoid untestable qualifiers ("เร็ว", "ใช้งานง่าย") in favor of a verifiable condition.

- Untestable: `ระบบต้องตอบสนองเร็ว`
- Testable: `ระบบต้องแสดงผลภายใน 2 วินาที`

## Given/When/Then: keep the labels in English

`[Project decision]`: write the content clause in natural Thai but keep `Given`/`When`/`Then` as structural labels, not translated into `เมื่อ`/`ถ้า`/`ดังนั้น`. They function as a recognized convention marker, not as sentence prose; mixing label-language with content-language is fine here the same way English technical keywords survive untranslated elsewhere in Thai technical writing (see `../terminology/terminology.md`). `[Open question]`: whether the project's actual BDD tooling localizes these keywords. Check the project's config rather than assuming.

```
Given ผู้ใช้ยังไม่ยืนยันอีเมล
When ผู้ใช้พยายามเข้าสู่ระบบ
Then ระบบแสดงข้อความให้ยืนยันอีเมลก่อน
```

## Business rules: state the rule, separate the rationale

A rule should be a single unambiguous conditional. Don't fold the reason into the same sentence as the rule. The rule needs to stay stable and grep-able even if the justification changes later.

- Mixed: `ยกเลิกออเดอร์ไม่ได้หลัง 24 ชั่วโมงเพราะระบบคลังสินค้าตัดสต๊อกไปแล้วและการคืนสต๊อกทำได้ยาก`
- Separated:
  - Rule: `ยกเลิกออเดอร์ได้เฉพาะภายใน 24 ชั่วโมงหลังสั่งซื้อ`
  - Note (separate field/comment): เหตุผล: ระบบคลังตัดสต๊อกอัตโนมัติหลัง 24 ชั่วโมง

`ในกรณีที่` and similar formal conditionals are genuinely the right register here. This is exactly the context where that phrasing earns its place (see `../../thai-writer/core/anti-ai.md`).

## Preconditions stated explicitly, even when "obvious"

An implicit precondition becomes ambiguous the moment the code changes under it. State it, even if today it seems redundant with common sense.
