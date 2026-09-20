---
title: LifeMode Addendum
related_brief: brief.md
updated: 2026-09-20
---

# Addendum: LifeMode

Supporting depth that informs the brief but belongs in later work (architecture, PRD) rather than the 1-2 page brief itself.

## LLM-as-game-master products and pitfalls

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

## AI Negotiation Mechanic — Guardrail Detail

Emerged from discovery: the negotiation mechanic (arguing with the bank for a better interest rate) is the sharpest point where the "helpfulness bias" risk meets the core financial-simulation loop. Team decision: the deterministic financial engine sets a base value and a bounded interval (e.g., a defined rate range); the AI selects a value *within* that interval based on argument quality — never outside it. This keeps "the financial engine determines the consequences" true even for AI-mediated outcomes, and the team explicitly does not want the AI to default to lenient/agreeable outcomes — realism over friendliness is the design goal.
