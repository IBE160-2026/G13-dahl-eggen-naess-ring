# Tilbakemelding på PRD

| | |
|---|---|
| **Gruppe** | G13 – G13-dahl-eggen-naess-ring |
| **PRD vurdert** | `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md` (status i frontmatter: final, sist endret 2026-11-11, commit 755b3b7). Lest sammen med `addendum.md` i samme mappe |
| **Dato** | 2026-11-12 |
| **Type** | Formativ tilbakemelding, ikke karakter |

## 1. Samlet inntrykk

Dette er en uvanlig gjennomarbeidet PRD med en tydelig tese, nesten helt testbare krav og ærlig avgrensning. Den viktigste risikoen er størrelsen: 57 FR-er, 11 NFR-er og ca. 24 800 ord, der kjernen (motor, ukesløyfe, endinger) deler plass med innlogging, hosting, minigame, telefon og månedsplan. Det er mer enn det er trygt å love for ett semester, og kutt-planen er ennå ikke knyttet til datoer.

## 2. Dette fungerer godt

1. **Tydelig tese og brukerreiser som driver kravene.** §1 «let young people make expensive money mistakes before those mistakes cost real money» går igjen i UJ-1 til UJ-6, der Markus følges gjennom hele livsløpet. UJ-4 har faktiske tall (22,6 % rente, 51 måneder, NOK 5 508 i rente) som er koblet til FR-26 og FR-31. Dette er ikke pynte-personas.
2. **FR-ene kan bli testtilfeller.** Nesten hvert FR har «Consequences (testable)» med verdier og fasit, for eksempel FR-25: «NOK 20,000 over 12 months gives monthly payments of NOK 1,805 … NOK 21,663 in total (worked example 3, F1)». Determinisme og seed (FR-12) gjør at hele spillet kan spilles om igjen i tester, uten KI.
3. **Ærlig scope.** §4.2 (aldri i V1), §4.3 (senere) og §4.4 (kuttrekkefølge med «These always stay») viser at dere har tenkt på hva som skal ofres. §7.1 sier åpent at testerne er 18–20 år og at resultatene ikke gjelder 15–17-åringer.

## 3. Oversikt per dimensjon

| Dimensjon | Vurdering | Kort begrunnelse |
|---|---|---|
| Beslutningsklarhet | god | Valg og avveininger er synlige (§4.4, §8, addendum), men status «final» med 13 åpne spørsmål og uferdige tallverdier er misvisende. |
| Substans | sterk | Domenetall med kilder, konkrete NFR-er (NFR-10: 1 s / 3 s), ingen boilerplate. |
| Strategisk sammenheng | god | Klar tese og mål som måler den (§7.1, §7.2 med motmål), men fire spillområder ble lagt til 10.–11. nov. og utvider kjernen. |
| Testbarhet | sterk | Konsekvenser per FR, 28 regneeksempler som fasit, innholdssjekk og NFR-7-liste med én test per avvisning. |
| Scope og avgrensning | god | Utelatelser er eksplisitte, men omfanget er stort og kutt-tidspunktene er ikke satt (OQ-13). |
| Brukbarhet for neste fase | god | IDer er rene og glossaret brukes konsekvent, men dokumentet er langt og regler («rule N», D1–D26, F1–F10) ligger utenfor PRD-en. |
| Formtilpasning | god | Brukerreiser passer et spill. Autentisering og drift er derimot detaljert som om det var kjernen. |

## 4. Viktigste forbedringer

### 4.1 Omfanget er større enn kutt-planen tåler
- **Alvorlighet:** høy
- **Hvor:** §4.4 «cuts are applied in groups at checkpoints the team sets under OQ-13»; §4.1 (16 punkter); FR-52 til FR-57
- **Problem og hvorfor det betyr noe:** Tilbakemeldingen på briefen anbefalte 4–5 mekanismer og kortere livsløp. PRD-en har rundt ti mekanismer, fem år, 40+ hendelser, 5+12–20 aktiviteter, kjøre-minigame, rom-lag og telefon. Kutt-listen har 11 punkter, men «checkpoints» finnes ikke ennå. Uten dem vet ingen i epics-fasen hva som må være ferdig først.
- **Forslag:** Del FR-ene i tre nivåer i en tabell: **Kjerne** (motor, ukesløyfe, hendelser, endinger, «Hvorfor?»), **Utvidelse** (telefon, månedsplan, jobbvisning, pengevisning), **Kan kuttes** (resten av §4.4). Sett to datoer: «Kjernen spillbar fra start til slutt: dd.mm» og «utvidelser fryses: dd.mm». Skriv også i §4.4: «Hvis kjernen ikke er spillbar 15. desember, utgår nivå Kan kuttes uten ny diskusjon».

### 4.2 Hosting og lokal kjøring peker i hver sin retning
- **Alvorlighet:** høy
- **Hvor:** NFR-6 «the required database and login service (Supabase) runs self-hosted in the local run»; NFR-5, NFR-10, NFR-11; OQ-14
- **Problem og hvorfor det betyr noe:** Dere krever null kostnad, EU-lagring, 7 dagers tilgjengelighet og brukbar skjerm innen 10 s etter hvile. OQ-14 sier selv at ikke alle kan holde. Selvhostet Supabase i Docker består av mange tjenester og kan sprenge «15–20 minutter» for sensor. Innlogging, tilbakestilling, rate-begrensning og sletting (FR-1 til FR-5, FR-44) utgjør også en stor del av kravteksten, selv om briefen foreslo å droppe innlogging i V1.
- **Forslag:** Gjør OQ-14 til en beslutning før arkitekturen. Skriv NFR-6 om til et krav med reservevei: «Sensor kan starte appen med én kommando og logge inn med seedede brukere (README). Hvis e-post ikke er tilgjengelig lokalt, verifiseres tilbakestilling kun av automatisk test.» Vurder å flytte innloggingens herding (allerede punkt 11 i §4.4) ut av V1-kravene.

