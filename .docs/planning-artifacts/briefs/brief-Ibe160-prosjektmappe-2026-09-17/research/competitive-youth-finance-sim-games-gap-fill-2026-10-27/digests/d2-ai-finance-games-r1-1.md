# D2 digest — AI/LLM finance games for youth 2025-2026 (round 1)

Method note: 17 tool calls, 10 sources attempted (7 read; Devpost x2 returned 403 and PromptZone returned 404, so those projects are evidenced only by search-engine snippets of the pages and are marked as such). Snippet-only claims are capped at medium/low confidence.

## Claims

- Life Finance is a 3D personal-finance strategy game played month by month (persona, plans, life events), with choices affecting cash, debt, taxes, investments and net worth | https://devpost.com/software/somename-u9gsz6 | Devpost (hackathon submission; team unnamed in snippet) | undated (mentions "Codex with GPT-5.6" as build partner, so likely 2026) | accessed 2026-10-27 (page 403; search snippet only) | medium | feature
- Life Finance deliberately separates AI from money math: a deterministic engine does all financial calculations with exact-cent arithmetic; a local ML ranker only ranks pre-approved events (648 queries / 3,240 candidates) and cannot bypass engine checks; optional language features do interpretation and narration, with button fallbacks; stated rule "AI can improvise the story but cannot hallucinate the player's money" | https://devpost.com/software/somename-u9gsz6 | Devpost | undated | accessed 2026-10-27 (snippet only) | medium | AI-use
- Life Finance target age and live availability not stated in retrieved text | https://devpost.com/software/somename-u9gsz6 | Devpost | undated | accessed 2026-10-27 | low | availability
- LongRuay is an "AI millionaire simulator": player starts with US$100M, one decision per simulated day; AI-personalized briefings, outcomes set by a deterministic rule-based engine | https://www.promptzone.com/sienna_fb1754b25bd8dd7aaa/longruay-the-ai-millionaire-simulator-that-turns-wealth-into-meaningful-decisions-20p3 | PromptZone (user post) | undated | accessed 2026-10-27 (page 404; snippet only) | low | AI-use
- Infinite Life Simulation (iOS) is a text-based "AI life sim" where the story "unfolds based on what you decide"; AI "remembers what you did three life stages ago"; NPCs react to treatment | https://apps.apple.com/py/app/infinite-life-simulation/id6503607456?l=en-GB | App Store / developer bugrahan senturk | v6.2.5 released ~5 days before access (prior: 6.2.4 on 19 Oct, 6.0.0 on 10 Jun) | accessed 2026-10-27 | high | AI-use
- Infinite Life Simulation tracks money: v6.2.0 "Your money is now adjusted by event results!"; v6.0.8 added Stock Market; v6.0.4 jobs and companies. Whether adjustments are computed by code or by the LLM is not stated | same URL | App Store | 2026 | accessed 2026-10-27 | high (feature) / unknown (math) | feature
- Infinite Life Simulation is rated 18+ (mature/suggestive themes), free with IAP (USD 0.49-4.99, "Lifetime Premium" USD 4.99), contains ads; too few ratings to display | same URL | App Store | 2026 | accessed 2026-10-27 | high | pricing
- Agentic Knowledge Tracing (arXiv 2606.25358, Santos, Julia, Nascimento, submitted 24 Jun 2026): 2D platformer serious game aligned with OECD/INFE; LLM agents used for assessment only (event classifier + 4 domain agents + judge feeding Bayesian Knowledge Tracing), no content generation; 193 K-12 participants, 264 sessions; mastery estimates correlate with learning gain r=0.276 and post-test r=0.333; single-LLM baseline r=0.095 (n.s.) | https://arxiv.org/abs/2606.25358 | arXiv | 2026-06-24 | accessed 2026-10-27 | high | AI-use
- Three Morris County (NJ) high schoolers partner with Gameclass to make "AI-generated video games and films" teaching money ("using AI to turn financial decisions into stories and challenges"); example given is hypothetical; no launch date, mechanics or access details | https://patch.com/new-jersey/randolph/morris-co-teens-use-ai-generated-video-games-teach-financial-literacy | Patch | 2026-02-18 | accessed 2026-10-27 | high (that project exists) / low (product substance) | AI-use
- Gameclass is a game-based education platform used by "nearly 10,000 educational organizations" (as reported) | same Patch URL; https://gameclass.ai/ (not fetched) | Patch | 2026-02-18 | accessed 2026-10-27 | low | traction
- Isaac Lamptey (founder, Piggy Investors) describes an AI-driven K-12 financial simulator in development: paycheck, fixed bills, savings goal, credit card balance, events (medical bill, cut hours, interest after missed payment), "compress 30 years of compounding into 30 minutes"; patent pending on AI architecture integrating real-time financial compliance into school simulations; no product name/URL; math implementation not stated | https://www.the74million.org/article/stop-trying-to-teach-21st-century-financial-literacy-with-20th-century-tools/ | The 74 (opinion) | 2026-04-22 | accessed 2026-10-27 | medium | feature
- A follow-up search for "Piggy Investors" found no product page | (search only) | — | — | accessed 2026-10-27 | medium | availability
- "Allowance Adventure!" web budgeting game (student/adult levels, random events, savings evaluation) was built with Gemini 2.5 Pro as a coding aid; no evidence of runtime LLM | https://iwant2study.moe.edu.sg/sg.iwant2study.org/ospsg/index.php/interactive-resources/sciences/food-nutrition/1077-wantsandneeds | iwant2study (Singapore MOE-linked OER) | undated | accessed 2026-10-27 (snippet only) | low | AI-use
- SimplyBudget described as an AI finance manager for teenagers with parental monitoring; free tier capped at 30 transactions/month | https://indexator.ai/startups/simplybudget-ai-finance-tool | indexator.ai (aggregator) | undated | accessed 2026-10-27 (snippet only) | low | feature
- Kidonomic: AI money coach for ages 8-16; reportedly removed from US App Store | https://appgoblin.info/apps/6476450084 | AppGoblin (aggregator) | undated | accessed 2026-10-27 (snippet only) | low | availability
- "The Road to Financial Freedom" is an AI-powered board game (budgeting, debt, investing, crypto) for families/youth programs; AI tool "Harriet" helps on open-ended questions | https://www.dmagazine.com/philanthropy-nonprofits/2026/06/ai-board-game-bostic-poindexter/ | D Magazine | 2026-06-18 | accessed 2026-10-27 (snippet only) | low | AI-use

