# Design Thinking Session: IBE160-G13

**Date:** 2026-10-16
**Updated:** 2026-11-12, aligned with the final PRD
**Facilitator:** SE
**Design Challenge:** Help young people aged 15–20 understand how today's money decisions shape their options later, before those decisions cost real money.
**Requirements basis:** `planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md` (status: final, 2026-11-11). Where this document and the PRD disagree, the PRD applies.

---

## 🎯 Design Challenge

> *How might we help young people aged 15–20 understand how today's money decisions shape their options months and years later, before those decisions cost them real money?*

- **Users:** Young people aged 15–20 in Norway, especially those close to their first real money decisions: a first pengegave, a first job, a first credit card at 18. They play in short bursts, often on a phone. Parents and teachers may suggest the game, but they are not users in version one (PRD §2.2).
- **Constraints:** Student team, a playable version delivered in December 2026, zero running cost, minors as users, minimal personal data. No AI in version one; AI as game master is planned for V2 (PRD §1, §4.3). Norwegian rules and real 2026 figures.
- **Success:** Users can explain how an earlier decision affected a later outcome, and the learning feels self-chosen rather than like schoolwork. The PRD turns this into playtest targets: 70% or more can explain the link, and a median of 4 or higher on "it felt more like a game than schoolwork" (PRD §7.1).
- **Existing research:** Finans Norge 2025, and the market research and competitor table in the brief. The player survey «Unge og penger», 133 responses, 22–29 October 2026 (`planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/user-research.md`). The team's hands-on playtest of Koll på cashen and PersonalFinanceLab (`planning-artifacts/research/playtest-competitors-2026-10-31/notes.md`).
- **Research rule:** The survey investigated the problem only, without revealing the solution idea. At the time, the idea was an AI-driven money game; the final PRD has no AI in version one. With the survey done, the later steps work with the concept. Playtesting the game is a separate, later step (PRD §7.1).

---

## 👥 EMPATHIZE: Understanding Users

**Sources and methods.** This step builds on the player survey «Unge og penger» (133 responses; `user-research.md`) and the team's competitor playtest notes. The methods are survey synthesis and empathy mapping. There were no interviews in this round, so the survey's free-text answers are the qualitative source. Percentages are of all 133 respondents.

### User Insights

1. **They know their balance, but not their future.** 88% know roughly how much money they have right now. Only 38% think about how a purchase affects their money months from now, and 39% often run out before they get more.
2. **Regret comes from small things that add up, not from big decisions.** The most frequent regrets are snacks, takeaway and drinks, then clothes, trend buys and collectibles such as blind boxes and Pokémon cards. «Jeg kjøper smågodt veldig ofte og pleier å angre ved slutten av uken når jeg ser hvor mye penger det blir til sammen.»
3. **Family is both the safety net and the teacher.** 68% get money from parents, and 88% learned most about money from family. In the trip dilemma, 26% would borrow from parents or friends. Of the 36% who had an unexpected expense that was hard to pay, about half got help from family.
4. **They want to learn, and they feel nearly ready.** 63% want to learn more about money, and 64% feel ready to make their own money choices at 18. Yet only 39% understand credit cards and consumer loans well, and 44% understand BSU well (26% among 15–16-year-olds).
5. **Credit is something they have not tried yet.** 4% have used a credit card or consumer loan, and 6% buy now pay later. Only one respondent chose either in the trip dilemma.
6. **Social pressure shows in what they regret, not in what they report.** Only 14% say they feel pressure from friends to spend. But the free text describes a jacket that was trending on TikTok and a laptop bought «bare på grunn av at jeg følte alle hadde en».
7. **Commitments catch them out.** A gym membership never used, and a subscription with a binding period they did not know about.
8. **They ask for plainer explanations, earlier.** They most want to learn budgeting and saving, interest, BSU, credit and loans, paying bills, and investing. Several ask for it to be explained more simply and taught earlier in school.

### Key Observations

**Surprises**
- **Saving is not the same as planning.** 73% save most or some of what they get, yet 39% often run out before the next money arrives.
- **Knowing a fact is not the same as acting on it.** 72% answered the credit-card question correctly (paying only the minimum costs more than the price). That is a quiz answer, not a habit. The PRD aims the game at behaviour: the player learns from what their own actions lead to, not from questions and answers (PRD §1).

