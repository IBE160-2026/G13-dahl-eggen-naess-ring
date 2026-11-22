# Product

<!-- impeccable:product-schema 1 -->

Source: written from the PRD (`.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md`, final, updated 2026-11-22) and the architecture (`.docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/`) on 2026-11-16, and checked against both on 2026-11-22 (#97). The PRD wins on any conflict.

## Platform

web

## Stack

Frontend: TypeScript (a course requirement) with Next.js, hosted on Vercel (the frontend team's choice, 2026-11-22). The backend is Python behind Caddy on Railway. The browser sees one origin: Vercel passes `/api/*` on to the backend (architecture AD-12). Fonts must be self-hosted: the game loads nothing from third parties (NFR-3).

## Users

Young people aged 15-20 in Norway, especially those about to make their first real money decisions: a first pengegave, a first job, a first credit card. Some play by their own choice and some because a parent or teacher told them to. They want to feel grown-up and make their own choices, and it must not feel like homework. They play in short bursts of 10-15 minutes, often on a phone on the bus, and sometimes on a shared school PC. The PRD protagonist is Markus, a sceptical 15-year-old whose mother told him to try it.

Not users in version one: parents, teachers, people under 15 or over 20, and players outside Norway.

## Product Purpose

LifeMode lets young people in Norway make expensive money mistakes before those mistakes cost real money. The player lives five years of a life, from 15 to their 20th birthday, one in-game year per session. Every choice carries forward, and the game always shows why. Success means the player understands why their money and wellbeing changed, thinks further ahead, and would rather play this than scroll.

## Positioning

A life sim where time is as limited as money. Each month the player plans their free time, manages their job and money, and reads what friends, family, the employer and the bank send them. A deterministic engine using real Norwegian 2026 rules and figures (frikort, BSU, credit only from 18, the moped licence at 16) decides every amount and explains its causes ("Hvorfor?", echo badges). Wellbeing (stress, free time, social life) counts in the ending, so getting rich at any cost gives a hollow win. The player learns from the consequences of their own actions, never from quizzes.

## Operating Context

- **The monthly loop:** the month opens, then a highlight event (4 active months a year) or a quiet-month summary. The player explores the phone, month plan, job and money. They plan activities in 1-4 slots and continue. A quiet month can be done in one tap.
- **A session is one in-game year,** and ends with a teaser for the next year. Returning shows a recap.
- **Endings:** ekte seier, hul seier, mål ikke nådd, tap, plus the top three choices that mattered. The player can play again from 15.
- **Playtest:** 18-20-year-old testers, planned from about 8 Dec 2026, with no email sent during the playtest.

## Capabilities and Constraints

- Login with email and password, no username, and no real age collected. The email address is typed once and shown back for checking (FR-1, WCAG 3.3.7). Saved on the server, so play picks up on any device.
- The server decides every result. The frontend never calculates or formats an amount; the backend sends finished Norwegian game text with figures filled in.
- All game text is in Norwegian bokmål. Messages are pre-written from fictional senders, and the player can't write messages.
- Never in version one: real money or bank connections, personal financial advice, AI anywhere, free text beyond the email address and the nickname, real-time lockouts, classroom tools, alcohol or tobacco content.
- Not a PWA, no offline mode, no push notifications.
- **Nickname:** the player picks a nickname at sign-up, and game text addresses them by it. It is the only free text beyond the email address and counts as personal data (PRD FR-1, FR-54, NFR-3; added in PR #100, 2026-11-16).
- **Open:** how the avatar looks (OQ-9).

## Brand Commitments

- Name: LifeMode.
- Voice: Norwegian bokmål written the way a Norwegian 16-year-old finds natural. Not childish, not corporate, not a banking app, not a quiz. Options read as actions.
- No real brands or logos.

## Evidence on Hand

- Survey "Unge og penger": 133 responses. It is a convenience sample, not representative, with only 8 respondents aged 19-20, and it didn't test the concept.
- Real 2026 figures with sources in Rule Set v1 (`.docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md`).
- Design thinking (`.docs/design/design-thinking-2026-10-16.md`), K2 paper sketches (`.docs/design/mobile-sketches/`), and round 1 UX concepts (`.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/.working/concepts/`).
- No testimonials, users or playtest results exist yet. Don't invent them.

## Product Principles

1. **Always show why.** Every change in money or wellbeing can be traced to its cause.
2. **A game first, not schoolwork.** It must beat scrolling. Learning comes from consequences, not questions.
3. **Time is as scarce as money.** Free time, work and social life compete with money in every month.
4. **Real Norwegian rules, real figures.** Figures come from the engine and sources, never from the screen.
5. **Short sessions.** One year in 10-15 minutes; a quiet month in one tap.

## Accessibility & Inclusion

WCAG 2.2 AA (NFR-2):
- Touch targets of at least 24×24 CSS px, and option buttons 44×44 where possible.
- Nothing shown by colour alone: a money change carries a sign and a word.
- Every picture also exists as text: room states, the moped, echo badges, wellbeing parts.
- The full flow, minigames included, can be played with a keyboard alone. Minigames have no time limits, motion or gestures.
- The month plan works by tap or select, never by dragging.
- Status messages and new messages are announced to screen readers.
- Mobile-first, down to 320 CSS px wide, adapting to tablet, laptop and desktop with no horizontal scroll (NFR-1).
