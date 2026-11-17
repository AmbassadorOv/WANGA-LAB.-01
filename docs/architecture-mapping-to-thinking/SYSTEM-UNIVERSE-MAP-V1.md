# System Universe Map V1
## Architecture Mapping to Thinking — Logical Deep Reasoning

**Status:** INITIAL / PARTIALLY SOURCE-INSPECTED  
**Model:** Dynamic, multi-paradigm, provenance-preserving architecture graph.

## 1. System purpose

The target capability is not merely a diagram generator and not merely an LLM-agent workflow. It is a system for extracting, representing, relating, validating, transforming, and operationalizing logical structures. Agent networks are execution units coordinated through these structures; diagrams are navigable projections of the evolving model.

## 2. System universe — functional domains

| Domain | Responsibility | Known anchors | Verification state |
|---|---|---|---|
| Source corpus | Preserve editions, texts, locations, and variants | Milaot records; research corpus | Partial |
| Terminological architecture | Track 175 terms and 14 gates with occurrence-specific roles | milaot-hahigayon/INDEX.md; ORCHESTRATOR.md | Index inspected; individual records pending |
| Logical structure | Represent components, relations, compositions, definitions, and distinctions | Gate 10; source-grounded logic records | Partial; source spans required |
| Symbolic/combinatorial mapping | Represent letter nodes, pair gates, directed transitions, triples | LETTER_GATE_MAP_231_V1.json | Enumeration inspected; semantics unassigned |
| Logic architecture R&D | Move from research need to candidate architecture, formalization, prototype, evidence, verification, configuration | FUTURE_LOGIC_ARCHITECTURE_PIPELINE.md | File inspected; pipeline is specified |
| Agent execution | Route tasks to specialized logic agents and orchestrators | agent-orchestrator (supplied URL) | Repository not yet inspected |
| Computational runtime | Store graph, execute transformations, validate invariants, emit events | Proposed implementation domain | Proposed, not verified as existing |
| Visual mapping | Render system, dependency, term, temporal, and paradigm projections | Figma board; GitDiagram; Wix atlas | Links supplied; content not yet inspected here |
| Knowledge operations | Manage records, files, evidence, and structured registries | Notion; Airtable; repository data | Integration candidates; not verified |
| Product/deployment | Package, publish, deploy, and manage the application | GitHub; AppDeploy; Wix | Integration candidates; not verified |
| Commercial/payment | Support future billing if product requirements establish it | Stripe | Optional external capability; not part of logical core |

## 3. Multi-paradigm projections

The same underlying graph may be projected through different analytical lenses. A projection must declare its own semantics and must not overwrite the underlying source model.

1. **Containment / taxonomic:** whole-part, genus-species, inclusion, and hierarchy where supported by the source.
2. **Network / graph:** nodes, typed edges, paths, neighborhoods, and connected components.
3. **Dependency:** which artifacts, conclusions, agents, or views depend on a given node or relation.
4. **Temporal / versioned:** states, revisions, provenance, and change history.
5. **Causal / process:** preconditions, actions, outcomes, and causal claims only when evidenced.
6. **Compositional:** valid constructions from components and their roles.
7. **Analogical:** explicitly declared correspondences between structures in different domains; analogy is not identity.
8. **Topological / spatial:** adjacency and spatial embedding as a representation hypothesis, requiring invariants and tests.
9. **Meta-structural:** rules governing extraction, mapping, validation, and transformation.

## 4. Dynamic architecture — two transformation patterns

### Spiral: convergence and integration

Input: multiple source-grounded entities or subgraphs.  
Operations: compare identity and role; detect compatible relations; preserve distinctions; compose a larger candidate structure; validate it; publish a new graph version.

Spiral does not mean that different terms or systems are merged merely because they look similar. It produces a candidate integration with explicit evidence and unresolved boundaries.

### Vortex: differentiation and branching

Input: a node, relation, contradiction, gap, or complex subgraph.  
Operations: decompose by context; branch competing interpretations; assign focused investigations; create child subgraphs; test each branch; return results and provenance to the parent graph.

Vortex does not delete the original structure. It creates traceable branches.

### Coupled cycle

`Source event → extraction → graph update → projection → gap/contradiction detection → Spiral or Vortex transformation → validation → versioned graph update`

The graph is both the current map and the input to the next mapping operation.

## 5. Dynamic behavior requirements

- Stable entity IDs; names and labels may change without losing identity.
- Relations are typed, contextual, directional where appropriate, and independently versioned.
- Each claim has evidence status: SOURCE_OBSERVED, DERIVED, HYPOTHESIS, UNRESOLVED, or REJECTED.
- Each transformation records input graph version, operation, actor/agent, output graph version, evidence, and validation.
- Changes trigger dependency analysis and invalidate only affected projections or conclusions.
- Multiple incompatible interpretations may coexist as branches.
- Every projection can navigate back to source entities and evidence.
- Import/export formats include JSON, CSV, XLSX, and Markdown; exported files retain stable IDs and provenance.
- No automated agent may silently promote a hypothesis to a verified source fact.

## 6. Core data flow

```text
Sources and repositories
        ↓
Source adapters / parsers
        ↓
Evidence and entity registry
        ↓
Dynamic knowledge graph
        ↔ typed relations and version history
        ↓
Multi-paradigm projection engine
        ↓
Spiral convergence / Vortex branching
        ↓
Logic-agent task planning and orchestration
        ↓
Validation, test evidence, and review
        ↓
Versioned graph update and refreshed views
```

## 7. Existing-source anchors and constraints

- The 175-term index assigns records 001–175 across 14 gates. Gate י is records 090–107.
- The Milaot orchestrator requires retrieval of individual term records and source checking before VERIFIED status.
- The Logic Corpus Atlas defines 10 macro maps × 10 submap lenses, but marks the atlas SPECIFIED / NOT_YET_VERIFIED.
- The 231 map describes K22 combinatorics: 231 unordered pairs and 462 ordered distinct pairs. Its vertex semantic roles are UNASSIGNED. The map explicitly distinguishes 1,540 unordered triples from 9,240 ordered triples without repetition.
- The future logic pipeline defines research → emerging need → architectural gap → candidate → logic family → formalization → prototype → evidence → verification → configuration → bundle → future agent interface. It is specified as an R&D pipeline, not proof of a deployed runtime.

## 8. Open mapping obligations

1. Inspect all 175 term files and build occurrence-level nodes and links.
2. Inspect all 14 gate source records and preserve source order, terminology, and evidence.
3. Inspect all listed repositories and identify actual dependencies, code modules, workflows, and shared artifacts.
4. Inspect the Figma board and compare it against repository artifacts.
5. Inspect the Wix Logic Corpus Atlas and determine which parts are live, which are generated, and which are merely specified.
6. Map the agent-orchestrator implementation and distinguish actual agent execution from proposed logic-agent architecture.
7. Validate cross-repository relations before marking them as implemented integrations.
