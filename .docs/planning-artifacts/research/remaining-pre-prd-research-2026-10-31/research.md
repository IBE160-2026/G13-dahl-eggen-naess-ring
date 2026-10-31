---
topic: 'Remaining pre-PRD desk research: competitors (#13, #14), AI provider limits and terms (#17), open domain questions'
created: 2026-10-31
status: complete
---

# Remaining pre-PRD research

Desk research done on 2026-10-31 to close the open questions from three earlier reports: the competitive gap-fill (2026-10-27), the domain research on Norwegian youth finance rules (2026-10-27), and the free-tier LLM provider research (2026-10-27). It also covers the playtest notes (2026-10-31). Numbers in brackets refer to the source table at the end.

## Verdict

- **Life Finance has been found.** It is a public GitHub repo, built July 2026 by three developers. It has a live Vercel demo and has not been updated since 21 July 2026. It uses the same split as LifeMode: a deterministic engine plus an LLM that only interprets, ranks and narrates. It even runs Groq. It is US-based, English, aimed at adults and goal-driven (financial independence). LifeMode's architecture is therefore **not novel**. What sets LifeMode apart is the combination of audience, Norwegian rules and wellbeing [1][3][4].
- **Wellbeing in the outcome is not unique.** At least three education games already score something like happiness alongside money. PersonalFinanceLab / Stock-Trak say outright that "avoiding every expense is not a winning strategy". SmooLah, aimed at ages 17–26, resets the game if happiness or peace of mind hits zero. Payback trades debt against happiness [23][24][25][26]. The closest Nordic competitors (Koll på cashen, Taloussankari) have **no** wellbeing meter [7][21]. A defensible claim is narrower: *Nordic/Norwegian + ages 15–20 + wellbeing in the outcome + AI narration*.
- **Groq's free-plan limits can now be read from the public page.** For `openai/gpt-oss-20b` and `-120b` they are 30 requests/min, 1,000 requests/day, 8K tokens/min and 200K tokens/day. The daily **token** cap binds first, at about 285 short events a day per model. Llama 3.1 8B and 3.3 70B are now listed as "Enterprise / Contact Sales" [27][28].
- **Domain:** cards with total limits ≤ NOK 30,000 are outside the whole utlånsforskrift, § 13 included. "Under 17" means every year before the calendar year in which you turn 17. The legally binding hospitality youth rates are still the June 2025 figures. DNB publishes no income floor. SpareBank 1 requires age 20+ for consumer loans [35][36][39][41][45][49].

## A. Competitors

### A1. Life Finance — who made it, is it live? (confidence: high on identity and status; medium that it is the same project as the Devpost entry)

- The Devpost page still returns HTTP 403 [5]. A GitHub search found `tiennguyentony/life_finance`. Its README matches the Devpost snippet almost word for word: "an LLM plays the antagonist, but a deterministic engine holds every dollar"; the AI "interprets free text, ranks pre-approved events, and writes character dialogue"; the model "can never invent a number" [1].
- **Who:** contributors `tiennguyentony`, `tony-ng-vn` and `hungtruongOwolf`. The README calls it a hackathon build ("intentional for the hackathon") [1].
- **Live/maintained:** the repo was created 2026-07-14, with the last push on 2026-07-21. It has 0 stars, no licence and is not archived. The demo at life-finance-mu.vercel.app answered HTTP 200 on 2026-10-31 [1][2]. In short, it is a live demo but not maintained (no commits for about 3 months).
- **Product:** a 3D board game (Next.js + Three.js) with monthly turns and personas with real salaries. The goal is financial independence, in USD with US tax via PolicyEngine. The AI provider is Groq, OpenAI or Ollama, and a self-trained ML model ranks events [1]. Under-18 ages are silently replaced by the persona's age, so the game assumes adult players [4]. Its event engine already computes **"cash-flow and wellbeing previews"** for each choice [3].
- **Roadmap:** "Nemesis Mode", where an AI villain picks the event that targets your weakest defence [1]. Nothing in the repo suggests it is being built.

### A2. Taloussankari — current mechanics and status (confidence: high on mechanics, medium on status)

