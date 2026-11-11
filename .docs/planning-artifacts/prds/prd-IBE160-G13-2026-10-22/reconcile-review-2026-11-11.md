---
title: LifeMode PRD, reconciliation of the 2026-11-11 review fixes
created: 2026-11-11
scope: PRD Finalize, read-only check. Input review-2026-11-11-solutions.md (38 fixes, D1-D12 as recommended)
checked_against: prd.md, addendum.md (PRD), Rule Set v1 in briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md
---

# Reconciliation: the 38 fixes from the 2026-11-11 review

Each fix in `review-2026-11-11-solutions.md` was checked against `prd.md`, the PRD `addendum.md`, and Rule Set v1 in the brief addendum. Where a fix's text was thin, the matching finding in `review-2026-11-11.md` was used. Line numbers are from the working copy on branch `docs/prd-review-2026-11-11`. "PRD add." is the PRD addendum and "Brief add." is the brief addendum. Nothing but this file was written.

The three deviations listed at the top of the solutions file aren't gaps here: J1 (savings NOK 23,500, moped insurance), J2 ("at 18" with no month), and B1 (42/46/37, careful player 85). Their figures were rechecked by hand and match: NOK 8,457 wage, NOK 2,364 at open, NOK 604 from the extra shifts, 73.8% / 79.8% / 77.8%, and NOK 2,335 in example 28.

## Result

| | Count | Fixes |
|---|---|---|
| Applied | 34 | All except the four below |
| Partial | 4 | O1, B3, B5, B6 |
| Missed | 0 | |
| New contradictions or dangling references | 5 | N1-N5 below, plus 6 minor (M-a to M-f) |

## 1. Fix by fix

