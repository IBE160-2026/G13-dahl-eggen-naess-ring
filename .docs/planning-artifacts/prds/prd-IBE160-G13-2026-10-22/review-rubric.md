# PRD Quality Review — LifeMode

Reviewed 2026-11-13: `prd.md` (frontmatter `status: draft`, `updated: 2026-11-12`, with content through the 2026-11-13 feedback round), its `addendum.md`, and Rule Set v1 in the brief addendum where the PRD cites it. `.memlog.md` was read so that logged decisions aren't flagged as oversights. Where I challenge a logged decision, I challenge its consequences, not the decision itself. This replaces the rubric review of 2026-11-11.

**What I checked by hand:** the figures in FR-21 (NOK 2,588), FR-22 (NOK 10,289; NOK 84), FR-25 (NOK 1,805), FR-27 (833 × 5 + 835), FR-39 (NOK 17,270), FR-47 (NOK 31,694; NOK 33,742), FR-48 (NOK 4,182 / 12,182), the FR-52 slot counts at 0, 10, 12, 25, 40 and 37.5 h, UJ-4 (NOK 188 of NOK 350), and UJ-6 (free time 72 gives 3 slots, NOK 604, 73.8% rising to 79.8%). All of them match the rules. One FR figure is stale (FR-29, below). I also checked ID continuity, cross-references and encoding by script.

## Overall verdict

This is a strong, unusually testable PRD. One protagonist carries six journeys, nearly every FR has numbered consequences tied to the worked-example answer key, and the glossary and IDs are clean enough for UX and architecture to extract from directly. The risk is in delivering it, not in defining it. The tier-and-date scheme added on 2026-11-13 (§4.4) contradicts itself, and as written it leaves the Extension tier unbuilt in the expected case. Meanwhile 46 of 57 FRs stay Core, and nothing says what happens if the core isn't playable before the 8 Dec playtest. A few stale figures, and architecture notes in the addendum that are only half superseded, should be cleaned up before the architecture run extracts them.

## Decision-readiness — adequate

Most decisions are stated as decisions, and the trade-offs are honest. FR-1 admits that sign-up reveals whether an address is in use, and the addendum gives the reason ("hiding it needs an email confirmation step before play, which the team ruled out"). The addendum's decision tables have "Why" and "Alternative rejected" columns (P1–P8, the 2026-11-11 fixes) and name what was given up: wages stay a system cause, so they "can't appear among the three choices the ending shows". The §8 table is genuinely open. Every question has an owner and a Blocks column, and none blocks UX. There are no `[NOTE FOR PM]` callouts, but the OQ table and the addendum do that job.

The weak points are in the newest material. The cut rules added to §4.4 on 2026-11-13 contradict each other. The status block at the top of §0 describes the document's history rather than its current state. One game-design question that matters for the thesis is filed as a UX detail.

### Findings

- **[high]** The §4.4 cut rules contradict each other, and on plan the Extension tier is never built (§4.4 "When to cut", checkpoint table, "Tiers").
  - The "When to cut" example says "if the month loop isn't playable from start to end at the first checkpoint, the first six items apply at once". The table's first checkpoint ("Extensions frozen", about 26-27 Nov) only leaves out "Extension FRs not started". The cut list is dropped only at the second checkpoint, as "the whole Can be cut tier", which also makes the 1–11 order meaningless.
  - "Extension is built once the core is playable from start to end", together with "Core playable ... about 1-3 Dec" and "Extensions frozen ... about 26-27 Nov", means no Extension FR can start unless the core is playable about five days early. In the planned case, all eight Extension FRs are dropped: avatar, recap, tips, consumer loans, visible opportunities, echo badges, disclosures, and change password.
  - The column heading "If it's missed" doesn't fit a freeze date.
  - Sprint planning will read these three rules three different ways.

  *Fix:* Keep one rule set and write it as a decision table. For each checkpoint, give the condition tested (for example "a seeded user plays month 1 to the ending") and the exact consequence. Then either move the Extension freeze to after the core-playable date, or state plainly that Extension is expected to be dropped and starts only if the core lands early. Delete the "first six items" example, or make it the rule. Say whether the 1–11 order still matters (for example items 1–6 at checkpoint 1 and items 7–11 at checkpoint 2).