- **Status:** taloussankari.com is a live web app. Its script cache-buster decodes to 2026-10-01, and its content database carries a 2025-10-27 timestamp [6][7]. The national 8th-grade Taloussankari competition was still running in 2026: the final was on 18 March 2026, run by Nordea, Pörssisäätiö, NYT ry and Finanssiala, with about 1,800 participants [8]. tat.fi, the previous publisher page, refused the connection [9].
- **Mechanics** (read straight from the game's public data file [7]): a chat-style branching story. Messages come from characters, the player's inner "brain" voice and narration. There are 514 cards across 7 chapters: intro, grandma's work camp, "more than work", first job, Kalle's loan, holiday trip, and compound interest/stocks. The tracked state is **cash** and **experience**. Choices are gated by cash thresholds (for example min 850), so cash appears to carry over between chapters. There is **no happiness or wellbeing stat** in the data. Each chapter has a "maxEarnableCash". It is available in Finnish, Swedish and English (Finance Hero / Cashhjälte). It has no AI and is not in the Finnish or Norwegian App Store under that name.
- **Audience:** about 8th grade (age 14) according to the competition [8], younger than LifeMode's 15–20.

### A3. Norwegian sources and tools (confidence: medium, since much of this is an absence finding)

| Source | What exists | Age | Format | Game-like? |
|---|---|---|---|---|
| NDLA | Topic "Forbruk og personlig økonomi" under Tverrfaglige temaer, with the cases "Pengesmart – personlig økonomi" and "Kredittfella" (articles, tasks, a learning path) [10]. Maths 1P/2P have "Kredittkort og lån". | vgs (inferred from the intro text) | Text, tasks, learning paths | **No.** An NDLA API search for "økonomispill" gave 0 hits, and no simulation was found [10] |
| Ungt Entreprenørskap | **ØkonoMIN** (vgs): 2 lessons, digital budget calculator; the student picks a job and salary, makes spending, saving, loan and lifestyle choices, and gets feedback on years until a home deposit [12]. **Økonomi og karrierevalg** (10th grade): an app with student login, career choices → personal finances [13] | 15–16 and vgs | Facilitator-led classroom session (often bank staff) plus a digital tool | **Partly.** Closest Norwegian analogue to LifeMode's premise (job → budget → saving for a home), but a one-session calculator, not a game loop. No wellbeing element is described [12] |
| Finans Norge | Project task "Kalle" with UE (lower secondary), the "På egne ben" guide, the NM i Pengequiz competition, Skolemeny.no [14] | 13–16 / young adults | PDF task, quiz, guide | Quiz only |
| Nordea Økonomipeil | Free 2-hour lesson for 9th–10th grade and vgs; a search snippet mentions "an interactive game for the class"; 8,500 pupils in 2024 [15] | 14–19 | Lesson + quiz + class game | Possibly. The game's content was not verified |
| Finansportalen | Price comparison only; no youth learning tool found | — | — | No |
| Eika, Sbanken | Nothing found. Sbanken's /ung page has no youth learning content (and now sits in DNB's domain); Eika's /ung returns 404 | — | — | No |
| "Sjef i eget liv" (FNO/Husbanken/NAV) | An old budget simulator for testing whether a consumer loan blocks a home purchase [16]. Current status unknown, probably retired | young adults | Web calculator | Calculator |

**Conclusion:** still no Norwegian digital personal-finance *game* for ages 15–20. The nearest things are UE's ØkonoMIN and Økonomi og karrierevalg: classroom sessions led by bank volunteers, with a digital budget tool. They are also a plausible channel partner.

### A4. Money Wise and Infinite Life Simulation in Norwegian stores (confidence: high)

| App | App Store (NO) | Google Play (requested from a Norwegian IP, gl=NO) |
|---|---|---|
| Money Wise Game: Life Sim (Dot Dot Fire UK) | **Available.** Free, 4+, English, v1.0.1 from Oct 2025 [17] | **Available.** Listing loads, developer "Dot Dot Fire", 500K+ downloads, updated 19 Mar 2026, PEGI 3 [18] |
| Infinite Life Simulation | **Available.** Developer bugrahan senturk, 18+, free + IAP, English, updated about 30 Oct 2026 [19] | **Available.** Developer "Pickle.co", 10K+ downloads, updated 29 Oct 2026; the listing shows PEGI 3, which contradicts the iOS 18+ rating (low confidence on the rating) [20] |

### A5. Koll på cashen — carry-over and wellbeing (confidence: high)

Source: the official teacher guide (lärarhandledning, 7 pages) [21], plus the lärarstöd page [22].

- **Structure:** four "TIDSLOOPar" (time loops): 18–25 (budget), 26–35 (saving), 36–54 (buying a home), 55–107 (pension). There are choices, chance cards ("chanskort") and random historical market scenarios (1 of 6).
- **Money does carry over, but in a simplified way.** In loop 1 the monthly surplus "carries forward" to later stages, and some expenses follow the character and grow over time. Loop 2 starts "from the conditions the character brings into the time loop", mainly income and savings. Long-term savings grow by the chosen stock/bond split. **Simplification:** the home deposit is always fixed at 15% of the price, no matter how much the player has saved in total. A partner from the story pays 50% of the deposit and loan. The final pension depends on job, income across the game, market performance and chosen retirement age.
- **Wellbeing/happiness:** **none.** The guide has no happiness, wellbeing or quality-of-life mechanic. The only test is whether the budget balances (a deficit forces the player to redo the choices).
- This confirms the playtest's differentiation note: Koll på cashen measures only money.

