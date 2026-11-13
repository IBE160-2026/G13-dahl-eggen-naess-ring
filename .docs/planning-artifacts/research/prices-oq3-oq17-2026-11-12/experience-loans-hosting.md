# Prices: big experience, consumer-loan interest, hosting costs

Research date: 2026-11-12. Currency conversions use Norges Bank mid rates of 2026-11-11 (API `data.norges-bank.no`, EXR series): **EUR 10.6145, USD 9.5394, AUD 6.5433, DKK 1.4199 NOK** (100 DKK = 141.99 NOK).

## Summary

| Item | Proposed value | Source | Date | Confidence |
|---|---|---|---|---|
| Big experience, game default | **NOK 60,000**, "8 weeks of Interrail through Europe". The four options below land between NOK 51k and 63k, so the label can change without changing the price | Breakdown in §1 (Interrail pass from DSB, hostel/day budgets from Hostelz, Norges Bank FX) | Seen 2026-11-12 | Medium |
| Option A: Interrail, 8 weeks | ~NOK 57,000 (6 weeks: ~NOK 46,000) | DSB Interrail price table; Hostelz | Seen 2026-11-12 | Medium |
| Option B: Southeast Asia backpacking, 8 weeks | ~NOK 51,000 | Momondo/Finnair fares; backpacker budgets (Hostelz and others); Bærum vaccine price list (valid from 2026-01-01) | Seen 2026-11-12 | Medium |
| Option C: Australia, 8 weeks (eVisitor) | ~NOK 63,000 (+NOK 5,500 on a Working Holiday visa) | Thai Airways/Finnair fares; Hostelz Sydney; Home Affairs fee change of 2026-07-01 | Seen 2026-11-12 | Medium |
| Option D: language course in Spain, 8 weeks | ~NOK 54,000 | languagecourse.net (course fee); accommodation and food are [ASSUMPTION] | Seen 2026-11-12 | Low |
| Consumer loan, nominal rate | **Keep 15% nominal** (show it as about 16-17% effective if the game displays APR) | Finanstilsynet/Gjeldsregisteret: average nominal rate on forbrukslån **14.8%** at 30.09.2023 (latest official figure found). Norges Bank's policy rate is now 4.50%, against 4.25% when that was measured | Report Oct 2023; policy rate 2026-09-24 | Medium-high |
| Credit card / revolving credit (rammekreditt) nominal rate, for reference | 19.7% | Finanstilsynet/Gjeldsregisteret | 30.09.2023 | Medium-high |
| Railway | A Free plan exists: $0 with **$1/month credit** (0.5 GB RAM, 1 vCPU, 1 project). Trial: $5 one-time credit for 30 days. **Hobby: $5/month including $5 of usage**. EU West (Amsterdam) region is available | docs.railway.com/pricing/plans; railway.com/pricing; docs.railway.com/deployments/regions | Seen 2026-11-12 | High |
| Supabase Free | 500 MB DB per project, 50k MAU, 1 GB file storage, 5 GB egress, **paused after 1 week of inactivity**, 2 active projects; EU regions (Frankfurt, Stockholm, Paris, Zurich). Pro from $25/month | supabase.com/pricing; supabase.com/docs/guides/platform/regions | Seen 2026-11-12 | High |
| Resend Free | **3,000 emails/month, max 100/day**, 3 domains, 30-day data retention; EU sending region (Ireland) open to all users. Pro $20/month for 50k emails | resend.com/pricing; resend.com/docs/knowledge-base/what-is-resend-pricing; resend.com/changelog/multi-region-for-everyone | Seen 2026-11-12 | High |
| Hosting cost during a short playtest | **About $5-8/month (NOK 50-80)**: Railway Hobby + Supabase Free + Resend Free | Derived from the rows above | 2026-11-12 | Medium |

---

## 1. Big experience (target NOK 50,000-75,000)

### Option A: Interrail through Europe, 6-8 weeks (recommended default)

This is the most recognisable "big trip" for a Norwegian 19-year-old after upper secondary school, and its key cost (the pass) is published by a first-hand rail seller.

