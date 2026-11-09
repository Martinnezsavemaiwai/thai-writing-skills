```yaml
context: notifications
purpose: text delivered outside the user's current screen: push, in-app notification center, system/email alerts
audience: End User, Customer
desired_tone: matches the event's severity, not a fixed brand voice (see core/tone.md)
desired_length: very short: push notifications especially are read at a glance, often on a lock screen
must_preserve: exact trigger/cause, any time-sensitive detail (deadline, amount, expiry)
common_mistakes: over_explanation, excessive_formal_connectors, redundant_politeness_particles
```

`[Open question: no dedicated authoritative source found for toast/notification copy specifically]`: this file extrapolates from the general error/UX principles in `ux-writing.md` and the one verified real-world data point below, rather than a named style guide section.

## Severity sets the register

The clearest real evidence available (AIS's fraud-SMS security alert, directly fetched; see `../../../../research/real-product-observations.md`) shows politeness particles dropped entirely and phrasing going to short direct imperatives specifically because the message is a security warning. Routine notifications ("your order shipped") sit further toward conversational; urgent/security notifications sit toward direct-and-formal-but-brief. Neither extreme is a fixed house style, so match the event.

- Routine: `พัสดุของคุณจัดส่งแล้ว ถึงภายในวันนี้`
- Urgent/security: `พบความพยายามเข้าสู่ระบบที่ผิดปกติ เปลี่ยนรหัสผ่านทันที`

## Lead with the actionable fact

A notification is read in a glance, often out of context (locked screen, notification center). Put the one fact/action that matters first, and don't build up to it.

- Buried: `ระบบตรวจพบว่ามีการทำรายการที่อาจจะผิดปกติเกิดขึ้นกับบัญชีของคุณเมื่อสักครู่นี้`
- Direct: `พบรายการผิดปกติในบัญชีของคุณ ตรวจสอบทันที`

## Don't over-explain in a channel meant to be skimmed

Push/toast copy that restates why the notification exists ("เราส่งข้อความนี้เพื่อแจ้งให้คุณทราบว่า...") wastes the one line a user will actually read. State the fact.

## Toasts vs. push vs. in-app notification center

A toast (transient, appears while the user is already in-app) can be shorter and more casual than a push notification (arrives cold, no on-screen context) or an in-app notification-center entry (persists, may be read minutes/hours later and needs enough context to stand alone without the triggering screen still visible).
