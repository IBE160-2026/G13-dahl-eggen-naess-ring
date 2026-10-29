# Digest: providers C, round 1, agent 1 (Cloudflare Workers AI, Hugging Face Inference Providers, GitHub Models)

Accessed 2026-10-27. Format: claim | source URL | publisher | pub_date / last-updated | accessed | confidence | class.
Quotes were extracted with WebFetch, so the wording may be lightly paraphrased by the fetch summariser. Check them against the live page before quoting them in a final document.

## Cloudflare Workers AI

- D4: The free allocation is "10,000 Neurons per day at no charge" and resets daily at 00:00 UTC. The page gives no purpose (prototyping or anything else) beyond letting anyone use the service without paying. | https://developers.cloudflare.com/workers-ai/platform/pricing/ | Cloudflare | last updated 2026-10-20 | accessed 2026-10-27 | high | limits
- D4: Rates: `@cf/meta/llama-3.1-8b-instruct` costs 25,608 neurons per M input tokens and 75,147 per M output tokens. `@cf/meta/llama-3.3-70b-instruct-fp8-fast` costs 26,668 per M input and 204,805 per M output. | same as above | Cloudflare | 2026-10-20 | accessed 2026-10-27 | high | limits
- D4 (my own arithmetic, assuming about 500 input and 200 output tokens per event): 8B costs about 28 neurons per request, so roughly 360 requests/day. 70B costs about 54 neurons per request, so roughly 180 requests/day. | derived from pricing page | — | — | accessed 2026-10-27 | medium (depends on the token assumption) | limits
- D4: JSON Mode supports `response_format` with `json_object` or `json_schema` on Llama 3.1 8B and Llama 3.3 70B fp8-fast, among other models. Caveats: output is not guaranteed to comply (the error is "JSON Mode couldn't be met"), and streaming is not supported. | https://developers.cloudflare.com/workers-ai/features/json-mode/ | Cloudflare | last updated 2026-09-14 | accessed 2026-10-27 | high | limits
- D2: "Cloudflare does not use Customer Content processed by Workers AI to train AI models." "Cloudflare does not retain inputs or outputs after they are no longer needed to process the request." Content is stored only if the customer enables AI Gateway logging or caching, or writes it to their own logs. | https://developers.cloudflare.com/workers-ai/platform/data-usage/ | Cloudflare | last updated 2026-10-16 | accessed 2026-10-27 | high | data-use
- D1: The Self-Serve Subscription Agreement (the governing contract for self-serve and free plans) sets no minimum age and does not mention minors, an age threshold or COPPA. The only capacity language: "representing to Cloudflare that you have the authority to bind such Entity to this Agreement." It incorporates Service-Specific Terms by reference; I did not read those. | https://www.cloudflare.com/terms/ | Cloudflare | last updated 2025-09-12 (older than 3 months) | accessed 2026-10-27 | medium (Service-Specific Terms and the AUP not checked) | terms
- D1: The Website and Online Services Terms (which do not govern subscription products) have no age clause either. The only related text says the services are "not intended to be technology protection measures" for COPPA/CIPA purposes. | https://www.cloudflare.com/website-terms/ | Cloudflare | effective 2025-08-01 (older than 3 months) | accessed 2026-10-27 | medium | terms
- D2/D3: Free services: "We will have no liability for any harm or damage arising out of or in connection with any Free Services" (Self-Serve Agreement §2.6). Under §6.1, where Customer Content includes Personal Data, "Cloudflare will handle such Personal Data in compliance with Cloudflare's" DPA. The agreement does not limit the DPA to paid plans. | https://www.cloudflare.com/terms/ | Cloudflare | 2025-09-12 | accessed 2026-10-27 | medium | terms
- D3: The Customer DPA is v6.4, effective 2026-04-03. It is part of the Main Agreement, which includes the Self-Serve Subscription Agreement, and takes effect from "the date on which Customer signed or the parties otherwise agreed to this DPA". It does not mention free plans specifically. EEA transfers use the EU SCCs (Modules 2/3, cl. 6.2(a)) or the EU-US Data Privacy Framework (cl. 6.4). | https://www.cloudflare.com/cloudflare-customer-dpa/ | Cloudflare | effective 2026-04-03 | accessed 2026-10-27 | medium | region
- D3: The Self-Serve Agreement makes no data-residency commitment. An EU Data Act Addendum applies to customers with an EU billing address. Norway is in the EEA, not the EU, so whether it applies there is unclear. | https://www.cloudflare.com/terms/ | Cloudflare | 2025-09-12 | accessed 2026-10-27 | medium | region

## Hugging Face Inference Providers

