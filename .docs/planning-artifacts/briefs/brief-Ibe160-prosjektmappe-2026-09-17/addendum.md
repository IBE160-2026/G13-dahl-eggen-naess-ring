---
title: LifeMode Addendum
related_brief: brief.md
updated: 2026-11-05
---

# Addendum: LifeMode

Supporting depth that informs the brief but belongs in later work (architecture, PRD) rather than the 1-2 page brief itself.

## Financial Engine — Rule Set v1

Added 2026-10-14 in response to teacher feedback: the engine must "always calculate correctly", so the rules it follows are written down here, together with worked examples that serve as the answer key for automated tests. The numbers are realistic Norwegian 2026 values from official sources where they exist. They are stored as configuration, not hard-coded, so they can be updated without changing the rules.

### Parameters

| Parameter | Value | Source |
|---|---|---|
| Savings account interest | 2.87% per year | SSB table 11018, households, non-fixed deposits, Aug 2026 |
| BSU interest | 5.61% per year | SSB table 11018, households, Aug 2026 |
| BSU deduction | 10% of the year's deposits, max deposit NOK 27,500 per year (max deduction NOK 2,750), max NOK 300,000 in total; the deduction can never exceed the year's tax and is not carried forward | Skatteetaten, satser BSU 2026 and BSU guidance (see research `domain-norwegian-youth-finance-rules-2026-10-27`) |
| Consumer loan interest | 15% per year (fixed) | [ASSUMPTION] No official 2026 average found; market offers range about 9-22% nominal (Smarte Penger, DNB, bytt.no). 15% sits mid-range. |
| Credit card interest (when interest is paid) | 22.6% per year | SSB table 12844, households, 2026 Q2 |
| Hourly wage, under 16 / under 18 / 18+ | NOK 136.41 / 139.40 / 195.04 | Virke/HK Landsoverenskomsten minimum rates from 1 April 2026 (18+ = wage step 1) |
| Working-hour limits | Under 15 or in compulsory schooling (grunnskole): max 2 h per school day and 12 h per school week; 7 h per day and 35 h per week on days and weeks without school. Ages 15-18 after compulsory schooling: max 8 h per day and 40 h per week. 18+: ordinary working hours, 9 h per day and 40 h per week | Arbeidsmiljøloven §§ 10-4 and 11-2 (see research `domain-norwegian-youth-finance-rules-2026-10-27`) |
| Tax-free card (frikort) limit | NOK 100,000 per calendar year; employers withhold 50% above it, but that is withholding, not final tax | Skatteetaten, frikort and forskuddsutskrivingen 2026 |
| Tax 2026 | Trygdeavgift lower limit NOK 99,650; rate 7.6% (5.1% under 17), never more than 25% of income above the lower limit. Minstefradrag 46%, max NOK 95,700. Personfradrag NOK 114,540. Tax on ordinary income 22%. Trinnskatt step 1: 1.7% from NOK 226,100 | Skatteetaten, satser 2026 (see research `domain-norwegian-youth-finance-rules-2026-10-27`) |
| Rent, 1-room flat (hybel) | NOK 8,770 per month (whole country) | SSB table 09895, 2025 (Bergen 7,510, Oslo 10,090) |
| Youth public transport, 30 days | NOK 238 | Ruter, from August 2026 (state-subsidised until April 2027) |
| Mobile subscription | NOK 299 per month | [ASSUMPTION] typical youth plan, not sourced |
| Example unexpected expense | NOK 2,500 (broken phone screen) | [ASSUMPTION] not sourced |
| Moped licence, total | NOK 12,000 (range 8,000-15,000) | TeoriPortalen, 2026-05-01, and Testen.no, 2026-07-24; commercial estimates (see research `prices-moped-and-licences-2026-11-05`) |
| Car licence (class B), total | NOK 32,500 (midpoint of 25,000-40,000) | Testen.no, 2026-07-24, commercial estimate |
| New moped | NOK 29,000 | Dealer ads on FINN for 2026 models, seen 2026-11-05 |
| Used moped, about 7-8 years old | NOK 13,750 | [ASSUMPTION] Midpoint of two private ads on FINN, seen 2026-11-05; not market data |
| Moped insurance | NOK 3,000 per year | [ASSUMPTION] Not verified at a primary source (#29) |
| Petrol 95 | NOK 20.64 per litre | SSB table 09654, average January-September 2026 |
| Policy rate (background only) | 4.5% | Norges Bank API, 13 Oct 2026 |
| Goal target: save for something big | NOK 100,000 net savings | Game design, tuning (PRD OQ-8) |
| Goal target: debt-free buffer | NOK 100,000 in current and savings accounts, no debt | Game design, tuning (PRD OQ-8); about 11 months of hybel rent |
| Big experience price | [needs figure], clearly below NOK 100,000 | To be researched and dated (PRD OQ-3, #43) |
| Spending level | Low 50%, normal 75% (default), high 95% of the wage left after tax and costs; social life −2 a month on low, +2 on high | Game design, tuning (PRD OQ-8) |
| First card limit | NOK 5,000-10,000, default NOK 10,000 | Game design, PRD FR-26 |
| Crisis debt floor | NOK 5,000 | Game design; the bottom of the first-card limit range |
| Crisis cooldown | 2 months | Game design, tuning |
| Payment plan term | 12 months | Game design, tuning |
| Wellbeing start values | Stress 20, social life 60 | Game design, tuning (PRD OQ-8) |
| Wellbeing weights, calm/free time/social | Save for something big 40/30/30; debt-free with a buffer 50/25/25; big experience 30/30/40 | Game design, tuning (PRD OQ-8) |
| Wellbeing threshold | 50 | Game design, tuning (PRD OQ-8) |
| Moped depreciation and floor | 15% of the start value a year; floor 20% of the start value | [ASSUMPTION] Tuning values; research found no Norwegian resale figures (PRD OQ-8) |
| Moped and car fuel use | [needs figure: litres a month] × NOK 20.64 | To be researched and dated (PRD OQ-3, #43) |
| Youth everyday spending | [needs figure], to check the spending levels and event-started costs against | To be researched and dated, for example SIFO's reference budget (PRD OQ-3, #43) |
| Car licence gift chance | 50% | Game design, tuning (PRD OQ-8) |

### Rules

1. **One round is one month.** Each month is processed in a fixed order: income → tax → fixed costs, everyday costs and spending → unexpected expense → loan instalments, the card bill and interest on debt → interest on savings → the month's event and the player's choice → wellbeing. The rule 8 check runs at the end of the month.
2. **Whole kroner.** All amounts are whole NOK. Monthly interest is `balance × annual rate / 12`, rounded to the nearest krone (0.5 rounds up).
3. **Tax.** Tax is calculated on the player's total wage income for the calendar year, using 2026 rates. Up to NOK 99,650 there is no tax. Above that, trygdeavgift applies: 7.6% of the whole income (5.1% under 17), but never more than 25% of the income above NOK 99,650. Income tax is 22% of ordinary income (income minus minstefradrag) above the personfradrag, plus trinnskatt step 1; higher trinnskatt steps are not modelled. Each month the tax step deducts the increase in the year's calculated tax. The 50% that employers withhold above the frikort limit is withholding, settled in the tax assessment, and is not modelled as tax in version one.
4. **Consumer loan.** An annuity loan: equal monthly payments `P × r / (1 − (1 + r)^−n)` with `r` = annual rate / 12, rounded to whole kroner. The final payment is adjusted so the balance ends at exactly zero. At 0% (family loans), each instalment is the amount divided by the number of months, rounded under rule 2, and the final instalment is the amount minus the others.
5. **Credit card.** Each month's debt step pays the card bill: the card balance at that point, including this month's card-payable costs. The engine pays the player's chosen amount (the whole balance, the minimum or a fixed amount), but never more than the current account and savings hold. If the whole balance is paid, no interest is charged. Otherwise interest is charged on the whole balance first, and then the payment is made. The minimum is the larger of 3.5% of the balance before the month's interest and NOK 300, or the whole balance after interest if that is smaller. Paying the minimum never counts as paying in full. Paying less than the minimum is a missed minimum, and it leaves an overdue amount: the minimum minus what was paid. Later payments cover the overdue amount first, and the player can also clear it with an extra payment, which lowers the balance at once and doesn't undo interest already charged. A fixed amount is at least the minimum, in steps of NOK 100. A purchase that would take the balance above the limit is declined. Interest can take it above the limit.
6. **Credit only from 18.** Consumer loans and credit cards are available only from the player's 18th birthday, as in Norway, where minors cannot take on loans. Before 18 the player cannot borrow from a bank. Family loans (PRD FR-27) aren't bank credit and are possible from 15.
7. **Quiet months.** A month without an event is still processed by rules 1-5, but the player only sees a short summary. A playthrough from 15 to the 20th birthday (60 months) is tuned to about 20-30 real choices.
8. **Crisis months.** The engine, not the AI, checks these triggers at the end of every month: the current account is below NOK 0 (savings already used up); the credit card minimum payment has been missed two months in a row, and the overdue amount hasn't been paid; or debt is above the larger of 3 × the average monthly wage income and NOK 5,000. Debt means the card balance, consumer loans and payment plans, not counting family loans, minus the savings account (not BSU), never below 0. Wage income is hourly wages before tax over this month and the two before; months before the game started count as 0. Sales, gifts, the pengegave, family money, interest and loan payouts don't count. The NOK 5,000 floor is configuration. If a trigger is true and no cooldown is running, the next month is a crisis month. There is only one, however many triggers are true, and its event follows the most urgent trigger: below zero, then missed minimum, then debt. A crisis month has up to 3 linked choices with realistic actions (sell something, take extra shifts, ask for a payment plan, stop the card, ask family, ignore it), and the engine calculates the effect of each. An option is shown only when it is possible; asking family and ignoring it are always offered. After each choice the triggers are checked again, and the crisis month ends as soon as none is true, when the player ignores it, or after the third choice. Money a crisis choice brings in goes first to a negative current account, then to overdue card minimums, and the rest stays in the current account. The missed-minimum trigger counts as solved once the overdue minimums are paid, or the card balance moves into a payment plan. After a crisis month, no new one starts for two months (configuration), and the game shows any trigger that is true during the cooldown. In version one a crisis never ends the game: ignored debt keeps growing under rules 4-5 and starts new crisis months after each cooldown. The loss ending applies when a trigger that was true at the end of month 59 is still true at the end of month 60. Month 60 is then always a crisis month, even during a cooldown. A trigger that first becomes true at the end of month 60 doesn't give a loss.
9. **BSU deduction.** The deduction is calculated once a year, at the end of December, so deposits made that month count: the lower of 10% of the year's BSU deposits (deposits capped at NOK 27,500) and the year's calculated tax under rule 3. If the player pays no tax, the deduction is NOK 0, and unused deduction is lost. The game says so plainly ("BSU deduction: NOK 0, you have no tax to reduce") and shows that BSU still pays off through its higher interest (5.61% against 2.87% on an ordinary savings account). Deposits above the year's NOK 27,500 are not accepted. The player can only withdraw the whole BSU. The BSU then closes, and the deductions received so far are added to that month's tax.
10. **Working hours follow Norwegian law.** The engine never lets the player work more hours than arbeidsmiljøloven allows. The limit depends on whether the player is in compulsory schooling, not on age alone: a 15-year-old in 10th grade gets 12 h per school week, while a 16- or 17-year-old in upper secondary school gets 40 h per week. Summer jobs use the limits for weeks without school. Rules on night work (§ 11-3) are not modelled, because the game does not track time of day. In the game, the player sets weekly hours. Monthly hours are weekly hours × 52 / 12, and the monthly cap is the weekly cap × 52 / 12, rounded down. In grunnskole (months 1-18, rule 11) the cap is 12 h a week in every month, because no summer job is offered before 16. From month 19 it is 40 h a week, and summer-job hours in July count towards the same monthly cap of 173 h. A 40 h week is paid for 173 h a month, and the engine cuts a summer-job offer to fit the cap. Daily limits aren't modelled.
11. **Calendar.** The player is born in January. Game month 1 is January of the year the player turns 15, and month 60 is December of the year they turn 19. The game ends on the 20th birthday, after month 60. Game year k (months 12k − 11 to 12k) is one calendar year: the player is 14 + k all year, and it is the income year for rules 3 and 9. The school year runs from August to June, and July is the summer month. The player is in grunnskole in months 1-18 (10th grade from month 8), in upper secondary school in months 20-54, and out of school from month 55. Trygdeavgift is 5.1% in game years 1-2, the years before the calendar year the player turns 17.
12. **Wellbeing.** Stress, free time and social life are whole numbers from 0 to 100. Stress starts at 20 and social life at 60. Each month, free time = 100 − 2 × (school hours + weekly work hours − 30), within 0-100. School counts as 30 hours a week in school months (rule 11), and weekly work hours are the month's hours ÷ (52 / 12). Each event choice changes stress and social life by its own effect, at most 20 points either way. Last in the month, after the choice: if interest was charged on any debt, stress rises by 5, but not above 50. If free time is below 50, stress rises by 5, but not above 50, and social life falls by 5. In a crisis month, stress rises by 10. A postponed family-loan instalment raises stress by 5. If none of these apply and stress is above 20, it falls by 5, but not below 20. On the low spending level (rule 16), social life falls by 2, and on high it rises by 2. Each part is then kept within 0-100. Wellbeing = w1 × (100 − stress) + w2 × free time + w3 × social life, rounded to a whole number (0.5 rounds up), with weights set by the life goal that add up to 100%. Ending wellbeing is the average wellbeing in months 37-60, rounded the same way.
13. **Life goals at 20.** The goal is checked once, after month 60 has been processed, including its choice. Debt is the card balance plus what's left of consumer loans, payment plans and family loans. Family loans count as debt here, although they don't count towards the 3× trigger in rule 8. Net savings = current account + savings account + BSU − debt. Available money = current account + savings account − debt. Belongings such as a moped don't count. Save for something big: net savings ≥ the target. Be debt-free with a buffer: debt is NOK 0, and current account + savings account ≥ the buffer target. Afford a big experience: available money, plus the experience price if the experience was bought, ≥ the experience price. The experience can only be paid for from the current and savings accounts. A goal measure equal to its target counts as reached.
14. **Moped.** The player owns at most one moped and needs the moped licence to own one. The start value is the price paid (new NOK 29,000, used NOK 13,750), or NOK 13,750 for a gift moped. Resale value = start value × (1 − 15% × months owned / 12), rounded to whole kroner, never below 20% of the start value. Months owned = the sale month − the month the player got the moped. In a month when the player owns a moped at the fixed-cost step, transport is moped insurance (NOK 250) and moped fuel, and the public transport ticket isn't charged. A moped got in month m is first charged in month m + 1, and a moped sold in month m is last charged in month m. If the engine draws that the parents pay part of the insurance, the player's NOK 250 falls by that share. The draw is made once, when the player gets the moped.
15. **Payment plan.** In a crisis month, the player can turn the card balance into a payment plan: an annuity loan under rule 4 at the card's interest rate, over 12 months. The card is blocked until the plan is paid. Only one plan can run at a time. The term is configuration.
16. **Spending level.** The player sets a spending level: low 50%, normal 75% or high 95%. The default is normal. Each month, at the fixed-cost step, that share of the wage income left after tax, fixed costs and everyday costs is spent, rounded under rule 2. With no wage left, nothing is spent. With card use on, spending goes on the card as far as it fits under the limit. A change applies from the next month. The shares are configuration.

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
| 9 | Debt trigger, age 19, wage NOK 8,452 in each of the last three months (limit NOK 25,356) | (a) Card NOK 9,000 + consumer loan NOK 17,000, no savings: NOK 26,000, crisis next month. (b) Same, but the NOK 17,000 is a family loan: NOK 9,000, no crisis. (c) As (a) with NOK 2,000 in savings: NOK 24,000, no crisis. (d) No wage for three months, card NOK 4,000: floor NOK 5,000, no crisis; card NOK 6,000: crisis. (e) A NOK 8,800 moped sale leaves the average unchanged |
| 10 | Crisis cadence, cooldown 2 | Below zero at the end of month 40: crisis in month 41, ignored. Months 42-43: cooldown, crisis shown. Still below zero at the end of month 43: crisis in month 44. The first linked choice sells the moped, the account is back above 0, and the crisis ends after one choice. Debt passes the 3× line at the end of month 45: shown, but month 46 is still in the cooldown. Still true at the end of month 46: crisis in month 47 |
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

**17a. Wellbeing over UJ-4 (rule 12).** Markus, 18, in Vg2, works 10 h a week. He starts at stress 20, free time 80, social life 60, wellbeing 74. Weights 40/30/30. W is the month interest starts. The kroner amounts are in the PRD addendum's UJ-4 trace.

| Month | What happens | Hours | Spending | Stress | Free time | Social | Wellbeing |
|---|---|---|---|---|---|---|---|
| W | Card interest starts, and the warning shows. He stops the card, moves spending down and asks for 2 h more a week (social −5) | 10 | High (+2) | 25 | 80 | 57 | 71 |
| W+1 | Interest. Extra shift starts | 12 | Normal | 30 | 76 | 57 | 68 |
| W+2 | Interest. He turns down a cabin weekend (social −5) | 12 | Normal | 35 | 76 | 52 | 64 |
| W+3 | Interest | 12 | Normal | 40 | 76 | 52 | 62 |
| W+4 | Interest | 12 | Normal | 45 | 76 | 52 | 60 |
| W+5 | The card is paid in full, so no interest. He sets 10 h from next month | 12 | Normal | 40 | 76 | 52 | 62 |
| W+6 | He goes to a party (social +10) | 10 | Normal | 35 | 80 | 62 | 69 |
| W+7 to W+9 | No effect on wellbeing from events | 10 | Normal | 30, 25, 20 | 80 | 62 | 71, 73, 75 |

For example, W+1: 0.4 × 70 + 0.3 × 76 + 0.3 × 57 = 67.9, which rounds to 68. Wellbeing never drops below 60, so a real win at 20 is still possible.

**17b. Ending wellbeing (months 37-60).** A careful player on normal spending works 10 h a week to month 54, then 37.5 h full-time: ending wellbeing is 75. A money chaser on low spending, with weights 40/30/30, works 12 h a week to month 18, 40 h from month 19 to 48, 10 h in months 49-54, and 37.5 h full-time after that. He has NOK 590,662 at 20. His ending wellbeing is 41, below the threshold of 50, so he gets a hollow win. It's 45 with goal 2's weights and 35 with goal 3's. If only months 49-60 counted, he would end at 55 and get a real win.

**18. Endings at 20 (rule 13, PRD FR-41)**

| # | State after month 60 | Ending |
|---|---|---|
| a | Current account −NOK 400 at the end of months 59 and 60 (rule 8 still true), net savings NOK 120,000, ending wellbeing 70 | Loss |
| b | Trigger true at the end of months 59 and 60, net savings NOK 30,000, ending wellbeing 30 | Loss |
| c | No condition, net savings NOK 100,000 (exactly the target), ending wellbeing 62 | Real win |
| d | No condition, net savings NOK 112,000, months 37-60 sum to 1,188 (average 49.5, shown as 50) | Real win (boundary) |
| e | As d, but the sum is 1,187 (average 49.46, shown as 49) | Hollow win |
| f | No condition, net savings NOK 99,999, ending wellbeing 80 | Goal not reached |
| g | No condition. Without a loan, net savings would be NOK 95,625. With NOK 50,000 borrowed in month 59 (rule 4, 12 months, instalment NOK 4,513): cash NOK 141,112, loan left NOK 46,112, net NOK 95,000 | Goal not reached either way |
| h | Debt-free goal: current and savings accounts NOK 120,000, BSU NOK 20,000, family loan NOK 1,500 left, ending wellbeing 70 | Goal not reached |
| i | Debt-free goal: current and savings accounts NOK 100,500, BSU NOK 30,000, no debt, ending wellbeing 55 | Real win |
| j | Experience goal: bought in month 56. At 20: current and savings accounts NOK 3,000, card balance NOK 2,000, so available money is NOK 1,000. Ending wellbeing 66 | Real win |
| k | Experience goal: not bought, available money ≥ the price, ending wellbeing 35 (the money chaser in 17b, with goal 3's weights) | Hollow win |

**19. Moped resale and costs (rule 14)**

| Moped | Start value | Months owned | Resale value |
|---|---|---|---|
| Used, bought month 16, sold month 40 | 13,750 | 24 | 13,750 × 0.70 = NOK 9,625 |
| New, owned 24 months | 29,000 | 24 | 29,000 × 0.70 = NOK 20,300 |
| Gift, got month 13, sold month 40 | 13,750 | 27 | 13,750 × 0.6625 = 9,109.375, so NOK 9,109 |
| Used, owned 7 months | 13,750 | 7 | 13,750 × 0.9125 = 12,546.875, so NOK 12,547 |
| Floor check, rate tuned to 25%, 48 months | 13,750 | 48 | 0, so the floor of NOK 2,750 applies |

For the used moped, bought in month 16 and sold in month 40: insurance is charged in months 17-40, so 24 × NOK 250 = NOK 6,000. The player pays the public transport ticket in months 41-60, never together with the moped's costs. Before 18, the parents pay the ticket.

**20. Reference run for goal reachability (rule 13).** Start with a NOK 10,000 pengegave, all in the savings account from month 1. No job until the summer jobs: 120 h in months 19, 31 and 43. Part-time 8 h a week in months 20-54 and full-time 37.5 h in months 55-60. Normal spending (rule 16) all the way. Mobile and transport (NOK 537 a month) from month 37, under PRD FR-23. No moped, licence, card or loan. Net savings at 20: NOK 119,299, with no tax in years 1-3, NOK 1,222 in year 4 and NOK 22,122 in year 5. The balance is NOK 50,487 in month 42 and NOK 76,631 in month 54. The lowest balance is NOK 10,024, in month 1. Ending wellbeing is 75. Goals 1 and 2 are reached, and goal 3 is checked once its price has a source. With one NOK 2,500 unexpected expense a year, net savings are NOK 105,835, which still reaches both.

**21. Earlier play has to matter (rules 13 and 16).** The same jobs as in example 20, with no unexpected expenses unless stated.

| # | Run | Net savings at 20 | Goals 1 and 2 (NOK 100,000) |
|---|---|---|---|
| a | Careless: pengegave spent in month 1, high spending to month 54, low from month 55 | NOK 96,365 | Missed |
| b | High spending all the way, NOK 10,000 kept | NOK 33,096 | Missed |
| c | Low spending all the way, NOK 10,000 kept. Ending wellbeing 57 | NOK 227,061 | Reached |
| d | No job before month 55, pengegave spent, low from month 55 | NOK 107,685, or NOK 94,303 with one NOK 2,500 expense a year | Reached without expenses, missed with them, so this margin is for tuning (PRD OQ-8) |

Examples 7-21 were added on 2026-11-05 from the PRD review and the final check. Examples 17, 20, and 21 were calculated with a script applying rules 2, 3, 12, and 16 month by month. Before the spending level was added, the same script reproduced the review's earlier reference run exactly.

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
| D11 | Credit card: limit and fees (FR-26) | The first card offer | «Forenklet: Kortet ditt har én fast kredittgrense i spillet, og du betaler ingen gebyrer, verken for å gå over grensen eller for å betale for sent. I virkeligheten setter banken grensen ut fra inntekten og gjelden din, den kan endres senere, og det koster ofte gebyr.» |
| D12 | Wages and hours (FR-20, FR-47, rule 10) | The first job offer | «Forenklet: Du velger hvor mange timer du jobber i uka, og spillet gjør det om til lønn for hele måneden, med 52 uker delt på 12 måneder. Skolen regnes som 30 timer i uka. Spillet følger arbeidstidsreglene for alderen din, men holder ikke oversikt over enkeltdager eller om du jobber kveld eller natt.» |
| D13 | Full-time job, no studies (FR-20) | The full-time job offer | «Forenklet: I spillet kan du ikke begynne å studere etter videregående, så det finnes ikke studielån. I virkeligheten er studielån fra Lånekassen rentefritt så lenge du studerer på heltid, og det er noe helt annet enn kredittkortgjeld.» |
| D14 | Feature: breaks and recap (FR-16) | The first recap | «Forenklet: Tiden i spillet går bare når du spiller. Mens du er borte, kommer det ingen renter, regninger eller hendelser, uansett hvor lenge du er borte.» |
| D15 | Feature: "if you had chosen differently" (FR-39) | The first ending summary | «Forenklet: Når spillet viser hva som kunne skjedd hvis du hadde valgt annerledes, regner det bare på pengene i det ene valget, som om alt annet var likt, og som om pengene sto på sparekonto. I virkeligheten kunne et annet valg også ha endret det som skjedde senere.» |
| D16 | Feature: wellbeing (FR-33) | The first wellbeing change | «Forenklet: Trivsel er mye mer enn tre tall. Spillet måler bare stress, fritid og sosialt liv, for å vise at et godt liv handler om mer enn penger. Tallet sier ikke noe om hvordan du har det i virkeligheten.» |
| D17 | Calendar (rule 11) | The first session | «Forenklet: I spillet har alle bursdag i januar. Skoleåret går fra august til juni, og juli er sommerferie.» |
| D18 | Accounts: savings cover the account (FR-45) | The first automatic transfer | «Forenklet: I spillet flytter vi penger fra sparekontoen automatisk når brukskontoen ikke har nok. I virkeligheten må du flytte pengene selv, ellers kan betalingen bli avvist.» |
| D19 | Accounts: negative balance (FR-45) | The first negative balance | «Forenklet: Går du i minus i spillet, betaler du ikke renter eller gebyrer, men det starter en krisemåned. I virkeligheten kan ubetalte regninger gi purregebyr og inkasso.» |
| D20 | Payment plan (rule 15) | The first payment plan offer | «Forenklet: I spillet blir en betalingsavtale et nedbetalingslån over 12 måneder med samme rente som kortet, og kortet sperres til lånet er betalt. I virkeligheten avtaler du vilkårene med banken.» |
| D21 | Consumer loan (FR-25) | The first loan offer | «Forenklet: I spillet koster det ingenting å betale ned lånet før tiden, og banken ser bare på lønna di de siste tre månedene.» |
| D22 | BSU withdrawal (FR-22) | The first BSU deposit | «Forenklet: I spillet kan du bare ta ut hele BSU-en, og da avsluttes den. Du betaler også tilbake skattefradraget du har fått. I virkeligheten skal BSU brukes til bolig, og bruker du pengene til noe annet, mister du fradraget.» |
| D23 | Fixed costs before 18 (FR-23) | The first month summary | «I spillet betaler foreldrene mobilen og bussen din til du fyller 18. Da overtar du regningene. Lommepenger er ikke med i denne versjonen.» |
| D24 | BSU: opening age (FR-18, FR-22) | The first BSU offer | «Forenklet: I spillet kan du opprette BSU selv fra du er 15. I virkeligheten må en foresatt som regel være med, og Skatteetaten fraråder BSU før du er 17 hvis du ikke har skattepliktig arbeidsinntekt.» |
| D25 | Spending level (FR-23, rule 16) | The first wage | «Forenklet: I spillet velger du et forbruksnivå, og en fast del av lønna di går til forbruk hver måned. I virkeligheten går pengene til mange små kjøp, og det er lett å miste oversikten.» |

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

**Decided by the team (recorded 2026-11-03, issue #27): content is cut before the core.** If time runs short before December, cut in this order:

1. "If you had chosen differently" lines during play, including the BSU comparison
2. The parents' share of the moped insurance
3. Events, down to the minimum of 50 (changed on 2026-11-05, proposed by Dahl from the PRD review; earlier 30)

The engine, wellbeing, the endings, cause links, "Hvorfor?", the card warning, the moped and login stay. The AI layer is already outside the MVP.

## Event Library — Decision

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
