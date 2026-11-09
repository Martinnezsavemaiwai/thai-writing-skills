# Native-Speaker Validation Plan

**Status: methodology only. Zero entries in this project — no taxonomy pattern, no corpus example, no benchmark case — have been reviewed by a native Thai speaker as of this research pass.** Every example currently in `thai-ai-smell-taxonomy.md`, `benchmark/cases.yaml`, and the skill's `examples/*.md` is model-generated and research-derived, not human-validated. Do not describe the skill as "native-speaker validated" until this methodology (or an equivalent one) has actually been run and its results recorded here.

## Three categories, kept separate

- **Research evidence** — claims traceable to an external source (a style guide, an academic paper, a standard). Lives in the other `research/*.md` files, tagged `[Source-backed principle]`.
- **Model-generated examples** — every bad/better example pair, every taxonomy entry's `bad_example`/`better_example`, every benchmark case's `input`/`good_examples`. These read as plausible to the model that wrote them; that is not evidence they read as natural to an actual Thai speaker. Tagged `[Observed pattern]` or `[Project decision]` throughout this project, never upgraded to source-backed status by virtue of being written confidently.
- **Human-validated examples** — currently an empty set. This file exists to define how examples move from the middle category into this one.

## Why borrow from translation-industry QA instead of inventing a rubric

This project already has a 7-dimension rubric (`benchmark/rubric.md`: Meaning Preservation, Naturalness, Context Fit, Audience Fit, Terminology Consistency, Conciseness, AI-Smell). Rather than treat that as a from-scratch invention, it's worth checking against an established, widely-used framework — if they converge, that's evidence the rubric carves reality at reasonable joints; if they diverge, that's useful signal too.

`[Source-backed principle]` **MQM (Multidimensional Quality Metrics)**, developed under the EU-funded QT21/QTLaunchPad project (DFKI), is the industry-standard analytic framework for translation/localization quality evaluation, later harmonized with TAUS's DQF into a shared error typology. MQM annotates errors as a substring of the text with a **category** and a **severity** (minor / major / critical), rather than a single holistic score. Its top-level dimensions: **Accuracy** (mistranslation, addition, omission, untranslated content), **Terminology** (incorrect/inconsistent term usage), **Linguistic conventions** (grammar, punctuation, unintelligibility — i.e. fluency/naturalness), **Style** (tone/register appropriateness), **Locale conventions**, **Audience appropriateness**, and **Design/markup**.

**Cross-mapping MQM onto this project's rubric:**

| This project | MQM equivalent | Fit |
|---|---|---|
| Meaning Preservation | Accuracy | Direct match |
| Naturalness | Linguistic conventions | Direct match |
| Context Fit | Locale conventions | Direct match |
| Audience Fit | Audience appropriateness | Direct match — validates that this project's Phase-6 addition (splitting Audience Fit out from Context Fit) tracks a real, independently-recognized MQM dimension, not an invented one |
| Terminology Consistency | Terminology | Direct match |
| Conciseness | Style (partial) | Style is broader in MQM (covers register generally); this project's Conciseness is narrower (padding/redundancy specifically) — Conciseness is this project's own specialization, not a 1:1 MQM category |
| AI-Smell | *(no MQM equivalent)* | Genuinely novel to this project's purpose — MQM predates the "does this read as machine-generated" question; this dimension has no external validation to lean on and should be weighted accordingly |

This is reassuring: 5 of 7 dimensions have a direct, independently-developed analogue, which is evidence the rubric isn't arbitrary. `AI-Smell` and (partially) `Conciseness` are this project's own additions and carry correspondingly less external backing — reviewers should be told this explicitly so they don't assume every dimension is equally well-established.

`[Source-backed principle]` MQM's severity model (minor/major/critical, defined respectively as: limited impact vs. no seriously impeding effect; seriously affects understandability/reliability/usability; renders content unfit for purpose or risks real-world harm) is directly reusable for calibrating how much weight a single reviewer disagreement should carry — a "minor" naturalness quibble on one case shouldn't block encoding a pattern; a "critical" meaning-preservation failure should.

