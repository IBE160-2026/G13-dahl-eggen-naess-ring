# Design Thinking Session: IBE160-G13

**Date:** 2026-10-16
**Updated:** 2026-11-12, aligned with the final PRD
**Facilitator:** SE
**Design Challenge:** Help young people aged 15–20 understand how today's money decisions shape their options later, before those decisions cost real money.
**Requirements basis:** `planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md` (status: final, 2026-11-11). Where this document and the PRD disagree, the PRD applies.

---

## 🎯 Design Challenge

> *How might we help young people aged 15–20 understand how today's money decisions shape their options months and years later, before those decisions cost them real money?*

- **Users:** Young people aged 15–20 in Norway, especially those close to their first real money decisions: a first pengegave, a first job, a first credit card at 18. They play in short bursts, often on a phone. Parents and teachers may suggest the game, but they are not users in version one (PRD §2.2).
- **Constraints:** Student team, a playable version delivered in December 2026, zero running cost, minors as users, minimal personal data. No AI in version one; AI as game master is planned for V2 (PRD §1, §4.3). Norwegian rules and real 2026 figures.
- **Success:** Users can explain how an earlier decision affected a later outcome, and the learning feels self-chosen rather than like schoolwork. The PRD turns this into playtest targets: 70% or more can explain the link, and a median of 4 or higher on "it felt more like a game than schoolwork" (PRD §7.1).
- **Existing research:** Finans Norge 2025, and the market research and competitor table in the brief. The player survey «Unge og penger», 133 responses, 22–29 October 2026 (`planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/user-research.md`). The team's hands-on playtest of Koll på cashen and PersonalFinanceLab (`planning-artifacts/research/playtest-competitors-2026-10-31/notes.md`).
- **Research rule:** The survey investigated the problem only, without revealing the solution idea. At the time, the idea was an AI-driven money game; the final PRD has no AI in version one. With the survey done, the later steps work with the concept. Playtesting the game is a separate, later step (PRD §7.1).

---

## 👥 EMPATHIZE: Understanding Users

**Sources and methods.** This step builds on the player survey «Unge og penger» (133 responses; `user-research.md`) and the team's competitor playtest notes. The methods are survey synthesis and empathy mapping. There were no interviews in this round, so the survey's free-text answers are the qualitative source. Percentages are of all 133 respondents.

### User Insights

1. **They know their balance, but not their future.** 88% know roughly how much money they have right now. Only 38% think about how a purchase affects their money months from now, and 39% often run out before they get more.
2. **Regret comes from small things that add up, not from big decisions.** The most frequent regrets are snacks, takeaway and drinks, then clothes, trend buys and collectibles such as blind boxes and Pokémon cards. «Jeg kjøper smågodt veldig ofte og pleier å angre ved slutten av uken når jeg ser hvor mye penger det blir til sammen.»
3. **Family is both the safety net and the teacher.** 68% get money from parents, and 88% learned most about money from family. In the trip dilemma, 26% would borrow from parents or friends. Of the 36% who had an unexpected expense that was hard to pay, about half got help from family.
4. **They want to learn, and they feel nearly ready.** 63% want to learn more about money, and 64% feel ready to make their own money choices at 18. Yet only 39% understand credit cards and consumer loans well, and 44% understand BSU well (26% among 15–16-year-olds).
5. **Credit is something they have not tried yet.** 4% have used a credit card or consumer loan, and 6% buy now pay later. Only one respondent chose either in the trip dilemma.
6. **Social pressure shows in what they regret, not in what they report.** Only 14% say they feel pressure from friends to spend. But the free text describes a jacket that was trending on TikTok and a laptop bought «bare på grunn av at jeg følte alle hadde en».
7. **Commitments catch them out.** A gym membership never used, and a subscription with a binding period they did not know about.
8. **They ask for plainer explanations, earlier.** They most want to learn budgeting and saving, interest, BSU, credit and loans, paying bills, and investing. Several ask for it to be explained more simply and taught earlier in school.

### Key Observations

