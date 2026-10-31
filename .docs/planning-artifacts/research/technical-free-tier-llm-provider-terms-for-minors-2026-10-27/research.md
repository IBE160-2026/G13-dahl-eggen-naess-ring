---
title: 'Technical research: free-tier LLM provider terms for products used by minors'
type: 'technical'
topic: 'free-tier LLM provider terms for products used by minors'
decision: 'Which free-tier LLM provider can LifeMode (players 15-20, Norway, zero running cost) use as its stage-2 AI Game Master without breaching terms or privacy obligations?'
source: 'native run (web search), 2 rounds, 5 assistants'
status: complete
preset: 'standard'
validation: 'normal'
created: '2026-10-27'
updated: '2026-10-27'
claims_verified: 18
claims_unverified: 4
claims_disputed: 1
---

# Technical research: free-tier LLM provider terms for products used by minors

**Decision this research serves:** Which free-tier LLM provider can LifeMode (players 15–20, Norway, zero running cost) use as its stage-2 AI Game Master without breaching terms or privacy obligations?

## Executive summary

**Google Gemini, the brief's first-named candidate, is ruled out, and not only on the free tier.** The Gemini API terms forbid use in any service "directed towards or is likely to be accessed by individuals under the age of 18", with no paid/unpaid distinction, and separately allow only Paid Services for apps available to users in the EEA, which includes Norway [1]. The architecture document should drop Gemini as a candidate.

**Two providers are usable at zero cost: Groq (top weighted score) and Cloudflare Workers AI (runner-up, best verified).**

- **Groq** does not ban apps used by minors; its Services Agreement makes the customer "solely responsible" for legal compliance when an app is likely to be accessed by people under the age of majority, does not train on inputs or outputs, and offers strict JSON-schema output on its gpt-oss models [9][12]. The account holder must be 18+. Its free-plan rate limits could not be read directly (unverified) [11].
- **Cloudflare Workers AI** has no age or minors clause in the terms checked, does not train on or retain inputs/outputs, gives 10,000 free "neurons" per day (roughly 180–360 short game events per day) at 300 requests per minute, and supports `json_schema` output on Llama models [20][21][22][23][24].

**Biggest caveat:** no free tier found offers a confirmed data processing agreement plus EU-only processing. Every finalist processes data in the US or "global jurisdictions" under standard contractual clauses at best [9][16][26]. LifeMode stays compliant mainly by **sending no personal data to the LLM at all** — game state only, no user IDs, no free text from the player — which the addendum's design principles already point toward.

## Requirements frame (select shape)

From the brief and addendum (project context frames the question; it is not evidence):

- **Hard gates:** terms permit a service used by 15–20-year-olds; zero ongoing cost; usable for end users in Norway/EEA.
- **Weighted preferences:** no training on inputs (25), EU processing / DPA on free tier (20), free limits sufficient for 10–20 playtesters plus sensor (20), structured JSON output (20), clarity of terms for minors (15).

## Candidate screen

| Candidate | Result | Why |
|---|---|---|
| Google Gemini API | **Cut (gate: minors, EEA)** | Under-18 ban applies to all tiers; EEA requires Paid Services [1] |
| Hugging Face Inference Providers | **Cut (gate: cost)** | Free users get no monthly credits ("Free Users \| None") [27] |
| GitHub Models | **Cut (gone)** | Fully retired 2026-07-30 [28] |
| Cerebras Inference | **Cut (gate: cost)** | Only a one-time USD 5 credit that expires after 30 days and needs a payment method [18] |
| Groq | Finalist | — |
| Cloudflare Workers AI | Finalist | — |
| Mistral AI (free mode) | Finalist, conditional | Minors allowed only with parental consent [2] |
| OpenRouter `:free` models | Finalist, weak | 50 requests/day [17] |
| Anthropic API | Reference only (paid) | Its minors guidelines are a useful safeguard checklist [8] |

## D1 — Age and minors

