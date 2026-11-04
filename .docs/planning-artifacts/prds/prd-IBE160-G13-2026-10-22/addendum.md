---
title: LifeMode PRD addendum
created: 2026-11-03
updated: 2026-11-04
---

# Addendum: LifeMode PRD

## Competitor playtests

Team verdict as reported on 2026-11-03: everyone on the team has tried both products. This replaces the note in `research/playtest-competitors-2026-10-31/notes.md` that only one member had played Koll på cashen and that PersonalFinanceLab had not been tried.

| Product | Team verdict | What LifeMode does instead |
|---|---|---|
| Koll på cashen | Not very rewarding, heavy and slow | More entertaining and smoother to play |
| PersonalFinanceLab | Professional, but not made for the Norwegian market, geared towards a teacher-led experience, and it costs money | Made for Norway first and foremost |

## Progression and visible consequences: MVP scope

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

**Moped licence:** when the player chooses to take it, they pay for driving lessons, mandatory lessons and the licence itself, at real prices from sources such as Statens vegvesen, driving schools and SSB. The recap's teaser names the cost, so no new screen is needed. [ASSUMPTION: payment only, with no exam or driving mechanics.] Owning a moped and the car licence were added from UJ-4; see "Credit card debt, family and the moped in UJ-4".

## Login with email: consequences for the build

Decided on 2026-11-03. This replaces the earlier decision on username, no email and no reset. Questions for architecture:

- **Sending email:** password reset needs a way to send email within the hard constraint of zero ongoing cost.
- **Examiner's local run:** the app has to run from Docker without the team's cloud account or keys, so reset email must either work there or have a stated local replacement.
- **Internal address plan:** the plan to build a fake address from the username (`@lifemode.invalid`) is no longer needed.
- **Playtests:** playtesters aged 18-20 will now give a real email address, while the brief says no contact details are stored with results, so the two have to be kept apart.

