# Review: coverage of the PRD feedback

| | |
|---|---|
| **Feedback checked** | `tilbakemelding-prd.md` (Bård, 2026-11-12) |
| **Checked against** | `prd.md` (frontmatter `status: draft`, `updated: 2026-11-12`), `addendum.md`, Rule Set v1 (`briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md`), `.memlog.md` lines 150-168, `refleksjon-prd-tilbakemelding.md`, open GitHub issues on 2026-11-13 |
| **Line numbers** | Working tree at `c67cc77` (main) |
| **Date** | 2026-11-13 |

## Overall verdict

**Mostly handled, but not ready to set final yet.** Every improvement section (4.1-4.5), the §5 mechanical notes, the §6 preconditions and both reflection questions got a visible response. There are 36 actionable points. 21 are applied and verified in the documents, 7 are partly applied, 5 are declined with a logged reason, 2 are deferred with an owner, and 1 (taking OQ-11 to the lecturer) is not addressed. Every change the memlog claims under "Feedback 4.x" is present in `prd.md`, `addendum.md` or Rule Set v1. I found no claimed change that's missing. But the new used-moped price wasn't carried through to FR-29 or the UJ-4 trace (F6).

Most of the problems are in the 2026-11-13 additions:
- The new checkpoint table contradicts the older "When to cut" paragraph (F1, high).
- The status line still says the tiers, dates and hosting are waiting for the team (F2).
- The tiers conflict with UJ-6, UJ-2, A-23 and three success metrics (F5).

Hosting was the other high-severity point. It was decided in the log, but OQ-14 still reads as an open question (F3). The new prices were applied unevenly. Fuel now has a figure that the worked examples say doesn't exist (F7). The new answer-key figures have only been checked by Claude's script, which bypasses the control the reflection itself names (F8).

**Remaining risk:** the tiers make the build order clear, but Core still holds 46 of 57 FRs. The PRD has also grown from about 24,800 to about 27,100 words. Bård's central concern, that the scope is larger than the cut plan can absorb, has been acknowledged and scheduled but not reduced. This is a deliberate team choice (memlog lines 105 and 164), but it puts most of the risk on the 1-3 Dec checkpoint. F1-F3, F5 and F7 are mostly text fixes. F8 needs a team member to recheck the figures in a spreadsheet.

**Status counts (36 actionable points):**
- Applied: 21
- Partly applied: 7
- Declined with logged reason: 5
- Deferred with owner: 2
- Not addressed: 1

Two positive observations were rechecked separately and still hold.

**Findings:** 1 high, 8 medium, 5 low.

## Coverage table

