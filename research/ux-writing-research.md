# UX Writing Research

Scope: general UX writing principles from Google and Microsoft, translated into guidance for Thai-language software product text. Feeds `contexts/ux-writing.md` and `contexts/notifications.md` in the skill.

Tags used below: **[Source-backed principle]** — traceable to a cited guideline. **[Observed pattern]** — seen in a real product but not from an official style doc. **[Project decision]** — a choice this skill makes where sources disagree or are silent. **[Open question]** — unresolved, needs more evidence or native-speaker review.

## Cross-source baseline (Google + Microsoft agree on these)

- **[Source-backed principle]** Address the user directly in second person ("you"/your work); keep the app's own voice out of the sentence except when the app itself performs an action for the user. (Material Design writing guidelines, m1.material.io/style/writing.html; Microsoft Windows apps writing style)
- **[Source-backed principle]** Lead with the point. Don't preface with throat-clearing ("if you want to add effects, select filters" → "select filters to add effects"). (Microsoft Windows apps writing style)
- **[Source-backed principle]** Use active voice; describe the user and the app as doing things, not having things done to them. (Microsoft Windows apps writing style, m1.material.io)
- **[Source-backed principle]** Write short, scannable segments — don't assume the user reads every word. (Both sources)
- **[Source-backed principle]** Be positive/reassuring rather than alarming, except where the situation genuinely is urgent (see Error messages below and the AIS security-alert observation in `real-product-observations.md`, which is a deliberate exception). (Material Design)
- **[Source-backed principle]** Don't blame the user in error copy; the product takes responsibility for what it can fix, and gives a real next step. (Microsoft: "Be warm and relaxed", "Be ready to lend a hand")

## Thai-specific translation of the baseline

- **[Project decision]** "Second person, active voice" in Thai does not require inserting a literal subject pronoun ("คุณ") in every sentence — Thai naturally drops the subject when it's understood from context (this is normal Thai grammar, not evasiveness). Forcing "คุณ" into every UI string to satisfy an English-derived "always say you" rule produces the literal-translation smell described in `review/thai-ai-smells.md`. Apply the *intent* (make the user the actor) without forcing the pronoun.
- **[Open question]** How to translate Microsoft's "use contractions, avoid stiffness" guidance into Thai, which has no direct grammatical equivalent to English contractions. The working hypothesis is that the Thai analogue is register choice (spoken-register connectors and particles vs. written/bureaucratic connectors) rather than a 1:1 substitution — needs native-speaker review before being stated as a rule.
- **[Source-backed principle, adapted]** One Thai UX-writing source (see Sources) notes Thai can omit the subject freely, and that register should shift by formality: กรุณา ("please") reads as more formal/service-context, ลอง ("try") reads as more casual/coaching-context. This lines up with the Microsoft guidance to reserve "please" for situations where the user is genuinely being asked to do something inconvenient.

## By category

### Error messages

- **[Source-backed principle]** Don't blame the user; state what happened and, if possible, what to do next; only apologize for things the product itself is responsible for, not for network/third-party failures. (Microsoft Style Guide "sorry" entry; Windows apps writing style)
- **[Source-backed principle]** Avoid technical jargon the end user can't act on. (Both sources)
- **[Observed pattern]** A published Thai UX-writing case study (rewriting 47 error messages with 8-person usability testing) reported cutting a transaction-abandon rate from 38% to 19% after the rewrite — cited as evidence that error-copy quality has measurable product impact, not just a style question. (See Sources — this is a single secondary-source case study, treat the specific numbers as illustrative, not as a benchmark to replicate.)
- **[Observed pattern]** In a real Thai security-alert page (AIS fraud-SMS warning, see `real-product-observations.md`), politeness particles are dropped entirely and sentences become short, direct imperatives when the message is a genuine warning. This is a deliberate register shift, not sloppiness — **[Project decision]**: the skill should treat "drop ค่ะ/ครับ, go direct" as valid for high-severity/security errors, not as an AI-smell.

### Confirmations / dialogs

- **[Source-backed principle]** The dialog title and its buttons must form a clear question-and-answer pair ("call and response") — buttons should read as direct answers to the title, and button phrasing should be consistent across the app. (Microsoft Windows apps writing style)
- **[Source-backed principle]** Keep dialog body text as short as the decision requires; dialogs interrupt the user's flow, so get them back to their task fast. (Microsoft)

