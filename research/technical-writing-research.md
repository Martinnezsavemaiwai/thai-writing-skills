# Technical Writing Research — Implications for Thai Engineering Content

Scope: code comments, README, API docs, PRs, issue descriptions, release notes. Source guides are English-language style guides for English text; every claim below is translated into an explicit implication for Thai technical writing, tagged separately from the source claim.

- `[Source-backed principle]` — the underlying English-language guidance, cited
- `[Project decision]` — how this project translates that guidance into a Thai-writing rule
- `[Open question]` — where the translation to Thai is not obviously correct and needs validation

## Voice, tone, and conciseness

`[Source-backed principle]` Microsoft Writing Style Guide: write for scanning first, reading second; front-load keywords; "make every word matter"; be affirmative without extra qualifiers; keep sentences short (Microsoft Writing Style Guide, learn.microsoft.com — see Sources).

`[Source-backed principle]` Google developer documentation style guide: use second person, present tense, active voice; aim for a conversational-but-respectful tone, "like a knowledgeable friend," not overly formal and not overly casual; over-politeness (e.g. stacking "please") is itself a style problem, not a virtue (developers.google.com/style/tone — see Sources).

`[Project decision]` For Thai technical content, this implies:
- README/docs opening sections should lead with what the reader needs to know first (what this does, why it exists), not with scene-setting or throat-clearing — the Thai equivalent failure mode is opening with formal preamble (`ในปัจจุบันการพัฒนาซอฟต์แวร์...`) before saying what the doc is about.
- Active voice with an explicit actor (`ระบบ`, `ฟังก์ชันนี้`, ผู้ใช้เป็นประธาน) by default in docs and comments, matching the passive-avoidance principle from `thai-writing-principles.md` §2/§4.
- Second person (`คุณ`, or context-appropriate omission of pronoun) for docs/README addressed to a developer reader, matching Google's "talk to the reader" stance — but see Open question below on register, since Thai second-person pronouns carry more social weight than English "you."

`[Open question]` English "second person, conversational" doesn't map 1:1 onto Thai, where pronoun choice (`คุณ`/no pronoun/name-of-role) itself signals formality and relationship. A literal `คุณ`-in-every-sentence translation of "friendly second person" can read as over-familiar or oddly repetitive in Thai, where omitting the subject once established is the more natural way to sustain a conversational tone (this connects to `thai-writing-principles.md` §5 on unnecessary subjects). Needs native-speaker review before codifying a specific rule.

## Code comments: what vs. why

`[Source-backed principle]` The English-language convention this project inherits (not from a single named guide, but consistent across Google's and Microsoft's engineering documentation culture, plus the existing `code-comment-humanizer` skill in this repo) is: a comment should explain *why* code exists or *why* a non-obvious choice was made, not restate *what* the code visibly does. A comment that only paraphrases the next line in prose is redundant and should be removed, not translated more smoothly.

`[Project decision]` For Thai code comments specifically, this means the review question is never "is this Thai natural?" in isolation — it's first "does this comment need to exist at all?" (does it explain a hidden constraint, a workaround, a business-rule reason?), and only then "is the Thai phrasing of that reason natural?" A perfectly natural-sounding Thai sentence that restates the code is still a defect; a slightly awkward Thai sentence that captures a real "why" is fixable, not deletable.

