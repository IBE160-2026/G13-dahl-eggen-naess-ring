---
title: LifeMode PRD addendum
created: 2026-11-03
updated: 2026-11-05
---

# Addendum: LifeMode PRD

This addendum holds the detail downstream work needs and the reasons behind decisions in the PRD. If it disagrees with the PRD, the PRD applies, and a decision reaches downstream work only once it's in the PRD or Rule Set v1. The decision history runs oldest first, and where two sections conflict, the later one applies. Detail sections are kept current, so they carry no date. The full log is `.memlog.md`.

## Detail for downstream work

### For the architecture

These items came out of the PRD review and belong in the next `bmad-architecture` run. They aren't in `architecture_technical_design.md` yet. Supabase facts in this addendum come from general knowledge and need verifying.

- **Authentication:** where email normalization and the sign-up limit live; which limits the login service gives out of the box and which need the backend; how a revoked login reaches the backend; token lifetimes; the chosen email relay and its quota.
- **Connectivity:** a state version per playthrough, a request ID for retries, browser visibility and online events, and the error format and codes.
- **Engine state:** storage for draws and the seed, content versions, the per-cause parts of each balance, and the card and account settings.
- **Hosting:** `architecture_technical_design.md` says no hosting provider is needed, which still holds for public production hosting, but NFR-11 requires a playtest environment. Name its provider, tier, and limits. The hosted Supabase free tier may pause idle projects (verify).
- **Responsiveness:** a server budget of at most 300 ms to process and save one month, for 9 out of 10 requests, with the backend and database in the same region. A browser test with network throttling plays a scripted first session, and a Lighthouse mobile run checks the first screen before each playtest.
- **Mobile-first:** add NFR-1's supported browsers and test devices as the test matrix.
- **Game flow:** the two-part month and the state check on every request that changes the game (FR-49), and the open-option model (FR-48).
- **Minigames:** they run on the server like the rest of the game, one saved answer at a time (FR-51). A real-time game would need its own decision on how to check results, so it's left for V2.
- **V2:** events reach the game through one schema and one selection step, which is enough for now. Generated events and their replay under FR-12 aren't designed, and V2 may need rework there.
- **Playtest:** the records in FR-50, the setting that keeps them off outside the playtest environment, test-user marking, and how they're exported.
- **Examiner:** seeding test users at the states NFR-6 names, and `.env.example`.
- **Other:** a scheduled deletion job, self-hosted fonts, and the accessibility check in CI.

### UJ-4 month by month

Reflects M13, the spending level with costs on top, and the 3.5% minimum, all decided on 2026-11-05. Markus keeps the moped (M13). This replaces the sale in the story that SE (sarahnaess) confirmed on 2026-11-04. With a NOK 10,000 limit, a sale for about NOK 9,300 and five months of extra shifts can't both be true: the sale alone would nearly clear the debt. This trace shows that the engine can reproduce UJ-4 under rules 1, 2, and 5. It's a set test state, not a scheduled playthrough: month 40, with the city trip, is quiet with the default active months, so a test sets the trip directly.

Entry state at month W, month 41 (May): age 18. His earlier bills were paid in full, including lunches and fuel. In month W−1, after that month's bill was paid, he put a NOK 10,000 city trip for everyone on the card at the event step. Card bill at the debt step: NOK 10,000. That's his limit, so the card takes no more purchases and his spending comes from the current account. Payment setting: the whole balance. NOK 1,000 in the current account and no savings. Wage 10 h a week, NOK 8,452. Mobile NOK 299 and moped insurance NOK 250. Spending level: high. Moped fuel is left out of the costs until #43 gives it a source. Tax is NOK 0 while his wages so far this year stay under NOK 99,650.