**Pain points**
- Running out before the month ends: «jeg hadde ikke penger til andre ting, som feks mat i kantina, eller faste utgifter.»
- Being locked into something they did not understand: binding periods, memberships, and, for one respondent, BSU itself, where the money is locked and NOK 300,000 is «ikke nok til leilighet engang».

**Patterns**
- **Age gap.** The 15–16-year-olds understand BSU and credit least, and they are where the game starts.
- **Investing is a frequent wish**, including among 15–16-year-olds. It is out of version one (team decision, 2026-10-31).
- **They want to be taken seriously.** In the team's playtest, Koll på cashen felt slow, heavy and too childish for this age group. That matches the PRD's description of users who "want to feel grown-up" and don't want it to feel like homework (PRD §2).

**How the PRD answers these insights**

| Insight | Where the PRD answers it |
|---|---|
| 1. Not thinking ahead | Cause links, echo badges, "Hvorfor?" and "If you had chosen differently" (FR-36 to FR-39); upcoming costs in the money view (FR-57) |
| 2. Small things add up | Fixed and everyday costs with spending levels (FR-23); activity spend in the money view (FR-57); small purchases, trend buys and collectibles as event topics (FR-17) |
| 3. Family | Help from family, not always on offer and often partial (FR-27) |
| 4–5. Credit and BSU | Saving and BSU (FR-22); credit card from 18 (FR-26), worked through in UJ-4 |
| 6. Social pressure | Invitations from friends (FR-54, FR-55) and wellbeing with social life as one part (FR-33) |
| 7. Commitments | Everyday costs with a binding period, which can't be stopped before the period ends (FR-23); subscriptions with a binding period as an event topic (FR-17) |
| 8. Plain explanations | Tips in events (FR-19), "Hvorfor?" (FR-38) and disclosed simplifications (FR-40) |

**Limitations**
- A convenience sample, probably spread through the team's own networks and schools, so it is not representative.
- The behaviour is self-reported; peer pressure in particular looks under-reported.
- Only 8 respondents aged 19–20.
- No questions on the LifeMode concept, no parent survey, and no interviews in this round. Concept and gameplay are tested in the playtest (PRD §7.1).

### Empathy Map Summary

The young person aged 15–20, close to their first real money decisions. *Says* and *Does* come from the survey. *Thinks* and *Feels* are the team's interpretation of the free text.

| | |
|---|---|
| **Says** | "I'd like to learn more about money." "Explain it more simply, and earlier." «Jeg hadde ikke penger til andre ting.» "I'd ask my parents first." |
| **Thinks** | "I have control: I know what's in my account." "I'm nearly ready for 18." "A small purchase doesn't matter." "Credit is for later." |
| **Does** | Saves some of what they get. Buys snacks, takeaway and trend items on impulse. Asks family when money runs short. Has a bank card and savings account, but rarely credit. Learns from family, social media and their own mistakes. |
| **Feels** | Regret at the end of the week, when the small purchases add up. Caught out by binding periods. Pulled along by what others have. Wants to be treated as grown-up, not lectured. |

**Emotional arc in the PRD journeys.** The journeys follow one persona, Markus, and are design intent, not research data. They move from irritation (UJ-1, told to try it) to curiosity (UJ-3, his savings grew), panic and then tired relief (UJ-4, the credit card), and finally «a bit stupid, but proud» (UJ-5, the ending). The empathy map above supports the low points: running out, regret and feeling caught out are what the survey describes.

---

## 🎨 DEFINE: Frame the Problem

This step frames the problem as the final PRD answers it. The PRD is the basis; the framing here explains why its features exist and does not add requirements.

### Point of View Statement

> **A young person aged 15–20 in Norway, close to their first real money decisions, needs to see what today's choices lead to months and years later, and why, because they already know what is in their account but rarely think ahead, and the costs that hurt them most add up quietly from small purchases and commitments.**

Two narrower points of view support it:

- **At 18:** a young person about to get their first credit card needs to try credit before it costs them real money, because almost none of them have used it and fewer than half understand it well.
- **In everyday life:** a young person with school, a part-time job and friends needs to see that time is as limited as money, because their regrets are about what they got for the money, not about the amount.

