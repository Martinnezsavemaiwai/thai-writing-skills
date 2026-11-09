# Terminology Model — Research Notes

## Why a terminology model, not a fixed dictionary

- **[Source-backed principle]** The Microsoft Language Portal / Microsoft Terminology Collection exists precisely because unmanaged translation lets the same UI concept surface as three different terms across one product, which erodes user trust and creates support overhead — Microsoft's own localization teams use one shared terminology database internally to prevent this. This is the direct precedent for "one product, one term, everywhere." (Language Portal accessed via Microsoft Learn archive; Language Unlimited, "Microsoft Terminology Collection: What It Is And Uses")
- **[Source-backed principle]** The Microsoft Terminology Collection ships ~30,000 English IT terms with translations into ~100 languages, including exact strings pulled from shipped products (Windows, Office, Azure) — i.e. it's a record of terms *as actually used in production UI*, not a bilingual dictionary of plausible translations. That's the right model to imitate: a per-product glossary should be seeded from strings the product actually ships, not translated fresh from a general dictionary.
- **[Project decision]** Terminology correctness in this skill is **per-product**, not universal. Microsoft's database is one company's internal consistency mechanism across its own product line — it is a precedent for the *mechanism* (one shared glossary, one preferred term per concept, explicit avoid-list), not a source of "the correct Thai word" for any given term outside a Microsoft product. A Thai fintech app and a Thai logistics app can legitimately choose different Thai terms for the same English concept if their own existing UI already established a convention — the glossary should capture *this product's* established choice, not import an external one and call it correct.

## Proposed schema

```yaml
term: order                      # canonical English/product term (identifier)
preferred: "Order"                # how it appears in English UI/docs, if kept in English
thai:
  preferred: "รายการสั่งซื้อ"     # this product's chosen Thai rendering
  avoid:                          # near-synonyms this product has decided NOT to use, to prevent drift
    - "คำสั่งซื้อ"
definition: >
  A single purchase transaction initiated by a customer, containing one or more line items.
contexts:                         # where this term's meaning/rendering applies
  - checkout
  - order-history
  - customer-support
notes: >
  Distinguish from "cart" (ตะกร้าสินค้า), which is pre-purchase and never becomes an "order"
  until checkout completes.
```

Design choices, all **[Project decision]** unless noted:

- `thai.avoid` exists to record near-synonyms the team has already considered and rejected, not to become a general blacklist — it is scoped to one `term` entry, so rejecting "คำสั่งซื้อ" for `order` says nothing about that word elsewhere.
- `contexts` lets the same English term resolve differently depending on where it appears (a term can be "Order" in customer support chat but need a different, more formal rendering in a legal/receipt context) — see [example glossary](../.claude/skills/thai-product-writer/terminology/glossary.example.yaml) for a worked case.
- No `alternatives` field for the English side was added beyond `preferred` — **[Open question]**: whether English source terms need their own synonym-avoidance list (mirroring `thai.avoid`) wasn't resolved; deferred until a real project shows the need (YAGNI).

## Illustrative entries (not prescriptive — every product decides its own)

| term | keep English? | Thai (if translated) | notes |
|---|---|---|---|
| login | often kept as "Login" / "เข้าสู่ระบบ" both seen in the wild | เข้าสู่ระบบ | **[Observed pattern]**: major Thai apps split roughly evenly between keeping "Login"/"Log in" as a button label and using เข้าสู่ระบบ; both read as natural to Thai users today, so this is a per-product choice, not a correctness question |
| dashboard | usually kept in English | แดชบอร์ด (transliterated) if translated at all | **[Observed pattern]**: แดชบอร์ด is common in Thai B2B/SaaS products; a semantic translation (e.g. "หน้าภาพรวม") is also valid and arguably clearer for non-technical audiences — context-dependent |
| cart | rarely kept in English | ตะกร้าสินค้า / ตะกร้า | Well-established Thai e-commerce convention |
| checkout | mixed | ชำระเงิน / เช็คเอาท์ | ชำระเงิน emphasizes the payment step; เช็คเอาท์ is a transliteration seen on some platforms — pick one per product and stay consistent |
| notification | mixed | การแจ้งเตือน | Fairly settled convention across Thai apps |
| settings | rarely kept in English | การตั้งค่า / ตั้งค่า | Well-established |
| account | rarely kept in English | บัญชี / บัญชีผู้ใช้ | บัญชีผู้ใช้ is more explicit when "account" could be confused with a financial account in a fintech context |
| order | mixed | รายการสั่งซื้อ / คำสั่งซื้อ | Both seen in production Thai e-commerce/logistics apps — see schema example above for how one product should pick and record one |

