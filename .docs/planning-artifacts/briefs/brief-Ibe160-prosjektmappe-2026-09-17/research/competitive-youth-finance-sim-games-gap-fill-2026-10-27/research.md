---
title: 'Competitive research: youth finance simulation games (gap-fill)'
type: 'competitive'
topic: 'Educational money-sim games for schools (international + Nordic) and AI/LLM finance games for youth, 2025-2026'
decision: "Does LifeMode's positioning (deterministic finance engine + LLM narrative) hold, and what does it mean for PRD differentiation?"
source: 'native run (web search), 2 rounds; complements ../../market-research.md'
status: complete
preset: 'standard'
validation: 'normal'
created: '2026-10-27'
updated: '2026-10-27'
claims_verified: 5
claims_unverified: 2
---

# Competitive research: youth finance simulation games (gap-fill)

**Decision this research serves:** Does LifeMode's positioning (deterministic finance engine + LLM narrative) hold, and what does it mean for PRD differentiation?

This run fills three gaps in [market-research.md](../../market-research.md): school money-sim games (international and Nordic), AI-driven finance games from 2025–2026, and a comparison table. Products already covered there (BitLife, Zogo, Greenlight, Copper, Step, EVERFI, Gimi, Økonomipeil, Finans Norge, AI Dungeon) are not repeated.

## Executive summary

**The positioning holds, but only in its narrow form, and it should be rewritten to say so.** No live product found for young people combines a code-based finance engine with an AI-generated life story. The claim in the brief, though, is broader than the evidence supports in two ways:

1. **The architecture itself is not new.** A 2026 hackathon project, *Life Finance*, describes exactly LifeMode's split: an exact-cent deterministic engine, with AI only narrating and ranking pre-approved events — "AI can improvise the story but cannot hallucinate the player's money" [3]. Its age group and live status are unknown, and the page could only be read through search snippets (unverified). LifeMode can claim to be first *for Norwegian youth*, not first with the design.
2. **The closest real competitor is Swedish and public-sector.** *Koll på cashen* (Finansinspektionen and Riksbanken, March 2025) is a live, free-to-play game for upper-secondary students. The player follows characters from moving out to retirement, and life and society events affect each decision [1][2]. It has no AI, and it is unclear whether money carries across stages, but it is the comparator a Norwegian sensor or teacher is most likely to recognise. It is missing from market-research.md.

What holds up well: **none of the school and Nordic money games found mention AI** [1][5][8][10][11][12][13][14], **most are one-session games or quizzes**, and **no Norwegian digital personal-finance simulation for ages 15–20 was found** after searching in Norwegian, Swedish, Danish and Finnish (an absence finding, medium confidence). No product covers Norwegian life-stage concepts such as BSU, studielån or frikort.

**Biggest caveat:** several of the closest products (Life Finance, LongRuay, Stukent) were only visible through search snippets because their pages blocked or failed to load. The run cannot rule out more products of this kind.

## D1 — International school money-sim games

The established category is **free, short, US-centred browser games**. NGPF Arcade gathers 12 free games of 5–20 minutes, each on one topic (budgeting, credit, compounding, insurance, car buying, crypto, tax) [5]. *Payback* (college costs versus happiness, social life and grades) is presented by NGPF as its own game; the commonly cited FINRA Foundation link could not be confirmed [6]. *SPENT* (survive a month on $1,000, Urban Ministries of Durham, 2011) is still reachable and listed in the Arcade [5][7][20]. None mention AI.

Only two products carry consequences across a longer run:

- **PersonalFinanceLab Personal Budget Game** — a paid school licence, 12 simulated months of about 20 minutes each, where choices "change the opportunities they face" and shift net worth, credit score and a Quality of Life Score [8]. This is the closest match to LifeMode's monthly loop and its happiness barometer, but it is fixed-script with no AI.
- **Money Wise Game: Life Sim** (iOS, Dot Dot Fire UK, free, last updated October 2025) — a branching story about a US high-school senior where job choices affect later jobs and the ending; covers scams and payday loans [10].

