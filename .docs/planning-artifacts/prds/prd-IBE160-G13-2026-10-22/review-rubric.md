# PRD Quality Review — LifeMode

Reviewed 2026-11-11: `prd.md` (draft, after the 2026-11-10 revision and the 2026-11-11 review fixes), its `addendum.md`, and Rule Set v1 in the brief addendum. This replaces the rubric review of 2026-11-05.

## Overall verdict

The PRD can be set final. The engine is its strongest part: every figure I recomputed matches, IDs and cross-references are clean, and nearly every FR has a testable consequence, so UX, architecture, and stories can extract from it directly. Two things are at risk. The first is the revision's own thesis, "time is as limited as money": activity limits make the slot count barely matter, and month-only effects can't stop low spending from draining social life. The second is delivery: the core that can't be cut grew by three game areas, and the dates for feature freeze and the playtest (OQ-13) are still open.

**What I checked.** With throwaway scripts I recomputed:
- the card table in the addendum (NOK 3,200, 8,400, and 10,000 at the minimum)
- the UJ-4 trace (NOK 682 interest, NOK 122 left)
- worked examples 17b (34/37/29, careful player 75), 24, 25 (NOK 8,457, 6,343, and 604; 73.8% rising to 79.8%), 26c (42/46/37, careful player 85), 26d (41 to 52, 68 to 79), and 28 (NOK 2,335)
- FR-39's NOK 17,270, UJ-3's NOK 84, and the figures in FR-25, FR-47, and FR-48

All of them match. Because the wellbeing script reproduces the PRD's own figures, I used it to test the alternatives proposed below. I didn't check legal claims, prices, or free-tier limits.

## Decision-readiness — strong

Decisions are stated as decisions, with the reason next to them or one link away. The addendum names the rejected alternative for every decision from 2026-11-10 and 2026-11-11 (P1-P8, D1-D12), and several trade-offs state what they cost:
- Wages stay a system cause, although that keeps job choices off the ending screen (addendum, "The ending screen").
- The 25-hour cliff stays because "a visible limit explains the drop".
- Sign-up reveals whether an address already has a user.

§8 gives every question an owner and a Blocks column, and OQ-8 says the threshold and the activity effects are tuned together. Someone pushing back on month-only activity effects gets a real answer in OQ-19 and example 26c, not a dodge. The one question that isn't really open is OQ-19 itself.

### Findings

- **[low]** OQ-19 is a decision written as a question (§8 OQ-19, FR-33, FR-53, rule 12, D26) — It asks the team to "confirm that activity effects count for their month only". It then gives the answer and the reason the alternative fails ("Lasting effects pile up … they remove the hollow win"), and it blocks "Nothing". Month-only effects are already written into FR-33, FR-53, rule 12, D26, and examples 26 and 28. An open question in a final PRD invites someone to reopen this during tuning. *Fix:* record it as decided in the addendum's "Review fixes" table and remove OQ-19, or say what evidence would reopen it.

## Substance over theater — strong

Nothing here is furniture. One protagonist carries six journeys, and the journeys produced real rules:
- UJ-4 produced the card warning and family loans.
- UJ-6 produced the job view's extra-shift figure (NOK 604) and the savings-target thresholds.

The Vision couldn't be moved to another product ("frikort, BSU, credit only from 18, and the moped licence at 16"), and the differentiation claim is narrowed to what the team has actually tried. The NFRs carry thresholds: 320 CSS pixels, 24 × 24 touch targets, and 1 second for 9 of 10 choices on throttled 4G. The survey figures in §2 match `user-research.md`. The PRD also states the survey's limits: it's a convenience sample with only 8 respondents aged 19-20.

### Findings

- **[low]** Two required items still have nothing that uses them (FR-10, FR-17 schema, glossary "LK20 code") — Every event must carry an LK20 code, and the content check enforces it. But no FR shows, uses, or reports the code, and §4.2 rules out classroom use. The avatar is picked in FR-10 and never appears again: not in the room (FR-34), the recap, or the ending. This was raised on 2026-11-05 and is unchanged. *Fix:* say in one line what each is for, such as a curriculum coverage report from the content check, or put them on the cut list.

