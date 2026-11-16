# AI231/WANGA System Requirement — Portability and Provider Independence

Requirement ID: SYS-PORTABILITY-001
Status: Mandatory architecture requirement
Applies to: Every existing and future AI231/WANGA development, agent, service, interface, data store, integration, deployment and deliverable.

## Normative requirement
No critical project capability may depend exclusively on ChatGPT, OpenAI, one model vendor, one cloud provider, one account, one credit system, or one proprietary user interface. The project owner must retain practical control of source code, specifications, data, agent definitions, configurations, logs, and deployment artifacts.

## Mandatory design rules
1. Provider-neutral model boundary: model calls pass through a replaceable adapter/interface; vendor APIs, prompt formats, tool schemas and response quirks remain behind adapters.
2. Replaceable inference: every model-dependent component documents another hosted provider, a self-hosted/open-weight route where feasible, or a degraded/manual fallback.
3. Owner-controlled source: canonical source, specifications, schemas and blueprints remain exportable in documented formats and owner-controlled repositories.
4. Data portability: state, memory, task history, evaluation records and configuration export to JSON/JSONL, CSV, Markdown, SQL dump or equivalent. No critical state exists only in provider conversation history.
5. Infrastructure portability: deployments are reproducible from versioned configuration and pinned dependencies; document services and avoid console-only setup.
6. Credential ownership: secrets live in owner-controlled secret management; never hard-code keys or bind project identity to a vendor account.
7. Graceful degradation: provider/account/API/credit outage preserves data, stops safely, reports failure and supports provider switching or reduced mode.
8. No credit lock-in: do not assume one vendor credit/token package; measure task cost and support budget caps and provider switching.
9. Exit test: each critical subsystem documents a portability test proving export and operation against a substitute provider or fallback. A plan is not a passed test.
10. Evidence discipline: mark portability Verified only after reproducible testing; otherwise Assessment, Hypothesis or Unresolved.

## Required component metadata
Every component specification includes provider_dependencies, model_adapter_interface, alternative_providers_or_fallback, data_export_format, owner_controlled_source_location, deployment_reproduction_steps, secrets_location_and_rotation, exit_test and portability_status. Explain non-applicability; mark unknowns Unresolved.

## Release gate
A component cannot be production-ready with a single-vendor critical dependency unless an explicit tested fallback and owner-controlled export path exist. Security, licensing, privacy and operational constraints remain mandatory.

## Enforcement
This requirement is part of definition of done for all AI231/WANGA work. Include it in agent blueprints, runtime contracts, CI checks, technical documents, relevant public project material and future repositories. Existing components must be inventoried and migrated. Do not claim universal coverage until each relevant repository and system is checked.

## Action record
Timestamp: 2026-11-16T05:28:32+00:00
Contract_Start_Time: 2026-11-16T05:28:32+00:00
Action_ID: ACT-20261116-AI231-PORTABILITY-001
SHA-256: fc7b1a469d390273269b68cfc9513ee7a4e4861da77b1cfd09a0d5580db7e42b