| Ref | Point | Status | Evidence / location |
|---|---|---|---|
| 4.1-a | Put the FRs into three tiers in a table | Applied | prd.md §5 FR overview, Tier column (lines 334-392); §4.4 "Tiers" (line 315). 46 Core, 8 Extension, 3 Can be cut. Memlog 164 |
| 4.1-b | Core = engine, month loop, events, endings, "Hvorfor?" | Applied | FR-12, FR-49, FR-13, FR-14, FR-17, FR-46, FR-38, FR-41, FR-42 are Core (lines 345-390) |
| 4.1-c | Extension = phone, month plan, job view, money view | Declined with logged reason | Memlog 164: FR-52 to FR-56 stay Core (team decision 2026-11-10, "These always stay", line 313). The money view's FR-57 went further than suggested and is Can be cut (line 364) |
| 4.1-d | Can be cut = the rest of §4.4, marked per FR | Partly applied | FR-30, FR-51, FR-57 and the partial cut items appear in the overview, but the login-hardening parts of cut item 11 aren't marked on FR-1, FR-3 or FR-5 (F4) |
| 4.1-e | Date: "core playable start to end" | Applied | §4.4 table line 324, "about 1-3 Dec 2026", tentative. See F1 |
| 4.1-f | Date: "extensions frozen" | Applied | §4.4 table line 323, "about 26-27 Nov 2026". See F1 |
| 4.1-g | §4.4: if core isn't playable by the date, Can be cut drops with no new discussion | Partly applied | Line 324 says this, but line 317 ("When to cut") gives a different rule for the same situation (F1) |
| 4.1-h / §6 | Tie the checkpoints to OQ-13 before UX, architecture and epics | Deferred with owner | OQ-13 (line 1453): Team, blocks sprint planning; tracked by #72 (duplicate #73). Dates are tentative until the delivery date is known |
| 4.2-a / §6 | Turn OQ-14 into a decision before architecture | Partly applied | Stack decided (memlog 155; addendum.md line 17). OQ-14 (line 1454) is still open, owned by Architecture, and blocks only the first playtest (F3) |
| 4.2-b | NFR-6: one command, local run | Applied | NFR-6 line 1313: "starts with one command and needs only Docker … no secrets" |
| 4.2-c | NFR-6: seeded users via the README | Applied | NFR-6 line 1315: test users seeded at three states |
| 4.2-d | NFR-6: if email isn't available locally, an automated test verifies reset | Applied | NFR-6 line 1313: local inbox or log, "If that fails, an automated test verifies password reset". Small wording issue (F3) |
| 4.2-e | Drop the self-hosted Supabase dependency from the local run | Applied | prd.md no longer mentions Supabase. NFR-3 line 1287 names "the database host". Superseded notes in addendum.md lines 17 and 270. Memlog 156 |
| 4.2-f | Consider moving login hardening (§4.4 item 11) out of V1 | Declined with logged reason | Memlog 157: stays as item 11 and is built if time allows. The logged reason is thin (F4) |
| 4.2-g | Reconcile NFR-5, NFR-10, NFR-11 (zero cost, EU, 7 days, 10 s) | Partly applied | NFR-5 becomes "Low cost" (line 1307) and NFR-11 drops to 3 days (line 1386). EU storage and the 10 s wake-up remain unverified in OQ-14 (F3). The side effect of the 3-day period is F14 |
| 4.3-a | FR overview at the top of §5 (ID, title, tier, UJ) | Applied | Lines 332-392, also with a Section column |
| 4.3-b | Split FR-9 into sub-requirements | Applied | FR-9a-c (lines 513-534) |
| 4.3-c | Split FR-32 into sub-requirements | Applied | FR-32a triggers, FR-32b steps and options, FR-32c ending (lines 1037-1059), matching Bård's example |
| 4.3-d | Split FR-46 into sub-requirements | Applied | FR-46a-c (lines 661-680) |
| 4.3-e | Restate a rule in one sentence where an FR uses it | Applied (alternative form, reason logged) | New §3.1 has one sentence per rule (lines 221-242). §0 points there (line 12), and FR-9a restates rule 13 (line 516). Memlog 158 explains why one table was chosen over about 80 inline copies |
| 4.3-f | FRs aren't in numeric order | Applied (mitigated) | Overview intro (line 332): "grouped by feature, so their numbers aren't in order". Not renumbered, which avoids churn. No memlog entry |
| §3 dim. | D1-D26 and F1-F10 are also outside the PRD | Partly applied | §3.1 covers rules 1-16 only. F1-F10 and D-numbers are still cited only by number (F11) |
| 4.4-a | Status: "final for UX and architecture; content figures provisional" | Partly applied | The wording is in the §0 status line (line 16), but the line is stale and contradicts the frontmatter `draft` (F2) |
| 4.4-b | Parameter table (parameter, default, source y/n, owner, deadline) | Applied | Rule Set v1 lines 17-64: Status (Sourced/Assumption/Tuning/Partly sourced/Missing), Owner and Deadline on every row. Owner is always "Team" (F12) |
| 4.4 follow-up | Replace placeholder values with sourced ones and recalculate the examples (team-initiated, memlog 160-168) | Partly applied | Example 19 (lines 156-166), example 20 goal 3 (line 168), example 21 text, example 22 (lines 189-199) and FR-9 updated. FR-29 and the UJ-4 trace were missed (F6). Fuel is ambiguous (F7). There's no human recheck (F8) |
| 4.5-a | Give the success metrics IDs | Applied | §7.1 SM-1 to SM-12 (lines 1400-1413), §7.2 CM-1 to CM-5 (lines 1427-1431) |
| 4.5-b | Name the FR/UJ each metric validates | Applied | Validates column, lines 1400-1413. Some targets are Extension or Can be cut FRs (F5) |
| 4.5-c | Address self-reporting ("can explain …") | Applied | Line 1416: written answers scored by two team members against a fixed rubric (SM-1, SM-3, SM-4). The rubric is tracked in #69 |
| §5 | FR-1 to FR-57 contiguous, references resolve (observation) | Still holds | 57 FR headings, 57 overview rows. Every OQ reference in prd.md resolves to a §8 row after OQ-6 was removed |
| §5 | UJ order 1, 2, 3, 6, 4, 5: renumber chronologically | Declined with logged reason | Memlog 159: stable IDs keep reviews, issues and logs matching. §2.3 note (line 67) |
| §5 | Assumptions such as A-26 should be in the PRD | Applied | §9 table (lines 1460-1466). Only A-26 was lifted. A-23 and A-30 also affect V1 (F5, F7) |
| §5 | Glossary consistent, named protagonist (observation) | Still holds | No new glossary drift found. The tier terms are defined in §4.4 |
| §6 | OQ-6: legal basis and data responsibility before the first test | Declined with logged reason | Memlog 167. OQ-6 removed, NFR-3 line 1294, §4.3 line 293, addendum.md line 201, #24. The residual inconsistency is F9 |
| §6 | Can wait: OQ-9, OQ-12, OQ-18, OQ-3, OQ-8, OQ-17, provided defaults exist | Deferred with owner | All are in §8 with owners. The defaults are in the parameter table. Issues #29, #43, #48, #50, #57 |
| §6 | Brief follow-up: no narrowing (lifespan 15-20 kept, login kept) | Declined with logged reason | Memlog 105 (full scope kept), 157 (login), 164 (tiers instead of cuts) |
| §6 | AI in the app: take OQ-11 directly to the lecturer | Not addressed | OQ-11 (line 1451) unchanged, "Team / Nothing". #39 open since 2026-11-05. No contact logged (F10) |
| §7 Q1 | Reflection: how the AI proposals were checked against existing FRs | Applied | refleksjon §1. Claims match memlog 125, 131, 132, 138 |
| §7 Q2 | Reflection: which of 42/46/37 were computed by whom | Applied | refleksjon §2. "About 42/46/37-38" by two lenses confirmed in review-2026-11-11.md line 33. The Tuning rows with an 8 Dec deadline are confirmed in Rule Set v1 lines 51-53. The FR-33 ≥50 check is at line 1079 |

