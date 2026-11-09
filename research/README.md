# Research Index

This directory backs `thai-product-writer` (`.claude/skills/thai-product-writer/`) and, for punctuation and formatting, `thai-writer` (`.claude/skills/thai-writer/`). It exists so the skill's rules are traceable to a source, an observed pattern, a deliberate project decision, or a flagged open question — never presented as settled fact when it isn't. See each file's own tagging legend (`[Source-backed principle]` / `[Observed pattern]` / `[Project decision]` / `[Open question]`).

## Files

| File | Covers |
|---|---|
| [sources.md](sources.md) | Consolidated bibliography, deduplicated across all research files |
| [thai-writing-principles.md](thai-writing-principles.md) | Sentence-level language problems: structure, calques, register, connectors |
| [technical-writing-research.md](technical-writing-research.md) | Code comments, README/docs, API docs, PRs/issues, release notes |
| [ux-writing-research.md](ux-writing-research.md) | Error messages, confirmations, notifications, empty states, labels/buttons, forms, accessibility |
| [real-product-observations.md](real-product-observations.md) | What could (and couldn't) be verified about LINE/Grab/SCB/K PLUS/AIS/True/Shopee/Lazada/Google/Microsoft Thai copy |
| [business-writing-research.md](business-writing-research.md) | Acceptance criteria, business rules, internal/stakeholder communication |
| [thai-ai-smell-taxonomy.md](thai-ai-smell-taxonomy.md) | 20-pattern taxonomy (not a blacklist) on the hardened schema — `id`/`name`/`category`/`evidence_type`/mandatory `when_it_is_not_a_problem`/`severity`/`confidence`/`sources`. `superlative_inflation` was removed this pass (ad-copy-era holdover, kept only as a historical note) |
| [terminology-research.md](terminology-research.md) | Why a per-product terminology model, not a fixed dictionary; proposed schema; broadened past Microsoft to ISO 704/12620, TBX, and general localization-industry practice; stress-tested against Order/User/Account/Return ambiguity — `Return` surfaced a distinct **term-conflation risk** (three unrelated concepts sharing one English gloss, not one contested rendering) |
| [native-speaker-validation.md](native-speaker-validation.md) | Methodology for eventually validating the taxonomy/corpus/benchmark against real Thai speakers, now with the 7 concrete Thai reviewer questions mapped onto the rubric, and a concrete storage mechanism (`research/human_review/<case-id>.yaml`) for keeping human judgments separate from model-generated ones — **zero cases have actually been reviewed** |
| [product-thai-corpus.md](product-thai-corpus.md) | Curated input→output writing-decision cases with reasoning — model-generated, `human_validated: false` on every entry |
| [translation-adaptation.md](translation-adaptation.md) | Common English software-writing structures ("You can...", "Please make sure...", "Successfully completed...") and what natural Thai does instead of translating them literally |
| [error-writing-research.md](error-writing-research.md) | When an error message needs just the fact vs. fact+retry vs. full recovery guidance — severity/recoverability/user-control/frequency as the deciding axes, not a fixed 3-part template |
| [punctuation-formatting-research.md](punctuation-formatting-research.md) | Sources for `thai-writer`'s punctuation, spacing, formatting, slide and Thai line-break rules: Royal Institute spacing rules (via a reproduction, full book not checked), em dash as an AI signal (Wikipedia, Plagiarism Today, Rolling Stone), structure and formatting patterns, assertion-evidence, UAX #14 |

## Problem categorization — canonical definition moved

The 7-way problem split (`natural-thai` / `translation` / `ux-writing` / `technical-writing` / `business-communication` / `terminology` / `ai-generation-pattern`) is now defined once, canonically, in **[thai-writing-principles.md](thai-writing-principles.md)'s "Problem categorization" section** — every entry in `thai-ai-smell-taxonomy.md` carries a `category` field using exactly that list. This index no longer duplicates the mapping (it drifted slightly from the taxonomy's actual field values before this pass); go to `thai-writing-principles.md` for the current, authoritative table.

## Context model (Phase 5)

Each file in `../.claude/skills/thai-product-writer/contexts/` opens with this header before the guidance body:

