---
title: Svar på refleksjonsspørsmålene i PRD-tilbakemeldingen
date: 2026-11-13
svarer-på: tilbakemelding-prd.md §7
status: ferdig, bekreftet av teamet 2026-11-13
---

# Svar på refleksjonsspørsmålene

Svarene bygger på PRD-ens `.memlog.md` og reviewene `review-2026-11-11.md` og `review-2026-11-11-solutions.md`, og teamet har bekreftet dem.

## 1. Hvordan sjekket vi at KI-forslagene om de fire nye spillområdene ikke motsa eksisterende krav, og hva fant vi?

Månedsplanen, telefonen, jobbvisningen og pengevisningen kom inn 10. november fra et revisjonsforslag Claude laget (`revision-proposal-2026-11-10-game-loop.md`). Vi sjekket dem i fire steg:

1. **Skriptsjekk underveis.** Mens forslaget ble lagt inn, regnet Claude ut tallene med skript. Én kontroll fant en konflikt med regel 12 i Rule Set v1: hvis aktivitetene påvirket trivselen varig, ville «pengejageren» gå fra 34 til 65 i trivsel. Da forsvinner den hule seieren, som er en kjerneregel. Vi endret det slik at aktivitetene bare teller den måneden de skjer.
2. **Uavhengig review 11. november.** Fire review-linser kjørte hver for seg uten å se hverandres funn. Tre av dem gikk gjennom innholdet, og den fjerde (prose) gikk gjennom språket. De fant 113 funn. Flere var reelle motsigelser mot eksisterende krav:
   - **Rekkefølge for betaling:** FR-45 og FR-23/FR-26 sa forskjellige ting om hvilken konto aktiviteter betales fra.
   - **Kuttlisten:** henvisningene pekte på feil punkter etter at nye punkter ble lagt øverst.
   - **UJ-6:** brukerreisen stemte ikke med sitt eget regneeksempel (38 % mot «halvveis»), og den kolliderte med mopeden Markus allerede hadde i UJ-4.
   - **Sommerjobben:** den ble fortsatt behandlet som en hendelse, så den ville bli blokkert.
   - **Tilbudsmeldinger:** de var definert på tre ulike måter.
   - **Krise ved «fortsett»:** aktiviteter som ble trukket ved «fortsett», kunne utløse en krise på nytt.
3. **Team-beslutninger.** De 12 beslutningene (D1–D12) som fulgte av reviewen, ble tatt av et teammedlem (sarahnaess) og lagt inn. Ingenting ble lagt inn uten at noen i teamet sa ja.
4. **Uavhengig kontroll av tallene.** Et teammedlem (sarahnaess) regnet de nye tallene i regneeksempel 25–28 og 26c/d på nytt i et regneark og fant dem i orden (memlog 2026-11-11).

**Hva vi lærte:** KI-forslaget var internt konsistent, men passet ikke alltid med kravene som fantes fra før. De fleste motsigelsene oppsto der et nytt område berørte et eksisterende FR. Reviewen fanget dem, men bare fordi vi kjørte den på hele PRD-en og ikke bare på endringene.

## 2. Hvilke av tallene 42, 46 og 37 i FR-9 og FR-33 har vi regnet ut selv, og hvilke bygger på KI-forslag vi ikke har kontrollert?

Tallene 42, 46 og 37 er trivselen en «pengejager» ender på med vektene for mål 1, 2 og 3. Det er det verste tilfellet: hver aktivitetsplass fylles med aktiviteter på effektgrensen (regneeksempel 26c). De skal vise at den hule seieren holder, altså at alle tre ligger under terskelen 50.

| Hva | Hvem regnet | Kontrollert av |
|---|---|---|
| Selve tallene 42, 46 og 37 | Claudes skript, 11. november. Før det ga en feil i eksempel 26c tallene 41/44/37 | To review-linser (også KI) anslo uavhengig «ca. 42/46/37–38». Sarahnaess regnet eksempel 26c på nytt i et regneark og fikk de samme tallene |
| Reglene tallene regnes fra (regel 12, ±10 per aktivitet, tak på ±15) | Teamet bestemte reglene etter forslag fra Claude | Teamet |
| Vektene (40/30/30, 50/25/25, 30/30/40), terskelen 50 og startverdiene (stress 20, sosialt 60) | Claude foreslo dem ut fra research, og teamet godtok dem. De er valgte tuningverdier, ikke utregninger | Merket «Tuning» i parametertabellen, med frist ved playteststart. Playtesten avgjør om de holder |

**Ærlig svar:** Utregningen ble først gjort av KI, og to KI-linser kom fram til det samme. Tallene er likevel kontrollert av et menneske: sarahnaess regnet dem på nytt i et regneark. Det som ikke er regnet ut, er vektene og terskelen. Claude foreslo dem ut fra research, og de testes først i playtesten.

**Hva vi gjør med det:** En sjekk i kode fanger tallene, for innholdssjekken feiler hvis noen av dem når 50 eller mer (FR-33). Vektene og terskelen er tuningverdier som vurderes på nytt etter playtesten (OQ-8).
