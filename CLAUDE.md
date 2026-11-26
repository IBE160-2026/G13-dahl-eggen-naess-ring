## Hva gjelder nå

Les disse når en oppgave trenger kravene, reglene eller designet:

| Hva | Fil |
|---|---|
| Krav: hva spillet gjør | `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md` og `addendum.md` |
| Regelsett v1 og regneeksemplene | `.docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md` |
| Arkitektur: hvordan det bygges | `.docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/ARCHITECTURE-SPINE.md` og `SOLUTION-DESIGN.md` |
| Utseende og oppførsel | `.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/DESIGN.md` og `EXPERIENCE.md` |
| Epics og storyer | `.docs/planning-artifacts/epics.md` |
| Sprintstatus | `.docs/implementation-artifacts/` (lages av `bmad-sprint-planning`) |
| Playtesten | `.docs/planning-artifacts/playtest/` |
| Hva sensor vurderer | `docs/sensorveiledning/sensorveiledning-ibe160-del1.md` |

Er de uenige, gjelder PRD-en for hva spillet gjør og spinen for hvordan det bygges. `PRODUCT.md` i roten er et sammendrag for designverktøyet, og PRD-en gjelder foran den.

**Resten av `.docs/` er historikk.** Les det bare når noen ber om det, eller når du må vite hvorfor noe ble bestemt:
- reviews og valideringsrapporter, og `.memlog.md`-filene (beslutningsloggene)
- `research/`, og alt i brief-mappa utenom `addendum.md`
- `ux-IBE160-G13-2026-11-17/` (erstattet av UX-en fra 2026-11-11) og `.working/`-mappene i UX
- `readiness-review-2026-11-23/`, `meeting-prep-2026-11-05.md`, `.docs/brainstorming/` og `.docs/design/`
- `arkiv/` og `.logs/`

Ikke flytt eller slett historikken. Den er sporene av prosessen, som sensor vurderer.

## Sesjonslogg

Når en oppgave eller økt avsluttes, før sluttoppsummeringen, bruk `sesjonslogg`-skillen: dokumenter Oppgave + Plan + Resultat + åpne punkter i `.logs/<bruker>/`, og før åpne punkter som GitHub Issues med label `sesjonslogg`. Skillen committer loggfila lokalt; push gjør du selv. Gruppens egne regler for commit og språk gjelder foran dette.
