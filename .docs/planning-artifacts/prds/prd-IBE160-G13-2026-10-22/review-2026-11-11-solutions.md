---
title: LifeMode PRD, proposed fixes for the review of 2026-11-11
date: 2026-11-11
applies-to: review-2026-11-11.md (A1-A27, E1-E35, S1-S15, P1-P36)
status: proposal
---

# Proposed fixes for the 2026-11-11 review

This file proposes fixes. It doesn't apply any of them, and none is logged as a decision. The team decides the 12 points in the decision table. The rest are recommended as written. The accepted fixes then go in through `bmad-prd` (Update), and the PRD is validated and set final (#55).

There are 38 fixes in 9 areas. Together they cover all 113 findings, and the table at the end shows which fix covers each finding. Figures marked *to verify* must be checked with the engine script when the fix is applied.

## Decisions for the team

| # | Question | Recommended | Alternative | Fix |
|---|---|---|---|---|
| D1 | How did Markus get his car licence in UJ-4? | He paid for it himself in month 39 with what he had saved since 17 (UJ-6). That's why he has no buffer when the card hits its limit, and his mother "can't afford to" help, which matches a parents' gift draw that said no. | Keep the parents' gift. UJ-6 then uses the 50% threshold, and UJ-4 needs a reason his savings are gone. | J2 |
| D2 | Which month is UJ-6? | November, month 35, a quiet month. UJ-6 is the only journey that shows an ordinary month, and October is an active month. | October, with that month's highlight event added to UJ-6 and to examples 25-26. | J3 |
| D3 | When does the credit card offer message arrive? | Month 39. The card opens at 18 (month 37), the bank writes two months later, and month 37 stays free for the car licence. It matches the addendum and the UJ-4 trace. | Month 37. | O1 |
| D4 | What if the player doesn't qualify in the offer month? | The offer arrives anyway and shows what's missing, such as a steady wage (FR-48). Offers stay guaranteed, and the condition is part of the lesson. | The offer waits for the first month the player qualifies. | O4 |
| D5 | What counts as progress towards the savings target? | Current account + savings against the price, at most 100%. It's the same amount FR-48 uses for the missing amount, so the two never disagree. | The savings account only, as now. | T1 |
| D6 | Are messages marked as read? | No. A message is "new" in the month it arrives (FR-54 already says so), and there are no unread badges. Nothing is stored, as now. | Store a read flag that doesn't affect the game and isn't a replay input. | M3 |
| D7 | How do invitations avoid running out? | Invitations are repeatable, at most once each per in-game year. The content check fails if seeded runs have more than 2 months a year with no eligible invitation. | Keep them one-off and raise the minimum to 12 eligible per in-game year. | M5 |
| D8 | Social life shown vs used in rule 12 (A17) | Show "usual" and "this month" separately. "Hvorfor?" says «Det vanlige sosiale livet ditt er under 20». Rule 12 is unchanged. | Count this month's activities in the "social life below 20" row. That changes rule 12, lets activities change carried stress, and needs 26c rechecked. | B4 |
| D9 | Goal 1 for a player who plans activities (A2) | Make a "careful player with some free time" run a pass/fail check now, and tune the targets once the catalogue has real prices (OQ-17, #48). | Lower the goal 1 target now, or accept that players who plan often miss goal 1. | B2 |
| D10 | When the plan would set off a crisis trigger | Warn and ask to confirm. The player decides, as in UJ-4. | Block continuing until the plan is changed. | C3 |
| D11 | Move the new game areas forward in §5 (S2, S3)? | Yes. Move 5.13-5.15 to after 5.4, and give the money view its own section. FR numbers are kept. | Leave the order and add only pointers from §5.4. | R3 |
| D12 | A "same as last month" button for the month plan (A18) | Yes, in the MVP. It places last month's activities again, and each one is checked like any placement. | Leave it to UX (`bmad-ux`) and measure the time in playtests first. | B5 |

## J. UJ-6 and the journeys

### J1. Markus saves for the car licence in UJ-6

Covers A5, A6, E11. Requires T1.

In Norway you can take the moped licence at 16 and the car licence (class B) at 18, so a 17-year-old who already has a moped saving for the car licence makes sense. It also matches UJ-4, where Markus has had the moped licence and a moped since 16.

- **Persona + context:** "Markus, 17, is in Vg2 and works 10 h a week in a shop. He has had the moped licence and a moped since he turned 16 (UJ-4). Now he's saving for the car licence, which he can take at 18, and has pinned it as his savings target (FR-57). In October he took the extra shifts his employer offered: 4 more hours a week for three months."
- **Price:** the car licence is NOK 32,500 (brief addendum parameters). It doesn't open until month 37 (FR-18), so FR-57 must let the player pin an option that hasn't opened yet (T1).
- **The bank message:** at NOK 4,600 of NOK 32,500 (14%), example 25's savings don't reach any threshold. Proposed: savings before the month of **NOK 24,400**, and the bank says he has passed **three quarters** of his target (current account + savings = NOK 24,900, 77%). Interest becomes 24,400 × 2.87% / 12 = 58, giving NOK 24,458. The threshold is passed under either D5 choice: savings alone are 75.1%. Nothing else in example 25 depends on savings, and variant b starts with no savings, so it stays. *To verify.*
- **Why 75% and not 50%:** with D1 as recommended, Markus must pay NOK 32,500 by month 39. From about NOK 24,900 in month 35, the extra shifts and the 18+ wage (NOK 8,452 at 10 h) get him there in about four months. That lands the licence in month 39 and leaves him with no buffer when UJ-4 starts. *To verify.*
- **The gift draw:** add to UJ-6's edge cases: "In month 37 his parents may give him the licence (FR-30). The target is then cleared with a note, and the savings are his to use (T1)."

### J2. UJ-4 follows on from UJ-6 (D1)

Covers A5.

- **Recommended:** replace "His parents paid for his car licence as a gift (FR-30)" with "His parents couldn't give him the car licence, so he paid for it himself in month 39 with what he had saved since 17 (UJ-6). His savings are almost empty."
- This gives UJ-4 its cause: no buffer, a card at its limit, and a mother who can't help.
- The UJ-4 trace in the PRD addendum is a set test state. Add savings of about NOK 0 to its start if it doesn't state them already. No other figure changes.

### J3. UJ-6 in a quiet month (D2)

Covers E12.

- Months 1, 4, 7 and 10 of each year are active, so month 34 (October) is active, yet UJ-6 continues with no real choice.
- **Recommended:** move UJ-6 to month 35 (November), a quiet month. The extra shifts still run from October to December.
- Change the title to "Markus fits a concert into a November with extra shifts".
- Change examples 25 and 26 to "Month 35 (November)". In 26, the values carry over to December. No figure changes.

### J4. UJ-6 wording and place

Covers A7, A25, S8, P6, P13, P14, P34, P35, and the UJ-6 minor fixes.

- Cut "Drafted from the team's month example on 2026-11-10, with the friend Emma from the UX concept." Log it in `.memlog.md`.
- Move UJ-6 between UJ-3 and UJ-4 and keep its ID, so the journeys run in age order: 17, then 18.
- Entry: "His free time (rule 12) is 72 out of 100, which gives him 3 activity slots this month instead of 4."
- Step 1: "Emma invites him to a concert this month, and the bank says he has passed three quarters of his savings target." This removes "on Friday", because the plan has no days (FR-52).
- Step 2: "He wants four things: the concert, an evening with friends, a rest night, and gaming."
- Step 3: "He places the concert and the evening with friends, and the plan shows what they cost together. He puts a rest night in the last slot, because the extra shifts make his weeks long." This replaces "his stress is rising", which example 26 contradicts.
- Step 4: "In the job view he sees that ending the extra shifts would give him 4 slots from December (W1), and how much less he'd keep after spending. He keeps them: they end after December anyway."
- Step 5: "The engine charges the two paid activities after the month's spending…"
- Resolution: "His savings carry over into December, and November's wellbeing score stays in his average. In January his hours drop back to 10 and he gets the fourth slot back. At 20, the ending can show «Konserter og arrangementer» as one entry with what they cost over five years, if they're among the choices that mattered most (FR-42)." «Utesteder» means bars and clubs (18+/20+), which NFR-8 rules out.
- Persona: "and he said yes" becomes "and he took the extra shifts", because replying to messages is V2.

## C. Continuing the month

### C1. Activities are paid like event options

Covers A4, E3.

- FR-45 "Activities": "An activity is paid like an event option (FR-26). With card use on, a card-payable activity that fits whole under the limit goes on the card. Otherwise it's paid from the current account, then savings. It's never split between the card and the accounts. It's paid when the player continues, not when it's planned."
- Add *variant c* to example 25: the concert on the card with card use on, and the interest share if the bill isn't paid in full (B10).

### C2. Check eligibility again at continue

Covers A20, E4.

- FR-53 "Applied at continue": "In slot order, each planned activity is checked again for eligibility (age range, flags, invitation month) and for payment. One that fails either is dropped with a short note and has no effect."
- A card blocked by a payment plan makes the activity not card-payable for that payment.
- NFR-7's non-refusal case becomes "a planned activity the player can no longer pay for or is no longer eligible for", with its own test.

### C3. Show what the plan does before continuing (D10)

Covers A19, E1, E2.

- FR-49: "Before the player continues, the money view shows the rule 8 trigger status and goal progress after the planned activities' payments. If the plan would set off a trigger, continuing asks the player to confirm. In months 59-60, the warning says a crisis then can't be solved before the ending."
- FR-9 and FR-57 show progress after the plan, marked as such.

### C4. A plan changed on another device

Covers E26.

- FR-49: "Continuing carries the version of the plan the device showed. If the plan has changed since, the server refuses and the device reloads (NFR-7)."

### C5. Count only applied activities

Covers E31.

- FR-50 and §7.2: the planning counter-metric counts months with at least one applied activity, and invitation acceptance counts invitations whose activity was applied.

## O. Offers

### O1. One offer-message column in FR-18 (D3)

Covers A10, E6, P7, P18.

Add a column "Offer message" to FR-18, and make FR-17, FR-55, the schema check and the disclosures point to it:

| Option | Offer message |
|---|---|
| Savings account and BSU | None, open from month 1 |
| Part-time job, up to 12 h | Month 3 |
| Moped licence | Month 13, as in the addendum |
| Owning a moped | Gift: a drawn offer (O3). Buying: none, it's in the money view |
| Part-time job, up to 40 h | None, it's in the job view from month 19 |
| Summer job | Months 18, 30 and 42, one repeatable message (O2) |
| Car licence | Month 37: one family message with the result of the gift draw. Either the gift, or "we can't pay, but you can take it yourself", which opens the paid licence |
| Credit card | Month 39 (D3). Open from month 37 |
| Consumer loan | Month 49. Open from month 37 |
| Experience, goal 3 | Month 44 |
| Full-time job | Month 54 |

- **Disclosures:** D10 ("the first licence offer") then fires on the month 13 message. D11 ("the first card offer") fires on the month 39 message. D24 ("the first BSU offer") has no offer, so it becomes "the first time the player opens BSU in the money view".
- **Schema check:** "Every FR-18 row with an offer month has exactly one offer message."
- Glossary "Offer": "The options with an offer month in the FR-18 table arrive this way."

### O2. The summer job is a repeatable offer message

Covers A9, E27, E34, P36.

- Remove "and the yearly summer job offer" from FR-46 "No repeats".
- Message schema, `when`: "Offers: the FR-18 offer months. The summer job message repeats in months 18, 30 and 42."

### O3. Gifts and extra shifts are drawn offers

Covers A11, E14, E15, E16.

- FR-54 "Offer": "points to an open option (FR-48), to extra shifts (FR-47), or to a one-time gift (FR-29, FR-30)."
- Message schema, `when`: add "Drawn offers: required and blocking flags plus a chance per in-game year (configuration)". This covers the employer's extra shifts and the gift moped.
- **Expiry:** a drawn offer can be taken only in the month it arrives. After that the message shows it as expired. Dated FR-18 offers expire as in FR-48. NFR-7 refuses an expired offer, with its own test.
- **Car licence gift:** it applies automatically, and the message tells the result. The gift moped is accepted or declined, because owning one has costs.
- **Extra-shift draw rule:**
  - the player has a job, is below the weekly limit, and has no extra shifts running
  - not in month 60 (W1)
  - new parameter rows: extra-shift offers per year, and the gift moped's chance

### O4. Offers that no longer apply, and players who don't qualify yet (D4)

Covers E7, E33.

- FR-55: "An offer message isn't sent if its option has already been taken, can't be taken again under its one-at-a-time rule, or has closed." This brings back the milestone rule the revision removed.
- FR-55 (D4): "A player who doesn't qualify yet still gets the offer message, and it shows what's missing (FR-48 'Blocked for another reason')." This replaces "in every playthrough where the player qualifies".

## M. Messages

### M1. A message cap with fixed priorities

Covers A15, E8.

- FR-55 "How many": "Offers and the event copy always arrive and don't count towards the limit. Invitations, then info messages, fill the rest of the 3 (configuration). A bank message that doesn't fit arrives the next month instead."

### M2. One way to show the highlight event

Covers A23, E17.

- The highlight event is always shown when the month opens (FR-13, FR-49). Its sender (event schema) also puts a copy in the phone, so the event reads as coming from someone. The copy isn't a separate message, needs no answer in the inbox, and doesn't count towards the limit.
- FR-54 "Event" becomes "the phone copy of the month's highlight event". Remove kind "event" from the message schema.
- FR-49's "unread messages never stop the player" then stays true.

### M3. No read state (D6)

Covers A24.

- FR-16: "The recap says how many messages arrived this month."
- Tell UX: messages are "new" in their own month, and there are no unread badges across months.

### M4. Bank progress messages

Covers A14, E9, P29.

- FR-55: "Bank messages follow goal 1's progress (the only goal with a percentage, FR-9) and the savings target's progress (FR-57)."
- "Each threshold is sent once per target in a playthrough. If several are passed in one month, only the highest is sent. Pinning the same option again doesn't resend thresholds already sent."
- FR-12: pins are part of the stored game state and are replay inputs.

### M5. Enough invitations (D7)

Covers A15.

- Invitations are repeatable, at most once each per in-game year.
- The content check fails if seeded runs have more than 2 months a year with no eligible invitation.

## T. Savings target

### T1. Savings target rules (D5)

Covers A13, E10, P15. Needed for J1.

- "The player can pin one option with a price, also one that hasn't opened yet. The view then shows when it opens (FR-18)."
- "Progress is the current account plus savings against the price, at most 100%, calculated by the engine. BSU and the card don't count. It's the same amount the missing amount uses (FR-48)." (D5)
- "An option with two prices, such as a new or a used moped, is pinned as one of them."
- "When the pinned option is taken, given as a gift, or closes, the target is cleared with a short note."
- "Pinning moves no money and isn't a choice, and the target can be changed in any month."

## W. Work and hours

### W1. Extra shifts on top of the hours setting

Covers A12, E13.

FR-47:
- "Weekly hours = the hours setting + running extra shifts, never above rule 10. An offer is capped at the limit. Changing the setting changes only the base."
- "Running extra shifts can be ended from the job view, from the next month."
- "Quitting or changing job ends them."
- "No new extra-shift offer comes while extra shifts run."

FR-56 shows the set hours and this month's hours with extra shifts.

### W2. Hours changes and the summer job

Covers E24, E25.

- "An hours change is checked against the rule 10 limit of the month it applies from. A change made in month 18 may set up to 40 h for month 19."
- "If an hours change or extra shifts would cut a summer job the player has taken, the control warns first. If July's cut leaves 0 h, the summer job is cancelled with a note."

### W3. Month 60

Covers E23.

- In month 60, actions that only take effect the next month are hidden or marked as having no effect. The upcoming-costs and slot previews are empty.

## H. Events and scheduling

### H1. Follow-ups

Covers A27, E18, E19, E20, E35.

FR-46:
- "Follow-ups are never drawn at random. They take a month only when due."
- "A due follow-up whose required flag is no longer set is dropped, and the month draws as normal."
- "When a crisis is skipped as the month opens (FR-32), the month's event is chosen again in the usual order: card warning, due follow-up, then a drawn event if the month is active."
- "A follow-up that can't get a month by month 60 is dropped, and the content check reports it." This replaces the promise that no follow-up is lost, in FR-32 "Nothing is lost" and FR-46 "Boomerang pairs".

In the PRD addendum, P4 changes from "no milestones or push-outs" to "no milestones; follow-ups can still be pushed out".

### H2. Enough events every player can draw

Covers A27.

- FR-17's per-year minimum of 8 counts only events that require no flags and aren't follow-ups.
- The content check fails if seeded runs turn more than one active month per playthrough quiet for lack of an event.

## B. Balance, wellbeing and content

### B1. Example 26c at the real limits

Covers A1, E30.

- Recalculate case c with activities at the limits (stress −10, social +10 each, at most ±15 a month). Both lenses estimate about 42/46/37-38. *To verify.*
- Update the figures in FR-33, example 26c and the addendum's OQ-19 note.
- Write "activities at the effect limits, within the monthly cap" instead of "the strongest activity allowed". Each activity can only be used once a month.
- Make 26c a check that fails if the catalogue, the caps, the slot divisor or the threshold change it to 50 or above.

### B2. Goal 1 for a player who plans (D9)

Covers A2.

- FR-9: add a reference run, "a careful player with some free time": free activities, plus the cheapest paid basic activity once a month.
- Its goal 1 and goal 2 results are pass/fail in the content check.
- With placeholder prices, mark it as expected to need tuning when OQ-17 gives real prices (#48).

### B3. The hollow win and 25 h with activities

Covers A3, E22.

- A seeded wellbeing check fills every slot with the catalogue's best free activities and reports ending wellbeing for 17b at 25 h and 26 h, and for 21c.
- FR-52: "slots = the month's free time ÷ the divisor, rounded down, at least 1 and at most 4." "Never zero" then holds whatever the divisor is tuned to. Update the OQ-8 note.

### B4. Social life shown vs used (D8)

Covers A17.

- FR-33 shows "usual" (carried) and "this month" (with activities) separately.
- The rule 12 "below 20" row is explained as «Det vanlige sosiale livet ditt er under 20».
- Rule 12 is unchanged.

### B5. "Same as last month" (D12)

Covers A18.

- FR-52: "One action places last month's activities again, where they're still available. Each one is checked like any placement."
- §7.1 measures the time spent on the month plan in playtests.

### B6. Activity groups on the ending screen

Covers A21, E28, E29.

- FR-39: the group line uses the group's kroner effect from FR-42, which is its cost plus any linked card interest. It also names what the group added to wellbeing (an engine figure), so free time isn't shown as pure loss (Vision, NFR-8). D15 covers groups.
- FR-42: a single activity can't take the hollow-win entry, as it can't be ranked alone.
- FR-42: choices in the same month that tie are ordered by when the server confirmed them.

### B7. A mechanism for free time

Covers A16.

- Add "everyday spending and free time" to the glossary's fixed list. It covers the spending level, activities, D25 and D26.
- FR-17's rule about events before and after 18 applies to events only.

### B8. Free basic activities are always available

Covers E21.

- NOK 0 basic activities have no flags and cover ages 15-20.
- The content check confirms that at least two NOK 0 basic activities can be placed in every month.

### B9. Invitations only for activities the player can place

Covers E5.

- An invitation is drawn only if its activity can be placed this month (age range and flags).
- The schema check confirms that the activity's age range covers the message's.

### B10. Answer keys for the new figures

Covers A22.

Add worked examples:
- 25c: a card-paid activity (C1)
- savings-target progress, using UJ-6's month (T1, J1)
- an activity group line on the ending screen (B6)
- the "kroner left after spending" for extra shifts (FR-47, FR-56)

## R. References, structure and wording

### R1. Refer to the cut list by name

Covers A8, E32, S1, S11.

- Write "(cut list: the in-play lines)" and similar, never item numbers. This fixes FR-29, FR-38, FR-39, FR-42 and FR-57.
- In the PRD addendum, l. 278 and l. 334 become "on the cut list (PRD §4.4)".
- Give the cut list its own heading, §4.4 Cut order.

### R2. Stale text in the addenda and the glossary

Covers A8, A26.

- In the brief addendum, mark "MVP Scope Priority" and "Event Library" as "superseded on 2026-11-10 by PRD FR-17 and §4.4". They still say 50 events, 60-80, and 10 a year.
- Bump `updated:` in both addenda.
- Glossary "Content check": add activities, messages and FR-55.
- NFR-4 "Versions": add activity and message versions.

### R3. Structure (D11)

Covers S2-S15.

- **Accept:**
  - S2: move 5.13-5.15 after 5.4, and Playtest support to the end of §5.
  - S3: give the money view its own section.
  - S4: FR-53 is the one home for activity rules.
  - S5: FR-55 is the one home for the offer rule.
  - S6: condense FR-56.
  - S9: condense the V2 text.
  - S10: "UX and architecture can start" goes in §0.
  - S12: condense NFR-4's topic list.
- **S7:** retitle FR-17 "Content library", because it already holds the counts for events, activities and messages. Drop the duplicate "at least 5" from FR-53.
- **S13:** only move "Available money" to its alphabetical place. The glossary stays before §4.
- **S8** is in J4. **S11** is in R1. **S14** and **S15** are kept.
- **Order:** apply the content fixes first, then the structure moves, then the prose. Each diff stays readable that way.

### R4. Prose

Covers P1-P36 and the minor fixes.

- Accept all the rows. Start with the terms: "activity slot" and "empty" (P1), "changes" not "adds to" (P2), "story event" defined (P3), offer vs option (P7, P8), and the two proposals (P4).
- **"Consider" rows:** accept P3, P13, P28, P31 and P32. P35 is replaced by J4, and P36 is the same as O2.
- P6, P13, P14 and P34 are in J4. P7 and P18 are in O1. P15 is in T1. P29 is in M4.

## Which fix covers each finding

| Fix | Findings |
|---|---|
| J1 | A5, A6, E11 |
| J2 | A5 |
| J3 | E12 |
| J4 | A7, A25, S8, P6, P13, P14, P34, P35 |
| C1 | A4, E3 |
| C2 | A20, E4 |
| C3 | A19, E1, E2 |
| C4 | E26 |
| C5 | E31 |
| O1 | A10, E6, P7, P18 |
| O2 | A9, E27, E34, P36 |
| O3 | A11, E14, E15, E16 |
| O4 | E7, E33 |
| M1 | A15, E8 |
| M2 | A23, E17 |
| M3 | A24 |
| M4 | A14, E9, P29 |
| M5 | A15 |
| T1 | A13, E10, P15 |
| W1 | A12, E13 |
| W2 | E24, E25 |
| W3 | E23 |
| H1 | A27, E18, E19, E20, E35 |
| H2 | A27 |
| B1 | A1, E30 |
| B2 | A2 |
| B3 | A3, E22 |
| B4 | A17 |
| B5 | A18 |
| B6 | A21, E28, E29 |
| B7 | A16 |
| B8 | E21 |
| B9 | E5 |
| B10 | A22 |
| R1 | A8, E32, S1, S11 |
| R2 | A8, A26 |
| R3 | S2-S7, S9, S10, S12-S15 |
| R4 | P1-P5, P8-P12, P16, P17, P19-P28, P30-P33, minor fixes |
