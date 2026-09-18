# Catalog details

Generated from [data/use-cases.json](../data/use-cases.json). The [README](../README.md) is the browseable list; this page keeps actions, caveats, and sources.

Evidence badges match the README legend. Readiness values are catalog labels, not product grades.

Updated 2026-09-17.

## Action-taking projects

### [Jev Ultrafast browser agent](https://github.com/browser-use/jev-ultrafast)
<!-- catalog:jev-ultrafast -->

Maintained by [Browser Use](https://github.com/browser-use).

Uses Jev to pick the next browser operation and target from an indexed DOM; a small LLM only types text.

- Action / outcome: Drives Chrome through a local inspector. The README documents a Google Flights search example. It does not book flights.
- Jev's role: Choice of operation plus speculative target questions in one request
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/browser-use/jev-ultrafast#try-it
- Demo: https://github.com/browser-use/jev-ultrafast/blob/main/docs/demo.mp4
- Caveat: Timing and cost claims in the README were not remeasured. Jev is text-only; the page is serialized to text/DOM, not pixels.

### [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario)
<!-- catalog:typesafe-mario -->

By [@fhshaik](https://github.com/fhshaik).

Uses Jev to choose NES controller macros from emulator RAM JSON, not screenshots.

- Action / outcome: Local play loop writes run JSONL. A dashboard shows action distribution.
- Jev's role: Choice over legal controller actions
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/fhshaik/typesafe-mario#setup
- Caveat: The ROM is not in the repo. Interactive demo, not a shipped product. No native vision.

### [TypeSafe Computer Use](https://github.com/awlevin/typesafe-computer-use)
<!-- catalog:typesafe-computer-use -->

By [Aaron Levin](https://github.com/awlevin).

OCRs a Mac screen, then Jev chooses the next UI action and the code clicks.

- Action / outcome: Local screenshot → OCR → Choice/Noul → OS action loop.
- Jev's role: Action selection on OCR text state
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/awlevin/typesafe-computer-use
- Caveat: Not native vision. Per-step cost in the GitHub description is an author claim.

### [Jev Review](https://github.com/devagrawal09/jev-review)
<!-- catalog:jev-review -->

By [Dev Agrawal](https://github.com/devagrawal09).

Runs staged Jev judgments over git diffs or a local codebase and shows them on a dashboard.

- Action / outcome: JSON reports plus a dashboard on 127.0.0.1:4317. Does not publish reviews remotely.
- Jev's role: Noul risk matrix, Choice/Score file profiles, evidence selection, severity routing
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/devagrawal09/jev-review#quick-start
- Caveat: Developer tool, not a hosted CI product. Thresholds are code policy.

### [pg-jev](https://github.com/realZachi/pg-jev)
<!-- catalog:pg-jev -->

By [@realZachi](https://github.com/realZachi).

PostgreSQL helpers that filter, sort, or classify rows with Jev.

- Action / outcome: SQL helpers call TypeSafe. Rows that match a Noul, Choice, or Score filter are returned by the database.
- Jev's role: Batched parallel Noul/Choice/Score per row
- Origin: community · Evidence: `code-inspected` · Readiness: installable-from-source
- Install / start: https://github.com/realZachi/pg-jev#install
- Caveat: Needs untrusted plpython3u / superuser. Row text is sent to TypeSafe. Latency numbers in the README were not re-run.

### [jevql](https://github.com/kylemclaren/jevql)
<!-- catalog:jevql -->

By [Kyle McLaren](https://github.com/kylemclaren).

psql-shaped CLI and Go/TS/Python SDKs that add jev(), jev_prob, jev_choice, and jev_score to plain SQL on a vanilla Postgres with no extension.

- Action / outcome: Runs the plain SQL on the server, sends the surviving rows to Jev in batches, caches answers, and applies the filter, sort, or group in the client.
- Jev's role: Batched Noul/Choice/Score per surviving row
- Origin: community · Evidence: `author-claim` · Readiness: runnable-from-readme
- Install / start: https://github.com/kylemclaren/jevql#install
- Demo: https://jevql.fly.dev
- Caveat: Every row that survives the SQL filters is sent to TypeSafe and judged, so put cheap predicates in SQL first. Author-submitted; no independent code inspection yet.

### [pi-warden](https://github.com/DevMortimer/pi-warden)
<!-- catalog:pi-warden -->

By [Ryan Joshua](https://github.com/DevMortimer).

Asks Jev whether a Pi agent tool call is irreversible or off-task before it runs.

- Action / outcome: Steers or blocks Pi tool calls. Published as a pi.dev package.
- Jev's role: Judgments on proposed tool calls, stuck loops, unverified done claims
- Origin: community · Evidence: `demo-inspected` · Readiness: installable
- Install / start: https://pi.dev/packages/pi-warden
- Caveat: Did not re-run against a live Pi session.

### [Foreman](https://github.com/thruwire/foreman)
<!-- catalog:foreman -->

Maintained by [ThruWire](https://github.com/thruwire).

Uses the official Python SDK so a software-factory supervisor can judge worker steps.

- Action / outcome: Semantic supervision of coding workers (per README/description).
- Jev's role: Noul/judgments via AsyncTypeSafeClient
- Origin: community · Evidence: `code-inspected` · Readiness: inspect-further
- Install / start: https://github.com/thruwire/foreman
- Caveat: Full README walkthrough was partial; grounded on import evidence and description.

### [beadsort](https://github.com/harrymunro/beadsort)
<!-- catalog:beadsort -->

By [Harry Munro](https://github.com/harrymunro).

Uses Jev to label beads issues from their text.

- Action / outcome: Writes labels onto beads items from issue text.
- Jev's role: Classification / labeling Choice or Noul over issue state
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/harrymunro/beadsort
- Caveat: 0 stars at check time; launch-week. Source tree not fully walked in this sweep.

### [JEVMETER](https://github.com/ChetasLua/jevmeter)
<!-- catalog:jevmeter -->

By [Chetas Lua](https://github.com/ChetasLua).

Scores transcript sentences with Jev, then renders an edited video.

- Action / outcome: CLI wizard writes a .jevmeter.mp4.
- Jev's role: Per-sentence scoring after transcription
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/ChetasLua/jevmeter
- Caveat: Audio is transcribed then scored as text. Jev is not a native audio model. Accuracy badges are author claims.

### [blink](https://github.com/ellipsis-dev/blink)
<!-- catalog:blink-code-search -->

Maintained by [ellipsis.dev](https://github.com/ellipsis-dev).

Walks the filesystem and uses Jev to score which files match a natural-language query.

- Action / outcome: CLI table of paths with percentages.
- Jev's role: Relevance scoring of candidate files
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/ellipsis-dev/blink
- Caveat: Prototype search, not an index. May issue many parallel Jev calls.

### [neo4jev](https://github.com/jexp/neo4jev)
<!-- catalog:neo4jev -->

By [Michael Hunger](https://github.com/jexp).

Walks a Neo4j graph by asking Jev which neighboring relationship to follow.

- Action / outcome: Graph navigation demo: classifier over edge types / neighbors.
- Jev's role: Choice over neighboring relationships
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/jexp/neo4jev
- Caveat: Small demo (6 stars). README not fully re-read in the owner pass.

### [semdecide](https://github.com/sharziki/semdecide)
<!-- catalog:semdecide -->

By [Sharvil Saxena](https://github.com/sharziki).

Turns Jev judgments into Unix pipeline exit codes or JSON.

- Action / outcome: CLI exit codes / JSON from Jev judgments on stdin or files.
- Jev's role: Native judgments on user-supplied text
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/sharziki/semdecide
- Caveat: Small project. Do not treat as a standard library.

## Model and skill routing

### [jev-router](https://github.com/gargpratyush/jev-router)
<!-- catalog:jev-router -->

By [Pratyush Garg](https://github.com/gargpratyush).

Uses Jev to pick a model for each Claude Code or Codex request.

- Action / outcome: jev-claude / jev-codex launch real upstream CLIs with a routed model.
- Jev's role: Per-turn difficulty / model Choice
- Origin: community · Evidence: `code-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/gargpratyush/jev-router
- Caveat: README uses JEV_API_KEY, not TYPESAFE_API_KEY. npm registry page was not separately opened.

### [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router)
<!-- catalog:jev-codex-router -->

By [@0xNatoshi](https://github.com/0xNatoshi).

Classifies each Codex Router turn with Jev, then code picks model, effort, and tier.

- Action / outcome: Local jev_server.py with fail-open and a JSONL decision log.
- Jev's role: Turn classification plus routing policy in code
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/0xNatoshi/jev-codex-router
- Caveat: Backtest savings are author-measured. Fail-open means a Jev outage does not block coding.

### [SkillRanker](https://github.com/Dicklesworthstone/skillranker)
<!-- catalog:skillranker -->

By [Jeff Emanuel](https://github.com/Dicklesworthstone).

Ranks which agent skill fits the next step from live session context.

- Action / outcome: sr demo (offline fixtures) or sr rank --allow-network; optional Claude Code hook.
- Jev's role: Skill ranking with abstention
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/Dicklesworthstone/skillranker
- Caveat: Offline demo is fixtures. Live ranking needs a TypeSafe key.

### [Official skill-suggestion cookbook](https://docs.typesafe.ai/cookbooks/skill_suggestion)
<!-- catalog:cookbook-skill-suggestion -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Two Jev requests rank 182 Hermes skills and may suggest none.

- Action / outcome: suggest() returns at most one skill name for the agent system prompt. Published table: wrong-skill loads 16.8% → 7.3% on a pinned Haiku run (author numbers).
- Jev's role: Choice over the roster plus Nouls for whether a skill is needed
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/cookbooks/skill_suggestion.md
- Demo: https://docs.typesafe.ai/cookbooks/skill_suggestion
- Caveat: Numbers are TypeSafe's published eval, not reproduced here. Not a drop-in Hermes skill.

### [Jev Agent Skill Router](https://github.com/GodsBoy/jev-agent-skill-router)
<!-- catalog:jev-agent-skill-router -->

By [Dewaldt Huysamen](https://github.com/GodsBoy).

Routes over a skill catalogue with Jev Choice and Noul gates; it does not load the skills.

- Action / outcome: Returns a routing decision with call evidence. Does not load or execute skills. Author-recorded synthetic 72-case run versus a lexical baseline.
- Jev's role: Parallel Choice over catalogue batches; final Choice plus need, review, and per-candidate fit Nouls; Python applies thresholds
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/GodsBoy/jev-agent-skill-router#install-and-verify
- Caveat: Native x_search named this repo without a status citation; GitHub independently inspected. Benchmark is 24 synthetic skills / 72 requests, not a live Hermes catalogue. CLI name jev-router collides with gargpratyush/jev-router. 3 stars. Accuracy numbers are author-recorded, not re-run here.

## Email and inbox routing

### [Jev email intent workflow](https://github.com/GiesN/typesafe-jev-workflow)
<!-- catalog:email-jev-langgraph -->

By [@GiesN](https://github.com/GiesN).

LangGraph demo that classifies mocked emails as invoice or general with Jev.

- Action / outcome: Prints intent, probabilities, and destination vs expected label. Does not send mail or pay invoices.
- Jev's role: Choice over two intents
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/GiesN/typesafe-jev-workflow
- Caveat: Smoke demo on 10 emails. Closest public analog to inbox triage; not a Hermes skill.

## MCP and agent bridges

### [Jev MCP (jkudish)](https://github.com/jkudish/jev-mcp)
<!-- catalog:jev-mcp -->

By [Joey Kudish](https://github.com/jkudish).

MCP tools that verify claims, screen content, and rank candidates with Jev.

- Action / outcome: An MCP host receives typed verdicts from Jev.
- Jev's role: Native judgments via TypeSafe API
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/jkudish/jev-mcp
- Caveat: Proof of concept. Several launch-week MCP clones exist; this is the one with inspected README. Author-claim catch examples.

### [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)
<!-- catalog:typesafe-mcp -->

By [@itsmostafa](https://github.com/itsmostafa).

Community MCP that exposes TypeSafe System One to Claude or Codex.

- Action / outcome: Agent tools call Jev; the host still executes side effects.
- Jev's role: Native API behind MCP tools
- Origin: community · Evidence: `demo-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/itsmostafa/typesafe-mcp
- Caveat: Not the official skill. Distinct from jkudish/jev-mcp and y0usaf/typesafe-mcp.

### [y0usaf/typesafe-mcp](https://github.com/y0usaf/typesafe-mcp)
<!-- catalog:y0usaf-typesafe-mcp -->

By [Sami Ansari](https://github.com/y0usaf). Announced by [@realy0usaf](https://x.com/realy0usaf).

One MCP evaluate(state, questions) tool that POSTs to the TypeSafe API.

- Action / outcome: Host POSTs to api.typesafe.ai/v1/systemone; the agent still executes side effects.
- Jev's role: Native System One API behind a single MCP tool
- Origin: community · Evidence: `code-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/y0usaf/typesafe-mcp#install
- Caveat: Launch-week MCP. Distinct from itsmostafa/typesafe-mcp and jkudish/jev-mcp. 3 stars. Not official.

## Official cookbooks and patterns

### [Official function-calling cookbook](https://docs.typesafe.ai/cookbooks/function_calling)
<!-- catalog:cookbook-function-calling -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Maps a natural-language trading request onto typed functions and closed-set arguments.

- Action / outcome: Dispatcher returns a function name plus Literal arguments with confidence; ordinary Python functions run.
- Jev's role: Choice over tools and closed-set args; Nouls for whether an arg was stated
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/cookbooks/function_calling.md
- Demo: https://docs.typesafe.ai/cookbooks/function_calling
- Caveat: Uses cached cookbook results unless you delete json_cache.json. Example domain is market data plots, not live brokerage.

### [Official LLM guardrails cookbook](https://docs.typesafe.ai/cookbooks/llm_guardrails)
<!-- catalog:cookbook-guardrails -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Screens an LLM input or output for hazards, then code chooses pass, review, block, or support.

- Action / outcome: guard() returns a policy action. Does not send the user message itself.
- Jev's role: Nouls per hazard plus a harm Score
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/cookbooks/llm_guardrails.md
- Demo: https://docs.typesafe.ai/cookbooks/llm_guardrails
- Caveat: Thresholds are yours. Cached published run unless you go live.

### [Official citation-check cookbook](https://docs.typesafe.ai/cookbooks/citation_check)
<!-- catalog:cookbook-citation-check -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Checks whether a quote's context supports a claim.

- Action / outcome: Choice plus confidence can flag a citation for human review.
- Jev's role: Choice: supports / does not support / uncertain
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/cookbooks/citation_check.md
- Demo: https://docs.typesafe.ai/cookbooks/citation_check
- Caveat: Cookbook page listed in the official index; not fully re-read beyond the index blurb in this owner pass.

### [Official intent-routing pattern](https://docs.typesafe.ai/patterns/intent-routing)
<!-- catalog:pattern-intent-routing -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Classifies a request, then code routes to deterministic logic, a specialist LLM, or a human.

- Action / outcome: Example ticket router uses intent Choice and complexity Score with confidence gates.
- Jev's role: Intent Choice and complexity Score
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/patterns/intent-routing.md
- Demo: https://docs.typesafe.ai/patterns/intent-routing
- Caveat: Pattern, not a packaged product.

## Official SDKs and adapter

### [TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python)
<!-- catalog:official-sdk-python -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Official Python client for POST /v1/systemone.

- Action / outcome: TypeSafeClient.system_one returns typed Choice/Noul/Score answers for your code to branch on.
- Jev's role: Native System One model behind the SDK
- Origin: official · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://pypi.org/project/typesafe-sdk/
- Caveat: Needs TYPESAFE_API_KEY. Text-only API.

### [TypeSafe JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js)
<!-- catalog:official-sdk-js -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Official TypeScript/JavaScript client with inferred answer types.

- Action / outcome: examples/demo.ts classifies a billing ticket with noul/choice/score.
- Jev's role: Native
- Origin: official · Evidence: `demo-inspected` · Readiness: installable
- Install / start: https://www.npmjs.com/package/@typesafe-ai/sdk
- Demo: https://github.com/typesafe-ai/typesafe-sdk-js/blob/main/examples/demo.ts
- Caveat: Live demo needs TYPESAFE_API_KEY.

### [System One Adapter (Python)](https://github.com/typesafe-ai/system-one-adapter-python)
<!-- catalog:official-system-one-adapter -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Drop-in TypeSafeClient.system_one backed by OpenAI or Anthropic instead of Jev.

- Action / outcome: Same typed questions; LLM structured output for A/B comparison.
- Jev's role: None (LLM stand-in)
- Origin: official · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://pypi.org/project/system-one-adapter/
- Caveat: Explicitly not Jev. Cassette tests block network by default.

## Official docs, skill, and launch demos

### [TypeSafe documentation](https://docs.typesafe.ai/llms.txt)
<!-- catalog:official-docs -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Live docs for the System One model, primitives, API, cookbooks, and demos.

- Action / outcome: Source of truth for contracts. llms.txt indexes every page.
- Jev's role: Documents Jev as jev-latest / text-only
- Origin: official · Evidence: `documented-example` · Readiness: docs
- Install / start: https://docs.typesafe.ai/introduction/quickstart.md
- Demo: https://docs.typesafe.ai/llms.txt
- Caveat: Mintlify .md paths. cookbooks.md URL served a specific cookbook, not an index, in this sweep.

### [Official TypeSafe agent skill](https://github.com/typesafe-ai/skills)
<!-- catalog:official-skills -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

SKILL.md that teaches agents to design System One workflows from the live docs.

- Action / outcome: Agent writes SDK code; the skill itself does not call Jev.
- Jev's role: Design-time guidance
- Origin: official · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://docs.typesafe.ai/agent-skill#installation
- Caveat: Not an inference wrapper. Keep live docs as source of truth.

### [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
<!-- catalog:official-launch-blog -->

By Diogo Almeida. Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Launch post (2026-09-15) covering RLCD, pricing, workflow evals, and Doom and Wikipedia-race videos.

- Action / outcome: Documents launch demos where game/page state is text/JSON and code issues actions.
- Jev's role: Judgments inside a harness; code owns the controller / browser
- Origin: official · Evidence: `author-claim` · Readiness: documented-launch
- Demo: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- Caveat: Doom/Wiki harnesses are not in the public typesafe-ai GitHub org. Speed/cost/eval charts are vendor-published, not remeasured. HN discussion: https://news.ycombinator.com/item?id=49717558

### [Smart home assistant demo](https://docs.typesafe.ai/demos/smart-home)
<!-- catalog:demo-smart-home -->

Maintained by [TypeSafe AI](https://github.com/typesafe-ai).

Official demo that evaluates smart-home requests with speculative questions and an LLM fallback.

- Action / outcome: Demo code decides device intents; Loom walkthrough. Not a physical home integration in the public org.
- Jev's role: Speculative questions over a user request
- Origin: official · Evidence: `documented-example` · Readiness: documented-example
- Install / start: https://docs.typesafe.ai/demos/smart-home.md
- Demo: https://docs.typesafe.ai/demos/smart-home
- Caveat: Did not download the Loom. Distinguish from production home automation.

## Platform integrations

### [Vercel AI Gateway + AI SDK evaluate](https://ai-sdk.dev/docs/ai-sdk-core/evaluation)
<!-- catalog:vercel-ai-gateway-jev -->

Maintained by [Vercel](https://github.com/vercel).

Jev as typesafe-ai/jev on AI Gateway, plus AI SDK 7 experimental_evaluate.

- Action / outcome: evaluate() returns typed answers; example routes a support case. ZDR/no-training flags documented.
- Jev's role: Native evaluation model via Gateway
- Origin: platform · Evidence: `documented-example` · Readiness: installable
- Install / start: https://vercel.com/ai-gateway/models/jev
- Demo: https://ai-sdk.dev/docs/ai-sdk-core/evaluation
- Caveat: API is experimental. TypeSafe workflow-eval multipliers in the changelog are vendor-attributed.

## Community clients

### [ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe)
<!-- catalog:ruby-llm-typesafe -->

By [Kieran Klaassen](https://github.com/kieranklaassen).

TypeSafe structured-output provider for RubyLLM 2.

- Action / outcome: Ruby apps can ask System One questions through RubyLLM.
- Jev's role: Native via TypeSafe API
- Origin: community · Evidence: `demo-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/kieranklaassen/ruby_llm-typesafe
- Caveat: Unofficial. Small star count.

### [TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net)
<!-- catalog:typesafeai-net -->

By [@Hawxy](https://github.com/Hawxy).

Unofficial .NET SDK for TypeSafe AI.

- Action / outcome: .NET clients call System One.
- Jev's role: Native via TypeSafe API
- Origin: community · Evidence: `demo-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/Hawxy/TypeSafeAI.Net
- Caveat: Unofficial. Older TypeSafe.Sdk URL is dead.

## Installable agent skills

### [building-with-jev skill](https://github.com/dbreunig/building-with-jev-skill)
<!-- catalog:building-with-jev-skill -->

By [Drew Breunig](https://github.com/dbreunig).

Community skill for writing Jev programs (Claude plugin and skills.sh).

- Action / outcome: Guides question design; does not execute Jev unless the agent writes code.
- Jev's role: Design-time
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/dbreunig/building-with-jev-skill
- Caveat: Overlaps the official typesafe-ai skill.

### [jev-axi](https://github.com/shiftynick/jev-axi)
<!-- catalog:jev-axi -->

By [Nicholas Underwood](https://github.com/shiftynick).

CLI and skill for log triage, diff review, untrusted-text screening, and ranking.

- Action / outcome: Shell commands return probabilities; hooks can block commands.
- Jev's role: Narrow judgments on user-supplied text
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/shiftynick/jev-axi
- Caveat: Latency/cost sentences in the skill body are author claims. Fails closed if the key is missing.

### [advocaat](https://github.com/pithings/advocaat)
<!-- catalog:advocaat -->

Maintained by [PiThings](https://github.com/pithings).

Small TypeScript ask() client plus an agent skill over Jev.

- Action / outcome: Typed answers under question keys in one request.
- Jev's role: Native
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/pithings/advocaat
- Caveat: Wrapper, not a new model.

## Other awesome-Jev lists

### [awesome-jev-by-typesafe (Anil-matcha)](https://github.com/Anil-matcha/awesome-jev-by-typesafe)
<!-- catalog:list-anil-matcha -->

By [Anil Chandra Naidu Matcha](https://github.com/Anil-matcha).

Independent Jev list with examples and prompts (highest star count among lists in this sweep).

- Action / outcome: Curation plus examples/python and examples/typescript.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Vendor latency/price cited from TypeSafe docs. Neighboring sibling lists by the same author are not Jev-only.

### [awesome-typesafe (AbdelStark)](https://github.com/AbdelStark/awesome-typesafe)
<!-- catalog:list-abdelstark -->

By [@AbdelStark](https://github.com/AbdelStark).

Official plus community directory with an independent disclaimer.

- Action / outcome: List plus GitHub Pages site.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Demo: https://abdelstark.github.io/awesome-typesafe/
- Caveat: Name collides with unrelated TypeScript 'typesafe' lists.

### [awesome-jev (yibie)](https://github.com/yibie/awesome-jev)
<!-- catalog:list-yibie -->

By [@yibie](https://github.com/yibie).

Category field guide that requires actual Jev use.

- Action / outcome: Per-category markdown files.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Smaller than auto-generated directories; inclusion criteria are stricter.

### [awesome-jev (AnotiaWang)](https://github.com/AnotiaWang/awesome-jev)
<!-- catalog:list-anotia -->

By [Andy Wang](https://github.com/AnotiaWang).

Bilingual EN/ZH awesome list (CC0).

- Action / outcome: Curation across SDKs, apps, cookbooks.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Launch-week overlap with other lists.

### [awesome-jev (hellogumbo)](https://github.com/hellogumbo/awesome-jev)
<!-- catalog:list-hellogumbo -->

Maintained by [GUMBO](https://github.com/hellogumbo).

Directory claiming hundreds of entries, plus awesomejev.com.

- Action / outcome: Broad directory. Treat claimed counts as catalog size, not unique production apps.
- Jev's role: n/a (list)
- Origin: community · Evidence: `author-claim` · Readiness: list
- Demo: https://awesomejev.com
- Caveat: Largest claimed entry count in this sweep. Many items are thin wrappers. Not treated as verified unique apps.

### [awesome-jev (rhc98)](https://github.com/rhc98/awesome-jev)
<!-- catalog:list-rhc98 -->

By [@rhc98](https://github.com/rhc98).

Auto-judged catalog: README says Jev curated the list.

- Action / outcome: Listed repos according to a Jev policy, not a human review.
- Jev's role: Inclusion classifier (meta)
- Origin: community · Evidence: `author-claim` · Readiness: list
- Demo: https://awesome-jev.xyz
- Caveat: Do not copy wholesale. Inclusion is a model output.

## Related, not TypeSafe Jev

### [OpenJev](https://github.com/TheoLeeCJ/openjev)
<!-- catalog:openjev -->

By [Theodore Lee](https://github.com/TheoLeeCJ).

Community open-weight attempt at the System One shape. Not api.typesafe.ai.

- Action / outcome: Local model / site. Not official Jev.
- Jev's role: none (reproduction)
- Origin: related · Evidence: `author-claim` · Readiness: related-not-jev-api
- Demo: https://openjev.com
- Caveat: Not TypeSafe Jev. Do not list as an official integration.

### [jevlike](https://github.com/vinnylarouge/jevlike)
<!-- catalog:jevlike -->

By [@vinnylarouge](https://github.com/vinnylarouge).

Another community reproduction of the System One interface.

- Action / outcome: Local analog, not the TypeSafe API.
- Jev's role: none (reproduction)
- Origin: related · Evidence: `author-claim` · Readiness: related-not-jev-api
- Caveat: Not official Jev. Listed only so people do not confuse it with TypeSafe.

### [jevmlx](https://github.com/bnsd55/jevmlx)
<!-- catalog:jevmlx -->

By [@bnsd55](https://github.com/bnsd55).

Jev-style parallel constrained decisions for MLX models on Apple Silicon.

- Action / outcome: Local MLX forward pass, not TypeSafe weights.
- Jev's role: none (local analog)
- Origin: related · Evidence: `demo-inspected` · Readiness: related-not-jev-api
- Caveat: Not Jev weights. Useful as an offline comparison, not a TypeSafe client.

