---
title: Review (currency lens): #116 changes to ARCHITECTURE-SPINE.md
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-23, uncommitted diff)
companion: ../.memlog.md (last five entries, 2026-11-23)
scope: Only the #116 changes. AD-9 "Flow class and month totals (#116)", AD-13 "Derived figures (#116)", the Time and Config rows of Consistency Conventions, and the matching Binds/Prevents edits. The rest of the spine was checked in review-currency.md (2026-11-13).
lens: Is every decision and factual claim in these changes reality-checked against the project's sources, and do the Python/Pydantic features they imply fit the Stack table?
method: Read against the brief addendum (Rule Set v1 rules 1, 2, 3, 9, 11, 12, D6), PRD FR-21, FR-22, FR-33 (around line 1138), FR-27, and the final UX (ux-IBE160-G13-2026-11-11 EXPERIENCE.md, DESIGN.md). No web lookup was needed: no claim depends on an external fact that the project's sourced tables don't already hold.
---

# Currency review of the #116 changes

**Verdict:** No new library, framework or technology. The changes use only the Python standard library and Pydantic 2 features that fit the Stack table. The FR-33 band rule, the D6 claim and the calendar example check out. One factual mismatch needs fixing: the BSU deduction is folded into `tax`, but rule 9, FR-21 and the UX treat it as a separate line. Two smaller points about which value gets banded also need fixing.

**Counts:** 7 confirmed · 1 contradicted · 3 underspecified · 1 nit

## Findings

### 1. The BSU deduction folded into `tax` (Medium, contradicted)

AD-9 says "the BSU deduction lowers `tax` in the month it is paid". The sources keep the two apart:

- Rule 9 (addendum line 76): the deduction is the lower of 10% of the year's deposits and "the year's calculated tax under rule 3", and it is "paid into the current account and isn't wage income". The deduction is a payment, and rule 3's tax is a separate figure.
- FR-21 (PRD line 952) and the UX year end (EXPERIENCE.md line 145) show "the year's tax" and "the expected BSU deduction" as two lines. The deduction is still only *expected* there, because it's paid when the player continues.
- So after December closes, Året's and the ending's year tax would be lower than the year-end screen's tax. December's `tax` can also go negative: the deduction can be as large as the whole year's tax, and December's tax step is only that month's increase.
- The spine doesn't say which flow class the deduction's `receive()` call carries, although "every ledger call also carries one flow class". If it carries `in` and also lowers `tax`, the deduction is counted twice in any net figure. If it carries neither, money reaches the current account without showing up in any total.

**Fix:** keep `tax` as rule 3's monthly tax step (never negative). Classify the deduction's ledger call as `in`, since it's money from outside and not wages. If a screen needs to show it on its own line, add a fifth running total, `bsu_deduction`. In the same bullet, also classify the BSU withdrawal clawback (rule 9, FR-22: "deductions received are taken from the payout at once"). It's `out`, while the rest of the withdrawal is `internal`.

### 2. Which stress and social-life value gets banded (Low, underspecified)

FR-33 ("Usual and this month") and the UX wellbeing tile show stress and social life twice: the usual value that carries over, and this month's value including activities («Vanligvis n» appears under the bar when they differ). AD-13 says "the three parts" are `{value, band}`, but doesn't say which of the two values. FR-33 also says stress is banded mirrored (100 − stress). The spine doesn't say whether `value` holds the raw stress figure, though the UI shows the raw one.

**Fix:** one clause: "`value` is the figure as shown: raw stress, not mirrored, and this month's value for stress and social life. The usual value, when shown, gets its own band from the same function."

### 3. The average so far: rounding before banding (Low, underspecified)

FR-33 rounds the ending average to a whole number. The average so far has no rounding rule in the PRD, and the spine bands it without stating one. If it stays a `Decimal`, two things go wrong:

- (a) Banding the unrounded mean can disagree with the shown whole number. For example, 49.6 is shown as 50 but banded `bad`, while the UX says "exactly the number counts as reached".
- (b) Pydantic 2 serializes `Decimal` as a JSON string by default, so `value` would change type between figures in the same view.

