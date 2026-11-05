---
title: LifeMode PRD
status: draft
created: 2026-10-22
updated: 2026-11-05
---

# PRD: LifeMode

## 0. Document Purpose

This PRD sets out what the first version of LifeMode must do and why. The team, the downstream BMAD work (UX, architecture, epics and stories) and the sensor all work from it. It builds on the product brief, `briefs/brief-Ibe160-prosjektmappe-2026-09-17/brief.md`. The brief's addendum holds the financial rule set (Rule Set v1), its parameters and the worked examples. This PRD refers to those rules by number ("rule 5") instead of repeating them.

This PRD's own `addendum.md` holds detail that belongs downstream, along with the reasons behind several decisions. Every decision and change is logged in `.memlog.md`. Where an older document disagrees, the latest logged decision applies.

**Tags:**
- **[ASSUMPTION]:** the facilitator inferred it, and the team has not confirmed it yet.
- **[OPEN]:** a question waiting for the team.
- **[NOTE FOR PM]:** something the team must handle outside the PRD.

## 1. Vision

LifeMode lets young people in Norway make expensive money mistakes before those mistakes cost real money. It is a life and money game for 15-20-year-olds. The player lives five years of a life, a few minutes at a time, and every choice carries forward. Spending the pengegave at 15 shapes what is possible at 18. Using a credit card like a debit card turns into months of extra shifts. The game always shows why.

**Built for Norway first and foremost.** The game uses Norwegian rules and life stages, such as frikort, BSU, credit only from 18 and the moped licence at 16, with real 2026 figures.

**Wellbeing counts too.** Good money management isn't just having the most money. The player's wellbeing (stress, free time and social life) counts in how the game ends, so getting rich at any cost gives a hollow win.

**It feels like a game, not schoolwork.** A 15-year-old should prefer it to scrolling on the bus. It should be more rewarding and smoother to play than Koll på cashen.

