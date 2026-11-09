# Thai AI-Smell Taxonomy

This is a **pattern taxonomy, not a blacklist**. No word in this file is banned. Every entry names a *construction* (a way words combine, or a way a whole piece is structured) and every entry carries a mandatory `when_it_is_not_a_problem` field, because the same construction is a smell in one context/register and completely normal in another. Evaluate by context, frequency, redundancy, register, sentence structure, audience, and meaning — never by matching a word against a list.

**Schema hardening (Evidence Hardening pass):** the schema has moved from `pattern/category/description/why_it_feels_unnatural/bad_example/better_example/when_it_is_valid/severity/confidence/source` to:

```yaml
id:
name:
category:
description:
why_it_can_be_a_problem:
bad_example:
better_example:
when_it_is_not_a_problem:    # MANDATORY, substantive — the field that prevents this from becoming a blacklist
contexts:                     # list of relevant contexts/*.md files, or [general]
severity:                      # low | medium | high — how much this degrades quality when it genuinely occurs
confidence:                    # low | medium | high — how much evidence backs the pattern's existence at all
evidence_type:                 # SOURCE_BACKED | OBSERVED | PROJECT_DECISION | HYPOTHESIS
sources:                       # list; empty list is honest for pure OBSERVED/PROJECT_DECISION entries
```

All prior content is preserved under the new field names — nothing was dropped in the migration, only renamed/restructured. `evidence_type` is a coarser, single-value classification of what `sources`/`confidence` already describe in prose; both are kept because `evidence_type` supports quick filtering and `confidence`/`sources` carry the actual nuance.

`confidence` levels: **high** — matches a well-documented pattern class in general AI-writing research applied to a clear Thai mechanism, or backed by an academic Thai-linguistics source. **medium** — plausible and internally consistent with Thai grammar, not yet checked against a corpus of real AI-generated Thai product text at scale. **low** — a hypothesis worth tracking, treat with the most skepticism.

None of these entries have been validated against a native-speaker review panel yet (see `native-speaker-validation.md`). Treat `confidence`/`evidence_type` as "how much I'd bet on this," not "proven."

## Register-model cross-reference