Worked example (matches the SKILL.md worked example, restated for this doc's audience):

- Not needed at all: `// บันทึกข้อมูล` above a line that says `save(data)` — the code already says this.
- Restates what, in Thai, still wrong: `// ตรวจสอบว่ามีข้อมูลหรือไม่เพื่อดำเนินการในขั้นตอนถัดไป` above `if (!order) return null;` — also triggers the `ดำเนินการ`-padding pattern from `thai-writing-principles.md` §3.
- Correct — explains why: `// ไม่มี Order ก็ไม่ต้องแสดงตาราง` above the same line.

## README / documentation structure

`[Source-backed principle]` Both guides converge on: lead with purpose, use short paragraphs and scannable structure (headings, lists) over dense prose blocks, and avoid stacking qualifiers/hedges that don't change the instruction (Microsoft: "affirmative without extra qualifiers"; Google: get to useful information directly rather than perfecting tone first).

`[Project decision]` A Thai README's failure mode to watch for is the bureaucratic-connector pattern from `thai-writing-principles.md` §3 (`ทั้งนี้`, `อย่างไรก็ตาม`, `ดังกล่าว`) showing up as paragraph glue in what should be scannable, list-first documentation — these words are much more defensible in a long-form legal/compliance document than in a project README's "Installation" section.

## API documentation

`[Source-backed principle]` Google's style guide treats API reference text as needing precision over personality — instructions should be literal and testable ("click X", "run Y"), not softened with hedging language.

`[Project decision]` For Thai API docs: prefer direct imperative phrasing for steps (`ตั้งค่า API key ในไฟล์ .env` rather than a hedged `คุณอาจจะต้องพิจารณาตั้งค่า...`), and keep parameter/field descriptions terminology-consistent with the project's glossary (see `terminology-research.md` / `terminology/terminology.md` in the skill) rather than re-describing the same field differently in different endpoints.

## Pull requests and issue descriptions

`[Project decision]` (no single external style guide covers this directly; derived from combining the "why not what" comment principle with Microsoft/Google's "lead with the point" principle): a Thai PR description should lead with *why* the change exists (the problem/goal) before *what* changed, since the diff itself already shows what changed — this is the PR-level analogue of the code-comment why-vs-what rule. Avoid formal throat-clearing openers (`ใน PR นี้จะทำการปรับปรุง...`) — state the change directly.

`[Open question]` Whether Thai engineering teams commonly write PR/issue text in Thai vs. English-with-Thai-comments varies by company; this project should treat Thai PR/issue guidance as applicable only when the team has actually decided to write these in Thai, not assume it's the default. No source found quantifying this split — flagged as an assumption to verify per-project rather than a taxonomy-wide claim.

## Release notes

`[Project decision]` Release notes are customer/stakeholder-facing in a way READMEs and code comments are not — apply the same "lead with what changed and why it matters to the reader" principle, but calibrate formality to the audience model (`terminology`/`contexts` files), not to the general "conversational" default, since an enterprise B2B release note audience expects a more measured register than an end-consumer app's in-app "what's new."

## Deepening the code-comment decision framework: triangulating beyond Google

The original research cited only Google (*Software Engineering at Google* ch.8, `google/eng-practices`) for "comments explain why, not what." Two more independent, well-established sources were checked to see if they agree, refine, or complicate that principle.

`[Source-backed principle]` **Robert C. Martin, *Clean Code*, ch.4 "Comments"** — a stronger, more skeptical position than Google's: "the proper use of comments is to compensate for our failure to express ourselves in code... comments are always failures," and "the best comment is the one you don't have to write." Martin's taxonomy of *bad* comments includes: mumbling (vague, adds no real information), redundant comments (restate what the code says), obsolete/inaccurate comments, and commented-out code. His *good* comments are narrower than "explains why" alone: legal notices, informative comments (e.g. explaining a regex), clarification of intent, warning of consequences, and TODOs. Key implication for this project: Martin would push further than "rewrite a bad comment" toward "first ask whether better naming/structure removes the need for the comment at all" — i.e. the code-quality fix sometimes outranks the comment-wording fix, which this project's Thai-writing skill has no mandate to touch, but should at least flag as a possibility rather than always defaulting to a text-level fix.

`[Source-backed principle]` **John Ousterhout, *A Philosophy of Software Design*** — frames comments as "documenting things that are not obvious from the code," splitting this into two directions: *lower-level* comments that add precision (e.g. exact units, exact null-handling behavior) and *higher-level* comments that add intuition (why this approach, what design tradeoff this resolves). Ousterhout explicitly rejects "one comment per method explaining what it returns" as insufficient when the real question is *why this design*. This is a useful refinement over a flat "why not what" rule: it gives two concrete sub-categories of legitimate "why," not just one.

**Triangulation result:** all three sources (Google, Martin, Ousterhout) converge on "redundant/what-restating comments are bad" and "comments should carry information the code itself cannot." They diverge on how far to go: Google's guidance is the most permissive (comments explaining why are simply good practice); Martin is the most skeptical of comments as a category, treating most of them as an admission that the code should have been clearer; Ousterhout sits between, giving positive sub-categories (precision-adding, intuition-adding) rather than treating comments as inherently suspect.

### Mapping the 5 outcomes onto the existing 3-way (keep/rewrite/delete)

This task asks for 5 named outcomes: (1) explain why, (2) explain a non-obvious constraint, (3) document a business rule, (4) be rewritten, (5) be removed entirely. Cross-referencing against the three sources above:

- Outcomes 1–3 ("explain why" / "non-obvious constraint" / "business rule") are not three different actions — they're three *content categories* that all resolve to the same action: **keep** (or write, if missing) the comment, because each is exactly the kind of information Ousterhout's "precision" and "intuition" categories and Martin's "clarification of intent" describe as legitimate. A business-rule comment is a specific case of "non-obvious constraint" (the constraint being: the code encodes a rule the reader can't derive from the code alone, e.g. "orders cancel-window is 24h because warehouse stock cuts automatically").
- Outcome 4 ("be rewritten") maps to **rewrite**: the underlying reason is legitimate (falls into 1–3) but the phrasing is padded, translated-sounding, or over-formal in Thai — this is where `core/anti-ai.md` and `core/conciseness.md` actually do their work, not before.
- Outcome 5 ("be removed entirely") maps to **delete**: Martin's "redundant comment" / Google's "restates what the code does" / the code-comments.md worked example (`// เพิ่มค่า count ขึ้นทีละ 1 หน่วย` above `count++;`).

`[PROJECT DECISION]`: keep the skill's existing 3-way framework (`contexts/code-comments.md`) rather than expanding it to a 5-way — the extra granularity (why vs. constraint vs. business-rule) is useful for *this research document's* classification purposes, but collapses to the same action ("keep/write it") from the skill's operational point of view. No skill file was changed by this research pass; this is a documented recommendation only.

### Validation: testing the framework against new examples

Three new test examples (from the Evidence Hardening research brief), run through the existing 3-way framework:

**Example 1 — restates the code:**
```ts
// ตรวจสอบว่า orders ว่างหรือไม่
if (!orders.length) {
```
**Classification: REMOVE.** The comment translates the condition literally ("check whether orders is empty") with zero information the `if` statement doesn't already show a reader who can read the language. This is Martin's "redundant comment" and Google's "restates what the code does" in one step — no rewrite earns this comment a place, matching the framework's own worked example (`// เพิ่มค่า count ขึ้นทีละ 1 หน่วย` above `count++;`).

**Example 2 — the skill's own canonical example, tested in isolation:**
```ts
// ไม่มี Order ก็ไม่ต้องแสดงตาราง
```
**Classification: KEEP, conditionally.** In context (immediately above `if (!order) return null;`, as it appears in SKILL.md and `contexts/code-comments.md`), this passes: it states *why* the guard exists (no table needed without an order) rather than restating *what* the guard does. Ousterhout's framework calls this an "intuition-adding" comment — the code shows the mechanism (early return), the comment shows the reasoning (there's nothing to display). The brief's own hedge ("KEEP/REWRITE depending on context") is right to flag that this classification depends on the comment actually being paired with the right code — the same sentence floating with no surrounding code, or attached to unrelated code, would need re-evaluation. This is not a gap in the framework; it's the framework correctly requiring context to classify, consistent with this whole skill's context-first design.

