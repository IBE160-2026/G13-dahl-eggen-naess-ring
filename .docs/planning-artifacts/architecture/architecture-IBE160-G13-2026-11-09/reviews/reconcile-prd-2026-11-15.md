---
title: Second reconcile — ARCHITECTURE-SPINE.md against the PRD and its addendum
created: 2026-11-15
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-15)
inputs:
  - ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (final, working copy of 2026-11-15)
  - ../../../prds/prd-IBE160-G13-2026-10-22/addendum.md (working copy of 2026-11-15)
  - ../../../briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md (Rule Set v1, rules 1, 4, 5, 8, 16 and worked examples 7 and 8)
scope: backend, database, content pipeline, infra and ops up to the HTTP API boundary
method: full read of all three documents in one pass, after the reviewer-gate fixes of 2026-11-14
---

# Second reconcile: spine vs PRD + addendum

Asked for by Dahl on 2026-11-15: everything must match before the spine is set final. The first reconcile (`reconcile-prd.md`, 2026-11-13) ran before the reviewer gate. This one checks the spine as it stood after the gate fixes, against every FR, NFR, open question and addendum detail section.

**Count:** 1 high · 6 medium · 13 low (20 findings). 14 are fixed in the spine. 6 needed a change in the PRD, its addendum or Rule Set v1; Dahl decided the two open ones and approved the edits on 2026-11-15. All 20 are closed.

**Result for the rest:** every FR-1 to FR-58 and NFR-3 to NFR-11 has a home in the spine's capability map, and nothing else in the spine contradicts the PRD. NFR-1 and NFR-2 are the frontend team's (Deferred).

## High

### H1. The FR-45 payment-order table contradicts rule 5 on the card bill

- **Source:** prd.md FR-45 payment-order table, row "Card bill, family-loan instalments: current account only, never below NOK 0". Rule 5 (brief addendum): the engine pays the chosen amount "but never more than the current account and savings hold". Worked example 7 and FR-31's test: bill NOK 6,000, "the account and savings hold NOK 4,000", the engine pays NOK 4,000. Addendum R1: "his savings would then pay the card bill under rule 5".
- **What doesn't match:** AD-9 makes `pay()` implement the FR-45 table. Built from the table, the card bill never touches savings, and worked example 7 fails whenever part of the NOK 4,000 is in savings. The table was added during the architecture run on 2026-11-13 with the note "Dahl to check the table against Rule Set v1"; that check hadn't happened.
- **Also open in the same table:**
  - Family-loan instalments: Rule Set v1 doesn't say whether savings pay them. FR-45's first bullet (savings pay the rest of any payment) and D18 say yes; the table says no.
  - Row 2 puts card-payable costs and spending together and says "the rest from the current account". For a cost, the rest is always charged (row 3); for spending it isn't.
  - Extra card payments and early payoff (money actions) have no row.
- **Decision (Dahl, 2026-11-15):** savings cover too. Card bill, family-loan instalments, extra card payments and early payoff are paid from the current account, then savings, never below NOK 0. Only spending never touches savings.
- **Fix (applied):** PRD FR-45 table (card-bill row corrected, money-action row added, card-payable row clarified), FR-27, and Rule Set v1 rule 4 with worked example 8. The spine needs no change: AD-9 keeps pointing to the table.

## Medium

### M1. `receive()` applied the crisis-month money order to all income

- **Source:** rule 8 and FR-32b: "money from a crisis choice or a money action [in a crisis month] goes first to a negative current account, then to overdue card minimums". Rule 5: the card is paid at the debt step.
- **What didn't match:** AD-9 said `receive()` "implements FR-32b's money-in order", with no limit. A builder would send every wage through it, so a wage would pay overdue card minimums at the income step, before tax and costs.
- **Fix (applied, AD-9):** `receive()` puts money in the current account, where it covers a negative balance first. Only crisis-month money from a crisis choice or a money action then pays overdue minimums. Wages never pay the card outside the debt step.

### M2. A limited reset request could answer differently from a sent one

- **Source:** FR-3: "The screen shows the same message whether an email was sent, held back by a limit, or the address has no user."
- **What didn't match:** AD-10 covered the unknown address, but not the limit. AD-13 lists `429 rate_limited`, so a reset held back by the per-address limit could return 429 and reveal that the address has a user.
- **Fix (applied, AD-10 and the AD-13 table):** a limited reset request gets the same response as a sent one; only sign-up and login answer 429.

### M3. FR-43 says an ended life "is deleted"; the spine keeps the row until the next start

- **Source:** FR-43 "Starting over before 20: … The ended life can't be resumed and is deleted."
- **What doesn't match:** AD-4 keeps the row with `status = ended` and deletes it only when a new life starts, so that a repeated "end life" request still finds its `request_id` (reviewer gate, 2026-11-13). The player sees the same thing either way, but the data lives until the next start or account deletion.
- **Decision (Dahl, 2026-11-15):** the PRD wording changes; the spine stands.
- **Fix (applied):** FR-43 says the ended life is deleted when the new life starts or the account is deleted. NFR-3 says "the last finished or ended one".

