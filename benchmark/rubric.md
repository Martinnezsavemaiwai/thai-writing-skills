# Evaluation Rubric

Seven dimensions, each scored 1-5. This supersedes the original 6-dimension sketch — Phase 11 of the research split "Audience Fit" out from "Context Fit" because a piece can match its surface (a toast is short and toast-shaped) while still missing its actual reader (too formal for an end user, too casual for an executive).

**Do not optimize for an AI-detector score.** The goal is quality, naturalness, clarity, and contextual correctness — a piece that "passes" as human-written but is unclear, wrong, or tonally mismatched is not a success.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Meaning Preservation** | Facts/conditions changed or lost | Minor imprecision, no lost condition | Every fact, number, and condition intact |
| **Naturalness** | Reads as translated/calqued | Mostly natural, one or two rough spots | A native writer would produce this |
| **Context Fit** | Wrong register/length/structure for the surface | Roughly right, some mismatch | Exactly matches what this surface (button, toast, README...) expects |
| **Audience Fit** | Tone assumes the wrong reader entirely | Close, slightly off for the actual reader | Matches exactly who reads this (see core/tone.md's audience model) |
| **Terminology Consistency** | Contradicts or ignores existing glossary/usage | Mostly consistent, one drift | Matches the project's established terms exactly |
| **Conciseness** | Padded with redundant connectors/verbs/content | Reasonably tight, minor padding | Nothing removable without losing information |
| **AI-Smell** | Multiple context-blind pattern matches (word-list thinking) | One or two, defensible edge cases | No pattern flagged without a genuine context check |

## Scoring notes

- A perfect score requires the piece to have gone through the actual pipeline (Meaning → Context → Audience → Terminology → Tone → Natural Thai → AI-Smell Review), not just landed on natural-sounding phrasing by chance.
- Terminology Consistency requires a stated project glossary to score against; without one, score N/A and note it rather than guessing an arbitrary target term.
- AI-Smell scoring should reference `../.claude/skills/thai-writer/review/thai-ai-smells.md`'s `when_it_is_valid` column for every flagged pattern — a flag without a checked "when it's fine" test is itself a rubric violation.

## What the benchmark's trap/control cases specifically stress-test

Added in the deep-research pass (`cases.yaml`'s `meaning-001`, `meaning-002`, `register-001`, `control-001`, `control-002`, `term-001`) because a rubric with only "obviously bad → obviously good" cases can't actually distinguish a skill that reasons correctly from one that pattern-matches:

- **Conciseness must never outrank Meaning Preservation.** `meaning-001`/`meaning-002` are natural-sounding, concise rewrites that silently drop a condition or a specific value. A grader (human or model) that scores these high because they read well is making exactly the mistake this rubric exists to prevent — Meaning Preservation is graded against the *set of facts/conditions*, independent of how fluent the result sounds.
- **The AI-Smell dimension must permit "no change."** `control-001`/`control-002` are cases where the correct output is the input, unchanged. A skill that always finds something to improve fails these regardless of output quality — this is the direct, gradable version of `core/anti-ai.md`'s design goal.
- **Formal register is sometimes the correct answer.** `register-001` is the benchmark's explicit negative test of the "no blacklist" principle — an answer that removes `ในกรณีที่`/`ทั้งนี้`/`ดังกล่าว` from a ToS clause and sounds more casual is *wrong* here, not an improvement.
- **Terminology Consistency requires looking across strings, not just at one.** `term-001` can't be solved by judging any single string in isolation — the defect only exists at the product level, across three surfaces.