## Memlog cross-check

Every "Feedback 4.x" change claimed in memlog lines 150-168 is in the documents:
- 3-day window: NFR-11, SM-6, the "Counted from records" bullet, the Dates line, OQ-14.
- NFR-3, NFR-5, NFR-6 and NFR-11 rewritten, with the addendum's superseded notes.
- FR overview, FR-9/32/46 splits, §3.1, and the §0 pointer.
- SM and CM IDs, and the rubric.
- Parameter-table columns and the new rows, rule 14, examples 19-22, FR-9 "all three goals", OQ-3 and OQ-17 narrowed.
- Tier column and Tiers paragraph, the dates table, OQ-13, §7.1 Dates, and the moved deadlines.
- A-26 in §9.
- OQ-6 closed: NFR-3, the FR-44 note, the §4.3 row, addendum line 201.

I spot-checked the arithmetic and found no errors:
- Example 19: 11,645 × 0.70 = NOK 8,152; the 27-month gift = NOK 7,715.
- Example 22a: the sale price of NOK 7,569 is right.
- Example 20, goal 3: 120,393 − 60,000 − about 576 in lost interest = NOK 59,817, and NOK 46,352 with expenses.

The only gaps are things the price change touched that the memlog doesn't claim to have changed: FR-29 and the UJ-4 trace (F6), and fuel (F7).

## Reflection document check

