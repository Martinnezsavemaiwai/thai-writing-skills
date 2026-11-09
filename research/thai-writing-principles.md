# Thai Writing Principles — Language-Problem Taxonomy

Scope: language-level problems only (sentence structure, calques, register, connectors). Context/audience/terminology models live in their own research files. Every claim is tagged:

- `[Source-backed principle]` — traceable to a cited source
- `[Observed pattern]` — recurring pattern the author has seen in AI-generated or translated Thai, not yet tied to a citation
- `[Project decision]` — a choice this project is making, not a linguistic fact
- `[Open question]` — unresolved, needs native-speaker or corpus validation

**Tag scheme note (deep-research pass):** `thai-ai-smell-taxonomy.md` has moved to a 5-tag scheme (`[SOURCE-BACKED]` / `[OBSERVED]` / `[PROJECT DECISION]` / `[HYPOTHESIS]` / `[OPEN QUESTION]`) that maps 1:1 onto the four tags above, plus a new `[HYPOTHESIS]` slot between `OBSERVED` and `OPEN QUESTION` for a reasoned claim with no source that hasn't recurred often enough to call "observed." This file keeps its original 4-tag style since nothing below needed re-tagging this pass — new content added elsewhere in `research/` uses the 5-tag style.

## Problem categorization (7-way split)

Every pattern in `thai-ai-smell-taxonomy.md` carries a `category` field using this exact 7-way split — kept here as the canonical definition so the taxonomy file, `research/README.md`'s index, and the skill's own categorization all point at one source of truth instead of drifting into slightly different lists over time:

| Category | What it covers | Example pattern(s) |
|---|---|---|
| `natural-thai` | Sentence-level structure/register problems independent of translation or context — the subject matter of this file | `redundant_verb_construction`, `unnecessary_nominalization`, `excessive_formal_connectors`, `bureaucratic_reference_words`, `classifier_errors`, `register_mixing` |
| `translation` | Specifically caused by carrying an English source-language habit into Thai | `passive_calque`, `not_just_x_but_y_calque`, `title_case_english_bleed`, `unnecessary_subject_insertion` |
| `ux-writing` | Surfaces in in-product UI/notification copy specifically | `redundant_politeness_particles` (particle-per-sentence is a UX-copy-rhythm problem, not a grammar problem) |
| `technical-writing` | Code comments, docs, PRs, commits — no taxonomy entry is *purely* this category yet; the relevant failure modes (over-explaining a comment, restating what code does) are currently filed under `ai-generation-pattern` because the underlying mechanism is content-redundancy, not a Thai-specific technical-writing rule. Flagged as an `[OPEN QUESTION]`: revisit if native-speaker review surfaces a technical-writing failure mode that isn't just over-explanation in a different context. |
| `business-communication` | Requirements, acceptance criteria, business rules, stakeholder communication | `superlative_inflation` (an ad-copy-era holdover kept low-relevance here rather than deleted) |
| `terminology` | Same-concept-different-rendering or unrecognizable-term problems | `unnatural_technical_terminology`, `inconsistent_terminology` |
| `ai-generation-pattern` | Structural/formatting tells largely independent of Thai specifically (attested in general, non-Thai AI-writing research too) | `generic_introductory_phrases`, `listicle_emoji_spam`, `over_explanation` |

