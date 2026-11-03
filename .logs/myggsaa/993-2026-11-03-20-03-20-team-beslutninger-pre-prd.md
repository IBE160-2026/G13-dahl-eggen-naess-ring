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
- **Ikke endret:** Regel 7 (72 måneder), kredittkortets minstebeløp og `market-research.md`. #19 er kommentert, men holdes åpen til dokumentendringene er committet. Dokumentendringene er ukommittert.

- **Korrigert personvernbeslutning:** Brukeren erstattet anonym innlogging med kode med innlogging med brukernavn: ingen e-post, ingen ekte alder, ingen fritekst utover brukernavnet, og speltest bare med 18–20-åringer. Addendum, brief, arkitektur, møtenotat og PRD-logg er oppdatert.
- **Vurdering i addendumet:** Et brukernavn bør behandles som personopplysning, men det utløser ikke samtykkekrav i seg selv. Aldersgrensen gjelder når samtykke er behandlingsgrunnlaget. Vurderingen bygger på prosjektets egen lesning av regelverket og er ikke juridisk råd. Søket fant ikke Datatilsynets egen veiledning om dette.
- **Anbefalt, venter på teamet:** Genererte brukernavn, en generert kode som innloggingshemmelighet, og et annet behandlingsgrunnlag enn samtykke. Dokumentendringene er fortsatt ukommittert.

### Åpne punkter
- Definer livsmål og velværemåler (#23)
- Behandlingsgrunnlag og tiltak for innlogging med brukernavn (#24)
- Er et gjennomspill 60 eller 72 måneder? (#25)
- Presiser årsakslenker, «hvis du hadde valgt annerledes» og omspill (#26)
- Hva kuttes først hvis omfanget ikke rekker til desember? (#27)
