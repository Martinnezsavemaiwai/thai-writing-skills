```yaml
context: documentation
purpose: README, technical docs, API reference, release notes
audience: Developer, PM, Customer (release notes), Stakeholder
desired_tone: Neutral-Technical for docs; Professional for release notes (calibrate to audience; see core/tone.md)
desired_length: scannable: short paragraphs, headings, lists over dense prose
must_preserve: exact setup steps, exact parameter/field behavior, exact version/scope of a release note
common_mistakes: excessive_formal_connectors, over_explanation, register_mixing
```

`[Source-backed principle]`, Microsoft Writing Style Guide + Google developer documentation style guide (see `../../../../research/technical-writing-research.md`): lead with purpose, scannable structure over dense prose, be affirmative without stacking qualifiers that don't change the instruction.

## README / technical docs: lead with what and why, first sentence

Don't open with scene-setting before saying what the project/doc is about.

- Scene-setting: `ในปัจจุบันการพัฒนาซอฟต์แวร์มีความสำคัญมากขึ้นเรื่อยๆ โปรเจกต์นี้จึงถูกสร้างขึ้นเพื่อ...`
- Direct: state what it does and why it exists in the first sentence, then expand.

Watch for `ทั้งนี้`/`อย่างไรก็ตาม`/`ดังกล่าว` showing up as paragraph glue in what should be scannable, list-first sections (e.g. an "Installation" section); much more defensible in a long-form legal/compliance doc than here.

## API documentation: precision over personality

`[Source-backed principle]`, Google style guide: instructions should be literal and testable, not softened with hedges.

- Hedged: `คุณอาจจะต้องพิจารณาตั้งค่า API key ในไฟล์ .env`
- Direct: `ตั้งค่า API key ในไฟล์ .env`

Keep parameter/field descriptions terminology-consistent across endpoints: don't describe the same field differently in two places (see `../terminology/terminology.md`).

## Release notes: audience determines register, not a fixed "friendly changelog" default

Release notes are stakeholder/customer-facing in a way READMEs aren't. Lead with what changed and why it matters to *that* reader, but calibrate formality to the actual audience: an enterprise B2B release note reads more measured than an end-consumer app's in-app "what's new"; see `../../thai-writer/core/tone.md`. Don't apply one changelog voice to both.
