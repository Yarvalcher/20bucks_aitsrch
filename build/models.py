"""Pydantic models mirroring data/SCHEMA.md."""

from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class Model(BaseModel):
    name: str
    role: str


class Interfaces(BaseModel):
    cli: Optional[str] = None
    ide: Optional[str] = None
    web: Optional[str] = None


class Benchmark(BaseModel):
    name: str
    score: str


class BudgetBehavior(BaseModel):
    scale_resilience_pct: int
    catch: str
    strength: str


class Tool(BaseModel):
    id: str
    name: str
    vendor: str
    price_summary: str
    price_usd_month: Optional[float] = None
    free_tier: bool
    tasks_per_month: str
    cost_per_task_usd: Optional[float] = None

    models: List[Model]
    interfaces: Interfaces
    architecture: List[str]
    benchmarks: List[Benchmark]
    metering: List[str]
    budget_behavior: BudgetBehavior
    sources: List[str]

    last_updated: date