- **Promised: the FR-33 content check fails at 50 or more.** Present (line 1079).
- **Promised: weights and threshold are tuning values, reassessed after the playtest (OQ-8).** They're tuning values. Neither OQ-8 nor the parameter table says they're reassessed after the playtest, and the deadline column says "Playtest start" (F12).
- **Implied by "Hva vi lærte" and the human recheck in Q1/Q2.** The reflection credits a review of the whole PRD and a team member's spreadsheet recalculation with catching AI errors. Neither has been done for this round's changes (memlog 168: "Claude's script only; no independent check yet"; #67 still open). See F8.
- **Naming note:** "D1-D12" in the reflection are the review decisions from 2026-11-11, not Rule Set v1's disclosures D1-D26. A reader who knows the feedback's "D1-D26" may confuse them. It doesn't need a fix in the PRD.

## Findings

### F1 — §4.4 cut rules contradict each other
- **Severity:** high
- **Feedback:** 4.1-e, 4.1-f, 4.1-g
- **Location:** prd.md §4.4, lines 315, 317, 321-326
- **Problem:**
  - Line 317 is from 2026-11-11. It says that if the month loop isn't playable at the first checkpoint, "the first six items apply at once". The new table is from 2026-11-13. It makes "Extensions frozen" the first checkpoint, with the consequence that unstarted Extension FRs are left out. It ties the cut to the second checkpoint, core playable, and drops the whole Can be cut tier (all 11 items). That's two different rules for the same situation.
  - Line 315 says Extension "is built once the core is playable from start to end". But the extension freeze (about 26-27 Nov) comes before the core-playable checkpoint (about 1-3 Dec). Read together, no Extension FR can start unless the core is playable early. That may be intended, but the PRD doesn't say so.
  - Bård asked for a date that triggers the cut "without new discussion". "About 1-3 Dec" is a range, so someone still has to decide which day counts.
- **Suggested fix:**
  - Rewrite line 317 to refer to the table, or delete its example.
  - State the order outright, for example: "Extension work starts only if Core is playable before the freeze; otherwise the Extension tier is skipped." Or move core playable before the freeze.
  - Give each checkpoint one date and name who confirms it on the day.

### F2 — The status line is stale and contradicts itself
- **Severity:** medium
- **Feedback:** 4.4-a
- **Location:**
  - prd.md frontmatter (lines 3-4): `status: draft`, `updated: 2026-11-12`
  - prd.md §0 status line (line 16)
  - Rule Set v1 frontmatter: `updated: 2026-11-12`
  - .memlog.md frontmatter: `updated: 2026-11-12T14:34`
- **Problem:**
  - Line 16 says "the tiers and dates in §4.4 and the hosting questions wait for the team". The tiers and dates were written on 2026-11-13 (memlog 164-165), and the hosting stack was decided on 2026-11-12 (memlog 155).
  - The same paragraph says "Final on 2026-11-11, and UX and architecture can start", while the frontmatter says `draft`. A reader can't tell which status applies, which is the problem 4.4 raised, in a new form.
  - None of the `updated` dates were changed for the 2026-11-13 edits.
- **Suggested fix:** Replace the opening of the status line with one current sentence, for example "Draft, being revised after the PRD feedback (2026-11-12/13). When final: final for UX and architecture; content figures provisional (Rule Set v1 parameter table)." Keep the history in one short trailing sentence. Update the `updated` dates. Tracked by #67.

### F3 — Hosting is still an open question in the PRD
- **Severity:** medium
- **Feedback:** 4.2-a, 4.2-d, 4.2-g, §6
- **Location:** prd.md OQ-14 (line 1454), OQ-4 (line 1448), NFR-6 (line 1313), FR-3 (line 434); addendum.md line 17; memlog 155; issues #47, #68
- **Problem:**
  - Bård asked for OQ-14 to become a decision before architecture. The team chose the reference setup: its own login, Railway with Supabase Postgres (memlog 155). The team also changed NFR-5 to low cost, which removes the cost conflict.
  - The choice appears only in the memlog and in a superseded note in the addendum. OQ-14 still asks whether "the chosen host" (unnamed) meets NFR-5, NFR-10 and NFR-11. Memlog 155 also flagged that Railway hasn't been checked against EU/EEA storage, and the 10 s wake-up is unverified.
  - OQ-4 still asks how reset works "in the examiner's local run", which NFR-6 now answers.
  - #47 still asks for a "free" host.
  - In NFR-6, "If that fails, an automated test verifies password reset" doesn't say what "that" is. FR-3 says without condition that reset works in the local run.
- **Suggested fix:**
  - Reword OQ-14 as "Decided 2026-11-12: reference setup (`architecture/technology.md`). Open: confirm an EU/EEA region and a wake-up within NFR-10's 10 s, and name the fallback." Cite #68.
  - Narrow OQ-4 to the playtest relay and go-live.
  - Retitle or close #47.
  - In NFR-6, write "If the local inbox isn't available, the README points to the automated reset test instead", and align FR-3's local-run bullet with it.

### F4 — Building login in-house raised its cost, and the tier marks are incomplete
- **Severity:** medium
- **Feedback:** 4.1-d, 4.2-f, §3 (form fit)
- **Location:** prd.md §4.4 item 11 (line 311); overview rows FR-1, FR-3, FR-5, FR-44 (lines 336-341); FR-1 (line 411); FR-3 (line 431); FR-4 (line 444); NFR-3 (line 1288); memlog 155, 157
- **Problem:**
  - Item 11 cuts five things: per-network limits, the daily email cap, "stay logged in", **Log out on all devices**, and the 12-month deletion job. The overview marks only "stay logged in" on FR-5. FR-1 (sign-up limit per network) and FR-3 (daily cap) are plain Core, and so is FR-5's "all devices". Line 315 promises that the overview names every cut part.
  - Replacing Supabase Auth with the team's own bcrypt + JWT login means the team now builds what a managed service used to provide: rate limits, single-use expiring reset tokens, and revoking other sessions (FR-3, FR-4, FR-44, all Core).
  - Bård's point that login takes up too much of V1 has therefore grown. The logged reason for declining it ("the team builds it itself", memlog 157) supports his suggestion more than it answers it.
- **Suggested fix:**
  - Add the item-11 parts to the FR-1, FR-3 and FR-5 rows, and note NFR-3's deletion job.
  - Log why login stays Core even though the team builds it itself.
  - Consider making the addendum's fallback the Core minimum for FR-3 in the playtest: a one-time reset link the team makes for known testers (addendum.md line 275).

### F5 — The tiers conflict with the journeys, a confirmed assumption and the metrics
- **Severity:** medium
- **Feedback:** 4.1-a, 4.1-d, 4.5-b
- **Location:** prd.md UJ-6 (lines 106-122), UJ-2 (lines 79-90), UJ-4 (line 128); overview rows FR-16, FR-30, FR-40, FR-51, FR-57; §7.1 SM-2, SM-6, SM-9 (lines 1403-1410); addendum.md A-23 (line 566)
- **Problem:**
  - **UJ-6:** it depends on the car licence (FR-30), the pinned savings target and the bank's "three quarters" message (FR-57), and the grouped ending line (cut item 2). All of these are Can be cut. If that tier drops on 1-3 Dec, UJ-6's context, climax and resolution disappear.
  - **UJ-2:** its recap (FR-16) is Extension, and its driving game (FR-51) is Can be cut.
  - **UJ-4:** it starts from a gift moped, which is cut item 9.
  - **A-23:** it confirms that disclosed simplifications "are a requirement", but FR-40 is Extension.
  - **Metrics:** SM-2 validates FR-19 and FR-40 (both Extension), SM-6 validates FR-16, and SM-9 validates FR-57.
  - The epics will be built from the tier column, so these conflicts bring back the ambiguity about what has to be done first.
- **Suggested fix:**
  - Move FR-40 (and possibly FR-16) to Core, or amend A-23.
  - Add one line per affected journey, such as "With the Can be cut tier dropped, Markus saves for the moped licence instead", or a sentence in §4.4 saying that the journeys show the full scope.
  - Make sure each SM row validates at least one Core FR, or mark which metrics fall away.

### F6 — FR-29 and the UJ-4 trace still use the old used-moped price
- **Severity:** medium
- **Feedback:** 4.4 follow-up
- **Location:** prd.md FR-29 "Resale value" (line 994); addendum.md lines 48 and 65 ("UJ-4 month by month")
- **Problem:**
  - Rule 14 and example 19 now use NOK 11,645 for a used or gift moped.
  - **FR-29**, a testable consequence in the PRD body, still says "A used moped sold after two years fetches NOK 9,625 (worked example 19)". Example 19 now gives NOK 8,152 for that case, so a story written from FR-29 would assert the wrong number.
  - **The UJ-4 trace** still says Markus's gift moped sells for "about NOK 9,300 (rule 14, a gift moped owned about 26 months)". That figure is 13,750 × 0.675. With 11,645 it's NOK 7,860. The reasoning on line 48 uses the same old figure. Its conclusion still holds: the sale is less than he owes, so he keeps the moped.
  - Memlog 168 reports the recalculation as finished, but it covered examples 19-23. It missed FR-29, which cites example 19 directly, and the trace.
- **Suggested fix:**
  - FR-29: "fetches NOK 8,152 (worked example 19)".
  - Trace: "about NOK 7,900 (NOK 7,860)", and update line 48 to match.
  - Search all three documents for any other value derived from NOK 13,750.

### F7 — Fuel now has a figure, but the rules and examples say it has none
- **Severity:** medium
- **Feedback:** 4.4-b, 4.4 follow-up
- **Location:**
  - Rule Set v1: line 55 (fuel row), line 81 (rule 14), line 189 (example 22: "moped fuel has no figure yet"), line 201 (example 23), line 218 (example 25: "has no figure yet")
  - PRD addendum: line 50, and A-30 (line 573)
  - prd.md OQ-8 (line 1449), which treats car fuel as a tuning value
  - Memlog 144 and 162
- **Problem:**
  - The fuel row now gives moped NOK 186 a month in April-October and car NOK 991 a month, with status Assumption. Rule 14 charges moped fuel.
  - Examples 22, 23 and 25, the UJ-4 trace and A-30 still leave fuel out because it "has no figure", and memlog 144 says NOK 0 until OQ-3.
  - The moped service row (line 40) says outright that it isn't charged yet. The fuel row doesn't. A developer who follows the table and rule 14 would charge NOK 186 and break examples 22 and 23, which are the test answer key.
  - OQ-8 calls car fuel a tuning value, while the table calls it an Assumption.
- **Suggested fix:** Add "Not charged yet: the examples use NOK 0 until OQ-3 confirms the distances" to the fuel row, as on the moped service row. Reword "no figure yet" in the examples to "left out (NOK 0) until OQ-3". Alternatively, charge fuel and recompute examples 22, 23 and 25 and the UJ-4 trace. Make OQ-8's car-fuel item match.

### F8 — The new figures haven't been checked independently
- **Severity:** medium
- **Feedback:** §7 (reflection), 4.4 follow-up
- **Location:** memlog 162 and 168 ("Claude's script only; no independent check yet"); Rule Set v1 examples 19, 20, 21 (goal-3 text) and 22; refleksjon §1 points 2 and 4 and "Hva vi lærte"; #67
- **Problem:**
  - The reflection names two controls that caught AI errors last time: a review of the whole PRD, and a team member recalculating the figures.
  - This round changed the answer key: examples 19, 20 and 22 have new figures, and example 20 now reaches goal 3. Only a script has checked them, and no whole-PRD review has been run (#67 is open). No open issue asks for a human recheck; the earlier one, #55, is closed.
  - F6 and F7 are the kind of slip such a pass catches.
  - My own spot checks reproduced the figures (see the memlog cross-check), but that doesn't replace the team's control.
- **Suggested fix:** Before setting the PRD final, have a team member recheck examples 19, 20 and 22 in a spreadsheet, as was done for examples 25-28, and record it in the memlog. Then run the whole-PRD review under #67, not a review of the changes only.

### F9 — OQ-6 is closed without naming who is responsible for the playtest data
- **Severity:** medium
- **Feedback:** §6 (OQ-6)
- **Location:** prd.md NFR-3 (lines 1280, 1292, 1294), §4.3 (line 293); addendum.md lines 201 and 414; memlog 167; #24
- **Problem:**
  - Bård listed the legal basis and the responsibility for playtest data as things to settle before the first test. The team closed OQ-6 as not needed for a school project. That's a logged decision.
  - NFR-3 itself says that email addresses, game data and network addresses are personal data, and the playtest collects them from real people. The PRD now names nobody as responsible for that data and gives no basis.
  - The statement that no approval is needed cites no source, such as the course rules, the lecturer or the institution.
  - Addendum line 414 still says "OQ-6 blocks the first playtest", without the "Superseded" mark the other rows in that table have.
- **Suggested fix:**
  - Add one sentence to NFR-3's playtest paragraph. It should say who holds the playtest data (for example, the team, within the course) and what basis the testers are told (for example, the adult testers' informed agreement, stated in the player information).
  - Record who confirmed that no further approval is needed, and when.
  - Mark addendum line 414 as superseded by memlog 167.

### F10 — OQ-11 hasn't been taken to the lecturer
- **Severity:** low
- **Feedback:** §6 (AI in the app)
- **Location:** prd.md OQ-11 (line 1451), §9 A-26 (line 1466); #39 (open since 2026-11-05); memlog 108
- **Problem:**
  - Bård said his feedback can't answer whether a delivery with no AI meets the course requirements, and advised asking the lecturer directly. Nothing in this round records that.
  - OQ-11 is still "Team / Nothing" and #39 hasn't changed.
  - The addendum (line 414) notes that architecture and epics change if the course requires AI in the app.
  - This doesn't block finalizing the PRD, but the answer costs least before the architecture run.
- **Suggested fix:** Ask the lecturer before the architecture run and record the answer and date in OQ-11 and #39. Otherwise, log a decision not to ask.

### F11 — D1-D26 and F1-F10 are still only outside the PRD
- **Severity:** low
- **Feedback:** §3 (usefulness for the next phase), 4.3
- **Location:** prd.md glossary (line 170), §7.3 (lines 1433-1439)
- **Problem:** §3.1 fixes the "rule N" problem. The same row in the feedback also named D1-D26 and F1-F10. The PRD still cites them only by number (for example D2, D6, D10, D11, F4, F5, F9, F10). §7.3 lists only the changes to F1-F10.
- **Suggested fix:** Add a 10-row table to §7.3 with one line per F-criterion. The D-texts can stay as pointers, since they're player-facing copy.

### F12 — Parameter table: no accountable owner, and the deadline doesn't match the reflection
- **Severity:** low
- **Feedback:** 4.4-b; reflection Q2
- **Location:** Rule Set v1 lines 39-64; refleksjon lines 37 and 41; prd.md OQ-8 (line 1449)
- **Problem:**
  - All 23 rows without a source have "Team" as owner, which doesn't make anyone accountable. That's the point of the column.
  - The deadlines say "Feature freeze (about 26-27 Nov)", a term the PRD doesn't use. §4.4's "Extensions frozen" is about Extension work, not content figures.
  - The reflection says the weights and threshold are reassessed after the playtest, but the table says "Playtest start" and OQ-8 doesn't mention a revisit afterwards.
- **Suggested fix:** Name a person per row or per group of rows. Use the §4.4 checkpoint name in the deadline column. Add "revisit after playtest" to the Tuning rows or to OQ-8.

### F13 — Tracking hygiene
- **Severity:** low
- **Feedback:** 4.1-h, 4.2-a
- **Location:** issues #46, #47, #72, #73; prd.md §8 rows OQ-13 and OQ-14; addendum.md line 267
- **Problem:**
  - #72 and #73 are duplicates with the same title and body.
  - #46 (OQ-13 dates) is still open and says the playtest needs "at least 7 days", which is now 3.
  - #47 asks for a "free" host, although NFR-5 now allows a low cost.
  - The OQ-13 and OQ-14 rows cite no issue.
  - The reset-quota placeholder "[needs figure: … OQ-3, #43]" points to OQ-3, which no longer covers the email quota after it was narrowed.
- **Suggested fix:** Close #73 as a duplicate of #72, and close #46 as superseded. Retitle #47 to match OQ-14. Cite #72 and #68 in the OQ rows. Point the quota placeholder to OQ-4 and #30. This review didn't change any issues.

### F14 — The 3-day return window doesn't fit a 3-day test period
- **Severity:** low
- **Feedback:** 4.2-g (availability; the team's change in memlog 153)
- **Location:** prd.md NFR-11 (line 1386), §7.1 (lines 1415, 1421), §4.4 (line 325)
- **Problem:** SM-6 counts returns over each tester's first 3 days, and the test period is "at least 3 days" (§4.4 says "3 days"). A tester who starts on day 2 or 3 can't complete the window before the period ends unless it's extended. Memlog 153 already notes that a 3-day window says less about habit.
- **Suggested fix:** Have every tester start on day 1. Otherwise, set the period in NFR-11 and §4.4 to 3 days plus the time it takes all testers to start, for example 5 days.
