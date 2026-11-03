---
topic: LifeMode PRD input extract, users and market
created: 2026-11-03
purpose: Facts only, for journey-led PRD work. No recommendations from the extractor. Where a source makes its own recommendation, it is labelled as that source's.
---

# Extract: users and market

**Source keys** (paths under `.docs/planning-artifacts/`)

| Key | File |
|---|---|
| UR | `briefs/brief-Ibe160-prosjektmappe-2026-09-17/user-research.md` |
| MR | `briefs/brief-Ibe160-prosjektmappe-2026-09-17/market-research.md` |
| MV | `briefs/brief-Ibe160-prosjektmappe-2026-09-17/market-validation.md` |
| TB | `briefs/brief-Ibe160-prosjektmappe-2026-09-17/tilbakemelding-product-brief.md` |
| GF | `briefs/brief-Ibe160-prosjektmappe-2026-09-17/research/competitive-youth-finance-sim-games-gap-fill-2026-10-27/research.md` |
| PT | `research/playtest-competitors-2026-10-31/notes.md` |
| MP | `meeting-prep-2026-11-05.md` |
| ML | `prds/prd-IBE160-G13-2026-10-22/.memlog.md` (the authoritative decisions; cited by line) |
| BR | `briefs/brief-Ibe160-prosjektmappe-2026-09-17/brief.md` (read only "What Makes This Different", to check issue #12) |
| #12, #13 | GitHub issues, read 2026-11-03 |

**Not read:** `research/remaining-pre-prd-research-2026-10-31/research.md`. MR, PT and MP rely on it, so anything they attribute to it is reported here second-hand.

---

## 1. Survey «Unge og penger»

### Sample

- **133 responses verified** (matches ML line 17). The age table adds up: 50 + 75 + 8 = 133. [UR § Results; § Respondents]
- Anonymous Google Form, run 22-29 October 2026, analysed 2026-10-31. Percentages are of all 133 respondents. Raw data is kept outside the repo. [UR § Results]

| Age | n | Share |
|---|---|---|
| 15-16 | 50 | 38% |
| 17-18 | 75 | 56% |
| 19-20 | 8 | 6% |

[UR § Respondents]

### Caveats about who responded and what was measured

- It is a convenience sample, "probably spread through the team's own networks and schools", so it is not representative. [UR § Limitations]
- Behaviour is self-reported. UR notes that the 14% reporting peer pressure "may be low", given how many free-text regrets are about trends and what others have. [UR § Limitations]
- The 19-20 group (n=8) is "too small for conclusions on its own". [UR § Respondents; § Limitations]
- **The survey did not test the concept.** It did not ask whether LifeMode sounds fun, or whether mechanics such as wellbeing and lasting consequences make sense. UR says those questions are "still open". [UR § Results, "What the survey covered"; § Limitations; MP § 4]
- **No parent survey in this round** (team decision, 2026-10-31). [UR § Results; § Limitations; MP § 4]
- UR's opening sections ("Pre-development User Research", "Research Purpose") still describe the two-survey plan, including concept and mechanics questions. Only the player survey ran, and it covered habits, knowledge and wishes. [UR § Pre-development; § Results]

### Income and products used

- **Sources of money** (multiple choice): parents or pocket money 68%, part-time job 52%, stipend or student loan 41%, summer or odd jobs 36%, gifts 36%, selling things (Finn, Tise) 24%. [UR § Respondents]
- **Used themselves** (multiple choice): bank account and card 98%, savings account 87%, own fixed costs such as mobile and transport 38%, borrowed from friends or family 35%, BSU 14%, buy now pay later 6%, credit card or consumer loan 4%. [UR § Respondents]

### Habits and attitudes

- **Saving:** 73% save most or some of what they get; 26% spend most or all. [UR § Habits and attitudes]
- **The trip dilemma** (trip costs NOK 3,200, you have NOK 1,500): work extra 29%, borrow from parents or friends 26%, stay home 20%, use savings 17%. Only one person chose buy now pay later or a credit card. Several free-text answers describe asking parents first. [UR § Habits and attitudes]
- **Unexpected expense in the last year:** 36% had one that was hard to pay. About half of them (17% of all) got help from family. [UR § Habits and attitudes]

| Agree (fully or partly) | Share |
|---|---|
| I know roughly how much money I have right now | 88% |
| I feel ready to make my own money choices at 18 | 64% |
| I'd like to learn more about money | 63% |
| I often run out of money before I get more | 39% |
| Before I buy something, I think about how it affects my money months from now | 38% |
| I buy things I regret later | 37% |
| I feel pressure from friends to spend money | 14% |

[UR § Habits and attitudes]

### Understanding of terms

| Term | Understand well | A little | Not at all |
|---|---|---|---|
| Budget | 86% | 13% | 1% |
| Fixed costs | 85% | 12% | 3% |
| Buy now, pay later | 71% | 26% | 4% |
| Frikort / tax card | 63% | 26% | 11% |
| Interest | 56% | 34% | 10% |
| BSU | 44% | 25% | 31% |
| Credit card and consumer loan | 39% | 41% | 20% |

- BSU is understood well by 26% of 15-16-year-olds and 57% of 17-18-year-olds.
- Asked what happens if you buy a NOK 5,000 phone on a credit card and pay only the minimum each month, 72% answered correctly (you pay more than NOK 5,000) and 28% answered wrong or "don't know".
- **Where they learned most about money** (up to three): parents or family 88%, social media 42%, school 38%, own mistakes 32%, bank or bank apps 15%, friends 11%.

[UR § Understanding of terms]

---

## 2. What users want, fear and pay attention to

No source reports fears as a measured category. The closest evidence is regrets, running out of money and hard-to-pay expenses, listed below as reported.

### What they want

- 63% would like to learn more about money. [UR § Habits and attitudes]
- **What they wish someone had taught them** (most frequent): budgeting and saving; interest; BSU, credit cards and loans; paying bills and invoices; funds, stocks and investing (mentioned often, including by 15-16-year-olds); housing loans and moving out; available stipends. [UR § Free text: what they wish]
- Several ask for it to be explained more simply and taught earlier in school. [UR § Free text: what they wish]

### What they regret and struggle with

Regret themes, roughly by frequency [UR § Free text: what they regret]:

1. **Small impulse purchases that add up:** snacks, food and drink they did not need, takeaway. «Jeg kjøper smågodt veldig ofte og pleier å angre ved slutten av uken når jeg ser hvor mye penger det blir til sammen.»
2. **Clothes** they did not use or like, often bought online or without trying them on.
3. **Trends and social comparison:** a jacket trending on TikTok, an expensive laptop «bare på grunn av at jeg følte alle hadde en».
4. **Collectibles and chance-based purchases:** blind boxes, Pokémon cards, in-game purchases. One describes getting hooked after a lucky draw.
5. **Commitments they did not understand:** a gym membership never used, a binding period on a subscription they were not aware of.
6. **Running out before the month ends:** «jeg hadde ikke penger til andre ting, som feks mat i kantina, eller faste utgifter.»
7. **BSU seen as a trap by one respondent:** the money is locked, and NOK 300,000 is «ikke nok til leilighet engang».

### Real-world behaviour relevant to journeys

- Asking family is a common real choice: 26% would borrow from parents or friends for the trip, 35% have borrowed from friends or family, and 17% of all got family help with an unexpected expense. [UR § Respondents; § Habits and attitudes]
- Current use of credit is low (4%), and buy now pay later is rare (6%). [UR § Respondents; § What this means]
- Awareness of current money is high (88%), but only 38% think months ahead and 39% often run out. [UR § Habits and attitudes]

### Interpretations recorded in UR ("What this means for LifeMode")

These are the team's own conclusions from the survey, not survey results. [UR § What this means]

- Regrets are about value for money and satisfaction, not amount, which UR says supports the wellbeing differentiator.
- UR calls thinking ahead "the weak spot" that persistent consequences and the choice → consequence link should train.
- Family is the main source of money, knowledge and help, and the event library should include family as an actor with its own consequences.
- Event library candidates: small purchases that add up, trend-driven buys, collectibles and loot-box-style spending, in-game purchases, subscriptions with binding periods, unused memberships, takeaway.
- BSU and credit/consumer loans are the least understood terms, and BSU is weakest among 15-16-year-olds. Explanations must use plain language. The BSU disclosure should cover both the NOK 0 deduction without tax and the fact that the money is locked.
- Investing stays out of version one for now (decided 2026-10-31), as a candidate for later. It is not one of the five money mechanisms in the brief.
- The credit mechanics from 18 introduce something most players have not tried, so they need more explanation than the rest.

### Later testing questions still open

Once a playable version exists, user testing can evaluate whether players understand the gameplay and consequences, whether it feels more like a game than schoolwork, whether they would voluntarily return, whether the mechanics work as intended, and whether they find it valuable enough to use voluntarily. [UR § Later User Testing]

---

## 3. Competitors and positioning

### Nearest comparators

"Nearest" is MR's label for the group added on 2026-10-31. [MR § Finance simulations]

| Product | Positioning as reported | Source |
|---|---|---|
| **Koll på cashen** (Finansinspektionen + Riksbanken, SE, 2025) | Free life-stage personal-finance game for the same age group (GF: upper secondary, 16-19). Four life phases where savings and income carry over; home deposit fixed at 15% of the price. No wellbeing mechanic, no AI. Swedish only. | MR § Finance simulations; PT § Answered by desk research; GF § D3 |
| **PersonalFinanceLab Personal Budget Game** (US/CA) | Paid school licence (price not public). 12 simulated months of about 20 minutes each. Choices shift net worth, credit score and a Quality of Life Score. Closest match to LifeMode's monthly loop with wellbeing, but more complex, fixed-script, US-based and college level. No AI. | MR § Finance simulations; GF § D1, § D3 |
| **SmooLah** (Singapore Management University, ages 17-26) | Tracks net worth, happiness, peace of mind and energy. Game resets if one reaches zero. | MR § Finance simulations |
| **Payback** (NGPF, US) | Trades student debt against happiness, social life and academics. Free browser game. | MR § Finance simulations; GF § D1 |
| **Life Finance** (hackathon prototype, July 2026) | Same split as LifeMode: code owns the money, an LLM narrates. Wellbeing previews for each choice. US/USD, adults, live demo, not maintained since July 2026. | MR § Finance simulations |
| **Taloussankari / Finance Hero** (Nordea, Pörssisäätiö, TAT, FI) | Live chat-style web game in 7 chapters for 8th graders. Tracks only cash and experience. No AI, no wellbeing. | MR § Finance simulations; GF § D1b |
| **Money Wise Game: Life Sim** (Dot Dot Fire, UK) | Free iOS branching story about a US high-school senior; job choices affect later jobs and the ending; scams and payday loans. | GF § D1; MR § Finance simulations |
| **Infinite Life Simulation** (indie, iOS) | LLM branching life story, rated 18+, free + IAP + ads, entertainment rather than finance education. | GF § D2, § D3; MR § Finance simulations |

MR says Money Wise and Infinite Life Simulation are available in the Norwegian stores and are built on US contexts. [MR § Finance simulations]

### Life-sim games

- **BitLife** (Candywriter) is the category leader: text-based, choice-driven. Finance is present but shallow, and decisions resolve instantly. Reviewers criticise it for oversimplifying and creating "a misleading sense of control"; one piece warns prolonged play "can desensitize young minds" to financial recklessness or gambling. [MR § Life-simulation games]

### Teen finance apps and courseware

- **Zogo:** gamified micro-learning, 1,200+ modules, gift-card rewards, distributed via banks and credit unions (B2B2C). Quiz/courseware, not a life sim. [MR § Teen-focused]
- **Greenlight, Copper, Step:** real debit-card or neobank products with parental controls and literacy features, on family subscriptions. [MR § Teen-focused]
- **EVERFI:** B2B2C courseware through banks and schools, 60M+ learners. Structured e-learning. [MR § Teen-focused]
- **Gimi** (SE; backed by or partnered with Nordea, Tink, Marqeta): app + card for ages about 7-15, 800k+ downloads, gamified lessons. Skews younger, no simulation. [MR § Norwegian and Nordic]

### Norway and the Nordics

- **Finans Norge:** Skolemeny.no and NM i Pengequiz. Its own 2025 research says Norwegian youth struggle with financial knowledge. [MR § Norwegian and Nordic]
- **Nordea Økonomipeil:** free, curriculum-anchored, grades 9-10 and upper secondary; videos, assignments, quizzes. [MR § Norwegian and Nordic]
- **Ungt Entreprenørskap's ØkonoMIN and Økonomi og karrierevalg, plus NDLA text and tasks:** the closest in Norway, classroom-based, with a digital budget tool. MR states there is still no digital personal-finance game for ages 15-20 in Norway. [MR § Finance simulations]
- **Norges Bank Horisont:** free 2.5-hour in-person role-play in Oslo, about the macro economy. **SpareBank 1 Økonomipatruljen, DNB:** guest teaching or self-tests. [GF § D1b]
- **OsloMet UngKomp, Forbrukerrådet Ung:** research and guidance, noted as possible longer-term partners along with Nordea. [MR § Norwegian and Nordic; § Potential partners]
- **Other Nordic:** Pengalabbet (SE, ages about 10-12), Ekonomilabbet (SE), Money Week and Money Quiz (DK, grades 7-9). [GF § D1b, § D3]

### Other products in GF

NGPF Arcade (12 free short games), SPENT, Stukent (snippet only, low confidence), LongRuay (snippet only, adult wealth sim), Piggy Investors (in development), the Agentic Knowledge Tracing paper (research prototype), and Gameclass × Morris County teens (no mechanics published). [GF § D1, § D2, § D3, § Source appendix]

### Reliability of this evidence

- The Norwegian gap is an absence finding, rated medium confidence in GF. [GF § Executive summary]
- Several close products (Life Finance, LongRuay, Stukent) were visible only through search snippets on 2026-10-27, and "the run cannot rule out more products of this kind". [GF § Executive summary]
- GF's red-team pass did not run. [GF § Contrary evidence]
- The two claims the positioning rests on (the Norwegian gap, AI-free school games) are due for re-check by 2027-01-27. GF says that if the PRD cites them, they should be re-checked before the December 2026 delivery. [GF § Staleness map]
- MR says these are "initial research findings", not a claim that no comparable exists globally. [MR § Market gap]

### Commercial context

- Parents are named as the main customer group in the initial commercial validation (value of a safe simulation, willingness to pay for a Family version, expected functionality). [MV § Initial Commercial Validation] No parent data exists yet, because the parent survey was not run. [UR § Results]
- Schools, banks, insurers and municipalities are longer-term hypotheses, outside the initial research. [MV § Future Commercial Validation]
- Possible revenue models: Family Premium, school licences, B2B2C partnerships, scenario packs. [MV § Potential Future Revenue Models]
- Public bodies and banks hold the Nordic school channel and publish free, AI-free games. [GF § Cross-dimension insights]

---

## 4. Current narrowed differentiation claim

**Current wording (narrowed 2026-10-31):**

> **Built for Norway: a personal-finance life game for 15-20-year-olds, based on Norwegian rules and life stages, that combines good money management with wellbeing without becoming complicated.**

[MR § Market gap; same content in MP § 5 and BR § What Makes This Different]

- **Why it was narrowed:** no single part is unique. Life Finance has the engine-plus-AI split, and PersonalFinanceLab, SmooLah and Payback weigh wellbeing against money. [MR § Market gap]
- **Supporting statement:** PersonalFinanceLab is the closest with wellbeing but is more complex, US-based and aimed at older students. No product found is built on Norwegian rules such as BSU, frikort and studielån. [MR § Market gap]
- **Status:** "a starting point; the team will refine it later". [MR § Market gap; MP § 5]
- **AI:** not part of the MVP. [ML line 17; BR § What Makes This Different; MP § 4 (#17 closed)]
- **Related candidate wording:** "money and how you use it, not just how much you have". [PT § Consequences for planning]
- **Advantage as stated in the brief:** not a technical moat, but being first with this combination for Norwegian teenagers, plus a small team that can iterate quickly on playtester input. [BR § What Makes This Different]

---

## 5. Competitor playtests

**The notes describe themselves as first impressions from playing, not a systematic review, and their status is `in-progress`.** [PT, frontmatter and intro]

| Product | Played? | Finding |
|---|---|---|
| Koll på cashen | **Yes**, by Myggsaa, 2026-10-31 | The visual style is too childish for 15-20-year-olds, so LifeMode needs a more grown-up style, as a deliberate contrast in DESIGN.md. Wellbeing should be tied directly into the economy, so that hoarding money at the cost of wellbeing is not a "win". [PT § Koll på cashen; § Consequences] |
| PersonalFinanceLab | **No** ("Not played yet") | Desk research only. MP says it scores "Quality of Life" alongside money and is "worth playing before deciding the wellbeing design". [PT § PersonalFinanceLab; MP § 3] |
| All others in section 3 | **No playtest notes exist** | PT covers only the two products above. Their descriptions in this extract come from desk research. [PT; MR § Finance simulations; GF] |

- Whether Koll på cashen's money carries over was **answered by desk research, not by playing**. [PT § Answered by desk research]
- The Koll på cashen findings come from one team member's session. No session length is recorded, and #13 estimated about an hour per product. [PT § Koll på cashen; #13]
- **Open questions in GF:** Life Finance's live status, Taloussankari's status and Norwegian store availability are later answered in MR. Who made Life Finance is not stated in the extracted text; MR lists only a GitHub repository (`github.com/tiennguyentony/life_finance`) as a source. GF also lists NDLA, ue.no, Finansportalen, Eika and Sbanken as unsearched; MR now covers ue.no and NDLA, and the extracted sources do not say whether the other three were checked. [GF § Open questions; MR § Finance simulations]

---

## 6. Feedback on the brief

Faglærer in IBE160 (prepared with KI support), 2026-10-06, on brief commit bb1ba16. [TB, header]

**Overall:** "Godt utgangspunkt med justeringer." Difficulty rated **Vanskelig**. Feasibility: "Gjennomførbart med justert omfang." [TB § Samlet vurdering; § Vurdert vanskelighetsgrad; § Konklusjon]

**Praised:**

- The idea and the 3,200 / 1,500 trip example with a consequence in month 9. [TB § Samlet vurdering]
- The principle «KI-en skaper livet, finansmotoren bestemmer konsekvensene». [TB § Samlet vurdering]

**Most important changes** [TB § Samlet vurdering]:

1. Success criteria rest almost only on a playtest with 10-20 people aged 14-20, which is demanding (minors, consent) and gives no testable requirements. Add functional criteria that can become test cases.
2. The engine must "alltid regne riktig", but no rules are stated. Define a small rule set with worked examples as fasit.
3. Plan how sensor can run the app locally without the team's accounts and keys, and consider whether v1 needs login at all.

**Risk ratings** [TB § Gjennomførbarhet]:

- **Stor risiko:** Kjørbar for sensor, because Supabase and an external LLM require accounts and keys. "Uten en lokal database og et sett med forhåndsskrevne hendelser (fallback) kan sensor ikke spille."
- **Risiko:** Tid og omfang, BMAD-flyten (no concrete game loop or rule set), Egnet for Claude Code (four-part stack), Kontroll på KI-ens arbeid, Testbarhet, Avhengigheter og kostnader.

**Proposed scope adjustments** [TB § Forslag til justering]:

1. V1 as one shorter life span (e.g. 16-19) with 4-5 mechanisms (lønn, sparing, faste kostnader, forbrukslån/kreditt med rente, uforutsette utgifter) and a monthly loop. Flytting, utdanning and førerkort in later steps.
2. Build the engine and a pre-written event library first, so the game works without KI.
3. Drop login in v1, and consider a simpler stack.

**Section notes on the brief** [TB § 1]:

- **Solution:** describe the loop in 3-5 steps (se situasjon → velg → se konsekvens i tall → neste måned).
- **Who This Serves:** both 14-20 and 15-20 appear; decide, and consider whether to test with minors or use medstudenter.
- **Success Criteria:** "Endre". Examples: «et lån på X kr med Y % rente gir riktig saldo etter 12 måneder», «en ugyldig KI-hendelse erstattes av en forhåndsskrevet», «spillet kan fullføres fra start til slutt uten KI».

**Del 1 weights and status** [TB § 2]:

| Criterion | Weight | Status |
|---|---|---|
| Prosess og KI-styring | 30% | OK |
| Funksjonalitet og omfang | 20% | Juster |
| Kvalitetssikring og testing | 15% | Endre |
| Design og brukeropplevelse | 10% | OK |
| Kodekvalitet og arkitektur | 10% | Juster |
| README og kjørbarhet | 10% | Endre |
| Ryddighet i repoet | 5% | Juster |

**Teacher's next steps** [TB § 3]: write the rule set with 3-5 worked examples; describe the loop and narrow "In"; add functional, testable success criteria; decide how the app runs without KI and without a Supabase account.

---

## 7. The 5 November meeting

**Goal, from the lecturer:** be "fit for fight" with enough research to start the PRD. MP's status is `draft`. [MP, frontmatter and intro]

### Already decided (do not reopen)

Endgame, choice → consequence, event library and privacy were recorded on 2026-11-03. [MP § 1; ML lines 15-16] Details:

- **Endgame:** 60 months, ending on the 20th birthday; three life goals; wellbeing = stress, free time, social life; four endings checked in order (loss, real win, hollow win, goal not reached). [ML line 16]
- **Choice → consequence:** cause link on every engine effect plus "Hvorfor?", tests F9 and F10. [ML line 15]
- **Event library:** fixed schema, minimum 30, target 60-80, plus about 10 crises, about 55/45 before/after 18. [ML line 15]
- **Privacy:** login with username, no email, no real age, no free text beyond the username, playtests 18-20 only. Open privacy questions are to be checked before go-live (#24) and do not block the MVP or PRD. [ML line 15]
- **Other settled items:** no AI in the MVP (#17); investing out of version one; no parent survey this round; #16 finance rules closed; #11 settled. [MP § 2, § 4, § 5; ML line 17]

### Still undecided

| Item | Source |
|---|---|
| How to make wellbeing different from PersonalFinanceLab's "Quality of Life" and SmooLah's happiness meter | MP § 6 |
| How wellbeing is measured and affects the ending (listed as open in MP § 6; the components and endings are now fixed by ML line 16, but no extracted source fixes the measurement detail) | MP § 6; ML line 16 |
| Credit-card minimum payment: change from 3% to 3.5%, min NOK 200-300 (rule 5 and worked example 4). Desk research says 3% at 22% likely fails utlånsforskriften § 13. | MP § 4, § 6 |
| What visual style fits 15-20-year-olds without feeling childish | MP § 6 |
| Family as an actor: how the game models it and what it costs the player | MP § 6 |
| Which survey regrets become events | MP § 6 |
| Whether a short concept test is needed before the PRD | MP § 6 |
| Further refinement of the differentiation wording | MP § 5; MR § Market gap |
| Whether to play PersonalFinanceLab before deciding the wellbeing design | MP § 3; #13 |

### Other items in the prep note

- **#18:** use the new LK20 subject codes and have a teacher review the quiz proposals. [MP § 5]
- **Age limit (#21):** 13 today (personopplysningsloven § 5). A rise to 15 is proposed, not adopted as of June 2026, with a bill expected in the Storting by end of 2026. It matters only if consent is the legal basis. [MP § 2]
- **Credit in practice:** SpareBank 1 requires age 20+ for consumer loans; DNB publishes no income floor. [MP § 4]
- **Trygdeavgift:** the 5.1% rate applies to every year before the calendar year you turn 17. [MP § 4]

---

## 8. What remains on issues #12 and #13

Both issues are **OPEN**, have no comments, and were last updated 2026-10-31. [#12; #13]

### #12: narrow the differentiation claim and add new competitors to market-research.md

| Asked for | State | Source |
|---|---|---|
| Add Koll på cashen and PersonalFinanceLab to `market-research.md` | Done | MR § Finance simulations |
| Rewrite the claim in the brief | Done, as a "Narrowed differentiation" paragraph. The earlier paragraph about what "we did not find elsewhere" (engine + AI) remains directly above it. | BR § What Makes This Different |
| Rewrite the claim in the PRD | **Not done.** A search of the current `prd.md` finds no differentiation text. | `prd.md` search, 2026-11-03 |

**Also remaining:** the wording is labelled a first version, "to be refined further". [MP § 5; MR § Market gap]

The adopted wording also differs from the one proposed in #12. It drops "no live product … combines" in favour of "built for Norway" and adds wellbeing. [#12; MR § Market gap]

### #13: play Koll på cashen and try PersonalFinanceLab before the UX journeys in the PRD

| Asked for | State | Source |
|---|---|---|
| Play Koll på cashen | Done by Myggsaa, 2026-10-31 | PT § Koll på cashen |
| Establish whether money carries between life phases | Answered by desk research, not play | PT § Answered by desk research |
| Try PersonalFinanceLab | **Not done** | PT § PersonalFinanceLab; MP § 3 |
| Note findings in the research folder or PRD | Done for Koll på cashen; the notes remain `in-progress` | PT |

---

## 9. Conflicts between sources

Where a source conflicts with the memlog, the memlog is authoritative.

| Topic | Stale or conflicting statement | Current position |
|---|---|---|
| Wellbeing components | "free time, social life, stress, housing" [PT § Koll på cashen; MP § 3] | Stress, free time, social life; housing is not listed [ML line 16; MP § 1] |
| Wellbeing as differentiator | "Must settle before the PRD", "kept open" [PT § Consequences; MP § 3] | Wellbeing is in the decided endgame [ML line 16] |
| Replay | "Replay from a crossroads" [MP § 1 table] | Replay from age 15, none from a crossroads [ML line 16] |
| Login | "Anonymous login or resume code" [MP § 1 table] | Username login, Supabase Auth, player-created password [ML line 15] |
| Login and scope, teacher's suggestion | Drop login in v1, shorter life span e.g. 16-19 [TB § Forslag til justering] | Login kept; 60 months, ending on the 20th birthday, replay from age 15 [ML lines 15-16] |
| AI in the differentiator | "Only the combination holds: … + AI narration" [MP § 4]; "deterministic financial simulation + persistent game state + AI-generated life narrative" [MR § Market gap, pre-narrowing]; engine + AI paragraph [BR] | AI is not part of the MVP [ML line 17] |
| AI in LifeMode's profile | "Stage 2: LLM events and negotiation" [GF § D3] and differentiation via "AI-driven variety and negotiation" [GF § Cross-dimension insights] | AI is not part of the MVP [ML line 17] |
| Who played Koll på cashen | "Played by the team" [MR § Finance simulations] | Played by Myggsaa [PT § Koll på cashen] |
| Koll på cashen money carry-over | "Unclear" [GF § Executive summary] | Carries over [MR; PT; MP § 4, all from later desk research] |
| Life Finance | Age and live status unknown [GF § D2] | US, adults, live demo, unmaintained since July 2026 [MR § Finance simulations] |
| Taloussankari | Ages about 13-17, mechanics unverified, evidence from 2022 [GF § D1b] | 8th graders, 7 chapters, cash and experience, live [MR § Finance simulations] |
| Money Wise, Infinite Life store availability | Not checked [GF § D3, § Open questions] | Available in the Norwegian stores [MR § Finance simulations] |
| user-research.md in the inputs | "Excluded for now (empty)" [ML line 6] | Now has results, use it [ML line 17] |
| Parent validation | Parents are the main customer group for initial validation [MV § Initial Commercial Validation] | No parent survey in this round [UR § Results] |