### Notifications / toasts

- **[Project decision]** No single cited source (Google/Microsoft docs found) targets toast/snackbar copy specifically in the sources reviewed here — treat the general "short, scannable, positive-first" principles as applying, and flag this as thin coverage. **[Open question]**: find a toast/snackbar-specific style reference in a follow-up research pass.

### Empty states

- **[Open question]** No dedicated source found in this pass. General principle applied by extension from "lead with what's important" + "don't overload with unnecessary info": an empty state should say what's missing and, where relevant, what action fills it — not apologize at length. Needs a dedicated source before being written as a hard rule.

### Labels / buttons

- **[Source-backed principle]** Button text should be readable at a glance — at most a couple of short words — and should name the action (active voice), e.g. "Install now" rather than a passive description. (Microsoft Windows apps writing style)
- **[Source-backed principle]** Refer to the actual on-screen label, not the element type — "select **Continue**", not "click the button". (Material Design writing guidelines)
- **[Source-backed principle]** Use consistent verbs for the same action everywhere in the product; don't vary "ลบ" vs "เอาออก" vs "นำออก" for the same delete action across screens. (Material Design "consistency" guidance, generalized)

### Forms / validation

- **[Open question]** Neither source reviewed here gives Thai-specific form-validation guidance. General principle carried over from error-message guidance: validation text should say what's wrong and how to fix it, not just "ข้อมูลไม่ถูกต้อง" (invalid data) with no detail — this is a **[Project decision]** applied from the error-message principle above, not yet a directly-sourced rule for forms specifically.

### Accessibility / plain language

