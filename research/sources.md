# Sources

Deduplicated bibliography across all `research/*.md` files. Each entry notes which file relies on it and the confidence of the fetch itself (directly fetched vs. found via search snippet only — a search-snippet-only source is weaker evidence regardless of how authoritative the underlying site is).

## Directly fetched and cited

- [Microsoft Writing Style Guide — Welcome](https://learn.microsoft.com/en-us/style-guide/welcome/) — `technical-writing-research.md`
- [Top 10 tips for Microsoft style and voice](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice) — `technical-writing-research.md`
- [Google developer documentation style guide — Voice and tone](https://developers.google.com/style/tone) — `technical-writing-research.md`, `ux-writing-research.md`
- [Google developer documentation style guide — About this guide](https://developers.google.com/style) — `technical-writing-research.md`
- [Microsoft Learn — Writing style, Windows apps](https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style) — `ux-writing-research.md` (primary source for tone/voice/errors/dialogs/buttons)
- [Material Design (M1) — Writing style guidelines](https://m1.material.io/style/writing.html) — `ux-writing-research.md`
- [AIS — cyber threat alert: fake SMS warning](https://www.ais.th/consumers/help-and-support/cyber-threat-alerts/fake-sms1) — `ux-writing-research.md`, `real-product-observations.md` — the one directly-verified real-product data point (formality/particle-density scales with severity)
- [Thai Localization Style Guide (Microsoft, PDF)](https://download.microsoft.com/download/3/f/2/3f236167-639e-46f2-8201-554c36bcbf31/tha-tha-StyleGuide.pdf) — `thai-writing-principles.md` — located but not yet deeply mined section-by-section; follow-up needed
- [Microsoft Localization Style Guides index](https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides) — `thai-writing-principles.md`
- [Lekawatana, Pongsri — "The So-Called Passive in Thai" (ANU)](https://openresearch-repository.anu.edu.au/server/api/core/bitstreams/0c55fe14-b11d-49a5-b316-9e607a184e7b/content) — `thai-writing-principles.md` — academic source on `ถูก`/`โดน` register
- [Satthachai, Mali — thesis on Passive, Deontic Modality and Cohesive Conjunction (DCU)](https://doras.dcu.ie/23093/1/Mali%20%20Satthachai_Thesis.pdf) — `thai-writing-principles.md` — secondary, not fully reviewed
- [The Annotation Guideline of LST20 Corpus (arXiv 2008.05055)](https://arxiv.org/pdf/2008.05055) — `thai-writing-principles.md` — confirms LST20 is 15 news genres, NOT UI/product text
- [LST20 Corpus — NECTEC Data Catalog](https://opend-portal.nectec.or.th/en/dataset/lst20-corpus) — `thai-writing-principles.md`
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — `thai-writing-principles.md`, `thai-ai-smell-taxonomy.md` — English-language structural analogy only, not Thai-specific evidence
- [Software Engineering at Google, ch. 8](https://abseil.io/resources/swe-book/html/ch08.html) — `thai-ai-smell-taxonomy.md` — source for "comments explain why, not what"
- [google/eng-practices — What to look for in a code review](https://github.com/google/eng-practices/blob/master/review/reviewer/looking-for.md) — `thai-ai-smell-taxonomy.md`
- [How to Write Effective Gherkin Acceptance Criteria](https://testquality.com/how-to-write-effective-gherkin-acceptance-criteria/) — `business-writing-research.md`
- [When to Use "Given-When-Then" Acceptance Criteria](https://www.ranorex.com/blog/given-when-then-tests/) — `business-writing-research.md`
- [Acceptance Criteria: Purposes, Types, Examples and Best Practices](https://www.altexsoft.com/blog/acceptance-criteria-purposes-formats-and-best-practices/) — `business-writing-research.md`
- [LINE Thailand help center — how to change in-app language](https://help.line.me/line/smartphone/pc?lang=th&contentId=20007465) — `real-product-observations.md` — low relevance, settings menu only
- [thestandard.co — AIS-True Cell Broadcast confirmation](https://thestandard.co/ais-true-android-alerts/) — `real-product-observations.md` — confirms feature exists, not its wording
- [True iService](https://iservice.true.th/setting) — `real-product-observations.md`
- [NN/g — 3 Design Considerations for Effective Mobile-App Permission Requests](https://www.nngroup.com/articles/permission-requests/) — `ux-writing-research.md`
- [NN/g — Confirmation Dialogs Can Prevent User Errors](https://www.nngroup.com/articles/confirmation-dialog/) — `ux-writing-research.md`
- [pdpa.pro — เคลียร์ชัดเรื่อง consent ตาม PDPA](https://pdpa.pro/blogs/pdpa-consent) — `ux-writing-research.md` — Thai-specific, legally-grounded plain-language requirement for consent/permission text
- [Lumen Learning — "Audience," Communication for Professionals](https://courses.lumenlearning.com/suny-esc-communicationforprofessionals/chapter/audience/) — `business-writing-research.md`
- [Fleximize — communication styles by audience](https://fleximize.com/articles/000592/communication-styles) — `business-writing-research.md`

## Found via search snippet only (not independently fetched — treat as weaker evidence)

- [Microsoft Style Guide — "sorry" entry](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/s/sorry) — `ux-writing-research.md`
- ["UX Writing" (Tang Thaneesa)](https://medium.com/@tangthaneesa/ux-writing-1240e9e6572b) / [mirror](https://tangthaneesa.wordpress.com/2019/11/02/ux-writing/comment-page-1/) — `ux-writing-research.md` — direct fetch returned HTTP 403
- ["Error Message คืออะไร? 5 หลักเขียนให้ลูกค้าไม่หนีเว็บ"](https://visionxbrain.com/blog/error-message-best-practices) — `ux-writing-research.md` — single secondary case study, treat the 38%→19% figure as illustrative only
- [scb.co.th SCB Easy pages](https://www.scb.co.th/th/personal-banking/digital-banking/scb-easy/get-start.html) — `real-product-observations.md`
- [Bangkok Bank FAQ](https://www.bangkokbank.com/th-TH/Personal/Digital-Banking/Bualuang-mBanking/FAQ) — `real-product-observations.md` — direct fetch timed out
- [Shopee TH — Apple App Store Thai-locale listing](https://apps.apple.com/th/app/shopee-th-...) — `real-product-observations.md` — title string seen in search result only
- [Microsoft Language Portal — Grokipedia summary](https://grokipedia.com/page/microsoft_language_portal) — `terminology-research.md`
- [Microsoft Terminology Collection: What It Is And Uses — Language Unlimited](https://www.languagesunlimited.com/microsoft-terminology-collection/) — `terminology-research.md`
- [Terminology management at Microsoft — Microsoft Learn archive](https://learn.microsoft.com/en-us/archive/blogs/terminology/terminology-management-at-microsoft) — `terminology-research.md`
- [Manage terminology — Globalization, Microsoft Learn](https://learn.microsoft.com/en-us/globalization/localization/managing-terminology) — `terminology-research.md` — directly fetched, current page
- [ISO 704:2022 — Terminology work, Principles and methods](https://www.iso.org/standard/79077.html) — `terminology-research.md` — catalog/abstract page fetched; the standard's full text is paywalled and was not read
- [ISO 12620:2009 — Management of terminology resources, Data category specifications](https://www.iso.org/standard/37243.html) — `terminology-research.md` — same caveat as above
- [TermBase eXchange (TBX) — Wikipedia](https://en.wikipedia.org/wiki/TermBase_eXchange), [ISO 30042:2019](https://www.iso.org/standard/45797.html), [tbxinfo.net — About TBX](https://www.tbxinfo.net/tbx-about/) — `terminology-research.md`
- [MQM Council — Multidimensional Quality Metrics framework](https://www.themqm.org/) and [MQM History](https://themqm.org/mqm-history/) — `native-speaker-validation.md`
- [10 Usability Heuristics for User Interface Design — NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/) — `native-speaker-validation.md` — directly fetched
- [NN/g — Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/) (Neusesser & Sunwall, 2023) — `error-writing-research.md` — directly fetched
- [NN/g — Hostile Patterns in Error Messages](https://www.nngroup.com/articles/hostile-error-messages/) — `error-writing-research.md` — directly fetched
- Krungthai NEXT security error message, via [modify.in.th](https://www.modify.in.th/35277) (quotes the exact real Thai error string) and [krungthai.com official announcement](https://krungthai.com/th/krungthai-update/announcement-detail/2821) — `real-product-observations.md` — second directly-verified real Thai security-error data point after AIS

## Found via search snippet only (not independently fetched — treat as weaker evidence)

(continued from above — deep-research pass additions)

- Iwasaki, Shoichi & Preeya Ingkaphirom, *A Reference Grammar of Thai* (Cambridge University Press, 2005/2009, ISBN 9780521108676) — `thai-ai-smell-taxonomy.md` — confirmed via publisher catalog metadata, a Google Books listing, and two ResearchGate review abstracts; direct fetch of the Cambridge page itself returned HTTP 403, so no primary-text content was read, only catalog/review-level confirmation the book covers Thai classifiers
- Sudmuk, Cholthicha, "The *thuuk* Construction in Thai" (Stanford CSLI, LFG proceedings) — `thai-ai-smell-taxonomy.md` — existence and publication venue verified; the PDF could not be parsed in this pass, so it corroborates this is a studied academic topic without adding quotable detail
- Robert C. Martin, *Clean Code*, ch.4 "Comments" — `technical-writing-research.md` — via [LinkedIn summary](https://www.linkedin.com/pulse/summary-clean-code-chapter-4-comments-robert-c-martin-ilias-el-mhamdi), [GitHub notes](https://github.com/azizkayumov/clean-code/blob/main/comments.md), [gist summary](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29) — not read from primary book text, treat as secondary-source triangulation only
- John Ousterhout, *A Philosophy of Software Design* — `technical-writing-research.md` — via search snippets and [johnousterhout/aposd-vs-clean-code](https://github.com/johnousterhout/aposd-vs-clean-code) (a first-party comparison written by Ousterhout himself, stronger than a random summary, but still not the primary book text)
- [Ciklopea — The Benefits of Terminology Management in Translation and Localization Projects](https://ciklopea.com/blog/translation/the-benefits-of-terminology-management-in-translation-and-localization-projects/) — `terminology-research.md` — source for the termbase-vs-style-guide distinction, cross-checked against similar articles from Andovar, Adhoc Translations, and GTE Localize stating the same distinction consistently

## Directly fetched and cited (Evidence Hardening pass)

- Diller, A.V.N., *High and Low Thai: Views from Within* (Pacific Linguistics, 1985) — `thai-writing-principles.md` — directly fetched (PDF); primary academic source for the register model (Thai diglossia, high/low Thai, written-vs-spoken register mapping, code-switching)

## Found via search snippet only (Evidence Hardening pass additions)

- Popular sociolinguistic register-inventory accounts (Street/Elegant/Formal/Rhetorical/Religious-Royal Thai, including the specific claim that ดำเนินการ belongs to Formal-register vocabulary) — `thai-writing-principles.md` — search-snippet level only; the underlying page (learnfluentthai.com) did not confirm this breakdown on direct fetch, so treat this specific 5-way naming as weaker evidence than Diller's academic diglossia framework, corroborating in spirit but not independently verified
- General English writing-craft guidance on strong vs. weak verbs (ProWritingAid "Weak words series," K5 Learning "Strong Verbs Versus Weak Verbs") — `thai-ai-smell-taxonomy.md` (`weak-verbs` entry) — general craft-writing sources, not academic; the Thai-specific application (ทำ/มี/เกิดขึ้น as the generic filler verbs) is this project's own extension, tagged PROJECT_DECISION accordingly

## Punctuation and formatting (`punctuation-formatting-research.md`)

- [trueplookpanya: หลักเกณฑ์การใช้เครื่องหมายวรรคตอน การเว้นวรรค ฉบับราชบัณฑิตยสถาน (คัดลอก)](https://www.trueplookpanya.com/knowledge/content/50093-lantha-lan-) — a reproduction of the Royal Institute book (7th printing, 2551, pp. 56-66), not the book itself
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — §2.1, §3.3, §3.5, §5.1, §6, Style, §13.5 and the caveats section; descriptive, not prescriptive
- [Plagiarism Today: Em dashes, hyphens and spotting AI writing](https://plagiarismtoday.com/2025/06/26/em-dashes-hyphens-and-spotting-ai-writing/) — humans use em dashes too, frequency is the signal
- [Rolling Stone: ChatGPT, the em dash and AI writing](https://www.rollingstone.com/culture/culture-features/chatgpt-hypen-em-dash-ai-writing-1235314945/) — same point, journalistic coverage
- [assertion-evidence.com (Michael Alley)](https://www.assertion-evidence.com/) — advocacy site for assertion-evidence slides; the homepage cites no studies or numeric limits, research papers page not read
- [Unicode UAX #14: Line Breaking Algorithm](https://www.unicode.org/reports/tr14/) — Thai line breaking needs word analysis, left to higher-level processing
- [Adobe Community: Line breaks in Thai (FrameMaker)](https://community.adobe.com/t5/framemaker-discussions/line-breaks-in-thai/m-p/3517439) — forum practice: dictionary-based breaking, zero-width space as a manual workaround

## Attempted but blocked/unavailable

- [Material Design 3 — Content design overview](https://m3.material.io/foundations/content-design/overview) — JS-rendered, fetch returned no body text. UX findings lean on the older M1 page instead. Revisit with a renderer that executes JS.
- MQM error-types page (`themqm.org/error-types-2/`) — HTTP 403; the error-dimension list in `native-speaker-validation.md` is cross-checked across multiple independent secondary summaries instead of read from the primary page — revisit before treating the exact dimension list as final.
- [Apple Human Interface Guidelines — Writing](https://developer.apple.com/design/human-interface-guidelines/foundations/writing) — `real-product-observations.md` — JS-rendered, same failure mode as Material Design 3; a fetch attempt returned only the page title and the fetching model then generated plausible-sounding "typical Apple guidelines" content instead of admitting failure — that generated content was discarded and NOT used as a source. Only a WebSearch-snippet-level summary (plain language, localization affects layout) is noted, explicitly flagged as unverified.
- DGA (Digital Government Development Agency) UX-writing or content-design guide — searched specifically this pass, not found. DGA's public materials found are about service consolidation/infrastructure (Tang Rat app), not content standards.
- Royal Institute punctuation and spacing book, full text via the Mahidol PDF (`si.mahidol.ac.th/.../373_18_1.pdf`): text could not be extracted, so only the trueplookpanya reproduction was read (`punctuation-formatting-research.md`). Revisit with the printed book.

## Not source-backed (no citable reference found)

- Thai classifier (ลักษณนาม) grammar — **upgraded this pass**, see Iwasaki & Ingkaphirom entry above. No longer belongs in this section; kept here as a changelog note rather than deleted outright.
- No Thai-language analogue to the English "plain language movement" was found (`business-writing-research.md`) — this project's plain-language stance for Thai remains a `[PROJECT DECISION]` by analogy, not backed by an equivalent Thai institutional reform effort. Worth a follow-up search (e.g. ก.พ., สำนักงานพัฒนารัฐบาลดิจิทัล) specifically for digital-government plain-language guidance.
