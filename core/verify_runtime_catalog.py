#!/usr/bin/env python3
"""Static checks for pinned external agent runtimes; no network or code execution."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "agent_runtime_catalog" / "catalog.json"
PORTABILITY_CONTRACT = ROOT / "contracts" / "SYS-PORTABILITY-001.md"
ALLOWED_LICENSES = {"MIT", "Apache-2.0"}

def main():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    frameworks = data.get("frameworks")
    assert isinstance(frameworks, list) and frameworks, "framework catalog is empty"
    ids = set()
    for item in frameworks:
        assert item["id"] not in ids, f"duplicate framework id: {item['id']}"
        ids.add(item["id"])
        assert re.fullmatch(r"[0-9a-f]{40}", item["commit"]), f"unpinned commit: {item['id']}"
        assert item["license"] in ALLOWED_LICENSES, f"license requires review: {item['id']}"
        assert item["repo"].count("/") == 1, f"invalid repository: {item['id']}"
        assert item["package_path"], f"missing package path: {item['id']}"
    core = set(data["selection_assessment"]["core"])
    assert core == {"langgraph", "smolagents"}, "unexpected core profile"
    assert data["policy"]["floating_refs_allowed"] is False
    assert data["policy"]["agent_network_egress"] is False
    policy = data["policy"]
    assert policy.get("system_requirements") == ["SYS-PORTABILITY-001"]
    assert policy.get("provider_neutral_model_adapter_required") is True
    assert policy.get("owner_controlled_source_required") is True
    assert policy.get("data_export_required") is True
    assert policy.get("replaceable_inference_required") is True
    assert policy.get("exit_test_required") is True
    assert policy.get("single_vendor_critical_dependency_allowed") is False
    assert PORTABILITY_CONTRACT.is_file(), "mandatory portability contract is missing"
    print("PASS: external runtime catalog structure")
    print(f"PASS: {len(frameworks)} frameworks use immutable commit pins")
    print("PASS: license allowlist (MIT / Apache-2.0)")
    print("PASS: core profile and fail-closed network policy")
    print("PASS: mandatory provider-independence and portability policy")
    print("NOTE: static metadata checks only; no package install, SBOM, sandbox or runtime tests")

if __name__ == "__main__":
    main()
