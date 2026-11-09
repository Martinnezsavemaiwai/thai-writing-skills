# Product Thai Corpus

**Status: model-generated, not yet human-validated.** Per `native-speaker-validation.md`, nothing in this file has gone through the review methodology designed there — zero reviewers, zero scores. `human_validated: false` on every single entry, no exceptions. Treat every entry as a draft hypothesis about what better Thai looks like in context, not a verified example. This file is distinct from `benchmark/cases.yaml`: the benchmark grades whether a rewrite passes/fails specific dimensions; this corpus is a teaching/reference set of realistic input→output pairs with reasoning, meant to illustrate the principles in `../.claude/skills/thai-product-writer/` at volume.

150 cases (Evidence Hardening pass — expanded from 100, schema hardened). Distribution:

```text
30 UX/UI microcopy
25 Error/Validation/Recovery
20 Notification/Toast/Confirmation
25 Engineering
20 Product/Business
20 Documentation
10 English-to-Thai Adaptation
```

Schema (every case, no exceptions):

```yaml
id:
category:               # one of the 7 names above, exactly
context:                 # matches a contexts/*.md file
audience:

input:
better_output:            # literal "(no change — already correct)" for control cases; "(delete the comment)" for removed code comments

problem:                   # 1-2 sentences: what's wrong, or why nothing needs fixing
principles:                # pointers into core/*.md or contexts/*.md
failure_modes:              # list of taxonomy `id` values (see thai-ai-smell-taxonomy.md); [] for control cases

meaning_constraints:         # facts/conditions that must survive unchanged; [] if none
terminology_constraints:      # terms that must stay glossary-consistent; [] if none

confidence: low|medium|high     # how confident THIS case's reasoning is
evidence_type: SOURCE_BACKED|OBSERVED|PROJECT_DECISION|HYPOTHESIS
source:                          # taxonomy entry, research file section, or "internal" for a plain worked example

human_validated: false
```

## UX/UI microcopy (30)

```yaml
- id: uxui-001
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "กรุณากดปุ่มด้านล่างเพื่อดำเนินการต่อไปยังขั้นตอนถัดไป"
  better_output: "ถัดไป"
  problem: A button doesn't need a full sentence describing itself — the label IS the instruction.
  principles: [core/conciseness.md, contexts/ux-writing.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#redundant-verb-construction
  human_validated: false

- id: uxui-002
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "บันทึกการเปลี่ยนแปลง"
  better_output: "บันทึก"
  problem: Thai buttons don't need the object restated when it's the only thing on screen that could be saved.
  principles: [core/clarity.md, contexts/ux-writing.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-003
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ท่านต้องการที่จะลบรายการนี้ออกจากระบบใช่หรือไม่"
  better_output: "ลบรายการนี้ใช่ไหม"
  problem: "ท่าน" and "ออกจากระบบ" over-formalize a routine confirmation beyond what end-user UX register calls for.
  principles: [core/tone.md, contexts/ux-writing.md]
  failure_modes: [unnecessary-subject-insertion]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-subject-insertion
  human_validated: false

- id: uxui-004
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ใส่ที่อยู่อีเมลของคุณในช่องด้านล่าง"
  better_output: "อีเมล"
  problem: A form field label doesn't need an instruction sentence — the field itself and its placement communicate what goes in it.
  principles: [core/clarity.md, core/conciseness.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-005
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ฟีเจอร์นี้ยังไม่พร้อมใช้งานในขณะนี้ ทางทีมงานกำลังดำเนินการพัฒนาอย่างเต็มที่ ขออภัยในความไม่สะดวก"
  better_output: "ฟีเจอร์นี้กำลังพัฒนาอยู่ เร็วๆ นี้"
  problem: Three sentences of apology and process description compress into one that says exactly what the user needs.
  principles: [core/conciseness.md]
  failure_modes: [over-explanation, generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#over-explanation
  human_validated: false

- id: uxui-006
  category: "UX/UI microcopy"
  context: ux-writing
  audience: Customer
  input: "แอปพลิเคชันมีความจำเป็นต้องเข้าถึงตำแหน่งที่ตั้งของท่านเพื่อวัตถุประสงค์ในการให้บริการที่ดียิ่งขึ้น"
  better_output: "ใช้ตำแหน่งของคุณเพื่อหาร้านใกล้คุณ"
  problem: Permission rationale should state the concrete payoff, not a formal justification clause.
  principles: [contexts/ux-writing.md#permissions]
  failure_modes: [generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: ux-writing-research.md#permissions (NN/g Skyscanner rationale finding)
  human_validated: false

- id: uxui-007
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "คุณแน่ใจหรือไม่ว่าต้องการดำเนินการต่อ"
  better_output: "ลบบัญชีนี้ถาวร ข้อมูลทั้งหมดจะหายไปและกู้คืนไม่ได้"
  problem: A destructive-action confirmation must name the actual consequence — a generic "are you sure" protects no one.
  principles: [contexts/ux-writing.md#destructive-actions, core/clarity.md]
  failure_modes: []
  meaning_constraints: ["the action is irreversible", "all data is lost"]
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: ux-writing-research.md#destructive-actions (NN/g "state the outcome" finding)
  human_validated: false

- id: uxui-008
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ขออภัย ขณะนี้ยังไม่มีข้อมูลการแจ้งเตือนใดๆ ปรากฏอยู่ในระบบของท่าน"
  better_output: "ยังไม่มีการแจ้งเตือน"
  problem: An empty state doesn't need an apology for having nothing to show.
  principles: [contexts/ux-writing.md]
  failure_modes: [over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#over-explanation
  human_validated: false

- id: uxui-009
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "เปิดใช้งานการแจ้งเตือน"
  better_output: "รับการแจ้งเตือน"
  problem: A settings toggle label reads more natural describing the resulting state than a verb-first "activate" framing.
  principles: [core/natural-thai.md, terminology/terminology.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: ["การแจ้งเตือน"]
  confidence: low
  evidence_type: HYPOTHESIS
  source: internal
  human_validated: false

- id: uxui-010
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ไม่พบผลลัพธ์การค้นหาที่ตรงกับคำค้นหาของท่านในขณะนี้ กรุณาลองค้นหาด้วยคำอื่น"
  better_output: "ไม่พบผลลัพธ์ ลองค้นหาคำอื่น"
  problem: A search-empty-state is read mid-task; cut it to the fact and the one useful next step.
  principles: [core/conciseness.md]
  failure_modes: [excessive-formal-connectors]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-011
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ยินดีต้อนรับสู่แอปพลิเคชัน ในหน้าจอนี้เราจะแนะนำท่านเกี่ยวกับฟีเจอร์หลักต่างๆ ที่มีอยู่ในแอปพลิเคชันของเรา"
  better_output: "มาดูฟีเจอร์หลักกัน"
  problem: A welcome screen that announces it's about to explain things wastes the one screen a first-time user actually reads.
  principles: [contexts/ux-writing.md#onboarding, core/conciseness.md]
  failure_modes: [generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-012
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "รูปภาพที่ท่านเลือกมีขนาดไฟล์ใหญ่เกินกว่าที่ระบบกำหนดไว้ กรุณาเลือกไฟล์ภาพอื่นที่มีขนาดเล็กกว่านี้"
  better_output: "ไฟล์ใหญ่เกินไป เลือกไฟล์ที่เล็กกว่า 5MB"
  problem: Naming the actual limit is more actionable than "smaller than this" — the real number must come from the product, not be invented.
  principles: [core/meaning-preservation.md, core/clarity.md]
  failure_modes: []
  meaning_constraints: ["the actual size limit, once known, must be stated exactly"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-013
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ตัวกรอง"
  better_output: "(no change — already correct)"
  problem: Standard, natural Thai software terminology for a filter control — nothing to fix.
  principles: [core/anti-ai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: internal
  human_validated: false

- id: uxui-014
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "กำลังโหลดข้อมูล กรุณารอสักครู่ ระบบกำลังดำเนินการประมวลผลคำขอของท่าน"
  better_output: "กำลังโหลด..."
  problem: A loading state shown for seconds doesn't need "the system is processing your request" padding.
  principles: [core/conciseness.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#redundant-verb-construction
  human_validated: false

- id: uxui-015
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "โปรดยืนยันตัวตนของท่านอีกครั้งเพื่อความปลอดภัยของบัญชีของท่าน"
  better_output: "ยืนยันตัวตนอีกครั้งเพื่อความปลอดภัย"
  problem: Dropping the doubled "ของท่าน" tightens the sentence without losing the stated reason.
  principles: [core/conciseness.md]
  failure_modes: [unnecessary-subject-insertion]
  meaning_constraints: ["the reason (security) must remain stated"]
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-subject-insertion
  human_validated: false

- id: uxui-016
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "เพิ่มลงในรายการโปรดของคุณเรียบร้อยแล้ว"
  better_output: "เพิ่มในรายการโปรดแล้ว"
  problem: A toast confirming a quick action doesn't need "ของคุณ" — whose list it is is already obvious.
  principles: [contexts/notifications.md]
  failure_modes: [unnecessary-subject-insertion]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-subject-insertion
  human_validated: false

- id: uxui-017
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "เลือกวิธีการชำระเงินที่ท่านต้องการใช้ในการทำธุรกรรมนี้"
  better_output: "เลือกวิธีชำระเงิน"
  problem: A screen heading above a list of payment options doesn't need a full sentence — the list makes the meaning obvious.
  principles: [core/clarity.md]
  failure_modes: [generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-018
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "หมดเวลาการใช้งาน กรุณาเข้าสู่ระบบใหม่อีกครั้งเพื่อดำเนินการต่อ"
  better_output: "เซสชันหมดอายุ เข้าสู่ระบบอีกครั้ง"
  problem: "เพื่อดำเนินการต่อ" is implied by the whole screen being a login prompt — restating it is redundant content, not just wordy phrasing.
  principles: [core/conciseness.md]
  failure_modes: [over-explanation, redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#over-explanation
  human_validated: false

- id: uxui-019
  category: "UX/UI microcopy"
  context: ux-writing
  audience: Designer
  input: "ป้ายกำกับปุ่มควรใช้คำกริยาที่ชัดเจนและสอดคล้องกับการกระทำที่เกิดขึ้นจริงเมื่อผู้ใช้กดปุ่มดังกล่าว"
  better_output: "ป้ายกำกับปุ่มต้องเป็นคำกริยาตรงกับสิ่งที่เกิดขึ้นจริง"
  problem: Design-system documentation for a Designer audience is rightly Neutral-Technical, but "ดังกล่าว" still pads a one-clause rule that doesn't need a formal back-reference.
  principles: [core/tone.md]
  failure_modes: [bureaucratic-reference-words]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#bureaucratic-reference-words
  human_validated: false

- id: uxui-020
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "เปิด"
  better_output: "(no change — already correct)"
  problem: A two-character toggle label needs no rewriting — recognizing there's nothing to fix is the correct output.
  principles: [core/anti-ai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: internal
  human_validated: false

- id: uxui-021
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "กำลังเตรียมข้อมูลของคุณ อาจใช้เวลาสักครู่เนื่องจากมีข้อมูลจำนวนมากที่ต้องดำเนินการประมวลผล"
  better_output: "กำลังเตรียมข้อมูล..."
  problem: A first-load skeleton-screen state doesn't need to justify why it's slow — this is a different loading moment than uxui-014's action-loading and stays this brief regardless.
  principles: [core/conciseness.md]
  failure_modes: [redundant-verb-construction, over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-022
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "การชำระเงินของคุณเสร็จสมบูรณ์เรียบร้อยแล้วอย่างสมบูรณ์แบบ ขอบคุณที่ใช้บริการของเรา"
  better_output: "ชำระเงินสำเร็จ"
  problem: Stacking three success-markers ("เสร็จสมบูรณ์...เรียบร้อยแล้ว...อย่างสมบูรณ์แบบ") on a routine, non-doubtful success state is the "successfully completed" over-translation pattern.
  principles: [core/conciseness.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: translation-adaptation.md#successfully-completed-saved
  human_validated: false

- id: uxui-023
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "รหัสนี้ใช้สำหรับยืนยันตัวตนของคุณเมื่อเข้าสู่ระบบจากอุปกรณ์ใหม่ที่ไม่เคยใช้งานมาก่อน เพื่อความปลอดภัยของบัญชีคุณ"
  better_output: "รหัสนี้ใช้ยืนยันตัวตนเมื่อเข้าสู่ระบบจากอุปกรณ์ใหม่"
  problem: Inline help text under a 2FA field doesn't need "for your account's security" — that's the implied point of every 2FA field, not new information.
  principles: [core/conciseness.md]
  failure_modes: [over-explanation]
  meaning_constraints: ["what the code is for (device verification) must remain"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-024
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "การตั้งค่านี้จะช่วยให้ท่านสามารถควบคุมปริมาณการใช้งานข้อมูลอินเทอร์เน็ตของท่านได้อย่างมีประสิทธิภาพมากยิ่งขึ้น"
  better_output: "จำกัดการใช้อินเทอร์เน็ตอัตโนมัติ"
  problem: A settings-screen description for a data-saver toggle should say what it does, not praise how effectively it'll help.
  principles: [core/clarity.md, core/conciseness.md]
  failure_modes: [unnecessary-abstraction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-abstraction
  human_validated: false

- id: uxui-025
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "เปลี่ยนอีเมล"
  better_output: "(no change — already correct)"
  problem: An account-management menu entry naming the exact action needs no rewriting.
  principles: [core/anti-ai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: internal
  human_validated: false

- id: uxui-026
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ต้องการเปลี่ยนอีเมลใช่ไหม เราจะส่งลิงก์ยืนยันไปที่อีเมลใหม่ของคุณ"
  better_output: "(no change — already correct)"
  problem: A two-sentence account-change confirmation that states the action and the exact next step is already at the right length and register for this surface — a control case against over-trimming useful process information.
  principles: [core/clarity.md, core/conciseness.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: uxui-027
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "บัญชีของคุณเชื่อมต่อกับ Google แล้ว"
  better_output: "(no change — already correct)"
  problem: A linked-account status line in a settings screen is already plain and correct; keeping "Google" untranslated as a proper noun is correct, not a Title Case bleed.
  principles: [core/natural-thai.md, terminology/terminology.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: internal
  human_validated: false

- id: uxui-028
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "ลบบัญชีผู้ใช้"
  better_output: "ลบบัญชี"
  problem: The menu entry that LEADS TO a destructive-action confirmation (distinct from the confirmation dialog itself) should match this product's chosen glossary term for the concept exactly — flagged here as a terminology-consistency check against whatever the confirmation dialog itself says, not a naturalness issue.
  principles: [terminology/terminology.md]
  failure_modes: [inconsistent-terminology]
  meaning_constraints: []
  terminology_constraints: ["must match the term used in the destructive-action confirmation dialog that follows"]
  confidence: low
  evidence_type: HYPOTHESIS
  source: internal
  human_validated: false

- id: uxui-029
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "แจ้งเตือนแบบ Push"
  better_output: "การแจ้งเตือน"
  problem: A settings-screen category label doesn't need the English technical qualifier "Push" when the screen only offers one kind of notification setting — keep the English qualifier only when the product genuinely distinguishes push vs. email vs. SMS notifications as separate toggles.
  principles: [terminology/terminology.md, core/clarity.md]
  failure_modes: [unnatural-technical-terminology]
  meaning_constraints: []
  terminology_constraints: ["การแจ้งเตือน"]
  confidence: low
  evidence_type: HYPOTHESIS
  source: thai-ai-smell-taxonomy.md#unnatural-technical-terminology
  human_validated: false

- id: uxui-030
  category: "UX/UI microcopy"
  context: ux-writing
  audience: End User
  input: "คุณสามารถเปลี่ยนภาษาได้ในหน้าตั้งค่า หรือจะเปลี่ยนตอนนี้เลยก็ได้"
  better_output: "(no change — already correct)"
  problem: "คุณสามารถ...ได้" is appropriate here because the sentence genuinely expresses optionality (change now or later) — this is the carve-out translation-adaptation.md notes for when the capability-framing is correct, not a calque to fix.
  principles: [core/natural-thai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: translation-adaptation.md#you-can
  human_validated: false
```

