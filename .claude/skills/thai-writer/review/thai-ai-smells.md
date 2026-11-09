# Thai AI-Smells: Applied Reference

Practical, in-task version of the taxonomy. Full sourcing, confidence ratings, and the raw YAML schema for the original 20 patterns live in `../../../../research/thai-ai-smell-taxonomy.md`. The punctuation and formatting patterns (em dash, arrows, bold labels, chatbot openers and closers) have their own research file, `../../../../research/punctuation-formatting-research.md`. Read those files for "how much should I trust this." This file is for "does this apply right now."

**Rule zero, always:** every pattern below has a `When it's fine` column. If you can't articulate why *this instance* fails that test, you don't have a finding, you have a word you recognized. See `../core/anti-ai.md`.

| Pattern | Looks like | When it's fine | Fix |
|---|---|---|---|
| Redundant verb (`ทำการ...`) | `ทำการบันทึกข้อมูล` | Formal institutional announcements | `บันทึกข้อมูล` |
| Unnecessary nominalization | `มีการดำเนินการตรวจสอบ` (turning a verb into an abstract noun) | Formal reports describing a process itself as the topic, not the action's result | `ตรวจสอบ` |
| Generic introductory phrases | `ในปัจจุบัน...`, `เป็นที่ทราบกันดีว่า...` before the actual point | Genuine scene-setting a reader needs before a complex topic (rare in software product text) | Cut it, lead with the point |
| Passive calque (`ถูก...`) | `ถูกออกแบบมาเพื่อ...` | Agent genuinely unknown/irrelevant; legal/technical convention | Active voice with a real subject |
| "Not just X but Y" calque / negative parallelism | `ไม่ใช่แค่...แต่ยัง...`, `ไม่ใช่ X แต่เป็น Y`, `Y มากกว่า X` | Correcting a misunderstanding the reader actually holds: `ไม่ได้ยกเลิก แค่เลื่อน` (see `../core/natural-thai.md`) | State both facts plainly, or say what actually happens |
| Excessive formal connectors | `ทั้งนี้`, `อย่างไรก็ตาม`, `กล่าวคือ` in a toast/button | Formal docs, legal/B2B, requirements, long-form docs with real logical work | a space, `แต่`, or nothing |
| Bureaucratic reference words | `ดังกล่าว`, `ในกรณีที่` in casual UI | Requirements/legal text needing precise back-reference or explicit conditionals | `นี้`/`นั้น`, `ถ้า` |
| Redundant politeness particles | ค่ะ/ครับ on every single sentence | Established intentional brand voice; very short pieces | Particle at natural rhythm points only |
| Weak verbs | `มีการเปลี่ยนแปลง`, `ทำให้เกิดข้อผิดพลาด` (a generic verb where a specific one exists) | Genuinely no more specific verb applies | `เปลี่ยน`, name the actual error |
| Unnecessary abstraction | Describing a concrete thing/action abstractly when a concrete term exists | The abstraction is genuinely the point (a design doc discussing a category of actions, not one instance) | Name the concrete thing |
| Fake conversational tone | Forcing casual particles (`จ้า`, `เลยนะ`) onto content that should stay neutral (e.g. a legal disclaimer) | Genuine end-user conversational surfaces where casual tone is the correct register | Match register to content type, not a blanket "sound friendly" instinct |
| Unnecessary summary repetition | A paragraph immediately followed by "สรุปแล้วคือ..." restating the same point, or a chat reply ending in `โดยสรุปแล้ว...` that repeats the paragraph just above | Genuine executive summary at the top of a long document, clearly separated from the body | Cut the restated conclusion |
| Classifier errors | `เสื้อยืด 3 ชิ้น` | No general exception, since this is a correctness check, not style | Match the noun's actual classifier |
| Title Case English bleed | `Premium Quality Serum ของคุณ` | Actual proper nouns / literal feature names in the UI | Normal Thai sentence, no Title Case |
| Register mixing | Formal opener, casual closer, same piece | Structurally justified shift (clearly separated disclaimer block vs. tip) | Pick one register, hold it |
| Listicle emoji spam | Every line: emoji + bold header + colon + no new content | Plain spec lists without emoji/repeated headers are NOT this | State the facts, drop the decoration |
| Over-explanation | Restating a consequence the reader already inferred | Onboarding/tutorial content for genuine first-timers | Cut the restated sentence |
| Unnecessary subject insertion | `ระบบจะทำการบันทึก...` where subject is recoverable | Subject is genuinely ambiguous or needs contrast/emphasis | Drop the subject |
| Inconsistent terminology | "รายการสั่งซื้อ" here, "คำสั่งซื้อ" there, same concept | Genuinely different concepts that happen to look similar (verify against glossary first) | Pick the glossary term, use it everywhere |
| Unnatural technical terminology | An invented literal-translation Thai coinage for a term real Thai developers/users always keep in English (or vice versa: an over-literal English calque no real product uses) | No general exception; check what real product copy/codebases actually call this before coining anything | Match established usage; if genuinely unsettled, keep the English term with a short Thai gloss |
| Em dash in Thai prose | `—` anywhere in Thai prose (banned by default even once; several in a paragraph is the strongest signal) | Code, quoted source text, proper names, or the user asked for it | Rewrite with a space, `คือ`, `เพราะ`, or a new sentence (`../core/punctuation.md`) |
| Symbols standing in for connectors | `A → B`, `A = B` inside a sentence | Code, quoted source text, proper names, a real diagram or flow, or the user asked for it | Write the connecting word (`แล้ว`, `จากนั้น`, `ทำให้`) or use a numbered list |
| Comma swapped in for em dash | `ผลสำรวจชัดเจน, ลูกค้าอยากได้ส่งฟรี` (the `—` became `,` but the sentence is still two English-style halves) | Commas inside numbers (`12,500`) or between English terms in a list | Rebuild the sentence: `ผลสำรวจบอกชัดว่าลูกค้าอยากได้ส่งฟรี`. Swapping one mark for another is not a fix |
| Bold label + colon on every line | `**ข้อดี:** ... **ข้อเสีย:** ...` | Reference material readers scan by label, such as a spec sheet | Write it as a paragraph with real connectors (`../core/formatting.md`) |
| Rule of three | `รวดเร็ว ง่ายดาย และมีประสิทธิภาพ` with nothing behind the three words | Each of the three is backed by its own content | One measurable fact: `สมัครเสร็จใน 2 นาที` |
| Inflated significance | `ถือเป็นหมุดหมายสำคัญ`, `สะท้อนให้เห็นถึง`, `ตอกย้ำ` | The text shows why it matters (a first, a record, a number) | State what happened and let the reader weigh it |
| Chatbot closer | `หวังว่าจะเป็นประโยชน์`, `หากมีคำถามเพิ่มเติมสามารถสอบถามได้เลย` | Customer service where follow-up is real, and then name the channel: `สอบถามเพิ่มได้ที่ LINE @xxx` | Cut it (`../core/conciseness.md`) |
| Order-taking opener | `แน่นอน!`, `คำถามที่ดีมาก` | When it is itself the answer (`แน่นอนครับ` to a yes/no question) or a chat acknowledgement of a request (`ได้ครับ เดี๋ยวส่งให้`) | Cut it and open with the answer |

