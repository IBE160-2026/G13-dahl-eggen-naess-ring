# PRD Consistency Review — IBE160-G13

Reviewed 2026-11-23 against the final PRD (`prds/prd-IBE160-G13-2026-10-22/prd.md`, status final, updated 2026-11-22), Rule Set v1 and the worked examples (`briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md`), and the architecture spine (`architecture/architecture-IBE160-G13-2026-11-09/ARCHITECTURE-SPINE.md`). Files reviewed: `EXPERIENCE.md`, `DESIGN.md`, `mockups/index.html`, `.working/round3/concept.md` and `.memlog.md`. Precedence: the PRD wins on product rules, and the UX spines win over the mockup.

Line references: `EXP:n` means EXPERIENCE.md line n. `DES:n` means DESIGN.md line n. `HTML:n` means mockups/index.html line n. `CON:n` means concept.md line n. `PRD:n` means prd.md line n. `RS:n` means the brief addendum line n. `ARCH:n` means ARCHITECTURE-SPINE.md line n.

## Verdict

**Consistent in most places. Fix 4 high findings before stories are written.** The money core matches Rule Set v1 exactly where it matters. That covers worked examples 24 and 25, the 604 kr and 302 kr offer texts, the wage of 139.40 kr/h, rule 16 spending, the card figures 188/350/51 months/5 508 kr, the 939 kr payment plan, and the moped value of 10 772 kr. The job and shift rules follow the new FR-47/FR-52. No finding is critical.

The 4 high findings:
- Flow 5 has the month loop the wrong way round.
- The crisis family option breaks "always offered".
- The interest formula in the spine is wrong.
- The event screen drops the balances that FR-13 requires.

There are 15 medium findings. Most are PRD consequences that the "less text" rule dropped without a PRD change: the month summary contents, the December tax line, FR-35, FR-40 first-time disclosures, money actions, and progress after the planned activities. A few are additions that the PRD or the architecture doesn't have yet, such as wellbeing bands sent by the server.

## Findings

### High

- **[high] Flow 5 opens an event *after* the quiet-month hub, in the same month, in a month that isn't active.** UX says: "08: «Fortsett» → 12: the mirror dims, the phone in his hand is cracked … (Markus, 16, November event)" (EXP:255–257). The hub CTA "Fortsett til desember" links to `#hendelse` (HTML:678), and the event and result use November's balances ("Brukskontoen hadde 2 364 kr", HTML:787). The result's Fortsett then returns to November's hub. PRD says: "When it opens, the engine runs rule 1 up to interest on savings … and the player sees the highlight event or the quiet-month summary. When the player continues, the engine applies the planned activities …, works out wellbeing, checks rule 8, and opens the next month" (FR-49, PRD:611). "The highlight event is always shown when the month opens" (FR-49, PRD:615). "By default they are months 1, 4, 7, and 10 of each in-game year" (FR-46a, PRD:706). UJ-6 calls November "a quiet month" (PRD:114). A developer could wire Continue so that it opens an event inside the current month. *Fix:* re-stage Flow 5 so that the event opens a month (for example October, an active month): the event comes first, then the result, then that month's hub. Point the November hub CTA at the next month's opening. Keep the November figures for Flow 3 only.

- **[high] The crisis hides "ask family" after the first ask. The PRD says it is always offered.** UX says: "Asking family and doing nothing are always offered, except that the family can't be asked twice in one crisis" (EXP:114). The prototype drops the option once `k.asked` is set (HTML:862). PRD says: "Asking family and ignoring the crisis are always offered" (FR-32b, PRD:1109). "Asking again in the same event or crisis month shows the same answer, moves no money, and doesn't use up a crisis step" (FR-27, PRD:1025). This states a rule in the spine that contradicts two Core FRs. *Fix:* keep "Spør mamma" on every step. After the first ask, it shows the stored answer again ("Mamma har allerede lånt deg 500 kr"), with no money and no step used.

