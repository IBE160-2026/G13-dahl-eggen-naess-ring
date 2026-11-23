---
title: Adversarial review and reconcile — #116 (flow class and month totals, bands, calendar year)
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-23, uncommitted #116 changes)
consulted: ../.memlog.md (last five entries), ../SOLUTION-DESIGN.md, ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (FR-15, FR-21, FR-22, FR-25 to FR-33, FR-45, FR-47, FR-53, FR-57, rules 1, 3, 4, 5, 8, 9, 11, 12, 15, 16 via the brief addendum), ../../../ux-designs/ux-IBE160-G13-2026-11-11/EXPERIENCE.md, DESIGN.md, mockups/index.html (only to read what the spine means where it's terse; EXPERIENCE wins)
lens: (1) Two units one level down that each obey every AD and still build incompatibly. (2) What the final UX shows that the view still can't supply from these rules, and any contradiction.
scope: AD-9 "Flow class and month totals (#116)", AD-13 "Derived figures (#116)", the Time and Config rows. The rest of the spine was read for context only. The spine was not edited.
---

# Review of #116: compliant pairs that collide

**Verdict:** the direction is right (one ledger owns flows, one function owns bands and the year, the frontend derives nothing), but the totals aren't safe to build yet. Two seams let a month-loop story and a ledger story each obey AD-9 and still produce different year figures: the month boundary of the totals isn't fixed, and tax has no flow class. Four more seams (loan interest inside instalments, the open month in the year view, which wellbeing figure gets a band, the year end's wellbeing average) make the UX unbuildable, or buildable two ways. The calendar year formula is correct for every month 1-60. Every hole closes with a sentence or two, and none needs a new unit.

| Severity | Count |
| --- | --- |
| Critical | 2 |
| High | 5 |
| Medium | 7 |
| Low | 7 |

The calendar year was checked month by month. Rule 11 makes month 1 January, so `start_year + (month − 1) // 12` gives 2026 for months 1-12, 2027 for 13-24, and so on up to 2030 for 49-60. That matches "game year k is one calendar year" and age 14 + k. The memlog example (November of year 2 = month 23 = 2027, age 16) checks out. The only gap is after month 60 (L3).

---

## Critical

### C1. Which month a flow belongs to isn't fixed, because continue both closes M and opens M+1

- **Unit A, the month loop (rule 1, AD-4 "Months"):** continue is one engine action. The builder resets the open month's totals at the start of `continue`, since "the ledger keeps the open month's running totals". Then it applies the planned activities, wellbeing and, in December, the BSU deduction. Last it runs M+1's income step, so all of those land in M+1's totals.
- **Unit B, the ledger (AD-9):** "Month close appends them to a per-month list." The builder appends at the end of closing M, after the activities and the deduction, and resets just before M+1's income step.
- **Collision:**
  - December's activities and the December BSU deduction land in January of the next year under A, and in December under B.
  - Rule 9 ties the deduction to "the year's calculated tax", so under A the year's `tax` is wrong in both years.
  - FR-57's "activity spend this in-game year" moves December's evenings into the next year.
  - In month 60 there is no month 61 to append to. Under A, the last deduction and the last activities are never appended, so the ending's figures leave them out.
  - The spine also names two writers: "the ledger keeps" the totals and "month close appends" them. So the append and the reset can end up in two modules.
- **Same gap, smaller cases:** a one-off shift worked in M is paid at M+1's income step (FR-47, #114). The spine doesn't say whether its pay is M+1's `in` (the open ledger) or M's (the month worked). FR-47 says it is taxed in the month it's paid. A December shift is therefore income for next year under rule 3, and nobody has written that down.
- **Fix (AD-9, Flow class bullet):** add
  > "A flow belongs to the month whose totals are open when its ledger call is made. Only `engine/ledger.py` writes the totals: the month loop calls `close_month(M)` as the very last step of closing M (after the planned activities, wellbeing and, in December, the BSU deduction), which appends M's totals; it then calls `open_month(M+1)` before M+1's income step. A start calls `open_month(1)` before any setup step. A one-off shift's pay therefore belongs to the month it is paid, as FR-47 taxes it, so a December shift is income of the next calendar year."

### C2. Tax has no flow class, and the spine's own definition makes it `out`

- **Unit A, income and tax steps:** rule 1 runs income, then tax, as two steps. FR-45's payment-order table pays tax like a cost ("current account, then savings ... always charged"). The builder calls `receive(gross wage)` and then `pay(tax)`. AD-9 makes every call carry one of four classes, and tax is "money leaving to the outside", so the builder books it `out`.
- **Unit B, the same steps read from the decision:** `in` is "wages after the month's tax". The builder books `in` net, either by booking the wage net or by subtracting the tax from `in`. Tax then goes only into the `tax` total.
- **Collision:**
  - Under A, Året's «Ut», the year end and the hub's «brukt» include tax, and «lønn» is gross. Under B they don't, and it's net. This happens in every taxed month (years 4-5 in worked example 20).
  - The BSU deduction (rule 9) is a `receive()` into the current account. "Lowers `tax`" says what happens to the total, not which class the call carries. It isn't wages, a gift or a sale, so one builder books it `in` (other income), another books it only as a tax reduction, and a third books it `internal`.
  - The deductions taken back at a BSU withdrawal (rule 9, FR-22: "taken from the payout at once") have no class at all.
- **Fix (AD-9):** replace the four classes with five:
  > "`tax` is its own flow class, carried by exactly three calls: the monthly tax step (plus), the December BSU deduction (minus, so a December's `tax` can be below 0 while a year's never is), and the deductions taken back at a BSU withdrawal (plus). A `tax` call is never `in` or `out`. Income is booked `in` before tax, and the view's 'in' and the hub's wage are the engine's `in − tax`."

  If the team prefers to store `in` net, the sentence must instead say that the tax call subtracts from `in`. Either way, one of the two has to be written down.

---

## High

### H1. Loan and payment-plan interest sits inside instalments that the rule calls `internal`

- **Unit A, consumer loan (FR-25, rule 4):** it keeps an annuity schedule and books each instalment (principal plus interest, NOK 1,805 in worked example 3) as one `pay()` call. AD-9 says "instalments" are `internal`, so the builder books it `internal`. Loan interest then never reaches `interest`, and the NOK 1,663 of interest in F1 disappears from Året.
- **Unit B, payment plan (rule 15):** it reads "loan interest charged −" and books the interest as an `interest` call on the plan balance each month, then the instalment as `internal`.
- **Collision:** the same rule 4 annuity shows interest under B and none under A. A third builder books the whole instalment `out` and the interest as `interest` as well, and counts it twice.
- **Fix (AD-9):**
  > "Each month, the interest on a consumer loan or payment plan is its own `interest` call that raises that balance, before the instalment; the instalment is `internal`. The card works the same way under rule 5. Family loans carry no interest."

  Also add an invariant that catches every misclassification in this review:
  > "A test asserts for every month of every worked example, seed run and replay: `in − tax − out + interest` = the change in (current account + savings + BSU − card − consumer loan − payment plan − family loan)."

  A moped is a belonging and not a balance, so buying it is `out` and selling it is `in`, and the identity still holds.

### H2. The year view and the year end need the open month, and the rule doesn't say it's included

- **UX:**
  - Året's chart has a "current" month that can be selected (DESIGN: the arrows "take the locked look at the first and current month"). The mockup's «Så langt i år» sums up to and including the current month.
  - The year end appears "when December opens" (EXPERIENCE surface 23). The year's money and the year's tax then have to include December's income, tax, costs and interest, which have already been booked.
- **Unit A, view builder:** "the view carries the current year's month totals from AD-9". It reads the appended list, which holds closed months only, so December is missing from the year end.
- **Unit B, view builder:** it adds the open month's running totals, marked open.
- **Collision:** the year end shows Jan-Nov under A and Jan-Dec so far under B. The chart's current month is empty under A.
- **Fix (AD-13, Money per month):**
  > "The view carries twelve entries for the current calendar year: closed months from the list, the open month from the running totals with `open: true`, and later months as null. The year so far sums the closed months and the open month. At the year end (December open) the year's tax is therefore complete, and the BSU deduction is shown as expected (FR-21), not yet in `tax`."

### H3. Which wellbeing figure gets the band, and on what value, is open to two readings

- **Spine:** "every wellbeing figure in the view (the score, the three parts, the average so far, the ending average) is `{value, band}` ... by FR-33's rule."
- **FR-33 and the UX:** stress and social life each come as a usual value (carried over) and this month's value with activities. EXPERIENCE's Wellbeing tile shows "the month's value including the plan, with «Vanligvis n» under the bar". That is a preview before continue, since rule 12 runs only at close.
- **Unit A, wellbeing builder:** it bands the last closed month's stored values, both usual and this-month.
- **Unit B, view builder:** it bands the plan-inclusive preview and leaves «Vanligvis» without a band.
- **More ways the same figure can band differently:**
  - **Rounding:** the average so far isn't an integer, and example 17b's 50.43 shows as 50, a real win. A builder who bands the unrounded value calls 49.6 `bad`. One who bands the rounded value (50) calls it `warn`, and only that reading agrees with the win check.
  - **Comparison:** with a configurable offset, "from the threshold to 9 above is ok" can be coded as `v > t + offset` for good (so 60 is `warn`) or `v ≥ t + offset` (so 60 is `good`, as in DESIGN's "60 and up").
  - **Before month 19:** the average so far is shown only "once month 19 has been calculated" (FR-33). The spine doesn't say the field is absent before that, so one builder sends null and another averages months 1..M.
  - **Stress:** the value is raw stress or 100 − stress.
- **Fix (AD-13, Bands):**
  > "`band` is computed on the same integer the view shows (rule 2 rounding, 0.5 up): `bad` if v < threshold, `good` if v ≥ threshold + offset, else `warn`; for stress v is 100 − stress, while `value` stays the raw stress. In an open month the banded score and parts are this month's rule 12 result with the planned activities applied (FR-33's 'this month'); the usual stress and social life are plain integers with no band. The average so far is null until month 19 has been calculated."

### H4. The year end shows the year's average wellbeing, and the view doesn't carry one

- **UX:**
  - EXPERIENCE Year end: "the average wellbeing against the trivselsmål".
  - The mockup reads «Trivselen din var 61 i snitt» under «2027 er over», which is that calendar year's average.
  - In year 1 (months 1-12) FR-33 has no average so far at all. In year 2, at December's open, the average so far covers months 19-23, which is not "the year".
- **Unit A, year-end builder:** it shows the average so far, so year 1's year end shows nothing and year 2's shows five months.
- **Unit B:** it averages the year's monthly scores itself, which the "frontend never derives" rule forbids. Or the engine builder adds a second average with its own rounding.
- **Fix:** a decision is needed, then one sentence in AD-13, Bands:
  > "The view also carries `year_average` (the rounded average of the current year's calculated months, as `{value, band}`), which the year end shows."

  Otherwise the UX row changes to "the average so far, from month 19". Today the spine and EXPERIENCE contradict each other.

### H5. "Reads these totals and nothing else" can't feed the hub chips, the month summary or FR-57

- **UX needs breakdowns:**
  - The hub's chips are «lønn», «brukt», «rente» (EXPERIENCE Quiet month, Flow 3). Wage is not `in`: `in` also holds gifts and sales.
  - The month summary lists everyday spending, fixed costs, each automatic transfer and "last month's evenings with their cost".
  - FR-57 shows "activity spend this in-game year, by kind".
- **Unit A, summary builder:** it obeys "nothing else", so it can't split `out` and shows one line.
- **Unit B, summary builder:** it keeps its own per-category accumulation, which is exactly the second count AD-9 is meant to prevent. Its lines need not add up to `out`.
- **Collision:** a gift or a moped sale shows under «lønn» under one reading and nowhere under the other. The year's activity spend in the bank and Året's «Ut» can disagree.
- **Fix (AD-9):**
  > "The totals carry fixed parts that sum to their class: `in` = wage + other income; `out` = spending, fixed and everyday costs, unexpected expenses, activities (by activity kind), and purchases (options, licences, moped, experience). The part comes from the ledger call's cause, and the hub chips, the month summary and FR-57 read the parts."

  The month summary's "last month's evenings" then reads the previous month's `activities` part. That follows from C1: activities belong to the month they were planned in, and they are shown on the next hub.

---

## Medium

### M1. Sign conventions are stated only for `interest`

- **Problem:** one builder stores `out` as −6,593. The view or formatting builder then prints «−» in front, as in the UX's «−6 593 kr brukt», and the screen shows «+6 593». December `tax` can be negative after C2.
- **Fix (AD-9):**
  > "`in` and `out` and their parts are non-negative; `interest` is signed (earned +, charged −); `tax` is signed (charged +, the BSU deduction −). The formatting function adds the sign the UI shows."

### M2. One net `interest` total can't feed the interest chip, its sheet, or Året's strip

- **Problem:** the hub's interest chip opens a sheet that explains savings interest ("23 500 kr × 2,87 % ÷ 12 = 56 kr"). In UJ-4, Markus pays about NOK 180 a month in card interest. The net total (56 − 180 = −124) then doesn't match the sheet's 56, and Flow 4's "blue interest strip" mixes earned and charged.
- **Fix (AD-9):**
  > "`interest` is kept as two parts, `earned` (savings, BSU) and `charged` (card, consumer loan, payment plan); the net is their sum."

### M3. Several money flows have no class, or more than one

Checked against Rule Set v1 and the PRD. The table below gives the one class each flow should get. Flows the current text doesn't settle are marked *.

| Flow | Class |
| --- | --- |
| Wages, summer job, one-off shift pay (paid M+1) | `in` (wage part) |
| Monthly tax step* | `tax` (C2) |
| December BSU deduction* | `tax` (minus), booked in December (C1) |
| Deductions taken back at a BSU withdrawal* | `tax` (plus) |
| BSU deposit, BSU withdrawal, current-savings moves, automatic cover from savings (FR-45) | `internal` |
| Savings and BSU interest | `interest` (earned) |
| Card purchase, card-payable cost, spending on the card | `out` when made |
| Card bill and extra payment, overdue minimums paid from crisis money (rule 8) | `internal` |
| Card interest | `interest` (charged) |
| Consumer loan payout, instalments, early payoff | `internal`; interest is its own call (H1)* |
| Card balance turned into a payment plan (rule 15)* | `internal` |
| Family loan payout and instalments; a postponed instalment moves no money | `internal` |
| Family gift or help money in an event or crisis (FR-27), pengegave | `in` (other) |
| Moped, licences, experience, options, activities, unexpected expenses, fixed and everyday costs | `out` |
| Moped sale, other sales | `in` (other) |
| Gift moped, car licence gift, the parents' share of moped insurance* | no ledger call (no money moves) |

- **Fix (AD-9):** add
  > "A gift of a thing (gift moped, car licence) and the parents' insurance share move no money and make no ledger call; turning the card balance into a payment plan is `internal`; covering a payment from savings is part of that payment, not a separate `out`."

  The rest follows from C2 and H1.

### M4. Engine rules that use "wage income" could read the `in` total

- **Problem:** rule 8's debt trigger and FR-25's loan cap use gross wages over three months, and exclude "sales, gifts, the pengegave, family money, interest and loan payouts". Rule 16 spends a share of "wage income after tax". A crisis-check or spending builder who reuses the new month totals reads `in`, which includes gifts and sales. Rule 16 would then spend part of the pengegave, and rule 8 would count a moped sale as wage.
- **Fix (AD-9):**
  > "The month totals are for display; rule 8, rule 16 and FR-25 read the wage figures their rules name, never `in`."

### M5. The view has the year but not the calendar month

- **Problem:** the timeline («November · 16 år · 2027», «Året, november 2027, du er 16 år»), Året's month labels and its life bar ("Hele livet i spillet", progress through the year) all need the calendar month. AD-13 says the year goes "next to the month and age". If "the month" is the game month 1-60, the frontend computes `(month − 1) % 12 + 1`, which is the kind of date derivation the new bullet forbids.
- **Fix (AD-13, Calendar year):**
  > "The view carries `calendar_month` (1-12) next to `year` and `age`, from the same engine function; the frontend only maps 1-12 to a month name."

### M6. Content authors and the formatting function can disagree on how a past month is written

- **Problem:** the UX writes past months both ways. Flow 4 uses a relative year («I januar i fjor satte du pengegaven på sparekontoen»), while the ending uses absolute years («Byturen på kortet i 2029», «Hytteturen i 2028»). One author writes «i {year}», another expects the function to produce «i fjor», and AD-13 says only that the year comes "only through the one formatting function".
- **Fix (AD-13, Calendar year):**
  > "Game text refers to a month only through one placeholder kind that takes a game month; the formatting function renders it as the month name in the current calendar year, '<month> i fjor' for the year before, and '<month> <year>' otherwise. Authors never write a year."

  If the team wants different wording, the rule can change, but it needs to be one rule.

### M7. The memlog says PRD rule 11 and Rule Set v1 rule 11 "get the start year", and neither has it yet

- **Problem:** AD-7 requires every figure in `content/config/vN/` to have a source and date. `start_year` and the band offset have no row in the Rule Set v1 parameter table. Only "Wellbeing threshold 50" exists. A config author has nothing to cite, and `config/test-vN/` needs both figures for the worked examples.
- **Fix:** add the two parameter rows (start year 2026, D6; band offset 10, FR-33/#111) and the rule 11 sentence upstream. In the spine, the Config row can read:
  > "including `start_year` and the band offset, each with its Rule Set v1 parameter row, also in `config/test-vN/`".

---

## Low

- **L1. `state_schema` for the new fields:** the upgrade function can't rebuild past months' totals from a snapshot (AD-5). Add: "a document upgraded to the totals schema starts its list empty; the v1 freeze clears playtest data anyway (AD-7)."
- **L2. SOLUTION-DESIGN §9, "For the frontend team":** the frontend team reads this table, and it has no rows for bands, the year and month, or the month totals. The nickname change set the precedent of updating it. Add three rows.
- **L3. After month 60:** the player is 20 and it's January of `start_year + 5`, but the formula gives 2030 and age 19. Say what the ending view carries, for example: "after month 60 the view's age is 20 and its year is `start_year + 5`."
- **L4. Enum wording:** the spine's `warn` is FR-33's "ok" and DESIGN's `status-warn`. Note "`warn` is FR-33's 'ok'" so nobody adds a fourth value.
- **L5. Binds lists:** AD-9 should also bind FR-47 (shift pay month) and FR-57 (activity spend this year). AD-13 should name rule 11 next to FR-15.
- **L6. Expected BSU deduction:** the year end shows it (FR-21, EXPERIENCE). It's an engine figure, so under the new "every sum from the engine" bullet the view must carry it. It isn't a month total, so name it in AD-13 next to the year so far.
- **L7. Per-month notes on Året:** the mockup has month notes («Sommerjobb», «Brukt moped»). EXPERIENCE doesn't list them, and EXPERIENCE wins. If the team keeps them, they're game text from the engine (biggest cause in the month), not frontend labels.

---

## Reconcile: what the UX shows against what the view can supply

| UX element | Needs | Supplied by #116? | Gap or contradiction |
| --- | --- | --- | --- |
| Timeline «November · 16 år · 2027» | year, age, calendar month | year and age yes; calendar month no | M5 |
| Wellbeing tile: score, three parts with status word | `{value, band}` on the plan-inclusive month value; «Vanligvis n» | band yes; which value, no | H3 |
| Wellbeing tile: average so far once month 19 is calculated | `{value, band}` or null before | band yes; null and rounding not stated | H3 |
| Hub chips «lønn / brukt / rente» | wage part, `out`, interest | `in` lumps wage with gifts and sales; interest is net | H5, M2 |
| Interest chip, then the interest sheet | savings interest this month | net interest only | M2 |
| Month summary (spending, fixed costs, transfers, last month's evenings) | parts of `out`; the previous month's activities | not from "these totals and nothing else" | H5, C1 |
| Året chart (in up, out down, interest strip, current month selectable, «Så langt i år») | 12 entries including the open month; year so far including open | ambiguous | H2 |
| Year end: year's money, year's tax («0 kr» with why), expected BSU deduction | the year so far including December open; expected deduction | ambiguous; deduction not named | H2, L6, C1 |
| Year end: average wellbeing for the year | year average with band | **not supplied**; contradicts "average so far" | H4 |
| Ending: average wellbeing with status | ending average `{value, band}` on the rounded value | yes, with H3's rounding | H3 |
| FR-57 activity spend this year by kind | `activities` part by kind, year | not supplied | H5 |
| PRD FR-33 status bands (#111) | threshold and offset in config, stress mirrored | matches, apart from the comparison wording | H3 |
| PRD FR-21 December summary | the year's tax before the deduction, expected deduction shown, paid on continue | matches once C1 and H2 hold | C1 |
| PRD rule 3 / FR-47 shift taxed when paid | pay in M+1, income year of payment | matches once C1 is written | C1 |
| PRD FR-45 automatic transfer lines | per-transfer records | outside the totals (internal); fine, but not "these totals" | H5 wording |

No contradiction was found between the spine's band rule and FR-33 or DESIGN, which uses the same boundaries: 60 and up good, 50-59 ok, under 50 bad; stress up to 40 good, 41-50 ok, over 50 bad. That holds once H3 fixes the comparison as `≥ threshold + offset` and bands the rounded value. The only direct contradiction is H4: the year's wellbeing average on the year end.
