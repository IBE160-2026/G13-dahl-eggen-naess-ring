---
title: LifeMode PRD input reconciliation, revision proposal 2026-11-10
created: 2026-11-11
scope: PRD Finalize, read-only check of prd.md and addendum.md against revision-proposal-2026-11-10-game-loop.md
---

# Input reconciliation: revision proposal 2026-11-10 ("more game, less quiz")

I checked `prd.md` (draft, updated 2026-11-11) and `addendum.md` (updated 2026-11-11) against `revision-proposal-2026-11-10-game-loop.md`. The team accepted proposals P1-P8 on 2026-11-10. The goal was to find anything the proposal intended that the PRD and addendum dropped or contradict without explanation. I looked hardest for qualitative intent, because the FR structure can lose it. Nothing but this file was written.

A difference doesn't count as a gap if one of these explains it:
- the proposal's frontmatter (the OQ renumbering, and P5's month-only refinement under OQ-19)
- the addendum's "Four game areas" section
- the addendum's "Review fixes (2026-11-11)" section (D1-D12)
- `.memlog.md`

**Severity:** Medium changes what a player, a writer, or a downstream reader takes away. Low is a one-line fix.

## Result

| Area | Result |
|---|---|
| P1-P8 decisions | All eight are in the PRD and addendum, as accepted or as refined with a logged reason |
| Core qualitative intent ("time is as limited as money", events as highlights, not a day-by-day simulator, no quiz answers, quiet month in one tap) | Kept: §1 Vision, §5.4, FR-13, FR-14, FR-52, FR-54 |
| Gaps | 4: one medium, three low |

## Gaps

**G1. Medium. P4's plan for the teaching in offers was dropped. Offers now carry no teaching point, LK20 code, or tip.**
- **Input:** proposal §3 P4, "What's lost" (line 95): "a few offers had teaching built into their event options, such as the loan event in month 49. The teaching moves into the message's tip text. Or the team keeps that one as a drawn event." The §2 reuse table (line 62) also reuses "FR-35 opened/closed texts" for the phone.
- **PRD and addendum:** neither alternative happened, and the decision history doesn't mention the loss (addendum "Four game areas", P4 row, line 444).
  - The message schema (addendum lines 145-154) has id, kind, sender, links to, when, and text. It has no tip, teaching point, or LK20 code.
  - The event schema keeps those fields for events only (addendum lines 104-105, 115). Line 129 notes that the `milestone` field is gone, and says nothing about what replaced the teaching.
  - FR-19 is still "Tips in events" (prd lines 590-596), and FR-35 still reads "the event's flags" (lines 956-961).
  - The credit card (month 39) and the consumer loan (month 49) now arrive as plain offer messages (FR-18, lines 565-566). Yet NFR-8 says credit gets "more explanation than the rest" (line 1215).
- **Why it matters:** the two offers the survey and NFR-8 single out for extra explanation have nowhere to carry it. The content check can't require a teaching point for them, and the "Same option" rule in FR-48 (line 582) refers to "texts" without saying where those texts are defined. Without a teaching line, an offer becomes a bare buy button, which works against the "learn from your own actions" intent.
- **Fix:** pick one of these and log it in the addendum's decision history:
  - (a) Give offer messages, or the open option they link to, a required teaching point and LK20 code and an optional tip. Then widen FR-19 to "Tips in events and offers" and FR-35 to "the event's or the open option's flags".
  - (b) Record that the consumer loan stays a drawn event, as P4 allowed, and that the credit card's explanation comes from the card warning (FR-31).

**G2. Low. The UX concept alignment never reaches UX, and the transfer correction isn't in the PRD.**
- **Input:** proposal §4, last row, "UX concept" (line 134). Shift kroner come from FR-47, the estimate covers activity costs only, and "Overføring til sparing −400 kr" is "shown as transfers, not costs". Also §9 (line 412): "UX: the concept sketches fit this proposal, with the changes in §4's last row". And P6 (line 106): "The UI label ('Kalender') is UX's choice."
- **PRD and addendum:** the three corrections appear only in the addendum's decision history, "UX concept alignment" (lines 454-457). By the addendum's own rule (line 9), a decision reaches downstream only once it's in the PRD.
  - The PRD covers shift pay (FR-56, line 681, "never a fixed amount per slot") and the estimate (FR-52, line 616).
  - The PRD doesn't cover transfers. FR-45's "The month summary shows each transfer" (line 715) is about savings covering a shortfall, not about how a transfer is shown.
  - "Detail for downstream work" has only "For the architecture" (lines 13-35), with no UX section.
  - The PRD never mentions the concept sketches, and the sketches aren't in the repo.
  - P6's note on the UI label is missing.
- **Why it matters:** the UX run starts from the concept sketches. Without the three corrections, those sketches still show "+500 kr per slot", a net estimate that includes a shift, and a savings transfer listed as a cost. All three break NFR-4 and FR-42.
- **Fix:**
  - Add a consequence to FR-45 (or FR-57): "Moving money between the player's own accounts is shown as a transfer, never as a cost. It isn't part of a costs total, the plan's total, or upcoming costs (FR-42)."
  - Add a short "For UX" subsection under "Detail for downstream work". It should name the four concept sketches as the starting point, list the three corrections, say the UI label for the month plan is UX's choice (P6), and point to NFR-2 (no dragging). If the sketches are kept, add them to the repo.

