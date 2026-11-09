# Real Thai Software Product Observations

Scope: Phase 3 — study how real Thai-market software products write Thai copy, without copying their text. Per instructions, this pass could not access live app UI directly; it relied on public web pages (help centers, security-alert pages, app-store listings) that these companies publish, and on search-engine summaries where direct fetch failed. Every entry below states its actual source and confidence. No verbatim strings are reproduced beyond single short labels (e.g. a button word) needed to identify a term choice.

## LINE

**Source:** [LINE Thailand help center — how to change in-app language](https://help.line.me/line/smartphone/pc?lang=th&contentId=20007465). **Confidence:** low — this is a help article about a settings menu, not representative product copy (errors, confirmations, etc.). **No verifiable public source found** for LINE's error/confirmation/notification copy in this pass. Open question for a later pass: LINE Thailand's official blog or design-team posts, if any exist publicly.

## Grab

**Source:** Google Play / App Store listing pages exist (`play.google.com/store/apps/details?id=com.grabtaxi.passenger`, Apple App Store Grab listing) but the search pass surfaced only the English-locale description text, not the Thai-locale listing copy. **No verifiable Thai-language public source found** in this pass — would require fetching the Play Store page with an `hl=th&gl=th` locale parameter directly, which wasn't attempted here. Flag as open question for a follow-up pass rather than guessing at Grab's Thai copy style.

## SCB / SCB Easy

**Source:** [scb.co.th SCB Easy pages](https://www.scb.co.th/th/personal-banking/digital-banking/scb-easy/get-start.html) and [Bangkok Bank FAQ](https://www.bangkokbank.com/th-TH/Personal/Digital-Banking/Bualuang-mBanking/FAQ) exist as real public Thai pages, but direct fetch of the Bangkok Bank FAQ timed out in this pass, and the SCB pages were not individually fetched — only surfaced via search snippets. **Confidence: low.** One search-engine synthesis (not a direct page read) reported that Thai banks, including Bangkok Bank and SCB, commonly use the transliterated loanword "ล็อกอิน" (login) rather than the translated "เข้าสู่ระบบ" for the sign-in action. This is plausible and consistent with general observation that Thai fintech UI keeps common English tech verbs as loanwords, but it is **not independently confirmed by a direct page read in this pass** — treat as an open question until verified by directly fetching a bank's login screen copy or app-store listing.

## K PLUS (Kasikornbank)

**No verifiable public source found** in this pass beyond general news/comparison articles (e.g. Techsauce's K PLUS vs SCB Easy comparison) that describe features, not copy style. Open question for a follow-up pass.

## AIS

**Source:** [AIS cyber-threat alert — fake SMS warning](https://www.ais.th/consumers/help-and-support/cyber-threat-alerts/fake-sms1) — fetched directly. **Confidence: medium-high** (real, current public page). Observed pattern: short declarative sentences (roughly 5–12 words), no politeness particles (ค่ะ/ครับ/กรุณา) despite being a customer-facing message, register described as "moderately formal yet urgent" — sits between conversational and official rather than either extreme, and instructions are direct imperatives rather than softened suggestions. This is a genuine data point that formality and directness scale with message severity, not a fixed "always formal" or "always casual" house style.

## True

**Source:** [True iService](https://iservice.true.th/setting) exists as a real customer portal, and a mainstream news article ([thestandard.co — AIS-True Cell Broadcast confirmation](https://thestandard.co/ais-true-android-alerts/)) confirms True (with AIS) rolled out a government-linked Cell Broadcast emergency-alert system supporting Thai among 5 languages. **No verifiable sample of True's actual UI/notification Thai copy found** in this pass — the news article covers the feature's existence, not its wording. Open question for a follow-up pass.

## Shopee (TH)

**Source:** [Shopee TH — Apple App Store Thai-locale listing](https://apps.apple.com/th/app/shopee-th-...) — the Thai-locale App Store title itself is visible in the search result: **"Shopee TH: ซื้อของออนไลน์ส่งไว"** ("Shopee TH: shop online, fast delivery"). **Confidence: medium** (the title string appeared directly in a search result page, not independently re-fetched from the store page). Observed pattern: the Thai app title is a short verb-phrase fragment (ซื้อของออนไลน์ส่งไว — "buy things online, ships fast") rather than a full grammatical sentence, prioritizing scannable keywords over sentence structure — consistent with app-store title conventions generally, not specific to Shopee.

## Lazada (TH)

**No verifiable public source found** in this pass — search results did not surface a Thai-locale Lazada listing or help article distinct from generic product pages. Open question for a follow-up pass.

## Google (Thai locale)

**Not directly investigated in this pass** — Google's own UX-writing *guidelines* were researched (see `ux-writing-research.md`), but Google's Thai-locale product copy itself (e.g. Android system strings, Google One Thai copy) was not fetched. Open question for a follow-up pass; Google publishes its own products' localized strings and these would be a strong evidence source if pulled directly (e.g. via Android AOSP translation files, which are public).

## Microsoft (Thai locale)

**Not directly investigated in this pass** for live product copy. Microsoft's own *style guide for Thai* was located (see `sources.md`) but not fetched in full (PDF, not attempted in this pass) — this is a stronger and more directly relevant source than trying to reverse-engineer live product copy, and should be prioritized in a follow-up pass over inspecting Windows' Thai UI directly.

## Cross-product synthesis

- **Loanword vs. translation for the same action varies by domain and needs per-term verification, not a blanket rule.** The one data point gathered (Thai banks reportedly favoring "ล็อกอิน" over "เข้าสู่ระบบ") is low-confidence on its own. **[Project decision, provisional]**: the skill's terminology guidance should never assume "always keep English loanwords" or "always translate" — it should ask the project's existing glossary/codebase first (see `terminology/terminology.md`), and only fall back to "what do comparable Thai products call this" as a tiebreaker, and only when that comparison is actually verified rather than assumed.
- **Formality and politeness-particle density scale with message severity/urgency, not with a single fixed brand register.** The AIS security-warning observation is the one directly-verified data point for this — a customer-facing message dropped all politeness particles under urgency. This directly supports `core/anti-ai.md`'s stance that particle frequency must be judged by context, not counted as an absolute defect or requirement.
- **App-store titles/short descriptions favor fragment phrasing over full sentences** — the one verified Shopee data point is consistent with the general (non-Thai-specific) convention that app-store metadata is keyword-forward, not prose. This is a weak, single-example signal — do not generalize far beyond "titles can be fragments" without more evidence.
- **Overall confidence for this phase is low-to-medium.** Most major Thai consumer apps' actual in-product microcopy was not accessible through public web search in this pass (it lives inside authenticated apps, not indexed pages). The strongest, most reusable finding is the AIS security-alert register data point and the general principle it supports; the rest should be treated as open questions for a follow-up pass that has live-app access or an install of these apps for direct observation (with no text copied verbatim, only patterns noted, per the original instruction).

## Permissions, destructive actions, onboarding (follow-up pass)

**Permissions:** No verifiable Thai-language in-app permission-rationale string was found for any named product. What *was* found: Thai consumer-tech sources (NSTDA's public safety guidance, Sanook's tech section) discuss "apps requesting more permissions than needed" as a recognized problem Thai users are advised to check for — real and Thai-specific, but describes user *behavior/awareness*, not product copy. **Confidence: low** for wording, **medium** for "Thai users are primed to notice over-broad permission asks" as a general claim.

**Destructive actions:** No verifiable Thai-language destructive-action confirmation string (e.g. a real "delete account" dialog) was found for any named product in this pass. Search results returned only generic OS-level permission-management help articles (Google/Apple support pages localized to Thai), which are Google/Apple's own support documentation, not a third-party app's confirmation-dialog copy. **No verifiable public source found.**

**Onboarding:** Not directly investigated with dedicated searches in this pass beyond what the earlier pass already covered (none). **No verifiable public source found.**

**Why this category is harder than error messages/security alerts:** the earlier pass's one strong data point (AIS's security alert) worked because that content is a public help-center page, not in-app-only text. Permission dialogs, destructive-action confirmations, and onboarding screens are almost never published outside the live app itself, so this category structurally resists the same web-research approach that worked for public-facing help/support pages. A future pass with actual device/app access (installing the apps and screenshotting, with no verbatim text reproduced beyond a short label) would be needed to close this gap — not a deeper search pass.

## New products/components (evidence-hardening pass)

```yaml
product: Krungthai NEXT (Krungthai Bank)
context: security/fraud-prevention error
component: full-screen blocking error (transaction denial)
audience: End User
observed_pattern: >
  Real, verified Thai string: "ไม่สามารถทำรายการได้ เนื่องจากพบการติดตั้งแอปพลิเคชั่นที่อาจ
  เสี่ยงต่อการทำธุรกรรมของคุณ" ("Unable to complete this transaction because an app that may
  risk your transactions was found installed"). States what happened (transaction blocked)
  and why (a risky app), then instructs the user to disable Accessibility services or
  remove non-store apps. No politeness particles; direct declarative register.
possible_reason: >
  Consistent with the earlier-verified AIS security-alert finding: severity/security
  context pushes toward direct, particle-free, cause-stated phrasing over softened UI
  copy — this is now a SECOND independent Thai banking/telecom data point for that
  pattern, not just one.
strength: strong-pattern
source: "https://www.modify.in.th/35277 (tech-news article quoting the app's actual error text); corroborated by https://krungthai.com/th/krungthai-update/announcement-detail/2821 (official Krungthai announcement referencing the same security requirement)"
notes: >
  This is the second directly-verified real Thai security/fraud-prevention error message
  found across all research passes (after AIS). Two independent banking/telecom sources
  converging on the same register pattern raises this from a single anecdote toward a
  genuine cross-product pattern — still short of "strong" in the sense of a systematic
  survey, but no longer a lone data point.
```

```yaml
product: "Thai government digital services (general — DGA, ทางรัฐ/Tang Rat)"
context: plain-language / content-design guidance
component: n/a — searching for institutional guidance, not app copy
audience: n/a
observed_pattern: "No DGA-published UX-writing or plain-language content guide was found."
possible_reason: >
  DGA's public materials found in this pass are about service consolidation (150+
  government services in one app) and infrastructure, not content/writing standards.
strength: possible-antipattern
source: "Multiple DGA/Tang Rat pages found (dga.or.th, opengovernment.go.th) — none address content writing style"
notes: >
  A separate, real Thai search surfaced official-letter-writing guidance
  (เทคนิคการเขียนหนังสือราชการ, opsmoac.go.th) whose snippet explicitly values
  "การใช้ถ้อยคำที่กระชับ ชัดเจน เข้าใจง่ายเมื่ออ่าน" (concise, clear, easy-to-understand
  wording) — but this is guidance for FORMAL government correspondence, not a plain-
  language reform movement that reduces formality. `[OBSERVED]`: this is a genuinely
  different thing from the English-language "plain language movement" the previous pass
  looked for — Thai official-writing training already prizes concision *within* the
  formal register, rather than a movement to write government text in a less formal
  register for citizen readability. This refines, but does not close, the open question
  in `business-writing-research.md` about a Thai plain-language analogue — it's evidence
  that "concise" and "formal" are not opposed in existing Thai institutional writing
  training, which is directly useful for `core/tone.md`'s tone-spectrum model.
```

```yaml
product: "SCB EASY, Apple Thai-locale HIG, general UX case studies"
context: various (banking app UX, platform localization guidance)
component: various
audience: n/a
observed_pattern: "No new verifiable finding."
possible_reason: n/a
strength: interesting-example
source: "Searches attempted; see notes"
notes: >
  SCB EASY: search surfaced only generic banking-UX case-study articles (not about SCB
  EASY specifically) — no verifiable finding, consistent with the prior pass's SCB
  low-confidence status. Apple HIG: the general (non-locale-specific) Writing page for
  Apple's Human Interface Guidelines exists (developer.apple.com/design/human-interface-
  guidelines/foundations/writing) but is JS-rendered — direct fetch returned only the
  page title, matching the earlier Material Design 3 fetch-blocked pattern. A search-
  snippet-level summary suggests it recommends simple/plain language and notes
  localization affects text length/layout, but nothing Thai-specific was found, and the
  snippet-level summary should not be treated as a verified quote. `[OPEN QUESTION]`:
  revisit both JS-rendered pages (Apple HIG, Material Design 3) with a renderer that
  executes JavaScript before treating their content as sourced.
```

## Explicit open questions carried forward

1. Grab, Lazada, K PLUS, True, LINE (beyond a settings help page), Google Thai locale, Microsoft Thai locale product copy — no verified public sample found in this pass.
2. The "ล็อกอิน vs เข้าสู่ระบบ" banking-sector claim needs direct verification against an actual bank app screen or app-store listing, not a search-engine synthesis.
3. Whether any of these companies publish a public Thai content-style guide or design-team writeup — not found in this pass, worth a dedicated search.
4. Permission-request, destructive-action-confirmation, and onboarding copy from any named real Thai product — not found in this pass either; likely needs live-app access rather than web search (see note above).
5. Grab, Lazada, K PLUS, True, LINE, Google/Microsoft/Apple Thai-locale copy remain unverified even after this pass's fresh angles (government services, Apple HIG, SCB EASY) — the two verified real-error-message data points (AIS, Krungthai NEXT) are both security/fraud contexts specifically, which may itself be a *reason* they're findable: security warnings are more likely to be publicly documented (news articles, official alerts) than routine UI copy. Don't generalize the "drop formality under severity" finding beyond security contexts without more evidence of ordinary UI copy.