**Example 3 — explains a business constraint:**
```ts
// ต้องตรวจสิทธิ์ก่อนสร้าง Order เพราะ API เดิมไม่ได้บังคับ rule นี้
```
**Classification: KEEP.** This is Ousterhout's "precision-adding" *and* "intuition-adding" comment simultaneously: it documents a non-obvious constraint (the old API doesn't enforce this permission rule) that a reader absolutely cannot derive from the code alone — the whole point of the comment is to explain a gap in a *different* system the current code has to compensate for. This is also a clean instance of Martin's legitimate "clarification of intent" category, and directly matches the business-rule sub-outcome the brief names.

**Conclusion:** the existing 3-way framework produces sensible classifications on all three new examples without modification. No gap surfaced. The one genuine nuance worth stating explicitly (not a framework gap, but worth naming): classification of a "why" comment like Example 2 is not purely a property of the comment text — it depends on the comment actually being attached to the code it explains. `contexts/code-comments.md` already implies this (it always shows comment + code together) but doesn't say it outright; worth a one-line addition there if this file's finding is promoted to production (see main research report).

## Sources

- [Microsoft Writing Style Guide — Welcome](https://learn.microsoft.com/en-us/style-guide/welcome/) and [Top 10 tips for Microsoft style and voice](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice) — conciseness, scanning-first, "make every word matter."
- [Google developer documentation style guide — Voice and tone](https://developers.google.com/style/tone) — conversational-but-respectful register, second person/active voice/present tense, caution against over-politeness.
- [Google developer documentation style guide — About this guide](https://developers.google.com/style) — general framing of the guide's authority and scope.
- This project's own `.claude/skills/code-comment-humanizer/SKILL.md` (English-language comment cleanup) — internal precedent for the why-vs-what distinction, extended here to Thai. Note: this skill is not part of this repository (not found under `.claude/skills/` in this project) — it's referenced as a cross-skill pointer from `SKILL.md`, likely a global/plugin skill available at runtime but not a local file this research could inspect directly.
- Robert C. Martin, *Clean Code*, ch.4 "Comments" — summarized via [LinkedIn summary](https://www.linkedin.com/pulse/summary-clean-code-chapter-4-comments-robert-c-martin-ilias-el-mhamdi), [GitHub notes](https://github.com/azizkayumov/clean-code/blob/main/comments.md), and [gist summary](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29) — not read from the primary book text directly in this pass, treat as secondary-source triangulation, consistent across multiple independent summaries.
- John Ousterhout, *A Philosophy of Software Design* — summarized via search snippets and [johnousterhout/aposd-vs-clean-code](https://github.com/johnousterhout/aposd-vs-clean-code) (Ousterhout's own comparison of his book against Martin's) — not read from primary text directly in this pass; the aposd-vs-clean-code repo is a first-party source (written by Ousterhout himself) comparing the two philosophies, which is a stronger secondary source than a random summary.
