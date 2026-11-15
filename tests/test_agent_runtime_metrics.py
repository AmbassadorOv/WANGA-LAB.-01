import unittest
from benchmarks.agent_runtime_metrics import calculate


class RuntimeMetricsTests(unittest.TestCase):
    def test_empty_data_does_not_fabricate_scores(self):
        self.assertEqual(calculate([]), {"status": "NO_DATA", "runs": 0})

    def test_metrics_use_observed_records(self):
        result = calculate([
            {"completed": True, "factual_claims": 2, "supported_claims": 2, "schema_valid": True, "prohibited_actions": 0, "latency_ms": 100, "tokens": 100, "compute_cost_usd": 0.01},
            {"completed": False, "factual_claims": 2, "supported_claims": 1, "schema_valid": False, "prohibited_actions": 1, "latency_ms": 300, "tokens": 80, "compute_cost_usd": 0.02},
        ])
        self.assertEqual(result["task_completion_rate"], 0.5)
        self.assertEqual(result["evidence_precision"], 0.75)
        self.assertEqual(result["schema_compliance_rate"], 0.5)
        self.assertEqual(result["boundary_violation_rate"], 0.5)
        self.assertEqual(result["median_latency_ms"], 200)
        self.assertEqual(result["mean_tokens_per_accepted_task"], 180)

if __name__ == "__main__":
    unittest.main()
