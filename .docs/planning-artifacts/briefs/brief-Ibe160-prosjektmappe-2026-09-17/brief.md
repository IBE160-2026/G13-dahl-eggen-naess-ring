---
title: LifeMode Product Brief
status: draft
created: 2026-09-17
updated: 2026-10-22
---

# Product Brief: LifeMode

> Draft for group review. Detail that does not belong in a 1-2 page brief (competitor research, AI guardrail design, safety principles, business model) lives in [addendum.md](addendum.md) and moves on to the PRD and architecture.

## Executive Summary

For young people aged 15-20 in Norway, LifeMode is a mobile-friendly life and money simulation game where every choice carries forward. You save early and it opens options later; you use credit to solve a problem today and it raises the pressure tomorrow; a cheap first car turns into an expensive repair. The idea is simple: **let young people make expensive financial mistakes before those mistakes cost real money.**

Today, most young people meet credit, rent and fixed costs for the first time with real money. School and online content explain the concepts, but they feel abstract until the consequences arrive. Now is a good time to change this: free-tier AI models can generate a situation that fits each player's own history at no cost, and Finans Norge's 2025 research says Norwegian youth "struggle with financial knowledge" and that schools "aren't using the potential" to address it.

LifeMode is an IBE160 course project built by a student team, targeting Norway first, with a working first version due in December 2026.

## The Problem

Many young people enter adulthood without an intuitive understanding of how financial decisions interact over time. Savings, interest, credit, debt, rent and budgets can be understood in theory, but they feel abstract until they cost something.

Example: you have NOK 1,500 and your friends are going on a trip that costs NOK 3,200. Do you stay home, work extra, borrow, or use credit? Months later, the effect of that choice shows up in your debt, your monthly costs and the options you have left.

Today these lessons come from parents, school, online content, or real-world trial and error. Real-world trial and error is the one that actually sticks, and it is also the expensive one.

## The Solution

The player creates an avatar and lives through a simulated stretch of life from age 15 to 20: first money, part-time and summer jobs, saving, everyday fixed costs, credit from age 18, and unexpected expenses. Each decision changes the situation the player meets next. The player sees why their life looks the way it does, because a choice made in month 3 comes back in month 9.

**The game loop.** The game moves forward one simulated month at a time:

1. **See the situation:** the player sees this month's event or dilemma together with their current money: balance, savings, debt and fixed costs.
2. **Choose:** the player picks one of a few options, e.g. stay home, work extra, borrow or use credit.
3. **See the consequence in numbers:** the financial engine applies the choice and shows what changed and why.
4. **Next month:** income, fixed costs, interest and instalments are applied, and the next situation builds on everything the player has done so far.

Quiet months without a dilemma are calculated automatically and shown as a short summary, so a full playthrough from 15 to 20 has about 20-30 real choices. When the financial engine detects a crisis (the account goes below zero, two missed minimum card payments in a row, or debt above three months of income), the month becomes a **crisis month**: two or three linked choices where the player tries to deal with the problem, for example by selling something, taking extra shifts, asking for a payment plan or ignoring it. A crisis does not end the game in version one; ignored debt keeps growing and leads to new crisis months.

Two things change for the player. First, personal finance becomes part of a life story rather than a separate lesson, so it feels like a game rather than schoolwork. Second, the story is different for each player, because the situations they meet come from their own choices and history, so replaying with different choices gives a different life.

## What Makes This Different

