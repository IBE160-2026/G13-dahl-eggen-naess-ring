---
title: LifeMode PRD addendum
created: 2026-11-03
updated: 2026-11-13
---

# Addendum: LifeMode PRD

This addendum holds the detail downstream work needs and the reasons behind decisions in the PRD. If it disagrees with the PRD, the PRD applies, and a decision reaches downstream work only once it's in the PRD or Rule Set v1. The decision history runs oldest first, and where two sections conflict, the later one applies. Detail sections are kept current, so they carry no date. The full log is `.memlog.md`.

## Detail for downstream work

The first two sections list what the architecture and UX work need to pick up. The rest hold the detail they point to: the UJ-4 test trace, event scheduling, the three content schemas, the V2 seam, engine repeatability, the ending screen, and privacy. Login limits and reset routes are under "Login with email: decisions, limits, and reset routes" in Decision history.

### For the architecture

These items came out of the PRD review and belong in the next `bmad-architecture` run. The team follows the reference setup in `architecture/technology.md` (decided 2026-11-12): login built in the Python backend with bcrypt and its own JWT tokens, Docker Compose locally with Caddy and its own Postgres, Alembic migrations, a local stand-in for every external service whose key is missing (NFR-6), and Railway with Supabase Postgres for the hosted playtest. NFR-5 allows a low cost during the playtest.

- **Authentication:** the backend enforces every limit itself: email normalization, the sign-up and login limits per network and per address, the failed-login pause, and the reset-email caps (the limits table under "Login with email: decisions, limits, and reset routes"). Name the token lifetimes, how a password change or **Log out on all devices** revokes other sessions (FR-4, FR-5), and the chosen email relay and its quota.
- **Connectivity:** a state version per playthrough, a request ID for retries, browser visibility and online events, and the error format and codes.
- **Engine state:** storage for draws and the seed, content versions, the per-cause parts of each balance, and the card and account settings. The month plan (FR-52, FR-53), the month's messages (FR-55), the savings-target pin, and the bank thresholds already sent for it (FR-55, FR-57) also belong in the playthrough's state. Nothing about reading messages is stored (FR-54).
- **Hosting:** the playtest runs on Railway with Supabase Postgres (OQ-14). Confirm an EU/EEA region, a usable screen within 10 seconds after sleep (NFR-10), and the expected cost (NFR-5), and name the fallback if one of these fails. Nothing may keep costing money after the playtest.
- **Responsiveness:** a server budget of at most 300 ms to process and save one month, for 9 out of 10 requests, with the backend and database in the same region. A browser test with network throttling plays a scripted first session, and a Lighthouse mobile run checks the first screen before each playtest.
- **Mobile-first:** add NFR-1's supported browsers and test devices as the test matrix.
- **Game flow:** the two-part month and the state check on every request that changes the game (FR-49), and the open-option model (FR-48). Placing and removing activities are requests that name their month. The request to continue carries the version of the month plan the device showed, and is refused if the plan has changed since (FR-49). The planned activities are applied in the same request as continuing, before wellbeing is calculated.
- **Content and selection:** events, activities, and messages make up the content library (FR-17). Each type has its own schema and versions (NFR-4). One selection step uses the state and the seed to decide what arrives each month: the event and the messages. Name it as one unit (see "Ready for V2").
- **Minigames:** they run on the server like the rest of the game, one saved answer at a time (FR-51). A real-time game would need its own decision on how to check results, so it's left for V2.
- **V2:** generated content and its replay under FR-12 aren't designed, but leave room to store generated content with the playthrough, so that V2 needs less rework. See "Ready for V2: AI as game master".
- **Playtest:** the records in FR-50, the setting that keeps them off outside the playtest environment, test-user marking, and how they're exported.
- **Examiner:** seeding test users at the states NFR-6 names, and `.env.example`.
- **Other:** a scheduled deletion job, self-hosted fonts, and the accessibility check in CI.

### For UX

From the concept sketches:
- **Shift pay:** the concept's "+500 kr per extra activity slot" becomes the engine's figure from FR-47.
- **Estimated net:** the month plan's estimate covers activity costs only, not shifts (FR-52).
- **Transfers:** «Overføring til sparing» is shown as a transfer, not a cost. FR-42 counts it as zero.
- **Labels:** the PRD says "month plan", because rule 11 and D17 already use "calendar". What the screen is called, such as «Kalender», is UX's choice.
- **Event options:** an option shows no wellbeing effect before the pick; the result after the pick shows it, with "Hvorfor?" (FR-13). The 8 design concepts from 2026-11-12 drew wellbeing figures on the options, so this changes the event screen in whichever concept is chosen.

### UJ-4 month by month

This trace shows that the engine can reproduce UJ-4 under rules 1, 2, and 5. It's a set test state, not a scheduled playthrough: the city trip in month 40 is a drawn event, so a test sets it directly. Markus plans no activities in this trace. It reflects M13 (Markus keeps the moped), the spending level with costs on top, and the 3.5% card minimum, all decided on 2026-11-05. With a NOK 10,000 limit, a sale for about NOK 7,900 and six months of extra shifts can't both be true: the sale would cover most of the debt.

Entry state at month W, month 41 (May): age 18. His earlier bills were paid in full, including lunches and fuel. In month W−1, after that month's bill was paid, he put a NOK 10,000 city trip for everyone on the card at the event step. Card bill at the debt step: NOK 10,000. That's his limit, so the card takes no more purchases and his spending comes from the current account. Payment setting: the whole balance. NOK 1,000 in the current account and no savings. Wage 10 h a week, NOK 8,452. Mobile NOK 299, moped insurance NOK 250, and moped fuel NOK 186 in April-October (rule 14), so NOK 735 in months W to W+5 (May-October) and NOK 549 from W+6. Spending level: high. Tax is NOK 0 while his wages so far this year stay under NOK 99,650, which they pass in W+6. He also worked 10 h a week in months 37-40.

| Month | Wage | Costs | Spending | Free for the card | Bill | Interest | Paid | Card after | What happens |
|---|---|---|---|---|---|---|---|---|---|
| W | 8,452 | 735 | 8,029 (high) | 688 | 10,000 | 188 | 688 | 9,500 | Card warning shows, and Markus acts (see below) |
| W+1 | 10,142 | 735 | 7,607 (normal) | 1,800 | 9,500 | 179 | 1,800 | 7,879 | 12 h a week, well within rule 10 |
| W+2 | 10,142 | 735 | 7,607 | 1,800 | 7,879 | 148 | 1,800 | 6,227 | |
| W+3 | 10,142 | 735 | 7,607 | 1,800 | 6,227 | 117 | 1,800 | 4,544 | |
| W+4 | 10,142 | 735 | 7,607 | 1,800 | 4,544 | 86 | 1,800 | 2,830 | |
| W+5 | 10,142 | 735 | 7,607 | 1,800 | 2,830 | 53 | 1,800 | 1,083 | He sets 20 h a week and low spending from next month |
| W+6 | 16,903 | 549 | 8,608 (low) | 5,190 | 1,083 | 0 | 1,083 | 0 | Tax NOK 2,556 this month. Paid in full, no interest: back on track, with NOK 4,107 left |

In month W:
- Interest starts, so the card warning shows: NOK 188 this month, and 51 months and NOK 5,508 in total interest if he pays only the minimum.
- He talks to his mother, and the family draw gives no money.
- He turns the card off, asks for one extra 2-hour shift a week, and moves spending down to normal.
- He checks what the moped would sell for: about NOK 7,900 (NOK 7,860 under rule 14, for a gift moped owned about 26 months). That's less than he owes, and without it he'd pay for the bus. He keeps it.

He pays NOK 771 in interest in total, against NOK 5,508 at the minimum. Without moped fuel he would have been back on track in W+5, with NOK 682 in interest. W+1 is June, so the summer job is on offer, and he says no because he already has the extra hours. Taking it would pay NOK 33,547 in July and leave NOK 375 on the card, paid in full in August, with NOK 515 in interest in total. The trace shows the slower path, and a player can choose either. No crisis trigger fires. Worked example 17a in the brief addendum covers his wellbeing, and example 23 covers what he has to do after this to reach his goal.

### Event scheduling and library size

