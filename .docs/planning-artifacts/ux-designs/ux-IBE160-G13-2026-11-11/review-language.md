# Plain-Language Review — IBE160-G13

Scope: every Norwegian string in `mockups/index.html` (script: `V.*`, `INBOX`, `RES`, `END`, `CH`, `BAD`, `TALL`, `PI`, `SPEND`, `GOALS`, `openSheet`, `live()`, aria-labels), quoted UI strings in `EXPERIENCE.md` and `DESIGN.md`, checked against NFR-8, the team's "no unnecessary text" rule and the feedback in `../decisions.md`. Screen numbers follow `mockups/oversikt.html`. Reviewed 2026-11-23. No existing file was changed.

## Verdict

**Close, but not ready to freeze.** The voice is right: no scolding, no quiz framing, verbs on options, signed kroner on chips, and the a-forms (lønna, lista, uka, renta, kantina) are used consistently. The team's fixes (Kveld 1, Tidligere valg, Hvor mye bruker du i måneden?, trivselsmål) hold. What's left falls into three groups:

1. **Money jargon in the 18+ screens** (20 card warning, 21 crisis, 27 Om tallene): «minstebeløpet», «betalingsavtale», «BSU», «skattekort/frikort», «tariffavtale». These are the screens where a teenager most needs to understand the words, and where the words are hardest.
2. **One concept, several words**: frie/ledige kvelder, Lappen/Lappen (bil)/Mopedlappen, ekstravakter/enkeltvakter, livsmål/sparemål/trivselsmål/«målet», Penger/Banken, brukt/ut/forbruk.
3. **Sentences that say something slightly untrue or unexplained**: «604 kr mindre i måneden» (it's one month), «30 000 kr tilgjengelig hver måned», «Valgene venter», «+1 920 kr i november», a trivselsmål that sounds like a rule but is never explained.

Counts: **10 high, 27 medium, 28 low.**

## Terms to settle (one word per concept)

| Concept | Used now | Suggest |
|---|---|---|
| An evening not taken by school or work | «fri kveld», «ledig kveld», «Kveld 1», «Ledig», «kveldene er brukt» | **fri kveld** is the unit. Use **planlagt / tom** for its state, not «ledig» (a teenager hears fri = ledig). «3 frie kvelder · 1 planlagt», sticker «Planlegg 2 kvelder», empty row «Tom». |
| What you put on an evening | «aktivitet», «Fritid», «Jobb», «vakt», «Kveld med venner» | **aktivitet** (fritid) and **vakt** (jobb). Rename «Kveld med venner» to «Henge med venner» so it doesn't repeat «Kveld 1». |
| The 20-year goal | «livsmål», «målet», «Målet var 100 000 kr», «Du klarte målet» | **livsmålet** whenever it stands next to another goal. «Du klarte målet» can stay as a heading, since it stands alone. |
| The pinned purchase | «sparemål», «Sparemål: Lappen», «Hva sparer du til?» | **sparemål**. Keep it. |
| The wellbeing threshold | «Trivselsmålet er 50», «Målet er 50», «Målet var 50» | **trivselsmålet** every time. Never bare «målet». |
| Driving licence | «Lappen», «Lappen (bil)», «Sparemålet Lappen», «Mopedlappen» | **Billappen** and **Mopedlappen**. «Lappen» alone reads as the moped licence the player already has. |
| Recurring extra hours vs one-off shifts | «Ekstravakter», «Enkeltvakter i november», «Vaktene», «Kveldsvakt» | **ekstravakter** (the +4 t/uke deal) and **vakter i november** (one-offs). Drop «enkeltvakter», which differs from «ekstravakter» by three letters. |
| Money going out | «brukt» (hub chip), «Ut» (Året, year end), «Hverdagsforbruk» (bank), «forbruk» (live message) | **brukt** in chips and sentences. «Ut» is fine as a chart legend. Drop «forbruk» completely, since the team already rejected «forbruksnivå». |
| The bank area | tab «Penger», screen «Banken», link «Åpne banken», sender «Banken» | Tab **Bank** (short, and matches the screen), or title the screen «Penger». Pick one. |
| Unread message | «Ikke åpnet» (aria), «1 ny», «2 nye» | **ulest** in aria, «ny/nye» on screen. «Åpnet» is a word the team already rejected. |
| Phone, PC, browser | «enhet», «alle enheter», «Andre enheter logges ut» | **mobil eller PC**, or **overalt**. |
| The boss | «Line», «Line · Butikken», «sjefen», «Tilbud fra sjefen» | **Line** in text. Use «Line (sjefen din)» once, in the job card. |
| «brukt» meaning three things | «−6 593 kr brukt», «Kjøp en brukt mobil», «kveldene er brukt» | Keep **brukt** for money and second-hand goods. Evenings are **fylt opp**. |
| Wellbeing "bad" word | «lite» (Fritid/Sosialt), «høyt» (Stress), «Tungt nå» (score), «lavt» (ending pill) | Use the score's words on the ending too, in past tense: «Det gikk bra» / «Helt ok» / «Tungt». |

## Findings

Ranked by how likely a 15-year-old is to misread the text, highest first.

### High

- **[high]** 20 `#kort` (and `k_nei`) — «Bare minstebeløpet · 51 måneder, 5 508 kr i rente» → «Betaler du bare det minste (i) · 51 måneder · −5 508 kr i rente». «Minstebeløp» is bank jargon a 15–18-year-old won't know, and the line is a label without a verb. You can't avoid the idea, so add an (i) sheet: «Minstebeløpet er det minste banken lar deg betale hver måned. Resten blir stående, og du betaler rente av det.» Use the same (i) in `k_nei`.
- **[high]** 21 `#krise` — «Be om betalingsavtale · 939 kr i mnd · I 12 måneder fra september. Kortet sperres.» → «Del opp hele kortgjelden · −939 kr i måneden · 12 måneder fra september. Kortet blir sperret.» «Betalingsavtale» is jargon. The real trap is that the screen just said «Du skylder 700 kr nå», and 939 kr a month looks like a mistake unless it says the *whole* debt is split up. «mnd» is an abbreviation, and the amount has no sign. Also fix the log line «939 kr i måneden, og kortet er sperret.» → «−939 kr i måneden i 12 måneder. Kortet er sperret.»
- **[high]** 05 `#start` — «Gjeldfri med buffer · 30 000 kr tilgjengelig hver måned det siste året» → «Ingen gjeld og en buffer (i) · 30 000 kr på konto hele det siste året». «Tilgjengelig hver måned» sounds like 30 000 kr a month in income. «Buffer» is adult finance talk, so explain it: «Penger du har liggende i tilfelle noe skjer.» Or drop the word: «Ingen gjeld, 30 000 kr i reserve».
- **[high]** 08 `#hjem` sticker, 15 `#plan` — «2 ledige kvelder» (sticker), «3 frie kvelder · 2 ledige» (plan), «Ledig» (empty row) → sticker «Planlegg 2 kvelder», plan «3 frie kvelder · 1 planlagt», empty row «Tom». *Fri* and *ledig* are synonyms in everyday speech. The difference (free from school and work vs not yet planned) is invisible, so «3 frie, 2 ledige» reads like 5 evenings or a contradiction. Count what is done, not what is left.
- **[high]** 16 `#jobb` — «Slutte med ekstravaktene? Fra desember får du 4 frie kvelder i stedet for 3, men sitter igjen med 604 kr mindre i måneden.» → «Slutte med ekstravaktene? I desember får du 4 frie kvelder i stedet for 3, og 604 kr mindre. Ekstravaktene slutter uansett etter desember.» The card above says the extra shifts run «ut desember», and Flow 3 says they end after December. So «fra desember … i måneden» falsely implies a lasting loss. The same sentence is quoted as a «Do» in EXPERIENCE.md → Voice and Tone, so update it there too. The row text «Slutter nå» after the button contradicts «fra desember»: → «Slutter etter november».
- **[high]** 08, 13, 17, 19, 23, 24, INBOX — «Sparemål: Lappen», «Lappen (bil)», «Mopedlappen», «Du har 79,8 % av Lappen» → «Sparemål: Billappen», «Billappen», «Mopedlappen». The player already has the moped licence («Mopedlappen henger på speilet»). A savings target called just «Lappen» reads as that one, and the result screen then says «Sparemålet Lappen: 79,8 % → 72,1 %». «Billappen» is the word teenagers use.
- **[high]** 17 `#penger` — «+1 920 kr i november» (chip under the total) → «+1 920 kr mer enn du brukte i november», or as a label: «Igjen etter november: +1 920 kr». It's the month's net, but nothing says so. A teenager will guess it's wage, interest or a deposit.
- **[high]** 17 `#penger`, 08 rente sheet — «BSU · Ikke åpnet · [Åpne]», «Til BSU», «BSU gir 5,61 % rente, men pengene er låst til bolig.» → «BSU (i) · Du har ingen ennå · [Start BSU]», and in the sheet «BSU er sparing til egen bolig. Den gir 5,61 % rente, men pengene kan bare brukes til å kjøpe bolig.» The acronym is never spelled out. «Ikke åpnet / Åpne» brings back the «Åpnet» word the team rejected, and «Åpne» can mean "open this view". «Til BSU» is offered when no BSU exists: disable or hide it until there is one.
- **[high]** 16 `#jobb`, 15 `#plan` — «Ekstravakter +4 t/uke ut desember» next to «Enkeltvakter i november» → keep «Ekstravakter», rename the second section «Vakter du kan ta i november». The two words differ by a few letters and mean different deals (recurring hours vs single evenings). The plan's Jobb tab and hint («Vaktene kommer fra Butikken») already say «vakter», so the section heading is the odd one out.
- **[high]** 08 `#hjem`, 23 `#aarsslutt`, 25 endings, 27 `#tallene` — «Trivselsmålet er 50.» (hub), «Trivselen din var 61 i snitt. Målet er 50.» (year end), «Trivsel i snitt · Målet var 50» right under «Spart · Målet var 100 000 kr» (ending) → «Trivselsmålet er 50.» everywhere, «Livsmålet: 100 000 kr» / «Trivselsmålet: 50» on the ending, and an (i) on the hub tile: «Trivselsmålet: Har du minst 50 i snitt når du fyller 20, har du klart deg både med penger og med livet.» This is text that sounds like a rule but isn't explained anywhere. The (i) under Om tallene → Trivsel doesn't mention it either. Bare «Målet» next to the life goal is ambiguous.

### Medium

- **[medium]** 12 `#hendelse` — «Den virker, men sprekkene går over halve skjermen.» → «Mobilen virker, men sprekkene går over halve skjermen.» «Den» points to a word that exists only in the handwriting on the mirror and in the hidden aria text. Screen readers and anyone skimming lose the referent.
- **[medium]** 13 `#resultat~repair` — «I januar i fjor satte du pengegaven på sparekontoen. Den dekket de 136 kr du manglet.» → «I januar i fjor satte du pengegaven på sparekontoen. Derfor var det nok der til de 136 kr du manglet.» «Den» can be the gift or the account. It was the account.
- **[medium]** 08 rente sheet vs 17 — «På sparekontoen 23 500 kr» while the bank and hub show «23 556 kr» → show the same figure, or label it «På sparekontoen 1. november». A teenager checking the sum will think the game is wrong. Flow 4 in EXPERIENCE.md repeats 23 500.
- **[medium]** 28 `#offline` — «Ingen nett. Valgene venter til du er på nett igjen.» → «Ingen nett. Du kan se, men ikke velge, før du er på nett igjen.» «Valgene venter» suggests choices are queued and will be sent later. They are locked. The same text is in EXPERIENCE.md → State Patterns.
- **[medium]** 17 `#penger` — «Hvor mye bruker du i måneden? · Av lønna di. Aktiviteter kommer i tillegg.» → «Mat, klær og annet hverdagsliv. Aktivitetene i planen kommer i tillegg.» «Av lønna di.» is a fragment, and it reads as "a share of your wage" while the options show fixed kroner.
- **[medium]** 17 `#penger` — heading «Fremover» over «Kommer i desember» and «Aktiviteter i år» → «Utgifter», or split it: «Kommer i desember» as its own row and «Brukt på aktiviteter i år». «Aktiviteter i år» is the past, not «fremover».
- **[medium]** 08 sticker, 16 — «Jobb 14 t», «Fast 10 t/uke», «+4 t/uke ut desember» → «Jobb 14 t i uka», «Faste timer: 10 i uka», «Ekstravakter: +4 t i uka til og med desember». «t» on its own doesn't say per what. «ut desember» can be read as "out in December".
- **[medium]** 13 result chips — «Stress −2 lettere», «Stress +3 mer», «Stress ±0», «Sosialt +4 mer» → «Stress −2», «Stress +3», «Stress uendret», «Sosialt +4». The "sign and a word" rule is for money. On a wellbeing chip the label is already the word, and «−2 lettere» / «+4 mer» say the same thing twice. «±» is a maths sign many 15-year-olds can't read.
- **[medium]** 13 `k_nei` — «Betaler du bare minstebeløpet, tar det 51 måneder. Av de første 350 kronene går 188 kr til rente.» → «Betaler du bare det minste, tar det 51 måneder å bli kvitt gjelden. Av de første 350 kr du betaler, går 188 kr til rente.» «Tar det 51 måneder» doesn't say to do what. Mixing «kronene» and «kr» in one sentence is uneven. The chip «188 kr rente denne måneden» needs a sign: «−188 kr rente denne måneden».
- **[medium]** 27 `#tallene` Skatt — «Skatten regnes ut fra hele årsinntekten din med satsene for 2026. I virkeligheten kan arbeidsgiveren trekke 50 % av lønna til du har skattekort, eller når frikortet er brukt opp.» → «I spillet regnes skatten av alt du tjener i løpet av året, med 2026-regler. I virkeligheten kan sjefen trekke halve lønna i skatt hvis du ikke har skattekort, eller når du har tjent mer enn frikortet dekker (i).» «Satsene», «årsinntekten» and «frikortet» are jargon, and «til du har … eller når …» breaks the parallel. «Skattekort» and «frikort» can't be avoided for a summer-job teenager, so link them to a one-line (i).
- **[medium]** 27 `#tallene` Lønn and Alle satser — «Timelønna i spillet er minstesatsen i tariffavtalen for varehandelen (Virke/HK) fra 1. april 2026. Norge har ingen lovbestemt minstelønn …» / «Alle satser og beløp er 2026-tall. De holdes faste …» → «Timelønna er det laveste butikker må betale etter avtalen mellom arbeidsgiverne og fagforeningen (2026). Norge har ingen lov om minstelønn, så ekte lønn kan bli høyere eller lavere.» / «Alle priser, renter og lønner er fra 2026. De endrer seg ikke, selv om du blir fem år eldre i spillet.» «Minstesatsen i tariffavtalen», «Virke/HK», «lovbestemt», «satser» and «holdes faste» read like a government page.
- **[medium]** 27 `#tallene` — «Her er det spillet forenkler.» → «Dette gjør spillet enklere enn virkeligheten.» The word order invites the reading "here, it is the game that simplifies".
- **[medium]** 08, 16 — «+8 457 kr lønn», «Lønn i november 8 457 kr» → «+8 457 kr lønn før skatt», or say in Om tallene → Skatt when tax is taken. Om tallene says tax exists, but no screen shows it. A player with a real summer job knows pay arrives smaller.
- **[medium]** 07 `#gave` — «Spar halvparten, bruk resten · −9 250 kr» → «Spar halvparten, bruk resten · −9 250 kr brukt». A bare minus figure on a half-save option looks like the price of saving. The other options are clear: «18 500 kr spart», and «Kjøp gaming-PC −15 000 kr» (the verb carries it).
- **[medium]** 10 INBOX Banken — «Tre fjerdedeler! Du har 79,8 % av Lappen.» → «Over tre fjerdedeler! Du har spart 79,8 % av det billappen koster.» «Du har 79,8 % av Lappen» is literally "you have 79,8 % of the licence". Also 79,8 % is more than three quarters, so add «Over».
- **[medium]** 02 `#opprett`, 26 info — «Serverne våre hos Railway lagrer logger med IP‑adresser i USA i 90 dager, og Vercel lagrer logger i 1 time.» / «Ellers slettes det etter 12 måneder uten spilling.» → «Railway i USA tar vare på IP-adressen din i 90 dager når du spiller, Vercel i 1 time.» / «Spiller du ikke på 12 måneder, slettes alt.» «Serverne» and «logger» are jargon («logger» also reads as the verb). The word order puts the IP addresses "in the USA". «det» has no clear referent. EXPERIENCE says the 12-month line may only appear if that job is built.
- **[medium]** 02, 03, 26, EXPERIENCE state — «Forbli innlogget på denne enheten», «Logg ut på alle enheter», «Andre enheter logges ut.», «Spillet ble oppdatert på en annen enhet.» → «Hold meg innlogget her», «Logg ut overalt» (the sheet button already says that), «Du blir logget ut på andre mobiler og PC-er.», «Du har spilt videre et annet sted. Her er det nyeste.» «Enhet» is IT jargon, and «Forbli» is formal.
- **[medium]** 10 `#telefon` aria — «Ikke åpnet» (unread dot) → «Ulest». It's the standard word, and «åpnet» is the term the team dropped.
- **[medium]** tab bar, rail, 17 — tab «Penger», screen «Banken», link «Åpne banken» → one word (see Terms). Tapping «Penger» and landing on «Banken» makes the player wonder if they went to the right place.
- **[medium]** 23 `#aarsslutt` — «Et valg du tok i år, kan få følger senere.» beside the post-it «Lappen (bil) fra 18 år» → «Billappen åpner når du fyller 18. Den koster 32 500 kr.» The line is vague and slightly ominous, it doesn't relate to the post-it next to it, and the spec says the teaser names the next unlock.
- **[medium]** 17 live message, bank list — «Vanlig forbruk valgt.» / «Hverdagsforbruk −6 343 kr» → «Du har valgt Vanlig: ca. 6 343 kr i måneden.» / «Mat, klær og annet (Vanlig) −6 343 kr». This brings back «forbruk», the word family the team rejected with «forbruksnivå». The bank row should match the choice the player made above it.
- **[medium]** 20, 21, 19 — unsigned costs: «Rente denne måneden 188 kr», «939 kr i mnd», «Så langt i år: inn 46 714 kr, ut 50 343 kr, rente 652 kr» → «−188 kr», «−939 kr i måneden», «+46 714 kr inn, −50 343 kr ut, +652 kr rente». NFR-8 says money always has a sign and a word. These are the places it slips. Year end does this correctly.
- **[medium]** 17 sell sheet — «Du får 10 772 kr på brukskontoen og slipper 250 kr i forsikring.» → «… og slipper 250 kr i forsikring hver måned.» Without «hver måned» it reads as a one-time saving.
- **[medium]** 21 `#krise` — «Valg 1 av inntil 3» → «Valg 1 av maks 3». «Inntil» is formal, and some read it as "until". DESIGN.md and EXPERIENCE.md quote it too.
- **[medium]** 21 `#krise` ends — «Krisen er over», «Krisen er ikke løst», «Neste krise kan komme tidligst i november.» → «Kortet er betalt» / «Gjelden er ikke ordnet ennå», and «Gjelden vokser videre. Du får en ny sjanse senere.» The player was never told this is a «krise» (the heading was «Kortet er ikke betalt på to måneder»). «Tidligst i november» sounds like a cooldown rule that is never explained. With the payment plan, «Krisen er over» while 12 months of payments remain also oversells.
- **[medium]** 16 offer — «Du sitter igjen med 302 kr mer i måneden. Du får 3 frie kvelder i desember, og fra januar 3 i stedet for 4.» (302 is what the formula gives; the text varies by state) → as labels: «+302 kr i måneden etter det du bruker · Desember: 3 frie kvelder · Fra januar: 3 frie kvelder (nå 4)». Two time frames and a bare «3 i stedet for 4» in one sentence make the reader do sums. Here the team's own rule says labels beat sentences.
- **[medium]** 06 `#start` aria — «Genser 1» … «Genser 6» → «Blå genser», «Gul genser», «Grønn genser», «Lilla genser», «Svart genser», «Rød genser». Numbered names give screen-reader users nothing to choose by.

### Low

- **[low]** 11 `#melding` — «Alle de frie kveldene er brukt.» → «Alle de frie kveldene er fylt opp.» «brukt» already means spent money and second-hand.
- **[low]** 13 `#resultat~used` marker — «Ny brukt» → «Brukt mobil». "New used" reads as a joke or a typo.
- **[low]** 13 `g_bruk` — «Du kjøpte gaming-PC.» → «Du kjøpte en gaming-PC.» The article is missing.
- **[low]** 13 `g_spar` / `g_halv` — «Rommet er som før.» / «Sosialt gikk opp.» → drop the first (the player never sees a «rom», only the mirror), and «Sosialt +3» for the second (other screens use numbers). The chip «+44 kr rente neste måned» vs the explanation «44 kr den første måneden» should use the same words: «neste måned».
- **[low]** 17 — «Moped, brukt», «Moped, ny», sheet «Moped, ny, 29 000 kr» → «Brukt moped», «Ny moped», «Ny moped · 29 000 kr». Inventory word order, and two commas in a row in the sheet.
- **[low]** 19 `#aar` — post-it «Mopedlappen · Tatt» vs «fra 18 år» → «tatt». Capitalisation is inconsistent across the post-its.
- **[low]** 19 `#aar` — «Full jobb · fra 19 år» → «Fulltidsjobb · fra 19 år». «Full jobb» can mean a busy job.
- **[low]** 19 `#aar` — «Forbrukslån» as a gold unlock post-it → keep the unlock, but give it a neutral line, «Forbrukslån · mulig fra 18 år», so a loan doesn't read like a prize.
- **[low]** 19 `#aar` — «Rente · maks 100 kr» (strip label) → «Rente (0–100 kr)», or drop it. «maks» reads as a cap on interest.
- **[low]** 19 `#aar` — «Hele livet i spillet» → «Fra 15 til 20 år». «Hele livet» is grand for a five-segment bar.
- **[low]** 10 INBOX — tag «Utløpt» → «For sent». It's bureaucratic, and Jonas is a friend.
- **[low]** 15 `#plan` — «Samme som i oktober» → «Samme kvelder som i oktober». Same what?
- **[low]** 15 `#plan` — «Kveld 1 · Kveld med venner», aria «Fjern Kveld med venner fra kveld 1» → activity «Henge med venner». «Kveld» twice in one row.
- **[low]** 15 `#plan` — «Gratis» in the add list, «0 kr» on the placed row for the same activity → «Gratis» in both.
- **[low]** 24 `#velkommen` — «Planen · 1 av 3 kvelder», «Du er her · November 2027, 16 år» → «Planlagt · 1 av 3 frie kvelder», «Du er her · November · 16 år · 2027» (the timeline's order).
- **[low]** 25 endings — the wellbeing pill reads «42 lavt» while the hub says «Tungt nå» and the bars say «lite» → «42 · Tungt», «61 · Det gikk bra». Use one set of words.
- **[low]** 25 `#slutt-ikke` — «Du brukte penger på livet underveis, og det er lov.» → «Du brukte penger på livet underveis.» «Det er lov» sounds like an adult granting permission. Teenagers hear that as talking down.
- **[low]** 25 CH — «Hadde du latt være, ville du hatt 10 210 kr mer …» → «Hadde du droppet dem, ville du hatt 10 210 kr mer …». «latt være» has no object.
- **[low]** 25 CH headings — mixed forms: «Konserter og arrangementer», «Du brukte 15 000 kr av pengegaven», «Sommerjobben i 2027», «Du droppet hytteturen i 2028» → all nouns: «Konserter og arrangementer», «Pengegaven», «Sommerjobben i 2027», «Hytteturen i 2028». The amount column already shows the kroner.
- **[low]** 13 `k_mamma` — marker «Et råd» next to «Mamma … har ikke råd» → marker «Mamma svarer». The pun on «råd» is confusing. Also, Mamma can't lend in May 2029 (`k_mamma`) but lends 500 kr in August 2029 (crisis): add a reason or make it consistent.
- **[low]** 16, 13 — «Tilbud fra sjefen», «Sjefen svarer neste måned» vs «Line svarer» → «Tilbud fra Line», «Line svarer neste måned».
- **[low]** rail — aria «Meny, Mak» on a link whose visible text is «Mak · 16 år» → «Mak · 16 år, meny». Label-in-name (WCAG 2.5.3): the accessible name should start with the visible text.
- **[low]** 08 sticker — visible «2 nye», accessible name «2 nye» → aria «2 nye meldinger». Out of context, «2 nye» says nothing.
- **[low]** all money strings — `kr()`/`plain()` use non-breaking spaces correctly. But the hard-coded engine sentences («2 500 kr», «18 500 kr», «8 152 kr», «79,8 %», «2,87 %», «50 %») and `pct()` (`' %'`) use normal spaces, so «2 500 | kr» or «79,8 | %» can wrap at 320 px. Since the engine sends these sentences, put «NBSP between digit groups and before kr/%» into the engine's text contract.
- **[low]** 04 `#glemt~sendt` — «Finnes adressen hos oss, har vi sendt en lenke.» → «Har du bruker med denne e-posten, har vi sendt deg en lenke.» Still the same answer either way (FR-3), and less formal.
- **[low]** 17 `SPEND` — «Kantina av og til, klær iblant» → «Kantina av og til, nye klær noen ganger». «Iblant» is written language.
- **[low]** 17 live message — «Sparemålet er valgt.» → «Sparemålet er nå Billappen.» Say which one.
- **[low]** 13, 21, 25 scene aria — «Speilbildet er alvorlig.» → «Speilbildet ser alvorlig ut.» A reflection can't be serious, it can only look it.

## What already works

Keep these as they are:

- **01:** «Gjør de dyre feilene her.» Short, honest, a little cheeky. The lead line under it is fine too.
- **02:** «Hva skal vi kalle deg?» + «2–16 tegn. Bare du ser det.», «Sjekk at e-posten er riktig» / «Endre e-post», and the error messages («Skriv en hel e-postadresse, som navn@eksempel.no.», «Passordet må ha minst 8 tegn.», «Feil e-post eller passord.»). Plain, specific, no blame.
- **05:** «Hva vil du ha klart når du fyller 20?», «Start som 15-åring».
- **Options as verbs with signed kroner:** «Reparer skjermen −2 500 kr», «Kjøp en brukt mobil −1 800 kr», «Lev med sprekkene 0 kr», «Skru av kortet», «Spør om flere timer».
- **The «Hvorfor?» panel on 13:** «Reparasjonen kostet 2 500 kr. Brukskontoen hadde 2 364 kr. Resten tok banken fra sparekontoen.» This is the model for every explanation in the game.
- **Outcome lines:** «Mobilen er hel igjen.», «Sparemålet Lappen: 79,8 % → 72,1 %» (only «Lappen» needs to become «Billappen»).
- **The plan's Tidligere valg note:** «Du sa ja til ekstravakter i september. Derfor har du 3 frie kvelder i stedet for 4.» It names the cause, the month and the effect in two sentences.
- **Hub chips:** «+8 457 kr lønn · −6 593 kr brukt · +56 kr rente (i)». The rente sheet's first lines, «Banken betaler deg for å ha penger på sparekontoen. Jo mer du har der, og jo lenger, jo mer får du.», and «Skjønner».
- **Wellbeing words:** «Det går bra / Helt ok / Tungt nå», «25 lavt», «Vanligvis 50». Each status has a word, and none of them scolds.
- **Phone texts:** «Legg i planen / Nei takk», «Lagt i planen», «Du svarer med det du gjør, ikke med tekst.», and the senders' voices (Emma, Mamma, Line).
- **Job texts:** «Du spurte om flere timer. Vil du ha 2 timer mer i uka fra desember?», «Svar på tilbudet først.», «Du har spurt om flere timer. Line svarer i desember.», «Du sa ja.» / «Du sa nei takk.»
- **Plan texts:** «Velg i lista →», «Skole og jobb tar resten av uka», «Ferdig».
- **The spending choice:** «Hvor mye bruker du i måneden?», with «Lite / Vanlig / Mye», kroner and everyday examples («Matpakke, sjelden nye klær»), and «Dette bruker du nå» / «Gjelder fra desember».
- **Crisis:** «Du skylder 700 kr nå. Det finnes alltid en vei ut.», «Hun kan kanskje låne deg noe», «Mamma lånte deg 500 kr uten rente. Du betaler 100 kr i måneden.»
- **Endings:** «Du nådde målet, men det kostet · Pengene er der. Vennene og fritiden fikk lite plass.», «Målet ble ikke nådd denne gangen» (no failure framing), «Hadde du valgt å spare alt, ville du hatt 17 270 kr mer da du fylte 20.», «Spill på nytt», «Ferdig for nå».
- **Year end:** «2027 er over» with «+ inn / − ut / + rente» chips. «Låses opp etter hvert».
- **Om tallene → Tid:** «Tiden i spillet går bare når du spiller …» Clear and reassuring.
- **Menu confirmations:** «Livet du har nå, slettes og kan ikke hentes tilbake.», «E-posten og hele spillet ditt slettes. Det kan ikke angres.»
- **Mechanics:** the a-forms are consistent, the comma after inserted clauses is correct («Livet du har nå, slettes»), money uses a real minus sign (U+2212), and there is no alcohol or tobacco anywhere. No string scolds or frames anything as a test.
