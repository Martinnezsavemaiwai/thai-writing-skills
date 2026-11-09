# Review Checklist

Run through this before delivering any rewrite. Order matters; it follows the pipeline in SKILL.md.

1. **Meaning**: every fact, number, condition, and named entity from the source is still present and unchanged in substance? (`../core/meaning-preservation.md`)
2. **Context**: did I confirm where this text lives before rewriting it, and open the matching context file in `../contexts/` (general writing) or `../../thai-product-writer/contexts/` (software)?
3. **Audience**: do I know who reads this, and does the tone match `../core/tone.md`'s audience×context model rather than a default guess?
4. **Terminology** (software text only, thai-product-writer): does every product-specific term match the project's existing glossary/shipped copy? If no glossary exists, did I flag that instead of inventing one silently? (`../../thai-product-writer/terminology/terminology.md`)
5. **Natural Thai**: any translated-sounding structure left? Check subject insertion, `ถูก`-passive, "not just X but Y" calques, Title Case English bleed, classifiers. (`../core/natural-thai.md`)
6. **Clarity**: would a first-time reader understand this without re-reading? Is the actionable part findable, not buried? (`../core/clarity.md`)
7. **Conciseness**: any padding left (`ทำการ...`, redundant connectors, restated-the-obvious content) that isn't earning its place at this register? (`../core/conciseness.md`)
8. **Punctuation**: no `—` or `→` (or `->`, `=>`) in the prose, outside code and quoted text? (`../core/punctuation.md`)
9. **Formatting fits the channel**: Markdown only where it will render; no `**`, `#`, or bullets in LINE, SMS, or plain-text email? (`../core/formatting.md`)
10. **AI-smell, context-checked**: for every pattern in `thai-ai-smells.md` that seems to apply, did I check it against register/frequency/redundancy/audience before flagging it, or did I match a word in isolation? (`../core/anti-ai.md`)
11. **No chatbot framing**: no opener like `แน่นอน!` or `คำถามที่ดีมาก`, and no closer like `หวังว่าจะเป็นประโยชน์` or a summary that repeats the reply? (`../core/conciseness.md`)
12. **NO_CHANGE**: If the source already passes every item above, say no change is needed instead of rewriting.

## Before sending the response

- Did I separate what changed for **meaning reasons** vs. **context/audience fit** vs. **AI-smell**, per SKILL.md's response format?
- If the user asked for a quick fix with no explanation, did I skip the summary and just send the text?
- If anything in the source was ambiguous, did I ask instead of guessing?
