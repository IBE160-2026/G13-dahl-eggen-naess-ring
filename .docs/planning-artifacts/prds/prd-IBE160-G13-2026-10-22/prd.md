---
title: LifeMode PRD
status: draft
created: 2026-10-22
updated: 2026-11-13
---

# PRD: LifeMode

## 0. Document Purpose

This PRD sets out what the first version of LifeMode (version one, also called the MVP) must do and why. The team, the downstream BMAD work (UX, architecture, epics and stories), and the examiner (sensor) all work from it. It builds on the product brief, `briefs/brief-Ibe160-prosjektmappe-2026-09-17/brief.md`. The brief's addendum holds the financial rule set (Rule Set v1), its parameters, and the worked examples. This PRD refers to those rules by number ("rule 5"). §3.1 sums up each rule in one sentence, and an FR restates one only where it needs the detail. Terms are defined in §3 Glossary. For the product, read §1, §2.3, §4, and §7. For building and testing, §5 and §6 are the reference.

**Status:** draft, revised after the PRD feedback (`tilbakemelding-prd.md`) and the validation of 2026-11-13 (`validation-report.md`). The team decisions it waited for are made: moped fuel (#29) and the playtest fallback (#76). Only a language and structure pass remains before it's set final. When it is final, it is final for UX and architecture, and the content figures stay provisional: values without a source, and tuning values, carry a status, owner, and deadline in Rule Set v1's parameter table. Open questions that block work are marked in §8. No AI in this version. The history is in `.memlog.md`.

This PRD's own `addendum.md` holds detail that belongs downstream, along with the reasons behind several decisions. Every decision and change is logged in `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/.memlog.md`, where a later entry replaces an earlier one. `#N` means a GitHub issue in the project's repo.

**Which source applies:**
- A decision that changes behaviour applies downstream only once it's written into this PRD, or into Rule Set v1 for financial rules.
- Where the brief, the architecture, or the research disagrees with this PRD, this PRD applies. The exception is how a financial result is calculated, where Rule Set v1 applies.
- If this PRD and the log disagree, the PRD is corrected before downstream work relies on that part.

## 1. Vision

LifeMode lets young people in Norway make expensive money mistakes before those mistakes cost real money. It is a life and money game for 15-20-year-olds. The player lives five years of a life, a few minutes at a time, and every choice carries forward. Spending the pengegave at 15 shapes what is possible at 18. Using a credit card like a debit card turns into months of extra shifts. The game always shows why.

**Built for Norway first and foremost.** The game uses Norwegian rules and life stages, such as frikort, BSU, credit only from 18, and the moped licence at 16, with real 2026 figures.

**Wellbeing counts too, without becoming complicated.** Good money management isn't just having the most money. The player's wellbeing (stress, free time, and social life) counts in how the game ends, so getting rich at any cost gives a hollow win.

**It feels like a game, not schoolwork.** A 15-year-old should prefer it to scrolling on the bus. The team's design aim is that it plays more smoothly and feels more rewarding than Koll på cashen, a free Swedish personal-finance game for the same age group. The playtest doesn't measure this comparison.

**Time is as limited as money.** Each month the player plans their free time, manages their job and money, and reads what friends, family, the employer, and the bank send them. Story events are the highlights, not the whole game. The player learns from what their own actions lead to, not from questions and answers. It is never a day-by-day simulator or a quiz.

- **Now (this PRD):** a complete game from 15 to 20, built on pre-written events, activities, and messages, and on a deterministic financial engine, with no AI.
- **Next (V2):** AI as the game master where possible, while the engine still decides every amount (§4.3). Also pocket money the player can earn, for example through minigames. After that, moving out and rent, education, negotiation, a parent view, and modes for schools.
- **Later:** a wider simulation of adult life.

## 2. Target User

LifeMode is for young people aged 15-20 in Norway who want or need to learn about money and become more independent. It is aimed especially at those who are about to make their first real money decisions: a first pengegave, a first job, a first credit card. Some come by their own choice, and some because a parent or teacher told them to. They want to feel grown-up and make their own choices, and they don't want it to feel like homework. They play in short bursts, often on a phone and on the go.

What the survey "Unge og penger" found (133 responses):
- **They want to learn:** 63% would like to learn more about money.
- **Thinking ahead is the weak spot:** 88% know how much money they have, but only 38% think about how a purchase affects their money months ahead, and 39% often run out of money.
- **What they regret:** most often small purchases that add up, such as snacks and takeaway, and also clothes, trend buys, and collectibles.
- **What they understand least:** BSU and credit.
- **Where they learn:** family is the main source of money, knowledge, and help, and 88% learned most about money from family.

The survey is a convenience sample, probably spread through the team's own networks and schools, so it isn't representative. It has only 8 respondents aged 19-20, and it didn't test the LifeMode concept.

### 2.1 Jobs To Be Done

- When I'm about to make my first real money decisions, I want to see what they lead to before they cost me real money.
- When I have a few spare minutes, I want something more useful than scrolling that still feels like a game.
- When something changes in my money, I want to understand why, so I can do it differently next time.
- When I have a goal such as a flat or a big trip, I want to try different ways of getting there and see what each one costs me, in money and in the rest of my life.

### 2.2 Non-Users (version one)

- **Parents and teachers.** They may suggest the game, and they could pay for it later. But version one is designed for the player alone, with no parent view, class mode, or teacher tools. In UJ-1, Markus's mother has no account and can't see his game.
- **People under 15 or over 20.** The game covers the years from 15 to 20, and its rules and figures are tuned for that range.
- **Players outside Norway.** The rules, figures, and texts are Norwegian.

### 2.3 Key User Journeys

The journeys follow Markus's life in order, so UJ-6, at 17, comes before UJ-4, at 18.

- **UJ-1. Markus is told to try LifeMode before he spends his pengegave.**
  - **Persona + context:** Markus, 15, has just been told by his mother that he can't spend his whole pengegave on Monster and Fortnite. She suggests LifeMode, so he can see that saving a little now can pay off later, and that being careless with money can have serious consequences. He opens it slightly irritated, just to test it.
  - **Entry state:** No account, on his phone, possibly on the bus. His mother has no account and no view of his game.
  - **Path:** Markus reaches his first real choice within about 2 minutes.
    1. The first screen offers two choices: **Log in** or **Create user**. Markus creates a user with an email address and password.
    2. He chooses his life goal: saving for something big, which for him is a flat of his own. The target is an amount the game sets, one that can be reached by 20, such as a start on the deposit, since a whole flat is out of reach by then.
    3. He chooses his avatar. In the game he is 15 and has just received a pengegave, a random amount between NOK 10,000 and NOK 30,000.
    4. His first real choice is what to do with the pengegave. Right afterwards, his money, wellbeing, and future opportunities change, and his room or belongings change with them.
    5. His phone gets a message from a shop that needs a part-timer (month 3). He takes the job in the job view and sets his hours. In the quiet months between events, friends' invitations show up, and he decides what to spend his free time on.
  - **Climax:** Markus understands that his own choices affect what happens next.
  - **Resolution:** The session ends after one in-game year. Before he leaves, the game shows a short teaser, such as "Next year you can take the moped licence" or "A choice you made earlier may have consequences later…". Progress is saved automatically. He wants to come back to see what happens next, what unlocks at the next age, and what his earlier choices lead to.
  - **Edge case:** Play can stop abruptly, for example when the bus arrives. Nothing he has already chosen and the server has confirmed is lost.

- **UJ-2. Markus picks up his game on a school PC to find out what the moped licence costs.**
  - **Persona + context:** Four days later, Markus is bored in class. He has realized that in real life he is only a year away from being old enough for a moped licence, and he comes back to find out what it would actually cost.
  - **Entry state:** He has an account but has never used LifeMode on this PC, so he is not logged in here.
  - **Path:**
    1. He logs in with his email address and password, leaving "Stay logged in on this device" unticked.
    2. He gets a quick recap of where he is, with a teaser for what opens later. The teaser names the moped licence and what it costs, based on real prices.
    3. He sees his balance and the next choice he has to make.
  - **Climax:** He sees what the moped licence would cost compared with what he has.
  - **Resolution:** He carries on with the same life from where he left it, and the game keeps saving his progress automatically. If he later chooses to take the licence, he pays for driving lessons, mandatory lessons, and the licence itself, and has to pass a short driving game (FR-51).
  - **Edge cases:**
    - **Long break:** he gets the same quick recap however long he has been away, so returning works after any gap. The game is exactly as he left it.
    - **Back on his phone:** the game checks for updates when he opens it, so he sees the progress he made on the PC (FR-8).
    - **Forgotten password:** he resets it by email (FR-3).

- **UJ-3. Markus sees that the little he saved has grown, and starts to think the moped might be possible.**
  - **Persona + context:** Markus spent most of his pengegave on things that felt exciting at the time, but after a short tip from the game he put a little into savings. He has heard that a moped is expensive.
  - **Entry state:** Logged in, mid-game. Some in-game months after the first choice.
  - **Path:**
    1. The bank sends a message: his savings have grown, because they have earned interest.
    2. He is glad and curious, so he presses "Hvorfor?".
    3. The game links the increase to his earlier choice and explains saving and interest. It shows the real figure: NOK 3,000 earns NOK 84 in a year in a savings account.
    4. The game points him to other ways of earning, such as more hours now or a summer job next year.
  - **Climax:** He understands that money he put aside earned more money without him doing anything, because of a choice he made himself.
  - **Resolution:** He starts thinking about other ways to earn more. With savings and a job, the moped he thought was too expensive might be possible after all.

- **UJ-6. Markus fits a concert into a November with extra shifts.**
  - **Persona + context:** Markus, 17, is in Vg2 and works 10 h a week in a shop. He has had the moped licence and a moped since he turned 16 (UJ-4). Now he's saving for the car licence, which he can take at 18, and has pinned it as his savings target, although it doesn't open until January (FR-57). In September his employer sent a message asking for extra help, and he took the extra shifts: 4 more hours a week for three months.
  - **Entry state:** Month 35 (November), a quiet month. The extra shifts run from October to December, so he works 14 h a week. His free time (rule 12) is 72 out of 100, which gives him 3 activity slots this month instead of 4 (worked example 24).
  - **Path:**
    1. November opens. The month summary shows his wage with the extra shifts. His phone has two new messages. Emma invites him to a concert this month, and the bank says he has passed three quarters of his savings target.
    2. He opens his month plan: 3 activity slots, with school and the shifts shown as blocks. He wants four things: the concert, an evening with friends, a rest night, and gaming.
    3. He places the concert and the evening with friends, and the plan shows what they cost together. He puts a rest night in the last slot, because the extra shifts make his weeks long.
    4. In the job view he sees that ending the extra shifts would give him 4 slots from December, and that they leave him NOK 604 more a month after spending. He keeps them: they end after December anyway.
    5. He continues. The engine charges the two paid activities after the month's spending, then works out wellbeing. The concert and his friends lift his social life this month, and the rest night eases his stress (worked examples 25 and 26).
  - **Climax:** He sees that time is as limited as money. The extra shifts bring the car licence closer, but cost him a slot every month.
  - **Resolution:** His savings carry over into December, and November's wellbeing score stays in his average. In January his hours drop back to 10 and he gets the fourth slot back. At 20, the ending can show «Konserter og arrangementer» as one entry with what they cost over five years, if they're among the choices that mattered most (FR-42).
  - **Edge cases:**
    - **He can't afford the concert:** it shows the missing amount and can't be placed (FR-53).
    - **He spends the money before he continues:** an activity he can no longer pay for is dropped with a note (worked example 25).
    - **He switches to the PC:** the plan is saved and looks the same there. If he changes the plan on the phone after the PC has loaded it, the PC reloads before he can continue (FR-49).
    - **No slot left:** he has to remove an activity first.
    - **He does nothing:** the invitation runs out at the end of the month, with no other effect.
    - **The gift:** in month 37 his parents may give him the licence (FR-30). The target is then cleared with a note, and the savings are his to use (FR-57). In UJ-4 they can't, so he pays for it himself.

- **UJ-4. Markus uses his first credit card like a debit card, and pays it off before it becomes a crisis.**
  - **Persona + context:** Markus, 18, has a part-time job, which is how he got his first credit card. He uses it as if it were a debit card, without thinking that it has to be paid back, with interest if he doesn't pay in time. He spends money on it for school lunches, a city trip with his friends where he pays for everyone, and fuel for his moped and for his parents' car when he borrows it. His parents couldn't give him the car licence (FR-30), so at 18 he paid for it himself with what he had saved since 17, cutting back on paid activities to get there (UJ-6). It emptied his savings.
  - **Entry state:** Logged in, aged 18, a couple of in-game months after getting the card. He has had a moped since he turned 16: he saved up for the licence from his part-time job and took a gift offer for a used moped, and it costs him fuel, repairs, and insurance (FR-29). He spends a lot from month to month, on the high spending level (FR-23). He pays his card bill as if it were a debit card: the bank takes what's on his account each month. Last month he paid for a city trip for everyone on the card, which took it to its limit, and he has about NOK 1,000 left on his account.
  - **Path:**
    1. The game warns him that his card debt has reached its NOK 10,000 limit, more than a month's wage, and that he couldn't pay it all by the deadline, so interest has started. This isn't a crisis month yet, and he decides for himself whether to act.
    2. The game shows the card's interest rate and, in kroner for his own balance, what the interest costs him this month and what the whole debt will cost if he pays only the minimum. At 22.6% a year on NOK 10,000, NOK 188 of his first NOK 350 minimum payment goes to interest. Paying only the minimum takes 51 months and costs NOK 5,508 in interest in total. He panics a little, because the longer he waits, the harder it gets.
    3. He talks to his mother. She wants to help but can't afford to, so she suggests he stops using the card until he has the repayment under control, and works more hours to pay the debt down faster.
    4. He stops using the card, moves his spending down to normal, and raises his hours from 10 to 12 a week, within the working-hour limits in rule 10. From the next month, the extra hours take up more of his month plan as work blocks, so he has fewer slots, and he starts turning down invitations from friends.
    5. He checks what his moped would sell for. After two years its price has dropped, so selling it wouldn't cover the debt, and he'd have to pay for the bus instead. He keeps it.
  - **Climax:** He realizes he has to work more hours and spend less for the next six months. He has less free time and does fewer social things, and the debt keeps weighing on him.
  - **Resolution:** After six months he is back on track, tired and relieved. Back on track means the card balance is paid in full, so it no longer accrues interest. In the game, his stress goes up from the debt, and his free time and social life go down while he works it off. He has learned to use a credit card carefully, and to spend only what he can afford.
  - **Edge cases:**
    - **He ignores the warning:** the debt barely shrinks, and interest keeps costing him about NOK 180 a month. If he misses the minimum two months in a row, a crisis month starts. A crisis that's still unsolved at 20 is a loss (FR-32, FR-41).
    - **Family help:** not always on offer and often partial. Family loans are interest-free (FR-27).

- **UJ-5. Markus turns 20, sees how his life turned out, and plays again to get rich.**
  - **Persona + context:** Markus is about to turn 20 in the game. He sorted out his credit card at 18, and since then he has been careful with money. He worked 20 h a week through his last eight months at school, and after upper secondary school he has taken a full-time job. He keeps his spending low and saves the rest towards a flat (worked example 23).
  - **Entry state:** Logged in, in the last in-game month before his 20th birthday. His stress has settled down, though he has cut back on social things to save.
  - **Path:**
    1. He turns 20, and the game ends.
    2. He sees a summary of how his life went. He has saved towards his flat, has no debt, and is doing fairly well. This is the real win: he reached his goal of saving for something big, and his wellbeing is at or above the threshold.
    3. The summary shows the three choices that mattered most, by their effect in kroner. One of them can be a group of activities, such as everything he spent on concerts. He opens one to see how things could have gone if he had chosen differently.
    4. With each choice he gets a short, general, pre-written tip: how a costly choice could have been avoided, or why a good one paid off (FR-42).
  - **Climax:** He feels a bit stupid for ending up in so much debt at 18, but proud that he found a way out.
  - **Resolution:** He has seen how things like the moped licence and the credit card affect his money, and now he wants to find out how to get rich. He starts again from 15. He chooses a life goal again and gets a new pengegave.
  - **Second playthrough:** He chooses to save for something big or to be debt-free with a buffer, and puts money ahead of everything else. He finds that getting rich is possible, but chasing as much money as possible often costs him his social life and raises his stress. This is the hollow win: goal reached, wellbeing below the threshold. The summary includes the choice that hurt his wellbeing most, so he can see why (FR-42).

## 3. Glossary

| Term | Meaning |
|---|---|
| Active month | A month with a highlight event, where the player makes a real choice. Each in-game year has the same scheduled active months (FR-46), and a card warning or a crisis can make another month active |
| Activity | A pre-written thing to do in an activity slot, such as meeting friends, resting, or going to a concert. It can cost money, and it changes stress and social life in that month's wellbeing (FR-53). Basic activities are always available. Invitation activities need an invitation (FR-54) |
| Activity slot | One unit of the month's free time that the player can fill with an activity. The month's free time (rule 12) sets how many there are (FR-52) |
| Available money | Current account plus savings account, minus all debt (rule 13) |
| Boomerang pair | Two linked events. An option in the first, the opener, sets a flag. The second, the follow-up, needs that flag and comes a few months later with an echo badge (FR-46, FR-37) |
| BSU | Boligsparing for ungdom: a savings account for a first home, with higher interest and a tax deduction (rule 9) |
| Card use | The setting that puts purchases and card-payable costs on the credit card while it's on (FR-26) |
| Card warning | The warning shown when interest starts on a card bill that wasn't paid in full (FR-31) |
| Cause link | The record of which choices or rules caused an effect, with each one's share |
| Choice | Anything the player decides: an option in an event or crisis month, a money action, an open option (taken from its offer message, the money view, or the job view, FR-48), or an applied activity (FR-53). Any choice can be a cause (FR-36). A real choice is an option picked in an active or crisis month, and those are what FR-46 counts |
| Content check | The automated check of the content library (events, activities, and messages): the schemas, the counts per in-game year, and seeded test playthroughs (FR-58) |
| Cooldown | The two months after a crisis month, when no new one starts (FR-32, rule 8) |
| Crisis month | A month the engine starts when a rule 8 trigger is met. It has up to three linked choices |
| Cut list | The ordered list in §4.4 of what gives way first when time runs short. Its items make up the Can be cut tier |
| D1-D26 | The disclosed simplification texts in the brief's addendum (FR-40) |
| Dated offer | An offer with a last day, such as the summer job or the experience (FR-48) |
| Debt step | The rule 1 step with loan instalments, the card bill, and interest on debt |
| Drawn offer | An offer that isn't tied to a set month, such as extra shifts from the employer or a gift moped. It's drawn by chance and can be taken only in the month it arrives (FR-55) |
| Echo badge | A marker showing that an effect comes from an earlier choice |
| Ending wellbeing | The average wellbeing in months 19-60, from the summer after 10th grade to the 20th birthday. The endings use it |
| Endings | Real win, hollow win, goal not reached, or loss (FR-41) |
| Engine | The backend that applies Rule Set v1 and decides every financial result |
| Event | A pre-written situation with a few options, taken from the content library (FR-17). Crisis events are used only in crisis months, and the rest are regular events. Regular events other than the card warning are also called story events |
| Extra shifts | Extra weekly hours for a few months, from an employer offer or an event option, on top of the hours setting (FR-47) |
| F1-F10 | The functional test criteria in the brief |
| Flag | A named yes/no marker in a playthrough, such as `owns_moped` or `has_card`. Options set or clear flags, and the engine sets flags for age unlocks and belongings. Flags decide which events can appear (FR-46), what a choice opened or closed (FR-35), and what the room shows (FR-34). Flag names come from a fixed list |
| Frikort | A tax card that lets someone earn up to NOK 100,000 a year (2026) with no tax deducted |
| Highlight event | The month's event: a story event, the card warning, or a crisis event. A month with one is active |
| "Hvorfor?" | The button that explains why something changed |
| "If you had chosen differently" line | An engine-calculated line comparing a choice with another option in the same event, or a group of activities with not doing them (FR-39) |
| Invitation | A message that makes an activity available in the month it arrives (FR-54) |
| Life goal | One of three goals chosen at the start: save for something big, be debt-free with a buffer, or afford a big experience |
| LK20 code | The code of the curriculum whose competence aim an event supports, such as MAT01-06 (maths after 10th grade) or SAF01-05 (social studies after 10th grade) |
| Mechanism | The money mechanism an event or effect belongs to, from a fixed list: wages and hours, tax, saving and BSU, fixed costs, consumer loans, credit card, unexpected expenses, family help, moped and licences, and everyday spending and free time. Disclosed simplifications are tied to mechanisms (FR-40) |
| Message | A pre-written text in the in-game phone from a friend, family, the employer, or the bank: info, an invitation, or an offer. The phone also holds a copy of the month's highlight event (FR-54) |
| Minigame | A short, turn-based game that takes skill, such as driving a route for a licence (FR-51) |
| Money action | Something the player can do in any month without using up the month's real choice (FR-45) |
| Money view | The place where the player sees their accounts, takes money actions (FR-45), takes open options (FR-48), and follows a savings target (FR-57). How it looks is UX |
| Month plan | The month's activity slots and the activities in them, with school and work shown as fixed blocks (FR-52). It isn't the calendar of rule 11 |
| Net savings | Current account, savings account, and BSU, minus all debt, family loans included. The savings goal uses it (rule 13) |
| Offer | A message that points to an open option (FR-48), to extra shifts (FR-47), or to a one-time gift (FR-29, FR-30). The options with an offer month in the FR-18 table arrive this way |
| Payment plan | A card balance turned into a 12-month annuity loan in a crisis month (rule 15) |
| Pengegave | Money the player gets at the start of the game, at 15. It is drawn at random between NOK 10,000 and NOK 30,000 |
| Playthrough | One life, from 15 to the 20th birthday: 60 in-game months |
| Quiet month | A month with no highlight event. It is processed by the same rules as an active month. The player sees a short summary and any new messages, and can plan, or continue straight away |
| Recap | The short summary a returning player sees before the next choice |
| Reference run | An automated run with set choices that checks that the goals can be reached (FR-9, worked example 20) |
| Room | The player's room. It's built from a handful of layers, one per belonging, that change with choices (FR-34) |
| Rule N | Rule N in Rule Set v1, in the brief's addendum |
| Savings target | An option with a price that the player pins to follow their progress towards it, even before it opens (FR-57) |
| Session | One in-game year, from January to December, about 10-15 minutes on a phone. A playthrough is five sessions |
| Sitting | One real-world stretch of play. A sitting can be shorter or longer than a session |
| Spending level | Low, normal, or high: the share of the player's wage after tax that's spent each month (rule 16). Costs come on top |
| Steady wage | Wage income in each of the last three months. A card and a consumer loan need it |
| Teaching point | One sentence saying what an event teaches |
| Teaser | A short line about what comes next, at the end of a session or in a recap |
| Threshold | The ending wellbeing needed for a real win, 50 by default (rule 12, FR-41) |
| Tier | How an FR ranks when time runs short (§4.4): **Core** (what a playthrough and the playtest need), **Extension** (left out if not started by the freeze), or **Can be cut** (the cut list). The team aims to build all three |
| Tip | A short, general, pre-written hint in an event, which the player can ignore. It isn't personal advice |
| Trigger | A rule 8 condition that starts a crisis month: the current account below NOK 0, two missed card minimums in a row, or too much debt (FR-32) |
| Trygdeavgift | The national insurance contribution on wages (rule 3) |
| V2 | The next version after the MVP |
| Virke/HK | The retail collective agreement whose minimum hourly rates the game uses (D2) |
| Wage income | Hourly wages before tax. It doesn't include sales, gifts, the pengegave, family money, interest, or loan payouts |
| Wellbeing | A score from 0 to 100 made from stress, free time, and social life, weighted by the life goal (rule 12) |

### 3.1 Rule Set v1 in brief

The FRs refer to the financial rules by number. Each line below sums up one rule. Rule Set v1 in the brief's addendum is the authority on the details and the worked examples.

| Rule | In one sentence |
|---|---|
| 1 Month order | Each month runs income, tax, costs and spending, unexpected expense, loan instalments with the card bill and debt interest, savings interest, the event and choices ending with planned activities, then wellbeing; the crisis check runs at month end |
| 2 Whole kroner | All amounts are whole NOK, and monthly interest is balance × annual rate / 12, rounded with 0.5 up |
| 3 Tax | Tax is worked out on the calendar year's wage income at 2026 rates, and each month deducts the increase in the year's tax |
| 4 Consumer loan | An annuity loan with equal monthly payments; a family loan at 0% is split into equal instalments |
| 5 Credit card | The monthly bill pays the whole balance, the minimum (the larger of 3.5% of the balance and NOK 300, rounded under rule 2) or a fixed amount; anything less than the whole balance is charged interest on the whole balance, and less than the minimum leaves an overdue amount |
| 6 Credit only from 18 | Bank loans and cards are possible from 18, family loans from 15, and no consumer loan can be taken in months 59-60 |
| 7 Quiet months | A month without a highlight event still runs rules 1-5, and a playthrough has about 20-30 real choices |
| 8 Crisis months | The current account below 0, two missed minimums in a row, or net debt (card, consumer loans and payment plans, minus a positive current account and savings, not counting family loans) above the larger of 3× the 3-month average wage and NOK 5,000 starts a crisis month with up to 3 linked choices and a 2-month cooldown; a trigger true at the end of both month 59 and month 60 is the loss ending |
| 9 BSU deduction | Once a year, 10% of the year's BSU deposits (at most NOK 27,500 in deposits), never more than the year's tax |
| 10 Working hours | At most 12 h a week in grunnskole (months 1-18) and 40 h a week from month 19, with a monthly cap of 173 h that summer jobs share |
| 11 Calendar | Month 1 is January of the year the player turns 15, month 60 is December of the year they turn 19, and school stages follow fixed months |
| 12 Wellbeing | Free time comes from school and work hours; stress and social life move with choices, spending, interest, and crises; activities add effects for this month only; wellbeing is their weighted sum, and ending wellbeing is the average over months 19-60 |
| 13 Life goals | Each goal is checked once after month 60, using net savings, available money, and debt |
| 14 Moped | One moped at most, only with the licence; its value falls 15% a year down to 20%, and insurance and fuel replace the transport ticket |
| 15 Payment plan | In a crisis month the card balance can become a 12-month annuity loan at the card's rate, and the card is blocked until it's paid |
| 16 Spending level | Low 60%, normal 75%, or high 95% of the wage after tax is spent after costs, never more than the current account holds |

## 4. MVP Scope

### 4.1 In Scope

- Account, login, password recovery by email, and account deletion (5.1)
- Saving on the server and picking up on any device (5.2)
- A start with a life goal, an avatar, and a pengegave (5.3)
- Months, sessions of one in-game year, moving to the next month, teasers, recaps, the content library, event scheduling, age unlocks, options that stay open, and tips (5.4)
- The month plan, activity slots, and activities (5.5)
- The phone, with messages such as invitations and offers (5.6)
- The job view (5.7)
- The money view, with a savings target, upcoming costs, and activity spend (5.8)
- Accounts, wages and hours, tax, saving and BSU, fixed and everyday costs, unexpected expenses, consumer loans, credit cards, and help from family (5.9)
- The moped licence, owning a moped, and the car licence as a gift or paid for (5.10)
- The card warning and crisis months (5.11)
- Wellbeing, room layers, and visible future opportunities (5.12)
- Cause links, echo badges, "Hvorfor?", "if you had chosen differently" lines, and disclosed simplifications (5.13)
- Four endings, the ending summary, and playing again from 15 (5.14)
- Minigames for the licences, such as the driving game (5.15)
- Playtest records (5.16)

### 4.2 Never in version one

Version one of LifeMode won't:
- use real money, real bank connections, or real financial data
- give personal financial advice (tips are general and about the game)
- use AI anywhere
- let the player type free text beyond the email address
- lock the player out in real time, or add interest or events during a break
- be a classroom or teacher-led tool

### 4.3 Later or left out

| Item | Status |
|---|---|
| AI as the game master: choosing and writing events and messages, including invitations, within the MVP's schemas, and AI checks | V2, after the base works. The engine still decides every amount (addendum "Ready for V2") |
| Moped insurance offers that vary between insurers, chosen and written by the AI | V2, with the AI as game master. The engine sets each price within sourced ranges (OQ-3). In the MVP, moped insurance is a flat NOK 3,000 a year (#29) |
| Pocket money, and earning it, for example through minigames | V2. The MVP has none, so a player with no job has no income |
| Job development: reliability leading to more offers, raises beyond the age steps, being let go, and several jobs to choose between | V2. In the MVP a job has a wage, a weekly limit, and extra-shift offers |
| Friends as lasting relationships, such as invitations stopping after the player turns down many | V2. In the MVP, friends' names are flavour only |
| Replying to messages, chat, or negotiation in the in-game phone | V2. In the MVP, the player can't reply to messages (FR-54) |
| Planning the next month, and weekly habits that repeat | V2. In the MVP the player plans the current month, and can repeat last month's plan in one action (FR-52) |
| Push notifications outside the game | Out. The MVP isn't a PWA (NFR-1) |
| Avatar and home that develop over time | Later |
| Unlocks based on progress towards the goal, and new areas | Later |
| Funds and investing | Candidate for later |
| Moving out and rent | Later, the first new life area |
| Education and student loans | Later. Must show that a student loan while studying isn't the same as card debt |
| Moped value based on actual use | Later |
| Comparing one playthrough with another | Later |
| Full privacy review: who is responsible for the data, the legal basis, and what applies to players aged 15-17 (#24) | Before any further development or go-live. Not needed for the school project and its playtest (NFR-3) |
| Negotiation, a parent view, school and private modes | Later |
| Replay from a crossroads | Out. It needs earlier game states to be stored |
| Tobacco and alcohol choices | Left out for now. The basis, if the team returns to it, is `research/domain-norwegian-tobacco-alcohol-advertising-la-2026-11-04/research.md` |

### 4.4 Cut order

If time runs short, content is cut before the core, in this order. Other sections call this the cut list and refer to its items by name, not number:
1. The savings target, upcoming costs, and activity spend in the money view (FR-57)
2. Grouped activities on the ending screen (FR-42). Activities are then not ranked
3. Invitation activities and info messages, down to their minimum (FR-17)
4. "If you had chosen differently" lines during play, including the BSU comparison
5. The parents' share of the moped insurance
6. Events, down to the minimum of 40
7. The driving game. The licences are then a payment only, and D10 drops its sentence about the game (FR-28, FR-51)
8. The car licence, both the gift and the paid licence, with car fuel (FR-30)
9. Gift mopeds. Buying a moped stays (FR-29)
10. Room layers, down to 3 (FR-34)
11. Login hardening: per-network limits, the daily email cap, the "stay logged in" choice, **Log out on all devices**, and the 12-month deletion job. These then go on a "before go-live" list. Creating a user, login, reset, logout, account deletion, and the pause after repeated failed logins stay

These always stay: the engine, wellbeing, the spending level, the endings, cause links, "Hvorfor?", the card warning, the moped, login, the month plan with the basic activities, the phone with offers and invitations, and the job view.

**Tiers.** Every FR has a tier in the FR overview (§5). **Core** is what a playthrough from 15 to 20 needs, and what the playtest needs to measure the thesis: the engine, the month loop, events, money, the moped, the card warning and crisis months, wellbeing, cause links, "Hvorfor?", the endings, the month plan, the phone, the job view, a minimal login, and playtest records. **Extension** is the avatar, the recap on return, tips, consumer loans, visible future opportunities, echo badges, disclosed simplifications, and changing the password. **Can be cut** is the cut list above. Where an FR is core but part of it is on the cut list, the overview says which part. The team aims to build every FR, Extension and Can be cut included (team decision 2026-11-13), so Extension work can run alongside the core. The tiers decide what gives way first when time runs short, not what gets built.

**When to cut:** cuts follow the checkpoint table below and are applied in groups, not one at a time. Extension FRs not started by the freeze are left out. If the core isn't playable from 15 to 20 by its checkpoint, the whole Can be cut tier is dropped. If the team has to cut before a checkpoint, it cuts in the order of the list above.

**If the core still isn't playable by the playtest:** the playtest starts on 8 Dec as planned, on what is playable, and isn't postponed (team decision 2026-11-13, #76). Metrics that need a full playthrough or an ending (SM-3, SM-5, SM-8) are reported as not measured. The other metrics are reported for the parts testers could play, and the report names the parts they couldn't.

**Tentative dates (OQ-13, set 2026-11-13):**

| Checkpoint | Date | If it's missed |
|---|---|---|
| Extensions frozen: no new Extension work starts | about 26-27 Nov 2026 | Extension FRs not started are left out |
| Core playable from 15 to 20 | about 1-3 Dec 2026 | The whole Can be cut tier is dropped, with no new discussion |
| Playtest starts (3 days) | 8 Dec 2026 | — |
| Delivery, earliest | about 17-19 Dec 2026 | — |

The dates are worked forward from the playtest start, because the exact delivery date isn't known yet. When it is, the team checks the dates again.

## 5. Features

**FR overview.** Every FR, in the order it appears. The FRs are grouped by feature, so their numbers aren't in order. A dash means the FR serves the section as a whole rather than a single journey. FR-9, FR-32, and FR-46 are split into parts (a, b, c) that can each become a story. The tier column says what is built first (§4.4).

| FR | Title | Section | User journeys | Tier |
|---|---|---|---|---|
| FR-1 | Create user | 5.1 | UJ-1 | Core; the per-network sign-up limit can be cut |
| FR-2 | Log in | 5.1 | UJ-2 | Core |
| FR-3 | Forgotten password | 5.1 | UJ-2 | Core; the daily total cap on reset emails can be cut |
| FR-4 | Change password | 5.1 | — | Extension |
| FR-5 | Log out and staying logged in | 5.1 | — | Core; "stay logged in" and **Log out on all devices** can be cut |
| FR-44 | Delete account | 5.1 | — | Core |
| FR-6 | Save every choice | 5.2 | UJ-1 | Core |
| FR-7 | Nothing waits on the device | 5.2 | UJ-1, UJ-2 | Core |
| FR-8 | Check for updates on opening or returning | 5.2 | UJ-2 | Core |
| FR-9 | Choose a life goal | 5.3 | UJ-1, UJ-5 | Core |
| FR-10 | Create an avatar | 5.3 | UJ-1 | Extension |
| FR-11 | Get a pengegave and make the first choice | 5.3 | UJ-1 | Core |
| FR-12 | Process each month in a fixed, repeatable way | 5.4 | UJ-3 | Core |
| FR-49 | Moving to the next month | 5.4 | UJ-1, UJ-2, UJ-6 | Core |
| FR-13 | Play an active month | 5.4 | UJ-1, UJ-3 | Core |
| FR-14 | Summarize a quiet month | 5.4 | UJ-1, UJ-6 | Core |
| FR-15 | End a session after one in-game year | 5.4 | UJ-1 | Core |
| FR-16 | Recap on return | 5.4 | UJ-2 | Extension |
| FR-17 | Content library | 5.4 | UJ-1 to UJ-6 | Core; invitation activities and info messages can be cut to their minimum |
| FR-58 | Content check | 5.4 | — | Core |
| FR-46 | Event scheduling | 5.4 | UJ-1 to UJ-6 | Core; events can be cut to the minimum of 40 |
| FR-18 | Unlock options by age | 5.4 | UJ-1, UJ-4 | Core |
| FR-48 | Options that stay open | 5.4 | UJ-2, UJ-3, UJ-4 | Core |
| FR-19 | Tips in events and offers | 5.4 | UJ-3 | Extension |
| FR-52 | Month plan and activity slots | 5.5 | UJ-4, UJ-6 | Core |
| FR-53 | Activities | 5.5 | UJ-6 | Core with the basic activities; invitation activities can be cut to their minimum |
| FR-54 | Phone and messages | 5.6 | UJ-1, UJ-3, UJ-6 | Core |
| FR-55 | Which messages arrive | 5.6 | UJ-1, UJ-6 | Core |
| FR-56 | Job view | 5.7 | UJ-1, UJ-4, UJ-6 | Core |
| FR-57 | Savings target, upcoming costs, and activity spend | 5.8 | UJ-3, UJ-6 | Can be cut |
| FR-45 | Accounts and paying for choices | 5.9 | UJ-1, UJ-3, UJ-4 | Core |
| FR-20 | Wages | 5.9 | UJ-1, UJ-4, UJ-5 | Core |
| FR-47 | Working hours | 5.9 | UJ-4, UJ-5, UJ-6 | Core |
| FR-21 | Tax | 5.9 | — | Core |
| FR-22 | Saving and BSU | 5.9 | UJ-3 | Core |
| FR-23 | Fixed and everyday costs | 5.9 | UJ-4 | Core; car fuel can be cut, with the car licence |
| FR-24 | Unexpected expenses | 5.9 | UJ-4 | Core |
| FR-25 | Consumer loans | 5.9 | — | Extension |
| FR-26 | Credit card | 5.9 | UJ-4 | Core |
| FR-27 | Help from family | 5.9 | UJ-4 | Core |
| FR-28 | Moped licence | 5.10 | UJ-2 | Core as a payment; the driving game can be cut |
| FR-29 | Own a moped | 5.10 | UJ-3, UJ-4 | Core for buying; gift mopeds and the parents' insurance share can be cut |
| FR-30 | Car licence | 5.10 | UJ-4, UJ-6 | Can be cut |
| FR-31 | Card warning | 5.11 | UJ-4 | Core |
| FR-32 | Crisis month | 5.11 | UJ-4 | Core |
| FR-33 | Wellbeing | 5.12 | UJ-4, UJ-5, UJ-6 | Core |
| FR-34 | Room layers | 5.12 | UJ-1, UJ-4 | Core with 3 layers; more can be cut |
| FR-35 | Visible future opportunities | 5.12 | UJ-1 | Extension |
| FR-36 | Cause links | 5.13 | UJ-3 | Core |
| FR-37 | Echo badges | 5.13 | UJ-3 | Extension |
| FR-38 | "Hvorfor?" | 5.13 | UJ-3 | Core; the BSU comparison can be cut, with the in-play lines |
| FR-39 | "If you had chosen differently" | 5.13 | UJ-5 | Core on the ending screen; lines during play can be cut |
| FR-40 | Disclosed simplifications | 5.13 | — | Extension |
| FR-41 | Four endings | 5.14 | UJ-5 | Core |
| FR-42 | Ending summary | 5.14 | UJ-5 | Core; grouped activities can be cut |
| FR-43 | Play again | 5.14 | UJ-5 | Core |
| FR-51 | Minigames | 5.15 | UJ-2 | Can be cut |
| FR-50 | Playtest records | 5.16 | — | Core |

### 5.1 Account and login

**Description:** The first screen offers **Log in** and **Create user**, with a link for a forgotten password. An account is an email address and a password, with no username. NFR-3 sets how the address is used. Realizes UJ-1 and UJ-2.

**Functional Requirements:**

#### FR-1: Create user

A new player can create a user with an email address and a password they choose. Realizes UJ-1.

**Consequences (testable):**
- Creating a user asks only for an email address and a password, plus the "stay logged in" choice (FR-5). No real age is collected.
- The password must have at least 8 characters (configuration). There are no other rules for what it contains, and paste and password managers work.
- The player types the email address twice, and a mismatch is caught before the user is created.
- The player information (NFR-3) is shown on the create-user screen, before the user is created.
- An email address that already has a user can't be used to create another one. The game then says the address is in use and points to **Log in** and the forgotten-password link. This is the only place the game shows that an address has a user (see addendum).
- Email addresses are matched without regard to letter case or spaces before and after. " Markus@Eksempel.no" and "markus@eksempel.no" are the same user, when creating a user, logging in, and resetting a password. Dots and "+tags" stay as typed.
- Sign-up attempts from one network are limited (default 60 an hour, configuration), so addresses can't be checked in bulk. A school class can still sign up at the same time.
- If someone else created a user with a player's address, the player can take it over. They reset the password by email (FR-3), which logs the other person out, then delete the account (FR-44) or keep playing.
- No email is sent when a user is created.
- No email confirmation step blocks play, which protects the 2-minute target in FR-11. After creating a user, the player goes straight to choosing a life goal.

#### FR-2: Log in

A registered player can log in with their email address and password on any device and continue the same game. Realizes UJ-2.

**Consequences (testable):**
- A failed login doesn't reveal whether the email address or the password was wrong.
- After repeated failed logins for one address (default 10 in 15 minutes), logins for that address pause for a while (default 15 minutes). The message still doesn't reveal whether the address has a user. A school class logging in on one network isn't blocked.
- A player can reach only their own game.

#### FR-3: Forgotten password

A player who has forgotten their password can reset it by email from the login screen. Realizes UJ-2.

**Consequences (testable):**
- The reset link can be used once and expires after 60 minutes (configuration). Asking for a new link makes earlier links stop working. A used or expired link says so and offers a new one.
- Reset emails are limited per address (default 1 a minute and 5 a day) and in total per day, below the email relay's daily quota (OQ-4). The screen shows the same message whether an email was sent, held back by a limit, or the address has no user.
- After a reset, every device that was logged in is logged out.
- The player's game is unchanged after a reset.
- Reset works in the local run (NFR-6) and in the playtest environment (NFR-11).

#### FR-4: Change password

A logged-in player can change their password from inside the game.

**Consequences (testable):**
- Changing the password requires the current password.
- The new password has the same minimum length as in FR-1.
- The old password stops working immediately.
- Every other device is logged out. The device where the password was changed stays logged in.
- The player's game is unchanged.

**If left out (Extension, §4.4):** a player who wants a new password uses forgotten password (FR-3). Nothing else changes.

#### FR-5: Log out and staying logged in

A logged-in player can log out from inside the game, because a player needs this on any device they share. The player also chooses whether to stay logged in on this device.

**Consequences (testable):**
- After logging out, the game can't be reached on that device without logging in again.
- The player can also choose **Log out on all devices**, for example after forgetting to log out on a school PC.
- A device that was logged out from somewhere else can't make a choice. Its next action shows the login screen, and the game is unchanged.
- **Staying logged in:** at login and when creating a user, the player chooses whether to stay logged in on this device. The box is unticked by default. Unticked, the login ends when the browser is closed or after 30 minutes with no activity. Ticked, it lasts until the player logs out or hasn't played for 30 days. Both times are configuration.

#### FR-44: Delete account

A logged-in player can delete their account and game data from inside the game, after confirming.

**Consequences (testable):**
- Deleting requires the current password and can't be undone.
- After deletion, the email address and the game data are gone, and the old login no longer works.
- Every device is logged out. A device that is still open can't save anything to the deleted account.
- The same email address can create a new user afterwards.

**Notes:** the full privacy review is outside this school project (NFR-3, §4.3).

### 5.2 Saving and picking up on any device

**Description:** A player's game is stored on the server, so they can stop at any moment and continue on another device. Realizes UJ-1 and UJ-2.

**Functional Requirements:**

#### FR-6: Save every choice

Each choice is saved on the server as soon as the player makes it, so an abrupt stop doesn't lose a confirmed choice. Realizes UJ-1.

**Consequences (testable):**
- If the game closes right after a confirmed choice, that choice is still there on the next login.
- A choice counts only when the server has confirmed it. Until then the game shows that it is saving, locks the other options, and shows no result.
- If there's no confirmation within 5 seconds (configuration), the game says it is still trying and tries again when the connection is back. Trying again never applies a choice twice (NFR-7).
- If the connection drops after the server saved a choice, the game shows that choice's result when it reconnects. If the server never got the choice, the player sees the same event again.

#### FR-7: Nothing waits on the device

Everything that changes the game is decided and saved by the server when it happens, so the device never holds progress the server doesn't have. Realizes UJ-1 and UJ-2.

**Consequences (testable):**
- Closing the game at any moment, then logging in on another device, shows the same progress straight away. A choice the server never confirmed isn't there.

#### FR-8: Check for updates on opening or returning

Before it accepts the next choice, the game fetches the latest progress whenever the player opens or reloads it, logs in, comes back to the tab, gets the connection back, or has left it idle (default 5 minutes, configuration). Realizes UJ-2.

**Consequences (testable):**
- Progress made on the PC appears on the phone when the game is opened there.
- A device showing old progress can't overwrite a newer choice. If two devices answer the same event, the first choice the server confirms counts. The other device's choice is refused, and it loads the latest progress with a short message saying the game was updated on another device.
- With no connection, for example on the bus, the game says it is offline. What's on screen stays readable, but the options are locked until the connection is back. Choices aren't queued for later, and saved choices aren't affected.

### 5.3 Starting a life

**Description:** After creating a user, the player chooses a life goal, then an avatar, and then gets a pengegave. The first real choice is what to do with it. Realizes UJ-1 and UJ-5.

**Functional Requirements:**

#### FR-9: Choose a life goal

The player chooses one of three life goals: (1) save for something big, (2) be debt-free with a buffer, or (3) afford a big experience. Realizes UJ-1 and UJ-5.

**Consequences (testable)**, in parts that can each become a story:

##### FR-9a: The goals and how they are checked

- The goal is chosen before the avatar.
- The engine checks the goal once, at age 20, using rule 13, which measures net savings, available money, and debt after month 60. Reaching the target exactly counts.
- **Save for something big:** net savings of at least NOK 100,000.
- **Be debt-free with a buffer:** available money of at least NOK 30,000 at the end of each of months 49-60, and no debt at all at 20, family loans and payment plans included. BSU doesn't count as a buffer. So this goal rewards keeping a buffer over time, not reaching a total at the end.
- **Afford a big experience:** the player bought the experience by the end of month 56 and has available money of at least NOK 0 at 20 (rule 13). Having the money without buying it doesn't count.
- **The experience offer:** a message offers it in month 44 (FR-55), and it stays open in the money view until the end of month 56 (FR-48). It can't be paid for on credit: buying it needs available money (current account + savings − debt) of at least the price at that moment, so a loan payout can't pay for it (rule 13, worked example 18 j2). Its price is NOK 60,000, eight weeks of Interrail through Europe (Rule Set v1 parameters), so this is a different, nearer goal.
- Borrowing never helps. A consumer loan can't be taken in months 59-60, and a loan taken earlier can't turn "goal not reached" into a reached goal (worked example 18).
- The goal can't be changed during a playthrough, only when starting again.

##### FR-9b: Goals are reachable, and earlier play matters

- **Earlier play has to matter:** every careless run in worked example 21 misses all three goals. The main one spends the pengegave in month 1, stays on the high spending level until month 54, and moves to low from month 55. The others vary the full-time hours, when low starts, and how much of the pengegave is kept.
- **Reachable:** the targets and the experience price are configuration. An automated reference run, exactly the run in worked example 20 (NOK 10,000 pengegave saved, the three summer jobs, 10 h a week from month 20, full-time from month 55, normal spending, and spare money moved to savings at each choice step), reaches all three goals, with the NOK 60,000 experience bought in month 56 (worked example 20). The first reference run and worked examples 1-23 plan no activities (FR-53).
- **With some free time:** a second reference run, for a careful player with some free time, is the reference run above plus the free basic activities and the cheapest paid basic activity once a month. The content check fails if this run misses goal 1 or goal 2. With the café (NOK 100) as the cheapest paid basic activity, it ends at NOK 113,950, or NOK 100,488 with a NOK 2,500 expense each June, with the lowest available money in months 49-60 at NOK 67,014 and NOK 56,374. It passes, but only NOK 488 above goal 1 with expenses, so any new monthly cost can tip it (validation 2026-11-13; tuning under OQ-8, #48).
- **Checked with real costs:** seeded runs repeat these checks with real event costs (OQ-8). A careless run ignores every crisis, and a careful run takes the first option in it that clears the trigger. Unexpected expenses come from the run's seed. Seeded runs plan the cheapest paid basic activity once a month, and report the goal results with and without it (OQ-8).
- **The moped has a price:** a player with the moped reaches goal 1 by working more hours or spending less (worked example 22).

##### FR-9c: Progress during play

- The game shows progress towards the goal during play, worked out the same way, including the lowest available money at a month-end so far from month 49 for the buffer goal. Before the player continues, progress is shown after the planned activities' payments, marked as such (FR-49).

#### FR-10: Create an avatar

The player creates an avatar for their life in the game. Realizes UJ-1.

**Consequences (testable):**
- The player picks from a small set of preset looks. Nothing is typed in, so the avatar has no free-text name.
- The avatar is shown with the player's money and wellbeing, and on the ending screen (FR-42). How it looks is UX (OQ-9).

**If left out (Extension, §4.4):** the start goes straight from the life goal to the pengegave (FR-11), and no avatar is shown with the money, the wellbeing, or the ending. The room (FR-34) stays the player's picture of their life. UJ-1 step 3 drops.

#### FR-11: Get a pengegave and make the first choice

The game starts at age 15 with a pengegave drawn at random between NOK 10,000 and NOK 30,000. The first real choice is what to do with it. Realizes UJ-1.

**Consequences (testable):**
- The amount is drawn once per playthrough and stored, so it stays the same when the player resumes. Starting again draws a new amount.
- **Resuming the start:** the playthrough starts when the player confirms a life goal, and the pengegave is drawn then. If play stops before the first real choice, the next login continues at the first step not done yet, and steps already done aren't asked again.
- Engine tests can set a fixed amount.
- A new player reaches the first real choice within about 2 minutes of opening the game. This is checked in playtests.

### 5.4 Months, sessions, and events

**Description:** A playthrough is 60 in-game months, from 15 to the 20th birthday. Each session covers one in-game year, and the player never has to wait in real time. The content library, event scheduling, and age unlocks decide what each month offers. Story events are the highlights. In between, the player explores, plans, and acts: they read messages, plan their free time, manage their job and money, and then see the consequences. Planning is never required, so a quiet month can be done in a tap. The four game areas each have their own section: the month plan (5.5), the phone (5.6), the job view (5.7), and the money view (5.8). Realizes UJ-1 to UJ-6.

```mermaid
flowchart LR
    P["Playthrough: 60 months, 5 sessions"] --> S["Session: one in-game year, 12 months, active and quiet"]
    S --> M["Month, in the order of rule 1"]
    M --> O["Income → tax → fixed costs, everyday costs and spending → unexpected expense → loan instalments, card bill and interest on debt → interest on savings → event and choices, ending with planned activities → wellbeing → rule 8 check"]
```

```mermaid
flowchart LR
    A["Month opens: rule 1 up to interest on savings, new messages"] --> B["Explore: summary, messages, month plan, job, money"]
    B --> C["Plan and act: activities, money actions, open options, hours for next month, the highlight event if any"]
    C --> D["Continue: planned activities applied, wellbeing, BSU in December, rule 8 check"]
    D --> A
```

**Functional Requirements:**

#### FR-12: Process each month in a fixed, repeatable way

The engine processes every month in the order set by rule 1: income, then tax, fixed costs, everyday costs and spending, any unexpected expense, loan instalments, the card bill and interest on debt, interest on savings, then the month's event and the player's choices, ending with the planned activities (FR-53), and last wellbeing. The rule 8 check runs at the end of the month. All amounts are in whole kroner (rule 2). Realizes UJ-3.

**Consequences (testable):**
- The same starting state, random draws, choices, and minigame answers always give the same result.
- The worked examples pass as unit tests, and they cover F1-F3, F7, and F8.
- **Calendar (rule 11):** month 1 is January, at the 15th birthday. Each session runs from January to December and is one tax year. Upper secondary school ends after month 54.
- **Random results:** every random result, such as the pengegave, which event comes next, which messages arrive, an unexpected expense, a gift offer, or whether family can help, is drawn by the engine once and stored before the player sees it. Reloading, logging in again, or switching device shows the same result.
- **Reproducible:** a playthrough's random results can be reproduced from values stored when it starts, so engine tests can replay a whole playthrough from those values, the player's choices, their applied activities, their savings-target pins, and their minigame answers.
- Everything the engine processes in a month, quiet or active, is saved as soon as it's processed (FR-6, FR-7).

#### FR-49: Moving to the next month

A month has two parts. When it opens, the engine runs rule 1 up to interest on savings and draws the month's messages (FR-55), and the player sees the highlight event or the quiet-month summary. When the player continues, the engine applies the planned activities (FR-53), works out wellbeing, checks rule 8, and opens the next month. Realizes UJ-1, UJ-2, and UJ-6.

**Consequences (testable):**
- A quiet month waits for the player to continue. In an active month, the player can continue once they've made the real choice. In a crisis month, the player can continue once the crisis has ended (FR-32). Nobody can continue while a minigame they've started is unfinished (FR-51).
- Empty activity slots and unread messages never stop the player from continuing. The highlight event is always shown when the month opens, so it's never only in the phone (FR-13).
- The player can take money actions and open options, and change the month plan, until they continue, so they can clear a trigger before the rule 8 check.
- **Warnings before continuing:** before the player continues, the money view shows the rule 8 trigger status and goal progress after the planned activities' payments. If the plan would set off a trigger, continuing asks the player to confirm. In month 59, the warning says a crisis in month 60 would be the last chance before the ending. In month 60, if a trigger was true at the end of month 59, it says that continuing like this gives the loss ending (FR-41).
- **Result screens:** an option's result shows that option's own effect. The month's wellbeing and the BSU deduction are worked out when the player continues, and the December summary marks the deduction as expected.
- Every request that changes the game names the month it belongs to. A request for an earlier month, such as one from another device, is refused (NFR-7). Continuing also carries the version of the month plan the device showed. If the plan has changed since, for example on another device, the server refuses and the device reloads (NFR-7).
- **Month 60:** actions that only take effect the next month, such as changing hours or the spending level, are hidden or marked as having no effect, and the slot and upcoming-cost previews are empty.
- After month 60, the player goes to the ending (FR-41). Month 60's summary says that continuing ends this life. A playthrough counts as completed once its ending is calculated.

#### FR-13: Play an active month

In a month with a highlight event, the player sees the situation together with their balance, savings, debt, and fixed costs, and picks one of a few options. If the event has a sender, a copy also goes in the phone (FR-54). Afterwards the game shows what changed in kroner and wellbeing, and why. Realizes UJ-1 and UJ-3.

**Consequences (testable):**
- Every option has a stored wellbeing effect (FR-33), which isn't shown before the pick (team decision 2026-11-13, OQ-9). After the pick, the result shows the change in wellbeing, and "Hvorfor?" explains it (FR-38).
- Options read as actions the player takes, never as quiz answers with one right option (NFR-8). The content check can't test this, so the team checks it when it approves each event.
- An option the player can't pay for follows FR-45.
- Tapping an option twice applies it only once.

#### FR-14: Summarize a quiet month

A month with no highlight event shows a short summary and any new messages. The player can plan and act, or continue straight away. Realizes UJ-1 and UJ-6.

**Consequences (testable):**
- Income, costs, and interest in a quiet month follow the same rules as in an active month.
- In a quiet month, the player can still take money actions (FR-45), take offers, and plan activities (FR-53).
- A player who does nothing but continue gets through a quiet month in one tap.

#### FR-15: End a session after one in-game year

A session ends after one in-game year with a teaser about what comes next, such as "Next year you can take the moped licence". Realizes UJ-1.

**Consequences (testable):**
- Nothing locks the player out in real time. The player can carry straight on into the next year.
- A teaser names the next age unlock (FR-18) or, if there's none, hints at an open boomerang pair (FR-46). From month 55, when nothing is left to unlock, it points to the ending at 20.

#### FR-16: Recap on return

A player who comes back sees a short recap of where they are, with a teaser for what opens later, and then their balance and the next choice. Realizes UJ-2.

**Consequences (testable):**
- The recap is shown after a login, or when the game is opened after at least an hour away (configuration). It's the same however long the break was. Its teaser follows the same rule as in FR-15.
- The game is exactly as the player left it. No interest or events run during the break, and no messages arrive.
- The recap says how many messages arrived this month. Activities already planned stay planned.
- After the ending, FR-43 applies instead.

**If left out (Extension, §4.4):** a returning player lands where they left off, with the game exactly as it was. The session-end teaser (FR-15) stays, and FR-28's licence-cost teaser goes there instead. UJ-2's recap step and its climax drop, and SM-6 then measures returns without a recap.

#### FR-17: Content library

The game is driven by a library of pre-written events, activities, and messages. Realizes UJ-1 to UJ-6.

**Consequences (testable):**
- **Size:** at least 40 regular events, twice the 20 regular active months in a playthrough (FR-46), with a target of 50-60, plus about 10 crisis events. Every in-game year has at least 8 events that aren't follow-ups, need no flags, and have an age range that covers it (configuration). Roughly 55% come before age 18 and 45% after. Unexpected expenses (FR-24) are a separate list and don't count.
- **Activities and messages:** at least 5 basic activities and 12-20 invitation activities (FR-53), an offer message for every row of the FR-18 table that has one, and enough invitation and info messages that every in-game year has at least 6 invitations whose age range covers it (configuration). Invitations are repeatable, at most once each per in-game year (FR-55). Activities and messages each follow a fixed schema (addendum), and the content check enforces it.
- **Schema:** every event follows a fixed schema: mechanism, age, flags, boomerang pair, teaching point, LK20 code, source, and a wellbeing effect for each choice. An automated check rejects an event that breaks the schema. LK20 codes are the ones valid from 1 August 2026, and the content check reports which LK20 aims the library covers, for the examiner. The fields and what the check enforces are listed in the addendum.
- **Choices that come back:** the library has at least 8 boomerang pairs (configuration), and a seeded playthrough meets at least 3 follow-ups on average. Every mechanism has events both before and after 18 where its rules allow it. Activities don't count towards this. The content check enforces both.
- **Options that always work:** every regular event has at least one option with no cost (FR-45). Every crisis event includes asking family and ignoring it (FR-32).
- **Players with no money:** at least half of the regular events before 18 have two options with no cost, so a player with NOK 0 still has a real choice (configuration). The content check runs a seeded playthrough at NOK 0 and reports the share.
- **Everyday costs:** options can change them (FR-23).
- **No AI needed:** the whole game can be played from start to finish with zero AI calls (F6).

**Notes:**
- Candidate event topics from the survey are small purchases that add up, such as snacks and takeaway; clothes; trend buys; collectibles and in-game purchases; subscriptions with a binding period; and budgeting and paying bills. From the market research, the costs of russ at 18-19, with no alcohol content. Family appears as an actor in events.

#### FR-58: Content check

An automated check validates the content library and plays seeded test playthroughs, so that a change to content or configuration can't silently break the rules the other FRs set. It runs in CI on every pull request (NFR-9). This FR collects what the other FRs already require of it; the source FR holds each rule.

**Consequences (testable):**
- **Hard gates (the check fails):**
  - events, activities, and messages break their schema (FR-17)
  - the library is below its minimums: event count, events per in-game year, activities, offer messages, and invitations per in-game year (FR-17)
  - fewer than 8 boomerang pairs, fewer than 3 follow-ups per seeded playthrough on average, or a mechanism without events before and after 18 where its rules allow it (FR-17)
  - an open option differs between its offer message, the money view, and the job view (FR-48)
  - more than one active month per seeded playthrough with no eligible event (FR-46b)
  - more than 2 months a year in seeded runs with no eligible invitation (FR-55)
  - random-choice pairs share more than two-thirds of their regular events, or a same-seed pair with different choices differs in no follow-up (FR-43)
  - the hollow-win runs reach 50 or above (FR-33)
  - the second reference run misses goal 1 or goal 2 (FR-9b)
- **Reports (the check doesn't fail):** the share of events before 18 with two free options, from a run at NOK 0 (FR-17); LK20 coverage (FR-17); drawn events left per in-game year (FR-46b); dropped follow-ups (FR-46c); ending wellbeing at 1-4 slots (FR-52); invitations per in-game year (FR-55); the 17b boundary runs and run 21c (FR-33).
- **Run policies:** seeded runs follow the careless and careful policies in FR-9b, with unexpected expenses from the run's seed.

#### FR-46: Event scheduling

The engine decides which months are active and which event each active month gets. Offers from the FR-18 table don't take an active month: they arrive as messages (FR-55). Realizes UJ-1 to UJ-6.

**Consequences (testable)**, in parts that can each become a story:

##### FR-46a: Active months and pace

- **Active months:** every in-game year has the same active months, 4 by default, and the rest are quiet. Which months are active is configuration. By default they are months 1, 4, 7, and 10 of each in-game year (January, April, July, and October), so there are never more than two quiet months in a row. Months 59-60 are quiet unless a crisis, a card warning, or a pushed-out follow-up takes them. A playthrough with no crisis months has 20 real choices, and crisis months add their linked choices. Rule 7 gives about 20-30 real choices in a playthrough.
- **Pace:** with the default, a session has 4 story events and 8 quiet months, with messages and optional planning in every month. It fits 10-15 minutes on a phone (checked in playtests).
- **First choice:** month 1 is always the pengegave choice (FR-11).
- **Card warning in a quiet month:** it makes that month active.

##### FR-46b: Which event an active month gets

- **Story events only:** active months go to drawn events and boomerang follow-ups. The car licence draw runs in month 37 (FR-30), and its result arrives as a message. The content check reports how many drawn events each in-game year has left.
- **Who can get an event:** an event can be drawn only when the player's age is in its age range, all its required flags are set, none of its blocking flags are set, and it hasn't appeared in this playthrough.
- **Drawn at random:** each active month without a follow-up gets an event drawn from the eligible ones, each with the same chance. The draw is stored (FR-12). Follow-ups are never drawn at random: they take a month only when due.
- **No repeats:** no regular event appears twice in one playthrough. Crisis events and the card warning can repeat (FR-32, FR-31).
- **No eligible event:** the active month becomes a quiet month. The content check runs seeded test playthroughs, reports every month this happens, and fails if it happens in more than one active month per playthrough (configuration).

##### FR-46c: Follow-ups and collisions

- **Boomerang pairs:** when the player picks an option that opens a pair, the follow-up is due after a delay drawn from the pair's range, and takes the first active month at or after that. An opener can be drawn only if its longest delay still lands by the last active month. A due follow-up whose required flag is no longer set is dropped, and the month gets a drawn event as normal.
- **When events collide:** a crisis month comes first (FR-32), then a card warning (FR-31). Follow-ups come next, in the order they're due, and a drawn event comes last. When a crisis is skipped as the month opens (FR-32), the month's event is chosen again in this order.
- **Pushed out:** a follow-up that is pushed out takes the next active month, or makes month 59 or 60 active if none is left. One that still can't get a month by month 60, because crises take months 59 and 60, is dropped, and the content check reports it.

#### FR-18: Unlock options by age

New options open in set in-game months (rule 11). Realizes UJ-1 and UJ-4.

| Option | Opens | In-game month | Offer message | Source |
|---|---|---|---|---|
| Savings account and BSU | 15 | 1 | None | FR-22. BSU has no lower age |
| Part-time job, up to 12 h a week (NOK 136.41 until month 12) | 15, in grunnskole | 3 | Month 3 | Rule 10. From 15, a minor can sign their own work contract (vergemålsloven § 10) |
| Moped licence | 16th birthday | 13 | Month 13 | FR-28. Class AM 146 from 16 |
| Owning a moped (buying, gift offer) | With a moped licence | 13 at the earliest | Gift: a drawn offer (FR-55). Buying: none | FR-29 |
| Part-time job, up to 40 h a week | After grunnskole | 19 | None | Rule 10 |
| Summer job | 16 | 18, 30, 42 (June), paid in 19, 31, 43 (July) | Months 18, 30, and 42, as one message that repeats | FR-20, worked example 1 |
| Car licence: the gift draw, then the paid licence | 18th birthday | 37 | Month 37: one family message with the result of the gift draw | FR-30. Class B is from 18 (Statens vegvesen) |
| Credit card | 18th birthday | 37 | Month 39 | Rule 6 |
| Consumer loan | 18th birthday | 37 | Month 49 | Rule 6, FR-48 |
| Big experience, for goal-3 players | 18 | 44, open until the end of month 56 | Month 44 | FR-9 |
| Full-time job | After upper secondary school | 55 | Month 54 | FR-20 |

**Consequences (testable):**
- **Offer message:** the column says when the option's offer message arrives (FR-55). The option opens in its in-game month, and where a row has no offer message, it opens in the money view or the job view. The full-time job is offered in month 54 and starts in month 55. The credit card and the consumer loan open in month 37, before their messages, so a player can take them from the money view.
- No offer message arrives before its offer month, and the engine rejects a choice for an option that hasn't opened (NFR-7).
- Teasers and recaps use the same table.
- In the MVP, only age unlocks options, not progress towards the goal.

#### FR-48: Options that stay open

An option that has unlocked stays open until the player takes it, and opens again when its one-at-a-time rule allows another. It's first offered in a message, where the FR-18 table has one (FR-55). After that the player can take it from the money view, or from the job view for a job, so a player who couldn't afford something can save up and come back. The credit card and the consumer loan are open from month 37, before their offer messages in months 39 and 49, so a player in trouble can reach them. Realizes UJ-2, UJ-3, and UJ-4.

**Consequences (testable):**
- **What stays open:** the moped licence, buying a moped, the paid car licence, the credit card, a consumer loan, a part-time or full-time job, and, for goal-3 players, the experience. The conditions and prices are the same as in the offer message.
- **Same option:** an open option is the same option, with all its effects, flags, and texts, wherever it's taken: from the offer message, the money view, or the job view. The content check enforces this.
- **Can't pay yet:** the option shows the missing amount and stays open. Test: a player on normal spending with NOK 8,000 saved can't afford the moped licence in month 13, and buys it after the summer job in month 19, when NOK 4,182 of the wage is left after spending, so they have NOK 12,182 before interest.
- **Blocked for another reason:** the option shows what's missing, such as a steady wage, stays open, and is refused until the condition is met (NFR-7).
- **Saying no or quitting:** a player who declines a job or quits can take a job again later.
- **Dated offers:** a summer job stays open only until that July's income step (months 19, 31, and 43), and can be taken from its message or the job view until then. The experience stays open until the end of month 56. After its last day, the message shows the offer as expired, and taking it is refused (NFR-7).
- Taking an open option counts as a choice, so cause links and echo badges can point to it (FR-36). It doesn't use up the month's real choice.
- Gift offers and family help aren't open options. They're drawn once (FR-12). A gift moped arrives as a drawn offer and can be taken only in the month it arrives (FR-54, FR-55). The car licence gift applies automatically (FR-30).

#### FR-19: Tips in events and offers

Some events and offer messages carry a short, general, pre-written tip, which the player is free to ignore. Realizes UJ-3.

**Consequences (testable):**
- A tip is about the situation in the game and is never personal advice.
- Ignoring a tip has no effect in the game.
- **Offers that need explaining:** the credit card and consumer loan offer messages always carry a tip and a teaching point, with any cost in kroner from the engine (NFR-4, NFR-8).

**If left out (Extension, §4.4):** events and offer messages carry no tips. The credit card and consumer loan offer messages still state their cost in kroner from the engine (NFR-4). The ending texts in FR-42 belong to FR-42 and stay. SM-2 then rests on "Hvorfor?" (FR-38) alone.

### 5.5 Month plan and activities

**Description:** Time is as limited as money. Each month the player has a few activity slots and decides what to spend them on: friends, rest, a hobby, or something a friend invited them to. School and work fill the rest of the month, so more work means fewer slots. It's a plan for the month, not a day-by-day calendar. Realizes UJ-4 and UJ-6.

**Functional Requirements:**

#### FR-52: Month plan and activity slots

Each month the player has a few activity slots for their free time. They fill them with activities or leave them empty. Work isn't placed in slots. It comes from the hours setting (FR-47), so more work means fewer slots. Realizes UJ-4 and UJ-6.

**Consequences (testable):**
- **How many:** slots this month = the month's free time (rule 12) ÷ 20, rounded down, at least 1 and at most 4. The divisor and the maximum are configuration (OQ-8). In a school month, 0 or 10 h a week gives 4 slots, 12 h gives 3, 25 h gives 2, and 40 h gives 1. Full-time at 37.5 h after school gives 4, and so does July (worked example 24).
- **Never zero:** the formula never gives fewer than 1, whatever the divisor is tuned to. At the default, rule 10 keeps free time at 20 or above anyway.
- **Fixed when the month opens:** the count comes from that month's hours, extra shifts included. An hours change applies from the next month (FR-47).
- **Never required:** an empty slot has no effect, and the player can always continue with empty slots (FR-49).
- **School and work as blocks:** the plan shows school and work as fixed blocks that the player can't move. Each month starts with empty slots, and plans don't carry over. The look is UX.
- **Same as last month:** one action places last month's activities again, where they're still available. Each one is checked like any placement (FR-53).
- **What a slot is worth:** the content check reports ending wellbeing for the reference runs at 1, 2, 3, and 4 slots, so the team can tune what a slot is worth (OQ-8).
- **No days or times:** the plan has no days, times, or dates within the month (D26).
- **Engine figures only:** the plan's total for the planned activities is calculated by the engine (NFR-4). It covers the activities' costs only, never wages.

#### FR-53: Activities

An activity is a pre-written thing to do in an activity slot. Some are always available, and some come only with an invitation (FR-54). Realizes UJ-6.

**Consequences (testable):**
- **What an activity has:** each activity uses one slot and has a cost of NOK 0 or more, a card-payable flag, an effect on stress and on social life (each within ±10), an age range, required and blocking flags, a mechanism, a kind (such as concerts, or time with friends), and a source for its price (OQ-17).
- **Always available:** a basic set (FR-17). At least two basic activities cost nothing, need no flags, and cover ages 15-20, so a player with NOK 0 can always plan.
- **Invitation activities:** available only in the month their invitation arrives (FR-55).
- **Once a month:** the same activity can be planned at most once a month (configuration).
- **Planning moves no money:** a planned activity shows its cost and its effects. An activity that the player couldn't pay for now, on top of the activities already planned, is shown with the missing amount and can't be placed (FR-45). Removing a planned activity before continuing is free and leaves no trace.
- **Applied on continuing:** when the player continues, the engine applies the planned activities in slot order at the end of the choice step (rule 1), before wellbeing. Each one is checked again for eligibility (age range, flags, invitation month) and for payment, which follows FR-45. One that fails either, for example after a BSU deposit or after the moped was sold, is dropped with a short note and has no effect (worked example 25). A card blocked by a payment plan can't pay for an activity.
- **On top of spending:** activity costs come on top of the spending level (rule 16), like event options. The month summary lists each activity and its cost.
- **Wellbeing:** effects follow rule 12. They're added after rule 12's rows, to that month's score only, and all activities together move each part at most ±15 a month (configuration). The stress and social life that carry over, and the rows themselves, don't include them, and activities never change free time (FR-33, worked example 26).
- **A choice, not the real choice:** an applied activity is a choice with a cause link (FR-36), so echo badges and "Hvorfor?" work. It doesn't use up the month's real choice.
- **In a crisis month:** activities can be planned under the same payment rules, and use no step (FR-32).
- **No earnings:** no activity pays money in the MVP. Earning pocket money is V2 (§4.3).

### 5.6 Phone and messages

**Description:** The phone is where the world comes to the player. Friends invite them to things, the employer asks for help, family has news, and the bank tells them how their money is doing. Messages are pre-written, and the player can't reply to them. Realizes UJ-1, UJ-3, and UJ-6.

**Functional Requirements:**

#### FR-54: Phone and messages

The phone is an inbox of pre-written messages from friends, family, the employer, and the bank. Realizes UJ-1, UJ-3, and UJ-6.

**Consequences (testable):**
- **Three kinds:**
  - **Info:** no action.
  - **Invitation:** makes an activity available in the month it arrives (FR-53).
  - **Offer:** points to an open option (FR-48), to extra shifts (FR-47), or to a one-time gift (FR-29, FR-30). It can carry a tip and a teaching point (FR-19).
- **The event copy:** the month's highlight event is always shown when the month opens (FR-13). If the event has a sender, a copy also goes in the phone, so the event reads as coming from someone. The copy isn't a separate message, needs no answer in the phone, and doesn't count towards the limit (FR-55).
- **No quiz answers:** an invitation is accepted by placing its activity, and an offer by taking it from the message, the job view, or the money view. Ignoring a message only means missing what it offered.
- **Expired offers:** a drawn offer, such as extra shifts or a gift moped, can be taken only in the month it arrives. After that, and after a dated offer's last day (FR-48), the message shows it as expired.
- **Pre-written:** all messages are pre-written in Norwegian (NFR-8), from fictional senders. The player can't write messages (§4.2).
- **Engine figures:** any amount or share in a message, such as «Du har nådd halvparten av sparemålet ditt», is the engine's figure (NFR-4).
- **New and old:** a message that arrived this month is marked new. Earlier messages stay readable for the rest of the playthrough. There are no unread badges across months.
- **Reading changes nothing:** reading a message changes nothing in the game, and nothing about reading is stored.

#### FR-55: Which messages arrive

The engine decides which messages arrive each month, in the same selection step that chooses the month's event (FR-46). Realizes UJ-1 and UJ-6.

**Consequences (testable):**
- **Drawn and stored:** messages are drawn when the month opens, from the playthrough's seed, and stored (FR-12). Reloading or switching device shows the same messages.
- **Who can get one:** a message needs the player's age to be in its age range and its required and blocking flags to fit. An invitation is drawn only if its activity is eligible this month (age range and flags). Payment isn't part of the check, so a player with little money still gets paid invitations. A one-off message can't have appeared before in the playthrough.
- **Bank messages:** they're triggered when progress towards the savings target (FR-57) or towards goal 1, the only goal with a percentage (FR-9), passes 25, 50, 75, or 100%. Each threshold is sent once per target in a playthrough. If several are passed in one month, only the highest is sent, and pinning the same option again doesn't resend thresholds already sent. One more bank message reports savings interest: the first month the interest earned so far passes NOK 50 (configuration), once per playthrough, with the engine's figure (UJ-3).
- **Offers always arrive:** each offer in the FR-18 table arrives as a message in its offer month, and so does the car licence result (FR-30). A player who doesn't qualify yet still gets it, and it shows what's missing (FR-48). An offer message isn't sent if its option has already been taken, can't be taken again under its one-at-a-time rule, or has closed. Nothing can push an offer out.
- **Drawn offers:** the employer's extra shifts (FR-47) and the gift moped (FR-29) are drawn offers. Each has required and blocking flags and a chance per in-game year (configuration), and can be taken only in the month it arrives (FR-54). Extra shifts need a job, hours below the weekly limit, no extra shifts running, and a month before 60.
- **How many:** at most 3 new messages a month (configuration). Offers and the event copy always arrive and don't count towards the limit. Invitations, then info messages, fill the rest. A bank message that doesn't fit arrives the next month instead.
- **Invitations:** 0-2 a month are drawn from the eligible ones (configuration). Invitations are repeatable, at most once each per in-game year. The content check reports invitations per in-game year, and fails if seeded runs have more than 2 months a year with no eligible invitation.

### 5.7 Job view

**Description:** The player sees and manages their job in one place. The job view builds on wages and hours (FR-20, FR-47). Realizes UJ-4 and UJ-6.

**Functional Requirements:**

#### FR-56: Job view

The job view shows the workplace and role, the hourly rate for the player's age, the hours setting and this month's hours with any extra shifts, the rule 10 limit, the expected monthly pay, and any current offers. Realizes UJ-1, UJ-4, and UJ-6.

**Consequences (testable):**
- **Engine figures:** the pay shown is the engine's, and FR-20, FR-47, and rule 10 apply unchanged. An extra-shift offer shows the kroner it would leave after spending (FR-47), never a fixed amount per slot.
- **Actions:** set hours from the next month, quit, take a job offer (FR-48), and take or end extra shifts (FR-47). Each shows the next month's slot count before the player confirms it (FR-52). These are the same actions as in FR-45 and FR-47.
- **Flavour only:** the workplace and role are flavour text. Every part-time and summer job pays the Virke/HK rate for the player's age (D2).
- **With no job:** the view shows the open job offers, or when the next one unlocks (FR-18).

### 5.8 Money view

**Description:** The money view is where the player sees their accounts and manages their money: money actions (FR-45), open options (FR-48), and a savings target with the costs ahead (FR-57). How it looks is UX. Realizes UJ-3, UJ-4, and UJ-6.

**Functional Requirements:**

#### FR-57: Savings target, upcoming costs, and activity spend

The money view shows progress towards one savings target the player picks, the costs already known for next month, and what activities have cost this year. It adds no money rule, and it's on the cut list (§4.4). Realizes UJ-3 and UJ-6.

**Consequences (testable):**
- **Savings target:** the player can pin one option with a price, such as the moped licence, even one that hasn't opened yet. The view then shows when it opens (FR-18). An option with two prices, such as a new or a used moped, is pinned as one of them. Pinning moves no money and isn't a choice, and the target can be changed in any month.
- **Progress:** the current account plus savings against the price, at most 100%, calculated by the engine. BSU and the card don't count, so it's the same money the missing amount is worked out from when the card isn't used (FR-48). Bank messages can name the progress (FR-55). Before the player continues, progress is shown after the planned activities' payments, marked as such (FR-49).
- **Cleared:** when the pinned option is taken, given as a gift, or closes, the target is cleared with a short note.
- **Life goal:** progress towards the life goal is shown as in FR-9.
- **Upcoming costs:** next month's known fixed and everyday costs, plus loan, payment-plan, and family-loan instalments. The card is shown as its current balance, not a forecast. In month 60 there's nothing to show (FR-49).
- **Activity spend:** the total cost of applied activities this in-game year, by kind, so small purchases that add up become visible (worked example 25).

### 5.9 Money

**Description:** The money side of the game covers accounts and money actions, wages and working hours, tax, saving, fixed and everyday costs, loans and credit cards, unexpected expenses, and help from family. Figures follow NFR-4. Realizes UJ-1, UJ-3, UJ-4, and UJ-5.

**Functional Requirements:**

#### FR-45: Accounts and paying for choices

The player has a current account, a savings account, and, if they open one, a BSU. Income lands in the current account, and costs are paid from it. Realizes UJ-1, UJ-3, and UJ-4.

**Consequences (testable):**
- When a payment would take the current account below NOK 0, savings pay the rest, as far as they reach. BSU never does. The month summary shows each transfer.
- An option can be picked only if the player can pay for it from the current account and savings, plus the card if card use is on and the cost fits under the limit. An option they can't pay for is shown with the missing amount and can't be picked. Every event has at least one option with no cost (FR-17).
- Tax, fixed costs, everyday costs, consumer-loan and payment-plan instalments, and unexpected expenses are always charged, even if the current account goes below NOK 0. Card payments, family-loan instalments, and spending never take it below NOK 0, and spending never draws on savings (rule 16).
- A negative current account has no interest or fee. It can't pay for choices, and the next income pays it off first.
- **Money actions:** in any month, from the money view, the player can:
  - move money between the current account and savings, from NOK 1 up to what the source holds
  - deposit in BSU from the current account, or withdraw the whole BSU (FR-22)
  - turn card use on or off, set the card payment, and pay extra on the card
  - pay off a consumer loan, a family loan, or a payment plan early, with no fee
  - set the spending level, and stop an everyday cost that has no binding period (FR-23)
  - set working hours or quit a job (FR-47), also from the job view (FR-56)
  - sell the moped (FR-29)

  Taking an open option (FR-48) works the same way. These actions don't use up the month's real choice.
- **Activities:** an activity (FR-53) is paid like an event option (FR-26). With card use on, a card-payable activity that fits whole under the limit goes on the card. Otherwise it's paid from the current account, then savings. It's never split between the card and the accounts, and it's paid when the player continues, not when it's planned (worked example 27).

#### FR-20: Wages

The player can earn hourly wages from part-time and summer jobs, at the Virke/HK collective-agreement rate for their age, and later from a full-time job. Realizes UJ-1, UJ-4, and UJ-5.

**Consequences (testable):**
- A summer job at 16, 120 hours at NOK 139.40, pays NOK 16,728 with no tax (worked example 1, F7).
- A full-time job is available from month 55, the July after upper secondary school, at age 19 (rule 11).

#### FR-47: Working hours

A player with a job sets how many hours a week they work. The setting stays until they change it. Realizes UJ-4, UJ-5, and UJ-6.

**Consequences (testable):**
- The player has at most one part-time or full-time job, plus a summer job in July. They set weekly hours when taking the job, and can change them or quit in any month. A change applies from the next month.
- Monthly pay is weekly hours × 52 / 12 × the hourly rate for the player's age, in whole kroner, for at most 173 h a month (rule 10). A full-time week of 37.5 h at 18+ pays NOK 31,694 a month, and a 40 h week pays NOK 33,742.
- **Weekly limit:** hours never go above rule 10: 12 h a week in grunnskole (months 1-18), and 40 h a week from month 19. An hours change is checked against the limit of the month it applies from, so a change made in month 18 can set up to 40 h for month 19.
- **Monthly cap:** a summer job and part-time hours share one monthly cap of 173 h. The engine cuts the summer job to fit at July's income step, using that month's hours, extra shifts included. With 30 h a week of part-time work (130 h), a 120 h summer job is cut to 43 h. If the player's hours leave 0 h when the offer is made, the summer job can't be taken: its message still arrives (FR-55), shows that the monthly cap is full, and says why. If an hours change or extra shifts would cut a summer job the player has taken, the control warns first. If July's cut leaves 0 h, the summer job is cancelled with a note.
- A full-time job is 37.5 h a week and can be raised to 40.
- **Extra shifts:** they add the offer's amount (default +4 h) to the hours setting for the offer's number of months (default 3), from the next month. Weekly hours are the setting plus any running extra shifts, never above rule 10, so an offer is capped at the limit. Changing the setting leaves running extra shifts as they are. Extra shifts come from an event option or an employer message (FR-55). They're offered only to a player with a job who is below the weekly limit and has no extra shifts running, and only while a later income step remains, so not in month 60. The offer shows the kroner it would leave after spending at the player's level, not only the extra wage (worked example 25).
- **Ending extra shifts:** running extra shifts can be ended from the job view, from the next month. Quitting or changing job ends them.
- **Never in a slot:** extra shifts and hours never take an activity slot, and no wage is paid outside the income step. The month plan shows them as work blocks from the month they start (FR-52).
- More hours mean less free time (FR-33) and fewer activity slots (FR-52). The hours control shows how many slots the new hours give, and the limit where free time goes below 50, which is 25 h a week beside school.

#### FR-21: Tax

Tax is calculated from the year's total wage income at 2026 rates (rule 3).

**Consequences (testable):**
- An 18-year-old earning NOK 110,000 in a calendar year pays NOK 2,588, all of it trygdeavgift (worked example 5, F8).
- Each in-game year is one tax year. Trygdeavgift is 5.1% in in-game years 1-2 and 7.6% from in-game year 3 (rule 11). Every year uses 2026 rates (D6).
- The December summary shows the year's tax and the expected BSU deduction, which is paid when the player continues (rule 9).

#### FR-22: Saving and BSU

The player can save in a savings account at 2.87% a year or in BSU at 5.61% a year, and interest is added under rule 2. The BSU deduction follows rule 9. Realizes UJ-3.

**Consequences (testable):**
- NOK 10,000 in savings for 12 months gives NOK 10,289 (worked example 2, F2).
- When the player pays no tax, the game says plainly that the BSU deduction is NOK 0, and shows that BSU still pays off through the higher interest (worked example 6).
- The game shows the real interest even when it's small. For example, NOK 3,000 earns NOK 84 in a year.
- BSU deposits are capped at NOK 27,500 per calendar year. The game accepts at most what's left of the year's cap and shows how much that is.
- BSU money can't pay for choices or cover a negative balance. The player can withdraw the whole BSU. It then closes for the rest of the playthrough, and any BSU deductions received are taken from the payout at once.

#### FR-23: Fixed and everyday costs

From the 18th birthday, the player pays for mobile and transport every month. Before that, the parents pay for them. On top of this, the player's spending level decides how much of their wage is spent each month (rule 16). Realizes UJ-4.

**Consequences (testable):**
- Fixed and everyday costs and spending are deducted at their place in the rule 1 order.
- **Spending level:** low is 60%, normal is 75%, and high is 95% of the wage income after tax. Costs come on top, so a new cost lowers what the player keeps by the whole amount. Spending is never more than the current account holds, and it never draws on savings or takes the account below NOK 0. The default is normal. With no wage, nothing is spent. A change in the money view applies from the next month. The shares are configuration.
- **It costs something either way:** in a month with spending, low lowers social life by 2, and high raises it by 2. High gives nothing in a month when interest is charged on debt (rule 12).
- **Shown as purchases:** the month summary shows what was spent in total, with a few example purchases that fit the player's age and spending level, such as canteen, clothes, and snacks. The examples are pre-written and have no amounts of their own, so the only figure shown is the one the engine calculated (NFR-4). They never name an activity kind (FR-53), such as cinema or concerts, because activities are paid on top of spending.
- **Transport:** it's the public transport ticket, or moped insurance and fuel in months when the player owns a moped (rule 14). The ticket and the moped costs are never charged in the same month. With a car licence, the player can start or stop borrowing the parents' car, an everyday cost with no binding period that pays for car fuel (FR-30).
- **Moped costs:** they're the player's own at any age, apart from any share of the insurance the parents pay (FR-29).
- **Before 18:** a player with no job who keeps a NOK 10,000 pengegave in savings never goes below NOK 0 (worked example 15). The MVP has no pocket money (§4.3). The month summary says when the player takes over the bills at 18.
- **Everyday costs:** some event options start, change, or stop a monthly everyday cost, such as canteen lunches or a subscription. It's charged with the fixed costs until a later choice stops it, and it links to the choice that started it. From the money view, the player can stop one that has no binding period. A cost with a binding period can't be stopped before the period ends.
- **Card:** with card use on, card-payable costs go on the card first, then spending as far as it fits under the limit, and the rest comes from the current account. That isn't shown as a declined purchase (FR-26). While a payment plan blocks the card, card use is off.

#### FR-24: Unexpected expenses

Unexpected expenses come up at random, such as a broken phone screen or a moped repair. Realizes UJ-4.

**Consequences (testable):**
- An unexpected expense is stored with a system cause, so "Hvorfor?" explains it from the rules.
- **How often:** one unexpected expense per in-game year by default, in a drawn month, of a kind that fits the player then. The number, amounts, and conditions are configuration.
- An expense tied to something the player owns, such as a moped repair, is drawn only while they own it.
- An unexpected expense is a deduction, not an event, so it doesn't use an active month. If it pushes the account below zero, rule 8 starts a crisis month where the player can respond.

#### FR-25: Consumer loans

From age 18, the player can take a consumer loan, repaid in equal monthly instalments (an annuity loan) at a fixed 15% a year (rule 4).

**Consequences (testable):**
- NOK 20,000 over 12 months gives monthly payments of NOK 1,805, a final payment of NOK 1,808, and NOK 21,663 in total (worked example 3, F1).
- A loan needs a steady wage, and it can't be taken in months 59-60 (rule 6).
- The amount can be from NOK 5,000 up to 3× the average monthly wage over the last three months, minus the player's other debt, not counting family loans, rounded down to the nearest NOK 1,000. Below NOK 5,000 no loan is offered. The multiplier is configuration.
- The term is 12, 24, 36, 48, or 60 months. A loan may run past age 20, and what's left counts as debt in the ending.
- The player can have one consumer loan at a time, and can pay off what's left at any time with no fee.

**If left out (Extension, §4.4):** there is no consumer loan. The FR-18 consumer-loan row and its month-49 offer message (FR-55) drop, and so do the loan in FR-48's open options, paying off a consumer loan in FR-45, its tip in FR-19, and the loan refusals in NFR-7. Rule 4 stays, because payment plans (rule 15) and family loans (FR-27) use it, and F1 stays an engine test of rule 4.

#### FR-26: Credit card

From age 18, a player with a steady wage can get a credit card, under rule 5. Realizes UJ-4.

**Consequences (testable):**
- If the wage stops later, the card stays open.
- The limit is fixed for the playthrough. It's configuration, NOK 5,000-10,000, with NOK 10,000 as the default.
- When taking the card, the player chooses how the bill is paid: the whole balance, the minimum, or a fixed amount of at least the minimum, in steps of NOK 100. They can change it at any time, and the change applies from the next bill. If nothing is set, which only happens in engine tests, the whole balance is paid.
- The bill is paid at the debt step and never takes the current account below NOK 0. Paying less than the minimum counts as a missed minimum (rule 8).
- A missed minimum leaves an overdue amount, and later payments cover that first (rule 5).
- An extra payment lowers the balance at once. It doesn't undo interest already charged that month.
- A NOK 3,200 balance, with only the minimum paid each month, is paid off after 13 months, NOK 3,606 in total (worked example 4, F3).
- While card use is on, purchases and card-payable monthly costs, such as fuel, go on the card as long as they fit under the limit. An event purchase that doesn't fit is paid from the current account as a whole, and the game says the card was declined. Spending follows FR-23.
- The player can turn card use off at any time.
- Interest can take the balance above the limit. The card then takes no purchases until the balance is below the limit again.
- The game shows, in kroner, this month's interest and the total cost of paying only the minimum, for the player's own balance.

#### FR-27: Help from family

In some events and crisis months, family can give or lend money. Talking to family can also bring advice instead of money. Realizes UJ-4.

**Consequences (testable):**
- Help isn't always on offer, and it often covers only part of the amount. Whether family can help, and how much, is drawn once per event or crisis month and stored. Asking again in the same event or crisis month shows the same answer, moves no money, and uses no step.
- A family loan carries 0% interest and is repaid in monthly instalments set by the event.
- Each instalment is the loan divided by the number of months, rounded to whole kroner, and the final instalment makes the total exact. NOK 5,000 over 6 months is NOK 833 five times and NOK 835 (worked example 8).
- If the player can't pay an instalment, it moves to the end of the loan, and stress rises, but no higher than 50 (rule 12). A family loan never takes the account below NOK 0. What's left at 20 counts as debt.
- A player has at most one family loan at a time, from age 15. While it's being paid back, family can still give advice or a gift, but doesn't lend more.
- A family loan doesn't count towards the debt trigger (FR-32). Otherwise a teenager with no income would go into crisis from any loan.

### 5.10 Moped and licences

**Description:** At 16 the player can get the moped licence and a moped. By 18 some players get a car licence from their parents, and others can pay for one. These add costs, choices, and something to sell. The licences and buying a moped stay open once unlocked (FR-48). Realizes UJ-2, UJ-3, and UJ-4.

**Functional Requirements:**

#### FR-28: Moped licence

From age 16, the player can choose to take the moped licence. They pay for driving lessons, the mandatory lessons, and the licence itself, at real prices, and have to pass a short driving game (FR-51). Realizes UJ-2.

**Consequences (testable):**
- Apart from the driving game, taking the licence is only a payment. A player who doesn't pass keeps the licence option open and can try again (FR-51).
- The recap's teaser names what the licence costs.
- Every price has a source and a date (#29).

#### FR-29: Own a moped

From age 16, the player can own a moped. They choose whether to buy one, and now and then a family message, drawn at random, offers one as a gift. Buying one is how saving up pays off, as in UJ-3. Realizes UJ-3 and UJ-4.

**Consequences (testable):**
- **One moped, with a licence:** the player can own one moped at a time, and only with the moped licence.
- **Gift offers:** a gift offer comes only to a player who has the moped licence and owns no moped, at most once per playthrough. A gift moped is a used moped. The offer is a drawn offer that can be accepted or declined in the month it arrives (FR-55), and its chance per in-game year is configuration.
- **Resale value:** it starts at the price paid, or at the used price for a gift. It drops by 15% of that each year, a little each month, but never below 20% (rule 14). A used moped sold after two years fetches NOK 8,152 (worked example 19). Tracking actual use comes later.
- **Costs only while owned:** insurance and fuel are charged only in months the player owns the moped (FR-23). Moped repairs follow FR-24, and moped events are drawn only while they own one. Whether the parents pay part of the insurance is drawn once, when the player gets the moped, and stored (cut list: the parents' share of the moped insurance).
- **Selling:** the player can sell the moped in any month at its current resale value. Public transport comes back from the next month, and the moped disappears from the room.

#### FR-30: Car licence

By age 18, some players get a car licence as a gift from their parents. In month 37, the engine draws once whether the gift comes, and stores the result. One family message tells the result in month 37 (FR-55): either the gift, which applies at once, or that the parents can't pay and the player can take the licence themselves. A player without the gift can pay for the licence at a real price. With a licence, the player can borrow the parents' car, and that opens car events. Borrowing costs fuel for as long as the player keeps it going (FR-23). Realizes UJ-4 and UJ-6.

**Consequences (testable):**
- The gift is drawn before the paid licence is offered. A player with the gift is never offered the paid licence.
- The gift costs the player nothing. Car fuel is a transport cost (FR-23).
- The paid licence works as in FR-28, with the driving game. The gift needs no driving game, because the parents' gift is the finished licence.
- How often the gift comes is configuration (OQ-8).
- Every price has a source and a date (#29).

### 5.11 Warnings and crises

**Description:** The game warns the player before money trouble turns into a crisis, and the player decides whether to act. Only the engine starts a crisis month. Realizes UJ-4.

**Functional Requirements:**

#### FR-31: Card warning

Each time a card bill isn't paid in full, and the month before had a bill paid in full or no card balance, the game warns the player in that month. The warning shows this month's interest, the balance, and how long the bill would take to pay and what it would cost if only the minimum were paid from now on. It says whether the player couldn't pay the whole bill or chose to pay less. The player then chooses whether to act, for example by talking to family, turning card use off, taking extra shifts, or selling something. Realizes UJ-4.

**Consequences (testable):**
- The warning is the event of the month in which interest starts. It's shown before the next interest charge.
- In a crisis month, the crisis shows the warning's figures first, and the warning counts as shown.
- The warning doesn't start a crisis month on its own.
- When the reason is "chose to pay less", one option switches the payment to the whole balance. Other options are shown only when they're possible, as in FR-32.
- Test: the setting is the whole balance, the bill is NOK 6,000, and the account and savings hold NOK 4,000. The engine pays NOK 4,000, charges NOK 113 interest, and shows the warning in that month (worked example 7).

#### FR-32: Crisis month

The engine checks rule 8 at the end of every month. When a trigger is true and no cooldown is running, the next month is a crisis month. The triggers are:
- the current account is below NOK 0
- the card minimum has been missed two months in a row
- debt, not counting family loans and after subtracting savings and a positive current account, is above 3× the average monthly wage over the last three months, or above NOK 5,000 if that's higher

A crisis month has up to three linked choices with realistic actions, such as selling something, taking extra shifts, taking a job, lowering the spending level, withdrawing BSU, asking for a payment plan, asking family, or ignoring it. The engine calculates the effect of each one. Realizes UJ-4.

**Consequences (testable)**, in parts that can each become a story:

##### FR-32a: Triggers and when a crisis month starts

- **Always started:** F4 has one test per trigger.
- **Check when it opens:** when the crisis month opens, after that month's income and costs, the triggers are checked again. If none is true, the crisis is skipped with a short note, with no crisis stress and no cooldown, and the month's event is chosen again (FR-46, worked example 10).
- **One at a time:** however many triggers are true, one crisis month starts. Its event follows the most urgent trigger: below zero, then missed minimum, then debt. It names every true trigger.
- **Cooldown:** no new crisis month starts in the two months after one, except month 60 (FR-41). The game shows any trigger that's true during a cooldown. The cooldown is configuration.

##### FR-32b: Crisis events, steps, and options

- **Crisis events:** each is written for one trigger and an age range, and the library of about 10 covers every trigger that can occur at each age. Before 18, only the below-zero trigger can occur.
- **Which crisis event:** crisis events can repeat. The engine draws among those that fit, preferring the one seen longest ago, and stores the draw (FR-12).
- **Linked choices:** a crisis event has up to three steps, and each step offers the options that are possible then. Starting something with a later effect, such as extra shifts or a payment plan, counts as a step.
- **Options that work:** a crisis option is shown only when it's possible. Selling needs something to sell, extra shifts need a job and hours left under rule 10, taking a job needs no job, lowering the spending level needs a level above low, withdrawing BSU needs a BSU, a payment plan needs a card balance and no plan already running, and turning card use off needs it to be on. Asking family and ignoring it are always offered. An option whose effect would land after month 60 isn't shown, and each option says when its effect lands.
- **Payment plan:** the card balance becomes a 12-month annuity loan at the card's rate, and the card is blocked until the plan is paid off (rule 15, worked example 12). The option shows the monthly instalment against what the player has left each month, because instalments are always charged (FR-45).
- **Money actions in a crisis month:** money actions and open options stay available, use no step, and the triggers are checked again after them.
- **Money arriving in a crisis month:** money from a crisis choice or a money action goes first to a negative current account, then to overdue card minimums, and the rest stays in the current account.
- **Activities:** they can be planned in a crisis month as in any month (FR-53), and use no step.
- **Follow-ups:** a follow-up that's pushed out is handled under FR-46.

##### FR-32c: How a crisis month ends

- **Ends when solved or after three steps:** after each linked choice, the engine checks the triggers again. The crisis month ends as soon as none is true, when the player ignores it, or after the third step, even if a trigger is still true.
- **Never fatal before 20:** a crisis doesn't end the game, and going below zero only starts a crisis month. It isn't a loss. Ignored debt keeps growing under rules 4-5 and starts new crisis months after each cooldown.

### 5.12 Wellbeing and visible consequences

**Description:** The player sees what their choices do to their life, not only their money. Realizes UJ-1, UJ-4, and UJ-5.

**Functional Requirements:**

#### FR-33: Wellbeing

Wellbeing is one score from 0 to 100, made from three parts (rule 12):
- **Stress** rises with interest on debt, crisis months, working too much, a very low social life, and postponed family-loan instalments, and falls again when they stop.
- **Free time** follows the hours of school and work.
- **Social life** follows the choices made in events and the spending level, and falls when the player works too much.

Activities (FR-53) change stress and social life in the month they happen. The change counts towards that month's score, and so towards ending wellbeing, but doesn't carry to the next month. The social life that carries over follows events, the spending level, and working hours. The life goal sets how much each part counts. Realizes UJ-4, UJ-5, and UJ-6.

**Consequences (testable):**
- Each part and the score stay between 0 and 100.
- Every event choice has a stored effect on stress and social life, which may be 0, and it isn't shown before the pick (FR-13). Free time changes only with hours.
- **The hollow win still holds:** a money chaser who fills every slot with activities at the effect limits, within the monthly cap, still ends below the threshold, at 42, 46, and 37 with the weights of goals 1, 2, and 3 (worked example 26c). The content check fails if a change to the catalogue, the limits, the slot divisor, or the threshold lifts any of them to 50 or above.
- **The boundary moves with activities:** with activities at the limits in every slot, the 26 h run on normal spending in worked example 17b rises from 41 to 52, a real win (worked example 26d). With the catalogue's best free activities, the content check reports the 17b boundary runs at 25 h and 26 h and careless run 21c, so the threshold and the activity effects are tuned together (OQ-8).
- **Usual and this month:** the game shows stress and social life both as the usual value, which carries over and which rule 12's rows use, and as this month's value with activities, so the player sees what the month's activities added. "Hvorfor?" explains the social-life row as «Det vanlige sosiale livet ditt er under 20».
- In UJ-4, extra shifts lower free time, cutting back lowers social life, interest raises stress, and paying the debt off lets it fall again (worked example 17).
- The ending uses ending wellbeing: the average score in months 19-60, rounded to a whole number. Easing off can't make up for the years before it: a money chaser who works 40 h a week until month 48 ends at 34, and one who stops at month 24 ends at 43, both below the threshold (worked example 17b).
- Permanent debt on the high spending level scores below a debt-free player on normal, because high gives no social bonus while interest is charged (rule 12).
- The game shows the score, its three parts, and the threshold. Once month 19 has been calculated, it also shows the average so far.
- The weights, start values, monthly changes, and threshold are configuration (OQ-8).

#### FR-34: Room layers

The player has one room that changes with choices and belongings. Realizes UJ-1 and UJ-4.

**Consequences (testable):**
- The room changes right after a choice that affects it. For example, the moped appears when the player gets it and disappears when it's sold.
- **Layers:** the room is built from one layer per belonging, at most 6 in the MVP, each with a few states. It always shows the current state of every belonging, so several changes in one month all show.
- **From flags:** each layer follows the playthrough's flags, so the room looks the same after a reload and on every device.
- Each room state has a short text that says what's in the room and what just changed (NFR-2).

#### FR-35: Visible future opportunities

After a choice, the game shows what the choice opened or closed. Realizes UJ-1.

**Consequences (testable):**
- What is shown comes from the event's flags, with a short text for each in the event (see the event schema in the addendum).

**If left out (Extension, §4.4):** the game doesn't show what a choice opened or closed. Flags still decide follow-ups, unlocks, and the room (FR-46, FR-18, FR-34), and the event schema keeps the texts so they can be added later.

### 5.13 Explaining consequences

**Description:** Every change can be traced to a cause, so the player can always find out why something happened. The game also shows what another choice would have led to, and says where it simplifies reality. Realizes UJ-3 and UJ-5.

**Functional Requirements:**

#### FR-36: Cause links

Every effect in the engine stores what caused it. An effect with no choice behind it is stored with a system cause. Realizes UJ-3.

**Consequences (testable):**
- Every cause link points to a choice that exists in the playthrough, or to a rule (F10).
- **Shared causes:** an effect with several causes stores each one with its share in whole kroner, and the shares add up to the effect. Interest on a card or loan is shared between the choices that make up the balance, and savings interest between the deposits, in proportion to each one's part of the balance.
- **Effects that continue:** an effect that keeps following from an earlier choice links to that choice, such as the moped's fuel and insurance, a subscription's monthly fee, or interest on a purchase made on the card.
- **System causes:** wages, tax, the mobile cost, unexpected expenses, and spending have a system cause. Interest on spending put on the card links to the spending's system cause. Setting a level or hours has no kroner of its own, so it isn't ranked in FR-42, and "Hvorfor?" explains it from the rules.
- **Wellbeing:** a wellbeing change links to the choice whose option set it, or to a rule, such as stress from a crisis month. An activity's effect links to the activity.
- **Activities:** an applied activity is a choice (FR-53). Its cost, and anything that follows from that cost, such as card interest, links to the activity.

#### FR-37: Echo badges

When an effect comes from an earlier choice, an echo badge marks the effect and links to that choice. Realizes UJ-3.

**Consequences (testable):**
- An echo badge is shown only for effects that carry a cause link to an earlier choice.
- An echo badge has a text that names the earlier choice, so a screen reader reads it out.

**If left out (Extension, §4.4):** no badge marks an effect from an earlier choice. Cause links (FR-36) are still stored, and "Hvorfor?" (FR-38) still names the earlier choice. A boomerang follow-up arrives without a badge.

#### FR-38: "Hvorfor?"

The player can press "Hvorfor?" on a change to see why it happened. The explanation links the change to the choice behind it. Realizes UJ-3.

**Consequences (testable):**
- An effect with a system cause is explained from the rules.
- The explanation of an effect with shared causes lists up to the three largest shares and sums the rest.
- The BSU comparison ("in BSU this would have been NOK …") is optional (cut list: the in-play lines).

#### FR-39: "If you had chosen differently"

The engine calculates what another choice would have led to. It does so only where it can calculate the result reliably, from the choice's own effect and the rules for interest and instalments, and never with AI. Realizes UJ-5.

**Consequences (testable):**
- **The comparison:** the line compares the chosen option with the option in the same event whose direct kroner effect differs most from it. Ties go to the option listed first.
- **Debt cost:** if the choice put money on a card or a loan, the line shows the interest linked to it (FR-36). For example: «Byturen på kortet sto for 406 kr av rentene dine.»
- **Money kept:** otherwise, if the two options' direct effects differ, the line shows the difference grown with savings interest (rule 2) from the month after the choice to the 20th birthday. Spending NOK 15,000 of the pengegave in month 1 instead of saving it gives «Hadde du valgt å spare alt, ville du hatt 17 270 kr mer da du fylte 20.»
- **No figure to show:** if neither applies, the line is a pre-written text, plus the difference in the two options' stored wellbeing effect where there is one. The game never shows a figure the engine didn't calculate.
- **Activity groups:** for a group of activities on the ending screen (FR-42), the line is "money kept", as for a single choice. It shows the group's cost, each part grown with savings interest from the month after it was paid to the 20th birthday, as if the player had done none of them, plus any card interest linked to the group (FR-36). The group still ranks by its kroner effect in FR-42, the plain sum. The line also names the group's summed wellbeing effect (FR-42), so free time isn't shown as pure loss (NFR-8). D15 covers groups (worked example 28).
- **No re-runs:** a line never re-runs later months or events, so no earlier game states need to be stored.
- **Where:** the lines for the choices on the ending screen stay in the MVP. The lines during play are optional (cut list: the in-play lines).

#### FR-40: Disclosed simplifications

Where the game simplifies reality, it says so (D1-D26 in the brief's addendum). Every mechanism or feature with a simplification has a disclosure. Each disclosure is shown the first time its mechanism or feature appears, behind an info icon or under "Hvorfor?". All the texts are also collected on one page, "Om tallene".

**Consequences (testable):**
- **Once per account:** a disclosure the player has seen isn't shown again on another device or in a later playthrough. It stays behind its info icon and on "Om tallene".

**If left out (Extension, §4.4):** no disclosure is shown during play, and FR-43 has no seen-disclosures record to keep. This conflicts with A-23, which makes the disclosures a requirement, and with SM-2, which validates against FR-40, so the team aims to build it (§4.4).

### 5.14 Ending and replay

**Description:** At 20, the game ends with one of four endings and a summary of the life. The player can start again from 15. Realizes UJ-5.

**Functional Requirements:**

#### FR-41: Four endings

At the 20th birthday, after month 60, the engine checks the endings in this order:
1. **Loss:** a rule 8 trigger that was true at the end of month 59 is still true at the end of month 60. The consequences are shown clearly, and the text also reflects wellbeing, for example "you had a good life, but the economy did not hold".
2. **Real win:** the goal is reached (rule 13), and ending wellbeing is at or above the threshold (rule 12).
3. **Hollow win:** the goal is reached, and ending wellbeing is below the threshold.
4. **Goal not reached:** none of the above. This is neither a win nor a loss: saving little or spending a lot is allowed. The player gets general advice on modest savings goals, what they bring, and what not saving costs.

Realizes UJ-5.

**Consequences (testable):**
- Every end state gives exactly one valid ending screen (F9, one test per end state).
- Every ending is calculated from measurable state and works with no AI.
- Ending wellbeing exactly at the threshold gives the real win, and a goal measure exactly at its target counts as reached (worked example 18).
- If a trigger is true at the end of month 59, month 60 is a crisis month, even during a cooldown.
- A trigger that first becomes true at the end of month 60 doesn't give a loss. The summary names it.
- Test: minimum missed in months 58 and 59 and paid in month 60 is not a loss (worked example 11).

#### FR-42: Ending summary

The ending shows how the life went and the three choices that mattered most, ranked by their effect in kroner. The player can open each of them to see the "if you had chosen differently" line (FR-39) and a short pre-written text about it. Realizes UJ-5.

**Consequences (testable):**
- **Kroner effect:** a choice's effect is the sum of the money effects linked to it over the playthrough (FR-36), with money in as plus and money out as minus. Moving money between the player's own accounts, taking a loan, and paying down debt count as zero, but the interest that follows counts. Belongings aren't valued, and a sale counts when it happens.
- **Ranking:** choices are ranked by the size of their effect, plus or minus. Ties go to the choice made first: by month, then by the order the server confirmed them in. Choices with no kroner effect aren't ranked.
- **Activities as groups:** applied activities of the same kind, such as all concerts, are ranked as one entry with their summed kroner effect, and the entry counts as made at the time of the first one. One activity alone is never ranked, and can't take the hollow-win place either (cut list: grouped activities).
- **Fewer than three:** if fewer than three choices have a kroner effect, the summary shows the ones there are.
- **Texts:** a choice that cost money gets a tip on how the cost could have been avoided or made smaller. A choice that brought money gets a short line on why it paid off. The texts are general and pre-written (FR-19).
- **Hollow win:** one of the three is the choice that hurt wellbeing most, by its linked wellbeing changes (FR-36), even if it wouldn't make the top three by kroner. An activity group counts here by its summed wellbeing effect, like any other choice. If it isn't already there, it takes third place. If no choice lowered wellbeing, that place shows the largest system cause instead, such as crisis months, explained from the rules.
- Only the choices shown can be opened.

#### FR-43: Play again

The player can start a new life from age 15. Realizes UJ-5.

**Consequences (testable):**
- **A fresh start:** the player chooses a life goal again and gets a newly drawn pengegave. Nothing in the game carries over from the last playthrough. Only the record of which disclosures the account has seen stays (FR-40).
- **No crossroads:** a replay always starts at 15, never from a point partway through.
- **Different choices, different story:** two playthroughs with different choices give different stories.
- **How it's checked:** in the content check, pairs of playthroughs with random choices share, on average, no more than two-thirds of their regular events. A second check uses pairs with the same seed and different choices, so the difference comes from the choices alone, and each pair must differ in at least one follow-up.
- **One life at a time:** an account has at most one playthrough in progress.
- **Starting over before 20:** the player can end the current life from the menu and start a new one, after confirming. The ended life can't be resumed and is deleted.
- **After the ending:** a finished playthrough is kept, read-only, until the player starts a new life or deletes the account. Then it's deleted.
- **Coming back after the ending:** a player whose life has ended sees the ending summary again, with **Play again**, instead of a recap.

### 5.15 Minigames

**Description:** Minigames come up along the way, so the player sometimes uses skill rather than only choosing. In the MVP, minigames are for the licences, such as a driving game. More can come in V2, such as earning pocket money (§4.3). Realizes UJ-2.

**Functional Requirements:**

#### FR-51: Minigames

Some events and options start a short, turn-based minigame. To take a licence, for example, the player drives a route step by step and has to follow the rules at each step (FR-28). The MVP's driving game is turn-based on purpose: the server can judge every answer, and it works the same for every player. Realizes UJ-2.

**Consequences (testable):**
- **The server runs it:** the server draws the route from the playthrough's seed (FR-12), sends one traffic situation at a time, judges each answer, and decides the result. The device sends only the player's answer (NFR-7).
- **The engine still decides the money:** what the result leads to is set in the event, and the engine calculates every effect (NFR-4). A minigame never sets an amount.
- **States:** a minigame is not started, started, passed, or not passed. Each answer is saved like a choice, so closing the game, losing the connection, or changing device continues the same attempt (FR-6, FR-7, FR-8). There's one attempt a month.
- **Payment and retries:** the licence is paid for when the player starts the first attempt. A player who doesn't pass keeps the option open and can try again from the next month. A retry follows "Can't pay yet" in FR-48 if it has a fee (OQ-16).
- **Real choice:** a minigame started from an event option uses that month's real choice, and one started from an offer message or the money view doesn't. The player can't continue to the next month with an attempt unfinished (FR-49).
- **Works for every player:** with no timing, motion, or gestures, it can be played on a phone, with a keyboard, and with a screen reader, so nobody needs a way past it (NFR-1, NFR-2).
- **Fits the pace:** a session with a minigame still fits 10-15 minutes on a phone (checked in playtests).
- **Tests and test users:** engine tests feed in the answers, and seeded test users already hold a licence (NFR-6, NFR-9). No request can skip a minigame.
- **Reaching it in tests:** the playtest script and the seeded runs each include a licence, because a player who never takes one never meets a minigame.

### 5.16 Playtest support

**Description:** The playtest environment keeps the records that the metrics in 7.1 need.

**Functional Requirements:**

#### FR-50: Playtest records

In the playtest environment only, the game keeps a small record for each account, so the metrics in 7.1 can be measured even though FR-43 deletes earlier lives.

**Consequences (testable):**
- **What's counted:** time to the first choice, session lengths, the days the tester played, the highest month reached in each playthrough, completed playthroughs with their ending, goal, and net savings at 20, playing again after an ending, and starting over before 20. For the month plan and the phone, the record also counts the months with at least one applied activity, the months whose applied activities differ from the month before, the time from the first change to the month plan to continuing, and invitations whose activity was applied against those received. No choices or other game content are kept.
- **How time is measured:** on the server. Time to the first choice runs from creating the user to the first confirmed real choice, so the time before that isn't included. Session length adds up the time between confirmed actions in one in-game year, and a gap above 10 minutes (configuration) doesn't count.
- The records survive when a playthrough is deleted (FR-43).
- **Deleting an account:** when a tester deletes their account (FR-44), the record goes with it, and only a count of testers who left is kept, with no link to anyone. A tester who creates a user again with the same email address keeps the same tester code.
- **Switched off elsewhere:** the setting is off by default and on only in the playtest environment. It's off in the examiner's local run, and a test covers both states.
- **Test users:** accounts used for checks (NFR-11) are marked and left out of the records and the export.
- **Tester code:** the team gives each tester a random code with the invitation, for the quiz, the survey, and the records. The key from email address to code is kept apart from the results. Records are exported with the code instead of the email address, and deleted with the playtest accounts (NFR-3).

## 6. Non-Functional Requirements

### NFR-1: Platform and every screen size

LifeMode is a web app that runs in the browser, with nothing to install. It isn't a PWA in the MVP and has no offline mode, because the server decides every result (FR-8). It is designed mobile-first, and its layout adapts to phone, tablet, laptop, and desktop, down to 320 CSS pixels wide. It has:
- no horizontal scrolling
- touch-friendly controls
- no core function that works only on hover
- text that is readable on a small screen

**Browsers:** the two newest major versions of Safari (iPhone, iPad, Mac), Chrome (Android, Windows, Mac, Chromebook), Edge, and Firefox.

**Tested:** the main flow, from creating a user to the ending, is tested on Safari on an iPhone, Chrome on an Android phone, a tablet, and Chrome or Edge on a Windows laptop.

### NFR-2: Accessibility

The game meets WCAG 2.2 level AA. This includes contrast, keyboard navigation, text alternatives, form labels, clear error messages, and touch targets of at least 24 × 24 CSS pixels, with option buttons at 44 × 44 where possible.
- Everything the game shows as a picture also exists as text: each room state, the moped, each echo badge, and the wellbeing parts.
- Nothing is shown by colour alone. A money change has a sign and a word, not only red or green.
- Messages such as "saved", "offline", and the card warning are read out by screen readers.
- Login works with password managers and paste.
- The main flow, including minigames, can be played with a keyboard alone. A minigame has no time limits, motion, or gestures.
- The month plan works by tapping or selecting, and never needs dragging (WCAG 2.2, criterion 2.5.7). Each slot's state, empty or holding an activity, is available as text.
- New messages are announced to screen readers without interrupting what the player is doing.

It's tested with an automated accessibility check on the main screens, with no serious or critical findings, and by hand before each playtest, with a keyboard alone and with a screen reader on a phone.

### NFR-3: Privacy and data minimization

The email address and the password are the only real personal data the player types in. The game collects no real age, takes no free text beyond the email address, and simulates the whole economy. Game data is tied to the email address, and the attempt limits briefly process network addresses, so these count as personal data too.

**How the data is handled:**
- The email address is used only for login and password recovery, and is never shown in the game or used for marketing.
- Passwords are stored only as a hash, never in game data. Neither the email address nor the password is written to the game's own logs.
- A player can reach only their own data.
- A player can delete their account and game data (FR-44).
- Before creating a user, the player sees short information in plain Norwegian: what is stored, what for, how long, how to delete it, and which services handle the data (the database host and any email relay). The full text can also be opened from inside the game.
- An account and its game data are deleted after 12 months without play (configuration). The player information says so, and no email is sent about it. If the deletion job is cut (cut list: login hardening), the player information doesn't promise it, and the job goes on the "before go-live" list.
- The game uses no analytics, advertising, or tracking cookies or scripts, and loads nothing from third parties.
- Only the current playthrough, or the last finished one, is kept (FR-43). In the playtest environment, the records in FR-50 are the one exception, and the playtesters' information describes them.

**Playtests:** only 18-20-year-olds take part, and they see the player information before they start. Game data is exported with a random tester code instead of the email address. If the team links game data to survey answers, the code key is kept apart from the results. The key and the playtest accounts are deleted when the analysis is done, no later than the December delivery.

**Scope of the privacy work:** LifeMode is a school project. The team runs the playtest within the measures above and needs no approval for it. Who is responsible for the data, the legal basis, and what applies to players as young as 15 are settled only if the game is developed further (§4.3, #24).

### NFR-4: Correct, explainable figures

The backend engine decides every financial result and all critical game state, and the frontend never calculates them.

**Figures:**
- They follow Rule Set v1, use real Norwegian 2026 values, and are held fixed for the whole playthrough (D6).
- Every figure is stored as configuration with its source and date, never hard-coded.
- The worked examples are the test answer key. New rules get worked examples and unit tests in the same way (brief addendum, examples 7-28).
- **Exact arithmetic:** money and rates are calculated with exact decimals or whole øre, never binary floating point, so that rule 2's "0.5 rounds up" lands the same way every time. Example: 11,645 × 0.70 = 8,151.5 rounds to NOK 8,152 (worked example 19), but a float gives 8,151.4999… and NOK 8,151.

**Versions:** each playthrough keeps the configuration and content-library version (events, activities, and messages) it started with until it ends. A changed figure or event applies only to playthroughs started afterwards, and cause links keep pointing to the event version the player saw. A correction to player-facing text that changes no figure, option, or flag can apply to running playthroughs.

### NFR-5: Low cost

The examiner's local run costs nothing. The hosted playtest environment (NFR-11), including the email for password reset (#30), may have a low cost during the playtest period, which the team covers. The architecture names the expected cost. Nothing keeps costing money after the playtest.

### NFR-6: Runs from the README

An examiner can run the full application on a clean machine with Docker, following only the README, in about 15-20 minutes. The full stack starts with one command and needs only Docker. It must work without the team's cloud account or keys: every external service, such as the database host and email, falls back to a local stand-in when its key is missing, so the app runs locally with no secrets. Password reset works locally. Reset emails land in a local inbox or in the log, and the README says where to find them (#30). If no local inbox is available, the README points to an automated test that verifies password reset instead. The repo has a `.env.example`.

The README also provides test users seeded at useful states: just before 18 with a steady wage, in debt with a crisis due, and in month 59 close to each ending. A full game takes about an hour, so this is how the examiner reaches the card, crisis, and ending flows. The README covers what criterion 6 in the examiner's guide asks for.

### NFR-7: Robust against wrong input

The server decides every result. The device sends only the player's inputs, never a result: the option, money action, or activity they picked, plus changes to the month plan, a savings-target pin, a disclosure they've seen, ending a life early, an amount where one is asked for, or an answer in a minigame. The server ignores anything else. The server refuses:
- a choice or money action for an event or month that isn't the current one (FR-49)
- moving to the next month before the real choice is made, with a crisis unfinished, or with a minigame unfinished (FR-49)
- a second real choice in the same month (FR-49)
- an option that wasn't offered, was shown as unavailable, or hasn't unlocked yet (FR-18)
- more working hours than rule 10 allows for the month they apply from, including extra shifts (FR-47)
- a loan or credit card before the 18th birthday (rule 6), a card or loan with no steady wage (FR-25, FR-26), or a loan in months 59-60 (rule 6)
- turning card use on while a payment plan blocks the card (rule 15)
- a BSU deposit when the year's cap is used up, or after the BSU has closed (FR-22)
- selling or using something the player doesn't have, such as a moped they don't own (FR-29)
- a second moped, or a moped without a licence (FR-29)
- the paid car licence before the draw or after a gift (FR-30)
- the experience bought when available money after debt is below its price, for example with a loan payout (FR-9, rule 13)
- an amount that isn't in whole kroner, is zero or below, or is outside the option's allowed range
- a minigame answer with no started attempt, for a situation that isn't the current one, or a second answer to the same situation (FR-51)
- a second minigame attempt in the same month (FR-51)
- an activity with no empty slot left, one that isn't available (its invitation came in another month, it hasn't unlocked yet, or its flags don't fit), the same activity twice in a month, or one the player can't pay for on top of what's already planned (FR-52, FR-53)
- a change to the month plan for a month that isn't the current one, or after the player has continued (FR-49)
- continuing with a month plan that has changed since the device loaded it (FR-49)
- an offer taken after it has expired: a drawn offer after its month, or a dated offer after its last day (FR-48, FR-54)
- a choice after the game has ended, or in a playthrough that no longer exists
- a request for another player's game (FR-2)
- a malformed request, such as a missing field or a value of the wrong type

Five cases aren't refusals, and each has its own test:
- a BSU deposit above what's left of the year's cap is cut to fit (FR-22)
- a summer job offer above the monthly cap is cut to fit (FR-47)
- a summer job that later hours cut to 0 h is cancelled with a note (FR-47)
- a card purchase that doesn't fit under the limit is paid from the current account (FR-26)
- a planned activity the player can no longer pay for, or is no longer eligible for, when they continue is dropped with a note (FR-53)

**Consequences (testable):**
- A refusal leaves the game unchanged, returns the current progress, and, where the player could see it, shows a short message in plain Norwegian.
- A repeated request applies the action once and returns the same result as the first time.
- Each case in the list has its own automated test (NFR-9).
- Refusals are logged without the email address or the password.

### NFR-8: Tone and content

Player-facing text is in Norwegian, in plain language a 15-year-old understands.
- **Tips:** they sound like tips, not lectures.
- **Warnings, crises, and endings:** they state the consequence plainly and don't scold. "Goal not reached" is never framed as failure.
- **Actions, not quizzes:** options and offers read as actions the player takes, never as quiz answers with one right option. Free time and activities are never framed as wasted money.
- **Visual style:** grown-up, not childish.
- **Credit and BSU:** these get more explanation than the rest, because most players have never used credit and BSU is what they understand least.
- **Age-appropriate content:** all content suits a 15-year-old. Chance-based purchases are shown as a cost, never as a reward.
- **Tobacco and alcohol:** the MVP has no tobacco or alcohol choices, and no content markets them. Invitations and activities, such as parties and concerts, never mention alcohol or tobacco.
- **Messages:** senders are fictional, and messages sound like the people sending them. A message from family can give advice, but never personal financial advice.

### NFR-9: Automated tests

The engine tests, meaning the worked examples and the F-criteria, can be run by following the README, and they run in GitHub Actions on every pull request. So do the input-refusal tests (NFR-7), the content check, including activities and messages (FR-17, FR-43, FR-46, FR-55), and the automated accessibility check (NFR-2). The results of manual tests (NFR-1, NFR-2) and the aggregated playtest results are kept in the repo.

### NFR-10: Responsiveness

Every choice is a round trip to the server, so the game has to answer fast enough to feel like a game. Measured on a mid-range phone on a throttled 4G connection, against the playtest environment (NFR-11):
- After the player picks an option, the result shows within 1 second for 9 out of 10 choices, and within 3 seconds for all of them.
- A quiet-month summary, and the plan after placing or removing an activity, show within the same times.
- On a first visit, the first screen is usable within 3 seconds.
- If the server has been asleep, the game shows a loading message within 1 second, and the first screen is usable within 10 seconds.

These are starting values, like the targets in 7.1. When the connection is lost, FR-6 and FR-8 apply instead.

### NFR-11: Playtest environment

The playtests run on one hosted environment that testers open on their own phones.
- It runs the same version as the README's local setup, at a low cost during the test period only (NFR-5).
- It stays available for the whole test period, which lasts at least 3 days. The team can extend it later.
- Player data is stored in the EU/EEA.
- An automated check logs in with a test user every day of the test period and alerts the team if it fails.
- Password reset works there (FR-3, OQ-4).
- The architecture names the provider and tier, and the limits that matter for the test: pausing or sleeping when idle, storage, number of users, and email quota.

## 7. Success Metrics

### 7.1 Playtest

Each metric has an ID (SM-N) that stories, tests, and the report can refer to, and the Validates column names the FRs and journeys it checks. Counter-metrics in 7.2 are CM-1 to CM-5.

There are 10-20 playtesters before the December delivery, all 18-20-year-olds. The targets below are starting values, which can change once real data exists.

| ID | Signal | Metric | Target | Validates |
|---|---|---|---|---|
| SM-1 | Understanding | Can explain how an earlier decision affected a later outcome | 70% or more | FR-36, FR-38, FR-42, UJ-3 |
| SM-2 | Understanding | 5-question money quiz, before and after | Higher after | FR-19, FR-38, FR-40 |
| SM-3 | Understanding | Can say what the wellbeing score shows, and why their ending came out as it did | 60% or more | FR-33, FR-41, FR-42, UJ-5 |
| SM-4 | Understanding | Can explain why more work hours gave them fewer activity slots | 60% or more | FR-47, FR-52, UJ-6 |
| SM-5 | Behaviour | Completes the full playthrough from 15 to 20 | 70% or more | FR-15, FR-41 |
| SM-6 | Behaviour | Comes back voluntarily for another sitting or a replay within 3 days | 50% or more | FR-15, FR-16, UJ-2 |
| SM-7 | Experience | "It felt more like a game than schoolwork" (1-5) | Median 4 or higher | FR-34, FR-52 to FR-56, UJ-6 |
| SM-8 | Experience | Describes two playthroughs with different choices as different stories | 60% or more | FR-43, FR-46, UJ-5 |
| SM-9 | Experience | "The money parts were easy to follow" (1-5) | Median 4 or higher | FR-38, FR-45, FR-57, UJ-4 |
| SM-10 | Pace | Reaches the first real choice, from creating the user | Within about 2 minutes | FR-1, FR-9 to FR-11, UJ-1 |
| SM-11 | Pace | One session, one in-game year | 10-15 minutes on a phone | FR-15, FR-46 |
| SM-12 | Mission | A parent or teacher wants to try the game after the team shows it to them | At least one, noted by the team | — |

- **Counted from records:** completion, coming back within 3 days, time to the first choice, and session length are counted from the playtest records (FR-50) in the playtest environment (NFR-11), across several sittings. Coming back is measured over each tester's own first 3 days, and the team sends no reminders during them. The window can be extended later if the test period allows it.
- **Written explanations (SM-1, SM-3, SM-4):** after the last sitting, each tester answers these in writing in a few sentences, without the game open. Two team members score each answer against a fixed rubric as correct, partly correct, or wrong, and only correct answers count towards the target. The rubric is written before the playtest, and disagreements are settled together. This replaces the testers' own judgement of whether they understood.
- **Quiz and survey:** the quiz is taken before the first sitting and after the last one. Its questions still need a teacher's review (#18). The quiz and the playtest survey use a random tester code instead of a name or email address.
- **Planning time:** the time spent on the month plan is counted from the records (FR-50), and the playtest survey asks whether planning the month felt quick (7.2).
- **Restarts:** starting over before 20 (FR-43) can lower the completion figure, so the team also counts how often testers do it, apart from playing again after an ending. Testers who deleted their account are reported as a separate count.

**Dates:** the playtest starts on 8 Dec 2026 (tentative, §4.4). The dates are checked against the delivery date once it is known (OQ-13). The playtest needs at least 3 days, plus time for analysis, before delivery.

**Validity limit:** all testers are 18-20, so the results show whether the game works for older players, not for 15-17-year-olds. A test with younger players is a later step.

### 7.2 Counter-metrics

- **CM-1. Completion rises but explaining falls:** players are tapping through without reading.
- **CM-2. The return rate rises but quiz scores don't:** the teaser hooks them, but they don't learn.
- **CM-3. Quiz scores rise but "more like a game" falls below a median of 4:** the game has turned into a lesson.
- **CM-4. Planning is ignored, with fewer than a third of invitations applied, or fewer than a third of months whose plan differs from the month before (FR-50):** the month plan adds screens without adding play.
- **CM-5. Sessions run past 15 minutes:** planning and messages slow the pace.

### 7.3 Functional criteria

F1-F10 from the brief apply, with these changes:
- F4 is read as: a trigger that's true outside a cooldown always starts a crisis month. During a cooldown the trigger is shown, not skipped silently.
- F5, the fallback when the AI fails, moves to V2, because the MVP has no AI.
- F9 has one test for each combination of crisis active or not, goal reached or missed, and ending wellbeing at or above the threshold or below it, plus both boundaries.
- F10 is read as "an earlier choice or a system cause" (FR-36).

## 8. Open Questions

The Blocks column names the work each question holds up. Gaps in the numbering are questions already resolved, recorded in the log.

| # | Question | Owner | Blocks |
|---|---|---|---|
| OQ-3 | Most figures got a source on 2026-11-12 (Rule Set v1 parameters, `research/prices-oq3-oq17-2026-11-12/`). Still open: a real moped insurance quote for a 16-year-old from an insurer's calculator (#29), the moped and car distances a month, and whether moped service is charged (#43) | Team | Writing those events and final tuning |
| OQ-4 | How password reset email works at low cost (NFR-5) in the playtest environment and at go-live. The examiner's local run is settled by NFR-6 (#30) | Architecture, first build sprint | FR-3 acceptance and the first playtest |
| OQ-8 | Tuning values: goal targets, spending levels and their social effect, wellbeing weights, start values, monthly changes and threshold (a player on low spending at exactly 25 h a week lands on it, worked example 17b), the idle check interval, the first card limit, how often family helps (the survey suggests about half of those in need), the parents' insurance share, how fast the moped loses value, how often the car licence gift comes, active months and their positions, unexpected expenses per year, boomerang delays, and which belongings get room layers. For the month plan and the phone: the slot divisor (20) and maximum (4), the activity effect range (±10) and monthly cap (±15), messages a month (3), invitations a month (0-2), extra-shift offers a year and the gift moped's chance (FR-55), and the planning policy of seeded runs (FR-9). The threshold and the activity effects are tuned together, because activities move the 25-26 h boundary (worked example 26d). What a slot is worth: a target such as "the fourth slot in a school month is worth at least N wellbeing points", with ±5 per activity and a ±20 cap as values to try. A candidate, not decided: whether a month with a social activity skips the low-spending −2 row | Team, when tuning | Event balancing |
| OQ-9 | What the avatar contains, and which control the player uses to set weekly hours (the mechanism is in FR-47). Whether an option's wellbeing effect shows before the pick was decided 2026-11-13: it doesn't (FR-13) | UX | Nothing |
| OQ-11 | Whether a delivery with no AI in the app meets the course requirements, including moving F5 to V2. So far it's checked only against part 1 of the examiner's guide, and the lecturer's difficulty rating leaned partly on in-app AI (#39). The team has decided to keep the AI driver in V2 and to update this PRD if that changes | Team | Nothing |
| OQ-12 | Whether typing the email address twice (FR-1) falls under an exception in WCAG 2.2 criterion 3.3.7, Redundant Entry | UX | Nothing |
| OQ-13 | The exact delivery date, and a check of the tentative dates in §4.4 (extensions frozen about 26-27 Nov, core playable about 1-3 Dec, playtest from 8 Dec) against it | Team | Sprint planning |
| OQ-14 | Host decided 2026-11-12: the reference setup in `architecture/technology.md` (Railway with Supabase Postgres, own login in the backend). Still open: confirm an EU/EEA region for the data (NFR-11) and a usable screen within 10 seconds after sleep (NFR-10), name the expected cost (NFR-5), and name the fallback if one of these fails (#68) | Architecture | First playtest |
| OQ-15 | The approved proposal isn't in the repo. The examiner's guide requires anything left out or changed from it to be described and justified, so the proposal needs adding to the repo, and the "Changes from the proposal" table in the addendum needs finishing | Team | Delivery |
| OQ-16 | The driving game: whether a retry has a fee and how large, how many situations a route has, and how many the player must get right. Its look is UX | Team, UX | Building it |
| OQ-17 | The activity catalogue: a starting catalogue of 6 basic and 16 invitation activities, with kinds and dated prices, is in `research/prices-oq3-oq17-2026-11-12/activities-spending.md`. Still open: the team approves it, finds sources for the nine prices marked [ASSUMPTION] (café, small concert, laser tag, birthday gift, pizza evening, restaurant, cabin weekend, local LAN, shopping trip), and sets each activity's effects (OQ-8). Also whether "school work" belongs in it as stress relief before exam months, or is left out, since the MVP has no school results | Team | Writing activities |
| OQ-18 | Whether friends such as Emma recur by name across a playthrough. In the MVP that's flavour only, with no relationship state | Team, UX | Writing messages |

## 9. Assumptions

Confirmed assumptions A-1 to A-30 are kept in `addendum.md`. The ones below change what version one delivers, so they are also stated here:

| ID | Assumption | Affects |
|---|---|---|
| A-26 | F5, the fallback when the AI fails, moves to V2 with the AI, because the MVP has no AI. Checked against part 1 of the examiner's guide only (OQ-11, #39) | §7.3, OQ-11 |
