---
title: Architecture spine validation
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (PR #119, docs/arkitektur-116)
---

# Architecture spine validation

**Verdict:** The spine is strong and buildable: the PRD is fully bound, the core (pure engine, one pipeline, one ledger, versioned content) holds, and no reviewer found a critical problem. What is left sits in the seams added late (the Vercel/Railway boundary, #105 one-off shifts and hours offers, the #116 figures) and in request-lifecycle facts the stories would otherwise guess. Fix the 12 high findings before epics and stories; most need one or two sentences.

| Severity | Count (after merging duplicates) |
| --- | --- |
| Critical | 0 |
| High | 12 |
| Medium | 21 |
| Low | ~28 |

## Reviews run

| Lens | File | Critical / high / medium / low |
| --- | --- | --- |
| Rubric walker (good-spine checklist) | `review-2026-11-23-rubric.md` | 0 / 3 / 7 / 8 |
| Currency (versions, services, facts) | `review-2026-11-23-currency.md` | 45 items: 40 confirmed, 3 contradicted, 2 unconfirmed |
| Adversarial (compliant units that still collide) | `review-2026-11-23-adversarial.md` | 0 / 8 / 13 / 11 |
| Drift against the current PRD and final UX | `review-2026-11-23-drift.md` | 0 / 2 / 6 / 9 |

Lint (`lint_spine.py`): clean apart from the known `{client_ip}` false positive.

## Checklist

| Item | Verdict | Evidence |
| --- | --- | --- |
| Fixes the real divergence points | adequate | Core fixed hard; response envelope, no-playthrough view, commit owner, sessions lock and worker count open |
| Every rule enforceable | adequate | ORIGIN_SECRET, RLS on every table and the no-clock rule have no check |
| Deferred is safe | adequate | Only the deferred request/response models can diverge, through the envelope |
| Technology current | adequate | FastAPI and SQLAlchemy notes stale; Railway edge header claim contradicted |
| PRD coverage | strong | FR-1 to FR-58 and NFR-3 to NFR-11 bound; FR-35 still bound though left out; #105 only partly carried |
| Owned dimensions | adequate | Deployment, infra, data lifecycle and tests strong; observability thin |
| No bloat | thin | 56 KB; inline rationale (Safari, bcrypt bytes), a 14-item spike checklist, a repeated paragraph |
| Internal consistency | adequate | Proxy fallback vs AD-10; 'tests never load a play library' vs seed checks; stale baseline dates |

## High

### H1. The client address through Vercel and Railway isn't settled

*Currency C1, Rubric H1, Adversarial M6*

AD-10 says Railway's edge appends to X-Forwarded-For; Railway's accepted forum answer (2026-09-29) says it overwrites it, so Caddy's leftmost address could be Vercel's egress IP and every tester would share one login limit. The AD-14 fallback (a Next.js route handler) contradicts AD-10's 'never through a Next.js function', and Next.js server code calling /api would swallow the re-issued session cookie.

**Fix:** State the edge behaviour as a spike check, not a fact; try x-vercel-forwarded-for first, then the route-handler fallback with its cookie and IP-header rules written into AD-10; forbid other server-side /api calls.

### H2. Nothing enforces the origin secret that makes trusting every proxy safe

*Rubric H2*

AD-10 trusts every peer 'only because' Caddy refuses requests without ORIGIN_SECRET, but the ≥32-byte, no-placeholder guard in AD-14 covers backend secrets only.

**Fix:** Add a Caddy entrypoint guard that refuses to start on a short or placeholder secret, and a refusal assertion in the daily check.

### H3. An action's result is a second projection outside the player view

*Adversarial H1*

The result can leak drawn delays or minigame routes, store filled-in nickname and 'i fjor' text in action_log, and can't be shown again after a reconnect (FR-6).

**Fix:** An action's result is engine state (ids, integers, cause links) in the open month; the view renders it under the same exclusion test; action_log stores only that structured result.

### H4. Text parameters can be filled when the item arrives or when the view is built

*Adversarial H2*

Filled at view time, an old message shows today's figures (month 14's interest message shows month 40's interest).

**Fix:** Every figure a text shows is captured as a named parameter when its item enters the state; only the nickname and the month placeholder are resolved at view time.

### H5. 'After the plan' figures can come from a preview that differs from continue

*Adversarial H3*

The #116 bands, the rule 8 trigger and goal progress 'after planned activities' can be computed by a light preview that disagrees with continue on card payments and dropped activities.

**Fix:** Continue is composed of apply_plan(state, content) (activities, wellbeing, rule 8; no draws, no month change); the view calls apply_plan on a copy for every after-the-plan figure.

### H6. Ledger tags and crisis-month money actions have two readings

*Adversarial H4, H5*

A subscription started by an option can be tagged purchases and charged by the wrong FR-45 row; a savings transfer or BSU withdrawal in a crisis month pays overdue minimums under receive() but not under transfer().

**Fix:** The calling step passes payment-order row, flow class and part from one engine table keyed by what is paid; each money action maps to one ledger function; the rule 8 money-in order runs after every money action or crisis choice that raises the current account.

### H7. A content-model field added after the freeze breaks every deploy

*Adversarial H6*

Frozen config/v1 lacks the new field, so startup fails; the quick escape is a hard-coded figure, which breaks NFR-4.

**Fix:** Fields added after a freeze are optional; content/config/backfill.yaml gives each older version's value with source and date; the engine never defaults a game figure.

### H8. Draws are reproducible only on the machine that made them

*Adversarial H7*

Directory order differs between macOS, CI and Railway, so the same seed can draw different events.

**Fix:** Draws use SHA-256 over (seed, month, key), and every collection and eligible list is sorted by content id.

### H9. No view before the first start or after a life ends early

*Adversarial H8, Rubric M2*

GET /api/game has no defined answer; a player who ended early is refused game_changed on every new start; the goal screen has no source for its config figures.

**Fix:** That view is built from the versions a start would pin now, chosen by one shell function the start action also uses, and carries the ended row's id.

### H10. 'Tests never load a play library' contradicts the seed and content checks

*Rubric H3, Adversarial M5*

CI's seed-state assertions and the FR-58 content check load the play library; seeded targets will turn CI red during tuning while v1 isn't frozen; the seed script can't pin versions through the pipeline.

**Fix:** Carve out the seed check and the content check from AD-7's rule, let seed targets warn until the freeze, and give the start action an optional version pin used only by the CLI.

### H11. One-off shifts and hours answers have no content home or owner

*Drift H1*

FR-47 (#105) takes shifts 'from the content library', but AD-7 has no folder, the addendum no schema, the message schema no link for an hours answer, and AD-8 picks only the event and messages.

**Fix:** Add shifts/ to AD-7 and a schema to the PRD addendum; AD-8 also picks the month's shifts and the triggered hours answer.

### H12. The loan sheet's quote per term has no read path

*Drift H2*

The UX shows the instalment and total cost for 12/24/36 months before the player takes the loan; AD-4 offers only GET /api/game and AD-13 forbids the frontend computing figures.

**Fix:** The view carries the engine's quote for each allowed term (or a read-only GET /api/game/quote); add FR-25 to AD-13's binds.

## Medium

### Request lifecycle

- The response envelope isn't fixed: where server_time goes, and 'player view' vs state (Rubric M1); Vercel and Caddy errors lack the shape (Adversarial M7); a malformed request is refused before the state it must return is loaded (Adversarial M8).
- Who commits is fixed only for the pipeline's write; the session slide on read and refusal paths has no owner (Rubric M3).
- The lock order leaves out sessions, and the session is checked before the lock, so revocation and deletion race the pipeline (Rubric M4, Adversarial M4).
- A retried start looks for its request_id in a playthrough that no longer exists (Adversarial M1).
- Sign-up and password change aren't idempotent but would be retried like game actions (Adversarial M2).
- Pydantic's lax mode accepts '5000' where NFR-7 refuses it; plan_version sits in the envelope (Adversarial M9).

### Inputs and refusals (#105)

- AD-2 accepts only NFR-7's input list, which lacks loan term, card payment mode, more/fewer hours and yes/no on an offer (Drift M1).
- NFR-7's refusal list wasn't updated for #105, and AD-13's codes and the one-test-per-refusal rule follow it (Drift M2, PRD change).
- One-off shift pay: rounding point, the rate's age and the stored figure aren't fixed (Drift M3).
- Rule Set v1 rule 10, D12 and the PRD addendum still say the player sets weekly hours (Drift M6, PRD/Rule Set change; widen #117).

### Frontend boundary

- The single error shape can't mark which form field failed (Drift M4): add fields: [{field, code}] for account forms.
- The live nickname preview at sign-up breaks 'the frontend never inserts it into game text' (Drift M5).
- FR-8's idle fetch built as a timer keeps a shared PC logged in (Adversarial M10).
- A raw integer can be formatted by both the frontend and the engine (Adversarial M13).

### Engine data

- FR-42's per-choice totals don't say which flow classes count, or which inputs are choices (Adversarial M11).
- Decimal in the state document has no defined JSON path; default=float brings float drift back (Adversarial M12).
- The inactivity job: last_active_at is null after sign-up, so those accounts are never deleted (Adversarial M3).

### Operations

- The Uvicorn worker count isn't fixed, but the pool of 5 and the in-process daily jobs assume one worker (Rubric M5).
- Observability is thin: no log format, request id, 500 handler or error alert; Uvicorn's default access log includes the client address (Rubric M6).
- .railway/railway.ts only applies through railway config apply; a partial file deletes undeclared services; the region goes in replicas; Serverless stays a dashboard toggle (Currency).
- Rationale and story-level detail inflate the spine and will rot (Rubric M7).

## Currency

- FastAPI: 0.165.0 (2026-11-18) is current; 0.163.2 changed parameter reading (touches NFR-7), 0.164.0 added max_body_size. Write 0.165.x and run the null-vs-omitted tests against the lock.
- SQLAlchemy: 2.1.9 (2026-11-16). Write 2.1.9 or rely on uv.lock.
- Railway logs: docs say 7 days on Hobby and no region; keep the stricter 90-days-in-US-West disclosure, citing the staff answer (2026-10-08).
- Newly confirmed: Vercel's routes entry with the header transform, x-vercel-enable-rewrite-caching: 0, the visitor IP reaching an external origin, fra1 (must be set; default iad1), 1-hour Hobby logs.

## Low

About 28 low findings (Rubric 8, Adversarial 11, Drift 9), each with a fix in its file. Examples: FR-35 still in binds though left out (#115); Stale baseline dates ('PRD as it stands on 2026-11-15', 'same region'); No CI check for RLS on every table; Structural Seed misses Dockerfiles, workflows, README; Capability map gaps (NFR-4/7/8/9, FR-47's spread); action_log cascade; Ops commands run a local checkout; Caddy healthcheck gets 403 on Railway; Ending view's year has no months; UX loan terms 12/24/36 vs PRD 12-60.

## Next steps

1. Roll the 12 high findings and the request-lifecycle mediums into an architecture Update (AD IDs stable), on the same PR #119 or a follow-up.
2. PRD/Rule Set side (needs the PM): NFR-7 inputs and refusals for #105, rule 10/D12 hours wording (#117), a shift schema in the addendum, loan terms.
3. Spike (#92) gets two more checks: the Railway edge's X-Forwarded-For behaviour and railway config plan.
4. Then bmad-create-epics-and-stories.