## Error/Validation/Recovery (25)

```yaml
- id: err-001
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "ข้อมูลที่ท่านกรอกไม่ถูกต้อง กรุณาตรวจสอบและกรอกใหม่อีกครั้ง"
  better_output: "รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร"
  problem: The generic version is true of any validation failure; the fix requires naming the specific rule actually violated.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: ["the actual validation rule, once known, must be stated exactly"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-002
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "ระบบไม่สามารถทำการบันทึกข้อมูลของท่านได้เนื่องจากเกิดข้อผิดพลาดขึ้น"
  better_output: "บันทึกไม่สำเร็จ ลองอีกครั้ง"
  problem: "เนื่องจากเกิดข้อผิดพลาดขึ้น" restates that there's an error without adding information.
  principles: [core/conciseness.md]
  failure_modes: [redundant-verb-construction, generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#redundant-verb-construction
  human_validated: false

- id: err-003
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "อีเมลหรือรหัสผ่านไม่ถูกต้อง"
  better_output: "(no change — already correct)"
  problem: Deliberately vague on purpose — a login error should NOT reveal which of the two fields was wrong. Meaning-preservation includes preserving intentional ambiguity.
  principles: [core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["must not disclose which specific field was incorrect"]
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-004
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "การเชื่อมต่ออินเทอร์เน็ตของท่านไม่เสถียร กรุณาตรวจสอบการเชื่อมต่อและลองใหม่อีกครั้งในภายหลัง"
  better_output: "ไม่มีอินเทอร์เน็ต ลองใหม่อีกครั้ง"
  problem: Asserting the exact cause ("unstable connection") the app hasn't actually verified is itself a meaning risk, not just wordiness.
  principles: [core/meaning-preservation.md, core/conciseness.md]
  failure_modes: []
  meaning_constraints: ["do not assert a specific diagnosis the app hasn't verified"]
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-005
  category: "Error/Validation/Recovery"
  context: notifications
  audience: Customer
  input: "การชำระเงินของท่านไม่สำเร็จ เนื่องจากข้อมูลบัตรเครดิตที่ท่านกรอกไม่ถูกต้องหรือบัตรของท่านถูกปฏิเสธโดยธนาคารผู้ออกบัตร กรุณาตรวจสอบข้อมูลหรือติดต่อธนาคารของท่าน"
  better_output: "ชำระเงินไม่สำเร็จ บัตรถูกปฏิเสธ ตรวจสอบข้อมูลบัตรหรือติดต่อธนาคาร"
  problem: Keeps both possible causes (bad info vs. bank decline) since dropping either is a meaning change, while cutting "ท่าน" repeated four times.
  principles: [core/meaning-preservation.md]
  failure_modes: [unnecessary-subject-insertion]
  meaning_constraints: ["both possible causes (invalid card info OR bank decline) must remain"]
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-006
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "ไฟล์ที่ท่านพยายามอัปโหลดไม่ได้รับการสนับสนุนจากระบบในขณะนี้"
  better_output: "ไม่รองรับไฟล์นี้ ใช้ไฟล์ JPG หรือ PNG"
  problem: "Not supported" alone isn't actionable; naming the accepted formats turns a dead-end into a next step, once those formats are actually confirmed.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: ["the accepted format list must be the product's real list, not invented"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-007
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "กรุณากรอกหมายเลขโทรศัพท์ให้ถูกต้องตามรูปแบบที่ระบบกำหนด"
  better_output: "เบอร์โทรต้องมี 10 หลัก เริ่มด้วย 0"
  problem: "In the format the system requires" doesn't tell the user what the format actually is.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: ["the actual format rule must be stated"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-008
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: Developer
  input: "เกิดข้อผิดพลาด: 500"
  better_output: "(no change — already correct)"
  problem: A raw status code is the correct level of detail for a developer-facing error surface (e.g. an internal admin panel) — "humanizing" it into vaguer end-user copy would remove needed information.
  principles: [core/tone.md, core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["the exact status code must remain visible"]
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#technical-detail-appropriateness
  human_validated: false

- id: err-009
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "จำนวนเงินที่ท่านระบุเกินกว่าวงเงินคงเหลือในบัญชีของท่าน"
  better_output: "ยอดเงินไม่พอ"
  problem: The plain fact suffices; whether to also show the actual remaining balance is a product decision, not a writing one.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-010
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "รหัส OTP ไม่ถูกต้องหรือหมดอายุแล้ว กรุณาขอรหัสใหม่อีกครั้ง"
  better_output: "รหัส OTP ไม่ถูกต้องหรือหมดอายุ ขอรหัสใหม่"
  problem: "แล้ว" and "อีกครั้ง" are filler that don't change the instruction; the OR condition stays intact after trimming.
  principles: [core/conciseness.md]
  failure_modes: []
  meaning_constraints: ["the OR condition (invalid OR expired) must remain"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-011
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "เกิดข้อผิดพลาดที่ไม่คาดคิด กรุณาลองใหม่อีกครั้งในภายหลัง หากปัญหายังคงเกิดขึ้นกรุณาติดต่อฝ่ายสนับสนุน"
  better_output: "เกิดข้อผิดพลาด ลองใหม่อีกครั้ง หรือติดต่อฝ่ายสนับสนุนถ้ายังไม่ได้"
  problem: Same two pieces of information (retry, then escalate) in about half the words, keeping the escalation path intact.
  principles: [core/conciseness.md]
  failure_modes: []
  meaning_constraints: ["the escalation path (retry, then contact support) must remain"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-012
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: QA
  input: "เมื่อผู้ใช้กรอกอีเมลผิดรูปแบบ ระบบควรที่จะทำการแสดงข้อความแจ้งเตือนความผิดพลาดให้ผู้ใช้ทราบในทันที"
  better_output: "เมื่อกรอกอีเมลผิดรูปแบบ ระบบต้องแสดงข้อความ error ทันที"
  problem: "ทำการแสดง" pads a QA test-case description even though the surrounding register is rightly more formal than end-user UI copy.
  principles: [core/tone.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#redundant-verb-construction
  human_validated: false

- id: err-013
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "กรุณากรอกข้อมูลในช่องนี้"
  better_output: "(no change — already correct)"
  problem: A required-field message this short and direct is already correctly calibrated for a routine client-side validation error — a control case against reflexively rewording something already minimal.
  principles: [core/clarity.md, core/conciseness.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: err-014
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: [Product Manager, Developer]
  input: "ช่องกรอกอีเมลแสดงข้อความ error ทันทีที่ผู้ใช้พิมพ์ตัวอักษรแรก ก่อนที่จะพิมพ์อีเมลเสร็จด้วยซ้ำ"
  better_output: "(no change — already correct; this is a PRODUCT/TIMING bug, not a wording problem)"
  problem: This describes a premature-error pattern (validating before the user has finished typing) — flagging when the error appears is an implementation/UX-timing issue; no Thai rewording of the eventual error text fixes a message that fires at the wrong moment.
  principles: []
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#hostile-patterns (NN/g "Hostile Patterns in Error Messages" — premature errors)
  human_validated: false

- id: err-015
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "ไม่มีไฟล์แนบ ผิดพลาด"
  better_output: "ไม่มีไฟล์แนบ"
  problem: Styling a neutral, expected empty state ("no attachments") with error-severity language is the hostile pattern in the opposite direction from under-explaining a real error — a routine absence-of-data notice isn't a failure.
  principles: [core/tone.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#hostile-patterns (NN/g — error-styling for non-errors)
  human_validated: false

- id: err-016
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "โหลดข้อมูลไม่สำเร็จ"
  better_output: "(no change — correct for this severity level)"
  problem: "Level 1" of the same underlying failure — sufficient for a non-critical dashboard widget where other content still works, retrying just means reopening/refreshing, and this error is common enough that spelling out 'try again' every time would be over-explanation.
  principles: [error-writing-research.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#worked-example
  human_validated: false

- id: err-017
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "โหลดข้อมูลไม่สำเร็จ"
  better_output: "โหลดข้อมูลไม่สำเร็จ ลองอีกครั้ง"
  problem: "Level 2" of the SAME underlying failure as err-016 — this time appropriate because there's no visible refresh control on this screen, so the retry action isn't obvious from context and needs to be named.
  principles: [error-writing-research.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#worked-example
  human_validated: false

- id: err-018
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "โหลดข้อมูลไม่สำเร็จ"
  better_output: "โหลดข้อมูลไม่สำเร็จ เพราะไม่มีสัญญาณอินเทอร์เน็ต เชื่อมต่อ Wi-Fi หรือเปิดข้อมูลมือถือแล้วลองใหม่"
  problem: "Level 3" of the SAME underlying failure — appropriate only because the cause is genuinely known (not guessed) and the user has a real choice of concrete remedies for an important/unfamiliar situation.
  principles: [error-writing-research.md, core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["the cause named must be a confirmed, not guessed, diagnosis"]
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#worked-example
  human_validated: false

- id: err-019
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: Customer
  input: "ไม่สามารถเพิ่มสินค้าชิ้นนี้ลงตะกร้าได้"
  better_output: "(no change — correct for this severity level)"
  problem: "Level 1" for a low-stakes checkout hiccup (an optional add-on item fails to add) — the user can simply try again or pick another item; no further detail is warranted for something this recoverable and low-consequence.
  principles: [error-writing-research.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: low
  evidence_type: HYPOTHESIS
  source: error-writing-research.md#axes
  human_validated: false

- id: err-020
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: Customer
  input: "ไม่สามารถเพิ่มสินค้าชิ้นนี้ลงตะกร้าได้"
  better_output: "สินค้าหมดสต๊อกระหว่างที่คุณเลือกซื้อ เอาออกจากตะกร้าแล้วเลือกสินค้าอื่นแทน"
  problem: "Level 3" for the SAME shape of failure but now at the main checkout item (higher stakes: this could be why the whole order fails) and the cause is actually known (stock ran out) — this is the higher-severity, higher-recoverability-cost version where more detail earns its place.
  principles: [error-writing-research.md, core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["the specific cause (out of stock) must be accurate, not assumed"]
  terminology_constraints: []
  confidence: low
  evidence_type: HYPOTHESIS
  source: error-writing-research.md#axes
  human_validated: false

- id: err-021
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "การซิงค์ข้อมูลล้มเหลว"
  better_output: "(no change — correct for a silent background process)"
  problem: A background auto-sync failure that the app will silently retry doesn't need recovery instructions the user can't act on anyway — user control is low here, so more detail would be misleading, not helpful.
  principles: [error-writing-research.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: low
  evidence_type: HYPOTHESIS
  source: error-writing-research.md#axes
  human_validated: false

- id: err-022
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "การซิงค์ข้อมูลล้มเหลวซ้ำหลายครั้งติดต่อกัน กรุณาลองออกจากระบบแล้วเข้าใหม่ หากยังไม่หายให้ติดต่อฝ่ายสนับสนุน"
  better_output: "(no change — correct once retries have genuinely been exhausted)"
  problem: The same underlying sync failure as err-021, escalated to full detail — appropriate ONLY once the silent auto-retry has genuinely failed repeatedly, since at that point user control (re-login) and support escalation become real, available next actions.
  principles: [error-writing-research.md, core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["do not offer 'contact support' as a next action if no such channel actually exists for this error"]
  terminology_constraints: []
  confidence: low
  evidence_type: HYPOTHESIS
  source: error-writing-research.md#axes
  human_validated: false

- id: err-023
  category: "Error/Validation/Recovery"
  context: requirements
  audience: [Developer, QA]
  input: "ระบบต้องแสดง error message ที่เข้าใจง่ายเมื่อเกิดปัญหา"
  better_output: "ระบบต้องแสดง error message ที่ระบุสาเหตุและวิธีแก้ไข เมื่อ user สามารถแก้ไขปัญหาได้เอง (เช่น รูปแบบอีเมลผิด); แสดงแค่ข้อความสั้นเมื่อเป็นปัญหาฝั่งเซิร์ฟเวอร์ที่ user ทำอะไรไม่ได้"
  problem: "Easy to understand" isn't a testable acceptance criterion; the actual requirement is that detail level should track user control, which is itself testable per case.
  principles: [contexts/requirements.md, error-writing-research.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#axes
  human_validated: false

- id: err-024
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "รหัสผ่านไม่ถูกต้อง"
  better_output: "(no change — correct for a high-frequency, self-service error)"
  problem: "Wrong password" is an error users will hit often and already understand fully — staying terse and self-service is correct per the frequency axis; adding explanation here would be over-explanation, not helpfulness.
  principles: [error-writing-research.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#axes
  human_validated: false

- id: err-025
  category: "Error/Validation/Recovery"
  context: ux-writing
  audience: End User
  input: "เกิดข้อผิดพลาดร้ายแรงในการประมวลผลคำขอชำระเงินของท่าน โปรดติดต่อฝ่ายสนับสนุนพร้อมแจ้งรหัสอ้างอิง ERR-4471 เพื่อรับความช่วยเหลือโดยเร็วที่สุด"
  better_output: "ชำระเงินไม่สำเร็จ (ERR-4471) ติดต่อฝ่ายสนับสนุนพร้อมแจ้งรหัสนี้"
  problem: A rare, high-severity payment failure with no available self-service fix earns the full detail level (reference code, explicit escalation) — trimming this to a bare fact would remove a next action the user genuinely needs, since this isn't a habituated, easily-retried error.
  principles: [error-writing-research.md, core/conciseness.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: ["the exact reference code ERR-4471 must be preserved"]
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#axes
  human_validated: false
```