### A6. Which youth finance games tie wellbeing into the outcome? (confidence: high that the idea is not unique)

| Game | Audience | How wellbeing counts | Source |
|---|---|---|---|
| PersonalFinanceLab Budget Game | K-12 and college | Three objectives: credit score, **Quality of Life** (raised by "spending your money on things that maximize your well-being") and emergency fund. "Game Score will depend on how well you balance all three" | [24] |
| Stock-Trak budgeting simulation (same engine, college) | College | QoL points for a nicer apartment and time with friends; "**Avoiding every expense is not a winning strategy**"; ranking by overall score, net worth, credit score and QoL | [25] |
| SmooLah (SMU Singapore, Citi Foundation) | Ages 17–26 (content 15–30) | Four meters: net worth, **happiness**, **peace of mind**, energy. The game resets if any meter hits zero, and the leaderboard combines net worth, happiness and peace of mind. Mobile; no AI mentioned | [23] |
| Payback (NGPF) | High school | Balances student debt against **happiness**, social life and academics. Scoring formula not published | [26] |
| Life Finance | Adults | Its engine computes "wellbeing previews" for each choice; the win condition is financial independence | [3] |
| Koll på cashen, Taloussankari | Nordic school audiences | **No** wellbeing stat | [7][21] |

**Honest assessment:** "good finance is how you use money, not just how much you have" is an established design pattern (PersonalFinanceLab, Stock-Trak and SmooLah say it almost word for word). It is **not** a unique differentiator on its own. It *is* missing from the two Nordic public-sector comparators. So the claim holds only in the combined form: Norwegian rules, ages 15–20, wellbeing in the outcome and AI narration. SmooLah is the best design reference: concrete meters, failure on zero, and a mixed leaderboard.

## B. AI provider (issue #17)

### Groq (confidence: high on the published table; medium that it applies unchanged to a given account)

- **Free-plan limits:** read from the page's embedded `freeRows` data, which the earlier fetch missed because the visible tab showed Developer limits [27].

  | Model | RPM | RPD | TPM | TPD |
  |---|---|---|---|---|
  | openai/gpt-oss-120b | 30 | 1K | 8K | 200K |
  | openai/gpt-oss-20b | 30 | 1K | 8K | 200K |
  | qwen/qwen3.8-27b (preview) | 30 | 1K | 8K | 200K |
  | openai/gpt-oss-safeguard-20b | 3 | 1K | 2K | 200K |
  | llama-prompt-guard-2-22m / -86m | 30 | 14.4K | 15K | 500K |

  Developer (paid) plan for comparison: gpt-oss 1K RPM, 500K RPD, 250K TPM [27].
- **Model availability:** the models page lists `llama-3.1-8b-instant` and `llama-3.3-70b-versatile` as "Enterprise / Contact Sales", and they are not in the free table. Production models are gpt-oss-120b/20b (plus Whisper); Qwen3.8-27B is a *preview* model, "may be discontinued at short notice" [28].
- **Capacity (own arithmetic):** an event of about 500 tokens in and 200 out is about 700 tokens, so 200K TPD gives **about 285 events/day per model**, and 8K TPM about 11 events/min. gpt-oss reasoning tokens also count, so real capacity is lower. Limits are per model and per organisation, so routing between gpt-oss-20b and -120b roughly doubles the daily budget [27].
- **Only in the console:** the page says limits are per organisation, that "there may be exceptions", and that "you can view the current, exact rate limits for your organization on the limits page in your account settings" [27]. The console is also the only way to check whether free accounts need a card, how much reasoning tokens consume in practice, and whether the DPA is accepted for the account (still disputed, see the earlier report).
- **Age/minors (verbatim, Services Agreement last modified 22 June 2026):** §2: "You must be 18 years of age or older to access or use the Cloud Services." §6.3: for a Customer Application "directed towards or is likely to be accessed by individuals under the age of majority… Customer will be solely responsible for ensuring that the Customer Application complies with all applicable laws and regulations related to (x) the use… by individuals under the age of majority… and (y) any collection of Personal Data from individuals under the age of majority" [29]. That is a responsibility clause, not a ban. The Acceptable Use & Responsible AI Policy (effective 15 Oct 2025) has no age rule; it bans child sexual abuse/exploitation and similar content [30].