```yaml
context: <name>
purpose: <what this text is for>
audience: <who reads it — see audience model below>
desired_tone: <point on the tone spectrum>
desired_length: <short/medium/long, with a concrete guideline>
must_preserve: <what must never be altered, e.g. exact conditions, error causes>
common_mistakes: <the 2-4 taxonomy patterns most likely to show up here>
```

Adopted contexts: UX/UI copy (buttons, labels, forms, validation, empty states, confirmation dialogs, onboarding — bundled into one `ux-writing.md` because they share one audience/tone decision process), notifications (a distinct surface: push/toast/email, async and interruptive in a different way than in-screen UI), code comments, git commits, pull requests, requirements/acceptance criteria/business rules, documentation (README/technical docs/release notes/API docs), customer-facing content (support, public changelogs).

## Audience model (Phase 6)

Audiences: End User, Customer, Developer, QA, Product Manager, Designer, Stakeholder, Executive, Internal Team. None of these maps 1:1 to a formality level — "professional" does not mean "formal" (an internal Slack message to a PM is professional and casual at once). Tone is a separate spectrum crossed against audience + context: Formal, Professional, Neutral, Conversational, Friendly, Technical, Executive. Full treatment in `../.claude/skills/thai-writer/core/tone.md`.

## Register model (Evidence Hardening pass)

`thai-writing-principles.md`'s "Register model" section grounds Thai register variation in real diglossia research (Diller, *High and Low Thai*) and concludes **Product Thai is its own point on the continuum**, not "spoken Thai applied to software" — it borrows written-register precision with spoken-register directness/brevity, and isn't uniform across this skill's own contexts (UX copy leans Elegant/polite spoken; requirements lean Formal; code comments sit in a Technical register neither classic account names). Explicitly recommends **against** a numeric formality/directness/warmth scoring system — no evidence it would be actionable beyond the qualitative per-context descriptions already in `contexts/*.md`'s headers.

## Terminology model (Phase 7)

See `terminology-research.md` for the research and `../.claude/skills/thai-product-writer/terminology/terminology.md` for the applied schema and `glossary.example.yaml` for a worked example.

## Architecture decision (Phase 12)