## Notification/Toast/Confirmation (20)

```yaml
- id: notif-001
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "เราตรวจพบว่าอาจมีความพยายามในการเข้าถึงบัญชีของคุณโดยไม่ได้รับอนุญาตค่ะ กรุณาดำเนินการเปลี่ยนรหัสผ่านของคุณโดยเร็วที่สุดนะคะ"
  better_output: "พบความพยายามเข้าสู่ระบบที่ผิดปกติ เปลี่ยนรหัสผ่านทันที"
  problem: Security alerts drop politeness particles and go direct — a deliberate severity-driven register shift, not a defect.
  principles: [core/anti-ai.md, core/tone.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: ["urgency and the instruction (change password) must remain"]
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: real-product-observations.md#ais (AIS fraud-SMS alert)
  human_validated: false

- id: notif-002
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "เราส่งข้อความนี้เพื่อแจ้งให้คุณทราบว่าพัสดุของคุณได้ถูกจัดส่งออกจากคลังสินค้าเรียบร้อยแล้วในวันนี้"
  better_output: "พัสดุของคุณจัดส่งแล้ว ถึงภายในวันนี้"
  problem: Meta-explaining why the notification exists wastes the one line a push notification gets read for.
  principles: [contexts/notifications.md]
  failure_modes: [over-explanation]
  meaning_constraints: ["shipped today"]
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#over-explanation
  human_validated: false

- id: notif-003
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "ยินดีด้วย! คุณได้รับสิทธิ์พิเศษแล้ว! กดที่นี่เพื่อดูรายละเอียดเพิ่มเติมเกี่ยวกับสิทธิ์พิเศษของคุณ!"
  better_output: "คุณได้รับส่วนลด 20% กดดูรายละเอียด"
  problem: "Special privilege" with three exclamation points says nothing concrete; name the actual benefit once known.
  principles: [core/clarity.md]
  failure_modes: [generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: notif-004
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "บัญชีของคุณจะถูกระงับการใช้งานชั่วคราวหากไม่มีการยืนยันตัวตนภายในระยะเวลาที่กำหนด"
  better_output: "ยืนยันตัวตนภายใน 7 วัน ไม่งั้นบัญชีจะถูกระงับชั่วคราว"
  problem: "Within the specified timeframe" must be replaced by the actual number of days — a vague deadline is a meaning loss if a real one exists.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: ["the actual deadline, once known, must be stated exactly"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: notif-005
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "แจ้งเตือน: มีการเข้าสู่ระบบจากอุปกรณ์ใหม่ หากไม่ใช่คุณ กรุณาดำเนินการเปลี่ยนรหัสผ่านโดยด่วนที่สุด"
  better_output: "มีการเข้าสู่ระบบจากอุปกรณ์ใหม่ ถ้าไม่ใช่คุณ เปลี่ยนรหัสผ่านทันที"
  problem: Keeps the urgency and the conditional exactly as given, drops "ดำเนินการ" padding and "โดยด่วนที่สุด" for the shorter, equally urgent "ทันที."
  principles: [core/conciseness.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: ["the conditional (if it wasn't you) must remain"]
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#redundant-verb-construction
  human_validated: false

- id: notif-006
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: Customer
  input: "ขอขอบพระคุณที่ท่านให้ความไว้วางใจใช้บริการของเรามาโดยตลอด ทางเราขอแจ้งให้ทราบว่าระบบจะปิดปรับปรุงชั่วคราวในวันที่ 15 มีนาคม เวลา 02:00-04:00 น."
  better_output: "ระบบปิดปรับปรุง 15 มี.ค. เวลา 02:00-04:00 น."
  problem: A time-critical maintenance-window notice needs the fact and time window; the gratitude preamble belongs elsewhere, not in a time-sensitive alert.
  principles: [contexts/notifications.md]
  failure_modes: [generic-introductory-phrases]
  meaning_constraints: ["exact date and time window"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: notif-007
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "ท่านมีข้อความใหม่ 3 ข้อความที่ยังไม่ได้อ่านในกล่องข้อความของท่าน"
  better_output: "มีข้อความใหม่ 3 ข้อความ"
  problem: "That you haven't read, in your inbox" is implied by a new-message notification appearing at all.
  principles: [core/conciseness.md]
  failure_modes: [over-explanation, unnecessary-subject-insertion]
  meaning_constraints: ["the count (3) must remain exact"]
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#over-explanation
  human_validated: false

- id: notif-008
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "คูปองส่วนลดของท่านกำลังจะหมดอายุในอีก 24 ชั่วโมงข้างหน้า อย่าลืมใช้สิทธิ์ก่อนหมดเขตนะคะ"
  better_output: "คูปองหมดอายุใน 24 ชั่วโมง"
  problem: "Don't forget to use it before the deadline" restates the implication of "expiring in 24 hours" the reader already draws themselves.
  principles: [core/conciseness.md]
  failure_modes: [over-explanation]
  meaning_constraints: ["24-hour deadline"]
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#over-explanation
  human_validated: false

- id: notif-009
  category: "Notification/Toast/Confirmation"
  context: ux-writing
  audience: End User
  input: "ต้องการลบวิธีการชำระเงินนี้ใช่ไหม"
  better_output: "ลบบัตรที่ลงท้าย 4471 ใช่ไหม"
  problem: A destructive-action confirmation dialog should name the specific item being deleted, not a generic category ("this payment method") — the user has likely saved more than one.
  principles: [contexts/ux-writing.md#destructive-actions]
  failure_modes: []
  meaning_constraints: ["must identify the specific payment method, not a generic reference"]
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: ux-writing-research.md#destructive-actions
  human_validated: false

- id: notif-010
  category: "Notification/Toast/Confirmation"
  context: ux-writing
  audience: End User
  input: "ยกเลิกการสมัครสมาชิกใช่หรือไม่ ท่านจะไม่ได้รับสิทธิประโยชน์ต่างๆ อีกต่อไป"
  better_output: "ยกเลิกสมาชิกใช่ไหม สิทธิประโยชน์ทั้งหมดจะหมดทันที ไม่มีการคืนเงินสำหรับรอบปัจจุบัน"
  problem: A subscription-cancellation confirmation should name the actual consequence (loses benefits immediately, no refund) rather than a vague "you won't get benefits anymore" — this is a meaning-completeness fix, not just a naturalness one.
  principles: [contexts/ux-writing.md#destructive-actions, core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["no-refund policy, if it applies, must be stated — omitting it would misrepresent the consequence"]
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: ux-writing-research.md#destructive-actions
  human_validated: false

- id: notif-011
  category: "Notification/Toast/Confirmation"
  context: ux-writing
  audience: End User
  input: "ต้องการออกจากระบบใช่ไหม"
  better_output: "(no change — already correct)"
  problem: A non-destructive confirmation (logout) is already at the right length and directness — this is not a destructive action and doesn't need consequence-stating language.
  principles: [contexts/ux-writing.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: notif-012
  category: "Notification/Toast/Confirmation"
  context: ux-writing
  audience: End User
  input: "คุณมีการเปลี่ยนแปลงที่ยังไม่ได้บันทึก คุณต้องการที่จะออกจากหน้านี้โดยไม่บันทึกการเปลี่ยนแปลงหรือไม่"
  better_output: "ออกโดยไม่บันทึกใช่ไหม การเปลี่ยนแปลงจะหายไป"
  problem: A discard-changes dialog should state the consequence (changes will be lost) directly rather than restating the question twice ("do you want to leave without saving" already implies unsaved changes exist).
  principles: [contexts/ux-writing.md#destructive-actions, core/conciseness.md]
  failure_modes: [over-explanation]
  meaning_constraints: ["unsaved changes will be lost if the user proceeds"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: notif-013
  category: "Notification/Toast/Confirmation"
  context: ux-writing
  audience: End User
  input: "การเปลี่ยนแปลงของท่านได้ถูกบันทึกแล้ว"
  better_output: "บันทึกการเปลี่ยนแปลงแล้ว"
  problem: Textbook passive calque — "have been saved" translated with ถูก...แล้ว when Thai defaults to active/topic-fronted phrasing for a routine, non-adversative confirmation toast.
  principles: [core/natural-thai.md]
  failure_modes: [passive-calque]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: translation-adaptation.md#your-changes-have-been-saved
  human_validated: false

- id: notif-014
  category: "Notification/Toast/Confirmation"
  context: ux-writing
  audience: End User
  input: "การส่งออกข้อมูลของท่านเสร็จสมบูรณ์แล้ว"
  better_output: "(no change — เสร็จสมบูรณ์ earns its place here)"
  problem: Unlike a routine save (see notif-013), a long-running export job genuinely could have failed partway — explicitly confirming full completion ("เสร็จสมบูรณ์") is warranted here, not over-translation, because failure was a real, salient possibility the user was watching for.
  principles: [translation-adaptation.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: translation-adaptation.md#successfully-completed-saved
  human_validated: false

- id: notif-015
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "มีการเข้าสู่ระบบจากอุปกรณ์ใหม่: iPhone 15, กรุงเทพฯ"
  better_output: "(no change — correct register for a routine, non-security-flagged login)"
  problem: A routine "new device" FYI notification (not flagged as suspicious by the system) can stay this plain and non-alarming — contrast with notif-016, the security-flagged version of the same event shape.
  principles: [core/tone.md]
  failure_modes: []
  meaning_constraints: ["device and location details must remain exact"]
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: real-product-observations.md#ais
  human_validated: false

- id: notif-016
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "เราตรวจพบการเข้าสู่ระบบจากอุปกรณ์ใหม่ที่อาจมีความเสี่ยง กรุณาตรวจสอบและดำเนินการหากไม่ใช่ท่าน"
  better_output: "พบการเข้าสู่ระบบที่มีความเสี่ยงจากอุปกรณ์ใหม่ ถ้าไม่ใช่คุณ เปลี่ยนรหัสผ่านทันที"
  problem: Same event SHAPE as notif-015 (new device login) but flagged as risky by the system — this is the AIS/Krungthai NEXT severity pattern: drop hedging ("อาจมีความเสี่ยง" → state it as found), drop vague "ดำเนินการ" for the specific action (change password).
  principles: [core/anti-ai.md, core/tone.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: ["the conditional (if it wasn't you) and the specific action (change password) must remain"]
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: real-product-observations.md#krungthai-next (2nd independent severity data point)
  human_validated: false

- id: notif-017
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "เพื่อนของคุณเพิ่งเข้าร่วมแอปนี้! กดเพื่อดูโปรไฟล์และเริ่มต้นแชทกับเพื่อนได้เลย!"
  better_output: "เพื่อนของคุณเข้าร่วมแอปแล้ว กดดูโปรไฟล์"
  problem: Two exclamation points and "start chatting with your friend right away!" oversell a routine social notification; state the fact and the one action.
  principles: [core/conciseness.md]
  failure_modes: [over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: low
  evidence_type: HYPOTHESIS
  source: internal
  human_validated: false

- id: notif-018
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: Customer
  input: "สรุปกิจกรรมประจำสัปดาห์ของคุณ: ใช้งานแอป 5 วัน ทำรายการทั้งหมด 12 รายการ"
  better_output: "(no change — already correct)"
  problem: A weekly-digest-email-style notification stating two concrete numbers plainly needs no rewriting.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: ["both numbers (5 days, 12 transactions) must remain exact"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: notif-019
  category: "Notification/Toast/Confirmation"
  context: notifications
  audience: End User
  input: "ไม่มีการแจ้งเตือนใหม่ ผิดพลาด"
  better_output: "ไม่มีการแจ้งเตือนใหม่"
  problem: A notification-center empty state styled/worded as an error ("ผิดพลาด") is the same hostile pattern as err-015 — a routine absence of new notifications is not a failure.
  principles: [core/tone.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: error-writing-research.md#hostile-patterns
  human_validated: false

- id: notif-020
  category: "Notification/Toast/Confirmation"
  context: ux-writing
  audience: End User
  input: "ลบโพสต์นี้ใช่ไหม การกระทำนี้ไม่สามารถย้อนกลับได้"
  better_output: "(no change — already correct)"
  problem: A destructive-action confirmation that names the action and states irreversibility in two short sentences is already well-calibrated — a control case against over-elaborating a dialog that's already doing its job.
  principles: [contexts/ux-writing.md#destructive-actions]
  failure_modes: []
  meaning_constraints: ["irreversibility must remain stated"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false
```