### Cloudflare Workers AI (confidence: high on the allowance; medium on the AUP)

- **Free allowance:** 10,000 neurons per day on both Workers Free and Paid. It resets at 00:00 UTC, and on the free plan requests **fail with an error** once over the limit. Pricing page updated 2026-10-20 [31].
- **Own arithmetic for a 500/200-token event:** `llama-3.1-8b-instruct-fp8-fast` (4,119 / 34,868 neurons per M tokens) ≈ 9 neurons → **~1,100 events/day**; `gpt-oss-20b` (18,182 / 27,273) ≈ 14.5 → **~690/day**; `llama-3.3-70b-fp8-fast` (26,668 / 204,805) ≈ 54 → **~185/day**; base `llama-3.1-8b-instruct` ≈ 28 → ~360/day [31]. This is more headroom than Groq's free tier for the small models.
- **Acceptable Use Policy:** the old standalone AUP URL returns 404 [33]. Acceptable use now sits in **§2.7 of the Self-Serve Subscription Agreement** (last updated 12 Sep 2025): no false sponsorship, no infringing or unlawful content, no malware, no phishing or spam, nothing illegal "including disseminating, promoting or facilitating child sexual exploitation and abuse". **There is no clause on minors as end users and no account-holder age clause** in that agreement [32].
- Cloudflare's *privacy policy* reportedly says its own sites and services are "not intended for… individuals under the age of eighteen". That covers Cloudflare collecting data from its own visitors, not customers' end users, and was seen only through a third-party mirror (low confidence) [34].

## C. Domain open questions

### C1. Is "3% of balance, min NOK 300" compatible with utlånsforskriften § 13? (confidence: medium; the legal reading is partly inference)

- **§ 13 text** (Lovdata): monthly repayment must be at least an amount that clears the loan within 5 years. For credit lines (rammekreditter), the minimum is "beregnes hver måned basert på benyttet kreditt" (calculated each month from the credit used) and must repay within 5 years as a serial loan [35]. Finansdepartementet's page repeats this and uses credit cards as the example. It does not say whether interest is included [37].
- **Finanstilsynet:** rundskriv 6/2022 was replaced by the **veiledning "Praksis for lån til forbrukere" of 20 December 2024**. It comments on §§ 9 and 13 only about repayment deferral and the 60% home-loan rule. It gives **no formula** for credit-card minimums [36].
- **Own inference:** banks recalculate the minimum each month on the current balance. A serial minimum then means a principal share of about balance/60 ≈ **1.67% a month plus interest**. At about 22% nominal interest (≈1.83% a month), that comes to about **3.5%**, which is exactly what DNB uses (3.5%, min NOK 200) [46] and Bank Norwegian uses (3.5%, min NOK 300, from the domain report). A **3% minimum leaves only ~1.17% principal at 22%**, so it fails the rolling test unless the rate is ≤ ~16%. Simulated payoff at 21.99% for NOK 20,000: 3%/300 → 109 months; 3.5%/300 → 90 months. Neither clears the debt in 60 months literally, which supports the rolling reading that banks use.
- **Most importantly, § 3 takes small cards out of scope** (see C2). A first card for an 18–20-year-old will typically have a limit of NOK 5,000–30,000, where § 13 does not apply at all.
- **Recommendation:** use **3.5% of balance, min NOK 300** (Bank Norwegian) or min NOK 200 (DNB). It matches the market and is safe under § 13 for limits above NOK 30,000 too.

### C2. Does § 3 exempt cards with total limits ≤ NOK 30,000? (confidence: high)