*Stukent's* personal finance simulation (random life events, curriculum) could not be loaded and rests on search snippets only (low confidence) [9]. All D1 products are in English (Payback also Spanish) and built on US institutions; no region lock was seen.

## D1b — Norwegian and Nordic money games

The Nordic offering is dominated by **one-off classroom programmes, quizzes and in-person role-plays**:

- **Norway:** Norges Bank's *Horisont* is a free 2.5-hour in-person role-play in Oslo for upper secondary, but it is about the macro economy, not personal finance [11]. Bank initiatives (SpareBank 1's Økonomipatruljen, DNB) are guest teaching or self-tests, not games. No NDLA game surfaced.
- **Sweden:** *Koll på cashen* (above) [1][2]; *Pengalabbet*, a free browser game on a monthly salary for ages about 10–12 [12][19]; Swedbank's *Ekonomilabbet* lecture-and-exhibition programme, whose exhibition may have ended [12]. A Swedish *Ekonomispelet* app (moving out, rent, insurance) has been withdrawn from the Microsoft Store (HTTP 410).
- **Finland:** *Taloussankari / Finance Hero* (Nordea, Pörssisäätiö, TAT), a digital role-play for about ages 13–17, is the other close Nordic analogue, but the evidence is from 2022 and its mechanics are unverified [13].
- **Denmark:** Money Week, with bank guest teachers and an online Money Quiz for grades 7–9 [14].

No Nordic product found uses AI, and none simulates BSU, studielån, Norwegian tax or credit-card debt over several years.

## D2 — AI/LLM-driven finance games for youth, 2025–2026

The hypothesis "no product combines a deterministic finance engine with an LLM-generated life narrative for youth" is **weakened, not overturned**. Each half exists separately:

| Product | Has the finance-engine half | Has the AI-narrative half | Why it does not match LifeMode |
|---|---|---|---|
| Life Finance (Devpost, ~2026) [3] | Yes — exact-cent deterministic engine | Partly — AI narrates and ranks a pre-approved event pool | Age group and live status unknown; hackathon prototype; snippet evidence only |
| Infinite Life Simulation (iOS, updated Oct 2026) [4] | Unknown — money "adjusted by event results" | Yes — LLM-style branching life story with memory | Rated 18+, entertainment not finance education |
| LongRuay (PromptZone post) [18] | Yes, per snippet | AI briefings only | Adult wealth fantasy ($100M start); snippet only |
| Piggy Investors simulator [16] | Unknown | "AI-driven", unspecified | In development; no product page |
| Agentic Knowledge Tracing paper (arXiv, Jun 2026) [15] | Coded game | No — LLM used only to assess learning | Research prototype; platformer, not a life sim |
| Gameclass × Morris County teens (Feb 2026) [17] | Unknown | AI generates game/film lessons | No mechanics or access details published |

AI money-coach apps for teens (SimplyBudget, Kidonomic) track real money rather than simulate it and are only visible through aggregators; they are not comparators. No Nordic AI-driven finance game for young people was found.

## D3 — Comparison table

Accessed 2026-10-27 for every row. "Persistent" means choices carry forward over simulated time in one playthrough.

