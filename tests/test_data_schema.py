"""Validates every data/*.yaml file against build.models.Tool."""

from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from build.models import Tool

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
YAML_FILES = sorted(DATA_DIR.glob("*.yaml"))


@pytest.mark.parametrize("path", YAML_FILES, ids=lambda p: p.stem)
def test_yaml_matches_tool_schema(path):
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    try:
        Tool.model_validate(raw)
    except ValidationError as e:
        pytest.fail(f"{path.name} failed schema validation:\n{e}")


def test_at_least_one_data_file_found():
    assert YAML_FILES, f"No YAML files found in {DATA_DIR}"


def test_tool_id_matches_filename():
    for path in YAML_FILES:
        with open(path, encoding="utf-8") as f:
            raw = yaml.safe_load(f)
        assert raw["id"] == path.stem, (
            f"{path.name}: id '{raw['id']}' does not match filename stem '{path.stem}'"
        )