Updated to match on 2026-11-03: brief (Scope In #9, Constraints), brief addendum (Privacy, Login secret), architecture (Database and Data Model, Authentication and authorization) and issue #24.

## Interest after a long break: left out of the MVP

The team suggested positive or negative interest after an extremely long break. Decided on 2026-11-03 to leave it out, and the game stays exactly as the player left it. Credit only starts at 18, so a younger player would mostly get free money for staying away, an older player in debt would be punished for coming back, and the game's clock runs in game months with fixed rates.

## Saving and interest in UJ-3

Decided on 2026-11-03.

**Funds stay out of version one.** The team's narrative said funds or savings, but investing was decided out on 2026-10-31, and funds need returns that go up and down, which the engine doesn't have. Many survey respondents asked about funds, so it's a candidate for later.

**The game shows the real interest, even when it's small.** First-year interest under rules 1-2:

| Saved | Savings account (2.87%) | BSU (5.61%) |
|---|---|---|
| NOK 2,000 | NOK 60 | NOK 116 |
| NOK 3,000 | NOK 84 | NOK 172 |
| NOK 5,000 | NOK 144 | NOK 287 |

Interest alone won't pay for a moped, so the moment rests on two things: the surprise that money earned money without the player doing anything, and a pointer to other income. A summer job at 16 pays NOK 16,728 (worked example 1).

**BSU comparison:** "Hvorfor?" can also show what the same money would earn in BSU. This counts as an "if you had chosen differently" line, which is first on the cut list, and the moment works without it.

## Tips from the game

Decided on 2026-11-03. Some events carry a short, general, pre-written tip that the player is free to ignore. A tip is about the situation in the game and isn't personal advice, which the brief rules out. It should sound like a tip rather than a lecture.

## Credit card debt, family and the moped in UJ-4

Decided on 2026-11-04.

**A warning comes before a crisis.** The crisis triggers stay as they are. A first card for ages 18-20 usually has a limit of NOK 5,000-10,000, and 10 hours a week at NOK 195.04 pays about NOK 8,400 a month, so a new card rarely pushes debt above 3× income on its own. Instead, the game warns the player once the balance can't be paid in full and interest starts, and the player decides whether to act. A crisis month starts only if the minimum is missed two months in a row, or if interest pushes the debt above 3× average monthly income.

**Family help.** Family can give or lend money, but mostly as a loan that has to be paid back, so the player learns from it. It's not always on offer: in the survey only 17% got family help with an unexpected expense, so most of the time the player has to find another way. Sometimes family can cover only part of the amount.

**Moped.** The player has a moped from age 16, either bought or received as a gift. It costs fuel, repairs and insurance, and the parents may pay part of the insurance. Its resale value drops with age and use. Prices should follow the real market. In the MVP, the player chooses whether to buy a moped, a gift offer comes up now and then, and the parents' share of the insurance is random. Once the AI game engine is added, they can be based on real data.

**Car licence.** By 18 some players get a car licence as a gift from their parents. The gift is random, and a player without it can pay for the licence at a real price. With a licence, the player pays for fuel when borrowing the parents' car. This changes brief Scope Out #5, which listed the driving licence as a later step; the brief was updated on 2026-11-04. If the moped licence is in, the car licence is in too, so there's more to play.
**What the card costs.** The small cost in worked example 4 comes from the small amount, not the rate: 22.6% a year is a normal card rate (SSB; the market's effective rates run from 20% to 30%). At a small balance, the NOK 300 minimum pays the debt off quickly. Interest is charged every month, so the game shows both this month's interest and the total cost of paying only the minimum. Under rule 5:

| Card debt | Interest in month 1 | Months to pay off at the minimum | Total interest |
|---|---|---|---|
| NOK 3,200 (worked example 4) | NOK 60 | 13 | NOK 406 |
| NOK 8,400 (about one month's wage) | NOK 158 | 41 | NOK 3,645 |
| NOK 10,000 (top of a typical first limit) | NOK 188 | 51 | NOK 5,508 |

UJ-4 shows the cost for the player's own balance. The figures use the proposed 3.5% minimum in rule 5, with monthly interest rounded under rule 2. The proposal only changes balances above about NOK 8,600, where 3.5% is more than NOK 300. At 3%, NOK 10,000 took 53 months.

**How to build it.** Accepted on 2026-11-04. Each addition reuses something the engine already has, so the only really new thing is an owned moped.

| Addition | Built as |
|---|---|
| Warning before a crisis | One extra check and one event. It's the core of UJ-4 and fits the LK20 aim on reflecting about credit cards |
| Fuel and insurance for the moped, fuel for the car | Transport costs, which the engine already has as fixed costs |
| Moped repairs | Unexpected expenses |
| Family loan | The existing loan rules at 0% interest |
| Moped resale value | Drops by a fixed share per year owned; tracking actual use comes later |
| Car licence as a gift | One event |
| The moped in the room | One of the room states, so it's gone once he sells it |

If time runs short, cut in this order: the "if you had chosen differently" lines, then the parents' share of the moped insurance, then events down to 30. The warning, the moped and selling it stay, because UJ-4 depends on them. (Changed by UJ-5 below: the lines on the ending screen stay.)

## The ending in UJ-5

Decided on 2026-11-04.

**No student loan in version one.** Markus takes a job after upper secondary school and saves towards a flat. A student loan would bring in problems that don't pay off within a game that ends at 20:
- At NOK 15,488 a month (Lånekassen basislån 2026-27), his debt passes 3× a part-time wage within two months, which starts a crisis month.
- It blocks the debt-free goal.
- A player could borrow the full amount and save it to reach a savings goal.
- Interest and repayment only start after studying, so the game would teach little from it.

**For the education step later:** the game has to make clear that a student loan while studying isn't bad, and isn't the same as credit card debt. It has no interest while studying, and repayment starts only after the degree.

**Markus's life goal.** He chose saving for something big in UJ-1, with a flat as the big thing. A 15-year-old picks what he wants rather than "debt-free", and choosing the flat means the card debt at 18 puts his goal at risk. In the second round he goes for saving for something big or for being debt-free with a buffer, and chases money at the cost of his wellbeing, which gives the hollow win.

**"If you had chosen differently" on the ending screen.** These lines stay for the three choices that mattered most, and only those three can be opened. The lines in "Hvorfor?" during play, including the BSU comparison, are cut first. New cut order: those lines during play, then the parents' share of the moped insurance, then events down to 30.

**Comparing playthroughs: later.** For now the ending shows a summary of the playthrough and the tips. Comparing one playthrough with the next is a candidate for a later step.

## Proposals awaiting the team

Proposed by Dahl on 2026-11-04, for the team to confirm on 2026-11-05. Several change decisions from 2026-11-03 and 2026-11-04.

| Proposal | Why |
|---|---|
| No tobacco or alcohol choices for now | Research found them probably allowed on conditions, but their effect on young players is unknown and can't be tested in playtests with 18-20-year-olds |
| The player chooses to buy a moped, with occasional gift offers | A random draw between buying and a gift could make saving up pointless, which works against UJ-3 |
| The car licence gift is random, and a player without it can pay | Gives a large, real money choice at 18 |
| All family gifts stay | They are no longer on the cut list |
| Family loans don't count towards the 3× income crisis trigger | A teenager with no income would otherwise go into crisis from any loan |
| A hollow win shows at least one choice that hurt wellbeing | A kroner ranking alone may not show why wellbeing ended up low |
| Card minimum of 3.5%, min NOK 300 | Matches Bank Norwegian, and DNB also uses 3.5%. Cards with limits up to NOK 30,000 fall outside utlånsforskriften, so this is about realism |
| Account deletion in the game | The game stores email addresses of players as young as 15, and the privacy check (#24) recommends it |
