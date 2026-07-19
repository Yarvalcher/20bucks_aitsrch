# Tasks

Status legend: ✅ done · 🔄 in progress · ⬜ not started

## Completed

- ✅ **Research: comparison data for 10 AI dev tools** — [tools-comparison-data.md](../tools-comparison-data.md)
  documents pricing, models, benchmarks, architecture, metering, and "$20
  budget behavior" for each tool, plus a summary leaderboard and a suggested
  multi-tool rotation strategy. Last verified 2026-07-19.
- ✅ **Git repo initialized and pushed to GitHub** — `https://github.com/Yarvalcher/20bucks_aitsrch`,
  public, `main` branch tracked.
- ✅ **`.gitignore` created** — excludes `.claude/settings.local.json`,
  `node_modules/`, `.env`, `*.log`, `dist/`.
- ✅ **Repo scaffolding: YAML + Jinja2 + build script**
  - `data/SCHEMA.md` — field reference for tool YAML files
  - `data/example-tool.yaml`, `data/example-tool-2.yaml` — placeholder entries
  - `build/build.py` — reads `data/*.yaml`, renders `templates/index.html.j2` to `dist/index.html`
  - `templates/index.html.j2` — basic sortable-by-eye comparison table
  - `requirements.txt` — pyyaml, jinja2
  - Verified locally: `python build/build.py` runs and produces `dist/index.html`
- ✅ **GitHub Actions deploy workflow** — [.github/workflows/deploy.yml](../.github/workflows/deploy.yml),
  builds with Python 3.12 and deploys `dist/` to GitHub Pages on push to `main`.
- ✅ **Project documentation** — this file and [project_spec.md](project_spec.md).

- ✅ **Extend YAML schema to capture full research detail** — `data/SCHEMA.md`
  now models architecture notes, metering, scale-resilience %, catch/strength,
  and sources.
- ✅ **Convert real tool data from `tools-comparison-data.md` into YAML** — all
  10 tools now have real YAML files in `data/`: `google-antigravity.yaml`,
  `kimi-k2-7-code.yaml`, `cursor-ai.yaml`, `vscode-kiro.yaml`,
  `ollama-cloud.yaml`, `github-copilot.yaml`, `microsoft-copilot.yaml`,
  `openai-codex.yaml`, `claude-code.yaml`, `ollama-local.yaml`. Placeholder
  files removed. Template (`templates/index.html.j2`) updated to render the
  richer schema; verified locally with `python build/build.py` (10 tools
  built).

## In progress

- 🔄 None currently.

## Not started

- ⬜ **Enable GitHub Pages in repo settings** — Settings → Pages → Source =
  "GitHub Actions". Required before the deploy workflow's output is reachable
  at a public URL.
- ⬜ **Improve template** — add sorting/filtering by price, scale-resilience
  score, or benchmark; render the summary leaderboard and suggested rotation
  strategy from `tools-comparison-data.md`.
- ⬜ **Decide on data refresh cadence** — tools-comparison-data.md is manually
  verified; define how often it (and the YAML files) get re-checked against
  vendor pricing pages.
- ⬜ **Commit current scaffolding** — `.gitignore` fix, `data/`, `build/`,
  `templates/`, `.github/`, `requirements.txt`, and `docs/` are created
  locally but not yet committed/pushed.