### How Might We Questions

| How might we… | Where the PRD answers it |
|---|---|
| 1. …make the link between an earlier choice and a later outcome visible when it happens? | Cause links, echo badges, "Hvorfor?" and "If you had chosen differently" (FR-36 to FR-39) |
| 2. …make small purchases visible as they add up, without lecturing? | Spending levels and everyday costs (FR-23); activity spend in the money view (FR-57) |
| 3. …let players try credit and BSU safely before they meet them in real life? | Saving and BSU (FR-22); the credit card from 18 (FR-26); UJ-4 |
| 4. …make time feel as limited as money? | Month plan and activity slots (FR-52, FR-53); UJ-6 |
| 5. …make good money management mean more than the biggest balance? | Wellbeing (FR-33) and the four endings, including the hollow win (FR-41) |
| 6. …include family as a real part of the money world without making it a free rescue? | Help from family, not always on offer and often partial (FR-27) |
| 7. …make it feel grown-up and like a game, in a few minutes on a phone? | One in-game year a session (FR-15); tone and content (NFR-8); pace targets (PRD §7.1) |
| 8. …explain money in plain language without slowing play? | Tips (FR-19), "Hvorfor?" (FR-38) and disclosed simplifications (FR-40) |

### Key Insights

1. **The problem is foresight, not knowledge.** They know their balance (88%) and can answer a quiz question on credit (72%), but only 38% think months ahead. The game has to train the link between choice and consequence, not teach facts. This is why the PRD makes the player learn from what their own actions lead to, not from questions and answers (PRD §1).
2. **The gap is widest where the stakes are highest.** At 18, credit opens for the first time, and credit and BSU are the least understood terms. That makes 18 the turning point in a playthrough (UJ-4).
3. **Money, time and wellbeing are one problem.** The regrets are about value and satisfaction, and a part-time job costs free time. A player who wins only on money gets a hollow win.
4. **Family is part of the real environment.** Family is the main source of money, knowledge and help, so leaving it out would make the game less true to life. Making it a free rescue would teach the wrong lesson.
5. **Respect and pace decide whether they play at all.** They want to feel grown-up, they play in short bursts, and the closest competitor felt slow and childish. If it feels like schoolwork, it fails, however correct the content is.

**Assumptions to watch.** The PRD tests these in the playtest (PRD §7.1, §7.2):
- That understanding consequences in a game carries over to real choices. Measured as explaining an earlier choice's effect (70% or more) and the money quiz before and after.
- That results from testers aged 18–20 say something about 15–17-year-olds. The PRD notes this as a validity limit.
- That wellbeing makes sense without making the game complicated. Measured as explaining the wellbeing score and the ending (60% or more).

---

## 💡 IDEATE: Generate Solutions

The solution is set by the final PRD. This step does not decide *what* the game contains. It explores *how* the PRD's areas can be clear, engaging and easy to use, and gives the UX work a starting point. For each area there are two questions: how will the player understand it, and what makes them want to use it?

### Selected Methods

- **Brainstorming from the How Might We questions:** quantity first, judgment deferred. Each HMW from the Define step was used as a prompt.
- **Analogous inspiration:** apps and games this age group already knows. Life sims with need bars, farming games with seasons, bank apps with spending categories, chat apps, short-session learning apps, and year-in-review summaries. What they already understand needs no teaching.
- **SCAMPER on the PRD's features:** what can be combined (the phone and the month plan), simplified (fewer taps), or reversed (show the consequence first, then the number).
- **Provotypes:** deliberately extreme versions, to find the limits. They are not meant to be built.

Ideas are tagged by what they mainly help with: **[C]** clear, the player understands it; **[E]** engaging, the player wants to use it; **[U]** easy to use. Every idea stays within the PRD; the anchor shows where.

### Generated Ideas

#### Month plan (FR-52, FR-53)

*Understand:* time is as limited as money. *Motivate:* the month is the player's own to plan, with real trade-offs.