**Surprises**
- **Saving is not the same as planning.** 73% save most or some of what they get, yet 39% often run out before the next money arrives.
- **Knowing a fact is not the same as acting on it.** 72% answered the credit-card question correctly (paying only the minimum costs more than the price). That is a quiz answer, not a habit. The PRD aims the game at behaviour: the player learns from what their own actions lead to, not from questions and answers (PRD §1).

**Pain points**
- Running out before the month ends: «jeg hadde ikke penger til andre ting, som feks mat i kantina, eller faste utgifter.»
- Being locked into something they did not understand: binding periods, memberships, and, for one respondent, BSU itself, where the money is locked and NOK 300,000 is «ikke nok til leilighet engang».

**Patterns**
- **Age gap.** The 15–16-year-olds understand BSU and credit least, and they are where the game starts.
- **Investing is a frequent wish**, including among 15–16-year-olds. It is out of version one (team decision, 2026-10-31).
- **They want to be taken seriously.** In the team's playtest, Koll på cashen felt slow, heavy and too childish for this age group. That matches the PRD's description of users who "want to feel grown-up" and don't want it to feel like homework (PRD §2).

**How the PRD answers these insights**

| Insight | Where the PRD answers it |
|---|---|
| 1. Not thinking ahead | Cause links, echo badges, "Hvorfor?" and "If you had chosen differently" (FR-36 to FR-39); upcoming costs in the money view (FR-57) |
| 2. Small things add up | Fixed and everyday costs with spending levels (FR-23); activity spend in the money view (FR-57); small purchases, trend buys and collectibles as event topics (FR-17) |
| 3. Family | Help from family, not always on offer and often partial (FR-27) |
| 4–5. Credit and BSU | Saving and BSU (FR-22); credit card from 18 (FR-26), worked through in UJ-4 |
| 6. Social pressure | Invitations from friends (FR-54, FR-55) and wellbeing with social life as one part (FR-33) |
| 7. Commitments | Everyday costs with a binding period, which can't be stopped before the period ends (FR-23); subscriptions with a binding period as an event topic (FR-17) |
| 8. Plain explanations | Tips in events (FR-19), "Hvorfor?" (FR-38) and disclosed simplifications (FR-40) |

**Limitations**
- A convenience sample, probably spread through the team's own networks and schools, so it is not representative.
- The behaviour is self-reported; peer pressure in particular looks under-reported.
- Only 8 respondents aged 19–20.
- No questions on the LifeMode concept, no parent survey, and no interviews in this round. Concept and gameplay are tested in the playtest (PRD §7.1).

### Empathy Map Summary

The young person aged 15–20, close to their first real money decisions. *Says* and *Does* come from the survey. *Thinks* and *Feels* are the team's interpretation of the free text.

| | |
|---|---|
| **Says** | "I'd like to learn more about money." "Explain it more simply, and earlier." «Jeg hadde ikke penger til andre ting.» "I'd ask my parents first." |
| **Thinks** | "I have control: I know what's in my account." "I'm nearly ready for 18." "A small purchase doesn't matter." "Credit is for later." |
| **Does** | Saves some of what they get. Buys snacks, takeaway and trend items on impulse. Asks family when money runs short. Has a bank card and savings account, but rarely credit. Learns from family, social media and their own mistakes. |
| **Feels** | Regret at the end of the week, when the small purchases add up. Caught out by binding periods. Pulled along by what others have. Wants to be treated as grown-up, not lectured. |

**Emotional arc in the PRD journeys.** The journeys follow one persona, Markus, and are design intent, not research data. They move from irritation (UJ-1, told to try it) to curiosity (UJ-3, his savings grew), panic and then tired relief (UJ-4, the credit card), and finally «a bit stupid, but proud» (UJ-5, the ending). The empathy map above supports the low points: running out, regret and feeling caught out are what the survey describes.

---

## 🎨 DEFINE: Frame the Problem

This step frames the problem as the final PRD answers it. The PRD is the basis; the framing here explains why its features exist and does not add requirements.

### Point of View Statement

