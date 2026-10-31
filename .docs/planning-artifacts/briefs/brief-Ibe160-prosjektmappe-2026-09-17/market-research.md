
# Market research

## Competitive & Comparable Landscape 

> This document summarizes the competitive landscape, comparable products, relevant Norwegian and Nordic initiatives, potential partners, and the market gap LifeMode aims to address.

---

### Life-simulation games

- BitLife (Candywriter) is the category leader: text-based, choice-driven life sim covering careers, relationships, crime, health. Finance is present but shallow — earn via careers/gambling/crime, can invest in stocks/real estate, but decisions resolve instantly via swipes/taps rather than sustained budgeting.

- Reviewers criticize BitLife for "oversimplifying real-life complexity" and creating "a misleading sense of control"; one piece warns prolonged play "can desensitize young minds" to financial recklessness/gambling — the opposite of financial-literacy intent despite touching the same subject matter.
  
- Compared with LifeMode, no life-simulation game identified in the team's initial research separates a deterministic financial ledger, including calculations such as interest and amortization, from the narrative layer. None identified are explicitly designed around learning from realistic financial mistakes, and none structure the experience around Norwegian or Nordic life milestones such as confirmation money, russefeiring, studielån/Lånekassen and leiekontrakt.

---

### Teen-focused financial-literacy apps

- Zogo uses gamified micro-learning with 1,200+ modules and rewards redeemable for gift cards. It is distributed through bank and credit-union co-branding (B2B2C), making it one of the closest existing examples to LifeMode's potential bank-partnership model. However, it is quiz/courseware-based rather than a life simulation with persistent narrative consequences.

-  Greenlight, Copper and Step are real debit-card or neobank products for teenagers with parental controls and bundled financial-literacy features. They use family-subscription models, but they are banking products with a literacy layer rather than life-simulation games.

-  EVERFI provides B2B2C financial-education courseware through banks and schools and has reached 60M+ learners. It is a relevant comparison for a possible school-license and bank-sponsored model, but its approach is structured e-learning rather than gameplay.

- A common pattern across these products is that gamification consists of points, quizzes and rewards added to courseware, or financial-literacy features added to real banking products. The initial research found none that combine an LLM-driven narrative/Game Master layer with a deterministic financial simulation; later research (2026-10-31) found one hackathon prototype that does (Life Finance, see below).

---

### Norwegian and Nordic comparables

- Finans Norge runs Skolemeny.no, a directory of free bank-provided teaching materials, and the annual "NM i Pengequiz." Finans Norge's own 2025 research states that Norwegian youth struggle with financial knowledge and that schools are not fully using the potential for practical financial education.

- Nordea's "Økonomipeil" is a free, curriculum-anchored personal-finance program for grades 9–10 and upper-secondary education using videos, assignments and quizzes. It represents an existing bank-school approach to financial education.

- Gimi (Sweden, backed by/partnered with Nordea, Tink, Marqeta): nearest Nordic comparable — app+card for ages ~7-15 combining pocket-money/chore tracking with gamified lessons (XP, quizzes) on budgeting/saving/interest. 800k+ downloads, "most popular pocket-money app in the Nordics." Skews younger, is courseware-gamified rather than simulation/narrative, no LLM/GM layer.

- OsloMet runs the "UngKomp" research project on upper-secondary students' financial knowledge.

- Forbrukerrådet Ung publishes guidance for young people on areas such as moving out, renting and first purchases.

---

### Finance simulations with wellbeing or life stages (added 2026-10-31)

Found in the follow-up research (`research/competitive-youth-finance-sim-games-gap-fill-2026-10-27/` and `../../research/remaining-pre-prd-research-2026-10-31/`). These are LifeMode's nearest comparators.

