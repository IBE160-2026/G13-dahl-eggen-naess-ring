---
title: LifeMode Addendum
related_brief: brief.md
updated: 2026-10-31
---

# Addendum: LifeMode

Supporting depth that informs the brief but belongs in later work (architecture, PRD) rather than the 1-2 page brief itself.

## Financial Engine — Rule Set v1

Added 2026-10-14 in response to teacher feedback: the engine must "always calculate correctly", so the rules it follows are written down here, together with worked examples that serve as the answer key for automated tests. The numbers are realistic Norwegian 2026 values from official sources where they exist. They are stored as configuration, not hard-coded, so they can be updated without changing the rules.

### Parameters

| Parameter | Value | Source |
|---|---|---|
| Savings account interest | 2.87% per year | SSB table 11018, households, non-fixed deposits, Aug 2026 |
| BSU interest | 5.61% per year | SSB table 11018, households, Aug 2026 |
| BSU deduction | 10% of the year's deposits, max deposit NOK 27,500 per year (max deduction NOK 2,750), max NOK 300,000 in total; the deduction can never exceed the year's tax and is not carried forward | Skatteetaten, satser BSU 2026 and BSU guidance (see research `domain-norwegian-youth-finance-rules-2026-10-27`) |
| Consumer loan interest | 15% per year (fixed) | [ASSUMPTION] No official 2026 average found; market offers range about 9-22% nominal (Smarte Penger, DNB, bytt.no). 15% sits mid-range. |
| Credit card interest (when interest is paid) | 22.6% per year | SSB table 12844, households, 2026 Q2 |
| Hourly wage, under 16 / under 18 / 18+ | NOK 136.41 / 139.40 / 195.04 | Virke/HK Landsoverenskomsten minimum rates from 1 April 2026 (18+ = wage step 1) |
| Working-hour limits | Under 15 or in compulsory schooling (grunnskole): max 2 h per school day and 12 h per school week; 7 h per day and 35 h per week on days and weeks without school. Ages 15-18 after compulsory schooling: max 8 h per day and 40 h per week. 18+: ordinary working hours, 9 h per day and 40 h per week | Arbeidsmiljøloven §§ 10-4 and 11-2 (see research `domain-norwegian-youth-finance-rules-2026-10-27`) |
| Tax-free card (frikort) limit | NOK 100,000 per calendar year; employers withhold 50% above it, but that is withholding, not final tax | Skatteetaten, frikort and forskuddsutskrivingen 2026 |
| Tax 2026 | Trygdeavgift lower limit NOK 99,650; rate 7.6% (5.1% under 17), never more than 25% of income above the lower limit. Minstefradrag 46%, max NOK 95,700. Personfradrag NOK 114,540. Tax on ordinary income 22%. Trinnskatt step 1: 1.7% from NOK 226,100 | Skatteetaten, satser 2026 (see research `domain-norwegian-youth-finance-rules-2026-10-27`) |
| Rent, 1-room flat (hybel) | NOK 8,770 per month (whole country) | SSB table 09895, 2025 (Bergen 7,510, Oslo 10,090) |
| Youth public transport, 30 days | NOK 238 | Ruter, from August 2026 (state-subsidised until April 2027) |
| Mobile subscription | NOK 299 per month | [ASSUMPTION] typical youth plan, not sourced |
| Example unexpected expense | NOK 2,500 (broken phone screen) | [ASSUMPTION] not sourced |
| Policy rate (background only) | 4.5% | Norges Bank API, 13 Oct 2026 |

### Rules