The originally proposed tree holds, with one addition: `core/tone.md` (Audience + Tone did not fit cleanly inside the other 5 core files and are load-bearing enough — they're two full pipeline stages — to warrant their own file). No other structural change was justified by this research pass.

## Evidence hierarchy (Evidence Hardening pass)

A rough preference ordering for weighing conflicting claims — **guidance, not an absolute ranking**. Widespread real-product usage can still be poor writing; a Thai-specific source beats a generalized-from-English one only when it's actually spoken to the specific question at hand.

```text
Native-speaker validated Product Thai        (none exist yet — see native-speaker-validation.md)
        ↓
Observed real Product usage                   (AIS/Krungthai NEXT security alerts; thin elsewhere)
        ↓
Thai-specific authoritative guidance           (Microsoft Thai Localization Style Guide, PDPA)
        ↓
Established UX / Technical Writing guidance   (NN/g, Google/Microsoft style guides, Clean Code)
        ↓
Thai linguistic research                       (Iwasaki & Ingkaphirom, Diller, Lekawatana/Sudmuk)
        ↓
Project decision                                (explicit, labeled choices this project made)
        ↓
Model hypothesis                                (reasoned but unverified)
```

Use judgment, not the ladder alone, when sources conflict — see "Documented conflicts" below for cases where this project had to actually make that call rather than mechanically applying the ranking.

## Documented conflicts (Evidence Hardening pass)

Cross-cutting because they span multiple files' topics. Schema: `issue` / `source_a` / `source_b` / `observed_usage` / `project_decision` / `reason` / `confidence`. Only genuine disagreements are logged here — see the note below on one candidate that was deliberately **not** logged as a conflict.

```yaml
- issue: "Fixed friendly/conversational brand voice vs. severity-driven register shifts"
  source_a: "Microsoft Windows apps writing style + Google dev-doc style guide (ux-writing-research.md, technical-writing-research.md) — both push toward one consistent, conversational-but-respectful voice throughout a product"
  source_b: "Direct real-product observation: AIS's fraud-SMS security alert drops all politeness particles and goes to short direct imperatives (real-product-observations.md) — a deliberate, situational register break from a 'consistent voice'"
  observed_usage: "The AIS page is the one directly-verified data point; it contradicts a literal reading of 'keep one consistent brand voice' whenever severity is high"
  project_decision: "Severity/context governs register, not a fixed brand voice — encoded in core/anti-ai.md and core/tone.md. This isn't actually a contradiction of the Western UX sources once read carefully (Microsoft's own error-message guidance already scales tone to severity) — the conflict is with a *naive over-reading* of 'be consistently friendly,' not with the sources' full guidance."
  reason: "One real data point plus the sourced guidance's own severity carve-outs, not two authorities flatly disagreeing"
  confidence: medium

- issue: "Direct/plain-language communication norms vs. Thai high-context/kreng jai indirectness"
  source_a: "Microsoft/Google style guides + this project's own core/clarity.md ('state the rule/fact directly'), and the English-language plain-language movement this project's stance is built on by analogy (business-writing-research.md)"
  source_b: "Thai high-context/kreng jai communication research (business-writing-research.md's Audience-based register research section) — indirectness and softened disagreement are documented, repeatedly-observed norms in Thai workplace communication"
  observed_usage: "No direct product-copy observation confirms which wins in practice for internal Thai business writing specifically — this is a genuine unresolved tension between sourced principles, not yet checked against real usage"
  project_decision: "Split directness from formality as separate axes (core/tone.md's 'Directness is a separate axis from formality' section): requirements/rules/business-rules stay direct regardless of cultural register norms (directness there is a correctness requirement); interpersonal content (feedback, disagreement, bad news) can flex toward Thai cultural indirectness"
  reason: "A real, sourced tension between two legitimate principles, not a case where one source is simply wrong — the resolution is a scope split, not a winner"
  confidence: medium
  open_question: "Exactly where the line sits in ambiguous cases needs native-speaker judgment (research/README.md open question #10) — this conflict is resolved in principle, not yet validated in practice"

- issue: "How skeptical should a code-comment guideline be of comments as a category?"
  source_a: "Google (Software Engineering at Google ch.8 / eng-practices) — comments explaining why are simply good practice, a permissive stance"
  source_b: "Robert C. Martin, Clean Code ch.4 — comments are 'always failures' to express intent in code; the best comment is often the one you don't write, and the real fix is frequently better naming/structure, not better comment wording"
  observed_usage: "N/A — this is a disagreement between two established software-engineering authorities, not a real-vs-guidance conflict"
  project_decision: "Keep the skill's existing 3-way keep/rewrite/delete framework (contexts/code-comments.md) rather than adopting Martin's more radical 'fix the code, not the comment' stance wholesale — but flag when a comment reads as compensating for unclear code, rather than silently polishing its Thai wording (already added to contexts/code-comments.md in the prior pass). Full triangulation lives in technical-writing-research.md's 'Deepening the code-comment decision framework' section."
  reason: "This project's mandate is Thai-language quality, not code refactoring — Martin's critique is noted and partially adopted (the flag) without expanding the skill's scope into code review"
  confidence: high
```

**Deliberately not logged as a conflict:** whether to keep English loanwords (e.g. "ล็อกอิน") or translate them (เข้าสู่ระบบ) for terms like `login`. Real-world Thai product usage genuinely splits on this with no clear majority, but **no authoritative source in this project's research takes a firm position either way** — Microsoft's own terminology guidance explicitly treats this as a per-product convention decision, not a rule with a right answer. A source disagreeing with observed usage is a conflict; multiple products making legitimately different, equally-valid choices in the absence of a rule is just real-world variation. Filed as a per-product `[Project decision]` in `terminology-research.md` instead.

## Open questions not yet resolved

See the tags scattered through each file for full context. Status as of the deep-research pass:

**Resolved/upgraded this pass:**

1. ~~Thai classifier system had no citable academic source~~ — **closed**: Iwasaki & Ingkaphirom, *A Reference Grammar of Thai* (Cambridge University Press) located and verified via catalog/review metadata (primary text not read). `classifier_errors` upgraded to source-backed.
2. ~~`ถูก`/`โดน` passive register rested on two uncross-checked theses~~ — **corroborated, confidence raised to medium-high**: a third academic source (Sudmuk, "The *thuuk* Construction in Thai") confirms this is a studied topic, and multiple independent secondary sources converge on a written-vs-spoken (`ถูก` vs `โดน`) split not previously surfaced. Not raised to "high" — none of the three academic sources were read in full.

**Still open, including new ones surfaced this pass:**

3. Whether Thai engineering teams write PRs/commits/issues in Thai at all varies by team; treat as a per-project setting, not a default.
4. Toast/snackbar and empty-state guidance has no dedicated authoritative source — extrapolated from adjacent principles.
5. Material Design 3's content-design page never loaded (JS-rendered); UX findings lean on the older M1 writing page.
6. Most named real products' actual in-product Thai microcopy (Grab, Lazada, K PLUS, True, LINE beyond a help page, Google/Microsoft Thai locale) has no verifiable public sample. **This pass again tried and failed to find permission-dialog, destructive-action-confirmation, and onboarding copy for any of them, plus SCB EASY and government digital services (DGA/ทางรัฐ)** — this category of text structurally resists web research (it's never published outside the live app) and needs actual device/app access in a future pass, not another search pass.
   - **New this pass, with a caveat:** a second real, directly-verified security-error example was found (Krungthai NEXT), corroborating the AIS finding that severity drops politeness particles. But **both verified real examples are security-warnings specifically** — this may just mean security warnings are more publicly documented (they show up in consumer-protection articles) than routine UI copy, not that the severity-formality relationship generalizes to non-security contexts. Don't over-extend this finding.