1. **The month as one bar, not a calendar.** School and work fill it as fixed blocks, and the free slots are the rest. When the player raises their hours, a work block visibly takes a slot. No days or times (D26). [C] — FR-52
2. **Activity cards you can read at a glance.** Price, plus small up or down icons for stress and social life, in a size that works on a phone. [C][U] — FR-53
3. **"Mangler 230 kr" on the card,** instead of a card that is greyed out without explanation. The player sees exactly what is missing. [C] — FR-53
4. **"Samme som forrige måned" as a prominent button,** so a quiet month takes a few seconds. [U] — FR-52
5. **The plan's running total** at the bottom, as in a shopping basket. [C] — FR-52 (engine figure)

#### Phone (FR-54, FR-55)

*Understand:* the world comes to the player through people they know. *Motivate:* it feels like their own life, not a task list.

6. **A phone that looks like a familiar chat app,** with a recognisable sender for each kind: a friend, mum, the boss, the bank. Unbranded. [C][E] — FR-54
7. **"Legg i planen" directly on an invitation,** so the player doesn't have to find the activity again in the month plan. [U] — FR-54 (an invitation is accepted by placing its activity)
8. **An offer shows its consequence before the player takes it:** "+604 kr i måneden, 3 aktivitetsplasser i stedet for 4". [C] — FR-47, FR-56
9. **Expired offers say «Utløpt»** and stay readable, so the player learns that opportunities have a deadline. [C] — FR-54
10. **A calm inbox:** at most three new messages a month, marked new, and no red badges piling up across months. [U][E] — FR-54, FR-55

#### Job view (FR-56, FR-47)

*Understand:* more hours give more money and less free time. *Motivate:* the player feels in control of their own trade-off.

11. **Hours control with a live preview** before confirming: "12 t/uke → 3 aktivitetsplasser · ca. X kr etter skatt". Which control is used is open (OQ-9). [C][U] — FR-56
12. **A pay slip the player already recognises:** gross, tax and net, with frikort explained when it applies. A real-life skill. [C] — FR-20, FR-21

#### Money view (FR-57, FR-45)

*Understand:* where the money goes and what is coming. *Motivate:* a goal they chose themselves, getting closer.

13. **The savings target as a picture with a progress bar:** the moped, "73 %", and "åpner om 7 måneder". [E][C] — FR-57
14. **«Småtteri» by kind,** as in a bank app's spending categories: what concerts and evenings out have cost this year. This is insight 2 made visible. [C] — FR-57 (activity spend)
15. **"Neste måned" as a list of bills,** like an invoice overview in a bank app, which also covers the survey's wish to learn about paying bills. [C] — FR-57 (upcoming costs)
16. **Bank words with a tap-to-explain,** which leads to "Om tallene". [C] — FR-40

#### Choices and consequences (FR-35 to FR-39)

*Understand:* every change has a cause the player can find. *Motivate:* curiosity about what an earlier choice led to.

17. **The ripple after a choice:** money, wellbeing, room and future opportunities change together in one short moment, so the link is seen, not explained. [C][E] — UJ-1 step 4, FR-34, FR-35
18. **The echo badge names its origin:** "Fra: Byturen, måned 38". [C] — FR-37
19. **"Hvorfor?" in the same place on every number that changed,** with an answer in one or two sentences and the choice as a link. [C][U] — FR-38
20. **«Låst opp» and «Stengt» chips** after a choice: "Mopedlappen kan tas fra 16". [C][E] — FR-35

#### Wellbeing (FR-33)

*Understand:* money alone isn't winning. *Motivate:* the player cares about the person, not just the balance.

21. **Three small meters (stress, free time, social life) with the threshold as a line,** and this month's activities shown as a lighter extension of the usual value. [C] — FR-33 (usual and this month)
22. **Show or hide a choice's wellbeing effect before the pick:** two variants to test, since this is open (OQ-9). [C] — OQ-9

#### Room (FR-34)

*Understand:* choices change what the player owns. *Motivate:* a visible life that grows.

23. **The room as the home screen,** where the newest belonging is gently highlighted, with a short text for screen readers. [E][C] — FR-34, NFR-2

#### Ending and replay (FR-41 to FR-43)

*Understand:* which choices mattered most. *Motivate:* wanting to try a different life.

