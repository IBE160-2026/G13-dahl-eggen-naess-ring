---
title: LifeMode Product Brief
status: draft
created: 2026-09-17
updated: 2026-09-20
---

# Product Brief: LifeMode/Aftermath/Ripple (game name is not set)

> **1. utkast** — dette er et førsteutkast til produktbrief, lagt frem for gjennomgang og godkjenning av resten av gruppen før det anses som endelig.

## Executive Summary

LifeMode is an AI-native life and personal finance simulation game for young people aged approximately 14–20 in Norway. Players create an avatar and move through realistic life stages such as receiving confirmation money, getting a summer job, saving, studying, moving away from home, paying rent, using credit and managing unexpected expenses. Decisions carry forward, meaning choices made early in the game can create opportunities or problems later. The core idea is simple: Let young people make expensive financial mistakes before those mistakes cost real money.

Instead of teaching personal finance mainly through quizzes, theory or isolated examples, LifeMode lets players experience financial consequences inside a safe simulation. An AI-powered Life Game Master generates events, dilemmas, NPCs and branching situations based on the player's accumulated state and previous choices, while a separate deterministic financial engine handles income, expenses, savings, debt, interest and other numerical consequences. This matters because many financial concepts remain abstract until they affect real choices, and recent Norwegian research points to gaps in young people's financial knowledge and unused potential for more practical financial education.

The timing is favorable because generative AI now makes adaptive, state-driven simulation experiences more feasible than traditional fixed decision trees. The first MVP targets Norwegian users aged 14–20 and is being developed as part of the IBE160 course for delivery in December 2026. If successful, LifeMode can grow over the next 2–3 years into a broader AI-powered simulation of early adulthood, covering increasingly complex decisions around education, career, housing, relationships, loans, family and long-term financial trade-offs.

---

## The Problem

Young people gradually enter adult financial life without necessarily understanding how financial decisions interact over time. Concepts such as saving, interest, credit, debt, fixed expenses, rent, budgeting and emergency funds may be understandable in theory, but they often remain abstract until they create real consequences.

For example, a young person may have NOK 1,500 available while friends plan a trip costing NOK 3,200. Do they stay home, work extra shifts, borrow money or use credit? Credit may solve the immediate problem, but later repayments and interest can reduce the money available for rent, food, transport or future opportunities. 

Today, young people mainly learn these lessons through parents, school, online content or real-world trial and error. Research highlighted by Finans Norge in 2025 shows that Norwegian youth have only moderate knowledge of personal finance, particularly around interest, loans and long-term planning, while also pointing to significant untapped potential for more practical financial education in upper-secondary schools. [Finans Norge, 2025][finans-norge]

The cost of the status quo is that many important financial lessons are learned only after real money is involved. A poor decision can create debt, reduce future flexibility and become expensive before the person fully understands why. The opportunity is therefore to let young people experience financial trade-offs and consequences before those decisions become real.

---

## The Solution

LifeMode turns personal finance into a dynamic life simulation rather than a traditional financial-literacy course. The first version follows the player from approximately age 14 to 20 through interconnected decisions involving: initial savings → summer job → spending → saving → driving licence → education → moving out → rent → recurring expenses → credit → unexpected costs

Every choice changes the player's financial and life situation. A player who spends most of their savings early may have fewer options later. A player who buys an inexpensive older car may face repair costs. A player who has built an emergency fund may handle the same event without taking on debt.

An AI-powered Life Game Master uses the player's accumulated state and previous decisions to generate relevant events, dilemmas, NPCs, conversations and branching situations. A separate deterministic financial engine ensures that financial consequences remain consistent and realistic.

The design principle is: The AI creates the life; the financial engine determines the consequences.

This creates the core gameplay loop: Choose → consequence → updated state → AI-generated situation → adapt → continue life

### Why generative AI?

The use of generative AI answers a central design question:
**Why does this need an LLM instead of hand-authored branching content?**

There are two concrete reasons:

1. **Combinatorial narrative variety**
The story must react coherently to a near-infinite combination of accumulated state (age × savings × debt × possessions × prior choices × current circumstances). Hand-authoring branches to cover that space doesn't scale; an LLM can generate a specific, coherent situation from state on demand.