## Per-product summary

| name | publisher | launched/updated | age | format | AI role | money math deterministic? | persistent consequences | price/model | Norway availability | URL |
|---|---|---|---|---|---|---|---|---|---|---|
| Life Finance | unnamed hackathon team (Devpost) | undated, likely 2026 | unknown | 3D web/desktop game, monthly turns | narration + NL interpretation; ML ranks pre-approved events | yes (explicit design principle, exact-cent engine) | yes (cash/debt/net worth carry month to month) | prototype, presumably free | unknown (prototype) | https://devpost.com/software/somename-u9gsz6 |
| Infinite Life Simulation | bugrahan senturk (indie) | updated Oct 2026 (v6.2.5) | 18+ | iOS text life sim | LLM-style generated branching life story with memory, NPC reactions | unknown (money "adjusted by event results") | yes (life stages, money, stocks, jobs) | free + IAP + ads | App Store listing observed on PY storefront; NO not checked | https://apps.apple.com/py/app/infinite-life-simulation/id6503607456?l=en-GB |
| LongRuay | unknown (PromptZone post) | undated | unknown (adult wealth theme) | web sim, one decision/day | personalized AI briefings | yes (per snippet) | yes (daily decisions) | unknown | unknown | promptzone URL above (404) |
| Agentic BKT platformer | Federal Univ. of Uberlândia (Santos et al.) | arXiv Jun 2026 | K-12 | 2D platformer research prototype | assessment only (multi-agent LLM) | presumably coded game (not detailed) | unknown | research | not available | https://arxiv.org/abs/2606.25358 |
| Gameclass x Morris Co. teens | students + Gameclass | announced Feb 2026 | HS (adaptable) | AI-generated game/film lessons | generate games/stories | unknown | unknown | unknown | unknown | https://patch.com/new-jersey/randolph/morris-co-teens-use-ai-generated-video-games-teach-financial-literacy |
| Piggy Investors simulator | Piggy Investors (Isaac Lamptey) | in development (Apr 2026 op-ed) | middle/high school | classroom simulator | "AI-driven" (unspecified) | unknown | yes (described: compounding, missed payments) | unknown | no | https://www.the74million.org/article/stop-trying-to-teach-21st-century-financial-literacy-with-20th-century-tools/ |
| SimplyBudget / Kidonomic | various | undated | teens / 8-16 | AI coach apps | chat coaching/tracking | n/a (real money tracking) | no simulation | freemium | unknown | aggregator URLs above |

