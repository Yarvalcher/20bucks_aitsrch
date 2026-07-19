# Project Spec — $20 AI Dev Tool Search

## Purpose

A static, data-driven site that compares AI coding tools available for ~$20/month
(or less), so a developer can pick the right tool per project phase instead of
overpaying for one general-purpose subscription.

Source research lives in [tools-comparison-data.md](../tools-comparison-data.md) —
10 tools evaluated (Google Antigravity 2.0, Kimi K2.7 Code, Cursor AI, VS Code +
Kiro, Ollama Cloud, GitHub Copilot, Microsoft Copilot, OpenAI Codex, Claude Code,
Ollama Local) on price, models, benchmarks, and "$20 budget behavior" (how cost
scales as a project grows).

## Audience

Solo/small-team developers deciding which AI coding tool(s) to subscribe to on a
tight budget.

## Architecture

Static site generator pattern, no backend, no database:

```
data/            One YAML file per tool (schema in data/SCHEMA.md)
templates/       Jinja2 HTML template(s)
build/build.py   Reads data/*.yaml -> renders templates/*.j2 -> writes dist/
dist/            Build output (gitignored, not committed)
.github/workflows/deploy.yml   CI: build + deploy dist/ to GitHub Pages on push to main
```

Why this shape:
- ~10 records, changing monthly at most — a YAML file per record *is* the
  database.
- YAML over Markdown: the data is structured (prices, benchmark scores, model
  lists), not prose — YAML maps to it natively and diffs cleanly in git.
- No AWS: GitHub Pages is free and sufficient for a static comparison table;
  S3+CloudFront was considered and rejected as unnecessary cost/complexity for
  this traffic profile.

## Data model

See [data/SCHEMA.md](../data/SCHEMA.md) for the authoritative field list. Each
tool YAML currently covers: vendor, price/month, free tier, models + context
windows, benchmark scores, CLI/IDE availability, and a `last_updated` date.

The richer detail captured in `tools-comparison-data.md` (architecture notes,
metering tables, "$20 budget behavior" scale-resilience scores, sources) is not
yet represented in the YAML schema — see tasks.md for the gap.

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) builds on every push to `main`
and publishes `dist/` via GitHub Pages. Requires: repo Settings → Pages → Source
= "GitHub Actions" (one-time manual step, not yet confirmed done).

## Out of scope (for now)

- Live pricing API integration (data is manually curated/verified per tool)
- User accounts, comments, or interactivity beyond static filtering/sorting
- Non-$20-tier tools (anything without a sub-$20 or pay-as-you-go path)
