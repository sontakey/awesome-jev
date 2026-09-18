# Contributing

Add a project only when a public source shows it. Do not add something because it is novel or because an LLM said it exists.

## What belongs

- Public TypeSafe AI / Jev / System One work: software that sends state to Jev (or the official adapter) and then does something in code.
- Official docs, SDKs, cookbooks, and verified community clients.
- Related open reproductions only in the "not TypeSafe Jev" section, clearly labeled.

## What does not

- Unrelated "Jev" gaming personalities, Scala/Akka Typesafe, or TypeScript "typesafe" libraries.
- Private repos, waitlist screenshots, or "I might build this".
- Copied third-party skill bodies without license review.
- Native vision / audio / robot-control claims. Jev is text-only; other programs may OCR or transcribe first.

## Entry requirements

1. Add or edit `data/use-cases.json` via `scripts/seed_catalog.py` (keep one source of truth).
2. Every entry needs: unique `id`, `title`, `category`, `short_description`, `actual_actions_or_outcome`, `jev_role`, `origin`, `evidence_level`, at least one `sources[]` with a live `http(s)` URL, `last_checked`, `caveats`, `readiness`.
3. Every entry needs `creator_display`, `creator_url`, and `credit_kind` (`by` or `maintained-by`). Link a verified public profile. If the individual author is unknown, credit the org or account that maintains the project. Do not invent a personal name from repository ownership.
4. If you found the project through another awesome list, keep the original creator credit and name that list.
5. `evidence_level` must be one of: `code-inspected`, `demo-inspected`, `documented-example`, `author-claim`, `proposed`.
6. Do not invent install commands, latency, user counts, or success rates. Attribute vendor numbers.
7. Regenerated README must include `<!-- catalog:ID -->` for every id and a visible credited profile link.

Write list descriptions as one short sentence that says what the project does. Keep commands, names, URLs, and caveats accurate.

## Validate

```bash
python3 scripts/seed_catalog.py
python3 scripts/render_readme.py
python3 scripts/validate.py
```

`validate.py` is stdlib-only. It checks ids, source URLs, duplication, required metadata, attribution, README catalog coverage, and local Markdown links.

## License

Original curation is CC BY 4.0. Do not relicense upstream code.
