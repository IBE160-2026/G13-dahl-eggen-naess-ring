# Brainstorm: fire åpne tema før PRD

## 2026-10-29 kl. 10:37 — Myggsaa

### Oppgave
Kjøre bmad-brainstorming på de fire åpne temaene fra #19 (sluttspill ved 20, sammenheng valg→utfall, hendelsesbibliotek, personvern/samtykke for 15–17) før PRD-en, slik at UJ-5 og FR-ene kan skrives. Brukeren valgte «Ideate for me» med teknikkene Yes And Building, SCAMPER, Five Whys og Drunk History Retelling.

### Plan
- Forankret i briefen (sluttspill utenfor scope), addendumets sluttspill-alternativer, PRD-memloggens UJ-1..UJ-5 og research #16–#18.
- Genererte ideer per teknikk, logget i memlog, syntetiserte innsikter, lagde HTML-keepsake via underagent.

### Resultat
- `.docs/brainstorming/brainstorm-lifemode-pre-prd-open-questions-2026-10-29/.memlog.md` — 105 ideer, 6 innsikter, status `complete`.
- `.docs/brainstorming/brainstorm-lifemode-pre-prd-open-questions-2026-10-29/brainstorm.html` — visuell oppsummering.
- Hovedforslag:
  1. UJ-5 = «Livet ditt ved 20» + topp 3 valg + omspill fra et veiskille; vinnerbetingelse/velværemåler forblir utenfor scope. Valgfritt: «brev fra deg selv som 15-åring».
  2. Årsakslenke-id på hver effekt i motoren driver ekko-merker, «Hvorfor?»-knapp, kontrafaktiske linjer og avslutningen; nye testkriterier F9/F10.
  3. Hendelsesskjema (mekanisme, alder, flagg, boomerang-par, læringspoeng, LK20, kilde); min ~30 hendelser for F6, mål 60–80 + ~10 krisesett; ~55/45 før/etter 18.
  4. «Lagring, ikke identitet»: anonym innlogging/gjenopptakskode, ingen fritekst, ingen ekte alder, playtest kun 18–20, anonymt debrief-skjema.
- Kommentert resultatene på #19 (holdes åpen til teamet bestemmer) og F8-funnet på #16.
- Brainstorm-filene er ikke committet.
- F8 rettet etter brukerens ønske: `brief.md` (F8 → 2 588 kr trygdeavgift, «frikort tax» → «tax on 2026 rates», `updated: 2026-10-29`) og `addendum.md` (regel 3 omskrevet til 2026-skatteberegning med trygdeavgift, minstefradrag, personfradrag og trinnskatt trinn 1; regneeksempel 5 → 2 588 kr; ny parameterrad for skatt 2026; frikort-raden presiserer at 50 % er forskuddstrekk). Kilde: research `domain-norwegian-youth-finance-rules-2026-10-27`.
- Committet på ny gren `docs/pre-prd-research-og-brainstorm` (4cc5651 research, d062485 brainstorming, b62c6c8 F8) og PR #22 mot main. Push feilet først med 403: `gh` og Git Credential Manager brukte kontoen Myggsa. Byttet til Myggsaa (`gh auth switch --user Myggsaa` + `gh auth setup-git`), og la til tildeling på #21 i etterkant.

### Åpne punkter
- Teamet må ta stilling til forslagene før PRD (#19).
- Resten av finansregel-rettingene: BSU-fradrag 0 kr uten skatt, arbeidstidsgrenser, opplysningstekster om forenklinger (#16).
- Les Groq-kvoter og Cloudflare AUP (#17).
- Verifiser norsk aldersgrense for digitalt samtykke (antatt 13 år) før PRD-krav om innlogging (#21).