- **[high] The interest explanation states a false equation.** UX says: "the sheet shows 23 500 kr × 2,87 % = 56 kr this month" (Flow 4 climax, EXP:250). The interest component row says "balance × rate = this month" (EXP:122). DESIGN calls it "a three-line calculation" (DES:260). PRD/Rule Set says: "Monthly interest is `balance × annual rate / 12`" (rule 2, RS:69). 23 500 × 2.87 % is 674 kr, a year's interest. NFR-4 requires figures that are "correct, explainable". This is the climax of UJ-3, the game's main lesson about interest. A content or engine developer who follows the spine would render an equation that doesn't hold. (The prototype sheet lists balance, yearly rate and this month as rows, HTML:1057, without stating the equation.) *Fix:* change both spine lines to "balance × yearly rate ÷ 12 = this month" (for example «23 500 kr × 2,87 % ÷ 12 = 56 kr»), and add the ÷ 12 row to the sheet.

- **[high] The event screen drops the balances that FR-13 requires.** UX says: "12 | Event | … | Dimmed mirror, options as actions with kroner (FR-13)" (EXP:55). The event shows only the scene, a sentence and three options (HTML:771–782). PRD says: "In a month with a highlight event, the player sees the situation together with their balance, savings, debt, and fixed costs, and picks one of a few options" (FR-13, PRD:625). The "Can't afford" state (EXP:162) depends on the player seeing what they have. *Fix:* add a compact facts row to surface 12 in the spine (current account, savings, debt and fixed costs, engine figures) and draw it.

### Medium

- **[medium] The quiet-month summary drops content that four FRs put there.** UX says: "Quiet month | 08 | The heading is "Denne måneden", the chips show wage, spending and interest. No event text." (EXP:152). The hub shows three chips only (HTML:663–666). PRD says: "the month summary shows what was spent in total, with a few example purchases that fit the player's age and spending level" (FR-23, PRD:973). "The month summary lists each activity and its cost" (FR-53, PRD:807). "The month summary shows each transfer" (FR-45, PRD:893). "The month summary says when the player takes over the bills at 18" (FR-23, PRD:976). *Fix:* add an expandable "Hva gikk pengene til?" row to surface 08 (example purchases, the activity lines, savings transfers, the note at 18). The chips can stay as they are.

- **[medium] The year end has no tax or BSU deduction line, and the spine doesn't mention the December summary.** UX says: "Year end | The year's money, what changed, the average wellbeing, and a teaser for the next unlock (FR-15)" (EXP:116). The prototype's year end shows in/out/interest only (HTML:864–870). PRD says: "The December summary shows the year's tax and the expected BSU deduction, which is paid when the player continues" (FR-21, PRD:952). "The December summary marks the deduction as expected" (FR-49, PRD:618). FR-22 asks for a plain «BSU-fradrag: 0 kr …» when there is no tax (PRD:960). *Fix:* add a "December" state to 08 or 23 with the year's tax and the expected BSU deduction, marked as expected, including the 0 kr wording.

- **[medium] FR-35 (what a choice opened or closed) was dropped without a PRD change.** UX says: "FR-35 … an extension in the PRD. Not drawn, after the team dropped «Åpnet/Stengt». The outcome list shows what changed." (EXP:286). PRD says: "After a choice, the game shows what the choice opened or closed" (FR-35, PRD:1160). The team aims to build every Extension (§4.4). UJ-1 step 4 says "future opportunities change" (PRD:81). *Fix:* either show the FR-35 flag texts as lines in the outcome list (for example «Du kan nå kjøpe moped»), or ask the PM to record FR-35 as left out, using its "If left out" clause.

- **[medium] FR-40 first-time disclosures have no pattern. Only the "Om tallene" page exists.** UX says: "27 | About the numbers | `#tallene` | 26 | Disclosed simplifications (FR-40)" (EXP:70). Nothing in the component or state patterns covers first-time display. The prototype page lists 5 of the 26 texts, and 2 of them are cut short (HTML:895). PRD says: "Each disclosure is shown the first time its mechanism or feature appears, behind an info icon or under "Hvorfor?" … Once per account" (FR-40, PRD:1219–1222). *Fix:* add a "Disclosure" component: a one-time info chip on the first appearance (D3 on the interest sheet, D25 on the spending choice, D26 on the first plan, and so on) that is seen once per account. Use the full D-texts on "Om tallene".

