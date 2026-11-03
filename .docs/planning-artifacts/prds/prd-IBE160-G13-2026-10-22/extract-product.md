# Extract: LifeMode product facts for the PRD

Facts only, taken from the sources below. Nothing here is a recommendation. Where a source contradicts the memlog, the memlog version is stated and the contradiction is listed in section 9.

## Sources and how they are cited

All planning paths are under `.docs/planning-artifacts/`.

| Tag | File | Status |
|---|---|---|
| memlog | `prds/prd-IBE160-G13-2026-10-22/.memlog.md` (cited by file line, L6-L18) | Read. Authoritative; later entries override earlier ones |
| brief | `briefs/brief-Ibe160-prosjektmappe-2026-09-17/brief.md` | Read. Frontmatter: final, updated 2026-11-03 |
| addendum | `briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md` | Read. Updated 2026-11-03 |
| arch | `architecture/architecture_technical_design.md` | Read |
| DT | `.docs/design-thinking-2026-10-16.md` | Read. **Mostly an unfilled template.** Only the header and the "Design Challenge" section have content. Every section from Empathize to Next Steps holds unfilled `{{placeholders}}`, so it has no user insights, ideas, test results or metrics |
| guide | `docs/sensorveiledning/sensorveiledning-ibe160-del1.md` | Read. It says it is a text version of `sensorveiledning-ibe160-del1.pdf`, and that the PDF is the original. The PDF was not opened or compared. The overall grading guide it refers to, and any part 2 guide, were not found in the repo search |

`prds/prd-IBE160-G13-2026-10-22/prd.md` holds only a title and frontmatter.

The memlog also names inputs outside this extract: market-research, market-validation, tilbakemelding-product-brief, user-research.md (133 responses), the research from 2026-10-27 to 2026-10-31, and meeting-prep-2026-11-05.md (memlog L6, L17).

## 1. Product purpose and target users

- **Purpose:** LifeMode helps youth reflect on financial choices and consequences, to understand how personal finance works and how it affects life (memlog L7).
- **Concept:** a mobile-friendly life and money simulation where every choice carries forward. "Let young people make expensive financial mistakes before those mistakes cost real money" (brief §Executive Summary).
- **Design challenge:** help young people aged 15-20 understand how today's money decisions shape their options months and years later, before those decisions cost real money (DT §Design Challenge).
- **Problem:** savings, interest, credit, debt, rent and budgets feel abstract until they cost something. Real-world trial and error is the lesson that sticks, and also the expensive one (brief §The Problem).
- **Primary user:** young people aged 15-20 in Norway, especially those approaching their first real financial decisions (brief §Who This Serves; DT §Design Challenge). They want to feel grown-up and make their own choices, and do not want it to feel like homework (brief §Who This Serves).
- **Success in a user's day:** a 10-15 minute phone session, after which they can say "that's why that happened" about a decision they made (brief §Who This Serves).
- **Others:** parents, schools and banks may later pay for or fund access, but the first version is designed for the player (brief §Who This Serves).
- **Differentiation (narrowed 2026-10-31):** built for Norway: Norwegian rules and life stages for 15-20-year-olds, combining good money management with wellbeing without becoming complicated (brief §What Makes This Different). The endgame also sets it apart from games such as Koll på cashen, and shows that good money management is not just about earning as much as possible (addendum §Win Condition & Endgame).
- **Project frame:** graded IBE160 course project, delivery Dec 2026. Readers are the team, downstream BMAD agents and the sensor. Rigor: thorough but not padded, with traceable FR IDs (memlog L9).
- **PRD approach:** coaching path, journey-led (memlog L12, L13).

### Confirmed user journeys (memlog L14)

| ID | Journey |
|---|---|
| UJ-1 | First session |
| UJ-2 | Pause and resume (possibly other device) |
| UJ-3 | Choice that comes back |
| UJ-4 | Crisis month |
| UJ-5 | Ending at age 20 and replay |

## 2. Game loop and rules

### Timeline and loop

