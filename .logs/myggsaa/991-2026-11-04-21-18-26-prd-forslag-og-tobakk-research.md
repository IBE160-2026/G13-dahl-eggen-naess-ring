# PRD-forslag og tobakk-research

## 2026-11-04 kl. 21:18 — Myggsaa

### Oppgave
Finne ut hvor prosjektet står i BMAD, gå gjennom det teamet må avgjøre i PRD-en, og undersøke om tobakks- og alkoholvalg i spillet er lov når formålet er å vise det negative. Til slutt skulle standpunktene pushes og legges ut til godkjenning.

### Plan
- Byttet til Sarahs PRD-utkast, som fortsettelse av [hennes logg](../sarahnaess/998-2026-11-04-14-43-54-prd-uj4-uj5-og-utkast.md).
- Gikk gjennom åpne spørsmål og antakelser ett og ett.
- Kjørte dyp research med `bmad-deep-recon`: fire temaer, oppfølgingsrunder, motpart og kildekontroll.
- Skrev standpunktene inn i PRD-en på en egen gren og åpnet PR.

### Resultat
- **PR #37** fra `docs/prd-forslag-til-godkjenning` til `main`, med review bedt fra sarahnaess, Sara-se-dev og noraringg. Den inneholder også Sarahs commits. Forslagene ligger i `5f22485`, researchen i `b78d229`.
- **Research:** `.docs/planning-artifacts/research/domain-norwegian-tobacco-alcohol-advertising-la-2026-11-04/research.md`. Hendelsene er trolig lovlige på vilkår, fordi spillet ikke har salgsformål, ikke fordi det viser det negative. Dette er en tolkning, ikke juridisk rådgivning. Effekten på unge er ukjent. Kildekontrollen fant 27 avvik, og alle ble rettet. Språkgjennomgangen ble ikke kjørt, og av strukturforslagene ble bare beslutningsnotatet og tabellen i kapittel 10 tatt inn, fordi hendelsene ble droppet.
- **Dahls forslag i PRD, addendum, brief og regelsett:** ingen tobakks- og alkoholvalg, tilfeldig førerkortgave med mulighet til å betale selv, kjøp av moped ved eget valg med gavetilbud av og til, familiegaver av kuttlisten, familielån utenfor krisetesten på 3× inntekt, hul seier viser et valg som skadet trivselen, kortminimum 3,5 % og ny FR-44 om sletting av konto. Antakelsene A-1, A-3, A-12, A-13, A-14, A-15, A-18 og A-26 er bekreftet av Dahl.
- **Rettet:** «ban on marketing to minors» til generelle reklameforbud for alle aldre. Møtenotatet er oppdatert.
- PRD-en er fortsatt `draft`. Trinnene for finalisering (sjekk mot kildedokumenter, kvalitetsgjennomgang) er ikke kjørt.
- Nytt: #38 og #39. Kommentert: #28, #29, #34, #35 og #36. Ingen issues er lukket.

### Åpne punkter
- Teamet må godkjenne forslagene i PR #37, deretter gjennomgang og finalisering av PRD-en (#28).
- Teamet bekrefter at tobakks- og alkoholvalg droppes (#34), kortminimum (#35) og sletting av konto (#36).
- Finn reell pris på førerkort i tillegg til de andre prisene (#29).
- Avklar avvik i korttallene: 5 885 kr mot 5 878 kr ved 3 % (#38).
- Sjekk at F5 kan flyttes til KI-trinnet mot kurskravene (#39).
- Brief og arkitektur beskriver fortsatt KI som del av første versjon (#32).

## 2026-11-05 kl. 09:18 — Myggsaa

### Oppgave
Finne status i BMAD, hente siste endringer og føre inn tre beslutninger i PRD-en: ingen tobakk og alkohol, kortminimum på 3,5 % og sletting av konto.

### Plan
- Sjekket status og kjørte `git pull`. PR #37 og #40 var allerede merget til `main`.
- Laget grenen `docs/prd-team-beslutninger` fra `origin/main`.
- Førte beslutningene inn i PRD, addendum og memlog.

### Resultat
- **`prd.md`:** fjernet OPEN-merket på FR-44, flyttet OQ-2 og OQ-10 til en liste over avklarte spørsmål, og snevret OQ-1 inn til førerkortgaven.
- **`addendum.md`:** de tre forslagene er flyttet til en egen tabell over beslutninger, og korttallene omtales ikke lenger som et forslag.
- **`.memlog.md`:** beslutningene er ført inn, med Dahls begrunnelse for sletting: det er lett å håndtere i Supabase.
- Endringene i disse tre filene er ikke committet. PRD-en er fortsatt `draft`.
- #34, #35 og #36 er ikke lukket, fordi lukkingen ble avvist av tillatelsessjekken.

### Åpne punkter
- Lukk #34, #35 og #36 med beslutningene som kommentar. #36 dekker også A-28 til det er avklart.
- Bekreft A-28: sletting krever gjeldende passord og kan ikke angres (#36).
- Teamet må bekrefte tilfeldig førerkortgave med mulighet til å betale selv (OQ-1, FR-30) og de øvrige forslagene i addendumet (#28).
- Avvik i korttallene ved 3 % betyr ikke lenger noe for spillet, så #38 kan trolig lukkes.