## Strategic coherence — adequate

The PRD has a clear thesis, and most features serve it: players learn from what their own choices lead to. Every effect carries a cause link (FR-36), and every change has a "Hvorfor?". Choices come back as boomerang pairs with enforced minimums (FR-17), and the ending ranks the choices that mattered (FR-42).

The metrics test the thesis, not just activity. One target is "Can explain how an earlier decision affected a later outcome — 70% or more", and counter-metrics watch for tapping through and for the game turning into a lesson. The cut order follows the thesis, with content cut before the core.

Earlier balance problems are fixed and guarded. Careless runs miss all three goals (example 21), and the content check fails if any change lifts the money chaser to 50 (FR-33).

The weak part is the revision's second thesis, "Time is as limited as money" (§1, §5.5). The money side of that trade-off is real: activities cost kroner, and the job view shows what extra shifts leave after spending. The time side mostly isn't, because of two parameter choices.

### Findings

- **[high]** The number of slots barely changes wellbeing (FR-52, FR-53, FR-33, rule 12, examples 26a-26d, UJ-6, §7.1) — Each activity may move stress and social life by up to ±10, but all activities in a month together only by ±15. Two strong activities therefore reach the cap, and slots three and four add almost nothing. The PRD's own numbers show this:
  - **UJ-6:** Markus's three planned activities give 74 that month (example 26a). A fourth, the gaming evening from 26b, gives 75. The slot that the extra shifts cost him is worth 1 point in one month. Over the three months that's about 0.07 points of ending wellbeing, against NOK 1,812 more after spending. UJ-6's climax, "cost him a slot every month", is true on screen but makes almost no difference to the outcome.
  - **Example 26c:** the money chaser has 1 slot in 27 school months at 40 h and gains 8 points (34 to 42). The careful player has 4 slots every month and gains 10 (75 to 85).
  - **Where slots matter:** with activities at the limits, two slots already reach the cap, so a player loses nothing until 31 h a week leaves one slot. The real time lever is still the free-time cliff between 25 h and 26 h, which was there before the revision.
  - **The metric:** the §7.1 row "Can explain why more work hours gave them fewer activity slots" measures whether players notice the mechanic, not whether it matters, so it passes either way.

  I reran the 17b runs with ±5 per activity and a ±20 monthly cap. The chaser stays hollow (41, 45, 36), and the careful player rises to 89. The 26 h boundary run stays below the threshold at 49, where it now becomes a real win at 52 (26d). Smaller per-activity effects would make slots matter and protect the hollow win at the same time. *Fix:* add a tuning target to FR-52 or OQ-8, such as "in a typical school month, the fourth slot is worth at least N wellbeing points", and have the content check report ending wellbeing at 1, 2, 3, and 4 slots. Consider ±5 per activity with a ±20 cap as starting values, then rerun 26c and 26d.

- **[medium]** Month-only activities can't stop low spending from draining social life (FR-33, FR-23, rule 12, D26, example 21c) — On the low spending level, social life falls by 2 in every month with a wage, and the loss carries over. Activities can't offset it, because their effects count only for the month, and rule 12's rows use the value that carries over.
  - **My run:** a saver works 10 h a week on low spending, with goal 1's weights, and fills every slot every month. The social life that carries over still falls to 0 by month 48, and the "social life below 20" row pushes stress to 50.
  - **What the player sees:** the month's shown social life is then 15, the most the +15 cap allows. The player plans four social activities a month and still sees a social life under 20, and "Hvorfor?" says «Det vanlige sosiale livet ditt er under 20».
  - **The contradiction:** FR-33 says "A good social life has to be kept up", and D26 says «Vil du ha et godt sosialt liv, må du fortsette å gjøre ting». On low spending, nothing in the month plan keeps it up.

  The ending isn't wrong: this saver ends at 68, a real win. The lesson is: being frugal ruins your social life whatever you do with your free time. *Fix:* one option is to let a month with at least one social activity skip the low-spending −2 row. That changes a row rather than carrying an effect, so nothing piles up. In my run the chaser then ends at 45, 48, and 41, still hollow, but goal 2's margin drops to 2 points, so tune it under OQ-8. The other option is to reword FR-33 and D26: the social life that carries over follows events and the spending level, and activities lift only the month.