7. **Zero taxonomy/corpus/benchmark entries have been checked against a native-speaker review panel.** A concrete methodology for eventually doing this now exists (`native-speaker-validation.md`, grounded in MQM and standard localization-QA practice) — but it has not been run. Do not describe any rule in this project as "native-speaker validated."
8. No taxonomy pattern is currently filed under the `technical-writing` category — the relevant failure modes (comment over-explanation, restating what code does) are filed under `ai-generation-pattern` instead, because the mechanism is general content-redundancy rather than Thai-specific. Revisit if a future pass surfaces a genuinely Thai-technical-writing-specific failure mode.
9. No Thai-language analogue to the English "plain language movement" was found — this skill's plain-language stance for Thai remains a project decision by analogy, not backed by an equivalent Thai institutional effort.
10. The kreng jai/high-context-culture research (`business-writing-research.md`) raises a real open question this project can't settle from outside: exactly where the line sits between "must stay direct because it's a rule/spec" and "can stay indirect because it's interpersonal" needs native-speaker judgment.
11. The "type the exact name to confirm" pattern for Thai destructive-action dialogs (as opposed to typing a Thai word, to avoid tone-mark mismatches) is a `[HYPOTHESIS]`, untested.
12. The `contexts`-field naming convention for internal-vs-customer-facing terminology (`internal-*`/`customer-*` prefixes, see `terminology-research.md`'s schema stress-test) is untested on a real, sizable multi-context glossary.
13. Terminology Consistency has **no coverage in the native-speaker validation protocol** — none of the 7 Thai reviewer questions can catch it, because it's a cross-string property, not something visible from one isolated case. Needs a separate glossary-comparison review step, not yet designed in detail.
14. The Royal Institute spacing and punctuation rules used by `thai-writer` come from a reproduction on trueplookpanya (หลักเกณฑ์ฉบับพิมพ์ครั้งที่ 7 พ.ศ. 2551 หน้า 56-66), not the book. The full PDF could not be text-extracted, so the rules and the absence of an em dash entry are unchecked against the real book (`punctuation-formatting-research.md`).
15. The punctuation and formatting patterns (em dash, bold labels, chatbot openers and closers) are `SOURCE_BACKED` only as English patterns from Wikipedia: Signs of AI writing. Arrows used as connectors in prose are a `[Project decision]`, not from that list. Whether they show up in real Thai AI-written text more than in human-written Thai has not been checked against a Thai corpus (`[Hypothesis]`).
