---
title: Adversarial review of the LifeMode PRD
reviewed: prd.md (updated 2026-11-12), addendum.md (updated 2026-11-11), with Rule Set v1 in briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md
date: 2026-11-13
lens: adversarial (general)
---

# Adversarial review: LifeMode PRD

## Overall take

This PRD is meticulous about arithmetic and edge cases. That is exactly why its gaps are dangerous: readers will trust it. The Core tier is nearly the whole product: 46 of 57 FRs, 11 NFRs with no tiers at all, a content library of at least 40 events written in Norwegian with sources and LK20 codes, and a simulator that plays seeded runs according to fixed choice rules, which no FR names as something to build. The PRD wants it playable in about three weeks, starting from a point where UX, architecture and epics don't exist yet. Its own sequencing also makes the whole Extension tier impossible to start. The precision is uneven exactly where it counts. The §3.1 summaries misstate two rules in a way that would put UJ-4's Markus into crisis on day one. The flagship UJ-4 trace works only because it leaves out costs that its own story says Markus pays. The NOK 5,508 answer-key figure depends on a rounding rule nobody wrote down. Worst of all, the ending summary, the payoff of "the game always shows why", can't show the two settings that the worked examples prove decide the outcome: the spending level and working hours. Core FRs keep pointing at Extension and Can-be-cut FRs without saying what happens when those aren't built. Several success metrics can't fail, or can't be measured as defined. A downstream team building from this document will either guess or stall.

Findings are numbered for reference only. The order is not a ranking.

---

### AG-01: The Extension tier can never start under the PRD's own sequencing

- **location:** §4.4 Tiers (prd.md:315) and the tentative-dates table (prd.md:319-326); FR overview (prd.md:334-392)
- **trigger_condition:** "Extension is built once the core is playable from start to end." But Extensions freeze on about 26-27 Nov, and Core is due playable on about 1-3 Dec. Unless Core is playable at least 5 days early, no Extension FR may legally start.
- **guard_snippet:** Decide now, FR by FR, for each of the 8 Extension FRs: promote it to Core, or move it to Can be cut with a fallback. Alternatively, move the freeze after the Core checkpoint. State it plainly: "Extension FRs ship only if Core is playable by <date>; otherwise they are out."
- **potential_consequence:** The avatar (UJ-1 step 3), the recap (all of UJ-2), tips (the start of UJ-3, and the credit-card offer tip), consumer loans (F1), visible future opportunities (the vision), echo badges, disclosed simplifications and change-password all drop silently at the freeze. The journeys and metrics that depend on them (SM-2, SM-6) are left validating features that don't exist.

### AG-02: Core is not a minimal version, and the schedule is not achievable for a student team

- **location:** §4.4 (prd.md:298-328), FR overview, §6 NFR-1 to NFR-11, FR-17, the content-check consequences across §5
- **trigger_condition:** Core holds 46 of 57 FRs. The NFRs have no tiers: WCAG 2.2 AA with manual screen-reader testing on a phone, a one-command Docker run, CI, response targets on throttled 4G, and a hosted EU environment with a daily automated login check. On top of that come at least 40 events and about 10 crisis events, activities, invitation, offer and info messages, about 18 ending texts, D1-D26 and room-state texts, all in reviewed Norwegian with sources and LK20 codes, plus a policy-driven simulator (AG-18). The window is about 18-20 days from 13 Nov to "Core playable", with UX, architecture and epics not yet written. No checkpoint covers content authoring.
- **guard_snippet:** Define a "Core-0" walking skeleton: the engine, the two-part month, one event per active month, a basic money view, and login without reset. Give it a date around 24 Nov. Tier the NFRs. Put content authoring and the content-check harness on the schedule with owners and weekly counts. Add a checkpoint: "content minimum written and passing the schema check by <date>".
- **potential_consequence:** Core isn't playable by 1-3 Dec. The 8 Dec playtest then runs on a partial game or slips, and the analysis needed before the 17-19 Dec delivery doesn't happen.

