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
- **#16 Arbeidstid:** Brukeren bestemte at vi følger vanlige norske lover og regler. `addendum.md` har fått en ny parameterrad for arbeidstidsgrenser (aml. §§ 10-4 og 11-2) og regel 10: grensen følger skolepliktstatus, ikke alder alene, og sommerjobb bruker grensene for uker uten skole. Nattarbeid (§ 11-3) modelleres ikke, fordi spillet ikke har klokkeslett. Grensen for 18+ (9 t/40 t, § 10-4) kommer ikke fra researchen, men er lagt til fra loven. Beslutningen er kommentert på #16.
- **#16 Opplysningstekster:** `addendum.md` har fått seksjonen «Simplifications the game discloses» med seks spillertekster på norsk: D1 skatt/forskuddstrekk, D2 tariffsats og ingen lovbestemt minstelønn, D3 BSU-rente som SSB-snitt, D4 forenklet bankgodkjenning, D5 lånerenten på 15 % er et anslag, D6 alle satser er 2026-tall og holdes faste. Tekstene vises første gang mekanismen dukker opp, og samles på en «Om tallene»-side. Med dette er alle punktene i #16 dekket.
- **Committet og pushet:** endringene i addendumet ligger i `ac65f67` på `docs/pre-prd-research-og-brainstorm` (PR #22). #16 er lukket med en kommentar som viser til `ac65f67` og `b62c6c8`.

- **#21 Aldersgrense:** Aldersgrensen for samtykke er 13 år i dag (pol. § 5, Lovdata). Regjeringen har sendt på høring et forslag om å heve den til 15 år. Forslaget var ikke vedtatt i juni 2026, og lovforslaget ventes i Stortinget innen utgangen av 2026. Funnene står i møtenotatet. Kommentaren på #21 og lukkingen ble stoppet av tillatelsesregelen og venter på at brukeren sier ja.
- **#19:** Brukeren kommer tilbake med svar på de fire valgene etter teammøtet.
- **#13 Speltesting:** Brukeren har spilt Koll på cashen. Funnene står i `.docs/planning-artifacts/research/playtest-competitors-2026-10-31/notes.md`: grafikken er for barnslig, og velvære bør kobles direkte til resultatet som kjennetegn for LifeMode. Kjennetegnet holdes åpent for teamet, men brukeren tror de lander på det. PersonalFinanceLab er ikke prøvd ennå.
- **Brukerundersøkelsen «Unge og penger»:** 133 svar er analysert i `user-research.md` (ny seksjon «Results»). Rådataene ligger utenfor repoet. Viktigste funn: angeren handler om valuta for pengene, bare 38 % tenker fremover, familien er den viktigste kilden, BSU og kreditt er minst forstått, og mange ønsker seg fond og investering.
- **Møtenotat** for torsdag 2026-11-05: `.docs/planning-artifacts/meeting-prep-2026-11-05.md`.
- Committet i `2f8d28b`.
- **Underagent:** startet på resten av researchen (#14, #17 og de åpne spørsmålene fra domeneresearchen). Rapporten skrives til `.docs/planning-artifacts/research/remaining-pre-prd-research-2026-10-31/research.md` og var ikke ferdig da loggen ble skrevet.

- **Beslutninger fra brukeren:** fond og investering holdes utenfor første versjon foreløpig, og det blir ingen foreldreundersøkelse i denne omgangen. Begge beslutningene er skrevet inn i `user-research.md` og møtenotatet. Brukeren ville ikke ha issues for dette.

### Åpne punkter
Ingen nye issues. Om vi trenger en kort konsepttest før PRD-en, står som tema i møtenotatet.