- **Length:** 60 months, ending on the 20th birthday (memlog L16; addendum Rule 7).
- **Pacing:** a playthrough is tuned to about 20-30 real choices (addendum Rule 7; brief §The Solution).
- **Loop** (brief §The Solution):
  1. See the situation: this month's event or dilemma, with balance, savings, debt and fixed costs.
  2. Choose one of a few options.
  3. See the consequence in numbers: what changed and why.
  4. Next month: income, fixed costs, interest and instalments are applied, and the next situation builds on earlier choices.
- **Quiet months:** still processed by rules 1-5, but the player only sees a short summary (addendum Rule 7).
- **Five money mechanisms:** wages from part-time and summer jobs; saving (savings account and BSU); fixed costs (mobile and transport); consumer loans and credit cards from age 18; unexpected expenses (brief §Scope In #1).

### Life goals (memlog L16; addendum §Win Condition & Endgame)

The player picks one of three at the start. All are checked at age 20:

1. Save for something big (a savings target)
2. Debt-free with a buffer
3. Afford a big experience, such as a trip

### Wellbeing (memlog L16; addendum §Win Condition & Endgame)

- Three parts, weighted by the chosen goal:
  - stress, from debt and crisis months
  - free time, from hours worked
  - social life, from choices in events
- Each event choice carries a wellbeing effect.
- Housing is not part of the meter in version one.
- Target amounts, wellbeing weights and the threshold are configuration, set when the game is tuned.

### Endings (memlog L16; addendum §Win Condition & Endgame)

Checked in this order at age 20:

1. **Loss:** a crisis condition from Rule 8 is active. Consequences are shown clearly, and the text also reflects wellbeing.
2. **Real win:** goal reached and wellbeing above the threshold.
3. **Hollow win:** goal reached, wellbeing below the threshold.
4. **Goal not reached:** neither win nor loss. The player gets advice on modest savings goals and their benefits, and a reflection on the consequences of not saving.

- Going below zero during the game only starts a crisis month; it is not a loss (memlog L16).
- All endings are calculated by the engine from measurable state and work with no AI (addendum §Win Condition & Endgame).

### Crises (addendum Rule 8; memlog L16)

- The engine, not the AI, starts a crisis month when any of these is true at the end of a month:
  - the current account is below NOK 0
  - the credit card minimum has been missed two months in a row
  - total debt is above 3 x average monthly income over the last three months
- A crisis month has 2-3 linked choices with real-world actions (sell something, take extra shifts, ask for a payment plan, ignore it). The engine calculates the effect of each.
- A crisis never ends the game in version one. Ignored debt keeps growing under rules 4-5 and triggers new crisis months.
- A crisis condition still active at age 20 leads to the loss ending.

### Events (addendum §Event Library; brief §Scope In #5; memlog L15)

- At least 30 events, target 60-80, plus about 10 crises.
- Split roughly 55/45 before and after age 18.
- Fixed schema for every event: mechanism, age, flags, boomerang pair, teaching point, LK20 code, source, wellbeing effect for each choice.
- The library lets the whole game be played start to finish without AI.

### Cause links and consequences (addendum §Choice and Consequence; brief §Scope In #8; memlog L15, L16)

- Every engine effect stores its cause. The same link drives:
  - echo badges, when an earlier choice comes back
  - a "Hvorfor?" button that explains a change
  - "if you had chosen differently" lines
  - the ending, which shows the three choices that mattered most
- Effects with no choice behind them (wages in a quiet month, a random expense) are stored with a system cause. "Hvorfor?" explains these from the rules.
- "If you had chosen differently" lines are calculated by the engine, never the AI, and only where the engine can calculate the result reliably, starting with interest and instalments.
- Top three choices are ranked by effect in kroner.
- Replay starts again from age 15. Replay from a crossroads is out of the MVP, because it requires storing earlier game states.

### Rule Set v1, with its numbering (addendum §Financial Engine)

Numbers are stored as configuration, not hard-coded.

| Rule | Content |
|---|---|
| 1 | One round is one month. Fixed order: income → tax → fixed costs → loan instalments and interest on debt → interest on savings → the month's event and the player's choice |
| 2 | Whole NOK. Monthly interest = `balance × annual rate / 12`, rounded to the nearest krone (0.5 rounds up) |
| 3 | Tax on total wage income for the calendar year at 2026 rates. Up to NOK 99,650, no tax. Above that, trygdeavgift of 7.6% of the whole income (5.1% under 17), never more than 25% of the income above NOK 99,650. Income tax is 22% of ordinary income (income minus minstefradrag) above the personfradrag, plus trinnskatt step 1; higher steps are not modelled. Each month deducts the increase in the year's calculated tax. The 50% employer withholding above the frikort limit is not modelled as tax |
| 4 | Consumer loan: annuity, `P × r / (1 − (1 + r)^−n)` with `r` = annual rate / 12, rounded to whole kroner. Final payment is adjusted so the balance ends at exactly zero |
| 5 | Credit card: no interest if the full balance is paid by end of month. Otherwise interest on the whole balance. Minimum payment is the larger of 3% of the balance and NOK 300 (or the whole balance if smaller) |
| 6 | Consumer loans and credit cards only from the 18th birthday |
| 7 | Quiet months (see above); 60 months tuned to about 20-30 real choices |
| 8 | Crisis months (see above) |
| 9 | BSU deduction, calculated in December's tax step: the lower of 10% of the year's BSU deposits (deposits capped at NOK 27,500) and the year's calculated tax. With no tax, the deduction is NOK 0 and unused deduction is lost. The game says so plainly ("BSU deduction: NOK 0, you have no tax to reduce") and shows that BSU still pays off through higher interest (5.61% against 2.87%) |
| 10 | Working hours follow arbeidsmiljøloven; the engine never allows more. The limit depends on compulsory schooling, not age alone: a 15-year-old in 10th grade gets 12 h per school week; a 16- or 17-year-old in upper secondary gets 40 h per week. Summer jobs use the limits for weeks without school. Night work (§ 11-3) is not modelled |

### Parameters (addendum §Financial Engine, Parameters; sources as listed there)

| Parameter | Value | Note |
|---|---|---|
| Savings account interest | 2.87% per year | SSB 11018, Aug 2026 |
| BSU interest | 5.61% per year | SSB 11018, Aug 2026 |
| BSU deduction | 10% of the year's deposits; max deposit NOK 27,500 per year (max deduction NOK 2,750); max NOK 300,000 total; cannot exceed the year's tax; not carried forward | Skatteetaten |
| Consumer loan interest | 15% per year, fixed | [ASSUMPTION] mid-range of about 9-22% |
| Credit card interest | 22.6% per year | SSB 12844, 2026 Q2 |
| Hourly wage under 16 / under 18 / 18+ | NOK 136.41 / 139.40 / 195.04 | Virke/HK from 1 April 2026 |
| Working hours, under 15 or in grunnskole | Max 2 h per school day, 12 h per school week; 7 h per day, 35 h per week without school | aml. §§ 10-4, 11-2 |
| Working hours, 15-18 after grunnskole | Max 8 h per day, 40 h per week | aml. §§ 10-4, 11-2 |
| Working hours, 18+ | 9 h per day, 40 h per week | aml. §§ 10-4, 11-2 |
| Frikort limit | NOK 100,000 per calendar year; 50% withholding above it is not final tax | Skatteetaten |
| Trygdeavgift | Lower limit NOK 99,650; 7.6% (5.1% under 17); max 25% of income above the limit | Skatteetaten 2026 |
| Income tax | Minstefradrag 46%, max NOK 95,700; personfradrag NOK 114,540; 22% on ordinary income; trinnskatt step 1: 1.7% from NOK 226,100 | Skatteetaten 2026 |
| Rent, hybel | NOK 8,770 per month | SSB 09895, 2025. Not used in version one |
| Youth public transport, 30 days | NOK 238 | Ruter, from Aug 2026 |
| Mobile subscription | NOK 299 per month | [ASSUMPTION] |
| Example unexpected expense | NOK 2,500 (broken phone screen) | [ASSUMPTION] |
| Policy rate | 4.5% | Background only |

### Worked examples and functional tests

Worked examples (addendum §Worked examples):

| Ex. | Situation | Expected result |
|---|---|---|
| 1 | Summer job at 16: 120 h × NOK 139.40 | NOK 16,728; no tax |
| 2 | NOK 10,000 in savings, 12 months at 2.87% | NOK 10,289 (a plain compound formula gives NOK 10,291; the result depends on Rule 2) |
| 3 | Consumer loan NOK 20,000 at 15% over 12 months | Monthly NOK 1,805, final NOK 1,808, total NOK 21,663 |
| 4 | NOK 3,200 on a credit card, minimum only | Paid off after 13 months, total NOK 3,606 |
| 5 | 18-year-old earns NOK 110,000 in a calendar year | NOK 2,588 tax, all trygdeavgift; income tax 0 |
| 6 | 17-year-old on frikort keeps NOK 10,000 in BSU for 12 months | Deduction NOK 0; balance NOK 10,576, against NOK 10,289 in ordinary savings |

Functional criteria (brief §Success Criteria, Functional / testable):

| # | Criterion | Expected result | Test |
|---|---|---|---|
| F1 | Consumer loan (ex. 3) | As ex. 3 | Unit test |
| F2 | Savings (ex. 2) | NOK 10,289 | Unit test |
| F3 | Credit card (ex. 4) | As ex. 4 | Unit test |
| F4 | A crisis trigger is met | Crisis month with linked choices every time; never silently skipped | Unit test per trigger |
| F5 | AI returns an invalid, malformed or unsafe event | Pre-written fallback; never a blank screen or unfiltered output | Mocked failing AI. AI dependency: see Conflict A2 |
| F6 | Full playthrough 15-20 | Completable using only the pre-written library, zero AI calls | Automated run with AI disabled |
| F7 | Summer job (ex. 1) | NOK 16,728, no tax withheld | Unit test |
| F8 | 18-year-old on NOK 110,000 (ex. 5) | NOK 2,588, no income tax | Unit test |
| F9 | Every end state: crisis active or not, goal reached or missed, wellbeing above or below threshold | Exactly one valid ending screen: loss, real win, hollow win or goal not reached | Automated test per end state |
| F10 | Every echo badge and "Hvorfor?" explanation | Refers to an earlier choice that exists in the playthrough | Automated integrity test of cause links. See Conflict B3 |

Rules 9-10 and worked example 6 have no F criterion in the brief's table.

### Disclosed simplifications (addendum §Simplifications the game discloses)

Each text is shown the first time the mechanism appears (info icon or under "Hvorfor?"), and all are collected on one "Om tallene" page. Player-facing text is in Norwegian. The full wording is in the addendum.

| # | Applies to |
|---|---|
| D1 | Tax (Rule 3): calculated from whole-year income; real employer withholding differs |
| D2 | Wages: minimum rate in the Virke/HK agreement; Norway has no statutory minimum wage |
| D3 | BSU interest: August 2026 average across Norwegian banks |
| D4 | Credit approval (rules 4-6): simplified; real banks check income, debt and payment remarks |
| D5 | Consumer loan interest: 15% is a mid-market estimate |
| D6 | All rates: 2026 numbers, held fixed for the whole game |

## 3. What a player sees and does in a session

- **Start:** log in or register, create an avatar and pick a life goal (brief §The Solution; brief §Scope In #1, #7, #9).
- **Each active month:** see the event or dilemma with balance, savings, debt and fixed costs, pick one of a few options, then see what changed and why (brief §The Solution).
- **Quiet month:** a short summary only (addendum Rule 7).
- **Crisis month:** 2-3 linked choices (addendum Rule 8).
- **Explanations:** echo badges, "Hvorfor?", "if you had chosen differently" lines, simplification texts behind an info icon or "Hvorfor?", and the "Om tallene" page (addendum §Choice and Consequence; addendum §Simplifications).
- **Pause and resume:** a playthrough is longer than one sitting; the player can take a break and pick up the same life later, also on another device (brief §Constraints; memlog L14 UJ-2).
- **Session length:** 10-15 minutes on a phone (brief §Who This Serves).
- **Ending:** one of four ending screens, showing how choices led there and the top three choices by kroner effect (brief §How it ends; addendum §Choice and Consequence).
- **Replay:** starts again from age 15, and different choices give a different life (brief §The Solution; brief §Scope In #8).
- **Input:** no free text beyond the username (memlog L15).
- **Devices:** mobile-first, with layout adapting dynamically to phone, tablet, laptop and desktop (memlog L10). No horizontal scrolling, touch-friendly controls, no core function depending only on hover, readable type on small screens, usable forms and navigation (arch §Mobile-First Requirements).
- **Accessibility:** WCAG 2.x level AA (memlog L11).

**Not specified in the files read:** what avatar creation contains, onboarding content, the amounts behind each life goal, the wellbeing threshold and weights (configuration, not yet set), and how the player chooses work hours.

## 4. Scope and cut order

### In (MVP)

From brief §Scope In, with AI excluded per memlog L17:

1. Avatar and a simulated life from 15 to 20 with the five money mechanisms, quiet months and crisis months (#1).
2. Financial engine following the written rule set with realistic Norwegian 2026 numbers, whole kroner, fixed monthly order and worked examples as the test answer key (#2).
3. Pre-written event library; whole game playable without AI (#5).
4. Mobile-first responsive website with zero ongoing cost: TypeScript frontend, Python backend, Supabase database (#6).
5. Three life goals, goal-weighted wellbeing meter and four endings (#7).
6. Cause links: echo badges, "Hvorfor?", "if you had chosen differently" lines, top three choices, replay from 15 (#8).
7. Login with username and player-created password, to save and resume (#9).

### Out

- **AI layer:** not part of the MVP, planned for later (memlog L17; brief §What Makes This Different, narrowed differentiation; addendum §MVP Scope Priority). It is described as stage two in brief §Scope In #3-4 and arch §Build stages.
- Open-ended negotiation with NPCs (brief §Scope Out #1; arch §Open-ended negotiation guardrails).
- Parent visibility (brief §Scope Out #2; arch §Content safety).
- Real bank connections, real financial data, personal advice, investments, crypto, advanced mortgages, complex tax, real-money transactions (brief §Scope Out #3).
- Payments, family or school accounts, partner features. School and private modes are possibly later (brief §Scope Out #4; memlog L15).
- Moving out and rent first, then driving licence and education, as later steps (brief §Scope Out #5). Rent is unused in version one (addendum §Rules).
- Replay from a crossroads (memlog L16).
- Password reset (memlog L15).
- Night-work rules and higher trinnskatt steps (addendum Rules 3, 10).
- Automatic deployment and public production hosting are not required (arch §Continuous Integration; arch §Docker and Local Execution).

### Cut order (memlog L16; addendum §MVP Scope Priority; brief §Scope)

If time runs short before December, content is cut before the core:

1. "If you had chosen differently" lines
2. Events, down to the minimum of 30

The engine, wellbeing, the endings, cause links, "Hvorfor?" and login stay (addendum §MVP Scope Priority).

### Playtest criteria (brief §Success Criteria, Playtest)

Starting values that may be adjusted once real data exists. 10-20 people before December delivery, only fellow students and other volunteers aged 18-20 (also memlog L15). No names or contact details stored with results; answers and scores recorded anonymously.

| Signal | Metric | Target |
|---|---|---|
| User outcome | Explains how an earlier decision affected a later outcome | 70% or more |
| User outcome | 5-question money quiz, before vs. after | Higher after |
| Behaviour | Completes the full playthrough 15 to 20 | 70% or more |
| Behaviour | Voluntarily returns for a second session or replay within one week | 50% or more |
| Experience | "It felt more like a game than schoolwork" (1-5) | Median 4 or higher |
| Experience | Two playthroughs with different choices described as different stories | Most players |
| Mission | A parent or teacher who sees it wants to try it | At least one |

## 5. Login and privacy

### Decided

- Login with username and a password the player creates, to save and resume progress (memlog L15; addendum §Login secret; brief §Scope In #9).
- No email, no real age, no free text beyond the username (memlog L15; addendum §Privacy).
- Supabase Auth stores the password as a hash. It is never kept in the project's own tables, logs or game state, and never sent to an AI (addendum §Login secret; arch §Authentication and authorization).
- A forgotten password cannot be reset; the player loses access. Password reuse is not addressed for now (memlog L15; addendum §Login secret).
- Playtests only with 18-20-year-olds (memlog L15).
- Open privacy questions do not block the MVP or the PRD; they are checked before go-live, issue #24 (memlog L15; addendum §Assessment).

### Planned, untested

Supabase Auth normally uses email or phone. The planned approach is an internal address made from the username, such as `raskrev482@lifemode.invalid`, with email confirmation off. It is never shown to the player. It has not been tested on self-hosted Supabase and should be tried early in the build (addendum §Login secret; arch §Authentication and authorization).

### Project assessment, not team decisions (memlog L15)

- All usernames should be treated as personal data. This is the project's own reading, not legal advice (addendum §Assessment).
- Recommended, not decided, to check before go-live (addendum §Recommended measures):
  1. Generated usernames.
  2. If typed, guidance and limits on length and characters, rejecting email addresses and phone numbers.
  3. Username kept private and never sent to an AI.
  4. A documented legal basis other than consent, and short player information a 15-year-old understands.
  5. No analytics or advertising cookies, deletion of inactive games, a player delete button.

### Data minimisation (arch §Data minimization)

The MVP does not need real bank accounts, salary, debt, national identity numbers, location history, contact lists, private messages, investments or transaction histories. Age, savings and income are simulated values.

## 6. Technical constraints that bear on requirements

- **Stack:** TypeScript frontend and Python backend (course requirement); Supabase is the required database and provides authentication (arch §Technology Choices; brief §Scope In #6).
- **Cost:** zero ongoing cost is a hard constraint (arch §Build stages; brief §Scope In #6).
- **Authority:** the deterministic backend is authoritative for financial calculations and critical game state (arch §Authoritative state).
- **Persistence:** the database stores the player reference tied to the username, avatar configuration, playthroughs, chosen life goal, financial state, wellbeing state, decisions, cause links, game history, the event library and which events a playthrough has seen (arch §Database and Data Model). The list also names generated life events.
- **Access control:** a player can reach only their own data. Row Level Security where relevant. Privileged credentials and service keys are never in frontend code (arch §Authentication and authorization).
- **Untrusted input:** player input is treated as untrusted; backend validation protects against invalid financial values and attempts to bypass game rules (arch §Untrusted input and output).
- **Local execution:** Docker for reproducible local execution and delivery. Self-hosted Supabase via Docker, so a sensor can run the full application without the team's cloud account or keys. The game runs AI-free with the pre-written library (arch §Docker and Local Execution; brief §Constraints).
- **CI:** GitHub Actions is planned, checking frontend build, backend tests and financial-engine tests. CD is not required (arch §Continuous Integration).
- **Dependencies:** must be reproducible; pnpm and uv are candidates, not final (arch §Package and Dependency Management).
- **Security testing named:** authentication and authorization, access to another player's data, database permissions, invalid financial values, account deletion, main mobile and browser flows (arch §Security testing). See Conflict B5 on deletion.
- **Stage-one technical success** (arch §Technical success criteria):
  - the full-stack application runs locally
  - F-criteria pass
  - a full playthrough works with zero AI calls
  - authentication separates stored data
  - state persists correctly
  - the primary flow works on all four device classes
- **Development evidence kept:** Git history, tests, technical decisions, development artifacts, evidence of code review and quality assurance (arch §Development Process).

### AI design recorded for later (not MVP)

- Principle: "The AI creates the life; the financial engine determines the consequences" (arch §Game Master).
- Structured output validated before display; moderation before display, with fallback to a pre-written event; no human reading of private sessions (addendum §AI Safety; arch §Content safety).
- Provider abstraction, with a free-tier provider not yet chosen (arch §AI provider abstraction).
- Negotiation only inside engine-defined bounds (arch §Open-ended negotiation guardrails; addendum §AI Negotiation Mechanic).

## 7. What the grading guide expects

**On a PRD specifically:** the guide has no PRD template or required sections. "PRD" appears once, as an example of a BMAD planning document that should be actually used and updated, not generated once (guide §4.1, Planlegging).

**Weights** (guide §2): part 1 is 70% of the total grade; the reflection report is 30% (guide §6).

| # | Kriterium | Vekt |
|---|---|---|
| 1 | Prosess og KI-styring | 30% |
| 2 | Funksjonalitet og omfang | 20% |
| 3 | Kvalitetssikring og testing | 15% |
| 4 | Design og brukeropplevelse | 10% |
| 5 | Kodekvalitet og arkitektur | 10% |
| 6 | README og kjørbarhet | 10% |
| 7 | Ryddighet i repoet | 5% |

**Expectations with a bearing on the PRD and project:**

- **Traceability:** functions in the code can be traced back to requirements and stories, and deviations from the plan are explained (guide §4.1).
- **Decisions:** choices of technology, architecture and solutions are documented with reasons (guide §4.1).
- **AI steering:** saved prompts and AI sessions, with examples of the group specifying requirements and rejecting, correcting or improving AI suggestions (guide §4.1).
- **Process:** even commit history, small commits with descriptive messages, branches, pull requests and issues (guide §4.1).
- **Functionality:** core flows from the proposal and README work end to end. Complexity is judged against the task, such as data storage, several user roles, integrations or non-trivial rules. The app withstands wrong input and repeated actions. Anything left out or changed from the proposal is described and justified (guide §4.2).
- **Testing:** automated tests that run per the README and test meaningful logic; documented manual tests or test plans where automation does not fit; traces of code review and fixed AI-generated errors; input validation and error handling; no secrets in code (guide §4.3).
- **Design:** consistent visuals, clear navigation, understandable feedback, error messages and empty states, basic accessibility (contrast, keyboard navigation, alt text, form labels), fit to relevant screen sizes, traces of design work such as sketches, wireframes or UX descriptions (guide §4.4).
- **Code:** structure matches the described architecture; little duplication or dead code; sensible handling of configuration and dependencies (guide §4.5).
- **README:** what the app does and for whom, prerequisites with versions, exact commands, environment variables with `.env.example`, test data or test users, how to run tests, folder overview, links to planning and process documents (guide §4.6).
- **Running the app:** the sensor follows only the README on a clean machine, spending a guideline 15-20 minutes. If the app cannot run, this clearly lowers criterion 6 and limits how high criterion 2 can go (guide §3).
- **Repo:** clear structure, `.gitignore`, no secrets, no stray files (guide §4.7).
- **What the sensor reads first:** the approved proposal and any product brief, to know what the group promised (guide §3, step 1).
- **Warning signs** (guide §5):
  - planning documents describing a different app than the one delivered, or clearly generated afterwards
  - documentation of AI use that is generic and cannot be tied to concrete changes
  - nearly all code in a few commits before the deadline
  - tests that fail or test only trivial things

## 8. Input status

- DT provides only the design challenge, users, constraints and success statement. It is otherwise unfilled, and this extract uses nothing beyond those.
- Grading guide: the Markdown text version was used; the PDF original was not compared.
- The approved proposal, which the guide treats as the baseline for criterion 2, is not among the files read for this extract.

## 9. Conflicts

### A. A source contradicts the memlog (memlog wins)

| # | Source says | Memlog says | Applied here |
|---|---|---|---|
| A1 | The AI is treated as part of the first version or MVP: brief §Scope In #3-4 list it under "In (version one)" as a second stage; brief §Constraints says "The MVP is built in two stages"; arch §Technical success criteria lists stage two under what "the MVP should also demonstrate"; brief §Executive Summary, §What Makes This Different (the "What LifeMode combines" paragraph), §Scope test and §Vision "Now" all frame the product as AI-driven; DT §Design Challenge names "AI-driven money game" and free-tier AI | AI is not part of the MVP (L17). Brief §What Makes This Different (narrowed) and addendum §MVP Scope Priority agree with this | AI out of MVP |
| A2 | Brief F5 is an unqualified functional criterion that needs an AI response. Arch §Technical success criteria counts F1-F8 under stage one, which includes F5, and also lists F5 under stage two | AI is not part of the MVP (L17) | F5 extracted as written, flagged as AI-dependent |
| A3 | Negotiation: addendum §AI Safety principle 2 says "at least in MVP" for constrained bank negotiation, and addendum §AI Negotiation Mechanic records a mechanic as a team decision | AI is not part of the MVP (L17); no free text beyond the username (L15). Brief §Scope Out #1 and arch also put negotiation out | Negotiation out of MVP |
| A4 | Addendum §Win Condition, "Options considered": net-worth targets, other goal sets (long-term savings, short-term savings, target amount, job/education), housing quality in the meter, three endings. The addendum itself marks this text as superseded | Three goals; stress, free time and social life; four endings (L16) | Memlog version |
| A5 | Brief §Constraints says "the game asks only for a username to log in" and "The player logs in with a username" | A password the player creates is decided (L15). Brief §Scope In #9 agrees | Username and password |
| A6 | Brief §Constraints states "Consent should not be the legal basis" | That recommendation is not a team decision (L15). Addendum §Recommended measures #4 lists it as not decided | Listed as not decided |
| A7 | DT §Design Challenge: "No primary user data yet" | user-research.md now has results, 133 responses (L17) | Memlog version; the research file itself is outside this extract |

Superseded inside the memlog itself: L15's three endings and endgame are replaced by L16; L6's exclusion of user-research.md is replaced by L17.

### B. Sources disagree with each other and the memlog does not settle it (not resolved here)

| # | Conflict | Sources |
|---|---|---|
| B1 | A full playthrough is measured "during the session" and the quiz is measured "before and after one session", but a session is 10-15 minutes and a playthrough is "longer than one sitting" | brief §Success Criteria, Playtest; brief §Who This Serves; brief §Constraints |
| B2 | Arch describes F1-F8 as financial-engine unit tests, but F5 is an AI fallback test and F6 is a full playthrough run | arch §Technical success criteria; brief §Functional / testable |
| B3 | F10 requires every "Hvorfor?" explanation to refer to an earlier choice, and brief says every effect stores the choice that triggered it; addendum says choiceless effects carry a system cause and "Hvorfor?" explains them from the rules | brief F10; brief §How it ends; brief §Scope In #8; addendum §Choice and Consequence (issue #26) |
| B4 | The executive summary example "a cheap first car turns into an expensive repair" sits beside driving licence as a later step. The problem text also names rent, which is unused in version one | brief §Executive Summary; brief §The Problem; brief §Scope Out #5; addendum §Rules |
| B5 | Arch lists account deletion under security testing; a player delete button is only an undecided recommendation, and deletion is not on the brief's scope list | arch §Security testing; addendum §Recommended measures #5; brief §Scope In |
| B6 | DT names parents and teachers as secondary users; brief says the first version is designed for the player | DT §Design Challenge; brief §Who This Serves |
| B7 | Addendum refers to Family Premium as already in the business model; brief puts payments and family accounts out | addendum §AI Safety principle 5; brief §Scope Out #4 |
| B8 | Addendum says of the worked examples "All five were independently recomputed" on 2026-10-22, but the table has six; example 6 was added on 2026-10-31 | addendum §Worked examples |
