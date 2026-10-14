---
title: LifeMode Addendum
related_brief: brief.md
updated: 2026-10-14
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
| Consumer loan interest | 15% per year (fixed) | [ASSUMPTION] No official 2026 average found; market offers range about 9-22% nominal (Smarte Penger, DNB, bytt.no). 15% sits mid-range. |
| Credit card interest (when interest is paid) | 22.6% per year | SSB table 12844, households, 2026 Q2 |
| Hourly wage, under 16 / under 18 / 18+ | NOK 136.41 / 139.40 / 195.04 | Virke/HK Landsoverenskomsten minimum rates from 1 April 2026 (18+ = wage step 1) |
| Tax-free card (frikort) limit | NOK 100,000 per calendar year; 50% withheld above it | Regjeringen, tax rates 2026 |
| Rent, 1-room flat (hybel) | NOK 8,770 per month (whole country) | SSB table 09895, 2025 (Bergen 7,510, Oslo 10,090) |
| Youth public transport, 30 days | NOK 238 | Ruter, from August 2026 (state-subsidised until April 2027) |
| Mobile subscription | NOK 299 per month | [ASSUMPTION] typical youth plan, not sourced |
| Example unexpected expense | NOK 2,500 (broken phone screen) | [ASSUMPTION] not sourced |
| Policy rate (background only) | 4.5% | Norges Bank API, 13 Oct 2026 |

### Rules

1. **One round is one month.** Each month is processed in a fixed order: income → tax → fixed costs → loan instalments and interest on debt → interest on savings → the month's event and the player's choice.
2. **Whole kroner.** All amounts are whole NOK. Monthly interest is `balance × annual rate / 12`, rounded to the nearest krone (0.5 rounds up).
3. **Tax.** Income within a calendar year is tax-free up to NOK 100,000 (frikort). Income above the limit is taxed at 50%.
4. **Consumer loan.** An annuity loan: equal monthly payments `P × r / (1 − (1 + r)^−n)` with `r` = annual rate / 12, rounded to whole kroner. The final payment is adjusted so the balance ends at exactly zero.
5. **Credit card.** If the full balance is paid by the end of the month, no interest is charged. Otherwise interest is charged on the whole balance, and the minimum payment is the larger of 3% of the balance and NOK 300 (or the whole balance if it is smaller).
6. **Credit only from 18.** Consumer loans and credit cards are available only from the player's 18th birthday, as in Norway, where minors cannot take on loans. Before 18 the player cannot borrow.
7. **Quiet months.** A month without an event is still processed by rules 1-5, but the player only sees a short summary. A playthrough from 15 to 20 (72 months) is tuned to about 20-30 real choices.
8. **Crisis months.** The engine, not the AI, starts a crisis month when any of these is true at the end of a month: the current account is below NOK 0; the credit card minimum payment has been missed two months in a row; or total debt is above 3 × the average monthly income over the last three months. A crisis month has 2-3 linked choices with real-world actions (sell something, take extra shifts, ask for a payment plan, ignore it), and the engine calculates the effect of each. In version one a crisis never ends the game: ignored debt keeps growing under rules 4-5 and triggers new crisis months.

Rent (NOK 8,770) stays in the parameter table for the later moving-out step; it is not used in version one.

### Worked examples (test answer key)

| # | Situation | Expected result |
|---|---|---|
| 1 | Summer job at 16: 120 hours × NOK 139.40 | NOK 16,728; no tax (under frikort limit) |
| 2 | NOK 10,000 in a savings account for 12 months at 2.87% | NOK 10,289 (NOK 289 interest) |
| 3 | Consumer loan of NOK 20,000 at 15% over 12 months | Monthly payment NOK 1,805, final payment NOK 1,808; total paid NOK 21,663 (NOK 1,663 interest) |
| 4 | The trip from the brief: NOK 3,200 on a credit card, paying only the minimum each month | Paid off after 13 months; total paid NOK 3,606 (NOK 406 interest) |
| 5 | An 18-year-old earns NOK 110,000 in one calendar year | NOK 5,000 tax (50% of NOK 10,000 above the limit) |

Examples 2-4 were calculated with a script applying rules 2, 4 and 5 month by month and should be re-checked by hand by the team before they become test cases.

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