| Component | Calculation | NOK | Source |
|---|---|---|---|
| Interrail Global Pass, Youth (12-27), 2nd class, **2 months continuous** | DKK 4,712 x 1.4199 | 6,691 | DSB price table, https://www.dsb.dk/en/tickets-and-services/Interrail (seen 2026-11-12; the page states no year). Cross-check: 1 month continuous Youth 2nd = DKK 3,968 = NOK 5,634, which matches the €522 youth price cited by Ulysse (https://ulysse.com/news/?p=48560, 2026) |
| Seat and night-train reservations | ~8 x €20 | 1,700 | [ASSUMPTION] Reservations are required on most high-speed and night trains (interrail.com Global Pass page, seen 2026-11-12). Ulysse cites reservations of up to €35 |
| Hostel dorm, 55 nights (8 weeks) | 55 x €35 | 20,430 | Hostelz: Europe-wide median €18.88 (Feb) to €24.36 (Aug); big-city medians Amsterdam $58, Paris $55, Berlin and Prague $37 (hostelz.com/articles/when-are-hostels-cheapest-europe, 2026 data). €35 is a blend for a Western/Central route in summer |
| Food, local transport, sights | 56 x €40 | 23,780 | Hostelz Backpacker Budget Planner (dated 2026-10-01): Balkans €30-35/day all-in, Western Europe much higher; other 2026 guides give €50-80/day all-in for DE/FR/Benelux. €40/day excluding accommodation is a moderate youth level |
| Travel insurance (annual policy) | | 1,500 | Bytt.no: annual travel insurance NOK 1,140-2,300 (bytt.no/forsikring/reiseforsikring, seen 2026-11-12) |
| Phone/data, gear, buffer | | 3,000 | [ASSUMPTION] |
| **Total, 8 weeks** | | **≈ 57,100** | |
| Total, 6 weeks (41 nights; still needs the 2-month pass) | | ≈ 46,000 | Same unit prices |

### Option B: Southeast Asia backpacking, 8 weeks (Thailand, Vietnam, Cambodia)

| Component | NOK | Source |
|---|---|---|
| Flight Oslo-Bangkok return | 7,500 | Momondo: cheapest NOK 6,504, typical NOK 6,427-8,754 (page updated 2026-08-04); Finnair from NOK 6,526-6,595 (autumn 2026 dates) |
| Daily budget $45 x 56 days (guesthouse/dorm, food, local transport) | 24,040 | 2026 backpacker guides: $30-45/day (several sources) and $40-70/day; Hostelz: Thailand/Vietnam ~€29/day on a tight budget |
| Flights/buses between countries | 4,000 | [ASSUMPTION] about 4 short-haul flights plus buses |
| Activities (dive course, tours) | 5,000 | [ASSUMPTION] |
| Vaccines: Japanese encephalitis 2 x 1,353 + hepatitis A+B 3 x 734 + typhoid ~280 | 5,200 | Bærum kommune price list valid from 2026-01-01; Asker kommune (typhoid NOK 280); FHI travel advice for Thailand |
| Visas (Vietnam/Cambodia e-visa) | 600 | [ASSUMPTION] about $25 + $36 |
| Insurance covering a 56-day trip | 2,000 | Bytt.no (as in A); longer trips may need an extension of the standard trip length |
| Gear/buffer | 3,000 | [ASSUMPTION] |
| **Total** | **≈ 51,300** | |

### Option C: Australia, 8 weeks (visiting on an eVisitor visa, or on a Working Holiday visa)

| Component | NOK | Source |
|---|---|---|
| Flight Oslo-Sydney return | 15,000 | Thai Airways from NOK 13,532 (Nov 2026 dates); Finnair from NOK 13,993-16,198 (Nov 2026); Singapore Airlines about NOK 22,600-22,800 in peak season |
| Visa: eVisitor (subclass 651) | 0 | Free for Norwegian citizens, stays of up to 3 months (third-party guides, e.g. visaenvoy.com/evisitor-subclass-651, seen 2026-11-12; not checked against Home Affairs directly) |
| Alternative: Working Holiday visa (417) | +5,500 | AUD 840 for first applications lodged on or after 2026-07-01, up from AUD 670 (thisisaustralia.com/news/visa-fee-increases-1-july-2026, published 2026-07-03; legislation.gov.au F2026L00878) |
| Daily budget AUD 100 x 56 days | 36,640 | Hostelz: Sydney about AUD 89/day including a dorm bed; dorm AUD 37 (June) to 56 (Dec); citiesinsider: AUD 55-88 |
| Domestic transport (bus pass or internal flight), AUD 600 | 3,930 | [ASSUMPTION] |
| Activities (Great Barrier Reef etc.), AUD 800 | 5,230 | [ASSUMPTION] |
| Insurance | 2,500 | Bytt.no (as in A) |
| **Total** | **≈ 63,300** | |