### M4. FR-50 still says a new user "gets that code"

- **Source:** FR-50 "Linking the code: … A new user whose address is on the list gets that code."
- **What doesn't match:** decided by Dahl on 2026-11-14: the code is resolved once, at export, by joining the normalized address to the list; records hold no code (AD-15). The PRD sentence still describes matching at sign-up.
- **Fix (applied):** FR-50 says the code is looked up from the email address when the records are exported.

### M5. The view could hide activity effects

- **Source:** FR-13 and FR-33: an event option's wellbeing effect isn't shown before the pick. FR-53: "a planned activity shows its cost and its effects".
- **What didn't match:** AD-13 hid "the wellbeing effects of options not yet picked". Read broadly, that hides an activity's effects too, and the month plan can't show them.
- **Fix (applied, AD-13):** the rule names event options (FR-13), and says an activity shows its cost and effects (FR-53).

### M6. Item `version`: the addendum says "rises on any change"

- **Source:** addendum, event, activity and message schema tables: "version rises on any change". NFR-4: a text-only correction can apply to running playthroughs.
- **What doesn't match:** AD-7 has the version rise on mechanics changes only. It has to: the version is inside the fingerprint, and a frozen folder may take text edits but no fingerprint change. The first reconcile changed the spine but not the addendum.
- **Fix (applied):** the three schema tables say the version rises on any change to a non-text field, and a text-only correction keeps it.

## Low

| # | Source | What didn't match | Fix |
| --- | --- | --- | --- |
| L1 | FR-58 "only the schema gate and the open-option gate" | AD-7 named a third "reference" gate | Applied, AD-7: two gates; the schema gate includes the reference checks in the schema tables |
| L2 | FR-1: the game says the address is in use | No error code for it in AD-13 | Applied: `email_in_use` (409) |
| L3 | NFR-7: continuing before the real choice, with a crisis or a minigame unfinished | No code among the 409 turn refusals | Applied: `cannot_continue` |
| L4 | FR-5: login ends after 30 minutes with no activity. FR-8 lists when the client fetches | Deferred said "polling"; a background poll would keep a shared PC logged in for ever | Applied, AD-10 and Deferred: the client never polls in the background |
| L5 | FR-5: "stay logged in" is unticked by default | The session a reset creates had no setting | Applied, AD-10: off |
| L6 | NFR-3: player information before a user exists | No owner; AD-13 gave the frontend "only UI chrome text" | Applied, AD-13 and Deferred: the frontend owns the page; its processor list follows AD-14. Default, Dahl can overrule |
| L7 | FR-10: preset avatar looks; NFR-7 refuses what wasn't offered | No list to validate the avatar against | Applied, AD-7: avatar looks in `lists.yaml` |
| L8 | FR-17 and FR-58 minimums and limits are "configuration" | No home for the content check's limits | Applied, Config convention: `content/config/vN/` |
| L9 | FR-6 (5 s) and FR-8 (5 min) are configuration | Client timings had no owner | Applied, Deferred: frontend team |
| L10 | FR-49: every request names its month | A start has no current month | Applied, AD-4: a start names month 1 |
| L11 | §4.4: cut-list items are named, not numbered | AD-10 said "item 11" | Applied |
| L12 | NFR-11, OQ-14 | AD-7 pinned "the newest frozen library", so the sprint-1 spike on the playtest host, before any freeze, had nothing to pin | Applied, AD-7 |
| L13 | NFR-7 input list | Life goal, avatar and starting a new life aren't listed, though FR-9, FR-10 and FR-43 make them inputs (AD-2 lists them) | Applied in the PRD |

**PRD-side syncs with no decision needed (applied):** addendum "For the architecture", Responsiveness: "backend and database in the same region" → Amsterdam and Frankfurt (AD-14 records the departure). OQ-14: answered by AD-14; what's left is the sprint-1 spike.

## Checked and matching

Account and login limits, session lifetimes and revocation (FR-1 to FR-5, FR-44, addendum limits table). Saving, idempotent retries and two devices (FR-6 to FR-8, NFR-7). Start and resume (FR-9 to FR-11). Month loop, two-part month and plan version (FR-12, FR-49). Selection, offers and messages (FR-18, FR-46, FR-48, FR-54, FR-55). Content layout, versions and the freeze (FR-17, FR-58, NFR-4). Exact money (NFR-4, rule 2). Cause links and the ending ranking (FR-36, FR-42, addendum "Cause link shares"). Derived flags and the room (FR-34). Disclosures per account (FR-40). Minigames (FR-51). Playtest records, tester codes, test accounts and export (FR-50, NFR-3). Email off in the playtest (FR-3, NFR-11, OQ-4). Hosting, limits, cost and logs (NFR-5, NFR-6, NFR-10, NFR-11). Tests (NFR-9, §7.3, F5 in V2). V2 seam (addendum "Ready for V2").

## Not re-run

The reviewer gate's three lenses (rubric, adversarial, currency) were not run again after these fixes.
