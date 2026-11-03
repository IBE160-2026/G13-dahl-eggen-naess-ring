---
title: LifeMode PRD addendum
created: 2026-11-03
updated: 2026-11-03
---

# Addendum: LifeMode PRD

## Competitor playtests

Team verdict as reported on 2026-11-03: everyone on the team has tried both products. This replaces the note in `research/playtest-competitors-2026-10-31/notes.md` that only one member had played Koll på cashen and that PersonalFinanceLab had not been tried.

| Product | Team verdict | What LifeMode does instead |
|---|---|---|
| Koll på cashen | Not very rewarding, heavy and slow | More entertaining and smoother to play |
| PersonalFinanceLab | Professional, but not made for the Norwegian market, geared towards a teacher-led experience, and it costs money | Made for Norway first and foremost |

## Progression and visible consequences: MVP scope

Decided on 2026-11-03 from UJ-1. These features come from the team's journey and weren't in the brief. They are the team's first concrete answer to "more entertaining". Scoped small because delivery is about five weeks away.

| Feature | Decision | Why |
|---|---|---|
| End-of-session teaser | In | Cheap, and supports the target of 50% coming back |
| Room and belongings that change with choices | In, small: one room with a handful of states | Makes consequences visible without much art |
| Developing the avatar and home | Later | Beyond the room states, it needs a lot of art and content |
| Visible future opportunities | In, simple: show what a choice opened or closed | Can use the flags already in the event schema |
| Unlocks | In, by in-game age only | Progress-based unlocks can come later |
| New areas to unlock | Later | A whole new layer of content |

**Sessions:** one session is one in-game year, and nothing locks the player out in real time. Five years at 20-30 choices gives about 4-6 choices a year, which fits a 10-15 minute session. Waiting in real time would work against the target of 70% finishing the game.

**Moped licence:** when the player chooses to take it, they pay for driving lessons, mandatory lessons and the licence itself, at real prices from sources such as Statens vegvesen, driving schools and SSB. The recap's teaser names the cost, so no new screen is needed. [ASSUMPTION: payment only, with no exam or driving mechanics, and buying or running a moped isn't included. Other driving licences stay a later step.]

## Login with email: consequences for the build

Decided on 2026-11-03. This replaces the earlier decision on username, no email and no reset. Questions for architecture:

- **Sending email:** password reset needs a way to send email within the hard constraint of zero ongoing cost.
- **Examiner's local run:** the app has to run from Docker without the team's cloud account or keys, so reset email must either work there or have a stated local replacement.
- **Internal address plan:** the plan to build a fake address from the username (`@lifemode.invalid`) is no longer needed.
- **Playtests:** playtesters aged 18-20 will now give a real email address, while the brief says no contact details are stored with results, so the two have to be kept apart.

Updated to match on 2026-11-03: brief (Scope In #9, Constraints), brief addendum (Privacy, Login secret), architecture (Database and Data Model, Authentication and authorization) and issue #24.

## Interest after a long break: left out of the MVP

The team suggested positive or negative interest after an extremely long break. Decided on 2026-11-03 to leave it out, and the game stays exactly as the player left it. Credit only starts at 18, so a younger player would mostly get free money for staying away, an older player in debt would be punished for coming back, and the game's clock runs in game months with fixed rates.

## Saving and interest in UJ-3

Decided on 2026-11-03.

**Funds stay out of version one.** The team's narrative said funds or savings, but investing was decided out on 2026-10-31, and funds need returns that go up and down, which the engine doesn't have. Many survey respondents asked about funds, so it's a candidate for later.

**The game shows the real interest, even when it's small.** First-year interest under rules 1-2:

| Saved | Savings account (2.87%) | BSU (5.61%) |
|---|---|---|
| NOK 2,000 | NOK 60 | NOK 116 |
| NOK 3,000 | NOK 84 | NOK 172 |
| NOK 5,000 | NOK 144 | NOK 287 |

Interest alone won't pay for a moped, so the moment rests on two things: the surprise that money earned money without the player doing anything, and a pointer to other income. A summer job at 16 pays NOK 16,728 (worked example 1).

**BSU comparison:** "Hvorfor?" can also show what the same money would earn in BSU. This counts as an "if you had chosen differently" line, which is first on the cut list, and the moment works without it.

## Tips from the game

Decided on 2026-11-03. Some events carry a short, general, pre-written tip that the player is free to ignore. A tip is about the situation in the game and isn't personal advice, which the brief rules out. It should sound like a tip rather than a lecture.
