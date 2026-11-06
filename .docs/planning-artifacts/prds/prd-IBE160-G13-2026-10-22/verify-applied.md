---
title: Verification that the review proposals landed
date: 2026-11-05
checked_against: review-2026-11-05-solutions.md, review-2026-11-05.md
branch: docs/prd-finalisering
---

# Verification: the 57 review proposals in the edited files

Read in full: `prd.md`, `addendum.md` (PRD), the brief's `addendum.md` and `brief.md`, against every proposal's "Lands in" list and draft text, section 3's adjustments, and `git show main:` for what was removed. Line numbers are from the working copy on this branch. "Brief addendum" means the brief's `addendum.md`, and "PRD addendum" means the PRD's.

## Result

- **53 of 57 proposals are fully applied**, measured by their "Lands in" targets and draft text in substance.
- **4 have a real miss:** M6, M12, K6, K11.
- **All 13 section 3 adjustments landed**, with one gap: adjustment 2 moved the offer months but left two older sentences behind (C1).
- **3 contradictions** sit inside the applied text (C1-C3). Each comes from proposals that were never lined up with each other, not from a bad edit.
- **8 proposals leave a rule from their Recommendation unwritten** (section 4). Their draft text is applied, but under K12 a rule applies downstream only once it's written into the PRD or Rule Set v1.
- No removed line from `main` lacks a proposal behind it. Every figure recomputed by script matches (section 7).

## 1. Real misses

| # | Proposal | Where | What's wrong | Fix |
|---|---|---|---|---|
| R1 | M6 (and M4) | `brief.md:39` | Still says "**crisis month**: two or three linked choices". M6's Conflicts names the brief as carrying this wording. The same line says "debt above three months of income", and the F4 row (`brief.md:94`) says "debt above 3x average monthly income", both older than M4 | Change to "up to three linked choices". Change the debt wording to "debt above 3x the average monthly wage, or NOK 5,000 if that's higher" in both places |
| R2 | M12 | `prd.md:600` (FR-45) | M12's "Lands in" includes "FR-45 money actions", but the list has no action for stopping an everyday cost. FR-23 (`prd.md:538`) allows it "from the money view", and the glossary (`prd.md:149`) points the money view to FR-45. FR-14 (`prd.md:405`) also relies on this list for quiet months | Add "stop an everyday cost that has no binding period (FR-23)" to the FR-45 list |
| R3 | K11 | `prd.md:938-956` (§7.1) | K11's "Lands in" says "Pointers in NFR-5 and 8.1". NFR-5 has its pointer (`prd.md:874`), but §7.1 doesn't mention NFR-11 | Add a clause to the paragraph at `prd.md:954`, such as "on the playtest environment (NFR-11)" |
| R4 | K6 | PRD addendum `:263-272` ("For the architecture") | K6 lands in architecture "Mobile-First Requirements" (test matrix). That section exists (`architecture_technical_design.md:255`), but this list has no item for it. It's the only architecture item from M, X and K that's missing | Add an item: "**Mobile-first:** add NFR-1's supported browsers and test devices as the test matrix" |

## 2. Contradictions in the applied text

| # | Proposals | Where | Contradiction | Fix |
|---|---|---|---|---|
| C1 | X2, G3, adjustment 2 | `prd.md:445`, `:464`, `:467`, `:470`, `:884`; PRD addendum `:202` | FR-18 and the PRD addendum offer the full-time job in month 54 and the summer job in June (months 18, 30, 42). But FR-46 says a milestone "takes the first active month at or after its unlock month", which gives month 56 for an unlock in month 55. FR-18 says "No option is offered before its month", and NFR-7 refuses an option that "hasn't unlocked yet" | FR-46: "…at or after its unlock month, or in the offer month FR-18 gives". FR-18: "No option is offered before the offer month in this table" |
| C2 | M11 against K8 and adjustment 13 | `prd.md:888` against `prd.md:525` and brief addendum `:92` | NFR-7 refuses "a BSU deposit above the yearly cap", and a refusal "leaves the game unchanged". FR-22 and worked example 14 accept part of it: NOK 7,500 of a NOK 10,000 deposit | NFR-7: "a BSU deposit when the year's room is used up, or after the BSU has closed" |
| C3 | M1 against K8 | `prd.md:887` against `prd.md:571` | NFR-7 refuses "a card purchase above the card limit". FR-26 pays that purchase from the current account and says the card was declined, so the game does change. The device also sends only the option picked, so it can't ask for a card purchase. NFR-7's "each case has its own test" then has nothing to test | Remove the NFR-7 line and leave the case to FR-26, or reword it to a case that is really refused |

