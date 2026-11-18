# מילות ההיגיון — Dynamic Logic Analytics Architecture
**Version:** 0.1.0
**Status:** SPECIFIED / IMPLEMENTATION IN PROGRESS
**Primary repository:** `AmbassadorOv/WANGA-LAB.-01`
**Source registry:** `milaot-hahigayon/INDEX.md` and `milaot-hahigayon/ORCHESTRATOR.md`

## 1. Scope boundary
This architecture belongs to the מילות ההיגיון project. It does not absorb unrelated robotics, crystal, biological, or general AI projects. External repositories and tools are integrations only when a concrete evidence-bearing dependency is established.

## 2. Source hierarchy
1. The supplied Saadia Gaon passage, The Book of Beliefs and Opinions, Treatise II, opening: the analytical object under examination.
2. Milot HaHigayon, Warsaw 1928: the source of logical tools used to test or articulate analytical structures.
3. WANGA registry: the indexed 175 term records distributed across 14 gates.
4. GitHub/Figma/GitDiagram/Canva/Airtable/AppDeploy: storage, representation, workflow and execution surfaces; never independent authorities for the source truth.

The analytic/logical distinction is mandatory:
- Analytics record: invariant wording, argument structure, distinctions, premises, conclusions, examples and limits extracted from the supplied source.
- Logic configuration: variable logical tools selected from Milot HaHigayon to represent or test part of an analytical record.
- Mapping: a versioned, evidence-bearing relation between the two. A mapping is not identity and does not prove the source claim.

## 3. Three applications
### App 1 — Logic Analytics Orchestrator
- Ingest and preserve source texts and exact locators.
- Extract atomic analytical units without changing source wording.
- Maintain the invariant analytics ledger.
- Split arguments into claims, premises, conclusions, examples, conditions, exceptions and boundaries only where the source supports the split.
- Create candidate work items for the 175 × 14 cross-index.
- Dispatch bounded analysis agents and retain their exact inputs and outputs.
Forbidden: converting an analytical unit into a logical category during extraction; inventing missing source wording; promoting a model-generated proposal to a verified fact.

### App 2 — Claim & Balance Validator
- Test each claim against its explicit premises and source context.
- Test proposed mappings in both directions: analytics to logical tool and logical tool to analytics.
- Identify contradiction, unsupported implication, missing premise, scope shift and unbalanced use of a tool.
- Preserve NO_MATCH and UNRESOLVED as valid results.
- Record what each mapping covers and what it does not cover.
Match statuses: DIRECT_TEXTUAL, STRUCTURAL_MATCH, CANDIDATE, NO_MATCH, UNRESOLVED.

### App 3 — Error Prevention & Balance Guard
- Detect source drift, term substitution, silent normalization, unsupported chapter/gate assignment and duplicate/conflicting relations.
- Ensure every displayed claim or relation has a source locator and provenance.
- Prevent analytics and logic configuration from being merged.
- Retain old relations when a new relation is proposed; version rather than overwrite.
- Block promotion when required evidence, reverse mapping or counterexample checks are missing.

## 4. Cross-index arithmetic
WANGA INDEX.md lists 175 records across 14 gates: א 001–004; ב 005–018; ג 019–023; ד 024–036; ה 037–040; ו 041–051; ז 052–063; ח 064–079; ט 080–089; י 090–107; יא 108–123; יב 124–132; יג 133–149; יד 150–175.
The cross-index has 175 × 14 = 2,450 candidate cells. Traversing it from term to gate and from gate to term is two directions over the same 2,450 cells, not 4,900 distinct source intersections. A cell becomes a verified relation only after source-level evidence and validation.

## 5. Source-grounded Saadia pilot
Source ID: S-RASAG-EMUNOT-DEOT-M2-OPENING.
The supplied passage explicitly distinguishes: faith as an inwardly established matter concerning a known thing according to its state; true and false belief; three roots of knowledge (sensible, intellectual and necessary knowledge); and a fourth root introduced by the speaker (trustworthy report). These are analytical units from Saadia. They are not automatically logical operators or terms from Milot HaHigayon. Each candidate mapping must identify the exact supporting passage in Milot HaHigayon, the part covered, and the non-match boundary.

## 6. Shared record model
Every source-backed item should carry: record_id, source_id, source_locator, exact_quote, record_layer (ANALYTICS / LOGIC_CONFIGURATION / MAPPING), status (VERIFIED / DERIVED / HYPOTHESIS / UNRESOLVED / REJECTED), created_by, created_at, version, supersedes, evidence_refs, counterexample_refs, scope_boundary. All mapping records must set analytics_mutated=false.

## 7. Agent topology
1. Source Locator Agent — retrieves exact passages and locators.
2. Analytical Extraction Agent — proposes atomic units while preserving quotations.
3. Logic Tool Matcher — proposes candidate Milot HaHigayon tools.
4. Reverse-Mapping Agent — searches for counterexamples and missing matches.
5. Claim Validator — tests premises, conclusions and scope.
6. Balance Guard — checks source fidelity, drift and unbalanced mapping.
7. Provenance Recorder — records every source, action, output and version.
Agents may propose and test. Only source-backed validation can change a record status. Execution over the proposed 4,000+ external nodes is not claimed as implemented; actual agent inventory and connected endpoints must be enumerated first.

## 8. Integration registry
- Master Plugin: top-level router; preserves the project boundary and delegates only typed records.
- Analytic–Logic Mapping Engine: invariant analytics / variable logic / bidirectional mapping.
- Logic Map Factory: diagram and map generation after source extraction; visualizations are not evidence.
- AI231 Logic Capture & Map Sync: source capture and controlled GitHub/Airtable/FigJam synchronization.
- Map Link Provenance: provenance receipts for map-to-map links.
- PCE Contract Guard: preflight and evidence checks before a contract or release is claimed complete.
- Logical Configuration Orchestrator: configuration extraction and dependency ordering.
- GitHub: versioned source registry and implementation record.
- Figma / FigJam: top-level map and interactive architecture views.
- GitDiagram: repository structure inspection; not a source-of-truth for logic.
- Canva: publication and explanatory artifacts; not a validator.
- Airtable: optional operational registry only after a dedicated base and schema are confirmed.
- AppDeploy: deploys the three application surfaces; each deployment status must be checked independently.

## 9. Runtime cycle
Source → immutable analytics ledger → candidate cross-index → forward mapping → reverse mapping → claim/balance validation → error guard → provenance receipt → versioned graph update → bounded agent dispatch → new evidence returned to the same cycle.

## 10. Status discipline
Never say verified, deployed, connected, synchronized or sealed without the corresponding tool output and test evidence. A generated map is not a deployed application; a deployed application is not a verified logical result.