- **Koll på cashen** (Finansinspektionen and Riksbanken, Sweden, 2025): a free life-stage personal-finance game for the same age group, with four life phases where savings and income carry over. No wellbeing mechanic. Played by the team on 2026-10-31: the visual style is too childish for 15-20-year-olds.
- **PersonalFinanceLab Personal Budget Game** (US/Canada): paid school licence, 12 simulated months, where choices shift net worth, credit score and a Quality of Life Score. The closest match to LifeMode's monthly loop with wellbeing, but more complex, fixed-script, US-based and aimed at college level.
- **SmooLah** (Singapore Management University, ages 17-26): tracks net worth, happiness, peace of mind and energy; the game resets if one of them reaches zero.
- **Payback** (NGPF, US): trades student debt against happiness, social life and academics.
- **Life Finance** (hackathon prototype, July 2026): the same split as LifeMode, where code owns the money and an LLM narrates, and it shows wellbeing previews for each choice. US/USD, for adults, live demo but not maintained since July 2026.
- **Taloussankari** (Finland): a live chat-style web game in 7 chapters for 8th graders that tracks only cash and experience. No AI and no wellbeing.
- **Money Wise** and **Infinite Life Simulation**: mobile life sims available in the Norwegian stores, both built on US contexts; Infinite Life Simulation uses an LLM and is rated 18+.
- **In Norway** there is still no digital personal-finance game for ages 15-20. The closest are Ungt Entreprenørskap's classroom programmes ØkonoMIN (upper secondary) and Økonomi og karrierevalg (10th grade), which include a digital budget tool, plus text and tasks on NDLA.

---

### Market gap

The research points to a gap between two existing product categories:

- life-simulation games provide narrative and branching choices, but do not appear to provide a detailed deterministic financial-learning system
- financial-literacy products provide structured financial education, but generally rely on lessons, quizzes, rewards or predefined scenarios rather than persistent generative life simulation

The specific combination LifeMode is exploring is:
> **deterministic financial simulation + persistent game state + AI-generated life narrative**

In the team's initial research, no Norwegian product has been identified that combines simulation gameplay, deterministic financial consequences and an AI-generated narrative layer.

This should be treated as an initial research finding rather than a claim that no comparable product exists globally.

**Narrowed on 2026-10-31.** The follow-up research showed that none of the parts is unique on its own: Life Finance has the engine-plus-AI split, and PersonalFinanceLab, SmooLah and Payback weigh wellbeing against money. The team's differentiation is therefore:

> **Built for Norway: a personal-finance life game for 15-20-year-olds, based on Norwegian rules and life stages, that combines good money management with wellbeing without becoming complicated.**

PersonalFinanceLab is the closest product with wellbeing, but it is more complex, US-based and aimed at older students. No product found is built on Norwegian rules such as BSU, frikort and studielån. This is a starting point; the team will refine it later.

---

## Potential partners

The research has also identified organizations that may be relevant for future partnerships, distribution or credibility.

### Nordea
Nordea already operates Økonomipeil as a financial-education initiative for schools and is therefore relevant as both a comparable and a potential future partner.

### OsloMet / UngKomp
OsloMet's research into young people's financial knowledge could be relevant as a future research or credibility connection.

### Forbrukerrådet Ung
Forbrukerrådet Ung produces practical financial guidance for young people and may be relevant as a future research or credibility partner.

Potential partnerships remain longer-term hypotheses and are not part of the initial user-research phase.

---

## Sources

### Life-simulation games
- bitlife-game.org
- playbitlifegame.com
- nahswingspan.com — "BitLife Ruined My Real Life"
- Google Play listings for Life Simulator 2026 / Life Simulator Business Game

### Teen-focused financial-literacy products
- zogo.com
- prnewswire.com (Zogo Finovate release)
- greenlight.com
- getcopper.com
- techcrunch.com (Copper $29M raise)
- bankingdive.com (Step)
- everfi.com
- cypherlearning.com (financial-literacy games list)

### Follow-up research (2026-10-31)
- `research/competitive-youth-finance-sim-games-gap-fill-2026-10-27/research.md`
- `../../research/remaining-pre-prd-research-2026-10-31/research.md` (sources 1-26)
- kollpacashen.se (teacher guide)
- personalfinancelab.com (Budget Game)
- skbi.smu.edu.sg (SmooLah FAQ)
- ngpf.org (Payback)
- github.com/tiennguyentony/life_finance
- taloussankari.com
- ue.no (ØkonoMIN, Økonomi og karrierevalg)

### Norwegian and Nordic sources
- finansnorge.no (Skolemeny, Pengequiz and 2025 "ungdom sliter med økonomikunnskap" article)
- nordea.no/okonomipeil
- tink.com (Gimi blog)
- oslomet.no (UngKomp)
- forbrukerradet.no/ung