**Fix:** "the average so far is rounded under rule 2 before it is banded or shown, like the ending average". With that, every `value` is an `int`, which matches the Money/`int` convention.

### 4. Real-world rules in the years now shown (Low, note for the PRD side)

D6 says «Alle satser og beløp er 2026-tall … holdes faste» (rates and amounts), not rules. With `start_year` 2026, the timeline shows 2026-2030. The addendum already records one known rule change in that window: class B at 17 with accompanied driving from 26 Nov 2028 (addendum line 36, "not in force"). The game's year 3 is 2028, the year the player turns 17. The design is still correct, but an alert tester could ask about it.

**Fix (optional):** when rule 11 gets the start year, broaden D6 to «satser, beløp og regler» or add one line to the licence disclosure. This doesn't touch the spine.

### 5. Nit: Unicode minus in a code span

`start_year + (month − 1) // 12` uses U+2212. Copied into Python, it's a syntax error. The spine already uses `−` in code spans elsewhere (`server_time − last_action_at`), so this follows house style. An ASCII `-` in this one formula would avoid a copy-paste trap.

## Confirmed

| # | Claim in the changes | Source | Status |
| --- | --- | --- | --- |
| 1 | `start_year` 2026 "matching D6's 2026 rates" | D6 (addendum line 276): all rates and amounts are 2026 figures, held fixed through the whole game. Rule 3/FR-21: "every year uses 2026 rates" | Confirmed. Year 1 is the rates' year, and later years show 2027+ with fixed 2026 rates, as D6 discloses. Rule 11 doesn't state the start year yet. The memlog records that as a pending PRD/Rule Set edit, so the spine is ahead of the PRD here, by decision. |
| 2 | Calendar year = `start_year + (month − 1) // 12`; "November of year 2 = 2027, age 16" (memlog) | Rule 11: month 1 is January of the year the player turns 15, and game year k is one calendar year at age 14 + k | Confirmed. Month 23 → 2026 + 22 // 12 = 2027, k = 2, age 16. This matches the UX's «November · 16 år · 2027» (EXPERIENCE.md line 32). Floor division on positive ints is plain Python. |
| 3 | `band(value, threshold, offset, mirrored)` → bad below the threshold, ok up to +9, good from +10, stress mirrored, offset in config | PRD FR-33 "Status bands (#111)" (line 1138); UX wellbeing tile (canonical band rule, threshold 50 by default) | Confirmed. `warn` is the UX/DESIGN token name for the PRD's "ok" (DESIGN.md `status-warn`). The memlog records that mapping, but the spine doesn't. Adding "(`warn` is FR-33's ok)" would help test writers. |
| 4 | Bands also on the average so far and the ending average | FR-33 bands "the score and each part". The UX year end and ending show the average against the trivselsmål, and the UX gives past-tense words for the ending | Consistent extension. Same rule, wider use. Recorded as a decision in the memlog. |
| 5 | Flow classes: card purchase is `out` when made, card bill payment is `internal`, interest is signed, loan payouts and instalments are `internal`, borrowed money is never `in`/`out` | Rules 1, 4, 5, 15; FR-27 (family loans 0% interest, so they never appear in `interest`) | Confirmed and internally consistent. Every krone that changes net savings is in exactly one of `in`/`out`/`interest`, apart from finding 1. |
| 6 | `int` totals; `good`/`warn`/`bad` as an enum | Stack: Python 3.12, Pydantic 2.x; Money convention `int` | Fits. `enum.StrEnum` (3.11+) or `Literal["good","warn","bad"]` both render as an `enum` in the generated OpenAPI schema, so AD-13's committed contract lists the three values. Signed `int` for `interest` is fine. No `Decimal` reaches the view, given finding 3's fix. |
| 7 | Config row: `start_year` and the band offset are pinned game figures in `content/config/vN/` | AD-6/Config convention; FR-33 "the offset is configuration" | Confirmed. Pinning `start_year` per playthrough keeps replay and stored texts stable. |

## New technology

None. The changes add no library, service or framework, and rely only on Python 3.12's standard library and Pydantic 2.x, both already in the Stack table.