2. **Open-ended interaction and negotiation**
Players can argue with an NPC — for example, negotiating a lower interest rate with the bank, where the quality of the player's reasoning genuinely affects the outcome, rather than the interaction being limited to a fixed menu of pre-written responses.

These interactions must still respect the game's financial rules. The AI cannot override those rules or simply reward the player because it is being agreeable. The goal is realistic consequence, not AI-generated leniency. Detailed negotiation guardrails are documented in [architecture_technical_design.md] and [addendum.md].

### How success is defined in the game

The objective is not simply to accumulate as much money as possible. At the start of a playthrough, the player can receive a longer-term mission, such as reaching a target net worth by the end of the simulated period. The target can vary between playthroughs so that players are not always pursuing the same goal.
  
Net worth alone is not the whole picture. A parallel simulated Life Balance score reflects factors such as working hours, free time, debt pressure, social life and living conditions.

Life Balance is strictly a game mechanic. It is not intended to measure the player's real happiness, mental health or psychological wellbeing. For example, working extreme hours may increase income and net worth while reducing free time and Life Balance. Spending money on an experience may reduce savings while improving other aspects of the simulated life.

A playthrough can therefore produce different outcomes:

> **Balanced success** - the financial target is reached while Life Balance remains sustainable  
> **Hollow financial success** — the financial target is reached, but at a high simulated personal cost
> **Unsuccessful run** — the target is missed or previous decisions create an unsustainable debt situation

The purpose is not to teach players that becoming as wealthy as possible is always the best outcome. It is to let them experience the trade-offs involved in building a financially sustainable life.

---

## What Makes This Different

Existing products generally approach this problem from two different directions.

1. **Life-simulation games**, such as BitLife, provide characters, choices and branching stories, but personal finance is primarily one part of the entertainment experience rather than a detailed financial-learning system.

2. **Teen financial-literacy products**, such as Zogo, Greenlight, EVERFI and Sweden's Gimi, focus more directly on financial knowledge but generally use lessons, quizzes, guided content or predefined scenarios rather than an open-ended life simulation with persistent narrative consequences.

In Norway, examples such as Nordea's Økonomipeil and Finans Norge's Skolemeny/Pengequiz also focus on financial education rather than a generative life simulation. 

In our initial competitive research, we have not identified a product aimed at this audience that combines a deterministic personal-finance simulation with an LLM-generated branching life narrative. This is an initial research finding rather than a claim that no comparable product exists globally. Full competitive research and source detail are documented in:[appendum](./appendum.md)

The central differentiation is the combination of: real financial consequences + persistent game state + generative life simulation

The project's advantage is not a proprietary AI model. At the MVP stage, there is no proven defensible technical moat. If the product succeeds, the advantage will come from execution: combining financial simulation, generative narrative, game design and safety into one coherent experience that is realistic enough to teach meaningful consequences while entertaining enough that young people voluntarily continue playing.

**Honest caveat**: Zogo and EVERFI demonstrate that bank- and school-distributed financial education can work with relatively cheap, highly controllable static content. An evaluator may therefore reasonably ask whether an LLM provides enough additional value to justify its added complexity, cost and risk compared with a well-designed decision tree.

The answer the team is building toward is the combination of **combinatorial narrative variety and open-ended negotiation described above**. This should be validated through the playable MVP rather than simply asserted.

---

## Who This Serves

- **Primary users** — Young people aged approximately 14–20 in Norway, especially those approaching their first meaningful financial decisions. They need a way to understand financial consequences through experience rather than theory. Success means making more informed choices and understanding how earlier decisions affect later opportunities, without the experience feeling like schoolwork. 

- **Potential secondary user/customer group** - Parents need a safe way for teenagers to practise financial decision-making and a better starting point for conversations about money. A future Family version could include shared scenarios, conversation starters and limited visibility into the types of situations a teenager has encountered without exposing private session content.Details in: [appendum](./appendum.md)

- **Future institutional customers and partners**

- **Schools** - could use selected scenarios as a practical supplement to financial education, particularly around budgeting, saving, credit and living costs. Success for schools would mean a more engaging way to teach financial consequences while giving teachers structured scenarios to work with.

