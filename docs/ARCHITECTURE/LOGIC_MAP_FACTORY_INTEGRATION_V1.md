# Logic Map Factory — WANGA / AI231 Integration Contract

**Architecture ID:** WANGA-LOGIC-MAP-FACTORY-001  
**Version:** 0.1.0  
**Status:** SPECIFIED / REPOSITORY REGISTRATION IN PROGRESS  
**Parent:** K — Lineage Knowledge & Governance  
**Execution interface:** D — Research Execution Fabric  
**Plugin ID:** `plugins_6afccd9edaf88191823ba5181aef89bc`  
**Plugin scope:** USER / PRIVATE  
**Plugin release:** `pluginrel_6afccda05618819186f9d36654bd3c92`  
**Plugin URL:** https://chatgpt.com/plugins/plugins_6afccd9edaf88191823ba5181aef89bc

## 1. Purpose

The Logic Map Factory converts supplied workbooks and source texts into source-grounded logical maps, 13-stage Mermaid diagram sequences, typed propagation rules, XL-link registers, and validation reports. It is the map-authoring and audit interface for the WANGA / AI231 logic-factory architecture.

The plugin is skills-based. It authors structured artifacts and workflow guidance. It does not, by its creation alone, provide a running simulator, execute neural processing, train models, or establish a live runtime connection to the repository or factory.

## 2. Canonical authority and placement

- Canonical map registry: `GLOBAL_ARCHITECTURE_REGISTRY.md`
- Map governance: `docs/ARCHITECTURE/LOGICAL_MAP_GOVERNANCE_V1.md`
- Agent operating contract: `.github/WANGA_AGENT_OPERATING_CONTRACT_V1.md`
- Repository: `AmbassadorOv/WANGA-LAB.-01`
- Integration branch: `integration/alf-logical-orders-20261117`

Every map package and newly introduced structural node must be registered in the canonical map. References remain subordinate to the map: `כל הריפרים כפופים למפות`.

## 3. Factory pipeline

```text
SOURCE WORKBOOKS + SOURCE TEXTS
          |
          v
SOURCE INVENTORY / PROVENANCE
          |
          v
MAP NORMALIZER
          |
          +-------------------------------+
          |                               |
          v                               v
13-STAGE DIAGRAM GENERATOR        NODE / EDGE REGISTRY
          |                               |
          +---------------+---------------+
                          |
                          v
                 PROPAGATION VALIDATOR
                          |
                          v
                    XL-LINK VALIDATOR
                          |
                          v
                 LOGIC FACTORY ADMISSION
                          |
                          v
             RESHIMU / CONTRACT VERIFICATION
                          |
                 +--------+--------+
                 |                 |
               PASS              GAP/FAIL
                 |                 |
                 v                 v
                LOCK             ABSTAIN
```

This is the specified target flow. Components are not marked implemented unless repository code and runtime evidence establish that state.

## 4. Data contract

The plugin's interchange schema is stored at:

`skills/logic-map-factory/references/map-schema.json`

Core entities:
- Map
- Workbook
- Node
- Edge
- XLLink
- Propagation
- Gap
- AuditEvent

Semantic edge types are distinct:
- `INTERNAL_LOGIC`
- `PROPAGATED_LOGIC`
- `XL_LINK`
- `LAYOUT_ONLY`

A Mermaid layout constraint is never admitted as a semantic XL Link. Each semantic edge must include direction, type, provenance, and validation state.

## 5. Workbook adapters

The intended input groups are:
1. Sentence / gates A–E workbook.
2. Inference / gates V–H workbook.
3. Definition / gates T–Y-D workbook.
4. Meta-map sources for Place, Division/Reason, Terms/Logic, and Gaps.

Exact workbook contents, sheet names, ranges, formulas, and IDs must be inspected before adapter implementation. Filenames alone do not establish workbook schema.

## 6. Required validation boundaries

- Keep source facts separate from derived relations and architecture proposals.
- Preserve `VERIFIED`, `MAPPED`, `DERIVED`, `HYPOTHESIS`, `MISSING`, `UNRESOLVED`, and `REJECTED` as distinct states.
- Do not promote a mapped edge to verified without evidence.
- Do not issue LOCK while required source evidence or acceptance rules are missing.
- Preserve `WEIGHTS = NOT_CREATED` unless the canonical contract is explicitly changed and verified.
- New structures must be entered into the canonical logical map before factory admission.

## 7. Current connection status

| Layer | Status | Evidence |
|---|---|---|
| Private plugin package | CREATED | Plugin Creator returned plugin ID and release ID |
| Plugin source files | READ-BACK VERIFIED | Plugin file listing includes manifest, skill, and JSON schema |
| WANGA integration contract | SPECIFIED | This document |
| Canonical map registration | PENDING | Requires registry commit and read-back |
| Workbook content adapters | NOT IMPLEMENTED / SOURCE INSPECTION REQUIRED | No workbook bytes inspected in this action |
| Logic-factory runtime connection | NOT CONNECTED | No runtime endpoint or integration test supplied |
| Reshimu verifier invocation | NOT RUN | No PASS output in this action |

Creation of the plugin must not be represented as a completed runtime integration.