### Option D: language course in Spain (Málaga), 8 weeks

| Component | NOK | Source |
|---|---|---|
| Course: 8 weeks of general Spanish (Andalusí, Málaga), €1,340 | 14,220 | languagecourse.net (search excerpt, 2026; the page itself returned 403, so the details are unverified) |
| Accommodation, homestay or shared flat, about €225/week x 8 | 19,110 | [ASSUMPTION] typical level at Spanish language schools |
| Food and spending, €150/week x 8 | 12,740 | [ASSUMPTION] |
| Activities and excursions, €400 | 4,250 | [ASSUMPTION] |
| Flight Oslo-Málaga return | 2,500 | [ASSUMPTION] low-cost return fare |
| Insurance | 1,500 | Bytt.no |
| **Total** | **≈ 54,300** | Low confidence. An EF course with homestay costs considerably more (EF gives prices only on request: ef.no/upa/price-quotation) |

A trip tied to the russ season (Sunny Beach-type package tours) costs well below NOK 50k, so it does not fit this range.

### Recommendation

**Game default: NOK 60,000, labelled "8 weeks of Interrail through Europe" (or generically "the dream trip").**
- Option A is the most recognisable trip for the target group, and its main cost item comes from a first-hand seller.
- NOK 60k sits in the middle of the cluster (51k / 54k / 57k / 63k), so the team can relabel it as Southeast Asia or Australia without recalculating.
- NOK 60k adds about 5% headroom over the Option A calculation for price rises and currency changes. It is within the 50-75k target and leaves room for an "upgraded" variant at about NOK 75k (Australia with an Asia stopover, 10 weeks).

---

## 2. Consumer-loan interest rate (forbrukslån) in Norway

**Findings**
- **SSB** (ssb.no/renter, published 2026-10-29, reference month September 2026) publishes household lending rates only for **loans secured on dwellings**: 5.31% on outstanding loans and 5.30% on new loans. SSB has no monthly average for unsecured consumer loans. Its "nedbetalingslån" category is also secured on dwellings.
- **Latest official average found:** Finanstilsynet's report "Utviklingen i forbruksgjeld" (October 2023), based on Gjeldsregisteret AS data:
  - Quote: "For forbrukslån var gjennomsnittlig nominell rente 14,8 prosent ved utgangen av tredje kvartal 2023, en økning på 0,9 prosentpoeng siste år." (The average nominal rate on consumer loans was 14.8% at the end of Q3 2023, up 0.9 percentage points year on year.)
  - Quote: "Gjennomsnittlig nominell rente for rammekreditter var 19,7 prosent per 30. september 2023." (The average nominal rate on revolving credit was 19.7% at 30 September 2023.)
  - The report notes that the average nominal rate is somewhat higher for the youngest borrowers (Figure 1.8).
  - Definition at the time: a consumer loan was an instalment loan with a nominal rate above 5%. From 2024 the threshold is 8% or more (Gjeldsregisteret "Gjeldsåret 2025"; Finanstilsynet, April 2025). The rate chapter was not continued in the 2024-2025 reports, and Gjeldsåret 2025 gives no average rate.
  - Source: https://finanstilsynet.no/contentassets/2aeeb336bc2c4f39892b889ebebd6507/utviklingen-i-forbruksgjeld-oktober-2023.pdf
- **Rate level now compared with then:** Norges Bank raised the policy rate to **4.50%** at its meeting on 2026-09-23 (press release 2026-09-24, norges-bank.no). At the time of Finanstilsynet's measurement (30.09.2023) it was 4.25%, so the general rate level is the same or slightly higher today.
- **Market range in 2026** (comparison sites, not official): Bytt.no (August 2026, 173 loans from 79 banks) lists the large banks at about 10.4-11.7% effective for NOK 100-140k over 5 years, and up to 48.76% effective through loan brokers. Summarum (July 2026) shows ranges such as 5.01-25.00% and 6.82-48.76% effective. Norges Bank's Bankplassen blog (2026-02-27) only says that consumer-debt rates are "often far higher" than rates on secured debt, without a figure.
- **Finansportalen** (now under forbrukerradet.no/finansportalen) compares individual offers but publishes no average.