- **[low]** Some §7 targets can't fail (§7.1, §7.2, §1):
  - Three rows have "Most players" as the target.
  - The Mission row ("A parent or teacher who sees the game wants to try it") has no method, since parents and teachers aren't in the playtest.
  - §1's bar, "more rewarding and smoother to play than Koll på cashen", has no metric at all.
  - The planning counter-metric, "fewer than a third of months holding an applied activity", can be met by tapping "Same as last month" (FR-52) with two free basic activities planned, so it can't tell real planning from habit.

  *Fix:* turn "Most players" into a share, such as 60%, and drop or define the Mission row. Base the planning counter-metric on something a single tap can't fake: the share of invitations applied, which FR-50 already records, or the months whose plan differs from the month before.

## Done-ness clarity — strong

Nearly every FR has consequences an engineer can test, most with a figure:
- the slot count for each number of hours (FR-52)
- the payment order for a card-paid activity (FR-45, example 27)
- the ranking tie-break (FR-42)
- the refusals, each with its own test, and five named cases that aren't refusals (NFR-7)

The worked examples serve as the answer key, and the ones I recomputed match. The non-functional sections give bounds, not adjectives. The soft spots are small: "a small set of preset looks" (FR-10, parked in OQ-9) and "a few states" for each room layer (FR-34). The real gaps are where a journey depends on something no FR produces.

### Findings

- **[medium]** No requirement produces UJ-3's opening message, and its step 4 contradicts UJ-1 (UJ-3, FR-55, message schema, UJ-1 step 5) — UJ-3 opens with "The bank sends a message: his savings have grown, because they have earned interest". FR-55 defines bank messages only as progress towards the savings target or goal 1 passing 25, 50, 75, or 100%. Info messages are drawn by age range and flags (message schema, "when"), with no condition on savings. So nothing guarantees this message, and a drawn one could tell a player with no savings that their savings have grown. The stories for UJ-3, the journey that shows the thesis working, would have nothing to build on.

  Step 4 points Markus to "a part-time job now or a summer job next year", which puts UJ-3 in year 1. But in UJ-1 step 5 he takes the part-time job in month 3, and UJ-4 says he saved for the licence "from his part-time job". *Fix:* add a bank message triggered by the game state to FR-55 and the message schema, such as the first month the year's savings interest passes a set amount, once per playthrough, with the engine's figure. Or move the moment to the December summary, which already shows the year's figures. In step 4, write "more hours now or a summer job next year".

- **[low]** "Can be placed" isn't defined for the message draw (FR-55 "Who can get one", UJ-6 edge cases) — FR-55 draws an invitation "only if its activity can be placed this month". It may include payment, as placing does in FR-53. Then a player with little money never gets a paid invitation, which removes the "small purchases add up" moment for the players who need it most. UJ-6's edge case "He can't afford the concert" could then happen only after he spends money during the month. *Fix:* write "if its activity is eligible this month (age range and flags)", or state that payment is part of the check.

- **[low]** NFR-7's list of what the device sends is narrower than the FRs (NFR-7 opening paragraph, FR-57, FR-52, FR-40, FR-43) — NFR-7 says "The device sends only which option, money action, or activity the player picked … and the server ignores anything else." These requests fit none of those three:
  - pinning a savings target (FR-57 says pinning "isn't a choice")
  - "Same as last month", and removing a planned activity
  - marking a disclosure as seen, which FR-40 stores per account
  - ending a life early (FR-43)

  Read literally, the server ignores all of them. *Fix:* reword it as "the device sends only the player's inputs, never a result", and list pins, plan changes, and disclosure markers among the inputs.

## Scope honesty — adequate

Omissions are stated, and most come with an argument:
- §4.2 says what version one will never do.
- §4.3 gives every later item a status and often a reason, such as "Replay from a crossroads | Out. It needs earlier game states to be stored".
- §2.2 names the non-users and ties one of them to UJ-1.
- The cut order in §4.4 is named and ordered, and says what each cut leaves behind. Item 7, for example, keeps the licences as a payment and changes D10.