- **Banks, insurers, municipalities and other organizations** - potential future B2B2C partners that could fund access through financial-literacy initiatives. This is a longer-term commercial hypothesis rather than part of the initial user-research phase, and any partnership should remain independent from the game's financial logic and avoid becoming disguised financial-product advertising.

---

## Success Criteria

The first version should demonstrate user value, technical viability and early evidence of commercial potential.

**User success**
User testing of the playable MVP should aim to show that:
- most users complete the first simulated life stage
- at least 50% voluntarily return for another session
- users describe the experience as more like a game than schoolwork
- players can explain how previous decisions affected later outcomes
- understanding of key financial concepts improves
- users want to replay with different choices
- different playthroughs produce meaningfully different stories
- users understand the trade-off between financial outcomes and Life Balance

These criteria will be evaluated through post-development user testing, not the initial discovery survey.

**Business validation**
Early commercial validation should measure:
- the share of surveyed parents who see value in a safe financial simulation for teenagers
- the share who indicate willingness to pay for a future Family version

Schools, banks, insurers, municipalities and other organizations remain longer-term commercial hypotheses and are not part of the initial validation phase.

**Technical success**
The MVP should also demonstrate that:
- the complete full-stack application can run locally
- authentication correctly identifies users and separates their stored data
- player accounts, game state, decisions and playthroughs persist correctly in the database
- AI-generated events can use stored player state and previous decisions as context
- the deterministic financial engine calculates financial consequences independently of the AI model
- AI output is validated before it can influence authoritative game state
- malformed or unexpected AI output does not corrupt the simulation
- the primary gameplay flow works on smartphones, tablets, laptops and desktop screens

---

## Scope

The MVP will simulate approximately ages 14–20 through a focused set of financial and life decisions, including initial savings, summer jobs and first salary, spending versus saving, interest, subscriptions, driving licence, education, moving out, rent, living costs, credit, a first car, unexpected expenses and emergency savings.

It should feel like a complete simulated life stage, not a collection of disconnected quizzes.

The MVP will include persistent player state, a deterministic financial engine, AI-generated life events and NPC interactions based on previous decisions, and a simulated Life Balance mechanic alongside financial progress. Open-ended interaction with AI-controlled NPCs is included, but financial outcomes must remain within boundaries defined by the deterministic game engine.

The MVP will be a mobile-first responsive web application supporting smartphones, tablets, laptops and desktops. It must be able to run locally without depending on paid runtime services. Public production deployment is not required for the MVP; the application may be tested locally or in a controlled test environment.

Because the target audience includes minors, the MVP follows privacy-by-design and data-minimization principles. It uses simulated financial information and does not require real bank accounts, real salary or debt information, national identity numbers or transaction data. AI-generated content cannot directly modify authoritative financial state and must remain within application-defined rules. Detailed security and AI-safety measures are documented in the technical architecture: [architecture_technical_design](./architecture_technical_design.md)

**Explicitly out of scope for the MVP**
The MVP will not include:
- real bank connections or real financial data
- personalized financial advice
- real investments or cryptocurrency
- advanced mortgages or complex tax calculations
- real-money transactions
- financial-product recommendations
- large-scale multiplayer functionality
- a fully simulated adult lifetime
- native iOS or Android applications

---

## Vision
If LifeMode succeeds, it can grow over the next 2–3 years from a financial simulation for ages 14–20 into a broader AI-powered simulation of early adulthood.

Players could face increasingly complex decisions around education, career, salary, housing, relationships, loans, insurance, family, investments and unexpected life events. The AI Game Master could create more varied and personalized life paths, while deterministic systems continue to control financial rules and long-term consequences.

Players could also pursue different long-term goals, such as financial freedom, home ownership, entrepreneurship, family life or a balanced lifestyle, increasing replayability and reinforcing that personal finance is ultimately about trade-offs rather than maximizing a single number.

Future versions could expand into family, school and partner-funded use, while keeping the core experience independent and financially neutral.

> "A safe simulation of adulthood where young people can experience important decisions before those decisions become real".

