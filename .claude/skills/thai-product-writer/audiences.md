# Audiences สำหรับงานซอฟต์แวร์

## Audience model

Nine recurring audiences for software-product Thai:

| Audience | Typically reads | Formality tends toward |
|---|---|---|
| End User | UI copy, notifications, help content | Conversational–Neutral |
| Customer (B2B/enterprise) | Contracts, invoices, formal support | Professional–Formal |
| Developer | Code comments, API docs, PRs, technical READMEs | Neutral–Technical |
| QA | Bug reports, test/acceptance criteria | Neutral–Technical |
| Product Manager | Requirements, specs, internal updates | Professional |
| Designer | Design specs, UX copy review notes | Professional |
| Stakeholder (non-technical) | Status updates, business summaries | Professional |
| Executive | Executive summaries, high-level release notes | Executive (concise, outcome-first, minimal jargon) |
| Internal Team (peer-to-peer) | Slack-style messages, internal docs, commit messages | Conversational–Neutral |

**Do not assume "professional" means "formal."** A message to a PM or a peer developer is professional and can still be direct, contraction-adjacent, particle-light Thai. The failure mode this skill exists to catch is defaulting every "business" audience to maximum formality regardless of who's actually reading (`[Observed pattern]`, see `../../../research/business-writing-research.md`).

## Context × audience

Tone is chosen by **context × audience**, never by default preference:

- End user + notification + routine event: Conversational-Neutral
- End user + notification + security/urgent event: drops toward Neutral-Direct, particles optional (see the AIS example in `../thai-writer/core/anti-ai.md`)
- Developer + code comment: Technical, terse, no politeness particles at all (a comment addressed to a colleague reading code, not a customer)
- Internal team + commit/PR: Neutral-Conversational, direct, no bureaucratic throat-clearing
- Stakeholder + status update: Professional, can still be plain and direct
- Executive + summary: Executive: lead with the outcome, minimal setup
