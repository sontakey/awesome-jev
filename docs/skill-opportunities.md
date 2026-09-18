# Skill opportunities

Three shelves. Do not treat an adaptation idea as a ready-to-install skill.

## Existing installable Jev integrations

Verified public install paths (frontmatter or docs read in this sweep):

| Skill / tool | Origin | Install (as documented) | Notes |
| --- | --- | --- | --- |
| typesafe-ai | official | `npx skills add typesafe-ai/skills --skill typesafe-ai` or `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai` | Design skill. Points at live docs. Does not call Jev by itself. |
| jev (dbreunig) | community | `npx skills add dbreunig/building-with-jev-skill` / Claude plugin `jev@building-with-jev` | Frontmatter `name: jev` verified. Overlaps official skill. |
| advocaat | community | `npx skills add pithings/advocaat` | Thin TS `ask()` client + skill. |
| jev-axi | community | `npm install -g jev-axi` plus skill in the repo | Log/diff/untrusted-text. Needs `TYPESAFE_API_KEY`. |
| jev-router | community | README: wrap `claude` / `codex` CLIs | Model routing. Uses `JEV_API_KEY` in README. |
| jkudish/jev-mcp | community | `npx -y @jkudish/jev-mcp` (README) | MCP verify/screen/rank. PoC. |
| SkillRanker | community | Build from `Dicklesworthstone/skillranker` | Offline `sr demo`; live needs a key. |
| Official skill-suggestion cookbook | official | Not a skill; a cookbook | Ranks the Hermes roster with Jev. |

Also: geilt/typesafe-cli, jtsang4/jev-cli, reachjalil/jevlogs (offline `npx jevlogs`), Stumble/jev-go, docxology/daf-jev. See GitHub lane `skills.json` for frontmatter flags.

Copies of the official skill inside random dotfiles are **not** unique skills.

## Generic skills you can adapt (not Jev-native)

These exist as agent skills/workflows but talk to LLMs or mail APIs, not Jev:

- Hermes **email-inbox-triage** (generic). Closest Jev analog: [GiesN/typesafe-jev-workflow](https://github.com/GiesN/typesafe-jev-workflow) (mocked emails, Choice invoice vs general, **no send**).
- Hermes config **fallback_model** / skill-pinned models — framework routing, not Jev.
- NousResearch/hermes-agent discussions of a model-router skill (issues/PRs) — generic, not TypeSafe.
- Claude “build an email triage skill” tutorials — LLM generation, not System One.

Adaptation means: keep IMAP/send/review UI in the existing skill; add a Jev request for labels; do **not** relabel the generic skill as Jev-backed until that code exists and is tested.

## Proposed (not built here)

No executable stubs. Minimal contracts only.

### 1. Email triage (Hermes or any agent)

**Status:** proposed. No public drop-in Jev email skill found.

**Action contract**

- Input state: message id, headers, body text, optional thread, optional allowlisted labels.
- Questions (one request): `needs_reply` Noul, `department` Choice including `none`, `priority` Score, `sensitive` Noul (credentials, legal hold, medical — generic, no private taxonomy).
- Code actions: apply **labels only** when `department.confidence` is above a threshold you set on your data.
- **Write actions (reply, forward, archive, delete) require human review.** Default: draft a reply in a review queue; never send.
- Fail closed if the TypeSafe key is missing or the API errors: leave the message unread, do not auto-send.

**Safe default:** dry-run / label-only. GiesN demo always routes and does not gate on confidence — do not copy that as production mail policy.

### 2. Model routing (authorized providers only)

**Status:** proposed as a Hermes-native skill. Community CLIs already exist (jev-router, jev-codex-router).

**Action contract**

- Input: user turn, current skill, declared **allowlist** of provider/model ids the operator already authorized.
- Questions: `task_kind` Choice, `needs_strong_model` Noul, `out_of_policy` Noul (request would need a provider not on the list).
- Code picks from the allowlist only. **Never fall through** to a cheaper/other vendor, personal vs work boundary, or health/finance profile because Jev was uncertain.
- Uncertain or `out_of_policy`: stay on the session’s pinned model or ask the user. Do not “helpfully” switch.
- Log the decision (model id, probabilities, allowlist hash). No secrets in the log.

**Safe default:** fail open to the **already pinned** model (so work continues) but fail closed across **boundaries** (no silent provider hop).

### 3. Outbound claim gate (optional third)

Pair the official citation-check cookbook with a “do not publish” hook: PRs, blog drafts, or README edits. Jev only scores support; git push stays human. Listed as an idea in `ideas.md`.