### AG-03: Core FRs depend on non-Core FRs, with no "if not built" behaviour

- **location:** FR-28 "The recap's teaser names what the licence costs" (prd.md:984) → FR-16 (Extension); FR-42 Texts "(FR-19)" → FR-19 (Extension); the FR-18 consumer-loan row, FR-48 "What stays open", FR-45 early loan payoff, FR-55 "Offers always arrive" and the NFR-7 loan refusals → FR-25 (Extension); FR-12 replay inputs, FR-49 previews, FR-55 bank messages and NFR-7 pins → FR-57 (Can be cut, first in line); FR-53 "so echo badges ... work" → FR-37 (Extension); FR-10's avatar on the ending screen
- **trigger_condition:** Core consequences call features that are likely never built. If FR-25 is dropped, FR-55 still obliges the engine to send a month-49 consumer-loan offer for a product that doesn't exist.
- **guard_snippet:** Give every Extension and Can-be-cut FR an "If not built" block listing the Core consequences that change. For example: "FR-25 not built: remove the consumer-loan row from FR-18, its month-49 offer from FR-55, loans from FR-48 and FR-45, and the loan refusals from NFR-7; F1 stays as an engine unit test only."
- **potential_consequence:** Developers either build Extension work under Core stories, or ship Core screens and acceptance tests that point at nothing. Either way, the tiers stop meaning anything.

### AG-04: The rule for when to cut contradicts the checkpoint table, and nothing covers a Core miss

- **location:** §4.4 "When to cut" (prd.md:317) against the dates table (prd.md:321-326)
- **trigger_condition:** The prose says that if the month loop isn't playable "at the first checkpoint, the first six items apply at once". In the table, the first checkpoint is the Extension freeze, whose consequence is "Extension FRs not started are left out". The second (Core playable) drops "the whole Can be cut tier". Nothing stops Can-be-cut work, such as the driving game, from being built before Core. Nothing says what happens if Core still isn't playable on 8 Dec. Dropping a tier that's already half-built saves no time.
- **guard_snippet:** Use one table: checkpoint, the test for "met", and the exact items dropped. Add "No Can-be-cut work starts before Core is playable." Add a Core-miss rule, for example "If Core isn't playable by 5 Dec, the playtest covers years 1-3 only" or "the playtest moves to <date>".
- **potential_consequence:** At the checkpoint the team argues over which rule applies. Meanwhile fun Can-be-cut items have already eaten Core time.

### AG-05: The cut order protects login hardening ahead of the game itself

- **location:** §4.4 cut item 11 (prd.md:311)
- **trigger_condition:** Per-network limits, the daily email cap, the "stay logged in" choice, **Log out on all devices** and the 12-month deletion job are cut *last*. They outrank room layers, the driving game, the car licence and gift mopeds, all for a closed playtest of 10-20 invited 18-20-year-olds.
- **guard_snippet:** Move item 11 to position 1 or 2, or move it to a before-go-live list now. Keep create user, login, logout, delete account and the failed-login pause.
- **potential_consequence:** Build time goes to anti-abuse controls no playtester will touch. Meanwhile the player-facing content that SM-7 ("felt like a game") measures is the first to go.

### AG-06: NFR-3 promises a deletion that the cut list removes

- **location:** NFR-3 "deleted after 12 months without play ... The player information says so" (prd.md:1288); §4.4 item 11 (prd.md:311)
- **trigger_condition:** The NFRs have no tiers, so NFR-3 still requires the player information to promise deletion after 12 months. Cut item 11 removes the job that performs it. FR-5 (Core) likewise still promises **Log out on all devices**.
- **guard_snippet:** Add to NFR-3: "If the 12-month job is cut, the player information must not state it." Or keep the job: it is one scheduled task. Mirror this in FR-5 for log-out-on-all-devices.
- **potential_consequence:** The privacy text tells players as young as 15 that their data is deleted when it isn't.

