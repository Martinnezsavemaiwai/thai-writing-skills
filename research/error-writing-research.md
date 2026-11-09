# Error-Writing Research

Scope: what makes a Thai software-product error message good, and — the part existing guidance under-emphasizes — when *less* detail is correct. Feeds `contexts/ux-writing.md`'s error-message guidance and `core/conciseness.md`.

Tags: `[SOURCE_BACKED]` / `[OBSERVED]` / `[PROJECT_DECISION]` / `[HYPOTHESIS]` / `[OPEN QUESTION]`.

## The three-question frame — and why it's not a checklist

`[SOURCE_BACKED]` Nielsen Norman Group's Error-Message Guidelines (Neusesser & Sunwall, 2023 — directly fetched) converge with Usability Heuristic #9 ("Help Users Recognize, Diagnose, and Recover from Errors") on: use plain language, describe the exact problem without excessive technical detail, and offer constructive next steps rather than just naming the problem. This maps onto three questions a good error answers: **what happened, what does it affect, what can the user do next.**

`[PROJECT_DECISION]` The task brief is explicit that these three should not be forced into every error, and the research agrees with that instinct even though NN/g doesn't phrase it this way directly: NN/g's own guidance to "match message severity to impact" (banners for warnings, modals for critical errors) already implies the *amount* of information should scale with the situation, not be maximized every time. A one-line search-empty-state ("ไม่พบผลลัพธ์") answering only "what happened" is not an incomplete error — for a low-stakes, instantly-retriable, fully-recoverable situation, "what happened" already implies "try a different search" without needing to spell it out.

## Axes that determine how much an error needs to say

None of these are individually sourced as a named "framework" — this is this project's synthesis of NN/g's severity-matching principle, the Hostile Patterns article's warning against over-styling routine messages as errors, and the existing AIS/Krungthai NEXT real-data points on severity-driven register (see `real-product-observations.md`). Treat the axes as `[PROJECT_DECISION]`, grounded in `[SOURCE_BACKED]` component principles:

- **Severity** — how bad is the outcome if the user does nothing? A failed search vs. a failed payment vs. a compromised account warrant escalating detail. (See the AIS/Krungthai NEXT real examples — both maximum-severity, both maximally direct and specific about cause.)
- **Recoverability** — can the user just retry, or is the action's effect permanent/hard to reverse? An easily-retried failure needs less hand-holding than one where the wrong recovery step makes things worse.
- **User control** — can the user actually do anything about the cause? A client-side validation error (bad input) is fully in the user's control and should say what to fix; a server outage is not, and telling the user to "check your input" when the input was fine is actively misleading.
- **Technical detail appropriateness** — is this error surface read by an end user or a developer/QA/admin? `[SOURCE_BACKED — internal precedent]` this project's own benchmark control case (`control-002`) already tests that a raw status code is *correct*, not under-explained, on a developer-facing surface — "humanizing" it would remove needed information.
- **Frequency** — an error the user will hit often (e.g. "wrong password") should be terse and self-service, since users habituate to it; a rare catastrophic error can afford more explanation because the user has no learned response to fall back on.
- **Available next action** — never invent a next step that doesn't exist. `[PROJECT_DECISION, ties to core/meaning-preservation.md]` "Contact support" as a filler recovery instruction when there's no actual support channel for this error is worse than stating the bare fact — a fabricated action is a meaning problem, not just a padding problem.

## Hostile patterns to avoid (independent of how much detail is included)

`[SOURCE_BACKED]` NN/g, "Hostile Patterns in Error Messages" (directly fetched):

1. **Premature errors** — showing an error before the user has actually finished or failed (e.g. flagging an email field invalid after the first keystroke). This is a timing bug, not a wording bug, but Thai phrasing can't fix a message shown at the wrong moment — flag this as a product/implementation issue if you see it, not something a text rewrite resolves.
2. **Error-styling for non-errors** — using red/warning visual treatment for routine, non-critical information (e.g. "no attachments to show" styled as a warning). The Thai-writing-skill-relevant version of this: don't *word* a neutral empty state or routine notice as if it were a failure ("ไม่มีข้อมูล ผิดพลาด" for a plain empty state) — that's a tone-severity mismatch in the opposite direction from under-explaining a real error.

## Worked example: one underlying failure, three valid Thai outputs

The task brief gives this exact case — reproduced and extended here as the canonical illustration that "more detail" isn't automatically "better":

- **Level 1 (bare fact)**: `โหลดข้อมูลไม่สำเร็จ` — sufficient when: low severity (e.g. a non-critical widget on a dashboard that other content still works around), instantly retriable by just re-opening/refreshing, end-user audience with no specific action needed beyond the implicit "try again," and this error is common enough that spelling out "try again" every time would be over-explanation (`taxonomy:over_explanation`).
- **Level 2 (fact + recovery)**: `โหลดข้อมูลไม่สำเร็จ ลองอีกครั้ง` — appropriate when the retry action isn't obvious from context (e.g. no visible refresh control), or when the failure is important enough that leaving the user to guess the next step is a real cost, but still not severe/complex enough to warrant explaining cause.
- **Level 3 (fact + cause + specific action)**: `โหลดข้อมูลไม่สำเร็จ เพราะไม่มีสัญญาณอินเทอร์เน็ต เชื่อมต่อ Wi-Fi หรือเปิดข้อมูลมือถือแล้วลองใหม่` — appropriate when the cause is actually known (not guessed — see `core/meaning-preservation.md`'s existing `err-006` corpus case, which specifically warns against inventing a diagnosis like "unstable connection" when the app hasn't verified that), the user genuinely has a choice of concrete remedies, and the situation is important/unfamiliar enough that a bare "try again" would leave the user stuck.

`[PROJECT_DECISION]`: the choice between these levels is not a Thai-language decision at all — it's a product/severity decision that happens to determine how much Thai text is needed. The skill's job is to write whichever level is correct for the situation cleanly, not to default to the most detailed version as "more helpful," and not to default to the shortest version as "more concise" — both are context-blind defaults this file exists to rule out.

## Sources

- [NN/g — Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/) (Neusesser & Sunwall, 2023) — directly fetched
- [NN/g — Hostile Patterns in Error Messages](https://www.nngroup.com/articles/hostile-error-messages/) — directly fetched
- [UX Tigers — Error Message Usability (Heuristic 9 explainer)](https://www.uxtigers.com/post/heuristic-9-error-messages) — found via search, secondary summary of Nielsen's original heuristic, not independently fetched
- Existing sources already covering related ground (not re-fetched, see `ux-writing-research.md`/`sources.md`): Microsoft Style Guide "sorry" entry, the VisionXBrain 47-message/38%→19% Thai case study, the AIS and Krungthai NEXT real-product security-error data points (`real-product-observations.md`)
