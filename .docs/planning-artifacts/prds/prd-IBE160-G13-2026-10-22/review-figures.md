# Figures review: PRD and Rule Set v1

Independent check of the arithmetic and figure consistency in the PRD (`prd.md`, `addendum.md`) and Rule Set v1 (brief addendum), done on 2026-11-13. Every worked example was recalculated from the rule text with new scripts. No earlier recalculation script was read or reused.

## Verdict

The engine figures hold up. Every published figure in worked examples 1-28 reproduces exactly: about 210 values across 28 examples and the PRD addendum's tables. That includes the examples an AI script recalculated on 2026-11-12/13 with the new prices (19, then 20, 22 and 23). Four of the reproductions depend on rounding or setup choices that the rule text doesn't state, so a developer working from the text alone can miss them by 1-3 kr or build a wrong test fixture. The real problems sit around the examples:
- **Stale moped values in two places.** The PRD still has two values from the old NOK 13,750 used-moped price: FR-29's NOK 9,625, and the UJ-4 trace's "about NOK 9,300".
- **The "Borrowing never helps" claim is wrong for goal 3.** A careless run can take a consumer loan in month 56, buy the NOK 60,000 experience, and still end with available money of at least NOK 0. That breaks FR-9a's claim and FR-9b's "careless runs miss all three goals".
- **Moped fuel is undecided.** The newly sourced fuel figure (NOK 186 a month, April-October) conflicts with rule 14, D9 and the examples, which all leave fuel out. Switching it on flips example 22a from "reached" to "missed".

With the two stale values fixed and the goal-3 loan question decided, the figures are safe to build tests from.

## How this was checked

