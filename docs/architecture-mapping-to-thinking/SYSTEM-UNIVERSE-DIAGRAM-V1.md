# System Universe Diagram V1

**Status:** Initial architecture projection; links between external projects remain provisional until inspected.

```mermaid
flowchart TB
  subgraph SOURCES["SOURCE & KNOWLEDGE DOMAIN"]
    CORPUS["Milaot corpus<br/>14 gates · 175 term records"]
    RESEARCH["Research corpus<br/>editions · documents · evidence"]
    REPOS["GitHub repositories<br/>WANGA · AI231 · Logical Orders · Qualia · Robotics"]
    DESIGN["Figma board / Wix Atlas<br/>design and exploration surfaces"]
  end

  subgraph LOGIC["LOGICAL & SYMBOLIC DOMAIN"]
    TERMS["Terminology and occurrence registry"]
    STRUCT["Logical structures<br/>components · relations · compositions"]
    SYMBOLS["Symbolic / combinatorial maps<br/>231 gates · 462 directed pairs"]
    PIPELINE["Logic Architecture R&D pipeline"]
  end

  subgraph DYNAMIC["DYNAMIC MAPPING DOMAIN"]
    GRAPH[("Versioned Dynamic Knowledge Graph")]
    PROJ["Multi-paradigm projections<br/>taxonomy · network · dependency · temporal<br/>causal · compositional · analogical · topological"]
    SPIRAL["SPIRAL<br/>converge · compare · compose · validate"]
    VORTEX["VORTEX<br/>decompose · branch · specialize · investigate"]
    HISTORY["Evidence / provenance / version history"]
  end

  subgraph EXECUTION["AGENT & COMPUTATION DOMAIN"]
    FACTORY["Logic Agent Factory<br/>candidate specialist agents"]
    ORCH["Agent Orchestrator<br/>routing and coordination"]
    RUNTIME["Graph / transformation runtime<br/>events · APIs · validation"]
  end

  subgraph PRODUCT["PRODUCT & PRESENTATION DOMAIN"]
    MAPUI["Interactive System Map"]
    DIAGRAMS["Diagram and graph views"]
    FILES["Linked artifacts<br/>Markdown · JSON · CSV · XLSX"]
    DEPLOY["Application / deployment"]
  end

  SOURCES --> TERMS
  SOURCES --> STRUCT
  REPOS --> PIPELINE
  CORPUS --> TERMS
  TERMS --> GRAPH
  STRUCT --> GRAPH
  SYMBOLS --> GRAPH
  PIPELINE --> GRAPH
  GRAPH <--> PROJ
  GRAPH --> SPIRAL
  GRAPH --> VORTEX
  SPIRAL --> GRAPH
  VORTEX --> GRAPH
  GRAPH <--> HISTORY
  GRAPH --> FACTORY
  FACTORY --> ORCH
  ORCH <--> RUNTIME
  RUNTIME --> GRAPH
  GRAPH --> MAPUI
  PROJ --> DIAGRAMS
  HISTORY --> FILES
  MAPUI --> DEPLOY
  DIAGRAMS --> MAPUI
  FILES --> MAPUI
  DESIGN -. reference / reconcile .-> MAPUI

  classDef source fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
  classDef dynamic fill:#dcfce7,stroke:#16a34a,color:#14532d
  classDef execution fill:#fef3c7,stroke:#d97706,color:#78350f
  classDef product fill:#ede9fe,stroke:#7c3aed,color:#4c1d95
  class SOURCES,CORPUS,RESEARCH,REPOS,DESIGN source
  class GRAPH,PROJ,SPIRAL,VORTEX,HISTORY dynamic
  class FACTORY,ORCH,RUNTIME execution
  class MAPUI,DIAGRAMS,FILES,DEPLOY product
```

## Reading rules

- Solid arrows show proposed data or execution flow, not proof of deployed integrations.
- Dashed arrow means a design/reference surface to be reconciled against source artifacts.
- The graph is the evolving data model; diagrams are projections.
- Spiral and Vortex are operations over the graph, not static layers.
- 231 gates / 462 directed pairs are recorded as combinatorial structures only until semantic roles are source-verified.

## Execution record

- Timestamp: 2026-11-18T00:38:00+02:00
- Contract_Start_Time: 2026-11-17T20:12:00+02:00
- Action_ID: GH_CREATE_FILE_SYSTEM_UNIVERSE_DIAGRAM_V1
- SHA256: 80fd0546dc1241f9a23f642e7a25da98c0c409d3255f914d635b0804b7e0c829
