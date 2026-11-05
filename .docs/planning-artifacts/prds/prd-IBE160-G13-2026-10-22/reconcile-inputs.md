---
title: LifeMode PRD input reconciliation and memlog audit
created: 2026-11-05
scope: PRD Finalize, read-only check of prd.md and addendum.md
---

# Input reconciliation and memlog audit

Checked `prd.md` and `addendum.md` (status draft, updated 2026-11-05) against the inputs and the memlog. Rule Set v1 means the brief addendum. Nothing but this file was written.

Not reported, by instruction: AI out of the MVP, rent, housing in wellbeing, anonymous login, crossroads replay, and student loans.

**Severity:** High changes what gets built or how it's graded. Medium changes what a player or reader takes away. Low is a one-line fix.

## Result

| Area | Result |
|---|---|
| Inputs with real gaps | brief, market-research, user-research, tilbakemelding, architecture, extract-domain |
| Inputs with no real gaps | market-validation, design-thinking, extract-product, extract-users-market |
| Memlog (87 entries) | 3 exceptions: L25 partly lost, L50 captured with a misread figure, L92 not reflected in FR-33 |
| Grading | 1 requirement the PRD would fail as written (guide §4.2, changes from the proposal), plus 5 other risks |
| Arithmetic | UJ-4, FR-26, FR-29, FR-31, FR-39, and FR-47 figures recomputed under rules 2, 5, and 14. All match |

## Part 1: Input reconciliation

### brief.md

**B1. High. "Situations come from your own choices" became a random draw that can pass its test without choices mattering.**
- **Source:** brief line 37, "the next situation builds on everything the player has done so far". Brief line 41, "the story is different for each player, because the situations they meet come from their own choices and history".
- **PRD:** FR-46 draws most active months at random, with equal chance. The addendum puts this at about 8 milestones plus 17 drawn slots out of 25. Boomerang pairs and flags are the only link from a choice to a later event, and neither FR-17 nor the content check sets a minimum for them.
- **Why it matters:** FR-43's test compares "pairs of seeded playthroughs with random choices". Different seeds give different events on their own, and the addendum's overlap table (8 + 17² / (N − 8)) shows the two-thirds limit is met by library size alone. A library with no boomerang pairs passes, while the brief's central promise and the "every choice carries forward" line in §1 go untested.
- **Fix:** in FR-43 and the content check, compare pairs with the same seed and different choices, because draws derive from the seed (addendum, "How the engine keeps results repeatable"). Add a configured minimum of follow-up events per playthrough, with the number left to tuning (OQ-8).

**B2. Medium. The voice of failure moments and the ending texts were dropped.**
- **Source:** brief line 43, goal not reached is "no loss, but advice on modest savings goals and what not saving costs". Brief addendum line 234, the loss text "reflects wellbeing, for example 'you had a good life, but the economy did not hold'", and "the consequences are shown clearly". Brief addendum line 237, goal not reached is "neither a win nor a loss. Saving little or spending a lot is allowed", with "a reflection on the consequences of not saving".
- **PRD:** FR-41 item 4 keeps only "advice on modest savings goals and what they bring". Item 1 says nothing about the loss text. NFR-8 gives a voice rule for tips only, so warnings, crises, and endings have none.
- **Fix:** add the loss text and "what not saving costs" to FR-41. Extend NFR-8: warnings, crises, and endings state the consequence plainly and don't scold, and goal not reached is never framed as failure.

### market-research.md

**M1. Medium. "Without becoming complicated" was dropped from the differentiation claim.**
- **Source:** market-research line 77 and brief line 57, "combines good money management with wellbeing without becoming complicated". Brief line 53 says PersonalFinanceLab is "more complex" and LifeMode combines the two "simply".
- **PRD:** §1 carries Norway and wellbeing, and "smoother" against Koll på cashen. Nothing in the PRD or addendum says simple, and no metric guards it. The addendum's PersonalFinanceLab row leaves out complexity. See also memlog L25.
- **Why it matters:** the PRD now has 47 FRs, 15 engine rules, and about ten money actions outside events (FR-45), so this half of the claim is the part most at risk.
- **Fix:** restore the phrase in §1. Add a playtest debrief question, for example "the money parts were easy to follow" (1-5).