| Product | Publisher, country | Age | Format | Finance depth | Persistent | AI | Price/model | In Norway | Source |
|---|---|---|---|---|---|---|---|---|---|
| Koll på cashen | Finansinspektionen + Riksbanken, SE | Upper secondary (16–19) | Web, retro "interactive journey"; teacher guide (Gy25) | Budget, saving, investing, mortgage, pension, macro effects | Partly — life stages with events; money carry-over not stated | No | Free to play (public authority; price not stated) | Swedish only | [1][2] |
| Pengalabbet | Ekonomiska museet + Finansinspektionen, SE | ~10–12 | Browser | Salary, job choice, budget, housing, buffer | Unknown | No | Free, no ads | Swedish only | [12][19] |
| Taloussankari / Finance Hero | Nordea, Pörssisäätiö, TAT, FI | ~13–17 | Web role-play + museum touchscreen | Decisions in life situations (unverified) | Unknown | No | Likely free (unverified) | Possibly English version | [13] |
| Horisont | Norges Bank, NO | Upper secondary + adults | In-person role-play, 2.5 h, Oslo | Macro economy, not personal finance | No | No | Free | Yes (NO/EN), Oslo only | [11] |
| Money Week / Money Quiz | Finans Danmark, DK | 13–16 | Guest lessons + online quiz | Personal finance quiz | No | No | Free | Danish only | [14] |
| NGPF Arcade (12 games incl. Payback, SPENT) | Next Gen Personal Finance, US | High school | Browser, 5–20 min per game | Budget, credit, compounding, insurance, car, tax, crypto | Mostly no; Payback and SPENT within one session | No | Free | English; US context | [5][6] |
| SPENT | McKinney for Urban Ministries of Durham, US | General / high school | Browser | Living paycheck to paycheck, rent, bills | Within a 30-day run | No | Free (donation ask) | English; US context | [7][20] |
| Personal Budget Game | PersonalFinanceLab, US/CA | College / new graduate role | Browser, teacher-run, 12 months × ~20 min | Budget, rent, car loan, insurance, credit score, income tax | Yes — net worth, credit score, Quality of Life Score | No | Paid school licence (price not public) | Not stated; English | [8] |
| Money Wise Game: Life Sim | Dot Dot Fire, UK | Rated 4+; US high-school senior story | iOS, offline | Scams, payday loans, credit, jobs | Yes — branching story and ending | No | Free, no ads | English; NO store not checked | [10] |
| Stukent Personal Finance Sim | Stukent, US | High school / college | Browser sim + curriculum | Life events, budgeting (unverified) | Likely (unverified) | Unverified | Paid courseware (unverified) | Unverified | [9] |
| Life Finance | Unnamed hackathon team (Devpost) | Unknown | 3D web/desktop, monthly turns | Cash, debt, tax, investments, net worth | Yes | Yes — narration and event ranking; money computed by code | Prototype | Unknown | [3] |
| Infinite Life Simulation | Indie developer (iOS) | 18+ | iOS text life sim | Money, jobs, stocks | Yes | Yes — LLM branching story | Free + IAP + ads | Store availability not checked | [4] |
| **LifeMode (planned, for contrast)** | IBE160 G13, NO | 15–20 | Mobile-first web | Norwegian rule set: interest, BSU, consumer loan, credit card, wage, frikort, rent | Yes — monthly loop to age 20 | Stage 2: LLM events and negotiation within engine-set bounds | Free (course project) | Norwegian | brief.md, addendum.md (not research evidence) |

## Cross-dimension insights

- **The gap is the combination, not any single feature.** Persistent consequences exist (PersonalFinanceLab, Money Wise, Koll på cashen), Nordic life stages exist (Koll på cashen), and the engine-plus-AI architecture exists (Life Finance). No product found has all three, and none localises to Norway [1][3][8][10].
- **Public bodies and banks own the Nordic school channel, and they publish free, AI-free games.** Koll på cashen and Pengalabbet come from a regulator and a central bank, and Taloussankari from a bank and a foundation. The B2B2C channel in the brief is proven, but its products are free, so LifeMode's differentiator in that channel would be the AI-driven variety and negotiation, not the simulation itself [1][12][13].

## Contrary evidence

The red-team pass did not run (`red_team = off`). The strongest counter-evidence found during the run is in the executive summary: Life Finance shows the architecture is already known [3], and Koll på cashen shows a Nordic public authority already ships a life-stage personal-finance game for the same age group [1].

## Recommendations