- **Gemini:** "You must be 18 years of age or older to use the APIs", and you "will not use the Services as part of a website, application, or other service … that is directed towards or is likely to be accessed by individuals under the age of 18" [1]. A 15–20 game is caught. No exception was found.
- **Groq:** account holders must be 18+. Section 6.3 covers apps "directed towards or is likely to be accessed by individuals under the age of majority in their state or territory" and puts compliance (use by minors, collection of their personal data) on the customer — a responsibility clause, not a ban [9]. The second half of the clause came back paraphrased, so the exact wording should be read on the live page (medium confidence on wording).
- **Cloudflare:** no minors or age clause in the Developer Platform Service-Specific Terms or the Self-Serve Subscription Agreement [24][25]. Models are third-party products whose acceptable-use policies apply; the Llama 3.3 AUP sets no end-user age minimum and bans harm to children and "failure to employ legally required age-gating" for illegal material [29]. Cloudflare's separate Acceptable Use Policy was not checked (open question).
- **Mistral:** no minimum age, but the customer must not "allow minors to use the Mistral AI Products without legally adequate consent from their parent or guardian", and this extends to end users of a customer's app [2]. For LifeMode that means a parental-consent flow for every 15–17-year-old player — a real product burden.
- **OpenRouter:** account holders must be 18+ [14]; customers' end users must use the service "in accordance with" the terms, which leaves the end-user age question ambiguous (medium confidence).
- **Anthropic (reference):** minors are allowed if the organization adds age verification, content moderation, monitoring and reporting, a child-safety system prompt, and discloses that users are talking to an AI [8].

## D2 — Data use on the free tier

- **Groq:** "not permitted to use Inputs or Outputs for training"; does not retain them "except as necessary to provide the Cloud Services" [9].
- **Cloudflare:** "does not use Customer Content processed by Workers AI to train AI models" and does not retain inputs or outputs after the request, unless the developer turns on AI Gateway logging [21].
- **Mistral:** free mode "may use your data (input and output) to train" by default; opt-out in Admin > Privacy > "Anonymous improvement data" [3][4]. Labs/Preview models always train, with no opt-out [2].
- **OpenRouter:** "Some Models may store or train on your Inputs"; an account setting stops routing to providers that train, with separate settings for free and paid models [14][16].
- **Gemini (cut):** free-tier content is used to "improve, and develop" products and may be read by human reviewers [1].

## D3 — EU/EEA and data processing agreements

- **Groq:** EEA customers contract with Groq UK Limited; the DPA is incorporated by reference and accepted online, which implies it covers self-serve accounts, but Groq's service-specific terms tie DPA processing to "Designated Models" — **disputed** [9][10]. Processing in the US and "various global jurisdictions" [13].
- **Cloudflare:** DPA v6.4 is part of the self-serve agreement, but does not mention free plans; EEA transfers rely on EU SCCs or the EU–US Data Privacy Framework; no EU-only inference option found (unverified) [25][26].
- **Mistral:** Paris-based; the DPA is listed "For Commercial Customers" and states neither free-plan coverage nor hosting location (unverified) [5].
- **OpenRouter:** US servers under SCCs; EU in-region processing only on Business/Enterprise plans [15][16].

## D4 — Free limits and structured output

| Provider | Free allowance | Throughput | Structured output |
|---|---|---|---|
| Groq | ~1,000 requests/day per model (unverified for the free plan) [11] | ~30 RPM (unverified) [11] | Strict `json_schema` on gpt-oss-20b/120b and Qwen; JSON object mode on all models [12] |
| Cloudflare | 10,000 neurons/day ≈ 360 (Llama 3.1 8B) or 180 (Llama 3.3 70B) events of ~500 in / 200 out tokens [20] | 300 RPM for text generation [23] | `json_schema` on Llama 3.1 8B and 3.3 70B; not guaranteed, no streaming [22] |
| Mistral | ~1B tokens/month (unverified, search snippet) [31] | ~1 request/second (unverified) [31] | Not verified (docs 404) |
| OpenRouter | 50 requests/day (1,000 after buying 10 credits) [17] | 20 RPM [17] | Varies per upstream model (not checked) |