**Recommendation:** Keep **15% nominal**. It matches the last official average (14.8%) and today's policy rate level. If the game shows the effective rate (which Norwegian loan marketing must state), use about **16-17% effective** for a loan of NOK 30-50k over 2-3 years with typical fees [ASSUMPTION: establishment fee about NOK 900-1,000 and a monthly fee of about NOK 40]. For an "expensive" variant (credit card debt or a loan through a broker), 20-25% is realistic.

---

## 3. Hosting costs

### Railway (railway.com)
Sources: https://docs.railway.com/pricing/plans and https://railway.com/pricing (seen 2026-11-12; neither page shows a last-updated date).

| Plan | Price | Included | Limits |
|---|---|---|---|
| Trial | $0 | $5 one-time credit, 30 days | 2 vCPU / 1 GB RAM per service, 500 MB volume, 2 projects / 5 services, 1 custom domain |
| **Free** | $0 | **$1 credit/month** | 1 vCPU / 0.5 GB RAM per service, 500 MB volume, 1 project / 3 services, **no custom domain**, 3-day logs |
| **Hobby** | **$5/month** | **$5 of usage/month** (you pay the $5 even if you use less) | Up to 48 vCPU / 48 GB per service, 5 GB volume, 2 custom domains, 7-day logs |
| Pro | $20/month per workspace | $20 of usage/month | |

