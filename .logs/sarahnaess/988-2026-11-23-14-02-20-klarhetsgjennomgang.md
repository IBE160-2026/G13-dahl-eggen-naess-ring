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
