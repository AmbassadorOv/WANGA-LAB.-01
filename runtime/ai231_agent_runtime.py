"""Bounded AI231 blueprint executor built on LangGraph.

SYS-PORTABILITY-001: injected workers must use provider-neutral model adapters;
provider credentials and APIs stay outside this graph. Keep source/data exportable
and document a tested provider exit path. This is orchestration, not a sandbox.
Execute workers in isolated runtimes with network egress denied.
"""
from __future__ import annotations

from typing import Any, Callable, TypedDict
from langgraph.graph import END, START, StateGraph

EVIDENCE = {"Verified", "Assessment", "Hypothesis", "Unresolved"}


class RunState(TypedDict, total=False):
    blueprint: dict[str, Any]
    task: dict[str, Any]
    status: str
    output: dict[str, Any]
    error: str
    failed_acceptance_tests: list[int]


Worker = Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]


def build_agent_graph(worker: Worker):
    """Compile a single-run graph. Worker must be sandboxed by its caller."""

    def validate(state: RunState) -> dict[str, Any]:
        blueprint = state.get("blueprint", {})
        required = ("id", "mission", "system_instructions", "acceptance_tests")
        missing = [field for field in required if not blueprint.get(field)]
        if missing:
            return {"status": "blocked", "error": "Missing blueprint fields: " + ", ".join(missing)}
        if blueprint.get("status") != "active":
            return {"status": "blocked", "error": "Only active blueprints may execute."}
        if len(blueprint.get("acceptance_tests", [])) < 3:
            return {"status": "blocked", "error": "At least three acceptance tests are required."}
        portability = blueprint.get("portability_contract", {})
        required_portability = ("provider_dependencies", "model_adapter_interface", "alternative_providers_or_fallback", "data_export_format", "owner_controlled_source_location", "deployment_reproduction_steps", "secrets_location_and_rotation", "exit_test", "portability_status")
        missing_portability = [field for field in required_portability if not portability.get(field)]
        if missing_portability:
            return {"status": "blocked", "error": "SYS-PORTABILITY-001 metadata missing: " + ", ".join(missing_portability)}
        if portability.get("portability_status") == "Verified" and not portability.get("exit_test_evidence"):
            return {"status": "blocked", "error": "Portability cannot be Verified without exit-test evidence."}
        runtime = blueprint.get("runtime", {})
        if runtime and (runtime.get("isolation_required") is not True or runtime.get("network_egress") is not False):
            return {"status": "blocked", "error": "Runtime policy must require isolation and deny network egress."}
        return {"status": "ready"}

    def after_validation(state: RunState) -> str:
        return "execute" if state.get("status") == "ready" else "stop"

    def execute(state: RunState) -> dict[str, Any]:
        try:
            result = worker(state["blueprint"], state["task"])
            if not isinstance(result, dict):
                raise TypeError("Worker output must be an object.")
            return {"status": "executed", "output": result}
        except Exception as exc:  # Fail closed; preserve a concise error for the report.
            return {"status": "error", "error": f"{type(exc).__name__}: {exc}"[:500]}

    def verify(state: RunState) -> dict[str, Any]:
        if state.get("status") == "error":
            return {}
        output = state.get("output", {})
        blueprint = state["blueprint"]
        tests = blueprint.get("acceptance_tests", [])
        flags = output.get("acceptance_tests_passed")
        if not isinstance(output.get("deliverable"), str) or not output["deliverable"].strip():
            return {"status": "needs_review", "error": "Worker did not return a non-empty deliverable."}
        if output.get("evidence_status") not in EVIDENCE:
            return {"status": "needs_review", "error": "Worker returned an invalid evidence status."}
        if not isinstance(flags, list) or len(flags) != len(tests) or not all(isinstance(flag, bool) for flag in flags):
            return {"status": "needs_review", "error": "Acceptance-test results must be one boolean per blueprint test."}
        failed = [index for index, passed in enumerate(flags) if not passed]
        if failed:
            return {"status": "needs_review", "failed_acceptance_tests": failed}
        return {"status": "completed"}

    graph = StateGraph(RunState)
    graph.add_node("validate", validate)
    graph.add_node("execute", execute)
    graph.add_node("verify", verify)
    graph.add_edge(START, "validate")
    graph.add_conditional_edges("validate", after_validation, {"execute": "execute", "stop": END})
    graph.add_edge("execute", "verify")
    graph.add_edge("verify", END)
    return graph.compile()