## The five words that must never become a blacklist entry

`ดำเนินการ`, `อย่างไรก็ตาม`, `ดังกล่าว`, `ในกรณีที่`, `ทั้งนี้` each appear in the table above (as `ทำการ`'s relative, or directly) with a real "when it's fine" column. If you're about to flag one of these five without checking register/audience/frequency first, stop and re-read `../core/anti-ai.md`.

## Confidence, condensed

28 patterns above. The original 20 are each tagged with a `category` and an `evidence_type` (`SOURCE_BACKED`/`OBSERVED`/`PROJECT_DECISION`/`HYPOTHESIS`) in `../../../../research/thai-ai-smell-taxonomy.md`. Most are well-attested structural classes applied to a clear Thai mechanism, or backed by an academic Thai reference grammar for classifiers; a handful are medium-confidence (plausible, not yet corpus-checked). **`Superlative inflation` was removed in an earlier pass** because it was an ad-copy holdover with no place in a software-product taxonomy; it survives only as a historical note in the research file.

The 8 rows from "Em dash in Thai prose" to "Order-taking opener" carry two tags, except "Symbols standing in for connectors", which is `PROJECT_DECISION`. For the other 7 the English pattern is `SOURCE_BACKED` (Wikipedia: Signs of AI writing). The Thai mapping is `HYPOTHESIS`: the examples are written by hand and not yet checked against a Thai corpus. Two more patterns from the same source (negative parallelism, a closing summary that repeats) were folded into the existing "Not just X but Y" and "Unnecessary summary repetition" rows instead of getting rows of their own. Sourcing is in `../../../../research/punctuation-formatting-research.md`.

None of the 28 have been checked against a native-speaker review panel. A methodology for doing that exists (`../../../../research/native-speaker-validation.md`, including 7 specific Thai-language reviewer questions), but it hasn't been run. See `../../../../research/README.md`'s open questions for the full status.