1. **One round is one month.** Each month is processed in a fixed order: income → tax → fixed costs → loan instalments and interest on debt → interest on savings → the month's event and the player's choice.
2. **Whole kroner.** All amounts are whole NOK. Monthly interest is `balance × annual rate / 12`, rounded to the nearest krone (0.5 rounds up).
3. **Tax.** Tax is calculated on the player's total wage income for the calendar year, using 2026 rates. Up to NOK 99,650 there is no tax. Above that, trygdeavgift applies: 7.6% of the whole income (5.1% under 17), but never more than 25% of the income above NOK 99,650. Income tax is 22% of ordinary income (income minus minstefradrag) above the personfradrag, plus trinnskatt step 1; higher trinnskatt steps are not modelled. Each month the tax step deducts the increase in the year's calculated tax. The 50% that employers withhold above the frikort limit is withholding, settled in the tax assessment, and is not modelled as tax in version one.
4. **Consumer loan.** An annuity loan: equal monthly payments `P × r / (1 − (1 + r)^−n)` with `r` = annual rate / 12, rounded to whole kroner. The final payment is adjusted so the balance ends at exactly zero.
5. **Credit card.** If the full balance is paid by the end of the month, no interest is charged. Otherwise interest is charged on the whole balance, and the minimum payment is the larger of 3% of the balance and NOK 300 (or the whole balance if it is smaller).
6. **Credit only from 18.** Consumer loans and credit cards are available only from the player's 18th birthday, as in Norway, where minors cannot take on loans. Before 18 the player cannot borrow.
7. **Quiet months.** A month without an event is still processed by rules 1-5, but the player only sees a short summary. A playthrough from 15 to 20 (72 months) is tuned to about 20-30 real choices.
8. **Crisis months.** The engine, not the AI, starts a crisis month when any of these is true at the end of a month: the current account is below NOK 0; the credit card minimum payment has been missed two months in a row; or total debt is above 3 × the average monthly income over the last three months. A crisis month has 2-3 linked choices with real-world actions (sell something, take extra shifts, ask for a payment plan, ignore it), and the engine calculates the effect of each. In version one a crisis never ends the game: ignored debt keeps growing under rules 4-5 and triggers new crisis months.
9. **BSU deduction.** The deduction is calculated once a year, in December's tax step: the lower of 10% of the year's BSU deposits (deposits capped at NOK 27,500) and the year's calculated tax under rule 3. If the player pays no tax, the deduction is NOK 0, and unused deduction is lost. The game says so plainly ("BSU deduction: NOK 0, you have no tax to reduce") and shows that BSU still pays off through its higher interest (5.61% against 2.87% on an ordinary savings account).
10. **Working hours follow Norwegian law.** The engine never lets the player work more hours than arbeidsmiljøloven allows. The limit depends on whether the player is in compulsory schooling, not on age alone: a 15-year-old in 10th grade gets 12 h per school week, while a 16- or 17-year-old in upper secondary school gets 40 h per week. Summer jobs use the limits for weeks without school. Rules on night work (§ 11-3) are not modelled, because the game does not track time of day.

Rent (NOK 8,770) stays in the parameter table for the later moving-out step; it is not used in version one.

### Worked examples (test answer key)

| # | Situation | Expected result |
|---|---|---|
| 1 | Summer job at 16: 120 hours × NOK 139.40 | NOK 16,728; no tax (under frikort limit) |
| 2 | NOK 10,000 in a savings account for 12 months at 2.87% | NOK 10,289 (NOK 289 interest) |
| 3 | Consumer loan of NOK 20,000 at 15% over 12 months | Monthly payment NOK 1,805, final payment NOK 1,808; total paid NOK 21,663 (NOK 1,663 interest) |
| 4 | The trip from the brief: NOK 3,200 on a credit card, paying only the minimum each month | Paid off after 13 months; total paid NOK 3,606 (NOK 406 interest) |
| 5 | An 18-year-old earns NOK 110,000 in one calendar year | NOK 2,588 tax, all of it trygdeavgift: the lower of 7.6% × 110,000 (NOK 8,360) and 25% × 10,350 (NOK 2,587.50, rounded up). Income tax is 0, because ordinary income (110,000 − 50,600 minstefradrag = 59,400) is below the personfradrag |
| 6 | A 17-year-old on frikort (no tax) keeps NOK 10,000 in a BSU for 12 months | BSU deduction NOK 0 (no tax to reduce). Balance NOK 10,576 (NOK 576 interest), against NOK 10,289 in an ordinary savings account (example 2) |

