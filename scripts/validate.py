#!/usr/bin/env python3
"""Stdlib validation for awesome-jev catalog and README coverage."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "use-cases.json"
README = ROOT / "README.md"
DETAILS = ROOT / "docs" / "catalog.md"

REQUIRED = (
    "id",
    "title",
    "category",
    "short_description",
    "actual_actions_or_outcome",
    "jev_role",
    "other_components",
    "origin",
    "evidence_level",
    "sources",
    "repo_url",
    "demo_url",
    "install_url",
    "last_checked",
    "caveats",
    "skill_frameworks",
    "readiness",
    "creator_display",
    "creator_url",
    "credit_kind",
)
ORIGINS = {"official", "community", "platform", "related"}
EVIDENCE = {
    "code-inspected",
    "demo-inspected",
    "author-claim",
    "documented-example",
    "proposed",
}
CREDIT_KINDS = {"by", "maintained-by"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")


def ok_url(value: str | None) -> bool:
    if value is None:
        return True
    if not isinstance(value, str) or not value:
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def local_markdown_targets(text: str, path: Path) -> list[str]:
    errors: list[str] = []
    for href in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        href = href.strip()
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        if href.startswith("#"):
            continue
        target, _, _frag = href.partition("#")
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.name} link escapes repo: {href}")
            continue
        if not resolved.exists():
            errors.append(f"{path.name} broken local link: {href}")
    return errors


def main() -> int:
    errors: list[str] = []
    data = json.loads(CATALOG.read_text())
    entries = data["entries"] if isinstance(data, dict) else data
    if not isinstance(entries, list) or not entries:
        errors.append("catalog entries must be a non-empty list")
        print("\n".join(errors))
        return 1

    ids: list[str] = []
    repo_urls: dict[str, str] = {}
    for i, entry in enumerate(entries):
        prefix = f"entry[{i}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix} not an object")
            continue
        for key in REQUIRED:
            if key not in entry:
                errors.append(f"{prefix} missing {key}")
        eid = entry.get("id")
        if not isinstance(eid, str) or not ID_RE.match(eid):
            errors.append(f"{prefix} bad id {eid!r}")
        else:
            ids.append(eid)
        if entry.get("origin") not in ORIGINS:
            errors.append(f"{prefix} bad origin {entry.get('origin')!r}")
        if entry.get("evidence_level") not in EVIDENCE:
            errors.append(f"{prefix} bad evidence_level {entry.get('evidence_level')!r}")
        if entry.get("credit_kind") not in CREDIT_KINDS:
            errors.append(f"{prefix} bad credit_kind {entry.get('credit_kind')!r}")
        if not isinstance(entry.get("other_components"), list):
            errors.append(f"{prefix} other_components must be a list")
        if not isinstance(entry.get("skill_frameworks"), list):
            errors.append(f"{prefix} skill_frameworks must be a list")
        if not isinstance(entry.get("creator_display"), str) or not entry.get("creator_display"):
            errors.append(f"{prefix} creator_display must be a non-empty string")
        if not ok_url(entry.get("creator_url")) or not entry.get("creator_url"):
            errors.append(f"{prefix} creator_url must be http(s)")
        sources = entry.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{prefix} sources must be a non-empty list")
        else:
            for j, src in enumerate(sources):
                if not isinstance(src, dict) or not ok_url(src.get("url")):
                    errors.append(f"{prefix}.sources[{j}] needs http(s) url")
                for field in ("url", "type", "what_verified"):
                    if not src.get(field):
                        errors.append(f"{prefix}.sources[{j}] missing {field}")
        for url_key in ("repo_url", "demo_url", "install_url"):
            if not ok_url(entry.get(url_key)):
                errors.append(f"{prefix} {url_key} is not http(s) or null")
        extras = entry.get("also_credits")
        if extras is not None:
            if not isinstance(extras, list):
                errors.append(f"{prefix} also_credits must be a list")
            else:
                for j, extra in enumerate(extras):
                    if not isinstance(extra, dict) or not extra.get("display") or not ok_url(extra.get("url")):
                        errors.append(f"{prefix}.also_credits[{j}] needs display and http(s) url")
        repo = entry.get("repo_url")
        if repo:
            prior = repo_urls.get(repo)
            if prior and prior != eid:
                errors.append(f"duplicate repo_url {repo} ({prior} vs {eid})")
            else:
                repo_urls[repo] = eid

    dupes = {x for x in ids if ids.count(x) > 1}
    if dupes:
        errors.append(f"duplicate ids: {sorted(dupes)}")

    readme = README.read_text()
    details = DETAILS.read_text() if DETAILS.exists() else ""
    if not DETAILS.exists():
        errors.append("docs/catalog.md missing")

    for i, entry in enumerate(entries):
        eid = entry.get("id")
        if not isinstance(eid, str):
            continue
        marker = f"<!-- catalog:{eid} -->"
        if marker not in readme:
            errors.append(f"README missing catalog marker for {eid}")
        if details and marker not in details:
            errors.append(f"docs/catalog.md missing catalog marker for {eid}")
        creator_url = entry.get("creator_url")
        display = entry.get("creator_display")
        if isinstance(creator_url, str) and creator_url:
            credited = f"]({creator_url})"
            if credited not in readme:
                errors.append(f"README missing credited link {creator_url} for {eid}")
        if isinstance(display, str) and display and display not in readme:
            errors.append(f"README missing creator_display {display!r} for {eid}")
        named = entry.get("named_creator")
        if isinstance(named, str) and named and named not in readme:
            errors.append(f"README missing named_creator {named!r} for {eid}")
        for extra in entry.get("also_credits") or []:
            if isinstance(extra, dict) and extra.get("url") and f"]({extra['url']})" not in readme:
                errors.append(f"README missing also_credits link {extra.get('url')} for {eid}")
            if isinstance(extra, dict) and extra.get("display") and extra["display"] not in readme:
                errors.append(f"README missing also_credits display {extra.get('display')!r} for {eid}")

    extra = set(re.findall(r"<!-- catalog:([a-z0-9-]+) -->", readme)) - set(ids)
    if extra:
        errors.append(f"README markers not in catalog: {sorted(extra)}")

    errors.extend(local_markdown_targets(readme, README))
    if DETAILS.exists():
        errors.extend(local_markdown_targets(details, DETAILS))

    if errors:
        print(f"{len(errors)} validation error(s):")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print(f"ok: {len(entries)} entries, {len(ids)} ids, README coverage complete, attribution complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