### AG-07: The §3.1 one-line summaries misstate rules 5 and 8

- **location:** §3.1 rows 5 and 8 (prd.md:231, 234); §0 says FRs rely on §3.1 and restate a rule only "where it needs the detail"
- **trigger_condition:** "the minimum (3.5% or NOK 300)" and "debt above 3× wage or NOK 5,000" read as OR. The rules say "the larger of". The rule 8 row also leaves out that a positive current account and savings are subtracted and that family loans are excluded.
- **guard_snippet:** Row 5: "the minimum is the larger of 3.5% of the balance before the month's interest and NOK 300". Row 8: "net debt (card + consumer loans + payment plans − positive current account − savings, never below 0, no family loans) above the larger of 3 × the average monthly wage over 3 months and NOK 5,000".
- **potential_consequence:** A developer who implements the summary as written puts every card balance above NOK 5,000 into crisis. Markus in UJ-4, at NOK 10,000, would be in crisis immediately, and the flagship journey breaks.

### AG-08: The card minimum has no rounding rule, and the answer key depends on one

- **location:** Rule 5 (brief addendum:72); UJ-4 step 2 (prd.md:131); FR-26 and FR-31; the addendum's UJ-4 trace; worked example 12
- **trigger_condition:** 3.5% of a balance produces fractions (NOK 9,314 → 325.99), and rule 2 defines rounding only for interest. Recomputed, NOK 10,000 paid at the minimum gives 51 months and NOK 5,508 with round-half-up, NOK 5,512 with floor, and NOK 5,503 with ceiling.
- **guard_snippet:** Add to rule 5: "The minimum is rounded under rule 2 (0.5 rounds up)." Add a worked example whose minimum is fractional.
- **potential_consequence:** Two of the three reasonable implementations fail the UJ-4 figure and the card-warning test. The engine then gets "fixed" by trial and error until the test passes.

### AG-09: UJ-4 works only by leaving out costs its own story says Markus pays

- **location:** UJ-4 persona and entry state ("fuel for his moped and for his parents' car", prd.md:127-128); addendum "UJ-4 month by month" (addendum.md:46-67); brief examples 17a and 23; the parameter table (moped fuel NOK 186 a month in April-October, car fuel NOK 991 a month)
- **trigger_condition:** The trace's costs are mobile (NOK 299) and insurance (NOK 250). Moped fuel is "left out until #43", although the parameter table now has a figure. Car fuel isn't mentioned, although the story has him borrowing the car. Re-running the trace under rules 1, 2, 5 and 16:
  - **Moped fuel added:** payoff takes W+6, not W+5, with NOK 771 in interest instead of NOK 682.
  - **Car fuel added too:** month W pays NOK 0, which is a missed minimum, and payoff takes about 15 months.
- **guard_snippet:** Recompute UJ-4, 17a and 23 with every cost the story names. Or rewrite the story so he never borrows the car and the moped is parked. Mark the trace as provisional until #43 closes. Add an engine test that replays the trace with the configured costs.
- **potential_consequence:** Once real parameters load, the engine can't reproduce the PRD's showcase journey or its "after five months" climax, and UX copy and playtest material built on it will be wrong.

### AG-10: The extra hours in UJ-4 use a mechanism that doesn't exist, and the card warning has no specified options

- **location:** UJ-4 step 4, "raises his hours from 10 to 12" (prd.md:133); the addendum trace, "asks for one extra 2-hour shift a week" (addendum.md:64); example 17a, "asks for 2 h more a week (social −5)"; FR-47 and FR-55 (extra shifts come only from an employer offer or an event option, by default +4 h for 3 months); FR-31
- **trigger_condition:** Three documents give three different mechanisms for the same action. The −5 social in 17a needs a card-warning option with a stated effect, but FR-31 lists only example actions. Extra shifts at the defaults can't produce +2 h for five months. Nor does anything say whether the card warning is a library event under the FR-17 schema (2-4 options, at least one with no cost) or something the engine builds.
- **guard_snippet:** Pick one mechanism: "Markus raises his hours setting to 12 from the job view, with no wellbeing effect of its own", and recompute 17a. Then specify the card warning in FR-31: where it comes from (library or engine), its options, their money and wellbeing effects, and which options are always present.
- **potential_consequence:** Example 17a can't be written as a unit test from the FRs, and the core event of UJ-4 is authored ad hoc.