| Alternative today | Why users tolerate it | Why LifeMode is better |
|---|---|---|
| Parents, school, online content | Familiar and free | Learning by doing, not by being told, and safe to get wrong |
| Life-sim games (e.g. BitLife) | Fun, with lots of choice | Finance is shallow flavour there; here the money is correct and the consequences are real |
| Teen finance apps (Zogo, Greenlight, EVERFI, Sweden's Gimi; in Norway Økonomipeil, Skolemeny, Pengequiz) | Correct content, and banks and schools already distribute them | They are quizzes and courseware with no story of your own; LifeMode is a simulation |
| Learning from real mistakes | Nothing to set up | Same lesson, without the real cost |

What LifeMode combines, and what we did not find elsewhere in our research, is a **financial engine that always calculates correctly** together with an **AI that creates events and dilemmas from the player's own history**. The AI creates the life; the engine decides the consequences. Why an AI rather than a hand-written decision tree: the story has to fit a huge combination of age, savings, debt and earlier choices, and hand-written branches do not scale to that.

**What the advantage is, and is not:** it is not a technical moat, since anyone could combine a financial engine with an AI. Our edge is being first with this combination for Norwegian teenagers, and a small team that can iterate quickly on what playtesters tell us.

**Honest caveat:** Zogo and EVERFI show that cheap, fully controlled static content already works and is already distributed. The AI is only worth its cost and risk if playtesters experience clearly more varied and more personal stories than a decision tree would give. We will test that, not assume it.

## Who This Serves

**Primary user:** young people aged 15-20, especially those approaching their first real financial decisions. The first version simulates the same span, ages 15-20. They want to feel grown-up and make their own choices, and they do not want it to feel like homework. Success in their day: a 10-15 minute session on their phone, after which they can say "that's why that happened" about a decision they made.

Parents, schools and banks may later pay for or fund access, but the first version is designed for the player.

## Success Criteria

Two kinds of criteria: playtest criteria that need real players, and functional criteria that become automated test cases and need no player at all. The targets below are proposals for the group to adjust.

### Playtest (small group, 10-20 people, before December delivery)

Because most of the target group are minors, the playtest is run with fellow students and other volunteers aged 18-20, the upper end of the target group, who can consent for themselves. Players aged 15-17 join only with written consent from a parent or guardian, and only if the group has time to handle that properly; the playtest does not depend on them. No names or contact details are stored with the results: debrief answers and quiz scores are recorded anonymously.

| Signal | Metric / evidence | Target | When measured |
|---|---|---|---|
| User outcome | Player explains in their own words how an earlier decision affected a later outcome | 70% or more | Short debrief right after the session |
| User outcome | Average score on a 5-question money quiz, before vs. after | Higher after | Before and after one session |
| Behaviour | Complete the first simulated life stage | 70% or more | During the session |
| Behaviour | Voluntarily come back for a second session or replay | 50% or more | Within one week of the first session |
| Experience | "It felt more like a game than schoolwork" (1-5) | Median 4 or higher | Debrief |
| Experience | Two playthroughs with different choices are described as different stories | Most players | After replay |
| Mission | At least one parent or teacher who sees it wants to try it | Yes | After the playtest |

### Functional / testable (automated, no playtest needed)

| # | Criterion | Expected result | How tested |
|---|---|---|---|
| F1 | Consumer loan of NOK 20,000 at 15% over 12 months | Monthly payment NOK 1,805, final payment NOK 1,808, total paid NOK 21,663 | Unit test against Rule Set v1 worked example 3 |
| F2 | NOK 10,000 in a savings account for 12 months at 2.87% | Balance NOK 10,289 | Unit test against worked example 2 |
| F3 | Credit card debt of NOK 3,200, minimum payments only | Paid off after 13 months, total paid NOK 3,606 | Unit test against worked example 4 |
| F4 | A crisis trigger condition is met (account below NOK 0, two missed minimum payments in a row, or debt above 3x average monthly income) | Engine starts a crisis month with linked choices every time; never silently skipped | Unit test per trigger condition |
| F5 | AI returns an invalid, malformed, or unsafe event | Game shows a pre-written fallback event; never a blank screen or unfiltered output | Automated test with a mocked failing AI response |
| F6 | A full playthrough from age 15 to 20 | Completable start to finish using only the pre-written event library, with zero AI calls | Automated run with AI disabled |
| F7 | Summer job at 16: 120 hours at the under-18 hourly wage (NOK 139.40) | NOK 16,728 paid out, no tax withheld (below the frikort limit) | Unit test against worked example 1 |
| F8 | An 18-year-old earns NOK 110,000 in one calendar year | NOK 5,000 tax (50% of the NOK 10,000 above the frikort limit) | Unit test against worked example 5 |

All worked examples and the full rule set are in [addendum.md](addendum.md#financial-engine--rule-set-v1).

## Scope

**In (version one)**

1. Create an avatar and live a simulated stretch of life from 15 to 20 with five money mechanisms: wages from part-time and summer jobs, saving (savings account and BSU), fixed costs (mobile and transport), consumer loans and credit cards from age 18, and unexpected expenses. Quiet months are skipped, and crisis months give the player linked choices to handle a problem.
2. A financial engine that follows a small, written rule set with realistic Norwegian 2026 numbers: wages, frikort tax, savings interest, consumer loans and credit cards (only from age 18, as in Norway), and fixed costs such as mobile and transport. Every month is processed in the same order and in whole kroner, and worked examples with expected results serve as the test answer key. Rules, sources and examples are in [addendum.md](addendum.md#financial-engine--rule-set-v1).
3. AI-generated events and dilemmas that fit the player's own situation and history.
4. AI output that is structured and checked before the player sees it. If the AI fails, times out, or returns an invalid or unsafe event, the game shows a pre-written event instead, so the player never sees a blank screen or unchecked output.
5. A library of pre-written events that lets the whole game be played from start to finish without the AI. This mode is also used for automated tests and when the app is run without an AI key.
6. A mobile-first responsive website, built with a free-tier AI model (zero ongoing cost).

**Out (not now)**

1. Open-ended negotiation with NPCs (e.g. arguing with the bank).
2. The endgame system: a win condition and wellbeing meter, and how they resolve into an ending. Shape not decided; options under discussion is in [addendum.md](addendum.md#win-condition--endgame-design-discussion-not-decided).
3. Parent visibility into what their teen encountered.
4. Real bank connections, real financial data, personal advice, investments, crypto, advanced mortgages, complex tax, real-money transactions.
5. Payments, family or school accounts, and partner features.
6. Further life areas, planned as later steps: moving out and rent first, then driving licence and education.

Scope test: without items 1-3 and 6 on the Out list, we can still find out whether the AI-driven life is fun and teaches consequences.

## Constraints and Open Risks

Because the players are minors, LifeMode collects as little real personal information as possible: the whole economy is simulated and the AI never needs the player's real identity. A free-tier model carries less built-in safety tuning than a frontier model, so checking the AI's output before display carries more of the safety work. An unresolved concern for the architecture phase is that an open-ended AI could drift into asking for or producing real personal information. Design principles are in [addendum.md](addendum.md#ai-safety--content-moderation--design-principles).

The MVP depends on Supabase (including authentication, since v1 has login from the start) and a free-tier AI provider. We considered dropping login and saving the game locally for v1, as suggested in feedback, and chose to keep it. A playthrough from 15 to 20 is longer than one sitting, so the player must be able to take a break and pick up the same life later, also on another device. The project is also expected to use a database, and building on it from the start is a deliberate trade-off: a little more setup now instead of rebuilding storage later, when we would need it anyway. Login stores only what authentication needs, never real personal details in the game itself. Supabase runs self-hosted via Docker for local development and evaluation, so a sensor can run the full application without the team's own cloud account or database keys. Only the AI provider key needs to be supplied separately, or the game runs AI-free end to end using the pre-written event library (Scope In, item 5).

## Vision

**Now:** prove that an AI-driven life story with correct money mechanics is fun and makes consequences understandable. **Next:** add moving out and rent, driving licence and education, negotiation, the wellbeing meter and endings, a parent view and scenarios for schools. **In 2-3 years:** a wider simulation of adulthood, covering education, career, housing, relationships, loans, insurance and family, where young people can experience important adult decisions before they are real.

LifeMode is where you learn how life works by living it once before it counts.