1. **Narrow the differentiation claim in the PRD** (input to PRD "Differentiation"; brief "Competitive landscape"): replace "no competitor pairs a deterministic finance engine with an LLM narrative" with "no live product for young people combines a deterministic finance engine with an AI-generated story, and none is built on Norwegian life stages (BSU, studielån, frikort)". Confidence: medium — rests on an absence finding plus the unverified Life Finance page [3].
2. **Add Koll på cashen and PersonalFinanceLab to the competitor section of market-research.md** as the nearest comparators. Confidence: high for Koll på cashen [1][2] and PersonalFinanceLab [8].
3. **Treat the Norwegian rule set as a differentiator in its own right** (PRD functional requirements, architecture constraint): no product found simulates BSU, studielån or frikort. Confidence: medium (absence finding).
4. **Play Koll på cashen and PersonalFinanceLab's trial before writing the PRD's UX journeys**: both are the best available reference for a life-stage loop and a quality-of-life score. Confidence: high that they are reachable [2][8].

## Open questions

- **Does Koll på cashen carry money across life stages?** Neither page says. Answer: play it (about an hour).
- **Who made Life Finance, and is it live?** Devpost returned 403 twice. Answer: open the page in a browser or search GitHub for the repository.
- **Taloussankari's current mechanics and status**: evidence is from 2022. Answer: open taloussankari.com in a browser.
- **Norway, still unsearched**: NDLA site search, Ungt Entreprenørskap's catalogue (ue.no), Finansportalen, Eika, Sbanken. Answer: a short Deepen run or a manual check.
- **Availability of Money Wise and Infinite Life Simulation in the Norwegian App Store**: not checked.

## Source appendix