### AG-11: No FR guarantees "The game always shows why"

- **location:** §1 Vision (prd.md:25); §5.13 description (prd.md:1107); FR-38 (prd.md:1131-1138); FR-13; FR-14
- **trigger_condition:** FR-38 lets the player press "Hvorfor?" "on a change" but never lists which changes or screens carry the button. FR-13 promises "why" only in active months. The quiet-month summary (FR-14), which is 8 of every 12 months, has no "why" requirement. Nothing requires a rule-based explanation to include the player's own inputs, such as "free time 48 because 30 h of school + 26 h of work". Dropped activities, declined card purchases, automatic transfers from savings, slot-count changes, skipped crises and bank messages have no explicit "Hvorfor?". UJ-3 step 2 presses "Hvorfor?" on a bank message, which FR-54 doesn't provide for.
- **guard_snippet:** Add a coverage table to FR-38. Each month-summary line, each change to a wellbeing part, the slot count, each change to a money-view balance, a dropped activity, a declined card purchase, an automatic transfer, a crisis start or skip, each bank message and each ending entry carries "Hvorfor?". The explanation names the choice or rule and the engine figures that went into it. Test it by listing every effect type and asserting that each one has an explanation.
- **potential_consequence:** UX decides where the button goes. The vision's headline promise, and SM-1 and SM-3, end up resting on placement nobody specified.

### AG-12: The ending summary can't show the levers that decide the ending

- **location:** FR-36 System causes (prd.md:1119: spending and wages are system causes; setting a level or hours "isn't ranked"); FR-42 (prd.md:1184-1195); the glossary "Choice ... Any choice can be a cause" (prd.md:166); UJ-5's second playthrough (prd.md:151); brief examples 17b and 21
- **trigger_condition:** The worked examples show that the spending level and weekly hours drive both money and wellbeing. Example 21a (high spending to month 54) misses the goal, and example 17b (40 h a week) gives the hollow win. Both levers are excluded from the kroner ranking. Their wellbeing effects (the −2 social on low spending, the +5 stress and −5 social below 50 free time) link to rules, not to the setting. UJ-5 promises "the choice that hurt his wellbeing most, so he can see why", but the real cause can't appear. FR-42 instead shows whichever event option had the largest negative wellbeing effect, or the "largest system cause". The glossary and FR-36 also contradict each other on whether a money action can be a cause.
- **guard_snippet:** Make each change of spending level and hours a choice with linked effects: the difference from the previous setting, for as long as the new setting lasts. Or add a fixed "Your settings" block to the ending: months at each spending level, with the kroner difference against normal, and months above 25 h, with the wellbeing points lost. Fix the glossary.
- **potential_consequence:** The ending lies by omission. A careless player is shown a concert and a phone screen as reasons, not 50 months on high spending. The survey's most common regret, small purchases that add up, stays invisible, and SM-3 measures the wrong thing.

### AG-13: FR-39 has no comparison for the choices most likely to make the top three, and the goal-3 purchase gets an "avoid this cost" tip