Yes, from the **whole regulation**. § 3: "Forskriften gjelder ikke ved innvilgelse av kredittkort dersom kundens samlede kredittkortrammer ikke vil overstige 30 000 kroner" (the regulation does not apply when a credit card is granted if the customer's combined card limits will not exceed NOK 30,000). It sits in the same list as the other exemptions, and those loans are left out of the flexibility quotas (§ 3 sixth ledd) [35]. Finanstilsynet's 2024 guidance repeats this and adds: "Finansavtalelovens bestemmelser om plikt til å vurdere kundens kredittverdighet gjelder uavhengig av forskriftens bestemmelser" (the finansavtaleloven duty to assess creditworthiness applies regardless of the regulation) [36]. The threshold was NOK 25,000 under the 2022 rundskriv [36]. The test is the customer's **combined** card limits, so a second card can push the total over NOK 30,000.

### C3. What exactly does "under 17" mean for the 5.1% trygdeavgift rate? (confidence: high)

- Folketrygdloven § 23-3 itself only says "personinntekt for personer under 17 år eller over 69 år" and does not define the age point [38]. Skatteetaten's 2026 rate page says "personer yngre enn 17 år og eldre enn 69 år **i inntektsåret**" (in the income year) [40].
- NAV's rundskriv on § 23-3 (on Lovdata) defines it: "Med «under 17 år» og «over 69 år» menes **årene før og etter det kalenderår en fyller henholdsvis 17 og 69 år**" (the years before and after the calendar year in which one turns 17 and 69, respectively). The medium rate applies "fra og med det kalenderår medlemmet fyller 17 år" (from the calendar year the member turns 17) [39].
- **Engine rule:** `low_rate = (income_year - birth_year) < 17`. Equivalently, the player is under 17 at the end of the income year. The year the player turns 17, the whole year is taxed at 7.6% (2026), even on income earned before the birthday. The NOK 99,650 lower limit and the 25% cap still apply [40].

### C4. Have the hospitality youth rates been updated for 2026? (confidence: medium)

- **Legally binding (allmenngjort) rates:** Arbeidstilsynet still shows the rates in force **from 15 June 2025**: under 17 NOK 142.58, age 17 NOK 152.08, age 18 NOK 166.34, adult starting wage NOK 204.79 [41]. No 2026 Tariffnemnda decision was found.
- **2026 collective agreement:** the Virke–Fellesforbundet Landsoverenskomst for hotell og restaurant was approved by both parties on 16 June 2026, with rates from 1 June 2026 [43]. The recommended proposal raises all minimum rates by NOK 10.50/h: under 17 **NOK 153.08**, 17 **162.58**, 18 **176.84** (37.5-hour week; 161.53 / 171.55 / 186.60 on a 35.5-hour week). The document says the figures were "ikke endelig godkjent" (not finally approved) [42]. These match the 2025 rates + 10.50 exactly.
- The NHO Reiseliv **Riksavtale**, which underlies the generalised regulation, went to a strike from 19 April 2026 and was settled through mediation on 28 May 2026. That rests on news snippets only, and the new rates were not verified [44].
- **For the game:** use the 2025 allmenngjort rates as the legal floor. Optionally use the 2026 tariff rates (153.08 / 162.58 / 176.84) as a "tariff employer" wage.

### C5. Income floors for 18–19-year-olds at DNB and SpareBank 1 (confidence: medium; official pages publish no floor)

- **DNB (official):** the Ung Mastercard is for ages "18 og frem til du fyller 28 år" (18 until you turn 28), with no annual fee. Price example: nominal 18.60%, effective 20.27% on NOK 5,000 [45]. The DNB Mastercard minimum payment is 3.5% of the balance, min NOK 200 [46]. **No income floor is published** on the card or consumer-loan pages; the loan page says income and debt are fetched from Altinn [47][48]. Aggregators cite NOK 25,000/year for DNB Ung and NOK 50,000/year for DNB Mastercard (low confidence, not from the bank) [50].
- **SpareBank 1 (official):** consumer loans require "**minst 20 år gammel**" (at least 20 years old), a "trygg og stabil økonomi" (secure, stable finances) and no payment remarks [49]. **An 18–19-year-old cannot get a SpareBank 1 consumer loan.** The card pages returned 404. Aggregators say the Ung Mastercard is for ages 18–34 with "fixed income", and that the lowest NOK 5,000 limit needs about NOK 100,000/year (low confidence) [51][52].
- **For the game:** credit cards from 18 with a small limit (5,000–10,000) and a creditworthiness check against job income. Consumer loans should be harder: some banks set 20+, so the game could gate loans to "only specialist lenders at 18–19, at higher interest" or to age 20.

## Consequences for the PRD

1. **Differentiation statement:** neither the architecture (Life Finance) nor wellbeing in the outcome (PersonalFinanceLab, Stock-Trak, SmooLah) is unique by itself. Suggested wording: *"The only finance game built on Norwegian rules (BSU, frikort, trygdeavgift, utlånsforskrift) for ages 15–20, where the outcome weighs wellbeing alongside money and an AI narrates within limits set by a deterministic engine."* Name Life Finance and SmooLah as prior art.
2. **Wellbeing as a core mechanic (#19):** the evidence supports moving it into version one, since every serious competitor with persistent consequences has some form of it. Borrow from SmooLah and PersonalFinanceLab: 2–3 concrete meters (for example social life, stress/peace of mind, housing quality), a failure or penalty state at zero, and an end score that mixes money and wellbeing. Then neither hoarding nor overspending wins.
3. **Engine rules:** credit-card minimum of 3.5%, min NOK 200–300. Card limits ≤ NOK 30,000 for 18–20-year-olds, which puts them outside the utlånsforskrift but still requires a creditworthiness check. Consumer loans age-gated, since SpareBank 1 requires 20+. Trygdeavgift at 5.1% when `income_year − birth_year < 17`, else 7.6%. Hospitality youth wages from the 2025 allmenngjort table.
4. **AI non-functional requirements:** Groq free = about 285 events/day per gpt-oss model (token-bound), 30 RPM. Cloudflare free = about 700–1,100 events/day on gpt-oss-20b / Llama 3.1 8B fp8-fast, with hard failure once over. Keep the provider adapter and the pre-written event fallback. Do not plan on Llama 3.x via Groq free. Neither provider bans products used by minors. Groq puts legal compliance for minors on the customer, which supports the rule of sending no personal data to the LLM.
5. **UX/positioning:** Koll på cashen simplifies the deposit to a fixed 15%, while LifeMode's monthly loop with real carry-over is a concrete improvement. UE's ØkonoMIN and Økonomi og karrierevalg are the nearest Norwegian classroom formats and a possible school channel.

## Still open

- **Devpost page for Life Finance:** still 403, so the link between the Devpost entry and the GitHub repo is inferred from near-identical wording, not confirmed. Open it in a browser.
- **Groq per-account limits:** the free table is published, but the page says exact limits and exceptions are only visible in the console (Settings → Limits). Check this when the account is created, along with real reasoning-token use per event.
- **Groq DPA coverage for free accounts:** not re-examined; still disputed per the earlier report.
- **Cloudflare privacy-policy wording on under-18s:** seen only via a third-party mirror. cloudflare.com/privacypolicy was not fetched directly.
- **Whether a rolling "balance/60" reading of § 13 is the official one:** no Finanstilsynet text gives the formula. The conclusion rests on § 3 (small cards exempt) and on market practice.
- **2026 allmenngjort hospitality rates:** no Tariffnemnda decision found. The Riksavtale 2026 rates and the final approval of the Virke figures were not seen in a primary source.
- **SpareBank 1 card income floor and DNB loan age limit:** not published on the bank pages that loaded (several returned 404). Only customer service or a test application would settle these.
- **Nordea Økonomipeil class game:** mentioned in a search snippet only; its content was not verified.
- **Taloussankari wellbeing:** no wellbeing stat in the game's data file [7]. Whether the narrative scores mood implicitly was not checked by playing.

## Sources

| # | Claim | URL | Accessed |
|---|---|---|---|
| 1 | Life Finance repo: README (engine/AI split, Groq, hackathon, roadmap), contributors, created 2026-07-14, last push 2026-07-21 | https://github.com/tiennguyentony/life_finance | 2026-10-31 |
| 2 | Life Finance live demo responds (HTTP 200, title "Life Finance") | https://life-finance-mu.vercel.app/ | 2026-10-31 |
| 3 | Life Finance: cash-flow and wellbeing previews; AI cannot create effects | https://github.com/tiennguyentony/life_finance/blob/main/docs/product/interactive-events-v1.md | 2026-10-31 |
| 4 | Life Finance: under-18 age falls back to persona age | https://github.com/tiennguyentony/life_finance/blob/main/docs/product/board-experience.md | 2026-10-31 |
| 5 | Devpost Life Finance page returns 403 | https://devpost.com/software/somename-u9gsz6 | 2026-10-31 (blocked) |
| 6 | Taloussankari web app live; FI/SV/EN titles; asset version 2026-10-01 | https://taloussankari.com/ | 2026-10-31 |
| 7 | Taloussankari game data: 7 chapters, 514 cards, cash + experience only, timestamp 2025-10-27 | https://taloussankari.com/data/taloussankari-db.json?v=10 | 2026-10-31 |
| 8 | Taloussankari competition final 18 Mar 2026; organisers; mobile game for 8th graders | https://www.nordea.com/fi/media/2026-03-18/nuorten-taloustaidot-testissa-taloussankari-kilpailu-vie-suomen-nuoria-kohti-maailman-talousosaamisen-karkea | 2026-10-31 |
| 9 | TAT Taloussankari page refused connection | https://tat.fi/palvelu/taloussankari/ | 2026-10-31 (blocked) |
| 10 | NDLA "Forbruk og personlig økonomi" (Pengesmart, Kredittfella); NDLA search API, 0 hits for "økonomispill" | https://ndla.no/e/tverrfaglige-temaer/forbruk-og-personlig-okonomi/4c5bc63914 ; https://api.ndla.no/search-api/v1/search/ | 2026-10-31 |
| 11 | UE programme list | https://www.ue.no/program | 2026-10-31 |
| 12 | UE ØkonoMIN: vgs, 2 lessons, digital budget calculator, job/salary → home deposit | https://www.ue.no/program/okonomin | 2026-10-31 |
| 13 | UE Økonomi og karrierevalg: 10th grade, app with student login | https://www.ue.no/program/økonomi-og-karrierevalg | 2026-10-31 |
| 14 | Finans Norge school resources (Kalle task, Pengequiz, På egne ben) | https://www.finansnorge.no/tema/personlig-okonomi/personlig-okonomi-i-skolen/ | 2026-10-31 |
| 15 | Nordea Økonomipeil, interactive class game (snippet); 8,500 pupils in 2024 | https://www.nordea.no/privat/din-okonomi/ung/okonomipeil.html ; https://www.nordea.com/no/nyheter/underviste-8500-skoleelever-i-personlig-okonomi | 2026-10-31 (search snippets) |
| 16 | "Sjef i eget liv" budget simulator (FNO/Husbanken/NAV), old | https://www.smartepenger.no/94-nyhet/1155-planlegg-boligkjop-med-nytt-nettverktoy | 2026-10-31 (search snippet) |
| 17 | Money Wise on App Store Norway | https://apps.apple.com/no/app/money-wise-game-life-sim/id1491095072 | 2026-10-31 |
| 18 | Money Wise on Google Play (gl=NO, Norwegian IP) | https://play.google.com/store/apps/details?id=com.DotDotFireLimited.TheNeighborMood&gl=NO | 2026-10-31 |
| 19 | Infinite Life Simulation on App Store Norway, 18+ | https://apps.apple.com/no/app/infinite-life-simulation/id6503607456 | 2026-10-31 |
| 20 | Infinite Life Simulation on Google Play (Pickle.co) | https://play.google.com/store/apps/details?id=co.pickle.infinite_life_sim&gl=NO | 2026-10-31 |
| 21 | Koll på cashen teacher guide: 4 time loops, savings carry over, 15% deposit simplification, no wellbeing | https://www.kollpacashen.se/wp-content/uploads/2025/03/lararhandledning-spelet.pdf | 2026-10-31 |
| 22 | Koll på cashen lärarstöd page | https://www.kollpacashen.se/lararstod/ | 2026-10-31 |
| 23 | SmooLah: ages 17–26, net worth/happiness/peace of mind/energy, reset at zero | https://skbi.smu.edu.sg/smoolah-stage/faq | 2026-10-31 |
| 24 | PersonalFinanceLab Budget Game: QoL + credit + emergency fund balance | https://www.personalfinancelab.com/teacher-resource-packet/budget-game/ | 2026-10-31 |
| 25 | Stock-Trak: "Avoiding every expense is not a winning strategy"; QoL ranking | https://www.stocktrak.com/personal-finance-professors/college-personal-finance-class-examples/ | 2026-10-31 |
| 26 | Payback: debt vs happiness, social life, academics | https://www.ngpf.org/blog/teacher-tips/teacher-tip-interactive-payback/ | 2026-10-31 |
| 27 | Groq free/developer rate limits (`freeRows`/`devRows`), per-org, console for exact limits | https://console.groq.com/docs/rate-limits | 2026-10-31 |
| 28 | Groq models: Llama 3.x "Enterprise/Contact Sales"; gpt-oss production; Qwen3.8 preview | https://console.groq.com/docs/models | 2026-10-31 |
| 29 | Groq Services Agreement §2 (18+), §6.3 (minors: customer responsible); last modified 22 Jun 2026 | https://console.groq.com/docs/legal/services-agreement | 2026-10-31 |
| 30 | Groq Acceptable Use & Responsible AI Policy, effective 15 Oct 2025, no age rule | https://console.groq.com/docs/legal/ai-policy | 2026-10-31 |
| 31 | Cloudflare Workers AI: 10k neurons/day, reset 00:00 UTC, error over limit, neuron rates | https://developers.cloudflare.com/workers-ai/platform/pricing/ | 2026-10-31 |
| 32 | Cloudflare Self-Serve Subscription Agreement §2.7 Acceptable Use, no minors clause; updated 12 Sep 2025 | https://www.cloudflare.com/terms/ | 2026-10-31 |
| 33 | Old standalone Cloudflare AUP URL returns 404 | https://www.cloudflare.com/website-terms/acceptable-use/ | 2026-10-31 (404) |
| 34 | Cloudflare privacy policy "not intended for… under the age of eighteen" (third-party mirror) | https://conductatlas.com/platform/cloudflare/cloudflare-privacy-policy/services-not-intended-for-minors/ | 2026-10-31 (search snippet, low) |
| 35 | Utlånsforskriften § 3 (card ≤ 30,000 exemption) and § 13 (5-year serial, monthly on used credit) | https://lovdata.no/dokument/SF/forskrift/2020-12-09-2648 | 2026-10-31 |
| 36 | Finanstilsynet veiledning "Praksis for lån til forbrukere", 20 Dec 2024; replaces rundskriv 6/2022; § 3 and kredittvurdering | https://www.finanstilsynet.no/contentassets/92f054dcf46040a1990e6c20c7133a55/praksis-for-lan-til-forbrukere2.pdf | 2026-10-31 |
| 37 | Finansdepartementet on utlånsforskriften: rammekreditt minimum calculated monthly (updated 12 Dec 2024) | https://www.regjeringen.no/no/tema/okonomi-og-budsjett/finansmarkedene/utlansforskriften2/ | 2026-10-31 |
| 38 | Folketrygdloven § 23-3: low rate for "personer under 17 år eller over 69 år" | https://lovdata.no/lov/1997-02-28-19/§23-3 | 2026-10-31 |
| 39 | NAV rundskriv to § 23-3: "under 17" = years before the calendar year one turns 17 | https://lovdata.no/nav/rundskriv/r23-00 | 2026-10-31 |
| 40 | Skatteetaten trygdeavgift 2026: 5.1% "yngre enn 17 år… i inntektsåret"; 7.6% wage rate | https://www.skatteetaten.no/satser/trygdeavgift/?year=2026 | 2026-10-31 |
| 41 | Arbeidstilsynet: hospitality minimum wage from 15 Jun 2025 (142.58/152.08/166.34/204.79) | https://www.arbeidstilsynet.no/en/pay-and-engagement-of-employees/pay-and-minimum-rates-of-pay/minimum-wage/ | 2026-10-31 |
| 42 | Fellesforbundet 2026 recommended proposal, hotel/restaurant: +10.50/h; youth 153.08/162.58/176.84 | https://www.fellesforbundet.no/globalassets/blokker/t26/riksavtalen/stemmemateriell-landsoverenskomst---2026-v3.pdf | 2026-10-31 |
| 43 | Virke–Fellesforbundet hotel/restaurant agreement 2026 approved 16 Jun 2026; rates from 1 Jun 2026 | https://www.virke.no/tariff-og-lonn/finn-tariffavtale/landsoverenskomst-for-hotell--og-restaurantvirksomheter-ff/ | 2026-10-31 |
| 44 | NHO Reiseliv hotel/restaurant strike from 19 Apr 2026, mediation accepted 28 May 2026 | https://pubt.io/view/91E3A9B3205459B93E9989CAAC551B294AA5AAD7 | 2026-10-31 (search snippet, low) |
| 45 | DNB Ung Mastercard: ages 18 to 28, 18.60% nominal / 20.27% effective | https://www.dnb.no/kort/ung | 2026-10-31 |
| 46 | DNB Mastercard minimum payment 3.5%, min NOK 200 | https://www.dnb.no/kort/kredittkort/mastercard | 2026-10-31 |
| 47 | DNB credit card overview: Ung 18–28, no income floor stated | https://www.dnb.no/kort/kredittkort | 2026-10-31 |
| 48 | DNB consumer loan: income/debt fetched from Altinn; no age/income floor stated | https://www.dnb.no/lan/forbrukslan | 2026-10-31 |
| 49 | SpareBank 1 consumer loan: at least 20 years old, stable finances, no payment remarks | https://www.sparebank1.no/nb/bank/privat/lan/forbrukslan.html | 2026-10-31 |
| 50 | Aggregator: DNB Ung NOK 25,000/yr, DNB Mastercard NOK 50,000/yr (unofficial) | https://www.kredittkortlisten.no/kredittkort/dnb-ung-kredittkort/ | 2026-10-31 (search snippet, low) |
| 51 | Aggregator: SpareBank 1 Mastercard ~NOK 100,000/yr for 5,000 limit (unofficial) | https://kortio.no/kort/sparebank1-kredittkort/ | 2026-10-31 (search snippet, low) |
| 52 | Aggregator: SpareBank 1 Ung Mastercard ages 18–34, fixed income (unofficial) | https://www.kredittkortlisten.no/kredittkort/sparebank-1-ung-mastercard/ | 2026-10-31 (search snippet, low) |