## 3. Minor wording

| # | Proposal | Where | Issue | Fix |
|---|---|---|---|---|
| L1 | G9 | `prd.md:344`, brief addendum `:152` | FR-9 says the reference run "reaches every target (worked example 20)". G9's sentence "Every target is reached" was dropped when the example was redone. The example now covers goals 1 and 2 only, and goal 3's price is still [needs figure] | Add to example 20: "Goals 1 and 2 are reached. Goal 3 is checked once its price has a source" |
| L2 | M10 | `prd.md:686`, brief addendum `:227` | M10 says a postponed instalment raises stress "(FR-33)". Rule 12 has this, as adjustment 9 asks, but FR-33's stress line and the Win Condition list don't, and neither does FR-27 | Add it to FR-27's postponement consequence |
| L3 | M8, X2 | PRD addendum `:202` | "Months 59-60 stay quiet, unless a crisis takes month 60". Worked example 11 has a crisis in month 59, and FR-46 lets a card warning make a quiet month active | "Months 59-60 are quiet by default. A crisis or card warning can still take them" |
| L4 | K4 | PRD addendum `:40` | "must either work there or have a stated local replacement" is older than K4. NFR-6 now says reset works locally, and `:59` names the inbox | Point the bullet to the routes at `:58-61` |
| L5 | M shared definitions | `prd.md:573`, brief addendum `:60` | "Debt step" is used but defined nowhere. The other three shared definitions (steady wage, money view, wage income) are in the glossary, and rule 1 doesn't name the step | Add a glossary row: "Debt step: the rule 1 step with loan instalments, the card bill, and interest on debt" |
| L6 | X2 | PRD addendum `:206` | "Lands in" says "default template and collision examples". The template and the order are there, but no example is. X2 has no draft text for one, so I count X2 as applied | Add one example, or leave it to the worked examples |

## 4. Rules only in a Recommendation

These are accepted, not in the proposal's draft text, and not in any of the four files. I searched for each one. Decide for each whether to write it into the rule set or leave it for implementers.

| Proposal | Rule not written anywhere | Effect if left out |
|---|---|---|
| M1 | A fixed card payment is at least the minimum, in steps of NOK 100 | The input range isn't testable under NFR-7 |
| M1 | With no setting, the engine pays the whole balance (engine tests only) | Tests may pick different defaults |
| M1 | An extra payment lowers the balance at once and doesn't undo interest already charged | Interest order is open for mid-month payments |
| M10 | The event sets P ≥ NOK 500 and n between 2 and 12, enforced by the schema check | The final instalment can reach zero or below; the event schema in the PRD addendum has no such check |
| G2 | The engine cuts a summer-job offer to fit the monthly cap (the test case: 130 h of part-time work cuts 120 h to 43 h) | Rule 10 gives the cap but not what happens at it |
| G2 | A full-time job is 37.5 h and can be raised to 40 | Implied by FR-47 and example 17b, not stated |
| G4 | The experience price is clearly below NOK 100,000 | Matters when the [needs figure] is filled in |
| G8 | The gift result is shown in the first active month from month 37, and later events can offer the paid licence again | Mostly content; month 37 is already active |
| X7 | Belongings aren't valued and a sale counts when it happens; ties within a crisis month go by order within it | FR-42's tie-break stops at "the choice made first" |
| K1 | Dots and "+tags" stay as typed, and no email is sent at sign-up | FR-1 handles only case and spaces |
| K13 | Option buttons should be 44 × 44 | A "should"; NFR-2 keeps the 24 × 24 minimum |

## 5. Proposal by proposal

"Applied" means every "Lands in" target and draft text is there in substance. References are `prd.md` lines unless marked. GitHub issue targets are deferred, as agreed.

