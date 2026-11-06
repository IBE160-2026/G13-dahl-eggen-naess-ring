---
title: LifeMode PRD review, proposed solutions
date: 2026-11-05
status: proposals awaiting the team
review: review-2026-11-05.md
---

# Proposed solutions for the PRD review, 2026-11-05

This document proposes a solution for every finding in `review-2026-11-05.md`. That's all 144 findings, and the coverage table at the end maps each finding ID to its proposal. Nothing here is in `prd.md` yet. Once the team accepts, rejects or changes a proposal, the PRD, the brief addendum, the PRD addendum and `.memlog.md` are updated to match, and the change goes to the team as a pull request.

There are 57 proposals in five areas:

| Area | Proposals | What it covers |
|---|---|---|
| M. Money engine | M1-M14 | Card, accounts, crisis months and triggers, month 60, loans, BSU, the UJ-4 numbers |
| G. Goals, wellbeing and time | G1-G9 | Calendar, working hours, unlock ages, life goals, wellbeing, endings, moped, car licence |
| X. Game loop and ending | X1-X12 | Random draws, event scheduling, library size, schema terms, versions, cause links, ending screen, restart, disclosures, room |
| K. Account and NFRs | K1-K13 | Sign-up, passwords, sessions, reset email, connectivity, platform, speed, input checks, privacy, playtest, hosting, accessibility |
| E. Editorial | E1-E9 | Structure and prose |

Each proposal has the same fields: Findings, Problem, Recommendation, Why, Alternative, Lands in, Draft text, Conflicts and Team decision. "Needed" marks a real product choice for the team. "Recommend accept" marks a clear fix.

## 1. Decisions the team needs to make

These 16 proposals change product behaviour or a decision the team already made. Each one has a recommendation. The full reasoning is in the proposal.

