```yaml
context: ux-writing
purpose: in-screen UI text the user reads while using the product
audience: End User, Customer
desired_tone: Conversational-Neutral by default; shifts with severity/urgency (see core/tone.md)
desired_length: short: a button is 1-3 words, most other strings 1-2 short sentences
must_preserve: exact conditions (when a button enables/disables), exact error causes, exact limits/units
common_mistakes: unnecessary_subject_insertion, excessive_formal_connectors, redundant_politeness_particles, over_explanation
```

Covers buttons, labels, forms, validation messages, error messages, toasts, empty states, confirmation dialogs, onboarding. (Async/out-of-flow notifications, meaning push, email, and system alerts, are `notifications.md`; the line is: does the user see this while looking at the screen, or does it arrive separately?)

## Buttons and labels

Name the actual action, active voice, readable at a glance. Refer to the on-screen label itself when giving instructions ("กด **ยืนยัน**", not "กดปุ่มยืนยัน"). Use the same verb for the same action everywhere, and don't let "ลบ"/"เอาออก"/"นำออก" all mean delete on different screens (see `../terminology/terminology.md`).

## Validation messages

Say what's wrong **and** what fixes it. "ข้อมูลไม่ถูกต้อง" alone fails this; "รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร" doesn't.

## Error messages

Don't blame the user. State what happened and, where possible, what to do next. Apologize only for things the product itself is responsible for, not for a third-party/network failure the product didn't cause (`[Source-backed principle]`, Microsoft Style Guide "sorry" entry; see `../../../../research/ux-writing-research.md`).

- User-blaming: `คุณกรอกข้อมูลผิด`
- Neutral + actionable: `อีเมลนี้ไม่ถูกต้อง ลองตรวจสอบอีกครั้ง`

For security/fraud-severity errors, formality and particle use can drop toward short direct imperatives; see `../../thai-writer/core/anti-ai.md`'s AIS example. This is a deliberate register shift, not a defect.

**How much detail an error needs is not a fixed template.** `[Source-backed, deepened this pass]`: NN/g's error-message guidance and Hostile Patterns research (see `../../../../research/error-writing-research.md`). Decide the level from severity, recoverability, whether the user can actually control the cause, whether this audience is technical, how often the user will hit this specific error, and whether a real next action actually exists (never invent one). The same underlying failure can correctly be any of three levels:

- Level 1 (bare fact): `โหลดข้อมูลไม่สำเร็จ`: fine for low-severity, instantly-retriable, high-frequency situations where "try again" is obvious
- Level 2 (fact + retry): `โหลดข้อมูลไม่สำเร็จ ลองอีกครั้ง`: when the retry action isn't visually obvious
- Level 3 (fact + known cause + specific action): `โหลดข้อมูลไม่สำเร็จ เพราะไม่มีสัญญาณอินเทอร์เน็ต เชื่อมต่อ Wi-Fi หรือเปิดข้อมูลมือถือแล้วลองใหม่`: only when the cause is actually known (not guessed) and the user has a real, specific remedy

Neither "always terse" nor "always maximally helpful" is correct, since both are context-blind defaults. Don't style a routine, non-critical notice (an empty state, a low-stakes heads-up) with error-level visual/verbal severity either, since that's the same mismatch in the other direction.

## Confirmation dialogs

Title and buttons must form a clear question-and-answer pair: buttons should read as direct answers to the title, and the same action's button wording should stay consistent across the app (`[Source-backed principle]`, Microsoft Windows apps writing style). Keep body text as short as the decision actually requires; a dialog interrupts the user's task.

- Weak pairing: title "ยืนยันการลบ" with buttons "ตกลง" / "ยกเลิก" (doesn't say what's being confirmed)
- Clear pairing: title "ลบรายการนี้ใช่ไหม" with buttons "ลบ" / "ไม่ลบ"

## Empty states

`[Open question: no dedicated source found]`: say what's missing and, where relevant, what fills it, and don't apologize at length for the absence of data.

## Onboarding

The one place where some restating of the obvious is intentional pedagogy, not the `over_explanation` smell, because a first-time user genuinely doesn't have the context yet. Still keep steps short and one-action-per-screen; "helpful" and "wordy" aren't the same thing.

## Forms

`[Open question: no Thai-specific source found]`: apply the error-message principle by extension: a field-level validation error should name the specific problem, not a generic "invalid."