`thai-writing-principles.md` now has a dedicated "Register model: where Product Thai sits" section — several `when_it_is_not_a_problem` entries below reference specific traditional registers (Formal Thai, Elegant/polite spoken Thai) defined there. Read that section for the full grounding (Diller 1985's diglossia study, register-inventory sources).

## Two open questions closed (prior pass, still current)

**1. Thai classifier (ลักษณนาม) system — source-backed.** Iwasaki & Ingkaphirom, *A Reference Grammar of Thai* (Cambridge University Press, 2005/2009, ISBN 9780521108676) — confirmed via publisher catalog, Google Books listing, two ResearchGate review abstracts. Primary text not read (Cambridge page returned HTTP 403); citation rests on metadata-level confirmation.

**2. `ถูก`/`โดน` passive register — corroborated, medium-high confidence.** Two academic theses (Lekawatana/ANU, Satthachai/DCU) plus a third confirmed-to-exist academic paper (Sudmuk, "The *thuuk* Construction in Thai," Stanford CSLI) plus convergent secondary sources establish: `ถูก` is the written/formal form, `โดน` colloquial, written Thai uses only `ถูก`, both historically adversative-leaning with modern neutral extension. Not raised to "high" — none of the three academic sources read in full.

## Coverage note: "excessive explanation" and "excessive politeness"

Both named explicitly in two successive research briefs. Both have dedicated entries (`over-explanation`, `redundant-politeness-particles`) and this pass concludes no third entry is needed for either — see each entry below.

## Recommendation: remove `superlative_inflation` from the live taxonomy

`[PROJECT DECISION]` **`superlative_inflation` is removed from the active taxonomy this pass**, kept only as this historical note. Reasoning: the project has an explicit, repeated scope guard against drifting back into advertising/marketing-copy territory (superlatives, hyperbole, "ที่สุดในโลก") — that entire failure mode belongs to the retired ad-copy version of this skill. Keeping a live entry for it, even flagged "low-relevance," still implicitly signals to anyone reading the taxonomy that hunting for superlatives is part of this skill's job. It essentially never is, for software-product surfaces (UX copy, code, docs, requirements) — the one plausible edge case (a marketing-adjacent release announcement drifting into hype language) is thin enough to not warrant a permanent taxonomy slot. If a future pass finds real software-product cases where this recurs, re-add it with real evidence rather than carrying it forward by inertia.

## Taxonomy (20 active entries)

```yaml
- id: redundant-verb-construction
  name: Redundant Verb Construction (ทำการ...)
  category: natural-thai
  description: >
    Prefixes a plain verb with an empty helper verb — most commonly "ทำการ + verb"
    (ทำการบันทึก, ทำการตรวจสอบ, ทำการติดตั้ง) — where the helper adds no meaning.
  why_it_can_be_a_problem: >
    "ทำการ" belongs to Formal Thai register vocabulary (see thai-writing-principles.md's
    register model). Attaching it to an ordinary verb in UI copy or casual internal text
    makes an everyday action sound like an official procedure — a register mismatch, not
    a grammar error.
  bad_example: "ทำการบันทึกข้อมูล"
  better_example: "บันทึกข้อมูล"
  when_it_is_not_a_problem:
    - "Formal announcements, legal/regulatory notices, government-facing documents — this is exactly Formal Thai register vocabulary, correctly used"
    - "The surrounding document is already consistently formal (e.g. a signed contract clause) and matching that register is the goal"
    - "Formal institutional actions where the emphasis is on the act of undertaking something, not just the result (\"ธนาคารได้ทำการปรับปรุงระบบ\")"
  contexts: [general]
  severity: medium
  confidence: high
  evidence_type: OBSERVED
  sources:
    - "Generalizes a well-attested class (empty/redundant verb constructions) documented across AI-writing critiques in other languages"

- id: unnecessary-nominalization
  name: Unnecessary Nominalization (มีการ + การ-/ความ-)
  category: natural-thai
  description: >
    Uses Thai's การ-/ความ- nominalizing prefixes to turn a perfectly good verb or
    adjective into an abstract noun, then wraps it in a generic verb like "มี" or
    "ดำเนิน" — "มีการดำเนินการตรวจสอบ" instead of just "ตรวจสอบ." Distinct from
    redundant-verb-construction (that pads a verb with an empty helper; this converts
    the verb itself into an abstract noun first, which licenses stacking further empty
    verbs/helpers around it). The two frequently co-occur.
  why_it_can_be_a_problem: >
    Nominalization is normal, necessary Thai grammar (ความสวยงาม, การพัฒนา are fine
    nouns). The smell is nominalizing an action that had a perfectly usable verb form
    and no reason to be an abstract noun-event — it adds a layer of abstraction between
    the writer and the actual action, reading as hedging/bureaucratic distancing rather
    than direct statement.
  bad_example: "มีการดำเนินการตรวจสอบข้อมูลก่อนการอนุมัติ"
  better_example: "ตรวจสอบข้อมูลก่อนอนุมัติ"
  when_it_is_not_a_problem:
    - "The nominalized form is the actual grammatical subject of the sentence, not a padded object — 'การตรวจสอบใช้เวลา 3 วัน' (the inspection takes 3 days) genuinely needs the noun form"
    - "Formal process documentation (audit trails, compliance reports) where naming the action as a discrete, referenceable event/noun is the actual communicative goal — see contexts/requirements.md"
  contexts: [general, documentation]
  severity: medium
  confidence: high
  evidence_type: OBSERVED
  sources:
    - "Generalizes the over-nominalization pattern documented for English AI-writing (needless -ion/-tion abstraction) to Thai's การ-/ความ- mechanism"

- id: passive-calque
  name: Passive Calque (ถูก + verb, translating English passive)
  category: translation
  description: >
    Translates English passive voice ("is designed to", "was built to") literally as
    "ถูก + verb + เพื่อ," producing a construction that is grammatically valid Thai but
    not how a Thai speaker would normally phrase the sentence.
  why_it_can_be_a_problem: >
    Thai ถูก-passives exist and are grammatical (written register uses only ถูก, never
    โดน — see the open-questions note above), but native usage skews toward agentless or
    adversative situations (ถูกไล่ออก, ถูกปฏิเสธ). Using ถูก as a default translation of
    any English passive produces a sentence a Thai speaker would normally phrase with a
    direct active subject instead. The calque problem is about mechanical translation
    default, not about ถูก being inherently wrong.
  bad_example: "กระเป๋าใบนี้ถูกออกแบบมาเพื่อรองรับการใช้งานในชีวิตประจำวัน"
  better_example: "กระเป๋าใบนี้ออกแบบมาให้ใช้งานง่ายในชีวิตประจำวัน"
  when_it_is_not_a_problem:
    - "The agent is genuinely unknown, irrelevant, or intentionally de-emphasized (incident reports: 'the request was rejected' without needing to name what rejected it)"
    - "Legal/technical text where passive voice is the established convention for stating a rule"
    - "Written/formal register generally accepts ถูก more readily than spoken register accepts โดน — a ถูก-passive in a formal document is less of a smell than the same construction in a casual UI string"
  contexts: [ux-writing, customer-facing]
  severity: high
  confidence: medium
  evidence_type: OBSERVED
  sources:
    - "Corroborated by Lekawatana (ANU), Satthachai (DCU), Sudmuk (Stanford CSLI) — see passive-voice open-question note above"

- id: not-just-x-but-y-calque
  name: "Not Just X But Also Y" Calque
  category: translation
  description: >
    Literal translation of the English "not just X, but also Y" rhetorical frame —
    "ไม่ใช่แค่...แต่ยังเป็น...", "ไม่เพียงแต่...แต่ยัง..." — used as a stock rhetorical
    device rather than because the contrast is meaningful.
  why_it_can_be_a_problem: >
    This frame is a marketing/rhetorical device borrowed wholesale from English
    copywriting conventions; it reads as a translated template rather than a sentence a
    Thai speaker would construct to make the same point plainly.
  bad_example: "โลชั่นตัวนี้ไม่ใช่แค่บำรุงผิว แต่ยังเป็นตัวช่วยให้คุณมั่นใจในทุกวัน"
  better_example: "โลชั่นตัวนี้บำรุงผิวให้ชุ่มชื้น ใช้แล้วมั่นใจได้ทั้งวัน"
  when_it_is_not_a_problem:
    - "Rare — when the contrast itself is the actual point being made and no simpler phrasing preserves it; even then, prefer restructuring over keeping the calque frame. This is the taxonomy's thinnest exception — flagged honestly rather than padded, since the construction is close to always a smell in software-product text specifically (it's fundamentally a marketing rhetorical device with little legitimate technical/UX use)"
  contexts: [customer-facing]
  severity: medium
  confidence: high
  evidence_type: OBSERVED
  sources: []

- id: generic-introductory-phrases
  name: Generic Introductory Phrases
  category: ai-generation-pattern
  description: >
    Stock scene-setting preambles before the actual point — "ในปัจจุบัน...", "เป็นที่
    ทราบกันดีว่า...", "ปฏิเสธไม่ได้ว่า...", "ท่ามกลางความเปลี่ยนแปลงของ..." — used to open
    a document or section instead of stating the point directly. Distinct from
    excessive-formal-connectors (mid-text connective glue between sentences): this is
    specifically about the OPENING move of a piece.
  why_it_can_be_a_problem: >
    A person writing under time pressure states the point and expands from there; a
    preamble that could be prepended to almost any document on the same general subject
    is a strong tell the opening was generated to "sound like an essay" rather than
    composed to communicate this specific thing. Mirrors the English "editorializing and
    unearned transition" AI-writing tell (Wikipedia: Signs of AI writing).
  bad_example: "ในปัจจุบันการพัฒนาซอฟต์แวร์มีความสำคัญมากขึ้นเรื่อยๆ โปรเจกต์นี้จึงถูกสร้างขึ้นเพื่อ..."
  better_example: "โปรเจกต์นี้จัดการคิวงานพื้นหลังสำหรับระบบที่มี throughput สูง"
  when_it_is_not_a_problem:
    - "A genuine executive summary or proposal document where establishing shared context/stakes before the recommendation is a real rhetorical need — the test is whether the preamble says something specific to this document's actual context, not a template sentence fitting any similar document"
    - "ในกรณีที่ used as a genuine conditional opener in requirements/business rules is a different, valid construction — don't conflate a formal conditional with a content-free scene-setter"
  contexts: [documentation, requirements]
  severity: medium
  confidence: high
  evidence_type: SOURCE_BACKED
  sources:
    - "Wikipedia: Signs of AI writing — general pattern class"

- id: excessive-formal-connectors
  name: Excessive Formal Connectors
  category: natural-thai
  description: >
    Formal written-register connectors — ทั้งนี้, ดังนั้น, อย่างไรก็ตาม, กล่าวคือ,
    โดยเฉพาะอย่างยิ่ง, นอกจากนี้แล้ว, ในขณะเดียวกัน — used in short casual UI text
    (buttons, toasts, empty states) where the register mismatch makes them stand out.
  why_it_can_be_a_problem: >
    These connectors belong to Formal Thai register (news writing, official documents,
    academic prose — see the register model). They are not wrong words — they are wrong
    *for a one-line toast or button label*, the same way "notwithstanding the foregoing"
    would stand out in a push notification in English. The smell is register mismatch
    with a short, casual, high-frequency-read surface, not the words themselves.
  bad_example: "ทั้งนี้ กรุณากรอกอีเมลก่อนกดยืนยัน"
  better_example: "กรอกอีเมลก่อนกดยืนยัน"
  when_it_is_not_a_problem:
    - "Formal documentation, legal/compliance text, B2B contracts, requirements docs, official notices — this is the established, expected register and their absence would itself look wrong"
    - "Long-form technical explanation where a genuine logical connective (ดังนั้น = therefore, อย่างไรก็ตาม = however) is doing real logical work, not decorative connective tissue"
  contexts: [ux-writing, notifications]
  severity: medium
  confidence: high
  evidence_type: OBSERVED
  sources:
    - "Covers the five words the project explicitly flagged as must-not-be-blacklisted: ดำเนินการ is covered by redundant-verb-construction; ดังกล่าว, ในกรณีที่, ทั้งนี้, อย่างไรก็ตาม are covered here"

- id: bureaucratic-reference-words
  name: Bureaucratic Reference Words (ดังกล่าว, ในกรณีที่)
  category: natural-thai
  description: >
    Words like ดังกล่าว ("aforementioned/said [X]") and ในกรณีที่ ("in the case that")
    used in short, plain-spoken product text where a simpler reference or conditional
    would read more naturally.
  why_it_can_be_a_problem: >
    ดังกล่าว is a formal anaphoric reference typical of legal/official prose; ในกรณีที่
    is a formal conditional. Both are precise and appropriate in documents needing
    unambiguous back-reference (contracts, policies, requirements docs) but read as
    stiff when substituted for how someone would actually talk about "this order" or
    say "if X happens" in a casual UI string.
  bad_example: "หากพบข้อผิดพลาดในการชำระเงินดังกล่าว ในกรณีที่ท่านต้องการยกเลิก กรุณาติดต่อฝ่ายบริการลูกค้า"
  better_example: "ถ้าการชำระเงินนี้มีปัญหาและอยากยกเลิก ติดต่อฝ่ายบริการลูกค้าได้เลย"
  when_it_is_not_a_problem:
    - "Requirements/business-rule documents and legal/policy text, where ดังกล่าว's precision in referring back to a specifically-defined term is exactly the point"
    - "Formal customer correspondence in regulated industries (banking, insurance) where the established register is closer to legal writing"
  contexts: [requirements, ux-writing]
  severity: medium
  confidence: high
  evidence_type: OBSERVED
  sources: []

- id: redundant-politeness-particles
  name: Redundant Politeness Particles
  category: ux-writing
  description: >
    Sentence-final politeness particles (ค่ะ/ค่า/นะคะ/ครับ/นะครับ) attached to nearly
    every sentence in a piece, rather than used at natural rhythm points.
  why_it_can_be_a_problem: >
    Native speech and native-written customer copy (Elegant/polite spoken Thai register)
    use these particles at conversational beats, not as a mechanical suffix on every
    clause; attaching one to every sentence flattens the rhythm in a way real speakers
    don't.
  bad_example: "สินค้าคุณภาพดีค่ะ ส่งไวค่ะ แพ็คดีค่ะ พร้อมส่งทุกวันค่ะ"
  better_example: "สินค้าคุณภาพดี ส่งไว แพ็คแน่นหนา พร้อมส่งทุกวันค่ะ"
  when_it_is_not_a_problem:
    - "An intentionally established brand voice that uses the particle every sentence on purpose for consistency — verify against the product's existing copy before flagging"
    - "Very short pieces (1-2 sentences) where 'every sentence' and 'natural rhythm' are the same thing"
  contexts: [ux-writing, customer-facing]
  severity: low
  confidence: medium
  evidence_type: OBSERVED
  sources: []

- id: classifier-errors
  name: Classifier Errors (ลักษณนาม)
  category: natural-thai
  description: >
    Wrong or missing Thai classifier for the noun being counted — e.g. using ชิ้น for
    something that should take ตัว, คู่, or a domain-specific classifier, or dropping
    the classifier entirely in a way that reads as translated from English.
  why_it_can_be_a_problem: >
    Classifiers are grammatically obligatory in Thai counting constructions and are
    noun-specific; getting them wrong or omitting them is a stronger "not written by a
    Thai speaker" signal than most lexical choices.
  bad_example: "เสื้อยืด 3 ชิ้น รองเท้า 2 ชิ้น"
  better_example: "เสื้อยืด 3 ตัว รองเท้า 2 คู่"
  when_it_is_not_a_problem:
    - "Honestly: essentially never. This is the one entry in this taxonomy that's closer to a grammar-correctness rule than a register/context judgment — flagged explicitly rather than forcing an artificial exception to satisfy the schema. The only real judgment call is WHICH classifier a given domain uses (some technical/software items have contested or emerging conventions, e.g. counting 'devices' or 'accounts') — in ambiguous cases, match existing product copy rather than guessing, but that's a lookup problem, not a context-appropriateness one."
  contexts: [ux-writing, general]
  severity: high
  confidence: high
  evidence_type: SOURCE_BACKED
  sources:
    - "Iwasaki & Ingkaphirom, A Reference Grammar of Thai (Cambridge University Press, 2005/2009)"

- id: title-case-english-bleed
  name: Title Case English Bleed
  category: translation
  description: >
    English words embedded mid-Thai-sentence written in Title Case as if they were an
    English heading, e.g. "สินค้า Premium Quality สำหรับ Perfect Skin ของคุณ".
  why_it_can_be_a_problem: >
    Thai has no capitalization system; Title Case only exists in the borrowed English
    fragment. Carrying English heading-style capitalization into a Thai sentence is a
    visible tell the phrase was assembled from an English template rather than composed
    as Thai.
  bad_example: "ให้ Perfect Skin ของคุณด้วย Premium Quality Serum ตัวนี้"
  better_example: "เซรั่มสูตรพรีเมียม ช่วยให้ผิวคุณดูดีขึ้น"
  when_it_is_not_a_problem:
    - "Actual proper nouns embedded in the sentence — brand names, product model names, named chemical/ingredient names, feature names that are genuinely capitalized identifiers in the product (e.g. a feature literally named 'Smart Mode' in the UI)"
  contexts: [ux-writing, customer-facing]
  severity: medium
  confidence: high
  evidence_type: OBSERVED
  sources: []

- id: register-mixing
  name: Register Mixing
  category: natural-thai
  description: >
    A single piece opens in formal/written register and closes in casual/spoken
    register (or mixes pronoun conventions — คุณ / เธอ / no pronoun at all) without a
    reason tied to structure.
  why_it_can_be_a_problem: >
    A human writer maintains one register through a single piece by default; register
    drift mid-piece is a strong signal that sentences were generated/assembled
    independently rather than composed as one coherent piece.
  bad_example: >
    Opens "ผลิตภัณฑ์นี้ได้รับการรังสรรค์ขึ้นเพื่อ..." then closes "...เอาไปลองเลยน้าา!"
  better_example: >
    Pick one register for the whole piece and hold it — decide up front from
    context/audience (see contexts/*.md), not sentence by sentence.
  when_it_is_not_a_problem:
    - "Deliberate register shift signals a structural boundary the reader needs (e.g. formal disclaimer block followed by a casual in-app tip clearly separated by a heading/card boundary) — the test is whether the shift is structurally justified, not accidental"
  contexts: [general]
  severity: medium
  confidence: medium
  evidence_type: OBSERVED
  sources: []

- id: listicle-emoji-spam
  name: Listicle Emoji Spam
  category: ai-generation-pattern
  description: >
    Every line in a list opens with an emoji (✅ 🔥 💯 ✨) followed by a bold heading and
    colon, with no new information in the line's actual content.
  why_it_can_be_a_problem: >
    A formatting pattern used to simulate structure/energy in place of actual content
    density — documented as a general AI-writing tell, not Thai-specific.
  bad_example: |
    ✅ **คุณภาพ:** สินค้าคุณภาพเยี่ยม
    🔥 **ราคา:** ราคาสุดคุ้ม
  better_example: "ผลิตจากวัสดุเกรด A ราคาเริ่มต้น 199 บาท"
  when_it_is_not_a_problem:
    - "Plain spec lists without emoji/repeated bold headers (size, color, material, weight) are normal and NOT this pattern — the smell is emoji+bold-header+empty-content specifically, not lists themselves"
  contexts: [ux-writing, documentation]
  severity: medium
  confidence: high
  evidence_type: SOURCE_BACKED
  sources:
    - "Wikipedia: Signs of AI writing — documented general AI-writing pattern (list-as-decoration)"

- id: over-explanation
  name: Over-Explanation
  category: ai-generation-pattern
  description: >
    Explains something the surrounding code/UI already makes obvious, rather than
    adding information the reader couldn't get by looking at the code/UI itself.
  why_it_can_be_a_problem: >
    A human writing under time pressure doesn't narrate the obvious; over-explanation is
    a strong AI-generation tell precisely because it costs the model nothing to add but
    costs a human writer effort they'd rather skip. In code comments this directly maps
    to the "why not what" principle.
  bad_example: "// ตรวจสอบว่ามีข้อมูลหรือไม่เพื่อดำเนินการในขั้นตอนถัดไป\nif (!order) return null;"
  better_example: "// ไม่มี Order ก็ไม่ต้องแสดงตาราง\nif (!order) return null;"
  when_it_is_not_a_problem:
    - "Never in code comments when the code is already self-explanatory — the correct move there is to recommend deleting the comment, not softening the over-explanation into shorter Thai"
    - "Onboarding/tutorial content for genuine first-time users, where some restating of the obvious is the intended pedagogy — context (contexts/ux-writing.md: onboarding) determines this, not a blanket exception"
  contexts: [code-comments, ux-writing, documentation]
  severity: high
  confidence: high
  evidence_type: SOURCE_BACKED
  sources:
    - "Google eng-practices (code-comment case)"

- id: unnecessary-subject-insertion
  name: Unnecessary Subject Insertion
  category: translation
  description: >
    Inserts an explicit subject/agent (ระบบ, ผู้ใช้, คุณ) where Thai would naturally
    omit it because it's recoverable from context — a literal carryover from English's
    stricter subject requirement.
  why_it_can_be_a_problem: >
    Thai freely drops recoverable subjects; English cannot. Translating sentence-by-
    sentence from an English source (or English-trained mental template) inserts
    subjects a Thai speaker would leave implicit, adding length without adding
    information.
  bad_example: "ระบบจะทำการบันทึกข้อมูลของคุณโดยอัตโนมัติ"
  better_example: "บันทึกข้อมูลอัตโนมัติ"
  when_it_is_not_a_problem:
    - "The subject is genuinely ambiguous or needs emphasis/contrast (distinguishing 'the system did this automatically' from 'you need to do this manually') — then keeping ระบบ/คุณ explicit is correct, not a smell"
  contexts: [code-comments, ux-writing]
  severity: medium
  confidence: medium
  evidence_type: OBSERVED
  sources: []

- id: unnatural-technical-terminology
  name: Unnatural Technical Terminology
  category: terminology
  description: >
    A technical/product term rendered in a way no real Thai software product or
    developer community would actually use — an over-literal word-for-word translation
    of a compound technical term, or an invented Thai neologism for a term every Thai
    developer keeps in English. Distinct from inconsistent-terminology (same concept,
    multiple renderings across a product): this is about one rendering itself being
    unrecognizable to the actual audience, even used consistently.
  why_it_can_be_a_problem: >
    Technical audiences learn terminology from the ecosystem they work in — English
    documentation, Stack Overflow, framework docs — not from a Thai dictionary. A
    linguistically "correct" translation no working Thai developer would recognize
    signals the text wasn't written by someone embedded in that community, and hurts
    comprehension for the audience it's supposedly serving.
  bad_example: "ฐานข้อมูลเชิงสัมพันธ์แบบกระจายศูนย์ที่ไม่มีโครงสร้างตายตัว (an invented, overly literal rendering) for what every Thai developer just calls 'NoSQL database'"
  better_example: "ฐานข้อมูลแบบ NoSQL"
  when_it_is_not_a_problem:
    - "End-user-facing (non-developer) contexts sometimes need a plain-Thai rendering even for a technical concept, because the audience doesn't share developer vocabulary — the smell is specifically about developer-facing or precision-critical technical text getting an unrecognizable rendering, not about end-user simplification"
    - "A genuinely established Thai rendering exists and is what the target product/community already uses — verify against the project's own glossary and real usage before assuming English-only is correct"
  contexts: [documentation, code-comments]
  severity: high
  confidence: medium
  evidence_type: HYPOTHESIS
  sources:
    - "Reasoned from general observation of Thai developer community conventions (heavy English-technical-term retention), not yet verified against a systematic survey — flag for native-speaker/practitioner validation"

- id: inconsistent-terminology
  name: Inconsistent Terminology
  category: terminology
  description: >
    The same product concept is rendered with different Thai terms across different
    surfaces (e.g. "รายการสั่งซื้อ" on one screen, "คำสั่งซื้อ" on another, "ออเดอร์" on
    a third, all referring to the same entity).
  why_it_can_be_a_problem: >
    Not a naturalness problem at the sentence level — each individual term may be fine
    — but it reads as uncoordinated/AI-assembled at the product level, and actively
    confuses users trying to map UI language to a mental model of the product.
  bad_example: "หน้าแรกใช้ \"รายการสั่งซื้อ\", หน้าประวัติใช้ \"คำสั่งซื้อ\", แจ้งเตือนใช้ \"ออเดอร์\""
  better_example: "ใช้ \"รายการสั่งซื้อ\" (หรือคำที่เลือกไว้ใน glossary) สม่ำเสมอทุกหน้า"
  when_it_is_not_a_problem:
    - "Deliberately different terms for genuinely different concepts that happen to be near-synonyms in English ('order' as a customer-facing purchase vs. an internal fulfillment work-item, if the product genuinely distinguishes these) — verify against the product's terminology glossary before flagging"
  contexts: [general, terminology]
  severity: high
  confidence: high
  evidence_type: SOURCE_BACKED
  sources:
    - "Direct rationale for Microsoft maintaining one shared terminology database (see terminology-research.md)"

- id: weak-verbs
  name: Weak Verbs (ทำ, มี, เกิดขึ้น used generically)
  category: natural-thai
  description: >
    Generic, low-information verbs (ทำ, มี, เกิดขึ้น, เป็น) used where a more specific
    verb would be both more natural and more informative — "มีการเปลี่ยนแปลง" instead
    of "เปลี่ยน," "ทำให้เกิดข้อผิดพลาด" instead of naming the specific error. Related to
    but distinct from unnecessary-nominalization (that's a grammatical
    verb-to-noun conversion) and redundant-verb-construction (that's an empty helper
    verb padding a real verb) — this is a lexical choice problem: picking a vague verb
    when a precise one exists.
  why_it_can_be_a_problem: >
    A weak verb names an action in its plainest, most generic form and leaves the real
    action either hidden or spread across extra words — the reader has to infer what
    actually happened. This is a well-established general writing-craft principle
    (strong/specific verbs over weak/generic ones), applied here to the Thai verbs that
    most often serve as the generic filler.
  bad_example: "มีการเปลี่ยนแปลงราคาสินค้า"
  better_example: "ราคาสินค้าเปลี่ยน" (or, better still, name the specific change: "ราคาสินค้าลดลง 10%")
  when_it_is_not_a_problem:
    - "The generic verb is genuinely the most accurate description available — 'เกิดข้อผิดพลาด' (an error occurred) is honest when the specific cause truly isn't known yet, and inventing false specificity would be a meaning-preservation violation worse than the weak-verb smell"
    - "Formal/legal register where a generic verb plus a precisely-defined object is the established convention (e.g. 'มีการละเมิดข้อตกลง' in a contract, where the object 'ข้อตกลง' is doing the precision work, not the verb)"
  contexts: [general, documentation]
  severity: low
  confidence: medium
  evidence_type: PROJECT_DECISION
  sources:
    - "General English writing-craft guidance on strong vs. weak verbs (ProWritingAid, K5 Learning) — general principle, not Thai-specific; the Thai application is this project's own extension"

- id: unnecessary-abstraction
  name: Unnecessary Abstraction
  category: natural-thai
  description: >
    Describing a concrete action or thing in abstract institutional language when a
    concrete term is available and clearer — e.g. "ดำเนินการเกี่ยวกับปัญหาที่เกิดขึ้น"
    (undertake action regarding the issue that occurred) instead of "แก้บั๊ก X" (fix bug
    X). Related to but distinct from unnecessary-nominalization: nominalization is a
    grammatical mechanism (verb→noun); this is a word-choice/concreteness problem that
    can occur without any nominalization at all.
  why_it_can_be_a_problem: >
    Abstraction distances the writer from stating what actually happened or what
    actually needs to happen — it reads as evasive or bureaucratic even when
    grammatically unremarkable, and it's genuinely less useful to a reader who needs to
    act on the information.
  bad_example: "ดำเนินการเกี่ยวกับปัญหาที่เกิดขึ้นในระบบ"
  better_example: "แก้บั๊กที่ทำให้ checkout ค้าง"
  when_it_is_not_a_problem:
    - "The specific detail genuinely isn't known yet or isn't relevant to this reader (a stakeholder update that says 'กำลังแก้ปัญหาระบบ' before root cause is confirmed is honest, not evasive) — abstraction is a problem when it hides available specifics, not when specifics don't exist yet"
    - "Formal status-reporting register where naming the abstract category of issue (not the specific bug) is the actual convention (e.g. a public status page saying 'ปัญหาด้านประสิทธิภาพ' rather than naming an internal bug ID customers can't use anyway)"
  contexts: [pull-requests, documentation, business-communication]
  severity: medium
  confidence: medium
  evidence_type: PROJECT_DECISION
  sources: []

- id: fake-conversational-tone
  name: Fake Conversational Tone
  category: natural-thai
  description: >
    Forcing casual particles/phrasing (จ้า, เลยนะ, เอาล่ะ, ใครที่...บ้าง) onto content
    that doesn't call for it — content that should stay neutral or technical dressed up
    with performed casualness. The mirror-image failure of
    redundant-politeness-particles: that pattern is about formal-register particle
    overuse; this is about an inappropriately casual register clashing with content that
    needs to stay neutral (e.g. a legal disclaimer or a precise technical instruction
    trying to sound "friendly").
  why_it_can_be_a_problem: >
    Real conversational Thai (Elegant/polite spoken register) is casual because the
    content and relationship call for it — a friend recommending a restaurant, a
    support agent chatting with a customer. Grafting the same particles onto a
    disclaimer, a technical instruction, or a precise business rule doesn't make it more
    approachable — it makes the content less trustworthy, because casualness and
    precision send conflicting signals about how seriously to take the text.
  bad_example: "ยกเลิกได้ภายใน 24 ชม.เท่านั้นนะจ๊ะ ถ้าเลยแล้วอดเลยน้า~"
  better_example: "ยกเลิกได้ภายใน 24 ชั่วโมงหลังสั่งซื้อเท่านั้น"
  when_it_is_not_a_problem:
    - "Genuine end-user-facing marketing/onboarding moments where a light, casual voice is the product's actual established brand voice and the content itself is low-stakes (a celebratory toast, a playful empty state) — verify against the product's existing voice before assuming casualness is wrong"
    - "The content is genuinely conversational by nature (an in-app chat/support message, not a rule or disclaimer) — this pattern is specifically about casualness clashing with content that needs precision/trust, not about casualness being wrong everywhere"
  contexts: [ux-writing, requirements, customer-facing]
  severity: medium
  confidence: medium
  evidence_type: PROJECT_DECISION
  sources: []

- id: unnecessary-summary-repetition
  name: Unnecessary Summary Repetition
  category: ai-generation-pattern
  description: >
    Restating a conclusion the reader just read, at the paragraph/document level — a
    paragraph followed immediately by "สรุปแล้วคือ..." repeating the same point already
    made. Distinct from over-explanation (that's explaining the obvious at the
    sentence/code level); this is restating an already-stated conclusion at a larger
    structural scale.
  why_it_can_be_a_problem: >
    A document that states its point once and moves on respects the reader's time; one
    that states a conclusion, then restates it in summary form a paragraph later, adds
    length without adding information — the same underlying redundancy problem as
    over-explanation, at a different structural level.
  bad_example: >
    A paragraph explaining a feature, immediately followed by: "สรุปแล้วคือฟีเจอร์นี้ช่วยให้ผู้ใช้ทำงานได้เร็วขึ้นตามที่กล่าวไปข้างต้น"
  better_example: >
    Let the paragraph's own conclusion stand; only add a summary if it's synthesizing
    multiple sections into one takeaway the reader hasn't seen assembled yet.
  when_it_is_not_a_problem:
    - "A genuine executive summary or TL;DR positioned BEFORE a long document, written for a reader who may only read the summary — this is a real, valuable document convention, distinct from restating a conclusion redundantly right after making it"
    - "A summary that synthesizes several preceding sections into a new, higher-level takeaway not stated anywhere else — that's adding information (a synthesis), not repeating it"
  contexts: [documentation, business-communication]
  severity: low
  confidence: medium
  evidence_type: PROJECT_DECISION
  sources: []
```

## Unifying theme: `context_inappropriate_formality` is not a separate entry

`[PROJECT DECISION]`: the research brief for this pass named "context-inappropriate formality" as a pattern to investigate. This pass concludes it should **not** become an 18th (or 21st) taxonomy entry — it's the general principle that `excessive-formal-connectors`, `bureaucratic-reference-words`, and (in the opposite direction) `fake-conversational-tone` are all specific instances of. Making it its own entry would either duplicate those three or become vague enough to be unfalsifiable ("formality doesn't match context" applies to nearly every entry in this file in some sense). It's documented here, in the file's framing, and in `core/anti-ai.md`'s register-evaluation axes, rather than as a 21st pattern competing with the concrete ones that actually name a construction.

## Code-comment note (carried over)

Two patterns above (`over-explanation`, `unnecessary-subject-insertion`) apply directly to code comments. The governing principle — comments should explain **why**, not **what** — is a well-established software-engineering norm, now triangulated across Google, Robert C. Martin (*Clean Code*), and John Ousterhout (*A Philosophy of Software Design*) — see `technical-writing-research.md`'s validation section. This implies a third valid action beyond "keep" or "rewrite": **recommend deleting the comment** when the code is already self-explanatory.

## Sources

- [Software Engineering at Google, ch. 8](https://abseil.io/resources/swe-book/html/ch08.html)
- [google/eng-practices — What to look for in a code review](https://github.com/google/eng-practices/blob/master/review/reviewer/looking-for.md)
- Iwasaki, Shoichi & Preeya Ingkaphirom, *A Reference Grammar of Thai* (Cambridge University Press, 2005/2009) — full citation in `sources.md`
- Sudmuk, Cholthicha, "The *thuuk* Construction in Thai" (Stanford CSLI, LFG proceedings) — existence/venue verified, full text not readable
- Diller, A.V.N., "High and Low Thai: Views from Within" (Pacific Linguistics, 1985) — directly fetched this pass; primary academic source for the register model in `thai-writing-principles.md`, which several `when_it_is_not_a_problem` entries above reference
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — general (non-Thai-specific) pattern-class framework
- See [terminology-research.md](terminology-research.md) for the Microsoft terminology sourcing behind `inconsistent-terminology`
- See [sources.md](sources.md) for the full source list
