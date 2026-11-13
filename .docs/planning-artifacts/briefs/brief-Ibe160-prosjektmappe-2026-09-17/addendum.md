---
title: LifeMode Addendum
related_brief: brief.md
updated: 2026-11-12
---

# Addendum: LifeMode

Supporting depth that informs the brief but belongs in later work (architecture, PRD) rather than the 1-2 page brief itself.

## Financial Engine — Rule Set v1

Added 2026-10-14 in response to teacher feedback: the engine must "always calculate correctly", so the rules it follows are written down here, together with worked examples that serve as the answer key for automated tests. The numbers are realistic Norwegian 2026 values from official sources where they exist. They are stored as configuration, not hard-coded, so they can be updated without changing the rules.

### Parameters

Status: **Sourced** has a source and date; **Assumption** is a reasoned estimate that still needs a source; **Tuning** is a game-design value set by playtesting (PRD OQ-8); **Partly sourced** mixes sourced values and estimates; **Missing** has no figure yet. Deadlines follow the tentative dates in PRD §4.4 and OQ-13 (updated 2026-11-13).

| Parameter | Value | Source | Status | Owner | Deadline |
|---|---|---|---|---|---|
| Savings account interest | 2.87% per year | SSB table 11018, households, non-fixed deposits, Aug 2026 | Sourced | — | — |
| BSU interest | 5.61% per year | SSB table 11018, households, Aug 2026 | Sourced | — | — |
| BSU deduction | 10% of the year's deposits, max deposit NOK 27,500 per year (max deduction NOK 2,750), max NOK 300,000 in total; the deduction can never exceed the year's tax and is not carried forward | Skatteetaten, satser BSU 2026 and BSU guidance (see research `domain-norwegian-youth-finance-rules-2026-10-27`) | Sourced | — | — |
| Consumer loan interest | 15% per year (fixed) | Finanstilsynet/Gjeldsregisteret, average nominal rate 14.8% (Q3 2023, latest official figure); 2026 market range about 10-22% nominal (research `prices-oq3-oq17-2026-11-12`, seen 2026-11-12) | Sourced | — | — |
| Credit card interest (when interest is paid) | 22.6% per year | SSB table 12844, households, 2026 Q2 | Sourced | — | — |
| Hourly wage, under 16 / under 18 / 18+ | NOK 136.41 / 139.40 / 195.04 | Virke/HK Landsoverenskomsten minimum rates from 1 April 2026 (18+ = wage step 1) | Sourced | — | — |
| Working-hour limits | Under 15 or in compulsory schooling (grunnskole): max 2 h per school day and 12 h per school week; 7 h per day and 35 h per week on days and weeks without school. Ages 15-18 after compulsory schooling: max 8 h per day and 40 h per week. 18+: ordinary working hours, 9 h per day and 40 h per week | Arbeidsmiljøloven §§ 10-4 and 11-2 (see research `domain-norwegian-youth-finance-rules-2026-10-27`) | Sourced | — | — |
| Tax-free card (frikort) limit | NOK 100,000 per calendar year; employers withhold 50% above it, but that is withholding, not final tax | Skatteetaten, frikort and forskuddsutskrivingen 2026 | Sourced | — | — |
| Tax 2026 | Trygdeavgift lower limit NOK 99,650; rate 7.6% (5.1% under 17), never more than 25% of income above the lower limit. Minstefradrag 46%, max NOK 95,700. Personfradrag NOK 114,540. Tax on ordinary income 22%. Trinnskatt step 1: 1.7% from NOK 226,100 | Skatteetaten, satser 2026 (see research `domain-norwegian-youth-finance-rules-2026-10-27`) | Sourced | — | — |
| Rent, 1-room flat (hybel) | NOK 8,770 per month (whole country) | SSB table 09895, 2025 (Bergen 7,510, Oslo 10,090) | Sourced | — | — |
| Youth public transport, 30 days | NOK 238 | Ruter, from August 2026 (state-subsidised until April 2027) | Sourced | — | — |
| Mobile subscription | NOK 299 per month | Youth plans NOK 229-449 a month; PlussMobil 25GB Ung NOK 299 (tek.no, talkmore.no, Nov 2026; research `prices-oq3-oq17-2026-11-12`) | Sourced | — | — |
| Example unexpected expense | NOK 2,500 (broken phone screen) | Independent repair of a recent iPhone NOK 1,800-2,390; Apple authorised repair of older models NOK 1,990-2,990 (Apple Norway, expert-zoom; research `prices-oq3-oq17-2026-11-12`, seen 2026-11-12) | Sourced | — | — |
| Moped licence, total | NOK 12,000 (range 8,000-15,000) | TeoriPortalen, 2026-05-01, and Testen.no, 2026-07-24; commercial estimates (see research `prices-moped-and-licences-2026-11-05`) | Sourced | — | — |
| Car licence (class B), total | NOK 32,500 (midpoint of 25,000-40,000) | Testen.no, 2026-07-24, commercial estimate | Sourced | — | — |
| Class B licence age | 18; practice driving from 16 after the basic traffic course | Statens vegvesen, seen 2026-11-12. From 26 Nov 2028, 17 with accompanied driving (not in force) | Sourced | — | — |
| New moped | NOK 29,000 | Dealer ads on FINN for 2026 models, seen 2026-11-05 | Sourced | — | — |
| Used moped, about 7-8 years old | NOK 11,645, including the NOK 645 transfer fee | Median of 31 FINN scooter ads, models 2018-2019, middle half NOK 8,145-17,645; transfer fee from Skatteetaten (research `prices-oq3-oq17-2026-11-12`, seen 2026-11-12) | Sourced | — | — |
| Moped insurance | NOK 3,000 per year | [ASSUMPTION] Within the published ranges for riders under 25 (delkasko about NOK 2,500-3,500; insurio.no, Førerkortet.no 2026-05-09); insurers publish no fixed price, so a real quote is still needed (#29, research `prices-oq3-oq17-2026-11-12`) | Assumption | Team | Feature freeze (about 26-27 Nov) |
| Moped service | NOK 2,900 a year, plus random repairs of NOK 500-3,000 | MC Service AS, 2026/27 season; repairs [ASSUMPTION] (research `prices-oq3-oq17-2026-11-12`). Not charged by rule 14 yet; whether to charge it is a tuning decision (OQ-8) | Assumption | Team | Feature freeze (about 26-27 Nov) |
| Petrol 95 | NOK 20.64 per litre | SSB table 09654, average January-September 2026 | Sourced | — | — |
| Policy rate (background only) | 4.5% | Norges Bank API, 13 Oct 2026 | Sourced | — | — |
| Goal target: save for something big | NOK 100,000 net savings | Game design, tuning (PRD OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Goal target: debt-free buffer | Available money of at least NOK 30,000 at the end of each of months 49-60, and no debt at 20 | Game design, tuning (PRD OQ-8); about 3 months of hybel rent | Tuning | Team | Playtest start (8 Dec) |
| Big experience price | NOK 60,000: eight weeks of Interrail through Europe | Interrail youth 2-month pass DKK 4,712, hostels about €35 a night, €40 a day otherwise; three other 8-week trips cost NOK 51,000-63,000, so the label can change without changing the price (research `prices-oq3-oq17-2026-11-12`, 2026-11-12) | Sourced | — | — |
| Spending level | Low 60%, normal 75% (default), high 95% of the wage after tax; social life −2 a month on low, +2 on high | Game design, tuning (PRD OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| First card limit | NOK 5,000-10,000, default NOK 10,000 | Game design, PRD FR-26 | Tuning | Team | Playtest start (8 Dec) |
| Crisis debt floor | NOK 5,000 | Game design; the bottom of the first-card limit range | Tuning | Team | Playtest start (8 Dec) |
| Crisis cooldown | 2 months | Game design, tuning | Tuning | Team | Playtest start (8 Dec) |
| Payment plan term | 12 months | Game design, tuning | Tuning | Team | Playtest start (8 Dec) |
| Wellbeing start values | Stress 20, social life 60 | Game design, tuning (PRD OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Wellbeing weights, calm/free time/social | Save for something big 40/30/30; debt-free with a buffer 50/25/25; big experience 30/30/40 | Game design, tuning (PRD OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Wellbeing threshold | 50 | Game design, tuning (PRD OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Moped depreciation and floor | 15% of the start value a year; floor 20% of the start value | [ASSUMPTION] Tuning values; research found no Norwegian resale figures (PRD OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Moped and car fuel use | Moped 3.0 l/100 km × 300 km a month in April-October = 9 l (NOK 186); car 6.0 l/100 km × 800 km a month = 48 l (NOK 991) | Fuel use: Spritmonitor owner logs, Statens vegvesen (2026-08-17). Distances: [ASSUMPTION] from TØI 2138/2026 and SSB tables 12577/12575 (2026-04-08) (research `prices-oq3-oq17-2026-11-12`) | Assumption | Team | Feature freeze (about 26-27 Nov) |
| Youth everyday spending | About NOK 7,800-8,300 a month for ages 15-19 (food, clothes, personal care, leisure and media incl. mobile, transport) | SIFO referansebudsjett 2026 (SIFO-rapport 9-2026, published 2026-05-18, February 2026 prices; research `prices-oq3-oq17-2026-11-12`). Used to check the spending levels, not charged as is | Sourced | — | — |
| Car licence gift chance | 50% | Game design, tuning (PRD OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Activity slots | The month's free time (rule 12) ÷ 20, rounded down, at least 1 and at most 4 | Game design, tuning (PRD FR-52, OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Activity effects | Each activity within ±10 on stress and on social life; all activities in a month together at most ±15 on each, counted in that month's wellbeing only | Game design, tuning (PRD FR-53, OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Activity prices | NOK 0-3,600 per activity; starting catalogue of 6 basic and 16 invitation activities | Catalogue with a price, source and date per activity in research `prices-oq3-oq17-2026-11-12`, `activities-spending.md` (seen 2026-11-12). Six prices are estimates marked est. (OQ-17) | Partly sourced | Team | Feature freeze (about 26-27 Nov) |
| Messages a month | At most 3 new, of which 0-2 invitations. Offers and the event copy don't count. An invitation repeats at most once per in-game year | Game design, tuning (PRD FR-55, OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Employer extra-shift offers | A drawn offer with a chance per in-game year [tuning value]; default +4 h a week for 3 months | Game design, tuning (PRD FR-47, FR-55, OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Gift moped offer | A drawn offer, at most once per playthrough, with a chance per in-game year [tuning value] | Game design, tuning (PRD FR-29, FR-55, OQ-8) | Tuning | Team | Playtest start (8 Dec) |
| Savings interest message | Once per playthrough, the first month the savings interest earned so far passes NOK 50 | Game design, tuning (PRD FR-55, UJ-3) | Tuning | Team | Playtest start (8 Dec) |

### Rules

1. **One round is one month.** Each month is processed in a fixed order: income → tax → fixed costs, everyday costs and spending → unexpected expense → loan instalments, the card bill and interest on debt → interest on savings → the month's event and the player's choices, ending with the planned activities (PRD FR-53) → wellbeing. The rule 8 check runs at the end of the month. Wages are paid only at the income step. Activities and the month plan never add hours or wages to the current month.
2. **Whole kroner.** All amounts are whole NOK. Monthly interest is `balance × annual rate / 12`, rounded to the nearest krone (0.5 rounds up).
3. **Tax.** Tax is calculated on the player's total wage income for the calendar year, using 2026 rates. Up to NOK 99,650 there is no tax. Above that, trygdeavgift applies: 7.6% of the whole income (5.1% under 17), but never more than 25% of the income above NOK 99,650. Income tax is 22% of ordinary income (income minus minstefradrag) above the personfradrag, plus trinnskatt step 1; higher trinnskatt steps are not modelled. Each month the tax step deducts the increase in the year's calculated tax. The 50% that employers withhold above the frikort limit is withholding, settled in the tax assessment, and is not modelled as tax in version one.
4. **Consumer loan.** An annuity loan: equal monthly payments `P × r / (1 − (1 + r)^−n)` with `r` = annual rate / 12, rounded to whole kroner. The final payment is adjusted so the balance ends at exactly zero. At 0% (family loans), each instalment is the amount divided by the number of months, rounded under rule 2, and the final instalment is the amount minus the others.
5. **Credit card.** Each month's debt step pays the card bill: the card balance at that point, including this month's card-payable costs. The engine pays the player's chosen amount (the whole balance, the minimum or a fixed amount), but never more than the current account and savings hold. If the whole balance is paid, no interest is charged. Otherwise interest is charged on the whole balance first, and then the payment is made. The minimum is the larger of 3.5% of the balance before the month's interest and NOK 300, or the whole balance after interest if that is smaller. Paying the minimum never counts as paying in full. Paying less than the minimum is a missed minimum, and it leaves an overdue amount: the minimum minus what was paid. Later payments cover the overdue amount first, and the player can also clear it with an extra payment, which lowers the balance at once and doesn't undo interest already charged. With the setting on the minimum, the payment is this month's minimum plus any overdue amount. A fixed amount is at least the minimum, in steps of NOK 100. A purchase that would take the balance above the limit is declined. Interest can take it above the limit.
6. **Credit only from 18.** Consumer loans and credit cards are available only from the player's 18th birthday, as in Norway, where minors cannot take on loans. Before 18 the player cannot borrow from a bank. Family loans (PRD FR-27) aren't bank credit and are possible from 15. A consumer loan can't be taken in months 59-60, so borrowing can't clear a trigger at the last check.
7. **Quiet months.** A month without a highlight event (a story event, the card warning, or a crisis) is still processed by rules 1-5. The player sees a short summary and any new messages, and can plan activities or continue at once. A playthrough from 15 to the 20th birthday (60 months) is tuned to about 20-30 real choices, counting options picked in events and crisis months. Activities, money actions, and offers taken aren't counted.
8. **Crisis months.** The engine, not the AI, checks these triggers at the end of every month: the current account is below NOK 0 (savings already used up); the credit card minimum payment has been missed two months in a row, and the overdue amount hasn't been paid; or debt is above the larger of 3 × the average monthly wage income and NOK 5,000. Debt means the card balance, consumer loans and payment plans, not counting family loans, minus a positive current account and the savings account (not BSU), never below 0. Wage income is hourly wages before tax over this month and the two before; months before the game started count as 0. Sales, gifts, the pengegave, family money, interest and loan payouts don't count. The NOK 5,000 floor is configuration. If a trigger is true and no cooldown is running, the next month is a crisis month. When that month opens, after rule 1 has run up to interest on savings, the triggers are checked again. If none is true, the crisis month is skipped: the month runs as usual with a short note, with no crisis stress and no cooldown. There is only one crisis month at a time, however many triggers are true, and its event follows the most urgent trigger: below zero, then missed minimum, then debt. A crisis month has up to 3 linked choices with realistic actions (sell something, take extra shifts, ask for a payment plan, stop the card, ask family, ignore it), and the engine calculates the effect of each. An option is shown only when it is possible, and an option whose effect would land after month 60 isn't shown; asking family and ignoring it are always offered. Money actions and open options can also be used in a crisis month. They use no choice. After each choice or action the triggers are checked again, and the crisis month ends as soon as none is true, when the player ignores it, or after the third choice. Money that a crisis choice or a money action brings in during a crisis month goes first to a negative current account, then to overdue card minimums, and the rest stays in the current account. The missed-minimum trigger counts as solved once the overdue minimums are paid, or the card balance moves into a payment plan. After a crisis month, no new one starts for two months (configuration), and the game shows any trigger that is true during the cooldown. In version one a crisis never ends the game: ignored debt keeps growing under rules 4-5 and starts new crisis months after each cooldown. The loss ending applies when a trigger that was true at the end of month 59 is still true at the end of month 60. Month 60 is then a crisis month, even during a cooldown, unless the check when it opens finds no trigger true. A trigger that first becomes true at the end of month 60 doesn't give a loss.
9. **BSU deduction.** The deduction is calculated once a year, when the player continues from December, so deposits made that month count. In month 60 this comes before the rule 13 check. It's paid into the current account and isn't wage income, so it isn't part of rule 16. It is the lower of 10% of the year's BSU deposits (deposits capped at NOK 27,500) and the year's calculated tax under rule 3. If the player pays no tax, the deduction is NOK 0, and unused deduction is lost. The game says so plainly ("BSU deduction: NOK 0, you have no tax to reduce") and shows that BSU still pays off through its higher interest (5.61% against 2.87% on an ordinary savings account). Deposits above the year's NOK 27,500 are not accepted. The player can only withdraw the whole BSU. The BSU then closes, and the deductions received so far are taken from the payout at once, outside rule 16.
10. **Working hours follow Norwegian law.** The engine never lets the player work more hours than arbeidsmiljøloven allows. The limit depends on whether the player is in compulsory schooling, not on age alone: a 15-year-old in 10th grade gets 12 h per school week, while a 16- or 17-year-old in upper secondary school gets 40 h per week. Summer jobs use the limits for weeks without school. Rules on night work (§ 11-3) are not modelled, because the game does not track time of day. In the game, the player sets weekly hours. Monthly hours are weekly hours × 52 / 12, and the monthly cap is the weekly cap × 52 / 12, rounded down. In grunnskole (months 1-18, rule 11) the cap is 12 h a week in every month, because no summer job is offered before 16. From month 19 it is 40 h a week, and summer-job hours in July count towards the same monthly cap of 173 h. A 40 h week is paid for 173 h a month, and the engine cuts a summer job to fit the cap at July's income step, using that month's hours, extra shifts included. If the cut would leave 0 h when the offer is made, no summer job is offered, and the game says why. Daily limits aren't modelled.
11. **Calendar.** The player is born in January. Game month 1 is January of the year the player turns 15, and month 60 is December of the year they turn 19. The game ends on the 20th birthday, after month 60. Game year k (months 12k − 11 to 12k) is one calendar year: the player is 14 + k all year, and it is the income year for rules 3 and 9. The school year runs from August to June, and July is the summer month. The player is in grunnskole in months 1-18 (10th grade from month 8), in upper secondary school in months 20-54, and out of school from month 55. Trygdeavgift is 5.1% in game years 1-2, the years before the calendar year the player turns 17.
12. **Wellbeing.** Stress, free time and social life are whole numbers from 0 to 100. Stress starts at 20 and social life at 60. Each month, free time = 100 − 2 × (school hours + weekly work hours − 30), within 0-100 and rounded under rule 2. School counts as 30 hours a week in school months (rule 11), and weekly work hours are the month's hours ÷ (52 / 12). Each event choice changes stress and social life by its own effect, at most 20 points either way. Last in the month, after the choice, these apply in this order. In a month with spending (rule 16), social life falls by 2 on the low level. On high it rises by 2, unless interest was charged on debt that month. If interest was charged on any debt, stress rises by 5. If free time is below 50, stress rises by 5, and social life falls by 5. If social life is then below 20, stress rises by 5. A postponed family-loan instalment raises stress by 5. Each of these rises stops at 50, and stress already above 50 stays where it is. In a crisis month, stress rises by 10, with no such stop. If none of these apply and stress is above 20, it falls by 5, but not below 20. An event's own effect doesn't count as one of these. Each part is then kept within 0-100. Activities applied this month (PRD FR-53) add their own effects on stress and social life after that, each within ±10, and together at most 15 points either way on each part. Each part stays within 0-100. These effects count only in this month's wellbeing. The stress and social life that carry over to the next month, and the rows above, don't include them, and activities never change free time. Wellbeing = w1 × (100 − stress) + w2 × free time + w3 × social life, using this month's parts including activity effects, rounded to a whole number (0.5 rounds up), with weights set by the life goal that add up to 100%. Ending wellbeing is the average wellbeing in months 19-60, rounded the same way.
13. **Life goals at 20.** The goal is checked once, after month 60 has been processed, including its choice. Debt is the card balance plus what's left of consumer loans, payment plans and family loans. Family loans count as debt here, although they don't count towards the 3× trigger in rule 8. Net savings = current account + savings account + BSU − debt. Available money = current account + savings account − debt. Belongings such as a moped don't count. Save for something big: net savings ≥ the target. Be debt-free with a buffer: debt is NOK 0 at 20, and available money ≥ the buffer target at the end of each of months 49-60. Afford a big experience: the experience was bought by the end of month 56, and available money ≥ NOK 0 at 20. The experience can only be paid for from the current and savings accounts. A goal measure equal to its target counts as reached.
14. **Moped.** The player owns at most one moped and needs the moped licence to own one. The start value is the price paid (new NOK 29,000, used NOK 11,645), or NOK 11,645 for a gift moped. Resale value = start value × (1 − 15% × months owned / 12), rounded to whole kroner, never below 20% of the start value. Months owned = the sale month − the month the player got the moped. In a month when the player owns a moped at the fixed-cost step, transport is moped insurance (NOK 250) and moped fuel, and the public transport ticket isn't charged. A moped got in month m is first charged in month m + 1, and a moped sold in month m is last charged in month m. If the engine draws that the parents pay part of the insurance, the player's NOK 250 falls by that share. The draw is made once, when the player gets the moped.
15. **Payment plan.** In a crisis month, the player can turn the card balance into a payment plan: an annuity loan under rule 4 at the card's interest rate, over 12 months. The card is blocked until the plan is paid, so card use is off and spending comes from the current account. Plan instalments are charged like consumer-loan instalments, and the plan can be paid off early with no fee. Only one plan can run at a time. The term is configuration.
16. **Spending level.** The player sets a spending level: low 60%, normal 75% or high 95%. The default is normal. Each month, after fixed and everyday costs have been charged, that share of the wage income after tax is spent, rounded under rule 2, so costs come on top of spending. Spending is never more than the current account holds at that point. It never draws on savings or takes the account below NOK 0. With no wage, nothing is spent. With card use on, card-payable costs go on the card first, and then spending goes on it as far as it fits under the limit. The rest comes from the current account, up to what it holds, and that isn't a declined purchase. A change applies from the next month. The shares are configuration.

Rent (NOK 8,770) stays in the parameter table for the later moving-out step; it is not used in version one.

### Worked examples (test answer key)

| # | Situation | Expected result |
|---|---|---|
| 1 | Summer job at 16: 120 hours × NOK 139.40 | NOK 16,728; no tax (under frikort limit) |
| 2 | NOK 10,000 in a savings account for 12 months at 2.87% | NOK 10,289 (NOK 289 interest) |
| 3 | Consumer loan of NOK 20,000 at 15% over 12 months | Monthly payment NOK 1,805, final payment NOK 1,808; total paid NOK 21,663 (NOK 1,663 interest) |
| 4 | The trip from the brief: NOK 3,200 on a credit card, paying only the minimum each month | Paid off after 13 months; total paid NOK 3,606 (NOK 406 interest) |
| 5 | An 18-year-old earns NOK 110,000 in one calendar year | NOK 2,588 tax, all of it trygdeavgift: the lower of 7.6% × 110,000 (NOK 8,360) and 25% × 10,350 (NOK 2,587.50, rounded up). Income tax is 0, because ordinary income (110,000 − 50,600 minstefradrag = 59,400) is below the personfradrag |
| 6 | A 17-year-old on frikort (no tax) keeps NOK 10,000 in a BSU for 12 months | BSU deduction NOK 0 (no tax to reduce). Balance NOK 10,576 (NOK 576 interest), against NOK 10,289 in an ordinary savings account (example 2) |
| 7 | Card warning. Setting: whole balance. Last month paid in full. Bill NOK 6,000; current account and savings hold NOK 4,000 | Pays NOK 4,000. Interest NOK 113. Balance NOK 2,113. Warning this month, reason "couldn't pay". At the minimum, the NOK 6,000 bill would take 26 months and NOK 1,599 in interest. Next month the account covers NOK 2,113: paid in full, no interest, no warning |
| 7b | Card warning, chosen. Setting: minimum. Bill NOK 3,000; account holds NOK 20,000 | Interest NOK 57, pays NOK 300, balance NOK 2,757. Warning, reason "chose to pay less", with an option to pay the whole balance. At the minimum: 12 months, NOK 357 |
| 8 | Family loan of NOK 5,000 over 6 months at 0% | NOK 833 five times and a final NOK 835. If the account can't cover month 3, that instalment moves to the end: 7 months, still NOK 5,000, never below NOK 0 |
| 9 | Debt trigger, age 19, wage NOK 8,452 in each of the last three months (limit NOK 25,356). The current account is NOK 0 unless stated | (a) Card NOK 9,000 + consumer loan NOK 17,000, no savings: NOK 26,000, crisis next month. (b) Same, but the NOK 17,000 is a family loan: NOK 9,000, no crisis. (c) As (a) with NOK 2,000 in savings: NOK 24,000, no crisis. (d) No wage for three months, card NOK 4,000: floor NOK 5,000, no crisis; card NOK 6,000: crisis. (e) A NOK 8,800 moped sale leaves the average unchanged. (f) As (a) with NOK 2,000 in the current account: NOK 24,000, no crisis |
| 10 | Crisis cadence, cooldown 2. The account is still below zero after each month's income, unless stated | Below zero at the end of month 40: crisis in month 41, ignored. Months 42-43: cooldown, crisis shown. Still below zero at the end of month 43: crisis in month 44. The first linked choice sells the moped, the account is back above 0, and the crisis ends after one choice. Debt passes the 3× line at the end of month 45: shown, but month 46 is still in the cooldown. Still true at the end of month 46: crisis in month 47. If the account is below zero at the end of month 50 and month 51's wage clears it: no crisis in month 51, only a note, no stress and no cooldown |
| 11 | Month 60 | Trigger true at the end of month 58: crisis in month 59. Still true at the end of month 59: month 60 is a crisis month despite the cooldown. Minimum missed in months 58 and 59 and paid in month 60: not a loss. A random expense first takes the account below 0 at the end of month 60: not a loss, and the summary names it |
| 12 | Payment plan for a NOK 10,000 card balance (rule 15) | 12 months at 22.6%: NOK 939 eleven times, a final NOK 935, NOK 11,264 in total (NOK 1,264 interest), against 51 months and NOK 5,508 at the minimum. The card is blocked until the plan is paid |
| 13 | Consumer loan cap. Average wage NOK 8,452, card balance NOK 4,000 | Maximum NOK 25,356 − 4,000 = NOK 21,356, rounded down to NOK 21,000. Example 3's NOK 20,000 fits. No wage in one of the last three months: no loan offered |
| 14 | BSU cap. NOK 20,000 deposited earlier in the calendar year, then a NOK 10,000 deposit | NOK 7,500 accepted; NOK 2,500 stays in the current account |
| 15 | Fixed costs before 18. No job, NOK 10,000 pengegave kept in savings | No mobile or transport costs before 18, so never below NOK 0 before 18. If NOK 537 a month were charged from 15, the account would go below 0 after about 19 months |

**16. Calendar and pay (rules 10-11)**

| Game year | Months | Age | School | Hourly rate | Trygdeavgift | Weekly cap |
|---|---|---|---|---|---|---|
| 1 | 1-12 | 15 | 9th grade (1-6), summer (7), 10th grade (8-12) | 136.41 | 5.1% | 12 h |
| 2 | 13-24 | 16 | 10th grade (13-18), summer (19), Vg1 (20-24) | 139.40 | 5.1% | 12 h to month 18, then 40 h |
| 3 | 25-36 | 17 | Vg1 (25-30), summer (31), Vg2 (32-36) | 139.40 | 7.6% | 40 h |
| 4 | 37-48 | 18 | Vg2 (37-42), summer (43), Vg3 (44-48) | 195.04 | 7.6% | 40 h |
| 5 | 49-60 | 19 | Vg3 (49-54), out of school (55-60) | 195.04 | 7.6% | 40 h |

The BSU deduction comes in months 12, 24, 36, 48 and 60. 10 h a week at 18: 10 × 52/12 × 195.04 = NOK 8,452 a month. Full-time, 37.5 h: NOK 31,694. A summer job in month 19 is 120 × 139.40 = NOK 16,728, as in worked example 1.

**17a. Wellbeing over UJ-4 (rule 12).** Markus, 18, in Vg2, works 10 h a week. He starts at stress 20, free time 80, social life 60, wellbeing 74. Weights 40/30/30. W is the month interest starts, month 41 (May), so W+2 is July with no school. This is a set test state, not a scheduled playthrough, so a test starts from it instead of playing from month 1. The cabin weekend and the party are set directly, because drawn events are random, and month 47 is quiet with the default active months (PRD addendum). In real play they would land in nearby active months, and the wellbeing in those rows would move by a few points. Markus plans no activities here (PRD FR-9). Social life starts at 60 here, which is on the low side for a player already on high. The kroner amounts are in the PRD addendum's UJ-4 trace, and example 23 continues the same run.

| Month | What happens | Hours | Spending | Stress | Free time | Social | Wellbeing |
|---|---|---|---|---|---|---|---|
| W | Card interest starts, and the warning shows. He stops the card, moves spending down and asks for 2 h more a week (social −5). High gives no +2, because interest was charged | 10 | High | 25 | 80 | 55 | 71 |
| W+1 | Interest. Extra shift starts | 12 | Normal | 30 | 76 | 55 | 67 |
| W+2 | July. Interest. He has said no to the summer job and turns down a cabin weekend (social −5) | 12 | Normal | 35 | 100 | 50 | 71 |
| W+3 | Interest | 12 | Normal | 40 | 76 | 50 | 62 |
| W+4 | Interest | 12 | Normal | 45 | 76 | 50 | 60 |
| W+5 | The card is paid in full, so no interest. He sets 20 h and low spending from next month | 12 | Normal | 40 | 76 | 50 | 62 |
| W+6 | He goes to a party (social +10), and low spending lowers social life by 2 | 20 | Low | 35 | 60 | 58 | 61 |
| W+7 to W+9 | No effect on wellbeing from events | 20 | Low | 30, 25, 20 | 60 | 56, 54, 52 | 63, 64, 66 |

For example, W+1: 0.4 × 70 + 0.3 × 76 + 0.3 × 55 = 67.3, which rounds to 67. Wellbeing never drops below 60, so a real win at 20 is still possible.

**17b. Ending wellbeing (months 19-60).** A careful player on normal spending takes the three summer jobs, works 10 h a week from month 20 to 54, then 37.5 h full-time: ending wellbeing is 75. A money chaser on low spending, with weights 40/30/30, works 12 h a week from month 4 to 18, 40 h from month 19 to 48, 10 h in months 49-54, and 37.5 h full-time after that. There's no summer job, because the 173 h cap leaves no room (rule 10). He has NOK 436,849 at 20. His ending wellbeing is 34, below the threshold of 50, so he gets a hollow win. It's 37 with goal 2's weights and 29 with goal 3's. Easing off earlier doesn't make up for it. With the same run and the summer jobs that fit under the cap, 40 h to month 36 gives NOK 349,232 and 39, and 40 h to month 24 gives NOK 280,578 and 43. The limit in free time sits between 25 h and 26 h a week beside school. With no job before month 19, the same hours from month 19 to 60, no full-time job, and summer jobs cut to the cap, normal spending gives NOK 190,387 and 68 at 25 h, and NOK 196,098 and 41 at 26 h. On low spending, 25 h gives NOK 305,678 and an average of 50.43, shown as 50, a real win close to the boundary of 49.5.

**18. Endings at 20 (rule 13, PRD FR-41)**

| # | State after month 60 | Ending |
|---|---|---|
| a | Current account −NOK 400 at the end of months 59 and 60 (rule 8 still true), net savings NOK 120,000, ending wellbeing 70 | Loss |
| b | Trigger true at the end of months 59 and 60, net savings NOK 30,000, ending wellbeing 30 | Loss |
| c | No condition, net savings NOK 100,000 (exactly the target), ending wellbeing 62 | Real win |
| d | No condition, net savings NOK 112,000, months 19-60 sum to 2,079 (average 49.5, shown as 50) | Real win (boundary) |
| e | As d, but the sum is 2,078 (average 49.48, shown as 49) | Hollow win |
| f | No condition, net savings NOK 99,999, ending wellbeing 80 | Goal not reached |
| g | No condition, and savings interest left out for simplicity. Without a loan, net savings would be NOK 95,625. With NOK 50,000 borrowed in month 58, the last month it's possible (rules 4 and 6, 12 months, instalment NOK 4,513): cash NOK 136,599, loan left NOK 42,175, net NOK 94,424 | Goal not reached either way |
| h | Debt-free goal: lowest available money in months 49-60 is NOK 40,000. At 20: family loan NOK 1,500 left, ending wellbeing 70 | Goal not reached. The player could have paid the loan off early (PRD FR-45) |
| i | Debt-free goal: lowest available money in months 49-60 is NOK 30,000 (exactly the target), no debt at 20, ending wellbeing 55 | Real win |
| i2 | Debt-free goal: NOK 150,000 and no debt at 20, but available money was NOK 29,999 at the end of month 49 | Goal not reached |
| j | Experience goal: bought in month 56. At 20: current and savings accounts NOK 3,000, card balance NOK 2,000, so available money is NOK 1,000. Ending wellbeing 66 | Real win |
| k | Experience goal: bought in month 56, ending wellbeing 29 (the money chaser in 17b, with goal 3's weights) | Hollow win |
| k2 | Experience goal: not bought, NOK 200,000 at 20, ending wellbeing 70 | Goal not reached |
| l | Loss check: account below 0 at the end of month 59, and a request for a consumer loan in month 60 | The loan is refused, so the trigger stays true: Loss |

**19. Moped resale and costs (rule 14)**

| Moped | Start value | Months owned | Resale value |
|---|---|---|---|
| Used, bought month 16, sold month 40 | 11,645 | 24 | 11,645 × 0.70 = 8,151.5, so NOK 8,152 |
| New, owned 24 months | 29,000 | 24 | 29,000 × 0.70 = NOK 20,300 |
| Gift, got month 13, sold month 40 | 11,645 | 27 | 11,645 × 0.6625 = 7,714.8125, so NOK 7,715 |
| Used, owned 7 months | 11,645 | 7 | 11,645 × 0.9125 = 10,626.0625, so NOK 10,626 |
| Floor check, rate tuned to 25%, 48 months | 11,645 | 48 | 0, so the floor of NOK 2,329 applies |

For the used moped, bought in month 16 and sold in month 40: insurance is charged in months 17-40, so 24 × NOK 250 = NOK 6,000. The player pays the public transport ticket in months 41-60, never together with the moped's costs. Before 18, the parents pay the ticket.

**20. Reference run for goal reachability (rule 13).** Start with a NOK 10,000 pengegave, moved to the savings account at the first choice, so it earns interest from month 2. Everything left in the current account is moved to savings at each month's choice step, so a month's wage earns interest from the next month. No job until the summer jobs: 120 h in months 19, 31 and 43. Part-time 10 h a week in months 20-54 and full-time 37.5 h in months 55-60. Normal spending (rule 16) all the way. Mobile and transport (NOK 537 a month) from month 37, under PRD FR-23. No moped, licence, card or loan. Net savings at 20: NOK 120,393, with no tax in years 1-3, NOK 6,295 in year 4 and NOK 25,298 in year 5. The balance is NOK 55,797 in month 42, NOK 72,206 in month 49, NOK 80,991 in month 54 and NOK 95,266 in month 56. The lowest balance is NOK 10,000. Ending wellbeing is 75. Goals 1 and 2 are reached. Goal 3 is reached too: the NOK 60,000 experience is bought in month 56, available money at 20 is NOK 59,817, and ending wellbeing with goal 3's weights is 73. With one NOK 2,500 unexpected expense each June, net savings are NOK 106,928, the lowest available money in months 49-60 is NOK 61,563, and both goals are still reached. Goal 3 is also still reached, with NOK 46,352 at 20. If the pengegave goes to savings but the wage always stays in the current account, net savings are NOK 116,184, or NOK 103,065 with the expenses, with savings covering any shortfall (PRD FR-45).

**21. Earlier play has to matter (rules 13 and 16).** The same jobs as in example 20, with no unexpected expenses unless stated.

| # | Run | Net savings at 20 | Goal 1 (NOK 100,000) |
|---|---|---|---|
| a | Careless: pengegave spent in month 1, high spending to month 54, low from month 55. Ending wellbeing 83 | NOK 71,584 | Missed |
| a2 | As a, with full-time at 40 h, paid for 173 h | NOK 74,985 | Missed |
| a3 | As a, low from month 53 | NOK 77,362 | Missed |
| a4 | As a, NOK 10,000 kept | NOK 83,094 | Missed |
| a5 | As a, low from month 49 | NOK 88,995 | Missed |
| b | High spending all the way, NOK 10,000 kept | NOK 25,029 | Missed |
| c | Low spending all the way, NOK 10,000 kept. Ending wellbeing 57, with social life at 0 from month 48 | NOK 193,674 | Reached |
| d | Summer jobs only before month 55, pengegave spent, low all the way | NOK 81,752 | Missed |
| e | No job at all before month 55, pengegave spent, normal to month 54, low after. Below NOK 0 from month 37 to 54, with crises not modelled | NOK 57,701 | Missed |
| f | As d, with a NOK 30,000 pengegave kept | NOK 116,297 | Reached: keeping a large pengegave counts as earlier care |

For goal 2, runs c and f reach the NOK 30,000 buffer, with a lowest available money in months 49-60 of NOK 113,050 and NOK 48,120. In the other runs it's at most NOK 19,456, so they miss. In month 56, runs a to a5 hold NOK 31,248-48,495, below the NOK 60,000 experience price, so they can't pay for goal 3 in time. The reference run holds NOK 95,266, or NOK 81,929 with expenses.

Switching level around big pay doesn't beat normal on money: low in months 19, 31, 43 and 55-60 and high otherwise gives NOK 109,705 and ending wellbeing 83, against NOK 120,393 and 75. Alternating month by month depends on where the big pay falls: low in odd months, which include the summer pay months and month 55, gives NOK 120,373 and 74, and high in odd months gives NOK 98,333 and 75, which misses goal 1. Moving to low from month 55 after a careful start gives NOK 145,280 and 74.

**22. Moped against the goal (rules 13, 14 and 16).** The reference run with the moped licence from month 20 (NOK 12,000) and a moped from month 32, each bought at the first choice step the player can pay for it, and sold in month 60. With the yearly expenses, the licence moves to month 21. Insurance is charged from the month after buying, and moped fuel has no figure yet, so it's left out.

| # | Run | Net savings at 20 | With NOK 2,500 a year | Goal 1 (NOK 100,000) |
|---|---|---|---|---|
| a | Used moped, bought in month 32, sold for NOK 7,569, 10 h, normal | NOK 100,949 | NOK 87,521 | Reached only with no expenses |
| b | Used moped, 14 h, normal | NOK 122,744 | NOK 109,322 | Reached |
| c | Used moped, 10 h, normal, low from month 49 | NOK 133,599 | NOK 120,174 | Reached |
| d | New moped, 10 h, normal. Bought in month 34 and sold for NOK 19,575, or with expenses in month 39 and sold for NOK 21,388 | NOK 95,079 | NOK 84,396 | Missed |
| e | New moped, 10 h, normal, low from month 49, bought as in d | NOK 127,729 | NOK 117,050 | Reached |

The paid car licence (NOK 32,500 in month 40) on the reference run gives NOK 86,299, so it has to be made up elsewhere too.

**23. Markus in UJ-5.** Markus leaves UJ-4 in month 46 with NOK 122, the moped kept, and costs of NOK 549 a month. To reach goal 1 he works 20 h a week on low spending in months 47-54, then 37.5 h full-time on low: NOK 104,824 at 20, with moped fuel left out. On normal he ends at NOK 62,637, and with 10 h on low at NOK 85,297. Wellbeing in months 47-60 runs from 61 to 70, and social life ends at 32. If months 19-40 average 74, his ending wellbeing is about 70, a real win.

Examples 1-23 plan no activities, so their figures stand as before (PRD FR-9). Examples 24-26 were added on 2026-11-10 with the month plan (PRD FR-52, FR-53). On 2026-11-11, examples 25 and 26 were updated and examples 27 and 28 added, from the PRD review fixes. Activity prices and effects in them are placeholder values until PRD OQ-17 gives them a source.

**24. Activity slots (rule 12, PRD FR-52).** Slots = free time ÷ 20, rounded down, at least 1 and at most 4.

| Situation | Free time | Slots |
|---|---|---|
| School month, no job | 100 | 4 |
| School month, 10 h a week | 80 | 4 |
| School month, 12 h a week (grunnskole limit) | 76 | 3 |
| School month, 25 h a week | 50 | 2 |
| School month, 40 h a week | 20 | 1 |
| Out of school, full-time 37.5 h | 85 | 4 |
| July, 40 h a week (summer job and part-time at the 173 h cap) | 80 | 4 |
| UJ-6: school month, 10 h + 4 h extra shifts | 72 | 3 |

**25. Paying for activities (rule 1, PRD FR-53, FR-57, UJ-6).** Month 35 (November), age 17, 14 h a week (10 h plus 4 h of extra shifts), normal spending. Before the month: current account NOK 500, savings NOK 23,500, no debt. Parents pay mobile (under 18). Markus owns a moped, so transport is moped insurance (NOK 250), which is his own at any age (PRD FR-23). Moped fuel has no figure yet and is left out, as in example 22. Tax is NOK 0, because the year's wages stay under NOK 99,650. Planned: a concert (NOK 450), an evening with friends (NOK 200), and a rest night (NOK 0).

| Step | Amount | Current account |
|---|---|---|
| Income: 14 × 52 / 12 × 139.40 | +8,457 | 8,957 |
| Tax | 0 | 8,957 |
| Moped insurance | −250 | 8,707 |
| Spending, normal 75% | −6,343 | 2,364 |
| Interest on savings: 23,500 × 2.87% / 12 | +56 to savings (23,556) | 2,364 |
| Continue: concert, then friends, then rest | −650 | 1,714 |

The activities come after spending and aren't part of rule 16.

- **Extra shifts:** with 10 h a week the wage would be NOK 6,041, spending NOK 4,531, and the current account NOK 1,760 before the activities. The extra shifts therefore leave NOK 604 more this month after spending (PRD FR-47, FR-56).
- **Savings target:** the car licence (NOK 32,500) is pinned. Progress is the current account plus savings (PRD FR-57): NOK 24,000 before the month (73.8%) and NOK 2,364 + NOK 23,556 = NOK 25,920 when it opens (79.8%). In October his activities cost less than NOK 375, so progress was still under 75% when October opened. It passes 75% this month, so the bank's "three quarters" message arrives (PRD FR-55). After the activities it's NOK 25,270 (77.8%).
- **Activity spend:** the money view's activity spend for the year rises by NOK 650 (PRD FR-57).

*Variant b, an activity dropped:* the same month with no savings. After planning the concert and the evening with friends (NOK 650 of NOK 2,364), the player deposits NOK 2,000 in BSU, which leaves NOK 364. When they continue, the concert (NOK 450) can't be paid from the current account or savings, so it's dropped with a note and has no effect. The evening with friends is paid, which leaves NOK 164.

**26. Activities in wellbeing (rule 12).** The same month, November, with weights 40/30/30 (goal 1), at the start of the month stress 30 and social life 55. Free time is 100 − 2 × (30 + 14 − 30) = 72. Spending is normal, there's no debt, free time is above 50, and social life is above 20, so none of the rows applies, and stress falls by 5 to 25. Social life stays at 55. Those are the values that carry over to December.

| Case | Activities (stress, social) | Sum after the cap | This month's stress, social | Wellbeing |
|---|---|---|---|---|
| a | Concert (0, +8), friends (0, +5), rest (−5, 0) | −5, +13 | 20, 68 | 0.4 × 80 + 0.3 × 72 + 0.3 × 68 = 74 |
| b | Concert (0, +8), friends (0, +5), gaming with friends (−2, +4) | −2, +15 (17 capped) | 23, 70 | 0.4 × 77 + 0.3 × 72 + 0.3 × 70 = 73.4 → 73 |
| none | No activities | 0, 0 | 25, 55 | 0.4 × 75 + 0.3 × 72 + 0.3 × 55 = 68.1 → 68 |

In every case December starts from stress 25 and social life 55.

*Case c, the hollow win holds:* the money chaser in example 17b fills every slot every month with activities at the effect limits (stress −10, social +10 each, at most ±15 a month on each). Each activity can be planned only once a month, so the bound comes from the limits, not from one activity repeated. He has 1 slot at 40 h in school, and 3-4 when he works less. His ending wellbeing rises from 34 to 42 (goal 1 weights), from 37 to 46 (goal 2), and from 29 to 37 (goal 3), all below the threshold of 50. The careful player in 17b rises from 75 to 85 with goal 1's weights. If activity effects lasted into later months, social life would pile up, because nothing pulls it back down. One free activity a slot (stress −2, social +4) would then lift the money chaser to 65 and remove the hollow win, which is why effects count for their month only (PRD FR-33).

*Case d, the boundary moves:* in 17b's boundary runs on normal spending, with activities at the same limits in every slot, the 26 h run rises from 41 to 52, a real win, and the 25 h run from 68 to 79. A 26 h school month gives 2 slots, enough to reach the monthly cap. The threshold and the activity effects are therefore tuned together, and the content check reports these runs with the catalogue's best free activities (PRD FR-33, OQ-8).

**27. A card-paid activity (PRD FR-45, FR-26, FR-36).** Month 41, age 18, card use on, limit NOK 10,000, with the bill set to the whole balance.
- **a, it fits:** the card balance is NOK 0. A concert (NOK 450, card-payable) goes on the card when the player continues. Next month's debt step pays the NOK 450 bill in full, with no interest.
- **b, it doesn't fit:** the card balance is NOK 9,800, so the concert doesn't fit whole under the limit. It's paid from the current account, then savings, and is never split between the card and the accounts.
- **c, interest:** the card holds NOK 10,000, of which NOK 450 is the concert, and the bill is set to the minimum. Interest is 10,000 × 22.6% / 12 = 188. The concert's share is 188 × 450 / 10,000 = 8.46, so NOK 8 links to the concert, and the other choices on the card share the remaining NOK 180 (PRD FR-36).

**28. An activity group on the ending screen (PRD FR-39, FR-42).** Five concerts at NOK 450, paid from the current account in months 35, 39, 43, 47 and 51, with no card. Each payment is grown with savings interest under rule 2, from the month after it was paid to month 60: NOK 475, 471, 467, 463 and 459. The group's line is «Hadde du droppet konsertene, ville du hatt 2 335 kr mer da du fylte 20.» The group ranks in FR-42 by its summed kroner effect, −NOK 2,250, and the entry counts as made in month 35. The same method gives FR-39's pengegave example: NOK 15,000 from month 1 grows to NOK 17,270. The line also names the group's summed wellbeing effect, which depends on the activities' effects. Those are placeholders until PRD OQ-17, so no figure is fixed for it here.

Examples 7-21 were added on 2026-11-05 from the PRD review and the final check, and examples 22-23 from the independent review the same day. Examples 17, 20, 21, 22 and 23 were recalculated after the independent review with a script applying rules 1, 2, 3, 10, 12 and 16 month by month, with two accounts and purchases at the choice step. The review found that the earlier figures in 17b, 20 and 21d came from a script that broke the monthly cap in rule 10 and the interest order in rule 1. An independent recalculation from the rule text the same day found further errors in 17, 20, 21, 22 and the 40 h pay, and these figures have been corrected to match it.

Examples 2-4 and 6 were calculated with a script applying rules 2, 4 and 5 month by month, and examples 1 and 5 are direct arithmetic. All five were independently recomputed on 2026-10-22 and match. Example 5 was corrected on 2026-10-29 after domain research showed that the earlier 50% figure (NOK 5,000) was withholding, not final tax. Rules 9-10, the working-hour parameter and example 6 were added on 2026-10-31 (issue #16). Note that example 2 depends on rule 2 (rounding each month); a plain compound formula gives NOK 10,291.

### Simplifications the game discloses

The rule set is deliberately simpler than real life. To keep the game honest, the player is told where it simplifies. Each text is shown the first time the mechanism appears (as an info icon or under "Hvorfor?"), and all of them are collected on one "Om tallene" page. The texts are player-facing and therefore in Norwegian.

| # | Applies to | Text shown to the player |
|---|---|---|
| D1 | Tax (rule 3) | «Forenklet: Skatten regnes ut fra hele årsinntekten din med satsene for 2026. I virkeligheten kan arbeidsgiveren trekke 50 % av lønna til du har skattekort, eller når frikortet er brukt opp. Det som er trukket for mye, får du tilbake i skatteoppgjøret.» |
| D2 | Wages | «Timelønna i spillet er minstesatsen i tariffavtalen for varehandelen (Virke/HK) fra 1. april 2026. Norge har ingen lovbestemt minstelønn, så den ekte lønna di kan bli både høyere og lavere.» |
| D3 | BSU interest | «BSU-renta i spillet er gjennomsnittet for norske banker i august 2026 (SSB). Noen banker gir mer, og renta endrer seg over tid.» |
| D4 | Credit approval (rules 4-6) | «Forenklet: I spillet kan du få lån og kredittkort fra du fyller 18. I virkeligheten sjekker banken inntekt, gjeld og betalingsanmerkninger, og mange krever fast inntekt eller at du er eldre. Lån fra familien er ikke banklån, og de kan du få før du fyller 18.» |
| D5 | Consumer loan interest | «Lånerenta på 15 % er et anslag midt i markedet. Ekte forbrukslån koster ofte mellom 9 og 22 %, avhengig av bank og hvem du er.» |
| D6 | All rates | «Alle satser og beløp er 2026-tall. De holdes faste gjennom hele spillet, selv om spillet varer fra du er 15 til du er 20.» |

Added on 2026-10-31 (issue #16), based on the required disclosures in research `domain-norwegian-youth-finance-rules-2026-10-27`.

D7-D25 were added on 2026-11-05 from the PRD review. A disclosure is seen once per account (PRD FR-40). The team should proofread the Norwegian.

| # | Applies to | Shown first when | Text shown to the player |
|---|---|---|---|
| D7 | Family help (FR-27) | Family first offers a loan | «Forenklet: Lån fra familien har ingen rente i spillet, og du betaler tilbake et fast beløp hver måned. I virkeligheten avtaler familier slike lån på mange måter. Spillet regner ikke med familielån når det sjekker om gjelden din er for stor, men du må betale dem tilbake likevel.» |
| D8 | Moped: resale value (FR-29) | The player first owns a moped | «Forenklet: Mopeden taper 15 % av kjøpsprisen hvert år du eier den. I virkeligheten avhenger prisen av modell, stand og hvor mye den er kjørt. Prisene i spillet bygger på annonser på FINN høsten 2026.» |
| D9 | Fixed costs: moped fuel and insurance (FR-23) | The first moped running cost | «Forenklet: Drivstoff og forsikring koster et fast beløp hver måned i spillet. I virkeligheten bruker du mer drivstoff jo mer du kjører, og prisen på forsikring avhenger blant annet av alderen din, hvor du bor og hvilken moped du har.» |
| D10 | Licences (FR-28, FR-30) | The first licence offer | «Forenklet: I spillet betaler du for lappen og må klare et lite kjørespill. I virkeligheten må du gjennom kurs og bestå prøver, og det tar tid. Prisen er et anslag, og trafikkskolene tar ulike priser.» |
| D11 | Credit card: limit and fees (FR-26) | When the card opens (month 37) | «Forenklet: Kortet ditt har én fast kredittgrense i spillet, og du betaler ingen gebyrer, verken for å gå over grensen eller for å betale for sent. I virkeligheten setter banken grensen ut fra inntekten og gjelden din, den kan endres senere, og det koster ofte gebyr.» |
| D12 | Wages and hours (FR-20, FR-47, rule 10) | The first job offer | «Forenklet: Du velger hvor mange timer du jobber i uka, og spillet gjør det om til lønn for hele måneden, med 52 uker delt på 12 måneder. Skolen regnes som 30 timer i uka. Spillet følger arbeidstidsreglene for alderen din, men holder ikke oversikt over enkeltdager eller om du jobber kveld eller natt.» |
| D13 | Full-time job, no studies (FR-20) | The full-time job offer | «Forenklet: I spillet kan du ikke begynne å studere etter videregående, så det finnes ikke studielån. I virkeligheten er studielån fra Lånekassen rentefritt så lenge du studerer på heltid, og det er noe helt annet enn kredittkortgjeld.» |
| D14 | Feature: breaks and recap (FR-16) | The first recap | «Forenklet: Tiden i spillet går bare når du spiller. Mens du er borte, kommer det ingen renter, regninger eller hendelser, uansett hvor lenge du er borte.» |
| D15 | Feature: "if you had chosen differently" (FR-39) | The first ending summary | «Forenklet: Når spillet viser hva som kunne skjedd hvis du hadde valgt annerledes, regner det bare på pengene i det ene valget, som om alt annet var likt, og som om pengene sto på sparekonto. For en gruppe aktiviteter regner det på det de kostet til sammen. I virkeligheten kunne et annet valg også ha endret det som skjedde senere.» |
| D16 | Feature: wellbeing (FR-33) | The first wellbeing change | «Forenklet: Trivsel er mye mer enn tre tall. Spillet måler bare stress, fritid og sosialt liv, for å vise at et godt liv handler om mer enn penger. Tallet sier ikke noe om hvordan du har det i virkeligheten.» |
| D17 | Calendar (rule 11) | The first session | «Forenklet: I spillet har alle bursdag i januar. Skoleåret går fra august til juni, og juli er sommerferie.» |
| D18 | Accounts: savings cover the account (FR-45) | The first automatic transfer | «Forenklet: I spillet flytter vi penger fra sparekontoen automatisk når brukskontoen ikke har nok. I virkeligheten må du flytte pengene selv, ellers kan betalingen bli avvist.» |
| D19 | Accounts: negative balance (FR-45) | The first negative balance | «Forenklet: Går du i minus i spillet, betaler du ikke renter eller gebyrer, men det starter en krisemåned. I virkeligheten kan ubetalte regninger gi purregebyr og inkasso.» |
| D20 | Payment plan (rule 15) | The first payment plan offer | «Forenklet: I spillet blir en betalingsavtale et nedbetalingslån over 12 måneder med samme rente som kortet, og kortet sperres til lånet er betalt. I virkeligheten avtaler du vilkårene med banken.» |
| D21 | Consumer loan (FR-25) | The first loan offer | «Forenklet: I spillet koster det ingenting å betale ned lånet før tiden, og banken ser bare på lønna di de siste tre månedene.» |
| D22 | BSU withdrawal (FR-22) | The first BSU deposit | «Forenklet: I spillet kan du bare ta ut hele BSU-en, og da avsluttes den. Du betaler også tilbake skattefradraget du har fått. I virkeligheten skal BSU brukes til bolig, og bruker du pengene til noe annet, mister du fradraget.» |
| D23 | Fixed costs before 18 (FR-23) | The first month summary | «I spillet betaler foreldrene mobilen og bussen din til du fyller 18. Da overtar du regningene. Lommepenger er ikke med i denne versjonen.» |
| D24 | BSU: opening age (FR-18, FR-22) | The first time the player opens BSU in the money view | «Forenklet: I spillet kan du opprette BSU selv fra du er 15. I virkeligheten må en foresatt som regel være med, og Skatteetaten fraråder BSU før du er 17 hvis du ikke har skattepliktig arbeidsinntekt.» |
| D25 | Spending level (FR-23, rule 16) | The first wage | «Forenklet: I spillet velger du et forbruksnivå, og en fast del av lønna di går til forbruk hver måned. I virkeligheten går pengene til mange små kjøp, og det er lett å miste oversikten.» |
| D26 | Month plan and activities (FR-52, FR-53) | The first month plan | «Forenklet: En måned har noen få ledige plasser for fritid. Jo mer du jobber, jo færre blir de. Spillet følger ikke dager eller klokkeslett, og en aktivitet gjør bare den måneden bedre. Det sosiale livet ditt over tid følger valgene dine, forbruksnivået og hvor mye du jobber.» |

D26 was added on 2026-11-10 with the month plan.

## LLM-as-game-master products and pitfalls

- AI Dungeon (Latitude) is the reference case: state-of-the-art AI-GM systems split a deterministic backend (rules, causal/graph-based state) from the LLM (narration/dialogue only), because LLMs used directly as randomness sources produce numbers that look random but statistically aren't, and free-running LLMs will silently rewrite established rules/state. This validates LifeMode's planned separation of the deterministic financial engine from the AI narrative layer.
- Documented LLM-GM failure modes (per "Can LLM Agents Stick to the Script?" and RPGBENCH): hallucination/factual contradiction, "forcibly changing reality," ignoring player input, and a "helpfulness bias" — RLHF-tuned models tend to grant requests that should be impossible, eroding narrative friction/consequence.
- Content-safety precedent: AI Dungeon's 2021 controversy — a GPT-3 upgrade caused generation of sexual content involving minors; Latitude's fix (aggressive filtering + human moderators reading private stories) caused backlash over over-blocking and privacy (moderators reading unpublished/private content). Directly relevant since LifeMode's entire user base is minors (15-20) — both under- and over-moderation are live risks, and "humans reading kids' private sessions to tune the model" is a specific trust/privacy trap to avoid by design.
- Cost economics: rough industry figures put a single LLM dialogue exchange at $0.001-0.005; at meaningful DAU this compounds fast — an argument for keeping "expensive" LLM calls to narrative beats only, while the deterministic engine (cheap, code-based) does continuous math.
- Sources: shiftmag.dev; vice.com "Text Adventure Game Community In Chaos"; aiaaic.org (AI Dungeon incident record); futurism.com; arxiv.org RPGBENCH (2502.00595); arxiv.org "Can LLM Agents Stick to the Script?" (2608.08160); theneuralbase.com.

## AI Safety & Content Moderation — Design Principles

Raised during brief discovery because the entire user base is minors (15-20) and the closest structural comparable (AI Dungeon) has a well-documented 2021 safety incident. Not solved here — flagged for the architecture phase — but the team's working stance:

1. **Structured AI output, not free text.** The AI Game Master generates events/dilemmas in a structured format (type + parameters) validated against a schema before rendering — not unconstrained prose. Reduces surface area for unwanted content reaching the player.
2. **Constrained player input for negotiation, at least in MVP.** For the bank-negotiation mechanic, the player selects from predefined argument *types* (e.g. "cite steady income," "offer collateral," "show a repayment plan") rather than fully open free-text chat with the AI. Preserves the "argument quality affects outcome" mechanic while avoiding open-ended text exchange between a minor and an LLM. Can be opened up later once moderation is proven.
3. **Automatic moderation before display, not after.** Generated content is checked against a content filter before reaching the player; a failed check falls back to a neutral, pre-written event — never a blank screen, never unfiltered output.
4. **No human reading of private sessions.** Review happens on flagged/aggregate content, not by staff reading individual children's play sessions — the specific trust/privacy trap that compounded the AI Dungeon incident.
5. **Parent visibility as a sellable feature, not just compliance.** Family Premium (already in the business model) can include parent-facing visibility into event *categories* their teen encountered, not verbatim content.

**Technical/architecture-level follow-ups (deeper than brief scope):**
- Rate limiting and cost control per session (ties to the LLM unit-economics risk above).
- GDPR / Datatilsynet review of minors' data handling — aligns with the already-stated goal of collecting no real PII (simulated_age, simulated_savings, etc.).
- Review of Anthropic's usage policies for products directed at minors before scaling beyond MVP.

## Win Condition & Endgame — Decision

**Decided by the team (recorded 2026-11-03, issue #19): the second option below, a player-chosen life goal plus a wellbeing meter.** This is the MVP solution and can be revisited later.

- **Life goals:** the player picks one of three goals at the start, and all of them are checked at age 20:
  - save for something big (a savings target)
  - be debt-free with a buffer
  - afford a big experience, such as a trip
- **Wellbeing meter:** calculated from three parts, weighted differently depending on the chosen goal:
  - stress, from interest on debt, crisis months and working too much
  - free time, from hours of school and work
  - social life, from choices in events, the spending level and working too much, so each choice in the event library carries a wellbeing effect

  The formula is rule 12, and the goal formulas are rule 13.
- **Housing:** not part of the meter in version one, because moving out and rent are out of scope.
- **Four endings** (corrected 2026-11-03, boundaries set 2026-11-05), checked in this order when the game ends at age 20:
  1. **Loss:** the economy is critical, meaning a rule 8 trigger that was true at the end of month 59 is still true at the end of month 60. The consequences are shown clearly. The text also reflects wellbeing, for example "you had a good life, but the economy did not hold".
  2. **Real win:** goal reached and ending wellbeing at or above the threshold.
  3. **Hollow win:** goal reached, but ending wellbeing below the threshold.
  4. **Goal not reached:** neither a win nor a loss. Saving little or spending a lot is allowed. The player gets advice on modest savings goals and their benefits, and a reflection on the consequences of not saving.
- **Going below zero during the game:** this starts a crisis month with clear consequences, not a loss. Rule 8 still applies, so the player can recover before age 20.
- **Numbers:** target amounts, wellbeing weights and the threshold are configuration, with defaults in the parameter table, and are adjusted when the game is tuned.
- **No AI needed:** the engine calculates everything from measurable state, so all four endings work with no AI.

Why: it sets LifeMode apart from similar games such as Koll på cashen, and it shows that good money management is not just about earning as much as possible.

### Options considered

Kept as a record of the discussion. Where the text below differs from the decision above, the decision applies.

One option discussed: at the start of a playthrough, the player receives a mission to reach a target net worth by around age 20. The target is randomized/personalized per playthrough rather than fixed, so no two players chase the same number, reinforcing that no two playthroughs should converge on the same story.

Net worth alone isn't the whole picture in this option. A parallel happiness/wellbeing meter ("lykkebarometer") tracks what a pure net-worth number hides: stress, free time, social life, housing quality. Like the financial numbers, it would be computed deterministically from measurable state (debt load, hours worked, living conditions, free time) — the AI creates the situations that move these numbers, but does not judge the outcome itself, keeping the "the AI creates the life, the financial engine determines the consequences" principle intact.

This would produce three possible endings, not a binary win/lose:
- **Real win** — net worth target reached and wellbeing stayed above a healthy threshold.
- **Hollow win** — net worth target reached, but wellbeing collapsed getting there: the money cost too much.
- **Loss** — net worth target missed, or an unmanageable debt spiral occurs before the deadline.

**Second option discussed:** instead of the system assigning a target, the player picks a life goal at the start of the playthrough, from a small set such as long-term savings, short-term savings, a specific target amount, or job/education. The chosen goal sets the win condition for that playthrough — its target and its deadline — so "what does winning mean" is answered by the player rather than fixed by the system. This also means the AI-generated events and dilemmas can lean toward situations relevant to the chosen goal (e.g. more education/career-shaped dilemmas for a job/education goal).

The wellbeing meter still runs in parallel, but what it weighs shifts with the chosen goal: a job/education goal would weigh stress and free time more heavily, a savings goal would weigh housing quality and social life more heavily, and so on. As in the first option, it is computed deterministically from measurable state, not judged by the AI.

This would produce the same three-outcome shape as the first option, but measured against the player's chosen goal instead of a system-set net-worth target:
- **Real win** — chosen goal reached and wellbeing stayed above a healthy threshold.
- **Hollow win** — chosen goal reached, but wellbeing collapsed getting there.
- **Loss** — chosen goal missed, or an unmanageable debt spiral occurs before the deadline.

## Choice and Consequence — Decision

**Decided by the team (recorded 2026-11-03, issue #19): cause links plus "Hvorfor?".**

Every effect in the engine stores which choice triggered it. The same link drives:

- echo badges, when an earlier choice comes back
- a "Hvorfor?" button that explains a change
- "if you had chosen differently" lines, calculated by the engine and never by the AI
- the ending, which shows the three choices that mattered most

The decision adds test criteria F9 and F10 to the brief.

Details (recorded 2026-11-03, issue #26):

- **Effects with no choice behind them:** wages in a quiet month or a random expense are stored with a system cause instead of a choice. "Hvorfor?" explains these from the rules.
- **"If you had chosen differently" lines:** only where the engine can calculate the result reliably, starting with interest and instalments.
- **Top three choices:** ranked by the size of their effect in kroner, plus or minus (PRD FR-42).
- **Replay:** starts again from age 15. Replay from a crossroads is left out of the MVP, because it requires storing earlier game states.

## MVP Scope Priority — Decision

*Superseded on 2026-11-10 by PRD §4.4 Cut order, which applies. Kept as history.*

**Decided by the team (recorded 2026-11-03, issue #27): content is cut before the core.** If time runs short before December, cut in this order:

1. "If you had chosen differently" lines during play, including the BSU comparison
2. The parents' share of the moped insurance
3. Events, down to the minimum of 50 (changed on 2026-11-05, proposed by Dahl from the PRD review; earlier 30)

The engine, wellbeing, the endings, cause links, "Hvorfor?", the card warning, the moped and login stay. The AI layer is already outside the MVP.

## Event Library — Decision

*Superseded on 2026-11-10 by PRD FR-17: a minimum of 40 events, a target of 50-60, and 8 per in-game year, with 20 active months. Kept as history.*

**Decided by the team (recorded 2026-11-03, issue #19): a target of 60-80 events, plus about 10 crises. The minimum was 30, and on 2026-11-05 Dahl proposed raising it to 50, twice the 25 regular active months, because 30 events would make two playthroughs share at least 20 of their 25 events (PRD FR-17, FR-43).**

- **Split:** roughly 55/45 before and after age 18.
- **Per year:** every in-game year has at least 10 events whose age range covers it.
- **Fixed schema for every event:**
  - mechanism
  - age
  - flags
  - boomerang pair
  - teaching point
  - LK20 code
  - source
  - wellbeing effect for each choice (added 2026-11-03, issue #23)

## Privacy — Decision

**Decided by the team (updated 2026-11-03): login with an email address and a password.** This replaces the earlier decisions on anonymous login with a code (issue #19) and then on login with a username (issues #19 and #21).

- **Login:** the player logs in with an email address and a password to save and resume progress.
- **Data:** an email address, but no username and no real age in the MVP.
- **Input:** no free text beyond the email address itself.
- **Playtests:** still only with 18-20-year-olds.
- **Later, not MVP:** possibly two modes, school and private.

### Assessment: email address, consent and age limit

This is the project's own reading of GDPR art. 4, 6 and 8 and personopplysningsloven § 5, not legal advice. The team decided on 2026-11-03 that the open privacy questions do not block the MVP and will be checked before LifeMode goes live (issue #24).

- **Is an email address personal data?** Yes. It often contains a real name, and it is tied to one person's stored game. LifeMode should therefore treat all email addresses as personal data.
- **Does that trigger a consent requirement?** Not by itself. Personal data needs a legal basis, and consent is only one of several. The age limit applies when consent is the legal basis for an online service offered directly to a child.
- **What still applies without consent?** The other privacy rules: a named legal basis, clear information to the player, data minimisation, security and deletion.
- **What if consent were used?** The age limit would apply: 13 today, proposed 15. Some 10th graders are 14 for part of the school year, so they would need parental consent if the limit is raised. LifeMode would then have to check age and reach parents, which conflicts with collecting no real age and having no contact with parents. Consent should therefore not be the legal basis.

### Recommended measures

On 2026-11-05 Dahl proposed making the build measures below MVP requirements (PRD NFR-3): player information, deleting accounts after 12 months without a login, and no tracking. The controller and the legal basis stay open until before go-live (#24).

1. **Use the email address only for login and password recovery.** It is not shown in the game, not used for marketing and never sent to an AI.
2. **Document a legal basis other than consent,** and give short player information in language a 15-year-old understands.
3. **Keep as little data as possible.** Use no analytics or advertising cookies, delete inactive games and their email addresses after a set time, and give the player a delete button.

These measures reduce the risk and keep LifeMode outside the consent requirement, but they do not take it outside the privacy rules.

### Login secret: a password the player creates

**Decided by the team (recorded 2026-11-03):** the player creates their own password at registration.

- **Storage:** Supabase Auth stores the password as a hash. The password is never kept in the project's own tables, logs or game state, and is never sent to an AI.
- **Forgotten password:** the player can reset it by email from the login screen.
- **Changing password:** a logged-in player can change it from inside the game.
- **Email confirmation:** no confirmation step before play. The player types the address twice when creating a user, to catch typos, because a mistyped address means a reset email can't reach the player.
- **Password reuse:** not addressed for now, even though some players will use a password they also use elsewhere.

Supabase Auth normally logs in with email or phone, so no internal address is needed. Sending reset email within the zero-cost constraint and on self-hosted Supabase has not been tested, so it should be tried early in the build.

## AI Negotiation Mechanic — Guardrail Detail

Emerged from discovery: the negotiation mechanic (arguing with the bank for a better interest rate) is the sharpest point where the "helpfulness bias" risk meets the core financial-simulation loop. Team decision: the deterministic financial engine sets a base value and a bounded interval (e.g., a defined rate range); the AI selects a value *within* that interval based on argument quality — never outside it. This keeps "the financial engine determines the consequences" true even for AI-mediated outcomes, and the team explicitly does not want the AI to default to lenient/agreeable outcomes — realism over friendliness is the design goal.