## Engineering (25)

```yaml
- id: eng-001
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// ตรวจสอบว่ามีข้อมูลหรือไม่เพื่อดำเนินการในขั้นตอนถัดไป\nif (!order) return null;"
  better_output: "// ไม่มี Order ก็ไม่ต้องแสดงตาราง"
  problem: The canonical worked example — this comment is only correct once paired with its actual code, stating why the guard exists rather than restating what it visibly does.
  principles: [contexts/code-comments.md]
  failure_modes: [over-explanation, redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: technical-writing-research.md#validation-testing-the-framework
  human_validated: false

- id: eng-002
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// เพิ่มค่า count ขึ้นทีละ 1 หน่วย\ncount++;"
  better_output: "(delete the comment)"
  problem: No rewrite earns this comment a place — the code says everything it says. Delete, not rewrite.
  principles: [contexts/code-comments.md]
  failure_modes: [over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: technical-writing-research.md#code-comments-what-vs-why
  human_validated: false

- id: eng-003
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// retry 3 ครั้งเพราะ API ตัวนี้ timeout บ่อยมากตอน peak hour ช่วงเที่ยง\nconst MAX_RETRIES = 3;"
  better_output: "// retry 3 ครั้งเพราะ API ตัวนี้ timeout บ่อยตอน peak hour ช่วงเที่ยง"
  problem: Already explains a real, non-obvious constraint (why 3, why retry at all) — only "มาก" is trimmed as a minor intensity-word tighten, nothing structural.
  principles: [core/anti-ai.md, contexts/code-comments.md]
  failure_modes: []
  meaning_constraints: ["the actual reason (peak-hour API timeouts) must remain"]
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-004
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// เช็ค null ก่อนเพราะบางครั้ง API เก่าจะ return field นี้เป็น null แทนที่จะเป็น empty array ตามที่ documented ไว้ในเวอร์ชันใหม่ ซึ่งทำให้เกิด error ตอน .map() ถ้าไม่เช็คก่อน"
  better_output: "// API เก่าคืน null แทน [] บาง endpoint (ไม่ตรง doc) เช็คก่อน .map() ป้องกัน error"
  problem: Keeps the exact constraint (old API returns null contradicting docs) while cutting the redundant explanation of a consequence the reader already infers.
  principles: [core/conciseness.md, core/meaning-preservation.md]
  failure_modes: [over-explanation]
  meaning_constraints: ["old API returns null instead of [] must remain the stated reason"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-005
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// function นี้ใช้สำหรับคำนวณราคารวมของตะกร้าสินค้า"
  better_output: "(delete — function name/signature already says this)"
  problem: If the function is named e.g. calculateCartTotal(), a comment restating that is pure redundancy regardless of Thai phrasing quality.
  principles: [contexts/code-comments.md]
  failure_modes: [over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: technical-writing-research.md#code-comments-what-vs-why
  human_validated: false

- id: eng-006
  category: Engineering
  context: commits
  audience: Developer
  input: "ทำการแก้ไขปัญหาเกี่ยวกับการคำนวณราคาสินค้าที่ไม่ถูกต้องเมื่อมีการใช้ส่วนลดหลายรายการพร้อมกัน"
  better_output: "แก้: คำนวณราคาผิดเมื่อใช้ส่วนลดซ้อนกันหลายรายการ"
  problem: Conventional-commit-style imperative subject, ทำการ padding removed, same scope preserved.
  principles: [contexts/commits.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: ["scope of the fix (multiple stacked discounts) must remain"]
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#redundant-verb-construction
  human_validated: false

- id: eng-007
  category: Engineering
  context: commits
  audience: Developer
  input: "เพิ่ม feature ใหม่"
  better_output: "เพิ่ม: รองรับการชำระด้วย QR พร้อมเพย์"
  problem: "Add new feature" tells a future git-log reader nothing; name the actual feature.
  principles: [core/clarity.md, contexts/commits.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-008
  category: Engineering
  context: commits
  audience: Developer
  input: "ปรับปรุงโค้ดให้ดีขึ้น"
  better_output: "ปรับ: แยก validation logic ออกจาก controller เป็น service แยก"
  problem: "Improve the code" is content-free; state what specifically changed even for a no-user-facing-effect refactor.
  principles: [core/clarity.md, contexts/commits.md]
  failure_modes: [weak-verbs]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#weak-verbs
  human_validated: false

- id: eng-009
  category: Engineering
  context: pull-requests
  audience: [Developer, QA]
  input: "ใน PR นี้จะทำการปรับปรุงฟังก์ชันการค้นหาสินค้าให้มีประสิทธิภาพมากยิ่งขึ้น โดยได้ทำการเปลี่ยนแปลง query ที่ใช้ในการดึงข้อมูลจากฐานข้อมูล"
  better_output: "ค้นหาสินค้าช้าเพราะ query เดิมสแกนทั้งตาราง เปลี่ยนไปใช้ index ที่มีอยู่แล้วแทน\n\nวิธีทดสอบ: ค้นหาคำที่มีผลลัพธ์เกิน 1000 รายการ เทียบเวลาก่อน/หลัง"
  problem: Leads with why (search was slow, actual cause) instead of announcing improvements will happen; adds a concrete test step the diff can't provide.
  principles: [contexts/pull-requests.md]
  failure_modes: [generic-introductory-phrases, redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-010
  category: Engineering
  context: pull-requests
  audience: Developer
  input: "Fix bug"
  better_output: "แก้บั๊กหน้า checkout ค้างเมื่อกดยืนยันซ้ำสองครั้งเร็วๆ"
  problem: A one-line PR title with no context forces every reviewer to open the diff cold; name the actual bug.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-011
  category: Engineering
  context: pull-requests
  audience: [Developer, Internal Team]
  input: "PR นี้ยังไม่ครอบคลุมกรณีที่ผู้ใช้ยกเลิกการชำระเงินกลางคัน แต่จะแก้ใน PR ถัดไป"
  better_output: "(no change — already correct)"
  problem: A known-limitation disclosure this direct and complete is exactly what should stay verbatim in a PR description.
  principles: [contexts/pull-requests.md, core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["the disclosed limitation must remain stated"]
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-012
  category: Engineering
  context: requirements
  audience: [Developer, QA]
  input: "ระบบต้องสามารถจัดการกับกรณีที่ผู้ใช้ยังไม่ได้ยืนยันอีเมลของตนเองในขณะที่พยายามเข้าสู่ระบบได้อย่างเหมาะสม"
  better_output: "Given ผู้ใช้ยังไม่ยืนยันอีเมล\nWhen ผู้ใช้พยายามเข้าสู่ระบบ\nThen ระบบแสดงข้อความให้ยืนยันอีเมลก่อน"
  problem: "Handle appropriately" is untestable; Given/When/Then names precondition, trigger, expected behavior, with structural labels kept in English.
  principles: [contexts/requirements.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: business-writing-research.md#acceptance-criteria
  human_validated: false

- id: eng-013
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// workaround สำหรับ Safari bug ที่ทำให้ flexbox gap ไม่ทำงานถูกต้องใน iOS < 14.5 อย่าลบ comment นี้จนกว่าจะ drop support เวอร์ชันเก่า"
  better_output: "(no change — already correct)"
  problem: Exactly the "non-obvious constraint" a comment should document — a browser bug plus a removal condition tied to a support policy.
  principles: [contexts/code-comments.md, core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["the removal condition (dropping old iOS support) must remain"]
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: technical-writing-research.md#code-comments-what-vs-why
  human_validated: false

- id: eng-014
  category: Engineering
  context: commits
  audience: Developer
  input: "Merge branch 'main' into feature/checkout"
  better_output: "(no change — already correct)"
  problem: An auto-generated merge commit message shouldn't be "humanized" — there's no authored prose here to review.
  principles: [core/anti-ai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-015
  category: Engineering
  context: pull-requests
  audience: [Developer, Designer]
  input: "อัปเดต UI ให้สวยขึ้น"
  better_output: "ปรับ spacing และสีปุ่มให้ตรงกับ design system เวอร์ชันใหม่ (ดู Figma link)"
  problem: "Make the UI prettier" isn't reviewable; name the specific visual change and link the source of truth.
  principles: [core/clarity.md]
  failure_modes: [unnecessary-abstraction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-abstraction
  human_validated: false

- id: eng-016
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// TODO: refactor this later"
  better_output: "// TODO: แยก validateOrder ออกจากฟังก์ชันนี้ ตอนนี้รวม validation + side-effect ไว้ด้วยกัน ทดสอบยาก"
  problem: A bare "refactor this later" TODO gives a future reader nothing to act on; state what specifically needs refactoring and why.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-017
  category: Engineering
  context: requirements
  audience: [Product Manager, Developer]
  input: "ยกเลิกออเดอร์ไม่ได้หลัง 24 ชั่วโมงเพราะระบบคลังสินค้าตัดสต๊อกไปแล้วและการคืนสต๊อกทำได้ยากในทางปฏิบัติ"
  better_output: "Rule: ยกเลิกออเดอร์ได้เฉพาะภายใน 24 ชั่วโมงหลังสั่งซื้อ\nNote (เหตุผล): ระบบคลังตัดสต๊อกอัตโนมัติหลัง 24 ชั่วโมง"
  problem: Separating rule from rationale keeps the rule stable and grep-able even if the justification changes later.
  principles: [contexts/requirements.md, core/meaning-preservation.md]
  failure_modes: []
  meaning_constraints: ["the 24-hour threshold must remain exact"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-018
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// อย่าเปลี่ยน magic number นี้เด็ดขาด"
  better_output: "// timeout = 4500ms ตรงกับ SLA ฝั่ง partner API เปลี่ยนต้องแจ้งทีม infra ก่อน"
  problem: "Never change this" without saying why invites someone to change it anyway the first time they don't understand the risk.
  principles: [contexts/code-comments.md, core/clarity.md]
  failure_modes: []
  meaning_constraints: ["the SLA value (4500ms) must remain exact"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-019
  category: Engineering
  context: pull-requests
  audience: QA
  input: "รบกวนช่วยทดสอบ PR นี้หน่อยได้ไหมครับ ขอบคุณมากครับ"
  better_output: "รบกวนทดสอบ PR นี้หน่อยครับ — ทดสอบ flow ชำระเงินด้วยบัตรหมดอายุ ควร reject ไม่ใช่ค้าง"
  problem: A test request needs to say what to actually test; the politeness level (ครับ, รบกวน) is fine for internal-team register and doesn't need trimming.
  principles: [core/clarity.md, core/tone.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: eng-020
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// initialize variable"
  better_output: "(delete the comment)"
  problem: A comment restating a variable declaration adds nothing in any language — the fix is deletion, not better Thai translation.
  principles: [contexts/code-comments.md]
  failure_modes: [over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: technical-writing-research.md#code-comments-what-vs-why
  human_validated: false

- id: eng-021
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// ตรวจสอบว่า orders ว่างหรือไม่\nif (!orders.length) {"
  better_output: "(delete the comment)"
  problem: This literally translates the condition ("check whether orders is empty") with zero information the if-statement doesn't already show a reader who can read the language.
  principles: [contexts/code-comments.md]
  failure_modes: [over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: technical-writing-research.md#validation-testing-the-framework
  human_validated: false

- id: eng-022
  category: Engineering
  context: code-comments
  audience: Developer
  input: "// เพิ่มการเช็คตรงนี้"
  better_output: "// ต้องตรวจสิทธิ์ก่อนสร้าง Order เพราะ API เดิมไม่ได้บังคับ rule นี้"
  problem: "Added a check here" restates that a check exists without saying why — the real, non-obvious information (a gap in a different, older API this code has to compensate for) is what's missing and what must be added.
  principles: [contexts/code-comments.md]
  failure_modes: [over-explanation, weak-verbs]
  meaning_constraints: ["the actual constraint (old API doesn't enforce this permission rule) must be the stated reason"]
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: technical-writing-research.md#validation-testing-the-framework
  human_validated: false

- id: eng-023
  category: Engineering
  context: pull-requests
  audience: [Developer, Internal Team]
  input: "เดี๋ยวมาแก้ให้จ้า รอแป๊บนึงนะจ๊ะ~ 😊"
  better_output: "แก้ให้ภายในวันนี้ครับ"
  problem: Forcing a casual, emoji-laden register onto a PR-thread status update clashes with the neutral-technical register this surface calls for — this is fake conversational tone, distinct from simply being informal in a context where informal is genuinely appropriate (contrast with eng-019, where the casual register IS correct).
  principles: [core/tone.md]
  failure_modes: [fake-conversational-tone]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#fake-conversational-tone
  human_validated: false

- id: eng-024
  category: Engineering
  context: commits
  audience: Developer
  input: "มีการเปลี่ยนแปลงในส่วนของฟังก์ชันคำนวณภาษี"
  better_output: "เปลี่ยนวิธีคำนวณภาษีมูลค่าเพิ่มให้รองรับอัตราหลายแบบ"
  problem: "มีการเปลี่ยนแปลง" (there was a change) is a weak-verb construction that doesn't say what changed; name the actual change.
  principles: [core/clarity.md, contexts/commits.md]
  failure_modes: [weak-verbs]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#weak-verbs
  human_validated: false

- id: eng-025
  category: Engineering
  context: pull-requests
  audience: [Developer, QA]
  input: "แก้ race condition ตอน 2 requests เขียน stock พร้อมกัน โดยเพิ่ม row-level lock ตอน decrement\n\nวิธีทดสอบ: ยิง 2 requests ซื้อสินค้าชิ้นสุดท้ายพร้อมกัน ต้องมีแค่ 1 คำสั่งซื้อสำเร็จ"
  better_output: "(no change — already correct)"
  problem: Leads with the actual cause, states the fix mechanism, and gives a concrete test — already a well-written PR description needing no rewrite.
  principles: [contexts/pull-requests.md]
  failure_modes: []
  meaning_constraints: ["the exact fix mechanism (row-level lock) and test procedure must remain"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false
```