- **location:** FR-39 "the option in the same event" (prd.md:1145); FR-42 Kroner effect and Texts (prd.md:1189, 1193); FR-48; the message schema (addendum.md:154-164), which has no ending-text field
- **trigger_condition:** The largest money effects in a playthrough come from open options, not event options: the car licence (NOK 32,500), a moped (NOK 29,000 new or NOK 11,645 used), the moped licence (NOK 12,000) and the experience (NOK 60,000). FR-39 defines a comparison only for event options and activity groups. For a goal-3 player, the NOK 60,000 experience that the goal requires ranks first, and FR-42 attaches "a tip on how the cost could have been avoided". Open options can't override that text, because their offer messages have no ending-text field.
- **guard_snippet:** Define FR-39 for open options as "not taking it": the price plus its linked running costs, grown with savings interest. Give the goal-3 experience a "goal purchase" text instead of the cost-avoidance tip. Add an ending-text field for open options.
- **potential_consequence:** In UJ-5's "opens one to see how things could have gone", most of the top entries fall back to generic text. Goal-3 winners are told they should have avoided their goal.

### AG-14: FR-47 and FR-55 contradict each other on the summer-job offer

- **location:** FR-47 Monthly cap, "no summer job is offered, and the game says why" (prd.md:880); FR-55, "Offers always arrive ... A player who doesn't qualify yet still gets it ... Nothing can push an offer out" (prd.md:798); addendum D4
- **trigger_condition:** Take a player at 40 h a week in June. FR-47 says the summer job isn't offered. FR-55 says the offer message arrives and shows what's missing. FR-55's exception list doesn't cover the case.
- **guard_snippet:** Add to FR-55: "except the summer job when the 173 h cap leaves 0 h; its message then arrives as info and says why". Or reword FR-47 to match FR-55.
- **potential_consequence:** Developers pick one reading, and tests written from the other fail.

### AG-15: FR-13 states a requirement that OQ-9 calls undecided, and the OQ says it blocks nothing

- **location:** FR-13, "Every option states its wellbeing effect" (prd.md:606); FR-33 (prd.md:1078); OQ-9, "whether an option's wellbeing effect is shown before the pick | Blocks: Nothing" (prd.md:1450)
- **trigger_condition:** The same behaviour is a requirement in one place and an open question in another. It shapes the event screen, NFR-8's "not a quiz", and FR-39's "no figure to show" fallback.
- **guard_snippet:** Decide now. If the effect is shown, specify the format. If not, reword FR-13 to "every option has a stored wellbeing effect". Mark OQ-9 as blocking the event UI.
- **potential_consequence:** UX and development build opposite versions, and the playtest tests a game nobody chose.

### AG-16: Open questions that can sink the delivery are marked "Blocks: Nothing"

- **location:** §8 OQ-11 (prd.md:1451) and OQ-12 (prd.md:1452); §9 A-26
- **trigger_condition:** OQ-11 asks whether an app with no AI meets the course requirement. The lecturer's difficulty rating leaned on in-app AI. The question has no deadline, no contingency, and "Blocks: Nothing". OQ-12 asks whether FR-1's typed-twice email field conflicts with WCAG 2.2 criterion 3.3.7, which NFR-2 requires. It also blocks nothing.
- **guard_snippet:** Give OQ-11 a deadline before epics are frozen, plus a pre-scoped contingency, such as one bounded AI feature behind a flag that never sets an amount. Make OQ-12 block FR-1's acceptance.
- **potential_consequence:** The team may learn at grading that the MVP's central premise fails the course, or ship an FR that fails its own NFR.

### AG-17: The reference run in FR-9b isn't the run in worked example 20, and a cross-reference is mislabelled

- **location:** FR-9b Reachable (prd.md:527) against brief example 20; FR-33, "careless run 21c" (prd.md:1080)
- **trigger_condition:** FR-9b describes the run as "starts with NOK 10,000, works 10 h a week, and stays on normal spending". Example 20 actually has no job until month 19, takes the three summer jobs, works 10 h a week from month 20 and full-time from month 55, and moves all spare money to savings at every choice step. FR-33 calls 21c "careless", but 21c is low spending all the way, the frugal run that reaches the goal.
- **guard_snippet:** In FR-9b, write "exactly the run in worked example 20", or list its full parameters. Correct the 21c label.
- **potential_consequence:** The content-check gate, which "fails if this run misses goal 1 or goal 2", gets coded against a different run, so it passes or fails for the wrong reason.