- **[medium]** The status block reads as a changelog, and parts of it are stale (§0 "Status", frontmatter).
  - "Status: final for UX and architecture" sits next to frontmatter `status: draft`.
  - "the tiers and dates in §4.4 and the hosting questions wait for the team" is out of date. Tiers and dates were written in on 2026-11-13, and the team chose the reference hosting setup on 2026-11-12 (addendum "For the architecture").
  - "Final on 2026-11-11" is followed by "It was first final on 2026-11-09", and the frontmatter says `updated: 2026-11-12`.
  - A UX or architecture lead can't tell from the top of the document what is settled.

  *Fix:* Replace the paragraph with three lines:
  - the current status (for example "Final for UX and architecture as of 2026-11-13. Figures are provisional per the Rule Set v1 parameter table, and the §4.4 dates are tentative (OQ-13)")
  - what is still open downstream (OQ-4, OQ-13, OQ-14)
  - a pointer to `.memlog.md` for the history

  Set the frontmatter to match.

- **[medium]** Whether players see an option's wellbeing effect before choosing is a game-design decision filed as UX (OQ-9; FR-13; FR-33; FR-53).
  - FR-13 says "Every option states its wellbeing effect", and FR-33 says "Every event choice states its effect on stress and social life". Yet OQ-9 asks "whether an option's wellbeing effect is shown before the pick", with owner UX and "Blocks: Nothing".
  - FR-53 already shows activity effects at planning: "a planned activity shows its cost and its effects".
  - Showing effects up front pushes events towards the quiz with a visible right answer that FR-13 and NFR-8 rule out. Hiding them makes discovery the mechanism of the thesis in §1: "The player learns from what their own actions lead to".
  - The decision changes how events are written and what the event screen shows, so it isn't a detail for UX alone.

  *Fix:* The team decides this before UX designs the event screen, and FR-13 records it (shown before the pick: yes, no, or direction only). If "states" in FR-13 and FR-33 means a stored schema field, say "has a stored effect". Align FR-53 with the decision, or give the reason for the difference.

- **[low]** OQ-11 has no deadline and is marked "Blocks: Nothing" (§8 OQ-11).
  - Keeping the AI driver in V2 is a logged team decision, and the V2 seam in the addendum limits the rework.
  - Still, OQ-11 says "the lecturer's difficulty rating leaned partly on in-app AI", delivery is about five weeks away, and nothing says when the lecturer will be asked.

  *Fix:* Add a date by which the team asks the lecturer (before sprint planning) and record the answer in OQ-11. Name the smallest AI scope that would go in through "Ready for V2" if the answer is "AI required".

## Substance over theater — strong

There's very little furniture. Markus is the only persona, and every journey forces specific requirements: UJ-4 alone drives the kroner figures in FR-26, the warning in FR-31, partial family help in FR-27, and moped resale under rule 14. The survey findings in §2 become decisions, not decoration:
- 38% thinking ahead becomes SM-1.
- "BSU and credit" understood least becomes NFR-8's "Credit and BSU: these get more explanation".
- "Small purchases that add up" becomes FR-23's example purchases and FR-42's activity groups.

The NFRs have bounds specific to this product: NFR-10 sets 1 s, 3 s, and 10 s after sleep, NFR-2 sets 24 × 24 and 44 × 44 targets, and NFR-6 sets 15–20 minutes, with seeded users at named states. The Vision couldn't be swapped into another PRD: frikort, BSU, credit only from 18, the moped licence at 16. The differentiation claim is modest ("Built for Norway first and foremost"), and the competitor playtests in the addendum back it.