Examples 2-4 and 6 were calculated with a script applying rules 2, 4 and 5 month by month, and examples 1 and 5 are direct arithmetic. All five were independently recomputed on 2026-10-22 and match. Example 5 was corrected on 2026-10-29 after domain research showed that the earlier 50% figure (NOK 5,000) was withholding, not final tax. Rules 9-10, the working-hour parameter and example 6 were added on 2026-10-31 (issue #16). Note that example 2 depends on rule 2 (rounding each month); a plain compound formula gives NOK 10,291.

### Simplifications the game discloses

The rule set is deliberately simpler than real life. To keep the game honest, the player is told where it simplifies. Each text is shown the first time the mechanism appears (as an info icon or under "Hvorfor?"), and all of them are collected on one "Om tallene" page. The texts are player-facing and therefore in Norwegian.

| # | Applies to | Text shown to the player |
|---|---|---|
| D1 | Tax (rule 3) | «Forenklet: Skatten regnes ut fra hele årsinntekten din med satsene for 2026. I virkeligheten kan arbeidsgiveren trekke 50 % av lønna til du har skattekort, eller når frikortet er brukt opp. Det som er trukket for mye, får du tilbake i skatteoppgjøret.» |
| D2 | Wages | «Timelønna i spillet er minstesatsen i tariffavtalen for varehandelen (Virke/HK) fra 1. april 2026. Norge har ingen lovbestemt minstelønn, så den ekte lønna di kan bli både høyere og lavere.» |
| D3 | BSU interest | «BSU-renta i spillet er gjennomsnittet for norske banker i august 2026 (SSB). Noen banker gir mer, og renta endrer seg over tid.» |
| D4 | Credit approval (rules 4-6) | «Forenklet: I spillet kan du få lån og kredittkort fra du fyller 18. I virkeligheten sjekker banken inntekt, gjeld og betalingsanmerkninger, og mange krever fast inntekt eller at du er eldre.» |
| D5 | Consumer loan interest | «Lånerenta på 15 % er et anslag midt i markedet. Ekte forbrukslån koster ofte mellom 9 og 22 %, avhengig av bank og hvem du er.» |
| D6 | All rates | «Alle satser og beløp er 2026-tall. De holdes faste gjennom hele spillet, selv om spillet varer fra du er 15 til du er 20.» |

Added on 2026-10-31 (issue #16), based on the required disclosures in research `domain-norwegian-youth-finance-rules-2026-10-27`.

## LLM-as-game-master products and pitfalls

- AI Dungeon (Latitude) is the reference case: state-of-the-art AI-GM systems split a deterministic backend (rules, causal/graph-based state) from the LLM (narration/dialogue only), because LLMs used directly as randomness sources produce numbers that look random but statistically aren't, and free-running LLMs will silently rewrite established rules/state. This validates LifeMode's planned separation of the deterministic financial engine from the AI narrative layer.
- Documented LLM-GM failure modes (per "Can LLM Agents Stick to the Script?" and RPGBENCH): hallucination/factual contradiction, "forcibly changing reality," ignoring player input, and a "helpfulness bias" — RLHF-tuned models tend to grant requests that should be impossible, eroding narrative friction/consequence.
- Content-safety precedent: AI Dungeon's 2021 controversy — a GPT-3 upgrade caused generation of sexual content involving minors; Latitude's fix (aggressive filtering + human moderators reading private stories) caused backlash over over-blocking and privacy (moderators reading unpublished/private content). Directly relevant since LifeMode's entire user base is minors (15-20) — both under- and over-moderation are live risks, and "humans reading kids' private sessions to tune the model" is a specific trust/privacy trap to avoid by design.
- Cost economics: rough industry figures put a single LLM dialogue exchange at $0.001-0.005; at meaningful DAU this compounds fast — an argument for keeping "expensive" LLM calls to narrative beats only, while the deterministic engine (cheap, code-based) does continuous math.
- Sources: shiftmag.dev; vice.com "Text Adventure Game Community In Chaos"; aiaaic.org (AI Dungeon incident record); futurism.com; arxiv.org RPGBENCH (2502.00595); arxiv.org "Can LLM Agents Stick to the Script?" (2608.08160); theneuralbase.com.

## AI Safety & Content Moderation — Design Principles

Raised during brief discovery because the entire user base is minors (15-20) and the closest structural comparable (AI Dungeon) has a well-documented 2021 safety incident. Not solved here — flagged for the architecture phase — but the team's working stance:

1. **Structured AI output, not free text.** The AI Game Master generates events/dilemmas in a structured format (type + parameters) validated against a schema before rendering — not unconstrained prose. Reduces surface area for unwanted content reaching the player.
2. **Constrained player input for negotiation, at least in MVP.** For the bank-negotiation mechanic, the player selects from predefined argument *types* (e.g. "cite steady income," "offer collateral," "show a repayment plan") rather than fully open free-text chat with the AI. Preserves the "argument quality affects outcome" mechanic while avoiding open-ended text exchange between a minor and an LLM. Can be opened up later once moderation is proven.
3. **Automatic moderation before display, not after.** Generated content is checked against a content filter before reaching the player; a failed check falls back to a neutral, pre-written event — never a blank screen, never unfiltered output.
4. **No human reading of private sessions.** Review happens on flagged/aggregate content, not by staff reading individual children's play sessions — the specific trust/privacy trap that compounded the AI Dungeon incident.
5. **Parent visibility as a sellable feature, not just compliance.** Family Premium (already in the business model) can include parent-facing visibility into event *categories* their teen encountered, not verbatim content.

**Technical/architecture-level follow-ups (deeper than brief scope):**
- Rate limiting and cost control per session (ties to the LLM unit-economics risk above).
- GDPR / Datatilsynet review of minors' data handling — aligns with the already-stated goal of collecting no real PII (simulated_age, simulated_savings, etc.).
- Review of Anthropic's usage policies for products directed at minors before scaling beyond MVP.

## Win Condition & Endgame — Design Discussion (not decided)

Raised during brief discovery for the "Out (not now)" scope item on the endgame system. Not settled — the team is still discussing whether to keep this shape or simplify it. Recorded here so the idea isn't lost, not as a commitment.

One option discussed: at the start of a playthrough, the player receives a mission to reach a target net worth by around age 20. The target is randomized/personalized per playthrough rather than fixed, so no two players chase the same number, reinforcing that no two playthroughs should converge on the same story.

Net worth alone isn't the whole picture in this option. A parallel happiness/wellbeing meter ("lykkebarometer") tracks what a pure net-worth number hides: stress, free time, social life, housing quality. Like the financial numbers, it would be computed deterministically from measurable state (debt load, hours worked, living conditions, free time) — the AI creates the situations that move these numbers, but does not judge the outcome itself, keeping the "the AI creates the life, the financial engine determines the consequences" principle intact.

This would produce three possible endings, not a binary win/lose:
- **Real win** — net worth target reached and wellbeing stayed above a healthy threshold.
- **Hollow win** — net worth target reached, but wellbeing collapsed getting there: the money cost too much.
- **Loss** — net worth target missed, or an unmanageable debt spiral occurs before the deadline.

**Second option discussed:** instead of the system assigning a target, the player picks a life goal at the start of the playthrough, from a small set such as long-term savings, short-term savings, a specific target amount, or job/education. The chosen goal sets the win condition for that playthrough — its target and its deadline — so "what does winning mean" is answered by the player rather than fixed by the system. This also means the AI-generated events and dilemmas can lean toward situations relevant to the chosen goal (e.g. more education/career-shaped dilemmas for a job/education goal).

The wellbeing meter still runs in parallel, but what it weighs shifts with the chosen goal: a job/education goal would weigh stress and free time more heavily, a savings goal would weigh housing quality and social life more heavily, and so on. As in the first option, it is computed deterministically from measurable state, not judged by the AI.

This would produce the same three-outcome shape as the first option, but measured against the player's chosen goal instead of a system-set net-worth target:
- **Real win** — chosen goal reached and wellbeing stayed above a healthy threshold.
- **Hollow win** — chosen goal reached, but wellbeing collapsed getting there.
- **Loss** — chosen goal missed, or an unmanageable debt spiral occurs before the deadline.

Open question for the group: a system-assigned target, a player-chosen goal, or a combination of the two — and whether the three-ending, dual-meter shape survives either way.

## AI Negotiation Mechanic — Guardrail Detail

Emerged from discovery: the negotiation mechanic (arguing with the bank for a better interest rate) is the sharpest point where the "helpfulness bias" risk meets the core financial-simulation loop. Team decision: the deterministic financial engine sets a base value and a bounded interval (e.g., a defined rate range); the AI selects a value *within* that interval based on argument quality — never outside it. This keeps "the financial engine determines the consequences" true even for AI-mediated outcomes, and the team explicitly does not want the AI to default to lenient/agreeable outcomes — realism over friendliness is the design goal.