| Fix | Status | Where it landed | Note |
|---|---|---|---|
| J1 | Applied | prd.md UJ-6 l.106-122; Brief add. ex 25 l.213-227; PRD add. l.479 | Persona, NOK 32,500, pin before opening, three-quarters message, gift edge case (l.122). Extra-shift offer moved to September so the shifts run October-December (FR-47 "from the next month"). Documented deviation. See M-f |
| J2 | Applied | prd.md UJ-4 l.125; PRD add. trace l.41 ("no savings"), l.465, l.480 | Documented deviation ("at 18", no month) |
| J3 | Applied | prd.md UJ-6 title l.105, entry l.107; Brief add. ex 25 l.213, ex 26 l.232, l.240 | December carry-over stated |
| J4 | Applied | prd.md UJ-6 l.105-122, placed between UJ-3 and UJ-4 | "Drafted from…" cut. Origin already in `.memlog.md` 2026-11-10 entry. All step texts, «Konserter og arrangementer», "took the extra shifts" in |
| C1 | Applied | prd.md FR-45 "Activities" l.729; Brief add. ex 27 l.246-249 | Variant c landed as a new example 27 instead of 25c. FR-45 points to example 27 |
| C2 | Applied | prd.md FR-53 "Applied on continuing" l.628; NFR-7 l.1201 | Payment-plan card case included |
| C3 | Applied | prd.md FR-49 l.474; FR-9 l.413; FR-57 l.698 | Text copied as proposed, but see N2 |
| C4 | Applied | prd.md FR-49 l.476; NFR-7 l.1195; PRD add. l.26 | |
| C5 | Applied | prd.md FR-50 l.1101; §7.2 l.1279 | |
| O1 | **Partial** | prd.md FR-18 table l.556-568, l.571; FR-17 l.523; glossary "Offer" l.189; PRD add. schema check l.153, offer table l.64-72; Brief add. D24 l.293 | D11 doesn't follow the fix: O1 says D11 fires on the month 39 card offer message, but Brief add. l.280 says "When the card opens (month 37)". That isn't one of the three listed deviations, and the memlog only says "D11 and D24 triggers". D10 is unchanged but now fires on the month 13 message as intended |
| O2 | Applied | prd.md FR-46 "No repeats" l.549; FR-18 l.563; PRD add. schema "when" l.153 | |
| O3 | Applied | prd.md FR-54 l.649, l.651; FR-55 l.666; FR-48 l.586-588; FR-29 l.860; FR-30 l.867; NFR-7 l.1196; Brief add. parameters l.58-59; OQ-8 l.1299 | See M-c |
| O4 | Applied | prd.md FR-55 "Offers always arrive" l.665 | |
| M1 | Applied | prd.md FR-55 "How many" l.667; Brief add. l.57 | |
| M2 | Applied | prd.md FR-13 l.482; FR-49 l.472; FR-54 l.646-650; glossary "Message" l.183; PRD add. event schema `sender` l.102, message schema `kind` l.150 | No "event" message kind remains. See M-b |
| M3 | Applied | prd.md FR-16 l.514; FR-54 l.654-655; PRD add. l.27, l.470 | |
| M4 | Applied | prd.md FR-55 "Bank messages" l.664; FR-12 l.463; PRD add. l.27, schema l.153 | |
| M5 | Applied | prd.md FR-17 l.523; FR-55 l.668; PRD add. schema l.153; Brief add. l.57 | |
| T1 | Applied | prd.md FR-57 l.697-699; glossary "Savings target" l.197 | Progress text adds "without the card", which matches FR-45 |
| W1 | Applied | prd.md FR-47 l.749-750; FR-56 l.678, l.682; FR-52 l.611 | |
| W2 | Applied | prd.md FR-47 l.746-747; NFR-7 l.1182, l.1201 | Rule 10 isn't changed and doesn't need to be: a cut to 0 h already pays nothing |
| W3 | Applied | prd.md FR-49 "Month 60" l.477; FR-57 l.701; FR-47 l.749 | |
| H1 | Applied | prd.md FR-46 l.544-547; FR-32 "Follow-ups" l.913; PRD add. l.483 | The P4 row at PRD add. l.444 still says "FR-46 loses milestones and push-outs". It's corrected by the later "P4 correction" bullet (l.483), which the addendum's "later section applies" rule covers. Editing the row would be cleaner |
| H2 | Applied | prd.md FR-17 "Size" l.522; FR-46 "No eligible event" l.550 | |
| B1 | Applied | prd.md FR-33 l.937; Brief add. 26c l.242; PRD add. l.450, l.481 | Documented deviation. "Strongest activity" wording is gone, and "only once a month" is in |
| B2 | Applied | prd.md FR-9 "With some free time" l.411 | Leaves a contradiction two lines up: see N1 |
| B3 | **Partial** | prd.md FR-52 l.609-610; FR-33 l.938; Brief add. parameter l.54, 26d l.244; OQ-8 l.1299 | The seeded wellbeing check names the 17b runs at 25 h and 26 h, but not **21c**, which B3 also lists. Example 24's header (Brief add. l.200) still says "at most 4" without "at least 1". See M-a |
| B4 | Applied | prd.md FR-33 "Usual and this month" l.939 | Rule 12 unchanged |
| B5 | **Partial** | prd.md FR-52 l.614; §4.3 l.251; §7.1 "Planning time" l.1267 | The action is in. §7.1 only asks a survey question and reads total session length. No record (FR-50) measures time spent on the month plan, which is what B5 asks for |
| B6 | **Partial** | prd.md FR-39 l.1007; FR-42 l.1048-1052 | Card interest, the wellbeing figure, D15, the hollow-win rule and the tie rule are in. But the line isn't "the group's kroner effect from FR-42": it still grows the cost with savings interest, so example 28 shows NOK 2,335 on the line and ranks by −NOK 2,250. That's the mismatch A21 complained about. See N4 |
| B7 | Applied | prd.md glossary "Mechanism" l.182; FR-17 l.525; PRD add. activity schema l.138 | |
| B8 | Applied | prd.md FR-53 l.624; PRD add. activity schema l.140 | The "can be placed every month" check follows from "no flags, ages 15-20" |
| B9 | Applied | prd.md FR-55 l.663; PRD add. message schema l.152 | |
| B10 | Applied | Brief add. ex 25 l.226-227 (extra shifts, savings target), ex 27 l.246-249 (card-paid activity), ex 28 l.251 (group line); NFR-4 l.1161 "examples 7-28"; Brief add. l.198 | 25c landed as 27 |
| R1 | Applied | prd.md §4.4 l.264-279; FR-29 l.862; FR-38 l.996; FR-39 l.1009; FR-42 l.1049; FR-57 l.694; PRD add. l.281, l.337 | Every place R1 names is fixed, and no item numbers remain. Moving the list to §4.4 left three other references pointing at §4.1: see N3 |
| R2 | Applied | Brief add. l.392, l.404, `updated:` l.4; PRD add. `updated:` l.4; prd.md glossary "Content check" l.164; NFR-4 "Versions" l.1163 | |
| R3 | Applied | prd.md §5.5-5.8 l.598-702, §5.16 l.1090, §4.1 l.213-230, §5.4 description l.435, FR-17 title l.517, FR-53 l.624, FR-56 l.676-684, §1 l.36, §4.3 l.246, FR-55 l.659, §0 l.14, NFR-4 l.1161, glossary order l.155-158 | S4: the payment rule lives in FR-45 (as C1 asks), and FR-53 points there. That's consistent |
| R4 | Applied | Spot-checked P1-P36 and the 15 minor fixes | No "free slot", "adds to stress", "said yes", "utesteder", "on Friday" or "catalog" remains. "Story event", "basic/invitation activities", "in-game phone" and "Applied on continuing" are in |

