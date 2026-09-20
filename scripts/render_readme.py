#!/usr/bin/env python3
"""Render README.md and docs/catalog.md from data/use-cases.json."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "use-cases.json"
README = ROOT / "README.md"
DETAILS = ROOT / "docs" / "catalog.md"
UPDATED = "2026-09-19"

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


def credit_sentence(entry: dict) -> str:
    parts: list[str] = []
    named = entry.get("named_creator")
    kind = entry["credit_kind"]
    link = f"[{entry['creator_display']}]({entry['creator_url']})"
    if named:
        parts.append(f"By {named}.")
        if kind == "maintained-by":
            parts.append(f"Maintained by {link}.")
        elif entry["creator_display"] != named:
            parts.append(f"By {link}.")
    elif kind == "maintained-by":
        parts.append(f"Maintained by {link}.")
    else:
        parts.append(f"By {link}.")
    for extra in entry.get("also_credits") or []:
        label = extra.get("label", "Also")
        parts.append(f"{label} [{extra['display']}]({extra['url']}).")
    return " ".join(parts)


def render_entry(entry: dict) -> str:
    eid = entry["id"]
    badge = EVIDENCE_BADGE[entry["evidence_level"]]
    return (
        f"- {link_line(entry)} — {entry['short_description']} "
        f"{credit_sentence(entry)} {badge} <!-- catalog:{eid} -->\n"
    )


def toc(entries: list[dict]) -> str:
    counts = Counter(e["category"] for e in entries)
    lines = []
    for cat, title in CATEGORY_ORDER:
        n = counts.get(cat, 0)
        if n:
            lines.append(f"- [{title}](#{slug(title)}) ({n})")
    lines.append("- [Quick start](#quick-start)")
    lines.append("- [Evidence](#evidence)")
    lines.append("- [Details](#details)")
    lines.append("- [Contributing](#contributing)")
    lines.append("- [Credits](#credits)")
    return "\n".join(lines)


def slug(title: str) -> str:
    out = []
    for ch in title.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_":
            out.append("-")
    collapsed = "".join(out).strip("-")
    while "--" in collapsed:
        collapsed = collapsed.replace("--", "-")
    return collapsed


def render_detail(entry: dict) -> str:
    eid = entry["id"]
    lines = [
        f"### {link_line(entry)}",
        f"<!-- catalog:{eid} -->",
        "",
        credit_sentence(entry),
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


def main() -> None:
    data = json.loads(CATALOG.read_text())
    entries = data["entries"]

    sections = []
    for cat, title in CATEGORY_ORDER:
        group = [e for e in entries if e["category"] == cat]
        if not group:
            continue
        sections.append(f"## {title}\n\n")
        sections.extend(render_entry(e) for e in group)
        sections.append("\n")

    detail_sections = []
    for cat, title in CATEGORY_ORDER:
        group = [e for e in entries if e["category"] == cat]
        if not group:
            continue
        detail_sections.append(f"## {title}\n\n")
        detail_sections.extend(render_detail(e) for e in group)

    body = f"""# Awesome Jev

**Public projects that use [Jev](https://typesafe.ai/), TypeSafe AI's System One model.** Unofficial. Not affiliated with TypeSafe AI.

Jev does not chat, write code, or see images. It returns Choice, Score, or Noul answers with probabilities. Your code decides what happens next.

[![CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![catalog](https://img.shields.io/badge/catalog-{len(entries)}_entries-111.svg)](data/use-cases.json)
[![updated](https://img.shields.io/badge/updated-2026.09.19-0a0.svg)](docs/research-method.md)

## Contents

{toc(entries)}

Related open reproductions sit in [Related, not TypeSafe Jev](#related-not-typesafe-jev). They are not Jev use cases. Unbuilt ideas are in [docs/ideas.md](docs/ideas.md), not in the catalog count.

{"".join(sections)}
## Quick start

1. Docs index: [docs.typesafe.ai/llms.txt](https://docs.typesafe.ai/llms.txt)
2. Python: `uv add typesafe-sdk` · JS: `npm install @typesafe-ai/sdk` (need `TYPESAFE_API_KEY`)
3. Agent skill: `npx skills add typesafe-ai/skills --skill typesafe-ai` or Claude Code plugin `typesafe@typesafe-ai`
4. HTTP: `POST https://api.typesafe.ai/v1/systemone`

## Evidence

| Badge | Meaning |
| --- | --- |
| `code-inspected` | README plus relevant source or example files were read |
| `demo-inspected` | A documented demo, cookbook run, or live page was inspected |
| `documented-example` | Official docs/cookbook/changelog |
| `author-claim` | Author or press described it; implementation not fully inspected |
| `proposed` | Not built; see [skill opportunities](docs/skill-opportunities.md) |

Vendor speed and cost charts are not remeasured here. Treat launch-week latency and “N users” claims as marketing unless a source is marked inspected.

## Details

Actions, caveats, and sources for every entry: [docs/catalog.md](docs/catalog.md) (generated from [data/use-cases.json](data/use-cases.json)).

How the sweep was done: [research method](docs/research-method.md). Skill-shaped gaps: [skill opportunities](docs/skill-opportunities.md).

This list is smaller than auto-generated directories on purpose. It includes a full public `typesafe-ai` org inventory (10 repos: 4 product, 3 supporting, 3 unrelated forks), evidence badges, and action-taking projects first.

Gaps: the first X lane used indexed web pages (`web_search`/`web_extract` of x.com; native `x_search` was unavailable). A 2026-09-17 native `x_search` rerun added two catalog entries. Google SERP was unavailable. No TypeSafe inference in this sweep.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs need a public source, an evidence level, and creator credit. Run `python3 scripts/validate.py`.

## Credits

README format inspired by [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) from [ComposioHQ](https://github.com/ComposioHQ). That list's prose, branding, logos, and affiliate links are not copied here.

Each project credits its author or maintainer from public README, package, or repository metadata. Other [awesome-Jev lists](#other-awesome-jev-lists) are listed as lists; their curators are credited there. This catalog does not claim those projects were all found independently of those lists.

TypeSafe, Jev, and System One are marks of TypeSafe AI.

## License

Original curation is [CC BY 4.0](LICENSE). Upstream code and docs keep their own licenses.

Updated {UPDATED}.
"""
    README.write_text(body)

    details = f"""# Catalog details

Generated from [data/use-cases.json](../data/use-cases.json). The [README](../README.md) is the browseable list; this page keeps actions, caveats, and sources.

Evidence badges match the README legend. Readiness values are catalog labels, not product grades.

Updated {UPDATED}.

{"".join(detail_sections)}"""
    DETAILS.parent.mkdir(parents=True, exist_ok=True)
    DETAILS.write_text(details)
    print(f"wrote {README} and {DETAILS} ({len(entries)} entries)")


if __name__ == "__main__":
    main()