**[Open question]**: this table is reasoned from general familiarity with Thai software UI conventions, not a systematic audit of specific live products (that audit is Phase 3 / `real-product-observations.md`, not yet done as a rigorous side-by-side screenshot comparison — treat entries here as plausible defaults to validate, not settled fact).

## Broadening the evidence base beyond one company

The original research cited only Microsoft's terminology practice. This pass adds standards-body and cross-industry evidence.

`[Source-backed principle]` **ISO 704 ("Terminology work — Principles and methods")** establishes the general principles for terminology work: the relationship between objects, concepts, definitions, and designations (terms), and general principles for forming terms and writing definitions — applicable across scientific, technical, legal, and administrative domains, not specific to software. This is the theoretical foundation the practical schema below sits on top of.

`[Source-backed principle]` **ISO 12620 ("Management of terminology resources — Data category specifications")** defines a standardized registry of *data categories* (the fields a term entry can have) so different terminology systems can interoperate. This is direct precedent for treating a term entry as a structured record with named fields, not a flat bilingual dictionary row.

`[Source-backed principle]` **TBX (TermBase eXchange), ISO 30042** is the actual industry-standard XML interchange format for termbases, originally from LISA (Localization Industry Standards Association), now an ISO standard. TBX is explicitly modular to support "blind interchange" — a receiving system doesn't need to contact the originator to interpret the data, because the data-category structure is standardized. This confirms the schema approach (structured, per-field, not a loose glossary) is the actual industry norm, not a project-specific invention.

`[Source-backed principle]` **Microsoft's current (2023, actively maintained) globalization guidance, "Manage terminology"** (directly fetched — see Sources) recommends every term entry include, per locale: Definition (minimum requirement), Source/context, Taxonomy (classification/grouping), Grammatical usage, Date, Author, Term status (approved/failed), Examples of use, Exclusions (terms that should NOT be used, including alternate spellings), Related terms, and **Product applicability** ("especially when different product lines use different translations for the same English term" — direct precedent for this project's `contexts` field). Microsoft explicitly recommends a dedicated terminology tool over a spreadsheet specifically because it should integrate with CAT tools via the TBX format.

`[Source-backed principle]` The termbase-vs-style-guide distinction is well-established industry practice, not a project invention: **a termbase manages *what words are approved* (vocabulary, at the segment/word level); a style guide manages *how the brand writes* (tone, punctuation, sentence structure, at the document level).** The two are complementary, not overlapping — this project's `terminology/` directory is explicitly termbase-shaped, while `contexts/`+`core/tone.md` are the style-guide-shaped half of the same overall system. This is a useful reframing: it clarifies why terminology.md and contexts/*.md are separate concerns rather than one merged file.

### Schema recommendation: `alternatives` and `audience` fields

The task's suggested schema adds `alternatives` and `audience` fields beyond what this project's existing schema (`term`/`preferred`/`thai.preferred`/`thai.avoid`/`definition`/`contexts`/`notes`) has. Evaluated against real practice:

`[PROJECT DECISION]` **Add `alternatives` — justified.** Microsoft's own field list includes "Related terms" and implicitly separates "the preferred term" from "other terms that exist and aren't wrong, just not preferred here" via its "Term status: approved or failed" field, which is a 3-way (preferred / acceptable-but-not-preferred / rejected), not the project's current 2-way (preferred / avoid). A near-synonym that's acceptable in some contexts but not the house choice (e.g. "ล็อกอิน" being understandable and not wrong, just not this product's pick) is a different case than a genuinely confusing/rejected term (e.g. "ออเดอร์" causing real ambiguity) — collapsing both into `avoid` loses that distinction. Recommend adding `alternatives` as a middle tier between `preferred` and `avoid`.