**Active months (P4):** months 1, 4, 7, and 10 of each in-game year (January, April, July, October). There are never more than two quiet months in a row. All four go to story events: the pengegave in month 1, then follow-ups and drawn events. Months 59-60 are quiet by default. A crisis, a card warning, or a pushed-out follow-up can still take them. Offers don't need an active month.

**Offer messages by year.** These arrive in their month (FR-55) and never take an active month.

| Year | Months | Offers |
|---|---|---|
| 1 | 1-12 | Month 3 part-time job |
| 2 | 13-24 | Month 13 moped licence, a gift moped as a drawn offer once the player has a licence, month 18 summer job |
| 3 | 25-36 | Month 30 summer job |
| 4 | 37-48 | Month 37 car licence result (one family message: the gift, or the option to pay for the licence), month 39 credit card, month 42 summer job, month 44 experience for goal 3 |
| 5 | 49-60 | Month 49 consumer loan, month 54 full-time job |

**Drawn offers.** The employer's extra shifts and the gift moped aren't tied to a month. Each has required and blocking flags and a chance per in-game year, set in configuration (see "Parameters" in the brief addendum). Each can be taken only in the month it arrives (FR-54, FR-55).

**Eligibility at draw time** covers `owns_moped`, `has_moped_licence`, `has_job`, and `has_car_licence`. The offers that must be guaranteed are in FR-55.

**Who gets a month:** the order in FR-46. An unexpected expense isn't in it, because it's a deduction with a system cause.

**Library size.** FR-17 sets the minimum at 40, twice the 20 active months, and targets 50-60. Only the pengegave event is fixed in every playthrough. The other 19 active months go to follow-ups and drawn events, so the expected number of events two playthroughs share is 1 + 19² / (N − 1):

| Library N | Shared on average | Share of 20 |
|---|---|---|
| 30 | 13.4 | 67% |
| 40 | 10.3 | 51% |
| 50 | 8.4 | 42% |
| 60 | 7.1 | 36% |

Goal 3's experience is an offer, so it doesn't add to the overlap. For the overlap before offers became messages, see P4.

Flag gating raises overlap and different choices lower it, so the seeded content check, not this table, is the real test. The check runs 1,000 seeded playthroughs with random choices.

### Event schema

| Field | Content | Checked |
|---|---|---|
| id, version | Unique text ID, and a whole-number version (NFR-4) | ID unique; version rises on any change |
| type, trigger | Regular or crisis. A crisis event also names its rule 8 trigger | Every trigger is covered at each age where it can occur |
| mechanism | One or more from the fixed list | Names exist |
| age range | From and to, in years and months, within 15y0m-19y11m | From ≤ to |
| requires flags, blocks flags | Lists of flag names | Names exist in the flag list |
| sender | Optional: who the event comes from (friend, family, employer, bank), and the text of its copy in the phone. The copy isn't a separate message (FR-54) | Sender is from the fixed list |
| boomerang | None, or a pair ID and a role (opener or follow-up). The opener also has a delay range in months | Both halves exist; 2 ≤ min ≤ max ≤ 12; the follow-up requires a flag that an opener option sets |
| teaching point | One sentence | Not empty |
| LK20 code | One or more codes from the fixed list, or "none", because no core aim names tax or BSU | Codes exist |
| source | The parameter keys the event's figures use, or a citation for any other figure | Every amount traces to a parameter or a citation |
| options | 2-4 options. See "Option fields" below | See "Option fields" below |

**Option fields.** Each option has:
- its text
- a money effect and a monthly-cost effect
- a card-payable flag and a binding period
- effects on stress and social life
- flags set or cleared, and a short text for each flag that shows the player something opened or closed (FR-35)
- optionally a tip and an ending text

An option can also have a type with its own values:
- a job
- extra shifts (hours and months)
- a loan (allowed range and terms)
- a family loan (amount of at least NOK 500, over 2-12 months)
- an amount the player enters (allowed range)
- a minigame (which one, its situations and right answers, and the result for passing and for not passing, FR-51)

**What the content check enforces on options:** every option states its wellbeing effect; every regular event has an option with no cost; every crisis event includes an option to ask family and an option to ignore the crisis; values stay inside the limits above.

Unexpected expenses are a separate list, each with a kind, an amount, the flags it needs, and a source.

The offers in FR-18 are offer messages (below), so events have no `milestone` field (P4).

### Activity schema (FR-53)

| Field | Content | Checked |
|---|---|---|
| id, version | Unique text ID, and a whole-number version (NFR-4) | ID unique; version rises on any change |
| availability | Basic (always available) or invitation (only with an invitation message) | Every invitation activity has at least one invitation message |
| kind | From a fixed list, such as concerts, time with friends, rest, hobby, trips. FR-42 groups by it | Kind exists |
| mechanism | One from the fixed list, usually "everyday spending and free time", for the disclosure and the cause | Name exists |
| age range, requires flags, blocks flags | As for events | As for events |
| cost | NOK 0 or more, with a card-payable flag | Whole kroner; at least two basic activities cost NOK 0, need no flags, and cover ages 15-20 |
| effects | Stress and social life, each within ±10 | Inside the limits |
| source | A citation for the price | Every price above NOK 0 traces to a citation (OQ-17) |
| texts | Name and a short description, in Norwegian | Not empty; no alcohol or tobacco (NFR-8) |

### Message schema (FR-54, FR-55)

| Field | Content | Checked |
|---|---|---|
| id, version | Unique text ID, and a whole-number version | ID unique; version rises on any change |
| kind | Info, invitation, or offer. The phone's copy of the highlight event comes from the event's sender field (event schema), not from a message | Kind exists |
| sender | Friend, family, employer, or bank, with a fictional name | Sender is from the fixed list |
| links to | Info: nothing. Invitation: an activity. Offer: an open option (FR-48), extra shifts (FR-47), or a one-time gift (FR-29, FR-30) | The target exists. An invitation's activity covers the message's age range, and the message requires at least the activity's flags |
| when | Depends on the kind. See "When messages arrive" below | Every FR-18 row with an offer month has exactly one offer message |
| tip, teaching point, LK20 code | Optional. The credit card and consumer loan offers must have a tip and a teaching point (FR-19) | Present where required; LK20 codes exist |
| text | Norwegian. Any amount is a placeholder the engine fills in (NFR-4) | No typed-in amounts; no alcohol or tobacco (NFR-8) |

**When messages arrive:**
- **Offers:** the month in FR-18's offer-message column. The summer job message repeats in months 18, 30, and 42.
- **Drawn offers** (extra shifts, gift moped): see "Drawn offers" under "Event scheduling and library size".
- **Invitations:** an age range and flags, repeatable, at most once each per in-game year.
- **Info:** an age range and flags, one-off or repeatable.
- **Bank messages:** when progress towards the savings target or goal 1 passes 25, 50, 75, or 100%, once per threshold and target.

### Ready for V2: AI as game master

The team wants AI to act as the game engine where possible in V2, and not in the MVP. The MVP keeps that cheap to add later, without building anything for it:

1. **One schema per content type, whoever writes it.** Events, activities, and messages have one schema each, checked by the content check. In V2, AI-written content goes through the same schema and the same check before a player sees it (brief addendum, AI safety principle 1).
2. **One selection step.** "What happens to this player this month" (FR-46, FR-55) is one step that takes the state and the seed and returns what arrives. In V2 the AI can propose what arrives, and the engine still checks eligibility (age, flags, rule 10, affordability) and stores the result.
3. **The engine decides every amount.** Prices and effects come from configuration, or are checked against the schema's limits. AI never sets an amount (NFR-4, rule 8 "the engine, not the AI"). The brief's research on LLM game masters supports this split.
4. **Stored, not regenerated.** Whatever arrives is stored with the playthrough (FR-12), so a reload or replay never asks the AI again. Generated content needs its own storage in V2, because library versions (NFR-4) don't cover it.
5. **A fallback to the library.** If generation or moderation fails, the selection step falls back to pre-written content (F5, in V2).
6. **No free text from the player.** Not in the MVP. In V2, only after a separate decision (brief addendum, AI safety principle 2).

### How the engine keeps results repeatable and traceable

