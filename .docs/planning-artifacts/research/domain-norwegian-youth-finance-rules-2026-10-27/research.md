---
title: 'domain research: Norwegian youth finance rules 2026'
type: 'domain'
topic: 'Norwegian youth finance rules for a simulation game (BSU, frikort/tax, minors and credit, credit cards, youth wages and working hours, Lånekassen)'
decision: 'Are the Norwegian rules in LifeMode (ages 15-20, simulated 2026) correct enough to put in a PRD, and which simplifications must the game disclose?'
source: 'native run (headless, lead inline)'
status: complete
preset: 'standard'
validation: 'normal'
created: '2026-10-27'
updated: '2026-10-27'
claims_verified: 13
claims_unverified: 2
claims_overturned: 0
---

# Domain research: Norwegian youth finance rules 2026

**Decision this research serves:** Are the Norwegian rules in LifeMode (ages 15-20, simulated 2026) correct enough to put in a PRD, and which simplifications must the game disclose?

## Executive summary

**Verdict: mostly yes. Most of the game's numbers match official 2026 sources. One rule is wrong in substance: "50% withheld above the frikort limit". Two rules need a scope label: youth minimum wages, and the age at which a player can open a BSU.**

- **Confirmed:** BSU 2026 (10% deduction, NOK 27,500 per year, NOK 300,000 in total) [1][2]. The SSB BSU interest rate of 5.61% for August 2026 [4]. The frikort limit of NOK 100,000 [6]. The Virke/HK youth rates of 136.41, 139.40 and 195.04 [17]. Under-18s cannot take on debt without the statsforvalteren's consent [10][11]. A minimum card payment of 3% or NOK 300 is realistic [14][16].
- **Overturned in substance:** 50% is a *withholding* rate, not a tax. It applies when earnings pass the frikort amount allocated to an employer, or when the employer has no tax card on file [6][7]. Withholding is settled in the annual tax assessment. An 18-year-old earning NOK 110,000 in wages finally pays about **NOK 2,588 (about 2.4%)**, and all of it is trygdeavgift [2][5]. If the game keeps 50% as the final tax, it overstates tax by roughly 20 times.
- **Biggest caveat:** the NOK 136.41/139.40/195.04 rates are tariff minimums (Landsoverenskomsten HK). They bind only employers covered by the agreement. Norway has no general statutory minimum wage [17][18].

## 1. BSU (boligsparing for ungdom)

