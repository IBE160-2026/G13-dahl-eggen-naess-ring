---
title: LifeMode PRD
status: draft
created: 2026-10-22
updated: 2026-11-03
---

# PRD: LifeMode

## 2. Target User

### 2.3 Key User Journeys

- **UJ-1. Markus is told to try LifeMode before he spends his pengegave.**
  - **Persona + context:** Markus, 15, has just been told by his mother that he can't spend his whole pengegave on Monster and Fortnite. She suggests LifeMode, so he can see that saving a little now can pay off later, and that being careless with money can have serious consequences. He opens it slightly irritated, just to test it.
  - **Entry state:** No account, on his phone, possibly on the bus. His mother has no account and no view of his game.
  - **Path:** Markus reaches his first real choice within about 2 minutes.
    1. The first screen offers log in or create a new user. Markus creates one with an email address and password.
    2. He chooses his life goal.
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
  - **Entry state:** Logged in, mid-game. [ASSUMPTION: some in-game months after the first choice.]
  - **Path:**
    1. He sees that his savings have grown, because they have earned interest.
    2. He is glad and curious, so he presses "Hvorfor?".
    3. The game links the increase to his earlier choice and explains saving and interest. It shows the real figure: NOK 3,000 earns NOK 84 in a year in a savings account.
    4. The game points him to other ways of earning, such as a summer job.
  - **Climax:** He understands that money he put aside earned more money without him doing anything, because of a choice he made himself.
  - **Resolution:** He starts thinking about other ways to earn more. With savings and a summer job, the moped he thought was too expensive might be possible after all.

## 4. Features

### 4.1 Account and login

**Description:** The first screen offers log in and create user, with a link for a forgotten password. An account is an email address and a password, with no username, so the email address is the only personal detail the player types in. [ASSUMPTION: the email address is used only for login and password recovery, and is never shown in the game or used for marketing.] The password is stored only as a hash and never in the game's own data. Realizes UJ-1 and UJ-2.

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
- [ASSUMPTION: the reset link can be used once and expires.]
- The response is the same whether or not the email address has a user.
- The player's game is unchanged after a reset.

#### FR-4: Change password

A logged-in player can change their password from inside the game.

**Consequences (testable):**
- [ASSUMPTION: changing the password requires the current password.]
- The old password stops working immediately.
- The player's game is unchanged.

#### FR-5: Log out

[ASSUMPTION: not on the team's list, but a player needs it on any device they share.] A logged-in player can log out from inside the game.

**Consequences (testable):**
- After logging out, the game can't be reached on that device without logging in again.

**Notes:**
- [NOTE FOR PM: staying logged in on shared school PCs is left for the team to solve later.]
- [NOTE FOR PM: the email address is personal data about players as young as 15. The privacy check before go-live (issue #24) has to cover it.]

### 4.2 Saving and syncing

**Description:** A player's game is stored in the cloud, so they can stop at any moment and continue on another device. Realizes UJ-1 and UJ-2.

**Functional Requirements:**

#### FR-6: Save every choice

[ASSUMPTION: added so an abrupt stop doesn't lose a choice, which saving only when idle wouldn't guarantee.] Each choice is saved to the cloud as soon as the player makes it. Realizes UJ-1.

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
- [ASSUMPTION: a device showing old progress cannot overwrite a newer choice.]
- [ASSUMPTION: with no connection, for example on the bus, the game says so and doesn't accept new choices until it is back. Saved choices aren't affected.]
