---
stepsCompleted: [1, 2, 3]
inputDocuments:
  - .docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md
  - .docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/ARCHITECTURE-SPINE.md
  - .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/DESIGN.md
  - .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/EXPERIENCE.md
  - .docs/planning-artifacts/readiness-review-2026-11-23/report.md
referenceDocuments:
  - .docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/addendum.md
  - .docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md
  - .docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/SOLUTION-DESIGN.md
---

# IBE160-G13 (LifeMode) - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for IBE160-G13 (LifeMode), decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

**How to read the inventory.** Requirement IDs keep the PRD's numbering (FR-1 to FR-58, NFR-1 to NFR-11), because the architecture, UX, worked examples and issues all refer to them. Each line is a summary for planning. The PRD's "Consequences (testable)" lists hold the full acceptance detail, and stories cite them. The tier (§4.4) is given in brackets. "Rule N" is Rule Set v1 in the brief addendum. "WE N" is worked example N there.

**Not in this breakdown:** FR-35 (visible future opportunities) is left out of the MVP (#115). FR-51 (minigames, the driving game) is V2 (#51); the licences are a payment only. F5 (AI fallback) is V2 (A-26).

## Requirements Inventory

### Functional Requirements

**Account and login (PRD 5.1)**

- FR-1: Create user [Core; per-network sign-up limit can be cut]. Sign-up asks only for email, password (≥ 8 characters, configuration), nickname (2-16 characters: letters incl. æ/ø/å, digits, spaces, hyphens; trimmed) and "stay logged in". No real age. The email is typed once and shown back for checking before the user is created (WCAG 3.3.7). The player information (NFR-3) is shown before creation. An address already in use is refused with pointers to Log in and the reset link; this is the only place that reveals an address has a user. Emails match case-insensitively with outer spaces trimmed; dots and +tags are kept. Sign-ups per network are limited (default 60/h). No email is sent and no confirmation step blocks play; the player goes straight to the life goal. The nickname can be changed in settings; the server fills it into game text, and no one else sees it.
- FR-2: Log in [Core]. A failed login never reveals whether email or password was wrong. 10 failed logins for one address from one network in 15 minutes pause that address on that network for 15 minutes; other networks and the reset link are unaffected, and a school class on one network isn't blocked. A player reaches only their own game.
- FR-3: Forgotten password [Core; the daily total cap can be cut]. One-use reset link, 60 minutes (configuration); a new link cancels older ones; a used or expired link says so and offers a new one. Limits per address (1/min, 5/day) and a daily total below the relay quota; the screen always shows the same message. A reset logs out every device and leaves the game unchanged. Works locally (local inbox or log) and in the playtest, where no email is sent and the team hands out links (NFR-11).
- FR-4: Change password [Extension]. Requires the current password and the FR-1 minimum length. The old password stops working at once; other devices are logged out, this one stays; the game is unchanged.
- FR-5: Log out and staying logged in [Core; "stay logged in" and Log out on all devices can be cut]. Log out; Log out on all devices. A device logged out elsewhere can't act; its next action shows login and the game is unchanged. "Stay logged in" is unticked by default: unticked ends when the browser ends its session or after 30 minutes idle (some browsers keep the session through a restart, so the 30 minutes is the promise); ticked lasts until logout or 30 days without play (configuration).
- FR-44: Delete account [Core]. Requires the current password, after confirming; irreversible. The email address and game data are deleted, every device is logged out, an open device can't save, and the same address can sign up again.

**Saving and devices (PRD 5.2)**

- FR-6: Save every choice [Core]. A choice counts only when the server confirms it; until then the game shows it is saving, locks the other options and shows no result. After 5 s (configuration) it says it is still trying and retries on reconnect, never applying a choice twice. After a reconnect the game shows the saved choice's result, or the same event if the server never got it.
- FR-7: Nothing waits on the device [Core]. The server decides and saves every change when it happens; any device shows the same progress straight away.
- FR-8: Check for updates on opening or returning [Core]. Before accepting the next choice, the game fetches the latest progress on open, reload, login, tab return, reconnect and after idle (default 5 min). The first confirmed choice wins; the other device is refused, reloads and says the game was updated on another device. Offline: readable, options locked, nothing queued.

**Starting a life (PRD 5.3)**

- FR-9a: The goals and how they are checked [Core]. Three goals, chosen before the avatar and fixed for the playthrough: save for something big (net savings ≥ NOK 100,000), debt-free with a buffer (available money ≥ NOK 30,000 at the end of each of months 49-60 and no debt at 20, family loans and payment plans included; BSU isn't a buffer), afford a big experience (bought by the end of month 56, available money ≥ 0 at 20). Checked once after month 60 under rule 13; reaching the target exactly counts. The experience (NOK 60,000, offered in month 44, open until the end of month 56) can't be paid on credit. Borrowing never helps.
- FR-9b: Goals are reachable and earlier play matters [Core]. Targets and the experience price are configuration. Every careless run in WE 21 misses all three goals. The reference run (WE 20) reaches all three; a second reference run with free basic activities plus the cheapest paid one monthly must reach goals 1 and 2 (content check fails otherwise). Seeded runs repeat the checks with real costs under the careless and careful policies.
- FR-9c: Progress during play [Core]. Progress towards the goal, worked out the same way, including the lowest available money at a month-end from month 49 for the buffer goal; before continuing it's shown after the planned activities' payments, marked as such.
- FR-10: Create an avatar [Extension]. Picked from a small set of preset looks; nothing typed. Shown with money and wellbeing and on the ending.
- FR-11: Pengegave and first choice [Core]. NOK 10,000-30,000 drawn once when the life goal is confirmed and stored. If play stops before the first real choice, the next login resumes at the first step not done. Engine tests can fix the amount. A new player reaches the first real choice within about 2 minutes (playtest).

**Months, sessions and events (PRD 5.4)**

- FR-12: Process each month in a fixed, repeatable way [Core]. Rule 1 order (income, tax, fixed costs, everyday costs and spending, unexpected expense, instalments, card bill and debt interest, savings interest, event and choices ending with planned activities, wellbeing, December BSU deduction; rule 8 check at month end), whole kroner (rule 2). A cost started by a choice in month M is first charged in M+1. Same start state, draws and choices give the same result. Worked examples pass as unit tests (F1-F3, F7, F8). Calendar per rule 11 (start year 2026, configuration), shown as «November · 16 år · 2027». Every random result is drawn once and stored before the player sees it; a playthrough can be replayed from its stored start values, choices, applied activities and pins. Each processed month is saved at once.
- FR-49: Moving to the next month [Core]. A month opens (rule 1 up to savings interest, message draw, highlight event or quiet summary) and closes on continue (planned activities, wellbeing, rule 8 check, next month opens). Continue needs the real choice made, and in a crisis month the crisis ended; empty slots and unread messages never block. Money actions, open options and plan changes are allowed until continue. Before continuing, trigger status and goal progress after the plan's payments are shown, and a trigger asks for confirmation (special texts in months 59 and 60). Every game request names its month and stale ones are refused; continue carries the plan version. In month 60 next-month actions and previews are hidden or marked as no effect. After month 60 the ending follows, and the playthrough counts as completed once its ending is calculated.
- FR-13: Play an active month [Core]. The event with current account, savings, debt and fixed costs, and a few options; a copy in the phone if it has a sender. The result shows the change in kroner and wellbeing and why. Each option's wellbeing effect is stored and hidden until picked (#79). Unaffordable options follow FR-45. A double tap applies once.
- FR-14: Summarize a quiet month [Core]. A short summary and new messages; same money rules; money actions, offers and planning allowed; one tap to continue.
- FR-15: End a session after one in-game year [Core]. A teaser naming the next age unlock, else an open boomerang pair; from month 55 the ending at 20. Nothing locks the player out in real time.
- FR-16: Recap on return [Extension]. After login or ≥ 1 h away (configuration), the same however long the break: where they are, a teaser (FR-15 rule), messages this month, the plan. Nothing runs during a break. After the ending FR-43 applies.
- FR-17: Content library [Core; invitation activities and info messages can be cut to their minimum]. ≥ 40 regular events (target 50-60) plus about 10 crisis events; ≥ 8 eligible non-follow-up, no-flag events per in-game year; about 55 % before 18. ≥ 5 basic and 12-20 invitation activities; an offer message for every FR-18 row that has one; ≥ 6 invitations per in-game year. Fixed schemas (PRD addendum) checked automatically, including LK20 codes valid from 1 Aug 2026 and an LK20 coverage report. ≥ 8 boomerang pairs and ≥ 3 follow-ups per seeded playthrough on average; every mechanism has events before and after 18 where its rules allow. Every regular event has a free option; every crisis event offers asking family and ignoring. ≥ half of pre-18 events have two free options (reported from a NOK 0 run). Playable end to end with zero AI calls (F6).
- FR-58: Content check [Core]. Runs in CI on every PR. Hard gates: schema and fixed-list names; library minimums; boomerang and mechanism coverage; open options identical across message, money view and job view; ≤ 1 active month per seeded run with no eligible event; ≤ 2 months a year with no eligible invitation; replay variety (FR-43); no hollow-win run at ≥ 50 (FR-33); second reference run reaches goals 1 and 2. Reports: free-option share at NOK 0, LK20 coverage, drawn events left per year, dropped follow-ups, ending wellbeing at 1-4 slots, invitations per year, WE 17b boundary runs and careless run 21c. Until tuning is frozen only the schema gate and the open-option gate fail; the rest warn.
- FR-46a: Active months and pace [Core]. The same active months every year (default 4: Jan, Apr, Jul, Oct; configuration); months 59-60 quiet unless a crisis, card warning or pushed-out follow-up takes them. Month 1 is always the pengegave choice. A card warning makes a quiet month active. A session fits 10-15 minutes on a phone.
- FR-46b: Which event an active month gets [Core; events can be cut to 40]. Eligible events: age in range, required flags set, no blocking flags, not seen this playthrough. Drawn uniformly and stored. No regular event repeats; crisis events and the card warning can. No eligible event makes the month quiet (CI fails if it happens more than once per seeded run). The car-licence draw runs in month 37 and arrives as a message.
- FR-46c: Follow-ups and collisions [Core]. A boomerang follow-up is due after a delay drawn from its pair's range and takes the first active month at or after that; an opener is drawable only if its longest delay lands by the last active month; a follow-up whose flag was cleared is dropped. Collision order: crisis, card warning, follow-ups in due order, drawn event. A pushed-out follow-up takes the next active month or makes month 59 or 60 active; if none is left it's dropped and reported.
- FR-18: Unlock options by age [Core]. The FR-18 table (savings and BSU from month 1; part-time job month 3; moped licence month 13; owning a moped with a licence; part-time up to 40 h from 19; summer jobs offered 18/30/42, paid 19/31/43; car licence draw and paid licence 37; credit card 37, offered 39; consumer loan 37, offered 49; the experience 44-56; full-time job offered 54, starts 55). No offer before its month; the engine refuses options not yet open. Teasers and recaps use the table. Only age unlocks.
- FR-48: Options that stay open [Core]. Moped licence, buying a moped, the paid car licence, credit card, consumer loan, part- or full-time job and the experience stay open until taken, from the offer message, the money view or the job view, as the same option everywhere (content check). Can't pay yet: the missing amount shows and the option stays open (test: NOK 8,000 saved in month 13, bought after the summer job in month 19). Blocked for another reason: shows what's missing and is refused. Declining or quitting a job allows another later. Dated offers (summer job until that July's income step; the experience until the end of month 56) then show as expired. Taking one is a choice (cause links) but not the month's real choice. Gifts and family help aren't open options. One-at-a-time table (#83): licences and the experience once per playthrough (paid car licence never after the gift); one moped at a time; one credit card per playthrough; one consumer loan at a time; one job at a time. Family loans and payment plans are also one at a time.
- FR-19: Tips in events and offers [Extension]. General, pre-written, ignorable, no game effect, never personal advice. Credit card and consumer loan offer messages always carry a tip, a teaching point and the engine's cost in kroner.

**Month plan and activities (PRD 5.5)**

- FR-52: Month plan and activity slots [Core]. Slots = month's free time ÷ 20, rounded down, 1-4 (divisor and maximum are configuration), fixed when the month opens. Empty slots have no effect and never block continue. A one-off shift takes a slot. School and work show as fixed blocks; plans don't carry over; "same as last month" re-places last month's activities with normal checks. No days or times (D26). The plan's total is the engine's and covers activity costs only. The content check reports ending wellbeing at 1-4 slots.
- FR-53: Activities [Core with the basic activities; invitation activities can be cut to their minimum]. One slot each, a cost ≥ 0, card-payable flag, stress and social effects within ±10, age range, flags, mechanism, kind and a price source. ≥ 2 free basic activities for ages 15-20. Invitation activities only in their invitation's month. At most once a month. Planning moves no money; an unaffordable activity shows the missing amount and can't be placed; removal is free. On continue, activities apply in slot order at the end of the choice step, rechecked for eligibility and payment (FR-45); failures drop with a note (WE 25). A card blocked by a payment plan can't pay. Costs come on top of spending. Effects count for that month's score only, ≤ ±15 per part per month (configuration). An applied activity is a choice with a cause link, not the real choice. Plannable in crisis months. No earnings.

**Phone and messages (PRD 5.6)**

- FR-54: Phone and messages [Core]. An inbox of pre-written Norwegian messages from friends, family, employer and bank: info, invitation (makes an activity available this month) or offer (open option, extra shifts, hours answer, one-time gift; may carry a tip). The highlight event's copy goes in the phone when it has a sender, needs no answer and isn't counted. No quiz answers: an invitation is accepted by placing its activity, an offer by taking it. Drawn offers expire after their month, dated offers after their last day. The nickname is filled in by the server; figures are the engine's. This month's messages are marked new; earlier ones stay readable; no unread badges across months. Reading changes nothing and isn't stored.
- FR-55: Which messages arrive [Core]. Decided at month open in the same selection step as the event, and stored. Drawn (invitations, info, drawn offers) vs triggered (bank messages, other offers). Eligibility by age range and flags; an invitation only if its activity is eligible; payment isn't checked; one-off messages never repeat. Bank messages at 25/50/75/100 % of the savings target or goal 1, once per threshold per target, only the highest per month; one savings-interest message the first month interest passes NOK 50. Every FR-18 offer and the car-licence result always arrive in their month (not if already taken, closed, or blocked by one-at-a-time). Drawn offers (extra shifts, gift moped) have flags and a yearly chance and can be taken only that month. Hours answers arrive next month and don't count. At most 3 new messages a month; offers and the event copy always arrive and don't count; fill order bank, invitations, info; a bank message that doesn't fit comes next month. 0-2 invitations a month, each at most once per in-game year.

**Job view (PRD 5.7)**

- FR-56: Job view [Core]. Workplace and role (flavour), hourly rate for the age (Virke/HK), weekly hours and this month's hours with extra and one-off shifts, the rule 10 limit, expected monthly pay, current offers. Actions: answer an hours offer, ask for more or fewer hours, quit, take a job offer, take or end extra shifts; one-off shifts listed here and placed from the plan. Each action previews kroner left after spending and next month's slots. With no job: open job offers or when the next unlocks.

**Money view (PRD 5.8)**

- FR-57: Savings target, upcoming costs and activity spend [Can be cut]. Pin one priced option (even unopened; one of two prices); pinning moves no money and isn't a choice. Progress = current account + savings against the price, at most 100 %, engine-calculated, shown after the plan's payments before continuing. Cleared with a note when taken, given or closed. Upcoming costs: next month's known fixed and everyday costs and instalments; the card as its current balance; empty in month 60. Activity spend: this year's applied activities by kind.

**Money (PRD 5.9)**

- FR-45: Accounts and paying for choices [Core]. Current account, savings and an optional BSU. Savings cover what the current account can't, BSU never; each transfer appears in the month summary. Options are pickable only if payable from current account + savings, or the card when card use is on and it fits under the limit; otherwise the missing amount shows. Tax, fixed and everyday costs, consumer-loan and payment-plan instalments and unexpected expenses are always charged, even below NOK 0; card payments, family-loan instalments and spending never take the account below 0, and spending never draws on savings. A negative balance has no interest, can't pay for choices and is paid first by the next income. Money actions (any month, money view): transfers, BSU deposit and full withdrawal, card use on/off, card payment mode, extra card payment, early payoff of loans and payment plans, spending level, stopping an everyday cost without a binding period, hours actions, selling the moped. The FR-45 payment-order table is the one rule for how each payment kind is paid. Activities are paid like event options, at continue, never split between card and accounts (WE 27).
- FR-20: Wages [Core]. Hourly wages at the Virke/HK rate for the age from part-time and summer jobs, and a full-time job from month 55. A summer job at 16, 120 h at NOK 139.40, pays NOK 16,728 with no tax (WE 1, F7).
- FR-47: Working hours [Core]. At most one part- or full-time job plus a July summer job; quit any month; every change applies from the next month. Pay = weekly hours × 52/12 × rate, whole kroner, ≤ 173 h a month. Weekly limit 12 h (months 1-18) and 40 h (from 19), checked against the month a change applies from. A summer job shares the 173 h cap and is cut at July's income step (WE: 30 h part-time cuts 120 h to 43 h); it can't be taken at 0 h left; the player is warned before a change would cut it; cut to 0 it's cancelled with a note. Full-time is 37.5 h, raisable to 40. Hours requests: one at a time, answered next month with ±2 h (configuration; floor 4 h) or a no with the reason; the offer lapses at month end. One-off shifts: listed in the job view and the plan's picker; each takes a slot; pay = hours × the rate at the age in the month worked, rounded once when placed, paid and taxed with next month's wage (#114); none in month 60; within rule 10 and 173 h; no wellbeing effect of its own. Extra shifts: +4 h for 3 months by default, from the next month, offered only to a player with a job, below the limit, with none running and a later income step left; endable from the job view; quitting ends them. Weekly hours and extra shifts never take a slot. Every hours offer previews slots and warns below 50 free time.
- FR-21: Tax [Core]. On the calendar year's wage income at 2026 rates (rule 3); each in-game year is a tax year. NOK 110,000 at 18 pays NOK 2,588, all trygdeavgift (WE 5, F8). Trygdeavgift 5.1 % in years 1-2 and 7.6 % from year 3. The December summary shows the year's tax and the expected BSU deduction, paid on continue.
- FR-22: Saving and BSU [Core]. Savings 2.87 %, BSU 5.61 %, interest under rule 2. NOK 10,000 for 12 months gives NOK 10,289 (WE 2, F2). With no tax, the BSU deduction is plainly NOK 0, and BSU still pays through interest (WE 6). Small interest is shown as it is. BSU deposits are capped at NOK 27,500 per calendar year; a larger deposit is cut to fit and the remaining cap shown. BSU can't pay for anything. A full withdrawal closes the BSU for the playthrough and claws back deductions received.
- FR-23: Fixed and everyday costs [Core; car fuel can be cut with the car licence]. From 18 the player pays mobile and transport. Spending level low 60 %, normal 75 % (default), high 95 % of wage after tax, on top of costs, never more than the current account holds, never from savings, nothing with no wage; changes apply next month. Low −2 and high +2 social in a month with spending; high gives nothing in a month with debt interest. The month summary shows total spending with pre-written example purchases that have no amounts and never name an activity kind. Transport is the ticket, or moped insurance and fuel while a moped is owned, never both; with a car licence the player can start or stop borrowing the car (fuel). A player with no job who keeps NOK 10,000 saved never goes below 0 before 18 (WE 15). Event options can start, change or stop everyday costs, some with binding periods. With card use on, card-payable costs go on the card first. A payment plan turns card use off.
- FR-24: Unexpected expenses [Core]. One per in-game year by default, in a drawn month, of a kind that fits; tied to an owned item only while owned; stored with a system cause; a deduction, not an event; may start a crisis via rule 8.
- FR-25: Consumer loans [Extension]. From 18 with a steady wage; not in months 59-60. Annuity at 15 % (rule 4); NOK 20,000 over 12 months: NOK 1,805 monthly, final NOK 1,808, NOK 21,663 total (WE 3, F1). Amount NOK 5,000 to 3× the 3-month average wage minus other debt (family loans excluded), rounded down to NOK 1,000, picked in steps of NOK 1,000 (amounts outside the range or the step are NFR-7 refusals); terms 12/24/36 (configuration) with the engine's quote for each before taking. One at a time; early payoff free; may run past 20 and then counts as debt.
- FR-26: Credit card [Core]. From 18 with a steady wage; stays open if the wage stops. Limit fixed per playthrough (default NOK 10,000). Payment mode chosen when taking the card: whole balance, minimum, or a fixed amount ≥ the minimum in steps of NOK 100; changes apply from the next bill. The bill is paid at the debt step, never below 0; paying less than the minimum is a missed minimum and leaves an overdue amount paid first later. Extra payments lower the balance at once. NOK 3,200 at minimum-only is paid off after 13 months, NOK 3,606 in total (WE 4, F3). With card use on, purchases and card-payable costs go on the card if they fit; an event purchase that doesn't fit is paid from the accounts and the game says the card was declined. Card use can be turned off any time. Above the limit (from interest) no purchases. Shows this month's interest and the minimum-only total cost in kroner.
- FR-27: Help from family [Core]. Whether family can help, and how much, is drawn once per event or crisis month and stored; asking again shows the same answer, moves no money and uses no crisis step. Family loans are 0 %, equal instalments with the last one making the total exact (NOK 5,000 / 6 = 833 × 5 + 835, WE 8). An instalment the accounts can't cover moves to the end and raises stress (≤ 50); never below 0; what's left at 20 is debt. One family loan at a time, from 15. Family loans don't count in the debt trigger.

**Moped and licences (PRD 5.10)**

- FR-28: Moped licence [Core, payment only]. From 16, paid at real, sourced and dated prices (lessons, mandatory course, licence); the player has it once paid. The recap teaser names its cost.
- FR-29: Own a moped [Core for buying; gift mopeds and the parents' insurance share can be cut]. One moped, only with the licence. A gift offer (used moped) comes as a drawn offer only to a licence holder with no moped, at most once per playthrough. Resale value starts at the price paid (or the used price), falls 15 % of it a year, monthly, floor 20 % (rule 14; WE 19: NOK 8,152 after two years). Insurance (flat NOK 3,000/year in the MVP) and fuel only while owned; moped repairs and events only while owned; the parents' share of insurance drawn once and stored. Sell any month at the current value; public transport returns next month; the moped leaves the room.
- FR-30: Car licence [Can be cut]. In month 37 the engine draws once whether the parents give it, and one family message says so. The gift applies at once and costs nothing; otherwise the player can pay a real, sourced price (payment only), and is never offered the paid licence after a gift. With a licence the player can borrow the parents' car, which costs fuel while borrowing and opens car events. Gift frequency is configuration.

**Warnings and crises (PRD 5.11)**

- FR-31: Card warning [Core]. Each time a bill isn't paid in full after a month with a bill paid in full or no balance: an event in that month, before the next interest charge, showing this month's interest, the balance, and minimum-only time and total cost, and whether the player couldn't pay or chose to pay less. It doesn't start a crisis. If chosen, one option switches to paying the whole balance; other options only when possible. In a crisis month the crisis shows its figures first and the warning counts as shown. Test: WE 7 (NOK 6,000 bill, NOK 4,000 available, NOK 113 interest).
- FR-32a: Crisis triggers and start [Core]. Rule 8 checked at the end of every month: current account < 0; card minimum missed two months in a row; net debt (excluding family loans, minus savings and a positive current account) above the larger of 3× the 3-month average wage and NOK 5,000. A true trigger with no cooldown makes the next month a crisis month (F4: one test per trigger). Rechecked when the crisis month opens: if none is true it's skipped with a note, no stress, no cooldown, and the month's event is re-chosen (WE 10). One crisis however many triggers; its event follows the most urgent (below zero, missed minimum, debt) and names all. Two-month cooldown (configuration), except month 60; triggers during a cooldown are still shown.
- FR-32b: Crisis events, steps and options [Core]. About 10 crisis events, each for one trigger and age range, covering every trigger possible at each age (before 18 only below-zero). Drawn among those that fit, preferring the one seen longest ago, stored. Up to three steps; each offers only options possible then (selling needs something to sell, extra shifts need a job and hours left, etc.); asking family and ignoring always offered; options landing after month 60 hidden; each says when it lands. Payment plan: card balance to a 12-month annuity at the card's rate, card blocked until paid (rule 15, WE 12), instalment shown against what's left monthly. Money actions and open options stay available and use no step; triggers rechecked after them. Money arriving goes first to a negative current account, then overdue minimums. Activities plannable and use no step.
- FR-32c: How a crisis month ends [Core]. Triggers rechecked after each step; ends when none is true, when the player ignores it, or after the third step. A crisis never ends the game before 20; ignored debt keeps growing and starts new crises after each cooldown.

**Wellbeing and the room (PRD 5.12)**

- FR-33: Wellbeing [Core]. One score 0-100 from stress, free time and social life, weighted by the life goal (rule 12). Activities change stress and social life for that month only. Each part and the score stay 0-100. Status bands (#111): below the threshold bad, threshold to +9 ok, +10 and up good; stress mirrored (100 − stress); offset is configuration. Every event choice has a stored effect, hidden until picked. Hollow win holds: the 26c money chaser ends at 42/46/37 (goals 1/2/3), and CI fails if any reaches ≥ 50. Usual vs this-month values shown for stress and social life. Ending wellbeing = average of months 19-60, rounded. Shows score, parts, threshold and, from month 19, the average so far. Weights, start values, monthly changes and threshold are configuration.
- FR-34: Room layers [Core with 3 layers; more can be cut]. One room that changes right after a choice; ≤ 6 layers, one per belonging, each with a few states, always showing the current state of every belonging; driven by flags so it's identical after reload and on every device; each state has a short text alternative.

**Explaining consequences (PRD 5.13)**

- FR-36: Cause links [Core]. Every effect stores its cause: a choice in the playthrough or a system cause (F10). Shared causes are stored with whole-kroner shares that sum to the effect (interest split in proportion to balance parts). Continuing effects link to the original choice (moped costs, subscriptions, card interest on a purchase). Wages, tax, mobile, unexpected expenses and spending have system causes. Wellbeing changes link to the option or rule behind them; an activity's cost and effects link to the activity.
- FR-37: Echo badges [Extension]. Shown only on effects with a cause link to an earlier choice; carries text naming that choice for screen readers.
- FR-38: "Hvorfor?" [Core; the BSU comparison can be cut with the in-play lines]. Explains a change from its cause links; system causes from the rules; shared causes list up to the three largest shares and sum the rest.
- FR-39: "If you had chosen differently" [Core on the ending screen; in-play lines can be cut]. Compares the chosen option with the option in the same event whose direct kroner effect differs most (ties to the first listed). Debt: the interest linked to the choice. Otherwise: the difference grown with savings interest to the 20th birthday. Otherwise: a pre-written text plus the stored wellbeing difference. Activity groups on the ending: their cost grown with interest plus linked card interest, and their summed wellbeing effect (WE 28). Never re-runs months; never AI.
- FR-40: Disclosed simplifications [Extension, aimed to build: A-23 and SM-2 need it]. Each disclosure (D1-D26) is shown the first time its mechanism or feature appears, then lives behind an info icon or "Hvorfor?"; all collected on «Om tallene». Seen once per account, across devices and playthroughs.

**Ending and replay (PRD 5.14)**

- FR-41: Four endings [Core]. Checked after month 60 in order: loss (a trigger true at the end of month 59 is still true at the end of month 60), real win (goal reached and ending wellbeing ≥ threshold), hollow win (goal reached, below threshold), goal not reached (never framed as failure, with general advice). Exactly one valid ending screen per end state (F9: one test per combination plus both boundaries). Calculated from measurable state, no AI. Exact threshold and exact target count as reached (WE 18). A trigger true at the end of 59 makes month 60 a crisis month even in a cooldown; a trigger first true at the end of 60 isn't a loss and is named. WE 11: minimum missed in 58 and 59 and paid in 60 is not a loss.
- FR-42: Ending summary [Core; grouped activities can be cut]. How the life went and the three choices with the largest kroner effect (sum of linked money effects; internal transfers, loans and repayments count zero, interest counts; belongings unvalued, sales count when made). Ties: earliest by month, then confirmation order. Activities of the same kind rank as one group (never one activity alone). Fewer than three if fewer have an effect. Each opens to the FR-39 line and a pre-written tip or explanation. A hollow win includes the choice that hurt wellbeing most (taking third place if needed), or the largest system cause if no choice lowered it. Only shown choices open.
- FR-43: Play again [Core]. A new life from 15 with a new goal and pengegave; nothing carries over except seen disclosures. No crossroads replay. Different choices give different stories: random-choice pairs share ≤ 2/3 of regular events on average, and same-seed pairs with different choices differ in at least one follow-up (content check). One life in progress per account. Starting over before 20 from the menu, after confirming; the ended life can't be resumed and is deleted when the new one starts or the account is deleted. A finished life is kept read-only until then; a returning player sees its ending summary with Play again instead of a recap.

**Playtest support (PRD 5.16)**

- FR-50: Playtest records [Core]. In the playtest environment only (off by default and in the examiner's run; a test covers both), a small per-account record for §7.1: time to first choice, session lengths, play days, highest month per playthrough, completed playthroughs with ending, goal and net savings, playing again, starting over, months with applied activities, months whose activities differ from the previous month, plan time, and invitations whose activity was applied. No choices or game content. Time is measured on the server (gaps > 10 min don't count). Records survive playthrough deletion, are deleted with the account (only an anonymous "testers left" count remains), are exported with tester codes (loaded by a command into a separate table and resolved at export) and never hold email or nickname. Test accounts are excluded.

### NonFunctional Requirements

- NFR-1: Platform and every screen size. A browser web app, no install, not a PWA, no offline mode. Mobile-first, adapts from 320 CSS px to desktop with no horizontal scroll, touch-friendly controls, nothing core on hover only, readable text. Browsers: the two newest versions of Safari, Chrome, Edge and Firefox. Verified on Safari/iPhone, Chrome/Android, a tablet and Chrome or Edge on Windows, creating a user through to the ending; the automated e2e run covers Chromium, WebKit and Firefox.
- NFR-2: Accessibility. WCAG 2.2 AA: contrast, keyboard navigation, text alternatives, labels, clear errors, targets ≥ 24 × 24 px (options 44 × 44 where possible). Every picture also as text (room states, moped, echo badges, wellbeing parts); nothing by colour alone (amounts have a sign and a word); "saved", "offline" and the card warning announced; password managers and paste work; the main flow is keyboard-only playable; the plan never needs dragging (2.5.7) and each slot's state is text; new messages announced without interrupting. Verified by an automated check with no serious or critical findings on the main screens, plus a manual keyboard and phone screen-reader test before each playtest.
- NFR-3: Privacy and data minimization. Email, password and nickname are the only inputs; nickname, game data and network addresses count as personal data. Email only for login and reset, never shown or used for marketing. Passwords only as a hash. Email, password and nickname never in the game's logs. Nickname shown only to the player. Player reaches only their data and can delete it. Player information in plain Norwegian before sign-up (what, why, how long, how to delete, which services: frontend and proxy host, backend and database host, any email relay), also reachable in the game. Accounts deleted after 12 months without play (configuration; not promised if the job is cut). No analytics, ads, tracking or third-party loads. Only the current or last finished/ended playthrough is kept. Playtest: only 18-20-year-olds, random tester codes, exports by code, the email-code list stored separately; lists, records and playtest accounts deleted after the analysis, no later than the December delivery.
- NFR-4: Correct, explainable figures. The backend engine decides every financial result and critical state; the frontend never calculates them. Rule Set v1, real 2026 values, fixed per playthrough (D6); every figure is configuration with source and date, never hard-coded. Worked examples are the answer key and run against their own frozen copy of the figures; the key changes only after a second, independent calculation (Dahl decides). Exact arithmetic (Decimal or øre, never float), so rule 2's half-up rounding is stable (WE 19: 8,151.5 → 8,152). Each playthrough keeps the config and library version it started with; cause links point to the version the player saw; text-only corrections may apply to running playthroughs.
- NFR-5: Low cost. The examiner's local run costs nothing. The hosted playtest may cost a little while it exists (sprint-1 spike to end of analysis, about two months); nothing keeps costing afterwards.
- NFR-6: Runs from the README. An examiner runs the full app on a clean machine with Docker only, following only the README, in about 15-20 minutes, with one command and no team keys or secrets (local stand-ins for every external service). Password reset works locally (local inbox or log, or an automated test the README points to). `.env.example` in the repo. Seeded test users at useful states (just before 18 with a steady wage; in debt with a crisis due; month 59 close to each ending), each made by scripted play from month 1 with stored choices, never by writing state.
- NFR-7: Robust against wrong input. The device sends only inputs; the server ignores anything else and refuses the listed cases (turn and month; options and offers; money, credit and work; belongings; month plan and activities; access and format). Five non-refusal cases have their own tests (BSU deposit cut to cap; summer job cut to cap; summer job cancelled at 0 h; card purchase over the limit paid from accounts; planned activity dropped at continue). A refusal leaves the game unchanged, returns the current progress and shows a short Norwegian message. A repeated request applies once and returns the same result. Each case has an automated test. Refusals are logged without email or password.
- NFR-8: Tone and content. Player-facing text in plain Norwegian a 15-year-old understands. Tips sound like tips; warnings, crises and endings state the consequence without scolding; "goal not reached" never framed as failure. Options read as actions, never quiz answers; free time is never wasted money. Grown-up visual style. Credit and BSU explained more. Age-appropriate; chance-based purchases shown as a cost. No tobacco or alcohol, not even in parties or concerts. Fictional senders who sound like themselves; family never gives personal financial advice.
- NFR-9: Automated tests. Engine tests (worked examples and F1-F10 as amended), the NFR-7 refusal tests, the content check and the automated accessibility check run from the README and in GitHub Actions on every PR. Manual test results (NFR-1, NFR-2) and aggregated playtest results are kept in the repo.
- NFR-10: Responsiveness. After picking an option the result shows within 1 s for 9 of 10 choices and within 3 s for all; the same for a quiet-month summary and placing or removing an activity. First visit usable within 3 s. If the server was asleep, a loading message within 1 s and usable within 10 s. Measured on a mid-range phone on throttled 4G against the playtest environment.
- NFR-11: Playtest environment. One hosted environment, the same version as the local run, low cost only while it exists, available for the whole test (≥ 3 days). Player data in the EU/EEA; host platform logs outside it are disclosed (Railway US 90 days, Vercel 1 hour). A daily automated login check alerts the team. Password reset without email: the team creates one-time links with a backend command; the relay is built in but off. The architecture names provider, tier and limits.

### Additional Requirements

**Starter template and scaffold (affects Epic 1, Story 1)**

- No starter template is named. The project is greenfield: the repo holds only planning documents today. The architecture's Structural Seed is the scaffold: `backend/` (`app/` with `main.py`, `settings.py`, `engine/`, `content/`, `persistence/`, `api/`, `auth/`, `email/`, `jobs/`, `cli.py`; `migrations/`; `tests/`; `Dockerfile` built from the repo root), `content/` (`config/v1/`, `config/test-v1/`, `config/backfill.yaml`, `library/v1/` with its subfolders), `infra/` (Caddyfile, Caddy Dockerfile with the origin-secret guard), `.github/workflows/` (`ci.yml`, `daily-check.yml`), `.railway/railway.ts`, `compose.yaml`, `.env.example`, committed `openapi.json`, `README.md`, and `frontend/` (`src/app/`, `src/api/` with `config.ts`, `src/components/` with `ui/`, `src/styles/tokens.css`, `src/fonts/`, `src/test/fixtures/`, `e2e/` with `manual-checks.md`, `scripts/`, `vercel.json`, `Dockerfile`, `package.json` + `package-lock.json`). The group builds the frontend too (since 2026-11-23).
- Stack pins: Python 3.12, uv with committed `uv.lock` and `--locked` installs, FastAPI 0.165.x + Uvicorn, Pydantic 2 + pydantic-settings, SQLAlchemy 2.1.x async + asyncpg 0.32.x, Alembic 1.20.x, PyJWT 2.x, bcrypt 5.x, Jinja2, resend[async], PostgreSQL 17, Caddy 2.11.x (≥ 2.11.8), Docker Compose plugin, Railway Hobby (EU West), Supabase Free Postgres (Frankfurt), Resend Free (off until go-live).
- Frontend stack pins: Node 24 LTS (`engines.node: "24.x"`), npm with committed `package-lock.json` and `npm ci`, Next.js 16.4.x (≥ 16.4.5) App Router with `output: 'standalone'` and Cache Components off, React 19, TypeScript 5.9.x `strict`, openapi-typescript 7.x + openapi-fetch, Vitest 5.x + Testing Library on jsdom, Playwright 1.65.x + @axe-core/playwright, ESLint 9.x, Prettier, stylelint; Vercel Hobby (Root Directory `frontend`, `fra1`, production branch `playtest`).

**Architecture decisions (ARCHITECTURE-SPINE AD-1 to AD-20; frontend AD-17 to AD-20 added 2026-11-23, #122)**

- AD-1 Pure engine: every financial result, wellbeing value, unlock, crisis check and ending is computed in `backend/app/engine/`, which imports none of sqlalchemy, fastapi, httpx, random, secrets, time, os (import-linter with external packages counted) and no wall-clock datetime calls (ruff banned-api). The engine owns the content model. A CI import-boundary check enforces the layer diagram.
- AD-2 Server decides: requests carry only the NFR-7 inputs plus protocol fields; unknown fields ignored, missing or wrongly typed refused (JSON null and omitted tested separately); no state change on GET; only `POST /api/game/actions` is auto-retried with the same `request_id`; the "continue anyway" confirmation is client-side only.
- AD-3 Postgres is storage only: no rules in SQL; Supabase used as Postgres only (Data API off; RLS on with no policies, set by one Alembic helper; CI test fails on any table without RLS); one SQLAlchemy `Base`; Alembic is the only schema path; CI fails on more than one head.
- AD-4 One mutation pipeline: every state-changing game request is `POST /api/game/actions` `{request_id, playthrough_id, month, action}` with `action` a discriminated union of the engine's action models, validated strictly in JSON mode (`TypeAdapter(GameRequest).validate_json`); `GET /api/game` returns the player view; read-only `GET /api/game/quote`. Idempotency via `request_id` in `action_log`; `409 game_changed`, `409 plan_changed` (`plan_version` on continue). Fixed lock order users → sessions → playthrough → playtest record. Life requests (start, end early, play again) in the same pipeline. Continue = one engine action closing M and opening M+1 (`apply_plan`, December step, rule 8, `close_month`, then ending or `open_month(M+1)`); the view computes after-the-plan figures on a copy; no read path opens a month. One AsyncSession per request; refusals before the first write; `action_log` insert last.
- AD-5 Snapshot plus append-only log: one `playthroughs` row per user with indexed columns copied from the JSONB state (the document is the authority), `state_schema` with in-memory upgrades on load (read paths never write), `action_log` rows never updated or deleted while the playthrough exists, `model_dump(mode="json")` with Decimals as strings (round-trip test). Per-account data that survives a new life (seen disclosures) in its own table.
- AD-6 Determinism and exact money: one seed per playthrough from `secrets`; every draw from `(seed, month, draw key)` via SHA-256 in `engine/draws.py`; collections sorted by content id; each drawn result has one owner and is stored in the draw store; tests pre-fill the draw store. Money is `int` kroner everywhere; rates, wages and hours are `Decimal` (quoted strings in YAML; the loader fails on floats); one rule 2 rounding function at the named points only; no float in game arithmetic; replay checks only on logs from the same build.
- AD-7 Content as versioned, frozen YAML: `content/config/vN/` and `content/library/vN/` (events, activities, messages, room, shifts, options, expenses, texts, lists.yaml), one YAML file per item. Manifests with fingerprints over non-text fields and `frozen: true|false`; new playthroughs pin the newest frozen library and its config (newest library in local/ci and pre-freeze playtest). While unfrozen only the schema and open-option gates fail; the schema gate also fails game text that writes a four-digit year or a month name. After freeze: text-only edits, fingerprint gate, every FR-58 gate fails, mechanics changes need a new version folder, no folder deleted. `cli clear-game-data` once when v1 freezes. All versions loaded and fingerprint-checked at startup; `backfill.yaml` for fields added after a freeze. Worked examples read only `config/test-vN/`.
- AD-8 One selection step: one engine unit decides the event, the messages (incl. hours answers) and the month's one-off shifts at month open; drawn and triggered items merged under FR-55's cap and order; stored in the state.
- AD-9 One ledger: every balance change goes through `engine/ledger.py` (`pay()` implements the FR-45 table, `transfer()`, `receive()`); every call carries a cause and updates per-cause parts (proportional interest, proportional payments, largest-remainder rounding); choice ids are a state sequence number; per-choice money and wellbeing totals for FR-42; flow classes `in`/`out`/`tax`/`interest`/`internal` with parts (#116); month totals written only by the ledger, closed by `close_month(M)` and read by every surface; a reconciliation test for every month of every worked example, seed run and replay.
- AD-10 Own login with revocable sessions: email normalized by one function; password `bcrypt(base64(sha256(pw)))`, 8-128 characters; `sessions` rows are the authority behind an HS256 JWT (`sid`, `exp`) in an httpOnly, SameSite=Lax cookie (Secure outside local/ci); sliding expiry at most once a minute with cookie re-issue; only the auth dependency writes `users.last_active_at`; the client never calls the API from a timer, except AD-18's retries of a pending action. Revocation per FR-3/4/5/44; a completed reset logs this device in. Attempt limits in `auth_attempts` keyed by HMAC-SHA256 address and network keys (IPv4 or IPv6 /64), unknown addresses do the same work, only sign-up and login answer 429, the reset cap follows Resend's UTC day. Client address only from `X-Client-IP` set by Caddy (`CADDY_MODE`); Vercel/Railway header choice and the route-handler fallback are verified in the spike. Reset links stored as SHA-256, one function for endpoint and CLI.
- AD-11 Email through one module: Resend when keyed; local stand-in (`[email:mock]` in the backend log) in local/ci without a key; null sender in the playtest; one Jinja2 template; the CLI prints playtest reset links without logging addresses.
- AD-12 One origin: playtest frontend is Next.js on Vercel Hobby (`fra1`), proxying `/api/(.*)` via `vercel.json` to Caddy on Railway with `x-origin-secret` set from `ORIGIN_SECRET`, rewrite caching off; Next.js server code never calls `/api`; `Cache-Control: no-store` on every API response; no CORS. Caddy is the only way into the backend in every environment (403 `origin_refused` without the secret, 503 `unavailable`); `/docs` only in local/ci. Locally Caddy serves the frontend and the API on one origin. Reset link `{PUBLIC_BASE_URL}/nytt-passord#token=…`. The player information page `/personvern` is a static frontend page reachable before sign-up, with NFR-3's list of contents. `vercel.json`: route `env: ["ORIGIN_SECRET"]`, `regions: ["fra1"]`; previews get 403 on `/api`; `next.config` has no `/api` rewrites, redirects or headers. Locally Caddy's frontend upstream can point at a host `next dev`.
- AD-13 API contract, player view and errors: the generated OpenAPI schema is committed and CI fails if stale. One engine `view(state, content, last_action_at, seen_disclosure_ids, nickname)` builds every response's player view and leaves out the seed, future schedule data and unpicked wellbeing effects (tested). Results are stored in the state as ids, integers, cause links and text parameters; the envelope's `result` is a reference `{result_id, replayed}`. The no-playthrough, ended and completed views carry the start screens. Every route declares its error responses with the shared envelope model. Identity `playthrough_id` + `state_version`; envelope `{result?, state, server_time, recap_threshold, client_times}` (saving-notice and idle times from settings). The backend renders all game text with one formatting function (NBSP group separator, U+2212 minus, «kr»); parameters captured when items enter the state; nickname and month placeholder resolved at view time; the frontend owns only UI chrome text. Derived figures in the view: wellbeing `{value, band}`, calendar (year, month, age from `start_year`), money per month (twelve entries, year so far, expected BSU deduction), trigger status, offer previews, slot counts, message `new` flags, loan quotes for 12/24/36 months, `pending` (`none`, `setup_avatar`, `setup_gift`, `event`, `crisis_step`), `year_end`, `continue_warning` (`none`, `trigger`, `month_59`, `month_60`) with its text, a `crisis_skipped` result entry, `min`/`max`/`step` on every amount action, room-layer state ids, the scene's text alternative and marker text; the place action's `slot` is optional (engine picks the first free evening). The frontend owns chrome text and form error texts, pre-validates only `required` and `type=email`, and formats only typed amounts through one `formatKroner(int)`. Errors: one `AppError(code, status)` and one envelope `{code, message, state?, fields?}` with the status table (401, 403, 404, 409, 410, 422, 429, 500, 503).
- AD-14 Environments and operations: one backend image; all settings in `settings.py` (pydantic-settings), listed in `.env.example`; `APP_ENV` (`local | ci | playtest`) required; secrets ≥ 32 bytes and no placeholders outside local/ci; one Uvicorn worker. `python -m app.cli schema upgrade` before start (Railway pre-deploy in `.railway/railway.ts`; compose entrypoint), then `cli seed --if-empty` locally; seeding refused outside local/ci; seeded users made by scripted play through the pipeline and asserted in CI. `DATABASE_URL` normalized for asyncpg; Supabase session pooler, pool 5 with no overflow, NullPool for Alembic/CLI. Railway Hobby EU West with sleeping off; Supabase Free Frankfurt; Vercel Hobby `fra1`; deploy from a `playtest` branch; usage alert USD 6, hard limit USD 10; delete everything after the analysis. Ops commands via `railway run`. Sprint-1 hosting spike verifies the AD-3/10/12/14 assumptions (#92). During the playtest `openapi.json` changes only add, and the backend deploys before the frontend. The `ci` environment raises the auth limits for Playwright.
- AD-15 Playtest data stays separate: everything playtest-only gated by `PLAYTEST_RECORDS` (default off); `records.on_action(...)` in the pipeline's transaction; records never rebuilt from `action_log`; one `delete_account(user_id)` for every deletion, following the lock order, deleting records and incrementing `testers_left` when applicable; tester codes loaded by CLI into their own table and resolved only at export; `users.is_test` set by CLI and skipped; exports hold codes, never email or nickname.
- AD-16 Typed facts have one owner: belongings, licences, job, BSU, card, loans and payment plan are typed fields; content sees them only as derived flags computed by one engine function, may require or block them but never set or clear them; `lists.yaml` marks derived flags and the content check rejects options that set them.
- AD-17 Game state decides the gate screens, the URL the area: `gateFor(envelope, session)` returns the first match of start screens, ending, setup step, recap, result, event (incl. card warning), crisis step, year end (from the view's `year_end`). Full-screen gates (start, setup, recap, ending) hide tabs, with `/meny`, `/om-tallene`, `/personvern` reachable over them; Hjem gates (result, year end, event, crisis step) replace only Hjem, other areas stay reachable and `cannot_continue` alone blocks the month (FR-32b). Recap while `recapDue` is set (login or completed reset, or the first envelope after load or a tab return over the threshold), cleared by «Fortsett» and by a setup step; year end dismissed per (playthrough, month); result only from a success response's `result_id`, closed by «Fortsett»; «Nytt liv» on a completed or ended life only sets `playAgain`. Routes `/hjem`, `/plan`, `/mobil` (`/mobil/[id]`), `/jobb`, `/penger`, `/aaret`, `/meny`, `/om-tallene`; outside the game `/`, `/logg-inn`, `/ny-bruker`, `/glemt-passord`, `/nytt-passord`, `/personvern`. From 1100 px one game layout with Hjem centre and a right pane (CSS breakpoint). A gate change counts as a route change (focus to `h1`, title, one live region). Static «Laster …» before the first envelope; Norwegian error and not-found pages.
- AD-18 One game client: only `frontend/src/api/` calls `fetch`; types generated by openapi-typescript (committed, regenerated in the PR that changes `openapi.json`, CI staleness check), calls via openapi-fetch. One store (`useSyncExternalStore` + `getServerSnapshot`) with the envelope and a page-session record (`recapDue`, `playAgain`, dismissed gates, `shownResult`, opened message ids, seen disclosure ids, toast closed, pending action); client sequence numbers, so an older response never replaces a newer one; `state: null` never touches it; the first envelope into an empty store never clears the record; `reset()` aborts requests in flight and starts a new epoch, called after a 2xx logout or deletion and on `401 not_logged_in` (a lost logout is never taken as done; `login_failed` is a form refusal; `/`, `/logg-inn` and `/ny-bruker` make one entry check and go to `/hjem` only on a `200`, the other routes outside the game never fetch it). `sendAction(action, shown)` uses the shown view's fields, single-flight with controls locked; request timeout; transport retries with the same `request_id` 2, 5 and 10 s after each failure, then every 30 s while visible, plus «Prøv igjen» and `online`; a failed GET is a transport failure and drops a waiting input; «Prøver fortsatt …» after 5 s; turn refusals (and `game_changed` with a new playthrough) show «Spillet ble oppdatert på en annen enhet.»; a list of what goes to `announce()` (saving, saved, still trying, offline, back online, new messages). `GET /api/game` on page load of a game route, the entry check, login/sign-up/reset, `online`, state-null refusal, lost account response, nickname change, and before the next input after 5 min idle or tab return (input dropped if the state changed or the recap is due). Quotes kept out of the store. Saving and idle times come from the envelope; the timeout and retry schedule live in `frontend/src/api/config.ts`. Unit tests for retry, error classes, triggers, single flight, stale envelopes, `reset()`.
- AD-19 Tokens and CSS Modules: `tokens.css` generated from DESIGN.md's frontmatter (`colors` → `--color-*`, `scene-*` → `--sc-*`, `rounded` → `--radius-*`, `spacing` → `--space-*`, typography → `--font-<name>-*`), committed, CI staleness check; colours only there (stylelint and ESLint bans in CSS, TSX and SVG). One `.module.css` per component; no component library; shared primitives in `components/ui/` (sheet on `<dialog>`, locked control, one live region with `announce()`, money figure, bar) built in the first frontend story. Scenes as inline SVG switched by the view's state ids; avatar colours from DESIGN's `scene-look-1-*` to `scene-look-6-*` tokens. Fonts self-hosted with `next/font/local` as `--font-bricolage` and `--font-kalam`. Light mode only.
- AD-20 Frontend tests against the real backend: Vitest + Testing Library with fixtures dumped from the seed states (committed, staleness check); Playwright on the full compose stack in Chromium, WebKit and Firefox at 320/390/900/1280 px, no horizontal scroll, fresh seeded DB, one seeded user per spec, no request to another origin; axe (WCAG 2.2 AA tags) on every route and gate fails CI on serious or critical; manual NFR-1, NFR-2 and NFR-10 results in `frontend/e2e/manual-checks.md` before each playtest.

**Consistency conventions**

- Naming: Python snake_case, DB tables plural snake_case, JSON snake_case, API paths `/api/<noun>`, content ids as in the addendum schemas (`E-041`). UUIDs for users, sessions, playthroughs and request ids.
- Time: UTC `timestamptz`; the engine never reads a clock; one `now` per transaction; day-based playtest metrics in Europe/Oslo.
- Logging: stdlib JSON lines with server request id, game `request_id`, `user_id`, `code` and `duration_ms`; one access-log middleware (Uvicorn's off) without client addresses or query strings; never email, password, nickname or reset token (except the local/ci email stand-in); server time per month process+save logged.
- Config split: game figures (pinned per playthrough) in `content/config/vN/`, each with its Rule Set v1 parameter row; operational limits in `settings.py` with PRD defaults.
- Accounts: `users.nickname` validated by one FR-1 function; `users.last_active_at` NOT NULL, written only by the auth dependency.
- Deletion cascades from parents; `tester_codes` has no link to `users`.
- Daily jobs inside the backend process at a fixed UTC hour, each under an advisory lock, as idempotent deletes: inactive accounts (via `delete_account`), expired sessions and reset links, attempt rows older than 24 h.
- `GET /api/health` (no auth) returns 200 once content is loaded and the database answers.
- Monitoring: a daily GitHub Actions check against the playtest (login with a test account, Caddy's 403 without the secret, no `error` log line in 24 h via a read-scoped Railway token), alerting on failure and keeping Supabase awake.
- Performance: p90 ≤ 300 ms server time per month process+save in the playtest; a CI regression bound with headroom.
- Frontend code: App Router, client components for game screens, `<html lang="nb">`, bokmål only with no i18n library, chrome words from EXPERIENCE's word table, no `NEXT_PUBLIC_*` and no secrets, relative `/api` only, a static Content-Security-Policy (`default-src 'self'`), no Vercel Analytics or Speed Insights.
- Lint and format on every PR: ruff check + ruff format --check; ESLint (incl. no `fetch` outside `src/api/`, import direction `app` → `components` → `api`, no colour literals), Prettier --check, stylelint, `tsc --noEmit`.
- Review: a ruleset on `main` before the first story PR (green CI, one approval from another member, no bypass); `playtest` takes merges from `main` only; reviews written as PR comments, also for AI code.
- Tests: pytest; engine tests without a DB; DB tests on Postgres 17 with the migrated schema (compose locally, a service container in Actions), never SQLite; one test per NFR-7 refusal (null and omitted separately); worked examples, F1-F4 and F6-F10, refusals, replays, the seed script, the import-boundary check, the single Alembic head and the content check on every PR.

**Left to stories by the architecture (Deferred table)**

- The members of the action union; the account, session and disclosure endpoints; request and response models (follow the FRs).
- The other fields of the engine state document and the player view (the PRD addendum lists what the state must hold).
- Content schemas in detail: the PRD addendum's schemas apply (event, crisis event, card warning, activity, one-off shift, message, open option, room state, text, unexpected expense, fixed lists; added 2026-11-23, #121).
- Event authoring: a content epic, drafted against the schemas and approved by PR.
- Layout inside each screen, and the player information page's wording (frontend stories, within AD-17 to AD-19, EXPERIENCE and DESIGN).
- Device matrix and throttled-network measurement (NFR-1, NFR-10): by hand before each playtest, written to `frontend/e2e/manual-checks.md`.
- Go-live only, not in these epics: email relay and domain (OQ-4), privacy review (#24), backups, zero-downtime deploys.

**Readiness review 2026-11-23: findings still open that shape stories**

Fixed since the review (commit 7cc1145, PR #127, PR #128): the §4.4 dates (moved; still to be checked against the real deadline), the answer key marked as set test states (#117, answer-key part), the missing content schemas (#121), minigames to V2 (#51), the one-at-a-time table (#83), FR-35 and OQ-9 cleanup, stale UX references and Flows 1 and 4, the brief note and the changes table, and loan terms only from config. Still open:

- #122 Frontend architecture: done in the spine on 2026-11-23 (AD-17 to AD-20, reviewed); closes when this branch is merged. The UX files were aligned the same day: DESIGN.md has the six avatar looks as `scene-look-1-*` to `scene-look-6-*` (colours from the round 3 mockup; `lists.yaml` ids `look-1` to `look-6`) and is marked final; EXPERIENCE points to AD-17 for routes, keeps the hash anchors as mockup-only, and makes the menu the `/meny` route.
- #123 Edge cases in Rule Set v1 and the PRD before the engine stories: one-off shift hours excluded from rule 12 free time, plus a worked example 29 (pay rounding, rate at the month worked, a December shift paid and taxed in January, the 173 h check, none in month 60); BSU deduction for a BSU closed in the same year; rule 9 rounding point; a fixed card payment below a later minimum; extra card payment above the balance; affordability with a negative current account and money in savings; progress clamped at 0; exact-threshold bank messages; the loss rule when month 60's crisis is skipped at open; cooldown vs "Krise i <måned>"; quitting with placed one-off shifts or a pending hours request; ±2 h steps across the limit or floor; summer job re-evaluation in June; the Decimal form of × 52/12; first instalment month for mid-month loans; partially covered family-loan instalments; quotes when no loan is possible; the steady-wage window; the AD-9 money-in wording; missing parameter rows; month-1 setup order (pengegave before any month-1 draw); start while a life is active; regular options whose typed effect conflicts with state; `plan_version` (or item id) on place and remove; "same as last month" with fewer evenings; frozen templates gaining placeholders; unknown content ids in unfrozen versions; month totals after a mid-year schema upgrade; `too_long` field codes; wrong-password attempt limits; reset links cancelled on password change and log-out-everywhere; log out on all devices including the current device; returning testers and `testers_left`; long nicknames in the marker; nickname genitive; the sign of the FR-39 line; card-payable activities when the accounts are short; double-submitted account forms.
- #125 Playtest safety: sign-up limited to addresses in `tester_codes` while `PLAYTEST_RECORDS` is on; «Ta kontakt med teamet» copy on forgotten-password and expired-link screens when no email is sent; a «Nytt passord» surface; one list of player information contents (NFR-3 as the source, including contact point and audience); pg_dump/restore before any switch to the Railway Postgres fallback.
- #126 Freeze vs "the playtest starts anyway": a playtest-minimum gate or a rule that the playtest may run unfrozen; tuning deadline before the freeze; event authoring starts with the content epic, with tuning running on the drafts and OQ-3 blocking only moped and car events; an owner and an events-per-week target.
- #92 The sprint-1 hosting spike, with AD-14's full checklist.
- #81 A team member reproduces the recalculated answer-key figures (17a, 22, 23, the UJ-4 trace) before engine stories cite them.
- #82, #69, #108 Metric definitions (SM-2 minimum gain, SM-6 window vs test length, SM-10 vs FR-11 start point), the written-explanations rubric and the quiz review, before the FR-50 story fixes its fields.
- #117 D12, D25 and D26 still describe the player setting hours, «forbruksnivå» and «plasser» (text only).
- #57 / OQ-17 The activity catalogue and its sourced prices, before activity content.
- #48 / OQ-8 Tuning with real event costs (goal 1 passes by only NOK 488 with expenses).
- #73 / #46 / OQ-13 The real delivery date, before sprint planning.

### UX Design Requirements

Source: `ux-IBE160-G13-2026-11-11` (DESIGN.md = look and tokens, EXPERIENCE.md = behaviour). Surface numbers refer to the EXPERIENCE IA table. Surface 22 (driving minigame) is V2.

**Foundations**

- UX-DR1: Design tokens. Implement DESIGN.md's colour, typography, radius and spacing tokens as CSS variables, including the scene palette as `--sc-*` variables. Money colours (`money-in`, `money-out`, `money-rate`) are marks only, never text colours; status colours (`status-good/warn/bad` and their soft tints) are used only for wellbeing; `locked` yellow only for locked things; `danger` only for "Si opp jobben", "Slett bruker" and form errors; coral is the only accent and always has a 2px ink border (meaningful coral dots have a 1.5px ink ring). Light mode only.
- UX-DR2: Typography. Self-host Bricolage Grotesque (400-800) and Kalam (700) (NFR-3: no third-party loads); tabular figures on all amounts; the type ramp (display, h1-h3, body 15/1.45, meta 13 as the running-text floor, caption 12 for short labels only, timeline and tab labels dropping to 11px under 360px). Kalam only on the scene marker, the plan's evening labels and post-its, never for amounts or values.
- UX-DR3: Responsive shell. 320-767: one column, bottom tab bar (Hjem, Plan, Mobil, Jobb, Penger), primary CTA fixed above the tab bar, phone/bank/job as full screens with a round back button. 768-1099: 220px left rail, one centred column (max 720), sticky CTA at the end. ≥ 1100: rail, centre (max 760) and a 400px right pane with the phone in a device frame; Mobil, Melding, Penger and Jobb open in the pane while the centre stays on Hjem; the pane shows Meldinger by default. No horizontal scroll at 320px. 4px grid, 16px mobile gutter.
- UX-DR4: Elevation and shape. Three levels (flat canvas and scene; resting cards with the two-layer soft shadow and no borders; stuck-on stickers and post-its with an offset shadow and −4° to 4° rotation); sheet and CTA lift shadows; square post-its; full-pill controls; `rounded.lg` cards and rows. Only hand-stuck things rotate.
- UX-DR5: Player-facing vocabulary. One word per concept in every surface and in engine texts: «fri kveld» / «Kveld 1» / «planlagt» / «Tom» (never plass, slot, ledig), «aktivitet» / «vakt» / «ekstravakter», «Tidligere valg» (not Ekko), «Hvor mye bruker du i måneden?» Lite/Vanlig/Mye, «trivselsmålet», «livsmålet» / «sparemålet», «Billappen» / «Mopedlappen», «Penger» tab / «Banken» title, «det minste» with an (i), «Del opp hele kortgjelden», «Forenklet», «Ingen krise på vei» / «Krise i <måned> hvis du fortsetter nå», «Bruk kortet». Time shown as month, age and year, never «måned X av 60» or «År N av 5». Microcopy follows the Voice and Tone do/don't table.

**Components (DESIGN.md Components, EXPERIENCE.md Component Patterns)**

- UX-DR6: Timeline. Heading «November · 16 år · 2027» plus «Året ›», 12 month segments (past solid ink, current coral with ink border and taller, future paper with muted outline; states differ by shape, not only colour), at the top of Hjem, Plan, Hendelse and Resultat in the same place. «Året ›» and the bar link to Året (the bar is a duplicate target hidden from screen readers; «Året ›» named «Året, november 2027, du er 16 år»). Below 768px the row ends with the avatar initial linking to the menu («Meny, Mak»).
- UX-DR7: Scene (mirror). Inline, editable SVG scenes `#sc-selfie` (hub, event) and `#sc-glad` (result) with named groups `-figur` and `-speilbilde`, colours from `--sc-*`; the avatar picker sets `scene-hoodie`. A Kalam marker on the glass (nickname with an arrow on the hub, the outcome on the result) placed right of the window, above the head, ≤ 27% wide. Events, the card warning and crisis steps dim the scene to 55% with a white marker. Only the artwork is `role="img"`, with a text alternative matching the scene state and marker; stickers are sibling links outside the image. Never a raster image.
- UX-DR8: Room layers. One named SVG group per belonging (`-lag-moped`, `-lag-hjelm`, `-lag-lapp`, `-lag-sprekk`), switched by CSS variables from engine flags: moped (none/owned, outside the window, helmet on the boxes), licence (none/moped/car, a pink card in the frame), phone (whole/cracked/used). Up to three more layers fit (bed, poster, free wall). A layer changes in the same view as the choice that changed it; the text alternative names every belonging; the change is announced and listed in the outcome list. No separate room screen.
- UX-DR9: Stickers. White pill, 1.5px ink-muted border, 28px icon, 800-weight label, slightly rotated and straightening on hover, as real links with count or state in text («2 nye» named «2 nye meldinger», «Planlegg 2 kvelder», «Jobb 14 t i uka»), coral dot with ink ring when unread.
- UX-DR10: Money chip. White pill with a 10px colour key (square for in and out, round for interest), a bold signed amount and a plain word («+8 457 kr lønn»). Read-only, except the interest chip, which is a button opening the interest sheet.
- UX-DR11: Buttons and locked controls. Primary (coral) and secondary (white) with 2px ink borders, 48px; CTA 56px with lift shadow; ghost buttons as underlined text; one primary button per screen. Locked controls take `hairline-soft` fill, muted border and text (never see-through), keep focus with `aria-disabled="true"` and `aria-describedby` pointing at the reason, never a bare `disabled`.
- UX-DR12: Focus ring. 3px ink outline 2px out with a 6px coral halo, never removed; outline outside the halo on ink-filled controls; inputs use the outline only.
- UX-DR13: Wellbeing tile (surface 18). «Trivsel» with an (i) explaining the trivselsmål; the score out of 100 with a status pill («Det går bra» / «Helt ok» / «Tungt nå»), wrapping under the score when narrow; three 6px bars (Stress, Fritid, Sosialt) filled by status with an 8px dot (ink ring on warn), the value and a word («25 lavt», «72 bra», «55 ok»; stress inverted); «Vanligvis n» under Stress and Sosialt when the month's plan changes them; a footer with an actionable consequence («Fritid 72 gir deg 3 frie kvelder. Snittet ditt er 61. Trivselsmålet er 50.»). Bands come from the engine (#111); the word is always shown; the dot is hidden from screen readers.
- UX-DR14: Slot row and add list (surface 15). Kalam evening label, title, cost · effect. Filled: white card with a round ×, removal free while the month is open. Empty: «Tom» with a 2px dashed border; below 1100px a coral «+ Legg til» opening the add list in a sheet titled with the evening; from 1100px the quiet text «Velg i lista →» and an always-visible right-column list where + places on the first free evening. School and work are one locked line with a lock icon. Add list: Fritid | Jobb segmented toggle (`aria-pressed`) filtering one list; activities with cost and effect; one-off shifts with name, hours and pay with its month («558 kr lønn i desember»); placed items show a check; with no free evening the add buttons lock with «Alle de frie kveldene er fylt opp. Fjern en aktivitet først.». The plan's «Aktivitetene koster» total is activity costs only. «Samme kvelder som i oktober» places last month's activities, hidden when nothing to place. Tap to place, never drag.
- UX-DR15: Past-choice note and note card. «Tidligere valg»: paper card, round cobalt history icon, cobalt label and one sentence naming the month and the choice, shown only when the engine has a cause link to an earlier choice. «Ble ikke noe av»: the same shape with an × icon, for an activity dropped at month close, shown on the next month's opening as part of the summary, not an alert.
- UX-DR16: Info button and interest sheet. A 24px cobalt (i) after a word, or an underlined amount (2px money-rate) with the (i) for interest; opens a sheet. The interest sheet shows what interest is, the four-line calculation (balance × yearly rate ÷ 12 = this month), a pointer to earning more and the BSU rate; texts from the engine.
- UX-DR17: Phone (surfaces 10, 11). Inbox split into «Nye i <måned>» and «Tidligere»; sender initials in sender colours (cobalt for the bank); a coral dot with ink ring and bold row for unopened messages, clearing on open in the page only (nothing stored, a reload shows them again, #112); Mobil tab badge with screen-reader text («Mobil, 2 nye»). Conversation view per thread; an offer can carry a one-sentence tip; an invitation has «Legg i planen» and «Nei takk» (which only closes it). Read-only; «Du svarer med det du gjør, ikke med tekst.».
- UX-DR18: Toast (surface 09). Below 1100px only, a white card at the top of Hjem, first in reading order, when the month opens with a new message: sender initial, name, one line, a 44px ×. It opens the conversation, closes with × or Esc (focus to «Denne måneden»), never closes by itself, never takes focus, is announced once («Ny melding fra Emma.»), and the message stays in the inbox.
- UX-DR19: Offer card and hours requests (surface 16). Offer card: sender and time, a question, one sentence of consequence (kroner left after spending each month, next month's free evenings, and a warning below 50 free time), Ja takk / Nei takk; answered offers drop the border and show «Du sa ja.» / «Du sa nei takk.»; unanswered offers lapse and show as expired; answerable only in their month. Ask for hours: «Spør om flere timer» / «Spør om færre timer» as full-width secondary buttons, locked with «Svar på tilbudet først.» while an offer is open; after asking, one line with a check («Du har spurt om flere timer. Line svarer i desember.»). One-off shift rows under «Vakter du kan ta i <måned>» with name, hours · signed pay and «Til planen» (opens Plan with Jobb chosen), «I planen» once placed. Ending extra shifts locks the button as «Avsluttet» and the job row says «Slutter etter <måned>». No-job state shows open job offers or when the next opens.
- UX-DR20: Event and event option (surfaces 12, 13). Event: dimmed mirror, four event-facts boxes (Brukskonto, Sparekonto, Gjeld, Faste utgifter; engine figures), options as 64px white buttons with a 2px ink border, the action on the left and signed kroner on the right, wellbeing hidden until picked, pick by tap or Enter. Result: chips (money, wellbeing), an optional past-choice note, «Hvorfor?» expanding in place (`aria-expanded`), an outcome list (26px icons: check on money-in-soft for better, arrow on money-out-soft for worse, dash for unchanged; in the engine's order; announced with the result), and one «Fortsett».
- UX-DR21: Saving, retry and update states. The chosen option reads «Lagrer …» where its amount was and keeps focus while all options lock (announced); after 5 s «Prøver fortsatt …» in the same place, retrying on reconnect and never applying twice; «Spillet ble oppdatert på en annen enhet.» on a stale device; «Du ble logget ut. Logg inn igjen for å spille videre.» after a remote logout; a loading message within 1 s while the server wakes.
- UX-DR22: Offline bar (surface 28). Ink bar with paper text and an icon at the top of the content: «Ingen nett. Du kan se, men ikke velge, før du er på nett igjen.»; the screen stays readable; options and next month lock (`aria-disabled`, described by the bar); announced once through the live region.
- UX-DR23: Bank (surface 17). Account rows (40px paper icon tile, title with optional (i), sub line, amount or one button), transaction rows (money colour key, text, signed amount), the savings target and life-goal progress bars (10px ink fill, percentage at the heading's right, «Etter planlagte aktiviteter» with the planned amount and the pre-plan figure before continuing; «Bytt sparemål» opens a sheet; cleared with a note), two closed «What comes next» rows (next month's known costs, empty in month 60; activity spend this year by kind), «Kan kjøpes eller selges» option rows (price, «Mangler … kr», the blocking reason, or a lock with the age; selling shows today's value and asks once in a sheet with what it changes), spending as option radio cards (kroner and examples, «Dette bruker du nå», «Gjelder fra desember» announced; never re-rendering the group so arrow keys keep working), and transfers and BSU actions.
- UX-DR24: Credit card panel (from 18). The card as an account row (signed balance, limit in the sub line), then a section with used of limit, yearly rate and this month's interest in kroner; «Ikke betalt» and a coral «Betal … nå» when overdue (focus then to the crisis check row); «Bruk kortet» as a 48 × 28 switch (`role="switch"`) saying where purchases go; «Slik betaler du kortregningen» as three option radio cards (whole bill, «det minste» with time and interest if only that is paid, fixed amount opening a stepper in NOK 100 steps from the minimum to the balance), applying from the next bill. Stepper: two 44px round buttons around the value; a button at its limit takes the locked look.
- UX-DR25: Consumer loan sheet (from 18). What the player can borrow and «Se hva et lån koster» opening a sheet with 12/24/36-month toggle buttons and the engine's amount, rate, monthly payment, last payment, total and cost before the loan is taken. Locked with the reason in months 59-60.
- UX-DR26: Crisis check. A soft status band (`status-good-soft` / `status-bad-soft`) with a 10px dot, a bold line and one sentence at the top of the bank before continuing, «Ingen krise på vei» or what would start a crisis month; when a trigger is true it repeats above the hub CTA, and the CTA opens a confirm sheet with «Til banken» first and «Fortsett likevel» second. Month 59 and month 60 texts per EXPERIENCE State Patterns. Paying what is overdue turns it to «Kortet er betalt».
- UX-DR27: Card warning and crisis (surfaces 20, 21). Card warning as an event: facts first (debt, yearly rate, this month's interest, time and cost at «det minste» with an (i), whether the player couldn't pay or chose to pay less), then only possible options; no scolding. Crisis: three 28 × 8px step pills and «Valg n av maks 3», what is owed, only possible options each saying when it lands, asking family and doing nothing on every step, a repeated family ask showing the stored answer («Hun har allerede lånt deg 500 kr»); the end screen lists what changed.
- UX-DR28: Disclosure. The first time a mechanism appears, a «Forenklet» note card (past-choice note shape, (i) icon, text ≤ 62ch, small secondary «Skjønner») under the screen's heading; after «Skjønner» it is gone on every device and playthrough and focus moves to the (i) beside the heading, where the text stays.
- UX-DR29: Month summary. A closed «Hva gikk pengene til?» row under the chips on Hjem; open, it holds transaction rows (example purchases in a meta line with no amounts of their own), fixed costs, each automatic transfer from savings («Flyttet fra sparekontoen … Brukskontoen hadde ikke nok»), a «Kveldene i <måned>» heading with last month's evenings and their cost (free ones as «Gratis»), and one line about taking over the bills at 18.
- UX-DR30: Year chart (surface 19). A diverging bar per month (income up, spending down, 14px bars, ink baseline), interest as a separate small strip on its own scale; each month a button; ‹ month › 44px arrow buttons as the equivalent control (locked at the first and current month); a three-figure detail (`role="status"`); a table view with the same data; coming months inert. Plus the life bar and what unlocks.
- UX-DR31: Locked post-it. Yellow, square, rotated, with a lock icon, a Kalam title and an age («fra 18 år»); never tappable as an option before it unlocks; when open it turns white with an open lock in money-in.
- UX-DR32: Sheet. Native `<dialog>`, paper, sliding up on mobile and centred on desktop, grab handle, title, round ×, 50% scrim; focus moves in and returns, Esc and scrim click close; one level deep, never stacked.
- UX-DR33: Menu (surface 26). White 56px rows with icon, label and value or chevron: nickname and password changes in sheets; player information; start a new life; log out; log out on all devices; delete user (danger text, asks for the password). Confirmations for log out everywhere, new life and delete.
- UX-DR34: Facts card, choice row and ending (surface 25). Facts card (label and bold value rows) on the recap, the card warning and the ending. Ending: outcome heading and one sentence per ending (#slutt, #slutt-hul, #slutt-ikke, #slutt-tap), three facts (saved against the livsmål, average wellbeing against the trivselsmål with a status in past tense, debt), up to three expandable choice rows (chevron, title, signed amount) opening to the «hvis du hadde valgt annerledes» line and a tip; one «Spill på nytt» button; login after the ending lands here.
- UX-DR35: Recap and year end (surfaces 23, 24). Recap: «Hei igjen, <nickname>. Alt er som da du gikk.», where they are, the current account, new messages this month, what's planned, and a teaser with a price against what they have; one button continues. Year end (December): the year's money, the year's tax (or «0 kr» with why), the expected BSU deduction when there is a BSU, what changed, the average wellbeing against the trivselsmål, notes for dropped activities, a teaser for the next unlock with its price; «Fortsett» or «Ferdig for nå».

**Surfaces and flows**

- UX-DR36: Account surfaces (01-04, 26 and the reset page). First screen with «Lag bruker» / «Logg inn». Create user: email once, password, nickname («Hva skal vi kalle deg?») with a live preview bubble, stay logged in, the «Dette lagrer vi» info box, then the email check step («Sjekk at e-posten er riktig», the address in h2 breaking after @ and dots, «Lag bruker» / «Endre e-post», going back keeps input). Log in with «Forbli innlogget» unticked and a forgot-password link. Forgot password with the same answer whatever the address. Error states and copy per EXPERIENCE State Patterns (login failed, repeated failures, password too short, email in use with links, email invalid, nickname invalid, password wrong, reset link used or expired), all shown at once with focus on the first error, `aria-invalid` and linked messages. Fields use `autocomplete` email/username, current-password/new-password and nickname; paste and password managers work.
- UX-DR37: Start surfaces (05-07). Life goal as option radio cards; six preset avatar looks that recolour the mirror figure; the pengegave screen with the random amount stated as a fact and the first real choice. A new player reaches the first real choice in about 2 minutes.
- UX-DR38: Hub (surface 08). Timeline, mirror with room layers and stickers, «Denne måneden» with the chips (wage, spending, interest) and the month summary row, accounts tile, wellbeing tile, and the CTA to continue (one tap finishes a quiet month; continuing opens the next month's event first if active, otherwise its hub). Visually hidden `h1` «Hjem, november». At 320px the hub keeps the timeline, the stickers, this month and the CTA.
- UX-DR39: «Om tallene» (surface 27). All 26 disclosed simplifications grouped by theme, reachable from the menu, rendered from the pinned library (or the start versions when no life is active).
- UX-DR40: Unread and "something new" marks. «1 ny» / «2 nye» on the sticker, a count badge on the Mobil tab or rail, bold inbox rows; a bare coral dot with ink ring on Plan (free evenings left) and Jobb (an unanswered offer), with screen-reader text «, noe nytt».

**Accessibility floor (EXPERIENCE Accessibility Floor, Interaction Primitives)**

- UX-DR41: Focus management. After a route change focus goes to the screen's `h1` (the pane's `h1` on desktop pane routes); the EXPERIENCE focus-move table applies (removing or placing an activity, answering an offer, asking for hours, saving a choice, selling, closing a sheet whose opener is gone, closing the toast, «Skjønner», paying overdue, controls that keep focus). Nothing re-renders a focused control without restoring focus. Focus not obscured (2.4.11): at least 150px bottom scroll padding below 768px and clearance from the sticky app bar in the pane; checked by tabbing every surface at 320 × 640.
- UX-DR42: Live region and announcements. One polite live region from page load; status text sent there (activity placed or removed, offer answered, spending changed, saving, offline, results, new message), never with a newly injected region. Document title «<screen> · LifeMode» on every route.
- UX-DR43: Interaction primitives. Tap or select everywhere, all keyboard-operable; no dragging; no timers, countdowns or self-dismissing content; random draws stated as facts, no chance-based rewards; targets ≥ 24 × 24 px and 44 × 44 px for options, round buttons and tabs; one authored motion moment (result chips pop in, sheets slide) plus sticker hover, all off under reduced motion; nothing core on hover.

**UX gaps flagged by the readiness review (still open, #125)**

- UX-DR44: An amount-entry pattern for money actions that take an amount (transfer from NOK 1, BSU deposit with the remaining cap, extra card payment, early payoff, loan amount) with states for NFR-7's "not whole kroner / zero or below / outside range" refusals. The view now carries each amount action's `min`, `max` and `step` (AD-13); the visual pattern is still open.
- UX-DR45: A «Nytt passord» surface for `/nytt-passord#token=…` (reads the token, removes it from the address bar, posts token and new password) with used, expired and replaced-link states, and playtest copy «Ta kontakt med teamet for ny lenke» on surface 04 and the expired-link state when no email is sent. How the frontend knows that email is off in the playtest is not yet decided (#125).

### FR Coverage Map

FR-1: Epic 1 - Create user
FR-2: Epic 1 - Log in
FR-3: Epic 1 - Forgotten password
FR-4: Epic 1 - Change password
FR-5: Epic 1 - Log out and staying logged in
FR-44: Epic 1 - Delete account
FR-6: Epic 2 - Save every choice
FR-7: Epic 2 - Nothing waits on the device
FR-8: Epic 2 - Check for updates on opening or returning
FR-9a: Epic 2 (choosing the goal) and Epic 4 (checking it after month 60)
FR-9b: Epic 8 - Goals reachable, reference and seeded runs
FR-9c: Epic 3 - Progress towards the goal during play
FR-10: Epic 2 - Avatar
FR-11: Epic 2 - Pengegave and first choice
FR-12: Epic 2 - Month processing (rule 1)
FR-13: Epic 2 - Active month with an event
FR-14: Epic 2 - Quiet month summary
FR-15: Epic 4 - Year end and teaser
FR-16: Epic 4 - Recap on return
FR-17: Epic 8 - Content library
FR-18: Epic 5 - Age unlocks
FR-19: Epic 8 - Tips in events and offers (the card offer's tip in Epic 7)
FR-20: Epic 6 - Wages
FR-21: Epic 6 - Tax
FR-22: Epic 3 - Saving and BSU
FR-23: Epic 3 - Fixed and everyday costs, spending level (moped transport and car fuel completed in Epic 8)
FR-24: Epic 3 - Unexpected expenses
FR-25: Epic 7 - Consumer loans
FR-26: Epic 7 - Credit card
FR-27: Epic 7 - Help from family
FR-28: Epic 8 - Moped licence
FR-29: Epic 8 - Own a moped
FR-30: Epic 8 - Car licence
FR-31: Epic 7 - Card warning
FR-32a: Epic 7 - Crisis triggers and start
FR-32b: Epic 7 - Crisis steps and options
FR-32c: Epic 7 - How a crisis month ends
FR-33: Epic 2 - Wellbeing (activity effects added in Epic 6)
FR-34: Epic 8 - Room layers
FR-36: Epic 2 - Cause links (in the ledger from the first money change)
FR-37: Epic 9 - Echo badges («Tidligere valg»)
FR-38: Epic 9 - «Hvorfor?»
FR-39: Epic 4 - "If you had chosen differently"
FR-40: Epic 9 - Disclosed simplifications and «Om tallene»
FR-41: Epic 4 - Four endings (the loss ending is exercised once crises exist, Epic 7)
FR-42: Epic 4 - Ending summary
FR-43: Epic 4 - Play again
FR-45: Epic 2 (current account and paying for choices) and Epic 3 (savings cover, payment order, money actions)
FR-46a: Epic 2 - Active months and pace
FR-46b: Epic 2 - Which event an active month gets
FR-46c: Epic 5 - Follow-ups and collisions
FR-47: Epic 6 - Working hours
FR-48: Epic 5 - Options that stay open
FR-49: Epic 2 - Moving to the next month
FR-50: Epic 1 (tester codes and the sign-up limit) and Epic 10 (playtest records)
FR-52: Epic 6 - Month plan and activity slots
FR-53: Epic 6 - Activities
FR-54: Epic 5 - Phone and messages
FR-55: Epic 5 - Which messages arrive
FR-56: Epic 6 - Job view
FR-57: Epic 9 - Savings target, upcoming costs and activity spend
FR-58: Epic 8 - Content check (the schema gate starts in Epic 2)

Not mapped: FR-35 (left out of the MVP, #115) and FR-51 (V2, #51). NFR-1, NFR-2, NFR-4 and NFR-7 apply to every epic and are tested in each story; NFR-3, NFR-5, NFR-6 and NFR-9 start in Epic 1; NFR-8 is checked with the content in Epic 8; NFR-11 (the environment and the daily check) is set up in Story 1.9; NFR-10 is measured in Epic 10.

## Epic List

Ten epics, each a vertical slice: backend, frontend and tests for the same player outcome (the group builds both sides). Order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10, one after the other. Each epic uses only earlier epics; where a story shows something a later epic builds, it says so, and the later story adds that part.

**Rule for every story: the game says no the right way (NFR-7, NFR-9).** A story that builds an action also builds every NFR-7 refusal that belongs to it, whether or not its own criteria repeat it (for example selling a moped the player doesn't own, or placing the same one-off shift twice). For each refusal:

- the game is unchanged, the response carries the current progress, and the player sees a short message in plain Norwegian where they could see the action
- it has its own automated test, with `null` and omitted fields tested separately; the five NFR-7 cases that aren't refusals have their own tests too
- it is logged without the email address or the password

The story isn't done until these are in place. Story 10.4 checks NFR-7's whole list against the tests.

**Rule for every story: no link to what isn't built.** A tab, sticker or link shows only when its page exists. The story that builds a page adds the links to it (`/penger` 3.1, `/aaret` 4.2, `/mobil` 5.1, `/plan` 6.1, `/jobb` 6.3).

**Tiers (PRD §4.4).** Each story has a **Tier** line under its heading, from the PRD's FR overview (§5): Core must be in, Extension is built when it is started before the freeze, and Can be cut goes first when time runs short. Setup, safety and check stories with no FR tier of their own are Core, because the Core stories or an NFR need them.

| Tier | Stories |
|---|---|
| Extension | 1.6, 2.4, 4.3, 7.3, 9.2, 9.3 |
| Can be cut | 8.4, 8.5, 9.4 |
| Not set by the PRD | 4.2 |
| Core | all the others, 9.1 («Hvorfor?») included |

### Epic 1: Konto og innlogging
A player can create a user, log in and out, change and reset the password, log out on all devices and delete the user. The app runs locally with one command and in the playtest environment, where only invited testers can sign up.
**FRs covered:** FR-1, FR-2, FR-3, FR-4, FR-5, FR-44, FR-50 (tester codes and the sign-up limit)
**Notes:** Story 1.1 is the scaffold from the Structural Seed: repo layout, compose with Caddy, backend, Postgres and frontend, and CI with lint, format and staleness checks. Story 1.2 adds the frontend shell with `tokens.css` and the shared primitives in `components/ui/` (AD-19). The review ruleset on `main` must be in place before the first story PR. The sprint-1 hosting spike (#92) belongs here. NFR-3 player information page `/personvern`, NFR-5, NFR-6 (README run), NFR-9 (CI) and NFR-11 (environment) start here.

### Epic 2: Start et liv og spill måned for måned
A player picks a life goal and an avatar, gets the pengegave and makes the first real choice, then plays active months with events and quiet months, sees wellbeing change, and continues on another device without losing anything.
**FRs covered:** FR-6, FR-7, FR-8, FR-9a (choosing the goal), FR-10, FR-11, FR-12, FR-13, FR-14, FR-33, FR-36, FR-45 (current account and paying for choices), FR-46a, FR-46b, FR-49
**Notes:** Builds the engine core (AD-1, AD-6), the mutation pipeline (AD-4, AD-5), the ledger with cause links (AD-9), content loading with the schema gate (AD-7), the player view (AD-13) and the frontend game client and gates (AD-17, AD-18). Uses a small starter set of events. Needs #123 and #81 settled for the stories that cite them.

### Epic 3: Pengene i hverdagen
A player moves money between the current account, savings and BSU, earns interest, pays fixed and everyday costs, picks a spending level, meets unexpected expenses, and sees progress towards the life goal.
**FRs covered:** FR-9c, FR-22, FR-23, FR-24, FR-45 (savings cover, the payment order table, money actions)
**Notes:** The bank screen (Penger) and the month summary. A life can be played with no job (WE 15); wages and tax come in Epic 6.

### Epic 4: Året, slutten og et nytt liv
A player gets the year end each December and a recap on return, reaches one of four endings at 20 with the three choices that mattered and what would have happened otherwise, and can start a new life.
**FRs covered:** FR-9a (checking the goal), FR-15, FR-16, FR-39, FR-41, FR-42, FR-43
**Notes:** The loss ending's rule is built here and exercised once crises exist (Epic 7). The year end and the recap are built here; messages, follow-up hints, planned activities and tax are added to them in Epics 5 and 6.

### Epic 5: Mobilen og valgene som står åpne
A player gets messages, invitations and offers on the phone, sees options unlock with age and stay open until taken, and meets follow-ups to earlier events.
**FRs covered:** FR-18, FR-46c, FR-48, FR-54, FR-55
**Notes:** Uses the starter events from Epic 2. Each option's own rules come with its epic (6, 7 and 8).

### Epic 6: Jobb, fritid og månedsplan
A player takes a part-time, summer or full-time job, asks for more or fewer hours, takes extra and one-off shifts, earns wages and pays tax, and plans activities in the free evenings.
**FRs covered:** FR-20, FR-21, FR-47, FR-52, FR-53, FR-56
**Notes:** Needs the age unlocks from Epic 5 (the job opens in month 3). The activity catalogue with sourced prices (#57) comes before the activity stories.

### Epic 7: Kort, lån og kriser
A player can take a credit card and a consumer loan, borrow from family, gets the card warning, and handles crisis months with up to three steps and a payment plan.
**FRs covered:** FR-25, FR-26, FR-27, FR-31, FR-32a, FR-32b, FR-32c
**Notes:** Needs the steady wage, hours and activities from Epic 6: a card and a loan need a steady wage, and crisis options use shifts and jobs.

### Epic 8: Moped, lappene, rommet og hele innholdet
A player takes the moped licence, buys and sells a moped, gets or pays for the car licence and borrows the parents' car, sees belongings in the mirror's room, and plays the full event library with tips.
**FRs covered:** FR-9b, FR-17, FR-19, FR-28, FR-29, FR-30, FR-34, FR-58
**Notes:** Car fuel can go on the card, so Epic 7 comes first. The full library (8.6-8.10, one story per year) and the content check (8.11) come last, since events use jobs, cards, loans and the moped. Drafting events can start once Story 2.1 is done. Story 8.11 needs only the engine and the starter set, so it can be built before 8.6; its reports then help the authors and the tuning (#48, 10.3) while the library grows. NFR-8 tone is checked with the content. The freeze and event-authoring plan (#126) and tuning with real event costs (#48) come before 8.6-8.11.

### Epic 9: Forstå tallene
A player can ask «Hvorfor?», sees «Tidligere valg» on effects of earlier choices, reads «Forenklet» notes and «Om tallene», pins a savings target and sees what comes next month.
**FRs covered:** FR-37, FR-38, FR-40, FR-57
**Notes:** Story 9.1 («Hvorfor?», FR-38) is Core, is always built and is never cut. The other stories are mostly Extension tier, so scope can be cut there first.

### Epic 10: Playtesten
The group can run the playtest: records per tester and export by tester code, the content freeze, the manual and measured checks before the playtest, the test players close to each ending, and the clean-up afterwards. Sign-up limited to testers, the playtest environment and the daily check are in Epic 1.
**FRs covered:** FR-50 (playtest records)
**Notes:** Also NFR-10 (measured), and the playtest-safety items in #125. NFR-11's environment and daily check are set up in Story 1.9. The metric definitions and rubrics (#82, #69, #108) come before these stories.

## Epic 1: Konto og innlogging

A player can create a user, log in and out, change and reset the password, log out on all devices and delete the user. The app runs locally with one command and in the playtest environment, where only invited testers can sign up.

### Story 1.1: Run the app from the README with one command

**Tier:** Core

As an examiner,
I want to start the whole app with one command on a clean machine,
So that I can run and grade it without the team's keys or secrets (NFR-6).

**Acceptance Criteria:**

**Given** a clean machine with only Docker installed and no `.env` file
**When** I follow the README and run `docker compose up`
**Then** Caddy serves `http://localhost:<port>`, with Postgres 17, the backend and the frontend as compose services, and `GET /api/health` answers `200` once the database answers
**And** Caddy sends `/api/*` and `/openapi.json` to the backend with the path unchanged and everything else to the frontend, and the backend serves no frontend files and enables no CORS (AD-12)

**Given** the backend image starts
**When** `APP_ENV` is missing
**Then** it refuses to start, and every setting is a pydantic-settings field in `backend/app/settings.py` listed in `.env.example`, with `compose.yaml` setting the local defaults inline (AD-14)
**And** the compose entrypoint runs `python -m app.cli schema upgrade` before the app starts, and the app never migrates inside its own startup

**Given** the first Alembic migration
**When** it creates a table
**Then** the RLS helper turns row-level security on with no policies, and a CI test fails on any table without RLS (AD-3)

**Given** a pull request
**When** CI runs
**Then** it runs `ruff check`, `ruff format --check`, the import-boundary check (engine imports nothing outside itself, AD-1), the banned-api rule, pytest against a Postgres 17 service container, the `openapi.json` staleness check and the single-Alembic-head check, and fails if any fails
**And** every `/api` response carries `Cache-Control: no-store`, logs are JSON lines written by one access-log middleware without client addresses or query strings, and unhandled exceptions return `500 internal_error` in the AD-13 error envelope

### Story 1.2: Open the first screen on any device

**Tier:** Core

As a new player,
I want the first screen to open quickly and look right on my phone or laptop,
So that I can choose to create a user or log in.

**Acceptance Criteria:**

**Given** the compose stack is running
**When** I open `/`
**Then** I see surface 01 with «Lag bruker» and «Logg inn», in a Next.js 16.4 App Router app with TypeScript `strict`, `<html lang="nb">` and the title «… · LifeMode»
**And** the page has no horizontal scroll at 320, 390, 900 and 1280 px, and follows the responsive shell (UX-DR3), with tabs only for areas that are built

**Given** `DESIGN.md`'s frontmatter
**When** the token script runs
**Then** it writes `frontend/src/styles/tokens.css` with the AD-19 mapping (`--color-*`, `--sc-*`, `--radius-*`, `--space-*`, `--font-*`), the file is committed, and CI fails if it is stale
**And** stylelint and ESLint fail on any colour value outside `tokens.css`, in CSS, TSX or SVG (AD-19, UX-DR1)

**Given** the shared primitives in `components/ui/`
**When** a later story needs a sheet, a locked control or an announcement
**Then** it uses the native `<dialog>` sheet (UX-DR32), the locked control with `aria-disabled` and `aria-describedby` (UX-DR11), the focus ring (UX-DR12), and the one polite live region mounted by the root layout through `announce()` (UX-DR42)
**And** Bricolage Grotesque and Kalam load with `next/font/local` from files in the repo, a `Content-Security-Policy` with `default-src 'self'` is sent on every page, and no request leaves the origin (NFR-3, UX-DR2)

**Given** a pull request
**When** CI runs
**Then** ESLint (including the `fetch` and import-direction rules), Prettier `--check`, stylelint, `tsc --noEmit` and Vitest run, and Playwright runs against the compose stack in Chromium, WebKit and Firefox with `@axe-core/playwright` on `/` using the WCAG 2.2 AA tags, failing on any `serious` or `critical` finding (AD-20)
**And** `error.tsx`, `global-error.tsx` and `not-found.tsx` show Norwegian text with a link back
**And** the primitives follow the three elevation levels and shapes (UX-DR4), chrome text uses EXPERIENCE's word table (UX-DR5), and every control is tap-or-select and keyboard-operable with targets of at least 24 × 24 px (44 × 44 for options and tabs), no dragging, no timers and motion off under reduced motion (UX-DR43)

### Story 1.3: Create a user

**Tier:** Core; the per-network sign-up limit can be cut

As a new player,
I want to create a user with my email, a password and a nickname,
So that my game is saved and only I can reach it (FR-1).

**Acceptance Criteria:**

**Given** I am on `/ny-bruker`
**When** the page loads
**Then** I see email, password, a nickname field with a live preview («Hva skal vi kalle deg?»), «Forbli innlogget» unticked, and the short player information above the submit button, and `/personvern` holds the full text (NFR-3's list, the processors and log notes from AD-14, and FR-5's browser note), reachable before any account exists
**And** the fields use `autocomplete` values that let paste and password managers work (UX-DR36)

**Given** I have filled in the form
**When** I submit
**Then** a check step shows my email address for me to confirm or change, and going back keeps what I typed (WCAG 3.3.7)

**Given** valid input and an unused address
**When** I confirm
**Then** a `users` row is created with the email normalized by one function (outer spaces trimmed, case-insensitive; dots and `+` tags kept), the password stored as `bcrypt(base64(sha256(password)))`, and the nickname validated by the FR-1 function (trimmed, 2-16 characters, letters including æ/ø/å, digits, spaces, hyphens)
**And** a session row is created with an httpOnly, `SameSite=Lax` cookie (Secure outside `local`/`ci`), no email is sent, and I land on `/hjem`
**And** in this epic `/hjem` is a simple page that says I am logged in, and `GET /api/game` answers only `401`, or `200` with `status` `none`; Story 2.2 adds the rest

**Given** an address that already has a user
**When** I confirm
**Then** I get `409 email_in_use` with its field and links to «Logg inn» and the reset page, and this is the only response that reveals an address has a user

**Given** invalid input
**When** I submit
**Then** I get `422 invalid_input` listing every failing field (`too_short`, `invalid_chars`, `invalid_email`), all errors show at once with `aria-invalid`, linked messages and focus on the first error, worded as in EXPERIENCE
**And** sign-ups from one network above the limit (default 60 an hour, settings) get `429 rate_limited` with the neutral message, counted in `auth_attempts` by HMAC keys
**And** no log line holds the email address, password or nickname, and each refusal has an automated test with `null` and omitted fields tested separately (NFR-7)

### Story 1.4: Log in, stay logged in and log out

**Tier:** Core; «Forbli innlogget» and «Logg ut på alle enheter» can be cut

As a player,
I want to log in on any device, choose whether to stay logged in, and log out when I'm done,
So that I can play on my own phone and on a shared school PC safely (FR-2, FR-5).

**Acceptance Criteria:**

**Given** I am on `/logg-inn`
**When** I enter a wrong email or password
**Then** I get `401 login_failed` with one neutral message on the form, never saying which field was wrong, and the form keeps my email

**Given** 10 failed logins for one address from one network within 15 minutes
**When** another login for that address comes from that network
**Then** it is paused for 15 minutes with the neutral message, while other networks still work (all values in settings); that the reset link still works is tested in Story 1.5
**And** the client address comes only from the header Caddy sets, and forged `X-Forwarded-For`, `X-Real-IP` and `x-vercel-forwarded-for` headers have no effect (tested)

**Given** I log in with «Forbli innlogget» unticked
**When** I am inactive for 30 minutes or the browser ends its session
**Then** my next request gets `401 not_logged_in` and I am sent to `/logg-inn`
**And** with it ticked, the session lasts until I log out or 30 days without play; expiry slides at most once a minute, and only the auth dependency writes `users.last_active_at` (AD-10)

**Given** I am logged in
**When** I open `/meny` and choose «Logg ut» or «Logg ut på alle enheter» (with a confirmation)
**Then** (from the menu's 56 px rows, UX-DR33) my session row, or all my session rows, are deleted, and a device logged out elsewhere gets `401 not_logged_in` on its next request and shows the login screen
**And** a logout whose response is lost is not treated as done: the page stays in the menu with «Prøv igjen» until it gets a `2xx` or a `401`

**Given** I am logged in
**When** I open `/`, `/logg-inn` or `/ny-bruker`
**Then** the page calls `GET /api/game` once, and the `200` replaces the route with `/hjem` (AD-17, AD-18)
**And** when I am not logged in or my session has ended, the `401 not_logged_in` leaves me on the page with no redirect, and any other failure leaves the form usable
**And** this is tested once the first version of the app (the prototype) is built, in Story 10.4, since there is no app to run the test against before that

### Story 1.5: Get a new password with a reset link

**Tier:** Core; the daily total cap on reset emails can be cut

As a player who forgot the password,
I want a one-time link to set a new password,
So that I can get back to my game (FR-3).

**Acceptance Criteria:**

**Given** I am on `/glemt-passord`
**When** I submit any address
**Then** the screen always shows the same message, unknown addresses do the same work, and the limits per address (1 a minute, 5 a day) and the daily total cap apply (settings)

**Given** an address with a user
**When** a link is created
**Then** it is `{PUBLIC_BASE_URL}/nytt-passord#token=<token>`, stored as a SHA-256 hash, usable once for 60 minutes, and a new link cancels older ones
**And** the email module sends it through Resend when keyed, writes it to the backend log as `[email:mock]` in `local`/`ci` without a key, and sends nothing in the playtest (AD-11)
**And** `python -m app.cli reset-link <email>` prints a link for the playtest without logging the address

**Given** I open a valid link
**When** `/nytt-passord` loads
**Then** it reads the token from the fragment, removes it from the address bar, and posts the token and my new password
**And** on success every device is logged out, this device is logged in, and the game is unchanged
**And** this works while logins for the address are paused (Story 1.4, FR-2)

**Given** a used, expired or replaced link
**When** I submit
**Then** I get `410 reset_link_invalid` and the page offers a new link (UX-DR45)
**And** when no email is sent (the playtest), surface 04 and the expired-link state say «Ta kontakt med teamet for ny lenke», by the mechanism #125 decides

### Story 1.6: Change my password and nickname

**Tier:** Extension (FR-4). Changing the nickname is Core (FR-1)

As a player,
I want to change my password and my nickname from the menu,
So that I can keep my account safe and be called what I like (FR-4, FR-1).

**Acceptance Criteria:**

**Given** I am in `/meny`
**When** I open «Bytt passord» and enter my current password and a new one of at least the FR-1 minimum
**Then** the old password stops working at once, my other devices are logged out, this device stays logged in, and the game is unchanged
**And** a wrong current password gives `403 wrong_password` on that field, and a too-short one gives `422 invalid_input`

**Given** I am in `/meny`
**When** I open «Bytt kallenavn» and save a valid nickname
**Then** `users.nickname` changes through the same FR-1 validation function, and the menu and every later view show the new nickname
**And** both sheets are one level deep, single-flight with their submit locked while saving, and never retried automatically (AD-18)

### Story 1.7: Delete my user

**Tier:** Core; the 12-month deletion job can be cut

As a player,
I want to delete my user and everything stored about me,
So that no data about me is kept when I stop playing (FR-44, NFR-3).

**Acceptance Criteria:**

**Given** I am in `/meny`
**When** I choose «Slett bruker», confirm, and enter my current password
**Then** one `delete_account(user_id)` deletes the user row and every child row by cascade (sessions, reset links and any table later stories add), every device is logged out, and I land on `/`
**And** the same address can sign up again, and a wrong password gives `403 wrong_password` with nothing deleted

**Given** the backend is running
**When** the daily jobs run at their fixed UTC hour, each under an advisory lock
**Then** accounts with no activity for 12 months (settings) are deleted through `delete_account`, and expired sessions, expired reset links and attempt rows older than 24 hours are deleted, all as idempotent deletes (Jobs convention)

### Story 1.8: Let only invited testers sign up in the playtest

**Tier:** Core

As the team,
I want only the testers we invited to be able to sign up in the playtest,
So that the playtest stays within the 18-20-year-olds the privacy assessment covers (NFR-3, #125).

**Acceptance Criteria:**

**Given** the email-to-tester-code list
**When** a team member runs the CLI command that loads it in the playtest environment
**Then** each address is normalized by the FR-1 function and stored with its code in `tester_codes`, a table with no link to `users`, and nothing else stores codes (AD-15)

**Given** `PLAYTEST_RECORDS` is on
**When** someone signs up with an address that isn't in `tester_codes`
**Then** the sign-up is refused with a neutral Norwegian message, and with the switch off (local, the examiner's run) sign-up is open, with a test for each state

**Given** the team's own and check accounts, whose addresses are on the list too
**When** a team member marks them with the CLI command
**Then** `users.is_test` is set, and Stories 10.1 and 10.2 leave those accounts out of the records and the export

### Story 1.9: Reach the app in the playtest environment

**Tier:** Core

As the team,
I want the app deployed to Vercel, Railway and Supabase with the sprint-1 checks done,
So that testers can reach it at one address and we know the hosting assumptions hold (AD-12, AD-14, NFR-11, #92).

**Acceptance Criteria:**

**Given** a push to the `playtest` branch
**When** Vercel and Railway deploy
**Then** the Vercel project (Root Directory `frontend`, `regions: ["fra1"]`) proxies `/api/(.*)` to Caddy on Railway with `x-origin-secret` set from `ORIGIN_SECRET` and rewrite caching off, and Railway runs Caddy and the backend in EU West with sleeping off, the pre-deploy schema upgrade and the backend healthcheck, from `.railway/railway.ts`
**And** the database is Supabase Free in Frankfurt through the session pooler, with a pool of 5 and no overflow, the Data API off and RLS on every table

**Given** the first deploy to the playtest environment
**When** the address can be reached
**Then** `PLAYTEST_RECORDS` is on, so only addresses in `tester_codes` can sign up (Story 1.8), and with an empty list nobody can

**Given** a request to Caddy without the right `x-origin-secret`
**When** it arrives
**Then** Caddy answers `403 origin_refused`, a preview deployment gets `403` on `/api`, and Caddy refuses to start with a secret shorter than 32 bytes or equal to the placeholder

**Given** the playtest environment exists
**When** the daily GitHub Actions check runs
**Then** it logs in with a test account, asserts Caddy's `403` without the secret, fails on any `error` log line in the last 24 hours, and alerts the team on failure
**And** the spike results (server time per request, no cold start, usage, pooler clients during a deploy, client-address header, cookies passed through, no `/api` caching, Supabase counting the check as activity) are written to the repo, and the usage alert (USD 6) and hard limit (USD 10) are set

## Epic 2: Start et liv og spill måned for måned

A player picks a life goal and an avatar, gets the pengegave and makes the first real choice, then plays active months with events and quiet months, sees wellbeing change, and continues on another device without losing anything.

### Story 2.1: Write game figures and events as checked YAML

**Tier:** Core

As a content author,
I want to write the game's figures and events as versioned YAML files that are checked on every pull request,
So that the game reads one source of truth and a broken file never reaches a player (AD-7, NFR-4).

**Acceptance Criteria:**

**Given** `content/config/v1/`, `content/config/test-v1/` and `content/library/v1/`
**When** the backend starts
**Then** the loader validates every version into the engine's Pydantic content model, computes each version's fingerprint over its non-text fields, and refuses to start on a broken file
**And** rates and wages are `Decimal` from quoted strings, and a float anywhere in a figure fails the load (AD-6)

**Given** a figure in `content/config/v1/`
**When** it is read
**Then** it carries its Rule Set v1 parameter row, source and date, including `start_year` (2026), the wellbeing threshold and band offset, the active months (January, April, July, October) and the pengegave range (NOK 10,000-30,000)

**Given** a pull request that changes content
**When** CI runs the content check
**Then** the schema gate and the fixed-list names fail on any error, and game text that writes a four-digit year or a month name fails (AD-7); the other FR-58 gates only warn while the library is unfrozen
**And** the library has a starter set of regular events with a free option each, at least two that can be drawn in every in-game year from 15 to 19, and one boomerang pair, so a life can be played to 20 with events before the full library (8.6-8.10)

### Story 2.2: Choose my life goal and start a life

**Tier:** Core

As a new player,
I want to pick one of three life goals,
So that my life starts with a goal I chose (FR-9a, FR-11).

**Acceptance Criteria:**

**Given** I am logged in with no playthrough
**When** I open `/hjem`
**Then** `GET /api/game` answers `200` with a view whose `status` is `none` and that carries the start screens' texts and the versions a start would pin, and the frontend shows the life-goal screen (surface 05) as a full-screen gate (AD-17)
**And** the three goals show as option radio cards with their targets from config (UX-DR37)

**Given** I confirm a goal
**When** the frontend sends the start action through `sendAction` with a new `request_id`
**Then** one `POST /api/game/actions` pipeline locks the user row, creates the `playthroughs` row with a seed from `secrets`, the pinned library and config versions and the state document, appends the `action_log` row last, and saves it all in one transaction (AD-4, AD-5)
**And** the response is `{result?, state, server_time, recap_threshold, client_times}`, and the game store replaces its envelope with it (AD-18)
**And** a gate entering or leaving counts as a route change: one focus manager moves focus to the new screen's `h1`, sets «<screen> · LifeMode», and announces the change, and nothing re-renders a focused control without restoring focus (UX-DR41)

**Given** the start action
**When** it carries a library version that is no longer the one a start would pin, or a playthrough already exists
**Then** it is refused (`409 game_changed` or the matching NFR-7 code) with the current view and nothing saved, and the start screens show again

**Given** any request to the game API
**When** the server reads it
**Then** it takes only the player's inputs in NFR-7 and the protocol fields, ignores unknown fields, refuses a missing or wrongly typed one, and works out every result and figure itself (AD-2)
**And** no `GET` changes state, and only `POST /api/game/actions` is ever retried automatically (AD-2)

**Given** the same `request_id` is sent twice
**When** the second arrives
**Then** nothing is applied again and the response marks the result `replayed`, tested for start and for every later action (NFR-7)
**And** the game client is single-flight: while the action is pending, the controls are locked and read «Lagrer …» (UX-DR21)

### Story 2.3: Get the pengegave and make my first choice

**Tier:** Core

As a new player,
I want to get my pengegave and choose what to do with it,
So that my first choice is about real money (FR-11).

**Acceptance Criteria:**

**Given** I have just picked a goal, so `pending` is `setup_gift` (Story 2.4 later puts the look step in between)
**When** the step opens
**Then** the pengegave (NOK 10,000-30,000, config) was drawn once by `draws.py` from (seed, month, draw key) when the goal was confirmed, and is stored in the draw store
**And** surface 07 shows the gift and the first choice on one full-screen setup step with no tabs, as in the mockup (`#gave`): the inert timeline for January, the mirror, «Du har fått <beløp>», «Hva gjør du med pengegaven?» and the options of the fixed pengegave event with their engine-formatted kroner (UX-DR37)
**And** this story builds the mirror scene and the timeline that later screens reuse: the scene as inline SVG with named groups and colours from `--sc-*`, the Kalam marker on the glass, and only the artwork as `role="img"` with its text alternative and marker text from the view (UX-DR7); the timeline's heading and 12 segments, inert here (UX-DR6); Story 2.6 makes the timeline live on the hub and adds the stickers
**And** the amount reaches the current account through the ledger with a system cause, so every krone has a cause (AD-9, FR-36)

**Given** the options on surface 07
**When** I pick one
**Then** the pipeline applies it as month 1's real choice (FR-46a), the ledger moves the money with the option as the cause, including to the savings account for an option that saves (interest and transfers come in Epic 3), and `setup_gift` is done
**And** the result shows as surface 13 with one «Fortsett», and month 1 has no other event: after `setup_gift`, `pending` is `none`, never `event`

**Given** I stop playing before the first choice
**When** I log in again
**Then** the game resumes at the first step not done, with the same pengegave and no recap first, so the amount is never shown before surface 07 (FR-11, AD-17)
**And** engine tests can fix the amount by pre-filling the draw store (AD-6)

### Story 2.4: Pick my avatar

**Tier:** Extension (FR-10). If left out, the start goes straight from the goal to the pengegave

As a new player,
I want to pick how I look,
So that the mirror shows me (FR-10).

**Acceptance Criteria:**

**Given** I have just picked a goal
**When** the view's `pending` is `setup_avatar`
**Then** I see six preset looks (surface 06) that recolour the mirror figure from Story 2.3 through `--sc-hoodie` and `--sc-hoodie-shade` from DESIGN's `scene-look-1-*` to `scene-look-6-*`, and nothing is typed (UX-DR37)
**And** from this story a confirmed goal leads to `setup_avatar` first; confirming a look saves it with the pipeline and the next step is `setup_gift`

**Given** I stop playing before I have picked a look
**When** I log in again
**Then** the game resumes at the look step with no recap first, and the goal isn't asked again (FR-11, AD-17)

### Story 2.5: Make a choice in an event and see what happened

**Tier:** Core

As a player,
I want to read an event, pick one of its options and see the result,
So that my choices change my money and my life (FR-13, FR-45, FR-36).

**Acceptance Criteria:**

**Given** an active month with an event (the first one after the pengegave is April; tests here use a prepared state until Story 2.6 opens months)
**When** `pending` is `event`
**Then** the event screen (surface 12) shows the dimmed mirror, the event facts (current account, savings, debt, fixed costs) from the engine, and options as buttons with their signed kroner, and the wellbeing effect of each option is stored but not in the view until picked (FR-13)
**And** month 1's choice is not shown here: it is the pengegave on surface 07 (FR-46a, Story 2.3)

**Given** an option I can't afford from my current account
**When** the event shows
**Then** the option shows the missing amount and is locked, and sending it anyway is refused with the NFR-7 code and nothing saved (FR-45)

**Given** I pick an option
**When** the pipeline applies it
**Then** the ledger moves the money with the option as the cause, the stored wellbeing effect is saved in the state, and the result is appended to the open month's results as ids, integers and cause links
**And** every cause link points to a choice that exists in the playthrough, or to a rule, tested in the engine for every effect, now and in later stories (F10, FR-36)
**And** the response's `result.result_id` raises the same result gate as in Story 2.3 (surface 13), with money and wellbeing chips, the outcome list in the engine's order, and one «Fortsett» that closes it (UX-DR20); the wellbeing chip and the score are added in Story 2.7

**Given** I tap an option twice
**When** both requests arrive
**Then** the choice is applied once and the second gets `already_chosen` or a replay (FR-13)
**And** every amount in the view is a formatted string beside its raw integer, with U+00A0, U+2212 and «kr» (AD-13), and the frontend never formats or computes a figure

### Story 2.6: Continue to the next month

**Tier:** Core

As a player,
I want to finish a month and move on to the next one,
So that my life moves forward month by month (FR-49, FR-12, FR-14, FR-46b).

**Acceptance Criteria:**

**Given** the month's real choice is made
**When** I press the CTA on the hub (surface 08)
**Then** one continue action closes month M and opens month M+1 in the same transaction, with the rule 1 steps that exist so far, and the hub shows the new month (AD-4)
**And** continuing before the real choice is made is refused with `cannot_continue`, and a request naming the wrong month gets `wrong_month`, both with the current view

**Given** month M+1 is an active month (January, April, July or October by default)
**When** it opens
**Then** one selection step draws its event uniformly from the eligible ones (age in range, required flags set, no blocking flags, not seen this playthrough) and stores it; with none eligible the month is quiet (FR-46b, AD-8)

**Given** a quiet month
**When** it opens
**Then** the hub shows a short summary and one tap continues (FR-14)
**And** the timeline shows «<month> · <age> år · <year>» from the view's calendar fields, with 12 segments for past, current and future months (UX-DR6), the stickers on the mirror are real links with their count or state in text (UX-DR9), for the areas that are built, and the hub keeps the timeline, the mirror, «Denne måneden» with its chips, and the CTA at 320 px (UX-DR38)

**Given** the same start state, draws and choices
**When** a playthrough is replayed from its `action_log`
**Then** every month gives the same result, tested by a replay test on every PR (FR-12)
**And** after month 60's continue the playthrough's status is `completed` and further game actions get `game_ended`

### Story 2.7: See how I'm doing

**Tier:** Core

As a player,
I want to see my wellbeing and what it's made of,
So that I understand how my choices affect my life, not only my money (FR-33).

**Acceptance Criteria:**

**Given** a month is open
**When** the hub loads
**Then** the wellbeing tile (surface 18) shows the score out of 100 with its status pill and the three parts (stress, free time, social life), each with a bar, a dot and a word (UX-DR13)
**And** each `{value, band}` comes from the engine: `bad` below the threshold, `warn` from the threshold to +9, `good` from +10, with stress mirrored as 100 − stress (AD-13)

**Given** the month closes
**When** wellbeing is calculated under rule 12
**Then** the score is the parts weighted by the life goal, each part and the score stay within 0-100, and weights, start values, monthly changes and the threshold come from config
**And** an option's result shows its wellbeing chip from here on (Story 2.5)
**And** from month 19 the view carries the average so far, rounded under rule 2, and null before that

### Story 2.8: Keep playing on a bad connection and on another device

**Tier:** Core

As a player,
I want my choices saved safely when the connection drops and when I switch devices,
So that I never lose a choice or make one twice (FR-6, FR-7, FR-8).

**Acceptance Criteria:**

**Given** I pick an option and the response is lost
**When** the game client retries
**Then** it resends with the same `request_id` 2, 5 and 10 s after each failure and then every 30 s while the page is visible, shows «Prøver fortsatt …» with «Prøv igjen» after `saving_notice_s`, and retries at once on `online` (AD-18)
**And** the choice is applied once, and after a reconnect the game shows that choice's result, or the same event if the server never got it

**Given** the device goes offline
**When** I look at the game
**Then** the offline bar shows, the screen stays readable, options and continue are locked with `aria-disabled`, nothing is queued, and the change is announced once (UX-DR22)

**Given** I played on another device
**When** I come back to this tab, or make my next input after `idle_refetch_s`
**Then** the client fetches `GET /api/game` first, and if (`playthrough_id`, `state_version`) changed it drops my input and shows «Spillet ble oppdatert på en annen enhet.»
**And** a turn refusal (`wrong_month`, `already_chosen`, and `plan_changed` once Story 6.1 adds the plan) shows the same notice with the current view, and an older response never replaces a newer one (client sequence numbers)

**Given** the game client
**When** its unit tests and a two-browser Playwright test run
**Then** they cover the same `request_id` on retry, the retry schedule, the error classes, the fetch triggers, single flight, stale responses and the other-device case

### Story 2.9: Log in as a seeded test player

**Tier:** Core

As an examiner,
I want ready-made test players at useful points in a life,
So that I can see the game mid-life without playing from the start (NFR-6, AD-14, AD-20).

**Acceptance Criteria:**

**Given** the local stack starts on an empty database
**When** the entrypoint runs `cli seed --if-empty`
**Then** each seeded user is made by scripted play from month 1 through the pipeline, with a fixed seed, pinned content versions and stored choices, never by writing state
**And** seeding is refused outside `local` and `ci`, and the README lists each seeded user, its state and its password

**Given** CI
**When** the seed script runs
**Then** it asserts each seeded user's target state, and later stories add their own seeded users the same way (just before 18 with a steady wage in 7.1, in debt with a crisis due in 7.7, month 59 close to each ending in 10.5)

**Given** the seeded states
**When** `cli dump-view-fixtures` runs
**Then** it writes their player views to `frontend/src/test/fixtures/`, CI fails if they are stale, and Vitest uses them (AD-20)

### Story 2.10: See only my own game

**Tier:** Core

As a player,
I want only me to reach my game,
So that no one else can see it or play it (FR-2, NFR-3).

**Acceptance Criteria:**

**Given** two players with a game each
**When** one of them calls any game, quote or account endpoint
**Then** the server takes the player only from the session, never from anything the device sends, and answers only with that player's own game and data
**And** a request with no session, or an ended one, gets `401 not_logged_in` with no game data

**Given** I send the other player's `playthrough_id`
**When** the server handles the request
**Then** it is refused with `409 game_changed` and my own current view, and nothing changes in either game (AD-4, NFR-7)

**Given** a shared PC where one player logs out and another logs in
**When** the second player's game loads
**Then** nothing from the first player's game shows, and no late response from it enters the store (`reset()`, AD-18)
**And** tests with two players cover each of these, and every endpoint a later story adds is included in them

## Epic 3: Pengene i hverdagen

A player moves money between the current account, savings and BSU, earns interest, pays fixed and everyday costs, picks a spending level, meets unexpected expenses, and sees progress towards the life goal.

### Story 3.1: Move money to savings and earn interest

**Tier:** Core

As a player,
I want to move money between my current account and my savings account and see the interest it earns,
So that I learn how saving grows over time (FR-22, FR-45).

**Acceptance Criteria:**

**Given** I open `/penger`
**When** the bank screen (surface 17) loads
**Then** it shows my accounts as account rows with engine-formatted amounts, the transactions of the open month, and a transfer action between the current account and savings (UX-DR23)
**And** a transfer is a money action: it is allowed any time before continue, uses no real choice, moves money through the ledger, and an amount above what the account holds, zero or below, or not in whole kroner is refused with the NFR-7 code (FR-45)
**And** the transfer uses the shared amount-entry pattern, with `min`, `max` and `step` from the view and a state for each NFR-7 amount refusal, reused by every later money action that takes an amount (UX-DR44)

**Given** money in savings
**When** a month is processed
**Then** savings interest at 2.87 % a year (config) is added at the rule 1 step under rule 2's rounding, and NOK 10,000 kept for 12 months gives NOK 10,289 (worked example 2, F2)
**And** small interest is shown as it is, and the interest chip opens the interest sheet with the four-line calculation from the engine (UX-DR10, UX-DR16)

### Story 3.2: Save in a BSU

**Tier:** Core

As a player,
I want to open and save in a BSU,
So that I can learn how tax-favoured saving works (FR-22).

**Acceptance Criteria:**

**Given** I have money in my current account
**When** I deposit into the BSU
**Then** it earns 5.61 % a year (config) under rule 2, deposits are capped at NOK 27,500 per calendar year, and a larger deposit is cut to fit with the remaining cap shown (an NFR-7 non-refusal case with its own test)
**And** a deposit when the cap is used up or after the BSU has closed is refused with the NFR-7 code

**Given** a BSU
**When** an option, activity or payment needs money
**Then** the BSU never pays for it, and nothing draws on it to cover a payment

**Given** I make a full withdrawal
**When** I confirm it
**Then** the money moves to the current account, the BSU closes for the rest of the playthrough, and any tax deductions received are clawed back once tax exists (Epic 6)
**And** with no tax, the expected BSU deduction is plainly NOK 0, and the BSU still pays through interest (worked example 6)

### Story 3.3: Pay my costs and choose how much I spend

**Tier:** Core

As a player,
I want my fixed costs paid each month and to choose how much I spend,
So that I learn what everyday life costs (FR-23).

**Acceptance Criteria:**

**Given** I turn 18
**When** a month is processed
**Then** mobile and transport are charged as fixed costs at the rule 1 step, always charged even below NOK 0, each with its system cause

**Given** the month I turn 18
**When** I open the month summary
**Then** it says that I now pay my own bills, which my parents paid before (FR-23)

**Given** a new life
**When** the spending level is first used
**Then** it is Vanlig, until I change it (FR-23)

**Given** I have a wage after tax
**When** I choose «Hvor mye bruker du i måneden?» Lite, Vanlig or Mye (60 %, 75 % or 95 % of the wage after tax, config)
**Then** the change applies from the next month, spending comes on top of costs, never takes the current account below 0 and never draws on savings, and with no wage nothing is spent
**And** Lite gives −2 and Mye +2 social life in a month with spending, and Mye gives nothing in a month with debt interest (engine tests with a prepared state, since wages come in Epic 6)

**Given** an event option starts, changes or stops an everyday cost
**When** the cost runs
**Then** it is first charged in the month after the choice, links to that choice as its cause, and can be stopped from the bank only when it has no binding period left

**Given** a player with no job who keeps NOK 10,000 in savings
**When** the months up to 18 are processed
**Then** the current account never goes below 0 (worked example 15)
**And** the month summary shows total spending with pre-written example purchases that have no amounts of their own and never name an activity kind (UX-DR29)

### Story 3.4: Let savings cover what the current account can't

**Tier:** Core

As a player,
I want savings to cover a payment my current account can't,
So that I can afford a choice with the money I actually have (FR-45).

**Acceptance Criteria:**

**Given** an option costs more than my current account holds
**When** current account plus savings cover it
**Then** the option is pickable, and when it is paid, savings cover the rest with an automatic transfer that shows in the month summary («Flyttet fra sparekontoen …»)
**And** if the two together can't cover it, the option shows the missing amount and stays locked

**Given** the month's payments
**When** they are processed
**Then** each payment kind is paid as the FR-45 payment-order table says: tax, fixed and everyday costs and unexpected expenses are always charged, even below NOK 0, and spending never takes the account below 0 or draws on savings
**And** a negative current account earns no interest, can't pay for choices, and is paid first by the next income

**Given** the month summary on Hjem
**When** I open «Hva gikk pengene til?»
**Then** it lists the month's transactions, fixed costs and every automatic transfer from savings, all from the engine (UX-DR29)

### Story 3.5: Meet unexpected expenses

**Tier:** Core

As a player,
I want unexpected expenses to happen now and then,
So that I learn why a buffer matters (FR-24).

**Acceptance Criteria:**

**Given** an in-game year
**When** its months are opened
**Then** one unexpected expense (config) comes in a drawn month, of a kind that fits the player's state, drawn once and stored (AD-6)
**And** an expense tied to something the player owns is drawn only while they own it

**Given** an unexpected expense
**When** its month is processed
**Then** it is deducted at its rule 1 step with a system cause, even below NOK 0, uses no active month, and shows in the month summary
**And** a current account pushed below 0 by it can start a crisis under rule 8 once crises exist (Epic 7)

### Story 3.6: See how close I am to my life goal

**Tier:** Core

As a player,
I want to see my progress towards my life goal,
So that I know whether my choices are taking me there (FR-9c).

**Acceptance Criteria:**

**Given** I have a life goal
**When** I open the bank
**Then** the life-goal progress bar shows the engine's progress, worked out the same way as the check after month 60, with the percentage beside the heading (UX-DR23)
**And** for the debt-free goal it includes the lowest available money at a month's end from month 49

**Given** I have planned payments this month (added in Story 6.1, which builds planning)
**When** I look at the progress before continuing
**Then** it is shown after those payments and marked «Etter planlagte aktiviteter», with the figure before them beside it

## Epic 4: Året, slutten og et nytt liv

A player gets the year end each December and a recap on return, reaches one of four endings at 20 with the three choices that mattered and what would have happened otherwise, and can start a new life.

### Story 4.1: Close the year in December

**Tier:** Core

As a player,
I want a summary of the year when December comes,
So that I see what the year gave me and what comes next, and can stop for now (FR-15).

**Acceptance Criteria:**

**Given** December is open and its event or crisis, if any, is done
**When** the view's `year_end` is true
**Then** the year end (surface 23) shows as a Hjem gate after any December event or crisis step: the year's money, the year's tax (or «0 kr» with why), the expected BSU deduction when there is a BSU, what changed, and the year's average wellbeing against the trivselsmål (UX-DR35)
**And** a teaser names the next age unlock with its price, or hints at an open boomerang pair when there is none, and from month 55 points to the ending at 20; the hint at a boomerang pair is added in Story 5.5 and the year's tax and BSU deduction in Story 6.5
**And** the teaser reads the FR-18 unlock table (ages and prices), which this story adds to config; Story 4.2 shows it on `/aaret` and Story 5.3 makes the options open from it

**Given** the year end shows
**When** I press «Fortsett» or «Ferdig for nå»
**Then** it closes into the page-session record for (`playthrough_id`, month), nothing locks me out, and «Ferdig for nå» returns to the hub with a line that everything is saved (AD-17)
**And** a reload may show it once more, and it closes for good when December is continued

### Story 4.2: See my year

**Tier:** not set by the PRD: no FR requires this screen (UX surface 19), so the group decides

As a player,
I want to see how my money went month by month this year,
So that I can spot where it comes from and where it goes (UX surface 19).

**Acceptance Criteria:**

**Given** I open `/aaret` from «Året ›» or the timeline
**When** the page loads
**Then** it shows the life bar and the year chart: a diverging bar per month (income up, spending down), interest as its own small strip, each month a button with ‹ › arrow buttons as the equivalent control, a three-figure detail and a table view of the same data (UX-DR30)
**And** every figure comes from the view's money per month: twelve entries for the current calendar year, closed months from the ledger's totals, the open month marked `open: true`, later months null and inert, and the year so far summed by the engine (AD-13)

**Given** the year chart's detail changes
**When** I pick another month
**Then** the change goes through the one live region (`announce()`), not a second `role="status"` region (AD-19)
**And** the page shows what unlocks at which age, with the age and price, from the FR-18 unlock table that Story 4.1 adds to config

### Story 4.3: Get a recap when I come back

**Tier:** Extension (FR-16)

As a returning player,
I want a short recap of where I am,
So that I can pick up the game after a break (FR-16).

**Acceptance Criteria:**

**Given** I log in, complete a reset, or open the game (a page load, a back-forward cache restore, or a return to the tab) at least `recap_threshold` (1 h, settings) after my last action
**When** the first envelope arrives
**Then** the page-session record's `recapDue` is set and the recap (surface 24) shows as a full-screen gate: «Hei igjen, <nickname>. Alt er som da du gikk.», where I am, the current account, how many messages arrived this month, what is planned, and a teaser by the FR-15 rule (UX-DR35); the message count is added in Story 5.2 and what is planned in Story 6.1
**And** the gap is `server_time − last_action_at` from the envelope, never the device clock, and idle, `online` and other fetches never raise it
**And** the first envelope after a login or a page load doesn't count as a changed playthrough, so it never clears `recapDue` (AD-18)
**And** during setup no recap shows: the game goes on at the first step not done, so the pengegave isn't revealed early (FR-11, AD-17)

**Given** an open tab I come back to after at least `recap_threshold`
**When** I press anything
**Then** the recap shows first, and what I pressed is not sent and changes nothing (AD-18)

**Given** the recap shows
**When** I press its one button
**Then** `recapDue` clears and I continue to the gate or area the game needs next

**Given** a break of any length
**When** I come back
**Then** the game is exactly as I left it: no interest, events or messages ran during the break, and planned activities stay planned

### Story 4.4: Reach one of four endings at 20

**Tier:** Core; the avatar on the ending is Extension (FR-10)

As a player,
I want my life to end at 20 with an ending that reflects my money and my wellbeing,
So that I see what my choices added up to (FR-41, FR-9a).

**Acceptance Criteria:**

**Given** month 60 is continued
**When** the engine checks the endings
**Then** it checks in order: loss (a rule 8 trigger true at the end of month 59 is still true at the end of month 60), real win (goal reached under rule 13 and ending wellbeing at or above the threshold), hollow win (goal reached, below the threshold), goal not reached; the result is stored and the playthrough is `completed`
**And** ending wellbeing is the average of months 19-60 under rule 2, a value exactly at the threshold or a goal measure exactly at its target counts as reached (worked example 18), and every end state gives exactly one ending (F9, one test per end state, plus both boundaries)

**Given** the three goals
**When** the goal is checked under rule 13
**Then** savings ≥ NOK 100,000, the debt-free buffer (available money ≥ NOK 30,000 at the end of each of months 49-60 and no debt at 20, BSU not counted) and the experience (bought by the end of month 56 and available money ≥ 0 at 20) are checked from measurable state with targets from config; the experience is tested with a prepared state until Story 5.4

**Given** a trigger first true at the end of month 60
**When** the ending is chosen
**Then** it isn't a loss and the summary names it, and a minimum missed in months 58 and 59 and paid in month 60 is not a loss (worked example 11); these loss-rule tests use prepared states until crises exist (Epic 7)

**Given** a `completed` view
**When** the ending (surface 25) shows as a full-screen gate
**Then** it shows the player's avatar with its chosen look in the mirror, as in the mockup (`#slutt`, FR-10), the ending's heading and sentence, three facts (saved against the livsmål, average wellbeing against the trivselsmål with a status in past tense, debt), and one «Spill på nytt» (UX-DR34); «goal not reached» gives general advice and is never framed as failure (NFR-8)
**And** the menu stays reachable over the ending; the seeded users at month 59 close to each ending come last, in Story 10.5, since they need wages, open options and crises

### Story 4.5: See the three choices that mattered most

**Tier:** Core; grouped activities can be cut

As a player,
I want to see which of my choices mattered most and what another choice would have given,
So that I learn from my life (FR-42, FR-39).

**Acceptance Criteria:**

**Given** a completed playthrough
**When** the ending summary is built
**Then** choices are ranked by their kroner effect (the sum of money effects linked to them through FR-36, with own-account transfers, taking a loan and paying down debt counting zero but the interest that follows counting), ties go to the earliest by month and then confirmation order, and fewer than three show when fewer have an effect
**And** applied activities of the same kind rank as one group by their summed effect, counted from the first one, and one activity alone is never ranked; activity groups are tested with prepared states until Story 6.2

**Given** a hollow win
**When** the summary is built
**Then** one of the three is the choice that lowered wellbeing most (an activity group by its summed effect), taking third place if it isn't there already, or the largest system cause when no choice lowered wellbeing

**Given** a choice row on the ending
**When** I open it
**Then** it shows the FR-39 line from the engine: the interest linked to a card or loan choice (prepared states until Epic 7); otherwise the difference to the option with the most different direct kroner effect, grown with savings interest to the 20th birthday (NOK 15,000 of the pengegave spent in month 1 instead of saved gives «… 17 270 kr mer …»); otherwise a pre-written text plus the stored wellbeing difference
**And** an activity group's line shows its cost grown with interest plus linked card interest and its summed wellbeing effect (worked example 28), with a pre-written tip or explanation; no line re-runs months, and only shown choices open

### Story 4.6: Start a new life

**Tier:** Core

As a player,
I want to start a new life from 15, after my ending or before it,
So that I can try other choices (FR-43).

**Acceptance Criteria:**

**Given** my life is `completed`
**When** I press «Spill på nytt»
**Then** `playAgain` is set and the start screens show from the `completed` view's start texts and versions, and only confirming a life goal sends the start (AD-17)
**And** the start creates a new playthrough with a new pengegave; the finished one is deleted in the same transaction, and only the account's seen disclosures carry over (stored from Story 9.3)

**Given** a life in progress
**When** I choose «Nytt liv» in the menu and confirm
**Then** the end-early action ends the life (`ended`), it can't be resumed, and the start screens follow; on a `completed` or `ended` life the menu only sets `playAgain`
**And** an account never has more than one playthrough in progress, and a start while one is active is refused (NFR-7)

**Given** my life has ended
**When** I log in or come back
**Then** I see the ending summary with «Spill på nytt» instead of a recap, and the finished life stays read-only until a new life starts or the account is deleted

## Epic 5: Mobilen og valgene som står åpne

A player gets messages, invitations and offers on the phone, sees options unlock with age and stay open until taken, and meets follow-ups to earlier events.

### Story 5.1: Read my messages on the phone

**Tier:** Core

As a player,
I want an inbox on my phone with messages from friends, family, my employer and the bank,
So that the game world talks to me like real life does (FR-54).

**Acceptance Criteria:**

**Given** I open `/mobil` (or the right pane from 1100 px)
**When** the inbox (surface 10) loads
**Then** messages are split into «Nye i <måned>» and «Tidligere», with sender initials in sender colours, and a thread opens at `/mobil/[id]` (surface 11) (UX-DR17)
**And** every message is pre-written Norwegian with the nickname filled in by the server and figures from the engine, and the highlight event's copy is in the phone when it has a sender, needs no answer and isn't counted
**And** this story is tested with a few prepared messages until Story 5.2 chooses each month's messages

**Given** a message is new this month
**When** I haven't opened it in this page
**Then** it shows a coral dot and a bold row, the Mobil tab shows «Mobil, 2 nye» to screen readers, and the sticker shows «2 nye» (UX-DR40)
**And** opening it clears the mark in this page only: reading is never stored, a reload shows it again, and there is no unread badge across months (#112)

**Given** the month opens with a new message below 1100 px
**When** the hub shows
**Then** a toast (surface 09) shows first in reading order with the sender and one line, opens the thread, closes with × or Esc with focus to «Denne måneden», never closes by itself, never takes focus, and is announced once (UX-DR18)

### Story 5.2: Get the right messages each month

**Tier:** Core; invitations and info messages can be cut to their minimum

As a player,
I want messages that fit my age and my situation,
So that the phone feels alive without flooding me (FR-55).

**Acceptance Criteria:**

**Given** a month opens
**When** the selection step runs with the event (AD-8)
**Then** drawn messages (info, drawn offers) are chosen by age range and flags and stored, triggered messages (bank messages, other offers) are added, and one-off messages never repeat
**And** the messages that belong to later stories are added by them: invitations in 6.2, the employer's extra shifts and hours answers in 6.6, the gift moped in 8.4, and the savings target's thresholds in 9.4; goal 1's thresholds work from here

**Given** savings reach 25, 50, 75 or 100 % of the savings target or goal 1
**When** the month opens
**Then** a bank message for that threshold arrives once per target, only the highest one per month, and one savings-interest message arrives the first month interest passes NOK 50

**Given** more messages are due than fit
**When** the month's messages are chosen
**Then** at most 3 new messages arrive (config), offers and the event copy always arrive and don't count, the fill order is bank, invitations, info, and a bank message that doesn't fit comes next month
**And** each message's arrival month and `new` flag are in the view (AD-13), and the recap from Story 4.3 says how many messages arrived this month (FR-16)

### Story 5.3: Unlock options as I grow up

**Tier:** Core

As a player,
I want new options to open as I get older,
So that the game grows with me from 15 to 20 (FR-18).

**Acceptance Criteria:**

**Given** the FR-18 unlock table in config (added in Story 4.1, the year end)
**When** a month opens
**Then** each option opens in its month (savings and BSU from month 1, part-time job month 3, moped licence month 13, part-time up to 40 h from 19, summer jobs offered 18/30/42 and paid 19/31/43, car licence draw and paid licence 37, credit card 37 offered 39, consumer loan 37 offered 49, the experience 44-56 and only for players with life goal 3, full-time job offered 54 and starting 55), and only age unlocks
**And** an option that a later story builds (jobs in 6.3 and 6.4, the card in 7.1, the loan in 7.3, licences and moped in 8.2-8.5) is only a row in the table until that story adds the option and its offer message
**And** an option before its month is refused by the engine (NFR-7), and the view may show its unlock age and price as a locked post-it (UX-DR31)

**Given** an offer's month comes
**When** the month opens
**Then** its offer message always arrives in that month, unless it is already taken, closed or blocked by the one-at-a-time table (FR-55)
**And** teasers and recaps (FR-15, FR-16) name the next unlock from the same table

### Story 5.4: Take options that stay open, including the big experience

**Tier:** Core

As a player,
I want offers like the big experience to stay open until I can take them,
So that I can save up instead of being rushed (FR-48, FR-9a).

**Acceptance Criteria:**

**Given** an open option
**When** I see it in its offer message, the bank or the job view
**Then** it is the same option with the same terms everywhere, and taking it from any of them is one action with a cause link that isn't the month's real choice
**And** when I can't pay yet, it shows the missing amount and stays open; when it is blocked for another reason, it shows what's missing and taking it is refused (NFR-7)

**Given** a dated offer
**When** its last day passes
**Then** it shows as expired and taking it is refused

**Given** the one-at-a-time table (#83)
**When** an option's rule doesn't allow another
**Then** it isn't offered again until the rule allows it: licences and the experience once per playthrough, one moped at a time, one credit card per playthrough, one consumer loan at a time, one job at a time, one family loan and one payment plan at a time
**And** here the rules are built and tested with the experience and prepared options; the job view comes in 6.3, and each other option comes with its own story in Epics 6-8

**Given** I chose life goal 3 and the experience (NOK 60,000, config) is offered in month 44
**When** I buy it by the end of month 56
**Then** it is paid from the current account and savings, never on credit, and buying it with less available money after debt than its price is refused (FR-9a, rule 13)
**And** a player with life goal 1 or 2 never gets the offer, and taking it anyway is refused (FR-18, FR-48, NFR-7)

### Story 5.5: Meet follow-ups to my earlier choices

**Tier:** Core

As a player,
I want earlier choices to come back as follow-up events,
So that I see that choices have consequences later (FR-46c).

**Acceptance Criteria:**

**Given** a boomerang opener is chosen
**When** its flag is set
**Then** the follow-up is due after a delay drawn from its pair's range and stored, and takes the first active month at or after that
**And** an opener is drawable only if its longest delay lands by the last active month, and a follow-up whose flag was cleared is dropped

**Given** several events are due in one active month
**When** the month opens
**Then** the order is crisis, card warning, follow-ups in due order, drawn event; a pushed-out follow-up takes the next active month or makes month 59 or 60 active, and if none is left it is dropped and reported (FR-58); the card warning and the crisis join the order in 7.6 and 7.7
**And** with nothing left to unlock, the teasers in the year end and the recap hint at an open boomerang pair (FR-15, Stories 4.1 and 4.3)

## Epic 6: Jobb, fritid og månedsplan

A player takes a part-time, summer or full-time job, asks for more or fewer hours, takes extra and one-off shifts, earns wages and pays tax, and plans activities in the free evenings.

### Story 6.1: Plan my free evenings

**Tier:** Core

As a player,
I want to place activities on my free evenings,
So that I choose how to spend my free time (FR-52, FR-53).

**Acceptance Criteria:**

**Given** a month opens
**When** the plan is built
**Then** the number of free evenings is the month's free time ÷ 20, rounded down, between 1 and 4 (config), fixed for the month, and school (and work, once I have a job) shows as one locked line

**Given** I open `/plan`
**When** the plan (surface 15) loads
**Then** each evening is a slot row («Kveld 1», title, cost · effect), empty ones show «Tom», and below 1100 px «+ Legg til» opens the add list in a sheet while from 1100 px the list is always visible and + places on the first free evening (the place action without `slot`) (UX-DR14)
**And** each activity in the add list shows its cost and effect, placed ones show a check, and with no free evening the add buttons lock with «Alle de frie kveldene er fylt opp. Fjern en aktivitet først.»

**Given** an activity I can afford
**When** I place or remove it
**Then** planning moves no money, removal is free while the month is open, an activity is placed at most once a month, an unaffordable one shows the missing amount and can't be placed, and «Samme kvelder som i <måned>» re-places last month's activities with the same checks
**And** empty evenings never block continue, the plan's total is the engine's activity cost only, continue carries `plan_version` (that planning works in crisis months is tested in Story 7.7); the library has at least 5 basic activities, 2 of them free for ages 15-20, and the activity catalogue with sourced prices (#57) is in place first
**And** the recap from Story 4.3 says what is planned (FR-16), and the life-goal progress in the bank is shown after the planned payments (Story 3.6, FR-9c)

### Story 6.2: Live my planned activities when the month ends

**Tier:** Core; invitation activities can be cut to their minimum

As a player,
I want my planned activities to happen when I continue,
So that they change my wellbeing and my money (FR-53, FR-55).

**Acceptance Criteria:**

**Given** activities are planned
**When** I continue
**Then** they apply in slot order at the end of the choice step, each rechecked for eligibility and payment under FR-45, and one that fails is dropped with a «Ble ikke noe av» note in the next month's opening (worked example 25, UX-DR15)
**And** each is paid like an event option, on top of spending (the card half of worked example 27 comes in Story 7.2), and links to the activity as its cause

**Given** an applied activity
**When** wellbeing is calculated
**Then** its stress and social effects count for that month's score only, within ±15 per part per month (config), and it is a choice with a cause link but not the month's real choice
**And** the wellbeing tile shows stress and social life both as the usual value and as this month's value with activities («Vanligvis n»), so I see what the activities added (FR-33, UX-DR13)

**Given** an invitation message
**When** it arrives (0-2 a month, each at most once per in-game year, FR-55)
**Then** its activity is available in the plan that month only, and «Legg i planen» places it while «Nei takk» only closes the message (UX-DR17)
**And** the month summary lists last month's evenings and their cost (UX-DR29)

### Story 6.3: Get a job and earn a wage

**Tier:** Core

As a player,
I want to take a part-time job and later a full-time job,
So that I earn my own money (FR-20, FR-47, FR-56).

**Acceptance Criteria:**

**Given** a job offer has arrived (part-time from month 3, full-time offered in month 54 and starting in month 55, FR-18)
**When** I take it from the offer message or the job view
**Then** I get the offer's weekly hours from the next month, I have at most one part- or full-time job, and taking it is a choice with a cause link
**And** I can quit in any month, from the next month, which also ends any extra shifts

**Given** I have a job
**When** the income step runs
**Then** monthly pay is weekly hours × 52 / 12 × the Virke/HK hourly rate for my age, in whole kroner, at most 173 h a month (rule 10), with `Decimal` arithmetic; a full-time week of 37.5 h at 18+ pays NOK 31,694 and 40 h pays NOK 33,742
**And** the weekly limit is 12 h in months 1-18 and 40 h from month 19, checked against the month a change applies from, and a full-time job is 37.5 h, raisable to 40 by an hours offer

**Given** I open `/jobb` (or the right pane from 1100 px)
**When** the job view (surface 16) loads
**Then** it shows workplace and role, the hourly rate for my age, weekly hours and this month's hours, the rule 10 limit, expected monthly pay and current offers, and with no job the open job offers or when the next one unlocks (UX-DR19); hours offers and extra shifts are added in Story 6.6 and one-off shifts in Story 6.7
**And** each job action previews the kroner left after spending each month and next month's free evenings, with a warning when free time would fall below 50

### Story 6.4: Work a summer job

**Tier:** Core

As a player,
I want to take a summer job in July,
So that I can earn extra money in the holidays (FR-20, FR-47).

**Acceptance Criteria:**

**Given** a summer job is offered (months 18, 30 and 42, paid in months 19, 31 and 43)
**When** I take it
**Then** it pays its hours at my age's rate at July's income step, and a summer job at 16 of 120 h at NOK 139.40 pays NOK 16,728 (worked example 1, F7); that no tax is due is checked in Story 6.5

**Given** a summer job and part-time hours in the same July
**When** July's income step runs
**Then** they share one cap of 173 h, and the summer job is cut to fit using that month's hours with extra shifts (30 h a week of part-time cuts 120 h to 43 h), an NFR-7 non-refusal case with its own test; hours above the offer's and extra shifts are prepared states until Story 6.6
**And** if the cut leaves 0 h, the summer job is cancelled with a note (non-refusal case with its own test)

**Given** my hours leave 0 h when the offer is made
**When** the offer message arrives
**Then** it shows that the monthly cap is full and why, and the summer job can't be taken

### Story 6.5: Pay tax on my wages

**Tier:** Core

As a player,
I want tax worked out from my year's wages,
So that I learn how tax and trygdeavgift work (FR-21).

**Acceptance Criteria:**

**Given** wage income in a calendar year
**When** tax is calculated under rule 3 at 2026 rates
**Then** each in-game year is one tax year, trygdeavgift is 5.1 % in in-game years 1-2 and 7.6 % from year 3, and an 18-year-old earning NOK 110,000 pays NOK 2,588, all of it trygdeavgift (worked example 5, F8)
**And** the summer job in worked example 1 has no tax (F7)
**And** tax is charged at its rule 1 step with a system cause and shows in the month summary

**Given** December
**When** the year end shows
**Then** it carries the year's tax and the expected BSU deduction under rule 9, and the deduction is paid when December is continued
**And** a full BSU withdrawal takes any deductions received from the payout at once

### Story 6.6: Ask for more or fewer hours and take extra shifts

**Tier:** Core

As a player,
I want to ask my employer for more or fewer hours and take extra shifts,
So that I can balance money and free time (FR-47).

**Acceptance Criteria:**

**Given** I have a job and no request pending
**When** I press «Spør om flere timer» or «Spør om færre timer»
**Then** the employer answers with a message next month: an offer of 2 h a week more or fewer (config), within rule 10 for the month it applies from and never below 4 h (config), or a no with the reason when I am at the limit or the floor
**And** a second request while one is pending or an offer is open is refused, and the buttons show «Svar på tilbudet først.» (UX-DR19)

**Given** an hours offer
**When** I answer «Ja takk» or «Nei takk» in its month
**Then** a yes changes weekly hours from the next month and leaves running extra shifts as they are; an offer not answered by the month's end lapses, and an answer to an offer that isn't open is refused
**And** the offer shows the kroner left after spending each month and next month's free evenings, and warns below 50 free time (worked example 25)

**Given** extra shifts are offered (by an event option or an employer message) to a player with a job, below the limit, with none running and a later income step left
**When** I take them
**Then** they add +4 h a week (config) for 3 months (config) from the next month, capped at the weekly limit, and can be ended from the job view from the next month («Avsluttet», «Slutter etter <måned>»)
**And** weekly hours and extra shifts never take an evening in the plan
**And** if an hours change or extra shifts would cut a summer job I have taken, the game warns before I confirm

### Story 6.7: Take one-off shifts

**Tier:** Core

As a player with a job,
I want to take a single shift on a free evening,
So that I can earn a bit more when I choose to (FR-47).

**Acceptance Criteria:**

**Given** I have a job
**When** I open the job view, or the plan's add list with its Fritid | Jobb toggle (`aria-pressed`)
**Then** I see this month's one-off shifts with name, hours and signed pay with its month («558 kr lønn i desember»), and none are offered in month 60

**Given** I place a one-off shift
**When** it is placed
**Then** it takes an evening, its pay is its hours × my age's rate in the month worked, rounded once when placed, paid and taxed with next month's wage at its income step (#114), and linked to the shift as its cause
**And** it can be placed only within rule 10 (the weekly limit × 52 / 12) and the 173 h cap, has no wellbeing effect of its own, and shows «I planen» once placed

## Epic 7: Kort, lån og kriser

A player can take a credit card and a consumer loan, borrow from family, gets the card warning, and handles crisis months with up to three steps and a payment plan.

### Story 7.1: Get a credit card and choose how to pay the bill

**Tier:** Core; the tip is Extension (FR-19); the cost in kroner stays

As a player from 18,
I want to get a credit card and decide how the bill is paid,
So that I learn what a card really costs (FR-26, FR-19).

**Acceptance Criteria:**

**Given** I am 18 or older with a steady wage, and the card offer has arrived (month 39, open from month 37)
**When** I take the card
**Then** it has the limit fixed for the playthrough (config, default NOK 10,000), I choose to pay the whole balance, the minimum, or a fixed amount of at least the minimum in NOK 100 steps, and it stays open if my wage stops later
**And** the offer message carries a tip, a teaching point and the engine's cost in kroner (FR-19), and taking a card under 18, without a steady wage, or a second card in the playthrough is refused (NFR-7)

**Given** a card balance
**When** the debt step runs
**Then** the bill is paid by the chosen mode and never takes the current account below 0, paying less than the minimum counts as a missed minimum and leaves an overdue amount that later payments cover first (rule 5), and a mode change applies from the next bill
**And** a NOK 3,200 balance with only the minimum paid is paid off after 13 months, NOK 3,606 in total (worked example 4, F3)

**Given** the card panel on the bank screen
**When** it shows
**Then** it has used of limit, the yearly rate, this month's interest and the minimum-only total cost in kroner from the engine, «Ikke betalt» with «Betal … nå» when overdue, and «Slik betaler du kortregningen» as three option radio cards with a stepper for the fixed amount (UX-DR24)
**And** an extra payment lowers the balance at once without undoing this month's interest, and the seeded user «just before 18 with a steady wage» is added and asserted in CI (NFR-6)

### Story 7.2: Use the card for purchases

**Tier:** Core

As a player with a card,
I want to choose whether purchases go on the card,
So that I control when I borrow (FR-26).

**Acceptance Criteria:**

**Given** card use is on («Bruk kortet», a switch saying where purchases go)
**When** I buy something or a card-payable monthly cost is due
**Then** it goes on the card if it fits under the limit; an event purchase that doesn't fit is paid whole from the current account, then savings, and the game says the card was declined (an NFR-7 non-refusal case with its own test)
**And** an activity is never split between the card and the accounts (worked example 27)

**Given** interest takes the balance above the limit
**When** I try to buy on the card
**Then** the card takes no purchases until the balance is below the limit again

**Given** card use is on
**When** I turn it off
**Then** it is off at once, and purchases are paid from the accounts

### Story 7.3: Take a consumer loan

**Tier:** Extension (FR-25)

As a player from 18,
I want to see what a loan costs before I take it,
So that I understand borrowing before I do it (FR-25).

**Acceptance Criteria:**

**Given** I am 18 or older with a steady wage, not in months 59-60, with no loan running
**When** I open «Se hva et lån koster»
**Then** the loan sheet shows what I can borrow (NOK 5,000 up to 3× the average monthly wage of the last three months minus other debt except family loans, rounded down to NOK 1,000) and the engine's quote for each term (12, 24, 36 months, config): amount, rate, monthly payment, last payment, total and cost (UX-DR25)
**And** another amount in NOK 1,000 steps gets its quote from `GET /api/game/quote`, kept in the sheet and never in the store (AD-13, AD-18)

**Given** I take a loan
**When** it is paid out
**Then** it is an annuity at 15 % a year (rule 4), and NOK 20,000 over 12 months gives NOK 1,805 a month, a final NOK 1,808 and NOK 21,663 in total (worked example 3, F1); instalments are always charged, even below NOK 0
**And** a term outside the config list, an amount outside the range or not in NOK 1,000 steps, a second loan, or a loan in months 59-60 is refused (NFR-7); early payoff is free, and a loan running past 20 counts as debt at the ending

### Story 7.4: Ask my family for help

**Tier:** Core

As a player in trouble,
I want to ask my family for help,
So that I learn what family can and can't do (FR-27).

**Acceptance Criteria:**

**Given** an event offers asking family (crisis months are added in Story 7.7, with the same rules)
**When** I ask
**Then** whether they can help, and how much, was drawn once for that event or month and stored, and asking again shows the same answer («Hun har allerede lånt deg 500 kr»), moves no money and uses no crisis step
**And** asking never guarantees a loan: family may lend all or part of what I need, give money, only give advice, or say they can't help (FR-27)

**Given** family lends me money
**When** the loan is set up
**Then** it is 0 % with equal instalments and the last one making the total exact (NOK 5,000 over 6 months is 833 × 5 + 835, worked example 8), one family loan at a time, from 15
**And** an instalment the accounts can't cover moves to the end and raises stress (up to 50), never takes the account below 0, what's left at 20 is debt, and family loans don't count in the debt trigger
**And** I can pay off the rest early from the bank with no fee, paid from the current account and then savings, and an amount above what they hold is refused (FR-45, NFR-7)
**And** while a family loan runs, family can still give advice or a gift but lends nothing more

### Story 7.5: Know before I continue whether a crisis is coming

**Tier:** Core

As a player,
I want to see whether continuing would start a crisis,
So that I can fix it first (FR-32a, FR-49).

**Acceptance Criteria:**

**Given** the end of every month
**When** rule 8 is checked
**Then** the triggers are: current account below 0; card minimum missed two months in a row; net debt (excluding family loans, minus savings and a positive current account) above the larger of 3× the 3-month average wage and NOK 5,000, with one test per trigger (F4)
**And** a true trigger with no cooldown makes the next month a crisis month (its event and steps come in Story 7.7; until then it opens as an ordinary month); the cooldown is two months (config) except in month 60, and triggers during a cooldown are still shown

**Given** the bank before continuing
**When** it shows
**Then** the crisis check band says «Ingen krise på vei» or «Krise i <måned> hvis du fortsetter nå» from the engine's trigger status after the planned payments, and when a trigger is true the hub's continue opens a confirm sheet with «Til banken» first and «Fortsett likevel» second (UX-DR26)
**And** the view's `continue_warning` carries the month 59 text (a crisis in month 60 is the last chance) and the month 60 text (a trigger still true gives the loss ending), and in month 60 actions that only work next month are hidden or marked as having no effect

**Given** a crisis month opens
**When** the triggers are rechecked and none is true
**Then** the crisis is skipped with no stress and no cooldown, a `crisis_skipped` note shows in «Denne måneden», and the month's event is chosen again (worked example 10)

### Story 7.6: Get a card warning

**Tier:** Core

As a player who didn't pay the whole card bill,
I want a clear warning about what it costs,
So that I understand card interest before it grows (FR-31).

**Acceptance Criteria:**

**Given** a bill not paid in full after a month with a bill paid in full or no balance
**When** that month runs
**Then** a card warning event comes that month, before the next interest charge, and makes a quiet month active (FR-46a)
**And** it shows this month's interest, the balance, the minimum-only time and total cost with an (i), and whether I couldn't pay or chose to pay less, with no scolding (UX-DR27)

**Given** I chose to pay less
**When** the warning shows
**Then** one option switches to paying the whole balance, and other options only when they are possible
**And** a NOK 6,000 bill with NOK 4,000 available gives NOK 113 interest (worked example 7), and the warning doesn't start a crisis

### Story 7.7: Get through a crisis month

**Tier:** Core

As a player in a crisis,
I want up to three chances to fix it, with a way out every time,
So that I learn to handle a money crisis (FR-32b, FR-32c).

**Acceptance Criteria:**

**Given** a crisis month
**When** it opens
**Then** its crisis event is drawn among those that fit the most urgent trigger (below zero, missed minimum, debt) and my age, preferring the one seen longest ago, stored, and it names all true triggers; the library has about 10 crisis events covering every trigger possible at each age
**And** when a card warning is due in the same month, the crisis shows its figures first and the warning counts as shown (FR-31)

**Given** a crisis step
**When** it shows (the Hjem gate, with «Valg n av maks 3» and three step pills)
**Then** it offers only options possible now, each saying when it lands, always asking family (Story 7.4) and doing nothing, with the payment plan added in Story 7.8, and hides options landing after month 60 (UX-DR27)
**And** money actions, open options and the plan stay available, use no step, and the triggers are rechecked after them; money arriving goes first to a negative current account and then to overdue minimums

**Given** a step is taken
**When** the triggers are rechecked
**Then** the crisis ends when none is true, when I ignore it, or after the third step, the end screen lists what changed, continue is refused (`cannot_continue`) until then, and a crisis never ends the game before 20
**And** ignored debt keeps growing and starts new crises after each cooldown, the loss ending's tests (Story 4.4) now run on played states, and the seeded user «in debt with a crisis due» is added and asserted in CI (NFR-6)

### Story 7.8: Split my card debt into a payment plan

**Tier:** Core

As a player in a crisis with card debt,
I want to split the whole card balance into monthly payments,
So that I can get out of card debt step by step (FR-32b, rule 15).

**Acceptance Criteria:**

**Given** a crisis step with card debt
**When** I choose «Del opp hele kortgjelden»
**Then** the card balance becomes a 12-month annuity at the card's rate, the card is blocked until the plan is paid, card use turns off, and the instalment shows against what's left each month (worked example 12)
**And** turning card use on while the plan runs is refused (NFR-7), only one payment plan runs at a time, instalments are always charged even below NOK 0, and the plan can be paid off early

## Epic 8: Moped, lappene, rommet og hele innholdet

A player takes the moped licence, buys and sells a moped, gets or pays for the car licence and borrows the parents' car, sees belongings in the mirror's room, and plays the full event library with tips.

### Story 8.1: See my belongings in the room

**Tier:** Core; with 3 layers; more can be cut

As a player,
I want the room in the mirror to show what I own,
So that my choices are visible in my world (FR-34).

**Acceptance Criteria:**

**Given** the mirror scene on the hub
**When** the view loads
**Then** one named SVG group per belonging (`-lag-moped`, `-lag-hjelm`, `-lag-lapp`, `-lag-sprekk`) is switched only by the view's room-layer state ids, at most 6 layers, with three in the MVP: moped (none or owned), licence (none, moped or car) and phone (whole, cracked or used) (UX-DR8, AD-19)
**And** the layers follow the playthrough's flags (derived flags for typed facts, AD-16), so the room looks the same after a reload and on every device
**And** the moped and licence layers are tested with prepared flags until Stories 8.2-8.5 set them, and the phone layer until events in 8.6-8.10 change the phone

**Given** a choice that changes a belonging
**When** its result shows
**Then** the layer changes in the same view, the change is announced and listed in the outcome list, and several changes in one month all show
**And** the scene's text alternative and marker text come from the view, name every belonging, and say what just changed (NFR-2, UX-DR7)

### Story 8.2: Take the moped licence

**Tier:** Core

As a player from 16,
I want to pay for the moped licence,
So that I can own a moped (FR-28).

**Acceptance Criteria:**

**Given** month 13 or later
**When** the moped licence is offered as an open option (FR-48)
**Then** it costs the real price of the lessons, the mandatory course and the licence, each with a source and a date in config, and I have the licence once it's paid (payment only; the driving game is V2)
**And** it can be taken once per playthrough, the recap's teaser names its cost, and the licence layer shows it in the room

### Story 8.3: Buy, own and sell a moped

**Tier:** Core; the parents' share of the insurance can be cut

As a player with the moped licence,
I want to buy a moped, pay what it costs to run, and sell it when I want,
So that I learn what owning something costs over time (FR-29, FR-23).

**Acceptance Criteria:**

**Given** I have the moped licence and own no moped
**When** I buy one
**Then** it is paid like an open option, I own one moped at a time, and buying one without the licence or while owning one is refused (NFR-7)
**And** whether the parents pay part of the insurance is drawn once when I get it and stored

**Given** I own a moped
**When** a month is processed
**Then** insurance (flat NOK 3,000 a year in the MVP, per month) and fuel are charged instead of the transport ticket, never both, moped repairs (FR-24) and moped events can be drawn, and none of these happen in months I don't own it
**And** the resale value starts at the price paid, drops by 15 % of it a year, a little each month, never below 20 % (rule 14), and a used moped sold after two years fetches NOK 8,152 (worked example 19)

**Given** I own a moped
**When** I sell it in any month
**Then** I get its current resale value, selling it is also a crisis option (FR-32b), public transport comes back from the next month, the moped leaves the room, and the sale counts as a money effect when it happens (FR-42)

### Story 8.4: Get a moped as a gift

**Tier:** Can be cut (gift mopeds, FR-29)

As a player with the moped licence,
I want the chance of getting a used moped from my family,
So that luck is part of life, stated as a fact (FR-29, FR-55).

**Acceptance Criteria:**

**Given** I have the moped licence and own no moped
**When** a month opens
**Then** a family message may offer a used moped as a drawn offer, with its chance per in-game year from config, at most once per playthrough, and takeable only that month

**Given** I take the gift
**When** it applies
**Then** I own a used moped with its resale value starting at the used price, and every rule in Story 8.3 applies to it

### Story 8.5: Get the car licence and borrow the car

**Tier:** Can be cut (FR-30, with car fuel in FR-23)

As a player turning 18,
I want to get the car licence, as a gift or by paying, and borrow my parents' car,
So that I meet the costs and choices that come with driving (FR-30, FR-23).

**Acceptance Criteria:**

**Given** month 37
**When** it opens
**Then** the engine draws once whether the parents give the car licence (frequency in config), stores it, and one family message tells the result
**And** the gift applies at once and costs nothing, and a player with the gift is never offered the paid licence

**Given** no gift
**When** I pay for the car licence
**Then** it costs a real, sourced and dated price, is a payment only, and can be taken once per playthrough; buying it before the draw or after a gift is refused (NFR-7)

**Given** I have a car licence
**When** I start or stop borrowing the parents' car from the bank
**Then** fuel is charged as a transport cost only in months I borrow it, goes on the card first when card use is on, and borrowing opens car events
**And** the licence layer shows the car licence in the room

### Story 8.6: Play the events of year 1 (age 15)

**Tier:** Core; events beyond the minimum of 40 can be cut, invitations can be cut to their minimum, and tips are Extension (FR-19)

As a player aged 15,
I want varied events written for my age,
So that this year of my life feels different (FR-17, FR-19, NFR-8).

**Acceptance Criteria:**

**Given** `content/library/v1/` and in-game year 1 (months 1-12)
**When** the content for the year is complete
**Then** at least 8 regular events that aren't follow-ups and need no flags, and at least 6 invitations, have an age range that covers the year (config)
**And** every regular event has a free option, at least half of the events before 18 have two free options, and each item carries its LK20 codes, valid from 1 August 2026

**Given** an event or offer with a tip
**When** it shows
**Then** the tip is general, pre-written, ignorable, has no game effect and is never personal advice (FR-19)
**And** all text is plain Norwegian a 15-year-old understands, options read as actions, nothing scolds, and there is no tobacco or alcohol (NFR-8); each event is approved by PR review

### Story 8.7: Play the events of year 2 (age 16)

**Tier:** Core; events beyond the minimum of 40 can be cut, invitations can be cut to their minimum, and tips are Extension (FR-19)

As a player aged 16,
I want varied events written for my age,
So that this year of my life feels different (FR-17, FR-19, NFR-8).

**Acceptance Criteria:**

**Given** `content/library/v1/` and in-game year 2 (months 13-24)
**When** the content for the year is complete
**Then** at least 8 regular events that aren't follow-ups and need no flags, and at least 6 invitations, have an age range that covers the year (config)
**And** every regular event has a free option, at least half of the events before 18 have two free options, and each item carries its LK20 codes, valid from 1 August 2026

**Given** an event or offer with a tip
**When** it shows
**Then** the tip is general, pre-written, ignorable, has no game effect and is never personal advice (FR-19)
**And** all text is plain Norwegian a 15-year-old understands, options read as actions, nothing scolds, and there is no tobacco or alcohol (NFR-8); each event is approved by PR review

### Story 8.8: Play the events of year 3 (age 17)

**Tier:** Core; events beyond the minimum of 40 can be cut, invitations can be cut to their minimum, and tips are Extension (FR-19)

As a player aged 17,
I want varied events written for my age,
So that this year of my life feels different (FR-17, FR-19, NFR-8).

**Acceptance Criteria:**

**Given** `content/library/v1/` and in-game year 3 (months 25-36)
**When** the content for the year is complete
**Then** at least 8 regular events that aren't follow-ups and need no flags, and at least 6 invitations, have an age range that covers the year (config)
**And** every regular event has a free option, at least half of the events before 18 have two free options, and each item carries its LK20 codes, valid from 1 August 2026

**Given** an event or offer with a tip
**When** it shows
**Then** the tip is general, pre-written, ignorable, has no game effect and is never personal advice (FR-19)
**And** all text is plain Norwegian a 15-year-old understands, options read as actions, nothing scolds, and there is no tobacco or alcohol (NFR-8); each event is approved by PR review

### Story 8.9: Play the events of year 4 (age 18)

**Tier:** Core; events beyond the minimum of 40 can be cut, invitations can be cut to their minimum, and tips are Extension (FR-19)

As a player aged 18,
I want varied events written for my age,
So that this year of my life feels different (FR-17, FR-19, NFR-8).

**Acceptance Criteria:**

**Given** `content/library/v1/` and in-game year 4 (months 37-48)
**When** the content for the year is complete
**Then** at least 8 regular events that aren't follow-ups and need no flags, and at least 6 invitations, have an age range that covers the year (config)
**And** every regular event has a free option, and each item carries its LK20 codes, valid from 1 August 2026

**Given** an event or offer with a tip
**When** it shows
**Then** the tip is general, pre-written, ignorable, has no game effect and is never personal advice (FR-19)
**And** all text is plain Norwegian a 15-year-old understands, options read as actions, nothing scolds, and there is no tobacco or alcohol (NFR-8); each event is approved by PR review

### Story 8.10: Play the events of year 5 (age 19)

**Tier:** Core; events beyond the minimum of 40 can be cut, invitations can be cut to their minimum, and tips are Extension (FR-19)

As a player aged 19,
I want varied events written for my age,
So that this year of my life feels different (FR-17, FR-19, NFR-8).

**Acceptance Criteria:**

**Given** `content/library/v1/` and in-game year 5 (months 49-60)
**When** the content for the year is complete
**Then** at least 8 regular events that aren't follow-ups and need no flags, and at least 6 invitations, have an age range that covers the year (config)
**And** every regular event has a free option, and each item carries its LK20 codes, valid from 1 August 2026

**Given** an event or offer with a tip
**When** it shows
**Then** the tip is general, pre-written, ignorable, has no game effect and is never personal advice (FR-19)
**And** all text is plain Norwegian a 15-year-old understands, options read as actions, nothing scolds, and there is no tobacco or alcohol (NFR-8); each event is approved by PR review

**Given** all five years are written
**When** the library is complete for the playtest
**Then** it has at least 40 regular events in total (target 50-60), about 55 % before 18, at least 8 boomerang pairs, 12-20 invitation activities, and every mechanism has events before and after 18 where its rules allow, with an LK20 coverage report

**Given** the game with zero AI calls
**When** a playthrough is played end to end
**Then** it works with the library alone (F6)

### Story 8.11: Check the content on every pull request

**Tier:** Core

As the team,
I want an automated content check that plays seeded runs on every pull request,
So that a content or config change can't silently break the rules (FR-58, FR-9b, FR-43).

**Acceptance Criteria:**

**Given** a pull request
**When** the content check runs in CI
**Then** it checks every hard gate: schemas and fixed lists, library minimums, boomerang and mechanism coverage, the open-option identity (FR-48), at most one active month per seeded run with no eligible event, at most 2 months a year with no eligible invitation, replay variety (random-choice pairs share at most two-thirds of regular events, same-seed pairs with different choices differ in a follow-up), no hollow-win run at 50 or above (FR-33), and the second reference run reaching goals 1 and 2 (FR-9b)
**And** it writes the reports (free-option share at NOK 0, LK20 coverage, drawn events left per year, dropped follow-ups, ending wellbeing at 1-4 slots, invitations per year, worked example 17b and careless run 21c)

**Given** seeded runs
**When** they play
**Then** they follow the careless and careful policies of FR-9b with unexpected expenses from the run's seed, and every careless run in worked example 21 misses all three goals while the reference run (worked example 20) reaches all three

**Given** the library is not frozen
**When** a gate other than the schema gate and the open-option gate fails
**Then** it reports a warning; from the freeze before the playtest every gate fails the check

## Epic 9: Forstå tallene

A player can ask «Hvorfor?», sees «Tidligere valg» on effects of earlier choices, reads «Forenklet» notes and «Om tallene», pins a savings target and sees what comes next month.

### Story 9.1: Ask why something changed

**Tier:** Core (FR-38), never cut

As a player,
I want to press «Hvorfor?» on a change,
So that I understand which choice or rule caused it (FR-38).

**Acceptance Criteria:**

**Given** a result or a money change with cause links
**When** I press «Hvorfor?»
**Then** it expands in place (`aria-expanded`) with the engine's explanation built from the cause links, naming the choice behind the change (UX-DR20)
**And** an effect with a system cause (wage, tax, mobile, unexpected expense, spending) is explained from the rules

**Given** an effect with shared causes, such as interest on a balance built from several choices
**When** it is explained
**Then** it lists up to the three largest whole-kroner shares and sums the rest, and the shares add up to the effect (FR-36)
**And** the BSU comparison line («I BSU ville dette vært …») is built only if the team keeps the in-play lines (cut list)

### Story 9.2: See when an earlier choice comes back

**Tier:** Extension (FR-37)

As a player,
I want to see when an effect comes from a choice I made earlier,
So that I notice how choices echo over time (FR-37).

**Acceptance Criteria:**

**Given** an effect with a cause link to an earlier choice
**When** it shows on a result, the hub or the bank
**Then** a «Tidligere valg» note shows a cobalt history icon and one sentence naming the month and the choice («Tidligere valg: Du sa ja til ekstravakter i september.»), with the text read out by screen readers (UX-DR15)
**And** an effect with no cause link to an earlier choice never shows the note, and the note's text comes from the view (AD-13)
**And** every note names a choice that exists in the playthrough (F10)

### Story 9.3: Read what the game simplifies

**Tier:** Extension (FR-40). A-23 and SM-2 rest on it, so the team aims to build it

As a player,
I want the game to tell me where it simplifies real life,
So that I know what's real and what isn't (FR-40).

**Acceptance Criteria:**

**Given** a mechanism with a disclosure (D1-D26) appears for the first time on my account
**When** its screen shows
**Then** a «Forenklet» note card with the text (at most 62ch) and a small «Skjønner» shows under the heading (UX-DR28)

**Given** I press «Skjønner»
**When** the disclosure call succeeds
**Then** the id is stored in `seen_disclosures` for my account, added to the page-session record with no refetch (AD-18), and focus moves to the (i) beside the heading where the text stays
**And** the note isn't shown again on any device or in a later playthrough, and the record survives a new life (FR-43)

**Given** I open «Om tallene» from the menu (`/om-tallene`)
**When** the page loads
**Then** it shows all 26 disclosures grouped by theme, rendered from my playthrough's pinned library, or from the start versions when no life is active (UX-DR39, AD-13)

### Story 9.4: Pin a savings target and see what's coming

**Tier:** Can be cut (FR-57)

As a player,
I want to save towards something I choose and see next month's known costs,
So that I can plan my money (FR-57).

**Acceptance Criteria:**

**Given** an option with a price, opened or not
**When** I pin it with «Bytt sparemål»
**Then** it becomes my one savings target (an option with two prices is pinned as one of them), pinning moves no money and isn't a choice, the target can be changed any month, and an unopened one shows when it opens (FR-18)
**And** progress is the current account plus savings against the price, at most 100 %, from the engine, without BSU or the card, shown after the planned payments before continuing (UX-DR23)

**Given** the pinned option is taken, given as a gift, or closes
**When** that happens
**Then** the target is cleared with a short note, and bank messages for the target's thresholds follow it (FR-55)

**Given** the bank
**When** I open «Hva kommer neste måned»
**Then** it lists next month's known fixed and everyday costs and the loan, payment-plan and family-loan instalments, with the card as its current balance, and is empty in month 60
**And** «Aktiviteter i år» shows this in-game year's applied activity cost by kind (worked example 25)

## Epic 10: Playtesten

The group can run the playtest: records per tester and export by tester code, the content freeze, the manual and measured checks before the playtest, the test players close to each ending, and the clean-up afterwards. Sign-up limited to testers, the playtest environment and the daily check are in Epic 1.

### Story 10.1: Record what testers do

**Tier:** Core

As the team,
I want a small record per tester account,
So that we can measure the success metrics in §7.1 (FR-50).

**Acceptance Criteria:**

**Given** `PLAYTEST_RECORDS` is on
**When** the pipeline confirms an action
**Then** one `records.on_action(user, before, after, action, now)` updates the account's record in the same transaction: time to the first real choice (from sign-up), session lengths (time between confirmed actions within an in-game year, gaps above 10 minutes, config, not counted), play days in Europe/Oslo, the highest month per playthrough, completed playthroughs with ending, goal and net savings at 20, playing again, starting over, months with applied activities, months whose activities differ from the month before, plan time, and invitations whose activity was applied
**And** all times come from the server's `now`, records are never rebuilt from `action_log`, and they hold no choices, game content, email address or nickname

**Given** a playthrough is deleted by a new life (FR-43)
**When** the new life starts
**Then** the record is updated before the old playthrough is deleted, and it survives

**Given** a tester deletes the account, or the inactivity job does
**When** `delete_account` runs
**Then** the record is deleted in the same transaction, and `testers_left` goes up by one only when the row was removed, the switch is on, the account isn't a test account, and its address is in `tester_codes`
**And** with the switch off, and for a test account, nothing is recorded, with a test for each

### Story 10.2: Export the records by tester code

**Tier:** Core

As the team,
I want to export the records by tester code,
So that the analysis never sees an email address (FR-50, NFR-3).

**Acceptance Criteria:**

**Given** the playtest has run
**When** a team member runs the export with `railway run` from a checkout of the deployed commit
**Then** it joins each record to its tester code through the normalized address, writes codes and never email addresses or nicknames, skips accounts with no code and test accounts, and the output stays on the team member's machine (AD-14, AD-15)

**Given** the database has to move to the Railway Postgres fallback during the playtest
**When** the team switches
**Then** it starts with `pg_dump` and a restore, and is recorded as a deviation from the course requirement (AD-14)

### Story 10.3: Freeze and tune the content before the playtest

**Tier:** Core

As the team,
I want the figures tuned and the library frozen before testers start,
So that every tester plays the same, checked game (FR-58, NFR-4, #126, #48).

**Acceptance Criteria:**

**Given** the tuning values in Rule Set v1's parameter table (OQ-8)
**When** the tuning deadline comes
**Then** the values are set with real event costs, and the second reference run still reaches goals 1 and 2 with a margin the team accepts (#48)

**Given** the library and config are ready
**When** the team freezes v1 (`frozen: true`)
**Then** every FR-58 gate fails the content check from then on, mechanics changes need a new version folder, text-only corrections are allowed, and `cli clear-game-data` runs once (AD-7)
**And** the playtest minimum and the rule for a library that isn't ready follow the team's decision in #126

### Story 10.4: Check devices, accessibility and speed by hand before the playtest

**Tier:** Core

As the team,
I want the manual checks done and written down before each playtest,
So that what CI can't measure is still verified (NFR-1, NFR-2, NFR-9, NFR-10).

**Acceptance Criteria:**

**Given** the playtest environment
**When** the team runs the main flow from creating a user to the ending
**Then** it works on Safari on an iPhone, Chrome on an Android phone, a tablet, and Chrome or Edge on a Windows laptop (NFR-1)
**And** a keyboard-only run and a phone screen-reader run pass, including 2.5.7 dragging, 2.5.8 target size and 3.3.7 redundant entry (NFR-2)

**Given** NFR-7's list of refusals and its five cases that aren't refusals
**When** the team compares it with the automated tests
**Then** every line has a test, and a missing one is written before the playtest

**Given** the first version of the app is built
**When** an ended session, with its cookie still in the browser, opens `/hjem`, and a logged-in player opens `/`, `/logg-inn` and `/ny-bruker`
**Then** the first ends on `/logg-inn` with no loop, and the others end on `/hjem` (Story 1.4)

**Given** a mid-range phone on throttled 4G
**When** the team measures against the playtest environment
**Then** the result after a choice shows within 1 s for 9 of 10 choices and within 3 s for all, the same for a quiet month and for placing or removing an activity, the first visit is usable within 3 s, and a loading message shows within 1 s and the game is usable within 10 s (NFR-10)
**And** the logged server time per month process and save has a p90 of at most 300 ms, and all results are written to `frontend/e2e/manual-checks.md`, with the aggregated playtest results added to the repo afterwards (NFR-9)

### Story 10.5: Log in as a test player close to each ending

**Tier:** Core

As an examiner,
I want ready-made test players in month 59 close to each ending,
So that I can see every ending without playing a whole life (NFR-6, FR-41).

**Acceptance Criteria:**

**Given** every other story that changes play is done (wages, open options, activities and crises included)
**When** the seed script runs
**Then** it adds users in month 59 close to each of the four endings (real win, hollow win, goal not reached, loss), each made by scripted play from month 1 through the pipeline as in Story 2.9, never by writing state
**And** CI asserts each user's target state and that the last months give its ending, and the README lists each user, its state and its password

**Given** these users and their dumped view fixtures
**When** the end-to-end run reaches the ending
**Then** Playwright and axe check each ending screen with them (AD-20)

### Story 10.6: Clean up after the playtest

**Tier:** Core

As the team,
I want to delete everything from the playtest when the analysis is done,
So that no data outlives the project and nothing keeps costing (NFR-3, NFR-5).

**Acceptance Criteria:**

**Given** the analysis is done
**When** the team cleans up, no later than the December delivery
**Then** the tester codes, the records and the playtest accounts are deleted, and the Railway and Vercel projects are deleted and the Railway plan cancelled, so nothing keeps costing (NFR-5)
