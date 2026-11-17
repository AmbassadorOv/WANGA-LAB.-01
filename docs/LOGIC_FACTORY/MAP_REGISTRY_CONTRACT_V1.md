# Map Registry Contract v1

**Status:** PROPOSED / INITIAL DATA ONLY / NOT RUNTIME-VERIFIED  
**Contract ID:** MAP-REGISTRY-CONTRACT-V1  
**Purpose:** Establish one canonical, auditable registry for logical maps, source artifacts, references, and dependent views.

## 1. Authority and non-claims

The registry is the canonical index of declared artifacts and their observed revisions. It does not make an artifact true, verified, synchronized, or executable merely by registering it.

A registry entry proves only that a specific artifact reference and revision were recorded. It does not prove semantic correctness, source authority, successful runtime integration, or live synchronization.

## 2. Required identity fields

Every registered artifact MUST have:
- `artifact_id`: immutable stable identifier.
- `artifact_type`: SOURCE, MAP, TERM_INDEX, GATE_DATA, PIPELINE, APPLICATION, WORKBOOK, DIAGRAM, or SCHEMA.
- `canonical_uri`: exact repository path or external URL.
- `repository` and `path` when hosted in Git.
- `revision`: Git commit SHA and/or blob SHA; external resources use a provider revision when available, otherwise null.
- `content_sha256`: SHA-256 of the retrieved bytes when computed; otherwise null (never substitute a Git blob SHA).
- `observed_at`: ISO-8601 timestamp with timezone.
- `evidence_status`: VERIFIED, DERIVED, HYPOTHESIS, UNRESOLVED, or REJECTED.
- `operational_status`: ACTIVE_REFERENCE, STALE, MISSING, or NOT_RUNTIME_VERIFIED.
- `depends_on`: artifact IDs, not display names.
- `change_policy`: MANUAL_REVIEW or AUTOMATED_CHECK.

## 3. Change-record protocol

A source change MUST create an append-only change record containing:
1. change_id and observed_at;
2. artifact_id and previous/new revision;
3. previous/new content hash, when available;
4. actor or detection mechanism;
5. affected artifact IDs and references;
6. validation results and unresolved checks;
7. disposition: ACCEPTED, REJECTED, or NEEDS_REVIEW.

No existing change record is overwritten. Corrections create a superseding record.

## 4. Dependency and propagation rules

- Dependencies are explicit directed edges: `dependent_artifact_id -> dependency_artifact_id`.
- A revision change marks all transitive dependents STALE until checked.
- A dependent is not marked current merely because its URL still resolves.
- Excel/XL links, Figma, Canva, Wix, and GitDiagram are consumer views. They must resolve canonical references from this registry rather than become competing authorities.
- External application synchronization is NOT IMPLEMENTED until a successful integration event, resulting revision, and read-back check are recorded.

## 5. Logical map clock

The logical map clock is a monotonic registry sequence, not wall-clock time.

It advances only after:
1. a change record is appended;
2. affected dependencies are computed;
3. stale flags are applied;
4. required validations are recorded.

The wall-clock timestamp is retained separately as `observed_at`. A failed or incomplete update does not advance the clock.

## 6. Validation and LOCK boundary

Allowed evidence statuses:
- VERIFIED: direct source evidence and required tests are recorded.
- DERIVED: mechanically derived from identified inputs and reproducible rules.
- HYPOTHESIS: proposed interpretation or architecture.
- UNRESOLVED: insufficient or conflicting evidence.
- REJECTED: contradicted by evidence or failed required checks.

LOCK is allowed only for the exact artifact revision whose required source, dependency, and validation checks pass. Otherwise the operation returns ABSTAIN. A later revision invalidates the prior LOCK for that revision.

## 7. Initial implementation boundary

Version 1 is a declarative registry contract and seed dataset. It is not yet a watcher, webhook, scheduler, Excel connector, Figma plugin, Wix runtime, or distributed synchronization service.

Runtime implementation requires, at minimum:
- schema validation;
- append-only change log;
- Git revision polling or webhook ingestion;
- dependency traversal;
- stale propagation;
- deterministic validation runner;
- read-back verification for every external connector.

## 8. Acceptance tests

1. Duplicate `artifact_id` is rejected.
2. Missing canonical URI or revision provenance is rejected or explicitly null with reason.
3. Git blob SHA is never labelled as content SHA-256.
4. Any changed dependency marks transitive dependents STALE.
5. A URL resolving does not clear STALE.
6. Clock sequence advances only after a complete change record and dependency update.
7. LOCK fails closed when any required dependency is STALE, UNRESOLVED, or NOT_RUNTIME_VERIFIED.
8. Every displayed status can be traced to a recorded source revision and validation event.

## 9. Initial source set

The initial seed registry is in `MAP_REGISTRY_V1.json`. Its entries reflect only files inspected from the repository default branch during initial registry construction. They do not claim that linked external applications are connected.
