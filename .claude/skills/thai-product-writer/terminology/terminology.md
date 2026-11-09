# Terminology

Consistent product terminology is a per-product model, not a universal dictionary. See `../../../../research/terminology-research.md` for the full research; this file is the applied version.

## Why per-product, not universal

`[Source-backed principle]`: Microsoft maintains one internal terminology database precisely because unmanaged translation lets the same concept surface as three different terms across a product, eroding user trust. That's a precedent for the *mechanism*: one shared glossary, one preferred term per concept, an explicit avoid-list, not for "the correct Thai word" for any given English term. A Thai fintech app and a Thai logistics app can legitimately choose different Thai renderings of the same English concept, as long as each is consistent within itself.

**Never assume a universal translation is correct.** Check the project's own glossary or existing shipped copy first. If neither exists, propose one and ask rather than guessing. The wrong guess, once shipped, becomes the inconsistency this whole file exists to prevent.

## Schema

See `glossary.example.yaml` for a runnable example. Fields:

- `term`: canonical identifier (usually the English product term)
- `preferred`: how it appears in English UI/docs, if kept in English at all
- `thai.preferred`: this product's chosen Thai rendering
- `thai.alternatives`: near-synonyms that are understandable and not wrong, just not this product's house choice (e.g. "ล็อกอิน" for `login` when the product picked "เข้าสู่ระบบ"). This is distinct from `thai.avoid` below. `[PROJECT DECISION, research-backed]`: added this pass because Microsoft's own terminology field list distinguishes "approved" from "acceptable but not preferred" from "failed," a 3-way split this schema previously collapsed into 2; see `../../../../research/terminology-research.md`.
- `thai.avoid`: near-synonyms this product has already considered and genuinely rejected as confusing or wrong, scoped to this one term only (not a general blacklist). Reserve this for real rejections, not just "not our first choice" (that's `alternatives`)
- `definition`: one sentence, precise
- `contexts`: where this rendering applies; the same English term can legitimately resolve differently in a different context (e.g. more formal in a legal/receipt context than in customer chat). Use separate context-scoped entries rather than a top-level `audience` field if a term needs a different rendering for internal vs. customer-facing use. No evidence was found that a dedicated `audience` field earns its keep over just adding another `contexts` entry.
- `notes`: anything that disambiguates this term from a near-neighbor (e.g. "order" vs. "cart")

## Keep English or translate? There's no universal answer

`[Observed pattern, not verified against a systematic audit]`: treat the table below as a starting point to validate per product, not settled fact:

| Term | Common in the wild | Notes |
|---|---|---|
| login | Split: "Login"/"Log in" and "เข้าสู่ระบบ" both seen widely | Per-product choice |
| dashboard | Usually kept in English, or transliterated "แดชบอร์ด" | Semantic translation ("หน้าภาพรวม") is valid and can be clearer for non-technical audiences |
| cart | Rarely kept in English | "ตะกร้าสินค้า" / "ตะกร้า" is well-established |
| checkout | Mixed | "ชำระเงิน" emphasizes payment; "เช็คเอาท์" is a seen transliteration |
| notification | Mixed | "การแจ้งเตือน" is fairly settled |
| settings | Rarely kept in English | "การตั้งค่า" / "ตั้งค่า" well-established |
| account | Rarely kept in English | "บัญชีผู้ใช้" is more explicit than "บัญชี" when a fintech context could confuse it with a financial account |
| order | Mixed | "รายการสั่งซื้อ" / "คำสั่งซื้อ" both seen; pick one per product, record it, stay consistent |

## Same English word, different concepts: don't force one entry

Before creating a `term` entry, confirm the English word actually names **one concept** in this product. "Return" is the clearest example: `คืนสินค้า` (return a purchased product), `ขายคืน` (sell back / trade-in), and `คืนขวด` (return a deposit bottle) are not competing renderings of one term. They're three unrelated real-world actions that happen to share an English gloss. A product with both a return policy and a bottle-deposit scheme needs **all three simultaneously**, as separate `term` entries with different `definition`s, not one entry forced to pick a winner. `[PROJECT DECISION, research-backed]`: call this **term-conflation risk**, distinct from `inconsistent_terminology` (same concept, different renderings); see `../../../../research/terminology-research.md`'s schema stress-test.

## Internal vs. customer-facing: a naming convention, not a new field

When the same term needs a different rendering for internal tooling vs. customer-facing surfaces (or admin vs. support-agent vs. end-user, or any N-way split), don't reach for new top-level schema fields. Prefix the `contexts` values instead: `internal-*` (e.g. `internal-admin-dashboard`) vs. `customer-*` (e.g. `customer-checkout`). This gets the same discoverability as a dedicated `internal`/`customer_facing` field without hard-coding a binary that doesn't cover every product's actual audience split. `[Open question]`: untested on a real, sizable multi-context glossary, so revisit if the prefix convention proves unwieldy in practice.

## Consistency check before delivering

Grep the existing codebase/UI strings for how this concept is already named. If you find more than one existing rendering, that's an `inconsistent_terminology` finding to raise (see `../../thai-writer/review/thai-ai-smells.md`), not something to add a third option to.