**Random draws.** One seed per playthrough. Each draw is derived from the seed, the month, and what is drawn (for example "family help, event E-41"), so it doesn't depend on the order of requests. Engine tests can set the seed or force a result. The player can still reroll the pengegave by starting over, and a NOK 30,000 pengegave, if kept, is enough for goal 1 with only summer jobs and low spending (worked example 21f). That's accepted: keeping it is a good choice, every goal is reachable from NOK 10,000, and the game has no score to compete on. Rerolling the car licence gift means replaying three in-game years.

**Content versions.** Each playthrough keeps the versions it started with (NFR-4). Old versions are kept while any playthrough uses them. Engine code fixes apply to all playthroughs, and the worked examples guard them.

**Cause link shares.** Interest on a balance is shared in proportion to each choice's part at the start of the month. Payments and withdrawals reduce every part in proportion. Rounding uses largest remainder, with ties to the earliest cause. Example: a card balance of NOK 6,000 is a city trip (NOK 4,000) and a jacket (NOK 2,000). The month's interest is NOK 113. The shares are 75.33 and 37.67, which round down to 75 and 37 (NOK 112), and the remaining krone goes to the largest remainder: trip NOK 75, jacket NOK 38.

### The ending screen

**Texts.** To keep authoring small, ending texts are written per mechanism and sign (positive or negative effect), about 18 texts, plus pre-written texts for system causes. An option can override with its own ending text. Wages stay a system cause, so job and hours choices have no linked kroner and can't appear among the three choices the ending shows. That's an accepted trade-off: wages are the game's largest money flow, and linking them would crowd out the choices the summary is meant to show.

**"If you had chosen differently."** The line types, in order, are debt cost, money kept, and a pre-written fallback (FR-39). The comparison needs no authoring field. Re-running the playthrough with one choice swapped was rejected, because later events diverge and the result is hard to explain or test. The "everything else equal" assumption has its own disclosure (D15).

### Privacy measures in the MVP