**G3. Low. The "less quiz" tone rule isn't in NFR-8, though FR-13 cites NFR-8 for it.**
- **Input:**
  - proposal §6.5, FR-13 (line 314): "options read as actions the player takes, never as quiz answers with one right option"
  - the Norwegian summary, item 4 (line 22): «Ingen melding har quiz-alternativer»
  - the §6.1 vision text (line 160): the player "learns from what their own actions lead to, not from questions and answers"
- **PRD:** FR-13 states the rule and points to "(NFR-8)" (line 486). But NFR-8, Tone and content (lines 1209-1218), has no such bullet. The rule therefore lives only in FR-13 (highlight events) and FR-54 (messages). It's absent from the tone section that content writers and UX use for tips, crisis texts, offer texts, and ending texts. FR-39 (line 1007) also cites NFR-8 for "free time isn't shown as pure loss", which NFR-8 doesn't say either. That one came from the review, not the proposal, but the same NFR-8 edit fixes both.
- **Fix:** add one bullet to NFR-8: "**Not a quiz:** options, messages, tips, and ending texts read as things that happen in the player's life and actions they can take, never as questions with one right answer. Free time and activities aren't framed as wasted money (FR-13, FR-39, FR-54)."

**G4. Low. "The architecture should leave room" for generated-content storage was dropped. The older "may need rework" stance stayed.**
- **Input:** proposal §8, item 4 (line 399): "Generated content needs its own storage in V2, because library versions (NFR-4) don't cover it. The architecture should leave room for that."
- **Addendum:** "Ready for V2", item 4 (line 163), keeps the first sentence and drops the second. The architecture bullet (line 32) keeps the wording from before the revision: "Generated content and its replay under FR-12 aren't designed, and V2 may need rework there." The 2026-11-10 commit changed only "events" to "content" in that bullet, and no decision in the history explains the reversal. The P8 row (line 448) still says the seam "costs nothing now".
- **Why it matters:** the team said it wants AI as game master in V2. The proposal asked the architecture to keep that cheap, and the addendum now tells the architect it's acceptable not to.
- **Fix:** either restore the sentence in the architecture bullet, for example "Leave room for generated content in stored draws, so a draw can hold content as well as a library ID", or log that the team accepts V2 rework there.

## Checked and consistent

These parts of the proposal are in the PRD or addendum, or differ only for a logged reason.

**Month loop (§1):** Explore → Plan → Act → Continue, inside the two-part month (§5.4 diagrams, FR-49). Quiet months can be done in one tap (FR-14). Plans don't carry over (FR-52). "Same as last month" is explained by D12. The game is never a day-by-day simulator (§1, FR-52, D26).

**Reuse (§2):** there's still one wage path, one spending path, and one wellbeing calculation (FR-56, FR-57 "adds no money rule"). The "usual and this month" display is explained by D8.

**P1-P3:** slot formula and table (FR-52). Planning moves no money, and the plan is applied at continue (FR-53, FR-12). Extra shifts never go in a slot (FR-47).

**P4:**
- offers as messages that can't be pushed out (FR-18 offer column, FR-46, FR-55)
- 4 active months (addendum "Event scheduling")
- minimum of 40 events (FR-17)
- overlap table
- the pengegave stays an event
- the event copy replacing the event message kind, and offers arriving before the player qualifies (D4 and the 2026-11-11 schema change)

**P5:** activity effect limits and the monthly cap (FR-53). The month-only refinement is OQ-19, in the addendum, with the 26c figures corrected under the review fixes.

**P6-P8:** the glossary uses "Month plan" (except the UI-label note, G2). Activities are grouped by kind (FR-42, FR-39, cut list item 2). The V2 seam is in the addendum's "Ready for V2", apart from G4.

**§6.1:**
- the vision text, plus "never a day-by-day simulator or a quiz"
- the V2 line
- in-scope items 5.5-5.8 (renumbered under D11)
- cut list items 1-3, and "These always stay"
- the five new §4.3 rows

**§6.2:** every glossary term. "Milestone event" is removed.

**§6.3:**
- UJ-6 was rewritten for November, the car licence target, and the three-quarters message (D1, D2, and the "Checked while applying" notes).
- UJ-1 step 5, UJ-3 step 1, UJ-4 step 4 with its climax ("turning down invitations"), and UJ-5 step 3 are all in.

**§6.4:** FR-52 to FR-57, including NFR-4 engine figures, refusals, and no reading state (D6).

**§6.5:** every delta, from FR-9 to FR-51. Invitations repeat at most once a year (D7).

**§6.6-6.7:** NFR-2, 7, 8, 9, and 10. Metrics 7.1 and 7.2, including the counter-metrics that planning is ignored and that sessions run past 15 minutes.

**§6.9:** open questions mapped as the frontmatter states. OQ-22 is resolved by the 2026-11-10 decision putting the whole revision in, with FR-57 and the grouping first on the cut list.

**§7:** the minimum core matches "These always stay".

**Not counted as a gap:** one V2 idea from the proposal's §5 table, "budget tools, several targets", isn't in PRD §4.3. The proposal's §6.1 never asked for it to be added there.