### Findings

- **[low]** The comparison with Koll på cashen has no measure (§1 "It feels like a game, not schoolwork"; §7.1).
  - §1 says the game should be "more rewarding and smoother to play than Koll på cashen".
  - No SM measures this. SM-7 compares the game with schoolwork, not with the competitor.

  *Fix:* Either add a survey item for testers who have played Koll på cashen, or recast the sentence as a design aim that the PRD doesn't claim to validate.

## Strategic coherence — strong

The thesis is stated, and the features follow from it:
- Players make expensive mistakes cheaply (§1).
- The game always shows why (FR-36, FR-38, FR-39, FR-42).
- Time is as limited as money (FR-47, FR-52, FR-53).

The four game areas added on 2026-11-10 are argued from the Vision ("Story events are the highlights, not the whole game") rather than tacked on. SM-1, SM-3 and SM-4 measure understanding through written explanations that two team members score against a fixed rubric, not through self-report. Five counter-metrics guard against tapping through, hooks without learning, and a month plan that adds screens without adding play (CM-4). The validity limit (all testers are 18-20) is stated openly. The MVP is clearly experience-first, built on a problem-solving spine.

The weak joints are where cuts meet the journeys, and in two metrics.

### Findings

- **[medium]** Cut items 1 and 8 remove the motivation behind UJ-6 and UJ-4 (§4.4 items 1 and 8; UJ-6; UJ-4; SM-4, SM-7, SM-9).
  - UJ-6 is "the only journey showing an ordinary month" (addendum, decision D2 of the 2026-11-11 fixes), and SM-4 and SM-7 validate against it.
  - Three parts of UJ-6 use FR-57, the first thing cut: his pinned target ("has pinned it as his savings target"), the bank message in step 1 ("passed three quarters of his savings target"), and the gift edge case.
  - UJ-4's setup ("at 18 he paid for it himself ... It emptied his savings") and the borrowed car both depend on FR-30, cut item 8.
  - If either cut happens, the journeys the playtest is checked against describe a game that wasn't built, and stories and test scripts written from them break.

  *Fix:* Add one line to each affected journey saying what replaces the thread if it's cut:
  - UJ-6 without FR-57: the bank message tracks goal-1 progress, which FR-55 already supports.
  - UJ-4 without FR-30: his savings went on the moped licence or a large event.

  Alternatively, take the savings-target pin out of item 1 and cut only upcoming costs and activity spend first.

- **[medium]** SM-6 can't separate a voluntary return from finishing the assigned playthrough (§7.1 SM-5, SM-6, "Counted from records").
  - A full game takes "about an hour" (NFR-6). SM-5 expects 70% of testers to finish within a 3-day window, and the written explanations come "after the last sitting".
  - Most testers who finish will need a second sitting, so "comes back voluntarily ... within 3 days" largely measures the completion they were asked for.
  - SM-6 is the only behavioural signal for the teaser-and-return loop (FR-15, FR-16, UJ-2).

  *Fix:* State what testers are told, for example "play at least the first in-game year; the rest is up to you". Count as a return only a sitting after the instructed part, or a replay after an ending. Report SM-5 and SM-6 against that instruction.

- **[medium]** The "careful player with some free time" check hasn't been run, although prices now exist, and its margin looks thin (FR-9b "With some free time"; worked example 20; OQ-17).
  - FR-9b still says "With the placeholder prices, the run is expected to need tuning once OQ-17 gives real prices". The starting catalogue from 2026-11-12 prices the cheapest paid basic activity (a café visit) at NOK 100.
  - My rough estimate from example 20, not a script run: NOK 100 a month for 60 months, plus the savings interest lost, comes to about NOK 6,400.
  - So the gated run without expenses lands near NOK 114,000 and passes.
  - The seeded runs with one NOK 2,500 expense a year (example 20: NOK 106,928) land near NOK 100,500, about NOK 500 above the goal-1 target. The random draws in seeded runs (expenses, family help) can flip that result.
  - If a careful player with one café visit a month misses goal 1, the game treats free time as wasted money. That works against NFR-8 ("Free time and activities are never framed as wasted money") and against the thesis that time is as limited as money.

  *Fix:* Run the second reference run and the seeded runs now with the catalogue prices, and record the figures in Rule Set v1 as a worked example. Replace the "expected to need tuning" sentence with the result and any tuning decision under OQ-8, before the 26-27 Nov freeze.

