# Extract: domain facts for the LifeMode PRD

Extracted 2026-11-03 from the sources below. Nothing here is new research. The memlog is authoritative where sources differ.

**Source codes** (research files are under `.docs/planning-artifacts/research/`; [n] is that file's own source number)

| Code | File |
|---|---|
| NOR | `domain-norwegian-youth-finance-rules-2026-10-27/research.md` |
| LK20 | `domain-lk20-personal-finance-curriculum-2026-10-27/research.md` |
| LLM | `technical-free-tier-llm-provider-terms-for-minors-2026-10-27/research.md` |
| REM | `remaining-pre-prd-research-2026-10-31/research.md` |
| MEM | `prds/prd-IBE160-G13-2026-10-22/.memlog.md` (cited by line) |
| #18, #24 | GitHub issues, read 2026-11-03 (#24 includes its 3 comments) |

**Flags**

- **YEARLY:** the value changes by year or agreement period. See section 7 for re-check dates.
- **UNCERTAIN:** the research marked it unverified, low or medium confidence, disputed or inferred.
- **CALC:** the researcher's own arithmetic or inference, not a figure from a source.

"Conf." is the confidence the research gave that source. The memlog records no decision on any rule value in sections 1-5, so these are research findings, not team decisions.

## 1. Wages and working hours

### Wages

Norway has no general statutory minimum wage. The sectors with generalised minimum wages do not include retail (NOR §5 [18]; high).

| Rate set | Figures (NOK/h) | Applies from | Conf. | Source | Flags |
|---|---|---|---|---|---|
| Landsoverenskomsten HK (Virke/HK, retail), tariff minimum | Under 16: 136.41. Under 18: 139.40. Lønnstrinn 1: 195.04 | 1 Apr 2026 | high | NOR §5 [17] | YEARLY. Binds only employers covered by the agreement |
| Hospitality, legally binding (allmenngjort) | Under 17: 142.58. Age 17: 152.08. Age 18: 166.34. Adult starting wage: 204.79 | 15 Jun 2025, still shown in 2026 | medium | REM C4 [41]; NOR §5 [18] | YEARLY. UNCERTAIN: no 2026 Tariffnemnda decision found |
| Hospitality, Virke-Fellesforbundet 2026 tariff | 37.5-hour week: under 17: 153.08, age 17: 162.58, age 18: 176.84. 35.5-hour week: 161.53 / 171.55 / 186.60 | 1 Jun 2026 | medium | REM C4 [42][43] | YEARLY. UNCERTAIN: agreement approved 16 Jun 2026 [43], but the figures come from a proposal marked "ikke endelig godkjent" [42] |

The NHO Reiseliv Riksavtale 2026 rates were not verified (REM C4 [44], news snippets only).

### Working hours (arbeidsmiljøloven §§ 11-2, 11-3; in force, read 2026-10-27; conf. high)

| Group | Daily and weekly limit | Night rule | Source |
|---|---|---|---|
| Under 15, or still in compulsory schooling (*skolepliktig*) | School days and weeks: 2 h/day, 12 h/week. Days and weeks without school: 7 h/day, 35 h/week | No work 20:00-06:00 | NOR §5 [19] |
| Ages 15-18, no longer in compulsory schooling | 8 h/day, 40 h/week | Rest of at least 8 h including 23:00-06:00. Work 21:00-23:00 only when necessary | NOR §5 [19] |

- The dividing line is *skoleplikt*, not age 16. A 15-year-old in 10th grade gets 2 h/12 h. A 16- or 17-year-old in upper secondary school gets 8 h/40 h (NOR §5).
- From age 15 a minor can sign their own employment contract (vergemålsloven § 10) and controls money earned from their own work (§ 12), except dispositions needing the statsforvalteren's consent (NOR §3 [10]; high).
- **Gap:** the research gives no working-hour limits for ages 18-20.

## 2. Tax

| Item | Figure | Year | Conf. | Source | Flags |
|---|---|---|---|---|---|
| Frikort limit | NOK 100,000; issued automatically from the year you turn 13 | 2026 | high | NOR §2 [6][7] | YEARLY |
| 50% | A *withholding* rate, not a tax. Applies when earnings exceed the frikort amount allocated to one employer (even if yearly income is under 100,000), or before the employer has a tax card (sktbl. § 5-5 (1)). Settled in the tax assessment; total tax is the same | Current | high | NOR Exec summary, §2 [6][7] | The research overturned "50% withheld above the frikort limit" as a final tax |
| Ordinary tax card | *Tabelltrekk* or *prosenttrekk* instead of 50% | Current | high | NOR §2 [6] | |
| Personfradrag | NOK 114,540 | 2026 | high | NOR §2 [2] | YEARLY |
| Minstefradrag | 46%, maximum NOK 95,700 | 2026 | high | NOR §2 [8] | YEARLY |
| Trinnskatt step 1 | Starts at NOK 226,100, 1.7% (higher steps are not in the research) | 2026 | high | NOR §2 [2] | YEARLY |
| Tax on ordinary income | 22% | 2026 | high | NOR §2 [2] | YEARLY |
| Trygdeavgift on wages | 7.6% for ages 17-69; 5.1% for those under 17 | 2026 | high | NOR §2 [5]; REM C3 [40] | YEARLY |
| Trygdeavgift floor and cap | Lower limit NOK 99,650; can never exceed 25% of income above that limit | 2026 | high | NOR §2 [5]; REM C3 [40] | YEARLY |
| "Under 17" definition | The years before the calendar year you turn 17. In the year you turn 17, the whole year is at 7.6%, including income before the birthday | Current | high | REM C3 [39][40] | Closes the open question in NOR |
| Worked example: 18-year-old, NOK 110,000 wages | Minstefradrag 50,600, ordinary income 59,400, income tax 0, trinnskatt 0, trygdeavgift NOK 2,588 (about 2.4%) | 2026 | n/a | NOR Exec summary, §2 | CALC, YEARLY |
| Where 22% starts | About NOK 212,000 in wages | 2026 | n/a | NOR §2 | CALC, YEARLY |
| Max 12 h/week at 136.41 | About NOK 85,000 per year, under the frikort limit | 2026 | n/a | NOR Cross-dimension insights | CALC, YEARLY |

The research states both the NOK 100,000 frikort limit and the NOK 99,650 trygdeavgift floor without addressing the NOK 350 between them (NOR §2).

## 3. BSU

| Item | Figure or rule | Year | Conf. | Source | Flags |
|---|---|---|---|---|---|
| Age | No lower age limit. Saving allowed through the year you turn 33. Skatteetaten advises against opening under 17 without taxable work income | Current | high | NOR §1 [3] | |
| Minors | Cannot dispose of funds alone (vergemålsloven § 9). In practice guardians open and sign | Current | high for the law; medium for bank practice | NOR §1 [9][10] | UNCERTAIN: bank practice from two banks |
| Deduction | 10% of the amount deposited | 2026 | high | NOR §1 [1][2][3] | YEARLY |
| Yearly cap | NOK 27,500 deposited, so at most NOK 2,750 deduction | 2026 | high | NOR §1 [1][2][3] | YEARLY |
| Total cap | NOK 300,000; interest does not count toward the caps | 2026 | high | NOR §1 [1][2][3] | YEARLY |
| Home ownership | No deduction if you own or part-own a home on 31 December | 2026 | high | NOR §1 [1] | |
| No tax to reduce | Deduction "cannot exceed what you would have paid in tax", so it is worth NOK 0 on frikort or below the tax threshold | Current | high source | NOR §1 [3]; Cross-dimension insights | UNCERTAIN: marked unverified, single primary source |
| Carry-forward | Skatteetaten does not mention one | Current | n/a | NOR §1 [3] | UNCERTAIN: absence noted, not confirmed |
| Non-housing use | Deductions received are added back to taxable income ("tilleggsskatt equal to the deduction"), limited to the part not used for housing. Furniture, holiday homes and similar are not allowed | Current | high source | NOR §1 [3] | UNCERTAIN: marked unverified, single primary source |
| Interest | SSB table 11018: 5.48% Jan 2026; 5.61% Jul and Aug 2026 (market average) | 2026 | high | NOR §1 [4] | YEARLY, refreshable monthly |
| Top market rates | About 6.35-6.55% | Aug 2026 | low-medium | NOR §1 [23] | UNCERTAIN, YEARLY |

LK20 calls the BSU figures "unverified" and rates Skatteetaten's BSU page medium (LK20 Recommendations, [17]). NOR confirms the caps from three sources rated high. Its two "unverified" marks cover only the no-tax and breach rules.

## 4. Credit and loans by age

### Under 18

- A minor cannot perform legal acts or dispose of funds unless the law specially provides otherwise (vergemålsloven §§ 8-9; NOR §3 [10]; high).
- A guardian needs the statsforvalteren's consent to incur debt for a minor, except for studielån and stipend (§ 40; NOR §3 [11]; high).
- The research concludes that this is a legal rule, not only bank policy (NOR §3).

### Age 18 and up: issuer and bank terms

| Provider | Terms | Conf. | Source | Flags |
|---|---|---|---|---|
| Bank Norwegian card | 18+, credit check on income and debt. Minimum 3.5% of balance, floor NOK 300 (reduced option 1.8%). Up to 45 interest-free days. 21.99% interest | high | NOR §3, §4, appendix [14] | YEARLY |
| re:member card | 18+, "fast inntekt", no payment remarks. Up to 45 interest-free days | high | NOR §3, §4 [15] | YEARLY |
| DNB Ung Mastercard | "18 og frem til du fyller 28 år". Nominal 18.60%, effective 20.27% on NOK 5,000. No published income floor | medium | REM C5 [45][47] | YEARLY |
| DNB Mastercard | Minimum 3.5% of balance, floor NOK 200 | medium | REM C1, C5 [46] | YEARLY |
| DNB consumer loan | Income and debt fetched from Altinn. No published age or income floor | medium | REM C5 [47][48] | UNCERTAIN |
| SpareBank 1 consumer loan | "Minst 20 år gammel", "trygg og stabil økonomi", no payment remarks, so not available at 18-19 | medium | REM Verdict, C5 [49] | |
| TF Bank Credits Blue | 3.30%, floor NOK 300 | low-medium | NOR §4 [16] | UNCERTAIN |
| Market range (checked issuers) | Nominal 18.5-25.2%; effective 20-30% | high | NOR §4 [14][15] | YEARLY |

Unofficial income floors, all from aggregators and all low confidence:

- Some issuers set age limits of 20, 23 or 25, with floors of NOK 120k-250k (NOR §3 [16]).
- DNB Ung NOK 25,000/year; DNB Mastercard NOK 50,000/year (REM C5 [50]).
- SpareBank 1 about NOK 100,000/year for a NOK 5,000 limit; Ung Mastercard ages 18-34 with fixed income (REM C5 [51][52]).

The research does not reconcile these ranges. The SpareBank 1 card pages returned 404, and the bank pages that loaded do not settle its card floor or DNB's loan age limit (REM Still open).

### Lending rules (utlånsforskriften, read on Lovdata 2026-10-27, last amended FOR-2024-12-04-2925; conf. high)

| Rule | Content | Source |
|---|---|---|
| § 6 | No loan if total debt exceeds 5 times annual income | NOR §3 [12] |
| § 5 | Stress test of +3 percentage points, floor 7%. Credit lines assessed as if fully used | NOR §3 [12] |
| § 13 | Consumer loans repaid monthly within 5 years. Credit-line minimum is calculated each month on credit used and must repay within 5 years as a serial loan | NOR §3, §4 [12]; REM C1 [35] |
| § 15 | 5% quarterly flexibility quota | NOR §3 [12] |
| § 3 | The whole regulation does not apply if the customer's combined card limits will not exceed NOK 30,000. A second card can push the total over. The threshold was NOK 25,000 under the 2022 rundskriv | REM C2 [35][36] (high; supersedes the medium rating in NOR §3) |
| Finansavtaleloven §§ 5-2, 5-4 | Thorough creditworthiness assessment; credit only if repayment is probable. Applies regardless of the § 3 exemption | NOR §3 [13] (medium); REM C2 [36] |

### Card minimum payment

- NOR §4 calls max(3%, NOK 300) "realistic but slightly low". REM C1 goes further.
- REM C1 (medium; legal reading partly inference, CALC): balance/60 is about 1.67% principal per month. At about 22% nominal interest (about 1.83% per month), that totals about 3.5%. So 3% leaves about 1.17% principal and fails the rolling test unless the rate is about 16% or lower.
- Simulated payoff at 21.99% on NOK 20,000: 3%/300 takes 109 months; 3.5%/300 takes 90 months (CALC). Neither clears in 60 months literally.
- UNCERTAIN: no Finanstilsynet text gives the formula. Rundskriv 6/2022 was replaced by the veiledning of 20 Dec 2024, which has none (REM C1, Still open [36]).
- REM C1 says a first card for ages 18-20 will typically have a limit of NOK 5,000-30,000, with no source cited for that range (UNCERTAIN).

## 5. Education (Lånekassen)

NOR §6 labels this a note for a future "education" step. The memlog has no decision on education content.

| Item | Figure | Year | Conf. | Source | Flags |
|---|---|---|---|---|---|
| Basislån, full-time study | NOK 15,488/month; NOK 170,368 over 11 months | 2026-27 | high | NOR §6 [20] | YEARLY |
| Conversion to stipend | Up to 40%, if the student does not live with parents, passes exams, and stays under the income and wealth limits | 2026 | high | NOR §6 [21] | YEARLY |
| Income limit, full year | NOK 234,821 | 2026 | high | NOR §6 [21] | YEARLY |
| Loan terms | Interest-free during full-time study; first bill about 7 months after the last payment | 2026 | high | NOR §6 [21] | YEARLY |
| Upper secondary under 21; apprentices under 21 | Separate schemes; no figures in the research | 2026 | medium | NOR §6 [22] | UNCERTAIN |

## 6. Does the game have to state that its rules are simplified?

- **Research position:** yes, listed as "Required disclosures" under the recommendations (NOR Recommendations item 5). The research question itself asks "which simplifications must the game disclose?".
- **Status:** this is the research's recommendation. The research cites no law or rule requiring a disclosure, and the memlog records no decision.
- **Items listed:**
  - simplified annual tax (no tabelltrekk)
  - tariff rather than statutory wages
  - BSU interest is the SSB August 2026 market average
  - bank approval rules are simplified
  - all rates are 2026 values
- **Suggested tax wording in the research** (NOR §2): *"Simplified: tax is calculated on yearly income using 2026 rates. In real life employers may withhold 50% until you get a tax card; the difference is refunded or charged in the tax assessment."*
- **Scope labels:** the research says wages and the BSU opening age need a scope label (NOR Exec summary). It also proposes showing "BSU deduction: NOK 0 (no tax to reduce)" (NOR Cross-dimension insights).

## 7. Figures that change by year: research's re-check dates

| Claim | Re-check by | Source |
|---|---|---|
| 2026 tax parameters, BSU caps, frikort limit, aml hours | 2027-01-01 (LK20 lists frikort and BSU amounts as 2027-10-01) | NOR Staleness map; LK20 Staleness map |
| Card minimum payment and interest | 2027-04-01 | NOR Staleness map |
| Virke/HK rates; Lånekassen 2026-27 | 2027-06-01 | NOR Staleness map |
| SSB BSU rate | 2027-08-01, refreshable monthly | NOR Staleness map |
| Utlånsforskriften limits | Whenever Finansdepartementet amends it | NOR Staleness map |
| SAK01-01, MAT05-04 still current | Overdue | LK20 Staleness map |
| SAF01-05, MAT01-06, MAT09-02 | 2027-05-01 | LK20 Staleness map |

All figures in sections 1-5 are point-in-time values. The research gives no figures for later years.

## 8. LK20 curriculum aims

Aims are quoted in the official nynorsk text, as in the research (LK20 D1). Each starts with "Mål for opplæringa er at eleven skal kunne".

| Subject and code | Level | Aim | Conf. | Source |
|---|---|---|---|---|
| Samfunnsfag SAF01-05 (from 01.08.2026) | etter 10. trinn | "vurdere korleis arbeid, inntekt og forbruk kan påverke personleg økonomi, levestandard og livskvalitet" | high | LK20 D1 [1][8] |
| SAF01-05 | etter 10. trinn | "beskrive trekk ved det politiske systemet og velferdssamfunnet i Noreg i dag og reflektere over sentrale utfordringar" (the only indirect link to tax) | high | LK20 D1 [1] |
| SAF01-05 | earlier trinn | "reflektere over korleis kommersiell påverknad kan verke inn på forbruk, personleg økonomi og sjølvbilete" | medium (trinn not re-checked) | LK20 D1 [8] |
| Matematikk MAT01-06 (from 01.08.2026) | etter 10. trinn | "hente ut og tolke relevant informasjon og reflektere over moglege konsekvensar ved kjøp og sal, renter på sparing, lån og kredittkjøp" | high | LK20 D1 [2] |
| MAT01-06 | etter 10. trinn | "planleggje, utføre og presentere eit utforskande arbeid knytt til personleg økonomi" | high | LK20 D1 [2] |
| MAT01-06 | etter 10. trinn | "utforske og forklare samanhengen mellom konstant prosentvis endring, vekstfaktor og eksponentialfunksjonar" | high | LK20 D1 [2] |
| Samfunnskunnskap SAK01-01 (from 01.08.2020) | VG1/VG2 | "drøfte korleis personleg økonomi, kommersiell påverknad og forbruk påverkar enkeltpersonar, grupper og samfunnet" | medium | LK20 D1 [4] |
| SAK01-01 | numeracy text | "Elevane må òg kunne rekne for å forvalte pengebruk og få oversikt over personleg økonomi." | medium | LK20 D1 [4] |
| Matematikk MAT08-01, 1P-Y (all yrkesfag) | VG1 | "vurdere val knytte til personleg økonomi og reflektere over konsekvensar av å ta opp lån og å bruke kredittkort" | high | LK20 D1 [5] |
| MAT08-01, 1P-Y | VG1 | "lese, bruke og lage rekneark i arbeidet med budsjett, anbod og kostnadsberekning knytt til [programområde]" | high | LK20 D1 [5] |
| Matematikk 2P MAT05-04 (from 01.08.2021) | VG2 | "vurdere val knytte til personleg økonomi og reflektere over konsekvensar av å ta opp lån og å bruke kredittkort" | high | LK20 D1 [7] |
| 2P MAT05-04 | VG2 | "utforske og forklare samanhengar mellom prisindeks, kroneverdi, reallønn, nominell lønn og brutto- og nettoinntekt" | high | LK20 D1 [7] |
| Tverrfagleg tema *folkehelse og livsmeistring* | across subjects | MAT01-06: "…om å gi elevane kompetanse i problemløysing, i statistikk og i personleg økonomi". 1P and 2P: "…om å gi elevane kompetanse i personleg økonomi". SAF01-05: "…handtere utfordringar knytte til seksualitet, personleg økonomi, rus, utanforskap og digital samhandling" | high | LK20 D1 [2][5][7][8] |

**No personal-finance aim**

- 1P, MAT08-01 (academic VG1): no loan, credit or budget aim. Closest is "bruke prosent, prosentpoeng, promille og vekstfaktor i utrekningar og presentere og grunngi løysingar" (LK20 D1 [19][5]; high).
- 1T, MAT09-02 (from 01.08.2026; replaces MAT09-01): none found by keyword search (LK20 D1 [6]; medium).

**Codes and limits**

- SAF01-04 and MAT01-05 expired 31.07.2026, replaced by SAF01-05 and MAT01-06 (LK20 Exec summary [3][21]; #18).
- No core-subject aim names tax, frikort, BSU or consumer rights. Those links are indirect only (LK20 Exec summary).
- The mechanism-to-aim mapping in LK20 D3 is the researcher's own derivation, not a finding. Fit ratings there: wages and frikort medium; interest high but BSU as such low; budget high; loans and cards high; crisis months medium.
- UNCERTAIN: whether SAK01-01 and MAT05-04 are still current is overdue for checking. 1P, 2P and SAK may be revised from 2027 (LK20 Open questions, Staleness map).
- Five before/after quiz questions in LK20 D4 are proposals derived from the aims, not research findings, and need teacher review (LK20 D4; #18). The memlog records no decision on a quiz.

## 9. AI provider findings: OUT OF MVP SCOPE

- Out of MVP scope (MEM line 17); these findings concern stage 2 only, and the memlog records no provider decision.
- Gemini is ruled out: its terms bar services likely accessed by under-18s on all tiers, and EEA apps need Paid Services (LLM Exec summary, D1 [1]; high).
- Groq: 18+ account holder, compliance for minors on the customer (§6.3), no training on inputs/outputs; free gpt-oss limits 30 RPM, 1K RPD, 8K TPM, 200K TPD (about 285 events/day per model, CALC) (LLM D1, D2 [9]; REM B [27][29]). UNCERTAIN: DPA coverage disputed.
- Cloudflare Workers AI: no minors clause found, no training or retention, 10,000 neurons/day with errors over the limit (about 185-1,100 events/day by model, CALC) (LLM D1, D2 [21][24]; REM B [31][32]). UNCERTAIN: AUP medium; privacy-policy under-18 wording low.
- No free tier found has a confirmed DPA plus EU-only processing; the research names sending no personal data to the LLM as the main protection. Limits go stale from 2026-11-20 (LLM Exec summary, Staleness map).

## 10. Privacy points deferred to issue #24: NOT BLOCKING THE PRD

- Not blocking the MVP or PRD; all to be checked before go-live, and the issue stays open as a reminder (#24 comment 2; MEM line 15).
- Who is behandlingsansvarlig (the group or the høgskole), and which behandlingsgrunnlag applies; berettiget interesse is a candidate, and children's interests weigh heavily (#24 comment 1).
- Whether to confirm generated usernames, which is stricter than the decision that allows free text in the username (#24 comment 1; not a team decision, MEM line 15).
- How long inactive games are stored and how they are deleted; the architecture still requires an account-deletion test. Also what 18-20-year-old playtesters are told, and how the untested 15-17 group is handled (#24 body, comment 1).
- The issue's points on generated and lost codes no longer apply: the player creates a password, Supabase Auth stores it, and there is no reset in the MVP (#24 comment 3; MEM line 15).

## 11. Research proposals for engine rules (not team decisions)

| Proposal in the research | Source |
|---|---|
| Final tax: 0 up to NOK 99,650, then trygdeavgift with the 25% phase-in, then 22% above roughly NOK 212k. 50% withholding plus refund only as an optional mechanic | NOR §2, Recommendations 1 |
| BSU from age 15 with a "guardian co-signs" flag; deduction = min(10% × deposit, tax payable); a breach adds the deductions back as tax | NOR Recommendations 2 |
| Credit blocked under 18. At 18-19, approval requires income, debt ≤ 5× income and a 5-year consumer-loan term | NOR Recommendations 3 |
| Label wages "tariff minimum (Virke/HK retail), not a legal minimum"; key hour caps to compulsory-schooling status | NOR Recommendations 4 |
| Card minimum 3.5% of balance, floor NOK 200-300; card limits ≤ NOK 30,000 for ages 18-20, with a creditworthiness check still required; small first limits of 5,000-10,000 | REM C1, C5, Consequences 3 |
| Consumer loans age-gated: "only specialist lenders at 18-19, at higher interest", or from age 20 | REM C5 |
| Trygdeavgift: `low_rate = (income_year - birth_year) < 17` | REM C3 |
| Hospitality youth wages from the 2025 allmenngjort table; optionally the 2026 tariff rates as a "tariff employer" wage | REM C4 |
| Take frikort and BSU figures from Skatteetaten and re-check every tax year | LK20 Recommendations |

## 12. Conflicts with the memlog

| Source statement | Memlog | Status |
|---|---|---|
| #24 body: "lagring, ikke identitet" with a gjenopptakskode | MEM line 15: username login, player-created password | Superseded by #24 comments 1 and 3 |
| REM Consequences 1 and 4: differentiation wording with "an AI narrates", and AI non-functional requirements for the PRD | MEM line 17: AI is not part of the MVP | Direct conflict; memlog governs |
| REM Consequences 2: example meters include housing quality, with a failure or penalty state at zero | MEM line 16: wellbeing = stress, free time, social life; four endings; going below zero only starts a crisis month | Conflict; memlog governs |
| #24 comment 1: "når samtykke ikke bør være grunnlaget", stated as a premise | MEM line 15: consent not used as legal basis is a recommendation, not a team decision | Different status |
| REM C3 engine rule uses `birth_year` | MEM line 15: no real age collected | Tension; the source does not say whose birth year |
| NOR frame: "simulated 2026", all rates 2026 values | MEM line 16: 60 months | Tension; the research gives no figures past 2026-27 |
| LK20: positioning for school use; 10-15 minute session with a quiz | MEM line 15: school mode possibly later. MEM line 14: pause and resume journey | Tension; the memlog has no decision on school positioning or session length |