## Product/Business (20)

```yaml
- id: biz-001
  category: Product/Business
  context: requirements
  audience: [Product Manager, Developer]
  input: "ระบบต้องตอบสนองเร็ว"
  better_output: "ระบบต้องแสดงผลภายใน 2 วินาที"
  problem: "Fast" is untestable; a verifiable threshold makes this an acceptance criterion rather than an aspiration.
  principles: [contexts/requirements.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: business-writing-research.md#acceptance-criteria
  human_validated: false

- id: biz-002
  category: Product/Business
  context: requirements
  audience: Stakeholder
  input: "เรียนท่านผู้บริหาร ทางทีมพัฒนาใคร่ขอเรียนให้ทราบว่าในขณะนี้ได้ดำเนินการแก้ไขปัญหาที่ท่านได้แจ้งมาเรียบร้อยแล้ว ทั้งนี้ ระบบสามารถใช้งานได้ตามปกติแล้วในขณะนี้"
  better_output: "แก้บั๊กที่แจ้งไว้เรียบร้อยแล้ว ระบบใช้งานได้ปกติ"
  problem: An internal status update to a PM/stakeholder the team works with regularly isn't a formal external letter — professional doesn't mean maximum formality here.
  principles: [core/tone.md]
  failure_modes: [excessive-formal-connectors]
  meaning_constraints: ["fix is complete, system is back to normal"]
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: business-writing-research.md#audience-based-register-research
  human_validated: false

- id: biz-003
  category: Product/Business
  context: documentation
  audience: Executive
  input: "เดือนนี้เราแก้บั๊กไปเยอะมาก ระบบเสถียรขึ้นเยอะเลย ลูกค้าน่าจะแฮปปี้"
  better_output: "เดือนนี้ปิดบั๊กสำคัญ 12 รายการ อัตราการเกิดข้อผิดพลาดของระบบลดลง 40%"
  problem: An executive summary needs concrete outcomes, not a casual impression — the opposite mismatch from biz-002, wrong for the same reason: audience/context mismatch.
  principles: [core/tone.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: biz-004
  category: Product/Business
  context: requirements
  audience: [Product Manager, Developer, QA]
  input: "ในกรณีที่ผู้ใช้ยกเลิกการสมัครสมาชิกก่อนครบกำหนดชำระเงินรอบถัดไป ทั้งนี้ ระบบจะไม่คืนเงินค่าบริการที่ชำระไปแล้วตามที่ระบุไว้ในข้อตกลงการใช้บริการดังกล่าว"
  better_output: "(no change — already correct)"
  problem: A ToS/business-rule clause where ในกรณีที่/ทั้งนี้/ดังกล่าว are all correct register — the key negative test for the "no blacklist" design.
  principles: [core/anti-ai.md]
  failure_modes: []
  meaning_constraints: ["all stated conditions must remain exactly"]
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: biz-005
  category: Product/Business
  context: pull-requests
  audience: Internal Team
  input: "อยากให้ทุกคนช่วยรีวิว PR นี้หน่อยนะครับ เพราะมันค่อนข้างสำคัญและอาจกระทบกับหลายส่วนของระบบ"
  better_output: "รบกวนช่วยรีวิว PR นี้หน่อยครับ กระทบ payment flow กับ order history"
  problem: "Quite important and might affect many parts of the system" is too vague to help prioritize review; name the actual affected areas.
  principles: [core/clarity.md]
  failure_modes: [unnecessary-abstraction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-abstraction
  human_validated: false

- id: biz-006
  category: Product/Business
  context: requirements
  audience: [Product Manager, Designer]
  input: "ผู้ใช้ต้องสามารถแก้ไขข้อมูลโปรไฟล์ของตนเองได้อย่างง่ายดายและสะดวกสบาย"
  better_output: "ผู้ใช้แก้ไขชื่อ รูปโปรไฟล์ และอีเมลได้จากหน้าตั้งค่า"
  problem: "Easily and conveniently" describes a feeling, not a requirement; list the actual editable fields and where.
  principles: [contexts/requirements.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: biz-007
  category: Product/Business
  context: documentation
  audience: Customer
  input: "ปรับปรุง indexing algorithm ของระบบค้นหาให้มีประสิทธิภาพมากขึ้น"
  better_output: "ค้นหาสินค้าได้เร็วขึ้น"
  problem: A public changelog entry should lead with user benefit, not internal implementation detail.
  principles: [contexts/customer-facing.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: biz-008
  category: Product/Business
  context: requirements
  audience: [PM, Internal Team]
  input: "ทีมงานควรพยายามทำงานให้เสร็จภายในเวลาที่กำหนดให้มากที่สุดเท่าที่จะเป็นไปได้"
  better_output: "ส่งมอบ feature นี้ภายในวันที่ 15 มี.ค."
  problem: "Try to finish as much as possible" hedges to the point of saying nothing; a real deadline, once known, is the actual requirement.
  principles: [core/clarity.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: biz-009
  category: Product/Business
  context: documentation
  audience: Executive
  input: "ในไตรมาสนี้บริษัทประสบความสำเร็จอย่างสูงในการดำเนินธุรกิจในทุกมิติ"
  better_output: "รายได้ไตรมาสนี้เติบโต 18% เทียบไตรมาสก่อน ต้นทุนลดลง 6%"
  problem: "Succeeded highly in every dimension" is the kind of statement filled in without real numbers — an executive summary needs the actual figures.
  principles: [core/clarity.md, core/meaning-preservation.md]
  failure_modes: [unnecessary-abstraction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-abstraction
  human_validated: false

- id: biz-010
  category: Product/Business
  context: requirements
  audience: QA
  input: "ทดสอบว่าฟีเจอร์ทำงานถูกต้องในทุกกรณี"
  better_output: "ทดสอบ: (1) checkout สำเร็จเมื่อสต๊อกพอ (2) checkout ล้มเหลวเมื่อสต๊อกหมดระหว่างชำระเงิน (3) checkout ล้มเหลวเมื่อบัตรถูกปฏิเสธ"
  problem: "Works correctly in every case" isn't a test plan; enumerate cases, splitting happy path from error/edge cases.
  principles: [contexts/requirements.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: business-writing-research.md#acceptance-criteria
  human_validated: false

- id: biz-011
  category: Product/Business
  context: documentation
  audience: Stakeholder
  input: "โปรเจกต์นี้ล่าช้ากว่ากำหนดเดิมเล็กน้อยเนื่องจากมีความท้าทายทางเทคนิคบางประการที่ทีมงานกำลังเร่งดำเนินการแก้ไขอยู่"
  better_output: "โปรเจกต์ล่าช้า 1 สัปดาห์ เพราะปัญหา integration กับระบบ payment ของพาร์ทเนอร์ คาดว่าจะเสร็จ 20 มี.ค."
  problem: "Slightly delayed due to some technical challenges" hides both the actual delay length and cause — a stakeholder needs both to plan.
  principles: [core/clarity.md, core/meaning-preservation.md]
  failure_modes: [unnecessary-abstraction]
  meaning_constraints: ["the actual delay length and cause, once known, must be stated"]
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-abstraction
  human_validated: false

- id: biz-012
  category: Product/Business
  context: pull-requests
  audience: Internal Team
  input: "เห็นด้วยกับแนวทางนี้ครับ แต่ส่วนตัวคิดว่าอาจจะยังมีจุดที่ควรพิจารณาเพิ่มเติมอยู่บ้างเล็กน้อย"
  better_output: "เห็นด้วยกับแนวทางหลัก แต่กังวลเรื่อง error handling ตอน API timeout — ลอง retry ไหมครับ"
  problem: This is exactly the kreng jai/directness tension: hedged feedback like this gives the author nothing to act on — feedback to a peer can be plainly stated without being harsh.
  principles: [core/tone.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: SOURCE_BACKED
  source: business-writing-research.md#audience-based-register-research
  human_validated: false

- id: biz-013
  category: Product/Business
  context: requirements
  audience: [PM, Developer]
  input: "ระบบควรมีความปลอดภัยในระดับที่เหมาะสม"
  better_output: "รหัสผ่านต้องเข้ารหัสด้วย bcrypt, บังคับ 2FA สำหรับ admin, session หมดอายุใน 30 นาทีที่ไม่มีการใช้งาน"
  problem: "Appropriate level of security" is not implementable; list the actual security requirements.
  principles: [contexts/requirements.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: business-writing-research.md#acceptance-criteria
  human_validated: false

- id: biz-014
  category: Product/Business
  context: documentation
  audience: Customer
  input: "เรามุ่งมั่นที่จะพัฒนาผลิตภัณฑ์อย่างต่อเนื่องเพื่อมอบประสบการณ์ที่ดีที่สุดให้แก่ท่านเสมอ"
  better_output: "(delete — no factual content to preserve)"
  problem: Filler with literally nothing to lose if removed — recommend cutting entirely rather than rewriting more naturally.
  principles: [core/conciseness.md]
  failure_modes: [generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#generic-introductory-phrases
  human_validated: false

- id: biz-015
  category: Product/Business
  context: requirements
  audience: [Product Manager, Developer]
  input: "ราคาสินค้าจะปรับตามส่วนลดที่มีอยู่ ณ ขณะนั้น"
  better_output: "(no change — already correct)"
  problem: Already a precise, testable business rule at the right register for a requirements doc.
  principles: [core/anti-ai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: biz-016
  category: Product/Business
  context: requirements
  audience: [PM, Developer]
  input: "มีการปรับปรุงในเรื่องของขั้นตอนการชำระเงินให้มีความสะดวกมากขึ้น"
  better_output: "ลดขั้นตอนการชำระเงินจาก 5 หน้าเหลือ 2 หน้า"
  problem: "There was an improvement regarding the payment process" is a weak-verb/unnecessary-abstraction combination that names no actual change; state the concrete before/after.
  principles: [core/clarity.md]
  failure_modes: [weak-verbs, unnecessary-abstraction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#weak-verbs
  human_validated: false

- id: biz-017
  category: Product/Business
  context: requirements
  audience: [PM, Developer, QA]
  input: "ระบบต้องมีกลไกในการจัดการกับสถานการณ์ที่ผู้ใช้ทำการยกเลิกคำสั่งซื้อ"
  better_output: "เมื่อผู้ใช้ยกเลิกคำสั่งซื้อ ระบบต้องคืนสต๊อกและยกเลิกการจองส่วนลดที่ใช้ไปทันที"
  problem: "Must have a mechanism to handle the situation" is unnecessary abstraction over a concrete event (order cancellation) with a concrete required response.
  principles: [contexts/requirements.md, core/clarity.md]
  failure_modes: [unnecessary-abstraction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-abstraction
  human_validated: false

- id: biz-018
  category: Product/Business
  context: documentation
  audience: Customer
  input: "เงื่อนไขการคืนเงินเป็นไปตามที่ระบุไว้ในสัญญาการใช้บริการ"
  better_output: "เงื่อนไขการคืนเงินเป็นไปตามที่ระบุไว้ในสัญญาการใช้บริการ"
  problem: Control case (deliberately unchanged) — this is a formal customer-facing policy reference; forcing casual particles or a friendlier tone onto it would be fake-conversational-tone in the wrong direction, not an improvement.
  principles: [core/tone.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: biz-019
  category: Product/Business
  context: documentation
  audience: Stakeholder
  input: "ทีมได้ปิด sprint นี้ไปแล้วโดยส่งมอบฟีเจอร์การค้นหาแบบใหม่และแก้ไขบั๊กที่เกี่ยวกับการชำระเงินเรียบร้อย สรุปแล้วคือ sprint นี้ทีมสามารถส่งมอบฟีเจอร์การค้นหาใหม่และแก้บั๊กการชำระเงินได้สำเร็จ"
  better_output: "ทีมปิด sprint นี้แล้ว ส่งมอบฟีเจอร์ค้นหาแบบใหม่และแก้บั๊กการชำระเงินเรียบร้อย"
  problem: The second sentence restates the first sentence's conclusion almost verbatim — unnecessary summary repetition at the paragraph level, distinct from restating an obvious consequence at the sentence level.
  principles: [core/conciseness.md]
  failure_modes: [unnecessary-summary-repetition]
  meaning_constraints: ["both delivered items (search feature, payment bug fix) must remain"]
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-summary-repetition
  human_validated: false

- id: biz-020
  category: Product/Business
  context: pull-requests
  audience: Internal Team
  input: "sprint นี้เต็มแล้ว เอาไปทำ sprint หน้าแทนได้ไหม"
  better_output: "(no change — already correct)"
  problem: A short, direct internal Slack-style planning message is already correctly calibrated for this audience/context — a control case against over-formalizing routine internal-team communication.
  principles: [core/tone.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false
```