- **[medium] Progress before continuing isn't shown "after planned activities, marked as such". The trigger status and the month 59/60 warnings are missing.** UX says: "Savings target | … progress from current account plus savings, the price, when it opens, and what's missing" (EXP:109). The prototype shows 79.8 % with "Kveld med venner −200 kr" planned (HTML:668, 939). PRD says: "Before the player continues, progress is shown after the planned activities' payments, marked as such" (FR-57, PRD:876; FR-9c, PRD:552). "Before the player continues, the money view shows the rule 8 trigger status … In month 59, the warning says … In month 60 …" (FR-49, PRD:617). Worked example 25 has 77.8 % after the activities (RS:235). *Fix:* add the "etter planlagte aktiviteter" marking to the savings target and the life goal, a trigger-status row in 17, and month-59 and month-60 warning states.

- **[medium] The money view leaves out FR-45 money actions.** UX says: "17 | Money (bank) | … Accounts, interest, BSU, card, savings target and life goal, what comes next, buy and sell, spending, transactions" (EXP:60). The card row lists "balance, limit, how the bill is paid …, card use on/off" (EXP:112). PRD says the player can "deposit in BSU …, or withdraw the whole BSU", "pay extra on the card", "pay off a consumer loan, a family loan, or a payment plan early", "stop an everyday cost that has no binding period" (FR-45, PRD:897–904; FR-23, PRD:977). *Fix:* list the missing actions in the 17 row and the Credit card row: withdraw BSU (whole, closes, deduction repaid), extra card payment, pay off early, and stop an everyday cost. The latter is shown with its binding period.

- **[medium] The job view leaves out the rule 10 limit and the no-job state.** UX says: "16 | Job | … Job, wage, hours, offers, ask for more or fewer hours, one-off shifts, end extra shifts, quit" (EXP:59). The prototype shows the wage, the fixed hours and the extra shifts but no limit (HTML:972–973). PRD says: "The job view shows … the rule 10 limit, the expected monthly pay" (FR-56, PRD:856). "With no job: the view shows the open job offers, or when the next one unlocks" (FR-56, PRD:862). *Fix:* add a "Maks 40 t/uke" row (or 12 in grunnskole), pay that includes placed one-off shifts, and a no-job state.

- **[medium] Wellbeing bands, and a server-sent band, go beyond the PRD and the architecture.** UX says: "under it is bad, from it to 9 above is ok, 10 above and up is good. Stress is mirrored … The server sends the band with the figure." (EXP:124). It also says "Fritid and Sosialt: «bra» (60 and up) / «ok» (50–59) / «lite» (under 50)" (EXP:155), and "Bands follow the PRD threshold (50, rule 12)" (DES:180). PRD says the threshold is "The ending wellbeing needed for a real win, 50" (glossary, PRD:220). Rule 12 ties social life to 20, not 50: "If social life is then below 20, stress rises by 5" (RS:79). AD-13 sends "raw integers where the UI needs a number (… wellbeing …)" (ARCH:201), with no band. The 60 cut-off and the band on each part are new rules that the engine would have to own. *Fix:* ask the PM to add the bands to FR-33 as configuration, and the architecture to add `band` to the player view. Alternatively, make them a frontend display rule over the threshold in the view. Revisit the Sosialt band, since its rule threshold is 20.

- **[medium] The summer job is ranked as an ending choice, but its wages have a system cause.** UX says (prototype): «Sommerjobben i 2027 +16 728 kr … Uten sommerjobben ville du hatt 18 000 kr mindre.» This is ranked first in three of the four endings (HTML:877, 879). PRD says: "System causes: wages, tax, the mobile cost … have a system cause" (FR-36, PRD:1181). "Choices with no kroner effect aren't ranked" (FR-42, PRD:1256). FR-39 compares "with the option in the same event" (PRD:1209). Only one-off shift pay links to its choice (FR-47, PRD:939). *Fix:* replace the entry with an event choice or an activity group. Optionally, add a sentence to the spine's Ending row that job wages are never ranked.