`[PROJECT DECISION]` **Add `audience` — justified, but scoped narrowly.** No source found an explicit "audience" field in a termbase schema by that name, but Microsoft's "Product applicability" field is doing adjacent work (the same underlying English term can resolve differently depending on where it's used), and this project's own research (`real-product-observations.md`) already found a real case — AIS dropping formality for security contexts — where the *audience/severity* of the surface, not the product, changed the register. Recommend adding `audience` as an optional per-context override (e.g. a term's `contexts` entry can specify a different Thai rendering for `internal` vs. `customer-facing` use, mirroring the internal_name/customer_facing_name pattern researched below) rather than a top-level field — this avoids forcing every term to declare an audience when most terms don't vary by one.

**Internal vs. customer-facing divergence:** no single named "internal_name/customer_facing_name" field standard was found in the sources reviewed, but the pattern is a natural extension of Microsoft's "Product applicability" mechanism (same term, different context key, different preferred rendering) — this project's existing `contexts` list field already supports this if a term needs two entries distinguished by context (e.g. `contexts: [internal-dashboard]` vs `contexts: [customer-support]`) rather than needing a wholly new field. `[Open question]`: whether this is common enough in practice to warrant being a named first-class field vs. just using two context-scoped entries — deferred, no evidence either way found.

## Schema stress-test: realistic ambiguous terms (Evidence Hardening pass)

Testing whether the schema can *express* real ambiguity — not resolving which Thai rendering is "correct," since per this file's own thesis there is no universal answer.

### Order / User / Account: competing renderings of one concept

These three are the schema's easy case — one concept, several near-synonym renderings, which is exactly what `thai.preferred`/`thai.alternatives`/`thai.avoid` already models:

```yaml
- term: order
  thai: { preferred: "รายการสั่งซื้อ", alternatives: ["ออเดอร์"], avoid: ["คำสั่งซื้อ"] }
- term: user
  thai: { preferred: "ผู้ใช้งาน", alternatives: ["ผู้ใช้"], avoid: ["สมาชิก"] }
  notes: >
    "สมาชิก" (member) is `avoid`, not `alternatives`, only if the product has no
    membership/subscription concept — if it does, "สมาชิก" is a genuinely different
    entity (a paying member), not a rejected synonym for "user." Verify before filing.
- term: account
  thai: { preferred: "บัญชีผู้ใช้", alternatives: [], avoid: ["บัญชี"] }
  notes: "บัญชี alone risks collision with a financial-account meaning in fintech contexts."
```

No schema change needed for these — the existing 3-tier field already does the job.

### Return: NOT competing renderings — three different concepts

`คืนสินค้า` (return a purchased product), `ขายคืน` (sell back / trade-in), and `คืนขวด` (return a deposit bottle) are **not synonyms of one term** — they're three different real-world actions that an English speaker happens to gloss with the same verb "return." Filing all three under one `term: return` entry with one competing `alternatives`/`avoid` list would be a modeling error: it would imply a product should pick just one, when a product with both a product-return policy and a bottle-deposit scheme genuinely needs both, simultaneously, as different features.

`[PROJECT_DECISION]`: the schema doesn't need a new field for this — it needs a **guidance rule in `terminology.md`**: before creating a `term` entry, confirm the English word actually names one concept in this product, not several. If "return" means two different things in the same product, that's two `term` entries with different `definition`s (e.g. `term: product-return` and `term: bottle-deposit-return`), not one term with contested rendering. This is a distinct failure mode from `inconsistent_terminology` (same concept, different renderings) — call it a **term-conflation risk**: different concepts, same English gloss, wrongly modeled as one entry.

### Internal vs. customer-facing: does the schema need a structural split?

The task proposes a more explicit schema than this project's current one:

```yaml
# Task's suggested shape
term: Order
internal: { preferred: Order }
customer_facing: { preferred: รายการสั่งซื้อ }
avoid: [คำสั่งซื้อ]
reason: product_convention
```