## Documentation (20)

```yaml
- id: doc-001
  category: Documentation
  context: documentation
  audience: Developer
  input: "ในปัจจุบันการพัฒนาซอฟต์แวร์มีความสำคัญมากขึ้นเรื่อยๆ และการจัดการข้อมูลอย่างมีประสิทธิภาพก็เป็นสิ่งจำเป็น โปรเจกต์นี้จึงถูกสร้างขึ้นมาเพื่อช่วยแก้ปัญหาดังกล่าว"
  better_output: "โปรเจกต์นี้จัดการคิวงานพื้นหลังสำหรับระบบที่มี throughput สูง"
  problem: A README should lead with what the project does in the first sentence, not scene-setting.
  principles: [contexts/documentation.md]
  failure_modes: [generic-introductory-phrases, bureaucratic-reference-words]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#generic-introductory-phrases
  human_validated: false

- id: doc-002
  category: Documentation
  context: documentation
  audience: Developer
  input: "คุณอาจจะต้องพิจารณาตั้งค่า API key ของท่านในไฟล์ .env ก่อนที่จะเริ่มต้นใช้งาน"
  better_output: "ตั้งค่า API key ในไฟล์ .env ก่อนเริ่มใช้งาน"
  problem: API docs need literal, testable instructions — "you might want to consider" isn't an instruction.
  principles: [contexts/documentation.md, core/clarity.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-003
  category: Documentation
  context: customer-facing
  audience: Customer
  input: "ปรับปรุง indexing algorithm ของระบบค้นหาให้มีประสิทธิภาพมากขึ้น"
  better_output: "ค้นหาสินค้าได้เร็วขึ้น"
  problem: Same principle as biz-007, restated for the internal-release-note vs. public-changelog distinction.
  principles: [contexts/customer-facing.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-004
  category: Documentation
  context: documentation
  audience: Stakeholder
  input: "อัปเดตใหญ่มาแล้ว! เร็วขึ้นเยอะ บั๊กหายเพียบ"
  better_output: "เวอร์ชันนี้ปรับปรุงประสิทธิภาพการประมวลผลข้อมูลและแก้ไขข้อบกพร่อง 8 รายการที่รายงานโดยลูกค้า"
  problem: An enterprise B2B release note needs a measured, specific register — the opposite mismatch from a consumer app's casual "what's new."
  principles: [core/tone.md]
  failure_modes: [fake-conversational-tone]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#fake-conversational-tone
  human_validated: false

- id: doc-005
  category: Documentation
  context: documentation
  audience: Developer
  input: "ฟังก์ชันนี้จะทำการรับค่า parameter สองตัวและทำการคืนค่าผลลัพธ์ที่ได้จากการคำนวณ"
  better_output: "รับ parameter สองตัว คืนค่าผลรวม"
  problem: API reference text should be literal and terse; "ทำการรับ...ทำการคืนค่า" is redundant-verb padding even in technical documentation.
  principles: [contexts/documentation.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#redundant-verb-construction
  human_validated: false

- id: doc-006
  category: Documentation
  context: documentation
  audience: Developer
  input: "# การติดตั้ง\n\nก่อนอื่นท่านจะต้องทำการติดตั้ง dependency ที่จำเป็นทั้งหมดเสียก่อน โดยสามารถทำได้ด้วยคำสั่งดังต่อไปนี้"
  better_output: "# การติดตั้ง\n\nติดตั้ง dependency:"
  problem: An "Installation" heading followed by a command doesn't need a sentence introducing the command.
  principles: [core/conciseness.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-007
  category: Documentation
  context: documentation
  audience: Developer
  input: "หมายเหตุ: โปรดทราบว่าฟังก์ชันนี้จะถูกยกเลิกการใช้งาน (deprecated) ในเวอร์ชันถัดไป ทั้งนี้ผู้ใช้งานควรพิจารณาเปลี่ยนไปใช้ฟังก์ชันใหม่แทน"
  better_output: "Deprecated: จะถูกลบในเวอร์ชันถัดไป ใช้ newFunction() แทน"
  problem: A deprecation notice needs the fact, timeline, and replacement — "should consider switching" hedges what should be a direct instruction.
  principles: [core/clarity.md]
  failure_modes: [excessive-formal-connectors]
  meaning_constraints: ["the replacement function name must remain exact"]
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#excessive-formal-connectors
  human_validated: false

- id: doc-008
  category: Documentation
  context: documentation
  audience: Developer
  input: "# Contributing\n\nเรายินดีต้อนรับทุกการมีส่วนร่วมจากชุมชน หากท่านสนใจที่จะมีส่วนร่วมในการพัฒนาโปรเจกต์นี้ กรุณาอ่านแนวทางด้านล่างนี้ก่อนทำการส่ง pull request"
  better_output: "# Contributing\n\nอ่านแนวทางนี้ก่อนส่ง PR"
  problem: Welcoming boilerplate can be cut to the one instruction that matters.
  principles: [core/conciseness.md]
  failure_modes: [generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-009
  category: Documentation
  context: documentation
  audience: Developer
  input: "`timeout` (number): กำหนดระยะเวลาที่ระบบจะรอก่อนที่จะทำการยกเลิกการเชื่อมต่อโดยอัตโนมัติ หน่วยเป็นมิลลิวินาที ค่าเริ่มต้นคือ 5000"
  better_output: "`timeout` (number): ระยะเวลารอก่อนตัดการเชื่อมต่อ (ms) ค่าเริ่มต้น 5000"
  problem: Every fact (unit, default, behavior) is preserved while cutting to what a developer scanning a reference table actually needs.
  principles: [core/conciseness.md, core/meaning-preservation.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: ["unit (ms) and default value (5000) must remain exact"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-010
  category: Documentation
  context: documentation
  audience: Developer
  input: "โปรเจกต์นี้ใช้ MIT License กรุณาดูรายละเอียดเพิ่มเติมได้ที่ไฟล์ LICENSE"
  better_output: "(no change — already correct)"
  problem: Already concise, standard boilerplate for a real, necessary purpose — nothing to trim.
  principles: [core/anti-ai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-011
  category: Documentation
  context: documentation
  audience: Developer
  input: "หากท่านพบปัญหาใดๆ ในระหว่างการใช้งาน กรุณาอย่าลังเลที่จะแจ้งให้ทีมงานทราบผ่านช่องทาง issue tracker ของเรา"
  better_output: "พบปัญหา แจ้งได้ที่ issue tracker"
  problem: "Please don't hesitate to let us know" is a translated politeness formula rather than natural Thai phrasing for a bug-report pointer.
  principles: [core/natural-thai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: translation-adaptation.md#please-make-sure
  human_validated: false

- id: doc-012
  category: Documentation
  context: documentation
  audience: PM
  input: "เอกสารฉบับนี้จัดทำขึ้นเพื่อสรุปภาพรวมของฟีเจอร์ที่จะพัฒนาในไตรมาสถัดไป โดยมีวัตถุประสงค์เพื่อให้ผู้มีส่วนเกี่ยวข้องทุกฝ่ายรับทราบและเข้าใจตรงกัน"
  better_output: "สรุปฟีเจอร์ที่จะพัฒนาไตรมาสหน้า"
  problem: A doc's stated purpose in its own opening sentence is meta-commentary the reader doesn't need.
  principles: [core/conciseness.md]
  failure_modes: [generic-introductory-phrases]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#generic-introductory-phrases
  human_validated: false

- id: doc-013
  category: Documentation
  context: documentation
  audience: Developer
  input: "### Error Handling\n\nในส่วนนี้จะอธิบายเกี่ยวกับวิธีการจัดการข้อผิดพลาดที่อาจเกิดขึ้นได้ในระหว่างการเรียกใช้งาน API"
  better_output: "### Error Handling"
  problem: A section heading followed by a sentence that just restates the heading adds nothing before the actual content.
  principles: [core/conciseness.md]
  failure_modes: [over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#over-explanation
  human_validated: false

- id: doc-014
  category: Documentation
  context: documentation
  audience: Developer
  input: "โปรเจกต์นี้รองรับ Node.js เวอร์ชัน 18 ขึ้นไป"
  better_output: "(no change — already correct)"
  problem: A precise, factual compatibility statement needs no rewriting.
  principles: [core/anti-ai.md]
  failure_modes: []
  meaning_constraints: ["version number (18) must remain exact"]
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-015
  category: Documentation
  context: documentation
  audience: Customer
  input: "เวอร์ชัน 2.4.0 — เราได้ทำการปรับปรุงหลายอย่างเพื่อให้ท่านได้รับประสบการณ์การใช้งานที่ดียิ่งขึ้นกว่าเดิม อาทิเช่น การแก้ไขบั๊กต่างๆ และการปรับปรุงประสิทธิภาพโดยรวมของระบบ"
  better_output: "เวอร์ชัน 2.4.0 — แก้บั๊ก 5 รายการ และทำให้แอปเปิดเร็วขึ้น"
  problem: "Various improvements for a better experience" is the generic-changelog failure mode — replace with the actual count/specifics.
  principles: [core/clarity.md]
  failure_modes: [generic-introductory-phrases, redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#generic-introductory-phrases
  human_validated: false

- id: doc-016
  category: Documentation
  context: documentation
  audience: Developer
  input: "`GET /api/orders/:id` — คืนข้อมูลออเดอร์ตาม id ที่ระบุ ถ้าไม่พบจะคืน 404"
  better_output: "(no change — already correct)"
  problem: A terse, complete API endpoint reference entry needs no rewriting — a control case for API docs specifically.
  principles: [contexts/documentation.md]
  failure_modes: []
  meaning_constraints: ["the 404-on-not-found behavior must remain stated"]
  terminology_constraints: []
  confidence: high
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-017
  category: Documentation
  context: documentation
  audience: Developer
  input: "มีการทำงานร่วมกันระหว่างโมดูลต่างๆ เพื่อให้เกิดการประมวลผลข้อมูลที่มีประสิทธิภาพ"
  better_output: "โมดูล A ส่งข้อมูลให้โมดูล B ประมวลผลแบบ stream ไม่ต้องรอข้อมูลทั้งหมดโหลดเสร็จ"
  problem: "There is collaboration between modules for efficient processing" is unnecessary abstraction describing an architecture diagram in words instead of stating the actual data flow.
  principles: [core/clarity.md]
  failure_modes: [unnecessary-abstraction, weak-verbs]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-abstraction
  human_validated: false

- id: doc-018
  category: Documentation
  context: documentation
  audience: Stakeholder
  input: "Release Notes v3.0 — เวอร์ชันนี้เพิ่มการรองรับหลายสกุลเงินสำหรับลูกค้าองค์กร ปรับปรุง API rate limit จาก 100 เป็น 500 requests/นาที และแก้ไขช่องโหว่ด้านความปลอดภัยระดับ high 1 รายการ (CVE รายละเอียดแจ้งแยกต่างหากทางอีเมล)"
  better_output: "(no change — already correct)"
  problem: An enterprise B2B release note already at the right measured, specific register with real numbers and a security-disclosure note — a control case distinguishing this from doc-004's fix (over-casual) and doc-015's fix (over-vague).
  principles: [core/tone.md]
  failure_modes: []
  meaning_constraints: ["the rate-limit numbers (100→500) and the CVE disclosure note must remain exact"]
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-019
  category: Documentation
  context: documentation
  audience: Developer
  input: "ฟังก์ชัน `formatCurrency(amount, currency)` ใช้สำหรับจัดรูปแบบตัวเลขให้เป็นสกุลเงิน ฟังก์ชันนี้จะรับ amount และ currency แล้วคืนค่าเป็น string ที่จัดรูปแบบแล้วซึ่งเป็นการทำให้ตัวเลขอ่านง่ายขึ้นสำหรับผู้ใช้"
  better_output: "`formatCurrency(amount, currency)` — จัดรูปแบบตัวเลขเป็น string สกุลเงิน (เช่น 1000 → \"฿1,000.00\")"
  problem: The signature already tells the reader what goes in and out; the prose restates that at length and then adds a vague, self-evident justification ("makes numbers easier to read") — a concrete example does more work than either.
  principles: [core/conciseness.md]
  failure_modes: [over-explanation]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: internal
  human_validated: false

- id: doc-020
  category: Documentation
  context: documentation
  audience: Developer
  input: "มีการดำเนินการ cache ข้อมูลเพื่อลดภาระของฐานข้อมูล"
  better_output: "cache ข้อมูลไว้ 10 นาที ลดจำนวน query ไปที่ฐานข้อมูล"
  problem: "There is a caching operation performed" is nominalization padding; state the mechanism and its actual parameter.
  principles: [core/natural-thai.md]
  failure_modes: [unnecessary-nominalization]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#unnecessary-nominalization
  human_validated: false
```

