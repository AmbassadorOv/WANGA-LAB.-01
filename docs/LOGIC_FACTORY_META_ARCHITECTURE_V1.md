# LOGIC FACTORY — Dynamic Meta-Architecture V1

**Status:** INITIAL ARCHITECTURE SPECIFICATION · NOT YET VERIFIED AS AN INTEGRATED RUNTIME  
**Primary source:** *מילות ההיגיון*, Warsaw 1928, supplied Hebrew edition and repository corpus.  
**Canonical repository:** https://github.com/AmbassadorOv/WANGA-LAB.-01

## 1. What this map is

This is a dynamic meta-architecture: one connected system that preserves source structure, contextual appearances, relations, compositions, transformations, evidence, versions, and multiple visual projections. It is not a static hierarchy, a flat node graph, or a diagram generator.

The graph is the shared structural record. Figma, GitDiagram, Mermaid, the Workbench, and repository maps are projections of that record; none of those projections may silently redefine the source.

## 2. Two counts that must never be conflated

- **Source structure:** the book contains **14 gates** and **175 named entries**, as stated in Gate 14 and represented by `milaot-hahigayon/INDEX.md`.
- **Product map structure:** **13 independent chapter maps + 1 integrated Map 14**. The product's Map 14 integrates the 13 chapter maps. It is not a replacement for Gate 14 of the book.
- **Term/entry maps:** 175 contextual records, one per indexed entry. A record can contain multiple appearances and contextual roles; do not force one global role where the source does not.
- **Pair-check space:** 175 × 175 = **30,625 ordered candidate pairs including self-pairs**. Excluding self-pairs gives 30,450 ordered pairs; unordered non-self pairs give 15,225. These are candidate checks, not established relations.

## 3. Source-grounded structure

The source register is maintained by:
- `milaot-hahigayon/INDEX.md` — 14 gate ranges and 175 numbered entries.
- `milaot-hahigayon/terms/001.md … 175.md` — individual entry records.
- `milaot-hahigayon/ORCHESTRATOR.md` — retrieval and evidence rules.

Source extraction must retain the exact wording, edition, gate, location, and appearance. A paraphrase is not a source quotation. An indexed entry is not automatically SOURCE-CHECKED or VERIFIED.

## 4. Structural ontology of the graph

Use distinct record types without turning them into new source categories:

1. **Source** — edition, document, passage, line/location.
2. **Appearance** — a particular occurrence of a term in a specific context.
3. **Term record** — stable index identity for one of the 175 entries.
4. **Role assertion** — a role assigned only within a specific appearance/context.
5. **Relation assertion** — directed or undirected relation, exact context, evidence, and status.
6. **Composition** — a source-grounded combination of components and its resulting structure.
7. **Operation** — an action applied to an existing structure, with inputs and outputs.
8. **Projection** — a view rendered in Mermaid, Figma, GitDiagram, or the Workbench.
9. **Change event** — an immutable record of a proposed or accepted change.
10. **Validation record** — tests, evidence, reviewer/agent, result, and timestamp.

Do not replace the user's exact term **עניינים** with categories, classes, entities, objects, or instances. Do not invent a category of עניינים נבדלים. Preserve the user's ontological/linguistic precision protocol as a guardrail; any claim about the five עניינים remains tagged USER PREMISE unless separately established from the exact source passage.

## 5. Dynamic movement

**SPIRAL** is a convergence operation over already identified material: gather, compare, test compatibility, and compose only where evidence supports the composition.

**VORTEX** is a divergence operation: split a structure into contextual appearances, unresolved alternatives, sub-questions, or specialist work units without erasing the parent or prior state.

They are operations on the same graph, not fixed layers or mutually exclusive worlds. Every operation records its inputs, rule, output, evidence, and reversibility.

## 6. Validation states

- `VERIFIED` — directly supported by inspected source/evidence.
- `DERIVED` — logically follows from specified supported premises.
- `HYPOTHESIS` — proposed relation or structure awaiting a test.
- `UNRESOLVED` — insufficient evidence or ambiguous source.
- `REJECTED` — conflicts with a source statement or validated constraint.