vs. the current schema's resolution (from the prior pass), which handles the same need via scoped `contexts` entries rather than new top-level fields:

```yaml
# Current schema's shape
term: order
thai: { preferred: "รายการสั่งซื้อ", avoid: ["คำสั่งซื้อ"] }
contexts: [checkout, order-history, customer-support]   # customer-facing rendering
notes: "internal admin dashboard uses \"Order\" untranslated — see internal-admin term entry"
```

`[PROJECT_DECISION, reaffirmed with reasoning this pass]`: **keep the flat `contexts` field; do not add top-level `internal`/`customer_facing` fields.** Reasoning:

1. **The binary is real but not universal.** Internal-vs-customer-facing is one common split, but not the only one a product needs (support-agent-facing vs. end-user-facing vs. admin-facing is a real three-way in some products). A schema with dedicated `internal`/`customer_facing` fields handles the 2-way case cleanly but doesn't generalize; `contexts` as a list already handles N-way splits without a schema change.
2. **No external terminology standard found in this pass names this as a first-class field either** — Microsoft's "Product applicability" field (the closest real-world precedent, see above) is itself a tag/context mechanism, not a fixed binary field.
3. **A naming convention closes the gap the task is actually worried about** — that a context-scoped list is less discoverable than an explicit field. Recommend (not a schema change, a documentation/convention change): **prefix context values to signal audience scope when relevant** — `internal-*` (e.g. `internal-admin`, `internal-dashboard`) vs. no prefix or an explicit `customer-*` prefix for external-facing contexts. This gets the discoverability benefit of the task's suggested schema without adding fields most terms will never use.

Worked example applying the convention:

```yaml
- term: order
  preferred: "Order"
  thai:
    preferred: "รายการสั่งซื้อ"
    avoid: ["คำสั่งซื้อ"]
  contexts: ["customer-checkout", "customer-order-history", "internal-admin-dashboard"]
  notes: >
    Customer-facing surfaces use "รายการสั่งซื้อ"; the internal admin dashboard keeps
    "Order" in English untranslated (internal tooling, English-speaking ops team) — the
    context prefix signals this without a separate top-level field.
```

`[Open question]`: this convention is untested on a real multi-context glossary of meaningful size; revisit if a real project shows the prefix convention getting unwieldy (e.g. needing internal/customer × multiple sub-audiences simultaneously — at that point a structured field may earn its keep after all).

## Sources

- [Microsoft Language Portal — Grokipedia summary](https://grokipedia.com/page/microsoft_language_portal)
- [Microsoft Terminology Collection: What It Is And Uses — Language Unlimited](https://www.languagesunlimited.com/microsoft-terminology-collection/)
- [Terminology management at Microsoft — Microsoft Learn archive](https://learn.microsoft.com/en-us/archive/blogs/terminology/terminology-management-at-microsoft)
- [Manage terminology — Globalization, Microsoft Learn](https://learn.microsoft.com/en-us/globalization/localization/managing-terminology) — directly fetched, current (last updated 2023-07-27, page metadata shows a 2026 refresh timestamp); primary source for the recommended per-term field list and the TBX/spreadsheet tooling recommendation.
- [ISO 704:2022 — Terminology work, Principles and methods](https://www.iso.org/standard/79077.html)
- [ISO 12620:2009 — Management of terminology resources, Data category specifications](https://www.iso.org/standard/37243.html)
- [TermBase eXchange (TBX) — Wikipedia](https://en.wikipedia.org/wiki/TermBase_eXchange), [ISO 30042:2019](https://www.iso.org/standard/45797.html), [tbxinfo.net — About TBX](https://www.tbxinfo.net/tbx-about/)
- [Ciklopea — The Benefits of Terminology Management in Translation and Localization Projects](https://ciklopea.com/blog/translation/the-benefits-of-terminology-management-in-translation-and-localization-projects/) — source for the termbase-vs-style-guide distinction, cross-checked against multiple similar industry articles in the same search pass (Andovar, Adhoc Translations, GTE Localize) that state the same distinction consistently.
