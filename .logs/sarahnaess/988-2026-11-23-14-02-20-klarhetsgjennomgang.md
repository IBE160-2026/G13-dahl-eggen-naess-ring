# Klarhetsgjennomgang

## 2026-11-23 kl. 14:02 — sarahnaess

### Oppgave
Sjekke at arkitekturen, PRD-en, designet og resten av planene henger sammen før neste BMad-steg (epics og stories, deretter sprintplanlegging), og at vi ikke mangler noe viktig. Startet med `bmad-help`, deretter `bmad-review`.

### Plan
- `bmad-help`: finne ut hvor prosjektet står. Brief, PRD, UX og arkitektur er ferdige. Neste påkrevde steg er Create Epics and Stories.
- `bmad-review` med to linser som kjørte samtidig: Adversarial og Edge-Case Hunter. Structure og Prose ble hoppet over fordi spørsmålet gjaldt innhold, ikke språk.
- Innhold: PRD + addendum, Regelsett v1 (brief-addendumet), ARCHITECTURE-SPINE + SOLUTION-DESIGN, DESIGN + EXPERIENCE (ux-11-11). Kurskriteriene, playtest-rubrikken og de åpne issuene var kontekst.
- De mest alvorlige funnene ble kontrollert mot teksten: datoene i §4.4, at FR-35 fortsatt står i §4.1, at brief.md fortsatt sier Supabase og 50 hendelser, Flyt 1 i EXPERIENCE og lånevilkårene i addendumet. Alle stemte.

### Resultat
- 65 funn (21 adversarial, 44 edge-case), uten rangering. Rapporten ligger i `.docs/planning-artifacts/readiness-review-2026-11-23/report.md`, og alle funn ligger som JSON i `findings.json` (ikke committet i denne økta).
- Hovedfunn:
  - Datoene i §4.4 holder ikke. Utvidelser fryses 26-27. nov, men det finnes ingen kode eller epics ennå.
  - Fasiten (UJ-4-sporet og eksempel 17a, 17b, 23 og 26c) setter timene direkte, noe FR-47 ikke lenger tillater.
  - Innholdsskjemaer mangler for åpne valg, krisetrinn, rom, tekster og utgifter.
  - Ingen frontend-arkitektur, og ingen konvensjon for lint eller review.
  - Én-om-gangen-regelen (FR-48) og småspillet er ikke avgjort.
  - FR-35, OQ-9 og Supabase står fortsatt i tekstene selv om de er utdatert.
  - Påmeldingen til playtesten er åpen for alle.
  - Fryseporten i AD-7 strider mot regelen om at playtesten starter uansett.
  - Mange udefinerte grenser i Regelsett v1.
- Funnene er lagt som kommentarer på #46, #117, #83, #51, #92, #81 og #82.
- #116 og #120 ser løst ut gjennom PR #119. De lukkes ved merge og ble ikke lukket her.

### Åpne punkter
- Skriv innholdsskjemaene som mangler før innholdshistoriene (#121)
- Lag en kort frontend-arkitektur (FE-AD) med lint- og review-regler før frontend-epicene (#122)
- Avklar grensetilfellene i Regelsett v1 og PRD-en før motorhistoriene (#123)
- Rydd utdaterte og motstridende tekster i PRD, brief og UX (#124)
- Sikre playtesten: påmelding med testerkode, tilbakestilling uten e-post, personvernside og databasebackup (#125)
- Bestem hva som skjer med frysen og innholdet hvis biblioteket ikke er klart til playtesten (#126)
- Sett nye datoer i §4.4 etter den ekte fristen før sprintplanleggingen (#46, #73)
- Fasiten bruker timer som FR-47 ikke tillater, så #117 er større enn ordlyden (#117)

## 2026-11-23 kl. 14:33 — sarahnaess

### Oppgave
Merge PR #119 og rett punkt 1-5 fra klarhetsgjennomgangen før epics: datoene, fasiten mot FR-47, innholdsskjemaene, de åpne beslutningene (småspill, én om gangen) og utdaterte tekster.

### Plan
- Merget PR #119 (f615bf0). #116 lukket ved merge, og #120 var allerede lukket.
- Beslutninger fra Sara: bare skriv om datoene (regelen står), småspill er V2, fasiten merkes som satte testtilstander, og standardtabellen for én om gangen.
- Ny gren `docs/klarhet-for-epics`, med endringer i PRD, addendum, Regelsett, brief, spine, SOLUTION-DESIGN og EXPERIENCE.

### Resultat
- Commit 7cc1145 (9 filer):
  - §4.4: frys ca. 3.-4. des., spillbar kjerne ca. 7. des. Playtesten 8. des. og leveringsdatoen står.
  - Småspill V2: FR-51 merket V2, FR-28/FR-30 bare betaling, punkt 7 fjernet fra kuttlista, OQ-16 venter på V2, D10 uten kjørespill, og FR-51 er fjernet fra binds og regler i spinen. Overflate 22 i UX er V2.
  - FR-48: tabell for én om gangen. Kredittkortet er ett per gjennomspilling, siden MVP-en ikke har noen måte å lukke kortet på.
  - Fasiten: 17a, 17b, 23, 26c og UJ-4-sporet er merket som satte testtilstander. Ingen tall er endret.
  - Addendum: nye skjemaer for krisehendelser, kortvarsel, åpne valg, romtilstander, tekster, uventede utgifter og faste lister. Lånevalget tar grensene fra FR-25 og vilkårene bare fra config, og FR-58 lister alle skjemaene.
  - FR-35 er ryddet ut av §4.1, §4.4 og ordlista. OQ-9 er lukket.
  - EXPERIENCE: Open Questions er oppdatert, 11-17-mappa er bare historikk, og Flyt 1 (5 000 kr på sparing) og Flyt 4 (juni i første år) stemmer nå med UJ-3 og FR-55.
  - brief.md har fått et datert notat, og endringstabellen har seks nye rader.
- Memlogger oppdatert for PRD og arkitektur.
- DESIGN.md fikk stå med Speilets DESIGN.md (11-17) som kilde. Det er bare opphav og ikke bindende.

### Åpne punkter
- Datoene må fortsatt sjekkes mot den ekte leveringsfristen (#73, #46).
- D12, D25 og D26 sier fortsatt at spilleren setter timer (#117). Fasitdelen er rettet.
- De tre andre tekstpunktene fra polishen (#83). Én-om-gangen-regelen er rettet.