| # | Claim / finding it supports | Publisher | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|
| [1] | Koll på cashen: FI + Riksbanken, upper secondary, three characters, budget/saving/home/pension, events affect decisions | [Sveriges Riksbank](https://www.riksbank.se/sv/press-och-publicerat/nyheter-och-pressmeddelanden/nyheter/2025/spel-fran-finansinspektionen-och-riksbanken-ska-oka-ungas-forstaelse-for-privatekonomi/) | 2025-03-18 | 2026-10-27 | high |
| [2] | Koll på cashen live, Swedish, moving out to retirement, teacher support Gy25, no AI mentioned | [Finansinspektionen (kollpacashen.se)](https://www.kollpacashen.se/) | undated | 2026-10-27 | high |
| [3] | Life Finance: deterministic exact-cent engine, AI narrates and ranks pre-approved events | [Devpost](https://devpost.com/software/somename-u9gsz6) | undated (~2026) | 2026-10-27 (403; search snippet only) | medium, unverified |
| [4] | Infinite Life Simulation: LLM-style branching life story, money and stocks, 18+, free + IAP, updated Oct 2026 | [Apple App Store](https://apps.apple.com/py/app/infinite-life-simulation/id6503607456?l=en-GB) | 2026-10 | 2026-10-27 | high |
| [5] | NGPF Arcade: 12 free short single-topic games, no AI | [Next Gen Personal Finance](https://www.ngpf.org/arcade/) | undated (© 2014–2026) | 2026-10-27 | high |
| [6] | Payback: college loans vs happiness, social life, grades; presented as NGPF's game | [Next Gen Personal Finance](https://www.ngpf.org/blog/teacher-tips/teacher-tip-interactive-payback/) | 2025-04-03 | 2026-10-27 | high |
| [7] | SPENT: one month on $1,000, McKinney for UMD, launched 2011 | [Wikipedia](https://en.wikipedia.org/wiki/Spent_(video_game)) | undated | 2026-10-27 (search snippet) | medium |
| [8] | Personal Budget Game: 12 months, net worth, credit score, Quality of Life Score, paid licence, no AI | [PersonalFinanceLab](https://www.personalfinancelab.com/?p=27730) | undated (Spring 2022 update) | 2026-10-27 | high |
| [9] | Stukent personal finance sim: role-play with random life events | [Stukent](https://www.stukent.com/mimic-personal-finance/) | undated | 2026-10-27 (404; search snippet) | low |
| [10] | Money Wise: free iOS branching story, US senior, scams/payday loans, updated Oct 2025, no AI | [Apple App Store](https://apps.apple.com/us/app/-/id1491095072) | 2025-10 | 2026-10-27 | high |
| [11] | Horisont: free in-person macro role-play, upper secondary, Oslo | [Norges Bank](https://www.norges-bank.no/kort-forklart/undervisning/horisont/) | 2023-06-09 | 2026-10-27 | high |
| [12] | Pengalabbet and Ekonomilabbet: browser salary game ~10–12; lecture + exhibition programme | [Swedbank](https://www.swedbank.se/om-oss/samhallsengagemang/sponsring/ekonomiska-museet) | undated | 2026-10-27 | medium |
| [13] | Taloussankari: Nordea/Pörssisäätiö/TAT digital role-play ~13–17 | [Taloustaito](https://www.taloustaito.fi/vapaalla/kaipaatko-tekemista-kokeile-taloutta-opettavia-peleja-kesapaivan-ratoksi/) | 2022-08-03 | 2026-10-27 | medium |
| [14] | Danish Money Week: guest teachers + Money Quiz, grades 7–9 | [Global Money Week](https://globalmoneyweek.org/countries/155-denmark) | 2024 | 2026-10-27 (search snippet) | low |
| [15] | Agentic Knowledge Tracing: LLM used for assessment only in a K-12 finance platformer | [arXiv](https://arxiv.org/abs/2606.25358) | 2026-06-24 | 2026-10-27 | high |
| [16] | Piggy Investors: AI-driven K-12 simulator in development | [The 74](https://www.the74million.org/article/stop-trying-to-teach-21st-century-financial-literacy-with-20th-century-tools/) | 2026-04-22 | 2026-10-27 | medium |
| [17] | Gameclass × Morris County teens: AI-generated finance games/films announced | [Patch](https://patch.com/new-jersey/randolph/morris-co-teens-use-ai-generated-video-games-teach-financial-literacy) | 2026-02-18 | 2026-10-27 | low (substance) |
| [18] | LongRuay: AI briefings + deterministic engine, adult wealth sim | [PromptZone](https://www.promptzone.com/sienna_fb1754b25bd8dd7aaa/longruay-the-ai-millionaire-simulator-that-turns-wealth-into-meaningful-decisions-20p3) | undated | 2026-10-27 (404; search snippet) | low |
| [19] | Pengalabbet site live, Swedish, free, no ads | [Ekonomiska museet / FI (pengalabbet.se)](https://www.pengalabbet.se/) | undated | 2026-10-27 | medium |
| [20] | playspent.org still resolves | [Urban Ministries of Durham (playspent.org)](https://playspent.org/) | undated | 2026-10-27 | medium |

## Staleness map

Computed with `recon_kit.py staleness` from the pack's freshness bars (features and pricing 3 months, traction 6 months), keyed to each source's **publication** date. Pages accessed live on 2026-10-27 (Koll på cashen, Money Wise, PersonalFinanceLab) are flagged stale only because their published dates are old; their existence was confirmed today.

| Claim | Class | Published | Re-check by | Stale |
|---|---|---|---|---|
| PersonalFinanceLab paid licence, price not public [8] | pricing | 2022-04 | 2022-07-01 | yes |
| Taloussankari digital role-play, 13–17 [13] | feature | 2022-08-03 | 2022-11-03 | yes |
| Danish Money Week, 46,000+ pupils in 2024 [14] | traction | 2024-03 | 2024-09-01 | yes |
| Koll på cashen: life-stage game, no AI [1][2] | feature | 2025-03-18 | 2025-06-18 | yes |
| Money Wise free, updated Oct 2025 [10] | feature | 2025-10 | 2026-01-01 | yes |
| Life Finance: deterministic engine + AI narration [3] | feature | ~2026-06 | 2026-09-01 | yes |
| Infinite Life Simulation: LLM life story, 18+ [4] | feature | 2026-10 | 2027-01-01 | no |
| No Norwegian personal-finance life-sim for 15–20 (absence) | feature | 2026-10-27 | 2027-01-27 | no |
| No school or Nordic money game uses AI | feature | 2026-10-27 | 2027-01-27 | no |

Earliest re-check: 2022-07-01 (PersonalFinanceLab pricing, already overdue). The two claims the positioning rests on, the Norwegian gap and AI-free school games, are due by **2027-01-27**; if the PRD cites them, re-check them before the December 2026 delivery.
