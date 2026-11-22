# Product

<!-- impeccable:product-schema 1 -->

Source of truth: `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md` (status final). Where this file and the PRD disagree, the PRD wins.

## Platform

web

## Stack

Next.js on Vercel, the frontend team's choice (2026-11-22); Vercel passes `/api/*` on to the backend, so the browser sees one origin (architecture spine, AD-12/AD-13). The backend renders all game text as finished Norwegian strings with engine figures; the frontend owns only UI chrome text and the player information page. Self-hosted fonts, nothing loaded from third parties (NFR-3).

## Users

Young people aged 15-20 in Norway who are about to make their first real money decisions: a first pengegave, a first job, a first credit card at 18. Some come by choice, some because a parent or teacher told them to. They play in short bursts, mostly on a phone, often on the bus or bored in class (UJ-1, UJ-2). They want to feel grown-up and make their own choices, and they do not want it to feel like homework. Parents and teachers are not users in version one.

## Product Purpose

LifeMode is a life and money game. The player lives five years, from 15 to the 20th birthday, one in-game year per session (about 10-15 minutes on a phone). Every choice carries forward, and the game always shows why something changed. Success: playtesters can explain how an earlier choice affected a later outcome, and say it felt more like a game than schoolwork (PRD §7.1).

## Positioning

Time is as limited as money. Each month the player plans free time in a few activity slots, manages job hours and money, and reads what friends, family, the employer and the bank send to an in-game phone. Story events are the highlights, not the whole game. Wellbeing (stress, free time, social life) counts in the ending, so getting rich at any cost gives a hollow win. Built on real Norwegian 2026 rules: frikort, BSU, moped licence at 16, credit only from 18.

## Operating Context

- One in-game year per session; four active months a year (January, April, July, October) with a story event, the rest quiet months that can be done in one tap.
- Four game areas: month plan, phone, job view, money view, plus the player's room that changes with belongings.
- Time is shown on a yearly basis (month name plus age / year of life). Screens never show a running month number such as "month 36".
- The player can't type free text beyond the email address and can't reply to messages.
- Every choice is a server round trip; the device shows saving, offline and "updated on another device" states.

## Capabilities and Constraints

- No AI anywhere in version one. All events, activities and messages are pre-written.
- The engine decides every figure; the frontend never calculates money.
- Option wellbeing effects are hidden until after the pick.
- Four endings: real win, hollow win, goal not reached (never framed as failure), loss.
- Driving minigame for licences is turn-based: no timing, motion or gestures.
- Month plan works by tapping, never dragging.

## Brand Commitments

- Name: LifeMode. Player-facing text in Norwegian, plain enough for a 15-year-old.
- Visual style is grown-up, not childish (NFR-8).
- Tips sound like tips, not lectures. Warnings and crises state the consequence plainly and never scold.
- Options read as actions, never quiz answers. Free time is never framed as wasted money.
- No tobacco or alcohol content. Chance-based purchases shown as a cost, never a reward.
- It must feel like an actual game, motivating and alive, not numbers and tapping (user, 2026-11-17).

## Evidence on Hand

- PRD worked journeys UJ-1 to UJ-6 (Markus, 15 to 20) with real figures.
- Survey «Unge og penger», 133 responses: regret comes from small purchases that add up; BSU and credit are least understood.
- Hand sketches `.docs/design/mobile-sketches/k2-01-03.pdf` and `k2-04-06.pdf` (month on one screen, UJ-6).
- No real testimonials, logos or brand assets exist. Do not invent claims.

## Product Principles

1. Consequences are felt, then explained: every change can be traced with "Hvorfor?".
2. Time and money are the same kind of scarce.
3. The player acts; the game never quizzes.
4. A quiet month costs one tap; depth is always optional.
5. Never scold; a missed goal is a story, not a failure.

## Accessibility & Inclusion

WCAG 2.2 AA. Down to 320 CSS px wide, no horizontal scrolling, touch targets at least 24 px (options 44 px). Nothing by colour alone: money changes carry a sign and a word. Every picture (room states, moped, echo badges, wellbeing parts) also exists as text. Keyboard-only play including minigames. New messages announced politely to screen readers.