The PRD has no inline `[ASSUMPTION]` or `[NOTE FOR PM]` tags. It uses 14 open questions instead, each with an owner and a blocker, which works for this team. That's a reasonable number of open items for the stakes: only OQ-4, OQ-6, and OQ-14 hold up the playtest, and OQ-15 holds up delivery. The schedule and the proposal are less honest than the rest.

### Findings

- **[high]** The core that can't be cut grew, and nothing says when cutting starts (§4.4, OQ-13, §7.1 "Dates", addendum "UJ-1 and UJ-2") — The 2026-11-10 revision added:
  - FR-52 to FR-57
  - three new content schemas
  - 12-20 invitation activities, and enough invitation and info messages for at least 6 invitations a year

  §4.4 now lists "the month plan with the basic activities, the phone with offers and invitations, and the job view" among the things that always stay. The revision proposal's own capacity question (OQ-22, "which of FR-52 to FR-57 are built first, and where the cut line goes now") was closed by putting FR-57 and the activity grouping at the top of the cut list (memlog, 2026-11-10).

  OQ-13, which sets the dates for feature freeze and the playtest, is still open. On 2026-11-03 the addendum put delivery about five weeks away, so about four weeks remain, and the playtest needs at least 7 days plus analysis (§7.1). "If time runs short" has no date or condition, so nobody can tell when to start cutting. With eleven cuts taken one at a time, the later ones would come too late to save any build time. *Fix:* settle OQ-13 now, since the delivery date is known, and tie the cut list to checkpoints, such as "if the month loop isn't playable from start to end by [date], apply cuts 1-6 at once". Also state the size of the smallest build (the always-stay list with every cut applied), so the team can see whether it fits.

