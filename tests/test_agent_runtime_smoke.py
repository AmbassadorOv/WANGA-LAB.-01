"""Non-model smoke tests for the pinned AI231 agent runtime dependencies."""
import unittest

class RuntimeSmokeTests(unittest.TestCase):
    def test_smolagents_import(self):
        import smolagents
        self.assertTrue(hasattr(smolagents, "__name__"))

    def test_langgraph_builds_and_runs_state_graph(self):
        from typing import TypedDict
        from langgraph.graph import END, START, StateGraph

        class State(TypedDict):
            value: int

        graph = StateGraph(State)
        graph.add_node("increment", lambda state: {"value": state["value"] + 1})
        graph.add_edge(START, "increment")
        graph.add_edge("increment", END)
        app = graph.compile()
        result = app.invoke({"value": 1})
        self.assertEqual(result["value"], 2)

if __name__ == "__main__":
    unittest.main()