- D4 (key finding): Free accounts get no monthly credits. The account table reads: "Free Users | None | - | yes (credits purchase required)". PRO users get $2.00/month and Team/Enterprise $2.00 per seat. "Free users can use Inference Providers by purchasing credits, or by upgrading to PRO." So there is currently no zero-cost runtime path. | https://huggingface.co/docs/inference-providers/pricing | Hugging Face | no date shown (contains a 2026-09 API example, so recent) | accessed 2026-10-27 | high | limits
- D4: hf-inference (formerly "Inference API (serverless)") "focuses mostly on CPU inference" as of July 2025 and is billed by compute time once included credits run out. It is not a free path for 8–70B LLMs. | same as above | Hugging Face | — | accessed 2026-10-27 | high | limits
- D1: "you must be a natural person of at least age 13, or a legal entity duly registered." There is no other clause on minors or on services aimed at under-18s. Inference Providers may fall under "Supplemental Terms", which I did not read. | https://huggingface.co/terms-of-service | Hugging Face | effective 2022-09-15 (older than 3 months) | accessed 2026-10-27 | medium | terms
- D2: "Hugging Face does not store any user data for training purposes. We do not store the request body or response when routing requests through Hugging Face. Logs are kept for debugging purposes for up to 30 days, but no user data or tokens are stored." It also says "please refer to the Data Security Policies of each provider", so the third-party provider's own retention policy applies. | https://huggingface.co/docs/inference-providers/security | Hugging Face | no date shown | accessed 2026-10-27 | high (HF side), low (provider side) | data-use
- D3: The ToS has no DPA reference. The security page mentions SOC2 Type 2 but makes no EU-region statement. | https://huggingface.co/terms-of-service ; https://huggingface.co/docs/inference-providers/security | Hugging Face | — | accessed 2026-10-27 | low | region

## GitHub Models

- All dimensions (key finding): "As of July 30, 2026, GitHub Models has been fully retired." "The playground, model catalog, inference API, and bring your own key (BYOK) are no longer available to any customer." GitHub points to Azure AI / Microsoft Foundry and Copilot instead. | https://docs.github.com/en/github-models/use-github-models/prototyping-with-ai-models | GitHub | no date shown | accessed 2026-10-27 | high | limits
- The timeline is confirmed by the changelog: closed to new customers on 2026-06-16, retirement announced 2026-07-01, retired 2026-07-30. | https://github.blog/changelog/2026-07-30-github-models-is-now-retired/ ; https://github.blog/changelog/2026-06-16-github-models-is-no-longer-available-to-new-customers | GitHub | 2026-06-16 / 2026-07-30 | accessed 2026-10-27 (search result snippets, pages not fetched) | high | limits
- D1 (GitHub account only, now moot for Models): "A User must be at least 13 years of age." "we do not permit any Users under 13 on our Service." "your country's minimum age may be older". | https://docs.github.com/en/site-policy/github-terms/github-terms-of-service | GitHub | effective 2026-04-27 | accessed 2026-10-27 | high | terms
- D2/D3/D4: Not applicable, because the service no longer exists.

## Underlying open-weight model policies (D1)

- Gemma Prohibited Use Policy: the only clause touching minors is §2.1, "Promoting or generating content related to child sexual abuse or exploitation;". There is no restriction on serving users under 18. | https://ai.google.dev/gemma/prohibited_use_policy | Google | policy last modified 2024-02-21, page updated 2024-08-05 (stale, older than 3 months) | accessed 2026-10-27 | high | terms
- Llama 3.3 AUP: not retrieved. llama.com/llama3_3/use-policy/ returns a 301 redirect to https://developer.meta.com/ai/llama3_3/use-policy/, which I did not fetch because of the tool budget. Unverified belief (training data only, not evidence): the Llama AUP prohibits exploitation or harm of children and CSAM, and has no ban on apps used by minors. | — | Meta | — | accessed 2026-10-27 (redirect only) | low | terms
- Mistral/Qwen (Apache-2.0): not checked this run.

## Leads worth chasing

- Fetch https://developer.meta.com/ai/llama3_3/use-policy/ and quote its child-related clauses, plus the Llama 3.1/3.3 license's 700M-MAU clause and its attribution requirement.
- Cloudflare Service-Specific Terms (Workers AI / Developer Platform section) and the Cloudflare Acceptable Use Policy: check for any AI or minors clauses.
- Cloudflare: does the DPA bind free self-serve accounts automatically (a dashboard click-through)? Also Workers AI processing location and whether the Data Localization Suite (believed to be Enterprise-only, unverified) covers Workers AI.
- Cloudflare Workers AI rate limits page (requests per minute per task type), developers.cloudflare.com/workers-ai/platform/limits/.
- Hugging Face Privacy Policy and any DPA (huggingface.co/privacy). Retention policies of the specific third-party providers (Together, Fireworks, Groq, and others).
- HF ZeroGPU Spaces quota as a possible free alternative path (it is a different product).
- Microsoft Foundry free tier as the successor to GitHub Models (out of scope for this run).

## Looked for but not found

- Any minor or under-18 clause in Cloudflare's self-serve terms or website terms: none found.
- A free-tier credit for HF Inference Providers: the table explicitly shows "None".
- A Cloudflare free-tier statement of "prototyping only": none found.
- An HF Inference Providers EU region or DPA statement: none found in the ToS or on the security page.
- GitHub Models rate limits and production terms: the pages are gone and the service is retired.
