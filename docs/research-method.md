# Research method

Sweep date: **2026-09-17** (America/Chicago). Social window: 2026-01-01 through 2026-09-18 UTC. Almost all on-topic public discussion is launch week **2026-09-15–18**. Native X rerun window: **2026-09-01 through 2026-09-17**.

This catalog covers the public sources that were checked. It is not a claim that every Jev project on the internet was found.

## Lanes

| Lane | Who | Model | Method | Output |
| --- | --- | --- | --- | --- |
| X (first pass) | native child | grok-4.6 | Native `x_search` **unavailable** (`-t hermes-cli` excluded the opt-in tool). `web_search` + `web_extract` of x.com | `scratch/x/` |
| X (native rerun) | owner | grok-4.6 calling `x_search` (model `grok-4.20-reasoning`) | Four targeted native queries, 2026-09-01–2026-09-17. Credential route label from the tool: `xai-oauth`. Grok OAuth chat is **not** treated as proof of native X access. | `scratch/x/X_RECOVERY.json` |
| Reddit | native child | grok-4.6 | reddit-reading anonymous Atom + site:reddit.com + pullpush | `scratch/reddit/` |
| GitHub | native child | grok-4.6 | `gh api` pagination + README/example inspection | `scratch/github/` |
| Web | owner | grok-4.6 | **Not Google.** Hermes browser Google SERP failed (`Invalid URL '/tabs'`). Used `web_search` / `web_extract` + live docs | `scratch/web/` |

Raw query logs stay in the compiler's private research workspace and are **not** published.

Children: `deleg_8edb9939` tasks 0–2, all `model: grok-4.6`, completed synchronously in this one-shot CLI session. Owner web work ran after children returned (overlap of four live surfaces was not possible once `delegate_task` joined).

## Official GitHub org

`GET /orgs/typesafe-ai` reported `public_repos=10`.

Pagination: `per_page=100` page 1 = 10, page 2 = 0. **Expected 10, collected 10.** Independently re-verified by the owner.

| Disposition | Count | Repos |
| --- | --- | --- |
| include (product) | 4 | typesafe-sdk-python, typesafe-sdk-js, skills, system-one-adapter-python |
| supporting | 3 | daggerverse (CI modules, no Jev), Overwatch (training dashboard; private CodeArtifact `typesafe`, not the public SDK), typesafe-ai.github.io (2024 manifesto HTML) |
| skip | 3 | forks of vllm, LLaDA, pulumi-clickhouse |

No public official Doom / Wikipedia-race / cookbook source repo. Those live in docs, blog videos, and Mintlify cookbooks.

Overwatch references private `typesafe-ai/Flow`, which is **not** in the public 10.

## Evidence policy

- `code-inspected` / `demo-inspected`: someone in this sweep read README and/or relevant source, or a live docs/demo page.
- `documented-example`: official docs/changelog.
- `author-claim`: tweet, README badge, or press; not fully inspected.
- Vendor latency, price, eval tables, and user counts are **attributed, not endorsed**.
- Jev is **text-only** (official system-one.md). Computer-use and video tools OCR/transcribe first.
- Offline simulators and mock-SDK tests are labeled.

## Access failures and gaps

- First X lane: no native X search; t.co expand blocked for one community roundup thread.
- Native X rerun (2026-09-17): `x_search` available and not degraded. Query 4 returned empty top-level `citations` with mixed inline user/status URLs; a GitHub URL in the prose was independently verified. Live `val.run` demos named on X could not be scraped (web_extract failed; Hermes browser Google `/tabs` error persisted).
- Google SERP unavailable in this agent browser.
- Reddit `web_extract` on reddit.com unsupported; anonymous feed ~1 req/min; some threads remain SERP-only.
- `gh search` caps (50–100) undercount the long tail that hellogumbo/rhc98 claim.
- `Hawxy/TypeSafe.Sdk` 404; live repo is `Hawxy/TypeSafeAI.Net`.
- `aliaihub/awesome-jev-usecases` exists but README was 404 on HEAD in the GitHub lane.
- npm search blocked in the GitHub child; PyPI versions for official packages were fetched.
- No TypeSafe inference, no billing, no social posts.
- Unrelated exclusions: Scala/Akka Typesafe, Java awesome-jav, jellydn/awesome-typesafe (TypeScript), HermitCraft “jev”.

## Existing awesome lists vs this one

Recorded: Anil-matcha/awesome-jev-by-typesafe (407★), AbdelStark/awesome-typesafe (66★), yibie/awesome-jev, AnotiaWang/awesome-jev, hellogumbo/awesome-jev (claims 410 entries), rhc98/awesome-jev (auto-judged 369 listed), OmniJev/awesome-jev, oxwen11, cagbal, yangzhou-chaofan/awesome-jev-prompt (stale star table), aliaihub (README 404).

Those lists keep their own curator credit in the catalog. Projects they also contain still credit the original author or maintainer.

This list adds: exhaustive official-org dispositions, evidence badges, generated README from JSON, action-taking ranking, skill-opportunity split, and a “related not Jev” shelf. It does **not** try to beat 410-entry directories on count.

## Daily sweep log

GitHub-only sweeps that add entries are logged here, one line per day.

- 2026-09-19: 6 queries, 8 entries added.
- 2026-09-20: 24 queries, 12 entries added.