| Month | Wage | Costs | Spending | Free for the card | Bill | Interest | Paid | Card after | What happens |
|---|---|---|---|---|---|---|---|---|---|
| W | 8,452 | 549 | 8,029 (high) | 874 | 10,000 | 188 | 874 | 9,314 | Card warning shows, and Markus acts (see below) |
| W+1 | 10,142 | 549 | 7,607 (normal) | 1,986 | 9,314 | 175 | 1,986 | 7,503 | 12 h a week, well within rule 10 |
| W+2 | 10,142 | 549 | 7,607 | 1,986 | 7,503 | 141 | 1,986 | 5,658 | |
| W+3 | 10,142 | 549 | 7,607 | 1,986 | 5,658 | 107 | 1,986 | 3,779 | |
| W+4 | 10,142 | 549 | 7,607 | 1,986 | 3,779 | 71 | 1,986 | 1,864 | |
| W+5 | 10,142 | 549 | 7,607 | 1,986 | 1,864 | 0 | 1,864 | 0 | Paid in full, no interest: back on track, with NOK 122 left |

In month W:
- Interest starts, so the card warning shows: NOK 188 this month, and 51 months and NOK 5,508 in total interest if he pays only the minimum.
- He talks to his mother, and the family draw gives no money.
- He turns the card off, asks for one extra 2-hour shift a week, and moves spending down to normal.
- He checks what the moped would sell for: about NOK 9,300 (rule 14, a gift moped owned about 26 months), less than he owes, and he'd pay for the bus without it. He keeps it.

He pays NOK 682 in interest in total, against NOK 5,508 at the minimum. W+1 is June, so the summer job is on offer, and he says no because he already has the extra shifts. Taking it would pay NOK 33,547 in July, and the card would be paid in full that month, with NOK 363 in interest. The trace shows the slower path, and a player can choose either. No crisis trigger fires. Worked example 17a in the brief addendum covers his wellbeing, and example 23 covers what he has to do after this to reach his goal.

### Event scheduling and library size

**Active months:** months 1, 3, 6, 8, and 10 of each in-game year (January, March, June, August, October). There are never more than two quiet months in a row. The June offers and goal 3's experience event in FR-46 fall in active months. Months 59-60 are quiet by default. A crisis, a card warning, or a pushed-out milestone or follow-up can still take them.

**Set placements by year.** The rest of each year's five months are follow-ups and drawn events.

| Year | Months | Set placements |
|---|---|---|
| 1 | 1-12 | Month 1 pengegave, month 3 part-time job |
| 2 | 13-24 | Month 13 moped licence, a moped offer once the player has a licence, month 18 summer job |
| 3 | 25-36 | Month 30 summer job |
| 4 | 37-48 | Month 37 car licence draw, month 39 credit card, month 42 summer job, month 44 experience for goal 3 |
| 5 | 49-60 | Month 49 consumer loan, month 54 full-time job |

**Eligibility at draw time** covers `owns_moped`, `has_moped_licence`, `has_job`, and `has_car_licence`. The placements that must be guaranteed are in FR-46.

**Who gets a month:** the order in FR-46. An unexpected expense isn't in it, because it's a deduction with a system cause.

**Library size.** X3 sets the minimum at 50, and FR-17 targets 60-80. The table above gives 11 milestones in every playthrough, and 12 for goal 3. The other 14 of the 25 slots are drawn evenly from the rest, so the expected number of events two playthroughs share is 11 + 14² / (N − 11):

| Library N | Shared at least | Shared on average | Share of 25 |
|---|---|---|---|
| 30 | 20 | 21 | 85% |
| 40 | 11 | 18 | 71% |
| 50 | 11 | 16 | 64% |
| 60 | 11 | 15 | 60% |
| 80 | 11 | 14 | 55% |

For goal 3 at N = 50 it's 12 + 13² / 38 = 16.4, or 66%, just inside FR-43's two-thirds. That's why the experience has one event, not two.

Flag gating raises overlap and different choices lower it, so the seeded content check, not this table, is the real test. The check runs 1,000 seeded playthroughs with random choices.

### Event schema