## 2. New contradictions and dangling references

**N1. FR-9 now contradicts itself on reference runs (from B2).**
- prd.md l.409: "Reference runs and worked examples 1-23 plan no activities (FR-53)."
- prd.md l.411: "a second reference run, for a careful player with some free time, is the reference run above plus the free basic activities and the cheapest paid basic activity once a month."
- Fix: l.409 "The first reference run and worked examples 1-23 plan no activities". PRD add. l.452 ("the reference runs plan no activities") is decision history and is superseded by D9 (l.473), so it can stay.

**N2. FR-49's warning for months 59-60 is wrong for month 59 (from C3).**
- prd.md l.474: "In months 59-60, the warning says that a crisis then can't be solved before the ending."
- A trigger set off in month 59 gives a crisis in month 60, which the player can still solve. It's a loss only if the trigger is still true at the end of month 60 (FR-41 l.1027, l.1038; FR-32). In month 60, a trigger that's true for the first time gives no loss (FR-41 l.1039). The danger is only when it was already true at the end of month 59 (E1's case).
- Fix: "In month 59, the warning says a crisis in month 60 is the last chance before the ending. In month 60, if a trigger was true at the end of month 59, it says continuing like this gives the loss ending."

**N3. Three PRD addendum references still point to §4.1 for the cut list (from R1 and the §4.4 move).**
- PRD add. l.321: "If time runs short, cut in the order in PRD §4.1." This is a live instruction, so change it to §4.4.
- PRD add. l.397, "Now in" column: "PRD §4.1, OQ-13" for the four extra cut steps. Change to §4.4.
- PRD add. l.413, "Now in" column: "FR-51, §4.1" for the driving game staying on the cut list. Change to "FR-51, §4.4".
- R1 listed only l.278 and l.334 (now l.281 and l.337), and both are fixed.

**N4. FR-39 uses "kroner effect" for a different figure than FR-42 (from B6).**
- FR-42 l.1047 defines a choice's kroner effect as the sum of its linked money effects. FR-39 l.1007 says "the line shows the group's kroner effect: its cost, each part grown with savings interest…", which is a different amount. Example 28 (Brief add. l.251) gives NOK 2,335 on the line and ranks by −NOK 2,250.
- Either keep the growth (it matches FR-39 "Money kept" and D15) and rename it ("the line shows what the group's cost would have grown to…"), or use the FR-42 figure as B6 proposed and update example 28. Whichever is chosen, it's a deviation from B6 and should be logged.

**N5. D11's trigger doesn't follow O1, and the change isn't logged as a deviation (from O1).**
- Brief add. l.280: "When the card opens (month 37)". O1: "D11 ('the first card offer') fires on the month 39 message."
- Month 37 can be defended, because the card can be taken from the money view from month 37. But nothing visible happens with the card in month 37, and FR-40 shows a disclosure "the first time its mechanism or feature appears". Choose one ("the first time the card is shown, in the money view or its offer message") and log it.

### Minor

- **M-a.** Brief add. example 24 header (l.200): "Slots = free time ÷ 20, rounded down, at most 4." The parameter (l.54) and FR-52 (l.609) both say "at least 1 and at most 4" (B3).
- **M-b.** The event schema's `sender` is "Optional" (PRD add. l.102), but FR-13 (l.482) and FR-54 (l.650) say without condition that "its sender also puts a copy in the phone". Either make the sender required for highlight events (card warning and crisis events included), or write "if it has one" (M2).
- **M-c.** FR-48 l.588: "A gift arrives as a drawn offer and can be taken only in the month it arrives." The car licence gift isn't a drawn offer: it's the dated month 37 message, and it applies automatically (FR-30 l.867, FR-55 l.665-666). Write "A gift moped arrives as a drawn offer…" (O3).
- **M-d.** FR-18 l.572: "No option is offered before its offer month" sits next to l.571 and FR-48 l.578, which open the card and the loan from month 37, before their offer messages (39, 49). Write "No offer message arrives before its offer month" (O1).
- **M-e.** PRD add. P4 row (l.444) still says "loses milestones and push-outs". The l.483 correction covers it (H1).
- **M-f.** Example 25's three-quarters message fires in November only if progress was below 75% when October opened. Progress at the end of October is NOK 24,000, so October's applied activities plus any BSU deposits must have been under NOK 375 (NOK 24,375 is 75%). UJ-6 doesn't say, and the UJ-4 timing check assumes about NOK 650 of activities a month. One line in example 25 would settle it, for example "October: no paid activities" (J1).

## 3. Checks that came back clean

- **§5 numbering:** §4.1 (l.215-230) and §5.4 (l.435) use 5.5-5.8 and 5.16, which match the headings. PRD add. D11 (l.475) says "right after §5.4". PRD add. A-6 "§5.1" still points to the right section. No reference to the old 5.13-5.15 remains in the three files.
- **"Free slot":** none in the three files. NFR-2 says "empty or holding an activity".
- **Cut-list item numbers:** none. Cut-list references use names, and the names match the §4.4 items.
- **FR-17's new name:** no "Event library" for FR-17 in the PRD or PRD addendum. The brief addendum l.333 and PRD add. l.201 use the phrase as history.
- **Removed "event" message kind:** gone from FR-54, the glossary, and the message schema. The phone copy comes from the event schema's sender.
- **Worked examples 24-28:** every PRD reference points to the right example: UJ-6 → 24, 25, 26; FR-45 → 27; FR-47, FR-53, FR-57 → 25; FR-33 → 26c, 26d; FR-39 → 28; NFR-4 → 7-28; OQ-8 → 26d; OQ-19 → 26c. Brief add. l.198 records which examples were changed and added.
- **Offer months:** FR-18, the PRD addendum offer table (l.64-72), FR-48 (39/49), D3 (l.467), and the UJ-4 trace (card in month 39, W = month 41) agree.
- **Rule Set v1:** rules 1, 7, 10, 12 and 16 agree with the activity, slot, and extra-shift changes. Only the parameter table and examples 24-28 needed edits, and those are in.