**M2. Medium. Russefeiring has no decision.**
- **Source:** market-research line 16 names four Norwegian milestones that competitors don't build on: confirmation money, russefeiring, studielån, and leiekontrakt. The brainstorm also had "Russ as a big boomerang: saving for russebuss from 16 vs. borrowing at 18-19".
- **PRD:** confirmation money became the pengegave (L29), and studielån and leiekontrakt are out by decision. Russ appears nowhere in the PRD, addendum, or memlog, though it is the most Norway-specific money decision at 18-19 and could be cost-only under NFR-8.
- **Fix:** add it to the FR-17 candidate topics as costs only, with no alcohol content, or log a decision to leave it out.

### user-research.md

**U1. Medium. The addendum misreads the family-help figure.**
- **Source:** user-research line 78, 36% had a hard-to-pay expense, and "about half of them (17% of all) got help from family".
- **PRD:** addendum line 97 says "only 17% got family help with an unexpected expense, so most of the time the player has to find another way". The base is wrong: among those who had such an expense, about half got help (17 / 36 = 47%). This also conflicts with §2, which names family as the main source of help.
- **Why it matters:** OQ-8 still has to tune how often family helps, and this sentence would bias it low.
- **Fix:** correct the sentence. Use about 50% as the survey-based starting point for OQ-8, or state why the game is stricter.

**U2. Medium. Whether wellbeing makes sense to players is an open research question with no home.**
- **Source:** user-research line 58, the survey didn't ask whether mechanics "such as wellbeing and lasting consequences make sense", and "those questions … are still open". The extract also lists the concept test as undecided (extract-users-market line 308).
- **PRD:** §7.1 tests lasting consequences through "can explain how an earlier decision affected a later outcome", but nothing tests wellbeing, which is half the differentiation claim. There's no OQ for it. §2 also reports the survey without its limits (user-research lines 135-138: convenience sample, 8 respondents aged 19-20), although §7.1 states a validity limit for the playtest.
- **Fix:** add a playtest measure, for example whether a tester can say why they got a hollow win. Add one line of survey limits to §2.

**U3. Medium. Two teaching priorities weren't carried over.**
- **BSU:** user-research line 129 makes BSU and credit the priority, with BSU weakest among 15-16-year-olds (26% understand it well), and BSU is open from month 1. §2 notes this, but NFR-8 gives extra explanation only to credit.
- **Budgeting and bills:** user-research line 121 lists "budgeting and saving" first among what they wish they'd been taught, and "paying bills and invoices" also appears. Brief line 22 names budgets as well. "Budget" appears nowhere in the PRD as a topic: not a mechanism, a candidate event, or a Later item. 86% say they understand the term already, so a feature may not be justified, but nothing records that choice.
- **Fix:** add BSU to NFR-8's credit line. Add budgeting to the FR-17 candidate topics or log a decision to leave it out.

### tilbakemelding-product-brief.md

**T1. High. No minimal version that can certainly be finished.**
- **Source:** tilbakemelding line 48, "Definer en minimal versjon som sikkert kan bli ferdig, og legg resten i tydelige trinn etterpå". Line 56 rates time and scope as a risk. Line 70 suggests 4-5 mechanisms and moving førerkort to later steps.
- **PRD:** §4.1 has three cuts: lines during play, the parents' insurance share, and events down to 50. None removes a feature with real build cost. Scope has grown since the feedback (moped ownership, car licence, family loans, payment plan, NFR-11 hosting), the addendum says delivery is about five weeks away, and the playtest alone needs at least 7 days. The car licence, which the teacher named for deferral, isn't on the cut list. Neither are room layers, consumer loans, or the payment plan, and §4.1 doesn't say whether they're cuttable.
- **Fix:** extend the cut list with feature-level steps, or state which features outside the "always stay" list can go and in what order. The order is a team decision.

**T2. Low. `.env.example` is missing everywhere.**
- **Source:** tilbakemelding line 102, "Planlegg lokal database, `.env.example` og en modus uten KI". The guide lists it under criterion 6 (line 166).
- **PRD:** the local database and no-AI mode are covered. `.env.example` isn't in the PRD, the addendum, the brief, or the architecture.
- **Fix:** add it to NFR-6, or to "For the architecture" in the addendum.

### architecture_technical_design.md