The Cloudflare request estimates are the assistant's own arithmetic from published neuron rates; the token assumption per event is the main uncertainty. With 20–30 real choices per playthrough, 180–360 events/day covers roughly 6–15 full playthroughs per day — enough for a playtest of 10–20 people over several days, tight on a single day.

## Decision matrix

Scores 1–5; weights from the requirements frame. Re-weight freely.

| Criterion (weight) | Groq | Cloudflare | Mistral | OpenRouter |
|---|---|---|---|---|
| No training on inputs (25) | 5 | 5 | 3 | 3 |
| EU processing / DPA on free tier (20) | 3 | 2 | 4 | 2 |
| Free limits sufficient (20) | 3 (unverified) | 4 | 3 (unverified) | 1 |
| Structured JSON output (20) | 5 | 4 | 2 (unverified) | 2 |
| Terms clear for minors (15) | 4 | 3 | 2 (consent duty) | 2 |
| **Weighted total (max 500)** | **405** | **370** | **285** | **205** |

- **Pick: Groq**, conditional on confirming the free-plan limits in the Groq console when the account is created (a five-minute check).
- **Runner-up: Cloudflare Workers AI.** It wins if Groq's free limits turn out low, or if the team prefers the provider with no minors clause at all and verified limits.
- **Mistral** wins only if EU processing becomes a hard requirement; the price is a parental-consent flow for under-18 players.
- **Strongest argument against the pick:** Groq's free-plan limits and DPA coverage are the two least-verified cells in its column, and its terms were last updated 2026-06-22 (slightly stale).
- **Cheapest hedge:** put the LLM behind a small provider adapter in the Python backend, so swapping Groq ↔ Cloudflare is a configuration change; the pre-written event library remains the fallback either way.

## Cross-dimension insights

- **Data minimisation does the privacy work that free tiers do not.** No finalist gives a confirmed free-tier DPA plus EU processing (D3), but all finalists' risk falls sharply if the request holds no personal data (D2). This turns the addendum's "structured AI output" principle into an architecture constraint: send only game-state parameters, never user IDs, email or free text.
- **Account-holder age and end-user age are different rules.** Groq, OpenRouter and Gemini require an 18+ account holder; only Gemini also bans under-18 end users. A student team of adults can hold the account; the question is what the terms say about players.
- **Free-tier wording moves fast.** GitHub Models disappeared, Hugging Face removed free credits, Cerebras became a trial, and Gemini moved free limits out of its public docs — all within 2026 [27][28][18][32]. The provider choice should be re-checked right before stage 2 starts.

## Contrary evidence

The red-team pass did not run (`red_team = off`). The strongest counter-evidence found is that Groq's DPA coverage is disputed between its DPA and its service-specific terms [10], and that Cloudflare's separate Acceptable Use Policy was not read, so a minors clause there cannot be ruled out.

## Recommendations

1. **Remove Gemini from the candidate list** in `architecture_technical_design.md` and the brief's constraints section (architecture constraint). Confidence: high — clauses verified twice on the primary page [1].
2. **Choose Groq as the primary stage-2 provider, with Cloudflare Workers AI as the named fallback**, behind a provider adapter (architecture decision / PRD non-functional requirement). Confidence: medium — Groq's free limits unverified [11].
3. **Add a PRD requirement: the LLM request contains no personal data** — game-state parameters only, no user identifiers, no player free text (PRD NFR; supports addendum principles 1–2). Confidence: high that it reduces exposure; it does not by itself settle GDPR processor questions.
4. **Adopt Anthropic's minors checklist as good practice whatever the provider**: AI disclosure to the player, moderation before display, monitoring of flagged output (PRD NFR, AI safety section) [8]. Confidence: high that the checklist exists; it is not legally binding for other providers.
5. **Before stage 2: read Groq's free-plan limits in the console, and Cloudflare's Acceptable Use Policy** (open questions below).