Project implementation states are separate: `SPECIFIED`, `BUILT`, `TESTED`, `DEPLOYED`. A built diagram is not proof that its logical edges are verified.

## 7. Repository ecosystem — current mapping boundary

User-supplied repository endpoints to be mapped as separate systems:
- https://github.com/AmbassadorOv/WANGA-LAB.-01
- https://github.com/AmbassadorOv/ARTIFICAL-LOGICAL-ORDERS
- https://github.com/AmbassadorOv/agent-orchestrator
- https://github.com/AmbassadorOv/Project-AI231-Miorna
- https://github.com/Quadruple-Multilevel-projection-project/WANGA-LAB
- https://github.com/Quadruple-Multilevel-projection-project/Qualia
- https://github.com/Quadruple-Multilevel-projection-project/AI231.meta.io
- https://github.com/AmbassadorOv/ROBOTICS_TRIPARTITA_Logos

The repositories are listed as ecosystem nodes because their URLs were supplied. A technical dependency, shared runtime, API integration, or data synchronization between them is **not established** until repository contents and execution paths demonstrate it.

## 8. Visual projections

- **Mermaid:** canonical text-based diagrams committed beside the specification.
- **Figma/FigJam:** editable strategic meta-map and focused submaps.
- **GitDiagram:** repository-specific code architecture. The GitDiagram connector reported no pre-generated diagram for the eight listed repositories; it supplies generation URLs but does not itself start generation.
- **Workbench:** interactive navigation across 13+1 maps, 175 entries, contextual appearances, candidate relations, and evidence.
- **Other projections:** generated from the same versioned graph data; each projection must retain a return path to its source record.

## 9. Change intake and synchronization

A prompt/rule becomes a **change candidate**, not an automatically accepted truth:
1. Capture exact text and origin.
2. Identify whether it is a source statement, user premise, derived result, hypothesis, or instruction.
3. Detect overlap/conflict with existing rules.
4. Attach affected terms, appearances, maps, repositories, and diagrams.
5. Run source/logic/consistency checks.
6. Accept, reject, or leave unresolved.
7. Commit a versioned change event.
8. Regenerate only the affected projections.
9. Preserve prior versions and the complete audit trail.

No unattended self-modification may rewrite source definitions or promote a candidate to VERIFIED.

## 10. Immediate implementation sequence

1. Treat this document and its Mermaid file as the initial architecture contract.
2. Inspect each repository's README, file tree, entry points, workflows, and API boundaries.
3. Build a repository registry with verified component paths and explicit unknowns.
4. Reconcile the 13 chapter-map contents against the 14 source gates without conflating the two numbering systems.
5. Populate contextual appearance and relation records from the 175 source entries.
6. Add deterministic validators and change-intake tests.
7. Synchronize Mermaid/Figma/Workbench projections from versioned graph data.

## 11. Diagram

See [LOGIC_FACTORY_META_ARCHITECTURE_V1.mmd](./LOGIC_FACTORY_META_ARCHITECTURE_V1.mmd).

## 12. Provenance and execution record

- Source text file: *Treatise on Logic - he - Milot Higayon, Warsaw, 1928.txt*, 237 lines, read from the supplied Project file.
- Repository index: `milaot-hahigayon/INDEX.md`, which records 175 entries across 14 gates.
- Existing Workbench: `docs/architecture-mapping-to-thinking/index.html`; its footer explicitly says chapter titles and semantic relations remain pending source alignment.
- Existing corpus atlas: `docs/LOGIC_CORPUS_MAP_ATLAS_V1.md`, marked SPECIFIED / NOT_YET_VERIFIED.

This first map is therefore a source-aware architecture specification, not a claim that the integrated graph engine or all repository connections are already implemented.


---

**Action signature**  
Timestamp: 2026-11-18T00:52:41+02:00  
Contract_Start_Time: 2026-11-17T20:29:00+02:00 *(interpreted from the user's stated 20:29 local time in the immediately preceding logic session)*  
Action_ID: LOGIC-META-MAP-001  
SHA-256: 48cd421ed20653f7627fb24aa651d1a496fcee3b18bc607eb51ce3a880c32833
