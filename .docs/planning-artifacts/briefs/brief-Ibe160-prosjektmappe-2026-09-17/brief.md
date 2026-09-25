---
title: LifeMode Product Brief
status: draft
created: 2026-09-17
updated: 2026-09-24
---

# Product Brief: LifeMode/Aftermath/Ripple (game name is not set)

> Draft for group review. Detail that does not belong in a 1-2 page brief (competitor research, AI guardrail design, safety principles, business model) lives in [addendum.md](addendum.md) and moves on to the PRD and architecture.

## Executive Summary

For young people aged about 14-20 in Norway, LifeMode is a mobile-friendly life and money simulation game where every choice carries forward. You save early and it opens options later; you use credit to solve a problem today and it raises the pressure tomorrow; a cheap first car turns into an expensive repair. The idea is simple: **let young people make expensive financial mistakes before those mistakes cost real money.**

Today, most young people meet credit, rent and fixed costs for the first time with real money. School and online content explain the concepts, but they feel abstract until the consequences arrive. Now is a good time to change this: free-tier AI models can generate a situation that fits each player's own history at no cost, and Finans Norge's 2025 research says Norwegian youth "struggle with financial knowledge" and that schools "aren't using the potential" to address it.

LifeMode is an IBE160 course project built by a student team, targeting Norway first, with a working first version due in December 2026.

## The Problem

Many young people enter adulthood without an intuitive understanding of how financial decisions interact over time. Savings, interest, credit, debt, rent and budgets can be understood in theory, but they feel abstract until they cost something.

Example: you have NOK 1,500 and your friends are going on a trip that costs NOK 3,200. Do you stay home, work extra, borrow, or use credit? Months later, the effect of that choice shows up in your debt, your monthly costs and the options you have left.

Today these lessons come from parents, school, online content, or real-world trial and error. Real-world trial and error is the one that actually sticks, and it is also the expensive one.

## The Solution

The player creates an avatar and lives through a simulated stretch of life, roughly ages 15-20: first money, a summer job, saving, driving licence, education, moving out, rent, credit and unexpected expenses. Each decision changes the situation the player meets next. The player sees why their life looks the way it does, because a choice made in month 3 comes back in month 9.

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

**Primary user:** young people aged about 14-20, especially those approaching their first real financial decisions (the first version simulates ages 14-20). They want to feel grown-up and make their own choices, and they do not want it to feel like homework. Success in their day: a 10-15 minute session on their phone, after which they can say "that's why that happened" about a decision they made.

Parents, schools and banks may later pay for or fund access, but the first version is designed for the player.

## Success Criteria

Measured in a small playtest (10-20 people in the target age group) before the December delivery. The targets below are proposals for the group to adjust.

| Signal | Metric / evidence | Target | When measured |
|---|---|---|---|
| User outcome | Player explains in their own words how an earlier decision affected a later outcome | 70% or more | Short debrief right after the session |
| User outcome | Average score on a 5-question money quiz, before vs. after | Higher after | Before and after one session |
| Behaviour | Complete the first simulated life stage | 70% or more | During the session |
| Behaviour | Voluntarily come back for a second session or replay | 50% or more | Within one week of the first session |
| Experience | "It felt more like a game than schoolwork" (1-5) | Median 4 or higher | Debrief |
| Experience | Two playthroughs with different choices are described as different stories | Most players | After replay |
| Quality / trust | All money numbers match an independent check of the financial engine | 100% | Before the playtest |
| Quality / trust | Unsafe or off-topic AI output shown to a player | Zero | During the playtest, from logs |
| Mission | At least one parent or teacher who sees it wants to try it | Yes | After the playtest |

## Scope

**In (version one)**

1. Create an avatar and live a simulated stretch of life, ages about 15-20, with the key money decisions: saving, first job, spending vs. saving, driving licence, education, moving out and rent, credit, unexpected expenses.
2. A financial engine that calculates all numbers correctly and consistently: income, interest, debt, expenses.
3. AI-generated events and dilemmas that fit the player's own situation and history.
4. AI output that is structured and checked before the player sees it.
5. A mobile-first responsive website, built with a free-tier AI model (zero ongoing cost).

**Out (not now)**

1. Open-ended negotiation with NPCs (e.g. arguing with the bank).
2. The endgame system: a win condition and wellbeing meter, and how they resolve into an ending. Shape not decided; options under discussion is in [addendum.md](addendum.md#win-condition--endgame-design-discussion-not-decided).
3. Parent visibility into what their teen encountered.
4. Real bank connections, real financial data, personal advice, investments, crypto, advanced mortgages, complex tax, real-money transactions.
5. Payments, family or school accounts, and partner features.

Scope test: without items 1-3 on the Out list, we can still find out whether the AI-driven life is fun and teaches consequences.

## Constraints and Open Risks

Because the players are minors, LifeMode collects as little real personal information as possible: the whole economy is simulated and the AI never needs the player's real identity. A free-tier model carries less built-in safety tuning than a frontier model, so checking the AI's output before display carries more of the safety work. An unresolved concern for the architecture phase is that an open-ended AI could drift into asking for or producing real personal information. Design principles are in [addendum.md](addendum.md#ai-safety--content-moderation--design-principles).

## Vision

**Now:** prove that an AI-driven life story with correct money mechanics is fun and makes consequences understandable. **Next:** add negotiation, the wellbeing meter and endings, a parent view and scenarios for schools. **In 2-3 years:** a wider simulation of adulthood, covering education, career, housing, relationships, loans, insurance and family, where young people can experience important adult decisions before they are real.

LifeMode is where you learn how life works by living it once before it counts.