## Open questions

- **Groq free-plan rate limits** — the tab did not render. Answer: create the account and read the console limits page.
- **Groq DPA vs. "Designated Models"** — which applies to free accounts? Answer: ask Groq support or read the service-specific terms in full.
- **Cloudflare Acceptable Use Policy** — any minors clause? Answer: read cloudflare.com/website-terms/acceptable-use (not fetched).
- **Mistral JSON mode and hosting location** — docs returned 404. Answer: Mistral docs search or Trust Center.
- **What counts as "legally adequate consent" for 15–17-year-olds in Norway** — relevant only if Mistral is chosen; links to the separate privacy research topic (item 5 in the topic list).

## Source appendix

| # | Claim / finding it supports | Publisher | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|
| [1] | Gemini under-18 ban (all tiers); EEA paid-only; free-tier data use | [Google — Gemini API Additional Terms](https://ai.google.dev/gemini-api/terms) | 2026-04-28 | 2026-10-27 | high |
| [2] | Mistral minors require parental consent; Labs models train | [Mistral AI — Commercial Terms](https://legal.mistral.ai/terms/commercial-terms-of-service) | 2026-09-25 | 2026-10-27 | high |
| [3] | Mistral free mode may train on inputs/outputs | [Mistral AI — Help 347617](https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models) | undated | 2026-10-27 | high |
| [4] | Mistral training opt-out procedure | [Mistral AI — Help 455207](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) | 2026-09-03 | 2026-10-27 | high |
| [5] | Mistral DPA scope; hosting not stated | [Mistral AI — DPA](https://legal.mistral.ai/terms/data-processing-addendum) | 2026-07-27 | 2026-10-27 | medium |
| [8] | Anthropic safeguards for organizations serving minors | [Anthropic — Guidelines for organizations serving minors](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors) | 2026-03-16 | 2026-10-27 | high |
| [9] | Groq 18+ account holder; §6.3 customer responsibility; no training; Groq UK for EEA | [Groq — Services Agreement](https://console.groq.com/docs/legal/services-agreement) | 2026-06-22 | 2026-10-27 | high |
| [10] | Groq DPA accepted online; coverage disputed | [Groq — Customer DPA](https://console.groq.com/docs/legal/customer-data-processing-addendum) | 2025-10-15 | 2026-10-27 | low (disputed) |
| [11] | Groq rate limits (Developer plan seen; free unverified) | [Groq — Rate limits](https://console.groq.com/docs/rate-limits) | undated | 2026-10-27 | low |
| [12] | Groq strict JSON schema on gpt-oss/Qwen | [Groq — Structured outputs](https://console.groq.com/docs/structured-outputs) | undated | 2026-10-27 | high |
| [13] | Groq processing in US and global jurisdictions | [Groq — Privacy policy](https://groq.com/privacy-policy) | 2025-11-12 | 2026-10-27 | medium |
| [14] | OpenRouter 18+; models may train; customer end users | [OpenRouter — Terms](https://openrouter.ai/terms) | 2026-08-31 | 2026-10-27 | high |
| [15] | OpenRouter US servers, SCCs | [OpenRouter — Privacy](https://openrouter.ai/privacy) | 2026-08-31 | 2026-10-27 | medium |
| [16] | OpenRouter training opt-out routing; EU region Business/Enterprise only | [OpenRouter — Privacy and logging](https://openrouter.ai/docs/features/privacy-and-logging) | undated | 2026-10-27 | high |
| [17] | OpenRouter free limits 20 RPM, 50 RPD | [OpenRouter — Limits](https://openrouter.ai/docs/api/reference/limits) | undated | 2026-10-27 | high |
| [18] | Cerebras one-time USD 5 credit, 30 days | [Cerebras — Pricing](https://www.cerebras.ai/pricing) | undated | 2026-10-27 | high |
| [20] | Cloudflare 10,000 neurons/day; neuron rates | [Cloudflare — Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) | 2026-10-20 | 2026-10-27 | high |
| [21] | Cloudflare no training, no retention | [Cloudflare — Workers AI data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/) | 2026-10-16 | 2026-10-27 | high |
| [22] | Cloudflare JSON mode with json_schema | [Cloudflare — JSON mode](https://developers.cloudflare.com/workers-ai/features/json-mode/) | 2026-09-14 | 2026-10-27 | high |
| [23] | Cloudflare 300 RPM text generation | [Cloudflare — Workers AI limits](https://developers.cloudflare.com/workers-ai/platform/limits/) | undated | 2026-10-27 | high |
| [24] | Cloudflare no minors clause; model AUPs apply | [Cloudflare — Developer Platform service-specific terms](https://www.cloudflare.com/service-specific-terms-developer-platform/) | 2026-09-28 | 2026-10-27 | medium |
| [25] | Cloudflare self-serve agreement: no age clause, DPA reference | [Cloudflare — Self-Serve Subscription Agreement](https://www.cloudflare.com/terms/) | 2025-09-12 | 2026-10-27 | medium |
| [26] | Cloudflare DPA v6.4: SCCs/DPF, free plans not mentioned | [Cloudflare — Customer DPA](https://www.cloudflare.com/cloudflare-customer-dpa/) | 2026-04-03 | 2026-10-27 | medium |
| [27] | Hugging Face: no free inference credits | [Hugging Face — Inference Providers pricing](https://huggingface.co/docs/inference-providers/pricing) | undated | 2026-10-27 | high |
| [28] | GitHub Models retired 2026-07-30 | [GitHub — Changelog](https://github.blog/changelog/2026-07-30-github-models-is-now-retired/) | 2026-07-30 | 2026-10-27 | high |
| [29] | Llama 3.3 AUP: no end-user age minimum | [Meta — Llama 3.3 Acceptable Use Policy](https://dev.meta.ai/llama/llama3_3/use-policy) | undated | 2026-10-27 | high |
| [31] | Mistral free limits ~1 RPS / 1B tokens/month | [Mistral AI — Help 225174 (search snippet; page 404)](https://help.mistral.ai/en/articles/225174-what-are-the-limits-of-the-free-tier) | undated | 2026-10-27 | low |
| [32] | Gemini free-tier limits moved to AI Studio | [Google — Gemini rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) | 2026-10-26 | 2026-10-27 | high |

## Staleness map

Computed with `recon_kit.py staleness` (windows: terms and data-use 3 months, limits 1 month — AI-adjacent).

| Claim | Class | Published | Re-check by | Stale |
|---|---|---|---|---|
| Anthropic minors guidelines [8] | terms | 2026-03-16 | 2026-06-16 | yes |
| Gemini under-18 ban; EEA paid-only [1] | terms | 2026-04-28 | 2026-07-28 | yes (re-read live today, unchanged) |
| Groq 18+ / §6.3 / no training [9] | terms | 2026-06-22 | 2026-09-22 | yes (re-read live today) |
| Cloudflare 10k neurons/day, 300 RPM [20][23] | limits | 2026-10-20 | 2026-11-20 | no |
| Groq free-plan limits [11] | limits | 2026-10-27 | 2026-11-27 | no |
| OpenRouter 50 RPD [17] | limits | 2026-10-27 | 2026-11-27 | no |
| Mistral free mode trains, opt-out [3][4] | data-use | 2026-09-03 | 2026-12-03 | no |
| Mistral parental-consent clause [2] | terms | 2026-09-25 | 2026-12-25 | no |
| Cloudflare no minors clause [24] | terms | 2026-09-28 | 2026-12-28 | no |
| Cloudflare no training/retention [21] | data-use | 2026-10-16 | 2027-01-16 | no |

The three "stale" rows are flagged by page date, not content; all three pages were read live on 2026-10-27. The limits rows go stale first (from **2026-11-20**). As a selection report, this should be refreshed before stage 2 starts, and in any case within two quarters.