- **[low]** SM-2's target "Higher after" has no bound (§7.1 SM-2; CM-2, CM-3).
  - With 10-20 testers on a 5-question quiz, any rise passes, and CM-2 and CM-3 inherit the noise.

  *Fix:* Set a bound, for example a mean rise of one correct answer, or at least 60% of testers improving. Report the distribution, not just the mean.

## Done-ness clarity — strong

This is where story creation will lean hardest, and it holds up. Nearly every FR has "Consequences (testable)" with figures tied to the answer key (FR-20, FR-21, FR-22, FR-25, FR-26, FR-27, FR-31, FR-39, FR-47, FR-48). Content rules have pass/fail gates:
- FR-17's library minimums
- FR-33's check that the hollow win still holds
- FR-43's overlap check
- FR-46b's limit of one empty active month
- FR-55's invitation supply

NFR-7 lists 22 refusal cases and five non-refusals, each with its own test. Phrases like "gracefully" or "user-friendly" don't appear anywhere. One test figure is stale, and a few phrases will make a story writer stop and ask.

### Findings

- **[medium]** FR-29's resale test contradicts worked example 19 (FR-29 "Resale value").
  - FR-29 says: "A used moped sold after two years fetches NOK 9,625 (worked example 19)".
  - Since 2026-11-12, rule 14 and example 19 use a used price of NOK 11,645, which gives 11,645 × 0.70 = NOK 8,152. NOK 9,625 is the old 13,750 × 0.70.
  - A story written from FR-29 would assert the wrong number. The same staleness is in the addendum's UJ-4 trace (see Mechanical notes).

  *Fix:* Change FR-29 to "fetches NOK 8,152 (worked example 19)". Search both files for other figures derived from NOK 13,750.

- **[low]** The 2-minute target has two start points (FR-11; FR-1; SM-10; FR-50).
  - FR-11 says "within about 2 minutes of opening the game", and FR-1 protects "the 2-minute target in FR-11".
  - SM-10 measures "from creating the user", and FR-50 says "from creating the user ... so the time before that isn't included".

  *Fix:* Pick one start point. FR-50 can't see time before the account exists, so either measure from when the create-user screen loads, or restate FR-11's target as starting at user creation.

- **[low]** Three phrases a story writer will have to ask about (FR-9c; FR-40; §4.4 item 3).
  - FR-9c, "the lowest available money so far for the buffer goal": goal 2 counts only months 49-60, so a minimum taken from month 1 shows lows that don't count.
  - FR-40, "shown the first time ... behind an info icon or under 'Hvorfor?'": is the disclosure shown to the player, or only available behind an icon?
  - Cut item 3, "info messages, down to their minimum": FR-17 sets no minimum for info messages.

  *Fix:* Write "lowest available money at a month-end from month 49"; "shown once without being asked for, then kept behind the info icon"; and either set an info-message minimum or say there is none.

- **[low]** Some NFR wording is adjectives, not bounds (NFR-1; NFR-10).
  - NFR-1 asks for "text that is readable on a small screen" with no bound. NFR-2 bounds touch targets, but nothing bounds text size.
  - NFR-10's "mid-range phone on a throttled 4G connection" names no device class or throttle profile, so the 1 s and 3 s targets can't be reproduced.

  *Fix:* For example, "body text at least 16 CSS px, usable at 200% zoom (WCAG 1.4.4)", and "Chrome DevTools 'Slow 4G' profile on a named reference phone".

