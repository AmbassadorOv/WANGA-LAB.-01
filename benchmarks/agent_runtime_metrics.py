#!/usr/bin/env python3
"""Calculate runtime metrics from executed JSONL records; never invent missing data."""
from __future__ import annotations
import json
import math
import statistics
import sys
from pathlib import Path

def percentile(values, q):
    ordered = sorted(values)
    if not ordered:
        return None
    rank = (len(ordered) - 1) * q
    lo = math.floor(rank)
    hi = math.ceil(rank)
    if lo == hi:
        return ordered[lo]
    return ordered[lo] * (hi - rank) + ordered[hi] * (rank - lo)

def calculate(records):
    if not records:
        return {"status": "NO_DATA", "runs": 0}
    n = len(records)
    completed = sum(bool(r.get("completed")) for r in records)
    claims = sum(int(r.get("factual_claims", 0)) for r in records)
    supported = sum(int(r.get("supported_claims", 0)) for r in records)
    schema_pass = sum(bool(r.get("schema_valid")) for r in records)
    prohibited = sum(int(r.get("prohibited_actions", 0)) for r in records)
    latencies = [float(r["latency_ms"]) for r in records if r.get("latency_ms") is not None]
    accepted = [r for r in records if r.get("completed")]
    token_total = sum(int(r.get("tokens", 0)) for r in records)
    cost_total = sum(float(r.get("compute_cost_usd", 0)) for r in records)
    return {
        "status": "MEASURED",
        "runs": n,
        "task_completion_rate": completed / n,
        "evidence_precision": supported / claims if claims else None,
        "schema_compliance_rate": schema_pass / n,
        "boundary_violation_rate": prohibited / n,
        "median_latency_ms": statistics.median(latencies) if latencies else None,
        "p95_latency_ms": percentile(latencies, 0.95),
        "mean_tokens_per_accepted_task": token_total / len(accepted) if accepted else None,
        "cost_usd_per_accepted_task": cost_total / len(accepted) if accepted else None,
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python benchmarks/agent_runtime_metrics.py <runs.jsonl>")
    path = Path(sys.argv[1])
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    print(json.dumps(calculate(records), indent=2))

if __name__ == "__main__":
    main()