24. **Five years as a short series of cards,** in the style of a year-in-review summary: the ending, the three choices that mattered most, and the hollow win explained if that's how it went. [E][C] — FR-41, FR-42
25. **A "hva om" card on each top choice,** leading straight to "Spill igjen". [E] — FR-39, FR-43

#### First minutes and sessions (FR-9 to FR-16, FR-19)

*Understand:* how the game works, without a tutorial. *Motivate:* reaching the first real choice fast and wanting to come back.

26. **No tutorial screen:** the first choice comes within about two minutes, and tips appear where they are needed. [U][E] — UJ-1, FR-19, §7.1
27. **The teaser at the end of a session as a cliffhanger card:** "Neste år kan du ta mopedlappen". [E] — FR-15, UJ-1
28. **The recap on return as three lines:** where you are, what changed, what's next. [C][U] — FR-16

#### Provotypes (not for building)

- **P1. No numbers at all,** only feelings and the room. *Learning:* numbers must be there (NFR-4), but showing the consequence first and the number second may read better.
- **P2. Everything as numbers,** like a spreadsheet. *Learning:* this is close to what made Koll på cashen feel heavy. Show the numbers that matter only where they are needed.
- **P3. The bank as a sarcastic narrator.** *Learning:* senders can have a voice, but the tone must respect the player (NFR-8).

### Top Concepts

Three concepts were chosen to prototype (2026-11-11). Together they cover the PRD's main success signal and the two newest, least tested areas.

1. **«Ringer i vannet»: the consequence moment** (ideas 17–20). After a choice, money, wellbeing, room and future opportunities change together. Later, an echo badge names the choice an effect came from, and "Hvorfor?" explains it. *Why:* this is the core of the PRD's main target, that 70% or more can explain how an earlier choice affected a later outcome (PRD §7.1). It answers insight 1, that the problem is foresight. PRD: FR-34 to FR-38.
2. **«Måneden på én skjerm»: month plan, invitations and work hours together** (ideas 1–3, 7, 8, 11). The month is one bar of school, work and free slots. Invitations go straight into the plan, and changing hours shows what it costs in slots before the player confirms it. *Why:* this is the newest part of the PRD and the hardest to understand, and the counter-metrics check whether planning is ignored (PRD §7.2). It answers insight 3, that money, time and wellbeing are one problem. PRD: FR-47, FR-52 to FR-54, FR-56.
3. **«Pengene som i en bankapp»: the money view** (ideas 13–15). The savings target is a picture with a progress bar, next month's costs are a list of bills, and «småtteri» shows activity spend by kind. *Why:* it makes small purchases that add up visible (insight 2) and builds on an app they already use, since 98% have a bank account and card. PRD: FR-45, FR-57.

---

## 🛠️ PROTOTYPE: Make Ideas Tangible

### Prototype Approach

**Hand sketches first, mobile first, then digital in the UX step.**

1. **Round 1: hand sketches at phone width.** Paper prototyping, with storyboarding to tie the screens into a sequence. Sara draws rough sketches by hand and scans them. Phone screens come first, because the PRD is mobile-first down to 320 CSS pixels (NFR-1) and the players play in short bursts on the phone.
2. **Review of the hand sketches.** Each sketch is checked against the PRD (the FR anchors above, NFR-1 and NFR-2) and against the insights. Findings are written down as notes for the digital round.
3. **Round 2: digital, in the UX step (`bmad-ux`).** The hand sketches are imported into the UX step, which has its own tools for wireframes, colour themes, design directions and HTML mock-ups of key screens. The visual style and behaviour are written down in DESIGN.md and EXPERIENCE.md, which win if a sketch and the spines disagree. The visual style must be explicitly less childish than Koll på cashen (playtest notes). Design tools come in here, not before. Doing the digital round in the UX step means navigation, components and layout are decided once.

**Rules for the hand sketches**
- **Phone frames,** portrait, roughly 9:19, one screen per frame. Several frames can share a sheet; the concept 2 sketches have three per sheet. Rough is fine: boxes, arrows and handwritten labels.
- **Real text and figures** from the PRD's journeys and worked examples, not placeholder text. Game texts are in Norwegian (NFR-8).
- **Mark what can be tapped,** for example with a thick outline or a small hand.
- **No dragging:** the month plan works by tapping (NFR-2, WCAG 2.2, criterion 2.5.7).
- **Not colour alone:** a money change has a sign and a word, such as «+604 kr» (NFR-2).
- **Name the files by concept and screen numbers,** for example `k2-01-03.pdf` for screens 1–3 of concept 2. Scans as PDF or photos as JPG or PNG both work.

