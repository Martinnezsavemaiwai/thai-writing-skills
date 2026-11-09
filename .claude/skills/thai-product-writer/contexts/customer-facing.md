```yaml
context: customer-facing
purpose: text addressed directly to a customer/end user outside the in-product UI itself, such as support replies, help center articles, public changelogs
audience: Customer, End User
desired_tone: Professional-Conversational; formal register locked for regulated-industry correspondence (see core/tone.md)
desired_length: as short as fully answering the customer's actual question allows
must_preserve: exact steps given to resolve an issue, any commitment made (refund terms, timelines)
common_mistakes: register_mixing, excessive_formal_connectors, over_explanation
```

This is distinct from `ux-writing.md`: that's text embedded in the product's own screens; this is text written *to* a specific customer or a general public audience outside the live UI (a support reply, a help article, a public-facing changelog entry).

## Support replies

State the resolution/next step clearly, don't bury it under apology or formal preamble. Match the customer's register somewhat: a casual question doesn't need a maximally formal reply, and a frustrated/urgent message doesn't need excessive cheerfulness.

## Help center articles

Same clarity/conciseness rules as documentation (`documentation.md`), but written for a non-technical reader. Avoid internal/technical terminology the customer wouldn't recognize; translate it to what the customer actually sees in the product (use the product's terminology glossary, `../terminology/terminology.md`, not internal engineering names).

## Public changelog / "what's new"

Distinct from the release-notes entry in `documentation.md` in audience: this is consumer-facing, not stakeholder-facing. Lead with the benefit to the user, not the internal implementation detail: "ตอนนี้ค้นหาเร็วขึ้น" not "ปรับปรุง indexing algorithm ของระบบค้นหา."

## Regulated-industry correspondence

Banking, insurance, and similarly regulated customer correspondence keeps a consistently formal register throughout. This is one of the contexts where `ดังกล่าว`, `ในกรณีที่`, `ทั้งนี้` are the expected, correct register, not a smell (see `../../thai-writer/core/anti-ai.md`). Don't "friendly-up" this content to match a general brand-voice preference.
