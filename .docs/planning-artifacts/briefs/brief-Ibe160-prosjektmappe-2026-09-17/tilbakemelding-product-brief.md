# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G13 – G13-dahl-eggen-naess-ring |
| **Product brief** | `.docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/brief.md` (commit bb1ba16), lest sammen med `addendum.md` og `architecture_technical_design.md` i samme mappe |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

## Samlet vurdering

- **Godt utgangspunkt med justeringer.** Gruppen kan gå videre og innarbeide punktene under.

**Det som er bra:**

1. LifeMode har en tydelig og original idé: «la unge gjøre dyre økonomiske feil før de koster ekte penger». Eksempelet med turen til 3 200 kroner når man har 1 500, og konsekvensen som dukker opp i måned 9, gjør problemet og løsningen konkret.
2. Prinsippet «KI-en skaper livet, finansmotoren bestemmer konsekvensene» er et svært godt arkitekturvalg. Det gjør appen testbar, og addendumet viser at dere har satt dere inn i kjente fallgruver (AI Dungeon, «helpfulness bias») og tenkt på sikkerhet for mindreårige. Det er også bra at dere har jobbet med branch og pull request og har ryddet briefen ved å flytte detaljer til addendum.

**De viktigste endringene:**

1. Suksesskriteriene bygger nesten bare på en playtest med 10–20 personer i alderen 14–20 år. Det er krevende å gjennomføre (mindreårige, samtykke) og gir ikke testbare krav til appen. Legg til funksjonelle kriterier som kan bli testtilfeller.
2. Finansmotoren må «alltid regne riktig», men briefen sier ikke hvilke regler den skal følge. Definer et lite, konkret regelsett (rente, lån, husleie, faste kostnader) med regneeksempler som fasit.
3. Løsningen avhenger av Supabase og en gratis LLM-API. Planlegg hvordan sensor kan kjøre appen lokalt uten deres kontoer og nøkler, og vurder om dere trenger innlogging i v1 i det hele tatt.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Vanskelig**

**Sammenlignbart med:** 3) KI-styrt simulering av prosjektledelse (vanskelig) – også en simulering der valg over tid gir konsekvenser, med en deterministisk motor og KI-genererte hendelser.

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Høy | Inntekt, sparing, renter, kreditt, gjeld, husleie og uforutsette utgifter over flere år, der tidligere valg skal påvirke senere situasjoner. Alt skal stemme «100 %». |
| Datamodell – antall entiteter og relasjoner mellom dem | Middels | Spiller/avatar, spilltilstand per måned, økonomiske kontoer/lån, hendelser og valg med historikk. Overkommelig, men tilstanden over tid må modelleres nøye. |
| Brukere, roller og innlogging | Middels | Én rolle, men Supabase-autentisering for mindreårige. Kan trolig utelates i v1 (lagre spill lokalt). |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Høy | KI-en skal lage hendelser ut fra spillerens historikk, i strukturert format som valideres mot et skjema og filtreres før visning, med reservehendelser ved feil. Dette er avansert. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Middels | Supabase og en gratis LLM-leverandør som ikke er valgt. Gratisnivåer har grenser som kan stoppe både testing og sensor. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Enspillerspill, ingen samhandling mellom brukere. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Lav | Ikke en del av v1. |
| Sikkerhet og personvern | Høy | Målgruppen er mindreårige. Dere har gode prinsipper (ingen ekte persondata, moderering før visning), men de må faktisk implementeres og testes. |

**Hva vanskelighetsgraden betyr for dere:**

