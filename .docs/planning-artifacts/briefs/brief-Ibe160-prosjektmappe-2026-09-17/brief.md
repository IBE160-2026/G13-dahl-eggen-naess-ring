---
title: LifeMode Product Brief
status: draft
created: 2026-09-17
updated: 2026-09-17
---

# Product Brief: LifeMode

> **1. utkast** — dette er et førsteutkast til produktbrief, lagt frem for gjennomgang og godkjenning av resten av gruppen før det anses som endelig.

## Executive Summary

LifeMode is an AI-native life and personal finance simulation game for young people aged approximately 14–20, built as an IBE160 course project by a student team, for delivery in December 2026, targeting Norway first.

The player creates an avatar and progresses through realistic life stages — confirmation money, a summer job, saving, driving licence, education, moving out, rent, credit, a first car, and larger financial decisions. Every decision carries forward: saving early opens future options, using credit solves a short-term problem but raises future pressure, a cheap car may mean expensive repairs later. The core idea is simple: **let young people make expensive financial mistakes before those mistakes cost real money.**

What makes this possible is a specific architectural split. An AI model acts as the "Life Game Master," generating events, NPCs, dilemmas, and branching narrative from the player's simulated state and history — so no two playthroughs, and no two players, converge on the same story. A separate, deterministic financial engine owns all the math: interest, savings growth, debt, income, and budgets. The AI creates the life; the financial engine determines the consequences. No product on the market today combines these two things for this audience, in this market — see [What Makes This Different](#what-makes-this-different).

## The Problem

Many young people enter adulthood without an intuitive understanding of how financial decisions interact over time. Savings, interest, credit, debt, fixed expenses, rent, budgeting, and emergency funds may be understandable in theory but feel abstract until they have real consequences.

Example: you have NOK 1,500. Your friends are going on a trip costing NOK 3,200. Stay home, work extra, borrow, or use credit? A few simulated months later, the player sees how that choice affected debt, monthly expenses, and future opportunities.

Today, these lessons are mostly learned through parents, school, online content, or real-world trial and error — and real-world trial and error is expensive. Finans Norge's own 2025 research states that Norwegian youth "struggle with financial knowledge" and that schools "aren't using the potential" to address it — the industry body most invested in financial literacy is naming the same gap LifeMode targets.

## The Solution

LifeMode turns personal finance into a dynamic life simulation across the stages above, where every decision reshapes the life ahead. The goal is not simply to become as rich as possible: the game balances financial security, freedom, lifestyle, debt, time, and stress, so personal finance becomes part of the player's life story rather than a separate learning module.

**AI as the game engine, not a chatbot feature.** The AI Game Master generates life events, dilemmas, NPCs, conversations, and branching storylines based on the player's current simulated situation and history — for example, a player with an old car, little savings, and existing credit debt may face a realistic repair crisis. A deterministic financial engine calculates everything numeric: interest, debt, repayments, income, recurring expenses, budgets. The central loop is: **choose → consequence → AI-generated new situation → adapt → continue life.**

This split isn't incidental — it's the answer to a real design question the team pressure-tested during discovery: *why does this need an LLM instead of hand-authored branching content?* Two concrete answers, not "AI is more scalable" in the abstract:

1. **Combinatorial narrative variety.** The story must react coherently to a near-infinite combination of accumulated state (age × savings × debt × prior choices). Hand-authoring branches to cover that space doesn't scale; an LLM can generate a specific, coherent situation from state on demand.
2. **Open-ended negotiation.** Players can argue with an NPC — e.g., negotiating a lower interest rate with the bank — where argument quality genuinely affects the outcome, not a fixed menu of pre-written responses.