- **[medium] The Flow 5 echo invents a cause link that FR-36 can't store, and the spine cites the wrong FR.** UX says: «Tidligere valg: I januar i fjor satte du pengegaven på sparekontoen. Den dekket de 136 kr du manglet.» (EXP:259, HTML:786). It also says "Past choice note … Replaces "Ekko" (FR-37 cause links)" (EXP:127). PRD says: "An echo badge is shown only for effects that carry a cause link to an earlier choice" (FR-37, PRD:1190). Shared causes are proportional only for interest and debt (FR-36, PRD:1179). A savings top-up is a payment-order transfer (FR-45), so no earlier deposit "covered" the 136 kr. FR-37 is "Echo badges", and FR-36 is "Cause links". *Fix:* use an echo the engine can derive (for example the extra-shifts note, HTML:726, or card interest linked to an earlier purchase). Correct the citation to "FR-37 echo badges, from FR-36 cause links".

- **[medium] Flow 4 (UJ-3) uses a different message and drops two journey steps.** UX says: "10: Banken: «Tre fjerdedeler! Du har 79,8 % av Lappen.» 17: he taps «+56 kr rente (i)»" (EXP:248–249). PRD says: "The bank sends a message: his savings have grown, because they have earned interest. He … presses "Hvorfor?" … It shows the real figure: NOK 3,000 earns NOK 84 in a year … The game points him to other ways of earning" (UJ-3, PRD:105–108). "One more bank message reports savings interest: the first month the interest earned so far passes NOK 50" (FR-55, PRD:843). *Fix:* make the Flow 4 trigger the FR-55 interest message, which opens the interest sheet or "Hvorfor?". Add the earning pointer (hours, summer job) as a line on the sheet, or as a tip (FR-19).

- **[medium] Days and times of day appear in a game with no days or times.** UX/prototype says: «Konsert lørdag?» and an invitation card reading "Lørdag · −450 kr · Sosialt +8" (HTML:901, 923). Message times are "14:02", "11:30" and "i går" (HTML:901–903), and the thread shows "I dag 14:02". PRD says: "No days or times: the plan has no days, times, or dates within the month (D26)" (FR-52, PRD:793). D26 says «Spillet følger ikke dager eller klokkeslett» (RS:303). The content model has no time or day field. *Fix:* drop the weekday from the invitation card and the times from the inbox. Show "Ny" / month labels instead (the "Nye i november" grouping already does this).

- **[medium] Missing account surfaces and states that the PRD and the architecture define.** UX lists 03, log in, and 04, forgot password (EXP:46–47), and the states at EXP:146–166. None covers:
  - (a) The new-password page that the reset link opens. Architecture: "Reset link: `{PUBLIC_BASE_URL}/nytt-passord#token=<token>` … The page reads it … and posts the token and the new password" (AD-12, ARCH:190). FR-3: after a reset every device is logged out (PRD:448).
  - (b) Email already in use. "The game then says the address is in use and points to **Log in** and the forgotten-password link" (FR-1, PRD:425).
  - (c) Logged out from elsewhere. "Its next action shows the login screen" (FR-5, PRD:472).
  - (d) Nickname character rules. "letters, including æ, ø, and å, digits, spaces, and hyphens … The screen says the nickname … needn't be their real name" (FR-1, PRD:419). The hint reads only «2–16 tegn. Bare du ser det.» (HTML:619).

  *Fix:* add surface "04b Nytt passord" (two states: set password, and link used or expired). Add the states "E-posten er i bruk", "Logget ut på en annen enhet" and "Ugyldige tegn i kallenavnet", and extend the nickname hint.