`[Source-backed principle]` **Nielsen's usability heuristics** (Nielsen Norman Group) aren't a translation-QA framework, but two are directly relevant to reviewing UX copy specifically: "Match between system and the real world" (use the user's language, not internal jargon) and "Help users recognize, diagnose, and recover from errors" (error messages in plain language, precisely indicating the problem, constructively suggesting a solution). These aren't a replacement for the MQM-based rubric above — they're a supplementary checklist specifically for the `ux-writing`/`notifications` context categories, since MQM was built for translation pairs, not originated-in-target-language UX copy.

## Methodology

### Who reviews

- **Minimum 2 reviewers per case**, not 1 — a single reviewer's judgment is a data point, not a validation; disagreement is itself informative (see below).
- Reviewers should be **native Thai speakers with actual software industry context** (engineers, PMs, designers, or QA who read/write product Thai as part of their job) — not just any Thai speaker. Context/audience appropriateness (e.g. "is this the right register for a PM status update") requires domain familiarity a general native speaker won't reliably have; this project's own `real-product-observations.md` findings (e.g. the AIS severity-based register shift) required someone who'd recognize that pattern as intentional, not accidental.
- Where possible, include at least one reviewer whose primary role is content/copy (a Thai UX writer or technical writer) alongside at least one engineer — the taxonomy spans both code-comment and UX-copy contexts, and a single background won't cover both well.

### What they review

A sample drawn from `benchmark/cases.yaml` (currently an 18-case starter set) plus a subset of `examples/*.md`. Reviewers see:
1. The `input` (the "before")
2. The proposed `good_examples`/`better_example` (the "after")
3. The stated `context` and `audience` (so they're judging fit, not guessing it)

They do **not** see this project's own reasoning/tags (`[Observed pattern]` etc.) before scoring — seeing the model's own justification first would bias the rating toward agreement. Reasoning is shown only after scoring, to explain *why* a rewrite was made, for the reviewer to react to separately.

### How they score

Per case, per dimension (the 7-dimension rubric above), a **1–5 Likert scale**, not binary pass/fail — this matches standard localization-QA practice of graded scoring rather than accept/reject, and matches this project's own `benchmark/rubric.md` scale already. For AI-Smell specifically, additionally ask a binary question: "would you, a Thai reader, guess this was AI-written?" — this is the one dimension worth keeping a simple check on directly, since it's the project's own novel concern with no external benchmark to lean on.

**In-context, not isolated-string, review where the context materially matters.** Standard localization QA distinguishes reviewing a string in isolation vs. reviewing it embedded in its real surface (a screenshot of the actual button, the actual code file for a comment). For `ux-writing`/`notifications` cases, prefer showing the surrounding screen/flow where feasible; for `code-comments`, show the actual surrounding code, not just the comment text — a decontextualized string review is known to produce different (often worse-calibrated) judgments than in-context review.

### Resolving disagreement

- If both reviewers agree within 1 point on every dimension: average the scores, done.
- If reviewers disagree by 2+ points on any dimension, or disagree on the binary AI-smell question: this is not immediately averaged — flag the case for a third reviewer or a short discussion between the two, since a 2+ point gap usually means they're evaluating different things (e.g. one assumed a more formal audience than the other), which is itself a finding about whether the case's stated `context`/`audience` was clear enough.
- Track inter-rater agreement rate over time as a coarse health signal — a taxonomy pattern where reviewers consistently disagree is a candidate for rewriting `when_it_is_valid`, not just re-scoring.

### What changes once a case is reviewed

- A taxonomy entry, corpus example, or benchmark case that scores ≥4/5 average on all 7 dimensions from ≥2 independent reviewers gets its confidence tag upgraded from `[Observed pattern]`/`[Project decision]`/`hypothesis`-level confidence to **human-validated** — a new status distinct from `[Source-backed principle]` (which means "an external authority says so") since this means "native speakers with domain context confirmed it in practice." Record the reviewer count and average scores next to the upgraded entry, don't just flip a label silently.
- A case scoring low on Meaning Preservation or Naturalness specifically should be corrected or removed, not kept with a caveat — those two dimensions are the ones this skill cannot function without getting right.
- A case scoring low on AI-Smell agreement (reviewers disagree on whether it reads as AI-written) should be treated as evidence that pattern is more context-dependent than currently documented, and its `when_it_is_valid` list should be revisited — this is the exact self-correction path the "no blacklist" design goal depends on actually working in practice, not just in theory.

## Reviewer-facing questions (Evidence Hardening pass)

The methodology above is the *analytic* structure (7-dimension Likert scoring, MQM-grounded). It's not how you'd actually hand a case to a working Thai reviewer — nobody scores "Terminology Consistency: 4/5" as a first instinct. This section adds the actual **questions to ask a reviewer**, in Thai, mapped onto the existing rubric so the two systems produce comparable data rather than two disconnected review layers.

```text
1. ความหมายเดิมยังอยู่ครบหรือไม่?              → Meaning Preservation
2. อ่านเป็นภาษาไทยธรรมชาติหรือไม่?              → Naturalness
3. เหมาะกับบริบทนี้หรือไม่?                     → Context Fit
4. เหมาะกับคนที่จะอ่านข้อความนี้หรือไม่?         → Audience Fit
5. กระชับพอดีหรือไม่?                          → Conciseness
6. มีคำหรือโครงสร้างที่ฟังเหมือนแปลจากอังกฤษหรือไม่? → AI-Smell (specifically the calque/translation angle)
7. ถ้าอยู่ใน Product จริง คุณจะเขียนแบบนี้ไหม?    → holistic gut-check (see below)
```

**Coverage gap, noted explicitly:** none of the 7 questions map to **Terminology Consistency**. This isn't an oversight in the 7-question list — terminology consistency is a *cross-string* property (does this rendering match the product's glossary and its use elsewhere), not something a single case shown in isolation can answer. `[PROJECT_DECISION]`: terminology consistency needs its own check, separate from the 7 questions — either (a) show the reviewer the product's glossary alongside the case and ask directly "does this match the glossary?", or (b) for cases without a stated glossary, skip scoring this dimension entirely (as `benchmark/rubric.md` already instructs: score N/A rather than guess). Do not fold it into question 3 (Context Fit) — a term can fit its context perfectly while still contradicting how the same concept is rendered three screens over.

**Question 7 is not a rubric dimension — it's a validity check on all of them combined.** "Would you actually ship this in a real product" is the question a reviewer asks after already having opinions on 1–6; if a reviewer answers "no" to 7 while scoring everything else 4-5, that's a signal the rubric itself is missing something the case has legitimately wrong. Treat a 7=no with high 1-6 scores as a case worth discussing, not averaging away.

### Reviewer response fields, beyond scores

Each dimension keeps its 1–5 Likert score, but every case review also collects:

- `preferred_output` — what the reviewer would actually write instead, if different from what's shown. This is the single most useful field: a score tells you something is wrong, this field tells you what right looks like.
- `reason` — why (free text, can be as short as "ฟังดูแปลจากอังกฤษ" or as specific as pointing at one phrase)
- `alternative` — a second acceptable option, when the reviewer genuinely thinks two renderings are both fine (this is itself useful data — a case where two independent reviewers give two different `preferred_output`s that are both plausible is evidence the "one correct answer" framing was wrong for that case, and the benchmark/corpus entry should record both rather than picking one arbitrarily)

### Where human review data actually lives (mechanism, not just principle)

**Human review results go in `research/human_review/`, never inside the same file as model-generated content.** This is a hard separation, not a labeling convention within one file, because a shared file makes it too easy for a future edit to blur "the model said" and "a human confirmed" — this project's stated rule ("never mark content as human-validated without actual human input") only holds if that's structurally hard to violate by accident.

Concretely, once review actually happens:
- One record per reviewed case, e.g. `research/human_review/eng-001.yaml` (matching the case `id` from `benchmark/cases.yaml` or `research/product-thai-corpus.md`), containing: reviewer count, each reviewer's 7 scores + 7-question answers + `preferred_output`/`reason`/`alternative`, the resolved/averaged score, and the resolution method if reviewers disagreed (see "Resolving disagreement" above).
- The *only* thing that changes in the original case file (in `benchmark/cases.yaml` or the corpus) is flipping `human_validated: false` → `true` (see the corpus schema's `human_validated` field) with a pointer comment to the `human_review/` record — the case's own `input`/`better_output`/`reasoning` text is never edited by review results directly; if review shows the original `better_output` was wrong, that becomes a tracked correction (a new corpus/benchmark entry version), not a silent overwrite that erases what the model originally proposed.
- **This directory does not exist yet in this repository.** Per the "don't create empty documentation files" instruction governing this phase, `research/human_review/` is a documented convention here, not a scaffolded empty folder — it gets created when the first real review round actually happens, with real content, not before.

## What this project has NOT done (be explicit)

- No reviewers have been recruited.
- No cases have been scored.
- No confidence tag in `thai-ai-smell-taxonomy.md`, no example in `examples/*.md`, and no case in `benchmark/cases.yaml` currently carries "human-validated" status.
- This methodology itself has not been pilot-tested — the 2-reviewer/1-point-tolerance thresholds above are reasonable defaults borrowed from general translation-QA practice, not numbers this project has tuned empirically. Treat them as a starting point to adjust once a first real review round happens.

## Sources

- [MQM Council — Multidimensional Quality Metrics framework](https://www.themqm.org/) and [MQM History](https://themqm.org/mqm-history/) — framework origin (QT21/QTLaunchPad, DFKI), later harmonization with TAUS DQF.
- MQM error typology and severity levels — summarized via search (direct fetch of `themqm.org/error-types-2/` returned HTTP 403 in this pass; the dimension list and severity definitions above are cross-checked across multiple independent secondary summaries in the search results, including academic papers citing MQM's dimension set consistently) — `[Open question]`: revisit with a direct fetch of the primary MQM error-types page before treating the exact dimension list as final.
- [10 Usability Heuristics for User Interface Design — NN/G](https://www.nngroup.com/articles/ten-usability-heuristics/) — directly fetched; source for "match with real world" and "help users recognize/diagnose/recover from errors" heuristics referenced above.
- General localization-QA practice (in-context vs. isolated-string review, Likert-scale scoring over binary pass/fail) — this is standard, widely-documented industry practice rather than attributable to one named source; treat as `[Observed pattern]` from cross-referencing multiple localization-industry articles in this and prior research passes, not a single citation.
