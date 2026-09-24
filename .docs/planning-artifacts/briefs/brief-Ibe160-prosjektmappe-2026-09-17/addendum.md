---
title: LifeMode Addendum
related_brief: brief.md
updated: 2026-09-17
---

# Addendum: LifeMode

Supporting depth that informs the brief but belongs in later work (architecture, PRD) rather than the 1-2 page brief itself.

## Competitive & Comparable Landscape (research detail)

**Life-simulation games**
- BitLife (Candywriter) is the category leader: text-based, choice-driven life sim covering careers, relationships, crime, health. Finance is present but shallow — earn via careers/gambling/crime, can invest in stocks/real estate, but decisions resolve instantly via swipes/taps rather than sustained budgeting.
- Reviewers criticize BitLife for "oversimplifying real-life complexity" and creating "a misleading sense of control"; one piece warns prolonged play "can desensitize young minds" to financial recklessness/gambling — the opposite of financial-literacy intent despite touching the same subject matter.
- Gap vs. LifeMode: no life-sim separates a deterministic financial ledger (correct interest/amortization) from narrative; none is explicitly a learning tool for real-world financial mistakes; none stages content by Nordic-relevant life milestones (confirmation money, russefeiring, studielån/Lånekassen, leiekontrakt).
- Sources: bitlife-game.org; playbitlifegame.com; nahswingspan.com "BitLife Ruined My Real Life"; Google Play listings for Life Simulator 2026 / Life Simulator Business Game.

**Teen-focused financial-literacy apps**
- Zogo: gamified micro-learning (1,200+ modules), rewards redeemable for gift cards, distributed via bank/credit-union co-branding (B2B2C) — closest existing model to LifeMode's bank-partnership monetization, but quiz/courseware, not simulation/narrative.
- Greenlight / Copper / Step: real debit-card/neobank products for teens with parent controls and bundled literacy features. Monetized via tiered family subscriptions — validates the family-subscription price point, but these are banking apps with a literacy layer, not a life-sim.
- EVERFI: B2B2C courseware licensed through banks who sponsor it into schools, reaching 60M+ learners — direct analog for LifeMode's "school license + bank sponsor" go-to-market, but compliance-style e-learning, not gameplay.
- Common pattern: gamification = points/quizzes/rewards on courseware, or a real financial product with a literacy add-on bolted on. None combine an LLM-driven narrative/GM layer with a deterministic finance simulation.
- Sources: zogo.com; prnewswire.com (Zogo Finovate release); greenlight.com; getcopper.com; techcrunch.com (Copper $29M raise); bankingdive.com (Step); everfi.com; cypherlearning.com financial literacy games list.

**Norwegian/Nordic comparables and potential partners**
- Finans Norge runs Skolemeny.no (directory of free bank-provided teaching materials) and the annual "NM i Pengequiz". Finans Norge's own 2025 research states Norwegian youth "struggle with financial knowledge" and schools "aren't using the potential" — the incumbent industry body publicly flags the exact gap LifeMode targets.
- Nordea "Økonomipeil": free, curriculum-anchored personal-finance program for grades 9-10/videregående (videos, assignments, quizzes) — an existing bank-school program, a natural partner or competitor for licensing.
- Gimi (Sweden, backed by/partnered with Nordea, Tink, Marqeta): nearest Nordic comparable — app+card for ages ~7-15 combining pocket-money/chore tracking with gamified lessons (XP, quizzes) on budgeting/saving/interest. 800k+ downloads, "most popular pocket-money app in the Nordics." Skews younger, is courseware-gamified rather than simulation/narrative, no LLM/GM layer.
- OsloMet runs "UngKomp" academic research into videregående students' financial knowledge; Forbrukerrådet Ung publishes guidance for youth moving out/renting/first purchases — potential research/credibility partners, not products.
- No Norwegian product found that combines simulation gameplay + deterministic finance + AI narrative — LifeMode would be first-mover domestically for the "simulated consequence-based" approach.
- Sources: finansnorge.no (Skolemeny, Pengequiz, 2025 ungdom-sliter article); nordea.no/okonomipeil; tink.com (Gimi blog); oslomet.no (UngKomp); forbrukerradet.no/ung.

**LLM-as-game-master products and pitfalls**
- AI Dungeon (Latitude) is the reference case: state-of-the-art AI-GM systems split a deterministic backend (rules, causal/graph-based state) from the LLM (narration/dialogue only), because LLMs used directly as randomness sources produce numbers that look random but statistically aren't, and free-running LLMs will silently rewrite established rules/state. This validates LifeMode's planned separation of the deterministic financial engine from the AI narrative layer.
- Documented LLM-GM failure modes (per "Can LLM Agents Stick to the Script?" and RPGBENCH): hallucination/factual contradiction, "forcibly changing reality," ignoring player input, and a "helpfulness bias" — RLHF-tuned models tend to grant requests that should be impossible, eroding narrative friction/consequence.
- Content-safety precedent: AI Dungeon's 2021 controversy — a GPT-3 upgrade caused generation of sexual content involving minors; Latitude's fix (aggressive filtering + human moderators reading private stories) caused backlash over over-blocking and privacy (moderators reading unpublished/private content). Directly relevant since LifeMode's entire user base is minors (14-20) — both under- and over-moderation are live risks, and "humans reading kids' private sessions to tune the model" is a specific trust/privacy trap to avoid by design.
- Cost economics: rough industry figures put a single LLM dialogue exchange at $0.001-0.005; at meaningful DAU this compounds fast — an argument for keeping "expensive" LLM calls to narrative beats only, while the deterministic engine (cheap, code-based) does continuous math.
- Sources: shiftmag.dev; vice.com "Text Adventure Game Community In Chaos"; aiaaic.org (AI Dungeon incident record); futurism.com; arxiv.org RPGBENCH (2502.00595); arxiv.org "Can LLM Agents Stick to the Script?" (2608.08160); theneuralbase.com.

## AI Safety & Content Moderation — Design Principles

Raised during brief discovery because the entire user base is minors (14-20) and the closest structural comparable (AI Dungeon) has a well-documented 2021 safety incident. Not solved here — flagged for the architecture phase — but the team's working stance:

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
