# Logical Map Governance and Four-Point Timestamp Handshake

**Architecture ID:** WANGA-LOGICAL-MAP-GOVERNANCE-001  
**Version:** 1.0.0  
**Status:** SPECIFIED / IMPLEMENTATION NOT YET VERIFIED  
**Parent:** K — Lineage Knowledge & Governance  
**Execution interface:** D — Research Execution Fabric  
**Canonical map:** `GLOBAL_ARCHITECTURE_REGISTRY.md`  
**Action ID:** `ACT-WANGA-MAP-4C0E3E4356A6`  
**Contract_Start_Time:** `2026-11-17T20:25:15+00:00` (UTC)

## 1. Mandatory map-admission rule

Every new structure, agent group, application connection, workflow, registry, service, or architecture component must be entered into the canonical logical map at the same time it is proposed or created. A structure without a map node and explicit parent/dependency links is not admitted as part of the architecture.

The map entry must identify, where applicable:

- stable `architecture_id` / `node_id`;
- exact name and purpose;
- parent map node and child/dependency nodes;
- source repository/path or external system;
- inputs, outputs, interfaces, and references;
- status and validation state;
- provenance, change history, and timestamp signature.

Do not create a parallel map for a component already owned by an existing map. Extend the canonical map and preserve earlier versions.

## 2. Logical map invariants

1. **מפה לוגית** is the structure containing repositories, Excel files, applications, markers, relations, links, and references.
2. **שעון מפה לוגית** is the map's time mechanism. It synchronizes component states according to changes in the map and its links. It is not an event clock or a generic timeline.
3. **כל הריפרים כפופים למפות** — every reference derives its position and validity from the logical map.
4. A map change updates dependent instructions and relations.
5. A component change updates the map while preserving the source and complete change history.
6. A reference whose target is not verified remains unresolved; names or apparent similarity do not establish a valid link.

## 3. AI231 Logic Operations collaboration structure

**Node ID:** `AI231-LOGIC-OPERATIONS`  
**Purpose:** coordinate work across the GitHub, Notion, Figma, Airtable, Gmail, and Gemini surfaces without merging their authority or falsely representing integrations as active.

| Node | Intended responsibility | Current evidence / state |
|---|---|---|
| GitHub | Canonical technical source, schemas, version history, verification | Repository and target branch identified |
| Notion | Work records and durable documentation | Connector available; target page/database not yet linked |
| Figma | Visual maps and interface artifacts | Connector available; target file not yet linked |
| Airtable | Structured agent/task/data registers | Connector available; target base/table not yet linked |
| Gmail | Communication and agent correspondence | Gmail labels/sub-labels supported; actual Google Groups not available through current connector |
| Gemini | Optional coordination/model interface | Direct account integration and permissions UNRESOLVED |

### Authority boundary

Gemini, if connected later, is a worker/coordination interface only. It does not become the source of truth, approver, or authority to rewrite architecture. GitHub's canonical map and the explicit approval record govern structure changes. A Gmail label is not a Google Group; no Google Group or Gemini connection is claimed as created.

### Required connection lifecycle

`DISCOVER -> IDENTIFY TARGET -> VERIFY CONNECTOR/AUTH -> MAP NODE -> AUTHORIZE -> CONNECT -> TEST -> RECORD RESULT`

Unavailable or unverified connections remain `UNRESOLVED`; they must not be displayed as connected.

## 4. Four-point timestamp handshake

Each action carries the same immutable `Contract_Start_Time` and `Action_ID` through four locations. Each location records its own event timestamp when that transition actually occurs.

| Stage | Location | Required record | Initial state |
|---|---|---|---|
| 1 | `REQUEST_ORIGIN` | Origin of the request; start timestamp; action ID | RECORDED |
| 2 | `MAP_RECEIVER` | Map node receiving the start link; exact target path/ref; receipt timestamp | PENDING_MAP_WRITE |
| 3 | `APPROVAL_NODE` | Identity/role of approver; approval decision; approval timestamp | APPROVED_BY_EXPLICIT_USER_INSTRUCTION |
| 4 | `RETURN_TO_ORIGIN` | Return to the same origin that sent the request; result/evidence link; return timestamp | PENDING_RETURN |

Every stage record must contain:
- `Timestamp` — the exact ISO 8601 time of that stage's event;
- `Contract_Start_Time` — the immutable start time, repeated unchanged at all four locations;
- `Action_ID` — the same unique action identifier across the round trip;
- `Stage_ID`, `Status`, `Source_Ref`, `Target_Ref`, and `SHA256`.

The SHA-256 signature is calculated over canonical UTF-8 JSON containing at minimum `Timestamp`, `Contract_Start_Time`, and `Action_ID`, plus `Stage_ID`, `Status`, and the action payload. A missing or invalid signature makes that stage `BLOCKED`; it is not entered as a completed log event. Do not fabricate timestamps for stages that have not occurred.

### Current action record

**Action:** Integrate this collaboration structure and the mandatory map-admission rule into the WANGA logical maps.

| Stage | Timestamp | Contract_Start_Time | Status | SHA-256 |
|---|---|---|---|---|
| REQUEST_ORIGIN | `2026-11-17T20:25:15+00:00` | `2026-11-17T20:25:15+00:00` | RECORDED | `bac3259bf674c6aca15bbc3775839a46bec63908f6b113b2b578b0493f13afd3` |
| MAP_RECEIVER | PENDING — record after GitHub map write | `2026-11-17T20:25:15+00:00` | PENDING_MAP_WRITE | PENDING |
| APPROVAL_NODE | `2026-11-17T20:25:15+00:00` | `2026-11-17T20:25:15+00:00` | APPROVED_BY_EXPLICIT_USER_INSTRUCTION | `6f426ebcb040366d869b0db1972855930a2c3055e7b1a4cdbc6e3e1260810dbe` |
| RETURN_TO_ORIGIN | PENDING — record when result is returned to this request origin | `2026-11-17T20:25:15+00:00` | PENDING_RETURN | PENDING |

**Request origin:** this ChatGPT conversation turn.  
**Map receiver:** `AmbassadorOv/WANGA-LAB.-01` → `docs/ARCHITECTURE/LOGICAL_MAP_GOVERNANCE_V1.md`.  
**Approver:** explicit user instruction in this conversation.  
**Return destination:** the same ChatGPT conversation turn that originated the request.

## 5. Change propagation and audit

- Every map update records the changed node, prior version/ref, new version/ref, source, timestamp, and dependent nodes.
- The map clock evaluates which dependent references and instructions must be re-read or invalidated.
- No dependent reference is silently rewritten; the old target and transition remain in history.
- The final action state is `SUCCEEDED` only after all four timestamp stages have valid signatures and the resulting map entry has been fetched and checked.
- A Git commit alone is not proof of runtime integration, connector authorization, or successful synchronization.

## 6. Implementation boundary

This document defines the required architecture and audit protocol. It does not assert that a live logical-map clock, cross-app synchronization service, Google Groups, or Gemini connection is already running. Those require separate implementation and verification evidence.