This is a classification of *primary* category — several patterns genuinely straddle two (e.g. `redundant_politeness_particles` is both a UX-rhythm issue and, in principle, a natural-Thai register issue; it's filed under `ux-writing` because that's where it's actually encountered and reviewed in practice, per `contexts/ux-writing.md`). `[PROJECT DECISION]`: primary-category assignment is for organizing review effort, not a claim that categories are mutually exclusive in the underlying linguistics.

## Register model: where Product Thai sits

`[SOURCE-BACKED]` Thai register variation is documented academically as a form of diglossia: A.V.N. Diller, *High and Low Thai: Views from Within* (Pacific Linguistics, 1985 — directly fetched this pass) studies the coexistence of "high" (formal, associated with education/literature/officialdom) and "low" (colloquial, everyday speech) Thai, differing in vocabulary, grammar, and phonology. Diller notes the written/spoken mapping is real but not absolute — educated speakers code-switch contextually — and that high Thai signals education/prestige while low Thai marks solidarity/informality. `[OBSERVED]` (weaker, search-snippet-level corroboration, not independently verified): popular sociolinguistic accounts of Thai further break the continuum into named registers — Street/informal spoken Thai (drops particles, slang), Elegant/polite spoken Thai (ครับ/ค่ะ particles, ผม/ดิฉัน pronouns — everyday polite speech, distinct from both informal street Thai and formal written Thai), Formal Thai (official documents, news, academic — uses vocabulary like ดำเนินการ instead of ทำ; **this is a directly relevant, independently-found corroboration that ดำเนินการ specifically belongs to a named formal register tier, not that it's simply "correct" or "incorrect"**), Rhetorical Thai (public speaking to large audiences), and Religious/Royal Thai (Buddhist monastic address, royal family — explicitly out of scope for software products).

**Where Product Thai sits — `[PROJECT DECISION]`, tested against existing findings:** the working hypothesis was that Product Thai is not simply "informal/spoken register applied to software" but its own point on the continuum, borrowing written-register clarity and precision with spoken-register directness and brevity, while avoiding both the most bureaucratic/literary end of Formal Thai and the slang end of Street Thai. This holds up against what's already documented elsewhere in this research:

- The AIS security-alert finding (`real-product-observations.md`) — dropping Elegant-register particles under urgency while staying grammatically precise — is exactly this: not sliding into Street Thai (no slang), but stripping the politeness layer of Elegant Thai while keeping Formal-Thai-level precision about what happened.
- The "professional ≠ formal" finding (`core/tone.md`) is the same phenomenon from the audience side: an internal message to a PM sits close to Elegant/polite spoken Thai in practice (direct, some particles, no ดำเนินการ-tier vocabulary), even though "professional" might suggest Formal Thai to someone applying the term naively.
- Product Thai is **not uniform across the skill's own contexts** — this is the key qualifier the hypothesis needs: end-user UX copy sits closest to Elegant/polite spoken Thai (with severity-based flexing per the AIS finding); requirements/business rules sit closer to Formal Thai (precision-driven, ในกรณีที่/ดังกล่าว genuinely earn their place); code comments sit in a register none of Diller's or the popular account's categories quite name — direct like spoken Thai, precise like written Thai, but with particles absent entirely (a "Technical" register this skill's own `core/tone.md` already names, that predates neither classic diglossia study because code comments as a genre didn't exist when Diller wrote in 1985).

**On dimensions and numeric scoring — `[PROJECT DECISION]`:** the brief suggested formality/directness/warmth/technicality/brevity/politeness as candidate dimensions. This pass did not find evidence that a numeric (e.g. 1-5) score on each dimension would be actionable — no source reviewed scores register this way, and a fabricated numeric scale risks exactly the "arbitrary formula" failure mode the brief warned against. The qualitative per-context descriptions above (and the existing `contexts/*.md` header fields `desired_tone`/`desired_length`) already do the practical work a numeric formula would attempt, without the false precision. **Recommendation: do not add a numeric register-scoring system.** If a future pass finds a genuine actionability gap the qualitative description can't fill, revisit with concrete evidence for what the numbers would be used for.

`[OPEN QUESTION]`: this register model, like the rest of this taxonomy, has not been checked against native-speaker judgment. In particular, whether "code-comment register" is really a 6th category or better described as a context-specific flexing of Formal Thai's precision minus its politeness/vocabulary layer is a modeling choice this research can't settle alone.

## 1. Unnatural Thai sentence structures

`[Observed pattern]` AI-generated Thai often chains clauses with subordinators the way English chains clauses with commas and relative pronouns, producing one long sentence where a native writer would use two or three short ones. Thai product/UI writing favors short, single-clause sentences (see `technical-writing-research.md` for the same finding applied to docs).

- Before: `ระบบจะทำการตรวจสอบข้อมูลที่ผู้ใช้กรอกก่อนที่จะทำการบันทึกลงในฐานข้อมูลซึ่งหากพบข้อผิดพลาดจะแสดงข้อความแจ้งเตือนให้ผู้ใช้ทราบ`
- After: `ระบบตรวจข้อมูลก่อนบันทึก ถ้าพบข้อผิดพลาดจะแจ้งเตือนทันที`

`[Open question]` No published corpus study measures average sentence length in Thai product UI specifically. LST20 (see Sources) is news/wiki text, not UI copy — its sentence-length norms should not be imported as a target for UX writing without separate validation (see Phase 3 research on real products).

## 2. Literal English-to-Thai translation patterns (calques)

`[Observed pattern]` Two calque shapes recur constantly in machine-translated or AI-generated Thai:

- **Passive calque** — `ถูก + verb` used to translate English passive ("designed to", "created for") even when Thai would normally state the actor or use an active/stative form.
  - Before: `กระเป๋าใบนี้ถูกออกแบบมาเพื่อรองรับการใช้งานในชีวิตประจำวัน`
  - After: `กระเป๋าใบนี้ออกแบบมาให้ใช้งานง่ายในชีวิตประจำวัน`
  - `[Source-backed principle]` Thai `ถูก`/`โดน` passive constructions exist and are grammatical, but carry a register split: `ถูก` is the written/formal form, `โดน` is colloquial, and both historically lean adversative (something unwelcome happening to the subject) even though modern usage has neutral cases too (Lekawatana, *The So-Called Passive in Thai*, ANU — see Sources). Using `ถูก` for neutral, non-adversative statements (a wallet "being designed" a certain way) is grammatical but reads as translated because native speakers default to active voice for neutral statements and reserve `ถูก` for cases where the passive framing is doing real work (something happened *to* someone/something).
- **"Not just X but also Y" calque** — direct translation of "not just... but also...".
  - Before: `โลชั่นตัวนี้ไม่ใช่แค่บำรุงผิว แต่ยังเป็นตัวช่วยให้คุณมั่นใจในทุกวัน`
  - After: `โลชั่นตัวนี้บำรุงผิวให้ชุ่มชื้น ใช้แล้วมั่นใจได้ทั้งวัน`

`[Open question]` No formal corpus-based study of calque frequency in Thai AI output was found; the above is pattern observation, consistent with how the Wikipedia "Signs of AI writing" taxonomy documents equivalent English-side patterns (structural argument, not Thai-specific evidence).

## 3. Excessive formality / bureaucratic phrasing

`[Observed pattern]` Words drawn from Thai government/legal register (e.g. `ดำเนินการ`, `ทั้งนี้`, `ดังกล่าว`, `กล่าวคือ`, `โดยเฉพาะอย่างยิ่ง`) read as stiff when used in UI copy or casual internal communication, because that register signals official/legal documents to Thai readers, not product software.

**Hard requirement — this is a register test, not a blacklist.** For the five words the project must treat carefully:

- **`ดำเนินการ`** ("proceed / carry out / undertake") — Fine in formal business process descriptions, government-adjacent workflows (banking, compliance), or documents where the actor is an institution ("ธนาคารจะดำเนินการตรวจสอบ"). Suspicious when it pads a UI action that has a direct verb ("ดำเนินการบันทึกข้อมูล" → just "บันทึกข้อมูล") — check: does removing it and using the direct verb lose any meaning? If not, it's padding.
- **`อย่างไรก็ตาม`** ("however") — Fine as a paragraph-level contrast connector in documentation, requirements, or business writing where a full "however" clause is genuinely needed. Suspicious in short UI strings (error messages, toasts) where a comma or a shorter connector (`แต่`) would carry the same contrast at the right register, and suspicious when it appears more than once or twice in a short document (redundant hedging).
- **`ดังกล่าว`** ("aforementioned / said [item]") — Fine in legal/contract text, formal specs, or long technical documents referring back to a named entity several paragraphs earlier, where re-stating the full noun would be clunky. Suspicious in short-lived UI copy or chat-style messages, where "นี้"/"นั้น" or just repeating the noun reads more natural and the referent is one sentence away, not paragraphs away.
- **`ในกรณีที่`** ("in the case that / if") — Fine in requirements and acceptance criteria where you are explicitly enumerating conditions ("ในกรณีที่ผู้ใช้ยังไม่ยืนยันอีเมล ระบบจะ...") — this is exactly the register technical requirements want. Suspicious in a plain error message or empty state where `ถ้า` is shorter and equally precise, and where the formal phrasing doesn't add legal/contractual weight that's actually needed.
- **`ทั้งนี้`** ("and so / with that said / accordingly") — Fine as a formal transition in official notices, contracts, or terms-of-service style text. Suspicious in UI microcopy or casual internal Slack-style messages, and suspicious when used as a generic connective tissue between unrelated sentences rather than to signal an actual accordingly/therefore relationship — that's the redundant-connector smell (Wikipedia "Signs of AI writing" documents the English-language version of this same failure: connective overuse without real logical work).

Evaluation axes for all five (and any similar word): **register** (does the surrounding text's formality level call for this?), **frequency** (once in a long document is fine, three times in one paragraph is not), **redundancy** (does it add logical/legal precision, or just length?), **sentence structure** (is it glueing together a genuinely complex conditional, or padding a simple statement?), **audience** (government/finance/legal-adjacent audiences expect this register; end users of a consumer app do not).

## 4. Unnecessary passive constructions

See item 2 above (`ถูก`/`โดน` calque) — this is the same phenomenon, called out separately because it can also occur without direct English influence, e.g. a Thai writer over-applying passive voice in a UI context because "formal-sounding" is mistaken for "professional-sounding."

`[Project decision]` Default to active voice with the user or system as subject in UX writing (`ระบบบันทึกข้อมูลแล้ว` not `ข้อมูลถูกบันทึกแล้ว`), unless the object of the action is what the user cares about and the actor is truly irrelevant, which is a legitimate use of passive in many languages including Thai.

## 5. Unnecessary subjects / redundant verb constructions

`[Observed pattern]` `ทำการ + verb` ("to carry out [verb]-ing") pads a sentence with a semantically empty verb where the following verb already carries the full meaning.

```yaml
pattern: redundant_verb_construction
context: general
description: >
  Uses unnecessary constructions such as "ทำการ..." when a direct verb is sufficient.
bad_example: "ทำการบันทึกข้อมูล"
better_example: "บันทึกข้อมูล"
when_it_is_valid:
  - "ทำการ + verb" can carry real weight in formal announcements of an institutional action ("ธนาคารได้ทำการปรับปรุงระบบ") where the emphasis is on the act of undertaking something, not just the result — still worth questioning per-case, not banning
confidence: medium
```

`[Observed pattern]` Similarly, restating an already-clear subject every sentence (Thai regularly omits subjects/pronouns when they're recoverable from context) is a translation artifact from English, which requires an explicit subject in almost every sentence.

## 6. Repetitive sentence structures

`[Observed pattern]` AI-generated Thai product copy tends to repeat the same sentence template back-to-back (`X คือ... X ช่วยให้... X มี...`), which reads as a list dressed as prose rather than natural writing. The fix is varying sentence openers and combining short related facts into one sentence instead of one-fact-per-sentence.

## 7. Over-explanation

`[Observed pattern]` Restating the obvious consequence of an action the reader already inferred (e.g., after "ลบรายการนี้ไม่ได้เพราะมีการอ้างอิงอยู่" adding "ดังนั้นกรุณาตรวจสอบการอ้างอิงก่อนทำการลบ" when that's the only reasonable next step) is a doc/UX-writing form of the same redundancy problem, distinct from the sentence-connector issue in §3 — this is redundant *content*, not redundant *connectors*.

## 8. Unnatural/redundant connectors

Covered in depth in §3. General rule beyond the five flagged words: any connector (`นอกจากนี้แล้ว`, `กล่าวคือ`, `ในขณะเดียวกัน`) should be evaluated by whether it's doing real logical work (contrast, causation, addition of genuinely new information) or just gluing sentences together because the writer/model defaults to formal connective tissue. This mirrors the general "AI-generated text favors connective words that suggest a flow of logic without establishing one" observation from the Wikipedia "Signs of AI writing" essay (English-language, used here only as a structural analogy, not as Thai-specific evidence).

## Sources

- [Thai Localization Style Guide (Microsoft, PDF)](https://download.microsoft.com/download/3/f/2/3f236167-639e-46f2-8201-554c36bcbf31/tha-tha-StyleGuide.pdf) — Microsoft's own Thai-specific style rules (orthography, tone, terminology conventions); primary source for what "acceptable formal register" looks like in Microsoft's Thai products. Not yet deeply mined section-by-section in this pass — flagged as follow-up.
- [Microsoft Localization Style Guides index](https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides) — current (post-2023) home for all per-language style guides after the old Language Portal was retired.
- [Lekawatana, Pongsri — "The So-Called Passive in Thai"](https://openresearch-repository.anu.edu.au/server/api/core/bitstreams/0c55fe14-b11d-49a5-b316-9e607a184e7b/content) (ANU) — academic source for the register/adversative properties of `ถูก`/`โดน` passive constructions.
- [Satthachai, Mali — thesis on Passive, Deontic Modality and Cohesive Conjunction](https://doras.dcu.ie/23093/1/Mali%20%20Satthachai_Thesis.pdf) (DCU) — secondary academic reference on Thai passive/cohesion, not yet fully reviewed; flagged for deeper follow-up before treating as settled.
- [The Annotation Guideline of LST20 Corpus (arXiv 2008.05055)](https://arxiv.org/pdf/2008.05055) — NECTEC's LST20 corpus: 3,164,864 words / 74,180 sentences across 3,745 documents, all in **15 news genres**. Used here only as evidence that formal/written Thai syntax patterns exist and are annotatable at scale — **explicitly not used as evidence about UI/product tone**, since it is a news/wiki corpus, not conversational or product text.
- [LST20 Corpus — NECTEC Data Catalog](https://opend-portal.nectec.or.th/en/dataset/lst20-corpus) — dataset access page, non-commercial license.
- Wikipedia, ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — English-language structural taxonomy (connective overuse, redundant sentence templates) used only as an analogy framework to name Thai-language patterns that appear structurally similar; not itself evidence about Thai.
- Thai classifier (`ลักษณนาม`) system — general descriptive overview cross-checked against multiple learner-oriented sources (BananaThai, Thai With Grace); no single academic reference found in this pass. `[Open question]`: a citable academic descriptive-grammar source for the classifier system should replace these informal sources before this project treats classifier rules as authoritative.
