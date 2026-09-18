# Awesome Jev

<img src="assets/mark.svg" alt="" width="48" height="48" align="left" />

**A researched list of useful things built with [Jev](https://typesafe.ai/), TypeSafe AI's System One model.**
Typed judgments in, software actions out. Unofficial. Not affiliated with TypeSafe AI.

<br clear="all" />

[![CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![catalog](https://img.shields.io/badge/catalog-45_entries-111.svg)](data/use-cases.json)
[![updated](https://img.shields.io/badge/updated-2026.09.17-0a0.svg)](docs/research-method.md)

Jev does not chat, write code, or see images. It returns Choice / Score / Noul answers with probabilities. **Your code** decides and acts. This list prefers projects that actually route, click, review, query, or gate something — then includes the rest of the useful ecosystem.

## Contents

| Section | Count |
| --- | ---: |
| [Action-taking projects](#action-taking-projects) | 12 |
| [Model and skill routing](#model-and-skill-routing) | 4 |
| [Email and inbox routing](#email-and-inbox-routing) | 1 |
| [MCP and agent bridges](#mcp-and-agent-bridges) | 2 |
| [Official cookbooks and patterns](#official-cookbooks-and-patterns) | 4 |
| [Official SDKs and adapter](#official-sdks-and-adapter) | 3 |
| [Official docs, skill, and launch demos](#official-docs-skill-and-launch-demos) | 4 |
| [Platform integrations](#platform-integrations) | 1 |
| [Community clients](#community-clients) | 2 |
| [Installable agent skills](#installable-agent-skills) | 3 |
| [Other awesome-Jev lists](#other-awesome-jev-lists) | 6 |
| [Related, not TypeSafe Jev](#related-not-typesafe-jev) | 3 |

## Highlights (inspected action)

1. [Jev Ultrafast browser agent](https://github.com/browser-use/jev-ultrafast) — Indexed DOM action space: Jev picks the operation and target; a small LLM only types text. (`demo-inspected`)
1. [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) — Jev chooses NES controller macros from structured emulator RAM JSON, not screenshots. (`code-inspected`)
1. [TypeSafe Computer Use](https://github.com/awlevin/typesafe-computer-use) — OCR a Mac screen, then Jev chooses the next UI action and code clicks. (`code-inspected`)
1. [Jev Review](https://github.com/devagrawal09/jev-review) — Staged Jev judgments over git diffs or a codebase, with a local dashboard. (`code-inspected`)
1. [pg-jev](https://github.com/realZachi/pg-jev) — PostgreSQL extension: natural-language WHERE / ORDER / classify via Jev over row composites. (`code-inspected`)
1. [pi-warden](https://github.com/DevMortimer/pi-warden) — Guardrails for the Pi coding agent: Jev judges irreversible or off-task tool calls before they run. (`demo-inspected`)
1. [jev-router](https://github.com/gargpratyush/jev-router) — Wraps Claude Code / Codex CLIs; Jev picks cheap vs strong model per user turn. (`code-inspected`)
1. [Official skill-suggestion cookbook](https://docs.typesafe.ai/cookbooks/skill_suggestion) — Two Jev requests rank 182 Hermes skills and may suggest none. (`documented-example`)
1. [Official function-calling cookbook](https://docs.typesafe.ai/cookbooks/function_calling) — Map a natural-language trading request onto typed functions and closed-set arguments. (`documented-example`)
1. [Vercel AI Gateway + AI SDK evaluate](https://ai-sdk.dev/docs/ai-sdk-core/evaluation) — Jev available as typesafe-ai/jev on AI Gateway; AI SDK 7 experimental_evaluate. (`documented-example`)

Vendor speed/cost charts are **not** remeasured here. Treat launch-week latency and “N users” claims as marketing unless a source is marked inspected.

## Evidence legend

| Badge | Meaning |
| --- | --- |
| `code-inspected` | README plus relevant source or example files were read |
| `demo-inspected` | A documented demo, cookbook run, or live page was inspected |
| `documented-example` | Official docs/cookbook/changelog |
| `author-claim` | Author or press described it; implementation not fully inspected |
| `proposed` | Not built; see [skill opportunities](docs/skill-opportunities.md) |

## Quick start (official)

1. Docs index: [docs.typesafe.ai/llms.txt](https://docs.typesafe.ai/llms.txt)
2. Python: `uv add typesafe-sdk` · JS: `npm install @typesafe-ai/sdk` (need `TYPESAFE_API_KEY`)
3. Agent skill: `npx skills add typesafe-ai/skills --skill typesafe-ai` or Claude Code plugin `typesafe@typesafe-ai`
4. HTTP: `POST https://api.typesafe.ai/v1/systemone`

Also: [research method](docs/research-method.md) · [skill opportunities](docs/skill-opportunities.md) · [unbuilt ideas](docs/ideas.md)

## Action-taking projects
### [Jev Ultrafast browser agent](https://github.com/browser-use/jev-ultrafast)
<!-- catalog:jev-ultrafast -->

Indexed DOM action space: Jev picks the operation and target; a small LLM only types text.

- Action / outcome: Drives Chrome through a local inspector; README documents a Google Flights search example. Does not book flights.
- Jev's role: Choice of operation plus speculative target questions in one request
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/browser-use/jev-ultrafast#try-it
- Demo: https://github.com/browser-use/jev-ultrafast/blob/main/docs/demo.mp4
- Caveat: Timing/cost claims in the README were not remeasured. Jev is text-only; the page is serialized to text/DOM, not pixels.

### [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario)
<!-- catalog:typesafe-mario -->

Jev chooses NES controller macros from structured emulator RAM JSON, not screenshots.

- Action / outcome: Local play loop writes run JSONL; dashboard shows action distribution.
- Jev's role: Choice over legal controller actions
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/fhshaik/typesafe-mario#setup
- Caveat: ROM is not in the repo. Interactive demo, not a shipped product. No native vision.

### [TypeSafe Computer Use](https://github.com/awlevin/typesafe-computer-use)
<!-- catalog:typesafe-computer-use -->

OCR a Mac screen, then Jev chooses the next UI action and code clicks.

- Action / outcome: Local screenshot → OCR → Choice/Noul → OS action loop.
- Jev's role: Action selection on OCR text state
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/awlevin/typesafe-computer-use
- Caveat: Not native vision. Per-step cost in the GitHub description is an author claim.

### [Jev Review](https://github.com/devagrawal09/jev-review)
<!-- catalog:jev-review -->

Staged Jev judgments over git diffs or a codebase, with a local dashboard.

- Action / outcome: JSON reports plus dashboard on 127.0.0.1:4317. Does not publish reviews remotely.
- Jev's role: Noul risk matrix, Choice/Score file profiles, evidence selection, severity routing
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/devagrawal09/jev-review#quick-start
- Caveat: Developer tool, not a hosted CI product. Thresholds are code policy.

### [pg-jev](https://github.com/realZachi/pg-jev)
<!-- catalog:pg-jev -->

PostgreSQL extension: natural-language WHERE / ORDER / classify via Jev over row composites.

- Action / outcome: SQL helpers call TypeSafe; rows that match a Noul/Choice/Score filter are returned by the database.
- Jev's role: Batched parallel Noul/Choice/Score per row
- Origin: community · Evidence: `code-inspected` · Readiness: installable-from-source
- Install / start: https://github.com/realZachi/pg-jev#install
- Caveat: Needs untrusted plpython3u / superuser. Row text is sent to TypeSafe. Latency numbers in README not re-run.

### [pi-warden](https://github.com/DevMortimer/pi-warden)
<!-- catalog:pi-warden -->

Guardrails for the Pi coding agent: Jev judges irreversible or off-task tool calls before they run.

- Action / outcome: Steers or blocks Pi tool calls; published as a pi.dev package.
- Jev's role: Judgments on proposed tool calls, stuck loops, unverified done claims
- Origin: community · Evidence: `demo-inspected` · Readiness: installable
- Install / start: https://pi.dev/packages/pi-warden
- Caveat: Did not re-run against a live Pi session.

### [Foreman](https://github.com/thruwire/foreman)
<!-- catalog:foreman -->

Software-factory supervisor that uses the official Python SDK to judge worker steps.

- Action / outcome: Semantic supervision of coding workers (per README/description).
- Jev's role: Noul/judgments via AsyncTypeSafeClient
- Origin: community · Evidence: `code-inspected` · Readiness: inspect-further
- Install / start: https://github.com/thruwire/foreman
- Caveat: Full README walkthrough was partial; grounded on import evidence and description.

### [beadsort](https://github.com/harrymunro/beadsort)
<!-- catalog:beadsort -->

Jev labels beads issues: typed, calibrated backlog labels.

- Action / outcome: Writes labels onto beads items from issue text.
- Jev's role: Classification / labeling Choice or Noul over issue state
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/harrymunro/beadsort
- Caveat: 0 stars at check time; launch-week. Source tree not fully walked in this sweep.

### [JEVMETER](https://github.com/ChetasLua/jevmeter)
<!-- catalog:jevmeter -->

Score transcript sentences on debate/earnings/podcast presets, then render an edited video.

- Action / outcome: CLI wizard writes a .jevmeter.mp4.
- Jev's role: Per-sentence scoring after transcription
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/ChetasLua/jevmeter
- Caveat: Audio is transcribed then scored as text. Jev is not a native audio model. Accuracy badges are author claims.

### [blink](https://github.com/ellipsis-dev/blink)
<!-- catalog:blink-code-search -->

Filesystem walkers plus Jev scoring of which files match a natural-language query.

- Action / outcome: CLI table of paths with percentages.
- Jev's role: Relevance scoring of candidate files
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/ellipsis-dev/blink
- Caveat: Prototype search, not an index. May issue many parallel Jev calls.

### [neo4jev](https://github.com/jexp/neo4jev)
<!-- catalog:neo4jev -->

Walk a Neo4j graph by classifying neighboring relationships with Jev.

- Action / outcome: Graph navigation demo: classifier over edge types / neighbors.
- Jev's role: Choice over neighboring relationships
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/jexp/neo4jev
- Caveat: Small demo (6 stars). README not fully re-read in the owner pass.

### [semdecide](https://github.com/sharziki/semdecide)
<!-- catalog:semdecide -->

Typed semantic decisions for Unix pipelines and CI.

- Action / outcome: CLI exit codes / JSON from Jev judgments on stdin or files.
- Jev's role: Native judgments on user-supplied text
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/sharziki/semdecide
- Caveat: Small project. Do not treat as a standard library.

## Model and skill routing
### [jev-router](https://github.com/gargpratyush/jev-router)
<!-- catalog:jev-router -->

Wraps Claude Code / Codex CLIs; Jev picks cheap vs strong model per user turn.

- Action / outcome: jev-claude / jev-codex launch real upstream CLIs with a routed model.
- Jev's role: Per-turn difficulty / model Choice
- Origin: community · Evidence: `code-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/gargpratyush/jev-router
- Caveat: README uses JEV_API_KEY, not TYPESAFE_API_KEY. npm registry page was not separately opened.

### [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router)
<!-- catalog:jev-codex-router -->

Plugs into Codex Router: Jev classifies the turn, then code picks model/effort/tier.

- Action / outcome: Local jev_server.py with fail-open and a JSONL decision log.
- Jev's role: Turn classification plus routing policy in code
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/0xNatoshi/jev-codex-router
- Caveat: Backtest savings are author-measured. Fail-open means a Jev outage does not block coding.

### [SkillRanker](https://github.com/Dicklesworthstone/skillranker)
<!-- catalog:skillranker -->

Rust CLI ranks which agent skill fits the next step from live session context.

- Action / outcome: sr demo (offline fixtures) or sr rank --allow-network; optional Claude Code hook.
- Jev's role: Skill ranking with abstention
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/Dicklesworthstone/skillranker
- Caveat: Offline demo is fixtures. Live ranking needs a TypeSafe key.

### [Official skill-suggestion cookbook](https://docs.typesafe.ai/cookbooks/skill_suggestion)
<!-- catalog:cookbook-skill-suggestion -->

Two Jev requests rank 182 Hermes skills and may suggest none.

- Action / outcome: suggest() returns at most one skill name for the agent system prompt. Published table: wrong-skill loads 16.8% → 7.3% on a pinned Haiku run (author numbers).
- Jev's role: Choice over the roster plus Nouls for whether a skill is needed
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/cookbooks/skill_suggestion.md
- Demo: https://docs.typesafe.ai/cookbooks/skill_suggestion
- Caveat: Numbers are TypeSafe's published eval, not reproduced here. Not a drop-in Hermes skill.

## Email and inbox routing
### [Jev email intent workflow](https://github.com/GiesN/typesafe-jev-workflow)
<!-- catalog:email-jev-langgraph -->

LangGraph demo: Jev Choice invoice vs general on mocked emails.

- Action / outcome: Prints intent, probabilities, and destination vs expected label. Does not send mail or pay invoices.
- Jev's role: Choice over two intents
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/GiesN/typesafe-jev-workflow
- Caveat: Smoke demo on 10 emails. Closest public analog to inbox triage; not a Hermes skill.

## MCP and agent bridges
### [Jev MCP (jkudish)](https://github.com/jkudish/jev-mcp)
<!-- catalog:jev-mcp -->

MCP tools: verify claims, screen content, rank candidates.

- Action / outcome: An MCP host receives typed verdicts from Jev.
- Jev's role: Native judgments via TypeSafe API
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/jkudish/jev-mcp
- Caveat: Proof of concept. Several launch-week MCP clones exist; this is the one with inspected README. Author-claim catch examples.

### [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)
<!-- catalog:typesafe-mcp -->

Community MCP exposing TypeSafe System One to Claude / Codex.

- Action / outcome: Agent tools call Jev; host still executes side effects.
- Jev's role: Native API behind MCP tools
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/itsmostafa/typesafe-mcp
- Caveat: Not the official skill. Distinct from jkudish/jev-mcp.

## Official cookbooks and patterns
### [Official function-calling cookbook](https://docs.typesafe.ai/cookbooks/function_calling)
<!-- catalog:cookbook-function-calling -->

Map a natural-language trading request onto typed functions and closed-set arguments.

- Action / outcome: Dispatcher returns a function name plus Literal arguments with confidence; ordinary Python functions run.
- Jev's role: Choice over tools and closed-set args; Nouls for whether an arg was stated
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/cookbooks/function_calling.md
- Demo: https://docs.typesafe.ai/cookbooks/function_calling
- Caveat: Uses cached cookbook results unless you delete json_cache.json. Example domain is market data plots, not live brokerage.

### [Official LLM guardrails cookbook](https://docs.typesafe.ai/cookbooks/llm_guardrails)
<!-- catalog:cookbook-guardrails -->

One TypeSafe request screens an LLM input or output for hazards, then code routes pass/review/block/support.

- Action / outcome: guard() returns a policy action. Does not send the user message itself.
- Jev's role: Nouls per hazard plus a harm Score
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/cookbooks/llm_guardrails.md
- Demo: https://docs.typesafe.ai/cookbooks/llm_guardrails
- Caveat: Thresholds are yours. Cached published run unless you go live.

### [Official citation-check cookbook](https://docs.typesafe.ai/cookbooks/citation_check)
<!-- catalog:cookbook-citation-check -->

Check whether a quote's context supports a claim.

- Action / outcome: Choice plus confidence can flag a citation for human review.
- Jev's role: Choice: supports / does not support / uncertain
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/cookbooks/citation_check.md
- Demo: https://docs.typesafe.ai/cookbooks/citation_check
- Caveat: Cookbook page listed in the official index; not fully re-read beyond the index blurb in this owner pass.

### [Official intent-routing pattern](https://docs.typesafe.ai/patterns/intent-routing)
<!-- catalog:pattern-intent-routing -->

Classify a request, then code routes to deterministic logic, a specialist LLM, or a human.

- Action / outcome: Example ticket router uses intent Choice and complexity Score with confidence gates.
- Jev's role: Intent Choice and complexity Score
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/patterns/intent-routing.md
- Demo: https://docs.typesafe.ai/patterns/intent-routing
- Caveat: Pattern, not a packaged product.

## Official SDKs and adapter
### [TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python)
<!-- catalog:official-sdk-python -->

Official sync/async client for POST /v1/systemone.

- Action / outcome: TypeSafeClient.system_one returns typed Choice/Noul/Score answers for your code to branch on.
- Jev's role: Native System One model behind the SDK
- Origin: official · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://pypi.org/project/typesafe-sdk/
- Caveat: Needs TYPESAFE_API_KEY. Text-only API.

### [TypeSafe JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js)
<!-- catalog:official-sdk-js -->

Official TypeScript/JavaScript client with inferred answer types.

- Action / outcome: examples/demo.ts classifies a billing ticket with noul/choice/score.
- Jev's role: Native
- Origin: official · Evidence: `demo-inspected` · Readiness: installable
- Install / start: https://www.npmjs.com/package/@typesafe-ai/sdk
- Demo: https://github.com/typesafe-ai/typesafe-sdk-js/blob/main/examples/demo.ts
- Caveat: Live demo needs TYPESAFE_API_KEY.

### [System One Adapter (Python)](https://github.com/typesafe-ai/system-one-adapter-python)
<!-- catalog:official-system-one-adapter -->

Drop-in TypeSafeClient.system_one backed by OpenAI/Anthropic instead of Jev.

- Action / outcome: Same typed questions; LLM structured output for A/B comparison.
- Jev's role: None (LLM stand-in)
- Origin: official · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://pypi.org/project/system-one-adapter/
- Caveat: Explicitly not Jev. Cassette tests block network by default.

## Official docs, skill, and launch demos
### [TypeSafe documentation](https://docs.typesafe.ai/llms.txt)
<!-- catalog:official-docs -->

Live docs: System One programming model, primitives, API, cookbooks, demos.

- Action / outcome: Source of truth for contracts. llms.txt indexes every page.
- Jev's role: Documents Jev as jev-latest / text-only
- Origin: official · Evidence: `documented-example` · Readiness: docs
- Install / start: https://docs.typesafe.ai/introduction/quickstart.md
- Demo: https://docs.typesafe.ai/llms.txt
- Caveat: Mintlify .md paths. cookbooks.md URL served a specific cookbook, not an index, in this sweep.

### [Official TypeSafe agent skill](https://github.com/typesafe-ai/skills)
<!-- catalog:official-skills -->

SKILL.md teaching agents to design System One workflows from live docs.

- Action / outcome: Agent writes SDK code; the skill itself does not call Jev.
- Jev's role: Design-time guidance
- Origin: official · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://docs.typesafe.ai/agent-skill#installation
- Caveat: Not an inference wrapper. Keep live docs as source of truth.

### [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
<!-- catalog:official-launch-blog -->

Launch post (2026-09-15): RLCD, pricing, workflow evals, Doom and Wikipedia-race videos.

- Action / outcome: Documents launch demos where game/page state is text/JSON and code issues actions.
- Jev's role: Judgments inside a harness; code owns the controller / browser
- Origin: official · Evidence: `author-claim` · Readiness: documented-launch
- Demo: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- Caveat: Doom/Wiki harnesses are not in the public typesafe-ai GitHub org. Speed/cost/eval charts are vendor-published, not remeasured. HN discussion: https://news.ycombinator.com/item?id=49717558

### [Smart home assistant demo](https://docs.typesafe.ai/demos/smart-home)
<!-- catalog:demo-smart-home -->

Official demo: evaluate smart-home requests with speculative questions and LLM fallback.

- Action / outcome: Demo code decides device intents; Loom walkthrough. Not a physical home integration in the public org.
- Jev's role: Speculative questions over a user request
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/demos/smart-home.md
- Demo: https://docs.typesafe.ai/demos/smart-home
- Caveat: Did not download the Loom. Distinguish from production home automation.

## Platform integrations
### [Vercel AI Gateway + AI SDK evaluate](https://ai-sdk.dev/docs/ai-sdk-core/evaluation)
<!-- catalog:vercel-ai-gateway-jev -->

Jev available as typesafe-ai/jev on AI Gateway; AI SDK 7 experimental_evaluate.

- Action / outcome: evaluate() returns typed answers; example routes a support case. ZDR/no-training flags documented.
- Jev's role: Native evaluation model via Gateway
- Origin: platform · Evidence: `documented-example` · Readiness: installable
- Install / start: https://vercel.com/ai-gateway/models/jev
- Demo: https://ai-sdk.dev/docs/ai-sdk-core/evaluation
- Caveat: API is experimental. TypeSafe workflow-eval multipliers in the changelog are vendor-attributed.

## Community clients
### [ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe)
<!-- catalog:ruby-llm-typesafe -->

TypeSafe structured-output provider for RubyLLM 2.

- Action / outcome: Ruby apps can ask System One questions through RubyLLM.
- Jev's role: Native via TypeSafe API
- Origin: community · Evidence: `demo-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/kieranklaassen/ruby_llm-typesafe
- Caveat: Unofficial. Small star count.

### [TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net)
<!-- catalog:typesafeai-net -->

Unofficial .NET SDK for TypeSafe AI.

- Action / outcome: .NET clients call System One.
- Jev's role: Native via TypeSafe API
- Origin: community · Evidence: `demo-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/Hawxy/TypeSafeAI.Net
- Caveat: Unofficial. Older TypeSafe.Sdk URL is dead.

## Installable agent skills
### [building-with-jev skill](https://github.com/dbreunig/building-with-jev-skill)
<!-- catalog:building-with-jev-skill -->

Community skill for writing Jev programs (Claude plugin + skills.sh).

- Action / outcome: Guides question design; does not execute Jev unless the agent writes code.
- Jev's role: Design-time
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/dbreunig/building-with-jev-skill
- Caveat: Overlaps the official typesafe-ai skill.

### [jev-axi](https://github.com/shiftynick/jev-axi)
<!-- catalog:jev-axi -->

CLI + skill for log triage, diff review, untrusted-text screen, ranking.

- Action / outcome: Shell commands return probabilities; hooks can block commands.
- Jev's role: Narrow judgments on user-supplied text
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/shiftynick/jev-axi
- Caveat: Latency/cost sentences in the skill body are author claims. Fails closed if the key is missing.

### [advocaat](https://github.com/pithings/advocaat)
<!-- catalog:advocaat -->

Small TypeScript ask() client plus an agent skill over Jev.

- Action / outcome: Typed answers under question keys in one request.
- Jev's role: Native
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/pithings/advocaat
- Caveat: Wrapper, not a new model.

## Other awesome-Jev lists
### [awesome-jev-by-typesafe (Anil-matcha)](https://github.com/Anil-matcha/awesome-jev-by-typesafe)
<!-- catalog:list-anil-matcha -->

Largest-star independent Jev list with examples and prompts.

- Action / outcome: Curation plus examples/python and examples/typescript.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Vendor latency/price cited from TypeSafe docs. Neighboring sibling lists by the same author are not Jev-only.

### [awesome-typesafe (AbdelStark)](https://github.com/AbdelStark/awesome-typesafe)
<!-- catalog:list-abdelstark -->

Structured official + community directory with an independent disclaimer.

- Action / outcome: List + GitHub Pages site.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Demo: https://abdelstark.github.io/awesome-typesafe/
- Caveat: Name collides with unrelated TypeScript 'typesafe' lists.

### [awesome-jev (yibie)](https://github.com/yibie/awesome-jev)
<!-- catalog:list-yibie -->

Category field guide that requires actual Jev use.

- Action / outcome: Per-category markdown files.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Smaller than auto-generated directories; inclusion criteria are stricter.

### [awesome-jev (AnotiaWang)](https://github.com/AnotiaWang/awesome-jev)
<!-- catalog:list-anotia -->

Bilingual EN/ZH awesome list (CC0).

- Action / outcome: Curation across SDKs, apps, cookbooks.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Launch-week overlap with other lists.

### [awesome-jev (hellogumbo)](https://github.com/hellogumbo/awesome-jev)
<!-- catalog:list-hellogumbo -->

Directory claiming hundreds of entries plus awesomejev.com.

- Action / outcome: Broad directory. Treat claimed counts as catalog size, not unique production apps.
- Jev's role: n/a (list)
- Origin: community · Evidence: `author-claim` · Readiness: list
- Demo: https://awesomejev.com
- Caveat: Largest claimed entry count in this sweep. Many items are thin wrappers. Not treated as verified unique apps.

### [awesome-jev (rhc98)](https://github.com/rhc98/awesome-jev)
<!-- catalog:list-rhc98 -->

Auto-judged catalog: README says Jev curated the list.

- Action / outcome: Listed repos according to a Jev policy, not a human review.
- Jev's role: Inclusion classifier (meta)
- Origin: community · Evidence: `author-claim` · Readiness: list
- Demo: https://awesome-jev.xyz
- Caveat: Do not copy wholesale. Inclusion is a model output.

## Related, not TypeSafe Jev
### [OpenJev](https://github.com/TheoLeeCJ/openjev)
<!-- catalog:openjev -->

Community open-weight attempt at the System One shape. Not api.typesafe.ai.

- Action / outcome: Local model / site. Not official Jev.
- Jev's role: none (reproduction)
- Origin: related · Evidence: `author-claim` · Readiness: related-not-jev-api
- Demo: https://openjev.com
- Caveat: Not TypeSafe Jev. Do not list as an official integration.

### [jevlike](https://github.com/vinnylarouge/jevlike)
<!-- catalog:jevlike -->

Another community reproduction of the System One interface.

- Action / outcome: Local analog, not the TypeSafe API.
- Jev's role: none (reproduction)
- Origin: related · Evidence: `author-claim` · Readiness: related-not-jev-api
- Caveat: Not official Jev. Listed only so people do not confuse it with TypeSafe.

### [jevmlx](https://github.com/bnsd55/jevmlx)
<!-- catalog:jevmlx -->

Jev-style parallel constrained decisions for MLX models on Apple Silicon.

- Action / outcome: Local MLX forward pass, not TypeSafe weights.
- Jev's role: none (local analog)
- Origin: related · Evidence: `demo-inspected` · Readiness: related-not-jev-api
- Caveat: Not Jev weights. Useful as an offline comparison, not a TypeSafe client.


## What this list adds

Launch week produced several [awesome-jev](#other-awesome-jev-lists) directories, including auto-judged catalogs that claim hundreds of repos. This one is smaller on purpose:

- Exhaustive public `typesafe-ai` org inventory (10 repos, 4 product, 3 supporting, 3 unrelated forks)
- Evidence badges and a machine-readable catalog generated into this README
- Action-taking projects near the top, not SDK clones
- Honest gaps: no native X search, no Google SERP, no TypeSafe inference in this sweep
- Explicit [skill opportunities](docs/skill-opportunities.md) for email triage and model routing (no fake drop-in skills)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs need a public source and an evidence level. Run `python3 scripts/validate.py`.

## License

Original curation is [CC BY 4.0](LICENSE). Upstream code and docs keep their own licenses. TypeSafe, Jev, and System One are marks of TypeSafe AI.

Updated 2026-09-17.
