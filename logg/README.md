# Promptlogg

Denne mappen inneholder alle prompts gruppen har sendt til Claude Code i dette repoet. Loggen skrives automatisk.

## Hvor finner jeg hva?

- `prompts/<navn>.md`: én fil per gruppemedlem, med navn fra `git config user.name`. Nyeste prompt ligger nederst.

Hver person har sin egen fil, slik at loggene ikke gir merge-konflikter når flere jobber samtidig.

## Format

Hver prompt logges som én oppføring:

````markdown
## 2026-10-08 14:32:05

| Felt | Verdi |
|---|---|
| Dato | 2026-10-08 |
| Klokkeslett | 14:32:05 (UTC+02:00) |
| Person | Myggsaa |
| Branch | `main` |
| Økt-ID | `3f9a1c2e` |
| Verktøy | Claude Code |

```text
Selve prompten, ordrett.
```
````

| Felt | Betydning |
|---|---|
| Dato / Klokkeslett | Når prompten ble sendt, i lokal tid med tidssone |
| Person | Git-navnet til den som skrev prompten |
| Branch | Git-branchen personen sto på |
| Økt-ID | De første 8 tegnene av Claude Code-øktens ID. Prompts med samme ID hører til samme samtale. |
| Verktøy | Hvilket AI-verktøy prompten ble sendt til |

## Slik fungerer det

En `UserPromptSubmit`-hook i `.claude/settings.json` kjører `.claude/hooks/log_prompt.py` hver gang noen sender en prompt i Claude Code i dette repoet. Skriptet legger til en oppføring i personens loggfil.

Krav for hvert gruppemedlem:

1. Python 3 installert (`python3` eller `python`).
2. Siste versjon av repoet hentet (`git pull`), slik at hooken er med.
3. Claude Code startet på nytt etterpå, og hooken godkjent hvis Claude Code spør.

Loggfilene blir commitet og pushet sammen med det øvrige arbeidet.

## Begrensninger

- Bare prompts sendt via **Claude Code i denne mappen** blir logget. Prompts i ChatGPT, claude.ai i nettleseren eller andre verktøy kommer ikke med automatisk.
- Prompten logges ordrett. **Ikke lim inn passord, API-nøkler eller andre hemmeligheter**, for loggen pushes til GitHub.