## Verdict on the hypothesis

**Weakened, not overturned.**

- **Life Finance** is the closest match to the architecture: it explicitly has a deterministic money engine plus AI narration/interpretation, with consequences carried over monthly turns. What it lacks, as far as we can tell: a confirmed youth target, an LLM-*generated* branching narrative (events are ranked from a pre-approved pool, so the branching is curated, not generated), and evidence that it is live beyond a hackathon page. It shows the "LLM narrates, code computes" pattern is already known and published, so the *architecture* cannot be claimed as novel.
- **Infinite Life Simulation** has the other half: a live, recently updated LLM-generated branching life narrative with memory and money/stock state. It lacks a youth audience (rated 18+), any financial-literacy purpose, and evidence that the money math is deterministic.
- **LongRuay** (snippet only) claims AI briefings + deterministic engine, but for an adult wealth fantasy.
- Nothing found is live, youth-targeted (13-22), finance-education-focused **and** has both halves. A narrower version of the hypothesis still holds as of this run: "No *live, youth-targeted* product combines a deterministic financial engine with an LLM-generated branching life narrative." Positioning should not rely on the architecture itself being new.

## Leads worth chasing

- Life Finance: find the repo/demo link, hackathon name, team and target audience (try Devpost via another fetcher, or search for the GitHub repo).
- Infinite Life Simulation: check the Norwegian App Store, Google Play, and whether money changes come from LLM output or code (reviews, dev site).
- Piggy Investors: company site / patent application (AI + real-time financial compliance in school simulations).
- Gameclass (https://gameclass.ai/): whether any finance lessons are live and AI-generated at runtime.
- "The ClockWork Dark" (Hugging Face forum): a deterministic-engine + LLM-narrator RPG pattern (not finance), useful as an architectural reference.
- Deep Life Simulator (iOS, id6749675615) and ReLife (iOS): rule-based finance life sims; check for AI features.
- Full text of arXiv 2606.25358 for how the game models money.
- Cleo / Frankly: AI money chatbots aimed at Gen Z (18+), adjacent to the coach angle.

## Looked for but could not find

- A neobank teen product with an AI money coach (searched generally; no youth-bank AI coach surfaced this run; Revolut <18, Lunar etc. were not checked).
- Any Norwegian or Nordic AI-driven finance game for young people (Norwegian query returned nothing relevant).
- A peer-reviewed study of an LLM-*generated* narrative finance game for teens (only an assessment-side LLM paper and a ChatGPT budget-negotiation role-play case, arXiv 2402.09161).
- Primary page content for Life Finance, LongRuay, Life$im (devpost.com/software/life-im, "AI advisor" finance sim): fetches blocked (403/404).
