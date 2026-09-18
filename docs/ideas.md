# Unbuilt ideas

These are **not** in the catalog as shipping projects. They are inspired by inspected public work. Do not confuse them with things people already built.

## 1. Review-gated mail desk

GiesN’s LangGraph demo classifies mocked mail and always routes. A useful next step is a real inbox worker that only **labels** and **drafts**, with send/archive behind an explicit approve action. Use department Choice + sensitive Noul + confidence gates. Default dry-run.

## 2. Allowlist-only model router for multi-provider agents

jev-router already wraps Claude/Codex. The gap is a router that cannot leave an operator-declared provider/model allowlist — including “do not spill from a work key to a personal key.” Uncertain → keep the pinned model. Community routers that fail open across vendors are the anti-pattern.

## 3. Publish-time citation brake

The official citation-check cookbook is a notebook. Wire the same Choice (“does this quote support the claim?”) into a pre-commit or “open PR” hook so unsupported sentences cannot merge without a human override. Jev never pushes.

## Explicitly not ideas

- Native vision Jev, audio Jev, or robot control (not in the current API).
- Another MCP clone of jkudish/jev-mcp.
- Inflating this list to match 400-entry auto-directories.