**A1. Medium. The age-appropriate content rule left with the AI.**
- **Source:** architecture line 374, "Because minors are part of the intended audience, generated narrative content must remain age-appropriate". Line 280 applies the AI-specific parts from stage two.
- **PRD:** with AI out, the pre-written library has no such rule. NFR-8 covers only tobacco and alcohol, and the content check covers schema and counts. Meanwhile FR-17 makes collectibles and in-game purchases candidate topics, the survey describes one respondent "getting hooked after a lucky draw" (user-research line 114), and market-research line 14 warns that BitLife "can desensitize young minds" to recklessness and gambling.
- **Fix:** add to NFR-8: content suits a 15-year-old, and chance-based purchases are shown as a cost, never as a reward.

### extract-domain.md (with its source, the youth finance research)

**D1. Low. The BSU opening age has no disclosure.**
- **Source:** the research verdict says "Two rules need a scope label: youth minimum wages, and the age at which a player can open a BSU" (research line 23, extract-domain line 158). Guardians open and sign in practice, and Skatteetaten advises against opening under 17 without taxable work income (research line 31).
- **PRD:** FR-18 opens BSU at 15 with "no lower age". D2 labels wages, but none of D1-D23 covers BSU opening, and FR-40 says the game discloses where it simplifies.
- **Fix:** add a D24 shown at the first BSU offer.

