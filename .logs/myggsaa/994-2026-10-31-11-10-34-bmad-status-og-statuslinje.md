# BMad-status og statuslinje

## 2026-10-31 kl. 11:10 — Myggsaa

### Oppgave
1. `bmad`: finne ut hvor prosjektet står i BMad-løpet, og hva som er neste steg.
2. Endre den personlige statuslinja i Claude Code: vise effortnivå, gi delene tydeligere farger, flytte kontekst/5t/7d til en egen linje, og vise tokenbruk mot det som er tilgjengelig.

### Plan
- Kjøre `bmad-help`: lese `_bmad/_config/bmad-help.csv` og konfigurasjonen, og sammenligne med artefaktene i `.docs/` og de åpne `sesjonslogg`-issuene.
- Lagre JSON-en som Claude Code sender til statuslinja midlertidig til fil, for å se hvilke felt som finnes. Deretter skrive `~/.claude/statusline.ps1` på nytt.

### Resultat
- **BMad-status:** Brief, design thinking, research (27.10) og pre-PRD-brainstorm (29.10) er ferdige. PRD-en (`.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md`) har `status: draft` og bare tittel. I memloggen er inngangsdata, coaching-modus og fem user journeys (UJ-1–UJ-5) bekreftet. Neste påkrevde steg er å fortsette PRD-en med `bmad-prd`. Etter det: UX, arkitektur (husk leverandørbytte, #17), epics/stories og sprint planning. Issue #19, #16 og #13 bør helst håndteres før PRD-en.
- **Statuslinje** (`C:\Users\Dahl\.claude\statusline.ps1`, utenfor repoet, ikke versjonert):
  - Linje 1: modell (cyan, fet) | `effort <nivå>` (lilla, fra `effort.level`) | mappe (blå) | branch (gul) | `tok <brukt> / <kontekstvindu> ($kostnad)` (turkis). Grå skillestreker.
  - Linje 2: `ctx` / `5h` / `7d` i prosent, grønn under 50 %, gul fra 50 % og rød fra 80 %.
  - Testet med ekte input fra økta. Midlertidig dumpfil i `%TEMP%` er slettet.
  - Begrensning: Claude Code sender ikke den absolutte tokenkvoten i abonnementet, bare prosent av 5t- og 7d-grensen. «Totalbruk mot tilgjengelig» vises derfor som tokens mot kontekstvindu og API-tilsvarende kostnad, og abonnementsbruken som prosent på linje 2.
- **Loggcommit pushet** til `docs/pre-prd-research-og-brainstorm`.
- **Issue-opprydding:**
  - #21 manglet labelen `sesjonslogg` og har fått den.
  - Lenkene til sesjonsloggene i #12, #13, #14, #16, #17, #18, #19 og #21 pekte på grenen `sesjonslogg/github-issues`, der filene 995–997 ikke finnes. Det samme gjaldt to kommentarer i #16 og #19. Alle lenkene peker nå på commiten der loggfila ble lagt til (permalenke), slik at de overlever merge og sletting av grenen. Lenkene er sjekket mot GitHub-API-et.

- **#16 BSU-fradrag:** Brukeren avklarte at det ikke gis fradrag uten skatt, men at BSU likevel gir god rente. `addendum.md` har fått en ny parameterrad for BSU-fradrag, regel 9 (fradrag = min(10 % av årets innskudd, årets skatt), beregnes i desember, 0 kr uten skatt, ikke overførbart, spillet forklarer at BSU lønner seg gjennom renta) og regneeksempel 6 (17-åring på frikort, 10 000 kr i 12 mnd, gir fradrag 0 kr og saldo 10 576 kr mot 10 289 kr på sparekonto, regnet med skript etter regel 2). `updated` er satt til 2026-10-31. Beslutningen er kommentert på #16.
- **#16 Arbeidstid:** Brukeren bestemte at vi følger vanlige norske lover og regler. `addendum.md` har fått en ny parameterrad for arbeidstidsgrenser (aml. §§ 10-4 og 11-2) og regel 10: grensen følger skolepliktstatus, ikke alder alene, og sommerjobb bruker grensene for uker uten skole. Nattarbeid (§ 11-3) modelleres ikke, fordi spillet ikke har klokkeslett. Grensen for 18+ (9 t/40 t, § 10-4) kommer ikke fra researchen, men er lagt til fra loven. Beslutningen er kommentert på #16. Endringene i addendumet er ikke committet.

### Åpne punkter
- Resten av #16: opplysningstekster om forenklinger (tariffsatser, BSU-snittrente, bankgodkjenning) (#16).
