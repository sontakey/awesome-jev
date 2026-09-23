# Catalog details

Generated from [data/use-cases.json](../data/use-cases.json). The [README](../README.md) is the browseable list; this page keeps actions, caveats, and sources.

Evidence badges match the README legend. Readiness values are catalog labels, not product grades.

Updated 2026-09-19.

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

### [Jev Search](https://github.com/superagents-lab/jev-search)
<!-- catalog:jev-search -->

Maintained by [SuperAgents Lab](https://github.com/superagents-lab).

Uses Jev to choose search sources and time ranges from a plain-language request, then rank the returned results.

- Action / outcome: Streams ranked links and snippets with visible relevance scores and editable source filters. It returns no generated answer text.
- Jev's role: Typed request-understanding judgments plus per-result relevance scoring
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/superagents-lab/jev-search#local-development
- Caveat: Independent project, not an official TypeSafe product. Needs both a Jev provider key and a Search1API key. Engine coverage and provider fallbacks vary per request.

### [Jev for social media](https://github.com/socai-io/jev-social)
<!-- catalog:jev-social -->

Maintained by [socai-io](https://github.com/socai-io).

Uses Jev to choose the next read-only social media operation from a changing list of concrete targets.

- Action / outcome: Runs socai CLI commands in a real Chrome session and returns cards, a table, and an evidence report. Read-only; it does not post.
- Jev's role: Choice of platform and of the next operation, re-asked after each observed result
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/socai-io/jev-social
- Demo: https://socai-io.github.io/jev-social/
- Caveat: Drives your own logged-in browser session against third-party sites; check each platform's terms before running. The README GIF shows an earlier routing-only prototype.

### [jev-trader](https://github.com/jarrodwatts/jev-trader)
<!-- catalog:jev-trader -->

By [Jarrod Watts](https://github.com/jarrodwatts).

Uses Jev to answer buy or sell on every Monad block and posts a matching post-only limit order.

- Action / outcome: Watches the Kuru MON-USDC order book, asks Jev for a direction roughly every 300 ms, and replaces a post-only limit order one tick inside the touch. Runs dry (real book, simulated fills) with no private key set.
- Jev's role: Per-block choice of buy or sell with probabilities over a short horizon
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/jarrodwatts/jev-trader#run
- Demo: https://jev-trader-production.up.railway.app
- Caveat: A demo, not trading advice. The default model is a mock heuristic; Jev requires MODEL=jev and a key. Published PnL and latency numbers were not reproduced here, and live mode posts real on-chain orders.

### [Jev-cu](https://github.com/Sac-Y/Jev-cu)
<!-- catalog:jev-cu -->

By [@Sac-Y](https://github.com/Sac-Y).

Uses Jev to pick the next computer-use element and action from text candidates while a local policy gate blocks sensitive operations.

- Action / outcome: Ships a Codex-installable skill plus scripts that run the decision loop over accessibility snapshots. Codex reads and executes the screen; only text is sent, never screenshots.
- Jev's role: Choice of target element and action, plus completion and risk judgments
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/Sac-Y/Jev-cu#%E5%AE%89%E8%A3%85-skill
- Caveat: README and skill docs are mostly Chinese. No license file at the time of check. Text-only element candidates mean anything not exposed in the accessibility tree is invisible to the model.

### [Jev experiments](https://github.com/dabit3/jev-experiments)
<!-- catalog:jev-experiments -->

By [Nader Dabit](https://github.com/dabit3).

A collection of latency-focused demo apps that use Jev through the official JavaScript SDK.

- Action / outcome: Each app lives in its own directory with a README, testing notes and screenshots. Server code creates a TypeSafeClient with retries and timeouts and asks Jev per request.
- Jev's role: Per-demo judgments served from a small backend, varying by app
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/dabit3/jev-experiments#jev-experiments
- Caveat: Demo code, written with an autonomous coding agent per the README badge. Latency claims were not remeasured. No repo-level license at the time of check.

### [Mobile Jev](https://github.com/droidrun/mobile-jev)
<!-- catalog:mobile-jev -->

Maintained by [Droidrun](https://github.com/droidrun).

Uses Jev to choose the next action on a real Android phone driven through the Mobilerun API.

- Action / outcome: A CLI and a React studio run a goal-directed loop against a cloud phone, with execution traces and per-request latency. The README demo reaches Uber's payment selection step and does not complete a booking.
- Jev's role: Next-action choice per step, with input verification handled separately
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/droidrun/mobile-jev#mobile-jev
- Demo: https://github.com/droidrun/mobile-jev/blob/main/docs/media/uber-demo.mp4
- Caveat: Requires a Mobilerun account and API key in addition to a TypeSafe key. The recorded timing (about 21 seconds for 9 actions) was not reproduced here.

### [jev-align](https://github.com/sutro-sh/jev-align)
<!-- catalog:jev-align -->

Maintained by [Sutro](https://github.com/sutro-sh).

Uses Jev to build AI functions, surfacing uncertain examples for labeling and optimizing the function with GEPA.

- Action / outcome: A Python CLI that captures production inputs, picks uncertain cases by acquisition score, asks for labels, and runs GEPA to improve the function's questions. Supports TypeSafe, Cloudflare and Vercel Jev gateways.
- Jev's role: The evaluated function under optimization; answers and confidence drive acquisition
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/sutro-sh/jev-align#quick-start
- Caveat: Self-described as experimental. Requires Python 3.11 or newer. Optimization quality depends on your labeled examples and was not evaluated here.

### [Jev Browser](https://github.com/jkudish/jev-browser)
<!-- catalog:jev-browser-jkudish -->

By [Joey Kudish](https://github.com/jkudish).

Uses Jev to pick one browser action per step from a page's clickable, typeable and selectable elements, exposed as an MCP server, CLI and library.

- Action / outcome: Drives headless Playwright Chromium toward a task and URL. Returns the final page, a step trace with per-step confidences, console errors and a screenshot. Code owns the loop: budgets, recovery and stop gates.
- Jev's role: Per-step choice of the next action and target element, plus goal-met and stuck probabilities
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/jkudish/jev-browser#install
- Caveat: Early software; the README warns about rough edges on harder sites. The published latency and cost figures were not reproduced here.

### [jev-lint](https://github.com/mizchi/jev-lint)
<!-- catalog:jev-lint -->

By [Kotaro Chikuba](https://github.com/mizchi).

Uses Jev to lint the things a parser cannot check, such as whether a function does what its name says or whether a comment is still true.

- Action / outcome: Matches code with ast-grep, then sends one file as state with many independent questions per run and prints flagged lines with probabilities and per-rule cutoffs. Ships rules for TypeScript, JavaScript, Rust, Python, Go, Markdown, package.json and git commits.
- Jev's role: Many independent per-match judgments over one file of state, batched into a single request
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Caveat: Rule cutoffs in RULES.md come from the author's own committed baselines and were not re-derived here. Checks that call the model need a key and cost money per run.

### [voice-browser](https://github.com/moritzkremb/jev-voice-browser)
<!-- catalog:jev-voice-browser -->

By [Moritz Kremb](https://github.com/moritzkremb).

Uses Jev to decide whether a partial voice transcript is a complete, addressed, non-destructive command, then acts on a real browser before the sentence ends.

- Action / outcome: Streams partial transcripts from the Web Speech API to a Node server that snapshots the page, asks Jev around a dozen typed questions in one request, and decides whether to act, wait, ask or ignore on a headed Chromium window driven by Playwright.
- Jev's role: One request with about a dozen typed questions: intent, target element, site, command completeness, addressed-to-me, destructiveness
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Caveat: Acts on a live browser from speech, so a misread command can navigate or type. The README's 250 to 350 ms latency claim was not reproduced here.

### [jev-shell-history](https://github.com/mrnugget/jev-shell-history)
<!-- catalog:jev-shell-history -->

By [Thorsten Ball](https://github.com/mrnugget).

Uses Jev to rank which of your recent shell history entries you are completing, shown as a fish-style zsh autosuggestion.

- Action / outcome: A zsh plugin that sends the last 100 distinct history entries plus the current input to Jev and renders the best match in grey after the cursor with its score. Right arrow or Ctrl-E accepts it. Prefix mode completes literally, fuzzy mode can replace the line.
- Jev's role: Ranks candidate history entries against the partially typed command and returns per-candidate probabilities
- Origin: community · Evidence: `code-inspected` · Readiness: installable-from-source
- Install / start: https://github.com/mrnugget/jev-shell-history#install
- Caveat: Every keystroke past the minimum length can trigger a request, so cost scales with typing. Your shell history is sent to the API. No license file at the time of review.

### [Jev Recruiter](https://github.com/skeptrunedev/jev-recruiter)
<!-- catalog:jev-recruiter -->

By [@skeptrunedev](https://github.com/skeptrunedev).

Uses Jev to choose where to browse on LinkedIn, screen professional titles, and judge visible profile excerpts against a written brief.

- Action / outcome: A local workspace built on Browser Use's Jev Ultrafast and Browser Harness. It starts from a people search, follows selected sidebar recommendations, saves discovered profile URLs with their source and screening result, and exports JSON. The live browser is visible and runs can be paused and stepped.
- Jev's role: Navigation choices, title screening, and per-criterion evidence selection with no secondary text model
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/skeptrunedev/jev-recruiter#quick-start
- Caveat: Automates a signed-in LinkedIn session, which can conflict with that site's terms and risks the account. Screening people is a consequential use; the model's judgments were not evaluated for fairness here.

### [is-malicious?](https://github.com/luantak/is-malicious)
<!-- catalog:is-malicious -->

By [@luantak](https://github.com/luantak).

Uses Jev to judge whether a dependency diff or package looks malicious, as a CLI, an agent skill and a GitHub Actions check.

- Action / outcome: Discovers and chunks changed files, runs deterministic built-in checks first, then asks Jev about the remaining chunks and prints a verdict. Ships benign, telemetry and dropper fixtures plus ready-made PR scanning workflows.
- Jev's role: Per-chunk judgments of suspicious behavior in source and package metadata
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Caveat: A screening aid, not a security guarantee: it can miss real attacks and flag benign code. Detection rates were not measured here beyond the shipped fixtures.

### [fastbrowse](https://github.com/agent-labs-dev/fastbrowse)
<!-- catalog:fastbrowse -->

Maintained by [Agent Labs](https://github.com/agent-labs-dev).

Uses Jev to choose browser actions, reaching the API directly or through the Vercel AI Gateway depending on which key is set.

- Action / outcome: A Python browser agent that captures page state, asks Jev for the next operation, and runs live evals comparing the direct TypeSafe path against the gateway path. Ships adapters for local Chrome and Browser Use Cloud plus an autoconsent bundle.
- Jev's role: Chooses the next browser operation and target from captured page state
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Caveat: Jev is one of two routes; with only a gateway key set the same questions go to the Vercel AI Gateway instead. The repository's own eval numbers were not reproduced here.

### [Jev DSH Decision Engine](https://github.com/Devin-AXIS/jev-dsh-decision)
<!-- catalog:jev-dsh-decision -->

By [@Devin-AXIS](https://github.com/Devin-AXIS).

A DSH desktop plugin that uses Jev to judge a selected task context against written criteria, with the key resolved from the host credential store.

- Action / outcome: Registers Jev-backed actions inside DSH, resolves TYPESAFE_API_KEY through the host's credentials service rather than plugin source, sends the selected task context and criteria to the System One endpoint, and returns the decision to the host's tools and skills services.
- Jev's role: Typed decision over a selected task context and user-written criteria
- Origin: community · Evidence: `code-inspected` · Readiness: installable-from-source
- Caveat: Documentation is in Chinese and the plugin only runs inside a DSH install that provides the credentials, tools and skills services. Young repository with a small commit history.

### [memsearch](https://github.com/zilliztech/memsearch)
<!-- catalog:memsearch-jev-reranker -->

Maintained by [Zilliz](https://github.com/zilliztech).

Uses Jev to rerank recalled memories before a coding agent sees them.

- Action / outcome: Runs a semantic memory store for coding agents across Claude Code, Codex and other harnesses, and offers Jev as an opt-in reranker: jev_reranker.py POSTs the query and candidate memories to the System One endpoint and reorders results by the returned judgment before they reach the agent.
- Jev's role: Opt-in reranking judgment over recalled memory candidates
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://zilliztech.github.io/memsearch/
- Caveat: Jev is one optional reranker backend, not the default path, so most of the project runs without TypeSafe. Reranking quality numbers in the evaluation docs were not reproduced here.

### [Hippo](https://github.com/kitfunso/hippo-memory)
<!-- catalog:hippo-memory-jev-reranker -->

By [Keith So](https://github.com/kitfunso).

Uses Jev to rerank recalled memories in a decay-based memory layer for agents.

- Action / outcome: Runs a local SQLite memory layer with decay and provenance for CLI agents, and ships an opt-in Jev reranker: src/rerankers/jev.ts posts the query and candidate memories to the System One endpoint so hippo recall can order results by judgment instead of raw similarity.
- Jev's role: Opt-in reranking judgment over recalled memory candidates
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/kitfunso/hippo-memory#readme
- Demo: https://hippo-memory.com
- Caveat: Jev is one opt-in reranker flag; the default recall path does not call TypeSafe. Large repository where the Jev surface is a small part of the whole.

### [Jeview](https://github.com/andududu/jeview)
<!-- catalog:jeview -->

By [Mihai Ionescu](https://github.com/andududu).

Uses a local gateway to record and draw every Jev call your code makes.

- Action / outcome: Sits between your code and TypeSafe on 127.0.0.1:4777, forwards each request to the System One endpoint with your key, returns Jev's answer unchanged, stores every call in a local SQLite database and draws them on a live map. Requests can be grouped under a project label by path.
- Jev's role: None of its own: it proxies and visualises the caller's Jev requests and answers
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/andududu/jeview#run-it
- Caveat: Unofficial and not affiliated with TypeSafe, as the README states. Young repository created 2026-09-21 with a small commit history, and it proxies your API key, so run it locally only.

### [jev-edge](https://github.com/kiwi0719/jev-edge)
<!-- catalog:jev-edge -->

By [@kiwi0719](https://github.com/kiwi0719).

Uses Jev at an nginx or APISIX gateway to judge requests before they reach a backend.

- Action / outcome: Runs as an OpenResty or Apache APISIX plugin that applies cheap L1 rules first, then sends the remaining requests to the System One endpoint for a typed admission judgment, logging one JSON line per judged request and exposing health and config endpoints under /_jev.
- Jev's role: Typed admission judgment on requests that pass the deterministic rule layer
- Origin: community · Evidence: `code-inspected` · Readiness: installable-from-source
- Install / start: https://github.com/kiwi0719/jev-edge#try-it-in-30-seconds
- Caveat: Independent project, not affiliated with TypeSafe. Only 4 stars and created 2026-09-21, so it is new and unproven in production. Putting a network judgment in the request path adds latency and a failure mode you must configure around.

### [jev-agent-browser](https://github.com/forvela/jev-agent-browser)
<!-- catalog:jev-agent-browser -->

By [@forvela](https://github.com/forvela).

Uses Jev to pick the next typed browser action and hands ambiguity back to the parent agent.

- Action / outcome: Gives a parent agent a bounded browser task: Jev chooses the next typed action through the official JavaScript SDK, Vercel's agent-browser executes it, and ambiguity, repetition or a stuck state becomes a structured handoff back to the parent instead of a guess.
- Jev's role: Typed next-action selection per browser step, plus stuck and ambiguity gates
- Origin: community · Evidence: `code-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/forvela/jev-agent-browser#quick-start
- Caveat: Young repository with 7 stars and a small commit history. Requires the separate agent-browser package. The npm package page returned 403 to an automated check, so install was verified from the repository rather than the registry page.

### [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)
<!-- catalog:jev-ood-calibration -->

By [@scienthoon](https://github.com/scienthoon).

Uses Jev on a task it cannot have seen to test whether its probabilities stay calibrated.

- Action / outcome: Sends JSONL records to Jev through the Vercel AI Gateway with one evaluate call per record, then reports accuracy, NLL, ECE and a refit temperature on three public benchmarks alongside a rule-based task built to be out of distribution.
- Jev's role: The system under test: typed answers with probabilities that the harness scores for calibration
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/scienthoon/jev-ood-calibration#readme
- Caveat: Independent single-author study with 4 stars whose numbers were not re-run here. It calls Jev through the Vercel AI Gateway rather than api.typesafe.ai directly, and running it costs gateway inference spend.

### [DocJev](https://github.com/jerryjliu/docjev)
<!-- catalog:docjev -->

By [Jerry Liu](https://github.com/jerryjliu).

Uses Jev to classify a document into one category, or to split a packet into ordered page ranges.

- Action / outcome: Python library and CLI take a PDF, DOCX, or PPTX plus natural-language category rules. LiteParse extracts page text. Optional LlamaParse and a local review app are in the repo.
- Jev's role: Choice over the category rules, via typesafe_sdk system_one
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/jerryjliu/docjev#quick-start
- Caveat: Independent of LlamaIndex hosted Classify and Split. Accuracy and latency figures in the README were not remeasured. Needs a TypeSafe API key.

### [JevGPT](https://github.com/Bewinxed/jevgpt)
<!-- catalog:jevgpt -->

By [Omar Al Matar](https://github.com/Bewinxed).

Uses Jev to pick the next word from a fixed dictionary so a chatbot can answer without generating text.

- Action / outcome: Chat client sends the transcript as state and walks a dictionary with bucketed choices, then a runoff choice, until a completeness check stops it.
- Jev's role: Choice over dictionary buckets, then a runoff choice, plus a completeness noul
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/Bewinxed/jevgpt#readme
- Caveat: Interactive demo, not a general chatbot. The author's 255-choice cap note and latency claims were not remeasured. Needs a TypeSafe API key.

### [System One Harness](https://github.com/HarnessRouter/SystemOneHarness)
<!-- catalog:systemone-harness -->

Maintained by [HarnessRouter](https://github.com/HarnessRouter).

Uses Jev, or an OpenRouter System One route, to answer the typed questions in a decision harness.

- Action / outcome: Python CLI runs a harness against a System One provider. The TypeSafe provider posts to the official endpoint. OpenRouter is the other key path.
- Jev's role: TypeSafe provider posts state and questions to api.typesafe.ai/v1/systemone
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/HarnessRouter/SystemOneHarness#quickstart
- Caveat: Jev is one of two providers, not the only route. A fixture path in provider.py returns scripted probabilities; the TypeSafe class is the live path. Conformance numbers were not remeasured.

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

### [jev-eval-agent](https://github.com/vinilana/jev-eval-agent)
<!-- catalog:jev-eval-agent -->

By [Vinicius Lana](https://github.com/vinilana).

Uses Jev to pick the tool before each agent step, then measures how many steps that takes versus letting the LLM choose from all 100 tools.

- Action / outcome: A personal-assistant agent with 100 mocked tools, served through OpenRouter, that runs in two modes selected by one environment variable. In jev-classifier mode Jev picks the tool from conversation state and only that tool is exposed to the LLM, which fills the arguments. Evals and a results UI are included.
- Jev's role: Choice of one tool out of 100 before every model step, from the conversation state
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Caveat: All 100 tools are mocked, so the comparison measures step counts on synthetic tasks rather than real outcomes. The committed eval results were not reproduced here.

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

### [Jev Review (MCP)](https://github.com/NiazMorshed2007/jev-review)
<!-- catalog:jev-review-mcp -->

By [Niaz Morshed](https://github.com/NiazMorshed2007).

Local MCP server that gives a coding agent structured Jev quality scores across correctness, complexity, tests and security while it works.

- Action / outcome: Exposes a single jev_review tool over MCP stdio to Claude Code, Codex, Cursor and OpenCode. The coding agent still diagnoses and edits; Jev supplies scalar scores per quality dimension. No hosted backend, the only remote call goes to the configured Jev API.
- Jev's role: Independent per-dimension quality scores over a code diff or file
- Origin: community · Evidence: `code-inspected` · Readiness: installable-from-source
- Install / start: https://github.com/NiazMorshed2007/jev-review#quick-start
- Caveat: A different project from the similarly named jev-review by devagrawal09 already in this catalog. Distributed from GitHub only, not npm. Score quality was not benchmarked here.

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

### [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev)
<!-- catalog:ha-jev -->

By [Colin de Vries](https://github.com/AboveColin).

Uses Jev to answer typed questions about a live Home Assistant house and exposes the answers as sensors and binary sensors.

- Action / outcome: A HACS custom integration with a config flow for the API address and key. It builds state snapshots from tracked entities, asks Jev, and publishes the typed results as entities plus a conversation agent, with usage accounting and diagnostics.
- Jev's role: Typed judgments over a snapshot of selected Home Assistant entity states
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Caveat: A custom HACS integration, not an official Home Assistant one. Polling a house full of entities bills per request; the built-in usage accounting was not verified against a real bill.

### [Jev for Apple Foundation Models](https://github.com/peterfriese/jev-foundation-models)
<!-- catalog:jev-foundation-models -->

By [Peter Friese](https://github.com/peterfriese).

Uses Jev to evaluate typed Swift structs and enums inside Apple's Foundation Models framework.

- Action / outcome: Swift package posts application state to Jev and maps the typed answer back into a Foundation Models language-model call.
- Jev's role: LanguageModel that posts to api.typesafe.ai/v1/systemone
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/peterfriese/jev-foundation-models#readme
- Caveat: Unofficial bridge. The 40-150ms claim was not remeasured. The README warns not to embed the API key in a mobile app.

### [Jev Labeler](https://github.com/yamadashy/jev-labeler-action)
<!-- catalog:jev-labeler -->

By [Kazuki Yamada](https://github.com/yamadashy).

Uses Jev to decide which existing GitHub labels apply to an issue or pull request.

- Action / outcome: GitHub Action asks one yes/no question per label already defined in the repo and applies the labels that clear a threshold.
- Jev's role: One noul question per label
- Origin: community · Evidence: `code-inspected` · Readiness: runnable-from-readme
- Install / start: https://github.com/yamadashy/jev-labeler-action#quick-start
- Caveat: Label quality depends on the descriptions already on the repo labels. Thresholds were not remeasured. A wrong label is the failure mode the README describes.

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

### [typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go)
<!-- catalog:typesafe-sdk-go-tangerg -->

By [@Tangerg](https://github.com/Tangerg).

Dependency-free Go client for the TypeSafe System One API.

- Action / outcome: Go programs send typed questions and read Choice, Score, and Noul answers with confidence.
- Jev's role: Native via TypeSafe API
- Origin: community · Evidence: `code-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/Tangerg/typesafe-sdk-go#readme
- Caveat: Unofficial. One of many competing community Go clients; small star count.

### [JevSwiftSDK](https://github.com/NSStudent/JevSwiftSDK)
<!-- catalog:jev-swift-sdk -->

By [@NSStudent](https://github.com/NSStudent).

Dependency-free Swift package for the System One HTTP API.

- Action / outcome: Swift apps on iOS, macOS, or Linux send typed questions with async/await, batching, and retries.
- Jev's role: Native via TypeSafe API
- Origin: community · Evidence: `code-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/NSStudent/JevSwiftSDK#installation
- Caveat: Unofficial and very new. No release tag yet, so the README recommends pinning a branch. Keep the key server-side; the quickstart is written for a server or CLI, not a shipped mobile app.

### [typesafe-sdk (Ruby)](https://github.com/joshmn/typesafe-sdk)
<!-- catalog:typesafe-sdk-ruby -->

By [@joshmn](https://github.com/joshmn).

Ruby gem client for the TypeSafe System One API.

- Action / outcome: Ruby code calls system_one with Choice, Score, and Noul questions and reads typed answers.
- Jev's role: Native via TypeSafe API
- Origin: community · Evidence: `code-inspected` · Readiness: installable-per-readme
- Install / start: https://github.com/joshmn/typesafe-sdk#installation
- Caveat: Unofficial. Distinct from ruby_llm-typesafe, which is a RubyLLM provider rather than a direct client.

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

### [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)
<!-- catalog:fast-jev-compaction -->

By [tamara tran](https://github.com/tamaratran).

Uses Jev to decide which tool calls and results to drop during context compaction, keeping everything else verbatim.

- Action / outcome: Replaces Claude Code's compaction summary. Every non-pinned tool call gets two noul questions; only calls and results Jev says are no longer needed are deleted or truncated. User and assistant text is never rewritten.
- Jev's role: Two noul questions per non-pinned tool call, asked over the whole conversation in one request
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/tamaratran/fast-jev-compaction#what-and-why
- Caveat: Token counts are estimated without a tokenizer, so compaction can throw when state does not fit. Retention quality was not remeasured here.

### [Jev Browser Use](https://github.com/wy-coliney/jev-browser-use)
<!-- catalog:jev-browser-use -->

By [@wy-coliney](https://github.com/wy-coliney).

Uses Jev to choose browser navigation, clicks and scrolling while the coding agent keeps text input and final verification.

- Action / outcome: Installs as a Codex skill with one npx command and drives an existing browser connection through a small bridge, with no extra driver or npm dependency.
- Jev's role: Choice of the next browser action from candidate elements, with confidence recorded per step
- Origin: community · Evidence: `code-inspected` · Readiness: installable
- Install / start: https://github.com/wy-coliney/jev-browser-use#install
- Caveat: The 5-10x speedup claim comes from the author's own workflows and was not reproduced here. Decisions run on text candidates, not pixels.

### [Skillbox](https://github.com/kitze/skillbox)
<!-- catalog:skillbox -->

By [@kitze](https://github.com/kitze).

Self-hosted agent skill library that uses Jev to recommend which stored skills fit the current request.

- Action / outcome: Runs as a self-hostable service with a CLI and MCP surface for managing a personal skill collection, and calls the System One endpoint to rank recommendations. Ships Docker Compose, Coolify and Umbrel deployment paths plus a recommendation benchmark script.
- Jev's role: Ranks stored skills against the current request to produce recommendations
- Origin: community · Evidence: `code-inspected` · Readiness: installable-from-source
- Caveat: Jev powers one feature, the recommendations; the rest of the product is a skill manager that works without a key. Self-hosting requires running the Compose stack.

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

### [awesome-jev (cobanov)](https://github.com/cobanov/awesome-jev)
<!-- catalog:list-cobanov -->

By [Mert Cobanov](https://github.com/cobanov).

Source-backed list that publishes dated research notes alongside each review.

- Action / outcome: README sections plus per-review research notes with pinned source evidence.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Entry counts move quickly. Review boundaries are documented per review rather than per entry.

### [awesome-jev-projects (logicrw)](https://github.com/logicrw/awesome-jev-projects)
<!-- catalog:list-logicrw -->

By [@logicrw](https://github.com/logicrw).

Bilingual ecosystem radar with a published site and automatic GitHub sync.

- Action / outcome: README plus a GitHub Pages radar covering 300+ tracked projects.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Demo: https://logicrw.github.io/awesome-jev-projects/en/
- Caveat: Automatic sync means breadth over verification; the project count is self-reported.

### [awesome-jev (AppitStudio)](https://github.com/AppitStudio/awesome-jev)
<!-- catalog:list-appitstudio -->

Maintained by [AppitStudio](https://github.com/AppitStudio).

Directory split into Jev-powered apps, developer resources, and small inspectable workflows.

- Action / outcome: Per-section markdown directories plus a separate beta web UI.
- Jev's role: n/a (list)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Promotes an associated hosted product (JevList), so it is a vendor-adjacent directory rather than a neutral one.

### [awesome-jev-tools (v-modal)](https://github.com/v-modal/awesome-jev-tools)
<!-- catalog:list-v-modal -->

Maintained by [v-modal](https://github.com/v-modal).

Curated Jev list whose README is generated as an aggregate of per-category files.

- Action / outcome: Publishes accepted entries on the homepage without drilling into subpages, splitting the catalog across category files.
- Jev's role: none (directory)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Entries were not independently verified by this catalog.

### [Awesome Jev (valentynkit)](https://github.com/valentynkit/awesome-jev-typesafe)
<!-- catalog:list-valentynkit -->

By [@valentynkit](https://github.com/valentynkit).

Curated Jev list following the awesome.re conventions with a CI lint on every change.

- Action / outcome: Carries the awesome badge and a GitHub Actions lint workflow that checks list formatting.
- Jev's role: none (directory)
- Origin: community · Evidence: `demo-inspected` · Readiness: list
- Caveat: Entries were not independently verified by this catalog.

### [Awesome JEV gallery (OmniJev)](https://github.com/OmniJev/awesome-jev-gallery)
<!-- catalog:list-omnijev -->

Maintained by [OmniJev](https://github.com/OmniJev).

Collects papers, open models, and evals around System One and Jev.

- Action / outcome: README gallery with a linked site. It is a papers, models, and evals list, not a directory of runnable apps.
- Jev's role: none (curated list)
- Origin: community · Evidence: `demo-inspected` · Readiness: curated-list
- Install / start: https://github.com/OmniJev/awesome-jev-gallery#readme
- Caveat: Papers and eval gallery, not a project directory. Outbound links were not opened one by one. Org created 2026-09-17. The 223-star count was not audited.

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

### [NanoJev](https://github.com/TianyuCodings/NanoJev)
<!-- catalog:nanojev -->

By [@TianyuCodings](https://github.com/TianyuCodings).

A 0.6B open replica of the System One shape, trained to answer decision questions with probability distributions.

- Action / outcome: Publishes a checkpoint and dataset on Hugging Face and reports ViZDoom, maze and Snake results against a matched Jev run. Not api.typesafe.ai.
- Jev's role: none (open-weight replica, compared against Jev)
- Origin: related · Evidence: `demo-inspected` · Readiness: related-not-jev-api
- Demo: https://huggingface.co/C-Tianyu/NanoJev
- Caveat: Not TypeSafe weights. Reported win rates against Jev are the author's own numbers on the author's tasks and were not reproduced here. The interactive development site requires access.

### [Simple Jev](https://github.com/featherless-ai/simple-jev)
<!-- catalog:simple-jev -->

Maintained by [Featherless AI](https://github.com/featherless-ai).

Builds System One style typed answers from open Hugging Face models by reading next-token logits instead of generating JSON.

- Action / outcome: A local Transformers and PyTorch server plus a public keyless demo API, with shared validation and scoring rules in a plain Python package. Not api.typesafe.ai.
- Jev's role: none (open-model reimplementation of the interface)
- Origin: related · Evidence: `demo-inspected` · Readiness: related-not-jev-api
- Install / start: https://github.com/featherless-ai/simple-jev#simple-jev-project
- Demo: https://simple-jev.featherless.ai/
- Caveat: Not TypeSafe weights and makes no equivalence claim. The demo API is limited to 2k tokens and 2 requests per second. Only models whose answer labels tokenize to one distinct token are supported.

### [openjev-sglang](https://github.com/ekzhang/openjev-sglang)
<!-- catalog:openjev-sglang -->

By [Eric Zhang](https://github.com/ekzhang).

Serves the TypeSafe HTTP API shape from an open Qwen model running on SGLang.

- Action / outcome: Deploys to Modal as a B200 SGLang container plus a FastAPI process, with MMLU-Pro and BoolQ eval scripts. Not api.typesafe.ai.
- Jev's role: none (API-compatible server backed by an open model)
- Origin: related · Evidence: `demo-inspected` · Readiness: related-not-jev-api
- Install / start: https://github.com/ekzhang/openjev-sglang#run-on-modal
- Caveat: Not TypeSafe weights, only the API shape. Running it needs a Modal account and B200 GPU time, so cost is on you. Eval numbers were not reproduced here.

### [Laya](https://github.com/receptron/laya)
<!-- catalog:laya -->

Maintained by [Receptron](https://github.com/receptron).

Runs an open Jev-compatible decision model in Node through ONNX Runtime. Not api.typesafe.ai.

- Action / outcome: Loads the open Laya weights from Hugging Face and answers choice, score and noul questions with calibrated probabilities in one forward pass, using a systemOne() call whose request and response shape follows TypeSafe Jev's system_one API. Runs locally on ONNX Runtime with no Python at runtime.
- Jev's role: none (open model reproducing the System One request and response shape)
- Origin: related · Evidence: `code-inspected` · Readiness: related-not-jev-api
- Install / start: https://github.com/receptron/laya#install
- Caveat: Not TypeSafe weights and not api.typesafe.ai, only the same API shape from the open Laya model by Convai Innovations. First use downloads about 1.7 GB of ONNX weights and needs roughly 2 GB of RAM. Parity with the Python reference is an author claim that was not re-run here.

### [decider](https://github.com/Mapika/decider)
<!-- catalog:decider -->

By [Mark Marosi](https://github.com/Mapika).

Answers choice, score, and noul questions from a local model. Not api.typesafe.ai.

- Action / outcome: Serves Jev-shaped requests from local weights. The repo includes a game bench that records probability bars for Tetris, Breakout, Pong, Snake, and Connect Four.
- Jev's role: none (local model using the System One wire format)
- Origin: related · Evidence: `code-inspected` · Readiness: related-not-jev-api
- Install / start: https://github.com/Mapika/decider#readme
- Caveat: Not TypeSafe weights and not api.typesafe.ai. Game scores in the README were not remeasured. Weights are a separate Hugging Face download.

