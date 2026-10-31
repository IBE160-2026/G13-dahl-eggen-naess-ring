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
- PersonalFinanceLab has not been tried yet. Desk research shows it already scores "Quality of Life" alongside money, so it is worth playing before deciding the wellbeing design.

## 4. Research in progress

- **Remaining desk research (done):** report in `.docs/planning-artifacts/research/remaining-pre-prd-research-2026-10-31/research.md`. Key points:
  - **Differentiation:** neither the engine + LLM split nor wellbeing is unique on its own. Life Finance (hackathon, July 2026, US, adults) has the same split and even uses Groq. PersonalFinanceLab, SmooLah and Payback weigh happiness or quality of life against money. Only the combination holds: Norwegian rules + ages 15-20 + wellbeing in the outcome + AI narration.
  - **Norway:** still no digital personal-finance game for ages 15-20. The closest are Ungt Entreprenørskap's classroom programmes and NDLA text.
  - **Koll på cashen:** money carries over between its four life phases; no wellbeing mechanic.
  - **AI (#17, closed: no AI in the MVP, provider chosen later):** Groq free plan allows about 1,000 requests and 200K tokens a day per model (gpt-oss-20b/120b); the token cap binds first at roughly 285 short events a day. Account holder must be 18+, and the customer is responsible for legal compliance when minors use the app (not a ban). Cloudflare gives 10,000 free neurons a day, roughly 700-1,100 events. Exact per-account limits can only be checked in the Groq console.
  - **Credit-card minimum:** 3% at 22% interest likely fails utlånsforskriften § 13 (repay within 5 years). Recommendation: 3.5%, min NOK 200-300 (DNB uses 3.5%, min 200). This would change rule 5 and worked example 4 in `addendum.md`.
  - **Trygdeavgift:** the 5.1% rate applies to every year before the calendar year you turn 17.
  - **Credit in practice:** SpareBank 1 requires age 20+ for consumer loans. DNB publishes no income floor.
- **User survey «Unge og penger» (done):** 133 responses, analysed in `briefs/brief-Ibe160-prosjektmappe-2026-09-17/user-research.md`. Key points:
  - Regrets are about value for money, not amount (impulse buys that add up, clothes, trends, collectibles). This supports the wellbeing differentiator.
  - Only 38% think about how a purchase affects their money months ahead, and 39% often run out. Persistent consequences hit the real weak spot.
  - Family is the main source of money, knowledge and help (88% learned most from family). Family should be an actor in the events.
  - BSU (31% don't understand it) and credit/consumer loans (20%) are the least understood terms.
  - Many want to learn about funds and investing. Decided 2026-10-31: investing stays out of version one for now.
  - The survey did not test the LifeMode concept itself. Decided 2026-10-31: no parent survey in this round.

## 5. Other open issues

- #12 (first version done 2026-10-31): differentiation is now "built for Norway: Norwegian rules and life stages for 15-20-year-olds, combining good money management with wellbeing without becoming complicated". New competitors added to `market-research.md`. To be refined further.
- #18: use the new LK20 subject codes; have a teacher review the quiz proposals.
- #11 (settled 2026-10-31): the session logs are enough for the requirement on saved prompts and AI sessions; the session-log skill was made by the course teacher.

## 6. Brainstorm topics for the meeting

- How is wellbeing measured, and how does it affect the ending, if we choose it? How do we make it different from PersonalFinanceLab's "Quality of Life" and SmooLah's happiness meter?
- Credit-card minimum payment: change from 3% to 3.5% (rule 5 and worked example 4)?
- What visual style fits 15-20-year-olds without feeling childish?
- Family as an actor: borrowing from or asking parents is a common real choice. How should the game model it, and what does it cost the player?
- Event library: which survey regrets become events (small purchases adding up, trend buys, blind boxes and in-game purchases, binding subscriptions)?
- Do we need a short concept test before the PRD, since the survey did not ask about the game itself?