## Scope honesty — adequate

Omissions are explicit and well organized:
- §4.2 lists what never goes in version one.
- §4.3 lists what comes later or is left out, with a status and a reason for each ("Replay from a crossroads | Out. It needs earlier game states to be stored").
- §2.2 names the non-users.
- The ordered cut list states the fallback for each cut ("The licences are then a payment only, and D10 drops its sentence").
- Every FR has a tier.

All assumptions are confirmed and indexed (A-1 to A-30), and A-26, the one that changes what version one delivers, is repeated in §9. There are 12 open questions. That's reasonable for a PRD going to UX and architecture: none blocks UX, and two belong to architecture.

The gap is size. The tiers relabel the build rather than shrink it, and two significant pieces of work have no tier at all.

### Findings

- **[high]** Core is nearly the whole product, and nothing says what happens if it isn't playable before the playtest (§4.4 "Tiers"; FR overview; §7.1 "Dates").
  - 46 of 57 FRs are Core, 9 of them with a part that can be cut. 8 are Extension, and 3 are Can be cut.
  - Keeping the month plan, phone, and job view in Core was a logged team decision (2026-11-13), and a defensible one. The consequence is that if "Core playable ... about 1-3 Dec" is missed, the only response is to drop three FRs and some content, 5-7 days before an 8 Dec playtest.
  - According to the log, the build had no code on 2026-11-05 and an estimated 2-3-week build window.
  - The PRD doesn't say what the playtest does if a full life from 15 to 20 can't be played: a shorter life, testers starting from seeded states like NFR-6's, or a later playtest. SM-5 and SM-11 both depend on full playthroughs.

  *Fix:*
  - Add a "playable spine" checkpoint about a week earlier: the engine, month loop, events, money, endings, and "Hvorfor?" on seeded users, without login hardening.
  - Write down a playtest fallback: if the core misses 1-3 Dec, testers play from NFR-6-style seeded states (for example month 37 and month 55), and SM-5 and SM-11 are reported as not measured.
  - Mark which Core FRs could ship in a reduced form.

- **[medium]** Extension FRs have no fallback text, so Core FRs refer to features that may not exist (FR-25, FR-16, FR-19, FR-40, FR-37). Each cut-list item says what remains when it's cut, but the Extension FRs don't, and under the first Decision-readiness finding they're expected to be dropped. The dangling references:
  - **FR-25 (consumer loans):** FR-18's "Consumer loan ... Month 49" row, FR-55's "Offers always arrive", FR-48's "What stays open", FR-19's "consumer loan offer messages always carry a tip", FR-45's "pay off a consumer loan", the NFR-7 loan refusals, and FR-9a's "Borrowing never helps". F1 stays testable, because payment plans use rule 4.
  - **FR-16 (recap):** FR-28's "The recap's teaser names what the licence costs", and the climax of UJ-2.
  - **FR-19 (tips):** the card offer's required tip, which NFR-8 ("Credit and BSU: these get more explanation") leans on.
  - **FR-40 (disclosures):** A-23 ("The disclosed simplifications are a requirement"), cut item 7's change to D10, and FR-39's reference to D15.
  - **FR-37 (echo badges):** the glossary's "Boomerang pair ... comes a few months later with an echo badge".

  *Fix:* Add an "If left out:" line to each Extension FR. For example, for FR-25: "no consumer loan; the FR-18 row, the month-49 offer, the FR-45 payoff action and the NFR-7 loan refusals drop; rule 4 stays for payment plans and family loans". Given A-23 and NFR-8, reconsider whether FR-40 and FR-19's card-offer tip belong in Core.