### Prototype Description

The screens to sketch for each concept. Each concept follows one scene from the PRD's journeys, so the screens form a storyboard.

**Concept 1, «Ringer i vannet»: Markus spends his pengegave (UJ-1), and later sees his savings grow (UJ-3).**
- **K1-01 The choice:** the pengegave event with two or three options.
- **K1-02 The ripple:** right after the choice: money, wellbeing, room and «Låst opp / Stengt» change together.
- **K1-03 The echo:** some months later, the bank's message that his savings have grown, with an echo badge «Fra: …».
- **K1-04 "Hvorfor?":** the answer: the choice behind it, saving and interest in one or two sentences, and the real figure (NOK 3,000 earns NOK 84 in a year).

**Concept 2, «Måneden på én skjerm»: Markus fits a concert into a November with extra shifts (UJ-6).**
- **K2-01 The month plan:** a school month with 14 h of work a week, so 3 slots. School and work are blocks.
- **K2-02 The phone:** Emma's concert invitation with «Legg i planen».
- **K2-03 Placing an activity:** a card with price and effects, and a card that can't be afforded, showing «Mangler … kr».
- **K2-04 The job view:** the hours control with a preview, "ending the extra shifts gives 4 slots from December, and NOK 604 less a month".

**Concept 3, «Pengene som i en bankapp»: Markus saves towards the car licence (UJ-6).**
- **K3-01 The money view:** accounts and the savings target with a picture, a percentage, and when it opens.
- **K3-02 «Neste måned»:** next month's known costs as a list of bills.
- **K3-03 «Småtteri»:** what activities have cost this year, by kind.
- **K3-04 The bank message:** «Du har passert tre firedeler av sparemålet ditt».

Twelve screens in all. Start with the first screen of each concept if there isn't time for all of them.

#### Round 1 result: concept 2 sketched (2026-11-11)

Sara sketched concept 2 by hand as six phone screens, following UJ-6 (`design/mobile-sketches/k2-01-03.pdf`, `k2-04-06.pdf`). The sketches are low-fi first drafts and are not revised. The notes below are carried into the digital round instead.

| # | Screen | Covers |
|---|---|---|
| 1 | Home: November opens, wage, savings target, two new messages (Emma, the bank) | UJ-6 step 1; K2-02 |
| 2 | Month plan: 3 of 4 slots, school and work as blocks, activity list with tick boxes | UJ-6 step 2; K2-01 |
| 3 | Chosen activities: concert, evening with friends, rest night, total NOK 650 | UJ-6 step 3; K2-03 |
| 4 | Job view: 14 h a week (10 + 4), keep or end the extra shifts, with slots and NOK 604 | UJ-6 step 4; K2-04 |
| 5 | November result: activities −NOK 650, wellbeing parts, "concert and friends lifted social life" | UJ-6 step 5 |
| 6 | The road ahead: December, January, savings target, a key insight | UJ-6 resolution |

**What works.** The six screens follow UJ-6 step by step. A bottom bar with Hjem, Plan, Jobb and Økonomi is easy to read on a phone. The month plan works by tapping, not dragging (NFR-2). Money changes have signs. Screen 5 shows the point of UJ-6: the activities lifted social life.

**For the digital round**
- **Figures:** use the worked examples (brief addendum, examples 25 and 26): wage NOK 8,457; car licence NOK 32,500 at 79.8% when November opens; concert NOK 450, evening with friends NOK 200.
- **Screen 4:** keeping the extra shifts gives 3 slots in December, and 4 from January. Ending them gives 4 from December and NOK 604 less a month. Show the kroner on both options, plus the hourly rate, expected pay and the hours limit (FR-56).
- **Screen 6:** a five-year total belongs on the ending screen (FR-42). During play, show this year's activity spend by kind (FR-57). Let the figures carry the lesson rather than stating it (PRD §1). The screen is not in the PRD, and its content overlaps the job view and money view.
- **No days or times within the month** (FR-52, D26): "Månedsoversikt", not "Ukesoversikt", and no clock times on messages.
- **Activity cards** show their effect on stress and social life as well as the price (FR-53), for example concert +8 social life, rest night −5 stress (example 26a). Write "Stress ned" or "−5", not a bare minus.
- **Not yet sketched:** «Legg i planen» on an invitation, a card the player can't afford («Mangler … kr»), and a place to read earlier messages (FR-54).