> **A young person aged 15–20 in Norway, close to their first real money decisions, needs to see what today's choices lead to months and years later, and why, because they already know what is in their account but rarely think ahead, and the costs that hurt them most add up quietly from small purchases and commitments.**

Two narrower points of view support it:

- **At 18:** a young person about to get their first credit card needs to try credit before it costs them real money, because almost none of them have used it and fewer than half understand it well.
- **In everyday life:** a young person with school, a part-time job and friends needs to see that time is as limited as money, because their regrets are about what they got for the money, not about the amount.

### How Might We Questions

| How might we… | Where the PRD answers it |
|---|---|
| 1. …make the link between an earlier choice and a later outcome visible when it happens? | Cause links, echo badges, "Hvorfor?" and "If you had chosen differently" (FR-36 to FR-39) |
| 2. …make small purchases visible as they add up, without lecturing? | Spending levels and everyday costs (FR-23); activity spend in the money view (FR-57) |
| 3. …let players try credit and BSU safely before they meet them in real life? | Saving and BSU (FR-22); the credit card from 18 (FR-26); UJ-4 |
| 4. …make time feel as limited as money? | Month plan and activity slots (FR-52, FR-53); UJ-6 |
| 5. …make good money management mean more than the biggest balance? | Wellbeing (FR-33) and the four endings, including the hollow win (FR-41) |
| 6. …include family as a real part of the money world without making it a free rescue? | Help from family, not always on offer and often partial (FR-27) |
| 7. …make it feel grown-up and like a game, in a few minutes on a phone? | One in-game year a session (FR-15); tone and content (NFR-8); pace targets (PRD §7.1) |
| 8. …explain money in plain language without slowing play? | Tips (FR-19), "Hvorfor?" (FR-38) and disclosed simplifications (FR-40) |

### Key Insights

1. **The problem is foresight, not knowledge.** They know their balance (88%) and can answer a quiz question on credit (72%), but only 38% think months ahead. The game has to train the link between choice and consequence, not teach facts. This is why the PRD makes the player learn from what their own actions lead to, not from questions and answers (PRD §1).
2. **The gap is widest where the stakes are highest.** At 18, credit opens for the first time, and credit and BSU are the least understood terms. That makes 18 the turning point in a playthrough (UJ-4).
3. **Money, time and wellbeing are one problem.** The regrets are about value and satisfaction, and a part-time job costs free time. A player who wins only on money gets a hollow win.
4. **Family is part of the real environment.** Family is the main source of money, knowledge and help, so leaving it out would make the game less true to life. Making it a free rescue would teach the wrong lesson.
5. **Respect and pace decide whether they play at all.** They want to feel grown-up, they play in short bursts, and the closest competitor felt slow and childish. If it feels like schoolwork, it fails, however correct the content is.

**Assumptions to watch.** The PRD tests these in the playtest (PRD §7.1, §7.2):
- That understanding consequences in a game carries over to real choices. Measured as explaining an earlier choice's effect (70% or more) and the money quiz before and after.
- That results from testers aged 18–20 say something about 15–17-year-olds. The PRD notes this as a validity limit.
- That wellbeing makes sense without making the game complicated. Measured as explaining the wellbeing score and the ending (60% or more).

---

## 💡 IDEATE: Generate Solutions

### Selected Methods

{{ideation_methods}}

### Generated Ideas

{{generated_ideas}}

### Top Concepts

{{top_concepts}}

---

## 🛠️ PROTOTYPE: Make Ideas Tangible

### Prototype Approach

{{prototype_approach}}

### Prototype Description

{{prototype_description}}

### Key Features to Test

{{features_to_test}}

---

## ✅ TEST: Validate with Users

### Testing Plan

{{testing_plan}}

### User Feedback

{{user_feedback}}

### Key Learnings

{{key_learnings}}

---

## 🚀 Next Steps

### Refinements Needed

{{refinements}}

### Action Items

{{action_items}}

### Success Metrics

{{success_metrics}}

---

_Generated using BMAD Creative Intelligence Suite - Design Thinking Workflow_