- **[medium]** The content check is a major build item with no FR, tier, or owner (Glossary "Content check"; FR-9b, FR-17, FR-33, FR-43, FR-46b, FR-48, FR-52, FR-55; NFR-9).
  - It's a seeded playthrough simulator with its own run policies (careless, careful, reference, and 1,000 seeded playthroughs per the addendum).
  - It also covers schema validation for three content types, and roughly a dozen reports and fail gates spread over eight FRs, all run in CI.
  - It's missing from the FR overview and the tier scheme, so it will appear late as unplanned work.

  *Fix:* Give it its own FR, for example "FR-58 Content check". List every gate and report with the FR it comes from, and put it in the overview with a tier (gates as Core, reports as Extension) and an owner.

- **[low]** The PRD says the playtest "needs no approval" but gives no basis (NFR-3 "Scope of the privacy work"; §4.3).
  - This is a logged decision from 2026-11-13.
  - The playtest still processes real email addresses, and links game records to quiz and survey answers through a code key, which is pseudonymous personal data.

  *Fix:* Add one line saying who confirmed this and when (course staff or the institution's rules for student projects). If nobody has confirmed it, make it a team-owned OQ that blocks the playtest.

## Downstream usability — strong

The PRD is built for extraction:
- The glossary has 63 terms, used consistently (session vs sitting, active vs quiet month, choice vs real choice, story event vs highlight event).
- FR-1–FR-57, NFR-1–NFR-11, SM-1–SM-12 and CM-1–CM-5 are unique, and every reference resolves.
- The FR overview gives each FR's section, journeys, and tier.
- §3.1 sums up each rule in one line, so sections make sense without the brief addendum.
- FR-9, FR-32, and FR-46 are split into parts the size of a story.
- Every UJ has a named protagonist with context inline, and §2.3 explains the journey order.

The cost is length (about 27,000 words), which the overview offsets. Two things will mislead the next workflows.

### Findings

- **[medium]** The architecture handoff in the addendum is only half superseded (addendum "For the architecture", "Reset email routes").
  - The section opens with "Superseded 2026-11-12 ... Notes below about the Supabase login service, its limits, and its mail inbox no longer apply".
  - The bullets below still ask "which limits the login service gives out of the box" and "how a revoked login reaches the backend", still say "`architecture_technical_design.md` says no hosting provider is needed", and still say "The hosted Supabase free tier may pause idle projects (verify)".
  - "Reset email routes" still frames reset "within the hard constraint of zero ongoing cost", using the Supabase CLI inbox.
  - The architecture run is the very next reader, and it will pick up the bullets, not the banner.

  *Fix:* Rewrite the bullets for the reference setup: the backend's own Python login (bcrypt and JWT), Railway with Supabase Postgres, local stand-ins per NFR-6, and the low cost allowed by NFR-5. Delete the superseded text; git keeps it.

- **[low]** §3.1 misstates the rule 8 debt trigger (§3.1, row 8).
  - The row says "debt above 3× wage or NOK 5,000", which reads as whichever is lower.
  - FR-32 and rule 8 say the larger of the two, and debt there is net of the current account and savings.
  - §3.1 exists so readers don't have to open the brief addendum, so this is exactly where the misreading will happen.

  *Fix:* "net debt above the larger of 3× the 3-month average wage and NOK 5,000".

## Shape fit — strong

The shape is right. LifeMode is a consumer game with meaningful UX, graded, and the PRD sits at the top of the UX → architecture → stories chain. The structure led by journeys, with one protagonist, carries real weight. The level of rigor fits a deterministic engine that an examiner will test: worked examples, the refusal list, and the content gates.

The detail on accounts and login (FR-1–FR-5, FR-44) looked heavy next to a brief that proposed dropping login. Now that the team builds its own login (reference setup, 2026-11-12), specifying the limits and reset behaviour in the PRD is justified. Decision history lives in the addendum, so the PRD can stay declarative, which is a good split.

No findings.

## Mechanical notes

- **ID continuity:**
  - FR-1–FR-57 are contiguous and unique (57 headings), as are NFR-1–NFR-11, SM-1–SM-12, and CM-1–CM-5.
  - The journeys are UJ-1–UJ-6 in the order 1, 2, 3, 6, 4, 5. This is by age, explained in §2.3, and kept by decision.
  - The gaps in OQ numbers are explained in §8.
  - `prd.md` has no references to closed OQs; OQ-6 and OQ-19 appear only in the addendum's history.
  - Every FR, NFR, UJ, and OQ reference resolves.
  - Every worked-example reference (1–28, 17b, 21c, 26c, 26d) exists in Rule Set v1.
- **The tier column misses partial cuts.** §4.4 says "Where an FR is core but part of it is on the cut list, the overview says which part", but the column doesn't name these parts:
  - FR-1: the sign-up limit per network (item 11)
  - FR-3: the daily email cap (item 11)
  - FR-5: notes "stay logged in", but not **Log out on all devices** (item 11)
  - FR-38: the BSU comparison (item 4)
  - FR-23: borrowing the parents' car and car fuel (item 8)

  NFR-3's 12-month deletion job is also on item 11. NFRs have no tier column, and if the job is cut, NFR-3's "The player information says so" needs changing too.
- **One ID prefix, two meanings.** The addendum's 2026-11-11 decisions are numbered D1–D12, the same prefix as the disclosed simplifications D1–D26:
  - "D10" is both a decision (confirm, don't block) and the driving-game disclosure (§4.4 item 7).
  - "D11" is both a decision (the game areas come after §5.4) and a disclosure ("Disclosure D11 fires when the card opens").
  - "(D1, D2)" in "How UJ-6 differs" means decisions.

  Rename the decisions, for example to R1–R12.
- **Stale figures:**
  - FR-29's NOK 9,625 (see Done-ness clarity).
  - The addendum's UJ-4 trace says "about NOK 9,300 (rule 14, a gift moped owned about 26 months)". With the new price it's 11,645 × (1 − 0.15 × 26/12) ≈ NOK 7,860. The story still holds, because that's less than the NOK 10,000 he owes.
  - A-30 says moped fuel "is left out until it has a source". Rule Set v1 now has a fuel figure (NOK 186 a month, April-October, status Assumption), so say whether the examples still leave fuel out.
- **Dates and frontmatter:**
  - `prd.md` has `status: draft` and `updated: 2026-11-12`, while §4.4 says "set 2026-11-13".
  - The addendum has `updated: 2026-11-11` but contains entries from 2026-11-12 and 2026-11-13.
  - `.memlog.md` has `updated: 2026-11-12T14:34` but contains entries from 2026-11-13.
- **Cross-reference drift:**
  - §4.4 still says "checkpoints the team sets under OQ-13", but the checkpoints are now in the table, and OQ-13 asks only for the delivery date and a recheck.
  - The last row of the addendum's "Decisions from the final PRD check" ("OQ-6 blocks the first playtest, and OQ-11 is widened and blocks epics") isn't marked superseded, though both were reversed. Other rows in that table are marked.
- **Glossary drift:**
  - The deadlines in the Rule Set v1 parameter table say "Feature freeze (about 26-27 Nov)", while §4.4 says "Extensions frozen".
  - The tier names (Core, Extension, Can be cut) and "cut list" aren't in the Glossary.
- **Literal conflict:** FR-1 says creating a user "asks only for an email address and a password", while FR-5 adds the "stay logged in" box "when creating a user". They agree in intent, but a literal reading conflicts.
- **Assumptions Index roundtrip:** `prd.md` has no inline `[ASSUMPTION]` tags; they were removed on purpose once all assumptions were confirmed. §9 repeats A-26, and the addendum lists A-1–A-30, each pointing to a PRD location that exists. The roundtrip is OK.
- **Required sections and journeys:** all required sections are present for a chain-top consumer PRD, and every UJ names Markus with context inline.
- **Encoding:** both files are clean UTF-8, Norwegian characters and «» quotes are intact, and no mojibake was found.