- **[medium]** "Changes from the proposal" has only one row (addendum "Changes from the proposal", OQ-15, OQ-11) — The examiner's guide requires anything left out of or changed from the approved proposal to be described and justified, and OQ-15 blocks delivery. The table lists only AI moving to V2. Yet the PRD's own history records several scope changes that may differ from the proposal:
  - login with email instead of a username
  - the car licence (brief Scope Out #5 was changed on 2026-11-04)
  - minigames
  - no tobacco or alcohol choices
  - no student loan
  - the four game areas

  Without the proposal, nobody can say which of these the examiner will look for. OQ-11, whether a delivery with no AI in the app meets the course requirements, depends on the same document. *Fix:* add the proposal to the repo, ideally before the PRD is set final, and fill in the table. Until then, list the known candidates in the table, marked "to check against the proposal".

- **[low]** Moped fuel is NOK 0 in every figure the journeys rely on (UJ-4, UJ-5, UJ-6, the addendum's UJ-4 trace, brief examples 22, 23, and 25, OQ-3) — UJ-4 says the moped "costs him fuel, repairs, and insurance". But the trace and the examples leave fuel out "until #43 gives it a source".
  - **UJ-4:** I reran the trace at 10 litres a month (NOK 206 at the rule set's petrol price). Clearing the card takes six months instead of five, with NOK 776 in interest instead of NOK 682. UJ-4's "After five months" would change.
  - **UJ-5:** the NOK 4,824 margin over goal 1 survives.

  *Fix:* set a placeholder in the parameter table now and rerun the trace and examples 22, 23, and 25. Or say in UJ-4 that its months leave fuel out.

## Downstream usability — strong

Downstream work can extract from this cleanly:
- **Glossary:** 55 terms, with FR pointers. The domain nouns I traced (activity, invitation, offer, real choice, ending wellbeing, net savings, available money) mean the same thing in the FRs, the UJs, the metrics, and the schemas.
- **IDs:** FR-1 to FR-57 each appear exactly once. UJ-1 to UJ-6 and NFR-1 to NFR-11 are complete, and the gaps in the OQ numbering are explained.
- **References:** every reference I checked resolves, including FR, NFR, OQ, UJ, rule, D, and worked-example references.
- **Sections:** each section stands alone, because it cites IDs and glossary terms instead of saying "see above".
- **Addendum:** it gives architecture a ready list (state, requests, the selection step, hosting, seeding), plus full schemas for events, activities, and messages.
- **Journeys:** all six have a named protagonist and an entry state.

### Findings

- **[low]** Terms the FRs rely on are missing from the glossary (§3; FR-47, FR-48, FR-54, FR-55, FR-32) — These terms are defined only inside one FR, or not at all, though each appears in several places:
  - extra shifts
  - drawn offer
  - dated offer
  - card use
  - trigger
  - cooldown
  - threshold (the wellbeing threshold)
  - reference run

  "Extra shifts" also changes meaning in UJ-4. There it means a raised hours setting (the trace adds 2 h a week for five months), not FR-47's offer (+4 h for 3 months by default). *Fix:* add the eight terms. In UJ-4, write "raises his hours", or make the extra hours an extra-shift option of the card warning.

## Shape fit — strong

A PRD built around user journeys is the right shape for a consumer game that feeds UX, architecture, and stories. The journeys carry real weight: each has a protagonist, an entry state, a climax, and edge cases tied to FRs. The financial rules live in Rule Set v1, with worked examples as the test key. That suits a product graded partly on whether it calculates correctly.

The two misfits raised on 2026-11-05 are fixed. The examiner gets seeded test users at the card, crisis, and ending states (NFR-6), and login hardening is the last cut (§4.4 item 11). Six journeys for one protagonist over five years is a fitting number, and UJ-6 is the only one set in a quiet month.

### Findings

- **[low]** The examiner has no reading path (§0) — The PRD is about 1,300 lines. Together with its addendum and Rule Set v1 it comes to about 260 KB, written to be looked up rather than read through. §0 names the examiner as a reader but doesn't say where to start. *Fix:* add two lines to §0: read §1, §2.3, §4, and §7 for the product, and use §5 and §6 as reference.

## Mechanical notes

- **IDs:** FR-1 to FR-57 are unique and contiguous. They aren't in document order (FR-44 is in 5.1, FR-49 in 5.4), which keeps the IDs stable and is fine. UJ-6 sits between UJ-3 and UJ-4 because the journeys follow Markus's life in order. One line in §2.3 would stop readers thinking it's misplaced.
- **Broken cross-references:** three places in the addendum still point to "PRD §4.1" for the cut list, which is now §4.4. They are line 321 ("cut in the order in PRD §4.1") and the "Now in" column at lines 397 and 413.
- **Superseded values in the decision tables:** the addendum's "Decisions from the final PRD check" still reads "low 50%", "Debt-free buffer raised from NOK 50,000 to NOK 100,000", and "months 37-60", each pointing to a current FR. The precedence rule ("the later one applies") covers this, but a reader who lands on that table gets the wrong current value. A "superseded" mark on those rows would help.
- **Teaser example and teaser rule:** FR-15 and UJ-1 use the example "Next year the summer job unlocks". FR-15's rule says the teaser names "the next age unlock (FR-18)", which at the end of year 1 is the moped licence in month 13, as UJ-2 shows.
- **FR-56 and FR-45:** FR-56 says its actions "are the same actions as in FR-45", but FR-45's list has no "take or end extra shifts".
- **Event sender:** the event schema makes `sender` optional, while FR-13 and FR-54 say that the sender of the highlight event "also puts a copy in the phone". Say whether an event with no sender gets no copy.
- **Glossary drift:**
  - "Active month" means both a scheduled slot (FR-46, "4 by default") and a month with a highlight event (glossary).
  - The card warning is a regular event under the glossary's Event entry, but the Highlight event entry lists it apart from story events.
  - For goal 3, FR-9 says "no net debt at 20", while rule 13 says available money of at least NOK 0. Pick one wording.
- **Assumptions Index:** §9 points to A-1 to A-28 in the addendum, and their "Where" entries resolve. The index is dated 2026-11-05. Two assumptions have been logged since: the planning policy, which is now a requirement in FR-9, and Markus paying his own moped insurance in UJ-6. Both appear in the text but not in the index.
- **Required sections:** all present for these stakes: vision, users, journeys, glossary, scope, FRs, NFRs, metrics with counter-metrics, open questions, and assumptions.
