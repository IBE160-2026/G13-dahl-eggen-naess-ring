# Team-beslutninger pre-PRD

## 2026-11-03 kl. 20:03 — Myggsaa

### Oppgave
1. `bmad`: finne ut hvor prosjektet står, og hva som er neste steg.
2. Bytte aktiv GitHub-konto i `gh` til `Myggsaa`.
3. Føre gruppens beslutninger om sluttspill, konsekvenser, hendelsesbibliotek og personvern inn i spesifikasjonen, uten å spørre om dem på nytt, og liste nye åpne spørsmål som følger av dem.

### Plan
- Kjøre `bmad-help` og sammenligne katalogen med artefaktene i `.docs/` og åpne issues.
- Lese addendum, brief, arkitektur, brainstormlogg og #19, og oppdatere det som strider mot beslutningene.
- Føre spørsmål som beslutningene åpner, som issues.

### Resultat
- **BMad-status:** PRD-en er neste påkrevde steg. Den har bare tittel, og `status: draft`.
- **GitHub-konto:** `gh` bruker nå `Myggsaa`, og `git push` følger samme konto. Kontoen mangler `workflow`-tilgang, som trengs for å endre `.github/workflows/`.
- **`addendum.md`:** Seksjonen om sluttspill er nå en beslutning: alternativ 2, livsmål + velværemåler med tre slutter. De gamle alternativene er beholdt som historikk. Nye seksjoner for beslutningene om konsekvenser, hendelsesbibliotek og personvern.
- **`brief.md`:**
  - Sluttspillet er flyttet fra Out til In, og Out-lista og scope-testen er nummerert om.
  - Nye In-punkter 7–9 og størrelse og skjema for hendelsesbiblioteket i punkt 5.
  - Nytt avsnitt «How it ends» og nye testkriterier F9 og F10.
  - Speltesten er bare for 18–20-åringer, og innlogging med e-post er erstattet av anonym innlogging med kode.
  - Velværemåler og slutter er fjernet fra «Next» i visjonen.
- **`architecture_technical_design.md`:** Datamodellen har fått livsmål, velværetilstand og årsakslenker. Autentiseringen er anonym med kode, og F9/F10 er lagt til i de tekniske suksesskriteriene.
- **`meeting-prep-2026-11-05.md`:** Beslutningene står øverst i seksjon 1. Temaene for møtet er beholdt.
- **PRD-loggen (`.memlog.md`):** Beslutningene er ført inn, med en merknad om at inndataene må oppdateres når PRD-en fortsetter.
- **Tolkninger gruppen bør se over:**
  - Tap er bare at målet ikke nås. Den tidligere «gjeldsspiral»-tapet er tatt ut, fordi regel 8 sier at en krise aldri avslutter spillet i første versjon.
  - F9 og F10 kommer fra brainstormingen. F9 er tilpasset de tre sluttene.
- **Ikke endret:** Regel 7 (72 måneder), kredittkortets minstebeløp og `market-research.md`.

- **Korrigert personvernbeslutning:** Brukeren erstattet anonym innlogging med kode med innlogging med brukernavn: ingen e-post, ingen ekte alder, ingen fritekst utover brukernavnet, og speltest bare med 18–20-åringer. Addendum, brief, arkitektur, møtenotat og PRD-logg er oppdatert.
- **Vurdering i addendumet:** Et brukernavn bør behandles som personopplysning, men det utløser ikke samtykkekrav i seg selv. Aldersgrensen gjelder når samtykke er behandlingsgrunnlaget. Vurderingen bygger på prosjektets egen lesning av regelverket og er ikke juridisk råd. Søket fant ikke Datatilsynets egen veiledning om dette.
- **Passord:** Brukeren bestemte at spilleren lager eget passord ved registrering, og at Supabase Auth lagrer det. Glemt passord aksepteres uten tilbakestilling i MVP-en, og gjenbruk av passord tas ikke hensyn til nå. Dette erstatter anbefalingen om generert kode i addendum, brief, arkitektur og PRD-logg. Intern e-postadresse laget av brukernavnet er planlagt, men ikke testet på selvhostet Supabase.
- **Anbefalt, ikke vedtatt:** Genererte brukernavn og et annet behandlingsgrunnlag enn samtykke.
- **Personvernspørsmålene utsatt:** Brukeren bestemte at de åpne spørsmålene ikke er viktige for MVP-en og skal sjekkes før lansering. #24 er holdt åpen som en påminnelse om dette, og addendum, møtenotat og PRD-logg er oppdatert.
- **Committet og pushet:** Dokumentendringene ligger i `87ba251` på `docs/pre-prd-research-og-brainstorm` (PR #22). #19 er lukket med en kommentar som viser til commiten.

- **Avklart #23, #25, #26 og #27 (brukerens valg):**
  - 60 måneder, så regel 7 er rettet. Spillet slutter på 20-årsdagen.
  - Tre livsmål: spare til noe stort, gjeldfri med buffer, og råd til en stor opplevelse.
  - Velvære regnes fra stress, fritid og sosialt liv. Hendelsesskjemaet får en velværeeffekt per valg.
  - Fire slutter, som endrer vedtaket om tre: tap (krisevilkår i regel 8 aktivt ved 20), ekte seier, hul seier og «målet ikke nådd» (råd, ikke tap). Minus underveis gir bare krisemåned, og brukeren korrigerte en skrivefeil om dette.
  - Slutten viser topp 3-valg, og omspill starter fra 15 år.
  - Hvis tiden ikke strekker til, kuttes «hvis du hadde valgt annerledes»-linjer først og deretter hendelser ned mot 30.
- **Mine standardvalg, ikke spurt om:** Effekter uten valg lagres med systemårsak. «Hvis du hadde valgt annerledes» gjelder der motoren kan regne det sikkert, først rente og avdrag. Topp 3 rangeres etter effekt i kroner. Alle livsmål sjekkes ved 20. Beløp, vekter og terskel er konfigurasjon som settes under tuning.
- **Committet og pushet:** Endringene i addendum, brief, arkitektur, møtenotat og PRD-logg ligger i `f3d0679` (PR #22). #23, #25, #26 og #27 er lukket med kommentarer som viser til commiten.

- **#20:** Lukket som duplikat av #21. Brukeren bestemte at #12, #13 og #18 kan tas senere, og de står åpne.

### Åpne punkter
- Sjekk personvern for innlogging med brukernavn før lansering, ikke før MVP (#24)