#### Concepts 1 and 3: decisions (2026-11-12)

- **Concept 1, «Ringer i vannet»: postponed.** It may be sketched later. It is still the concept closest to the PRD's main target (PRD §7.1), so the echo badge and "Hvorfor?" (K1-03, K1-04) are the screens to sketch first if the team returns to it. Until then, they are designed directly in the UX step.
- **Concept 3, «Pengene som i en bankapp»: dropped.** The money view's savings target, upcoming costs and activity spend (FR-57) are on the PRD's cut list (§4.4), and the view builds on bank apps the players already use, so it carries the lowest risk of being misunderstood. Its ideas (13–15) stay in this document for the UX step.
- **Why stop at concept 2:** concept 2 is the newest and least tested part of the PRD, and its sketches give the design work a documented starting point. The time is better spent on the UX step, which sets the visual style, components and accessibility of the app.

### Key Features to Test

What the sketches should answer. The questions mirror the PRD's playtest targets (PRD §7.1), so the prototype prepares for the playtest instead of replacing it. Only concept 2 was sketched; the questions for concepts 1 and 3 are kept for the UX step.

- **Concept 1 (postponed):** Can a person who hasn't seen the game explain, from K1-03 and K1-04, *why* the savings grew? Do they notice the echo badge, and do they find "Hvorfor?" without help?
- **Concept 2:** Can they explain why more working hours gave fewer slots? Do they understand that the plan is for the month, not for given days? Is placing an activity faster than reading about it?
- **Concept 3 (dropped):** Do they understand what the percentage on the savings target means? Does «Småtteri» make them think "that adds up"? Are «Neste måned» and the card balance read correctly?
- **For all three:** Does it look like a game for their age or like schoolwork? Is everything readable and tappable at phone width?

---

## ✅ TEST: Validate with Users

**Decision (2026-11-12):** the concept 2 sketches are not tested with users. Users meet the design in the PRD's playtest, which tests the playable game rather than paper screens. Until then, this step records the plan and what the design review found.

### Testing Plan

Testing follows the playtest in PRD §7.1. The PRD is the basis, so this plan adds no requirements; it shows which of the PRD's measures answer this session's questions.

- **Who:** 10–20 playtesters aged 18–20, before the December delivery (PRD §7.1). Results say little about 15–17-year-olds, which the PRD notes as a validity limit.
- **What they do:** play the game in the playtest environment over several sittings, with no reminders from the team during their first 7 days (PRD §7.1, NFR-11).
- **How it is captured:** playtest records (FR-50), the money quiz before and after, and the playtest survey, all with a random tester code instead of a name or email address.

| Question from this session | PRD measure (§7.1, §7.2) |
|---|---|
| Can they explain why more working hours gave fewer slots? (concept 2) | "Can explain why more work hours gave them fewer activity slots": 60% or more |
| Do they use the month plan, or tap past it? (concept 2) | Counter-metric: planning ignored, with fewer than a third of invitations applied, or fewer than a third of months whose plan differs from the month before (FR-50) |
| Does planning slow the game down? (concept 2) | Planning time from the records; sessions past 15 minutes as a counter-metric |
| Can they link a later outcome to an earlier choice? (concept 1, postponed) | "Can explain how an earlier decision affected a later outcome": 70% or more |
| Does wellbeing make sense? | "Can say what the wellbeing score shows, and why their ending came out as it did": 60% or more |
| Game or schoolwork? | "It felt more like a game than schoolwork": median 4 or higher |
| Are the money parts easy to follow? | "The money parts were easy to follow": median 4 or higher |

The prototype questions under *Key Features to Test* can also serve as observation notes for the team during the playtest sittings.