**Privacy review (was OQ-6, #24):** closed for the school project on 2026-11-13. Who the controller is, the legal basis, and the full privacy text are settled only if the game is developed further (PRD §4.3).

**Player information covers:** what is stored (email, password as a hash, game data); what for (login, recovery, saving the game); how long; how to delete it; which services handle the data (the database host and any email relay); that there's no marketing, no other sharing, and no AI; who to contact; and who the game is for (15-20).

**Deleting inactive accounts:** 12 months covers a whole school year and a summer, far longer than a five-session playthrough needs. No warning email is sent, so the address is used only for login and recovery.

**Keeping only one life (X9, FR-43).** Deleting ended lives is the simplest privacy answer and keeps minors' data small.

**No age statement.** "I am 15 or older" stores and proves nothing. The brief addendum advises against consent as the legal basis, so the consent age doesn't apply, and the statement would turn away 14-year-olds in 10th grade or teach them to tick it falsely. Revisit if the privacy review (#24) is reopened and chooses consent (PRD §4.3).

**Playtest data.** Game metrics are counted per account in the playtest environment. NFR-3 sets the export and the code key (the list that links each tester's email address to their tester code). No email addresses leave the system, and one team member keeps the key if game data is linked to survey answers. Until the key is deleted the results are pseudonymous, and after that anonymous.

## Changes from the proposal

The examiner's guide requires anything left out or changed from the approved proposal to be described and justified. The proposal isn't in the repo, so this table is incomplete (OQ-15). Rows marked *to check* are decisions that may or may not differ from the proposal.

| Change | Why |
|---|---|
| AI-generated events moved to V2, so the MVP has no AI. F5 moves with them | Team decision, logged on 2026-11-03. The lecturer's feedback of 2026-10-06 advised building the engine and the event library first, so the game works with no AI, and rated in-app AI among the hardest parts. Whether this meets the course requirements is OQ-11 |
| *To check:* login with an email address and a password, with no username | Password recovery needs an address, and a username would be a second identifier to protect (NFR-3) |
| *To check:* the car licence is in the MVP | Added from UJ-4 on 2026-11-04, so Markus has a reason to borrow the parents' car in the card story (FR-30) |
| *To check:* minigames for the licences | Decided on 2026-11-05, so the player sometimes uses skill, not only choices (FR-51) |
| *To check:* no tobacco or alcohol choices | Content suitable for a 15-year-old, and the marketing rules for minors (NFR-8, research of 2026-11-04) |
| *To check:* no student loan | Education is a later life area (PRD §4.3) |
| *To check:* four game areas: the month plan, the phone, the job view, and the money view | Team decision of 2026-11-10: more game, less quiz |

## Decision history

Most topics run through several dated sections, and the latest one applies. This table lists each topic's sections, oldest first, and where the topic stands now.

| Topic | Sections, oldest first | Where it stands now |
|---|---|---|
| Ending wellbeing and activity effects | "Decisions from the PRD review" (G5) → "Decisions from the final PRD check" → "Decisions from the independent review" → "Four game areas: more game, less quiz (2026-11-10)" (OQ-19) → "Finalize (2026-11-11)" | The ending uses months 19-60 (rule 12, FR-33). An activity's effect counts in its own month only (rule 12, FR-33, D26) |
| Spending level | "Decisions from the final PRD check" → "Decisions from the independent review" → "Example purchases in the month summary" → "Finalize (2026-11-11)" | A share of the wage after tax, with costs on top, that can't take the account below zero or draw on savings. Low is 60% (rule 16, FR-23) |
| Goal 2 buffer | "Decisions from the PRD review" (G4) → "Decisions from the final PRD check" → "Decisions from the independent review" | NOK 30,000 of available money at the end of each of months 49-60, and no debt at 20 (rule 13, FR-9) |
| Goal 3 and the experience months | "Decisions from the PRD review" (G4) → "Decisions from the final PRD check" → "Decisions from the independent review" → "Four game areas: more game, less quiz (2026-11-10)" (P4) | One offer message in month 44, then open in the money view. The purchase must be made by the end of month 56 (rule 13, FR-9, FR-18) |
| Moped: owning, gift, and resale | "UJ-1 and UJ-2: progression, sessions, and the moped licence" → "UJ-4: card warning, family help, moped, and car licence" → "Team decisions on Dahl's proposals" → "Decisions from the PRD review" (M13) | Owning one is a choice (FR-29), and the gift moped is a drawn offer once the player has a licence ("Event scheduling and library size"). Resale value drops with the time owned (rule 14). In UJ-4, Markus keeps his moped (M13) |
| Car licence | "UJ-4: card warning, family help, moped, and car licence" → "Team decisions on Dahl's proposals" → "Decisions from the independent review" → "Review fixes (2026-11-11)" (R1, R3) | The gift is random, and a player without it can pay (FR-30). The result arrives as one family message in month 37. Car fuel is a cost the player starts or stops (FR-23). In UJ-4, Markus paid for the licence himself (R1) |
| Minigames and the driving game | "UJ-1 and UJ-2: progression, sessions, and the moped licence" → "Minigames" → "Decisions from the independent review" | Turn-based and judged by the server (FR-51). It's on the cut list, with "payment only" as the fallback. A real-time game can come in V2 |
| Login and reset | "Login with email: decisions, limits, and reset routes" → "Team decisions on Dahl's proposals" → "Decisions from the PRD review" (K3) | Email and password (FR-1 to FR-5), and account deletion with the current password (FR-44). The default limits and reset routes stay in "Login with email: decisions, limits, and reset routes". The email relay is still open (OQ-4) |
| AI and V2 (OQ-11) | "Changes from the proposal" → "Decisions from the final PRD check" → "Decisions from the independent review" → "Four game areas: more game, less quiz (2026-11-10)" (P8) | No AI in the MVP, and OQ-11 blocks nothing (PRD §8). The V2 seam is in "Ready for V2: AI as game master" |
| Privacy (OQ-6, #24) | "Login with email: decisions, limits, and reset routes" → "Team decisions on Dahl's proposals" → "Decisions from the PRD review" (K9) → "Decisions from the final PRD check" | Closed for the school project on 2026-11-13 (PRD §4.3). The MVP's measures are in "Privacy measures in the MVP" |
| Offers and active months | "Decisions from the PRD review" (X3) → "Decisions from the final PRD check" → "Four game areas: more game, less quiz (2026-11-10)" (P4) → "Review fixes (2026-11-11)" (R3, R4) → "Finalize (2026-11-11)" | Offers arrive as messages and never take an active month. Active months are 1, 4, 7, and 10 of each in-game year, and the event minimum is 40 ("Event scheduling and library size") |

### Competitor playtests

As reported on 2026-11-03, everyone on the team has tried both products. This replaces the note in `research/playtest-competitors-2026-10-31/notes.md` that only one member had played Koll på cashen and that PersonalFinanceLab had not been tried. The team's verdict:

| Product | Team verdict | What LifeMode does instead |
|---|---|---|
| Koll på cashen | Not very rewarding, heavy and slow | More entertaining and smoother to play |
| PersonalFinanceLab | Professional, but not made for the Norwegian market, geared towards a teacher-led experience, and it costs money | Made for Norway first and foremost |

### UJ-1 and UJ-2: progression, sessions, and the moped licence

Decided on 2026-11-03 from UJ-1. These features come from the team's journey and weren't in the brief. They are the team's first concrete answer to "more entertaining". Scoped small because delivery is about five weeks away.

| Feature | Decision | Why |
|---|---|---|
| End-of-session teaser | In | Cheap, and supports the target of 50% coming back |
| Room and belongings that change with choices | In, small: one room with a handful of states | Makes consequences visible without much art |
| Developing the avatar and home | Later | Beyond the room states, it needs a lot of art and content |
| Visible future opportunities | In, simple: show what a choice opened or closed | Can use the flags already in the event schema |
| Unlocks | In, by in-game age only | Progress-based unlocks can come later |
| New areas to unlock | Later | A whole new layer of content |

**Sessions:** one session is one in-game year, and nothing locks the player out in real time. 20-30 choices over five years gives about 4-6 choices a year, which fits a 10-15 minute session. Waiting in real time would work against the target of 70% finishing the game.

**Moped licence:** when the player chooses to take it, they pay for driving lessons, mandatory lessons and the licence itself, at real prices from sources such as Statens vegvesen, driving schools, and SSB. The recap's teaser names the cost, so no new screen is needed. It's a payment only, with no exam or driving mechanics. Owning a moped and the car licence were added from UJ-4; see "UJ-4: card warning, family help, moped, and car licence". *Superseded 2026-11-05 (Minigames): a minigame replaced "payment only" (FR-51).*

### Login with email: decisions, limits, and reset routes

Decided on 2026-11-03. This replaces the earlier decision on username, no email and no reset. Updated to match on 2026-11-03: brief (Scope In #9, Constraints), brief addendum (Privacy, Login secret), architecture (Database and Data Model, Authentication and authorization), and issue #24. The sign-up decision, default limits, and reset routes came from review proposals K1-K4 on 2026-11-05.

What this changes for the build:
- **Internal address plan:** the plan to build a fake address from the username (`@lifemode.invalid`) is no longer needed.
- **Playtests:** playtesters aged 18-20 will now give a real email address, while the brief says no contact details are stored with results, so email addresses and results have to be kept apart. See "Playtest data" under "Privacy measures in the MVP".

**Sign-up shows whether an address has a user.** Accepted: hiding it needs an email confirmation step before play, which the team ruled out on 2026-11-03. The sign-up limit stops bulk checks, and the owner can take back an address someone else registered by resetting the password and deleting the account. FR-2 and FR-3 still don't reveal it. Revisit if the privacy review (#24) is reopened (PRD §4.3).

**Same typo in both email fields.** It isn't caught: the player can play, but can't reset the password.

**Default limits (all configuration).** FR-1, FR-2, FR-3, and FR-5 state the defaults players see. If this table differs from them, the PRD applies.

| Limit | Default | Why |
|---|---|---|
| Sign-up attempts per network | 60 an hour | A class of 30 with one retry each fits |
| Password length | At least 8 characters; the maximum allowed is at least 64 | A 12-15-character minimum would slow sign-up for a 15-year-old |
| Failed logins per address | 10 in 15 minutes, then a 15-minute pause | Stops guessing, and the message stays neutral |
| Login attempts per network | 300 an hour | A class of 30 at three attempts each isn't blocked |
| Reset emails | 1 per address a minute and 5 a day; total per day at most 80% of the relay's daily quota | One script can't use up the quota and block recovery [needs figure: the chosen relay's quota, OQ-4, #30] |
| Reset link | 60 minutes, and a new link cancels older ones | |
| Login without "stay logged in" | Until the browser closes, or 30 minutes with no activity | Shared school PCs |
| Login with "stay logged in" | Until logout, or 30 days without play | The box is unticked by default, which suits shared school PCs. The cost is that a phone player logs in again more often, which could lower the return rate. Check this in the playtest |

**Reset email routes (OQ-4, #30).** Password reset has to send email at NFR-5's low cost, and it has to work in the examiner's Docker run without the team's cloud account or keys (NFR-6).
- **Examiner's local run:** with no email key, the backend's local stand-in puts reset emails in a local inbox or in the log, and the README says where (NFR-6). If no local inbox is available, the README points to the automated reset test.
- **Hosted playtest:** an email relay whose quota covers 10-20 testers plus the limits above. The architecture names the relay and its cost.
- **Fallback if the relay fails:** a tester who asks in person gets a one-time reset link that the team creates from the backend. This works for 10-20 testers the team knows, but not for go-live.

### Interest after a long break: left out of the MVP

The team suggested positive or negative interest after an extremely long break. Decided on 2026-11-03 to leave it out, and the game stays exactly as the player left it. There are three reasons. Credit only starts at 18, so a younger player would mostly get free money for staying away. An older player in debt would be punished for coming back. And the game's clock runs in game months with fixed rates.

### Saving and interest in UJ-3

Decided on 2026-11-03.

**Funds stay out of the MVP.** The team's narrative said funds or savings, but the team ruled out investing on 2026-10-31, and funds need returns that go up and down, which the engine doesn't have. Many survey respondents asked about funds, so they're a candidate for later.

**The game shows the real interest, even when it's small.** First-year interest under rules 1-2:

| Saved | Savings account (2.87%) | BSU (5.61%) |
|---|---|---|
| NOK 2,000 | NOK 60 | NOK 116 |
| NOK 3,000 | NOK 84 | NOK 172 |
| NOK 5,000 | NOK 144 | NOK 287 |

Interest alone won't pay for a moped, so the UJ-3 moment rests on two things: the surprise that money earned money without the player doing anything, and a pointer to other income. A summer job at 16 pays NOK 16,728 (worked example 1).

**BSU comparison:** "Hvorfor?" can also show what the same money would earn in BSU. This counts as an "if you had chosen differently" line, which is on the cut list (PRD §4.4, the in-play lines), and the moment works without it.

### Tips from the game

Decided on 2026-11-03. Some events carry a short, general, pre-written tip that the player is free to ignore. A tip is about the situation in the game and isn't personal advice, which the brief rules out. It should sound like a tip rather than a lecture.

### UJ-4: card warning, family help, moped, and car licence

Decided on 2026-11-04.

**A warning comes before a crisis.** A first card for ages 18-20 usually has a limit of NOK 5,000-10,000, and 10 hours a week at NOK 195.04 pays NOK 8,452 a month, so a new card rarely pushes debt above 3× income on its own. Instead, the game warns the player once a card bill isn't paid in full and interest starts, and the player decides whether to act. With a NOK 10,000 limit, the 3× income trigger is out of reach on a 10-hour wage (3 × NOK 8,452 = NOK 25,356), so in UJ-4 only the missed minimum can start a crisis. *Superseded 2026-11-05 (M4): the trigger now uses net debt and wages, with a NOK 5,000 floor. The UJ-4 result holds (see "UJ-4 month by month").*

**What the card costs.** The small cost in worked example 4 comes from the small amount, not the rate: 22.6% a year is a normal card rate (SSB; the market's effective rates run from 20% to 30%). At a small balance, the NOK 300 minimum pays the debt off quickly. Interest is charged every month, so the game shows both this month's interest and the total cost of paying only the minimum. Under rule 5:

| Card debt | Interest in month 1 | Months to pay off at the minimum | Total interest |
|---|---|---|---|
| NOK 3,200 (worked example 4) | NOK 60 | 13 | NOK 406 |
| NOK 8,400 (about one month's wage) | NOK 158 | 41 | NOK 3,645 |
| NOK 10,000 (top of a typical first limit) | NOK 188 | 51 | NOK 5,508 |

UJ-4 shows the cost for the player's own balance. The figures use the 3.5% minimum in rule 5 (decided on 2026-11-05), with monthly interest rounded under rule 2. Compared with 3%, it changes the figures only for balances above about NOK 8,600, where 3.5% is more than NOK 300. At 3%, NOK 10,000 took 53 months.

**Family help.** Family can give or lend money, but mostly as a loan that has to be paid back, so the player learns from it. It's not always on offer: in the survey, 36% had an unexpected expense that was hard to pay, and about half of them got family help (17% of all respondents). So roughly half the time, the player has to find another way. Sometimes family can cover only part of the amount.

**Moped.** As first decided, the player has a moped from age 16, either bought or received as a gift. It costs fuel, repairs, and insurance, and the parents may pay part of the insurance. Its resale value drops with the time owned (rule 14), and tracking actual use comes later. Prices should follow the real market. In the MVP, the parents' share of the insurance is random. Once the AI game master is added, the gift offers and the parents' share can be based on real data. *Superseded 2026-11-05 (Team decisions on Dahl's proposals): owning a moped is a choice, with occasional gift offers (FR-29).*

**Car licence.** By 18 some players get a car licence as a gift from their parents. The gift is random, and a player without it can pay for the licence at a real price. With a licence, the player pays for fuel when borrowing the parents' car. This changes brief Scope Out #5, which listed the driving licence as a later step; the brief was updated on 2026-11-04. If the moped licence is in, the car licence is in too, so there's more to play.

**How to build it.** Accepted on 2026-11-04. Each addition reuses something the engine already has, so the only really new thing is an owned moped.

| Addition | Built as |
|---|---|
| Warning before a crisis | One extra check and one event. It's the core of UJ-4 and fits the LK20 aim on reflecting about credit cards |
| Fuel and insurance for the moped, fuel for the car | Transport costs, which the engine already has as fixed costs |
| Moped repairs | Unexpected expenses |
| Family loan | The existing loan rules at 0% interest |
| Moped resale value | Drops by a fixed share per year owned; tracking actual use comes later |
| Car licence as a gift | One event |
| The moped in the room | One of the room layers, so it's gone once it's sold |

If time runs short, cut in the order in PRD §4.4. The warning, the moped, and selling it stay, because UJ-4 depends on them.

### UJ-5: no student loan, Markus's goal, and the ending

Decided on 2026-11-04.

**No student loan in the MVP.** Markus takes a job after upper secondary school and saves towards a flat. A student loan would add complexity that doesn't pay off within a game that ends at 20:
- At NOK 15,488 a month (Lånekassen basislån 2026-27), his debt passes 3× a part-time wage within two months, which starts a crisis month. *Superseded 2026-11-05 (M4): written against the trigger as it stood on 2026-11-04; the debt trigger now uses net debt and wages, with a NOK 5,000 floor (FR-32).*
- It blocks the debt-free goal.
- A player could borrow the full amount and save it to reach a savings goal.
- Interest and repayment only start after studying, so the game would teach little from it.

**For the education step later:** the game has to make clear that a student loan while studying isn't bad, and isn't the same as credit card debt. It has no interest while studying, and repayment starts only after the degree.

**Markus's life goal.** He chose saving for something big in UJ-1, with a flat as the big thing. A 15-year-old picks what he wants rather than "debt-free", and choosing the flat means the card debt at 18 puts his goal at risk. In the second round he goes for saving for something big or for being debt-free with a buffer, and chases money at the cost of his wellbeing, which gives the hollow win.

**"If you had chosen differently" on the ending screen.** These lines stay for the three choices that mattered most, and only those three can be opened. The lines in "Hvorfor?" during play, including the BSU comparison, are on the cut list (PRD §4.4). See "The ending screen" for the line types.

**Comparing playthroughs: later.** For now the ending shows a summary of the playthrough and the tips. Comparing one playthrough with the next is a candidate for a later step.

### Team decisions on Dahl's proposals

Decided on 2026-11-05.

| Decision | Why | Now in |
|---|---|---|
| No tobacco or alcohol choices for now | Research found them probably allowed, with conditions, but their effect on young players is unknown and can't be tested in playtests with 18-20-year-olds | NFR-8 |
| Card minimum of 3.5%, min NOK 300 | Matches Bank Norwegian, and DNB also uses 3.5%. Cards with limits up to NOK 30,000 fall outside utlånsforskriften, so this is about realism | Rule 5 |
| The card minimum is calculated on the balance before the month's interest | Keeps the figures for NOK 10,000: a NOK 350 first payment, 51 months, and NOK 5,508 in interest. Calculating it after interest gives NOK 5,437 at 3.5% (#38) | Rule 5 |
| Account deletion in the game, with the current password and no undo | The game stores email addresses of players as young as 15, and the privacy review (#24) recommends it. Requiring the password stops someone else deleting the account on a shared PC | FR-44 |
| The player chooses to buy a moped, with occasional gift offers | A random draw between buying and a gift could make saving up pointless, which works against UJ-3 | FR-29 |
| The car licence gift is random, and a player without it can pay | Gives a large, real money choice at 18 | FR-30 |
| All family gifts stay | They are no longer on the cut list | PRD §4.4 |
| Family loans don't count towards the 3× income crisis trigger (now the debt trigger in FR-32) | A teenager with no income would otherwise go into crisis from any loan | FR-27 |
| A hollow win shows at least one choice that hurt wellbeing | A kroner ranking alone may not show why wellbeing ended up low | FR-42 |

### Minigames

Decided by the team, as Dahl reported on 2026-11-05 (`.memlog.md`). The game gets small minigames along the way, to make it more fun. Not all of them are defined yet. The example so far is the licence: to take it, the player plays a game where they drive a route and have to follow some rules.

This replaces "the licence is a payment only, with no exam or driving" from 2026-11-03. See FR-28, FR-30, and D10. A minigame is the first thing in the game the player does with skill rather than by choosing, and it runs on the device, so FR-51 sets how its result reaches the engine. Dahl added on 2026-11-05 that the team sees minigames along the lines of the driving test for the licence, so the MVP's minigames are for the licences. *Superseded 2026-11-05 (independent review): the driving game is turn-based and judged by the server (FR-51).*

### Decisions from the PRD review

Proposed by Dahl on 2026-11-05 and accepted by the team, as Dahl reported the same day (`.memlog.md`). The review is `review-2026-11-05.md`, and the full reasoning and alternatives are in `review-2026-11-05-solutions.md`. Dahl chose M4, M5, M6, M8, M12, M13, and G1 one at a time, and accepted the recommendations for the rest.

This table lists the 16 proposals that needed a team decision. Wording in quotes comes from `.memlog.md`.

| Proposal | Decision | Changes an earlier decision? | Now in |
|---|---|---|---|
| M4 | Debt trigger uses net debt and wages, with a NOK 5,000 floor | Yes: "crisis triggers unchanged" (2026-11-04) | FR-32 |
| M5 | Parents pay mobile and public transport until 18 | No | FR-23 |
| M6 | One crisis month at a time, then a 2-month cooldown | Yes: F4 and "2-3 linked choices" reworded | FR-32 |
| M8 | Loss only if a trigger from month 59 is still true in month 60 | Narrows "active at 20" | FR-41 |
| M12 | Choices start and stop monthly everyday costs | No, scope addition | FR-17, FR-23 |
| M13 | In UJ-4, Markus keeps the moped | Yes: "sells the moped, not enough" (2026-11-04) | UJ-4 step 5 |
| G1 | Everyone is born in January | No | FR-12 |
| G3 | Part-time job from 15, up to 12 h a week | Fixes a contradiction in UJ-1 | FR-18, FR-47 |
| G4 | Life goals measured on net position at 20. The final PRD check table later raises the debt-free buffer and moves the experience months | No | FR-9 |
| G5 | Wellbeing is one score. The ending first used the average of months 49-60, and the final PRD check table changes that to months 37-60 | Adds overwork to stress and social life | FR-33 |
| X3 | At least 50 regular events | Yes: "minimum 30" (#19) | FR-17 |
| X7 | Ending ranks by size of kroner effect, with texts by sign | Rewords UJ-5 step 4 | FR-42 |
| X9 | One life at a time, and starting over is allowed after confirming | No | FR-43 |
| K3 | "Stay logged in on this device" box, unticked by default | Brings part of #31 into the MVP | FR-5 |
| K5 | A choice counts only when the server confirms it | Rewords FR-7 (2026-11-03) | FR-6 |
| K9 | Player information, deletion after 12 months, and no tracking | Makes three brief-addendum recommendations MVP requirements | NFR-3 |

The other 41 proposals fix gaps without changing a decision.

### Decisions from the final PRD check

Proposed by Dahl on 2026-11-05 and accepted by the team, as Dahl reported the same day (`.memlog.md`). The checks are `review-rubric.md`, `reconcile-inputs.md`, and `verify-applied.md`.

| Decision | Why | Changes an earlier decision? | Now in |
|---|---|---|---|
| A spending level (low 50%, normal 75%, high 95% of what's left of the wage). Low lowers social life by 2 a month, and high raises it by 2. *Superseded 2026-11-05 (independent review): low is now 60% (FR-23).* | Nothing else absorbed wages: a player who saved nothing until month 54 still reached NOK 166,249 on six months of full-time pay, and UJ-4 relied on a cost level no rule created. It also gives the player a monthly lever for trading money against wellbeing | Adds to M12, which stays. Dahl first chose event-started costs over a spending level, but those alone can't absorb a wage with about five choices a year | FR-23 |
| Debt-free buffer raised from NOK 50,000 to NOK 100,000, and a careless run must miss goals 1 and 2. *Superseded 2026-11-05 (independent review): goal 2 is now NOK 30,000 at each month-end 49-60 (FR-9).* | The buffer was reachable in two months of full-time pay. The earlier check tested only that goals weren't too hard | Changes the G4 default | FR-9 |
| Unlocked options stay open in the money view (FR-48), and a quiet month waits for a tap (FR-49) | Milestones came once and events never repeated, so a player who couldn't afford the licence in month 13 had no second chance, which contradicted UJ-3 | No | FR-48, FR-49 |
| Ending wellbeing uses months 37-60. *Superseded 2026-11-05 (independent review): the window is now months 19-60 (rule 12).* | With months 49-60, a player who worked 40 h a week for years could ease off in the last year and end at 55, a real win. With months 37-60, the same run ends at 41, a hollow win. Markus in UJ-4 stays at 60 or above | Changes G5 | FR-33 |
| Crisis events are written per trigger and age and can repeat, and a third step ends the crisis month (FR-32) | About 10 crisis events can't cover about 8 crisis months with no repeats, and nothing ended a crisis month if no choice cleared the trigger | No | FR-32 |
| The experience offer moves to months 44 and 56, and a pushed-out summer job stays open until its July pay month | Two required events landed in June for goal-3 players, and a summer job offer pushed out of June could arrive after the July it pays in | Moves the months in G4 | FR-9, FR-46, FR-48 |
| Playtest records that survive deletion, only in the playtest environment (FR-50) | FR-43 deletes the playthroughs the metrics count | Exception in NFR-3 | FR-50 |
| Four more cut steps, and dates set by the team (OQ-13) | The old cut list removed no feature with real build cost, and the lecturer asked for "en minimal versjon som sikkert kan bli ferdig" | Adds to the cut list | PRD §4.4, OQ-13 |
| OQ-6 blocks the first playtest, and OQ-11 is widened and blocks epics. *Superseded 2026-11-13 (PRD §8): OQ-6 is closed for the school project, and OQ-11 blocks nothing.* | Real email addresses first arrive with the playtest, and the project has no go-live. If the course requires AI in the app, architecture and epics change | Narrows "privacy questions don't block" (2026-11-03), which still holds for the MVP and the PRD | PRD §8 |

### Decisions from the independent review

Dahl asked Claude on 2026-11-05 to decide on the findings from the independent review (`review-2026-11-05-independent.md`), and the team reviews them in PR #52. Every finding's outcome is in `review-2026-11-05-independent-solutions.md`. The figures come from a month-by-month simulation. Where a row disagrees with an earlier table, this one applies.

| Decision | Why | Changes an earlier decision? | Now in |
|---|---|---|---|
| Spending is a share of the wage after tax, with costs on top. It can't take the account below zero or draw on savings | With the old base, spending absorbed most costs: NOK 12,000 of costs lowered net savings by only NOK 620 on high, so event-started costs and the moped barely mattered. Now the same costs lower net savings by NOK 12,340 on normal, and cause links and FR-39 tell the truth. A 3-month hold was tested and dropped, because it isn't needed at 60% | Changes the spending base from the final check | Rule 16, FR-23, FR-45 |
| Low spending is 60%, not 50%, and the reference run works 10 h a week, not 8 | Six months on low made 86% of the careless run's money, and small changes took it past the target. With 60%, every careless variant ends at or below NOK 88,995, while the reference run with expenses ends at NOK 106,928. A household contribution from month 55 was tested and dropped: it adds a mechanic with no source, and it hits the reference run as hard | Changes the shares from the final check | Rule 16, examples 20-21 |
| Ending wellbeing uses months 19-60. A social life below 20 raises stress, and high spending gives no social bonus while interest is charged | With months 37-60, working 40 h a week until month 36 and then easing off was still a real win. Now it ends at 39. Permanent debt on high scored the same as a debt-free player on normal. Saving at 25 h on low all the way now ends at 50, close to the boundary, and on 10 h a saver ends at 57, which stays a real win | Changes the window from the final check | Rule 12, FR-33 |
| The limit of 25 h a week stays, shown in the hours control | Scaling the penalty adds a formula for little teaching value, and a visible limit explains the drop. It remains a cliff: 25 h gives 68 and 26 h gives 41 | No | FR-47 |
| Goal 2 needs NOK 30,000 of available money at the end of each of months 49-60, and no debt at 20 | With a NOK 100,000 buffer, everyone reaching goal 2 also reached goal 1. This one is different in kind, and six good months can't reach it | Changes the buffer from the final check | Rule 13, FR-9 |
| Goal 3 needs the purchase by the end of month 56. One offer in month 44, then open in the money view | Buying and not buying passed or failed the goal test the same way, so the offers and events changed nothing. Two offers broke "no repeats" and FR-43's limit at 50 events | Changes goal 3 and the months from the final check | Rule 13, FR-9, FR-18 |
| No consumer loan in months 59-60 | A loan could clear the below-zero trigger and turn the loss into a win | No | Rule 6, FR-25 |
| The driving game is turn-based and judged by the server. It stays on the cut list, with "payment only" as the fallback, and the gift licence needs no game | A real-time game would let the device report its own pass, break NFR-7 and FR-7, and clash with WCAG AA. This keeps the route and the rules from the team's idea, and it's much cheaper to build. A real-time game can come in V2 | Narrows FR-51. Dahl described a game where the player drives a route and follows rules, so the team should check it still matches | FR-51, §4.1 |
| Car fuel is a cost the player starts or stops, and a licence opens car events | Half of players got a recurring cost they never chose, and the licence gave nothing | Settles part of OQ-8 | FR-23, FR-30 |
| Early payoff for family loans and payment plans, and a crisis month rechecks its triggers when it opens | A player with cash could lose goal 2 for lack of a button, and a player could get a crisis for a problem their wage had already fixed | No | FR-45, rule 8, FR-32 |
| Half of the events before 18 have two options with no cost | A player with no money got a first session of locked options. Pocket money stays in V2 | No | FR-17 |
| The AI driver (the AI game master in "Ready for V2") stays in V2, and the team doesn't wait for the lecturer's answer | Decided by the team, as Dahl reported on 2026-11-05. The PRD is updated if that changes. So no fallback is written, and OQ-11 no longer blocks epics | Changes OQ-11's blocker from the final check | §8 |

### Example purchases in the month summary

Decided by Dahl on 2026-11-05 (`.memlog.md`). The spending level is a percentage, but the most common regret in the survey is small purchases that add up, such as snacks and takeaway. So the month summary names a few example purchases next to the total. This adds some writing and no new rules, and it isn't in the worked examples, because it changes no figures (FR-23).

### Pocket money and V2

Decided by the team, as Dahl reported on 2026-11-05 (`.memlog.md`). Pocket money, and earning it, goes in V2, for example through minigames.

In the survey, 68% get money from parents or pocket money, so the MVP differs from many players' lives here: a player with no job has no income before 18. D23 tells the player. M5 had already left pocket money out, because it had no sourced figure.

### Four game areas: more game, less quiz (2026-11-10)

Decided by the team, as Dahl reported on 2026-11-10 (`.memlog.md`). The change came from the team's prompt and the UX concept sketches for a calendar, a job, a phone, and money. The full proposal, with the options weighed, is `revision-proposal-2026-11-10-game-loop.md`.

| # | Decision | Why | Alternative rejected |
|---|---|---|---|
| P1 | Activity slots come from free time (rule 12), ÷ 20, at most 4. Hours stay the only source of pay and free time | Pay, tax, free time, and rule 10 stay unchanged. More work means fewer slots by itself | Slots replacing hours. It would rewrite rules 3, 10, and 12, FR-47, and examples 1, 5, 17, and 20-23, and need a second wage path |
| P2 | The player plans the current month. Activities are applied when the player continues, at the end of the choice step | The rule 1 order is unchanged, there's no undo logic, and payment is checked again at the end | Planning the next month. It splits money, payment, and cause links over two months. V2 |
| P3 | Extra shifts are never placed in a slot, and start next month as in FR-47 | This month's income and tax are already calculated when the month opens | The concept's "+500 kr per slot", now replaced by the engine's own figure |
| P4 | FR-18 offers arrive as messages and open options. 4 active months a year go to story events. Event minimum 40 | Offers stop looking like A/B/C questions, FR-46 loses milestones and push-outs, and the overlap drops from 64% to 51% at N = 40. The 64% was N = 50 with 11 milestone events in 25 active months, and 66% for goal 3 | Keeping milestones as events with 5 active months (1, 3, 6, 8, and 10, chosen so that the June offers fell in active months) |
| P5 | Activities change stress and social life only, capped, and never free time | No double counting with hours | — |
| P6 | "Month plan" in the PRD | "Calendar" is already rule 11 and D17 | — |
| P7 | The ending summary groups activities by kind | Single activities never rank, but together they show small purchases adding up, the survey's most common regret | — |
| P8 | One schema per content type and one selection step (V2 AI seam) | Costs nothing now, and V2 AI can propose content without touching the engine | — |

**Refined while applying (OQ-19):** P5 didn't say how long an activity's effect lasts. A script applying rule 12 showed that lasting effects pile up, because nothing pulls social life back towards a baseline. One free activity in every slot (stress −2, social +4) lifted the 17b money chaser from 34 to 65 and a careful player to 95. That would remove the hollow win. Effects therefore count in their own month only (rule 12, example 26). The chaser then ends at 41, 44, and 37 at worst with the weights of goals 1, 2, and 3 (corrected to 42, 46, and 37 on 2026-11-11, see "Review fixes" below).

**Also decided:** the whole revision goes in, with FR-57 and the activity grouping (P7) at the top of the cut list. Tuning values are starting values under OQ-8. Worked examples 1-23 and the reference runs plan no activities.

**UX concept alignment:** recorded under "For UX" in "Detail for downstream work".

### Sources for the 2026-11-10 revision

Added on 2026-11-11 from saegg1205's branch `docs/prd-sara-endringer`. The revision had two sources: the team's written prompt («Videreutvikle LifeMode PRD – mer spill, mindre quiz») and the UX concept sketches for the four areas. Neither is stored in the repo, so this section records what the PRD took from the prompt. The sketches are recorded through "UX concept alignment" above and "For UX" under "Detail for downstream work".

**The team's prompt, by area:**
- **Whole game:** calendar, job, phone, and money are four parts of one life, not four minigames. What the player does in one place affects the others. The player shouldn't have to answer questions all the time. Instead, the player plans, reaches goals, discovers chances, and lives with the results. In the PRD: §5.5-5.8, FR-52 to FR-57.
- **Calendar:** time is as limited as money. No 30-day calendar to fill in over 60 months. Instead, a limited number of activity slots each month. School and daily duties are automatic, and the player plans only the free time left. More shifts mean more money and less time, and more friends and free time mean better wellbeing and less income. In the PRD: the month plan and slots (§5.5, FR-52, FR-53, P1).
- **Job:** a simple job system where the player applies, gets shifts, and gradually gets better chances. Turning up for shifts can lead to more shift offers later, and frequent overwork raises stress. In the MVP a job can be just a wage, a shift limit, and a few job events, with rules that fit ages 15-20. In the PRD: the job view (§5.7, FR-56), FR-47, and FR-48. Job development over time is V2 (§4.3).
- **Phone:** a simple inbox, not a quiz dressed as a chat, with pre-written messages and no free AI chat. Messages link to other areas: Emma's invitation adds a concert to the calendar, an extra-shift offer updates work, and a due bill is paid through the money system. Some messages are information, some open chances, and some need action. In the PRD: §5.6, FR-54, FR-55, and the message schema. Emma is the friend named here, not in the UX concept.
- **Money:** the engine, not the story or the messages, decides every amount, and the amounts add up exactly. Earning NOK 1,000, spending NOK 550, and moving NOK 400 to savings must match to the krone. The player can set money aside for goals, see upcoming costs, and understand why the balance changed, without a full online bank in the MVP. In the PRD: the money view (§5.8, FR-57), FR-45, and NFR-4.
- **Balance:** calendar and money are the core systems, while the phone and the job make life more dynamic. The phone doesn't always have new messages, and the job doesn't always need a decision. Some months are about saving and planning, others about new chances, unexpected costs, or big life changes. In the PRD: 4 active months a year and quiet months (FR-46, P4).

**The month example, as the team wrote it:**

> 1. Mobilen får en melding. En venn inviterer deg på konsert. Du får en ny aktivitet tilgjengelig.
> 2. Kalenderen oppdateres. Konserten krever én aktivitetsplass. Du har allerede lagt inn flere jobbvakter.
> 3. Spilleren planlegger. Du flytter på aktiviteter for å få plass. Du trenger kanskje å redusere antall jobbvakter.
> 4. Økonomimotoren beregner resultatet. Du får mindre lønn denne måneden, og konserten koster penger. Men du får også en sosial opplevelse.
> 5. Neste måned begynner. Sparepengene, trivselen og kalenderbeslutningene videreføres. Tidligere valg kan påvirke fremtidige muligheter.

**How UJ-6 differs from the example:**
- **Persona and figures:** Markus, his hours, the car licence target, month 35, and all amounts are the PRD's own, taken from worked examples 24-26 (R1, R2).
- **Shifts:** in the example the player places shifts in the calendar and cuts them to get less pay this month. In the PRD, shifts are never placed in a slot, and hours change from the next month (P3, rule 10). Markus therefore sees in the job view what ending the extra shifts would give from December, and keeps them.
- **What carries over:** savings and the month's wellbeing score carry over. An activity's effect on stress and social life counts in its own month only (rule 12, decided 2026-11-11). The player plans one month at a time, and planning the next month is V2 (P2, §4.3).

**Not taken from that branch:** it solved the same contradiction as R1 and R2 (Markus saving for the moped licence at 17 although he has had a moped since 16) by moving the concert journey to month 15, with examples 24-26 recalculated for that month, and by renumbering the journeys by age. This PRD keeps the car licence in month 35, which feeds UJ-4 (R1), and keeps the journey IDs stable while ordering them by age (§2.3), so that reviews, issues, and logs keep matching. Its other changes were already here: OQ-19 decided, ending extra shifts, and the wording of UJ-6 step 3.

### Review fixes (2026-11-11)

Decided by sarahnaess, who asked on 2026-11-11 to apply the recommended fixes from `review-2026-11-11-solutions.md` (`.memlog.md`). The team reviews them in PR #59. The review is `review-2026-11-11.md`. These decisions settle what the 2026-11-10 revision left open or contradictory. They are numbered R1-R12 (renamed from D1-D12 on 2026-11-13, so they don't clash with the disclosures D1-D26).

| # | Decision | Why | Alternative rejected |
|---|---|---|---|
| R1 | In UJ-4, Markus paid for the car licence himself at 18, with what he saved from 17 (UJ-6) | It explains why he has no buffer when the card hits its limit, and matches a mother who can't help | Keeping the parents' gift: his savings would then pay the card bill under rule 5, and UJ-4 wouldn't happen |
| R2 | UJ-6 is in November (month 35), a quiet month | October is active, and UJ-6 is the only journey showing an ordinary month | October with a highlight event added |
| R3 | The credit card's offer message comes in month 39, and the card opens in month 37 | It matches the UJ-4 trace and keeps month 37 for the car licence | Month 37 |
| R4 | An offer arrives even when the player doesn't qualify yet, and shows what's missing | Offers stay guaranteed, and the condition is part of the lesson | Waiting until the player qualifies |
| R5 | Savings-target progress is the current account plus savings | The missing amount uses the same total, so the two never disagree | The savings account only |
| R6 | No read state for messages, and no unread badges | Nothing new to store or replay | A stored read flag |
| R7 | Invitations repeat, at most once each per in-game year | Supply meets the 0-2 invitations drawn a month without a much larger library | One-off invitations with a minimum of 12 a year |
| R8 | Stress and social life are shown as the usual value and this month's value | Rule 12 is unchanged, and "Hvorfor?" matches the number it explains | Counting this month's activities in the social-life row, which would let activities change carried stress |
| R9 | A "careful player with some free time" run is pass/fail, and targets are tuned once prices exist | Goal 1 was only shown reachable without activities | Lowering goal 1 now |
| R10 | A plan that would set off a trigger asks the player to confirm, and isn't blocked | The player decides, as in UJ-4 | Blocking continuing |
| R11 | The four game areas come right after §5.4, and the money view has its own section | The vision calls them the game itself | Pointers only |
| R12 | A "same as last month" action for the month plan | It keeps 12 plans a session from becoming a chore | Leaving it to UX |

**Checked while applying:**
- **UJ-6 and example 25:** Markus owns a moped, so its insurance (NOK 250) is his own at 17 (FR-23), and example 25 now includes it. For the bank's "three quarters" message to fire in November, progress must pass 75% that month. Example 25 therefore has NOK 500 + NOK 23,500 before the month (73.8%) and NOK 25,920 after it opens (79.8%). The proposal's NOK 24,400 had already passed 75% in October.
- **UJ-4 timing:** a script ran months 35-40 from that state. With NOK 650 of activities a month he has about NOK 31,100 by month 40, and about NOK 34,300 if he plans no paid activities from December. UJ-4 therefore says he paid for the licence "at 18, cutting back on paid activities", with no month. The proposal's "month 39" didn't hold.
- **Example 26c:** a script that reproduces 17b (34, 37, 29) and the old 26c (41, 44, 37) gives 42, 46, and 37 at the real limits (stress −10). The careful player rises from 75 to 85 with goal 1's weights. The old "82-85" wasn't reproduced.
- **Boundary (26d):** with activities at the limits, the 17b run at 26 h on normal spending rises from 41 to 52, and the 25 h run from 68 to 79. The threshold and the activity effects are tuned together (OQ-8).
- **P4 correction:** FR-46 lost milestones, but follow-ups can still be pushed out. One that can't get a month by month 60 is now dropped and reported.

### Finalize (2026-11-11)

Decided by sarahnaess on 2026-11-11 during Finalize, from the rubric review (`review-rubric.md`) and the input reconciliation (`reconcile-revision-proposal-2026-11-10.md`, `reconcile-review-2026-11-11.md`). sarahnaess checked the new figures in examples 25-28 and 26c/d and found them OK.
- **Month-only activity effects are decided** (was OQ-19). They're in FR-33, FR-53, rule 12, and D26. Lasting effects would pile up and remove the hollow win. Effects fading back towards a baseline were also rejected, because they need a new rule, new tuning, and new worked examples before the delivery.
- **What a slot is worth goes to tuning (OQ-8).** With ±10 per activity and a ±15 cap, two activities reach the cap, so slots 3 and 4 add little. The content check reports ending wellbeing at 1-4 slots, and ±5 with a ±20 cap are values to try. The figures in examples 26a-d are unchanged.
- **Low spending and social life:** FR-33 and D26 now say that activities lift only the month, and that the social life that carries over follows events, spending, and hours. Letting a social activity skip the low-spending −2 row is a tuning candidate under OQ-8.
- **Cut timing:** cuts are applied in groups at checkpoints set under OQ-13 (§4.4).
- **Ending extra shifts:** running extra shifts can be ended from the job view, from the next month (FR-47, FR-56). The team's month example lets the player cut shifts to make room for an activity, and the change still applies only from the next month (P3).
- **Disclosure D11 fires when the card opens (month 37),** not on the card's month-39 message, because the card can be taken from the money view from month 37. This differs from fix O1 in `review-2026-11-11-solutions.md`.
- **Offers carry teaching:** the credit card and consumer loan offers have a tip and a teaching point (FR-19), as P4 planned.
- **Smaller fixes:** FR-49's month 59-60 warning, the FR-9 reference runs, UJ-3's interest message (FR-55), "eligible" instead of "can be placed" for invitations, NFR-7's list of inputs, NFR-8's "actions, not quizzes", the glossary terms, the §7 targets, and the UJ-4 wording on extra hours.

## Confirmed assumptions (2026-11-05, A-29 and A-30 added 2026-11-11)

| # | Assumption | Where |
|---|---|---|
| A-1 | The goal's target is an amount the game sets, reachable by 20, such as a start on a flat deposit | UJ-1, FR-9 |
| A-2 | UJ-3 takes place some in-game months after the first choice | UJ-3 |
| A-3 | A full-time job is available from month 55, at age 19 | UJ-5, FR-20 |
| A-4 | In the ending, the advice consists of general, pre-written tips | UJ-5, FR-42 |
| A-5 | A replay means choosing a goal again and drawing a new pengegave | UJ-5, FR-43 |
| A-6 | The email address is used only for login and recovery, and is never shown or used for marketing | §5.1 |
| A-7 | A reset link works once and expires | FR-3 |
| A-8 | Changing the password requires the current one | FR-4 |
| A-9 | The player can log out | FR-5 |
| A-10 | Every choice is saved as soon as it's made | FR-6 |
| A-11 | A device showing older progress can't overwrite a newer choice | FR-8 |
| A-12 | With no connection, the game accepts no new choices | FR-8 |
| A-13 | The goal can't be changed during a playthrough | FR-9 |
| A-14 | The avatar is picked from preset looks, with no free text | FR-10 |
| A-15 | The player can carry straight on into the next year | FR-15 |
| A-16 | An automated check enforces the event schema | FR-17 |
| A-17 | Tax uses the character's age in the game and fixed 2026 rates | FR-21 |
| A-18 | A card needs a steady wage, and the first limit is NOK 5,000-10,000 | FR-26 |
| A-19 | A family loan is repaid in monthly instalments | FR-27 |
| A-20 | Owning a moped requires the moped licence | FR-29 |
| A-21 | The card warning comes back each time interest starts again | FR-31 |
| A-22 | F10 accepts a system cause | FR-36, §7.3 |
| A-23 | The disclosed simplifications are a requirement | FR-40 |
| A-24 | GitHub Actions runs the tests on every pull request | NFR-9 |
| A-25 | Completion and the quiz are measured across sittings | §7.1 |
| A-26 | F5 moves to V2, with the AI. Checked against part 1 of the examiner's guide only (OQ-11, #39) | §7.3 |
| A-27 | The new rules get worked examples and unit tests | NFR-4 |
| A-28 | Deleting an account requires the current password and can't be undone | FR-44 |
| A-29 | The first reference run and worked examples 1-23 plan no activities | FR-9 |
| A-30 | In UJ-6, Markus pays his own moped insurance at 17. Moped fuel is charged only in April-October (rule 14, from 2026-11-13), so UJ-6's November has none | UJ-6, brief example 25 |
