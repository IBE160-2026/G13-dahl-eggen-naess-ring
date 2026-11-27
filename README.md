# G13 — PromptSquad

Gruppeprosjekt i **IBE160 Programmering med KI** ved Høgskolen i Molde, høsten 2026 (15 studiepoeng).

Repoet inneholder gruppens applikasjon og dokumentasjon av utvikling, testing og kvalitetssikring med KI.

## Medlemmer

- Magnus O Dahl
- Sara Eggen
- Sara H Naess
- Nora Ring

## Appen: LifeMode

LifeMode er et spill om liv og penger for 15–20-åringer i Norge. Spilleren lever fem år av et liv, noen minutter om gangen, og hvert valg får følger senere. Spillet bruker norske regler og tall for 2026, som BSU, frikort, kreditt først fra 18 og mopedlappen fra 16. Trivselen teller også, så å bli rik for enhver pris gir en hul seier. Første versjon har ingen KI. En motor regner ut alle tallene, og hendelsene er skrevet på forhånd.

**Status (26.11.2026):** planleggingen er ferdig (PRD, arkitektur, UX, 73 storyer i 10 epics). Byggingen starter med sprintplanleggingen. Slik kjører og tester du appen, kommer her med den første storyen (1.1).

## Hvor finner du hva

Planleggingen ligger i `.docs/` og øktene i `.logs/`. Begge mappene starter med punktum, så de kan være skjult i filutforskeren.

| Hva | Hvor |
|---|---|
| Krav (PRD) | [prd.md](.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md) og [addendum.md](.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/addendum.md) |
| Regelsett v1 og regneeksemplene | [brief-addendum](.docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md) |
| Arkitektur | [ARCHITECTURE-SPINE.md](.docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/ARCHITECTURE-SPINE.md), [SOLUTION-DESIGN.md](.docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/SOLUTION-DESIGN.md) og [diagrammer](.docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/diagrams/) |
| UX: utseende og oppførsel | [DESIGN.md](.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/DESIGN.md) og [EXPERIENCE.md](.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/EXPERIENCE.md) |
| Epics og storyer | [epics.md](.docs/planning-artifacts/epics.md) og [diagrammer](.docs/planning-artifacts/epics-diagrams/) |
| Beslutninger | `.memlog.md` i hver planleggingsmappe, [PR-ene](https://github.com/IBE160-2026/G13-dahl-eggen-naess-ring/pulls?q=is%3Apr) og [issuene](https://github.com/IBE160-2026/G13-dahl-eggen-naess-ring/issues?q=is%3Aissue) |
| KI-øktene | [.logs/](.logs/), én mappe per gruppemedlem, og den første promptloggen i [arkiv/promptlogg](arkiv/promptlogg/) |
| Kvalitetssikring av planene | reviews og valideringsrapporter i hver planleggingsmappe, og [klarhetsgjennomgangen](.docs/planning-artifacts/readiness-review-2026-11-23/report.md) før epics |
| Tidligere runder | research, brainstorming, design thinking, skisser og UX-runde 2 i `.docs/`. De er beholdt som spor av prosessen |

## Slik jobber vi

- Vi planlegger og bygger med [BMAD](https://docs.bmad-method.org/) og Claude Code.
- Endringer går inn i `main` via pull requests. Fra første story merges ingenting på rød CI eller uten review: enten i GitHub (kommentarer eller godkjenning fra en annen i gruppa) eller live med gruppa, og etter en live-gjennomgang kan forfatteren merge selv (#132).
- Hver KI-økt avsluttes med en sesjonslogg i `.logs/<bruker>/`. Det som gjenstår blir GitHub-issues med label `sesjonslogg`.

## Vurdering

- [Sensorveiledning del 1](docs/sensorveiledning/sensorveiledning-ibe160-del1.md) – hva sensor vurderer i del 1 (applikasjon og prosess, 70 %). Originalen ligger som [PDF](docs/sensorveiledning/sensorveiledning-ibe160-del1.pdf).