### 4.3 Lange FR-er og regler utenfor PRD-en gjør uttrekk vanskelig
- **Alvorlighet:** medium
- **Hvor:** FR-9, FR-32, FR-46 (hver 12–15 punkter); §0 «refers to those rules by number ("rule 5")»
- **Problem og hvorfor det betyr noe:** Én story per FR er ikke mulig. FR-ene blander flere regler, og leseren må åpne brief-addendumet for å forstå «rule 12». FR-ene står heller ikke i tallrekkefølge (FR-44 etter FR-5, FR-49 før FR-13).
- **Forslag:** Legg inn en FR-oversikt (ID, tittel, nivå fra 4.1, UJ) øverst i §5. For de tre lengste FR-ene: del i delkrav, f.eks. FR-32a «Utløsere», FR-32b «Krisemånedens trinn», FR-32c «Avslutning». Gjengi regelen i én setning der FR-en bruker den («rule 12: velvære = vektet snitt av stress, fritid, sosialt liv»).

### 4.4 «final» og tallverdier som ennå er plassholdere
- **Alvorlighet:** medium
- **Hvor:** frontmatter `status: final`; FR-9 «With the placeholder prices, the run is expected to need tuning once OQ-17 gives real prices»; FR-33 «The content check fails if a change … lifts any of them to 50 or above»; OQ-3, OQ-8, OQ-17
- **Problem og hvorfor det betyr noe:** Mål om at mål 1–3 er nåbare og at «hollow win» holder, hviler på tall som ikke finnes ennå. Da er testene avhengige av verdier som kan endres, og «final» lover mer enn dokumentet kan holde.
- **Forslag:** Skriv status om til «final for UX og arkitektur; innholdstall foreløpige» og legg til en parametertabell (parameter, standardverdi, kilde ja/nei, eier, frist). Da kan dere fortsatt teste mot standardverdiene og samtidig se hva som gjenstår.

### 4.5 Suksessmålene mangler ID-er
- **Alvorlighet:** lav
- **Hvor:** §7.1 (tabell), §7.2
- **Problem og hvorfor det betyr noe:** Målene kan ikke refereres fra stories, tester eller rapport (som «SM-3»), og noen er selvrapportering («can explain …»).
- **Forslag:** Gi hver rad en ID (SM-1 …), og legg til hvilket FR/UJ den validerer, f.eks. «SM-1 (forklare tidligere valg) → FR-38, FR-42, UJ-3».

## 5. Mekaniske funn

- FR-1 til FR-57 er sammenhengende og unike, og alle henvisninger til FR og OQ løser seg. Hullene i OQ-nummereringen er forklart i §8.
- UJ-rekkefølgen er 1, 2, 3, 6, 4, 5. Det er forklart i §2.3, men en kronologisk nummerering ville vært enklere å bruke.
- Ingen inline `[ASSUMPTION]`; antakelsene A-1 til A-30 ligger i `addendum.md`, og §9 i PRD-en peker bare dit. Antakelser som A-26 (F5 flyttet til V2) bør stå i PRD-en.
- Glossaret er stort og konsekvent (økt/sitting, aktiv/stille måned). Jeg fant ingen avvik.
- UJ-ene har alle en navngitt hovedperson (Markus) med kontekst inline.

## 6. Før dere går videre

**Må avklares før UX, arkitektur og epics:**
- Nivå og datoer for kjerne/utvidelse/kutt (4.1, OQ-13).
- Hosting og lokal kjøring (4.2, OQ-14, OQ-4), siden arkitekturen avhenger av svaret.
- Behandlingsgrunnlag og ansvar for data i playtesten (OQ-6), som må være på plass før første test.

**Kan vente:** OQ-9, OQ-12 og OQ-18 (UX og tekst), samt kilder og tuning i OQ-3, OQ-8 og OQ-17, så lenge standardverdier brukes til testene.

**Oppfølging av briefen (delvis):** Ja på regelsett med regneeksempler (Rule Set v1, 28 eksempler), spillsløyfe (diagram i §5.4) og funksjonelle kriterier (F1–F10, konsekvenser per FR). Ja på kjøring uten egne nøkler og på spill uten KI. Nei på å smalne inn: livsløpet er fortsatt 15–20 år, og innlogging er beholdt.

**KI i appen:** PRD-en har ingen KI i V1 (§4.2), så det finnes ingen KI-funksjon å kontrollere i denne versjonen. V2-sporet er tydelig avgrenset (§4.3: «the engine still decides every amount»). Spørsmålet i OQ-11 om dette er tilstrekkelig for emnet svarer ikke denne tilbakemeldingen på. Ta det direkte med faglærer.

## 7. Refleksjonsspørsmål

1. Fire nye spillområder (månedsplan, telefon, jobbvisning, pengevisning) ble lagt til 10. november og påvirket mange FR-er. Hvordan sjekket dere at KI-forslagene ikke motsa eksisterende krav, og hva fant dere?
2. FR-9 og FR-33 setter grenser som «42, 46 og 37». Hvilke av disse tallene har dere regnet ut selv, og hvilke bygger på KI-forslag dere ikke har kontrollert?

_Vurdert mot kvalitetsrubrikken i bmad-prd. Dette er veiledning, ikke sensur._