- Usage prices are billed per second. Monthly equivalents: RAM about $10/GB, CPU about $20/vCPU, volume $0.15/GB, egress $0.05/GB.
- Trial users cannot buy credits without upgrading to Hobby.
- **Regions:** US West (California), US East (Virginia), **EU West (Amsterdam, `europe-west4-drams3a`)** and Southeast Asia (Singapore) (https://docs.railway.com/deployments/regions, seen 2026-11-12). The docs mention no plan restrictions on regions. According to a reply on Railway's forum (station.railway.com), build and deploy logs are stored in US West whatever region you deploy to. This is not confirmed in Railway's official terms.
- **Playtest estimate:** one small Node service using about 0.25-0.5 GB RAM and little CPU costs roughly $3-6/month in usage, so it fits mostly inside the Hobby credit. **Cost: about $5-8/month (NOK 50-80).** The Free plan ($1 credit, 0.5 GB RAM, no custom domain) is probably too small for an app that must stay up throughout a playtest.

### Supabase
Sources: https://supabase.com/pricing and https://supabase.com/docs/guides/platform/regions (seen 2026-11-12).
- Free plan: **500 MB database per project** (shared CPU, 500 MB RAM), 50,000 monthly active users, 1 GB file storage, 5 GB egress (plus 5 GB cached egress), 500,000 Edge Function invocations, **at most 2 active projects**.
- **"Free projects are paused after 1 week of inactivity."** Inactivity means no database queries; dashboard visits do not count. A paused project keeps its data but must be restored manually from the dashboard. This is no problem during an active playtest, but the team needs a scheduled ping or a manual restore before and after it.
- Pro plan: from $25/month (8 GB database, no pausing).
- **EU regions are available**, including Frankfurt (eu-central-1), Stockholm (eu-north-1), Paris and Zurich. For GDPR purposes, pick a specific EU region rather than the general "Europe" option. Stockholm does not support regional invocation of Edge Functions.

### Resend
Sources: https://resend.com/pricing, https://resend.com/docs/knowledge-base/what-is-resend-pricing and https://resend.com/changelog/multi-region-for-everyone (seen 2026-11-12).
- Free plan: **3,000 emails/month, max 100 emails/day**, 3 custom domains, 30-day data retention.
- Pro plan: $20/month for 50,000 emails, with no daily limit.
- Sending regions: us-east-1, **eu-west-1 (Ireland)**, sa-east-1 and ap-northeast-1. The changelog post of 2025-03-06 (updated 2026-07-09) says every Resend user, including Free users, can choose a region. Some third-party pages say Ireland is Pro-only, but the official changelog takes precedence. Account data and logs stay in the US even when emails are sent from Ireland.
- In practice the 100-per-day cap is the limit that matters, for example at most about 100 magic-link logins per day.

### Total for a short playtest
Railway Hobby about $5-8 + Supabase Free $0 + Resend Free $0 = **about $5-8/month (NOK 50-80)**. If the team needs Supabase without pausing, add $25/month. If it needs more than 100 emails a day, add $20/month for Resend Pro.

---

## Sources (seen 2026-11-12 unless another date is given)
- Norges Bank exchange-rate API, rates of 2026-11-11: https://data.norges-bank.no/api/data/EXR/B.EUR+USD+DKK+AUD+THB.NOK.SP
- DSB Interrail: https://www.dsb.dk/en/tickets-and-services/Interrail
- Interrail Global Pass (terms, reservations): https://www.interrail.com/en/interrail-passes/global-pass
- Ulysse, Interrail 2026: https://ulysse.com/news/?p=48560
- Hostelz hostel prices in Europe: https://www.hostelz.com/articles/when-are-hostels-cheapest-europe ; budget planner: https://www.hostelz.com/en/backpacker-budget/Europe ; Sydney: https://www.hostelz.com/backpacker-budget/cities/sydney-australia
- Momondo Oslo-Bangkok (updated 2026-08-04): https://www.momondo.se/flyg/oslo/bangkok ; Finnair OSL-BKK: https://www.finnair.com/no-no/flights/city-to-city/osl/bkk/flights-from-Oslo-to-Bangkok
- Thai Airways OSL-SYD: https://www.thaiairways.com/flights/en-no/flights-from-oslo-to-sydney ; Finnair OSL-SYD: https://www.finnair.com/no-en/flights/city-to-city/osl/syd/flyreiser-fra-Oslo-til-Sydney
- Australian visa fees from 2026-07-01: https://www.thisisaustralia.com/news/visa-fee-increases-1-july-2026/ ; https://www.legislation.gov.au/F2026L00878/asmade/text
- eVisitor 651: https://visaenvoy.com/evisitor-subclass-651/
- Southeast Asia budgets: https://www.hostelz.com/en/backpacker-budget/South---Southeast-Asia ; https://backpackingislife.com/cost-of-backpacking-southeast-asia/
- Vaccine prices: https://www.baerum.kommune.no/tjenester/helse-og-omsorg/vaksiner-og-smittevern/vaksinasjonspriser ; https://www.asker.kommune.no/helse-og-omsorg/helsetjenester/vaksinasjon-og-smittevern/priser-vaksinasjons--og-smittevern/ ; FHI Thailand: https://www.fhi.no/sm/smittevernrad-ved-reiser/reiserad/asia/thailand/
- Travel insurance: https://www.bytt.no/forsikring/reiseforsikring/a-mve/reiseforsikring-for-ungdom-og-studenter
- Language course, Málaga: https://www.languagecourse.net/no/skole-andalusi-instituto-de-idiomas-malaga
- SSB interest rates: https://www.ssb.no/renter (published 2026-10-29)
- Finanstilsynet consumer-debt reports, October 2023: https://finanstilsynet.no/contentassets/2aeeb336bc2c4f39892b889ebebd6507/utviklingen-i-forbruksgjeld-oktober-2023.pdf ; April 2025: https://www.finanstilsynet.no/4990ef/contentassets/aaf5f43e56c8450b97ba4a50190679eb/rapport-om-utviklingen-i-forbruksgjeld-april-2025.pdf
- Gjeldsregisteret, Gjeldsåret 2025: https://media.gjeldsregisteret.com/images/assets/Gjeldsaret_2025_99bc7c57ad.pdf
- Norges Bank, policy rate raised to 4.50% (2026-09-24): https://www.norges-bank.no/aktuelt/nyheter/Pressemeldinger/2026/2026-09-24-rente/ ; Bankplassen blog, 2026-02-27: https://www.norges-bank.no/bankplassen/arkiv/2026/dyrtid-og-hoye-renter-har-ikke-fort-til-storre-forbrukslan/
- Bytt.no consumer loans: https://www.bytt.no/bank/forbrukslan/forbrukslan-med-lav-rente ; Summarum (July 2026): https://loans.summarum.fi/?country=NO
- Railway: https://docs.railway.com/pricing/plans ; https://railway.com/pricing ; https://docs.railway.com/deployments/regions
- Supabase: https://supabase.com/pricing ; https://supabase.com/docs/guides/platform/regions
- Resend: https://resend.com/pricing ; https://resend.com/docs/knowledge-base/what-is-resend-pricing ; https://resend.com/changelog/multi-region-for-everyone