That second mechanic reintroduces a known risk (an LLM being too agreeable, undermining the "let consequences bite" premise), so the team set a guardrail: the deterministic engine sets a base value and a bounded interval, and the AI can only select a result *within* that interval based on argument quality — never outside it. The AI does not get to be lenient; realism is the design goal, not friendliness. (Detail: [addendum.md](addendum.md#ai-negotiation-mechanic--guardrail-detail).)

## Win Condition

At the start of a playthrough, the player receives a mission: reach a target net worth by around age 20. The target is randomized/personalized per playthrough rather than fixed, so no two players are chasing the same number — reinforcing that no two playthroughs should converge on the same story.

Net worth alone isn't the whole picture. A parallel **happiness/wellbeing meter** ("lykkebarometer") tracks what a pure net-worth number hides: stress, free time, social life, housing quality. Like the financial numbers, it is computed deterministically from measurable state (debt load, hours worked, living conditions, free time) — the AI creates the situations that move these numbers, but does not judge the outcome itself, keeping the "the AI creates the life, the financial engine determines the consequences" principle intact.

This produces three possible endings, not a binary win/lose:

1. **Real win** — net worth target reached and wellbeing stayed above a healthy threshold.
2. **Hollow win** — net worth target reached, but wellbeing collapsed getting there: the money cost too much.
3. **Loss** — net worth target missed, or an unmanageable debt spiral occurs before the deadline.

## What Makes This Different

The market splits into two camps that don't overlap:

- **Life-simulation games** (e.g. BitLife) have narrative and choice, but finance is shallow flavor — reviewers note it can even desensitize players to financial recklessness, the opposite of a literacy goal.
- **Teen financial-literacy apps** (Zogo, Greenlight, EVERFI, and the closest Nordic comparable, Sweden's Gimi) have correct-ish financial content and proven bank/school distribution, but deliver it as quizzes or courseware — no narrative agency, no branching consequence.

No product found — in this research, globally or in Norway — pairs a deterministic, correct financial engine with an LLM-generated branching life narrative. In Norway specifically, existing efforts (Nordea's Økonomipeil, Finans Norge's Skolemeny/Pengequiz, Gimi) are courseware or quiz-based; none is a simulation. LifeMode would be a domestic first-mover on this combination. Full competitive landscape and sources: [addendum.md](addendum.md#competitive--comparable-landscape-research-detail).

**Honest caveat:** the team is aware of the obvious rebuttal — Zogo and EVERFI already prove that bank/school distribution works with cheap, fully-controllable static content, so an evaluator may reasonably ask whether an LLM is worth its cost and risk versus a well-designed decision tree. The answer the team is building toward is the combinatorial-narrative and open-ended-negotiation mechanics above; this should be validated, not just asserted, once a playable MVP exists.

## Who This Serves

**Primary users** — Young people aged approximately 14–20, especially those approaching their first major financial decisions. Success for the player means understanding financial consequences better, without it feeling like schoolwork.

**Parents** — May pay for a family version giving teenagers a safe environment to make financial mistakes, and giving parents an easier way into money conversations (including visibility into event categories their teen encountered — see addendum).

**Schools** — Can use selected scenarios to teach budgeting, credit, saving, and living costs interactively.

**Banks and other partners** — Banks, insurers, or municipalities may fund access through financial literacy initiatives. Any partnership stays independent from the game's financial logic and must not become disguised financial advertising.

## Business Model

LifeMode can combine several revenue streams, so it is not solely dependent on teenagers paying directly:

- **Family Premium** — parents pay for expanded simulations, family challenges, and additional content.
- **School licences** — schools pay per class, pupil, or institution.
- **B2B2C partnerships** — banks, insurers, or other organizations fund access as part of financial literacy initiatives (a channel already proven for EVERFI, Zogo, and Nordea's Økonomipeil).
- **Scenario packs** (future) — modules such as moving out, first car, student life, credit and debt, first job, housing.

## Scope

**MVP** simulates roughly ages 15–20, with a limited number of meaningful decisions: confirmation money or initial savings, summer job, first salary, spending versus saving, basic interest, subscriptions, driving licence, education, moving away from home, rent, food and living costs, credit, unexpected expenses, and emergency savings. It should feel like a complete simulated life stage, not a collection of disconnected quizzes.

**Explicitly out of scope for MVP:** real bank connections, real financial data, personalized financial advice, real investments, cryptocurrency, advanced mortgages, complex tax calculations, real-money transactions.

The goal is to validate whether users enjoy the core loop enough to keep playing, and whether they develop a stronger understanding of financial consequences.

## Technology Overview

LifeMode is a website — a mobile-first, responsive web application (smartphones, tablets, laptops, desktop) that should feel like a mobile game even though it runs in the browser. Responsive behavior is a core requirement from the start, tested across small mobile widths, tablet, and desktop.

- HTML / CSS for structure and responsive styling
- JavaScript / TypeScript for frontend interactivity
- Python for the backend — game logic, the deterministic financial simulation engine, and orchestration of calls to the AI Game Master API
- Supabase for database, authentication, and backend services
- A free-tier LLM API as the runtime AI Game Master — provider not locked in yet (candidates include Google Gemini's free tier or an open-weight model via a free host such as Groq); final choice is an architecture-phase decision. **Zero ongoing cost is a hard constraint**: the team has no budget for paid API usage, so the chosen provider's free-tier rate limits are a real design boundary, not just a cost-optimization — and reduced safety-tuning guarantees relative to a frontier provider are a tradeoff to design around (see Privacy & Safety).
- Claude Code as the development assistant; BMAD Method as the development methodology

High-level flow: responsive frontend (HTML/CSS/JS) → Python backend (financial simulation engine + orchestration) → Supabase (database/auth) and the AI Game Master API → validation and game rules → updated player state → game interface.

## Privacy & Safety

Because the audience includes minors, LifeMode collects as little real-world personal information as possible. The MVP needs no bank access, real salary information, national identity numbers, location history, contact lists, or private messages — the game economy is fully simulated (e.g. `simulated_age`, `simulated_savings`, `simulated_income`), and the AI never needs the player's real identity.

Because the entire user base is 14–20 and the closest structural comparable (an LLM driving open-ended narrative) has a well-documented 2021 safety incident involving minors, the team is treating content safety as a named risk to design against from the start, not an afterthought. This matters more, not less, given the zero-budget constraint on the AI provider (see Technology Overview): a free-tier or open-weight model cannot be assumed to carry the same safety tuning as a frontier provider, so the structured-output and pre-display moderation principles below carry more of the safety burden by design, rather than relying on the model's own training. Working design principles (structured AI output, constrained player input for negotiation, pre-display moderation, no human reading of private sessions, parent-facing visibility as a feature) are recorded for the architecture phase in [addendum.md](addendum.md#ai-safety--content-moderation--design-principles).

**Open concern: the AI going out of control.** Even with a minimal-PII, fully simulated economy by design, the AI narrative/negotiation layer introduces a specific, unresolved privacy risk: an open-ended AI conversation could drift into asking for or generating real personal information, or otherwise behave unpredictably in a way that undermines the privacy-by-design intent. This is flagged here as a known open concern for the architecture phase, not yet mitigated — distinct from the content-moderation risk above.

## Success Criteria

The first pilot should demonstrate that:

- most users complete the first simulated life stage
- at least 50% voluntarily return for another session
- users describe the experience as more like a game than schoolwork
- players can explain how previous decisions affected later outcomes
- understanding of key financial concepts improves
- users want to replay with different choices
- different playthroughs produce meaningfully different stories

Early commercial validation should include interest from parents, at least one school willing to test the product, and interest from potential institutional partners.

## Vision

If LifeMode succeeds, it can evolve from a personal finance game into a broader AI-powered simulation of adulthood: education → career → salary → housing → relationships → loans → insurance → family → investments → unexpected life events. The long-term ambition is a safe environment where young people can experience important adult decisions before those decisions become real.

LifeMode is where you learn how life works by living it once before it counts.