**Now (this PRD):** a complete game from 15 to 20, built on a pre-written event library and a deterministic financial engine, with no AI.
**Next:** AI-generated events as a second stage (brief Scope In #3-4). After that, moving out and rent, education, negotiation, a parent view and modes for schools.
**Later:** a wider simulation of adult life.

## 2. Target User

LifeMode is for young people aged 15-20 in Norway who want or need to learn about money and become more independent. It is aimed especially at those who are about to make their first real money decisions: a first pengegave, a first job, a first credit card. Some come by their own choice, and some because a parent or teacher told them to. They want to feel grown-up and make their own choices, and they don't want it to feel like homework. They play in short sessions, often on a phone and on the go.

What the survey "Unge og penger" found (133 responses):
- **They want to learn:** 63% would like to learn more about money.
- **Thinking ahead is the weak spot:** 88% know how much money they have, but only 38% think about how a purchase affects their money months ahead, and 39% often run out.
- **What they regret:** mostly small purchases that add up, clothes, trend buys and collectibles.
- **What they understand least:** BSU and credit.
- **Where they learn:** family is the main source of money, knowledge and help, and 88% learned most about money from family.

### 2.1 Jobs To Be Done

- When I'm about to make my first real money decisions, I want to see what they lead to before they cost me real money.
- When I have a few spare minutes, I want something more useful than scrolling that still feels like a game.
- When something changes in my money, I want to understand why, so I can do it differently next time.
- When I have a goal such as a flat or a big trip, I want to try different ways of getting there and see what each one costs me, in money and in the rest of my life.

### 2.2 Non-Users (v1)

- **Parents and teachers.** They may suggest the game, and they could pay for it later. But v1 is designed for the player alone, with no parent view, class mode or teacher tools. In UJ-1, Markus's mother has no account and can't see his game.
- **People under 15 or over 20.** The game covers the years from 15 to 20, and its rules and figures are tuned for that range.
- **Players outside Norway.** The rules, figures and texts are Norwegian.

### 2.3 Key User Journeys

- **UJ-1. Markus is told to try LifeMode before he spends his pengegave.**
  - **Persona + context:** Markus, 15, has just been told by his mother that he can't spend his whole pengegave on Monster and Fortnite. She suggests LifeMode, so he can see that saving a little now can pay off later, and that being careless with money can have serious consequences. He opens it slightly irritated, just to test it.
  - **Entry state:** No account, on his phone, possibly on the bus. His mother has no account and no view of his game.
  - **Path:** Markus reaches his first real choice within about 2 minutes.
    1. The first screen offers log in or create a new user. Markus creates one with an email address and password.
    2. He chooses his life goal: saving for something big, which for him is a flat of his own. The target is an amount the game sets and that can be reached by 20, such as a start on the deposit, since a whole flat is out of reach by then.
    3. He chooses his avatar. In the game he is 15 and has just received a pengegave, a random amount between NOK 10,000 and NOK 30,000.
    4. His first real choice is what to do with the pengegave. Right afterwards, his money, wellbeing and future opportunities change, and his room or belongings change with them.
    5. A new event follows, for example a summer job opportunity or saving for a moped licence.
  - **Climax:** Markus understands that his own choices affect what happens next.
  - **Resolution:** The session ends after one in-game year. Before he leaves, the game shows a short teaser, such as "Next year the summer job unlocks" or "A choice you made earlier may have consequences later…". Progress is saved automatically. He wants to come back to see what happens next, what unlocks at the next age, and what his earlier choices lead to.
  - **Edge case:** The session can end abruptly, for example when the bus arrives. Nothing he has already chosen is lost.

- **UJ-2. Markus picks up his game on a school PC to find out what the moped licence costs.**
  - **Persona + context:** Four days later, Markus is bored in class. He has realised that in real life he is only a year away from being old enough for a moped licence, and he comes back to find out what it would actually cost.
  - **Entry state:** He has an account but has never used LifeMode on this PC, so he is not logged in here.
  - **Path:**
    1. He logs in with his email address and password.
    2. He gets a quick recap of where he is, with a teaser for what opens later. The teaser names the moped licence and what it costs, based on real prices.
    3. He sees his balance and the next choice he has to make.
  - **Climax:** He sees what the moped licence would cost compared with what he has.
  - **Resolution:** He carries on with the same life from where he left it, and progress keeps saving automatically. If he later chooses to take the licence, he pays for driving lessons, mandatory lessons and the licence itself.
  - **Edge cases:**
    - **Long break:** he gets the same quick recap however long he has been away, so returning works after any gap. The game is exactly as he left it.
    - **Back on his phone:** the game checks for updates when he opens it, so he sees the progress he made on the PC (FR-8).
    - **Forgotten password:** he resets it by email (FR-3).

- **UJ-3. Markus sees that the little he saved has grown, and starts to think the moped might be possible.**
  - **Persona + context:** Markus spent most of his pengegave on things that felt exciting at the time, but after a short tip from the game he put a little into savings. He has heard that a moped is expensive.
  - **Entry state:** Logged in, mid-game. Some in-game months after the first choice.
  - **Path:**
    1. He sees that his savings have grown, because they have earned interest.
    2. He is glad and curious, so he presses "Hvorfor?".
    3. The game links the increase to his earlier choice and explains saving and interest. It shows the real figure: NOK 3,000 earns NOK 84 in a year in a savings account.
    4. The game points him to other ways of earning, such as a summer job.
  - **Climax:** He understands that money he put aside earned more money without him doing anything, because of a choice he made himself.
  - **Resolution:** He starts thinking about other ways to earn more. With savings and a summer job, the moped he thought was too expensive might be possible after all.

- **UJ-4. Markus uses his first credit card like a debit card, and pays it off before it becomes a crisis.**
  - **Persona + context:** Markus, 18, has a part-time job, which is how he got his first credit card. He uses it as if it were a debit card, without thinking that it has to be paid back, with interest if he doesn't pay in time. He spends it on school lunches, on a city trip with his friends where he pays for everyone, and on fuel for his moped and for his parents' car when he borrows it. His parents paid for his driving licence as a gift. The gift is random, so only some players get it. A player without it can pay for the licence (FR-30).
  - **Entry state:** Logged in, aged 18, a couple of in-game months after getting the card. He has had a moped since he turned 16, and it costs him fuel, repairs and insurance. He chose to buy it or took a gift offer when one came up (FR-29). Whether his parents pay part of the insurance is random in the MVP.
  - **Path:**
    1. The game warns him that his card debt is much larger than his monthly wage, and that he can't pay off the whole balance before the interest-free deadline. This isn't a crisis month yet, and he decides for himself whether to act.
    2. The game shows the card's interest rate, in kroner for his own balance: what the interest costs him this month, and what the whole debt will cost if he pays only the minimum. At 22.6% a year on NOK 10,000, NOK 188 of his first NOK 350 minimum payment goes to interest. Paying only the minimum takes 51 months and costs NOK 5,508 in interest in total. He panics a little, because the longer he waits, the harder it gets.
    3. He talks to his mother. She wants to help but can't afford to, so she suggests he stops using the card until he has the repayment under control, and takes extra shifts to pay it down faster.
    4. He stops using the card and takes extra shifts, within the working-hour limits in rule 10.
    5. He sells his moped. After two years its price has dropped with age and use, and the sale doesn't cover the debt.
  - **Climax:** He realizes he has to work extra shifts and spend less for the next five months. He has less free time and does fewer social things, and the debt keeps weighing on him.
  - **Resolution:** After five months he is back on track, tired and relieved. Back on track means the card balance is paid in full, so it no longer earns interest. In the game, his stress goes up from the debt, and his free time and social life go down while he works it off. He has learned to use a credit card carefully, and to know he can afford what he spends on it.
  - **Edge cases:**
    - **He ignores the warning:** the debt keeps growing under rules 4-5. A crisis month starts if he misses the minimum two months in a row, or if the debt grows above 3× his average monthly income. If a crisis is still active when he turns 20, the game ends in a loss.
    - **Family help:** family can sometimes give or lend money, but it isn't always on offer, it's often less than the full amount, and a loan has to be paid back. The engine draws whether family can help and how much each time, and a family loan carries no interest.

- **UJ-5. Markus turns 20, sees how his life turned out, and plays again to get rich.**
  - **Persona + context:** Markus is about to turn 20 in the game. He sorted out his credit card at 18, and since then he has been careful with money. After upper secondary school he has taken a job, and he saves some of his wage every month towards a flat. He is more aware of what he spends. A full-time job from about 19.
  - **Entry state:** Logged in, in the last in-game month before his 20th birthday. His social life and stress have settled down.
  - **Path:**
    1. He turns 20, and the game ends.
    2. He sees a summary of how his life went. He has saved towards his flat, has no debt and is doing fairly well. This is the real win: he reached his goal of saving for something big, and his wellbeing is above the threshold.
    3. The summary shows the three choices that mattered most, by their effect in kroner. He opens one to see how things could have gone if he had chosen differently. Only those three can be opened.
    4. With each choice he also gets advice on how the problem could have been avoided. These are short, general, pre-written tips about the situation in the game, as decided for tips, and not personal advice.
  - **Climax:** He feels a bit stupid for ending up in so much debt at 18, but proud that he found a way out.
  - **Resolution:** He has seen how things like the moped licence and the credit card affect his money, and now he wants to find out how to get rich. He starts again from 15. He chooses a life goal again and gets a new pengegave, as decided.
  - **Second playthrough:** He chooses to save for something big or to be debt-free with a buffer, and puts everything into money. He finds that getting rich is possible, but chasing as much money as possible often costs him his social life and raises his stress. This is the hollow win: goal reached, wellbeing below the threshold. The summary includes the choice that hurt his wellbeing most, so he can see why (FR-42).

## 3. Glossary

| Term | Meaning |
|---|---|
| Playthrough | One life, from 15 to the 20th birthday: 60 in-game months, tuned to about 20-30 real choices |
| Session | One in-game year, about 10-15 minutes on a phone. A playthrough is five sessions |
| Sitting | One real-world stretch of play. A sitting can be shorter or longer than a session |
| Engine | The backend that applies Rule Set v1 and decides every financial result |
| Rule N | Rule N in Rule Set v1, in the brief's addendum |
| Active month | A month with an event, where the player makes a choice |
| Quiet month | A month with no event. It is processed by the same rules and shown as a short summary |
| Event | A pre-written situation with a few options, taken from the event library |
| Crisis month | A month the engine starts when a rule 8 trigger is met. It has 2-3 linked choices |
| Card warning | The warning shown when a card balance can't be paid in full and interest starts. It comes before any crisis |
| Pengegave | Money Markus gets at the start of the game, at 15. It is drawn at random between NOK 10,000 and NOK 30,000 |
| Life goal | One of three goals chosen at the start: save for something big, be debt-free with a buffer, or afford a big experience |
| Wellbeing | Stress, free time and social life, weighted by the life goal |
| Cause link | The record of which choice, or which rule, caused an effect |
| Echo badge | A marker showing that an earlier choice has come back |
| "Hvorfor?" | The button that explains why something changed |
| "If you had chosen differently" line | An engine-calculated line showing what another choice would have led to |
| Tip | A short, general, pre-written hint in an event, which the player can ignore. It isn't personal advice |
| Teaser | A short line at the end of a session about what comes next |
| Recap | The short summary a returning player sees before the next choice |
| Room | The player's room. It has a handful of states that change with choices and belongings |
| Endings | Real win, hollow win, goal not reached, or loss (FR-41) |
| F1-F10 | The functional test criteria in the brief |

## 4. Features

### 4.1 Account and login

**Description:** The first screen offers log in and create user, with a link for a forgotten password. An account is an email address and a password, with no username, so the email address is the only personal detail the player types in. The email address is used only for login and password recovery, and is never shown in the game or used for marketing. The password is stored only as a hash and never in the game's own data. Realizes UJ-1 and UJ-2.

**Functional Requirements:**

#### FR-1: Create user

A new player can create a user with an email address and a password they choose. Realizes UJ-1.

**Consequences (testable):**
- Creating a user asks only for an email address and a password. No real age is collected.
- The player types the email address twice, and a mismatch is caught before the user is created.
- An email address that already has a user cannot create another one.
- No email confirmation step blocks play, so the player can reach the first real choice within about 2 minutes. After creating a user, the player goes straight to choosing a life goal.

#### FR-2: Log in

A registered player can log in with their email address and password on any device and continue the same game. Realizes UJ-2.

**Consequences (testable):**
- A failed login does not reveal whether the email address or the password was wrong.
- A player can reach only their own game.

#### FR-3: Forgotten password

A player who has forgotten their password can reset it by email from the login screen. Realizes UJ-2.

**Consequences (testable):**
- The reset link can be used once and expires.
- The response is the same whether or not the email address has a user.
- The player's game is unchanged after a reset.

#### FR-4: Change password

A logged-in player can change their password from inside the game.

**Consequences (testable):**
- Changing the password requires the current password.
- The old password stops working immediately.
- The player's game is unchanged.

#### FR-5: Log out

A logged-in player can log out from inside the game, because a player needs this on any device they share.

**Consequences (testable):**
- After logging out, the game can't be reached on that device without logging in again.

#### FR-44: Delete account

A logged-in player can delete their account and game data from inside the game, after confirming.

**Consequences (testable):**
- Deleting requires the current password and can't be undone.
- After deletion, the email address and the game data are gone, and the old login no longer works.
- The same email address can create a new user afterwards.

**Notes:**
- [NOTE FOR PM: staying logged in on shared school PCs is left for the team to solve later.]
- [NOTE FOR PM: the email address is personal data about players as young as 15. The privacy check before go-live (issue #24) has to cover it.]

### 4.2 Saving and syncing

**Description:** A player's game is stored in the cloud, so they can stop at any moment and continue on another device. Realizes UJ-1 and UJ-2.

**Functional Requirements:**

#### FR-6: Save every choice

Each choice is saved to the cloud as soon as the player makes it, so an abrupt stop doesn't lose a choice, which saving only when idle wouldn't guarantee. Realizes UJ-1.

**Consequences (testable):**
- If the game closes right after a choice, that choice is still there on the next login.

#### FR-7: Save when idle

When the game has been open for a set time with no activity, it saves and updates the cloud, so a login on another device is up to date. Realizes UJ-2.

**Consequences (testable):**
- After the idle time has passed, a login on another device shows the same progress.
- The idle time is configuration.

#### FR-8: Check for updates on opening

When the player opens or returns to the game on a device, it checks the cloud for newer progress before showing the next choice. Realizes UJ-2.

**Consequences (testable):**
- Progress made on the PC appears on the phone when the game is opened there.
- A device showing old progress cannot overwrite a newer choice.
- With no connection, for example on the bus, the game says so and doesn't accept new choices until it is back. Saved choices aren't affected.

### 4.3 Starting a life

**Description:** After creating a user, the player chooses a life goal, then an avatar, and then gets a pengegave. The first real choice is what to do with it. Realizes UJ-1.

**Functional Requirements:**

#### FR-9: Choose a life goal

The player chooses one of three life goals: save for something big, be debt-free with a buffer, or afford a big experience. Realizes UJ-1 and UJ-5.

**Consequences (testable):**
- The goal is chosen before the avatar.
- Each goal has a target the engine checks at age 20. The targets are configuration, and each one can be reached from the lowest pengegave of NOK 10,000.
- The goal can't be changed during a playthrough, only when starting again.

#### FR-10: Create an avatar

The player creates an avatar for their life in the game. Realizes UJ-1.

**Consequences (testable):**
- The player picks from a small set of preset looks. Nothing is typed in, so the avatar has no free-text name.

#### FR-11: Get a pengegave and make the first choice

The game starts at age 15 with a pengegave drawn at random between NOK 10,000 and NOK 30,000. The first real choice is what to do with it. Realizes UJ-1.

**Consequences (testable):**
- The amount is drawn once per playthrough and stored, so it stays the same when the player resumes. Starting again draws a new amount.
- Engine tests can set a fixed amount.
- A new player reaches the first real choice within about 2 minutes of opening the game. This is checked in playtests.

### 4.4 Months, sessions and events

**Description:** A playthrough is 60 in-game months, from 15 to the 20th birthday. Each session covers one in-game year, and the player never has to wait in real time. Realizes UJ-1, UJ-2 and UJ-3.

**Functional Requirements:**

#### FR-12: Process each month in a fixed order

The engine processes every month in the order set by rule 1: income, then tax, fixed costs, loan instalments and interest on debt, interest on savings, and last the month's event and the player's choice. All amounts are in whole kroner (rule 2). Realizes UJ-3.

**Consequences (testable):**
- The same starting state, random draws and choices always give the same result.
- Worked examples 1-6 pass as unit tests, including F1-F3, F7 and F8.

#### FR-13: Play an active month

In a month with an event, the player sees the situation together with their balance, savings, debt and fixed costs, and picks one of a few options. Afterwards the game shows what changed in kroner and wellbeing, and why. Realizes UJ-1 and UJ-3.

**Consequences (testable):**
- Every option has a wellbeing effect.
- Tapping an option twice applies it only once.

#### FR-14: Summarize a quiet month

A month with no event is processed by the same rules and shown only as a short summary. Realizes UJ-1.

**Consequences (testable):**
- Income, costs and interest in a quiet month follow the same rules as in an active month.

#### FR-15: End a session after one in-game year

A session ends after one in-game year with a teaser about what comes next, such as "Next year the summer job unlocks". Realizes UJ-1.

**Consequences (testable):**
- Nothing locks the player out in real time. The player can carry straight on into the next year.

#### FR-16: Recap on return

A player who comes back sees a short recap of where they are, with a teaser for what opens later, and then their balance and the next choice. Realizes UJ-2.

**Consequences (testable):**
- The recap is the same however long the break was.
- The game is exactly as the player left it. No interest or events run during the break.

#### FR-17: Event library

The game is driven by a library of pre-written events. Realizes UJ-1 to UJ-5.

**Consequences (testable):**
- **Size:** at least 30 events, with a target of 60-80, plus about 10 crises. Roughly 55% come before age 18 and 45% after.
- **Schema:** every event follows a fixed schema: mechanism, age, flags, boomerang pair, teaching point, LK20 code, source, and a wellbeing effect for each choice. An automated check rejects an event that breaks the schema.
- **No AI needed:** the whole game can be played from start to finish with zero AI calls (F6).

**Notes:**
- Candidate events from the survey are small purchases that add up, trend buys, collectibles and in-game purchases, and subscriptions with a binding period. Family appears as an actor in events.

#### FR-18: Unlock options by age

New options open at set in-game ages, such as the summer job, the moped licence and credit. Realizes UJ-1 and UJ-4.

**Consequences (testable):**
- Consumer loans and credit cards are offered only from the 18th birthday (rule 6).
- In the MVP, only age unlocks options, not progress towards the goal.

#### FR-19: Tips in events

Some events carry a short, general, pre-written tip, which the player is free to ignore. Realizes UJ-3.

**Consequences (testable):**
- A tip is about the situation in the game and is never personal advice.
- Ignoring a tip has no effect in the game.

### 4.5 Money

**Description:** The game has five money mechanisms: wages, saving, fixed costs, loans and credit cards, and unexpected expenses. It also has help from family. All of them use real Norwegian 2026 figures, held fixed for the whole game. The rules, parameters and sources are in Rule Set v1. Every figure is stored as configuration, with its source and date. Realizes UJ-1, UJ-3, UJ-4 and UJ-5.

**Functional Requirements:**

#### FR-20: Wages and working hours

The player can earn hourly wages from part-time and summer jobs, at the Virke/HK tariff rate for their age, and later from a full-time job. Realizes UJ-1, UJ-4 and UJ-5.

**Consequences (testable):**
- A summer job at 16, 120 hours at NOK 139.40, pays NOK 16,728 with no tax (worked example 1, F7).
- The engine never allows more hours than the limits in rule 10, including extra shifts.
- More hours worked means less free time.
- A full-time job becomes available after upper secondary school, from about 19.

#### FR-21: Tax

Tax is calculated from the year's total wage income at 2026 rates (rule 3).

**Consequences (testable):**
- An 18-year-old earning NOK 110,000 in a calendar year pays NOK 2,588, all of it trygdeavgift (worked example 5, F8).
- Tax uses the character's age in the game, with the simulated year fixed at 2026 rates.

#### FR-22: Saving and BSU

The player can save in a savings account at 2.87% or in BSU at 5.61%, and interest is added under rule 2. The BSU deduction follows rule 9. Realizes UJ-3.

**Consequences (testable):**
- NOK 10,000 in savings for 12 months gives NOK 10,289 (worked example 2, F2).
- When the player has no tax, the game says plainly that the BSU deduction is NOK 0, and shows that BSU still pays off through the higher interest (worked example 6).
- The game shows the real interest even when it's small. For example, NOK 3,000 earns NOK 84 in a year.

#### FR-23: Fixed costs

Mobile and transport costs are deducted every month. Transport includes fuel and insurance for the moped and fuel for the car when the player borrows the parents' car. Realizes UJ-4.

**Consequences (testable):**
- Fixed costs are deducted at their place in the rule 1 order.
- Whether the parents pay part of the moped insurance is drawn at random. This is on the cut list.

#### FR-24: Unexpected expenses

Unexpected expenses come up at random, such as a broken phone screen or a moped repair. Realizes UJ-4.

**Consequences (testable):**
- An unexpected expense is stored with a system cause, so "Hvorfor?" explains it from the rules.

#### FR-25: Consumer loans

From age 18, the player can take a consumer loan, repaid as an annuity at a fixed 15% (rule 4).

**Consequences (testable):**
- NOK 20,000 over 12 months gives monthly payments of NOK 1,805, a final payment of NOK 1,808 and NOK 21,663 in total (worked example 3, F1).

#### FR-26: Credit card

From age 18, a player with a wage can get a credit card, under rule 5. Realizes UJ-4.

**Consequences (testable):**
- NOK 3,200 paid at the minimum is paid off after 13 months, NOK 3,606 in total (worked example 4, F3).
- The game shows, in kroner, this month's interest and the total cost of paying only the minimum, for the player's own balance.
- The player can choose to stop using the card.
- A card needs a wage income, and the first limit is NOK 5,000-10,000, set as configuration.

#### FR-27: Help from family

In some events and crisis months, family can give or lend money. Talking to family can also bring advice instead of money. Realizes UJ-4.

**Consequences (testable):**
- Help isn't always on offer, and it often covers only part of the amount. The engine draws whether family can help, and how much, each time.
- A family loan is paid back at 0% interest. It is paid back in monthly instalments set by the event.
- A family loan doesn't count towards the crisis trigger of debt above 3× income (FR-32). Otherwise a teenager with no income would go into crisis from any loan.
- Family can sometimes give cash. Family gifts stay in the MVP.

### 4.6 Moped and driving licences

**Description:** At 16 the player can get the moped licence and a moped, and by 18 some players get a car licence from their parents. These add costs, choices and something to sell. Realizes UJ-2 and UJ-4.

**Functional Requirements:**

#### FR-28: Moped licence

From age 16, the player can choose to take the moped licence. They pay for driving lessons, the mandatory lessons and the licence itself, at real prices. Realizes UJ-2.

**Consequences (testable):**
- The licence is a payment only. There is no exam and no driving.
- The recap's teaser names what the licence costs.
- Every price has a source and a date (#29).

#### FR-29: Own a moped

From age 16, the player can own a moped. They choose whether to buy one, and now and then a random event offers one as a gift. This way, saving up pays off as in UJ-3. Realizes UJ-3 and UJ-4.

**Consequences (testable):**
- **Running costs:** fuel and insurance are transport costs (FR-23), and repairs come as unexpected expenses (FR-24).
- **Resale value:** it drops by a fixed share for each year the player has owned the moped, starting from real used prices. Tracking actual use comes later.
- **Selling:** the player can sell the moped at its current resale value. It then disappears from the room.
- Owning a moped requires the moped licence.

#### FR-30: Car licence

By age 18, some players get a car licence as a gift from their parents. The engine draws who gets it. A player without the gift can pay for the licence at a real price. With a licence, the player pays for fuel when borrowing the parents' car. Realizes UJ-4.

**Consequences (testable):**
- The gift costs the player nothing. Car fuel is a transport cost (FR-23).
- The gift doesn't depend on tobacco or alcohol, because the MVP has no such choices.
- Every price has a source and a date (#29).

### 4.7 Warnings and crises

**Description:** The game warns the player before money trouble turns into a crisis, and the player decides whether to act. Only the engine starts a crisis month. Realizes UJ-4.

**Functional Requirements:**

#### FR-31: Card warning

When a card balance can't be paid in full and interest starts, the game warns the player. It shows this month's interest and what the debt will cost if the player pays only the minimum. The player then chooses whether to act, for example by talking to family, stopping the card, taking extra shifts or selling something. Realizes UJ-4.

**Consequences (testable):**
- The warning doesn't start a crisis month on its own.
- The warning is shown each time interest starts again after the balance has been paid in full.

#### FR-32: Crisis month

The engine starts a crisis month when any rule 8 trigger is true at the end of a month:
- the current account is below NOK 0
- the card minimum has been missed two months in a row
- total debt is above 3× the average monthly income over the last three months

A crisis month has 2-3 linked choices with real-world actions, such as selling something, taking extra shifts, asking for a payment plan, asking family or ignoring it. The engine calculates the effect of each one. Realizes UJ-4.

**Consequences (testable):**
- **Never skipped:** a met trigger always starts a crisis month (F4, one test per trigger).
- **Never fatal before 20:** a crisis doesn't end the game. Ignored debt keeps growing under rules 4-5 and triggers new crisis months.
- **Below zero:** going below zero only starts a crisis month. It isn't a loss.

### 4.8 Wellbeing and visible consequences

**Description:** The player sees what their choices do to their life, not only their money. Realizes UJ-1, UJ-4 and UJ-5.

**Functional Requirements:**

#### FR-33: Wellbeing

Wellbeing has three parts, weighted by the life goal:
- **Stress** rises with debt and crisis months.
- **Free time** falls with hours worked.
- **Social life** follows the choices made in events.

Realizes UJ-4 and UJ-5.

**Consequences (testable):**
- Every event choice has a wellbeing effect.
- In UJ-4, extra shifts lower free time and social life, debt raises stress, and paying the debt off lowers it again.
- The weights and the threshold are configuration.

#### FR-34: Room states

The player has one room with a handful of states that change with choices and belongings. Realizes UJ-1 and UJ-4.

**Consequences (testable):**
- The room changes right after a choice that affects it. For example, the moped appears when the player gets it and disappears when it's sold.

#### FR-35: Visible future opportunities

After a choice, the game shows what it opened or closed. Realizes UJ-1.

**Consequences (testable):**
- What is shown comes from the event's flags.

### 4.9 Explaining consequences

**Description:** Every change can be traced to a cause, so the player can always find out why something happened. Realizes UJ-3 and UJ-5.

**Functional Requirements:**

#### FR-36: Cause links

Every effect in the engine stores the choice that caused it. An effect with no choice behind it, such as wages in a quiet month or a random expense, is stored with a system cause. Realizes UJ-3.

**Consequences (testable):**
- Every cause link points to a choice that exists in the playthrough, or to a rule (F10). F10 is read as "a choice or a system cause".

#### FR-37: Echo badges

When an earlier choice comes back, an echo badge marks it and links to that choice. Realizes UJ-3.

**Consequences (testable):**
- An echo badge is shown only for effects that carry a cause link to an earlier choice.

#### FR-38: "Hvorfor?"

The player can press "Hvorfor?" on a change to see why it happened. The explanation links the change to the choice behind it, or explains it from the rule. Realizes UJ-3.

**Consequences (testable):**
- An effect with a system cause is explained from the rules.
- The BSU comparison ("in BSU this would have been NOK …") is optional and is cut first.

#### FR-39: "If you had chosen differently"

The engine calculates what another choice would have led to. It does so only where it can calculate the result reliably, starting with interest and instalments, and never with AI. Realizes UJ-5.

**Consequences (testable):**
- The lines on the ending screen, for the three choices that mattered most, stay in the MVP.
- The lines during play are the first thing cut if time runs short.

#### FR-40: Disclosed simplifications

Where the game simplifies reality, it says so (D1-D6 in the brief's addendum). The text is shown the first time the mechanism appears, behind an info icon or under "Hvorfor?". All the texts are also collected on one page, "Om tallene".

**Consequences (testable):**
- Every mechanism with a simplification shows its text the first time it appears.

### 4.10 Ending and replay

**Description:** At 20, the game ends with one of four endings and a summary of the life. The player can start again from 15. Realizes UJ-5.

**Functional Requirements:**

#### FR-41: Four endings

At the 20th birthday, the engine checks the endings in this order:
1. **Loss:** a rule 8 crisis condition is active.
2. **Real win:** the goal is reached and wellbeing is above the threshold.
3. **Hollow win:** the goal is reached, but wellbeing is below the threshold.
4. **Goal not reached:** neither a win nor a loss. The player gets advice on modest savings goals and what they bring.

Realizes UJ-5.

**Consequences (testable):**
- Every end state gives exactly one valid ending screen (F9, one test per end state).
- Every ending is calculated from measurable state and works with no AI.

#### FR-42: Ending summary

The ending shows how the life went and the three choices that mattered most, ranked by their effect in kroner. The player can open each of them to see the "if you had chosen differently" line and a tip on how the problem could have been avoided. Realizes UJ-5.

**Consequences (testable):**
- Only these three choices can be opened.
- On a hollow win, at least one of the three is the choice that hurt wellbeing most, even if it wouldn't rank by kroner.
- The tips are general and pre-written (FR-19).

#### FR-43: Play again

The player can start a new life from age 15. Realizes UJ-5.

**Consequences (testable):**
- **A fresh start:** the player chooses a life goal again and gets a newly drawn pengegave. Nothing carries over from the last playthrough.
- **No crossroads:** a replay always starts at 15, never from a point partway through.
- **Different choices, different story:** two playthroughs with different choices give different stories.

## 5. Non-Functional Requirements

#### NFR-1: Every screen size

The game is designed mobile-first, and its layout adapts to phone, tablet, laptop and desktop. It has:
- no horizontal scrolling
- touch-friendly controls
- no core function that works only on hover
- text that is readable on a small screen

The main flow works on all four device classes.

#### NFR-2: Accessibility

The game meets WCAG 2.x level AA. This includes contrast, keyboard navigation, alt text, form labels and clear error messages.

#### NFR-3: Privacy and data minimization

The email address and the password are the only real personal data. The game collects no real age, takes no free text beyond the email address, and simulates the whole economy.

**How the data is handled:**
- Supabase Auth stores the password, only as a hash. It is never kept in game data or logs.
- A player can reach only their own data.
- A player can delete their account and game data (FR-44).

**Playtests:** only 18-20-year-olds take part. Results are recorded anonymously and kept apart from the testers' accounts.

The privacy check before go-live is still open (#24).

#### NFR-4: Correct, explainable figures

The backend engine decides every financial result and all critical game state, and the frontend never calculates them.

**Figures:**
- They follow Rule Set v1, use real Norwegian 2026 values and are held fixed for the game (D6).
- Every figure is stored as configuration with its source and date, never hard-coded.
- The worked examples are the test answer key.

The disclosed simplifications are a requirement, as a product choice.

#### NFR-5: Zero ongoing cost

Everything the game uses runs at no ongoing cost, including the email for password reset (#30).

#### NFR-6: Runs from the README

A sensor can run the full application on a clean machine with Docker, following only the README, in about 15-20 minutes. This must work without the team's cloud account or keys, so Supabase is self-hosted. Password reset works locally, or the README names a local replacement (#30). The README also provides test users.

#### NFR-7: Robust against wrong input

The backend validates all player input. The game rejects:
- invalid financial values
- choices that weren't offered
- attempts to get around the rules

A repeated request doesn't apply an action twice.

#### NFR-8: Tone and content

Player-facing text is in Norwegian, in plain language a 15-year-old understands.
- **Tips:** they sound like tips, not lectures.
- **Visual style:** grown-up, not childish.
- **Credit:** the credit mechanics get more explanation than the rest, because most players have never used credit.
- **Tobacco and alcohol:** the MVP has no tobacco or alcohol choices, and no content markets them.

#### NFR-9: Automated tests

The engine tests, meaning the worked examples and the F-criteria, run from the README and in GitHub Actions on every pull request.

## 6. Non-Goals

Version one of LifeMode won't:
- use real money, real bank connections or real financial data
- give personal financial advice (tips are general and about the game)
- use AI anywhere in the MVP
- let the player type free text beyond the email address
- lock the player out in real time, or add interest or events during a break
- be a classroom or teacher-led tool

## 7. MVP Scope

### 7.1 In Scope

- Account, login, password recovery by email and account deletion (4.1)
- Saving to the cloud and syncing between devices (4.2)
- A start with a life goal, an avatar and a pengegave (4.3)
- Months, sessions of one in-game year, teasers, recaps, the event library, age unlocks and tips (4.4)
- Five money mechanisms plus help from family (4.5)
- The moped licence, owning a moped, and the car licence as a gift or paid for (4.6)
- The card warning and crisis months (4.7)
- Wellbeing, room states and visible future opportunities (4.8)
- Cause links, echo badges, "Hvorfor?", "if you had chosen differently" lines and disclosed simplifications (4.9)
- Four endings, the ending summary and playing again from 15 (4.10)

**If time runs short,** content is cut before the core, in this order:
1. "If you had chosen differently" lines during play, including the BSU comparison
2. The parents' share of the moped insurance
3. Events, down to the minimum of 30

These always stay: the engine, wellbeing, the endings, cause links, "Hvorfor?", the card warning, the moped and login.

### 7.2 Out of Scope for MVP

| Item | Status |
|---|---|
| AI-generated events and AI checks | Second stage, after the base works |
| Avatar and home that develop over time | Later |
| Unlocks based on progress towards the goal, and new areas | Later |
| Funds and investing | Candidate for later |
| Moving out and rent | Later, the first new life area |
| Education and student loans | Later. Must show that a student loan while studying isn't the same as card debt |
| Moped value based on actual use | Later |
| Comparing one playthrough with another | Later |
| Negotiation, a parent view, school and private modes | Later |
| Replay from a crossroads | Out. It needs earlier game states to be stored |
| Interest or events during a long break | Left out |
| Staying logged in on shared school PCs | The team will solve it later (#31) |
| Tobacco and alcohol choices | Left out for now. The basis, if the team returns to it, is `research/domain-norwegian-tobacco-alcohol-advertising-la-2026-11-04/research.md` |

## 8. Success Metrics

### 8.1 Playtest

There are 10-20 playtesters before the December delivery, all 18-20-year-olds. These are starting values, which can change once real data exists.

| Signal | Metric | Target |
|---|---|---|
| Understanding | Can explain how an earlier decision affected a later outcome | 70% or more |
| Understanding | 5-question money quiz, before and after | Higher after |
| Behaviour | Completes the full playthrough from 15 to 20 | 70% or more |
| Behaviour | Comes back voluntarily for another session or a replay within a week | 50% or more |
| Experience | "It felt more like a game than schoolwork" (1-5) | Median 4 or higher |
| Experience | Describes two playthroughs with different choices as different stories | Most players |
| Pace | Reaches the first real choice | Within about 2 minutes |
| Pace | One session, one in-game year | 10-15 minutes on a phone |
| Mission | A parent or teacher who sees the game wants to try it | At least one |

Completion is measured across several sittings during the test period, and the quiz before the first sitting and after the last one.

### 8.2 Counter-metrics

- **Completion rises but explaining falls:** players are tapping through without reading.
- **The return rate rises but the quiz doesn't:** the teaser hooks them, but they don't learn.
- **The quiz rises but "more like a game" falls below a median of 4:** the game has turned into a lesson.

### 8.3 Functional criteria

F1-F10 from the brief apply, with two changes:
- F5, the fallback when the AI fails, moves to the AI stage, because the MVP has no AI.
- F10 is read as "an earlier choice or a system cause" (FR-36).

The new rules from this PRD get worked examples and unit tests in the same way. These cover the card warning, family loans and the moped's resale value.

## 9. Open Questions

| # | Question | Owner | Blocks |
|---|---|---|---|
| OQ-3 | Prices are in the brief addendum's parameters (research `prices-moped-and-licences-2026-11-05`). Still missing: moped insurance from a primary source, moped repairs, and a better used-moped price (#29) | Team | Writing those events |
| OQ-4 | How password reset email can work at zero cost and in the sensor's local run (#30) | Architecture | No |
| OQ-5 | Staying logged in on shared school PCs (#31) | Team, later | No |
| OQ-6 | The privacy check before go-live, including email addresses of players as young as 15 (#24) | Team | Go-live |
| OQ-7 | The brief and the architecture still describe AI as part of version one (#32) | Team | No |
| OQ-8 | Tuning values: goal targets, wellbeing weights and threshold, idle time, the first card limit, how often family helps, and how fast the moped loses value | Team, when tuning | No |
| OQ-9 | What the avatar contains, and how the player chooses working hours | UX | No |

**Resolved on 2026-11-05:**
- **OQ-1:** no tobacco or alcohol choices (#34), and the car licence gift is random, with the option to pay (FR-30).
- **OQ-2:** the card minimum is 3.5%, min NOK 300 (#35).
- **OQ-10:** the player can delete their account in the game (FR-44, #36).

## 10. Assumptions Index

All of these were confirmed on 2026-11-05, so the entries are no longer tagged in the text. A-26 has been checked against part 1 of the sensor guide, which only mentions AI in the development process; other course requirements are still to be checked (#39).

| # | Assumption | Where |
|---|---|---|
| A-1 | The goal's target is an amount the game sets, reachable by 20, such as a start on a flat deposit | UJ-1, FR-9 |
| A-2 | UJ-3 takes place some in-game months after the first choice | UJ-3 |
| A-3 | A full-time job is available from about 19 | UJ-5, FR-20 |
| A-4 | In the ending, the advice consists of general, pre-written tips | UJ-5, FR-42 |
| A-5 | A replay means choosing a goal again and drawing a new pengegave | UJ-5, FR-43 |
| A-6 | The email address is used only for login and recovery, and is never shown or used for marketing | 4.1 |
| A-7 | A reset link works once and expires | FR-3 |
| A-8 | Changing the password requires the current one | FR-4 |
| A-9 | The player can log out | FR-5 |
| A-10 | Every choice is saved as soon as it's made | FR-6 |
| A-11 | A device showing older progress can't overwrite a newer choice | FR-8 |
| A-12 | With no connection, the game accepts no new choices | FR-8 |
| A-13 | The goal can't be changed during a playthrough | FR-9 |
| A-14 | The avatar is picked from preset looks, with no free text | FR-10 |
| A-15 | The player can carry straight on into the next year | FR-15 |
| A-16 | An automated check enforces the event schema | FR-17 |
| A-17 | Tax uses the character's age in the game and fixed 2026 rates | FR-21 |
| A-18 | A card needs a wage income, and the first limit is NOK 5,000-10,000 | FR-26 |
| A-19 | A family loan is repaid in monthly instalments | FR-27 |
| A-20 | Owning a moped requires the moped licence | FR-29 |
| A-21 | The card warning comes back each time interest starts again | FR-31 |
| A-22 | F10 accepts a system cause | FR-36, 8.3 |
| A-23 | The disclosed simplifications are a requirement | NFR-4 |
| A-24 | GitHub Actions runs the tests on every pull request | NFR-9 |
| A-25 | Completion and the quiz are measured across sittings | 8.1 |
| A-26 | F5 moves to the AI stage | 8.3 |
| A-27 | The new rules get worked examples and unit tests | 8.3 |
| A-28 | Deleting an account requires the current password and can't be undone | FR-44 |