## English-to-Thai Adaptation (10)

```yaml
- id: adapt-001
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "คุณสามารถเปลี่ยนภาพโปรไฟล์ได้โดยการกดที่ไอคอนรูปภาพ"
  better_output: "กดไอคอนรูปภาพเพื่อเปลี่ยนโปรไฟล์"
  problem: "You can X by Ying" is a permission-framing Thai doesn't need for a single, straightforward instruction — reserve คุณสามารถ...ได้ for genuine optionality (contrast uxui-030).
  principles: [core/natural-thai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: translation-adaptation.md#you-can
  human_validated: false

- id: adapt-002
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "เพื่อที่จะดำเนินการต่อ กรุณายืนยันอีเมลของท่าน"
  better_output: "ยืนยันอีเมลก่อนดำเนินการต่อ"
  problem: "In order to" is frequently just "to" in disguise — a padded purpose-clause opener Thai's เพื่อ alone already carries.
  principles: [core/conciseness.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: translation-adaptation.md#in-order-to
  human_validated: false

- id: adapt-003
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "กรุณาตรวจสอบให้แน่ใจว่าท่านได้กรอกข้อมูลครบถ้วนก่อนกดส่ง"
  better_output: "กรอกข้อมูลให้ครบก่อนกดส่ง"
  problem: "Please make sure X" is an English hedge-politeness pattern around what is really just an instruction to do X.
  principles: [core/natural-thai.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: translation-adaptation.md#please-make-sure
  human_validated: false

- id: adapt-004
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "เราไม่สามารถทำการประมวลผลคำขอของท่านได้ในขณะนี้"
  better_output: "ประมวลผลคำขอไม่สำเร็จ"
  problem: English error messages often frame "we" as the grammatical subject; Thai states the result directly without an actor.
  principles: [core/natural-thai.md]
  failure_modes: [redundant-verb-construction, unnecessary-subject-insertion]
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: translation-adaptation.md#we-were-unable-to
  human_validated: false

- id: adapt-005
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "มีบางอย่างผิดพลาดเกิดขึ้น"
  better_output: "เกิดข้อผิดพลาด"
  problem: "Something went wrong" is already content-free filler in English; translating it well doesn't fix that it says nothing — look for a more specific cause before translating at all.
  principles: [error-writing-research.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: PROJECT_DECISION
  source: translation-adaptation.md#something-went-wrong
  human_validated: false

- id: adapt-006
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "คุณแน่ใจหรือไม่ว่าต้องการที่จะลบรายการนี้"
  better_output: "ลบรายการนี้ใช่ไหม"
  problem: The English confirmation template translates into stiff, grammatical-but-awkward Thai — a plain question form is more natural for a routine (non-destructive-tier) confirmation.
  principles: [contexts/ux-writing.md]
  failure_modes: []
  meaning_constraints: []
  terminology_constraints: []
  confidence: medium
  evidence_type: OBSERVED
  source: translation-adaptation.md#are-you-sure
  human_validated: false

- id: adapt-007
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "การบันทึกข้อมูลของท่านเสร็จสมบูรณ์เรียบร้อยแล้วอย่างสำเร็จ"
  better_output: "บันทึกแล้ว"
  problem: Stacking three success-markers redundantly states both the action and its success; Thai's simple completive แล้ว already implies success for an action with no salient partial-failure state.
  principles: [core/conciseness.md]
  failure_modes: [redundant-verb-construction]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: translation-adaptation.md#successfully-completed-saved
  human_validated: false

- id: adapt-008
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "การเปลี่ยนแปลงของท่านได้ถูกบันทึกแล้ว"
  better_output: "บันทึกการเปลี่ยนแปลงแล้ว"
  problem: Textbook passive calque — "have been saved" translated with ถูก...แล้ว for a routine, non-adversative confirmation where Thai defaults to active/topic-fronted phrasing.
  principles: [core/natural-thai.md]
  failure_modes: [passive-calque]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: translation-adaptation.md#your-changes-have-been-saved
  human_validated: false

- id: adapt-009
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "เสื้อยืด 3 ชิ้น รองเท้า 2 ชิ้น"
  better_output: "เสื้อยืด 3 ตัว รองเท้า 2 คู่"
  problem: Wrong or missing Thai classifier for the noun being counted — a correctness check, source-backed via an academic reference grammar.
  principles: [core/natural-thai.md]
  failure_modes: [classifier-errors]
  meaning_constraints: ["quantities (3, 2) must remain exact"]
  terminology_constraints: []
  confidence: high
  evidence_type: SOURCE_BACKED
  source: thai-ai-smell-taxonomy.md#classifier-errors (Iwasaki & Ingkaphirom, A Reference Grammar of Thai)
  human_validated: false

- id: adapt-010
  category: "English-to-Thai Adaptation"
  context: ux-writing
  audience: End User
  input: "ให้ Perfect Skin ของคุณด้วย Premium Quality Serum ตัวนี้"
  better_output: "เซรั่มสูตรพรีเมียม ช่วยให้ผิวคุณดูดีขึ้น"
  problem: Thai has no capitalization system — carrying English heading-style Title Case into a Thai sentence is a visible seam from an English template.
  principles: [core/natural-thai.md]
  failure_modes: [title-case-english-bleed]
  meaning_constraints: []
  terminology_constraints: []
  confidence: high
  evidence_type: OBSERVED
  source: thai-ai-smell-taxonomy.md#title-case-english-bleed
  human_validated: false
```

## Coverage note

31 of these 150 cases (~21%) are explicit "no change needed" control cases (plus 5 more "delete, don't rewrite" cases for code comments/filler prose), spread across every category except English-to-Thai Adaptation — that category's cases are, by construction, all literal-translation patterns that need fixing (uxui-030 plays the equivalent role there, showing when the underlying "คุณสามารถ...ได้" *construction* is correct rather than a full untouched sentence). Two controls are deliberately load-bearing negative tests: `biz-004` (a formal ToS clause a naive rewriter would wrongly casualize) and `err-008` (a developer-facing status code a naive rewriter would wrongly "humanize"). A corpus that only ever shows text getting improved would implicitly train the reviewer — human or model — to always find a fault; recognizing "this is already fine" is as important a skill output as recognizing a real problem. See `core/anti-ai.md`.

Three sets of same-underlying-failure, different-detail-level cases (`err-016/017/018`, `err-019/020`, `notif-015/016`) exist specifically to test that detail level is chosen per-situation, not defaulted to a fixed "always more detail" or "always less" answer — see `error-writing-research.md`.