- **[medium] One-off shift pay contradicts Rule Set rule 1. The UX doesn't say when the pay lands.** UX says: "Jobb lists this month's one-off shifts with name, hours and pay" (EXP:126). The plan row reads "+558 kr lønn" (HTML:697), but the hub's wage chip stays at 8 457 kr (HTML:664). PRD says: "Its pay … paid with this month's wage" (FR-47, PRD:939), and also "no wage is paid outside the income step" (FR-47, PRD:942). Rule Set says: "Activities and the month plan never add hours or wages to the current month" (rule 1, RS:68). The income step runs when the month opens (FR-49). *Fix:* this is a PRD and Rule Set conflict, not a UX error. Ask the PM to say when one-off pay is credited (on continuing, or next month's income step). Then add one line to the spine's Add list row, and update the hub chip or the bank list.

- **[medium] The BSU line on the interest sheet states a rule the game doesn't have.** UX says (prototype): «BSU gir 5,61 % rente, men pengene er låst til bolig.» (HTML:1059). The spine wants "the BSU rate" on the sheet (EXP:122). PRD says: "The player can withdraw the whole BSU. It then closes for the rest of the playthrough, and any BSU deductions received are taken from the payout at once" (FR-22, PRD:963). D22 says «I spillet kan du bare ta ut hele BSU-en» (RS:299). *Fix:* «BSU gir 5,61 % rente. Du kan bare ta ut alt på en gang, og da forsvinner fradraget.» The text comes from the engine (AD-13).

### Low

- **[low] The phone event mirrors the Rule Set's unexpected expense, which the PRD says isn't an event.** UX says: "Mobilen gikk i bakken … «Reparer skjermen −2 500 kr»" as an event with three options (EXP:257–258, HTML:779–781). PRD says: "Example unexpected expense NOK 2,500 (broken phone screen)" (RS:33). "An unexpected expense is a deduction, not an event, so it doesn't use an active month" (FR-24, PRD:988). The figures are declared (CON:71), so the severity is lowered. *Fix:* add one line in Coverage: this is a story event (FR-17), and FR-24 broken-phone expenses arrive as a deduction with a "Hvorfor?" system cause.

- **[low] UX additions the PRD doesn't name: absolute calendar years and the year chart's monthly history.** UX says: "shown as a month name, age and year ("November · 16 år · 2027")" (EXP:30). Ending texts read «Sommerjobben i 2027» and «hytteturen i 2028» (HTML:877–878). The year chart totals are "Så langt i år: inn … ut … rente" (HTML:756). PRD says: "Month 1 is January of the year the player turns 15" (rule 11, PRD:246), with no start year. The frontend "never calculates" sums (NFR-4). *Fix:* ask the PM or the architecture to fix a start-year setting, and add the year's monthly totals to the player view (AD-13 "other fields … engine stories", ARCH:399).

- **[low] The invitation "Nei takk" and the disabled ask buttons are rules or inputs the PRD doesn't have.** UX says: "An invitation has one action, "Legg i planen", plus "Nei takk"" (EXP:135). It also says "Offer open | 16 | The two ask buttons are disabled, with «Svar på tilbudet først.»" (EXP:156). PRD says: "Ignoring a message only means missing what it offered" (FR-54, PRD:829). NFR-7's input list has no "decline invitation" (PRD:1388). FR-47 says only "one request at a time" (PRD:938). *Fix:* state that "Nei takk" on an invitation is client-only (it just closes), or remove it. Mark the ask-lock as [ASSUMPTION] for the PM.

- **[low] Terms differ from the PRD glossary, and the D-texts still use the banned words.** UX uses:
  - "Tidligere valg" / "Past choice note" for **Echo badge** (PRD:180)
  - "trivselsmål" for **Threshold** (PRD:220; EXP:124)
  - "Kveld" / "frie kvelder" / "Slot row" for **Activity slot** (PRD:164)
  - "Hvor mye bruker du i måneden?" / Lite–Vanlig–Mye for **Spending level** low/normal/high (PRD:216)
  - "Penger" / "Banken" for **Money view** (PRD:199)
  - "Welcome back" for **Recap**

  The UX rejects "forbruksnivå" and "plass" as jargon (EXP:209). D25, however, reads «I spillet velger du et forbruksnivå» (RS:302), and D26 reads «noen få ledige plasser» (RS:303). D12 and rule 10 say the player sets their hours («Du velger hvor mange timer du jobber i uka», RS:289, and "In the game, the player sets weekly hours", RS:77), which contradicts FR-47 (PRD:930). *Fix:* add a glossary-mapping table to the spine. Ask the Rule Set owner to reword D12, D25, D26 and the rule 10 sentence.

