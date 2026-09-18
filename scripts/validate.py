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
)
ORIGINS = {"official", "community", "platform", "related"}
EVIDENCE = {
    "code-inspected",
    "demo-inspected",
    "author-claim",
    "documented-example",
    "proposed",
}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")


def ok_url(value: str | None) -> bool:
    if value is None:
        return True
    if not isinstance(value, str) or not value:
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


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
        if not isinstance(entry.get("other_components"), list):
            errors.append(f"{prefix} other_components must be a list")
        if not isinstance(entry.get("skill_frameworks"), list):
            errors.append(f"{prefix} skill_frameworks must be a list")
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
    for eid in ids:
        marker = f"<!-- catalog:{eid} -->"
        if marker not in readme:
            errors.append(f"README missing catalog marker for {eid}")

    extra = set(re.findall(r"<!-- catalog:([a-z0-9-]+) -->", readme)) - set(ids)
    if extra:
        errors.append(f"README markers not in catalog: {sorted(extra)}")

    if errors:
        print(f"{len(errors)} validation error(s):")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print(f"ok: {len(entries)} entries, {len(ids)} ids, README coverage complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