### User Feedback

Not collected yet. The sketches have not been shown to users (decision above). This section is filled in after the playtest, from the records and the playtest survey.

### Key Learnings

So far from the design review of the concept 2 sketches against the PRD (2026-11-11), not from users:

1. **A month plan pulls towards weeks and clock times.** The first sketch had a "week overview" and messages with times of day. The PRD's plan has no days or times (D26), so the design has to keep the month as one unit.
2. **The extra-shift trade-off is easy to get wrong.** Even the sketch mixed up which option gives 4 slots in December. The job view has to show both options side by side, each with its slots and kroner.
3. **The future is tempting to show, but unknown.** A five-year total fits the ending screen; during play, only this year's spend is known.
4. **Stating the lesson feels like school.** «Tid er like begrenset som penger» is the point of UJ-6, but the PRD has the player learn from consequences, so the figures should carry it.
5. **A price alone isn't enough.** An activity card needs its effect on stress and social life too, or the player can't weigh time against money.

**Assumptions still open** (from the Define step): that understanding in the game carries over to real choices, that results from 18–20-year-olds say something about 15–17-year-olds, and that wellbeing makes sense without making the game complicated. The playtest tests the first and the third; the second needs a later test with younger players.

---

## 🚀 Next Steps

> **Provisional.** This plan builds on the design review of the sketches against the PRD, not on user tests. It is revised after the playtest (PRD §7.1).

### Refinements Needed

For the digital round in the UX step, from the round 1 notes above:

- **Figures from the worked examples** (examples 25 and 26), not invented ones.
- **Job view:** both extra-shift options side by side, with slots and kroner, plus hourly rate, expected pay and the hours limit (FR-56).
- **Month plan:** called «Månedsoversikt», with no days or times; activity cards with price and effect; a card the player can't afford shows «Mangler … kr».
- **Phone:** «Legg i planen» on invitations, and a place to read earlier messages (FR-54).
- **Result and road-ahead screens:** wellbeing before and after the month's activities, worded so "down" for stress reads as good; this year's spend instead of a five-year total; no stated moral. Decide whether "Veien videre" is merged into the job view and money view, since it isn't in the PRD.

**Next cycle:** the prototype is ready to refine digitally. The problem framing holds and needs no new empathy work before the playtest. A test with 15–17-year-olds is a later cycle (PRD §7.1, validity limit).

### Action Items

In order:

1. **Commit and merge this session's work.** This document and the concept 2 sketches, from the branch `ux/sara-design-thinking` to `main`, through a pull request. Then close issue #49. *Sara.*
2. **Run the UX step (`bmad-ux`), including the digital round.** Import the concept 2 sketches, and make wireframes and key-screen mock-ups with the refinements above. Write DESIGN.md and EXPERIENCE.md from the PRD, building on this document's insights, ideas 1–28, the concept 2 notes, and the playtest notes on a less childish style than Koll på cashen. Design tools come in here, not before. *Team.*
3. **Concept 1, if there is time.** Sketch K1-03 (the echo badge) and K1-04 ("Hvorfor?"), or design them directly in the UX step. *Team.*
4. **After the playtest:** fill in *User Feedback* and *Key Learnings* from the playtest results, and note what changes. *Team.*

### Success Metrics

**For the game:** the PRD's playtest targets (PRD §7.1). The ones this session's concepts aim at most directly:

| Metric | Target |
|---|---|
| Can explain how an earlier decision affected a later outcome | 70% or more |
| Can explain why more work hours gave them fewer activity slots | 60% or more |
| Can say what the wellbeing score shows, and why their ending came out as it did | 60% or more |
| "It felt more like a game than schoolwork" (1–5) | Median 4 or higher |
| "The money parts were easy to follow" (1–5) | Median 4 or higher |
| One session, one in-game year | 10–15 minutes on a phone |

The counter-metrics in PRD §7.2 apply as well, especially planning being ignored.

**For this design work:**
- The UX documents build on this session, and the digital prototype includes the round 1 refinements.
- *User Feedback* and *Key Learnings* are filled in from the playtest before the delivery.

---

_Generated using BMAD Creative Intelligence Suite - Design Thinking Workflow_