| # | Decision | Recommendation | Alternative | Changes a prior decision? |
|---|---|---|---|---|
| M4 | What counts in the debt trigger | Subtract savings (not BSU) from debt, count only wages before tax, and set a NOK 5,000 floor when income is zero | Keep gross debt; add only the income definition and the floor | Yes: "crisis triggers unchanged" (2026-11-04) |
| M5 | Fixed costs before 18 | Parents pay mobile and public transport until the 18th birthday | Pocket money every month [needs figure] | No |
| M6 | Crisis cadence | One crisis month at a time, chosen by trigger priority, then a 2-month cooldown. A crisis ends as soon as no trigger is true, and an event it displaces moves to a later month | One crisis per episode, armed again only when the trigger clears | Yes: F4 "never silently skipped" is read as "shown during the cooldown"; "2-3 linked choices" becomes "up to 3" |
| M8 | Month 60 and the loss | Loss only if a trigger true at the end of month 59 is still true at the end of month 60. Month 60 is then always a crisis month | No random expenses in months 59-60 | Narrows "a crisis condition active at 20" |
| M12 | Everyday costs set by choices | Event options can start or stop a monthly cost (lunches, subscriptions), which the player can stop from the money view | One spending level (low, normal or high) | No (scope addition) |
| M13 | UJ-4 numbers | Keep the NOK 10,000 limit and every confirmed figure. Markus checks the moped's value and keeps it, and five months of extra shifts pay off the card | Raise the first limit to NOK 20,000 and keep the sale (step 2 becomes NOK 377 / NOK 700 / 94 months / NOK 17,171) | Yes: UJ-4 "sells the moped, not enough" |
| G1 | Calendar | Every player is born in January, so each session is one calendar and tax year | August birthday (sessions follow school years) | No |
| G3 | Unlock ages | A part-time job from 15 (max 12 h a week), the summer job from 16, and the full-time job from month 55 | No job before 16 | Fixes a contradiction in UJ-1 step 5 |
| G4 | Life-goal formulas | Measured on net position at 20 (debt includes family loans). Save: NOK 100,000. Debt-free: no debt and NOK 50,000 outside BSU. Experience: bought without ending in net debt, or affordable at 20 | Experience goal only counts if bought | No |
| G5 | Wellbeing | One 0-100 score from stress, free time and social life, weighted by the goal. The ending uses the average of months 49-60 against a threshold of 50 | Average over all 60 months | Adds overwork to stress and social life |
| X3 | Library minimum | 50 regular events (twice the 25 active months), at least 10 per in-game year, and a replay-overlap check | 4 active months a year and a floor of 40 | Yes: "minimum 30" (2026-11-03, #19) |
| X7 | Ending ranking and texts | Rank by the size of the kroner effect, plus or minus. Costly choices get a tip, and good choices get a line on why they paid off. On a hollow win, the wellbeing choice takes third place | Rank by most negative effect only | Rewords UJ-5 step 4 |
| X9 | One life at a time | Starting over before 20 is allowed after confirming. The ended life is deleted, and a finished life is kept read-only until the next one | Play again only from the ending screen | No |
| K3 | Shared school PCs | Add a "Stay logged in on this device" box at login, unticked by default. Ending other logins on password change and "Log out on all devices" are "Recommend accept" | Leave it for later (#31) | Brings part of #31 into the MVP |
| K5 | Saving on a patchy connection | A choice counts only when the server confirms it, and the first confirmed choice wins across devices. FR-7 becomes "nothing waits on the device" | None | Rewords the FR-7 sync decision (2026-11-03) |
| K9 | Privacy measures in the MVP | Show player information at sign-up, delete accounts after 12 months without login, and load no tracking or third-party code. No age checkbox | Leave all of it to #24 before go-live | Makes three brief-addendum recommendations MVP requirements |

## 2. Recommended for acceptance

The other 41 proposals fix gaps without changing a decision:

- **M:** M1 card spending and payment, M2 card warning, M3 accounts and savings as a buffer, M7 crisis options and payment plan, M9 consumer loan limits, M10 family loans, M11 BSU cap and withdrawal, M14 worked examples.
- **G:** G2 working hours, G6 endings boundary, G7 moped, G8 car licence draw, G9 worked examples.
- **X:** X1 draws stored once, X2 event scheduling, X4 glossary and schema, X5 content versions, X6 cause links with shares, X8 "if you had chosen differently", X10 resuming the start, X11 disclosures D7-D16, X12 room layers.
- **K:** K1 sign-up, K2 passwords and attempt limits, K4 reset email (OQ-4 blocks FR-3), K6 platform, K7 responsiveness, K8 input checks, K10 playtest data, K11 playtest hosting, K12 which document wins, K13 accessibility.
- **E:** E1-E9 (structure and prose).

Some numbers need a source before they become requirements. They're marked [needs figure]: the big-experience price, youth everyday spending, fuel use, pocket money and the free email quota. The Supabase and free-tier facts in K are from general knowledge and marked "verify".

## 3. How the areas were lined up

The four areas were drafted separately and then checked against each other. These adjustments apply when the proposals go into the PRD:

1. **Order within a month (rule 1):** M1, X2 and G5 together give income → tax → fixed and everyday costs → unexpected expense → loan instalments, card bill and interest on debt → interest on savings → the month's event and the player's choice → wellbeing → rule 8 check.
2. **Active months (X2 with G2-G4):** the default active months become 1, 3, 6, 8 and 10 of each in-game year (January, March, June, August, October) instead of 1, 3, 5, 8 and 10. This way the June offers (summer job in months 18, 30 and 42, and the full-time job in month 54 to start in month 55) and goal 3's experience event fall in active months. Months 59-60 stay quiet, and there are still never more than two quiet months in a row.
3. **Month 60 (M8 with X2):** M8's rule makes X2's "no unexpected expense in months 59-60" unnecessary, so that line is dropped.
4. **Card warning in the schedule (M2 with X2):** the order for who gets a month becomes crisis month, then card warning, then milestones and follow-ups, then a drawn event. A card warning in a quiet month makes that month active.
5. **Actions in any month (M3, G2, G7):** one list in FR-45. It covers M3's money actions, plus setting working hours and selling the moped. None of them uses up the month's choice.
6. **Extra shifts (M7 with G2):** extra shifts raise weekly hours for the event's number of months (default +4 h for 3 months), then go back, never above rule 10.
7. **Debt for the goals (G4 with M7):** the goal check's debt also includes payment plans: card + consumer loans + payment plans + family loans.
8. **Moped value in UJ-4 (M13 with G7):** M13 uses G7's resale rule instead of its illustrative 20%. Markus's used or gift moped is worth about NOK 9,300 after about 26 months, still less than the NOK 10,000 debt. Worked example 8a (wellbeing over UJ-4) follows whichever UJ-4 version the team picks in M13. G's draft has him selling the moped and working 20 h, and M13's recommendation has him keeping it and working 12 h.
9. **Family-loan postponement (M10 with G5):** rule 12's monthly table gets one more row: a postponed family-loan instalment raises stress by 5.
10. **Disclosure texts:** one list. D7-D16 come from X11. M1's fee sentence merges into D11, G7's 15% into D8, G2's 52/12 into D12, G5 into D16 and G8 into D10. New texts: D17 calendar (G1), D18 savings cover the account (M3), D19 negative balance (M3), D20 payment plan (M7), D21 consumer loan (M9), D22 BSU withdrawal (M11) and D23 parents pay until 18 (M5). M10 adds one sentence to D4.
11. **Numbering:** FR IDs stay stable, so new FRs get new numbers: FR-45 accounts (M3), FR-46 event scheduling (X2's FR-17a), FR-47 working hours (G2's FR-20a). New NFRs: NFR-10 responsiveness and NFR-11 playtest environment (K). New rules: 11 calendar (G1), 12 wellbeing (G5), 13 life goals (G4), 14 moped (G7), 15 payment plan (M7's "rule 11"). New worked examples: 7-15 from M, and 16-20 from G (G's 7-11).
12. **Recalculation after the decisions:** if M5 is accepted, G4's reference run (NOK 211,398) and its lowest balance (NOK 550 in month 18) are recalculated. If M12 is accepted, the goal targets are checked again once everyday-cost amounts have a source.
13. **NFR-7 (K8):** the list also covers G's cases: an option before its unlock month, a second moped, a moped without a licence, the paid car licence before the draw or after a gift, the experience paid on credit, and a BSU deposit above the yearly cap.

## 4. Suggested order of work

1. The team decides the 16 items in section 1. The quickest route is to accept the recommendations and note any exceptions.
2. Apply the M, G, X and K proposals to the brief addendum (rules, parameters, worked examples, D-texts), then to the PRD and the PRD addendum. Log each decision in `.memlog.md`.
3. Apply the editorial proposals E1-E9 last, so the prose isn't polished before the content is settled.
4. Run PRD Finalize: memlog audit, reviewer pass, open items and polish.

## M. Money engine
Area: card mechanics, crisis months and their triggers, month 60, consumer and family loans, BSU, the UJ-4 numbers and worked examples for the new money rules. All findings were checked against `prd.md`, Rule Set v1 (brief addendum), the PRD addendum and the memlog. Every finding in this area holds. None is "No change".

Figures come from the brief addendum's parameters and research. Calculations use rule 2 rounding (0.5 rounds up). The calculations were run with small scripts during the review session. Weekly hours are turned into a monthly wage with 52/12 weeks a month, for example 10 h × NOK 195.04 × 52/12 = NOK 8,452. The hours model itself is A13/E22 (another area). If that area picks another conversion, the kroner amounts below shift a little, but the conclusions don't.

### Shared definitions used below

- **Steady wage:** wage income in each of the last three months. Needed for a card (M1) and a consumer loan (M9).
- **Debt step:** rule 1 step 4 (loan instalments, the card bill and interest on debt).
- **Money view:** the place where the player sees their accounts and takes money actions (M3). How it looks is UX.
- **Wage income:** hourly wages before tax. It doesn't include sales, gifts, the pengegave, family money, interest or loan payouts.

### Dependencies on other areas

- Hours and extra shifts: A13, E22. M7 and M13 assume weekly hours that can be raised for a set number of months, capped by rule 10.
- Calendar (start month, birthday month, calendar year): A14, E21. M11's yearly BSU cap and M13's tax-free months depend on it.
- Storing random draws: A2, E26, E27. M7 assumes the family draw is made once per crisis month and stored.
- Event scheduling and events after month 60: A1, E31, E32. M6 hands displaced events to that rule.
- Moped resale and transport after a sale: A38, E28, E29, E33. M13 uses an illustrative resale share.
- Goal formulas and borrow-to-win: A4, A5, E15-E17. M9 limits the loan; the goal side decides how debt counts at 20.
- D-texts: A32. The texts for this area's mechanisms are drafted in each proposal, ready for the D7+ list.
- New FR numbers: M3 proposes FR-45. Check the number against other areas' new FRs before applying.

---

### M1. Card spending and paying the bill

- **Findings:** A10, E2, E3, E54
- **Problem:** Nothing says how a purchase gets onto the card, who picks the monthly payment or when it's paid. Rule 1 charges card interest before the choice step, so the engine can't know at that point whether the bill gets paid. An empty account at payment time and the limit are undefined.
- **Recommendation:**
  1. **Card use** is an on/off setting. Taking the card turns it on. The player can turn it off at any time (FR-26 already lets them stop).
  2. While card use is on, purchases from event options and **card-payable monthly costs** (fuel, and everyday costs from M12) go on the card, as long as they fit under the limit. A purchase that doesn't fit is paid from the current account, and the game says the card was declined.
  3. **Payment setting:** the whole balance, the minimum, or a fixed amount of at least the minimum, in steps of NOK 100. The player picks it as part of the card event's options (for example "Ta kortet og betal hele regningen hver måned" or "Ta kortet og betal minstebeløpet"). They can change it from the money view, and the change applies from the next bill. If nothing is set, which only happens in engine tests, the engine pays the whole balance.
  4. **The bill** is the card balance at the debt step. It holds earlier months' purchases and this month's card-payable costs. The engine pays the chosen amount, but never more than the current account and savings hold, so a card payment never takes the account below NOK 0.
  5. **Interest:** if the whole balance is paid, no interest is charged. Otherwise interest is charged on the whole balance first, and then the payment is made, as in worked example 4. Paying the minimum never counts as paying in full. Without that last sentence, example 4 would become 12 months and NOK 3,600, and UJ-4 would become NOK 5,503, so it must stay.
  6. **Missed minimum:** if the engine pays less than the minimum, the minimum counts as missed, and the shortfall stays on the card. Because a card payment never takes the account below zero, a missed minimum never also starts the below-zero trigger.
  7. **Extra payment:** an event option or a money action can pay down the card at the choice step. It lowers the balance at once. It doesn't undo interest already charged that month.
  8. **Limit:** fixed for the playthrough, NOK 5,000-10,000 as configuration, with NOK 10,000 as the default. Interest can take the balance over the limit. While the balance is at or over the limit, the card takes no purchases. The MVP has no over-limit fee and no late fee.
  9. A card needs a steady wage. If the wage stops later, the card stays open.
- **Why:** Paying the bill at rule 1's existing debt step means the engine knows the payment before it charges interest, and examples 3-6 keep passing unchanged. One switch and one setting are enough for the whole UJ-4 loop.
- **Alternative:** every option with a cost gets a payment method (account or card). That's more realistic, but it doubles the options in every event.
- **Lands in:** PRD FR-26 (consequences), FR-12 and rule 1 (step wording), brief addendum rule 5, FR-45 money actions (M3), D-text list (A32), architecture (where the settings are stored).
- **Draft text:**

  Rule 1 (brief addendum): «**One round is one month.** Each month is processed in a fixed order: income → tax → fixed costs and everyday costs → loan instalments, the card bill and interest on debt → interest on savings → the month's event and the player's choice. The rule 8 check runs at the end of the month.»

  Rule 5 (brief addendum): «**Credit card.** Each month's debt step pays the card bill: the card balance at that point, including this month's card-payable costs. The engine pays the player's chosen amount (the whole balance, the minimum or a fixed amount), but never more than the current account and savings hold. If the whole balance is paid, no interest is charged. Otherwise interest is charged on the whole balance first, and then the payment is made. The minimum is the larger of 3.5% of the balance before the month's interest and NOK 300, or the whole balance after interest if that is smaller. Paying the minimum never counts as paying in full. Paying less than the minimum is a missed minimum. A purchase that would take the balance above the limit is declined. Interest can take it above the limit.»

  FR-12, first sentence: «The engine processes every month in the order set by rule 1: income, then tax, fixed costs and everyday costs, loan instalments, the card bill and interest on debt, interest on savings, and last the month's event and the player's choice.»

  FR-26 (replaces the consequences list):
  > From age 18, a player with a steady wage can get a credit card, under rule 5. Realizes UJ-4.
  >
  > **Consequences (testable):**
  > - A steady wage means wage income in each of the last three months. If the wage stops later, the card stays open.
  > - The limit is fixed for the playthrough. It's configuration, NOK 5,000-10,000, with NOK 10,000 as the default.
  > - When taking the card, the player chooses how the bill is paid: the whole balance, the minimum or a fixed amount. They can change it at any time, and the change applies from the next bill.
  > - While card use is on, purchases and card-payable monthly costs, such as fuel, go on the card as long as they fit under the limit. A purchase that doesn't fit is paid from the current account, and the game says the card was declined.
  > - The player can turn card use off at any time.
  > - The bill is paid at the debt step and never takes the current account below NOK 0. Paying less than the minimum counts as a missed minimum (rule 8).
  > - Interest can take the balance above the limit. The card then takes no purchases until the balance is below the limit again.
  > - A NOK 3,200 balance, with only the minimum paid each month, is paid off after 13 months, NOK 3,606 in total (worked example 4, F3).
  > - The game shows, in kroner, this month's interest and the total cost of paying only the minimum, for the player's own balance.

  D-text: «Forenklet: I spillet har kortet en fast kredittgrense, og du betaler ingen gebyrer, verken for å gå over grensen eller for å betale for sent. I virkeligheten koster det ofte gebyr, og banken kan endre grensen.»
- **Conflicts:** None. It keeps the 3.5%, NOK 300 minimum on the balance before interest (#35, #38) and A-18's limit range.
- **Team decision:** Recommend accept.

### M2. Card warning: exact trigger and timing

- **Findings:** A37, E4
- **Problem:** FR-31's "can't be paid in full and interest starts" mixes a forecast with an event, so the timing is open. It also never fires when the player could pay but pays less.
- **Recommendation:**
  - **Trigger:** in month m, the card bill isn't paid in full, and month m−1 was either paid in full or had no card balance.
  - **Timing:** the warning is month m's event, shown after the debt step. The player sees it before the next interest charge, and at least a month before the missed-minimum trigger can start a crisis. In a crisis month, the crisis shows the warning's figures as its first screen, and the warning counts as shown.
  - **Content:** this month's interest in kroner; the balance; how many months and how much interest the bill would cost if only the minimum were paid, starting with this month's bill (rule 5); and the reason. The reason is either "couldn't pay" (the current account and savings held less than the bill) or "chose to pay less" (they held enough).
  - **Options:** as in FR-31, shown only when possible (M7). When the reason is "chose to pay less", one option switches the payment to the whole balance.
- **Why:** The trigger is a fact the engine already has after the debt step, so no forecast is needed. It also covers the player who chose the minimum. For UJ-4, the figures come out exactly as written: a NOK 10,000 bill, NOK 188 interest this month, and 51 months and NOK 5,508 at the minimum.
- **Alternative:** a forecast at the end of month m (the bill is larger than next month's income can cover) that warns before any interest. It's kinder, but it needs a dry run of next month and can be wrong after a random expense.
- **Lands in:** PRD FR-31, Glossary (Card warning), UJ-4 step 1 (wording, see M13).
- **Draft text:**

  FR-31:
  > When a card bill isn't paid in full in a month that follows one paid in full, or one with no card balance, the game warns the player in that month. The warning shows this month's interest, the balance, and how long and how much the bill would cost if only the minimum were paid from now on. It says whether the player couldn't pay the whole bill or chose to pay less. The player then chooses whether to act, for example by talking to family, stopping the card, taking extra shifts or selling something. Realizes UJ-4.
  >
  > **Consequences (testable):**
  > - The warning is the event of the month in which interest starts. It's shown before the next interest charge.
  > - In a crisis month, the crisis shows the warning's figures first, and the warning counts as shown.
  > - The warning doesn't start a crisis month on its own.
  > - The warning is shown again each time interest starts after a month paid in full.
  > - Test: the setting is the whole balance, the bill is NOK 6,000, and the account and savings hold NOK 4,000. The engine pays NOK 4,000, charges NOK 113 interest and shows the warning in that month (worked example 7).

  Glossary, Card warning: «The warning shown in the first month a card bill isn't paid in full. It comes before any crisis.»
- **Conflicts:** UJ-4 step 1 says "he can't pay off the whole balance before the interest-free deadline". Under this rule he didn't pay it all, so interest has just started. It's a one-phrase change (M13).
- **Team decision:** Recommend accept.

### M3. Accounts, savings as a buffer and paying for choices

- **Findings:** A9, E18, E19
- **Problem:** No account model exists. A solvent player with savings gets a below-zero crisis. A negative balance is a free overdraft, and an under-18 player can overspend into credit, which breaks rule 6.
- **Recommendation:** a new FR-45 with these rules:
  - **Three accounts:** the current account (income in, costs out), savings (2.87%) and BSU (5.61%, M11).
  - **Savings cover automatically:** whenever a payment would take the current account below NOK 0, savings pay the rest, as far as they reach. BSU never does. The month summary lists each transfer. The current account can only go below zero once savings are empty.
  - **Paying for choices:** an option can be picked only if its cost fits within the current account plus savings, plus the room left on the card when card use is on. Otherwise the option is shown greyed out with the missing amount. Every event has at least one option with no cost, which the schema check enforces. This holds at every age, so a choice never creates a negative balance, and rule 6 holds before 18.
  - **Costs the player doesn't choose** (fixed and everyday costs, bank loan instalments, unexpected expenses) are always charged, even if the account goes below zero. Card payments (M1) and family-loan instalments (M10) never go below zero.
  - **A negative current account** has no interest or fee. It can't pay for choices, and next month's income pays it off first. It starts a crisis (rule 8).
  - **Money actions,** in any month, without using up the month's choice: move money between the current account and savings, deposit in BSU, turn card use on or off, set the card payment, make an extra card payment, pay off a consumer loan early and withdraw the BSU (M11).
- **Why:** A player with enough savings never gets a false crisis. A negative balance can't be spent, and the next wage clears it, so it isn't free credit. Under-18 players can't borrow by overspending, and nobody is stuck in an event with no affordable option.
- **Alternative:** instead of covering automatically, offer the player a transfer from savings before the end-of-month check.
- **Lands in:** PRD new FR-45 in 4.5, rule 8 (below-zero definition, M4), FR-17 schema (one option with no cost), D-text list, architecture.
- **Draft text:**

  > #### FR-45: Accounts and paying for choices
  >
  > The player has a current account, a savings account and, if they open one, a BSU. Income lands in the current account, and costs are paid from it. Realizes UJ-1, UJ-3 and UJ-4.
  >
  > **Consequences (testable):**
  > - When a payment would take the current account below NOK 0, savings pay the rest, as far as they reach. BSU never does. The month summary shows each transfer.
  > - An option can be picked only if the player can pay for it from the current account and savings, plus the card if card use is on and the cost fits under the limit. An option they can't pay for is shown with the missing amount and can't be picked. Every event has at least one option with no cost.
  > - Fixed costs, everyday costs, loan instalments and unexpected expenses are always charged, even if the current account goes below NOK 0.
  > - A negative current account has no interest. It can't pay for choices, and the next income pays it off first.
  > - In any month, the player can move money between the current account and savings, deposit in BSU, turn card use on or off, set the card payment, pay extra on the card and pay off a consumer loan early. These money actions don't use up the month's choice.

  D-texts:
  - «Forenklet: I spillet flytter vi penger fra sparekontoen automatisk når brukskontoen ikke har nok. I virkeligheten må du flytte pengene selv, ellers kan betalingen bli avvist.»
  - «Forenklet: Går du i minus i spillet, betaler du ikke renter eller gebyrer, men det starter en krisemåned. I virkeligheten kan ubetalte regninger gi purregebyr og inkasso.»
- **Conflicts:** None.
- **Team decision:** Recommend accept.

### M4. What counts in the debt trigger

- **Findings:** A36, E12, E13, A9 (net debt and seasonal income)
- **Problem:** FR-32 leaves out the family-loan exception that FR-27 and rule 8 state. "Average monthly income" isn't defined, so a moped sale or a gift can hide a debt problem. With zero income, any card balance starts a crisis every month. Debt counts in full even when savings cover it.
- **Recommendation:** rule 8's third trigger becomes:
  - **Debt** = card balance + consumer loans + payment plans (M7), not counting family loans, minus savings (not BSU), never below 0.
  - **Income** = wage income before tax, averaged over this month and the two before. Months before the game started count as 0. Sales, gifts, the pengegave, family money, interest and loan payouts don't count.
  - **Trigger:** debt > the larger of 3 × that average and NOK 5,000. The NOK 5,000 floor is configuration (`crisis_debt_floor`), set at the bottom of the first-card limit range.
  - Before 18 the player has no bank debt, so this trigger can't fire.
- **Why:** Subtracting savings stops false crises for solvent players. Counting only wages stops one-off money from delaying a crisis. The floor stops a small card balance from starting a crisis every month after a job ends. A debt the player really can't pay is still caught, because the missed minimum starts a crisis within two months.
- **Alternative:** keep gross debt, and add only the income definition and the floor.
- **Lands in:** PRD FR-32 (trigger list), brief addendum rule 8, addendum Win Condition section (the loss text repeats the old wording).
- **Draft text:**

  FR-32, third bullet: «debt, not counting family loans and after subtracting savings, is above 3× the average monthly wage over the last three months, or above NOK 5,000 if that's higher»

  Rule 8, third trigger: «or debt is above the larger of 3 × the average monthly wage income and NOK 5,000. Debt means the card balance, consumer loans and payment plans, not counting family loans, minus the savings account (not BSU). Wage income is hourly wages before tax over this month and the two before; months before the game started count as 0. Sales, gifts, the pengegave, family money, interest and loan payouts don't count. The NOK 5,000 floor is configuration.»
- **Conflicts:** The memlog (2026-11-04, SE) says "crisis triggers unchanged", and rule 8 says "total debt". Subtracting savings and adding a floor change what the trigger means. The family-loan exception itself was decided on 2026-11-05 and is only copied into FR-32.
- **Team decision:** Needed.

### M5. Fixed costs before 18

- **Findings:** A12
- **Problem:** The finding holds. Mobile (NOK 299) and youth transport (NOK 238) cost NOK 537 a month from age 15, which is NOK 19,332 by 18. A player with no job who keeps the lowest pengegave of NOK 10,000 goes below zero after about 19 months, at around 16 and a half, through no choice of their own.
- **Recommendation:** parents pay mobile and public transport until the 18th birthday. From 18, the player pays them, and the month summary says so. Moped costs (fuel, insurance and repairs) are the player's own from the day they own a moped, and FR-23's random share from the parents still applies. Reachability check: a player with no job who keeps NOK 10,000 in savings never goes below zero before 18. From 18, the costs total NOK 12,888 by 20. A player who never works after 18 does run out, at about 19 and a half, but jobs are open by then.
- **Why:** It matches how most 15-17-year-olds live. The early game no longer punishes caution, and taking over the bills at 18 becomes its own small lesson.
- **Alternative:** pocket money every month until 18 [needs figure].
- **Lands in:** PRD FR-23 (first sentence and a new consequence), D-text list, worked example 15 (M14).
- **Draft text:** FR-23: «From the 18th birthday, the player pays mobile and public transport every month. Before that, the parents pay them. Moped fuel and insurance are the player's own costs from the day they own a moped.» New consequence: «A player with no job who keeps a NOK 10,000 pengegave in savings never goes below NOK 0 before 18.» D-text: «I spillet betaler foreldrene mobilen og bussen din til du fyller 18. Da overtar du regningene.»
- **Conflicts:** None logged. FR-23 currently charges these costs from 15. UJ-4 already has Markus paying his own moped costs since 16, which fits.
- **Team decision:** Needed.

### M6. Crisis cadence, priority, early end and displaced events

- **Findings:** E5, E6, E10, E7, A8 (cadence)
- **Problem:** A trigger that stays true would start a crisis every month. Several triggers at once have no rule. A choice that solves the problem still forces the player through the rest of the crisis. A crisis can silently replace an age unlock or a boomerang event.
- **Recommendation:**
  - **One crisis month at a time:** rule 8 is checked at the end of every month. If any trigger is true and no cooldown is running, the next month is a crisis month. There's only ever one, however many triggers are true.
  - **Priority:** the crisis event follows the most urgent true trigger: below zero, then missed minimum, then debt. It names every true trigger.
  - **Cooldown:** after a crisis month in month c, no new crisis month starts in months c+1 and c+2 (configuration `crisis_cooldown_months`, default 2). During the cooldown, the money view shows that the economy is in crisis and lists the true triggers. A trigger that's still true at the end of month c+2 starts a crisis in month c+3. A player who ignores everything therefore gets a crisis every third month, about 8 in the 24 months after 18. Month 60 is the exception (M8).
  - **Ends when solved:** after each linked choice, the engine checks the triggers again. The crisis month ends as soon as none is true. Money a crisis choice brings in goes first to a negative current account, then to overdue card minimums, and the rest stays in the current account. The missed-minimum trigger counts as solved once the overdue minimums are paid, or the card balance moves into a payment plan. Picking "ignore it" ends the crisis month.
  - **Displaced events:** a crisis month, or a card warning, takes the month's event slot. The displaced event moves to the next month without a crisis or card warning, ahead of anything already scheduled there. An event pushed past month 60 follows the event-scheduling rule (E31, another area).
- **Why:** Ignored debt still comes back, as FR-32 and the brief promise, but the rest of the game doesn't disappear. With about 10 crisis events, the library can carry it. Ending early means the player never has to sell a moped they no longer need to sell.
- **Alternative:** no cooldown, but only one crisis per episode, armed again only when the trigger clears. That breaks "ignored debt triggers new crisis months".
- **Lands in:** PRD FR-32 (consequences), brief addendum rule 8, §8.3 (F4 reading), Glossary (Crisis month: "up to 3 linked choices").
- **Draft text:**

  FR-32, replacing the first paragraph and the consequences:
  > The engine checks rule 8 at the end of every month. When a trigger is true and no cooldown is running, the next month is a crisis month. [trigger list as in M4]
  >
  > A crisis month has up to 3 linked choices with realistic actions, such as selling something, taking extra shifts, asking for a payment plan, asking family or ignoring it. The engine calculates the effect of each one. Realizes UJ-4.
  >
  > **Consequences (testable):**
  > - **Always started:** a trigger that's true outside a cooldown starts a crisis month the next month (F4, one test per trigger).
  > - **One at a time:** however many triggers are true, one crisis month starts. Its event follows the most urgent trigger: below zero, then missed minimum, then debt.
  > - **Cooldown:** no new crisis month starts in the two months after one. The game shows any trigger that's true during a cooldown. The cooldown is configuration.
  > - **Ends when solved:** after each linked choice, the engine checks the triggers again. The crisis month ends as soon as none is true, or when the player ignores it.
  > - **Nothing is lost:** an event displaced by a crisis month moves to the next month without one.
  > - **Never fatal before 20:** a crisis doesn't end the game. Ignored debt keeps growing under rules 4-5 and starts new crisis months after each cooldown.
  > - **Below zero:** going below zero only starts a crisis month. It isn't a loss.

  §8.3, add: «F4 is read as: a trigger that's true outside a cooldown always starts a crisis month. During a cooldown the trigger is shown, not skipped silently.»
- **Conflicts:** FR-32 says "a met trigger always starts a crisis month", and brief F4 says "every time; never silently skipped". With a cooldown, a trigger that's true during the cooldown is shown but doesn't start a crisis. Rule 8, the brief and the glossary say "2-3 linked choices", and this allows a crisis to end after one.
- **Team decision:** Needed.

### M7. Crisis options and the payment plan

- **Findings:** A8 (options), E11, E23
- **Problem:** Options have no rules: there may be nothing to sell or no job for extra shifts, and the payment plan has no terms, so the engine can't calculate it. A crisis can leave the player with no valid option.
- **Recommendation:** each option is shown only when it's possible.

  | Option | Shown when | Effect |
  |---|---|---|
  | Sell something | The player owns something that can be sold (MVP: the moped) | Resale value in (FR-29); it leaves the room |
  | Extra shifts | The player has a job, and rule 10 leaves room for at least 1 more hour a week | Weekly hours up by the event's amount (default +4) for the event's number of months (default 3), never above rule 10 |
  | Payment plan | The card balance is above 0 and no payment plan is running | Rule 11 (new) |
  | Stop using the card | Card use is on | Card use off |
  | Ask family | Always, once per crisis month | Family draw (FR-27), made once and stored; may be no, part or all |
  | Ignore it | Always | Ends the crisis month; stress rises (FR-33) |

  Every crisis event includes "ask family" and "ignore it", so at least two options are always available. The schema check enforces this. The card warning (M2) uses the same availability rules.

  **New rule 11, payment plan:** the card balance becomes an annuity loan under rule 4 at the card's rate (22.6%) over 12 months (configuration). The card is blocked until the plan is paid off. Instalments are charged like other bank loan instalments. One plan at a time. Worked example 12: NOK 10,000 gives NOK 939 a month, a final NOK 935 and NOK 11,264 in total, which is NOK 1,264 in interest against NOK 5,508 at the minimum.
- **Why:** It reuses rule 4, so the plan needs no new maths, and it teaches that a fixed plan costs far less than the minimum. Shown-only-when-possible options can't break rule 10 or NOK 0, and NFR-7 never has to reject an option the game offered.
- **Alternative:** drop the payment plan from the MVP and keep the other options.
- **Lands in:** PRD FR-32 (new consequence), brief addendum rule 8 (option list) and new rule 11, FR-17 schema note, D-text list.
- **Draft text:**

  FR-32, new consequence: «**Options that work:** a crisis option is shown only when it's possible: selling needs something to sell, extra shifts need a job and room under rule 10, and a payment plan needs a card balance. Asking family and ignoring it are always offered.»

  Rule 11: «**Payment plan.** In a crisis month, the player can turn the card balance into a payment plan: an annuity loan under rule 4 at the card's interest rate, over 12 months. The card is blocked until the plan is paid. Only one plan can run at a time. The term is configuration.»

  D-text: «Forenklet: I spillet blir en betalingsavtale et nedbetalingslån over 12 måneder med samme rente som kortet, og kortet sperres til lånet er betalt. I virkeligheten avtaler du vilkårene med banken.»
- **Conflicts:** None.
- **Team decision:** Recommend accept.

### M8. Month 60 and the loss ending

- **Findings:** A7, E8, E9
- **Problem:** A random expense in month 60 can push the account below zero and give a loss with no crisis month to respond in. "Active" isn't defined per trigger. A minimum missed in months 58-59 but paid in month 60 could go either way.
- **Recommendation:**
  - **When a trigger is true:** below zero means the current account is below 0 at the end of the month (savings already used up). Missed minimum means the last two debt steps both paid less than the minimum and the overdue amount hasn't been paid. Debt is measured as in M4 at the end of the month.
  - **Last chance:** if a trigger is true at the end of month 59, month 60 is a crisis month, even during a cooldown.
  - **Loss:** a trigger that was true at the end of month 59 is still true at the end of month 60.
  - A trigger that first becomes true at the end of month 60 doesn't give a loss. The ending is picked from the other three, and the summary names the problem.
- **Why:** The loss always comes after a crisis month the player could act in, so a random draw alone can't decide the ending. Late random expenses don't need to be removed. A minimum missed in months 58-59 and paid in month 60 isn't a loss.
- **Alternative:** no random expenses in months 59-60, and loss = any trigger true at the end of month 60.
- **Lands in:** PRD FR-41 (item 1 and a consequence), brief addendum rule 8 (last sentence), UJ-4 edge case (no change needed).
- **Draft text:**

  FR-41, item 1: «**Loss:** a rule 8 trigger that was true at the end of month 59 is still true at the end of month 60.»

  FR-41, new consequences:
  > - If a trigger is true at the end of month 59, month 60 is a crisis month, even during a cooldown.
  > - A trigger that first becomes true at the end of month 60 doesn't give a loss. The summary names it.
  > - Test: minimum missed in months 58 and 59 and paid in month 60 is not a loss.

  Rule 8, last sentence: «The loss ending applies when a trigger that was true at the end of month 59 is still true at the end of month 60. Month 60 is then always a crisis month.»
- **Conflicts:** The memlog (2026-11-03, #25) and rule 8 say the loss applies when "a crisis condition from rule 8 is active at 20". This defines "active". It doesn't reverse the decision, but it changes which end states are losses.
- **Team decision:** Needed.

### M9. Consumer loan limits

- **Findings:** E14
- **Problem:** A player with no income can take one or several loans of any amount and term. NFR-7's "invalid financial value" has nothing to check against. The cap here also limits the borrow-to-win exploit (the goal side is A4/E15, another area).
- **Recommendation:**
  - From 18 (rule 6), only with a steady wage.
  - **Amount:** NOK 5,000 up to 3 × the average monthly wage income over the last three months, minus the player's other debt (not family loans), rounded down to NOK 1,000. Below NOK 5,000, no loan is offered. A loan alone can then never start the debt trigger.
  - **Term:** 12, 24, 36, 48 or 60 months. Utlånsforskriften § 13 requires consumer loans to be repaid within 5 years (research, youth finance rules §3). A loan may run past age 20; what's left counts as debt in the ending.
  - One consumer loan at a time.
  - **Early payoff:** in any month, the player can pay off what's left from the current account and savings, with no fee. The next instalment then doesn't come.
  - Loans are offered through events. Paying off early is a money action (M3).
- **Why:** The limits are simple and testable, they tie the cap to the game's own crisis line, and the term matches the real 5-year rule. The examples hold: a part-time wage of NOK 8,452 allows up to NOK 25,356 minus other debt, so worked example 3's NOK 20,000 fits.
- **Alternative:** cap at a fixed configurable amount (for example NOK 50,000) instead of tying it to income.
- **Lands in:** PRD FR-25 (consequences), NFR-7 rejected cases (A31, another area), D-text list.
- **Draft text:**

  FR-25 consequences, added:
  > - A loan needs a steady wage: wage income in each of the last three months.
  > - The amount is NOK 5,000 up to 3× the average monthly wage over the last three months, minus the player's other debt, not counting family loans. Below NOK 5,000 no loan is offered.
  > - The term is 12, 24, 36, 48 or 60 months.
  > - The player can have one consumer loan at a time, and can pay off what's left at any time with no fee.

  D-text: «Forenklet: I spillet koster det ingenting å betale ned lånet før tiden, og banken ser bare på lønna di de siste tre månedene.»
- **Conflicts:** None. D4 already says real banks require income or that the borrower is older (SpareBank 1 requires 20+, research C5).
- **Team decision:** Recommend accept. The cap's multiplier is configuration.

### M10. Family loans

- **Findings:** E24, E25
- **Problem:** The rule 4 annuity formula divides by zero at 0%. Rule 6 ("before 18 the player cannot borrow") contradicts family loans for under-18 players. A family-loan instalment a teenager can't pay would push them into a below-zero crisis every month.
- **Recommendation:**
  - **0% instalments:** each instalment is P / n, rounded under rule 2. The final instalment is P minus the others. The event sets P ≥ NOK 500 and n between 2 and 12, which keeps the final instalment positive (schema check).
  - **Postponement:** an instalment is taken only if the current account and savings cover it. Otherwise it moves to the end, so the loan runs a month longer, and stress rises (FR-33). A family loan never takes the account below zero and never starts a crisis by itself.
  - One family loan at a time (also part of E26, another area).
  - **Allowed from 15:** rule 6 covers bank credit only.
  - It doesn't count in the debt trigger (rule 8, M4). How it counts in the goal check belongs to the goal area.
- **Why:** The formula becomes well defined, and rule 6 and FR-27 stop contradicting each other. Family stays flexible, as real family is, but the money is still paid back, as the team decided.
- **Alternative:** charge family instalments like bank instalments, which can go below zero.
- **Lands in:** PRD FR-27 (consequences), brief addendum rule 4 (zero rate) and rule 6 (wording), D4 (one added sentence), worked example 8.
- **Draft text:**

  Rule 4, added: «At 0% (family loans), each instalment is the amount divided by the number of months, rounded under rule 2, and the final instalment is the amount minus the others.»

  Rule 6: «**Credit only from 18.** Consumer loans and credit cards are available only from the player's 18th birthday, as in Norway, where minors cannot take on loans. Before 18 the player cannot borrow from a bank. Family loans (FR-27) aren't bank credit and are possible from 15.»

  FR-27 consequences, added:
  > - Each instalment is the loan divided by the number of months, rounded to whole kroner, and the final instalment makes the total exact. NOK 5,000 over 6 months is NOK 833 five times and NOK 835 (worked example 8).
  > - If the player can't pay an instalment, it moves to the end of the loan. A family loan never takes the account below NOK 0.
  > - The player can have one family loan at a time, from age 15.

  D4, added: «Lån fra familien er ikke banklån, og de kan du få før du fyller 18.»
- **Conflicts:** None. The decision that family loans are paid back (memlog 2026-11-04) still holds.
- **Team decision:** Recommend accept.

### M11. BSU yearly cap and withdrawal

- **Findings:** A16, E20
- **Problem:** FR-22 has no yearly cap and no withdrawal rule. BSU at 5.61% beats savings at 2.87% with no downside, and it works as free cash in a crisis.
- **Recommendation:**
  - **Cap:** deposits are capped at NOK 27,500 per calendar year (Skatteetaten 2026, already a parameter). The game accepts at most what's left of the year's room and says how much that is. Interest doesn't count. The NOK 300,000 total can't be reached in five years (5 × 27,500 = 137,500), so it needs no check.
  - **Locked:** BSU can't pay for choices and never covers a negative balance (M3). It isn't counted as savings in the debt trigger (M4).
  - **Withdrawal:** only the whole balance, as a money action, into the current account. The BSU then closes for the rest of the playthrough. Any BSU deductions already received are charged back as tax that month. In reality, using BSU money for anything but housing adds the deductions back as tax (research, youth finance rules §1). For a player on frikort that's NOK 0, but they lose the higher interest from then on.
  - The calendar year follows the game calendar (A14, another area).
- **Why:** The cap is real and sourced. Locking the BSU with a cost on withdrawal teaches that BSU is for a home, not a better savings account, and keeps it out of crisis cash.
- **Alternative:** lock BSU for the whole MVP with no withdrawal, since buying a home is out of scope.
- **Lands in:** PRD FR-22 (consequences), brief addendum rule 9, FR-45 money actions, D-text list, worked example 14.
- **Draft text:**

  FR-22 consequences, added:
  > - BSU deposits are capped at NOK 27,500 per calendar year. The game accepts at most what's left of the year's room and shows how much that is.
  > - BSU money can't pay for choices or cover a negative balance. The player can withdraw the whole BSU. It then closes for the rest of the playthrough, and any BSU deductions received are paid back as tax.

  Rule 9, added: «Deposits above the year's NOK 27,500 are not accepted. The player can only withdraw the whole BSU. The BSU then closes, and the deductions received so far are added to that month's tax.»

  D-text: «Forenklet: I spillet kan du bare ta ut hele BSU-en, og da avsluttes den. Du betaler også tilbake skattefradraget du har fått. I virkeligheten skal BSU brukes til bolig, og bruker du pengene til noe annet, mister du fradraget.»
- **Conflicts:** None.
- **Team decision:** Recommend accept.

### M12. Everyday costs set by choices (needed for UJ-4)

- **Findings:** A11 (cause), and it affects A12 and the goal area
- **Problem:** The engine has fixed costs (mobile, transport) and one-off event costs, nothing else. From 18, a 10 h/week wage of NOK 8,452 minus NOK 549 in fixed costs leaves about NOK 7,900 a month untouched. Card trouble then needs huge one-off purchases, a first-card debt is gone within weeks, and UJ-4 can't happen (M13). The money-against-wellbeing trade-off behind the hollow win also loses its everyday lever.
- **Recommendation:** an event option can start, change or stop a **monthly everyday cost**, such as canteen lunches, a subscription, the gym or fuel for borrowing the car. It's charged in the fixed-cost step every month until a choice stops it. Each one stores its choice as a cause link, a card-payable flag and an optional binding period (subscriptions with a binding period are already an event topic in FR-17). The player can stop any cost without a binding period from the money view, which is how "spending less" works. Amounts are event content with a source (NFR-4) [needs figure: a sourced youth spending level, for example SIFO's reference budget]. The social-life effect comes from the choice that starts or stops the cost, so no new meter is needed.
- **Why:** It reuses fixed costs and the planned subscription events, and it gives "spend less" a real effect in kroner.
- **Alternative:** one spending level (low, normal or high) that the player sets, with configurable amounts and a social-life effect.
- **Lands in:** PRD FR-23 (renamed "Fixed and everyday costs"), FR-17 schema (monthly-cost effect), FR-45 money actions, rule 1 (M1 wording). The goal and wellbeing areas should check goal reachability with it.
- **Draft text:** FR-23, added: «Some event options start, change or stop a monthly everyday cost, such as canteen lunches or a subscription. It's charged with the fixed costs until a later choice stops it. A cost with a binding period can't be stopped before the period ends.» Consequences: «Each everyday cost links to the choice that started it.» «The player can stop an everyday cost without a binding period from the money view.» «With card use on, card-payable costs go on the card (FR-26).»
- **Conflicts:** None logged. It's a scope addition, though it builds on content already planned.
- **Team decision:** Needed.

### M13. UJ-4: consistent numbers and a month-by-month trace

- **Findings:** A11
- **Problem:** The finding holds, and it goes further than the limit:
  - **Debt against wage:** the NOK 10,000 limit is 1.2 × a NOK 8,452 wage, which is larger but not "much larger".
  - **Moped sale:** a used moped (NOK 13,750) is worth about NOK 8,800 after two years at an illustrative 20% a year (the share isn't set yet, OQ-8). That pays off almost all of the debt.
  - **Extra shifts:** each extra hour a week pays NOK 845 a month. Five months at +4 h is about NOK 16,900, more than the whole debt.
  - **Free cash:** without M12, Markus has about NOK 7,900 a month free and clears the card in about six weeks with neither the sale nor the shifts.
  - **Trigger reach:** the edge case's 3× trigger is out of reach on his wage (3 × 8,452 = NOK 25,356). At the minimum the debt shrinks slowly; it doesn't "keep growing".
  - **Conclusion:** with a NOK 10,000 limit, the sale and five months of extra shifts can't both be true.
- **Recommendation:** keep the NOK 10,000 limit, every step-2 figure and the five months. Markus checks what his moped would sell for and keeps it. This needs M1, M2 and M12.

  **Entry state at month W:** age 18. Card bill NOK 10,000 at the debt step, at the limit after the city trip, lunches and fuel. Payment setting: the whole balance ("like a debit card"). No savings. Wage 10 h/week, NOK 8,452. Mobile NOK 299 and moped insurance NOK 250. Everyday costs (lunches, fuel, going out) NOK 7,500 a month (illustrative, [needs figure]). Tax is NOK 0, which holds while his wages so far this year stay under NOK 99,650, for example if W falls in January-May at 10 h/week from January (calendar: A14). Any spending path that ends with a NOK 10,000 bill and about NOK 400 free gets here.

  | Month | Wage | Costs | Free for the card | Bill | Interest | Paid | Card after | What happens |
  |---|---|---|---|---|---|---|---|---|
  | W | 8,452 | 549 + 7,500 | 403 | 10,000 | 188 | 403 | 9,785 | Interest starts, so the card warning shows: NOK 188 this month, and 51 months and NOK 5,508 at the minimum (step 2, unchanged). Talks to his mother: the family draw gives no money. Turns the card off, asks for one extra 2-hour shift a week, cuts NOK 400 a month. Checks the moped: about NOK 8,800, less than he owes, and he'd pay for the bus without it. Keeps it. |
  | W+1 | 10,142 | 549 + 7,100 | 2,493 | 9,785 | 184 | 2,493 | 7,476 | 12 h/week, well within rule 10 (40 h at 18+) |
  | W+2 | 10,142 | 549 + 7,100 | 2,493 | 7,476 | 141 | 2,493 | 5,124 | |
  | W+3 | 10,142 | 549 + 7,100 | 2,493 | 5,124 | 97 | 2,493 | 2,728 | |
  | W+4 | 10,142 | 549 + 7,100 | 2,493 | 2,728 | 51 | 2,493 | 286 | |
  | W+5 | 10,142 | 549 + 7,100 | 2,493 | 286 | 0 | 286 | 0 | Paid in full, no interest: back on track, with NOK 2,207 left |

  He pays NOK 661 in interest in total, against NOK 5,508 at the minimum. No trigger fires: he never misses the minimum, his account never goes below zero, and his debt stays under NOK 25,356. Wellbeing follows FR-33: free time down for five months, stress down as the debt falls.
- **Why:** It keeps every confirmed figure (the NOK 10,000 limit, NOK 188, NOK 350, 51 months, NOK 5,508), the warning moment, extra shifts, spending less and the five months. It still teaches depreciation through the price he checks. The engine reproduces it month by month under rules 1, 2 and 5.
- **Alternative:** keep the sale by raising the default first limit to NOK 20,000, still under the NOK 30,000 line in utlånsforskriften § 3. Step 2 becomes NOK 377 of a NOK 700 minimum, 94 months and NOK 17,171. A NOK 8,800 sale then leaves about NOK 11,000, which takes five months at about NOK 2,500 a month.
- **Lands in:** PRD UJ-4 (entry state, step 1, step 5, edge case), PRD addendum "Credit card debt, family and the moped in UJ-4" (the trace, and the sentence about interest pushing debt above 3× income), worked example 13 (optional).
- **Draft text:**
  - Entry state, added: «He pays his card bill as if it were a debit card: the bank takes what's on his account each month.»
  - Step 1: «The game warns him that his card debt has reached its NOK 10,000 limit, more than a month's wage, and that he couldn't pay it all by the deadline, so interest has started. This isn't a crisis month yet, and he decides for himself whether to act.»
  - Step 5: «He checks what his moped would sell for. After two years its price has dropped with age and use, so selling it wouldn't cover the debt, and he'd have to pay for the bus instead. He keeps it.»
  - Edge case, "He ignores the warning": «the debt barely shrinks, and interest keeps costing him about NOK 180 a month. If he misses the minimum two months in a row, a crisis month starts. If a crisis is still active when he turns 20, the game ends in a loss.»
  - PRD addendum, replace "or if interest pushes the debt above 3× average monthly income" with «With a NOK 10,000 limit, the 3× income trigger is out of reach on a 10-hour wage (3 × NOK 8,452 = NOK 25,356), so in UJ-4 only the missed minimum can start a crisis.»
- **Conflicts:** UJ-4 is confirmed, and the memlog (2026-11-04, SE) records the resolution as "sells the moped, not enough; extra shifts for five months". The recommendation drops the sale. The alternative keeps the sale but changes confirmed figures (memlog 2026-11-04 and 2026-11-05) and A-18's NOK 5,000-10,000 range. A third route, keeping the sale and shortening to about two months, loses the five months instead.
- **Team decision:** Needed.

### M14. Worked examples for the new money rules

- **Findings:** A33 (card warning, family loan payoff, 3× trigger with and without a family loan, crisis cadence), plus the other rules above
- **Problem:** §8.3 promises worked examples and unit tests for the new rules, but none exist.
- **Recommendation:** add examples 7-15 to the brief addendum's answer key. Each is a unit test.
- **Why:** The engine is tested against the rules, not against whatever the developer wrote.
- **Lands in:** brief addendum "Worked examples" (rows 7-15), PRD §8.3 (list of covered rules), NFR-9.
- **Draft text:**

  | # | Situation | Expected result |
  |---|---|---|
  | 7 | Card warning. Setting: whole balance. Last month paid in full. Bill NOK 6,000; current account and savings hold NOK 4,000 | Pays NOK 4,000. Interest NOK 113. Balance NOK 2,113. Warning this month, reason "couldn't pay". At the minimum, the NOK 6,000 bill would take 26 months and NOK 1,599 in interest. Next month the account covers NOK 2,113: paid in full, no interest, no warning |
  | 7b | Card warning, chosen. Setting: minimum. Bill NOK 3,000; account holds NOK 20,000 | Interest NOK 57, pays NOK 300, balance NOK 2,757. Warning, reason "chose to pay less", with an option to pay the whole balance. At the minimum: 12 months, NOK 357 |
  | 8 | Family loan of NOK 5,000 over 6 months at 0% | NOK 833 five times and a final NOK 835. If the account can't cover month 3, that instalment moves to the end: 7 months, still NOK 5,000, never below NOK 0 |
  | 9 | Debt trigger, age 19, wage NOK 8,452 in each of the last three months (limit NOK 25,356) | (a) Card NOK 9,000 + consumer loan NOK 17,000, no savings: NOK 26,000, crisis next month. (b) Same, but the NOK 17,000 is a family loan: NOK 9,000, no crisis. (c) As (a) with NOK 2,000 in savings: NOK 24,000, no crisis. (d) No wage for three months, card NOK 4,000: floor NOK 5,000, no crisis; card NOK 6,000: crisis. (e) A NOK 8,800 moped sale leaves the average unchanged |
  | 10 | Crisis cadence, cooldown 2 | Below zero at the end of month 40: crisis in month 41, ignored. Months 42-43: cooldown, crisis shown. Still below zero at the end of month 43: crisis in month 44. The first linked choice sells the moped, the account is back above 0, and the crisis ends after one choice. Debt passes the 3× line at the end of month 45: shown, but month 46 is still in the cooldown. Still true at the end of month 46: crisis in month 47 |
  | 11 | Month 60 | Trigger true at the end of month 58: crisis in month 59. Still true at the end of month 59: month 60 is a crisis month despite the cooldown. Minimum missed in months 58 and 59 and paid in month 60: not a loss. A random expense first takes the account below 0 at the end of month 60: not a loss, and the summary names it |
  | 12 | Payment plan for a NOK 10,000 card balance | 12 months at 22.6%: NOK 939 eleven times, a final NOK 935, NOK 11,264 in total (NOK 1,264 interest), against 51 months and NOK 5,508 at the minimum. The card is blocked until the plan is paid |
  | 13 | Consumer loan cap. Average wage NOK 8,452, card balance NOK 4,000 | Maximum NOK 25,356 − 4,000 = NOK 21,356, rounded down to NOK 21,000. Example 3's NOK 20,000 fits. No wage in one of the last three months: no loan offered |
  | 14 | BSU cap. NOK 20,000 deposited earlier in the calendar year, then a NOK 10,000 deposit | NOK 7,500 accepted; NOK 2,500 stays in the current account |
  | 15 | Fixed costs before 18. No job, NOK 10,000 pengegave kept in savings | No mobile or transport costs before 18, so never below NOK 0 before 18. Under the current FR-23 (NOK 537 a month from 15), the account would go below 0 after about 19 months |

  §8.3, last paragraph: «The new rules from this PRD get worked examples and unit tests in the same way (brief addendum examples 7-15). These cover the card warning, family loans, the debt trigger, crisis cadence, month 60, the payment plan, consumer loan limits, the BSU cap, fixed costs before 18 and the moped's resale value.» The moped resale and wellbeing examples come from other areas.
- **Conflicts:** None. The figures depend on M1-M11 being accepted. If a proposal changes, its examples change with it.
- **Team decision:** Recommend accept.

## G. Life goals, wellbeing, time and ownership
Findings covered: A4 (goal side), A5, A6, A13, A14, A15, A33 (part), A38, E1, E15, E16, E17, E21, E22, E28, E29, E30, E33, E34, E35. All findings were checked against the PRD, Rule Set v1 and the memlog. Each is real: none is already handled.

New Rule Set v1 rules are numbered 11-14 and new worked examples 7-11. These numbers are placeholders, because other proposals also add rules and examples. Renumber when merging. Calculations were run with a small script applying rules 2-4 month by month.

### G1. An in-game calendar: January birthday, school years and tax years

- **Findings:** A14, E21
- **Problem:** The game counts months from the 15th birthday, but tax, frikort, trygdeavgift and the BSU deduction work per calendar year, and school status sets the hour limits. With no start month, birthday month or school calendar, every implementer places them differently.
- **Recommendation:** Every player is born in January.
  - Game month 1 is January of the year the player turns 15. Month 60 is December of the year they turn 19. The game ends on the 20th birthday, after month 60.
  - Game year k (months 12k − 11 to 12k) is one calendar year, one tax year and one session. The player is 14 + k all year.
  - The school year runs from August to June, and July is the summer month. Grunnskole: months 1-18 (9th grade in months 1-6, 10th grade in months 8-18). Upper secondary school (three years): months 20-54. Out of school from month 55.
  - Rule 3 restarts year-to-date income in months 1, 13, 25, 37 and 49. The 5.1% trygdeavgift rate applies in game years 1-2, which are the calendar years before the year the player turns 17 (NAV rundskriv to ftrl. § 23-3, research `remaining-pre-prd-research-2026-10-31` C3). From game year 3, the rate is 7.6%. The NOK 99,650 lower limit and frikort are per game year. The BSU deduction (rule 9) comes in months 12, 24, 36, 48 and 60.
  - The Virke/HK rate follows age: NOK 136.41 in months 1-12, NOK 139.40 in months 13-36 and NOK 195.04 in months 37-60.
  - The December summary shows the year's tax and BSU deduction.
  - Test: a unit test maps months 1, 7, 12, 13, 18, 19, 25, 37, 54 and 55 to age, school status, hourly rate and trygdeavgift rate (worked example 7). Another test checks that year-to-date income restarts in month 13 and that the BSU deduction happens only in December months.
- **Why:** With one calendar year per session, tax, frikort and BSU line up with what the player sees, and there are no partial tax years. Age stays the same all year, which keeps the tests simple.
- **Alternative:** An August birthday, so sessions follow school years. Tax years would then cut across sessions.
- **Lands in:** brief addendum new rule 11 and worked example 7; PRD FR-12 (new consequence), FR-21 (replaces the second consequence), §3 Glossary (Session); a D-text, for whoever owns A32.
- **Draft text:**

  Brief addendum, new rule:
  > 11. **Calendar.** The player is born in January. Game month 1 is January of the year the player turns 15, and month 60 is December of the year they turn 19. The game ends on the 20th birthday, after month 60. Game year k (months 12k − 11 to 12k) is one calendar year: the player is 14 + k all year, and it is the income year for rules 3 and 9. The school year runs from August to June, and July is the summer month. The player is in grunnskole in months 1-18 (10th grade from month 8), in upper secondary school in months 20-54, and out of school from month 55. Trygdeavgift is 5.1% in game years 1-2, the years before the calendar year the player turns 17.

  PRD FR-12, new consequence:
  > - **Calendar (rule 11):** month 1 is January, at the 15th birthday. Each session runs from January to December and is one tax year. Upper secondary school ends after month 54.

  PRD FR-21, replace "Tax uses the character's age in the game, with the simulated year fixed at 2026 rates." with:
  > - Each game year is one income year. Trygdeavgift is 5.1% in game years 1-2 and 7.6% from game year 3 (rule 11). Every year uses 2026 rates (D6).
  > - The December summary shows the year's tax and BSU deduction.

  PRD §3 Glossary, Session row:
  > | Session | One in-game year, from January to December, about 10-15 minutes on a phone. A playthrough is five sessions |

  D-text (Norwegian, player-facing):
  > «Forenklet: I spillet har alle bursdag i januar. Skoleåret går fra august til juni, og juli er sommerferie.»
- **Conflicts:** None. No start month was decided before. A-17 (tax uses in-game age and 2026 rates) still holds. This text replaces P10's rewording of FR-21.
- **Team decision:** Needed (the January birthday is a product choice).

### G2. Working hours as a job setting the player keeps

- **Findings:** A13, E22
- **Problem:** Wages, rule 10 and free time all depend on hours, but how the player sets them is left to UX in OQ-9. It's also unclear how weekly legal limits turn into monthly rounds, and what happens when grunnskole ends partway through the game.
- **Recommendation:** Add FR-20a and extend rule 10.
  - The player has at most one job at a time: a part-time job, or from month 55 a full-time job. A summer job can come on top of it in July.
  - The player sets weekly hours when taking a job, as whole hours from 1 up to the month's cap. The setting stays until the player changes it.
  - The player can change hours in any month, active or quiet, and can quit. The change counts at that month's choice step, so it applies from the next month's income step. These standing actions are only "set hours" and "sell the moped" (G7).
  - Monthly hours = weekly hours × 52 / 12. Monthly pay = monthly hours × the hourly rate for the player's age, rounded to whole kroner (rule 2). Check: 37.5 h × 52/12 × NOK 195.04 = NOK 31,694, which is the Virke/HK monthly rate for wage step 1. 10 h a week at 18 pays NOK 8,452, which matches the addendum's "about NOK 8,400".
  - Caps come from rule 10 and school status (rule 11). In months 1-18 the cap is 12 h a week, July included. That's safe, because no summer job is offered before 16, so the 35 h limit for weeks without school is never needed. From month 19 the cap is 40 h a week. Monthly cap = weekly cap × 52/12, rounded down: 52 h and 173 h. Daily limits aren't modelled, because the game doesn't track days.
  - A summer job is a set number of hours, 120 by default, paid in July (months 19, 31 and 43). Summer-job hours and part-time hours together must fit the monthly cap, so the engine cuts the offer to fit.
  - A full-time job is 37.5 h a week and can be raised to 40.
  - Extra shifts, in events, crisis months and UJ-4, raise the weekly setting. They're never above the cap, and they aren't offered to a player who has no job or is already at the cap.
  - Free time comes from hours (G5).
  - Test: setting 41 h, or 13 h in month 18, is rejected (NFR-7). 12 h at 15 pays NOK 7,093 a month. A July with 30 h a week of part-time work (130 h) cuts a 120 h summer job to 43 h.
- **Why:** One number per job drives pay, the legal limit and free time. It reuses rule 10 instead of adding a shift system, and the 52/12 factor reproduces the official monthly rate.
- **Lands in:** PRD new FR-20a; FR-20 (replaces the fourth consequence); FR-14 (new consequence); OQ-9 (narrowed); brief addendum rule 10 (new last paragraph).
- **Draft text:**

  PRD, new FR after FR-20:
  > #### FR-20a: Working hours
  >
  > A player with a job sets how many hours a week they work. The setting stays until they change it. Realizes UJ-4 and UJ-5.
  >
  > **Consequences (testable):**
  > - The player has at most one part-time or full-time job, plus a summer job in July. They set weekly hours when taking the job, and can change them or quit in any month. A change applies from the next month.
  > - Monthly pay is weekly hours × 52 / 12 × the hourly rate for the player's age, in whole kroner. A full-time week of 37.5 h at 18+ pays NOK 31,694 a month.
  > - Hours never go above rule 10: 12 h a week in grunnskole (months 1-18), and 40 h a week from month 19. A summer job and part-time hours share one monthly cap of 173 h.
  > - Extra shifts raise the weekly hours. They're offered only to a player with a job who is below the cap.
  > - More hours mean less free time (FR-33).

  PRD FR-20, replace "A full-time job becomes available after upper secondary school, from about 19." with:
  > - A full-time job is available from month 55, the July after upper secondary school, at age 19 (rule 11).

  PRD FR-14, new consequence:
  > - In a quiet month, the player can still change their hours or sell the moped (FR-20a, FR-29).

  PRD OQ-9:
  > | OQ-9 | What the avatar contains, and which control the player uses to set weekly hours. The mechanism is in FR-20a | UX | No |

  Brief addendum, rule 10, new last paragraph:
  > In the game, the player sets weekly hours. Monthly hours are weekly hours × 52 / 12, and the monthly cap is the weekly cap × 52 / 12, rounded down. In grunnskole (months 1-18, rule 11) the cap is 12 h a week in every month, because no summer job is offered before 16. From month 19 it is 40 h a week, and summer-job hours in July count towards the same monthly cap of 173 h. Daily limits aren't modelled.

  D-text:
  > «Forenklet: Du velger timer per uke, og spillet regner om til måned med 52 uker delt på 12 måneder. Skolen regnes som 30 timer i uka.»
- **Conflicts:** None. OQ-9 shrinks rather than being reversed. "About 19" (A-3) becomes month 55, at age 19 and a half.
- **Team decision:** Recommend accept.

### G3. A table of unlock ages

- **Findings:** A15
- **Problem:** Only credit has an exact unlock age. The summer job, part-time job, licences and full-time job are vague, so the teaser, event authors and engine can disagree. It's also unclear whether the under-16 rate is ever used.
- **Recommendation:** Replace FR-18's examples with a table keyed to rule 11 months.
  - A part-time job opens at 15, capped at 12 h a week. This is the only place the under-16 rate (NOK 136.41, months 1-12) is used. If the team says no, remove that rate from the configuration, and the early-game costs in A12 get harder.
  - The summer job opens at 16. That keeps the UJ-1 teaser "Next year the summer job unlocks" and worked example 1.
  - Test: for each row, the option is never offered in the month before it opens, and a forced request for it is rejected (NFR-7). The year-1 teaser names the summer job.
- **Why:** One table feeds the engine, the teasers and event authoring. It also answers "when exactly" for every age-gated option.
- **Alternative:** No job before 16. That's simpler, but it leaves months 1-18 with no income at all.
- **Lands in:** PRD FR-18 (replaces the description and consequences); UJ-1 step 5 (wording).
- **Draft text:**
  > #### FR-18: Unlock options by age
  >
  > New options open in set game months (rule 11). Realizes UJ-1 and UJ-4.
  >
  > | Option | Opens | Game month | Source |
  > |---|---|---|---|
  > | Savings account and BSU | 15 | 1 | FR-22. BSU has no lower age |
  > | Part-time job, up to 12 h a week (NOK 136.41 until month 12) | 15, in grunnskole | 1 | Rule 10. From 15, a minor can sign their own work contract (vergemålsloven § 10) |
  > | Moped licence | 16th birthday | 13 | FR-28. Class AM 146 from 16 |
  > | Owning a moped (buying, gift offer) | With a moped licence | 13 at the earliest | FR-29 |
  > | Part-time job, up to 40 h a week | After grunnskole | 19 | Rule 10 |
  > | Summer job | 16 | Offered in June, paid in July: months 19, 31, 43 | FR-20, worked example 1 |
  > | Car licence: the gift draw, then the paid licence | 18th birthday | 37 | FR-30 [needs source: class B minimum age, Statens vegvesen] |
  > | Credit card and consumer loan | 18th birthday | 37 | Rule 6 |
  > | Full-time job | After upper secondary school | 55 | FR-20 |
  >
  > **Consequences (testable):**
  > - No option is offered before its month, and the engine rejects a choice for one that hasn't opened (NFR-7).
  > - Teasers and recaps use the same table.
  > - In the MVP, only age unlocks options, not progress towards the goal.

  UJ-1 step 5: replace "a summer job opportunity" with "a part-time job offer". If the part-time job at 15 is rejected, use "saving for a moped licence" alone.
- **Conflicts:** UJ-1 (confirmed 2026-11-03) contradicts itself. Step 5 offers a summer job in year 1, while its resolution says "Next year the summer job unlocks". This keeps the teaser and changes step 5's example. UJ-4 says "had a moped since he turned 16", which means paying NOK 12,000 for the licence in month 13. That's realistic only with income before 16 or a large pengegave, which is one argument for the part-time job at 15.
- **Team decision:** Needed (the part-time job at 15 and the under-16 rate).

### G4. A formula for each life goal, measured on net position at 20

- **Findings:** A4 (goal side), A5, E15, E16, E17
- **Problem:** The goals have no formula. Nothing says which balances count, whether family loans or card debt count, or whether the experience must be bought. Borrowing just before 20 and holding the cash could win "save for something big".
- **Recommendation:** Add rule 13 and rewrite FR-9.
  - The check is made once, after month 60 has been processed, including its choice.
  - **Debt** = card balance + what's left of consumer loans + what's left of family loans. Family loans count here, although they don't count towards the 3× trigger.
  - **Net savings** = current account + savings account + BSU − debt.
  - **Available money** = current account + savings account − debt. BSU is left out, because BSU money is for housing.
  - Belongings, such as a moped, don't count. The player can sell them first.
  - **Save for something big:** net savings ≥ NOK 100,000.
  - **Be debt-free with a buffer:** debt = NOK 0, and current account + savings account ≥ NOK 50,000. That's almost six months of hybel rent at NOK 8,770 (SSB, parameter table).
  - **Afford a big experience:** available money + the experience price, if it was bought, ≥ the experience price. In words: the player went on the trip without ending in net debt, or can pay for it at 20. The experience is one item with a real, sourced price [needs figure]. It's bought in an event, with money from the current and savings accounts only, so no card or loan. For goal-3 players, the event is guaranteed in months 42 and 54 (June of years 4 and 5) until they buy it. The price should be clearly below NOK 100,000, so goal 3 is a different, nearer goal.
  - Reaching a target exactly counts (≥).
  - During play, the game shows progress towards the goal, worked out the same way.
  - **Borrowing never helps.** A loan adds the same amount to money and to debt, and every loan rate (15%, 22.6%) is above every savings rate (2.87%, 5.61%). A NOK 50,000 loan in month 59 (rule 4, 12 months) costs NOK 625 of interest in month 60, so net savings end NOK 625 lower. Family loans at 0% placed in BSU gain a little interest, but family loans come only from events, so this doesn't matter.
  - **Reference run (reachability).** Start with a NOK 10,000 pengegave, all in the savings account. Work no job until the summer jobs: 120 h in months 19, 31 and 43. Work part-time 8 h a week in months 20-54 and full-time 37.5 h in months 55-60. Pay mobile and transport (NOK 537 a month) from month 1, as FR-23 says today. Have no moped, licence, card or loan. Each month, spend half the wage left after tax and fixed costs, and save the rest at 2.87%. Result: net savings of NOK 211,398 at 20. The balance is NOK 74,618 at month 42 and NOK 126,255 at month 54. Tax is NOK 1,222 in year 4 and NOK 22,122 in year 5, and nothing before that. The run still reaches goal 1 when spending up to 76% of take-home pay, and goal 2 up to 88%. Its ending wellbeing is 76 (75 a month in school, 76 in full-time work), so a real win is possible.
  - Tests: the reference run reaches every target. The run plus a month-59 loan never changes "not reached" into "reached". There's one test per goal at the target and NOK 1 below it. An outstanding NOK 1 family loan fails goal 2. An experience bought in month 54 with available money of NOK 0 or more at 20 reaches goal 3 (worked example 9).
- **Why:** Each goal uses account state the engine already has, so F9 tests are simple. Measuring net position means borrowing can't win, and that teaches the right lesson.
- **Alternative:** Goal 3 reached only if the experience is bought by 20. That's simpler, but a player who saved up and had no chance to buy can't win.
- **Lands in:** brief addendum new rule 13, parameter rows for the targets, worked examples 9 and 11; PRD FR-9 (replaces the second consequence and adds consequences), §3 Glossary (new Net savings row), OQ-3 (the experience price), OQ-8 (defaults); event library (the experience event and its guaranteed months, for whoever owns A1).
- **Draft text:**

  Brief addendum, new rule:
  > 13. **Life goals at 20.** The goal is checked once, after month 60 has been processed, including its choice. Debt is the card balance plus what's left of consumer loans and family loans. Family loans count as debt here, although they don't count towards the 3× trigger in rule 8. Net savings = current account + savings account + BSU − debt. Available money = current account + savings account − debt. Belongings such as a moped don't count. Save for something big: net savings ≥ the target. Be debt-free with a buffer: debt is NOK 0, and current account + savings account ≥ the buffer target. Afford a big experience: available money, plus the experience price if the experience was bought, ≥ the experience price. The experience can only be paid for from the current and savings accounts. A goal measure equal to its target counts as reached.

  Parameter rows:
  > | Goal target: save for something big | NOK 100,000 net savings | Game design, tuning (OQ-8) |
  > | Goal target: debt-free buffer | NOK 50,000 in current and savings accounts, no debt | Game design, tuning (OQ-8); about six months of hybel rent |
  > | Big experience price | [needs figure] | To be researched and dated (OQ-3) |

  PRD FR-9 consequences (replace the second bullet, keep the first and last):
  > - The engine checks the goal once, at age 20, using rule 13. Reaching the target exactly counts.
  > - **Save for something big:** net savings, meaning the accounts and BSU minus all debt, of at least NOK 100,000.
  > - **Be debt-free with a buffer:** no debt at all, family loans included, and at least NOK 50,000 in the current and savings accounts. BSU doesn't count as a buffer.
  > - **Afford a big experience:** the player bought the experience in the game and didn't end up in net debt, or can pay for it from the current and savings accounts at 20. The experience is offered in months 42 and 54 until it's bought, and it can't be paid for on credit.
  > - Borrowing never helps. A loan taken in month 59 can't turn "goal not reached" into a reached goal (worked example 9).
  > - The targets and the experience price are configuration. An automated reference run that starts with NOK 10,000 reaches every target (worked example 11).
  > - The game shows progress towards the goal during play, worked out the same way.

  PRD §3 Glossary, new row:
  > | Net savings | Current account, savings account and BSU, minus all debt, family loans included. The savings goal uses it (rule 13) |
- **Conflicts:** None. A-1 ("an amount the game sets, reachable by 20, such as a start on a flat deposit") is kept. UJ-5 ("saved towards his flat, has no debt") fits. Leaving BSU out of goals 2 and 3 assumes the BSU withdrawal rule from A16 keeps BSU for housing.
- **Team decision:** Needed (goal 3 bought or affordable, BSU left out of the buffer, and the defaults).

### G5. Wellbeing as one score from 0 to 100

- **Findings:** A6, E35
- **Problem:** Wellbeing has no scale, no bounds and no rule for combining its parts. Nothing says whether the ending uses the final value or an average, so chained crises could push stress without limit, and one good last month could undo years.
- **Recommendation:** Add rule 12 and rewrite FR-33.
  - Stress (higher is worse), free time and social life are whole numbers from 0 to 100, kept within 0-100 every month.
  - **Free time** is worked out from hours each month: 100 − 2 × (school hours + weekly work hours − 30), kept within 0-100. School counts as 30 h a week in school months (months 1-54, not July). For example: 10 h of work a week in school gives 80, 20 h gives 60, and a full-time 37.5 h week after school gives 85. Events don't change free time directly.
  - **Stress** starts at 20 and **social life** at 60. Both carry over from month to month. Each event choice changes them by its own effect, at most ±20 per part.
  - **Monthly changes**, applied last in the month, after the choice:

    | If this month… | Stress | Social life |
    |---|---|---|
    | interest was charged on any debt | +5, not above 50 | |
    | free time is below 50 (working too much) | +5, not above 50 | −5 |
    | it's a crisis month | +10 | |
    | none of the above, and stress is above 20 | −5, not below 20 | |

  - **Wellbeing** = w1 × (100 − stress) + w2 × free time + w3 × social life, rounded to a whole number (0.5 rounds up). The weights add up to 100%. Defaults, as calm/free time/social: save for something big 40/30/30, debt-free with a buffer 50/25/25 (being debt-free is about peace of mind), and a big experience 30/30/40.
  - **Ending wellbeing** is the average of the monthly wellbeing in months 49-60, the last session, rounded the same way. The ending compares this shown number with the threshold, which is 50 by default.
  - **UI:** one bar from 0 to 100 with the threshold marked, plus three small bars. After each choice, the game shows the change ("+5 sosialt liv"). From month 49 it also shows "the average so far".
  - Add "→ wellbeing" as the last step of rule 1.
  - Tests: each part is clamped at 0 and 100 in long chains of crises. Worked example 8 is reproduced exactly. Overworking stops raising stress at 50, and a crisis month still raises it above 50.
- **Why:** Every input is something the engine already tracks: hours, interest charged, crisis months and choices. A 15-year-old can follow it in one sentence. The 12-month average stops a last-month fix, but a player can still recover from trouble at 18, as Markus does between UJ-4 and UJ-5.
- **Alternative:** Average over all 60 months. It's stricter, because early mistakes count as much as late ones.
- **Lands in:** brief addendum new rule 12, rule 1 (last step), parameter rows (weights, start values, threshold), worked example 8; PRD FR-33 (replaced), FR-12 (order sentence), §3 Glossary (Wellbeing, and a new Ending wellbeing row), OQ-8; event schema (the wellbeing effect becomes two numbers, for whoever owns A35).
- **Draft text:**

  Brief addendum, new rule:
  > 12. **Wellbeing.** Stress, free time and social life are whole numbers from 0 to 100. Stress starts at 20 and social life at 60. Each month, free time = 100 − 2 × (school hours + weekly work hours − 30), within 0-100. School counts as 30 hours a week in school months (rule 11), and weekly work hours are the month's hours ÷ (52 / 12). Each event choice changes stress and social life by its own effect, at most 20 points either way. Last in the month, after the choice: if interest was charged on any debt, stress rises by 5, but not above 50. If free time is below 50, stress rises by 5, but not above 50, and social life falls by 5. In a crisis month, stress rises by 10. If none of these apply and stress is above 20, it falls by 5, but not below 20. Each part is then kept within 0-100. Wellbeing = w1 × (100 − stress) + w2 × free time + w3 × social life, rounded to a whole number (0.5 rounds up), with weights set by the life goal that add up to 100%. Ending wellbeing is the average wellbeing in months 49-60, rounded the same way.

  PRD FR-33 (replace the requirement):
  > #### FR-33: Wellbeing
  >
  > Wellbeing is one score from 0 to 100, made from three parts (rule 12):
  > - **Stress** rises with interest on debt, crisis months and working too much, and falls again when they stop.
  > - **Free time** follows the hours of school and work.
  > - **Social life** follows the choices made in events, and falls when the player works too much.
  >
  > The life goal sets how much each part counts. Realizes UJ-4 and UJ-5.
  >
  > **Consequences (testable):**
  > - Each part and the score stay between 0 and 100.
  > - Every event choice states its effect on stress and social life, which may be 0. Free time changes only with hours.
  > - In UJ-4, extra shifts lower free time and social life, interest raises stress, and paying the debt off lets it fall again (worked example 8).
  > - The ending uses the average score over the last 12 months, rounded to a whole number. One good last month can't make up for a bad year.
  > - The game shows the score, its three parts and the threshold. In the last year, it also shows the average so far.
  > - The weights, start values, monthly changes and threshold are configuration (OQ-8).

  PRD FR-12, order sentence: "…interest on savings, then the month's event and the player's choice, and last wellbeing."

  PRD §3 Glossary:
  > | Wellbeing | A score from 0 to 100 made from stress, free time and social life, weighted by the life goal (rule 12) |
  > | Ending wellbeing | The average wellbeing over the last 12 months, months 49-60. The endings use it |

  D-text:
  > «Trivselen er et tall i spillet. Den bygger på stress, fritid og sosialt liv, og sier ikke noe om hvordan du har det i virkeligheten.»
- **Conflicts:** The 2026-11-03 decision lists stress "from debt and crisis months" and social life "from choices in events". This adds overwork to both. That fits UJ-4 ("fewer social things") and UJ-5 ("chasing as much money as possible often … raises his stress"). The event schema's "wellbeing effect for each choice" becomes two numbers: stress and social life.
- **Team decision:** Needed (the model, weights, threshold and the 12-month window).

### G6. Endings at 20: the threshold boundary and one ending per state

- **Findings:** E1 (with A6)
- **Problem:** "Above" and "below" the threshold leave equality uncovered. A player who reached the goal with wellbeing exactly at the threshold matches neither win, and falls through to "Goal not reached".
- **Recommendation:** Keep the FR-41 order. The real win needs ending wellbeing at or above the threshold, and the hollow win is below it. A goal measure equal to its target counts as reached (G4). The comparison uses the rounded number the player sees: an average of 49.5 is shown as 50 and gives the real win. "Active" for the loss uses the month-60 definition from the crisis proposal (A7, E8, E9). F9 gets one test for each of the eight combinations (crisis active or not × goal reached or missed × wellbeing at or above the threshold, or below), plus both boundaries.
- **Why:** It closes the gap, so every end state gives exactly one ending, and F9 can be written as a truth table.
- **Lands in:** PRD FR-41; brief addendum "Win Condition & Endgame — Decision" (the endings list) and worked example 9.
- **Draft text:**
  > At the 20th birthday, after month 60, the engine checks the endings in this order:
  > 1. **Loss:** a rule 8 crisis condition is active.
  > 2. **Real win:** the goal is reached (rule 13), and ending wellbeing is at or above the threshold (rule 12).
  > 3. **Hollow win:** the goal is reached, and ending wellbeing is below the threshold.
  > 4. **Goal not reached:** none of the above. The player gets advice on modest savings goals and what they bring.
  >
  > New consequence:
  > - Ending wellbeing exactly at the threshold gives the real win, and a goal measure exactly at its target counts as reached (worked example 9).
- **Conflicts:** The 2026-11-03 decision says "wellbeing above the threshold". This makes equality explicit without changing the intent.
- **Team decision:** Recommend accept.

### G7. Moped: gift conditions, resale value and costs only while owned

- **Findings:** A38, E28, E29, E30, E33
- **Problem:** Several moped rules are missing. A gift offer can reach a player with no licence, or one who already has a moped. The resale value of a new moped, and its value after part of a year, are undefined. Repairs and moped events can come after a sale, and the public transport ticket and moped costs can both be charged in the same month.
- **Recommendation:** Add rule 14 and update FR-23, FR-24 and FR-29.
  - The player can own at most one moped, and only with the moped licence.
  - A gift offer comes only to a player who has the licence and owns no moped, at most once per playthrough. A gift moped is a used moped.
  - Start value = the price paid (new NOK 29,000 or used NOK 13,750), or NOK 13,750 for a gift.
  - Resale value = start value × (1 − 15% × months owned / 12), in whole kroner, never below 20% of the start value. Months owned = the sale month − the month the player got the moped. The 15% and 20% are tuning values (OQ-8), because research found no Norwegian resale figures. With 15%, the 20% floor is never reached within the 48 months a player can own a moped. It only protects higher tuned rates.
  - Running costs are charged at the fixed-cost step in each month the player owns the moped at that step: insurance of NOK 250 (NOK 3,000 a year ÷ 12), plus fuel at [needs figure: litres a month] × NOK 20.64. A moped got in month m is first charged in month m + 1, and one sold in month m is last charged in month m. Since costs are monthly, a sale needs no refund.
  - Transport is the public transport ticket (NOK 238) only in months without a moped. With a car licence, car fuel ([needs figure: litres a month] × NOK 20.64) is added every month, as decided on 2026-11-04.
  - Moped repairs and moped events need the player to own a moped when they're drawn.
  - Selling is a standing action in any month (G2), and also an option in crisis months. It counts at that month's choice step, and the moped then leaves the room.
  - The parents' share of the insurance (cut list item 2) is drawn once, when the player gets the moped, and stored.
  - Tests: the gift is never offered without a licence or to a player who owns a moped. The values match worked example 10. The ticket and the moped costs never appear in the same month. No repair is drawn after a sale.
- **Why:** It reuses fixed costs and draw-time eligibility. A new moped no longer loses half its value on day one, and the value can't go negative.
- **Alternative:** Car fuel only through events where the player borrows the car, instead of every month. It's more accurate, but it changes the 2026-11-04 decision.
- **Lands in:** brief addendum new rule 14, parameter rows (depreciation rate and floor), worked example 10; PRD FR-23 (description and consequences), FR-24 (new consequence), FR-29 (replaces the resale and selling consequences, adds new ones), OQ-8.
- **Draft text:**

  Brief addendum, new rule:
  > 14. **Moped.** The player owns at most one moped and needs the moped licence to own one. The start value is the price paid (new NOK 29,000, used NOK 13,750), or NOK 13,750 for a gift moped. Resale value = start value × (1 − 15% × months owned / 12), rounded to whole kroner, never below 20% of the start value. Months owned = the sale month − the month the player got the moped. In a month when the player owns a moped at the fixed-cost step, transport is moped insurance (NOK 250) and moped fuel, and the public transport ticket isn't charged. A moped got in month m is first charged in month m + 1, and a moped sold in month m is last charged in month m.

  PRD FR-29 consequences:
  > - **One moped, with a licence:** the player can own one moped at a time, and only with the moped licence.
  > - **Gift offers:** a gift offer comes only to a player who has the moped licence and owns no moped, at most once per playthrough. A gift moped is a used moped.
  > - **Resale value:** it starts at the price paid, or at the used price for a gift. It drops by 15% of that each year, a little each month, but never below 20% (rule 14). A used moped sold after two years fetches NOK 9,625 (worked example 10).
  > - **Costs only while owned:** insurance and fuel are charged only in months the player owns the moped (FR-23). Repairs and moped events are drawn only while they own one (FR-24).
  > - **Selling:** the player can sell the moped in any month at its current resale value. Public transport comes back from the next month, and the moped disappears from the room.

  PRD FR-23 description:
  > Mobile and transport costs are deducted every month. Transport is the public transport ticket, or moped insurance and fuel in months when the player owns a moped (rule 14). With a car licence, car fuel for borrowing the parents' car is added. Realizes UJ-4.

  PRD FR-23, new consequence:
  > - The ticket and the moped costs are never charged in the same month.

  PRD FR-24, new consequence:
  > - An expense tied to something the player owns, such as a moped repair, is drawn only while they own it.

  D-text:
  > «Forenklet: Mopeden taper 15 % av kjøpsprisen hvert år. I virkeligheten avhenger prisen av modell, stand og hvor mye den er brukt.»
- **Conflicts:** FR-29 says the value starts "from real used prices", and the 2026-11-04 decision says it "drops by a fixed share per year owned". This proposal starts at the price paid and spreads the same yearly share over months. UJ-4 step 5 ("the sale doesn't cover the debt") holds against NOK 10,000 of debt for a used or gift moped (about NOK 9,100-9,600), but not for a new one (NOK 20,300). That's for whoever writes the UJ-4 worked example (A11).
- **Team decision:** Recommend accept. The rate and floor are tuning values.

### G8. Car licence: draw the gift before the paid licence is offered

- **Findings:** E34
- **Problem:** The gift draw has no fixed time. A player could pay NOK 32,500 for the licence and then also get it as a gift.
- **Recommendation:** In month 37 (the 18th birthday), the engine draws once whether the parents give the car licence, and stores the result. The chance is 50% by default, as a tuning value (OQ-8). It's shown in the first active month from month 37. With the gift, the player has the licence at NOK 0 and is never offered the paid one. Without it, the paid licence (NOK 32,500) is offered from the month the result is shown, and later events can offer it again. It's never offered before the draw. Like FR-28, the licence is a payment only. Test: in seeded runs with the gift, the paid option never appears. Without the gift, it never appears before the result is shown.
- **Why:** A fixed order rules out paying and also getting the gift, and it doesn't need any refund rule.
- **Lands in:** PRD FR-30 (requirement text and consequences), OQ-8.
- **Draft text:**
  > By age 18, some players get a car licence as a gift from their parents. In month 37, the engine draws once whether the gift comes, and stores the result. A player without the gift can pay for the licence at a real price. With a licence, the player pays for fuel when borrowing the parents' car. Realizes UJ-4.
  >
  > **Consequences (testable):**
  > - The gift is drawn before the paid licence is offered. A player with the gift is never offered the paid licence.
  > - The gift costs the player nothing. Car fuel is a transport cost (FR-23).
  > - The licence is a payment only, as in FR-28.
  > - How often the gift comes is configuration (OQ-8).
  > - Every price has a source and a date (#29).

  D-text, shared with FR-28:
  > «Forenklet: Førerkortet er bare en betaling i spillet. Du kjører ikke opp og kan ikke stryke.»
- **Conflicts:** None. It fits the 2026-11-05 decision: "random car licence gift with option to pay".
- **Team decision:** Recommend accept.

### G9. Worked examples for this area

- **Findings:** A33 (part: wellbeing over UJ-4, the F9 endings including the boundary, moped resale after two years)
- **Problem:** §8.3 promises worked examples and unit tests for the new rules, but there are none.
- **Recommendation:** Add these examples to the brief addendum's answer key. Each becomes a unit test (NFR-9). §8.3 or NFR-4 names them. The defaults are those in G1-G8: goal "save for something big", target NOK 100,000, threshold 50.
- **Why:** New engine logic is tested against agreed numbers, not against whatever the developer wrote.
- **Lands in:** brief addendum, Worked examples (7-11); PRD §8.3 (list).
- **Draft text:**

  **7. Calendar and pay (rules 10-11)**

  | Game year | Months | Age | School | Hourly rate | Trygdeavgift | Weekly cap |
  |---|---|---|---|---|---|---|
  | 1 | 1-12 | 15 | 9th grade (1-6), summer (7), 10th grade (8-12) | 136.41 | 5.1% | 12 h |
  | 2 | 13-24 | 16 | 10th grade (13-18), summer (19), Vg1 (20-24) | 139.40 | 5.1% | 12 h to month 18, then 40 h |
  | 3 | 25-36 | 17 | Vg1 (25-30), summer (31), Vg2 (32-36) | 139.40 | 7.6% | 40 h |
  | 4 | 37-48 | 18 | Vg2 (37-42), summer (43), Vg3 (44-48) | 195.04 | 7.6% | 40 h |
  | 5 | 49-60 | 19 | Vg3 (49-54), out of school (55-60) | 195.04 | 7.6% | 40 h |

  The BSU deduction comes in months 12, 24, 36, 48 and 60. 10 h a week at 18: 10 × 52/12 × 195.04 = NOK 8,452 a month. Full-time, 37.5 h: NOK 31,694. A summer job in month 19 is 120 × 139.40 = NOK 16,728, as in worked example 1.

  **8a. Wellbeing over UJ-4 (rule 12).** Markus, 18, in Vg2, works 10 h a week. He starts at stress 20, free time 80, social life 60, wellbeing 74. Weights 40/30/30. The timing follows UJ-4's story, and the kroner amounts come from the UJ-4 worked example.

  | Month | What happens | Hours | Stress | Free time | Social | Wellbeing |
  |---|---|---|---|---|---|---|
  | 1 | Card interest starts, and the warning shows. He stops the card and takes extra shifts (social −5) | 10 | 25 | 80 | 55 | 71 |
  | 2 | Interest. Extra shifts start. He sells the moped (social −5) | 20 | 30 | 60 | 50 | 61 |
  | 3 | Interest, quiet month | 20 | 35 | 60 | 50 | 59 |
  | 4 | Interest. He turns down a cabin weekend (social −5) | 20 | 40 | 60 | 45 | 56 |
  | 5 | Interest, quiet month | 20 | 45 | 60 | 45 | 54 |
  | 6 | The card is paid in full, so no interest. He sets 10 h from month 7 | 20 | 40 | 60 | 45 | 56 |
  | 7 | He goes to a party (social +10) | 10 | 35 | 80 | 55 | 67 |
  | 8-10 | Quiet months | 10 | 30, 25, 20 | 80 | 55 | 69, 71, 73 |

  For example, month 4: 0.4 × 60 + 0.3 × 60 + 0.3 × 45 = 55.5, which rounds to 56. Wellbeing never drops below 50, so a real win at 20 is still possible.

  **8b. Ending wellbeing.** A careful player works 10 h a week to month 54, then 37.5 h full-time: wellbeing is 74 in months 49-54 and 76 in months 55-60, so ending wellbeing is 75. A money chaser starts month 49 at stress 20 and social life 40. He works 40 h a week in school in months 49-54, so free time is 20 and he's overworking, then 40 h full-time with free time 80. His monthly wellbeing is 47, 43, 40, 36, 33, 29, 49, 51, 53, 55, 57, 59, so ending wellbeing is 46, which is below 50.

  **9. Endings at 20 (rule 13, FR-41)**

  | # | State after month 60 | Ending |
  |---|---|---|
  | a | Current account −NOK 400 (rule 8 active), net savings NOK 120,000, ending wellbeing 70 | Loss |
  | b | Crisis condition active, net savings NOK 30,000, ending wellbeing 30 | Loss |
  | c | No condition, net savings NOK 100,000 (exactly the target), ending wellbeing 62 | Real win |
  | d | No condition, net savings NOK 112,000, months 49-60 sum to 594 (average 49.5, shown as 50) | Real win (boundary) |
  | e | As d, but the sum is 593 (average 49.42, shown as 49) | Hollow win |
  | f | No condition, net savings NOK 99,999, ending wellbeing 80 | Goal not reached |
  | g | No condition. Without a loan, net savings would be NOK 95,625. With NOK 50,000 borrowed in month 59 (rule 4, 12 months, instalment NOK 4,513): cash NOK 141,112, loan left NOK 46,112, net NOK 95,000 | Goal not reached either way |
  | h | Debt-free goal: current and savings accounts NOK 60,000, BSU NOK 20,000, family loan NOK 1,500 left, ending wellbeing 70 | Goal not reached |
  | i | Debt-free goal: current and savings accounts NOK 50,500, BSU NOK 30,000, no debt, ending wellbeing 55 | Real win |
  | j | Experience goal: bought in month 54. At 20: current and savings accounts NOK 3,000, card balance NOK 2,000, so available money is NOK 1,000. Ending wellbeing 66 | Real win |
  | k | Experience goal: not bought, available money ≥ the price, ending wellbeing 46 (the money chaser in 8b) | Hollow win |

  **10. Moped resale and costs (rule 14)**

  | Moped | Start value | Months owned | Resale value |
  |---|---|---|---|
  | Used, bought month 16, sold month 40 | 13,750 | 24 | 13,750 × 0.70 = NOK 9,625 |
  | New, owned 24 months | 29,000 | 24 | 29,000 × 0.70 = NOK 20,300 |
  | Gift, got month 13, sold month 40 | 13,750 | 27 | 13,750 × 0.6625 = 9,109.375, so NOK 9,109 |
  | Used, owned 7 months | 13,750 | 7 | 13,750 × 0.9125 = 12,546.875, so NOK 12,547 |
  | Floor check, rate tuned to 25%, 48 months | 13,750 | 48 | 0, so the floor of NOK 2,750 applies |

  For the used moped, bought in month 16 and sold in month 40: insurance is charged in months 17-40, so 24 × NOK 250 = NOK 6,000. The public transport ticket is charged in months 1-16 and 41-60, and never together with the moped's costs.

  **11. Reference run for goal reachability (rule 13).** The pattern is in G4. Net savings at 20: NOK 211,398, with no tax in years 1-3, NOK 1,222 in year 4 and NOK 22,122 in year 5. The balance is NOK 74,618 in month 42 and NOK 126,255 in month 54. Ending wellbeing is 76. Every target is reached. The lowest balance is NOK 550, in month 18.
- **Conflicts:** None.
- **Team decision:** Recommend accept.

### Notes for other areas

- **A12 (who pays the under-18 costs):** under today's FR-23, the reference run (G4) comes within NOK 550 of going below zero in month 18. Any unexpected expense before month 19 would start a crisis month for a careful player. If parents pay the fixed costs until 18, the lowest balance is NOK 10,024. With a 4 h a week job at 15 (G3), it's NOK 10,941.
- **A11 (UJ-4 numbers):** see G7. The moped sale fails to cover NOK 10,000 of debt only for a used or gift moped.
- **A16 (BSU withdrawal):** G4 leaves BSU out of the buffer and the experience goal. That's consistent if BSU stays for housing.
- **A1 (event scheduling):** these placements need to be guaranteed: the car licence draw from month 37, a part-time job offer by month 20, the full-time job offer in month 55, and the experience event in months 42 and 54 for goal-3 players. Eligibility checks at draw time cover owns_moped, has_moped_licence, has_job and has_car_licence.
- **A2 / E27 (stored draws):** the car licence gift and the parents' insurance share are drawn once and stored.
- **E23 (extra shifts):** extra shifts are offered only to a player with a job who is below the cap (G2).
- **A31 (NFR-7 rejections):** hours above the cap, an option before its month, a second moped, a moped without a licence, the paid car licence before the draw or after a gift, and the experience paid for on credit.
- **A32 (D-texts):** draft texts for the calendar, hours, wellbeing, moped value and licences are in G1, G2, G5, G7 and G8, ready to number.
- **A7 / E8 / E9 (loss at 20):** G6 uses whatever "active" definition that proposal sets.

## X. Game loop, events, ending and content
Area: random draws, event scheduling and library size, schema terms, content versions, cause links and the ending screen, restart and return, onboarding resume, disclosures and room states.

Every finding below was checked against `prd.md`, the PRD addendum, the memlog and the brief addendum. All of them hold up, so none gets "No change". Three proposals need a team decision (X3, X7, X9), and one of those (X3) conflicts with a confirmed team decision.

| Proposal | Findings | Team decision |
|---|---|---|
| X1. Every random result is drawn once and stored | A2, E26, E27 | Recommend accept |
| X2. Event scheduling (new FR-17a) | A1, E31, E32, S2 | Recommend accept |
| X3. Library minimum that supports replay | A34 | **Needed** (conflicts with "min 30") |
| X4. Glossary and schema terms | A35, S5 | Recommend accept |
| X5. A playthrough keeps its content version | A17 | Recommend accept |
| X6. Cause links with shares | A18 (part), E37 | Recommend accept |
| X7. Ending ranking, texts and the hollow-win choice | A18, E38, E39, E41, P20 | **Needed** |
| X8. "If you had chosen differently" on the ending screen | A19, E40 | Recommend accept |
| X9. One life at a time, starting over, and coming back after the ending | A3, E42, E43 | **Needed** |
| X10. Resuming the start | E44 | Recommend accept |
| X11. Disclosure texts D7-D16, seen once per account | A32, E45 | Recommend accept |
| X12. Room layers | E36 | Recommend accept |

---

### X1. Every random result is drawn once and stored

- **Findings:** A2, E26, E27
- **Problem:** Only the pengegave is "drawn once and stored" (FR-11). Family help is drawn "each time" (FR-27, UJ-4), and nothing says when events, expenses or gift offers are drawn, so a player can reload until family says yes or a bad expense goes away. Stacked 0% family loans also bypass the 3× trigger.
- **Recommendation:**
  - Every random result is drawn by the engine once, stored before the player sees it, and reused. This covers the pengegave, which event an active month gets, a boomerang delay, the unexpected expense, gift offers (moped, car licence), the parents' insurance share and family help.
  - Family help is drawn once per event or crisis month. Asking again in the same event or crisis month gives the same answer.
  - At most one family loan at a time. While one is being paid back, family can still give advice or a gift, but doesn't lend more.
  - Every processed month, quiet or active, is saved as soon as it's processed.
  - A playthrough's random results can be reproduced from values stored when it starts. In the addendum: one seed per playthrough, and each draw is derived from the seed, the month and what is drawn (for example "family help, event E-41"), so it doesn't depend on the order of requests. Engine tests can set the seed or force a result.
- **Why:** It closes the reload exploit with one rule that also makes FR-12's "same draws, same result" testable across devices. One active family loan stops 0% loans being stacked to dodge rule 8.
- **Lands in:** PRD FR-12 (new consequences); FR-11 (unchanged, now a case of FR-12); FR-27 (changed and new consequences); PRD addendum (seed and draw identity); architecture (storage).
- **Draft text:**

  FR-12, add to **Consequences (testable):**
  > - **Random results:** every random result, such as the pengegave, which event comes next, an unexpected expense, a gift offer or whether family can help, is drawn by the engine once and stored before the player sees it. Reloading, logging in again or switching device shows the same result.
  > - **Reproducible:** a playthrough's random results can be reproduced from values stored when it starts, so engine tests can replay a whole playthrough from those values and the player's choices.
  > - Every processed month, quiet or active, is saved as soon as it's processed (FR-6).

  FR-27, replace the first consequence and add one:
  > - Help isn't always on offer, and it often covers only part of the amount. Whether family can help, and how much, is drawn once per event or crisis month and stored. Asking again in the same event or crisis month gives the same answer.
  > - A player has at most one family loan at a time. While it's being paid back, family can still give advice or a gift, but doesn't lend more.

  Test: reload at the family-help answer and on a second device; the answer, the month's expense and the next event are the same.
- **Conflicts:** None. It reads "drawn each time" (UJ-4 edge case, memlog 2026-11-04) as once per event or crisis month, which is a clarification. UJ-4 can optionally say "each time he asks in a new event or crisis month".
- **Team decision:** Recommend accept

---

### X2. Event scheduling (new FR-17a)

- **Findings:** A1, E31, E32, S2
- **Problem:** No FR says which months are active, which event fires, how age, flags and boomerang pairs gate it, what happens to a follow-up due after month 60, or what happens when no event fits. The only pacing target, "tuned to about 20-30 real choices", sits in the glossary and rule 7.
- **Recommendation:**
  - **Fixed active months:** each in-game year has the same active months, 5 by default (configuration). The default positions are months 1, 3, 5, 8 and 10 of each in-game year, so there are never more than two quiet months in a row, and months 59-60 are quiet. That gives 25 regular choices plus crisis choices, which matches "about 20-30" and the addendum's 4-6 choices a year.
  - **Pinned events:** month 1 is the pengegave choice. Milestones (age unlocks, FR-18) take the first active month at or after their unlock month.
  - **Eligibility:** age in range, required flags set, blocking flags not set, not seen in this playthrough. State such as owning a moped or having a card is a flag.
  - **Selection:** equal chances among eligible events, drawn and stored under X1.
  - **Boomerang pairs:** each pair has a delay range (2-12 months). The delay is drawn when the opener's option is picked, and the follow-up takes the first active month at or after it. An opener is eligible only if its longest delay still lands by the last active month (month 58 by default), so no follow-up falls after month 60. This avoids E31's "resolve it in the ending" special case.
  - **Collisions:** crisis month first, then milestones and follow-ups by due month (milestone wins a tie), then a drawn event. A pushed-out milestone or follow-up takes the next active month. This gives E7 (crisis area) its displacement rule.
  - **No repeats** within a playthrough. Crisis events follow FR-32.
  - **Fallback (E32):** no eligible event means a quiet month, never a repeat. The content check runs 1,000 seeded playthroughs with random choices (in CI, NFR-9) and reports every fallback month.
  - **Unexpected expenses stay automatic deductions** with a system cause, as FR-24 and the issue #26 detail say, not events. One per in-game year by default, in a drawn month, of a kind that fits the player then (a moped repair needs a moped). The player responds in the following months, or in the crisis month if it pushes the account below zero. None in months 59-60, unless the month-60 fix (A7/E8) sets a different window. Rule 1 should name where the expense falls; the suggestion is right after fixed costs (coordinate with E2).
- **Why:** A fixed template is the simplest way to guarantee the 20-30 choices and the 10-15 minute session, and it's trivially testable. Replays still differ through which events fill the slots. Gating openers removes the "after month 60" case completely.
- **Alternative:** Make expenses short events with a choice of how to pay. This gives the player a choice at the moment of the expense, but it changes the FR-24 system cause and costs active months.
- **Lands in:** PRD new FR-17a after FR-17; FR-24 (new consequences); §3 Glossary, Playthrough row (S2); OQ-8 (add active months per year, their positions, expenses per year and boomerang delay ranges); PRD addendum (default template and collision examples); brief addendum rule 1 (expense position, with E2).
- **Draft text:**

  > #### FR-17a: Event scheduling
  >
  > The engine decides which months are active and which event each active month gets. Realizes UJ-1 to UJ-5.
  >
  > **Consequences (testable):**
  > - **Active months:** every in-game year has the same active months, 5 by default, and the rest are quiet. Which months are active is configuration. A playthrough with no crisis months has 25 real choices, and crisis months add their linked choices, so a playthrough has about 20-30 real choices (rule 7).
  > - **Pace:** with the default, a session has 5 choices and 7 quiet-month summaries, which fits 10-15 minutes on a phone (checked in playtests).
  > - **First choice:** month 1 is always the pengegave choice (FR-11).
  > - **Milestones:** an event tied to an age unlock (FR-18), such as the credit card offer, takes the first active month at or after its unlock month.
  > - **Who can get an event:** an event can be drawn only when the player's age is in its age range, all its required flags are set, none of its blocking flags are set, and it hasn't appeared in this playthrough.
  > - **Drawn at random:** each other active month gets an event drawn from the eligible ones, each with the same chance. The draw is stored (FR-12).
  > - **Boomerang pairs:** when the player picks an option that opens a pair, the follow-up is due after a delay drawn from the pair's range, and takes the first active month at or after that. An opener can be drawn only if its longest delay still lands by the last active month, so no follow-up is lost after month 60.
  > - **When events collide:** a crisis month comes first (FR-32). Milestones and follow-ups come next, in the order they're due, and a drawn event comes last. A milestone or follow-up that is pushed out takes the next active month.
  > - **No repeats:** no event appears twice in one playthrough. Crisis events follow FR-32.
  > - **No eligible event:** the active month becomes a quiet month. The content check runs seeded test playthroughs and reports every month this happens.

  FR-24, add:
  > - **How often:** one unexpected expense per in-game year by default, in a drawn month, of a kind that fits the player then. For example, a moped repair needs a moped. The number, amounts and conditions are configuration.
  > - An unexpected expense is a deduction, not an event, so it doesn't use an active month. If it pushes the account below zero, rule 8 starts a crisis month where the player can respond.
  > - No unexpected expense is drawn for month 59 or 60.

  §3 Glossary, Playthrough row:
  > | Playthrough | One life, from 15 to the 20th birthday: 60 in-game months |
- **Conflicts:** None. Unexpected expenses stay a system cause, as FR-24 and the issue #26 detail in the brief addendum say. The month 59-60 window should match whatever A7/E8 decides.
- **Team decision:** Recommend accept

---

### X3. Library minimum that supports replay

- **Findings:** A34
- **Problem:** FR-17 and the cut list allow 30 events, but a playthrough uses 25 regular events (X2). Two playthroughs then share at least 20 of their 25 events (25 + 25 − 30), so the FR-43 promise "different choices, different story" and the 8.1 replay metric can't hold.
- **Recommendation:**
  - Floor of 50 regular events, which is 2× the regular active months. The 60-80 target and about 10 crisis events stay.
  - Every in-game year has at least 10 events whose age range covers it (2× its 5 active months).
  - The 55/45 split stays as guidance. Unexpected expenses are a separate list and don't count.
  - The cut list's last item becomes "events, down to 50".
  - The replay promise becomes testable: in the content check, pairs of seeded playthroughs with random choices share, on average, no more than two-thirds of their regular events.

  The calculation assumes about 8 milestones every playthrough gets (pengegave, summer and part-time job, moped licence, moped, card, car licence, full-time job). The other 17 slots are drawn evenly from the rest, so expected shared events = 8 + 17² / (N − 8):

  | Library N | Shared at least | Shared on average | Share |
  |---|---|---|---|
  | 30 | 20 | 21 | 85% |
  | 40 | 10 | 17 | 68% |
  | 50 | 0 | 15 | 60% |
  | 60 | 0 | 14 | 54% |
  | 80 | 0 | 12 | 48% |

  The two-thirds limit passes from about 42 events (8 + 17² / 34 ≈ 16.5 of 25). Flag gating raises overlap and different choices lower it, so the seeded check, not this table, is the real test.
- **Why:** The floor follows from the replay goal and the scheduler, not from a guess. The overlap check gives the team a number to watch while writing events.
- **Alternative:** 4 active months a year (20 regular choices, still inside "about 20-30") and a floor of 40. Expected overlap is 8 + 12² / 32 ≈ 12.5 of 20 (62%), which passes the same check.
- **Lands in:** PRD FR-17 (Size); FR-43 (Different choices); §7.1 cut item 3; brief Scope In #5 and the cut-list sentence; brief addendum "Event Library — Decision" and "MVP Scope Priority — Decision"; PRD addendum cut-order lines in "Credit card debt…" and "The ending in UJ-5"; memlog entry when decided.
- **Draft text:**

  FR-17, replace Size:
  > - **Size:** at least 50 regular events, twice the 25 regular active months in a playthrough (FR-17a), with a target of 60-80, plus about 10 crisis events. Every in-game year has at least 10 events whose age range covers it. Roughly 55% come before age 18 and 45% after. Unexpected expenses (FR-24) are a separate list and don't count.

  FR-43, replace the third consequence:
  > - **Different choices, different story:** two playthroughs with different choices give different stories. In the content check, pairs of seeded playthroughs with random choices share, on average, no more than two-thirds of their regular events.

  §7.1, item 3:
  > 3. Events, down to the minimum of 50
- **Conflicts:** Yes. Memlog 2026-11-03 (issue #19, "do not ask again"): "event library = fixed schema, min 30, target 60-80". Memlog corrections (#27) and the brief, brief addendum and PRD addendum cut lists say "events down to 30". Raising the floor changes that confirmed decision, and makes the cut-list item worth 10-30 events instead of 30-50.
- **Team decision:** Needed

---

### X4. Glossary and schema terms

- **Findings:** A35, S5
- **Problem:** FR-17's schema fields ("mechanism", "flags", "boomerang pair", "LK20 code", "teaching point") have no definition or type, so an automated check can't tell a real value from a meaningless one. D1-D6 and Norwegian terms like BSU and frikort are used undefined, and §3 comes after the journeys that use its terms.
- **Recommendation:**
  - Add glossary entries for the terms in the draft text below.
  - Add a field table to the PRD addendum and point to it from FR-17's Schema consequence.
  - Add a one-line pointer to §3 from §0 instead of moving the glossary.
  - LK20 codes use the codes valid from 1 August 2026, per the LK20 research. "None" is allowed, because no core aim names tax or BSU.
- **Why:** It makes the schema check meaningful with no new mechanism, and the same terms are used by X2, X6 and X11.
- **Lands in:** PRD §3 Glossary (new and changed rows); §0 (pointer); FR-17 Schema (pointer); PRD addendum (field table).
- **Draft text:**

  §0, add after the first paragraph:
  > Terms are defined in §3 Glossary.

  §3, new or changed rows (alphabetical placement as the team prefers):
  > | Boomerang pair | Two linked events. An option in the first, the opener, sets a flag. The second, the follow-up, needs that flag and comes a few months later with an echo badge (FR-17a, FR-37) |
  > | BSU | Boligsparing for ungdom: a savings account for a first home, with higher interest and a tax deduction (rule 9) |
  > | Content check | The automated check of the event library: the schema, the counts per in-game year and seeded test playthroughs (FR-17, FR-17a) |
  > | D1-D16 | The disclosed simplification texts in the brief's addendum (FR-40) |
  > | Event | A pre-written situation with a few options, taken from the event library. Crisis events are used only in crisis months, and the rest are regular events |
  > | Flag | A named yes/no marker in a playthrough, such as `owns_moped` or `has_card`. Options set or clear flags, and the engine sets flags for age unlocks and belongings. Flags decide which events can appear (FR-17a), what a choice opened or closed (FR-35) and what the room shows (FR-34). Flag names come from a fixed list |
  > | Frikort | A tax card that lets someone earn up to NOK 100,000 a year (2026) with no tax deducted |
  > | LK20 code | The code of the curriculum whose competence aim an event supports, such as MAT01-06 (maths after 10th grade) or SAF01-05 (social studies after 10th grade). The game uses codes valid from 1 August 2026 |
  > | Mechanism | The money mechanism an event or effect belongs to, from a fixed list: wages and hours, tax, saving and BSU, fixed costs, consumer loans, credit card, unexpected expenses, family help, and moped and licences. Disclosed simplifications are tied to mechanisms (FR-40) |
  > | Milestone event | An event tied to an age unlock (FR-18), such as the credit card offer at 18. Every playthrough gets it once the player qualifies |
  > | Teaching point | One sentence saying what an event teaches |
  > | Trygdeavgift | The national insurance contribution on wages (rule 3) |
  > | Virke/HK | The retail collective agreement whose minimum hourly rates the game uses (D2) |

  FR-17, Schema, add at the end:
  > The fields and what the check enforces are listed in the addendum.

  PRD addendum, new section "Event schema":
  > | Field | Content | Checked |
  > |---|---|---|
  > | id, version | Unique text id, and a whole-number version (NFR-4) | Id unique; version rises on any change |
  > | mechanism | One or more from the fixed list | Names exist |
  > | age range | From and to, in years and months, within 15y0m-19y11m | From ≤ to |
  > | requires flags, blocks flags | Lists of flag names | Names exist in the flag list |
  > | milestone | The unlock it belongs to (FR-18), or none | Unlock exists |
  > | boomerang | None, or a pair id and a role (opener or follow-up). The opener also has a delay range in months | Both halves exist; 2 ≤ min ≤ max ≤ 12; the follow-up requires a flag that an opener option sets |
  > | teaching point | One sentence | Not empty |
  > | LK20 code | One or more codes from the fixed list, or "none" | Codes exist |
  > | source | The parameter keys the event's figures use, or a citation for any other figure | Every amount traces to a parameter or a citation |
  > | options | 2-4 options, each with text, a money effect, a wellbeing effect, flags set or cleared, and optionally a tip and an ending text (X7) | Every option has a wellbeing effect (FR-13) |
- **Conflicts:** None.
- **Team decision:** Recommend accept

---

### X5. A playthrough keeps its content version

- **Findings:** A17
- **Problem:** Figures and events will be retuned during playtests, but nothing ties a running playthrough to the configuration and event versions it started with. A mid-playtest change would silently alter existing games, break FR-12's determinism and leave cause links pointing to changed events (F10).
- **Recommendation:**
  - Each playthrough stores the configuration version and event-library version it started with, and uses them until it ends. Changes apply only to playthroughs started afterwards.
  - Old versions are kept while any playthrough uses them, and cause links point to the event version the player saw.
  - Text-only fixes (no figure, option or flag changed) may apply to running playthroughs.
  - Engine code fixes apply to all playthroughs, and the worked examples guard them. Say this in the addendum.
- **Why:** Retuning is guaranteed during playtests. Pinning versions keeps each tester's game consistent with almost no extra logic.
- **Lands in:** PRD NFR-4 (new bullet); PRD addendum (text-fix exception, engine code note); architecture (how versions are stored).
- **Draft text:**

  NFR-4, add under **Figures:**
  > - **Versions:** each playthrough keeps the configuration and event-library version it started with until it ends. A changed figure or event applies only to playthroughs started afterwards, and cause links keep pointing to the event version the player saw. A correction to player-facing text that changes no figure, option or flag can apply to running playthroughs.

  Test: start a playthrough, change a parameter, play on, and the old value applies. A new playthrough uses the new value.
- **Conflicts:** None.
- **Team decision:** Recommend accept

---

### X6. Cause links with shares

- **Findings:** A18 (attribution part), E37
- **Problem:** FR-36 stores "the choice that caused it", but card interest, loan interest and savings interest come from balances built by several choices. Without a sharing rule, "Hvorfor?" and the ending's kroner ranking point to an arbitrary choice.
- **Recommendation:**
  - **Shares:** a cause link can list several causes, each with a whole-kroner share, and the shares add up to the effect.
  - **Interest on a balance:** interest on a card or loan is shared between the choices that make up the balance, and savings interest between the deposits, in proportion to each one's part at the start of the month. Payments and withdrawals reduce every part in proportion. Rounding uses largest remainder, with ties to the earliest cause.
  - **Continuing effects** link to the choice that started them: moped fuel and insurance link to buying it or taking the gift, a subscription fee to signing up.
  - **System causes:** wages, tax, the mobile cost and unexpected expenses keep a system cause, as FR-36 and FR-24 already say.
  - **Wellbeing:** a change links to the choice whose option set it, or to a rule (stress from a crisis month, free time from hours).
  - **"Hvorfor?":** lists the up to three largest shares and sums the rest as "annet" (addendum).

  Example: a card balance of NOK 6,000 is a city trip (NOK 4,000) and a jacket (NOK 2,000). The month's interest is 6,000 × 22.6% / 12 = NOK 113. The pro-rata shares are 75.33 and 37.67. The floors give 75 + 37 = 112, so the remaining krone goes to the largest remainder (jacket): trip NOK 75, jacket NOK 38.
- **Why:** Pro rata is the simplest rule that's fair, deterministic and sums exactly. UJ-3 already expects savings interest to link back to the deposit choice.
- **Alternative:** Link each shared effect only to the largest contributor. It's simpler to build, but misattributes when two purchases are close in size.
- **Lands in:** PRD FR-36 (new consequences); §3 Glossary, Cause link row; PRD addendum (method, rounding, example); architecture (per-cause parts of each balance).
- **Draft text:**

  FR-36, **Consequences (testable):**
  > - Every cause link points to a choice that exists in the playthrough, or to a rule (F10).
  > - **Shared causes:** an effect with several causes stores each one with its share in whole kroner, and the shares add up to the effect. Interest on a card or loan is shared between the choices that make up the balance, and savings interest between the deposits, in proportion to each one's part of the balance.
  > - **Effects that continue:** an effect that keeps following from an earlier choice links to that choice, such as the moped's fuel and insurance, a subscription's monthly fee, or interest on a purchase made on the card. Wages, tax, the mobile cost and unexpected expenses have a system cause.
  > - **Wellbeing:** a wellbeing change links to the choice whose option set it, or to a rule, such as stress from a crisis month.

  §3, Cause link row:
  > | Cause link | The record of which choices or rules caused an effect, with each one's share |
- **Conflicts:** None. Moped fuel and insurance stay transport costs (FR-23). They just carry a link to the moped choice instead of a system cause.
- **Team decision:** Recommend accept

---

### X7. Ending ranking, texts and the hollow-win choice

- **Findings:** A18, E38, E39, E41, P20
- **Problem:** FR-42's "ranked by their effect in kroner" has no definition, sign, tie-break or rule for fewer than three choices. Its "tip on how the problem could have been avoided" is wrong for a choice that helped. "At least one … is the choice that hurt wellbeing most" contradicts itself (P20) and has no answer when low wellbeing comes from system causes.
- **Recommendation:**
  - **Kroner effect:** the sum of the money effects linked to a choice over the playthrough (X6). Money in counts as plus and money out as minus. Moving money between own accounts, taking a loan and paying down debt count as zero, but the interest that follows counts. Belongings aren't valued; a sale counts when it happens.
  - **Ranking:** by size of effect, plus or minus. "Mattered most" means biggest either way. Ties go to the choice made first (month, then order within a crisis month). Choices with zero effect aren't ranked. Wages stay a system cause (X6), so the job choices never fill all three places.
  - **Fewer than three:** show the ones there are.
  - **Texts by sign:** a choice that cost money gets a tip on how the cost could have been avoided or made smaller. A choice that brought money gets a line on why it paid off. To keep authoring small, the texts are written per mechanism and sign (about 18 texts), and an option can override with its own ending text (schema field in X4).
  - **Hollow win:** "the choice that hurt wellbeing most" is the choice whose linked wellbeing changes add up to the largest drop in the goal-weighted score (FR-33, scale per the wellbeing proposal). If it isn't already in the top three, it takes third place. Only if no choice lowered wellbeing does that place show the largest system cause (crisis months, hours worked, debt stress) with a pre-written text. That keeps the 2026-11-05 decision that a hollow win shows a choice.
- **Why:** Absolute size is what "mattered most" means to a player, and sign-matched texts avoid telling someone how to avoid a good choice. Texts per mechanism keep the content load at about 20 texts instead of one per option.
- **Alternative:** Rank only by most negative effect. It matches UJ-5's "how the problem could have been avoided" wording, but a careful player then sees trivial costs as "what mattered most".
- **Lands in:** PRD FR-42 (rewritten consequences); UJ-5 step 4; PRD addendum (ending texts per mechanism and sign, system-cause texts).
- **Draft text:**

  > #### FR-42: Ending summary
  >
  > The ending shows how the life went and the three choices that mattered most, ranked by their effect in kroner. The player can open each of them to see the "if you had chosen differently" line (FR-39) and a short pre-written text about it. Realizes UJ-5.
  >
  > **Consequences (testable):**
  > - **Kroner effect:** a choice's effect is the sum of the money effects linked to it over the playthrough (FR-36), with money in as plus and money out as minus. Moving money between the player's own accounts, taking a loan and paying down debt count as zero, but the interest that follows counts.
  > - **Ranking:** choices are ranked by the size of their effect, plus or minus. Ties go to the choice made first. Choices with no kroner effect aren't ranked.
  > - **Fewer than three:** if fewer than three choices have a kroner effect, the summary shows the ones there are.
  > - **Texts:** a choice that cost money gets a tip on how the cost could have been avoided or made smaller. A choice that brought money gets a short line on why it paid off. The texts are general and pre-written (FR-19).
  > - **Hollow win:** one of the three is the choice that hurt wellbeing most, by its linked wellbeing changes (FR-36), even if it wouldn't make the top three by kroner. If it isn't already there, it takes third place. If no choice lowered wellbeing, that place shows the largest system cause instead, such as crisis months, explained from the rules.
  > - Only the choices shown can be opened.

  UJ-5, step 4:
  > 4. With each choice he gets a short, general, pre-written tip: how a costly choice could have been avoided, or why a good one paid off (FR-42).

  Test: a fixture playthrough with known linked effects gives a known top three, including a tie, a positive choice and fewer than three choices. A hollow-win fixture puts the wellbeing choice in third place.
- **Conflicts:** UJ-5 (confirmed 2026-11-04) step 4 says each choice comes with "advice on how the problem could have been avoided". This proposal changes that to sign-matched texts. It's consistent with the memlog decisions "top three choices by kroner effect" and "a hollow win shows at least one choice that hurt wellbeing".
- **Team decision:** Needed

---

### X8. "If you had chosen differently" on the ending screen

- **Findings:** A19, E40
- **Problem:** FR-39 allows the line only "where it can calculate the result reliably", yet FR-42 needs one for each of the top three choices. Those choices often changed later events, and re-simulating them would need the stored game states that were cut with crossroads replay.
- **Recommendation:**
  - **Reliable:** the line uses only the choice's own effect and the interest and instalment rules (rules 2, 4, 5). It never re-runs later months or events.
  - **Comparison:** the option in the same event whose direct kroner effect differs most from the chosen one. Ties go to the first listed. No authoring field is needed.
  - **Line types, in order:**
    1. **Debt cost:** if the choice put money on a card or loan, show the interest linked to it (X6). Example: a NOK 3,200 trip on the card, paid at the minimum, has NOK 406 in interest (worked example 4): «Byturen på kortet sto for 406 kr av rentene dine.»
    2. **Money kept:** if the direct effects differ, grow the difference with savings interest (2.87%, rule 2 rounding) from the month after the choice to month 60. Example: NOK 15,000 spent in month 1 instead of saved has 59 interest months, giving NOK 17,270: «Hadde du valgt å spare alt, ville du hatt 17 270 kr mer da du fylte 20.»
    3. **Fallback:** a pre-written text per mechanism, plus the difference in the two options' stated wellbeing effect where there is one. This covers the hollow-win wellbeing choice.
  - **No invented figures:** the game never shows a figure the engine didn't calculate.
  - **Disclosure:** the line's "everything else equal" assumption gets its own text (D15 in X11).
- **Why:** Every top-three choice gets a line, every figure is exact under a stated assumption, and nothing needs earlier states. Ranking only "calculable" choices (E40's first option) would bias what "mattered most" means.
- **Alternative:** Re-run the playthrough from month 1 with the one choice swapped and the same seed. It's possible with X1, but later events diverge, and the result is hard to explain or test.
- **Lands in:** PRD FR-39 (rewritten); §3 Glossary, "If you had chosen differently" row; PRD addendum (method and examples); brief addendum D15 (X11).
- **Draft text:**

  > #### FR-39: "If you had chosen differently"
  >
  > The engine calculates what another choice would have led to. It does so only where it can calculate the result reliably, from the choice's own effect and the rules for interest and instalments, and never with AI. Realizes UJ-5.
  >
  > **Consequences (testable):**
  > - **The comparison:** the line compares the chosen option with the option in the same event whose direct kroner effect differs most from it. Ties go to the option listed first.
  > - **Debt cost:** if the choice put money on a card or a loan, the line shows the interest linked to it (FR-36). For example: «Byturen på kortet sto for 406 kr av rentene dine.»
  > - **Money kept:** otherwise, if the two options' direct effects differ, the line shows the difference grown with savings interest (rule 2) from the month after the choice to the 20th birthday. Spending NOK 15,000 of the pengegave in month 1 instead of saving it gives «Hadde du valgt å spare alt, ville du hatt 17 270 kr mer da du fylte 20.»
  > - **No figure to show:** if neither applies, the line is a pre-written text, plus the difference in the two options' stated wellbeing effect where there is one. The game never shows a figure the engine didn't calculate.
  > - **No re-runs:** a line never re-runs later months or events, so no earlier game states need to be stored.
  > - **Where:** the lines for the choices on the ending screen stay in the MVP. The lines during play are first on the cut list.

  §3, row:
  > | "If you had chosen differently" line | An engine-calculated line comparing a choice with another option in the same event (FR-39) |
- **Conflicts:** None. The decision that the ending-screen lines stay and the in-play lines are cut first (memlog 2026-11-04) is kept.
- **Team decision:** Recommend accept

---

### X9. One life at a time, starting over, and coming back after the ending

- **Findings:** A3, E42, E43
- **Problem:** FR-9 ("only when starting again") hints that a player can restart mid-game, but FR-43 only covers play again after the ending. Nothing limits an account to one active life, says what happens to old playthroughs, or says what a player sees on logging in after the ending. FR-16's recap expects a next choice that doesn't exist.
- **Recommendation:**
  - **One life at a time:** one playthrough in progress per account.
  - **Starting over before 20:** allowed from the menu after confirming. The ended life can't be resumed and is deleted.
  - **After the ending:** the finished playthrough is kept read-only until the player starts a new life or deletes the account, and then it's deleted. This is the minimum E42 needs and keeps minors' data small.
  - **Coming back after the ending:** login shows the ending summary again with **Play again**, not a recap.
  - **Rerolling:** a player can still reroll the pengegave, but it's harmless because every goal is reachable from NOK 10,000 (FR-9). Rerolling the car licence gift means replaying three in-game years.
- **Why:** Being stuck in a run you hate is the opposite of "feels like a game", and FR-9 already implies restarting. Deleting ended lives is the simplest privacy answer.
- **Alternative:** Play again only from the ending screen, with no starting over before 20. That's even simpler and enforces "live with your choices", but a player who wants a fresh start has to finish or delete the account.
- **Lands in:** PRD FR-43 (new consequences); FR-16 (new consequence); NFR-3 (one retention line); PRD addendum (retention rationale).
- **Draft text:**

  FR-43, add:
  > - **One life at a time:** an account has at most one playthrough in progress.
  > - **Starting over before 20:** the player can end the current life from the menu and start a new one, after confirming. The ended life can't be resumed and is deleted.
  > - **After the ending:** a finished playthrough is kept, read-only, until the player starts a new life or deletes the account. Then it's deleted.
  > - **Coming back after the ending:** a player whose life has ended sees the ending summary again, with **Play again**, instead of a recap.

  FR-16, add:
  > - The recap is for a life in progress. After the ending, the player sees the ending summary instead (FR-43).

  NFR-3, add under **How the data is handled:**
  > - Only the current playthrough, or the last finished one, is kept (FR-43).
- **Conflicts:** None with the memlog: "replay from age 15, no replay from a crossroads" and "nothing carries over" both hold. The playtest completion metric (70%) may drop if testers start over, which is worth noting in 8.1.
- **Team decision:** Needed

---

### X10. Resuming the start

- **Findings:** E44
- **Problem:** If play stops after creating a user but before the goal, avatar or first choice, the landing state is undefined. The pengegave could be redrawn before the first choice.
- **Recommendation:**
  - **When the playthrough starts:** when the player confirms a life goal, which is also what "during a playthrough" means for FR-9. The pengegave is drawn and stored then (X1) and shown after the avatar step.
  - **Resuming:** on the next login, the player continues at the first step not yet done. Steps already done aren't asked again.
- **Why:** It's one rule, it fits the 2-minute target and it closes the pengegave reroll inside onboarding.
- **Lands in:** PRD FR-11 (new consequence).
- **Draft text:**

  FR-11, add:
  > - **Resuming the start:** the playthrough starts when the player confirms a life goal, and the pengegave is drawn then. If play stops before the first real choice, the next login continues at the first step not done yet, and steps already done aren't asked again.

  Test: create a user and close. Log in and land on the goal step. Choose a goal and close. Log in and land on the avatar step. Finish, see the amount and close. Log in and land on the first choice with the same amount.
- **Conflicts:** None.
- **Team decision:** Recommend accept

---

### X11. Disclosure texts D7-D16, seen once per account

- **Findings:** A32, E45
- **Problem:** FR-40 points only to D1-D6, so the PRD's newer simplifications have no player text, and FR-40's own test fails. These are 0% family loans, moped value and running costs, licences as payment, the fixed card limit, weekly hours, no studies, the frozen clock, the ending lines and wellbeing as numbers. Nothing says whether a seen text comes back in a new playthrough or on another device.
- **Recommendation:**
  - **New texts:** add D7-D16 to the brief addendum table, next to D1-D6, so "Om tallene" has one source. They follow the D1/D4 style: «Forenklet:», then what the game does and what real life does, in two or three short sentences.
  - **Triggers:** each text is tied to a mechanism (X4) or, for D14-D16, a feature.
  - **Grounding:** the facts come from the research. Moped prices come from FINN ads seen in autumn 2026, and insurance price factors from the moped price research. Licences need courses and tests (ung.no, Statens vegvesen), and the student loan is interest-free while studying full-time (Lånekassen). Card limits depend on income and debt (issuer terms in the youth-finance research).
  - **Seen once per account:** a disclosure is seen once per account and stored server-side, so it isn't repeated on another device or in a later playthrough. It stays behind its info icon and on "Om tallene".
  - **Dependencies:** D11 depends on the card proposal (A10/E54) and D12 on the hours proposal (A13); revise if those change the mechanics. The BSU deposit and withdrawal text comes with the BSU proposal (A16). The team should proofread the Norwegian.
- **Why:** Each text is cheap, keeps the game honest where it's least realistic, and closes FR-40's test. Seen-per-account avoids nagging on replays without hiding anything.
- **Lands in:** brief addendum "Simplifications the game discloses" (D7-D16); PRD FR-40 (changed text, new consequence); §3 Glossary, D1-D16 row (X4).
- **Draft text:**

  Brief addendum, add to the table:

  | # | Applies to | Shown first when | Text shown to the player |
  |---|---|---|---|
  | D7 | Family help (FR-27) | Family first offers a loan | «Forenklet: Lån fra familien har ingen rente i spillet, og du betaler tilbake et fast beløp hver måned. I virkeligheten avtaler familier slike lån på mange måter. Spillet regner ikke med familielån når det sjekker om gjelden din er for stor, men du må betale dem tilbake likevel.» |
  | D8 | Moped and licences: resale value (FR-29) | The player first owns a moped | «Forenklet: Mopeden taper like stor del av verdien hvert år du eier den. I virkeligheten avhenger prisen av modell, stand og hvor mye den er kjørt. Prisene i spillet bygger på annonser på FINN høsten 2026.» |
  | D9 | Fixed costs: moped fuel and insurance (FR-23) | The first moped running cost | «Forenklet: Drivstoff og forsikring koster et fast beløp hver måned i spillet. I virkeligheten bruker du mer drivstoff jo mer du kjører, og prisen på forsikring avhenger blant annet av alderen din, hvor du bor og hvilken moped du har.» |
  | D10 | Moped and licences: licences (FR-28, FR-30) | The first licence offer | «Forenklet: I spillet har du lappen så snart du har betalt for den. I virkeligheten må du gjennom kurs og bestå prøver, og det tar tid. Prisen er et anslag, og trafikkskolene tar ulike priser.» |
  | D11 | Credit card: limit (FR-26) | The first card offer | «Forenklet: Kortet ditt har én fast kredittgrense i spillet. I virkeligheten setter banken grensen ut fra inntekten og gjelden din, og den kan endres senere.» |
  | D12 | Wages and hours (FR-20, rule 10) | The first job offer | «Forenklet: Du velger hvor mange timer du jobber i uka, og spillet gjør det om til lønn for hele måneden. Spillet følger arbeidstidsreglene for alderen din, men holder ikke oversikt over enkeltdager eller om du jobber kveld eller natt.» |
  | D13 | Wages and hours: full-time job, no studies (FR-20) | The full-time job offer | «Forenklet: I spillet kan du ikke begynne å studere etter videregående, så det finnes ikke studielån. I virkeligheten er studielån fra Lånekassen rentefritt så lenge du studerer på heltid, og det er noe helt annet enn kredittkortgjeld.» |
  | D14 | Feature: breaks and recap (FR-16) | The first recap | «Forenklet: Tiden i spillet går bare når du spiller. Mens du er borte, kommer det ingen renter, regninger eller hendelser, uansett hvor lenge du er borte.» |
  | D15 | Feature: "if you had chosen differently" (FR-39) | The first ending summary | «Forenklet: Når spillet viser hva som kunne skjedd hvis du hadde valgt annerledes, regner det bare på pengene i det ene valget, som om alt annet var likt, og som om pengene sto på sparekonto. I virkeligheten kunne et annet valg også ha endret det som skjedde senere.» |
  | D16 | Feature: wellbeing (FR-33) | The first wellbeing change | «Forenklet: Trivsel er mye mer enn tre tall. Spillet måler bare stress, fritid og sosialt liv, for å vise at et godt liv handler om mer enn penger.» |

  PRD FR-40, replace the description and consequences:
  > Where the game simplifies reality, it says so (D1-D16 in the brief's addendum). Each disclosure is shown the first time its mechanism or feature appears, behind an info icon or under "Hvorfor?". All the texts are also collected on one page, "Om tallene".
  >
  > **Consequences (testable):**
  > - Every mechanism or feature with a simplification shows its text the first time it appears.
  > - **Once per account:** a disclosure the player has seen isn't shown again on another device or in a later playthrough. It stays behind its info icon and on "Om tallene".
- **Conflicts:** None.
- **Team decision:** Recommend accept

---

### X12. Room layers

- **Findings:** E36
- **Problem:** FR-34's "a handful of states" doesn't say what the room shows when several belongings change at once, such as the moped sold and a new purchase in the same month. A set of whole-room states can't show every combination, and a room built from a history of changes can go stale.
- **Recommendation:**
  - **Layers:** a base room plus one layer per belonging, at most 6 in the MVP, each with up to 3 states (for example moped: none or owned). Any combination then shows correctly.
  - **From flags:** each layer follows the playthrough's flags (X4), not a history of changes, so the room is the same after a reload and on every device.
  - **Text equivalent:** each layer has one, which ties in with A40/NFR-2.
  - **Content:** which belongings get layers is UX and content (OQ-8).
- **Why:** Layers are the simplest way to make combinations correct by construction, and they fit the addendum's "one room with a handful of states" without more art.
- **Lands in:** PRD FR-34 (new consequences); §3 Glossary, Room row; OQ-8 (which belongings).
- **Draft text:**

  FR-34, add:
  > - **Layers:** the room is built from one layer per belonging, at most 6 in the MVP, each with a few states. It always shows the current state of every belonging, so several changes in one month all show.
  > - **From state:** each layer follows the playthrough's flags, so the room looks the same after a reload and on every device.
  > - Each layer has a text equivalent (NFR-2).

  §3, Room row:
  > | Room | The player's room. It's built from a handful of layers, one per belonging, that change with choices (FR-34) |
- **Conflicts:** None. The addendum decision "In, small: one room with a handful of states" (2026-11-03) is kept.
- **Team decision:** Recommend accept

---

### Dependencies on other areas

These proposals assume or feed decisions in other areas. They should be applied together.

- **Month 60 (A7, E8):** X2 keeps months 59-60 quiet and free of unexpected expenses by default. Align with whatever final window that fix chooses.
- **Crisis displacement (E7):** X2's collision order gives it a rule: crisis first, and a displaced milestone or follow-up takes the next active month.
- **Rule 1 order (E2):** rule 1 should name where an unexpected expense falls (X2 suggests right after fixed costs).
- **Unlock table and calendar (A14, A15):** X2's milestones use the unlock months from FR-18.
- **Wellbeing scale (A6, E35):** X7's hollow-win choice uses the goal-weighted score in whatever scale that proposal sets.
- **Card mechanics (A10, E54), hours (A13), BSU (A16):** these affect D11, D12 and a BSU disclosure text (X11).
- **Privacy retention (A26), accessibility (A40):** X9's retention line and X12's text equivalents should match those proposals.
- **Prose and structure (S9, S11):** X7's UJ-5 step 4 wording also covers S11's condensing of step 3-4.

## K. Account, security, connectivity, privacy, platform and other NFRs
Covers A20-A31, A39, A40 and E46-E53. Each finding was checked against `prd.md`, the PRD addendum, the brief addendum (Privacy decision, Login secret), the architecture document, the memlog and issues #24, #30 and #31. None of them is fully handled already. NFR-6 already allows a local replacement for reset email, so A25 is only partly open (see K4).

Facts about Supabase and free tiers below are from general knowledge, not from the project's research. They're marked "verify" and belong in the architecture, not the PRD. New NFR numbers (NFR-10, NFR-11) may need to be reconciled with other areas' proposals.

---

### K1. Sign-up: one address, one user, and a way back for the real owner
- **Findings:** A22, E46, E47, E48
- **Problem:** FR-1 refuses an address that already has a user, so sign-up shows whether an address is registered, while FR-2 and FR-3 hide that. With no email confirmation, someone can register a classmate's address. FR-1 doesn't say how the real owner gets it back, or how letter case and spaces are handled.
- **Recommendation:**
  1. Accept that sign-up shows an existing user. You can't hide it without an email confirmation step before play, and the team ruled that out. Instead, limit sign-up attempts from one network address to 60 an hour (configuration), so nobody can check addresses in bulk. A class of 30 signing up at once, with a retry each, fits (30 × 2 = 60).
  2. The "address in use" message points to **Log in** and the forgotten-password link, so the real owner has a way in.
  3. The real owner takes the account over with the mechanisms the game already has. They reset the password by email (FR-3), which logs the other person out (K3). Then they delete the account (FR-44) or play on. Nothing new is needed.
  4. Email addresses are trimmed and compared without regard to letter case at sign-up, login and reset. Dots and "+tags" are left as typed.
  5. No email is sent at sign-up, so the address stays "login and recovery only" (4.1) and costs no email quota.
  6. Accept that the double entry can't catch the same typo made twice. That player can still play, but can't reset the password. Record this as a known limit.
- **Why:** This keeps the memlog decision (no confirmation step before play) and the 2-minute first choice. The recovery path reuses FR-3 and FR-44.
- **Alternative:** Send a non-blocking email at sign-up ("A user was created with this address. Not you? Reset and delete it."). It costs email quota and widens what the address is used for.
- **Lands in:** PRD FR-1 (one changed and three new consequences). PRD addendum "Login with email: consequences for the build" (trade-off note, sign-up limit default, known typo limit). Architecture "Authentication" (where the normalization and the sign-up limit live; Supabase Auth may already lowercase addresses, verify). Issue #24 (add the trade-off to the privacy check).
- **Draft text:**

  FR-1, replace "An email address that already has a user cannot create another one." with:
  > - An email address that already has a user can't create another one. The game then says the address is in use and points to **Log in** and the forgotten-password link. This is the only place the game shows that an address has a user (see addendum).
  > - Email addresses are matched without regard to letter case or spaces before and after. " Markus@Eksempel.no" and "markus@eksempel.no" are the same user, when creating a user, logging in and resetting a password.
  > - Sign-up attempts from one network are limited (default 60 an hour, configuration), so addresses can't be checked in bulk. A school class can still sign up at the same time.
  > - If someone else created a user with your address, you can take it over. Reset the password by email (FR-3), which logs the other person out, then delete the account (FR-44) or keep playing.

  PRD addendum, new bullet under "Login with email":
  > - **Sign-up shows whether an address has a user.** Accepted: hiding it needs an email confirmation step before play, which the team ruled out on 2026-11-03. The sign-up limit stops bulk checks, and the owner can take back an address someone else registered by resetting the password and deleting the account. FR-2 and FR-3 still don't reveal it. The same typo made in both email fields isn't caught: the player can play, but can't reset the password. To be reviewed in the privacy check (#24).
- **Conflicts:** None. It keeps "no email confirmation step before play" (memlog 2026-11-03). FR-3's "same response either way" now protects only partly, and the addendum says so.
- **Team decision:** Recommend accept.

### K2. Passwords and limits on attempts
- **Findings:** A23, E49, E50
- **Problem:** The PRD sets no password minimum and no limit on login guesses or reset emails, and FR-3's "expires" has no value. A script could guess short passwords on minors' accounts, or use up the free email quota and block recovery for everyone.
- **Recommendation:** All values are configuration, listed in the PRD addendum.
  - **Password:** at least 8 characters, with no rules about what it contains. At least 64 characters are allowed, and paste and password managers work. Checked in FR-1, FR-3 (new password) and FR-4.
  - **Login, per address:** after 10 failed attempts within 15 minutes, logins for that address pause for 15 minutes. The message stays the neutral one, including for addresses with no user.
  - **Login, per network:** up to 300 attempts an hour. A class of 30 at three attempts each (90) isn't blocked.
  - **Reset email:** at most 1 per address a minute and 5 a day. The daily total is capped at 80% of the email service's free daily quota [needs figure: depends on the service chosen under OQ-4]. The screen shows the same message whether an email was sent, held back by a limit, or the address has no user.
  - **Reset link:** expires after 60 minutes. Asking for a new link makes older links stop working. A used or expired link says so and offers a new one.
- **Why:** These are standard protections and cheap to set. Many are settings in the login service. The numbers are sized so a class on one school network isn't blocked.
- **Alternative:** A 12-15-character minimum, as recent guidance suggests for password-only login. It makes sign-up slower for a 15-year-old.
- **Lands in:** PRD FR-1, FR-2, FR-3 and FR-4 (consequences). PRD addendum (defaults table). Architecture (which limits the login service gives out of the box, and which need the backend. Counting failures per address and linking the email cap to the relay's quota probably need the backend; verify).
- **Draft text:**

  FR-1, add:
  > - The password must have at least 8 characters (configuration). There are no other rules for what it contains, and paste and password managers work.

  FR-2, add:
  > - After repeated failed logins for one address (default 10 in 15 minutes), logins for that address pause for a while (default 15 minutes). The message still doesn't reveal whether the address has a user. A school class logging in on one network isn't blocked.

  FR-3, replace "The reset link can be used once and expires." with:
  > - The reset link can be used once and expires after 60 minutes (configuration). Asking for a new link makes earlier links stop working. A used or expired link says so and offers a new one.
  > - Reset emails are limited per address (default 1 a minute and 5 a day) and in total per day, below the email service's free quota. The screen shows the same message whether an email was sent, held back by a limit, or the address has no user.

  FR-4, add:
  > - The new password has the same minimum length as in FR-1.
- **Conflicts:** None. "Password reuse is not addressed for now" (memlog 2026-11-03) stands, because there's no check against leaked passwords.
- **Team decision:** Recommend accept.

### K3. Sessions: ending other logins, logging out everywhere, and shared school PCs
- **Findings:** A24, E51 (and OQ-5, #31)
- **Problem:** Changing or resetting the password, or deleting the account, leaves other devices logged in. On a shared school PC, a classmate can keep making permanent choices in someone else's game, or keep writing to a deleted account.
- **Recommendation:**
  1. **Password change:** every other device is logged out, and this device stays logged in.
  2. **Reset:** every device that was logged in is logged out.
  3. **Deletion:** every device is logged out. A device that's still open can't save anything.
  4. **Log out on all devices:** this option sits next to **Log out** (FR-5).
  5. **When it takes effect:** "Logged out" applies at that device's next action. Its next choice is refused and it shows the login screen. Technical: the backend checks that the login is still valid on each request (architecture).
  6. **Shared school PCs (closes OQ-5 if accepted):** a "Stay logged in on this device" box at login, unticked by default.
     - Unticked: the login ends when the browser closes, or after 30 minutes with no activity.
     - Ticked: the login lasts until the player logs out, or until 30 days without play.
     - Both values are configuration.
- **Why:** Points 1-5 use features the login service already has (signing out other sessions). FR-4 and FR-44 already require the password for the worst actions. Point 6 is the smallest MVP answer to #31.
- **Alternative:** Do points 1-5 now and leave point 6 to the team later, as decided. A login then lasts indefinitely unless the player logs out.
- **Lands in:**
  - PRD FR-3, FR-4, FR-5 and FR-44 (consequences).
  - If point 6 is accepted: remove the school-PC note in 4.1 Notes, the 7.2 row and OQ-5.
  - Architecture (how a revoked login reaches the backend, and token lifetimes).
  - Issue #31.
- **Draft text:**

  FR-3, add:
  > - After a reset, every device that was logged in is logged out.

  FR-4, add:
  > - Every other device is logged out. The device where the password was changed stays logged in.

  FR-5, add:
  > - The player can also choose **Log out on all devices**, for example after forgetting to log out on a school PC.
  > - A device that was logged out from somewhere else can't make a choice. Its next action shows the login screen, and the game is unchanged.

  FR-44, add:
  > - Every device is logged out. A device that is still open can't save anything to the deleted account.

  FR-5, add only if point 6 is accepted:
  > - At login, the player chooses whether to stay logged in on this device. The box is unticked by default. Unticked, the login ends when the browser is closed or after 30 minutes with no activity. Ticked, it lasts until the player logs out or hasn't played for 30 days. Both times are configuration.
- **Conflicts:** Memlog 2026-11-03 (sync decision) left shared school PCs for the team to solve later, and PRD 7.2 marks it "later (#31)". Points 1-5 don't touch that. Point 6 brings it into the MVP and needs the team's yes.
- **Team decision:** Needed (point 6). Points 1-5: recommend accept.

### K4. Reset email at zero cost: OQ-4 blocks FR-3 and the playtest
- **Findings:** A25 (#30)
- **Problem:** OQ-4 is marked as not blocking. But FR-3 is in the MVP, NFR-5 requires zero cost, and the playtest runs on testers' own phones. NFR-6 already lets the README name a local replacement, so the examiner's run is partly covered. The playtest isn't covered: testers who can't reset their password distort the completion and return metrics.
- **Recommendation:**
  - OQ-4 blocks acceptance of FR-3 and the first playtest. The architecture decides it and tests it in the first build sprint.
  - **Examiner's local run:** reset emails go to a local mail inbox that comes with the local login stack. The README gives its address, so the examiner can open the reset link without the team's keys. The Supabase CLI includes such an inbox (Inbucket, or Mailpit in newer versions; verify).
  - **Hosted playtest:** use a free-tier email relay whose quota covers 10-20 testers plus the K2 limits [needs figure: quota of the chosen relay]. The hosted login service's built-in sender probably won't do: Supabase's default sender is reported to deliver only to the project team's own addresses, a few an hour (verify).
  - **Fallback if no free relay works:** a tester who asks in person gets a one-time reset link that the team creates with the login service's admin tools. This works for 10-20 testers the team knows, but not for go-live.
- **Why:** The local route costs almost nothing. The playtest route is the real risk, so it should be settled early.
- **Lands in:** PRD §9 OQ-4 (Blocks column), NFR-6 (name the local route at capability level), FR-3 (one consequence). PRD addendum "Login with email" (the three routes and the fallback). Architecture "Authentication" (chosen relay, its quota, the K2 caps). Issue #30.
- **Draft text:**

  OQ-4 row:
  > | OQ-4 | How password reset email works at zero cost in the examiner's local run, in the playtest environment and at go-live (#30) | Architecture, first build sprint | FR-3 acceptance and the first playtest |

  NFR-6, replace "Password reset works locally, or the README names a local replacement (#30)." with:
  > Password reset works locally. Reset emails land in a local inbox that comes with the local setup, and the README says where to open it (#30).

  FR-3, add:
  > - Reset works in the local run (NFR-6) and in the playtest environment (NFR-11).
- **Conflicts:** None. The architecture already says reset email "should be tried early in the build".
- **Team decision:** Recommend accept.

### K5. Choices on a patchy connection and on two devices (FR-6 to FR-8)
- **Findings:** A20, A21, E52, E53, and the "opens or returns" part of A30
- **Problem:**
  - FR-7's "saves when idle" implies the device holds progress the server doesn't have. That contradicts NFR-4 and FR-6.
  - Nothing says what happens to a choice sent just before the connection drops, or when two devices answer the same event.
  - "Opens or returns" isn't defined for a browser tab that stays open.
- **Recommendation:**
  - **FR-7, "nothing waits on the device":** the server decides and saves every change when it happens. Idle time becomes a reason to check for newer progress (FR-8), not to save.
  - **Confirmed choices:** a choice counts only once the server has confirmed it. Until then:
    - the chosen option shows that it's saving ("Lagrer …")
    - the other options are locked
    - no result is shown

    With no confirmation after 5 seconds (configuration), the game says it's still trying, and tries again when the connection is back. Trying again never applies a choice twice (NFR-7, FR-13).
  - **Lost confirmation:** if the server saved the choice, the game shows the saved result on reconnect. If the server never got it, the player sees the same event again. Random results are stored by the server, so choosing again gives the same outcome.
  - **Two devices:** each choice names the event it answers. The server accepts the first confirmed choice and refuses a later one for the same event. The losing device loads the latest progress, with a short message such as "Spillet ble oppdatert på en annen enhet". Both devices may be logged in at the same time.
  - **"Opens or returns" means any of these:**
    - the player opens or reloads the game, or logs in
    - the tab becomes visible again
    - the connection comes back
    - the game has been idle for 5 minutes (configuration)

    Each time, the game fetches the latest progress before it accepts the next choice.
  - **Offline:** the game says it's offline and what's on screen stays readable. Options are locked, and choices aren't queued for later, because only the server can decide a result (NFR-4).
- **Why:** With the server as the only source of truth, every case is deterministic and testable, and the device needs no sync logic.
- **Lands in:** PRD FR-6 (new consequences), FR-7 (rewritten), FR-8 (definition and consequences). OQ-8 keeps "idle time", now as the check interval. Architecture (state version per playthrough, request ID for retries, browser visibility and online events). Norwegian message wording goes to UX.
- **Draft text:**

  FR-6, add:
  > - A choice counts only when the server has confirmed it. Until then the game shows that it is saving, locks the other options and shows no result.
  > - If there's no confirmation within 5 seconds (configuration), the game says it is still trying and tries again when the connection is back. Trying again never applies a choice twice (NFR-7).
  > - If the connection drops after the server saved a choice, the game shows that choice's result when it reconnects. If the server never got the choice, the player sees the same event again.

  FR-7, replace the whole requirement:
  > #### FR-7: Nothing waits on the device
  >
  > Everything that changes the game is decided and saved by the server when it happens, so the device never holds progress the server doesn't have. Realizes UJ-1 and UJ-2.
  >
  > **Consequences (testable):**
  > - Closing the game at any moment, then logging in on another device, shows the same progress straight away. A choice the server never confirmed isn't there.
  > - The device keeps no progress of its own.
  > - When the game has been idle for a set time (default 5 minutes, configuration), it checks for newer progress as in FR-8.

  FR-8, replace the title, the description and the last two consequences:
  > #### FR-8: Check for updates on opening or returning
  >
  > Before it accepts the next choice, the game fetches the latest progress whenever the player opens or reloads it, logs in, comes back to the tab, gets the connection back, or has left it idle (FR-7). Realizes UJ-2.
  >
  > **Consequences (testable):**
  > - Progress made on the PC appears on the phone when the game is opened there.
  > - A device showing old progress can't overwrite a newer choice. If two devices answer the same event, the first choice the server confirms counts. The other device's choice is refused, and it loads the latest progress with a short message saying the game was updated on another device.
  > - With no connection, for example on the bus, the game says it is offline. What's on screen stays readable, but the options are locked until the connection is back. Choices aren't queued for later, and saved choices aren't affected.
- **Conflicts:** Memlog 2026-11-03 (sync, per user): "game saves to the cloud after idle time with the game open, and checks for updates when opened on a device (FR-7, FR-8)". K5 keeps the aim (another device is always up to date) and makes it stronger, but turns "save when idle" into "check when idle". The assumption "no new choices without a connection" (memlog, confirmed as A-12) is kept.
- **Team decision:** Needed, because it rewords a logged user decision.

### K6. Platform and supported browsers
- **Findings:** A30
- **Problem:** NFR-1 names screen sizes but not the platform or the browsers. The architecture says "web app" but the PRD doesn't, so "works on all four device classes" can't be tested.
- **Recommendation:**
  - LifeMode is a web app in the browser, with nothing to install.
  - It isn't a PWA in the MVP: no service worker and no offline mode. Offline play can't work, because the server decides every result (K5), and cached old versions would clash with the FR-8 check.
  - **Supported browsers:** the two newest major versions of Safari (iPhone, iPad, Mac), Chrome (Android, Windows, Mac, Chromebook), Edge and Firefox. Narrowest layout: 320 CSS pixels.
  - **Tested:** the main flow on Safari on an iPhone, Chrome on an Android phone, one tablet, and Chrome or Edge on a Windows laptop.
  - "Opens or returns" for a tab is defined in K5.
- **Why:** It matches the architecture. The list and the test devices make NFR-1 testable.
- **Alternative:** Add a web manifest so the player can put an icon on the home screen, without a service worker.
- **Lands in:** PRD NFR-1. Architecture "Mobile-First Requirements" (test matrix).
- **Draft text:**

  NFR-1, replace the title and opening sentence. The four bullets stay:
  > #### NFR-1: Platform and every screen size
  >
  > LifeMode is a web app that runs in the browser, with nothing to install. It isn't a PWA in the MVP and has no offline mode, because the server decides every result (FR-8). It is designed mobile-first, and its layout adapts to phone, tablet, laptop and desktop, down to 320 CSS pixels wide. It has:

  NFR-1, replace "The main flow works on all four device classes." with:
  > **Browsers:** the two newest major versions of Safari (iPhone, iPad, Mac), Chrome (Android, Windows, Mac, Chromebook), Edge and Firefox.
  >
  > **Tested:** the main flow, from creating a user to the ending, is tested on Safari on an iPhone, Chrome on an Android phone, a tablet, and Chrome or Edge on a Windows laptop.
- **Conflicts:** None. The memlog decision (mobile-first, adapts to all surfaces) is kept.
- **Team decision:** Recommend accept.

### K7. Responsiveness (new NFR-10)
- **Findings:** A29
- **Problem:** Every choice is a round trip to the server, but no NFR sets a response time. Lag would undercut "feels like a game" and the 2-minute first choice, with nothing to test against.
- **Recommendation:** Add NFR-10. Measure on a mid-range phone on a throttled 4G connection (a browser preset named in the architecture), against the playtest environment (K11):
  - **Choices:** the result shows within 1 s for 9 out of 10 choices, and within 3 s for all.
  - **Quiet months:** the summary shows within the same times.
  - **First visit:** the first screen is usable within 3 s.
  - **Cold start:** after the server has been asleep, a loading message shows within 1 s and the first screen within 10 s. Free hosts may sleep when idle (verify per host).
  - **Server budget (architecture):** one month processed and saved in at most 300 ms for 9 out of 10 requests, with the backend and database in the same region.
  - **How it's tested:**
    - a browser test with network throttling plays a scripted first session and records each choice's time to result
    - a Lighthouse mobile run checks the first screen before each playtest
    - the playtest server logs response times, with no personal data
- **Why:** These numbers fit a server round trip on 4G, and they give UX and the architecture a target.
- **Lands in:** PRD §5, new NFR-10. Architecture (server budget, same region, test setup).
- **Draft text:**
  > #### NFR-10: Responsiveness
  >
  > Every choice is a round trip to the server, so the game has to answer fast enough to feel like a game. Measured on a mid-range phone on a throttled 4G connection, against the playtest environment (NFR-11):
  > - After the player picks an option, the result shows within 1 second for 9 out of 10 choices, and within 3 seconds for all of them.
  > - A quiet-month summary shows within the same times.
  > - On a first visit, the first screen is usable within 3 seconds.
  > - If the server has been asleep, the game shows a loading message within 1 second, and the first screen is usable within 10 seconds.
  >
  > These are starting values, like the targets in 8.1. When the connection is lost, FR-6 and FR-8 apply instead.
- **Conflicts:** None.
- **Team decision:** Recommend accept.

### K8. NFR-7: a testable list of what the server refuses
- **Findings:** A31
- **Problem:** "Invalid financial values" and "attempts to get around the rules" can't be tested as written.
- **Recommendation:**
  - **One principle:** the device sends only which option the player picked, plus an amount where the option asks for one. The server works out everything else and ignores any other values. This removes most ways to edit a request.
  - **A closed list of refusals.** Each one leaves the game unchanged, returns the current progress, and shows a short plain-Norwegian message where the player could see it.
  - **Repeats:** a repeated request (same request ID) isn't an error. It applies once and returns the same result.
  - **Tests:** each case has one automated API test in CI (NFR-9).
  - **Caps from other proposals:** limits on cards, loans and BSU come from those FRs, so NFR-7 points to "the option's allowed range" instead of repeating numbers.
- **Why:** NFR-7 becomes a test checklist, and every case reuses a rule that's already stated.
- **Lands in:** PRD NFR-7 (replace). Architecture (error format, request ID, error codes).
- **Draft text:**
  > #### NFR-7: Robust against wrong input
  >
  > The server decides every result. The device sends only which option the player picked, plus an amount where the option asks for one, and the server ignores anything else. The server refuses:
  > - a choice for an event or month that isn't the current one
  > - an option that wasn't offered, or was shown as unavailable
  > - more working hours than rule 10 allows, including extra shifts
  > - a loan or credit card before the 18th birthday (rule 6), or a card with no wage income (FR-26)
  > - a card purchase above the card limit (FR-26)
  > - selling or using something the player doesn't have, such as a moped they don't own (FR-29)
  > - an amount that isn't in whole kroner, is zero or below, or is outside the option's allowed range
  > - a choice after the game has ended, or in a playthrough that no longer exists
  > - a request for another player's game (FR-2)
  > - a malformed request, such as a missing field or a value of the wrong type
  >
  > **Consequences (testable):**
  > - A refusal leaves the game unchanged, returns the current progress and, where the player could see it, shows a short message in plain Norwegian.
  > - A repeated request applies the action once and returns the same result as the first time.
  > - Each case in the list has its own automated test (NFR-9).
  > - Refusals are logged without the email address or the password.
- **Conflicts:** None.
- **Team decision:** Recommend accept.

### K9. Privacy measures in NFR-3: player information, deleting inactive accounts, and no age statement
- **Findings:** A26
- **Problem:** The brief addendum recommends a legal basis other than consent, short player information and deleting inactive games. None of these are requirements yet. The MVP could ship without them, and so could the playtest, which already handles real email addresses. Minors' addresses would be kept forever.
- **Recommendation:** Split the cheap build measures (MVP, from the first playtest) from the legal questions (#24, before go-live, still not blocking).
  - **MVP:**
    1. **Player information:** short text in plain Norwegian on the create-user screen, with a link to the full text, which can also be opened from inside the game. It covers what is stored (email, password as a hash, game data), what for (login, recovery, saving the game), how long, and how to delete it. It also says there's no marketing, no sharing and no AI, and who to contact.
    2. **Inactive accounts:** an account and its game data are deleted after 12 months without a login (configuration). That covers a whole school year and a summer, which is far longer than a 5-session playthrough needs. No warning email is sent, so the address stays login and recovery only (4.1).
    3. **No tracking:** no analytics, advertising or tracking cookies or scripts. Nothing is loaded from third parties apart from the login service, so fonts are served by the game itself. This can be tested in the browser's network log.
    4. **Logs:** the email address isn't written to the game's own logs. NFR-3 already says this for the password.
    5. **Playtest data:** deleted when the analysis is done (K10).
  - **Before go-live (#24, unchanged):** who the controller is (group or university), the legal basis and the full privacy text. The answers go into the PRD addendum when settled.
  - **Age statement:** don't add "I am 15 or older" in the MVP.
    - It stores and proves nothing.
    - The brief addendum advises against consent as the legal basis, so the consent age doesn't apply.
    - It would turn away 14-year-olds in 10th grade or teach them to tick it falsely. The brief addendum notes that some 10th graders are 14 for part of the school year.
    - The age for a child's own consent online is 13 today, with 15 proposed (brief addendum).
    - The player information says who the game is for (15-20). Revisit if #24 chooses consent.
- **Why:** These measures are cheap and testable, and the playtest already processes real addresses. The legal decisions stay with #24, as decided.
- **Alternative:** Add the "I am 15 or older" checkbox (not stored), as a visible signal that the game isn't for under-15s.
- **Lands in:** PRD NFR-3 (new bullets and a reworded last line). FR-1 (information shown before sign-up). Replace 4.1 Notes with a pointer to OQ-6 (see S6). OQ-6 (name the controller and legal basis). PRD addendum (retention values, contents of the player information). Architecture (scheduled deletion job, self-hosted fonts). Issue #24 (tick off the measures).
- **Draft text:**

  NFR-3, add under "How the data is handled":
  > - Before creating a user, the player sees short information in plain Norwegian: what is stored, what for, how long, and how to delete it. The full text can also be opened from inside the game.
  > - An account and its game data are deleted after 12 months without a login (configuration). The player information says so, and no email is sent about it.
  > - The game uses no analytics, advertising or tracking cookies or scripts, and loads nothing from third parties apart from the login service.
  > - Neither the email address nor the password is written to the game's own logs.

  NFR-3, replace "The privacy check before go-live is still open (#24)." with:
  > Who is responsible for the data, and on which legal basis, must be settled before go-live (OQ-6, #24). The brief addendum recommends a legal basis other than consent.

  FR-1, add:
  > - The player information (NFR-3) is shown on the create-user screen, before the user is created.
- **Conflicts:** Memlog 2026-11-03: "Open privacy questions do not block the MVP or the PRD and are to be checked before go-live (#24) … Recommendations in the addendum … are not team decisions." K9 makes three of the addendum's recommended measures MVP requirements (information, deleting inactive games, no tracking). It leaves the controller and legal basis to #24, and #24 still doesn't block anything.
- **Team decision:** Needed.

### K10. Playtest data: measuring without breaking anonymity, and recording the age limit
- **Findings:** A27
- **Problem:** Completion and return need game data per tester, but NFR-3 says results are anonymous and kept apart from accounts. The before-and-after quiz needs pairing. All testers are 18-20, so the results may not hold for 15-year-olds.
- **Recommendation:**
  - **Game metrics** come from the playtest environment's own records, counted per account: completion, coming back within a week, time to first choice and session length. Before export, each account is replaced by a random tester code, and no email addresses leave the system.
  - **Quiz and survey** use the tester code, never a name or email. The before and after quizzes are paired by code.
  - **Linking game data to survey answers (if wanted):** one team member keeps the code-to-account key apart from the results. It's deleted when the analysis is done, no later than the December delivery. Until then the results are pseudonymous, and after that anonymous.
  - **Playtest accounts** are deleted at the same time.
  - **Test period:** at least 7 days, so the return metric can be measured.
  - **8.1 records a validity limit:** the results show whether the game works for 18-20-year-olds, not for 15-17-year-olds. A test with younger players is a later step, with consent arranged as the privacy check (#24) requires.
- **Why:** This gets every 8.1 metric with no email address in the results, and keeps "playtests 18-20 only".
- **Lands in:** PRD 8.1 (measurement note and validity limit). NFR-3 (Playtests line). PRD addendum (playtest data plan). Issue #24 (the playtest information item).
- **Draft text:**

  8.1, replace "Completion is measured across several sittings during the test period, and the quiz before the first sitting and after the last one." with:
  > Completion, coming back within a week, time to the first choice and session length are counted from the game's own records for each playtest account, across several sittings. The test period lasts at least 7 days. The quiz is taken before the first sitting and after the last one. The quiz and the survey use a random tester code instead of a name or email address.
  >
  > **Validity limit:** all testers are 18-20, so the results show whether the game works for older players, not for 15-17-year-olds. A test with younger players is a later step.

  NFR-3, replace the Playtests line:
  > **Playtests:** only 18-20-year-olds take part, and they see the player information before they start. Game data is exported with a random tester code instead of the email address. If the team links game data to survey answers, the code key is kept apart from the results. The key and the playtest accounts are deleted when the analysis is done, no later than the December delivery.
- **Conflicts:** None. Playtests stay at 18-20 (memlog 2026-11-03).
- **Team decision:** Recommend accept.

### K11. A hosted environment for the playtest (new NFR-11)
- **Findings:** A28
- **Problem:** 8.1 needs 10-20 testers on their own phones for at least a week, but no NFR names a hosted environment, and the architecture says none is needed. Free tiers can pause idle projects or put servers to sleep, which would distort the return and pace metrics.
- **Recommendation:** Add NFR-11:
  - one hosted playtest environment over HTTPS, running the same version as the README's local setup, at zero cost
  - available for the whole test period (at least 7 days, K10)
  - player data stored in the EU/EEA
  - an automated daily check (scheduled CI job) logs in with a test user and loads the game, and alerts the team if it fails. Used only within the provider's terms, this also counts as activity against pause-when-idle rules.
  - password reset works there (K4), and playtest data is deleted after the analysis (K10)

  The architecture names the provider, the tier and the limits that matter: pausing or sleeping when idle, cold-start time, storage, monthly users and email quota [needs figure: from the provider pages once chosen]. Known risk to check: Supabase's hosted free tier pauses a project after a period without activity (verify the current rule).
- **Why:** The return and pace metrics need a stable environment that's always on. Naming the limits up front avoids surprises in test week.
- **Alternative:** Run the playtests in person on team devices only, and drop "comes back within a week" as a metric.
- **Lands in:** PRD §5, new NFR-11. Pointers in NFR-5 and 8.1. Architecture "Docker and Local Execution" (keep "no public production hosting" for go-live, but add the playtest environment).
- **Draft text:**
  > #### NFR-11: Playtest environment
  >
  > The playtests run on one hosted environment that testers open on their own phones.
  > - It runs the same version as the README's local setup, at no ongoing cost (NFR-5).
  > - It stays available for the whole test period, which lasts at least 7 days.
  > - Player data is stored in the EU/EEA.
  > - An automated check logs in with a test user every day of the test period and alerts the team if it fails.
  > - Password reset works there (FR-3, OQ-4).
  > - The architecture names the provider and tier, and the limits that matter for the test: pausing or sleeping when idle, storage, number of users and email quota.
- **Conflicts:** The architecture says "Public production hosting is not required for the MVP" and "no hosting provider needs to be selected at this stage". That's document text, not a memlog decision. K11 keeps it for go-live but requires an environment for the playtest.
- **Team decision:** Recommend accept.

### K12. §0: which document wins
- **Findings:** A39
- **Problem:** "Where an older document disagrees, the latest logged decision applies" lets any `.memlog.md` entry override the PRD without anyone seeing it, and the log's path isn't given.
- **Recommendation:**
  - This PRD, with Rule Set v1 for financial rules, is what downstream work uses.
  - The log records decisions and why. Within the log, a later entry still replaces an earlier one.
  - A decision that changes behaviour applies downstream only once it's written into the PRD or Rule Set v1.
  - Where the brief, the architecture or research disagrees with the PRD, the PRD applies. If the PRD and the log disagree, fix the PRD before downstream work relies on that part.
  - Give full paths.
- **Why:** Downstream agents and the examiner get one source to trust, without auditing the log.
- **Lands in:** PRD §0, second paragraph. S4 (status line) and S8 (move "Resolved" to the log) touch the same section.
- **Draft text:**

  §0, replace the second paragraph:
  > This PRD's own `addendum.md` holds detail that belongs downstream, along with the reasons behind several decisions. Every decision and change is logged in `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/.memlog.md`, where a later entry replaces an earlier one. A decision that changes behaviour applies downstream only once it's written into this PRD, or into Rule Set v1 for financial rules. Where the brief, the architecture or research disagrees with this PRD, this PRD applies. If this PRD and the log disagree, the PRD is fixed before downstream work relies on that part.
- **Conflicts:** None. The log's own rule (the latest entry wins inside the log) stays.
- **Team decision:** Recommend accept.

### K13. Accessibility: WCAG 2.2 AA, and text for everything shown as a picture
- **Findings:** A40
- **Problem:** "WCAG 2.x" can't be checked. Room states, echo badges, the moped and wellbeing have no text equivalents, so screen-reader users miss the core feedback on consequences.
- **Recommendation:** Use WCAG 2.2 level AA, with these game-specific musts:
  - Each room state has a text equivalent: what's in the room and what just changed.
  - Each echo badge has an accessible name that names the earlier choice, such as "Følge av valget ditt i måned 8".
  - Wellbeing and money changes also appear as text or numbers. Nothing is shown by colour alone: a money change has a sign and a word.
  - Status messages (saved, offline, card warning, start of a crisis month) are announced by screen readers without moving focus.
  - Touch targets are at least 24 × 24 CSS pixels (WCAG 2.2, 2.5.8). Option buttons should be 44 × 44.
  - Login works with password managers and paste (3.3.8).
  - The main flow can be played with a keyboard alone.
  - **Tests:**
    - an automated accessibility check (such as axe) on the main screens in CI, with no serious or critical findings
    - before each playtest, a keyboard-only run of the first session and a screen-reader run on a phone
- **Why:** 2.2 is the current W3C version and includes 2.1 AA. Norwegian universal-design rules point to 2.1 (not in the research; verify before citing). The game's core feedback is visual, so text equivalents matter most here.
- **Lands in:** PRD NFR-2, FR-34 and FR-37 (one consequence each). Architecture (accessibility check in CI). UX.
- **Draft text:**

  NFR-2, replace:
  > #### NFR-2: Accessibility
  >
  > The game meets WCAG 2.2 level AA. This includes contrast, keyboard navigation, text alternatives, form labels, clear error messages and touch targets of at least 24 × 24 CSS pixels.
  > - Everything the game shows as a picture also exists as text: each room state, the moped, each echo badge and the wellbeing parts.
  > - Nothing is shown by colour alone. A money change has a sign and a word, not only red or green.
  > - Messages such as "saved", "offline" and the card warning are read out by screen readers.
  > - Login works with password managers and paste.
  > - The main flow can be played with a keyboard alone.
  >
  > It's tested with an automated accessibility check on the main screens, with no serious or critical findings, and by hand before each playtest, with a keyboard alone and with a screen reader on a phone.

  FR-34, add:
  > - Each room state has a short text that says what's in the room and what just changed.

  FR-37, add:
  > - An echo badge has a text that names the earlier choice, so a screen reader reads it out.
- **Conflicts:** Memlog: "Accessibility: follow WCAG 2.x level AA". K13 picks a version within that decision. One possible issue to check: FR-1's double email entry (accepted 2026-11-03) against WCAG 2.2 criterion 3.3.7 Redundant Entry. Whether a confirmation field falls under its exceptions isn't settled here.
- **Team decision:** Recommend accept.

## E. Editorial: structure and prose
Editorial findings don't change what the product does. Per the PRD workflow, polish goes last so it doesn't redo work: apply the behavioural fixes above first, then these. S2 and S5 are handled in X (event library, glossary), and P20 is handled in the FR-42 text in X.

### E1. Move the Assumptions Index out of the PRD
- **Findings:** S1
- **Problem:** §10 is 491 words of confirmed assumptions that repeat FR consequences. Its only open item (#39) is hidden in the intro.
- **Recommendation:** Move the A-1 to A-28 table to the PRD addendum under "Confirmed assumptions (2026-11-05)". In the PRD, replace §10 with one line: "Confirmed assumptions A-1 to A-28 are kept in `addendum.md`." Move "other course requirements are still to be checked (#39)" into §9 as a new open question.
- **Why:** Keeping the table in the addendum preserves the visible record the examiner may value, while the PRD loses about 465 words.
- **Alternative:** Cut the table and rely on `.memlog.md` only.
- **Lands in:** PRD §10, §9; PRD addendum.
- **Conflicts:** None.
- **Team decision:** Recommend accept.

### E2. Put scope before the features, and merge Non-Goals into it
- **Findings:** S3, S13
- **Problem:** Scope and the cut order come after ~5,000 words of FRs, and §6 and §7.2 partly repeat each other.
- **Recommendation:** Move §7 MVP Scope to just before §4 and fold §6 into it as a short "Never in version one" list next to the "Later" table. Drop the duplicate "Interest or events during a long break" row. Renumber sections.
- **Why:** UX, architecture and epics need the scope and cut order first. One list tells "never" from "not yet".
- **Alternative:** Keep the order and condense §7.1 to "Everything in §4 is in scope".
- **Lands in:** PRD §4-§7.
- **Conflicts:** None.
- **Team decision:** Recommend accept.

### E3. Add a status line to §0
- **Findings:** S4
- **Recommendation:** After the first paragraph of §0: "**Status:** draft, updated 2026-11-05. No AI in this version. Open questions that block work are marked in §9."
- **Lands in:** PRD §0.
- **Team decision:** Recommend accept.

### E4. One home for each open item and each rule
- **Findings:** S6, S8, S14, S15, S16, S17
- **Recommendation:**
  - The privacy check (#24) and shared school PCs (#31) live only in §9 (OQ-5, OQ-6). 4.1 Notes, the last line of NFR-3 and the §7.2 row become pointers, e.g. "(open: OQ-6)".
  - Move "Resolved on 2026-11-05" from §9 to `.memlog.md` (it's already logged and applied).
  - 4.1 Description: replace the data-minimization and hash sentences with "(see NFR-3)".
  - 4.5 Description: replace the figures sentences with "Figures follow NFR-4."
  - FR-23, FR-38 and FR-39: replace the cut-order claims with "(cut list, item N)". §7.1 is the only place that orders the cuts.
  - Move the §8.3 paragraph on worked examples and unit tests for the new rules to NFR-4, next to "The worked examples are the test answer key".
- **Lands in:** PRD 4.1, 4.5, FR-23, FR-38, FR-39, NFR-3, NFR-4, §7.2, §8.3, §9.
- **Team decision:** Recommend accept.

### E5. Remove decision history from the requirements
- **Findings:** S7, S9
- **Recommendation:** Cut the unused [ASSUMPTION] and [OPEN] tags from the §0 legend (keep [NOTE FOR PM] only if one remains). Cut the leftover history lines: FR-30 "The gift doesn't depend on tobacco or alcohol…", FR-27 "Family gifts stay in the MVP.", FR-36 "F10 is read as…" (the reading stays in §8.3), NFR-4 "The disclosed simplifications are a requirement, as a product choice." (FR-40 already says it), UJ-5 "as decided" and "A full-time job from about 19." (FR-20 keeps it; see G for the exact month).
- **Why:** These lines answer debates the reader never saw.
- **Lands in:** PRD §0, FR-27, FR-30, FR-36, NFR-4, UJ-5.
- **Team decision:** Recommend accept.

### E6. Let the journeys tell the story and point to the FRs
- **Findings:** S10, S11 (S12: the journeys and their figures are preserved)
- **Recommendation:** In UJ-4, keep Markus's own facts (his parents paid for his car licence, he has had a moped since 16) and replace the rule asides with FR pointers. The edge cases become: "**He ignores the warning:** the debt grows and can start a crisis month; a crisis still active at 20 is a loss (FR-32, FR-41). **Family help:** not always on offer, often partial, and family loans are interest-free (FR-27)." In UJ-5, steps 3-4 become: "He opens one of the three choices that mattered most to see how things could have gone, with a short tip (FR-42)."
- **Why:** The journeys stop being a second copy of FR-27, FR-29, FR-30, FR-32 and FR-42 to keep in sync.
- **Lands in:** PRD UJ-4, UJ-5. Apply after any UJ-4 number fix from M.
- **Conflicts:** None; the story itself doesn't change.
- **Team decision:** Recommend accept.

### E7. Keep technology choices as constraints, not requirements
- **Findings:** S18
- **Recommendation:** Supabase is a course requirement, so keep it, but in one place: NFR-6 says "The required database and login service (Supabase) runs self-hosted in the local run." NFR-3 keeps the requirement ("passwords are stored only as a hash") and drops "Supabase Auth stores…".
- **Lands in:** PRD NFR-3, NFR-6.
- **Team decision:** Recommend accept.

### E8. Outline and a time-model diagram
- **Findings:** S20, S21 (S19: the §4 order is preserved)
- **Recommendation:** Promote NFR-1 to NFR-9 from #### to ###. Add a small Mermaid diagram in §4.4: playthrough (60 months, 5 sessions) → session (one in-game year, 12 months, active and quiet) → month (the rule 1 order of steps, as fixed in M).
- **Lands in:** PRD §4.4, §5.
- **Team decision:** Recommend accept.

### E9. Prose fixes
- **Findings:** P1-P19, P21-P29 (P20 is in X)
- **Recommendation:** Accept all prose fixes as listed in the review report. The most important:
  - False friends: "sensor" becomes "examiner (sensor)" once, then "examiner" (P1); "tariff rate" becomes "collective-agreement rate" (P2).
  - "Session" only means one in-game year; real-world play is a "sitting" (P3).
  - Money wording: debt "accrues" interest (P4); the interest rate isn't "in kroner" (P5); "puts money ahead of everything else" (P6); "A NOK 3,200 balance, with only the minimum paid each month…" (P22); "a fixed 15% a year" and "% a year" on all rates (P21).
  - One gloss for scope: "the first version of LifeMode (version one, also called the MVP)" (P7).
  - "car licence", not "driving licence" (P15).
  - Serial comma throughout, per the Microsoft Writing Style Guide (P16).
  - Keep the PRD's voice: -ize spelling with "licence", "behaviour" and "instalment", contractions, and the Norwegian terms (pengegave, BSU, frikort, "Hvorfor?").
- **Lands in:** PRD, throughout.
- **Team decision:** Recommend accept.

## Coverage: every finding and its proposal

**Adversarial:** A1 → X2; A2 → X1; A3 → X9; A4 → G4; A5 → G4; A6 → G5, G6; A7 → M8; A8 → M6, M7; A9 → M3, M4; A10 → M1; A11 → M12, M13; A12 → M12, M5; A13 → G2; A14 → G1; A15 → G3; A16 → M11; A17 → X5; A18 → X6, X7; A19 → X8; A20 → K5; A21 → K5; A22 → K1; A23 → K2; A24 → K3; A25 → K4; A26 → K9; A27 → K10; A28 → K11; A29 → K7; A30 → K5, K6; A31 → K8; A32 → X11; A33 → G9, M14; A34 → X3; A35 → X4; A36 → M4; A37 → M2; A38 → G7; A39 → K12; A40 → K13

**Edge-case hunter:** E1 → G6; E2 → M1; E3 → M1; E4 → M2; E5 → M6; E6 → M6; E7 → M6; E8 → M8; E9 → M8; E10 → M6; E11 → M7; E12 → M4; E13 → M4; E14 → M9; E15 → G4; E16 → G4; E17 → G4; E18 → M3; E19 → M3; E20 → M11; E21 → G1; E22 → G2; E23 → M7; E24 → M10; E25 → M10; E26 → X1; E27 → X1; E28 → G7; E29 → G7; E30 → G7; E31 → X2; E32 → X2; E33 → G7; E34 → G8; E35 → G5; E36 → X12; E37 → X6; E38 → X7; E39 → X7; E40 → X8; E41 → X7; E42 → X9; E43 → X9; E44 → X10; E45 → X11; E46 → K1; E47 → K1; E48 → K1; E49 → K2; E50 → K2; E51 → K3; E52 → K5; E53 → K5; E54 → M1

**Structure:** S1 → E1; S2 → X2; S3 → E2; S4 → E3; S5 → X4; S6 → E4; S7 → E5; S8 → E4; S9 → E5; S10 → E6; S11 → E6; S12 → E6; S13 → E2; S14 → E4; S15 → E4; S16 → E4; S17 → E4; S18 → E7; S19 → E8; S20 → E8; S21 → E8

**Prose:** P1 → E9; P2 → E9; P3 → E9; P4 → E9; P5 → E9; P6 → E9; P7 → E9; P8 → E9; P9 → E9; P10 → E9; P11 → E9; P12 → E9; P13 → E9; P14 → E9; P15 → E9; P16 → E9; P17 → E9; P18 → E9; P19 → E9; P20 → E9, X7; P21 → E9; P22 → E9; P23 → E9; P24 → E9; P25 → E9; P26 → E9; P27 → E9; P28 → E9; P29 → E9