| ID | Status | Evidence |
|---|---|---|
| M1 | Applied (section 4) | Rule 1 and rule 5 (brief addendum `:56`, `:60`), FR-12 `:380`, FR-26 `:565-576`, FR-45 `:600`, D11 (brief addendum `:181`), PRD addendum `:269` |
| M2 | Applied | FR-31 `:647-655`, glossary `:130`, UJ-4 step 1 `:100` |
| M3 | Applied | FR-45 `:593-600`, rule 8, FR-17 `:430`, D18-D19 |
| M4 | Applied | FR-32 `:662`, rule 8, Win Condition (brief addendum `:234`), floor parameter (brief addendum `:43`) |
| M5 | Applied | FR-23 `:530`, `:534-535`, D23, worked example 15 |
| M6 | **Miss R1** | FR-32 `:659-675`, rule 8, §7.3 `:967`, glossary `:133`, F4 are done; `brief.md:39` isn't |
| M7 | Applied | FR-32 `:672-673`, rule 8 options, rule 15, FR-17 `:430`, FR-47 `:505`, D20, worked example 12 |
| M8 | Applied | FR-41 `:779`, `:790-792`, rule 8, worked example 11 |
| M9 | Applied | FR-25 `:558-561`, NFR-7 `:893`, D21, worked example 13 |
| M10 | Applied (L2, section 4) | FR-27 `:584-587`, rules 4 and 6, D4, worked example 8, rule 12 |
| M11 | Applied (C2) | FR-22 `:525-526`, rule 9, FR-45, D22, worked example 14 |
| M12 | **Miss R2** | FR-23 `:528-539`, FR-17 `:431`, event schema (PRD addendum `:233`), rule 1, OQ-8 are done; FR-45 isn't |
| M13 | Applied | UJ-4 `:98-108`, PRD addendum `:95`, `:126-139` |
| M14 | Applied | Worked examples 7-15, NFR-4 `:869`, NFR-9 |
| G1 | Applied | Rule 11, worked example 16, FR-12 `:385`, FR-21 `:514-515`, glossary `:158`, D17 |
| G2 | Applied (section 4) | FR-47 `:499-506`, FR-20 `:495`, FR-14 `:405`, OQ-9 `:982`, rule 10, D12 |
| G3 | Applied (C1) | FR-18 `:455-472`, UJ-1 step 5 `:66` |
| G4 | Applied (section 4) | Rule 13 with payment plans, parameters (brief addendum `:39-41`), FR-9 `:339-345`, glossary `:150`, OQ-3, OQ-8 |
| G5 | Applied | Rule 12, rule 1, parameters (brief addendum `:46-48`), worked example 17, FR-33 `:685-698`, FR-12, glossary `:136`, `:167`, OQ-8, event schema, D16 |
| G6 | Applied | FR-41 `:778-789`, brief addendum `:233-237`, worked example 18 c-e, §7.3 `:969`, F9 |
| G7 | Applied | Rule 14, parameter (brief addendum `:49`), worked example 19, FR-23, FR-24 `:549`, FR-29 `:622-626`, OQ-8, D8 |
| G8 | Applied (section 4) | FR-30 `:630-637`, OQ-8, parameter (brief addendum `:52`), D10 |
| G9 | Applied (L1) | Worked examples 16-20, NFR-4 |
| X1 | Applied | FR-12 `:386-388`, FR-27 `:583`, `:587`, PRD addendum `:237`, `:269` |
| X2 | Applied (C1, L6) | FR-46 `:439-451`, FR-24 `:548-550`, glossary `:153`, OQ-8, PRD addendum `:200-218`, rule 1 |
| X3 | Applied | FR-17 `:428`, FR-43 `:813`, cut list `:187`, `brief.md:112`, `:129`, brief addendum `:292`, `:298-301`, PRD addendum `:124`, `:155` |
| X4 | Applied | All 13 glossary rows, §0 pointer `:12`, FR-17 `:429`, event schema (PRD addendum `:220-233`) |
| X5 | Applied | NFR-4 `:870`, PRD addendum `:239`, `:269` |
| X6 | Applied | FR-36 `:728-731`, glossary `:131`, FR-38 `:747`, PRD addendum `:241` |
| X7 | Applied (section 4) | FR-42 `:796-804`, UJ-5 step 4 `:118`, PRD addendum `:245` |
| X8 | Applied | FR-39 `:752-760`, glossary `:144`, PRD addendum `:247`, D15 |
| X9 | Applied | FR-43 `:814-817`, FR-16 `:421`, NFR-3 `:856`, PRD addendum `:237`, `:249`, §7.1 `:954` |
| X10 | Applied | FR-11 `:361` |
| X11 | Applied | D7-D16 (brief addendum `:177-186`), FR-40 `:764-768`, glossary `:134` |
| X12 | Applied | FR-34 `:706-708`, glossary `:156`, OQ-8 |
| K1 | Applied (section 4) | FR-1 `:233-236`, PRD addendum `:43`, `:49`, `:267` |
| K2 | Applied | FR-1 `:237`, FR-2 `:246`, FR-3 `:254-255`, FR-4 `:266`, PRD addendum `:50-54` |
| K3 | Applied | FR-3 `:256`, FR-4 `:268`, FR-5 `:277-279`, FR-44 `:288`, UJ-2 `:75`, PRD addendum `:55-56`; OQ-5, the school-PC note and the old row are gone |
| K4 | Applied (L4) | OQ-4 `:979`, NFR-6 `:878`, FR-3 `:258`, PRD addendum `:58-61` |
| K5 | Applied | FR-6 `:305-307`, FR-7 `:309-316`, FR-8 `:318-325`, OQ-8, PRD addendum `:268` |
| K6 | **Miss R4** | NFR-1 `:821-831` is done; the architecture list item isn't |
| K7 | Applied | NFR-10 `:916-924`, PRD addendum `:271` |
| K8 | Applied (C2, C3) | NFR-7 `:880-902` with adjustment 13's cases, PRD addendum `:268` |
| K9 | Applied | NFR-3 `:852-855`, `:860`, FR-1 `:231`, 5.1 Notes `:291`, OQ-6 `:980`, PRD addendum `:251-259`, `:272`, brief addendum `:333` |
| K10 | Applied | §7.1 `:954-956`, NFR-3 `:858`, PRD addendum `:261` |
| K11 | **Miss R3** | NFR-11 `:926-934`, NFR-5 `:874`, PRD addendum `:270` are done; the §7.1 pointer isn't |
| K12 | Applied | §0 `:16` |
| K13 | Applied (section 4) | NFR-2 `:835-842`, FR-34 `:708`, FR-37 `:739`, NFR-9 `:914`, OQ-12 `:984`, PRD addendum `:272` |
| E1 | Applied | §9 `:988`, OQ-11 `:983`, PRD addendum `:274-305` (A-1 to A-28, references renumbered) |
| E2 | Applied | §4 `:169-215`, with 4.2 "Never in version one" and 4.3 "Later"; the duplicate row is gone |
| E3 | Applied | §0 `:14` |
| E4 | Applied | Pointers at `:291`, `:860`; 5.1 and 5.5 descriptions `:221`, `:484`; cut-list pointers `:540`, `:748`, `:760`; NFR-4 `:869`; resolved OQs are in `.memlog.md:77-78` |
| E5 | Applied | Tag legend and all listed history lines are gone |
| E6 | Applied | UJ-4 `:97-98`, `:107-109`, UJ-5 `:117-118` (step 4 uses X7's wording) |
| E7 | Applied | NFR-3 `:849`, NFR-6 `:878`, which is now the only "Supabase" in the PRD |
| E8 | Applied | NFR-1 to NFR-11 are `###`; Mermaid diagram at `:369-374` |
| E9 | Applied (sample) | See section 8 |

## 6. Section 3 adjustments

| # | Adjustment | Status | Evidence |
|---|---|---|---|
| 1 | Order within a month | Applied | Rule 1, FR-12 `:380`, diagram `:373` all agree |
| 2 | Active months 1, 3, 6, 8, 10 | Applied, with C1 | PRD addendum `:202`; FR-18 `:467`. No "1, 3, 5, 8" remains. Months 18, 30, 42, 54 fall on position 6 |
| 3 | Month 60 line dropped | Applied | Not in FR-24 `:548-550` |
| 4 | Card warning in the schedule | Applied | FR-46 `:449`, PRD addendum `:206` |
| 5 | One list in FR-45 | Applied, with R2 | FR-45 `:600`, FR-14 `:405`. The adjustment names M3, G2 and G7; M12's action comes from M12's own "Lands in" |
| 6 | Extra shifts | Applied | FR-47 `:505` |
| 7 | Debt for the goals | Applied | Rule 13, FR-9 `:341` |
| 8 | Moped value in UJ-4 | Applied | PRD addendum `:126`, `:132` (NOK 9,300, 26 months); example 17a is redone for keeping the moped at 12 h |
| 9 | Family-loan postponement | Applied (L2) | Rule 12 |
| 10 | One D-text list | Applied | D11, D8, D12, D16 and D10 merged; D17-D23 present; D4 has M10's sentence |
| 11 | Numbering | Applied | FR-45, FR-46, FR-47, NFR-10, NFR-11, rules 11-15, examples 7-20 |
| 12 | Recalculation | Applied | Example 20; OQ-8 and example 20 carry the re-check for everyday costs |
| 13 | NFR-7 cases | Applied, with C2 | `prd.md:884`, `:888`, `:890-892` |

## 7. Figures recomputed by script

All of these match the text:

- **Card at the minimum (rule 5):** NOK 3,200 gives 13 months and NOK 406; 8,400 gives 41 and 3,645; 10,000 gives 51 and 5,508; 6,000 gives 26 and 1,599; 3,000 gives 12 and 357.
- **Loans:** example 3 (1,805, 1,808, 21,663); example 12 (939, 935, 11,264); example 18g (instalment 4,513, cash 141,112, net 95,000).
- **FR-39:** NOK 15,000 over 59 months gives NOK 17,270.
- **Rule 14:** 9,625, 20,300, 9,109, 12,547, and 9,281 after 26 months ("about NOK 9,300").
- **UJ-4 trace:** every row, and NOK 661 in total.
- **Wages and caps:** NOK 8,452, 31,694, monthly caps of 52 h and 173 h.
- **Wellbeing:** 17a (71, 67, 64, 62, 60, 62, 68, 70, 72, 74, lowest 60); 17b (money chaser's sum 552, ending 46; careful player 75); example 20 ending 76.
- **Example 20:** NOK 227,572; 90,109 in month 42; 142,199 in month 54; lowest 10,024 in month 1; tax 1,222 and 22,122; 79% and 91%. It matches only when the 8 h part-time job runs on top of the summer job in months 31 and 43, which is how the text reads ("months 20-54"). Without that overlap the run gives 222,064.
- **Library table (PRD addendum):** the formula gives the listed averages and shares.

## 8. Cross-references, stale wording and prose

- **Requirements:** every FR, NFR, OQ, rule and worked-example reference resolves to the right thing. OQ-5 and OQ-7 aren't referenced anywhere. Rule references stop at 15, and "rule 11" always means the calendar. No FR-17a, FR-20a, D1-D6, D1-D16 or example 8a/8b remains.
- **Sections:** every section reference resolves: 5.1-5.10 in §4.1, §4.1 from the PRD addendum, 7.1, 7.3, §3, §8. No §9, §10 or 8.x remains in the PRD.
- **Issues:** #24, #29, #30, #31, #39 and #43 exist and are open. #32 is closed, which fits OQ-7 being closed.
- **Stale phrases:** "2-3 linked choices", "sells the moped" and "minimum 30" appear only in the PRD addendum's decision table (`:183`, `:186`, `:191`), quoting what changed. "above a healthy threshold" (brief addendum `:253`, `:262`) is in the "Options considered" record, which says the decision applies. "driving licence" (PRD addendum `:101`) describes the old brief. "above the threshold" appears only as "at or above the threshold". The brief addendum's "The minimum was 30" (`:298`) is the record of the change. No "save when idle" or "minimum of 30" remains. The one live stale case is R1.
- **Removed lines:** every line from `main` that no longer appears in the PRD, PRD addendum or brief addendum has a proposal behind it.
- **E9 sample:** P1, P2, P3, P4, P5, P6, P7, P8, P9, P11, P12, P13, P14, P15, P16, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26, P27 and P28 read as applied. P10 is replaced by G1's FR-21 text. For P29, "cannot" no longer appears in the PRD, and the wordings I checked are fixed.

## 9. Checked, not findings

- Section renumbering per E2, closed and new OQs, UJ-4 keeping the moped, examples 17a and 20 redone, and the next-active-month reconciliation of M6 with X2 are all as the task for this check describes them.
- `architecture_technical_design.md` is unchanged against `main`.
- Worked example 9(e) keeps "NOK 8,800". M14's draft has that figure, and it only tests that a sale doesn't count as income, so adjustment 8 doesn't reach it.
- FR-32's "Ignored debt keeps growing" stays as M6's draft has it. UJ-4's "barely shrinks" is M13's case of a player who keeps paying the minimum.