- **Age:** There is no lower age limit to open a BSU, so a 15-year-old can have one. Skatteetaten advises *against* opening one under 17 without taxable work income. Saving is allowed through the year you turn 33 [3]. A minor cannot dispose of funds alone (vergemålsloven § 9) [10]. In practice, banks have guardians open and sign the account: KLP has both guardians sign electronically, and Jæren Sparebank uses a guardian power-of-attorney form [9] (medium confidence: individual banks' practice).
- **Caps and deduction for 2026:** 10% of the amount deposited, a maximum of NOK 27,500 per year (so a maximum deduction of NOK 2,750), and NOK 300,000 in total. Interest does not count toward the caps. There is no deduction if you own, or part-own, a home on 31 December [1][2][3].
- **Deduction with no tax:** the deduction is a reduction of tax and "cannot exceed what you would have paid in tax" [3]. On frikort, or below the tax threshold, it is **worth NOK 0**. Unused deduction is not carried forward; Skatteetaten does not mention any carry-forward (absence noted, not explicitly confirmed). *Unverified: single primary source.*
- **Interest:** SSB table 11018 (BSU, households) shows 5.48% in January 2026 and 5.61% in July and August 2026, which confirms the game's figure [4]. This is a market average. The top rates listed by a comparison site were about 6.35-6.55% (low-medium confidence) [23].
- **Non-housing use:** a breach of the rules adds back to taxable income the deductions received ("tilleggsskatt equal to the deduction"), limited to the part not used for housing. Furniture, holiday homes and similar uses are not allowed [3]. *Unverified: single primary source.*

## 2. Frikort and tax in 2026

- **Limit:** NOK 100,000 for 2026. Frikort is issued automatically from the year you turn 13 [6][7].
- **What happens above the limit:** if earnings exceed the frikort amount allocated to one employer, that employer must withhold 50% (this applies even when total income for the year is below NOK 100,000). Before an employer receives any tax card, it withholds 50% (sktbl. § 5-5 (1)) [6][7]. An ordinary tax card uses *tabelltrekk* (table withholding) or *prosenttrekk* (percentage withholding) instead [6]. The total tax is the same either way, because the difference is settled in the tax assessment [7].
- **2026 parameters:** personfradrag (personal allowance) NOK 114,540. Minstefradrag (standard deduction) 46%, maximum NOK 95,700. Trinnskatt (bracket tax) step 1 starts at NOK 226,100 at 1.7%. Tax on ordinary income is 22%. Trygdeavgift (national insurance contribution) on wages is 7.6% for ages 17-69 and 5.1% for those under 17. Its lower limit is NOK 99,650, and it can never exceed 25% of the income above that limit [2][5][8].
- **Worked example: 18-year-old, NOK 110,000 in wages, no other income** (lead calculation from [2][5]):
  - Minstefradrag is NOK 50,600, which leaves NOK 59,400 of ordinary income. That is below the personfradrag, so income tax is 0.
  - Trinnskatt is 0.
  - Trygdeavgift is the lower of 7.6% × 110,000 (= 8,360) and 25% × 10,350 (= 2,587.50), so NOK **2,588**.
  - Income tax at 22% only starts at about NOK 212,000 in wages (where 54% of wages exceeds 114,540).
- **Recommendation:** model the final tax as 0 up to NOK 99,650, then trygdeavgift with the 25% phase-in, then 22% above roughly NOK 212k. As an optional realism mechanic, model 50% *withholding* followed by a refund at the "skatteoppgjør" (tax assessment). Suggested disclosure: *"Simplified: tax is calculated on yearly income using 2026 rates. In real life employers may withhold 50% until you get a tax card; the difference is refunded or charged in the tax assessment."*

## 3. Minors and credit

- **Under 18:** a minor cannot perform legal acts or dispose of funds unless the law specially provides otherwise (vergemålsloven §§ 8-9) [10]. From age 15 a minor can sign their own employment contract (§ 10) and controls money earned from their own work (§ 12). That control does not extend to dispositions that need the statsforvalteren's consent [10]. The guardian needs the statsforvalteren's consent to incur debt on the minor's behalf, with an exception for studielån and stipend (§ 40) [11]. **Conclusion:** consumer loans and credit cards for players under 18 should be blocked in the game. This is a legal rule, not just bank policy.
- **Ages 18-19 in practice:** both issuers checked require age 18 or older plus a credit check. Bank Norwegian looks at income and debt [14]. re:member requires "fast inntekt" (steady income) and no payment remarks [15]. Comparison sites say some issuers set their limit at 20, 23 or 25, and that income floors typically range from NOK 120k to 250k (low confidence, affiliate sites) [16].
- **Lending rules** (utlånsforskriften, current text read on Lovdata 2026-10-27, last amended FOR-2024-12-04-2925) [12]:
  - No loan if total debt exceeds 5 times annual income (§ 6).
  - Stress test of +3 percentage points, with a floor of 7%. Credit lines are assessed as if fully used (§ 5).
  - Consumer loans must be repaid monthly within 5 years (§ 13).
  - A 5% quarterly flexibility quota (§ 15).
  - Credit cards are exempt when total card limits are NOK 30,000 or less (§ 3; medium confidence, from the fetch summary).
- **Creditworthiness and gjeldsregister:** finansavtaleloven § 5-2 requires a thorough creditworthiness assessment, using a debt-information company where necessary, and § 5-4 allows credit only if repayment is probable [13] (medium confidence, from a search snippet).

## 4. Credit-card rules

- **Minimum payment:** Bank Norwegian charges 3.5% of the balance with a NOK 300 floor (a reduced option of 1.8% is available) [14]. TF Bank's Credits Blue charges 3.30% with a NOK 300 floor [16]. The game's max(3%, NOK 300) is **realistic but slightly low**. 3.5% would match the market leader.
- **Interest-free period and rates:** up to 45 interest-free days at both Bank Norwegian and re:member. Nominal interest is 18.5-25.2%, and effective interest is 20-30% [14][15].
- **Regulatory nuance:** for credit lines, the monthly minimum must be set so that the used credit is repaid within 5 years on a serial basis [12]. See the open questions.

## 5. Youth wages and working hours

- **Wages:** Landsoverenskomsten HK (Virke/HK) minimum rates from 1 April 2026 are NOK 136.41/h under 16, NOK 139.40/h under 18, and NOK 195.04/h for lønnstrinn 1 [17]. **Confirmed.** These rates bind only employers covered by the agreement. Norway has no general statutory minimum wage. The sectors with generalised (legally binding) minimum wages do not include retail. Hospitality has its own youth rates (from 15 June 2025): under 17 NOK 142.58, age 17 NOK 152.08, age 18 NOK 166.34 [18].
- **Working hours** (arbeidsmiljøloven § 11-2) [19]:
  - Under 15, or still in compulsory schooling (*skolepliktig*): at most **2 h per day and 12 h per week** on school days and in school weeks, and **7 h per day and 35 h per week** on days and weeks without school.
  - Ages 15-18 and no longer in compulsory schooling: at most **8 h per day and 40 h per week**.
- **Night work** (§ 11-3): no work between 20:00 and 06:00 for those under 15 or still in compulsory schooling. For ages 15-18, a rest period of at least 8 hours that includes 23:00-06:00, and work between 21:00 and 23:00 only when necessary [19].
- **What this means for the game:** the dividing line is compulsory schooling (*skoleplikt*), not age 16. A 15-year-old in 10th grade gets the 2 h/12 h limits. A 16- or 17-year-old in upper secondary school gets 8 h/40 h.

## 6. Lånekassen (note for a future "education" step)

- Basislån for 2026-27 is NOK 15,488 per month for full-time study, or NOK 170,368 over 11 months [20].
- Up to 40% can be converted to stipend if the student does not live with their parents, passes their exams, and stays under the income and wealth limits. The full-year income limit for 2026 is NOK 234,821. The loan is interest-free while studying full-time, and the first bill comes about 7 months after the last payment [21].
- Students under 21 in upper secondary school, and apprentices under 21, have separate schemes [22].
- A future education step needs these modelled: the living-with-parents flag, the income limit, and the conversion rule.

## Cross-dimension insights

- **Frikort and BSU interact:** most players aged 15-18 will be on frikort, so BSU gives them **no tax benefit** in those years. The game should show "BSU deduction: NOK 0 (no tax to reduce)" instead of a phantom 10% gain. That matches Skatteetaten's advice not to open a BSU under 17 without taxable income [3][6].
- **Hours, wages and tax combine:** a student in compulsory schooling working the maximum 12 h per week at NOK 136.41 earns about NOK 85k per year. That is under the frikort limit, so tax is realistically 0 for younger players [17][19][6] (lead calculation).
- **Credit at 18:** players who just turned 18 hit two barriers. Issuers require steady income [15], and the 5× debt-to-income rule applies [12]. A player with NOK 100k income could at most hold NOK 500k of total debt (lead calculation).

## Recommendations (feed PRD constraints and domain vocabulary)

1. **PRD tax rule (high confidence):** replace "50% above frikort" with the 2026 year-end calculation in §2. Keep 50% only as withholding plus a refund, if you want that mechanic.
2. **PRD BSU (high confidence):** allow a BSU from age 15 with a "guardian co-signs" flag. Set the deduction to min(10% × deposit, tax payable). A breach adds the deductions back as tax.
3. **PRD credit (high confidence):** under 18, credit is blocked by law. At 18-19, approval requires income, debt ≤ 5× income, and a 5-year consumer-loan term. Optionally raise the card minimum payment to 3.5%.
4. **PRD wages and hours (high confidence):** label wages as "tariff minimum (Virke/HK retail), not a legal minimum". Key the hour caps to compulsory-schooling status, not to age.
5. **Required disclosures:** simplified annual tax (no tabelltrekk); tariff rather than statutory wages; BSU interest is the SSB August 2026 market average; bank approval rules are simplified; all rates are 2026 values.

## Open questions

- Is a pure "3% of balance" minimum compatible with utlånsforskriften § 13 (repayment within 5 years on a serial basis)? The NOK 300 floor makes the repayment finite. To settle it, read Finanstilsynet's rundskriv on utlånsforskriften.
- Does the § 3 exemption for cards with total limits of NOK 30,000 or less apply in full? A direct read of § 3 is needed.
- The exact definition of "under 17" for the 5.1% trygdeavgift rate (age at the end of the income year) needs a direct read of ftrl. § 23-3.
- The hospitality youth rates shown date from June 2025. Have they been updated for 2026? Check Arbeidstilsynet.
- What income floors apply for 18-19-year-olds at the large banks (DNB, SpareBank 1)? Their pages did not render. Product pages or customer service would settle it.

## Source appendix

| [n] | claim/finding it supports | publisher | pub date | accessed | confidence |
|---|---|---|---|---|---|
| [1] | BSU 2026: 10%, 27,500, 300,000, ownership rule | [Skatteetaten – satser BSU 2026](https://www.skatteetaten.no/satser/fradrag-for-boligsparing-for-ungdom-bsu/?year=2026) | 2026 | 2026-10-27 | high |
| [2] | 2026 tax parameters; BSU confirmation | [Finansdepartementet – Skattesatser 2026](https://www.regjeringen.no/no/tema/okonomi-og-budsjett/skatter-og-avgifter/skattesatser-2026/id3121978/) | 2026 | 2026-10-27 | high |
| [3] | BSU age, caps, deduction cap, breach | [Skatteetaten – BSU](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/bank-og-lan/bsu/) | 2025 (current page) | 2026-10-27 | high |
| [4] | BSU rate 5.61% Aug 2026 | [SSB – table 11018 (API)](https://data.ssb.no/api/v0/no/table/11018) | 2026-08 data | 2026-10-27 | high |
| [5] | Trygdeavgift 2026 rates, 25% rule | [Skatteetaten – trygdeavgift 2026](https://www.skatteetaten.no/satser/trygdeavgift/?year=2026) | 2026 | 2026-10-27 | high |
| [23] | Top BSU rates ~6.35-6.55% | [Bytt.no – beste BSU](https://bytt.no/bank/sparekonto/beste-bsu) | 2026-08 | 2026-10-27 | low-medium |
| [6] | Frikort 2026 = 100,000; tabelltrekk/prosenttrekk; 50% without card | [Skatteetaten – Forskuddsutskrivingen 2026](https://www.skatteetaten.no/en/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/) | 2025/2026 | 2026-10-27 | high |
| [7] | 50% above employer allocation; total tax same | [Skatteetaten – Frikort](https://www.skatteetaten.no/person/skatt/skattekort/frikort/) | current | 2026-10-27 | high |
| [8] | Minstefradrag 2026 | [Skatteetaten – minstefradrag 2026](https://www.skatteetaten.no/satser/minstefradrag/?year=2026) | 2026 | 2026-10-27 | high |
| [9] | Guardians open BSU for under-18s | [KLP – BSU](https://www.klp.no/bank/sparing-pa-konto/bsu); [Jæren Sparebank – fullmakt](https://jaerensparebank.no/-/media/banker/jaerensparebank/dokumenter/skjema/oppdatert_Fullmakt-fra-foresatt-el-verge.pdf) | undated | 2026-10-27 | medium |
| [10] | Vergemålsloven §§ 8-10, 12 | [Lovdata – vergemålsloven](https://lovdata.no/dokument/NL/lov/2010-03-26-9) | in force | 2026-10-27 | high |
| [11] | Vergemålsloven § 40 debt needs consent | [Lovdata – vergemålsloven § 40](https://lovdata.no/lov/2010-03-26-9/§40) | in force | 2026-10-27 | high |
| [12] | Utlånsforskriften §§ 3, 5, 6, 13, 15 | [Lovdata – utlånsforskriften](https://lovdata.no/dokument/SF/forskrift/2020-12-09-2648) | amended 2024-12 | 2026-10-27 | high |
| [13] | Finansavtaleloven § 5-2, § 5-4 | [Lovdata – finansavtaleloven kap. 5](https://lovdata.no/dokument/LTI/lov/2020-12-18-146/KAPITTEL_5-1) | 2020 | 2026-10-27 | medium |
| [14] | Bank Norwegian: 18+, 3.5%/300, 45 days, 21.99% | [Bank Norwegian – kredittkort](https://www.banknorwegian.no/kredittkort/) | current | 2026-10-27 | high |
| [15] | re:member: 18+, steady income, 45 days | [re:member – kredittkort](https://www.remember.no/kredittkort) | current | 2026-10-27 | high |
| [16] | TF Bank 3.3%/300; issuer age/income ranges | [kredittkort360 – Credits Blue](https://kredittkort360.com/kort/credits-blue/); [kredittkortlisten](https://www.kredittkortlisten.no/kredittkort-alle-kan-fa/) | undated | 2026-10-27 | low-medium |
| [17] | Virke/HK 2026 youth minimum rates | [Virke – Landsoverenskomsten HK](https://www.virke.no/tariff-og-lonn/finn-tariffavtale/landsoverenskomsten-hk/) | 2026-06 | 2026-10-27 | high |
| [18] | No general statutory minimum wage; sector list; hospitality youth rates | [Arbeidstilsynet – Minimum wage](https://www.arbeidstilsynet.no/en/pay-and-engagement-of-employees/pay-and-minimum-rates-of-pay/minimum-wage/) | current (2026 changes noted) | 2026-10-27 | high |
| [19] | Aml §§ 11-2, 11-3 working hours | [Lovdata – arbeidsmiljøloven kap. 11](https://lovdata.no/lov/2005-06-17-62/§11-3) | in force | 2026-10-27 | high |
| [20] | Basislån 2026-27 | [Lånekassen – Studere til høsten 2026](https://lanekassen.no/en-US/presse-og-samfunnskontakt/nyheter/studere-til-hosten-2026/) | 2026 | 2026-10-27 | high |
| [21] | 40% conversion conditions, income limit | [Lånekassen – høyere utdanning](https://lanekassen.no/nb-NO/stipend-og-lan/hoyere-utdanning/) | 2026 | 2026-10-27 | high |
| [22] | Under-21 vgs / apprentice grants | [Lånekassen – upper secondary](https://lanekassen.no/en-US/grants-and-loans/norway/upper-secondary-school/upper-secondary-school/) | 2026 | 2026-10-27 | medium |

## Staleness map

Computed with `recon_kit.py staleness` (windows: regulatory 12 mo, quantitative 12 mo, pricing 6 mo):

| claim | re-check by |
|---|---|
| Utlånsforskriften limits | flagged stale by the amendment date (2024-12). The current text was read on 2026-10-27; re-check whenever Finansdepartementet amends it |
| 2026 tax parameters, BSU caps, frikort limit, aml hours | 2027-01-01 (new budget year) |
| Card minimum payment and interest | 2027-04-01 |
| Virke/HK rates; Lånekassen 2026-27 | 2027-06-01 |
| SSB BSU rate | 2027-08-01 (can be refreshed monthly through the API) |

Earliest re-check: **2027-01-01**, when all 2026 tax and BSU figures roll over. Run a Refresh then if the game simulates 2027.
