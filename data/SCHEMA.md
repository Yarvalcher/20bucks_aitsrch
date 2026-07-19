# Tool YAML schema

Each file in `data/` is one AI tool. Fields:

```yaml
id: string                    # slug, matches filename without .yaml
name: string                  # display name
vendor: string
price_summary: string         # human-readable price line, e.g. "$20/mo (Pro) | $100/mo (Max 5x)"
price_usd_month: number       # lowest entry-level $/mo price (0 if free, null if pure pay-as-you-go)
free_tier: boolean
tasks_per_month: string       # effective $20 capacity range, e.g. "150-250"
cost_per_task_usd: number     # approx, null if not applicable

models:
  - name: string
    role: string               # e.g. "Primary", "Fallback", param/context notes

interfaces:
  cli: string|null             # name/description, or null if none
  ide: string|null
  web: string|null

architecture:
  - string                     # bullet notes

benchmarks:
  - name: string                # e.g. "SWE-bench Verified"
    score: string                # keep as string, values include "~", ranges, footnotes

metering:
  - string                      # bullet notes / plan lines flattened to strings

budget_behavior:
  scale_resilience_pct: number  # 0-100
  catch: string
  strength: string

sources:
  - string                      # URLs

last_updated: date              # YYYY-MM-DD
```

Notes:
- Free-text fields keep source wording rather than forcing premature normalization
  (e.g. `cost_per_task_usd` may be null for tools billed in credits/GPU-time).
- Data is sourced from [tools-comparison-data.md](tools-comparison-data.md).
