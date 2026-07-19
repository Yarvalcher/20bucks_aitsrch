"""Reads data/*.yaml, renders templates/index.html.j2, writes dist/index.html."""

import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TEMPLATE_DIR = ROOT / "templates"
DIST_DIR = ROOT / "dist"


def load_tools():
    tools = []
    for path in sorted(DATA_DIR.glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            tools.append(yaml.safe_load(f))
    tools.sort(key=lambda t: t["name"].lower())
    return tools


def main():
    tools = load_tools()
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("index.html.j2")
    html = template.render(tools=tools)

    DIST_DIR.mkdir(exist_ok=True)
    (DIST_DIR / "index.html").write_text(html, encoding="utf-8")
    print(f"Built {len(tools)} tools -> {DIST_DIR / 'index.html'}")


if __name__ == "__main__":
    sys.exit(main())
