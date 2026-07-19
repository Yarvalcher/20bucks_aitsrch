# $20 AI Dev Tool Search

A static, data-driven comparison of AI coding tools available for ~$20/month,
built from YAML data files rendered through a Jinja2 template. See
[docs/project_spec.md](docs/project_spec.md) for the full architecture and
[docs/tasks.md](docs/tasks.md) for status/roadmap.

## Requirements

- Python 3.12+ (project is validated against 3.12/3.13; some dependency
  syntax may not work on older versions)

## Setup

### 1. Create a virtual environment

Check installed Python versions:
```
py -0
```

Create the venv with Python 3.12+ (replace `3.12` with your installed version if newer):
```
py -3.12 -m venv .venv
```

### 2. Activate it

PowerShell:
```
.venv\Scripts\Activate.ps1
```
If you hit an execution-policy error, run once:
```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Git Bash:
```
source .venv/Scripts/activate
```

You'll know it worked when your prompt is prefixed with `(.venv)`.

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Deactivate when done

```
deactivate
```

## Usage

### Build the site

```
python build/build.py
```
Renders `data/*.yaml` through `templates/index.html.j2` into `dist/index.html`.

### Run tests

```
python -m pytest tests/ -v
```
Validates every `data/*.yaml` file against the Pydantic schema in `build/models.py`.

## Project structure

```
data/            One YAML file per tool + SCHEMA.md (field reference)
templates/       Jinja2 HTML template(s)
build/           build.py (site generator), models.py (Pydantic schema)
tests/           pytest suite validating data/*.yaml against the schema
dist/            Build output (gitignored, not committed)
docs/            Project spec and task tracking
.github/workflows/deploy.yml   CI: build + deploy to GitHub Pages on push to main
```

## Deployment

Pushes to `main` trigger a GitHub Actions build that publishes `dist/` to
GitHub Pages (requires repo Settings → Pages → Source = "GitHub Actions",
set once).