- _Vanskelig:_ Et vanskelig prosjekt gir større mulighet for toppkarakter, men også større risiko. Definer en minimal versjon som sikkert kan bli ferdig, og legg resten i tydelige trinn etterpå. For LifeMode betyr det: en finansmotor med få, veldefinerte regler og et kort livsløp som virker, før KI-genererte hendelser og flere livsfaser kommer på plass.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | Risiko | Det er bra at forhandling, sluttspill og foreldrevisning er lagt utenfor. Likevel er «In» fortsatt stort: åtte livsområder fra sparing til kreditt, KI-hendelser, validering og moderering, og en responsiv nettside med egen Python-backend. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Risiko | Visjonen og avgrensningen er god, men det mangler en konkret spillsløyfe (hva skjer i én «måned»?) og et regelsett for økonomien. Uten dette må PRD-en finne opp spilldesignet. Spillnavnet er heller ikke bestemt. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | Risiko | Hver del er vanlig, men TypeScript-frontend + Python-backend + Supabase + LLM-leverandør er fire deler å sette opp og holde i sync. Vurder én enklere stakk. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | Risiko | Privatøkonomi på dette nivået kan dere kontrollere selv, *hvis* dere definerer reglene og regner ut eksempler for hånd. Det er avgjørende for kriteriet «alle tall stemmer». |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | Risiko | Finansmotoren er godt egnet for automatiske tester så snart reglene er skrevet ned. KI-delen kan testes med skjemavalidering og mock-svar. Playtest-kriteriene kan ikke bli automatiske tester. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Stor risiko | Supabase og en ekstern LLM krever kontoer og nøkler. Uten en lokal database og et sett med forhåndsskrevne hendelser (fallback) kan sensor ikke spille. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | «Null løpende kostnad» er tydelig, og fallback til forhåndsskrevne hendelser er nevnt i addendumet. Gjør denne fallbacken til en fullverdig modus som også brukes i tester og av sensor. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart med justert omfang.** Se forslagene under.

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. V1: ett kortere livsløp (f.eks. 16–19 år) med 4–5 økonomiske mekanismer (lønn, sparing, faste kostnader, forbrukslån/kreditt med rente, uforutsette utgifter) og en månedlig spillsløyfe. Legg flytting, utdanning og førerkort til i senere trinn.
2. Bygg finansmotoren og et bibliotek med forhåndsskrevne hendelser først, slik at spillet virker helt uten KI. Legg deretter til KI-genererte hendelser som et eget trinn som velger og tilpasser hendelser innenfor rammer motoren setter.
3. Dropp innlogging i v1 (lagre spilltilstand lokalt eller i en lokal database), og vurder om en enkelt stakk er nok i stedet for separat TypeScript-frontend og Python-backend.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | Klart og engasjerende. Eksemplene (sparing, kreditt, billig bil som blir dyr) gjør ideen lett å forstå. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | OK | Konkret, med et godt eksempel og en kilde (Finans Norge). |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | Juster | Beskriver opplevelsen godt, men ikke hva spilleren konkret gjør i én runde. Beskriv spillsløyfen i 3–5 steg: se situasjon → velg → se konsekvens i tall → neste måned. |
| What Makes This Different – er vurderingen ærlig og realistisk? | OK | Ærlig sammenligning med BitLife, Zogo og norske alternativer, og en god «honest caveat» om at KI-en må bevise sin verdi. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | Juster | Tydelig målgruppe, men det står både 14–20 og 15–20 år. Bestem aldersspennet, og vurder om dere kan teste med målgruppen (mindreårige) eller må bruke medstudenter. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Endre | Kriteriet om at alle tall stemmer er utmerket. De øvrige er playtest- og atferdsmål (70 % forklarer, 50 % kommer tilbake, en forelder vil prøve) som er vanskelige å måle i emnet. Legg til funksjonelle kriterier, f.eks. «et lån på X kr med Y % rente gir riktig saldo etter 12 måneder», «en ugyldig KI-hendelse erstattes av en forhåndsskrevet», «spillet kan fullføres fra start til slutt uten KI». |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | Juster | God «Out»-liste og en fin «scope test». «In» bør likevel smalnes inn (se forslagene), og det bør stå hva spillet gjør når KI-en feiler. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | OK | Tydelig delt i nå, neste og 2–3 år, og holder v1 adskilt. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | OK | Briefen er iterert over flere commits og en pull request, og avveiningene er dokumentert. Fortsett slik, og la PRD-en bygge på et konkret regelsett for økonomien. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Juster | Ambisiøst. Et kortere livsløp med få, solide mekanismer gir nok funksjonalitet for et vanskelig prosjekt. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | Endre | Skriv regneeksempler med fasit for finansmotoren og testbare kriterier for KI-valideringen. Playtesten kan være et supplement. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | OK | Mobilførst, 10–15 minutters økter og «spill, ikke lekse» gir god retning. Skisser hovedskjermen (situasjon, valg, økonomioversikt) tidlig. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | Juster | Skillet mellom motor og KI er godt. Stakken med fire deler er mer kompleks enn nødvendig, og begrunnelsene i arkitekturdokumentet er ennå ikke skrevet. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Endre | Avhengig av Supabase og en LLM-leverandør. Planlegg lokal database, `.env.example` og en modus uten KI. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | Planleggingsdokumentene ligger ryddig i `.docs/`. Arkitekturdokumentet ligger i brief-mappen og bør få egen plass. Sjekk at `.mcp.json` ikke inneholder nøkler, og hold API-nøkler i `.env`. |

## 3. Neste steg for gruppen

1. Skriv ned regelsettet for finansmotoren (få mekanismer) med 3–5 regneeksempler som fasit, og legg det i briefen eller addendumet.
2. Beskriv spillsløyfen i 3–5 steg og smaln inn «In» til et kortere livsløp.
3. Legg til funksjonelle, testbare suksesskriterier ved siden av playtest-målene.
4. Bestem hvordan appen kjører uten KI og uten Supabase-konto (forhåndsskrevne hendelser, lokal lagring), og gå deretter videre til PRD.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
