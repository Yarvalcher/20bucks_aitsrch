# Tool YAML schema

Each file in `data/` is one AI tool. Fields:

```yaml
id: string            # slug, matches filename without .yaml
name: string           # display name
vendor: string
website: string        # URL
price_usd_month: number
free_tier: boolean
models:
  - name: string
    context_window: number   # tokens
benchmarks:
  - name: string        # e.g. "SWE-bench Verified"
    score: number        # percent or raw score
    unit: string          # "%" or "pts"
cli: boolean            # has a CLI
ide_integrations:
  - string               # e.g. "VS Code", "JetBrains"
notes: string            # free-text, optional
last_updated: date       # YYYY-MM-DD
```
