---
title: Meeting prep, Thursday 2026-11-05
status: draft
created: 2026-10-31
---

# Meeting prep: Thursday 2026-11-05

Goal from the lecturer: be "fit for fight" with enough research to start the PRD. This note collects what the team must decide, what we already know, and what is still open.

## 1. Decisions the team must make (blocks the PRD)

From issue #19, brainstorm on 2026-10-29 (`.docs/brainstorming/brainstorm-lifemode-pre-prd-open-questions-2026-10-29/`).

| # | Topic | Brainstorm proposal | New input since then |
|---|---|---|---|
| 1 | Endgame at 20 | "Your life at 20": summary, top 3 choices, replay from a crossroads. No win condition or wellbeing meter in version one. | Playtest of Koll på cashen points the other way: tie wellbeing directly into the outcome to stand out (see section 3). Likely to change. |
| 2 | Choice → consequence | Every engine effect carries a cause link. It drives echo badges, a "Why?" button, counterfactual lines and the ending. New test criteria F9/F10. | None. |
| 3 | Event library | Fixed event schema. At least 30 events, target 60-80 plus about 10 crisis sets, roughly 55/45 before/after 18. | None. |
| 4 | Privacy | "Storage, not identity": anonymous login or resume code, no free text, no real age, playtests only with 18-20-year-olds. | Age limit verified (#21), see section 2. |

## 2. Verified since last time

- **Age limit for digital consent (#21):** 13 years today (personopplysningsloven § 5). The government has proposed raising it to 15; not adopted as of June 2026, bill expected in the Storting by end of 2026. The limit only matters if consent is our legal basis. With "storage, not identity" we may not need consent at all. Pitfall: 10th graders turn 15 during the year, so some are 14 for part of the school year.
- **Finance rules (#16, closed):** tax rule, BSU deduction (NOK 0 without tax, but BSU still pays through higher interest), working hours under Norwegian law, and six player-facing disclosure texts are now in `addendum.md` (rules 9-10, example 6, D1-D6).

## 3. Competitor playtest (#13)

Notes: `.docs/planning-artifacts/research/playtest-competitors-2026-10-31/notes.md`.

- Koll på cashen looks too childish. LifeMode needs a more grown-up visual style.
- Proposed differentiator: good finance is not just having the most money, but how you use it. Wellbeing (free time, social life, stress, housing) is tied directly into the outcome. Kept open for the team, but the current lean is yes.
- PersonalFinanceLab has not been tried yet.

## 4. Research in progress

- **Remaining desk research:** competitors (#14), AI provider quotas and terms (#17), and the open questions from the domain research. Report: `.docs/planning-artifacts/research/remaining-pre-prd-research-2026-10-31/research.md` (being written).
- **User survey «Unge og penger» (done):** 133 responses, analysed in `briefs/brief-Ibe160-prosjektmappe-2026-09-17/user-research.md`. Key points:
  - Regrets are about value for money, not amount (impulse buys that add up, clothes, trends, collectibles). This supports the wellbeing differentiator.
  - Only 38% think about how a purchase affects their money months ahead, and 39% often run out. Persistent consequences hit the real weak spot.
  - Family is the main source of money, knowledge and help (88% learned most from family). Family should be an actor in the events.
  - BSU (31% don't understand it) and credit/consumer loans (20%) are the least understood terms.
  - Many want to learn about funds and investing. Decided 2026-10-31: investing stays out of version one for now.
  - The survey did not test the LifeMode concept itself. Decided 2026-10-31: no parent survey in this round.

## 5. Other open issues

- #12: narrow the differentiation claim and add new competitors to `market-research.md` (depends on decision 1 and section 3).
- #17: switch AI provider in the architecture (Gemini out, Groq primary, Cloudflare fallback).
- #18: use the new LK20 subject codes; have a teacher review the quiz proposals.
- #11: are the session logs enough to meet the requirement for saved prompts and AI sessions?

## 6. Brainstorm topics for the meeting

- How is wellbeing measured, and how does it affect the ending, if we choose it?
- What visual style fits 15-20-year-olds without feeling childish?
- Family as an actor: borrowing from or asking parents is a common real choice. How should the game model it, and what does it cost the player?
- Event library: which survey regrets become events (small purchases adding up, trend buys, blind boxes and in-game purchases, binding subscriptions)?
- Do we need a short concept test before the PRD, since the survey did not ask about the game itself?
