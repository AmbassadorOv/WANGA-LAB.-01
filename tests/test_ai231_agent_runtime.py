import unittest

from runtime.ai231_agent_runtime import build_agent_graph


def blueprint(status="active"):
    return {
        "id": "test-agent",
        "status": status,
        "mission": "Run a bounded acceptance-test task.",
        "system_instructions": "Do not exceed the declared tool and task boundaries.",
        "acceptance_tests": [{"id": "a"}, {"id": "b"}, {"id": "c"}],
        "runtime": {"isolation_required": True, "network_egress": False},
        "portability_contract": {
            "provider_dependencies": "model provider injected by caller",
            "model_adapter_interface": "provider-neutral worker interface",
            "alternative_providers_or_fallback": "test stub / degraded mode",
            "data_export_format": ["JSON"],
            "owner_controlled_source_location": "repository/runtime",
            "deployment_reproduction_steps": "pinned requirements and CI",
            "secrets_location_and_rotation": "external secret store",
            "exit_test": "replace model worker with test stub",
            "portability_status": "Assessment",
        },
    }


class AgentRuntimeGraphTests(unittest.TestCase):
    def test_active_agent_executes_and_passes_contract(self):
        def worker(bp, task):
            return {
                "deliverable": "Test deliverable",
                "evidence_status": "Assessment",
                "acceptance_tests_passed": [True] * len(bp["acceptance_tests"]),
            }
        result = build_agent_graph(worker).invoke({
            "blueprint": blueprint(),
            "task": {"title": "Test task"},
        })
        self.assertEqual(result["status"], "completed")

    def test_draft_agent_is_blocked_before_worker_runs(self):
        called = []
        def worker(bp, task):
            called.append(True)
            return {}
        result = build_agent_graph(worker).invoke({
            "blueprint": blueprint("draft"),
            "task": {"title": "Must not execute"},
        })
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(called, [])

    def test_failed_acceptance_test_requires_review(self):
        def worker(bp, task):
            return {
                "deliverable": "Partial result",
                "evidence_status": "Assessment",
                "acceptance_tests_passed": [True, False, True],
            }
        result = build_agent_graph(worker).invoke({
            "blueprint": blueprint(),
            "task": {"title": "Partial task"},
        })
        self.assertEqual(result["status"], "needs_review")
        self.assertEqual(result["failed_acceptance_tests"], [1])

    def test_worker_exception_is_recorded_as_error(self):
        def worker(bp, task):
            raise RuntimeError("controlled test failure")
        result = build_agent_graph(worker).invoke({
            "blueprint": blueprint(),
            "task": {"title": "Failure path"},
        })
        self.assertEqual(result["status"], "error")
        self.assertIn("controlled test failure", result["error"])


if __name__ == "__main__":
    unittest.main()