- **[low] The crisis sale value doesn't follow rule 14 for the prototype's own timeline.** UX says: «Selg mopeden +8 152 kr» in August 2029 (month 44) (HTML:862, 1101). The moped was bought in May 2027, month 17 (HTML:534; the bank's 6-month value of 10 772 kr confirms it). PRD/Rule Set says: resale = start × (1 − 15 % × months owned / 12). 27 months gives 11 645 × 0.6625 = **7 715 kr** (rule 14, RS:81; worked example 19 row "Gift … 27 months", RS:163). 8 152 kr is the figure for 24 months. This figure isn't declared. *Fix:* use 7 715 kr.

- **[low] The year chart's 10 h wage is off by 5 kr.** UX says: August and September income of 6 036 kr ("Fast jobb", HTML:533). Rule Set says: "with 10 h a week the wage would be NOK 6,041" (worked example 25, RS:234). The chart is declared (CON:68), but the figure is derivable. *Fix:* 6 041 kr.

- **[low] The prototype's wellbeing start values differ from worked example 26.** UX says: `USUAL={st:25,so:50}` (HTML:682), shown as "Vanligvis 50". Worked example 26 says: "stress 30 and social life 55 … stress falls by 5 to 25. Social life stays at 55" (RS:240). The hub's 68 then needs an activity (+5) instead of no activities. *Fix:* use social 55, so that case "none" = 68 and case a = 74 match the answer key.

- **[low] The card warning and the payment plan leave out a figure each.** UX shows the debt, this month's interest and the minimum-only cost (HTML:849), and the plan shows "939 kr i mnd" (HTML:862). PRD says: "The game shows the card's interest rate" (UJ-4 step 2, PRD:136). The plan "option shows the monthly instalment against what the player has left each month" (FR-32b, PRD:1110). *Fix:* add «22,6 % rente i året» to the facts card and «Du har ca. … kr igjen i måneden» to the plan option.

- **[low] The age and story differ between flows (age declared, the rest not).** Flow 2 is "Markus, 15", and its climax is "the teaser names the licence" (EXP:226, 230). The recap shows the car licence (32 500 kr) at 16 (HTML:845), while UJ-2's teaser is the moped licence (PRD:92). Flow 3 is "Markus, 17" and Flow 5 is "Markus, 16" for the same November figures (EXP:235, 255). Flow 7 says «Du brukte 15 000 kr av pengegaven» (EXP:275), while Flow 5 and the prototype say the gift went to savings (EXP:259, HTML:786). *Fix:* name the moped licence and 12 000 kr in Flow 2. Use one age for the November flows (16, as declared in CON:73). Make the Flow 7 story match.

- **[low] The sign-up preview puts the nickname and an amount into game text on the client.** UX says: "nickname with a live preview" and "Emma's preview bubble updates as he types" (EXP:45, 218). It renders «Hei Mak! Konsert lørdag? Billetten er 450 kr.» (HTML:635). The architecture says: "the frontend never inserts it into game text" (AD-13, ARCH:201). It "prevents … figures put into text outside the backend" (ARCH:196). *Fix:* treat the bubble as UI chrome with no amount («Hei Mak!»), or drop it.

- **[low] The spine doesn't say which strings come from the engine.** UX sets strings that carry game data as patterns: «Du har spurt om flere timer. Line svarer i desember.» (EXP:157). «Fritid 72 gir deg 3 frie kvelder. Snittet ditt er 61. Trivselsmålet er 50.» (DES:257). PRD/architecture says: "The frontend owns only UI chrome text" (AD-13, ARCH:201). *Fix:* tag pattern strings as [engine] or [UI] in the Voice table.

- **[low] The player information text leaves out two NFR-3 items.** UX says (prototype): «Spillet ligger hos Supabase i Tyskland. Serverne våre hos Railway lagrer logger …» (HTML:822). NFR-3 says: "the attempt limits briefly process network addresses, so … network addresses count as personal data" (PRD:1346), and the text must name "which services handle the data" (PRD:1354). The backend runs at Railway, EU West (ARCH:223). AD-12 makes it "a static page … reachable before any account exists" (ARCH:191), while UX shows it only inside sign-up and the menu (EXP:120). *Fix:* add the network-address line and the server location, and link the page from the first screen and the login screen too.

- **[low] Smaller drops and wording issues:**
  - FR-13/FR-54 event copy in the phone isn't mentioned (PRD:625, 828).
  - «Slutter nå» for extra shifts that end "from the next month" (HTML:973; FR-47, PRD:941).
  - The spending cards show money only, not the social −2/+2 (FR-23, PRD:972), and claim «Det de fleste velger» (HTML:928).
  - The savings-target sheet offers "Moped, ny" to a moped owner (HTML:1066; FR-29, PRD:1052).
  - The ending pill uses «lavt» while the hub uses «Tungt nå» (HTML:882, 692).
  - The goal card for goal 2 omits "no debt at 20", and the card for goal 3 omits the 60 000 kr price and the month-56 deadline (HTML:639; FR-9a, PRD:536–538).
  - The licence layer is exclusive (none/moped/car), so it can't show a moped and a car licence together (EXP:107).

## Declared examples that are fine

These are declared in concept.md §"Invented figures" (CON:67–73). Where the arithmetic can be checked, it matches the rule set:

- **Pengegave 18 500 kr and its three choices.** The figure is within the 10 000–30 000 kr range (FR-11). The first month's interest is 44 kr (18 500 × 2.87 % / 12 = 44.2), which matches rule 2.
- **Phone event 2 500 / 1 800 / 0 kr.** The split of 2 364 kr from the current account and 136 kr from savings follows the FR-45 payment order and worked example 25's 2 364 kr. 79.8 % → 72.1 % and → 74.2 % are arithmetically right against 32 500 kr.
- **Crisis figures.** 700 kr overdue (2 × the 350 kr minimum), a 500 kr interest-free family loan (FR-27), and 939 kr a month for 12 months (worked example 12). "Neste krise … tidligst i november" fits a 2-month cooldown after a crisis in August.
- **Ending amounts.** Other than 17 270, 16 728 and 5 508 kr, the ending amounts are invented. The 17 270 kr line matches FR-39 and worked example 28.
- **Activity spend of 3 150 kr by kind.**
- **One-off shift names and hours.** The pay is right: 4 × 139.40 = 557.6, giving 558 kr, and 5 × 139.40 = 697 kr.
- **Spending examples and effects.** The amounts are right: 60/75/95 % of 8 457 kr is 5 074 / 6 343 / 8 034 kr under rule 16.
- **Moped value of 10 772 kr.** 11 645 × (1 − 0.15 × 6/12) = 10 771.6 under rule 14.
- **Age 16 instead of UJ-6's 17.** Wages are the same (139.40 kr/h under 18), and month 23 is in Vg1 with a 40 h limit.
- **The year chart's monthly figures, apart from the 6 036 kr above.** The July figure of 16 728 kr is worked example 1, the summer job at 16.

## Consistent areas checked

- **Wages and money (worked examples 24 and 25):**
  - 139.40 kr/h under 18 (job view).
  - Income 8 457 kr, moped insurance 250 kr, spending 6 343 kr, "−6 593 kr brukt", interest 56 kr, current account 2 364 kr, savings 23 556 kr, and 79.8 % of 32 500 kr.
  - Free time 72 gives 3 slots, and 4 again at 10 h.
- **Hours (FR-47, FR-56):**
  - Ending extra shifts: "4 frie kvelder i stedet for 3 … 604 kr mindre" (UJ-6, worked example 25).
  - The hours offer is the answer to last month's request: +2 h, "302 kr mer", next month's slot count, Ja/Nei, lapses at month end. Asking for more or fewer is one request at a time, with the answer next month.
  - No extra-shift offer while extra shifts run. Hours can't be set directly.
- **One-off shifts (FR-47, FR-52):** they take one slot, have no wellbeing effect and no date, are listed in the job view and placed from the plan, and the plan total covers activities only.
- **Plan (FR-52, FR-53):** tap-to-place with no dragging, × removes for free, «Samme som i oktober», an empty slot has no effect, and activities show their cost and effects (event options don't, FR-13 #79).
- **Spending (FR-23, rule 16):** low/normal/high at 60/75/95 %, "Gjelder fra desember", activities on top.
- **Card at 18 (FR-26, FR-31, worked example 12, UJ-4):**
  - The card warning in May 2029 is month 41, which equals worked example 17a's W. The crisis is in month 44. Both are after month 37.
  - The figures are 10 000 / 188 / 350 kr, 51 months and 5 508 kr. The warning says the player "couldn't pay", without scolding, and "Spør om flere timer" is answered in June.
- **Crisis (FR-32):** "Valg n av inntil 3", a way out on every step, ends when ignored or solved, and money goes to the overdue amount first (500 of 700 kr).
- **Endings (FR-41 to FR-43):**
  - Four endings, with "goal not reached" never framed as failure. The loss text reflects wellbeing.
  - Three facts. Ranking by size (16 728 > 15 000 > 9 450, apart from the system-cause issue above).
  - The hollow win takes third place for the choice that hurt wellbeing most.
  - The ending is read-only and "Spill på nytt" goes to the goal. Login after the ending lands on it.
- **Wellbeing (FR-33):** the score, the three parts, the threshold of 50 with exactly 50 counting, the average once month 19 is calculated (the hub is in month 23), and "Vanligvis n" for usual against this month.
- **Room (FR-34):** layers from flags, at most 6 (3 drawn), the change shown on the choice's own view (result, or the hub after a sale), and a text alternative for every state. Selling the moped removes it and brings the bus back from next month (FR-29).
- **Savings target and open options (FR-57, FR-48):**
  - The target uses current account plus savings and shows "fra 18 år" and «Mangler 6 580 kr».
  - Upcoming costs and activity spend by kind.
  - Open options show "Mangler", a lock with the age, and one moped at most. A sale asks once and shows what it changes.
- **Unlocks and teasers (FR-18, FR-15, FR-16):**
  - Post-its follow the FR-18 table.
  - The year-end and recap teasers name the next age unlock (the car licence at month 23).
  - The recap shows where the player is, the current account, messages this month, the plan, one button, and "Fortsett i november".
- **Messages (FR-54, FR-55):** read-only, new this month grouped as "Nye i november", nothing about reading stored (cleared in the open page only, #112), the bank's 75 % message once, an invitation placed through "Legg i planen", "Alle de frie kveldene er brukt."
- **Account (FR-1 to FR-5, FR-44):**
  - Email typed once with a check step (WCAG 3.3.7), password of at least 8, nickname 2–16 that only the player sees and that can be changed in the menu.
  - "Forbli innlogget" unticked at sign-up and login.
  - A neutral login failure and the pause message. Reset gives the same answer whether or not the address exists, and the link works once for 60 minutes.
  - Change password needs the current one and logs out other devices. Log out on all devices. Delete needs the password and can't be undone. A new life asks for confirmation.
- **Saving and devices (FR-6 to FR-8):** «Lagrer …» locks the options, «Prøver fortsatt …», «Spillet ble oppdatert på en annen enhet.», and offline is readable with the options locked.
- **Access (NFR-1, NFR-2):** 320 px with no horizontal scroll, 44 px option targets, nothing by colour alone (money and wellbeing words), polite live region, focus on the heading.
- **Architecture:** the server renders game text and figures (AD-13), as stated in the Foundation (EXP:26–29). The player information includes the Railway and Vercel log notes (NFR-11, AD-14). The start order is goal before avatar (FR-9a), and the avatar recolours the mirror (FR-10).