| Field | Content | Checked |
|---|---|---|
| id, version | Unique text ID, and a whole-number version (NFR-4) | ID unique; version rises on any change |
| type, trigger | Regular or crisis. A crisis event also names its rule 8 trigger | Every trigger is covered at each age where it can occur |
| mechanism | One or more from the fixed list | Names exist |
| age range | From and to, in years and months, within 15y0m-19y11m | From ≤ to |
| requires flags, blocks flags | Lists of flag names | Names exist in the flag list |
| milestone | The unlock it belongs to (FR-18), or none | Unlock exists |
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

**What the content check enforces on options:** every option states its wellbeing effect; every regular event has an option with no cost; every crisis event includes asking family and ignoring it; values stay inside the limits above.

Unexpected expenses are a separate list, each with a kind, an amount, the flags it needs, and a source.

### How the engine keeps results repeatable and traceable

**Random draws.** One seed per playthrough. Each draw is derived from the seed, the month, and what is drawn (for example "family help, event E-41"), so it doesn't depend on the order of requests. Engine tests can set the seed or force a result. The player can still reroll the pengegave by starting over, and a kept NOK 30,000 is enough for goal 1 with only summer jobs and low spending (worked example 21f). That's accepted: keeping it is a good choice, every goal is reachable from NOK 10,000, and the game has no score to compete on. Rerolling the car licence gift means replaying three in-game years.

**Content versions.** Each playthrough keeps the versions it started with (NFR-4). Old versions are kept while any playthrough uses them. Engine code fixes apply to all playthroughs, and the worked examples guard them.

**Cause link shares.** Interest on a balance is shared in proportion to each choice's part at the start of the month. Payments and withdrawals reduce every part in proportion. Rounding uses largest remainder, with ties to the earliest cause. Example: a card balance of NOK 6,000 is a city trip (NOK 4,000) and a jacket (NOK 2,000). The month's interest is NOK 113. The shares are 75.33 and 37.67, the floors give 112, and the remaining krone goes to the largest remainder: trip NOK 75, jacket NOK 38.

### The ending screen

**Texts.** To keep authoring small, ending texts are written per mechanism and sign, about 18 texts, plus pre-written texts for system causes. An option can override with its own ending text. Wages stay a system cause, so job and hours choices have no linked kroner and can't appear among the three choices the ending shows. That's an accepted trade-off: wages are the game's largest money flow, and linking them would crowd out the choices the summary is meant to show.

**"If you had chosen differently."** The line types, in order, are debt cost, money kept, and a pre-written fallback (FR-39). The comparison needs no authoring field. Re-running the playthrough with one choice swapped was rejected, because later events diverge and the result is hard to explain or test. The "everything else equal" assumption has its own disclosure (D15).

### Privacy measures in the MVP

**Player information covers:** what is stored (email, password as a hash, game data); what for (login, recovery, saving the game); how long; how to delete it; which services handle the data (the login service and any email relay); that there's no marketing, no other sharing, and no AI; who to contact; and who the game is for (15-20).

**Deleting inactive accounts:** 12 months covers a whole school year and a summer, far longer than a five-session playthrough needs. No warning email is sent, so the address is used only for login and recovery.

**Keeping only one life (X9, FR-43).** Deleting ended lives is the simplest privacy answer and keeps minors' data small.

**No age statement.** "I am 15 or older" stores and proves nothing. The brief addendum advises against consent as the legal basis, so the consent age doesn't apply, and the statement would turn away 14-year-olds in 10th grade or teach them to tick it falsely. Revisit if #24 chooses consent.