### AG-18: The content check is an unnamed Core deliverable, and the PRD expects it to fail CI

- **location:** FR-9b, FR-17, FR-33, FR-43, FR-46b-c, FR-52, FR-55; NFR-9 (prd.md:1370); addendum, "The check runs 1,000 seeded playthroughs" (addendum.md:100)
- **trigger_condition:** The content check needs a simulator that plays seeded runs by fixed rules: careless and careful runs, policies for crises and activities, pairs of random-choice runs, pairs with the same seed, a sweep over slot counts, and boundary runs. It must run on every pull request. FR-9b says the "careful player with some free time" run "is expected to need tuning", which means it is expected to fail, until OQ-17 closes. The tuning deadlines are 8 Dec.
- **guard_snippet:** Make the content check an epic with its own tier and estimate. In CI, separate the hard gates (schema, references) from the balance reports. Let the balance checks warn rather than fail until a stated tuning-freeze date.
- **potential_consequence:** Either CI is red on every PR for weeks and gets switched off, or the simulator is never built and every balance claim in the PRD goes untested.

### AG-19: The worked examples are the answer key, but their tuning values are finalized on playtest day

- **location:** NFR-4, "The worked examples are the test answer key" (prd.md:1303); the brief parameter table (deadline "Playtest start (8 Dec)" for spending shares, weights, threshold and start values); the brief's note that examples 17, 20, 21, 22 and 23 were wrong twice and recomputed by script (brief addendum:258)
- **trigger_condition:** Examples 17b, 20-23 and 26 depend on tuning values that may change until the playtest starts. The answer key has already been wrong more than once. Nothing says who regenerates it, or how a disagreement between the engine and the key is settled.
- **guard_snippet:** Freeze a separate test configuration for the worked examples, so tuning the play configuration doesn't move the tests. Name the person who triages a disagreement between engine and key, and require an independent second computation before the key changes.
- **potential_consequence:** Either the engine gets coded to match a wrong key, or every tuning change breaks dozens of tests the day before the playtest.

### AG-20: The pace target conflicts with four game areas visited every month

- **location:** FR-46a Pace (prd.md:664); SM-11; CM-4 and CM-5 (prd.md:1430-1431); the §5.4 description; FR-52 "Same as last month"
- **trigger_condition:** A 10-15 minute session covers 12 months. Each month has a summary, up to 3 messages, a plan of up to 4 slots, and the job and money views. Add 4 events and possibly a minigame, and the budget is roughly 60-75 seconds a month. There's no time budget per month. The thesis needs players to plan, the pace target needs them to skip planning, and CM-4 and CM-5 pull in opposite directions with no rule for which wins.
- **guard_snippet:** Set a time budget per month, for example a quiet month with planning in 45 seconds or less. Pre-agree the response: if CM-5 fires, cut messages to 2 a month and repeat last month's plan automatically. Otherwise, relax SM-11 now.
- **potential_consequence:** The playtest shows either long sessions (CM-5) or ignored planning (CM-4), and the team has no pre-agreed action for either.

### AG-21: Several metrics can't fail, or can't be measured as defined