**D2. Low. The playtest quiz has no source or owner.**
- **Source:** extract-domain line 205, the five quiz questions are proposals that need teacher review (#18, open).
- **PRD:** §7.1 uses the quiz as a target metric, but neither §7.1 nor §8 points to the questions or to #18.
- **Fix:** link the questions and #18 in §7.1 or §8.

### Inputs with no real gaps

- **market-validation.md:** everything in it is future commercial work. The parent survey was dropped by team decision, and the mission metric in §7.1 remains.
- **design-thinking-2026-10-16.md:** only the header and design challenge have content. "Learning feels self-chosen" is carried by the voluntary return metric, §2, and tips that can be ignored. Naming parents and teachers as secondary users is superseded by §2.2. See grading risk G6 for the file itself.
- **extract-product.md and extract-users-market.md:** nothing beyond the findings above.

### Qualitative ideas checked and kept

| Idea | Where it lives |
|---|---|
| A game, not schoolwork or homework | §1, §2, §7.1, counter-metrics in §7.2 |
| Grown-up, not childish | §2, NFR-8 |
| Tips, not lectures, and free to ignore | NFR-8, FR-19 |
| "That's why that happened" | §2.1, FR-38 |
| More useful than scrolling, on the bus | §1, §2.1 |
| Smoother and more rewarding than Koll på cashen | §1, addendum, NFR-10 |
| Money isn't the whole win | §1, hollow win, FR-42 |
| Plain language for a 15-year-old | NFR-8, NFR-3 |
| Family as an actor | FR-17 notes, FR-27 |

## Grading: guide part 1

The PRD meets most of what the guide asks for: running from the README in 15-20 minutes without keys (NFR-6), tests run from the README and in CI (NFR-9), wrong input and repeated actions (NFR-7), WCAG and screen sizes (NFR-1, NFR-2), and test users (NFR-6).

**G1. Would fail as written: changes from the proposal aren't described and justified (criterion 2, 20%).**
- **Requirement:** guide line 83, "At det som er utelatt eller endret fra proposal, er beskrevet og begrunnet". Step 1 of the sensor's method starts from the approved proposal (line 36). The D-E level describes a scope "klart mindre enn proposal tilsier uten god begrunnelse" (line 91). Criterion 1 also asks that "avvik fra planen er forklart" (line 58).
- **State:** the PRD and addendum never mention the proposal, and it isn't in the repo. The largest change, removing AI from the MVP, is recorded as a fact with no reason. The nearest text is §4.3, "Second stage, after the base works". Memlog L17 records it as an event, and #17 says only that the team decided. The addendum explains far smaller decisions in detail, but has no row for this one.
- **Not reopening the decision:** only the written reason is missing, and the teacher's own feedback supports it (tilbakemelding lines 48 and 71: build the engine and library first, so the game works with no AI).
- **Fix:** add the proposal to the repo or link it, and add a short "Changes from the proposal" table to the addendum, with AI as the first row. I couldn't list the other changes, because the proposal isn't available to me.

**G2. High risk: the examiner can't practically reach most of the game (criteria 2 and 4).**
- **Requirement:** guide line 39 has the sensor go through the core flows, and line 80 checks that they work "fra start til slutt". Line 167 asks for "testdata eller testbrukere ved behov".
- **State:** NFR-6 says only that the README "provides test users". A full game is five sessions at 10-15 minutes each, so 50-75 minutes. Credit, the card warning, and UJ-4 start at month 37, about 30-45 minutes in, and the endings and FR-42 come last. Both are core to the game and sit in "always stays".
- **Fix:** require in NFR-6 that test users are seeded at useful states, for example just before 18, in debt with a crisis due, and in month 59.

**G3. Low risk: README content.** NFR-6 names test users and the local inbox, but not the rest of guide lines 163-169. T2 covers the one item that's named nowhere. The simplest fix is to say NFR-6's README meets guide criterion 6.

**G4. Open, can't be closed from the repo: OQ-11 and the difficulty rating.** Part 1 of the guide has no requirement that the app contains AI, since the course is about steering AI-assisted development, so moving F5 doesn't fail part 1. The overall guide it supplements isn't in the repo. The teacher also rated the project "Vanskelig" partly for its AI (tilbakemelding lines 31 and 40), and says a hard project gives more room for a top grade (line 48). Widen OQ-11 to ask the teacher both questions.

**G5. Low risk: manual tests aren't required to leave a record.** Guide line 101 looks for documented manual tests. NFR-1, NFR-2, and the playtests require manual testing, but nothing requires results to be stored in the repo. NFR-3 deletes the code key and accounts, so the aggregated results should be kept.

**G6. Low risk, outside the PRD: an unfilled template.** `.docs/design-thinking-2026-10-16.md` is mostly `{{placeholders}}`, and it still says "AI-driven money game" and "free-tier AI". Guide line 71 marks planning documents that seem generated once and never used as D-E. Fill it in or mark it as abandoned.

## Part 2: Memlog audit

Walked all 87 entries: 45 decisions, 11 changes, 5 overrides, 6 assumptions, and 20 events. Events and process entries (working mode, journey-led) need no capture. Everything else is captured in the PRD or addendum, or superseded, except these three. The entries dated 2026-11-05 "per Dahl, for team approval" (L82-L92) were checked as current. M4, M5, M6, M8, M12, M13, G1, and the accepted group in L89 all match the PRD, the addendum, and Rule Set v1.

| Entry | What it says | Status | Detail | Fix |
|---|---|---|---|---|
| L25 (decision) | "PRD keeps the full differentiation claim from market-research.md" | Partly lost | §1 has Norway and wellbeing, but "without becoming complicated" is in neither the PRD nor the addendum, and no later entry drops it | M1 |
| L50 (decision) | Family help "not always available (17% got family help)" | Captured, with a misread figure | The decision stands in FR-27 and addendum line 97. The evidence is wrong: 17% is of all respondents, and about half of those with such an expense got help | U1. Log the correction |
| L92 (decision) | "Rule 12 gets the family-loan stress row" | PRD doesn't reflect it | Rule 12 has it: a postponed instalment adds 5 stress. FR-33 lists what raises stress as "interest on debt, crisis months, and working too much", which reads as complete, and FR-27 doesn't mention it either | Add it to FR-33 or FR-27 |

Other superseded chains checked and resolved:
- **Login:** L15, L27, and L35 are replaced by L36 and L40.
- **Moped:** L39 and L51 are replaced by L75 and L78. L53 is replaced by L87.
- **Car licence:** L52 and L60 are replaced by L71, L75, and L78.
- **Cut list and event minimum:** L16 and L61 are replaced by L75 and L89.
- **Card figures:** L56 and L59 are replaced by L76.
- **Sync:** L38 is replaced by K5 in L89.
- **Crisis triggers:** L49 and L55 are replaced by L82 for the debt trigger. The missed-minimum trigger is unchanged.

## Side findings, outside the brief for this check

**S1. Medium. Two "guaranteed" events can land in one month for goal-3 players.** The addendum's scheduling template and FR-9 place the experience event in months 42 and 54. The summer job offer also falls in month 42, and the full-time job offer in month 54. An active month gets one event, and the loser moves to the next active month (FR-46). Either the experience event misses the month FR-9 names, or the summer job offer moves from June to August, after the July it pays for. A crisis month in June moves the offer the same way for any player, and FR-32's "nothing is lost" doesn't cover offers tied to a date.

**S2. Low. The parents' insurance share has no rule.** FR-23 and cut list item 2 draw it, but rule 14 charges a flat NOK 250, the parameter table has no chance or size, and OQ-8 doesn't list it.