**To settle before the first playtest (OQ-6, #24):** who the controller is (group or university), the legal basis, and the full privacy text.

**Playtest data.** Game metrics are counted per account in the playtest environment. NFR-3 sets the export and the code key. No email addresses leave the system, and one team member keeps the key if game data is linked to survey answers. Until the key is deleted the results are pseudonymous, and after that anonymous.

## Changes from the proposal

The examiner's guide requires anything left out or changed from the approved proposal to be described and justified. The proposal isn't in the repo, so this table is incomplete (OQ-15).

| Change | Why |
|---|---|
| AI-generated events moved to V2, so the MVP has no AI. F5 moves with them | Team decision, logged on 2026-11-03. The lecturer's feedback of 2026-10-06 advised building the engine and the event library first, so the game works with no AI, and rated in-app AI among the hardest parts. Whether this meets the course requirements is OQ-11 |

## Decision history

### Competitor playtests

Team verdict as reported on 2026-11-03: everyone on the team has tried both products. This replaces the note in `research/playtest-competitors-2026-10-31/notes.md` that only one member had played Koll på cashen and that PersonalFinanceLab had not been tried.

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

**Sessions:** one session is one in-game year, and nothing locks the player out in real time. Five years at 20-30 choices gives about 4-6 choices a year, which fits a 10-15 minute session. Waiting in real time would work against the target of 70% finishing the game.

**Moped licence:** when the player chooses to take it, they pay for driving lessons, mandatory lessons and the licence itself, at real prices from sources such as Statens vegvesen, driving schools and SSB. The recap's teaser names the cost, so no new screen is needed. It's a payment only, with no exam or driving mechanics. (The minigame decision of 2026-11-05 replaced "payment only". See FR-51.) Owning a moped and the car licence were added from UJ-4; see "UJ-4: card warning, family help, moped, and car licence".

### Login with email: decisions, limits, and reset routes

Decided on 2026-11-03. This replaces the earlier decision on username, no email and no reset. Updated to match on 2026-11-03: brief (Scope In #9, Constraints), brief addendum (Privacy, Login secret), architecture (Database and Data Model, Authentication and authorization) and issue #24. The sign-up decision, default limits, and reset routes came from review proposals K1-K4 on 2026-11-05.

What this changes for the build:
- **Internal address plan:** the plan to build a fake address from the username (`@lifemode.invalid`) is no longer needed.
- **Playtests:** playtesters aged 18-20 will now give a real email address, while the brief says no contact details are stored with results, so the two have to be kept apart. See "Playtest data" under "Privacy measures in the MVP".

**Sign-up shows whether an address has a user.** Accepted: hiding it needs an email confirmation step before play, which the team ruled out on 2026-11-03. The sign-up limit stops bulk checks, and the owner can take back an address someone else registered by resetting the password and deleting the account. FR-2 and FR-3 still don't reveal it. To be reviewed in the privacy check (#24).

**Same typo in both email fields.** It isn't caught: the player can play, but can't reset the password.

**Default limits (all configuration).** FR-1, FR-2, FR-3, and FR-5 state the defaults players see. If this table differs from them, the PRD applies.

| Limit | Default | Why |
|---|---|---|
| Sign-up attempts per network | 60 an hour | A class of 30 with one retry each fits |
| Password length | At least 8 characters, at least 64 allowed | A 12-15-character minimum would slow sign-up for a 15-year-old |
| Failed logins per address | 10 in 15 minutes, then a 15-minute pause | Stops guessing, and the message stays neutral |
| Login attempts per network | 300 an hour | A class of 30 at three attempts each isn't blocked |
| Reset emails | 1 per address a minute and 5 a day; total per day at most 80% of the free quota | One script can't use up the quota and block recovery [needs figure: the chosen service's quota, OQ-3, #43] |
| Reset link | 60 minutes, and a new link cancels older ones | |
| Login without "stay logged in" | Until the browser closes, or 30 minutes with no activity | Shared school PCs |
| Login with "stay logged in" | Until logout, or 30 days without play | The box is unticked by default, which suits shared school PCs. The cost is that a phone player logs in again more often, which could lower the return rate. Check this in the playtest |

**Reset email routes (OQ-4, #30).** Password reset has to send email within the hard constraint of zero ongoing cost, and it has to work in the examiner's Docker run without the team's cloud account or keys.
- **Examiner's local run:** reset emails go to a local mail inbox that comes with the local login stack, and the README gives its address. The Supabase CLI includes one (Inbucket, or Mailpit in newer versions; verify).
- **Hosted playtest:** a free-tier email relay whose quota covers 10-20 testers plus the limits above. Supabase's default sender is reported to deliver only to the project team's own addresses, a few an hour (verify).
- **Fallback if no free relay works:** a tester who asks in person gets a one-time reset link that the team creates with the login service's admin tools. This works for 10-20 testers the team knows, but not for go-live.

### Interest after a long break: left out of the MVP

The team suggested positive or negative interest after an extremely long break. Decided on 2026-11-03 to leave it out, and the game stays exactly as the player left it. Credit only starts at 18, so a younger player would mostly get free money for staying away, an older player in debt would be punished for coming back, and the game's clock runs in game months with fixed rates.

### Saving and interest in UJ-3

Decided on 2026-11-03.

**Funds stay out of version one.** The team's narrative said funds or savings, but investing was decided out on 2026-10-31, and funds need returns that go up and down, which the engine doesn't have. Many survey respondents asked about funds, so they're a candidate for later.

**The game shows the real interest, even when it's small.** First-year interest under rules 1-2:

| Saved | Savings account (2.87%) | BSU (5.61%) |
|---|---|---|
| NOK 2,000 | NOK 60 | NOK 116 |
| NOK 3,000 | NOK 84 | NOK 172 |
| NOK 5,000 | NOK 144 | NOK 287 |

Interest alone won't pay for a moped, so the UJ-3 moment rests on two things: the surprise that money earned money without the player doing anything, and a pointer to other income. A summer job at 16 pays NOK 16,728 (worked example 1).

**BSU comparison:** "Hvorfor?" can also show what the same money would earn in BSU. This counts as an "if you had chosen differently" line, which is first on the cut list (PRD §4.1), and the moment works without it.

### Tips from the game

Decided on 2026-11-03. Some events carry a short, general, pre-written tip that the player is free to ignore. A tip is about the situation in the game and isn't personal advice, which the brief rules out. It should sound like a tip rather than a lecture.

### UJ-4: card warning, family help, moped, and car licence

Decided on 2026-11-04.

**A warning comes before a crisis.** A first card for ages 18-20 usually has a limit of NOK 5,000-10,000, and 10 hours a week at NOK 195.04 pays NOK 8,452 a month, so a new card rarely pushes debt above 3× income on its own. Instead, the game warns the player once a card bill isn't paid in full and interest starts, and the player decides whether to act. With a NOK 10,000 limit, the 3× income trigger is out of reach on a 10-hour wage (3 × NOK 8,452 = NOK 25,356), so in UJ-4 only the missed minimum can start a crisis. (M4 later changed this trigger to net debt and wages, with a NOK 5,000 floor. The UJ-4 result holds: see "UJ-4 month by month".)

**What the card costs.** The small cost in worked example 4 comes from the small amount, not the rate: 22.6% a year is a normal card rate (SSB; the market's effective rates run from 20% to 30%). At a small balance, the NOK 300 minimum pays the debt off quickly. Interest is charged every month, so the game shows both this month's interest and the total cost of paying only the minimum. Under rule 5:

| Card debt | Interest in month 1 | Months to pay off at the minimum | Total interest |
|---|---|---|---|
| NOK 3,200 (worked example 4) | NOK 60 | 13 | NOK 406 |
| NOK 8,400 (about one month's wage) | NOK 158 | 41 | NOK 3,645 |
| NOK 10,000 (top of a typical first limit) | NOK 188 | 51 | NOK 5,508 |

UJ-4 shows the cost for the player's own balance. The figures use the 3.5% minimum in rule 5 (decided on 2026-11-05), with monthly interest rounded under rule 2. Compared with 3%, it changes the figures only for balances above about NOK 8,600, where 3.5% is more than NOK 300. At 3%, NOK 10,000 took 53 months.

**Family help.** Family can give or lend money, but mostly as a loan that has to be paid back, so the player learns from it. It's not always on offer: in the survey, 36% had an unexpected expense that was hard to pay, and about half of them got family help (17% of all respondents). So roughly half the time, the player has to find another way. Sometimes family can cover only part of the amount.

**Moped.** As first decided, the player has a moped from age 16, either bought or received as a gift. The team's decision of 2026-11-05 replaced that: owning one is a choice, with occasional gift offers (FR-29). It costs fuel, repairs and insurance, and the parents may pay part of the insurance. Its resale value drops with the time owned (rule 14), and tracking actual use comes later. Prices should follow the real market. In the MVP, the parents' share of the insurance is random. Once the AI game engine is added, the gift offers and the parents' share can be based on real data.

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

If time runs short, cut in the order in PRD §4.1. The warning, the moped and selling it stay, because UJ-4 depends on them.

### UJ-5: no student loan, Markus's goal, and the ending

Decided on 2026-11-04.

**No student loan in version one.** Markus takes a job after upper secondary school and saves towards a flat. A student loan would bring in problems that don't pay off within a game that ends at 20:
- At NOK 15,488 a month (Lånekassen basislån 2026-27), his debt passes 3× a part-time wage within two months, which starts a crisis month. (Written against the trigger as it stood on 2026-11-04. M4 later changed it.)
- It blocks the debt-free goal.
- A player could borrow the full amount and save it to reach a savings goal.
- Interest and repayment only start after studying, so the game would teach little from it.

**For the education step later:** the game has to make clear that a student loan while studying isn't bad, and isn't the same as credit card debt. It has no interest while studying, and repayment starts only after the degree.

**Markus's life goal.** He chose saving for something big in UJ-1, with a flat as the big thing. A 15-year-old picks what he wants rather than "debt-free", and choosing the flat means the card debt at 18 puts his goal at risk. In the second round he goes for saving for something big or for being debt-free with a buffer, and chases money at the cost of his wellbeing, which gives the hollow win.

**"If you had chosen differently" on the ending screen.** These lines stay for the three choices that mattered most, and only those three can be opened. The lines in "Hvorfor?" during play, including the BSU comparison, are cut first. See "The ending screen" for the line types.

**Comparing playthroughs: later.** For now the ending shows a summary of the playthrough and the tips. Comparing one playthrough with the next is a candidate for a later step.

### Team decisions on Dahl's proposals

Decided on 2026-11-05.

| Decision | Why | Now in |
|---|---|---|
| No tobacco or alcohol choices for now | Research found them probably allowed, with conditions, but their effect on young players is unknown and can't be tested in playtests with 18-20-year-olds | NFR-8 |
| Card minimum of 3.5%, min NOK 300 | Matches Bank Norwegian, and DNB also uses 3.5%. Cards with limits up to NOK 30,000 fall outside utlånsforskriften, so this is about realism | Rule 5 |
| The card minimum is calculated on the balance before the month's interest | Keeps the figures for NOK 10,000: a NOK 350 first payment, 51 months, and NOK 5,508 in interest. Calculating it after interest gives NOK 5,437 at 3.5% (#38) | Rule 5 |
| Account deletion in the game, with the current password and no undo | The game stores email addresses of players as young as 15, and the privacy check (#24) recommends it. Requiring the password stops someone else deleting the account on a shared PC | FR-44 |
| The player chooses to buy a moped, with occasional gift offers | A random draw between buying and a gift could make saving up pointless, which works against UJ-3 | FR-29 |
| The car licence gift is random, and a player without it can pay | Gives a large, real money choice at 18 | FR-30 |
| All family gifts stay | They are no longer on the cut list | PRD §4.1 |
| Family loans don't count towards the 3× income crisis trigger (now the debt trigger in FR-32) | A teenager with no income would otherwise go into crisis from any loan | FR-27 |
| A hollow win shows at least one choice that hurt wellbeing | A kroner ranking alone may not show why wellbeing ended up low | FR-42 |

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
| A spending level (low 50%, normal 75%, high 95% of what's left of the wage). Low lowers social life by 2 a month, and high raises it by 2 | Nothing else absorbed wages: a player who saved nothing until month 54 still reached NOK 166,249 on six months of full-time pay, and UJ-4 relied on a cost level no rule created. It also gives the player a monthly lever for trading money against wellbeing | Adds to M12, which stays. Dahl first chose event-started costs over a spending level, but those alone can't absorb a wage with about five choices a year | FR-23 |
| Debt-free buffer raised from NOK 50,000 to NOK 100,000, and a careless run must miss goals 1 and 2 | The buffer was reachable in two months of full-time pay. The earlier check tested only that goals weren't too hard | Changes the G4 default | FR-9 |
| Unlocked options stay open in the money view (FR-48), and a quiet month waits for a tap (FR-49) | Milestones came once and events never repeated, so a player who couldn't afford the licence in month 13 had no second chance, which contradicted UJ-3 | No | FR-48, FR-49 |
| Ending wellbeing uses months 37-60 | With months 49-60, a player who worked 40 h a week for years could ease off in the last year and end at 55, a real win. With months 37-60, the same run ends at 41, a hollow win. Markus in UJ-4 stays at 60 or above | Changes G5 | FR-33 |
| Crisis events are written per trigger and age and can repeat, and a third step ends the crisis month (FR-32) | About 10 crisis events can't cover about 8 crisis months with no repeats, and nothing ended a crisis month if no choice cleared the trigger | No | FR-32 |
| The experience offer moves to months 44 and 56, and a pushed-out summer job stays open until its July pay month | Two required events landed in June for goal-3 players, and a summer job offer pushed out of June could arrive after the July it pays in | Moves the months in G4 | FR-9, FR-46, FR-48 |
| Playtest records that survive deletion, only in the playtest environment (FR-50) | FR-43 deletes the playthroughs the metrics count | Exception in NFR-3 | FR-50 |
| Four more cut steps, and dates set by the team (OQ-13) | The old cut list removed no feature with real build cost, and the lecturer asked for "en minimal versjon som sikkert kan bli ferdig" | Adds to the cut list | PRD §4.1, OQ-13 |
| OQ-6 blocks the first playtest, and OQ-11 is widened and blocks epics | Real email addresses first arrive with the playtest, and the project has no go-live. If the course requires AI in the app, architecture and epics change | Narrows "privacy questions don't block" (2026-11-03), which still holds for the MVP and the PRD | PRD §8 |

### Decisions from the independent review

Dahl asked Claude on 2026-11-05 to decide the findings from the independent review (`review-2026-11-05-independent.md`), and the team sees them in PR #52. Every finding's outcome is in `review-2026-11-05-independent-solutions.md`. The figures come from a month-by-month simulation. Where a row disagrees with an earlier table, this one applies.

| Decision | Why | Changes an earlier decision? | Now in |
|---|---|---|---|
| Spending is a share of the wage after tax, with costs on top. It can't take the account below zero or draw on savings | With the old base, spending absorbed most costs: NOK 12,000 of costs lowered net savings by only NOK 620 on high, so event-started costs and the moped barely mattered. Now it's NOK 12,340 on normal, and cause links and FR-39 tell the truth. A 3-month hold was tested and dropped, because it isn't needed at 60% | Changes the spending base from the final check | Rule 16, FR-23, FR-45 |
| Low spending is 60%, not 50%, and the reference run works 10 h a week, not 8 | Six months on low made 86% of the careless run's money, and small changes took it past the target. With 60%, every careless variant ends at or below NOK 88,995, while the reference run with expenses ends at NOK 106,928. A household contribution from month 55 was tested and dropped: it adds a mechanic with no source, and it hits the reference run as hard | Changes the shares from the final check | Rule 16, examples 20-21 |
| Ending wellbeing uses months 19-60. A social life below 20 raises stress, and high spending gives no social bonus while interest is charged | With months 37-60, working 40 h a week until month 36 and then easing off was still a real win. Now it ends at 39. Permanent debt on high scored the same as a debt-free player on normal. Saving at 25 h on low all the way now ends at 50, close to the boundary, and on 10 h a saver ends at 57, which stays a real win | Changes the window from the final check | Rule 12, FR-33 |
| The limit of 25 h a week stays, shown in the hours control | Scaling the penalty adds a formula for little teaching value, and a visible limit explains the drop. It remains a cliff: 25 h gives 68 and 26 h gives 41 | No | FR-47 |
| Goal 2 needs NOK 30,000 of available money at the end of each of months 49-60, and no debt at 20 | With a NOK 100,000 buffer, everyone reaching goal 2 also reached goal 1. This one is different in kind, and six good months can't reach it | Changes the buffer from the final check | Rule 13, FR-9 |
| Goal 3 needs the purchase by the end of month 56. One offer in month 44, then open in the money view | Buying and not buying were the same inequality, so the offers and events changed nothing. Two offers broke "no repeats" and FR-43's limit at 50 events | Changes goal 3 and the months from the final check | Rule 13, FR-9, FR-18 |
| No consumer loan in months 59-60 | A loan could clear the below-zero trigger and turn the loss into a win | No | Rule 6, FR-25 |
| The driving game is turn-based and judged by the server. It stays on the cut list, with "payment only" as the fallback, and the gift licence needs no game | A real-time game would let the device report its own pass, break NFR-7 and FR-7, and clash with WCAG AA. This keeps the route and the rules from the team's idea, and it's much cheaper to build. A real-time game can come in V2 | Narrows FR-51. Dahl described a game where the player drives a route and follows rules, so the team should check it still matches | FR-51, §4.1 |
| Car fuel is a cost the player starts or stops, and a licence opens car events | Half of players got a recurring cost they never chose, and the licence gave nothing | Settles part of OQ-8 | FR-23, FR-30 |
| Early payoff for family loans and payment plans, and a crisis month rechecks its triggers when it opens | A player with cash could lose goal 2 for lack of a button, and a player could get a crisis for a problem their wage had already fixed | No | FR-45, Rule 8, FR-32 |
| Half of the events before 18 have two options with no cost | A player with no money got a first session of locked options. Pocket money stays in V2 | No | FR-17 |
| The AI driver stays in V2, and the team doesn't wait for the lecturer's answer | Decided by the team, as Dahl reported on 2026-11-05. The PRD is updated if that changes. So no fallback is written, and OQ-11 no longer blocks epics | Changes OQ-11's blocker from the final check | §8 |

### Minigames

Decided by the team, as Dahl reported on 2026-11-05 (`.memlog.md`). The game gets small minigames along the way, to make it more fun. Not all of them are defined yet. The example so far is the licence: to take it, the player plays a game where they drive a route and have to follow some rules.

This replaces "the licence is a payment only, with no exam or driving" from 2026-11-03. See FR-28, FR-30, and D10. A minigame is the first thing in the game the player does with skill rather than by choosing, and it runs on the device, so FR-51 sets how its result reaches the engine. Dahl added on 2026-11-05 that the team sees minigames along the lines of the driving test for the licence, so the MVP's minigames are for the licences. The independent review later made the driving game turn-based. See the table above.

### Example purchases in the month summary

Decided by Dahl on 2026-11-05 (`.memlog.md`). The spending level is a percentage, but the most common regret in the survey is small purchases that add up, such as snacks and takeaway. So the month summary names a few example purchases next to the total. This adds some writing and no new rules, and it isn't in the worked examples, because it changes no figures (FR-23).

### Pocket money and V2

Decided by the team, as Dahl reported on 2026-11-05 (`.memlog.md`). Pocket money, and earning it, goes in V2, for example through minigames. The AI play driver also stays in V2 for now.

In the survey, 68% get money from parents or pocket money, so the MVP differs from many players' lives here: a player with no job has no income before 18. D23 tells the player. M5 had already left pocket money out, because it had no sourced figure.

## Confirmed assumptions (2026-11-05)

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