- **location:** §7.1 SM-2, SM-6, SM-10 and SM-12 (prd.md:1403-1413); FR-11 (prd.md:552); FR-1 (prd.md:414); FR-50 (prd.md:1244)
- **trigger_condition:**
  - **SM-2:** "Higher after" has no minimum gain. With 10-20 testers and a quiz still awaiting review (#18), a +0.1 noise gain passes.
  - **SM-6:** "Voluntarily" is unmeasurable for recruited testers. A full game takes about an hour, so SM-5's completion target already requires several sittings.
  - **SM-10:** It counts from creating the user, while FR-11 counts from opening the game. FR-1 cites the 2-minute target as its reason for having no email confirmation, so the measurement excludes the very step it is meant to protect.
  - **SM-12:** "At least one, noted by the team" can't fail.
- **guard_snippet:**
  - **SM-2:** Set a minimum mean gain and a date for the teacher's sign-off on the quiz.
  - **SM-6:** Redefine it as a sitting on a later calendar day than the tester's first one, or drop "voluntarily".
  - **SM-10:** Measure from the first screen load.
  - **SM-12:** Define who counts and how many, or remove it.
- **potential_consequence:** The success claims in the report can't be falsified, and the examiner sees metrics designed to pass.

### AG-22: The playtest validates nothing about the primary persona

- **location:** §7.1 Validity limit (prd.md:1423); NFR-3 Playtests (prd.md:1292); NFR-8 (prd.md:1358, 1364); UJ-1 to UJ-6
- **trigger_condition:** All testers are 18-20. The persona is 15-17, and most of the journeys happen before 18. NFR-8's "plain language a 15-year-old understands" and "all content suits a 15-year-old" have no test at all. Even so, SM rows claim to validate UJ-1 and UJ-3.
- **guard_snippet:** Say in each SM row that it is valid for ages 18-20 only. Add a check of the Norwegian text for 15-17-year-olds before 8 Dec, such as a review by a teacher or a readability review, with an owner.
- **potential_consequence:** The delivery claims the thesis holds for the target group when it was tested on a different one.

### AG-23: Under the PRD's own rules, a tester code can't be attached to an account

- **location:** FR-50 Tester code and Deleting an account (prd.md:1246, 1249); §4.2, "type free text beyond the email address" (prd.md:271); NFR-3
- **trigger_condition:** The team hands out the code with the invitation. The player can't type anything but an email address. The email-to-code key is "kept apart from the results", yet "a tester who creates a user again with the same email address keeps the same tester code", which requires the system to hold that key. Deleting an account also deletes the record, while the re-created account keeps the code, so the same tester is counted both as having left and as active.
- **guard_snippet:** Specify the mechanism. Either the team pre-loads email-to-code in the playtest environment, accepting that the key lives there, or the invitation link carries a signed code that is never typed. Define how a tester who deletes and re-creates an account is counted for SM-5 and SM-6.
- **potential_consequence:** The records can't be joined to the quiz and survey answers (SM-1 to SM-4), or the privacy separation is quietly broken.

### AG-24: Seeded test users clash with cause links and replay

- **location:** NFR-6 seeded users (prd.md:1315); FR-51 "seeded test users already hold a licence" (prd.md:1229); FR-36 and F10 (prd.md:1116); FR-12 Reproducible (prd.md:584); FR-42
- **trigger_condition:** A state injected at month 59 has no choice history. F10 requires every cause link to point to a choice that exists. FR-42 needs choices to rank, and FR-12 needs a replay from the starting values plus the choices.
- **guard_snippet:** Require seeded users to be produced by scripted playthroughs from month 1 with their choices recorded, not by injecting state. Otherwise define a "seeded" system cause and exempt such users from F10 and FR-12 explicitly.
- **potential_consequence:** NFR-6 makes these users the examiner's only practical route to the ending, and they will show an empty or broken ending summary.

### AG-25: The pengegave event, the one event every playthrough has, is unspecified, and the schema can't express it

- **location:** FR-11 (prd.md:544-552); FR-46a First choice; the FR-39 example (prd.md:1147); addendum Option fields (addendum.md:118-134)
- **trigger_condition:** The pengegave is drawn between NOK 10,000 and NOK 30,000. Options in the schema have a fixed money effect or an amount the player enters. There's no effect for moving money to savings or BSU, yet FR-39's own example is «Hadde du valgt å spare alt». There's no effect sized as a share of the drawn amount. FR-39's "option whose direct kroner effect differs most" is undefined when the player enters the amount.
- **guard_snippet:** Specify the pengegave event in FR-11: its options, effects as shares of the drawn amount, and a transfer to savings or BSU. Add those effect types to the option schema. Define the FR-39 comparison for an amount the player enters.
- **potential_consequence:** The first screen of every playthrough, which carries the 2-minute target, gets designed ad hoc, and the PRD's own FR-39 example can't be produced.

### AG-26: The failed-login pause hands classmates a way to lock a player out

- **location:** FR-2 (prd.md:422: 10 failed logins in 15 minutes pause that address); FR-1 (prd.md:409: sign-up reveals that an address has a user); UJ-2 (a school PC)
- **trigger_condition:** Anyone who knows or checks a classmate's email address can lock them out again and again with 10 bad attempts every 15 minutes. The PRD considers a school class sharing one network, but not targeted abuse.
- **guard_snippet:** Apply the pause per address and network pair, or slow down only the failing network or device, while the reset link still logs the real player in. Otherwise, document the risk as accepted.
- **potential_consequence:** Among 15-year-olds, the trick spreads fast. Players lose access, and the return rate falls.

### AG-27: Status and precedence are unreadable, and a binding decision lives only in the addendum

- **location:** front matter `status: draft` (prd.md:3); §0 Status (prd.md:14); §4.4 "set 2026-11-13" against OQ-13 still open; addendum notes marked superseded but kept inline (addendum.md:15-22, 272-275, 391, 414); active-month positions only in the addendum (addendum.md:71)
- **trigger_condition:**
  - **Status:** The document is "draft", "final for UX and architecture" and "being revised" at once, with dates that are "set", "tentative" and "waiting for the team".
  - **Superseded text:** The addendum keeps superseded guidance inline, such as Supabase login limits, a reset fallback through "the login service's admin tools", "X3: at least 50 regular events", and "OQ-6 blocks the first playtest".
  - **Active months:** Months 1, 4, 7 and 10 are stated only in the addendum. UJ-6 and example 17a depend on them, yet §0 says a decision applies downstream only once it's written into the PRD.
- **guard_snippet:** Use one status line that says what is frozen. Move the active-month positions into FR-46a. Delete superseded addendum text instead of annotating it. Move the change history out of §0.
- **potential_consequence:** The architect builds on superseded guidance. Developers treat the active months as free configuration and break UJ-6 and the examples.

### AG-28: Parts of the monthly loop still have to be guessed from the FRs and Rule Set v1

- **location:** FR-12 (prd.md:577); FR-23 Everyday costs (prd.md:919); FR-30; FR-55 Bank messages and How many (prd.md:797, 800); FR-49 flowchart (prd.md:569); rule 1
- **trigger_condition:**
  - **(a) Start of option costs:** Nothing says whether an everyday cost started by an option in month M, or car borrowing, is first charged in M or M+1. The fixed-cost step has already run when the month opens, and only rule 14 answers this, for mopeds.
  - **(b) Bank messages:** Their place under the 3-message cap relative to invitations and info messages is undefined, and so is the moment "passes 25/50/75/100%" is measured. The goal-1 measure (net savings) and the savings-target measure (current account + savings) can also report contradictory progress.
  - **(c) BSU deduction:** It is missing from FR-12's processing order and appears only in a flowchart.
  - **(d) Messages and seeding:** FR-55 says messages are drawn "from the playthrough's seed", but bank messages depend on state, not the seed.
- **guard_snippet:**
  - **(a)** Add "An option-started cost is first charged in the next month's fixed-cost step and last charged in the month it is stopped", mirroring rule 14.
  - **(b)** Define bank messages as one priority class (offers > bank > invitations > info) and say that progress is measured after the month opens.
  - **(c)** Add the December BSU step to FR-12's order.
  - **(d)** Separate drawn messages from triggered ones.
- **potential_consequence:** Two developers will implement two different month loops. The worked examples, which never exercise these cases, won't catch the difference.