- **[Source-backed principle]** Write for both new and experienced readers; avoid unusual/specialized words when a plain one works, partly because plain language is also easier to localize. (Microsoft: "Accessibility and localization" section, Windows apps writing style)
- **[Open question]** Reading-level guidance (e.g., a Thai equivalent of English's "8th-grade reading level" heuristics) was not found in this pass — no verifiable Thai-specific readability standard located.

## Permissions

- **[Source-backed principle]** An effective permission-request rationale is framed around the user's benefit, not the app's feature list. NN/g's own before/after comparison: ineffective — "Party Planner would like to access your address book to show you the cheapest attractions by your contacts' location and other purposes" (vague, feature-centric); effective — "Skyscanner would like to access your location, so that you can quickly select departure airports near you" (names the concrete payoff). A controlled test in the same research found the most compelling rationale produced an 81% lift in grants over the least compelling one for the same permission. (NN/g, "3 Design Considerations for Effective Mobile-App Permission Requests")
- **[Source-backed principle]** Timing matters as much as wording: a context-triggered request (user taps the camera icon, then the camera-permission dialog appears) is granted far more often than a system-initiated request (permission asked at app launch, before the user has done anything that explains why). Request only what's needed for first launch; ask for everything else at the point of use. (NN/g, same article; Android Developers, "Request runtime permissions")
- **[Source-backed principle]** Android's own guidance: the rationale UI should state what data is being accessed and what the user gets for granting it, and must let the user back out of the explanation screen without being forced into the system dialog. (developer.android.com/training/permissions/requesting)
- **[Project decision]** Applying the above to Thai: state the benefit in one plain clause, not a formal justification. `[Bad, formal/vague]`: "แอปพลิเคชันมีความจำเป็นต้องเข้าถึงตำแหน่งที่ตั้งของท่านเพื่อวัตถุประสงค์ในการให้บริการที่ดียิ่งขึ้น" `[Better]`: "ใช้ตำแหน่งของคุณเพื่อหาร้านใกล้คุณ" — same shape as NN/g's Skyscanner example, translated as a concrete payoff rather than a formal justification clause. The vague version also triggers `excessive_formal_connectors`-adjacent bureaucratic phrasing ("เพื่อวัตถุประสงค์ในการ...") that the taxonomy already flags.
- **[Source-backed principle, Thai-specific]** Thailand's PDPA (Personal Data Protection Act) requires consent/permission-style requests to use "ภาษาที่อ่านง่าย" (easy-to-read language) with "ข้อความไม่กำกวม" (unambiguous phrasing), stated separately from other text, with an explicit affirmative action (e.g. a real checkbox, not a pre-checked one) — this is a genuine Thai-specific, legally-grounded reason to prefer plain permission/consent copy over formal legal-sounding phrasing, independent of the general UX argument above. (pdpa.pro, "เคลียร์ชัดเรื่อง consent ตาม PDPA")
- **[Observed pattern, Thai-specific]** General Thai consumer-tech commentary (NSTDA's public guidance, Sanook's consumer-tech section) treats "apps requesting more permissions than they need" as a recognized, named problem Thai users are told to watch for — this doesn't give wording guidance, but it does confirm Thai users are primed to notice over-broad or unexplained permission requests, which strengthens the case for a stated rationale rather than a bare system dialog. `[OPEN QUESTION]`: no citable source with actual Thai-language in-app rationale copy was found — the "better" example above is this project's own construction, not a verified real string.

## Destructive actions

- **[Source-backed principle]** Reserve confirmation dialogs for actions with serious, hard-to-reverse consequences — not routine operations. Overusing them trains users to click through automatically, which defeats the safety purpose entirely. (Nielsen, via NN/g "Confirmation Dialogs Can Prevent User Errors")
- **[Source-backed principle]** Never use generic "OK/Cancel" or "Yes/No" for a destructive confirmation. Buttons should each state the outcome: NN/g's example is "Delete file" / "Keep file", not "OK" / "Cancel" — this mirrors this skill's existing confirmation-dialog guidance in `contexts/ux-writing.md` (title and buttons as a question-and-answer pair), and adds the specific finding that "Are you sure?" alone is not protective, because the user is just re-confirming a choice they already made.
- **[Source-backed principle]** Severity should scale the confirmation mechanism, not just the wording: standard case gets descriptive buttons; higher-risk gets a "tell me more" expansion; the most dangerous, hardest-to-reverse actions (NN/g cites Mailchimp requiring the user to type a specific word to delete a mailing list) should require a non-standard action, specifically because a single click becomes reflexive and stops functioning as a real checkpoint.
- **[Project decision]** For Thai destructive-action copy: name the specific consequence, not a generic warning. `[Bad, generic]`: "คุณแน่ใจหรือไม่ว่าต้องการดำเนินการต่อ" (says nothing about what happens). `[Better]`: "ลบบัญชีนี้ถาวร ข้อมูลทั้งหมดจะหายไปและกู้คืนไม่ได้" paired with buttons "ลบบัญชี" / "ยกเลิก" — matches this skill's `contexts/ux-writing.md` confirmation-dialog guidance and NN/g's "state the outcome" principle simultaneously. For a type-to-confirm pattern in Thai, matching the exact product/account name the user must type is safer than asking them to type a Thai word, since it avoids tone-mark/spelling mismatches silently failing the check — `[HYPOTHESIS]`, not tested.
- `[OPEN QUESTION]`: no verifiable real Thai product's destructive-action confirmation copy was found this pass (see `real-product-observations.md`) — the examples above are this project's own construction from the sourced English-language principles, not observed Thai strings.

## Onboarding

- **[Source-backed principle]** Progressive disclosure — revealing complexity gradually instead of upfront — is the governing principle for onboarding, originally named by Jakob Nielsen. Research NN/g cites shows it can cut task-completion time 20–40% while improving comprehension, and it improves 3 of the 5 core usability components (learnability, efficiency, error rate). (NN/g-linked progressive-disclosure research, via UXPin/secondary summaries — the specific 20–40% figure is from a secondary source, not independently re-verified against NN/g's primary publication; treat the number as illustrative)
- **[Source-backed principle]** A commonly cited structure caps disclosure at 2 levels within any single interaction, and for a full onboarding journey uses 3 layers: orientation (what is this, why am I here), contextual (feature explained at the moment it's first used, not upfront), and power-user (advanced options discovered later, not forced early).
- **[Project decision]** This directly reinforces this skill's existing stance in `contexts/ux-writing.md` that onboarding is the one place where some restating of the obvious is legitimate pedagogy — but progressive disclosure specifically means *pacing* that explanation across the moment-of-first-use, not front-loading it all into a single wall-of-text first screen. A Thai onboarding flow that explains every feature on screen one before the user has touched anything is over-explaining even by onboarding's more lenient standard.
- `[OPEN QUESTION]`: no verifiable Thai-language onboarding flow from a named real product was found this pass (see `real-product-observations.md`).

## Sources

- [Material Design (M1) — Writing style guidelines](https://m1.material.io/style/writin+g.html) — fetched and summarized directly.
- [Material Design 3 — Content design overview](https://m3.material.io/foundations/content-design/overview) — page exists and is the current official content-design section, but direct fetch was blocked (script-rendered page returned no body text); guidance above relies on the M1 writing page and secondary summaries, not a direct M3 read. **[Open question]**: revisit with a renderer that executes JS, or find an archived/text mirror.
- [Microsoft Learn — Writing style, Windows apps](https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style) — fetched and summarized directly; primary source for tone/voice, error messages, dialogs, buttons sections above.
- [Microsoft Style Guide — "sorry" entry](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/s/sorry) — found via search, not directly fetched; cited claim (apologize only for product's own faults) is consistent across multiple search snippets referencing the Microsoft Style Guide, but should be directly re-verified.
- Tang Thaneesa, ["UX Writing"](https://medium.com/@tangthaneesa/ux-writing-1240e9e6572b) and mirror on [tangthaneesa.wordpress.com](https://tangthaneesa.wordpress.com/2019/11/02/ux-writing/comment-page-1/) — Thai-language UX writing commentary; direct fetch returned HTTP 403, so the subject-omission/กรุณา-vs-ลอง register point above is taken from search-result summaries of this article, not a direct read. **[Open question]**: needs direct verification.
- VisionXBrain, ["Error Message คืออะไร? 5 หลักเขียนให้ลูกค้าไม่หนีเว็บ"](https://visionxbrain.com/blog/error-message-best-practices) — source of the 47-message/38%→19% case study, found via search snippet only, not directly fetched. Treat as a single secondary account, not a verified statistic.
- [AIS — cyber threat alert: fake SMS warning](https://www.ais.th/consumers/help-and-support/cyber-threat-alerts/fake-sms1) — fetched directly; real-product evidence for the security-alert register shift noted above.
- [NN/g — 3 Design Considerations for Effective Mobile-App Permission Requests](https://www.nngroup.com/articles/permission-requests/) — fetched directly; primary source for the Permissions section above.
- [Android Developers — Request runtime permissions](https://developer.android.com/training/permissions/requesting) — fetched via search summary; permission-rationale-UI requirements.
- [NN/g — Confirmation Dialogs Can Prevent User Errors](https://www.nngroup.com/articles/confirmation-dialog/) — fetched directly; primary source for the Destructive actions section above.
- [pdpa.pro — เคลียร์ชัดเรื่อง consent ตาม PDPA](https://pdpa.pro/blogs/pdpa-consent) — fetched directly; Thai-specific, legally-grounded plain-language requirement for consent/permission text.
- [NSTDA — วิธีตรวจสอบการให้สิทธิ์ App ในมือถือ](https://nstda.or.th/home/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%AA%E0%B8%AD%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B8%AA%E0%B8%B4%E0%B8%97%E0%B8%98%E0%B8%B4/) and [Sanook — วิธีดูค่าแอปมือถือว่าตัวไหนขอสิทธิ์การเข้าถึงอะไร](https://www.sanook.com/hitech/1608595/) — found via search, confirm Thai consumer awareness of over-broad permission requests as a named concern, no wording guidance.
- Progressive disclosure / onboarding structure — synthesized via search summaries (UXPin and others secondarily citing NN/g's original progressive-disclosure work); the specific 20–40% task-time figure is from a secondary source, not independently re-verified against an NN/g primary page.

## What this pass did not cover (flag for a follow-up research pass)

- Google's actual M3 content-design page text (blocked on fetch — see Sources).
- Any Thai-specific UX writing style guide published by a Thai company/agency as an internal or public standard (none surfaced in this search pass).
- Toast/snackbar and empty-state guidance from a named authoritative source.
- Accessibility/reading-level guidance specific to Thai.
- Verbatim/paraphrased real Thai permission-request, destructive-action-confirmation, or onboarding copy from a named product — despite a dedicated search pass, none was found publicly indexed (see `real-product-observations.md`); the Thai examples in the Permissions/Destructive actions/Onboarding sections above are this project's own constructions from sourced English-language principles, not observed real strings.
