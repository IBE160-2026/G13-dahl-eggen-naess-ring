---
title: LifeMode PRD, independent review
date: 2026-11-05
reviewed: prd.md (draft, PR #52), with the brief addendum (Rule Set v1) and the PRD addendum as support
---

# Independent PRD review, 2026-11-05

Run with `bmad-review` on `prd.md`. Lenses: adversarial (A) and edge-case-hunter (E). The two ran separately, without the earlier review reports or session logs, and recalculated the figures with their own scripts. Scope: the seven final-check decisions, FR-51, V2, and worked examples 17, 20 and 21, which no independent reviewer had checked. All findings are also in `review-2026-11-05-independent-findings.json`.

Findings: A 47, E 55; 102 in total. No severity or ranking. No findings have been applied.

## Where the lenses agree

Overlap is signal, not duplication.

| Theme | Findings |
|---|---|
| Spending level changes wellbeing when nothing is spent | A1, E1 |
| Spending against a negative balance, and the FR-45 charge lists | A5, E2 |
| The careless run is a thin and undefined test | A7, E7, E9 |
| Worked examples 20, 21d and 17b don't match the rules or their labels | A16, E53; A8, E54; A9, E55 |
| Goal 3 has no careless-run requirement | A11, E8 |
| Family loans and payment plans can't be paid off early, so goal 2 can be out of reach | A13, E10 |
| Easing off before month 37 still gives a real win | A17, E26 |
| Social life at 0 still gives a real win | A18, E27 |
| The stress cap above 50 and the order of effects | A21, E28 |
| A loan in month 60 can clear the loss ending | A22, E16 |
| Milestones that repeat, get pushed out or are lost | A23, A24, E24, E31, E35 |
| When the part-time job is first offered | A25, E36 |
| A crisis month runs after next month's income has solved the problem | A29, E13 |
| Options in a crisis that can't help or that repeat | A30, A31, E18, E23 |
| The debt trigger ignores money in the current account | A33, E11 |
| The device can report a minigame result it didn't earn | A36, E47 |
| The minigame lifecycle: abandon, offline, second result, continue, not passed | A37, E45, E46, E48, E49, E50 |
| The way past a minigame exists in the playtest build | A40, E51 |
| Time and session metrics are not measurable as defined | A41, E41 |
| FR-50 records and account deletion | A42, E37 |

## Checked after the lenses reported

The main session recalculated these with its own script or read them against the PRD. Other findings are as the lenses reported them.

| Findings | Claim | Result |
|---|---|---|
| A9, E55 | Example 17b uses uncut summer jobs on a 40 h week | Confirmed. NOK 590,662 uncut, NOK 567,315 under the rule 10 cap. Ending wellbeing is 41 in both |
| A8, E54 | Example 21d's label doesn't match its figure | Confirmed. NOK 107,685 needs summer jobs and low spending throughout. With no job at all it is about NOK 77,000 (77,181 in this check, 76,957 from E54, because of interest order) |
| A16, E53 | Example 20 depends on one pot earning interest on the same month's wage | Confirmed. NOK 119,299 as published, NOK 119,014 in rule 1 order with monthly transfers, about NOK 115,200 with no transfers |
| A7, E7 | The careless run flips on small changes | Confirmed. 40 h full-time NOK 100,762, low from month 53 NOK 102,068, keeping NOK 3,200 NOK 100,060. Months 55-60 add NOK 83,311 of NOK 96,365 |
| A2 | Timing the spending level beats normal | Confirmed. NOK 140,570 and wellbeing 87 against NOK 119,299 and 75 |
| A3 | Costs shrink the spending base | Confirmed. NOK 12,000 of costs lower net savings by NOK 620 on high, 3,094 on normal and 6,185 on low |
| A1, E1 | The level moves wellbeing with no wage | Confirmed for a run with no wage at all: 92, 80, 62. E1's run differs and gives 90, 78, 61 |
| A14 | A moped run lands near the target | Confirmed in substance. This check gives NOK 100,249 and A14 gives NOK 99,947, so it sits on the line. The two differ on small assumptions |
| A17, E26 | Easing off at month 37 | Confirmed. NOK 457,247, ending wellbeing 56 in this check and 55 from the lenses, a real win either way |
| A18, E27 | Social life at 0 | Confirmed. Social life reaches 0 at month 30 on low. Ending wellbeing 57 |
| A19 | Cliff at 25 h a week | Confirmed in substance. 69 at 25 h and 41 at 26 h in this check, 68 and 39 in A19, which assumes slightly different hours |
| A20 | The careless run scores best | Confirmed. Careless 87, reference 75 |
| A22, E16 | A loan in month 60 can clear a trigger | Confirmed against FR-9, FR-48 and rule 8 by reading. Not run in an engine |
| A36, E47 | The server can't check a minigame result | Confirmed against FR-51 by reading |
| A23 | Milestone count against FR-43 | Formula confirmed: 11 milestones give 16.0 of 25 (64%), 13 give 16.9 (68%) at 50 events. The count itself comes from A23 |

## Adversarial

### Spending level (FR-23, rule 16)

**A1** (FR-23 "It costs something either way"; rule 12; rule 16)

- Problem: The ±2 social effect depends on the level setting, not on money spent. A player with no wage on high spends NOK 0 and still gains +2 social a month. No-job runs all end at net −NOK 1,730, with ending wellbeing 92 on high, 80 on normal and 62 on low.
- Fix: Apply the social effect only in months where spending > 0, or scale it to kroner spent. Add a test: "no wage, high: social unchanged".
- Consequence: The best wellbeing setting is free for jobless players, and low penalises someone who has nothing to cut. The claim in FR-23 is false, and a test written from it will fail.

**A2** (FR-23 "A change in the money view applies from the next month"; rule 16)

- Problem: The level can change every month with no friction, so the normal default is beaten on both money and wellbeing. On example 20's jobs, normal gives NOK 119,299 and wellbeing 75. Low in months 19, 31, 43 and 55-60 and high otherwise gives NOK 140,570 and 87. Alternating (high in even months, low in odd) gives NOK 143,290 and 75.
- Fix: Base spending on a rolling 3-month wage average, or exclude the summer job from the base. Or add a minimum hold of 3 months per level. Add a content-check rule that no timing pattern beats normal on both axes.
- Consequence: The "monthly lever" becomes a timing trick around big pay months, not a trade-off. Advanced players see through it, and it teaches nothing about habits.

**A3** (Rule 16 base "after tax, fixed costs and everyday costs"; FR-23 everyday costs; FR-36; FR-39; FR-42)

- Problem: Costs shrink the spending base, so spending absorbs most of them. A NOK 500 monthly cost from month 37 (NOK 12,000 charged) lowers final net savings by NOK 620 on high, NOK 3,094 on normal and NOK 6,185 on low. Cause links and the ending will still show the full NOK 12,000.
- Fix: Take the share from wage after tax only, with costs on top, then re-run UJ-4 and examples 17, 20 and 21. Or make FR-39 and FR-42 report the net effect after spending.
- Consequence: M12's event-started costs and the moped's running costs barely bite. The survey's top regret, small purchases adding up, is not modelled. FR-39's "you would have had X more" overstates the real difference by up to about 20× on high.

**A4** (FR-31 and FR-32 "extra shifts"; FR-47; rule 16)

- Problem: Extra wage is also spent automatically. Taking +2 h for 5 months (NOK 8,450 gross) adds only NOK 328 by age 20 on high and NOK 1,655 on normal. The option's text says nothing about this.
- Fix: The option must show the kroner it frees at the current level. If the player is on high, pair it with the option to lower the level.
- Consequence: A player in trouble picks the "realistic action", gets almost nothing, and sees no explanation. That breaks "the game always shows why".

**A5** (FR-45 "always charged" and "never below NOK 0" lists; rule 16; FR-25; rule 15)

- Problem: Spending appears in neither list, and it runs before the debt step. FR-45 says income pays off a negative balance first. Take −NOK 2,500, wage NOK 8,452, high: 7,903 × 95% is still spent, so the balance shrinks by only NOK 395 a month. Also, NOK 395 left against a NOK 1,805 instalment forces a negative balance every month.
- Fix: State one of two rules. Either spending can't exceed what the current account holds after costs, or it can go negative and the summary says so. Add a worked example of each with a negative start and with a loan.
- Consequence: Two developers will build different engines. A recurring below-zero crisis can come from a percentage the player set years earlier, and the summary won't explain it.

**A6** (FR-36 "System causes"; FR-42; addendum "The ending screen")

- Problem: Spending is the game's largest money outflow after wages, yet it has no defined cause. Setting a level is a money action, and the glossary says any choice can be a cause. If it links, one tap on "high" tops every ending. If it doesn't, F10 has no rule for the default level. The addendum settles this only for wages. Interest on spending put on the card also has no choice to share to.
- Fix: Add to FR-36: "Spending has a system cause. Level changes are excluded from FR-42's ranking but explained in Hvorfor?". Say how card interest on spending is attributed.
- Consequence: The top-three ending, the core of UJ-5, is either dominated by one setting or inconsistent with F10.

### NOK 100,000 target and careless run (FR-9, examples 20, 21)

**A7** (FR-9 "Earlier play has to matter"; example 21a)

- Problem: In 21a, months 55-60 produce NOK 83,311 of the final NOK 96,365 (86%). The miss is NOK 3,635, and any of these small changes flips it: full-time at 40 h, which FR-47 allows (NOK 100,762); low from month 53 instead of 55 (NOK 102,068); or keeping NOK 3,200 of the pengegave (NOK 100,060).
- Fix: Replace the single careless run with a grid of careless variants that must all miss. Fix the root cause by reducing what six months can do: a fixed household contribution from month 55, or a goal also checked at month 54.
- Consequence: The automated test passes while the requirement is false. Six months of low spending erases 54 months of carelessness, the opposite of §1's "every choice carries forward".

**A8** (Example 21d; FR-9; NFR-4 "worked examples are the test answer key")

- Problem: The row reads "No job before month 55, pengegave spent, low from month 55" and gives NOK 107,685, Reached. That figure only reproduces with all three summer jobs and low spending in every month, summers included. As labelled it gives NOK 77,181 with no summer jobs (and −NOK 9,666 at month 54, so repeated crises the row ignores). With summer jobs it gives NOK 92,597 on normal before 55 and NOK 80,636 on high.
- Fix: Relabel it "summer jobs only, low all the way", or correct the value and the verdict. Add the crisis months if the balance goes negative.
- Consequence: A unit test built from the label fails, and the tuning decision rests on a verdict that flips to Missed.

**A9** (Example 17b; FR-33)

- Problem: NOK 590,662 reproduces only if the 120 h summer jobs are paid on top of 40 h weeks: 293 h in months 19 and 31, 163 h in month 43 is fine. That breaks rule 10's 173 h cap and FR-47. With the cap applied, the run gives NOK 567,315. The wellbeing values (41, 45, 35, 55) do match.
- Fix: Correct the example to NOK 567,315 and note the cap. Add a cap assertion to the script behind examples 17, 20 and 21.
- Consequence: The answer key contradicts the engine rule. Either the test fails, or a developer removes the cap to make it pass. The claim that the earlier script was independently checked is also unreliable.

**A10** (FR-43 "Starting over"; addendum "player can still reroll the pengegave ... harmless")

- Problem: Rerolling isn't harmless. A NOK 30,000 draw is worth about NOK 34,500 at 20. Keeping it with no job at all before month 55, then low from 55, gives NOK 111,579, which reaches goals 1 and 2. FR-9 tests only the NOK 10,000 start.
- Fix: Run the careless and lazy grids at both NOK 10,000 and NOK 30,000. Either narrow the draw or accept and record this outcome.
- Consequence: Restarting at the first screens until a high draw appears makes goals 1 and 2 reachable with almost no play, and no test sees it.

**A11** (FR-9 goal 3; rule 13; example 18j and 18k)

- Problem: FR-9 requires the careless run to miss only goals 1 and 2. Goal 3's price is "clearly below NOK 100,000", so 21a's NOK 96,365 reaches it at any such price, and no test covers this. Rule 13 also makes buying irrelevant: bought (A − P + P ≥ P) and not bought (A ≥ P) are the same inequality.
- Fix: Add a careless-run requirement for goal 3. Make the goal require the purchase, or give the purchase a wellbeing effect that matters.
- Consequence: Goal 3 is close to a free win. The offers in months 44 and 56, the event slots and the NFR-7 refusal all exist for a purchase that changes nothing. A rational player never needs the experience.

**A12** (FR-9 goals 1 and 2; example 21 column "Goals 1 and 2")

- Problem: With the buffer at NOK 100,000, goal 2 is a strict subset of goal 1. Any state that reaches goal 2 also has net savings of at least NOK 100,000. The only other differences are the wellbeing weights and BSU not counting. The stated rationale, "about 11 months of hybel rent", refers to a cost the MVP doesn't have.
- Fix: Make goal 2 different in kind, such as a lower buffer plus no interest paid in months 37-60, or the buffer held for N months.
- Consequence: The three-goal choice is really two, and the replay in UJ-5 ("save or be debt-free") doesn't feel different.

**A13** (FR-27; FR-45 money actions; rule 15; example 18h; FR-9 goal 2)

- Problem: Only consumer loans and the card can be paid early. A family loan or payment plan still running at month 60 can't be cleared. Example 18h shows NOK 120,000 cash and NOK 1,500 family loan as Goal not reached, and the player has no action that fixes it. A plan started after month 48 or a long family loan makes goal 2 impossible with no warning.
- Fix: Add "pay off a family loan or payment plan early" to FR-45 and test it. Otherwise warn before accepting a term that runs past month 60 for goal-2 players.
- Consequence: A player with ample cash loses because of a missing button. That feels like a bug, not a lesson.

**A14** (FR-9 reference run; example 20; UJ-2, UJ-3, UJ-4, UJ-5)

- Problem: The reachability proof excludes the moped, the licence and the card, which are the game's flagship content. Adding a licence in month 20 and a used moped in month 32, sold in month 60, on normal spending, with no fuel or repairs, gives NOK 99,947 (a miss). With a new moped it's NOK 93,590, and with the used moped plus yearly expenses it's NOK 86,479. Markus from the UJ-4 trace (W=41, NOK 1,713 at month 46, no summer job or fuel) ends with NOK 58,064 on normal, and NOK 98,808 on low from month 55. Low from month 47 is needed (NOK 114,352), but UJ-5 doesn't say so.
- Fix: Add a reference run with the moped and with UJ-4's card episode. State the level UJ-5 needs. Tune the target so the journey's real win works.
- Consequence: The default path through the game's headline purchase misses the goal. UJ-5's real win is reachable only on a setting the journey doesn't state.

**A15** (FR-30; FR-23 transport; OQ-8; parameter table)

- Problem: The paid licence costs NOK 32,500, a third of the goal, and has no defined benefit ("what the licence gives the player" is open). It also adds a monthly fuel cost. On example 20's run it drops net savings to NOK 85,933. A 50% draw forces fuel on gift recipients, with no way to refuse or stop it.
- Fix: Define the benefit before writing the events. Charge fuel only when the player chooses to borrow the car.
- Consequence: Buying the licence is always wrong, and half of players get a random recurring cost for 24 months that they never chose.

**A16** (Example 20; FR-45 "Income lands in the current account")

- Problem: NOK 119,299 needs every month's surplus moved to interest-bearing savings, but the run doesn't state this and FR-45 doesn't do it automatically. Left in the current account, the result is NOK 115,196, or NOK 102,076 with expenses.
- Fix: State the monthly transfer in the example, or require the automated run to use actual money actions.
- Consequence: The test implementer gets a different figure, and the real margin for a player who doesn't move money is about NOK 2,000.

### Ending wellbeing (FR-33, rule 12, example 17)

**A17** (FR-33; rule 12 window; §1 "getting rich at any cost gives a hollow win"; UJ-5 second playthrough)

- Problem: The window only moved the gap. The 17b chaser who eases off at month 37 instead of 49 (40 h in months 19-36, 10 h after, low all the way) ends with NOK 457,247 and ending wellbeing 55, a real win on goal 1. Goal 2 gives 59, and goal 3 gives 48, a hollow win. Years of 40 h weeks at 16-17 count for nothing.
- Fix: Use months 19-60 for the window, which puts this run at about 43, or add a sustained-overwork penalty. Test the window with a grid of when the player eases off, not one run.
- Consequence: The headline design claim is false for anyone who reads the game's display and adjusts. The 17b example only proves the one path it tested.

**A18** (Rule 12 threshold 50; example 21c)

- Problem: A player can reach social life 0 and still get a real win. Example 21c does it at 57. 25 h a week on low with goal 1 weights reaches NOK 480,620 and ending wellbeing 50, with no overwork penalty at all. 40 h to month 36, then 24 h on low in months 37-54, gives NOK 538,864 at 50, about 95% of the 17b chaser's capped money.
- Fix: Add a floor for each part, such as average social ≥ 30, or raise the threshold to about 60. 60 still fits UJ-4's minimum and makes 21c hollow.
- Consequence: A player with no social life for years gets the "real win" text, and the hollow win costs only about 5% of wealth to avoid. The wellbeing argument in §1 fails.

**A19** (Rule 12 "free time below 50")

- Problem: There's a cliff at 25 h a week. On normal, 25 h gives ending wellbeing 68 and 26 h gives 39. One more hour costs 29 points and adds only NOK 5,036. Below 25 h, work has only a mild effect.
- Fix: Scale stress and social loss with hours over the limit, and show the player the limit in the hours control.
- Consequence: The optimal strategy is exactly 25 h, which is a solver's result, not a lived trade-off. A player who picks 26 h gets a hollow win with no way to see why that one hour mattered.

**A20** (Rule 12 stress cap; FR-33; UJ-4 "the debt keeps weighing on him")

- Problem: Debt stress is capped at 50, worth −12 points at most, while high spending adds up to +12. An indebted player on high with 10 h a week scores 74, the same as a debt-free player on normal (74). On goal 3's weights the indebted one wins, 79 to 72. The careless run 21a ends at 87, well above the careful reference run at 75 and the low-spending saver at 57.
- Fix: Raise the debt-stress cap or remove the high bonus while the player is carrying interest. Add a test: "permanent debt on high scores below debt-free on normal".
- Consequence: Wellbeing rewards the behaviour UJ-4 warns against. Testers asked "what does the score show?" (§7.1) will see careless play score best.

**A21** (Rule 12 "rises by 5, but not above 50")

- Problem: Stress can exceed 50 through a crisis (+10 uncapped) or an event (up to +20). With stress at 60 and interest charged, `min(stress + 5, 50)` lowers stress to 50, while "no increase" keeps it at 60. The order of the steps also changes the result, and "none of these apply" doesn't say whether an event's own stress effect counts. Social, by contrast, has no natural recovery, although UJ-5 says it has "settled down".
- Fix: Give the order explicitly and state "if already above 50, no change". Add a worked case of a crisis with interest at stress 48 and 60.
- Consequence: The worked examples never exercise this case, so builds will differ with no test catching it, and F9's boundary results depend on it.

### Options that stay open and moving on (FR-48, FR-49)

**A22** (FR-9 "Borrowing never helps"; FR-41; FR-48; FR-49; example 18a)

- Problem: A consumer loan stays open in the money view, and FR-49 lets the player clear a trigger before the check. Take 18a: current −NOK 400, net NOK 120,000, wellbeing 70, Loss. A NOK 5,000 loan in month 60 makes the account positive, net savings stay NOK 120,000, and the ending becomes Real win. Swapping below-zero for a debt trigger also works, because a trigger first true at month 60 isn't a loss. FR-9's PRD wording "can pay ... from the current and savings accounts" also ignores debt, unlike rule 13.
- Fix: Decide and write it down. For example, money borrowed in months 59-60 doesn't clear a trigger, or the loan is closed in those months. Add 18a-with-loan as a worked example. Align FR-9's goal 3 wording with rule 13.
- Consequence: "Borrowing never helps" is false for the worst ending, and the loss becomes avoidable with one tap by anyone with a steady wage. That teaches the opposite lesson about credit in the final month.

**A23** (FR-48; FR-46 "Milestones", "Pushed out", "No repeats"; addendum "About 8 milestones")

- Problem: Three connected gaps. (a) FR-48 says a milestone offers the option first, while FR-46 says it stays open in the meantime. Nothing removes a due milestone if the player has already taken the option from the money view, so the event offers what they already own. (b) Summer job offers in months 18, 30, 42 and the experience in 44, 56 repeat, but "No repeats" excepts only crises and warnings. (c) There are at least 11 milestones (13 for goal 3), not 8. The addendum's formula at N=50 then gives 16.0 or 16.9 shared events of 25: 64% or 68%, against FR-43's two-thirds limit.
- Fix: Add "a milestone is cancelled once its option is taken". Allow listed milestone repeats or write them as separate events. Recount and rerun the library-size table.
- Consequence: The content check rejects the required schedule, or the game offers owned items. The cut to 50 events (§4.1 item 3) can fail FR-43 for goal-3 players even before flag gating raises overlap.

**A24** (FR-46 "Pushed out"; FR-48 "Dated offers"; FR-32 "Nothing is lost")

- Problem: Three ways an offer is lost. A summer job pushed from June has no later slot before July's income step, and nothing requires telling the player, though NOK 23,405 in month 43 is about 23% of the target. A crisis in month 54 can push the full-time offer to month 56 (or later), costing up to a third of the months that decide goals 1 and 2. A follow-up due late can be pushed past month 58, while months 59-60 are quiet, despite "no follow-up is lost".
- Fix: Require a visible notice in the crisis or summary whenever a dated or valuable offer is open. Let a pushed follow-up take month 59 or 60.
- Consequence: A crisis silently costs far more through the missed offer than the crisis itself. The player can't see why, and "Nothing is lost" isn't true.

**A25** (FR-18; FR-46 "A part-time job offer also comes by month 20"; FR-48)

- Problem: Year 4 has 5 active months, and goal-3 players have 5 fixed demands: gift reveal, card, loan, summer job, experience. That leaves no slot for drawn events, follow-ups or warnings. Also, the part-time row opens in month 1 while FR-46 says by month 20, and FR-48 says it can't be taken until a milestone event offers it. That leaves up to 19 months with no job available.
- Fix: Give a single earliest offer month for the part-time job. Publish a slot budget per year and have the content check report drawn-event starvation.
- Consequence: The credit year has none of the planned events (russ and so on) for some players. A 15-year-old may be told by UJ-3 to get a job the game won't offer yet.

**A26** (FR-48 "Taking an open option counts as a choice"; addendum "Option fields"; FR-13; FR-35)

- Problem: A milestone option carries stress and social effects, flags, tips, an opener for a boomerang pair and teaching text. FR-48 says only that conditions and prices are the same. Declining in the event and then taking it from the money view may skip all of those.
- Fix: State "an open option is the same option record, and applies all its effects, flags and texts", and add it to the content check.
- Consequence: Moving the choice to the money view dodges its consequences and follow-ups. FR-43's "choices give different stories" weakens without any test noticing.

**A27** (FR-48 test "a player who can't afford the moped licence in month 13 buys it after the summer job in month 19")

- Problem: The test predates rule 16. On normal, the NOK 16,728 summer job nets NOK 4,182 (NOK 836 on high, NOK 8,364 on low). UJ-3's Markus, with a little saved such as NOK 3,000, has about NOK 7,300 and can't buy the NOK 12,000 licence in month 19.
- Fix: State the starting savings and level in the test. Re-check UJ-3's "the moped might be possible" and the addendum's reference to the summer wage against net money after spending.
- Consequence: The test passes only for an unstated starting state, while the journey it realizes fails for the character it's about.

**A28** (FR-49; NFR-7 list)

- Problem: New refusal cases have no test: continuing before the real choice is made, a second real choice in one month, continuing with an unfinished crisis step, and an open option after the month has moved on. NFR-7 says each listed case has its own test, so an unlisted case has none.
- Fix: Add these to the NFR-7 list.
- Consequence: A crafted or duplicate request can skip a month's choice or a crisis, and the suite would still pass.

### Crises (FR-32)

**A29** (FR-32; rule 8; FR-49; FR-24)

- Problem: A trigger true at the end of month M makes M+1 a crisis, but M+1's income runs first. If the wage clears the balance, no trigger is true at the moment the crisis appears. Rule 8 rechecks only after a choice, so the player must answer a solved crisis and takes +10 stress anyway.
- Fix: Recheck after the month opens. If nothing is true, skip the crisis and show a note, or state explicitly that it still runs. Add a worked example.
- Consequence: A phantom crisis with stress damage appears, and F4's test can't distinguish correct from wrong behaviour.

**A30** (FR-32 "Options that work" and the realistic actions list)

- Problem: The list omits the actions that actually fix below-zero: taking a job (an 18-year-old with no job goes negative by NOK 537 every month), lowering the spending level, and withdrawing BSU (example 18a has NOK 120,000 net while negative). They exist only in the money view. "Asking family" is always offered, yet asking again returns the same stored answer (FR-27), so it can use up steps.
- Fix: Add those three options where possible. Mark family as already asked after the first step. Add content-check coverage.
- Consequence: A player can get a Loss with a large BSU by following the crisis screen as designed. A step can be wasted on a repeat answer.

**A31** (FR-32 "Linked choices"; FR-47 "A change applies from the next month"; FR-41)

- Problem: In month 60, an extra shift or similar later effect can't happen, because there's no month 61, yet the rule shows any option that's "possible". The same applies to crisis steps generally: a later-effect step doesn't clear the trigger, and the player is left with family and ignore.
- Fix: Hide options whose effect lands after month 60, and show when each option's effect will land.
- Consequence: The last chance to avoid a Loss offers an option that can't help. The player picks it and gets a Loss with no explanation.

**A32** (Rule 15; FR-45 "bank loan instalments ... always charged"; FR-32 payment plan; example 12)

- Problem: A payment plan turns a NOK 350 minimum, which can never push the account negative, into NOK 939 a month. If that counts as an instalment it is always charged, so it can push the account negative. UJ-4's Markus on high has NOK 395 free, so he'd go about NOK 544 negative every month. The plan needs only a balance and no plan running, so no affordability check applies. FR-45 doesn't say which class the plan belongs to.
- Fix: Classify the plan in FR-45. Show the monthly cost against free money on the option.
- Consequence: The option offered as a way out starts a repeating below-zero crisis cycle for the players who most need help.

**A33** (Rule 8 and FR-32 debt trigger; FR-45; example 9c)

- Problem: The debt trigger subtracts savings but not the current account, and income stays in the current account by default. A 10 h player with a NOK 21,000 loan, a NOK 10,000 card balance and NOK 40,000 in the current account is above the NOK 25,356 line and gets a crisis.
- Fix: Subtract a positive current account too, and update example 9.
- Consequence: False crises hit solvent players who never moved money, and a below-zero style message appears when they're fine.

**A34** (FR-46 "Rule 7 gives about 20-30 real choices"; "Pace"; cooldown)

- Problem: With a crisis every third month, a player from month 37 alone gets about 8 crisis months × 3 steps, adding up to 24 choices to the 25, plus repeating warnings that turn quiet months active. That's far outside 20-30, and the pace claim holds only "with the default". The pace check doesn't include this.
- Fix: Add a seeded worst-case run to the pace check, and limit or merge repeated warnings.
- Consequence: Players in trouble, who are the ones the game most wants to teach, get the longest and most repetitive sessions. The most common failure mode isn't playtested.

### Journey consistency

**A35** (UJ-4 step 1; addendum "UJ-4 month by month"; FR-31)

- Problem: The trace has the card at its NOK 10,000 limit before W's spending, built from "city trip, lunches, and fuel", on a whole-balance setting. FR-31 requires the previous month's bill to have been paid in full. So the whole NOK 10,000 must have arrived at the event step of W−1, as one purchase. Lunches and fuel fall at the fixed-cost step and would have been paid off in W−1.
- Fix: Name the one-off cost in the trace and make sure an event for it exists. Or start the trace from a smaller trip plus W's own spending going on the card, and recompute the figures.
- Consequence: The flagship journey isn't reproducible in the engine from its described history, so the seeded test user and the story will disagree.

### Minigames (FR-51, FR-28, FR-30, NFR-7, NFR-2)

**A36** (FR-51 "Checked by the server"; NFR-7 "The server decides every result"; NFR-4; FR-7)

- Problem: The result is reported by the device, and the only check is that a game was started this month. Anyone can send "passed". That contradicts "the server decides every result" and FR-7's "decided by the server". FR-12's "every random result is drawn by the engine" also doesn't cover a route or obstacles generated on the device.
- Fix: Make the driving test turn-based: the server sends a route with rule decisions and judges each answer. If it stays real-time, write the accepted risk into NFR-7, limit the result to pass or fail, use a one-time server token, and have the seed supply the route.
- Consequence: The requirement can't be met as written, so either the architecture fails a stated NFR or the examiner finds the contradiction.

**A37** (FR-51; NFR-7 list; FR-49; FR-13)

- Problem: The lifecycle is undefined. Does payment come before or after play? Can a player abandon a game and restart it to avoid a bad result, or play it on a second device (FR-8)? How many attempts are allowed? Does it use the month's real choice? Can the player continue with one unfinished? What about a result for a different minigame or a second result? OQ-16 covers only failure cost, the gift, the way past and the cut list.
- Fix: Add a state model (not started, started, passed, not passed), attempt rules, and NFR-7 cases for each.
- Consequence: Abort-and-retry makes failure meaningless, and the first implementer's guess becomes the rule. Each new state also needs idempotency and cross-device behaviour.

**A38** (FR-51 "a player who can't play it can still get past it"; FR-28 "have to pass"; NFR-2; NFR-3; OQ-16)

- Problem: A real-time driving game conflicts with screen readers and motor limits on a phone, and WCAG 2.2 AA has timing, motion and gesture criteria that NFR-2 doesn't address for it. FR-51 mentions only phone and keyboard. A way past that's open to all empties "have to pass". One gated on a statement of disability collects health-related data, which NFR-3's "only email and password" forbids.
- Fix: Offer an equivalent text-based version with the same pass rules, available to everyone, with no statement required. Add the minigame to the NFR-2 manual test.
- Consequence: The AA requirement fails at the moped, which is on the always-stays list. Alternatively, the skill mechanic becomes pointless.

**A39** (§4.1 cut list; FR-28; D10; OQ-16; addendum Minigames)

- Problem: The minigame is the only new real-time component, added about five weeks before delivery, and it isn't on the cut list. The moped is on "always stay", and FR-28 requires the game to pass. So it's effectively uncuttable. Cutting it would also require changing FR-28, UJ-2 and D10. §1's "Now" description omits it. With only licences, a player who never takes one never sees a minigame, so "come up along the way" and the pace check may not be exercised.
- Fix: Put it high on the cut list now, with the fallback "licence is payment only" and a matching D10 text. Require the seeded and playtest flows to include one.
- Consequence: A late feature with unknown cost competes with the engine in the final weeks, and there's no documented way to drop it. A last-minute cut leaves player-facing text wrong.

**A40** (FR-51 "automated runs and the seeded test users can get past"; NFR-11 "runs the same version")

- Problem: A way for automated runs to skip the game has to exist on the server. The PRD doesn't limit it, while the playtest and local builds are required to be the same version.
- Fix: Limit the override to engine tests through injection, and tie the examiner's path to the seeded accounts' state, not a request flag. Add a refusal test in NFR-7.
- Consequence: A testing back door ships in the playtest build, undermining both FR-51 and NFR-7.

### Playtest records (FR-50, NFR-3, §7.1)

**A41** (FR-50 "time to the first choice", "session lengths"; FR-11; §7.1; NFR-7; NFR-3)

- Problem: Two listed metrics can't be measured as defined. FR-11's clock starts at opening the game, before any account exists, and NFR-7 lets the device send only choices, while NFR-3 forbids analytics. A session is one in-game year that may span sittings, so server timestamps include breaks, and no gap rule separates sittings.
- Fix: Define the start as account creation with a client-reported elapsed time allowed only in the playtest environment, and add this to NFR-7 and NFR-3. Define session length as active time, with a stated idle gap.
- Consequence: The Pace rows in §7.1 report numbers that don't mean what they say, or the team adds tracking that NFR-3 forbids.

**A42** (FR-50 "survive"; FR-44; NFR-3 "A player can delete"; §7.1 completion)

- Problem: FR-50 says records survive FR-43 deletion and are deleted with the playtest accounts, but it doesn't address a tester deleting their own account under FR-44. If the record survives, it contradicts "game data are gone". If it goes, dropouts vanish and completion is biased upward. NFR-3's "no analytics" bullet and its player information also don't mention the exception.
- Fix: State the behaviour. For example, on FR-44 the record is deleted but an anonymous count of withdrawn testers is kept. Add FR-50 to the player information for the playtest and to the analytics bullet.
- Consequence: The team either breaks its own privacy promise to testers or inflates the headline 70% metric. OQ-6's legal review also has an incomplete description of the processing.

**A43** (FR-50 "What's counted"; FR-43; OQ-8; §7.1 "why their ending came out as it did")

- Problem: The records keep no ending, goal or final net savings, and FR-43 deletes a finished life when the player starts again. The team therefore can't compare a tester's explanation with what happened, or see the real ending distribution. FR-9 calls the margins thin, and OQ-8 relies on tuning.
- Fix: Add ending type, goal and end-state figures to the records, which contain no choices or free text.
- Consequence: The one real-player test can't show whether hollow wins or misses happen. Tuning remains untested on real play.

**A44** (§7.1 "Comes back voluntarily ... within a week"; NFR-11 7 days; FR-50)

- Problem: A tester who starts late in a 7-day window has less than a week to return, and records can't tell a voluntary return from one the team prompted. FR-50 is also switched off in the examiner's run, so NFR-6's route can't verify it.
- Fix: Fix a start window and measure each tester's own 7 days. Log or forbid team reminders. Add a test that runs with the playtest setting on, and record the result in the repo.
- Consequence: The 50% return figure is an artefact of scheduling, and the examiner has no evidence the records work.

### V2 scope (§1, §4.3)

**A45** (§4.3 pocket money; FR-46 "Who can get an event"; FR-45; FR-17 candidate topics)

- Problem: Eligibility ignores affordability. A player who spends the pengegave in month 1 with no job has NOK 0, so every costed option is locked. That's up to 8 active months before the first summer wage in month 19, and the survey's core regret topics (snacks, takeaway) can't be played. FR-23's examples also show nothing because spending is zero. This is the exact path UJ-3 and 21a describe. §4.3 says "before 18", but a player with no job has no income after 18 either. 68% of the survey get money from parents.
- Fix: Add a content-check rule that at NOK 0 at least a set share of events still has two pickable options. Or include a simple fixed allowance with a stated assumption. Correct the §4.3 wording.
- Consequence: The players who most need the lesson get a first session of locked buttons, in the session meant to hook them and in the 10-15 minute test.

**A46** (§1; §4.2 "use AI anywhere"; §4.3; OQ-11; OQ-15; addendum "Changes from the proposal")

- Problem: The approved proposal isn't in the repo, and the PRD's "which source applies" rule doesn't cover it. Whether a no-AI delivery passes the course is open, with no deadline and no fallback, though delivery is about five weeks out. OQ-11 blocks epics, while "UX and architecture can start". §4.2's absolute wording leaves no room for a small fallback.
- Fix: Give OQ-11 a date. Write the fallback now: the smallest AI feature that would satisfy the course, behind a pre-written fallback, using brief F5, and what it would displace on the cut list. Put the proposal in the repo first.
- Consequence: A late "AI is required" answer lands with no plan. It would hit NFR-3's no-AI promise, NFR-5's zero cost and the epics together, and could affect the grade.

**A47** (§1 V2; FR-46 random draw; FR-17 schema; NFR-4)

- Problem: Nothing states what the MVP must preserve so that V2 can add AI events: a replaceable event source, events that arrive through the same schema, and replay under FR-12 when an event isn't from a stored library. FR-12's "reproducible from stored values" and NFR-4's versions assume a fixed library, and §4.3 only says "after the base works".
- Fix: Add a short V2 readiness note: all events pass through one schema and validator behind one selection interface, and generated events would be stored as content. Otherwise, explicitly state that V2 may require rework.
- Consequence: Architecture either over-builds for an unspecified V2 or builds something that needs replacing. The PRD's "Next" is then a promise without a path.

## Edge cases

**E1** (prd.md:605-606; brief-addendum.md:68,72)

- Condition: High or low spending level set with no wage, so nothing is spent.
- Guard: apply social +2/-2 only in months where rule 16 spending > 0; add a test for it
- Consequence: No-wage run: same NOK 76,957 gives ending wellbeing 90 (high), 78 (normal), 61 (low).

**E2** (prd.md:545-546; brief-addendum.md:72)

- Condition: Negative current account, no savings, wage arrives: spending and next-income payoff compete.
- Guard: add spending and tax to the FR-45 charge lists; state whether the rule 16 share applies before or after clearing the negative balance
- Consequence: High spending can keep an account negative for months; implementations and answer keys diverge.

**E3** (prd.md:612,647; brief-addendum.md:61,72)

- Condition: Card room is smaller than this month's card-payable costs plus spending.
- Guard: fix the order: card-payable costs first, then spending; state split versus declined for each
- Consequence: Rule 16 splits, FR-26 moves whole purchases; cause links and declined messages diverge.

**E4** (prd.md:548,648,738; brief-addendum.md:71)

- Condition: Card use turned on, or spending due, while a payment plan blocks the card.
- Guard: treat card use as off during a plan; add a refusal to NFR-7; spending comes from the current account
- Consequence: Rule 16 spending could land on a blocked card; no refusal case covers it.

**E5** (prd.md:414,418,586; brief-addendum.md:57,65)

- Condition: December BSU deposit after month opens; the deduction has no step in the two-part month.
- Guard: run the deduction at continue in month 12k; mark the December summary provisional; state whether it enters rule 16 wage left
- Consequence: December summary shows a stale deduction; month 60 deduction timing against rule 13 is undefined.

**E6** (prd.md:549,597; brief-addendum.md:65,69)

- Condition: BSU withdrawn from money view after that month's tax step has run.
- Guard: charge the clawback from the payout at once and keep it out of rule 16; state that month-60 withdrawal counts or not for goal 2
- Consequence: Month-60 withdrawal can reach goal 2's buffer; clawback has no defined charge point.

**E7** (prd.md:364,575; brief-addendum.md:160)

- Condition: Careless run raises full-time from 37.5 h to 40 h in months 55-60.
- Guard: add this variant to the seeded check. Recomputed with example 21's no-expense basis: NOK 100,762 against 96,365; with NOK 2,500 a year: 87,132
- Consequence: Careless run reaches the NOK 100,000 goals with ending wellbeing 86: a real win.

**E8** (prd.md:361-365; brief-addendum.md:69,160)

- Condition: Goal-3 player follows the careless profile and never buys the experience.
- Guard: extend the FR-9 careless requirement to goal 3 once priced: 21a ends at NOK 96,365, above any price clearly below 100,000
- Consequence: Goal 3 is reached with no earlier care; FR-9 guards only goals 1-2.

**E9** (prd.md:364-366,620)

- Condition: Automated careless or careful run meets a crisis month or an FR-24 expense.
- Guard: define each run's crisis answers and expense draws. Careless with NOK 2,500 in January each year has 52 negative month-ends, from month 1
- Consequence: Run outcome is undefined, so the seeded check can't decide miss or reach.

**E10** (prd.md:360,551,633; brief-addendum.md:137)

- Condition: Goal-2 player with cash has a family loan or plan running past month 60.
- Guard: add a money action: pay off a family loan or payment plan early at no fee
- Consequence: Goal 2 is unreachable at any balance, for example with a plan from month 49.

**E11** (prd.md:418,723; brief-addendum.md:64,89)

- Condition: Debt trigger true while the player's money sits in current account, not savings.
- Guard: subtract a positive current account too, or state that the transfer is the intended way to clear it
- Consequence: Free transfer before continue clears crisis, including at 59-60; unaware players get needless crisis.

**E12** (prd.md:417,725)

- Condition: Crisis month falls on a calendar quiet month; FR-49 gives no continue condition.
- Guard: crisis month: continue is accepted only after the crisis has ended (solved, ignored, or third step)
- Consequence: A request could continue past an unanswered crisis month.

**E13** (prd.md:414,720; brief-addendum.md:64)

- Condition: Trigger true at month end, but next month's rule 1 income clears it.
- Guard: re-check after rule 1 when the crisis month opens: skip it if none is true, or state it still runs and which state picks the event
- Consequence: Player gets a crisis event and +10 stress for a problem already gone.

**E14** (prd.md:139,418,556,732-734; brief-addendum.md:64)

- Condition: Money action or open option clears a trigger during a crisis month's steps.
- Guard: state: both are allowed in a crisis month, use no step, and trigger re-check runs after them and can end the crisis
- Consequence: Same moped sale uses a step as crisis option, not via money view.

**E15** (prd.md:735; brief-addendum.md:64)

- Condition: Money-view sale or loan in a crisis month while card minimums are overdue.
- Guard: apply the same order to all money arriving in a crisis month, or state that only crisis options use it
- Consequence: Same sale clears overdue one way, not the other; missed-minimum trigger stays true.

**E16** (prd.md:363,418,843)

- Condition: Consumer loan taken in month 60 clears a below-zero trigger held since month 59.
- Guard: state whether borrowing may avoid the loss ending; if not, exclude a month 59-60 payout from clearing it
- Consequence: Loss becomes goal not reached or real win; FR-9's borrowing rule covers goals only.

**E17** (prd.md:420,452,913)

- Condition: Player stops in month 60 and never presses continue.
- Guard: month 60 recap says continuing ends the life; define completed as ending calculated
- Consequence: No ending, summary, or completion record; life sits unfinished until the deletion job.

**E18** (prd.md:571,576,737)

- Condition: Extra shifts offered in month 60, after which no wage comes.
- Guard: extra shifts are possible only while a later income step remains: month <= 59
- Consequence: Crisis step is spent on an option with zero effect in the deciding month.

**E19** (prd.md:514,517,633,684)

- Condition: Player sold the moped or repaid the consumer loan and wants another.
- Guard: open until taken, and reopens when the one-at-a-time condition is free again
- Consequence: 'Until the player takes it' closes rebuying and a second loan that FR-29 and FR-25 imply.

**E20** (prd.md:518,544)

- Condition: Open option blocked for a non-money reason: no steady wage, or a loan cap below 5,000.
- Guard: show the unmet condition, keep the option open, and refuse it under NFR-7
- Consequence: Only a missing amount is defined, so the screen has nothing to show.

**E21** (prd.md:548-549,994; brief-addendum.md:94)

- Condition: Money move or BSU deposit exceeds its source, or the current account is negative.
- Guard: allowed range for moves is 1 to the source balance; state whether a BSU deposit can draw on savings
- Consequence: Allowed range is undefined; a transfer could create a negative account and a crisis trigger.

**E22** (prd.md:644; brief-addendum.md:61,91)

- Condition: After a miss, setting stays minimum, and payments cover the overdue amount first.
- Guard: minimum setting pays the minimum plus overdue; give amounts in worked example 11
- Consequence: This month's minimum is missed again each month; trigger and month-60 loss stay true.

**E23** (prd.md:657,737)

- Condition: Family gift given at step one, and player asks family again at step two.
- Guard: a repeat ask shows the stored answer and moves no money
- Consequence: 'Gives the same answer' read literally pays the gift up to three times.

**E24** (prd.md:483-485,736; prd-addendum.md:54)

- Condition: Follow-up or milestone pushed out of month 58, the last active month.
- Guard: let a pushed item make month 59 or 60 active, or count due items in the opener's delay check
- Consequence: Item is lost silently despite 'nothing is lost'; the opener check ignores collisions.

**E25** (prd.md:660-662; brief-addendum.md:68)

- Condition: Teen with no income has a family loan; every instalment gets postponed.
- Guard: cap postponement stress at 50 like the other rule causes, and state an end state for the loan
- Consequence: Stress climbs 5 monthly, uncapped to 100, and instalments keep moving back.

**E26** (prd.md:760; brief-addendum.md:68,124)

- Condition: Chaser works 40 h a week to month 36, then eases off at 37.
- Guard: add to example 17b, or count earlier overwork. Recomputed on low spending: 12 h to 18, 40 h to 36, 10 h to 54, 37.5 h after: NOK 457,247, ending wellbeing 55
- Consequence: Real win: FR-33's easing-off protection only moved to the window's start.

**E27** (brief-addendum.md:68,162; prd.md:128,752)

- Condition: Low spending all game: social life hits 0 at month 30 and stays.
- Guard: add a consequence or a test for social life at 0. Recomputed 21c: social 0 in all 24 months; ending 57 on goal 1, 61 on goal 2, 49 on goal 3
- Consequence: Real win with no social life on goals 1-2, which the hollow win should catch.

**E28** (brief-addendum.md:68; prd.md:762)

- Condition: Stress above 50 from a crisis or event, then interest or overwork rule applies.
- Guard: define the cap as max(stress, min(stress + 5, 50)) and state the order of stacked effects
- Consequence: Stress either drops to 50 or stays; scores differ across implementations.

**E29** (brief-addendum.md:68)

- Condition: July summer-job hours make free time fractional, for example 8 h plus 120 h.
- Guard: round free time under rule 2 before the below-50 test and the score
- Consequence: Monthly scores can differ by implementation near the threshold.

**E30** (prd.md:414,424,761)

- Condition: Option result or month-37 average shown before continue calculates that month's wellbeing.
- Guard: result screen shows the option's effect only; the average starts after month 37's continue, with a stated empty state
- Consequence: Shown score omits monthly effects; 'average so far' has no value in month 37.

**E31** (prd.md:485,520)

- Condition: June summer offer pushed by a crisis or warning; next active month is August.
- Guard: drop dated milestones at expiry and name the open offer on the crisis or warning screen
- Consequence: August shows a dead offer, or the player misses summer pay unaware.

**E32** (prd.md:574; brief-addendum.md:66)

- Condition: Player at 40 h a week gets a summer offer: the cap leaves 0 h.
- Guard: when the cut leaves 0 h, show no offer or say why
- Consequence: Player can take a zero-hour, zero-pay summer job.

**E33** (prd.md:571,574)

- Condition: Hours changed in June after accepting a summer job, so July's cap room changes.
- Guard: calculate the cut at July's income step from that month's hours, including extra shifts
- Consequence: Job stays cut despite room, or July goes above 173 h.

**E34** (prd.md:476,480,1093; prd-addendum.md:54)

- Condition: Active-month configuration moves off months 18, 30, 42, 44, 54, or 56.
- Guard: content check fails when an FR-18 offer month isn't active
- Consequence: Offer lands after its July or start month, with nothing catching the configuration.

**E35** (prd.md:362,481,487,504)

- Condition: Goal-3 experience offered in month 44 and again in 56, or bought at 44.
- Guard: exempt this event from no-repeat, and block the month 56 offer once bought
- Consequence: No-repeat removes the second offer, or a buyer is offered it again.

**E36** (prd.md:480,497,514,571; brief-addendum.md:124)

- Condition: Player wants a part-time job at 15, before the milestone offer due by month 20.
- Guard: fix the part-time offer month and open the money view from it; start 17b's hours at the first possible pay month
- Consequence: FR-18's month 1 and FR-48 disagree; 17b's 12 h from month 1 is impossible.

**E37** (prd.md:308,914,916,951)

- Condition: Tester deletes account while an FR-50 record exists.
- Guard: delete the record with the account, or disclose that it survives and state how metrics treat it
- Consequence: Data outlives the deletion promise; the orphan escapes deletion with playtest accounts.

**E38** (prd.md:310,913,916)

- Condition: Tester deletes account and creates a user again with the same email during playtest.
- Guard: state whether the tester code follows the email through the key or starts anew
- Consequence: One tester counts twice in completion and return rates.

**E39** (prd.md:875,880,913,1064)

- Condition: Play again after an ending versus starting over before 20, and highest month across lives.
- Guard: count the two separately; store highest month per playthrough; completed means an ending calculated
- Consequence: Completion and restart figures can't be told apart.

**E40** (prd.md:913,1038)

- Condition: Daily automated login check uses a test user in the playtest environment.
- Guard: flag test accounts and exclude them from records and export
- Consequence: Monitoring adds days played and return visits to the metrics.

**E41** (prd.md:383,913,1062)

- Condition: Tab left idle for hours, or the first choice is resumed days later.
- Guard: define both clocks and cap idle gaps in session length and time to first choice
- Consequence: Pace metrics report absences, not play.

**E42** (prd.md:915)

- Condition: The switch that keeps FR-50 off locally is missing or wrongly set.
- Guard: default off, explicit setting only in the playtest environment, and a test of both states
- Consequence: Records could run in the examiner's run, or the feature stays untested.

**E43** (prd.md:957,1063)

- Condition: Quiz comes before the first sitting, yet the tester code is tied to an account.
- Guard: state who issues the code and when, and how it reaches the tester, since the game takes no typed code
- Consequence: Quiz, survey, and records can't be linked as the metrics assume.

**E44** (prd.md:300,953)

- Condition: Stay-logged-in player keeps playing within 30 days but never logs in again.
- Guard: measure the 12 months from last play, not last login
- Consequence: An active player's account can be deleted with no warning.

**E45** (prd.md:896; prd-addendum.md:102)

- Condition: Player closes or reloads mid-minigame, before any result exists.
- Guard: add a third state, abandoned, to the schema: restart at no extra cost, or counts as not passed
- Consequence: Closing escapes a failing run for free, or money already paid has no outcome.

**E46** (prd.md:335,344,896)

- Condition: Connection lost at minigame end, with the result held only on the device.
- Guard: no start offline; server stores the start; retry with a request ID; define what happens if the device closes first
- Consequence: Contradicts FR-7; going offline can erase a failing result.

**E47** (prd.md:897,984; prd-addendum.md:24)

- Condition: Device sends pass for a started minigame without playing it.
- Guard: state a server check, such as a minimum play time or input log, or accept the risk explicitly
- Consequence: One request bypasses the skill gate; no refusal in NFR-7 covers it.

**E48** (prd.md:896,1004)

- Condition: A second, different result arrives for one start, such as fail then pass.
- Guard: first confirmed result per start wins; a new attempt needs a new server-recorded start
- Consequence: Repeat rule covers identical requests only, so a replay could overwrite a failure.

**E49** (prd.md:417,521,897)

- Condition: Minigame started from the money view; player continues before a result is reported.
- Guard: block continue while a minigame is open, or void the attempt and state what happens to the payment
- Consequence: Next month refuses the result, leaving the fee paid with no outcome.

**E50** (prd.md:517-518,521,675,1100)

- Condition: Licence not passed: option status, unaffordable retry, and real choice all unstated.
- Guard: not passed keeps the option open; a retry follows 'Can't pay yet'; state whether an event attempt uses the real choice
- Consequence: 'Open until taken' could close the licence; OQ-16 names only what failing costs.

**E51** (prd.md:900,1035)

- Condition: The way past minigames for automated runs exists in the playtest build.
- Guard: allow it only in engine tests and seeded local data; refuse it when the playtest environment is set
- Consequence: Playtesters or forged requests skip minigames, distorting pace results.

**E52** (prd.md:405,409)

- Condition: Replay from stored values and the player's choices omits minigame results.
- Guard: add stored minigame results to the Reproducible bullet
- Consequence: A replayed playthrough diverges at the first licence, and the FR-12 test fails.

**E53** (brief-addendum.md:154; prd.md:402,418,540,822)

- Condition: Example 20 gives same-month wage and month-1 pengegave savings interest before the choice.
- Guard: recomputed: 119,299 only with one pot earning on same-month wage; rule 1 order with monthly transfers gives 119,014; no transfers 115,196, or 102,010 with January expenses; month 1 is then 10,000, as FR-39's 59 months assume
- Consequence: Answer key fails a rule-1 engine; the margin depends on 60 manual transfers.

**E54** (brief-addendum.md:163)

- Condition: Example 21d says no job and low from 55; figure needs summer jobs, low throughout.
- Guard: recomputed: no jobs at all 76,957; summer jobs and normal to month 54 gives 92,597; 107,685 only with summer jobs and low from the first wage; 94,303 is a June expense with 18 negative month-ends and no crisis modelled
- Consequence: Unit test can't reproduce the label; 'reached' becomes missed on a literal reading.

**E55** (brief-addendum.md:124; prd.md:574)

- Condition: Chaser's NOK 590,662 adds uncut 120 h summer jobs to a 40 h week.
- Guard: the cap leaves 0 h at 40 h: recomputed 567,315. Wellbeing 41, 45, 35, and 55 match the capped run, while 590,662 needs 293 h in July
- Consequence: Test expects money the monthly cap forbids; money and wellbeing come from different runs.