- **Scripts** are in `C:\Users\Dahl\AppData\Local\Temp\claude\eae7983a26745fb0\7c82482c-8f96-42d9-b122-93c1eadbbc7f\scratchpad\figcheck\`. To rerun everything, run `python run_all.py` from that folder (add `-v` for every row).
  - `engine.py`: rules 1-16, with exact `Fraction` arithmetic and rule 2 rounding.
  - `check_small.py`: examples 1-16, 18, 19 and 24-28, plus the PRD addendum tables.
  - `check_runs.py`: examples 17b, 20, 21, 22 and 26c/d.
  - `check_uj4_ex23.py`: the UJ-4 trace, 17a and 23.
  - `check_claims.py`: reachability, goal 3 with a loan, moped fuel, and float traps.
  - `check_rounding_modes.py`, `check_second_ref.py`, `sensitivity.py`, `probe_*.py`: rounding variants, FR-9b's second reference run, and how the examples react to setup choices.
- **Interpretations I had to choose.** The published figures need each one, and each is a gap in the rule text (see findings M5, L1 and L2):
  - I1. In a July with both a part-time job and a summer job, each part's pay is rounded separately, and summer hours cut to the cap stay fractional.
  - I2. The year's tax is rounded once, not part by part.
  - I3. Trinnskatt is charged on the gross wage.
  - I4. Rule 12's "If none of these apply" means no stress row fired. The low-spending row doesn't block the fall in stress.
  - I5. Examples 17b, 21, 22 and 23 use example 20's setup: the pengegave goes to savings in month 1, and each month's surplus is moved to savings at the choice step.
  - I6. In example 23, months 37-40 paid 10 h a week.
  - I7. In example 22, the licence is bought "not before month 20" and the moped "not before month 32", each at the first choice step after that when the player can pay.
  - I8. A "month with spending" means one where the spending amount is above 0.

## Worked examples

"Same" means every figure listed in the published column reproduced exactly.

| Example | Published figure(s) | My figure(s) | Match | Note |
|---|---|---|---|---|
| 1 | NOK 16,728, no tax | 16,728 | yes | |
| 2 | 10,289 (plain compound 10,291) | 10,289 (10,291) | yes | |
| 3 | 1,805; final 1,808; total 21,663 | same | yes | |
| 4 | 13 months; NOK 3,606 paid (406 interest) | same | yes | |
| 5 | 2,588 tax; minstefradrag 50,600 | same | yes | |
| 6 | 10,576 (576 interest); deduction 0 | same | yes | |
| 7 | pays 4,000; interest 113; balance 2,113; at the minimum 26 months, 1,599 | same | yes | |
| 7b | interest 57; pays 300; balance 2,757; at the minimum 12 months, 357 | same | yes | |
| 8 | 833 five times, then 835 | same | yes | |
| 9 | limit 25,356; outcomes (a)-(f) | same | yes | |
| 10, 11 | crisis cadence, month 60 | — | n/a | Logic with no arithmetic. Read, not simulated |
| 12 | 939 eleven times, then 935, total 11,264; at the minimum 51 months, 5,508 | same | yes | |
| 13 | 21,000 | 21,000 | yes | |
| 14 | 7,500 accepted, 2,500 left | same | yes | |
| 15 | below 0 "after about 19 months" | first below 0 in month 19 | yes | |
| 16 | 8,452; 31,694; 16,728 | same | yes | |
| 17a | 10 rows of stress, free time, social life and wellbeing (W to W+9) | same | yes | Needs I4 |
| 17b | careful player 75; chaser NOK 436,849 and 34/37/29; to month 36 349,232 and 39; to month 24 280,578 and 43; 25 h normal 190,387 and 68; 26 h 196,098 and 41; 25 h low 305,678 and 50.43 | same | yes | Needs I1, I2 and I5. Literal pay or tax rounding is off by 1-3 kr (M5) |
| 18 | d 49.5; e 49.48, shown as 49; g 4,513, 136,599, 42,175, 94,424 | same | yes | Other rows are ending logic |
| 19 | 8,152; 20,300; 7,715; 10,626; floor 2,329; insurance 6,000 | same | yes | A float implementation gives 8,151 (M3) |
| 20 | 120,393; tax 0 / 6,295 / 25,298; balances 55,797, 72,206, 80,991, 95,266; lowest 10,000; wellbeing 75. Goal 3: bought month 56, 59,817, wellbeing 73. With expenses: 106,928, lowest 61,563, goal 3 46,352. Wage kept in the current account: 116,184 and 103,065 | same | yes | Needs I3 for year 5 |
| 21 | a 71,584; a2 74,985; a3 77,362; a4 83,094; a5 88,995; b 25,029; c 193,674 (wellbeing 57, social life 0 from month 48); d 81,752; e 57,701 (below 0 in months 37-54); f 116,297; goal-2 lows 113,050, 48,120, ≤ 19,456; month 56 holdings 31,248-48,495; reference 95,266 / 81,929; level switching 109,705/83, 120,373/74, 98,333/75, 145,280/74 | same | yes | The "can't pay for goal 3 in time" sentence is wrong once loans count (H2) |
| 22 | a 100,949 / 87,521, sold for 7,569; b 122,744 / 109,322; c 133,599 / 120,174; d 95,079 / 84,396 (months 34 and 39, sold for 19,575 / 21,388); e 127,729 / 117,050; licence moves to month 21; paid car licence 86,299 | same | yes | Needs I1 for b and I7 for the purchase months (M4) |
| 23 | 104,824; normal 62,637; 10 h low 85,297; wellbeing 61-70; social life 32; about 70 | same | yes | Needs I5 and I6 (L1). Without the savings sweep: 103,410 |
| 24 | 8 slot rows | same | yes | |
| 25 | 8,457; 6,343; 2,364; 56; 1,714; 1,760; 604; 73.8 / 79.8 / 77.8% | same | yes | |
| 26 | a 74, b 73, none 68; c 42/46/37 and careful 85; d 52 and 79 | same | yes | |
| 27c | interest 188; concert share 8 | same | yes | |
| 28 | 475, 471, 467, 463, 459 = 2,335; pengegave 17,270 | same | yes | |
| PRD addendum, UJ-4 trace | 6 rows; interest 682; 122 left; summer job 33,547; 363 | same | yes | |
| PRD addendum, UJ-4 trace | moped sale "about NOK 9,300" | about 7,860 | **no** | Stale: 13,750 × 0.675 = 9,281 (M1) |
| PRD FR-29 | used moped sold after two years: NOK 9,625 | 8,152 | **no** | Stale: 13,750 × 0.70 (H1) |
| PRD addendum, interest and card tables | savings/BSU 60/116, 84/172, 144/287; card 60/13/406, 158/41/3,645, 188/51/5,508; 5,437 after interest; 53 months at 3%; cause shares 75/38 | same | yes | |

**Tally:** Rule Set v1 examples 1-28 reproduce with 0 mismatches. The PRD has 2 stale figures (FR-29, and the UJ-4 trace in two places).

### Other PRD figures checked against the parameter table and examples

All of these match:
- **Wages and pay:** hourly wage 136.41 / 139.40 / 195.04 (FR-18, example 16); full-time pay 31,694 and the 40 h week at 33,742 (FR-47); summer job cut to 43 h (FR-47).
- **Savings:** rates 2.87% and 5.61% (FR-22); 10,289 (FR-22); NOK 84 on NOK 3,000 (UJ-3, FR-22).
- **Card:** limit NOK 5,000-10,000 with a 10,000 default (FR-26); 22.6%; 188, 350, 51 months, 5,508 (UJ-4); 3,200 for 13 months, 3,606 (FR-26).
- **Consumer loan:** 15%; 1,805 / 1,808 / 21,663 (FR-25).
- **Goals and endings:** pengegave NOK 10,000-30,000 (UJ-1, FR-11, glossary); experience NOK 60,000 (FR-9a); goal targets 100,000 and 30,000; threshold 50.
- **Other FRs:** 16,728 (FR-20); 2,588 (FR-21); 833 / 835 (FR-27); 4,000 / 113 (FR-31); 4,182 / 12,182 (FR-48); slot counts (FR-52).
- **UJ-6 and endings:** free time 72 and 3 slots, NOK 604 (UJ-6); 17,270 and 406 (FR-39); 42/46/37, 41 → 52, 34 and 43 (FR-33); the 25 h limit (FR-47).
- **§3.1** rule sentences (except the abbreviation in L6).

§7 quotes no parameter values. "13,750" and "8,938" appear nowhere in `prd.md`, the PRD addendum or Rule Set v1; the stale values that remain are derived from 13,750 (H1, M1).

## Findings

Severity is the impact on the correctness of what developers would build: **critical** (wrong engine results everywhere), **high** (a wrong test, acceptance criterion or goal rule), **medium** (likely to cause a wrong implementation or a test that fails by a few kroner), **low** (wording, sourcing or traceability).

### H1. FR-29 quotes the old used-moped resale value
- **Severity:** high
- **Location:** `prd.md` FR-29, "Resale value" bullet (line 994).
- **Problem:** "A used moped sold after two years fetches NOK 9,625 (worked example 19)." Worked example 19 now says NOK 8,152. The figure is a testable consequence, so an acceptance test written from FR-29 would assert the wrong value.
- **Evidence:** 13,750 × 0.70 = 9,625, the old price. 11,645 × 0.70 = 8,151.5, which rounds to 8,152 (example 19 and `check_small.py`, row "PRD FR-29").
- **Fix:** replace NOK 9,625 with NOK 8,152.

### H2. A consumer loan lets careless runs reach goal 3, despite "Borrowing never helps"
- **Severity:** high
- **Location:** rule 13 (Rule Set line 80); `prd.md` FR-9a (lines 520-521: "It can't be paid for on credit", "Borrowing never helps"); FR-9b (line 526: "every careless run in worked example 21 misses all three goals"); NFR-7 (line 1331); Rule Set example 21 note (line 185: "runs a to a5 … can't pay for goal 3 in time").
- **Problem:** rule 13 only requires that the experience is paid "from the current and savings accounts" and that available money is at least NOK 0 at 20. A loan payout lands in the current account, so nothing stops a player from borrowing in month 56 and paying the experience with that money. Two full-time months (55-56) raise the FR-25 loan cap to NOK 71,000. The months 57-60 of full-time pay then cover the debt in "available money". Example 18g only proves that borrowing can't help goal 1.
- **Evidence** (`check_claims.py`):
  - Run 21a holds NOK 31,248 in month 56. A NOK 29,000 loan over 60 months lets it buy the experience in month 56 and end with available money of NOK 9,851.
  - With the maximum loan, runs a, a2, a3, a4, a5 and d all end at NOK 8,175-25,588 and reach goal 3 as a real win (ending wellbeing 75-84 with goal 3's weights).
  - The rule 8 debt trigger doesn't fire: net debt is about 28,800 against a limit of 71,840.
- **Fix:** decide what "on credit" means and write it into rule 13. Options:
  - (a) Refuse the experience while a consumer loan is outstanding.
  - (b) Require available money, net of debt, of at least the price when buying.
  - (c) Count a consumer loan taken in months 44-56 as credit for this purchase.

  Then add a goal-3 row to worked example 18, and either correct the FR-9b and example 21 claims or make them say "without borrowing".

### M1. The UJ-4 trace still uses the old moped sale value
- **Severity:** medium
- **Location:** PRD `addendum.md`, "UJ-4 month by month", line 48 ("a sale for about NOK 9,300 … the sale alone would nearly clear the debt") and line 65 ("about NOK 9,300 (rule 14, a gift moped owned about 26 months)").
- **Problem:** a gift moped now starts at NOK 11,645. After 26 months it sells for NOK 7,860. If it was got in month 13 (28 months owned), it sells for 7,569. The trace is a set test state, so "check what the moped would sell for" can be asserted from it.
- **Evidence:** 11,645 × (1 − 0.15 × 26/12) = 7,860.4, which rounds to 7,860. At the old price, 13,750 × 0.675 = 9,281, which is the "about 9,300".
- **Fix:** write "about NOK 7,900" in both places. Soften line 48 to "the sale would cover most of the debt". The keep-the-moped story still holds, because 7,860 is less than the NOK 9,314 he owes.

### M2. Moped fuel now has a figure, but the rules and examples say it has none
- **Severity:** medium
- **Location:**
  - Rule Set parameter "Moped and car fuel use" (line 55: NOK 186 a month in April-October, status Assumption).
  - Rule 14 (line 81: transport is insurance and moped fuel, with no seasons).
  - D9 (line 283: «fast beløp hver måned»).
  - Examples 22 and 25 ("moped fuel has no figure yet, so it's left out").
  - PRD addendum UJ-4 trace (line 50).
  - `prd.md` OQ-3 (line 1447).
  - The moped service parameter, which points to OQ-8 while OQ-3 also lists it.
- **Problem:** developers can't tell whether the V1 engine charges moped fuel, and if so whether by season or as a flat amount. The examples' "no figure yet" is now stale wording. Switching the fuel on changes goal outcomes in the test key.
- **Evidence** (`check_claims.py`), with NOK 186 in April-October:
  - Example 22a falls from 100,949 ("reached only with no expenses") to 97,880, which misses goal 1. A flat NOK 108 a month gives 97,825.
  - Example 22b falls to 119,678, c to 130,529, e to 125,057 (all still reached). Example 23 falls to 103,507 (still reached).
  - The UJ-4 card is paid in full one month later (month 47, not W+5), with NOK 771 of interest instead of 682, so 17a and the "five months" story change.
- **Fix:** decide one of two options:
  - (a) Fuel is NOK 0 in V1, like moped service. Say so in the parameter row and rule 14, and write "is set to NOK 0 in these examples" instead of "has no figure yet".
  - (b) Fuel is charged. Add the season (or the flat NOK 108 alternative from the research) to rule 14 and D9, then recalculate examples 22, 23 and 25, the UJ-4 trace and 17a.

  Give moped service one OQ owner.

### M3. Rounding 0.5 up needs exact arithmetic, and floats get example 19 wrong
- **Severity:** medium
- **Location:** rule 2 and rule 14 (Rule Set lines 69 and 81); `prd.md` NFR-4.
- **Problem:** several examples land exactly on .5 (8,151.5 in example 19, 2,587.50 in example 5, 56.5 in example 7b, 7,606.5 in the UJ-4 trace). Nothing in the PRD or Rule Set says the engine must use exact decimal arithmetic.
- **Evidence:** in double precision, 11645 × 0.70 = 8151.499999999999, so "round half up" gives 8,151 instead of 8,152 (`check_claims.py`, "floating-point traps"). The other three cases happen to be exact in binary.
- **Fix:** add to NFR-4, or to the architecture, that money and rates use exact decimal or integer arithmetic (for example `Decimal`, or øre with rates in basis points). Keep example 19's first row as the regression test.

### M4. Example 22's purchase wording contradicts its own months
- **Severity:** medium
- **Location:** Rule Set example 22 (line 189): "each bought at the first choice step the player can pay for it".
- **Problem:** read literally, the player can pay for the licence in month 19, after the summer job, with about NOK 14,600, and for the used moped in month 25. The published months 20 and 32 (34 and 39 for the new moped) only come out if they are earliest months. A fixture built from the text gets different numbers and a different goal result.
- **Evidence:** the literal reading gives licence in month 19, moped in month 25, and net savings of NOK 97,800 for 22a, which misses goal 1 against the published 100,949, reached (`check_runs.py`, rows "22a literal").
- **Fix:** reword as "the licence from month 20 and a moped from month 32, each bought at the first choice step from then on at which the player can pay for it".

### M5. Rounding and tax-base rules that the published figures need aren't written down
- **Severity:** medium
- **Location:** rule 3 (Rule Set line 70), rule 10 (line 77), and `prd.md` FR-47 ("Monthly pay is weekly hours × 52 / 12 × the hourly rate …, in whole kroner").
- **Problem:** three choices change the test key by a few kroner, and the text gives no answer:
  - (a) Is a July with a part-time job and a cut summer job paid as one wage or as two separately rounded lines? Are cut summer hours whole or fractional?
  - (b) Is the year's tax rounded once, or each part (trygdeavgift, income tax, trinnskatt) separately?
  - (c) What is the base for trinnskatt?
- **Evidence** (`check_rounding_modes.py`):
  - **Pay as one wage:** 22b gives 122,745 against the published 122,744. The 17b 25 h runs give 190,385 against 190,387 (normal spending) and 305,675 against 305,678 (low).
  - **Tax rounded per part:** the 17b chaser gives 436,851 against 436,849, and example 23 gives 104,825 against 104,824.
  - **Trinnskatt on ordinary income:** year-5 tax in example 20 would be 25,047, not the published 25,298. The published value needs the gross wage (personinntekt).
- **Fix:** write into rule 10 that summer-job and part-time pay are rounded separately, and that cut summer hours aren't rounded. Write into rule 3 that the year's tax is rounded once under rule 2, and that trinnskatt is charged on the gross wage.

### L1. Several example setups are only implied
- **Severity:** low
- **Location:** Rule Set examples 17b (line 135) and 23 (line 201).
- **Problem:** 17b doesn't say what happens to the pengegave or whether surplus is moved to savings. Example 23 doesn't give the year-4 wages before month 41 (they set the year's tax) or the savings policy. The figures only reproduce with example 20's setup (I5) and with months 37-40 at 10 h (I6).
- **Evidence:**
  - Example 23 without the savings sweep gives 103,410 / 61,795 / 84,409.
  - Other month 37-40 wages give 104,138-107,618 (`sensitivity.py`).
  - The conclusions (goal 1 reached, about 70) hold either way.
- **Fix:** add one sentence to each: "as in example 20: pengegave saved in month 1, surplus moved to savings each month", and for 23, "10 h a week in months 37-40".

### L2. Rule 12: "If none of these apply" is ambiguous
- **Severity:** low
- **Location:** Rule Set rule 12 (line 79).
- **Problem:** "these" could include the low/high spending row. Example 17a W+6 (low spending, and stress still falls from 40 to 35) only works if it means the stress rows only.
- **Fix:** write "If none of the stress rises above apply …".

### L3. The consumer-loan source line cites a range the research doesn't give
- **Severity:** low
- **Location:** Rule Set parameter "Consumer loan interest" (line 24); D5 (line 272).
- **Problem:** the parameter cites "2026 market range about 10-22% nominal (research `prices-oq3-oq17-2026-11-12`)". The research doesn't contain that range. D5 tells players «mellom 9 og 22 %», which disagrees with the parameter row.
- **Evidence:** `experience-loans-hosting.md` §2 gives large banks about 10.4-11.7% *effective*, broker loans up to 48.76% effective, comparison ranges of 5.01-25.00% and 6.82-48.76% effective, and "20-25% realistic" for an expensive variant. The 15% value itself is well sourced (14.8%, Q3 2023).
- **Fix:** quote what the research says (effective rates), and align D5 with the parameter row.

### L4. "Six estimated prices" in the activity catalogue is actually nine
- **Severity:** low
- **Location:** Rule Set parameter "Activity prices" (line 60: "Six prices are estimates marked est."); `prd.md` OQ-17 (line 1457).
- **Problem:** `activities-spending.md` uses no "est." marker. It marks nine activity prices [ASSUMPTION]: café 100, small concert 350, laser tag 300, birthday gift 150, pizza evening 200, restaurant 300, cabin weekend 600, local LAN 250 and shopping trip 500. OQ-17 would have the team source six. Separately, examples 25-28 price the concert at NOK 450, which matches neither catalogue concert (350 small venue, 750 arena).
- **Fix:** write "nine prices are [ASSUMPTION]" and list them in OQ-17. Either keep NOK 450 as a declared test placeholder or align examples 25-28 once the catalogue is approved.

### L5. Some status labels claim more than the research supports
- **Severity:** low
- **Location:** Rule Set parameters "Big experience price" (line 45), "Used moped" (line 38) and "Moped insurance" (line 39).
- **Problem:**
  - **Experience (NOK 60,000), marked Sourced.** The research rates it Medium confidence. 60,000 is the Option A calculation (≈ 57,100) plus about 5% headroom. Its reservation (1,700) and buffer (3,000) lines, and most of Option D, are [ASSUMPTION]. This would be "Partly sourced" under the table's own definition.
  - **Used moped "including the NOK 645 transfer fee".** The research says the fee can't be confirmed in a single ad, and that these are asking prices, not sale prices.
  - **Moped insurance "published ranges … delkasko about NOK 2,500-3,500".** Insurio publishes "from 2,500" and Førerkortet.no "often 2,000-3,000" for young riders. No source publishes 3,500.
- **Fix:** mark the experience Partly sourced. Write "probably including the transfer fee" for the moped. Cite the two insurance figures as published.

### L6. FR-32 leaves out netting against the current account
- **Severity:** low
- **Location:** `prd.md` FR-32 trigger list (line 1031); §3.1 rule 8 (line 234).
- **Problem:** FR-32 says debt is counted "after subtracting savings". Rule 8 also subtracts a positive current account, and example 9(f) depends on it (NOK 24,000, no crisis, against 26,000, crisis). A developer reading FR-32 alone would get 9(f) wrong. Rule Set v1 governs calculations, so the risk is limited.
- **Fix:** write "after subtracting savings and a positive current account".

### L7. Records of where the figures came from are out of date
- **Severity:** low
- **Location:** Rule Set provenance paragraph (lines 258-260); the frontmatter `updated:` dates in Rule Set v1 and `prd.md` (both 2026-11-12).
- **Problem:** the provenance paragraph doesn't mention that examples 19, 20, 22 and 23 were recalculated on 2026-11-12/13 with the new prices, and both files changed on 2026-11-13.
- **Fix:** add one sentence on the 2026-11-13 recalculation and this independent check, and update the dates.

**Counts:** critical 0, high 2, medium 5, low 7.

## Sourced and partly sourced parameters against the cited research

| Parameter | Value | What the research says | Match |
|---|---|---|---|
| Consumer loan interest | 15% | 14.8% nominal (Finanstilsynet, Q3 2023), policy rate now 4.50%. No "10-22% nominal" range | Value yes; range no (L3) |
| Mobile subscription | 299 | Youth plans 229-449; PlussMobil 25GB Ung 299. The research proposes 279 but accepts 299 | yes |
| Unexpected expense | 2,500 | Independent repair 1,800 / 2,390; Apple, older models 1,990-2,990; recommends keeping 2,500 | yes |
| Used moped | 11,645 | Median of 31 scooter ads, 2018-2019 models, 11,645; middle half 8,145-17,645. Fee inclusion is inferred | yes (wording, L5) |
| New moped | 29,000 | `moped-car.md` §3: "a new Kisbee costs NOK 29,000 (earlier research)" | yes |
| Big experience | 60,000 | Pass DKK 4,712, hostels €35, €40 a day: all match. Other trips 51,300 / 54,300 / 63,300 match "51,000-63,000". Option A itself is ≈ 57,100. I checked the research arithmetic: totals and currency conversions are correct | yes (status, L5) |
| Youth everyday spending | 7,800-8,300 | SIFO 2026: 7,808 / 8,188 (ages 15-17), 7,973 / 8,303 (ages 18-19) | yes |
| Activity prices (partly sourced) | 0-3,600; 6 basic + 16 invitation | 6 + 16 activities and a maximum of 3,600 (Øya under-23 pass) match. Nine [ASSUMPTION] prices, not six "est." | Partly (L4) |
| Moped insurance (Assumption) | 3,000 | Insurio "from 2,500" for delkasko under 25; Førerkortet "often 2,000-3,000" | Value in range; wording (L5) |
| Moped service (Assumption) | 2,900 | MC Service AS "normally about NOK 2,900" | yes |
| Fuel use (Assumption) | 9 l = 186; 48 l = 991 | 3.0 and 6.0 l per 100 km, 300 and 800 km; 9 × 20.64 = 185.76, 48 × 20.64 = 990.72 | yes (use: M2) |
| Class B licence age | 18 (17 from 26 Nov 2028) | Statens vegvesen, as cited | yes |
| Petrol, policy rate | 20.64; 4.5% | `moped-car.md` line 3; research §2 (raised to 4.50% on 2026-09-23) | yes |
| Youth transport ticket | 238 (not cited to this research) | The SIFO table in `activities-spending.md` shows Ruter 6-19 at 338 in February 2026. That fits only with the subsidised August 2026 price, which runs until April 2027. D6 holds 2026 figures fixed, so this is a note, not a mismatch | note |

## Reachability spot check

| Claim | Where | My result |
|---|---|---|
| The reference run reaches goal 1 | Example 20, FR-9b | 120,393; 106,928 with June expenses. Holds |
| …and goal 2 | Example 20 | Lowest available money in months 49-60: 72,206, or 61,563 with expenses; no debt. Holds |
| …and goal 3 | Example 20, FR-9b | Bought in month 56; 59,817 at 20, or 46,352 with expenses; wellbeing 73. Holds |
| Careless runs miss all three goals | FR-9b, example 21 | Without borrowing: all of a-a5, b, d and e miss all three. With a loan in month 56, a-a5 and d reach goal 3 (H2) |
| A moped player reaches goal 1 with more hours or less spending | FR-9b, example 22 | b, c and e reach it; a reaches it only with no expenses. Holds with fuel at 0; 22a flips if fuel is charged (M2) |
| Markus's real win | Example 23, UJ-5 | 104,824, ending wellbeing about 70. Holds, with the setup in L1 |
| The hollow win holds with activities | FR-33, example 26c | 42 / 46 / 37, all below 50. Holds |
| Second reference run ("with some free time") | FR-9b | Not published. With the catalogue's cheapest paid basic activity (café, NOK 100) once a month: 113,950 and lowest 67,014; with expenses 100,488 and 56,374. Passes, but only NOK 488 above goal 1 with expenses, so any extra monthly cost (such as fuel) can tip it |
