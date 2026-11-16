# AI231 Upstream Agent Runtime Integration — v1.0

Status: **Pinned source catalog and installation profiles committed. Runtime installation and compatibility tests are not yet executed.**

## Objective
Build an executable agent-creation stack by reusing maintained open-source frameworks without surrendering AI231's blueprint contract, logic invariants, provenance, or execution boundaries.

## Selected architecture
- **LangGraph (MIT)** — primary orchestration and durable workflow/state layer.
- **Hugging Face smolagents (Apache-2.0)** — lightweight specialist workers. Any code-execution capability must be disabled or placed behind an independently verified sandbox.
- **Google ADK, Microsoft Agent Framework, Agno, CrewAI** — catalogued alternatives, not simultaneous default dependencies. Each is isolated in its own optional environment and must pass the same benchmark before adoption.

Exact upstream commit pins, package paths, license identifiers, and review notes are stored in `agent_runtime_catalog/catalog.json`.

## Installation
The default profile is installed into a new dedicated virtual environment, never into the host Python environment:

```bash
bash scripts/install_agent_runtime.sh core
```

Optional profiles:
- `bash scripts/install_agent_runtime.sh adk`
- `bash scripts/install_agent_runtime.sh microsoft`
- `bash scripts/install_agent_runtime.sh agno`

CrewAI remains catalogued but blocked from automated installation until its workspace package path is validated.

## Runtime roles being built
1. Source & License Auditor — provenance, license and supply-chain gate.
2. Agent Blueprint Architect — turns evidence-backed work units into agent blueprints.
3. Runtime Integration Engineer — prepares pinned, isolated runtime packages.
4. Agent Runtime Verifier — independently checks contracts, isolation and execution evidence.

The four versioned definitions are in `agent_blueprints/`. All are **draft**. Registration or static validation does not make an agent active.

## Execution pipeline
1. Inventory repositories and project sources.
2. Select a framework profile by measurable fit, not popularity.
3. Install into a new virtual environment using immutable commit pins.
4. Capture resolved dependency inventory.
5. Run import, smoke, policy, and task-acceptance tests.
6. Run a hostile-input and prompt-injection suite.
7. Verify filesystem/network isolation and credential boundaries.
8. Record test evidence, hashes, and runtime environment.
9. Promote only after independent verification.

## Acceptance and performance calculations
The benchmark harness must record, per task and per framework:
- task completion rate = passed tasks / executed tasks;
- evidence precision = supported factual claims / all factual claims;
- schema compliance = valid outputs / all outputs;
- boundary violation rate = prohibited actions / executed tasks;
- median and p95 latency;
- token and compute cost per accepted task;
- recovery rate after injected tool/model failures.

No target values are asserted before a baseline is measured. Safety is a hard gate: any prohibited action or network-egress violation blocks promotion, regardless of average score.

## Security and licensing
- Upstream source is treated as untrusted until reviewed.
- Commit pins are immutable; branch names are not dependency versions.
- Model weights, datasets, browser agents and arbitrary-code-execution agents are not bundled by this catalog.
- Each framework profile gets a separate environment to prevent dependency conflicts.
- Agent execution must use a real sandbox with denied network egress; a Python virtual environment alone is **not** a security sandbox.
- Review upstream license text and transitive dependency licenses before redistribution or commercial deployment.

## Current limitations
- This repository integration does not prove packages have been downloaded or installed.
- No WANGA-X, LNL Model Builder, Wix, or private runtime adapter is claimed as connected.
- No runtime acceptance benchmark has yet been executed.
- The core profile is a selected integration candidate, not a verified production stack.


## Executable orchestration and measurement
- `runtime/ai231_agent_runtime.py` provides a LangGraph state machine: validate active blueprint → invoke an injected worker → verify deliverable/evidence status/acceptance-test vector → complete or require review.
- Draft and malformed blueprints are blocked before worker invocation. Worker exceptions are recorded as errors. Failed acceptance tests produce `needs_review`, never automatic activation.
- The graph is an orchestration layer, **not** a sandbox. The worker must run in an external isolated environment with network egress denied.
- `benchmarks/agent_runtime_cases.json` defines initial task and security cases. `benchmarks/agent_runtime_metrics.py` computes completion, evidence precision, schema compliance, boundary violations, median/p95 latency, tokens and cost per accepted task.
- An empty run dataset produces `NO_DATA`; no performance values are fabricated.
- CI now installs the two pinned core frameworks in a clean Python 3.11 virtual environment, imports them, compiles and invokes a minimal LangGraph, and runs executor/metrics unit tests.

## Mandatory system requirement: portability and provider independence
All components in this integration are governed by [SYS-PORTABILITY-001](../contracts/SYS-PORTABILITY-001.md). The model provider is a replaceable dependency, not the system owner or system of record. Agent state, task history, blueprints, configuration and evaluation records must be exportable. Provider credentials must be owner-controlled. Every critical runtime must document a tested substitute provider or degraded mode and a reproducible exit test. Current status: requirement committed; implementation coverage and provider-switch tests remain NOT YET VERIFIED.
