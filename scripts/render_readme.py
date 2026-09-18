#!/usr/bin/env python3
"""Render README.md from data/use-cases.json so catalog sections cannot drift."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "use-cases.json"
README = ROOT / "README.md"
UPDATED = "2026-09-17"

CATEGORY_ORDER = [
    ("action-taking", "Action-taking projects"),
    ("model-routing", "Model and skill routing"),
    ("email-routing", "Email and inbox routing"),
    ("mcp", "MCP and agent bridges"),
    ("official-cookbook", "Official cookbooks and patterns"),
    ("official-sdk", "Official SDKs and adapter"),
    ("official-docs", "Official docs, skill, and launch demos"),
    ("platform-integration", "Platform integrations"),
    ("community-sdk", "Community clients"),
    ("agent-skill", "Installable agent skills"),
    ("awesome-list", "Other awesome-Jev lists"),
    ("related-not-jev", "Related, not TypeSafe Jev"),
]

EVIDENCE_BADGE = {
    "code-inspected": "`code-inspected`",
    "demo-inspected": "`demo-inspected`",
    "author-claim": "`author-claim`",
    "documented-example": "`documented-example`",
    "proposed": "`proposed`",
}


def link_line(entry: dict) -> str:
    url = entry.get("repo_url") or entry.get("demo_url") or entry.get("install_url")
    title = entry["title"]
    return f"[{title}]({url})" if url else title


def render_entry(entry: dict) -> str:
    eid = entry["id"]
    lines = [
        f"### {link_line(entry)}",
        f"<!-- catalog:{eid} -->",
        "",
        entry["short_description"],
        "",
        f"- Action / outcome: {entry['actual_actions_or_outcome']}",
        f"- Jev's role: {entry['jev_role']}",
        f"- Origin: {entry['origin']} · Evidence: {EVIDENCE_BADGE[entry['evidence_level']]} · Readiness: {entry['readiness']}",
    ]
    if entry.get("install_url"):
        lines.append(f"- Install / start: {entry['install_url']}")
    if entry.get("demo_url") and entry.get("demo_url") != entry.get("repo_url"):
        lines.append(f"- Demo: {entry['demo_url']}")
    if entry.get("caveats"):
        lines.append(f"- Caveat: {entry['caveats']}")
    lines.append("")
    return "\n".join(lines) + "\n"


def toc(entries: list[dict]) -> str:
    counts = Counter(e["category"] for e in entries)
    rows = ["| Section | Count |", "| --- | ---: |"]
    for cat, title in CATEGORY_ORDER:
        n = counts.get(cat, 0)
        if n:
            rows.append(f"| [{title}](#{slug(title)}) | {n} |")
    return "\n".join(rows)


def slug(title: str) -> str:
    out = []
    for ch in title.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_":
            out.append("-")
    return "".join(out).strip("-").replace("--", "-")


def main() -> None:
    data = json.loads(CATALOG.read_text())
    entries = data["entries"]
    highlights = [e for e in entries if e.get("highlight")]
    highlight_block = "\n".join(
        f"1. {link_line(e)} — {e['short_description']} ({EVIDENCE_BADGE[e['evidence_level']]})"
        for e in highlights
    )

    sections = []
    for cat, title in CATEGORY_ORDER:
        group = [e for e in entries if e["category"] == cat]
        if not group:
            continue
        sections.append(f"## {title}\n")
        sections.extend(render_entry(e) for e in group)

    body = f"""# Awesome Jev

<img src="assets/mark.svg" alt="" width="48" height="48" align="left" />

**A researched list of useful things built with [Jev](https://typesafe.ai/), TypeSafe AI's System One model.**
Text/state in, typed decisions out. Unofficial. Not affiliated with TypeSafe AI.

<br clear="all" />

[![CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![catalog](https://img.shields.io/badge/catalog-{len(entries)}_entries-111.svg)](data/use-cases.json)
[![updated](https://img.shields.io/badge/updated-2026.09.17-0a0.svg)](docs/research-method.md)

Jev does not chat, write code, or see images. It returns Choice / Score / Noul answers with probabilities. **Your code** decides and acts. This list prefers projects that actually route, click, review, query, or gate something — then includes the rest of the useful ecosystem.

## Contents

{toc(entries)}

## Highlights (inspected action)

{highlight_block}

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

{"".join(sections)}
## What this list adds

Launch week produced several [awesome-jev](#other-awesome-jev-lists) directories, including auto-judged catalogs that claim hundreds of repos. This one is smaller on purpose:

- Exhaustive public `typesafe-ai` org inventory (10 repos, 4 product, 3 supporting, 3 unrelated forks)
- Evidence badges and a machine-readable catalog generated into this README
- Action-taking projects near the top, not SDK clones
- Honest gaps: first X lane was web-indexed (`web_search`/`web_extract` of x.com; native `x_search` unavailable). A 2026-09-17 native `x_search` rerun recovered two catalog entries. Google SERP still unavailable. No TypeSafe inference in this sweep
- Explicit [skill opportunities](docs/skill-opportunities.md) for email triage and model routing (no fake drop-in skills)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs need a public source and an evidence level. Run `python3 scripts/validate.py`.

## License

Original curation is [CC BY 4.0](LICENSE). Upstream code and docs keep their own licenses. TypeSafe, Jev, and System One are marks of TypeSafe AI.

Updated {UPDATED}.
"""
    README.write_text(body)
    print(f"wrote {README} ({len(entries)} entries)")


if __name__ == "__main__":
    main()
