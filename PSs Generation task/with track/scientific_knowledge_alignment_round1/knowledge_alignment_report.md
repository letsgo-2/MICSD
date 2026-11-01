# Scientific Knowledge Alignment — Round 1

## 1. Project goal and evidence
Goal: develop candidate molecules with improved photosensitizing performance. This run covers all 47 Markdown files under `markdown/`, including supplementary-information files. Paper evidence is primary; ontology sources only normalize terminology.

## 2. Core concept system
The concepts below are project-level alignments. `pending` means the mapping or boundary still requires expert confirmation.

| concept_id | name | definition | mapping_status | expert_status |
|---|---|---|---|---|
| C001 | Photosensitizer | A light-absorbing molecular agent used in the supplied papers to initiate photochemical or photodynamic effects; the exact operational boundary varies by paper. | close | pending |
| C002 | Photodynamic therapy | A treatment modality combining a photosensitizer, light, and molecular oxygen or other photochemical reactants to produce biologically active species; condition-specific mechanisms must be retained. | close | pending |
| C003 | Reactive oxygen species | Reactive oxygen-containing chemical species discussed as photochemical effectors; the corpus includes singlet oxygen and other species, but does not justify treating all ROS as interchangeable. | close | pending |
| C004 | Type-I and Type-II photochemistry | Two mechanistic labels used in the papers for photochemical generation of reactive species; the exact species and oxygen dependence are system- and condition-dependent. | close | pending |
| C005 | Pyroptosis | A lytic regulated cell-death phenotype associated in the corpus with gasdermin pores and inflammatory signaling; pathway assignment requires assay-specific confirmation. | close | pending |
| C006 | Structure-property-mechanism-performance relationship | A project-level relation connecting molecular architecture, photophysical/biological properties, proposed mechanism, and measured outcome under stated conditions. | local | pending |

## 3. Core indicator system
All directions are conditional on the listed assay context. Scores are provisional 1–5 values and are intentionally not treated as expert-approved.

| indicator_id | name | optimization_role | optimization_direction | importance | computability | data_readiness | priority | expert_status |
|---|---|---|---|---|---|---|---|---|
| I001 | Singlet oxygen quantum yield (ΦΔ) | primary_objective | maximize | 5 | 4 | 3 | P0 | pending |
| I002 | Absorption maximum and usable absorption | secondary_objective | target_range | 4 | 5 | 4 | P0 | pending |
| I003 | Photodynamic potency / light-induced cytotoxicity | primary_objective | minimize | 5 | 3 | 2 | P1 | pending |
| I004 | Dark toxicity / dark IC50 | constraint | minimize | 5 | 3 | 2 | P1 | pending |
| I005 | Photostability | secondary_objective | maximize | 4 | 3 | 1 | P1 | pending |
| I006 | Aggregation / aqueous dispersibility | constraint | minimize | 4 | 3 | 2 | P1 | pending |
| I007 | Subcellular localization / target engagement | intermediate | target_range | 4 | 2 | 2 | P2 | pending |
| I008 | Oxygen dependence / hypoxia performance | constraint | context_dependent | 5 | 3 | 2 | P1 | pending |
| I009 | Fluorescence quantum yield / excited-state lifetime | diagnostic | context_dependent | 3 | 4 | 2 | P2 | pending |
| I010 | Irradiation fluence and exposure time | feature_only | none | 5 | 5 | 3 | P0 | pending |

## 4. Domain-expert view
Domain interpretation should focus on whether the proposed molecular change actually changes the relevant excited-state pathway, ROS identity, localization, and phenotype under matched experimental conditions. The strongest recurring design hypotheses are: cationic/targeting motifs can alter organelle enrichment; electronic structure and aggregation alter photophysics; type-I/type-II labels imply different oxygen dependencies; and biological endpoints cannot be inferred from a single photophysical metric. All such relationships remain pending validation.

## 5. Computer-expert optimization view
Treat observations as molecule–condition–assay records, not molecule-only labels. Primary candidates are ΦΔ/ROS output and light-induced potency, but efficacy must be paired with dark toxicity and exposure conditions. Absorption is a P0-compatible secondary objective; aggregation, oxygen dependence, and photostability are constraints or conditional objectives. Fluorescence/lifetime and localization are diagnostic/intermediate until comparable datasets and mechanistic definitions are available.

### Optimization targets
{
  "primary": [
    "I001",
    "I003"
  ],
  "secondary": [
    "I002",
    "I005"
  ],
  "constraints": [
    "I004",
    "I006",
    "I008"
  ],
  "intermediate": [
    "I007"
  ],
  "diagnostic": [
    "I009"
  ],
  "not_ready": [
    "I003",
    "I004",
    "I005",
    "I006",
    "I007",
    "I008",
    "I009"
  ]
}

## 6. Structure–property–mechanism–performance relationships

| claim_id | subject | relation | object | claim_type | confidence | expert_status |
|---|---|---|---|---|---|---|
| K001 | Cationic substitution / charge pattern | promotes | I007 mitochondrial or organelle localization | correlation | medium | pending |
| K002 | Molecular architecture and electronic/photophysical properties | correlates_with | I001 singlet oxygen or ROS output | mechanism | medium | pending |
| K003 | Mitochondrial localization plus local ROS generation | promotes | C005 pyroptotic or other regulated-cell-death phenotype | causal | medium | pending |
| K004 | Type-I photochemistry | is_proxy_for | I008 lower oxygen dependence | hypothesis | low | pending |
| K005 | Aggregation | tradeoff_with | I001 photochemical output and I003 biological potency | mechanism | medium | pending |


## 7. Evidence and conflicts
The generated machine-readable file contains 1016 keyword-localized evidence excerpts and a complete 47-source inventory. Cross-paper comparisons are not normalized automatically because solvent, oxygenation, wavelength, fluence, cell line, incubation, and assay definitions differ. Reported IC50/ROS/ΦΔ values must therefore not be ranked across papers without harmonization.

## 8. Importance and priority
P0: absorption and exposure metadata are operationally ready; ΦΔ is potentially P0 but needs method harmonization. P1: biological potency, dark toxicity, photostability, aggregation, and oxygen dependence need matched data or explicit protocols. P2: localization and excited-state diagnostics support mechanism interpretation. P3: none are promoted automatically to task orchestration until expert review is complete.

## 9. Expert certification state
No object is approved in Round 1. Required reviewers: materials/photochemistry expert for definitions, importance, direction, and mechanism; experimental expert for assay conditions and comparability; computational expert for computability and cost; computer expert for task-role assignment.

## 10. Pending evidence and decisions
See `expert_review_queue.yaml`. Unresolved items include exact ontology IDs, assay-normalized metric definitions, Type-I/Type-II assignment, whether each reported ROS signal is singlet oxygen versus another species, structure identity/tautomer/protonation state, and pathway-specific interpretation of pyroptosis markers.

## 11. Candidates eligible for task orchestration
None are fully eligible before expert certification. Provisional candidates for review are I001 and I002; I003 and I004 remain blocked by cross-paper assay heterogeneity; I010 is required metadata rather than a molecular target.

## Appendix: ontology sources
| term | source | url | status | note |
|---|---|---|---|---|
| photosensitizer / photodynamic therapy / photophysical terms | IUPAC Gold Book | https://goldbook.iupac.org/ | authority identified; exact term-level mapping requires expert check | Direct term endpoint access was unavailable during this run; no exact definition was asserted. |
| chemical entity and reactive species classes | ChEBI | https://www.ebi.ac.uk/chebi/ | authority identified; exact IDs pending | Use exact ChEBI IDs only after term-level confirmation. |
| regulated cell death and pyroptosis | Gene Ontology / Cell Ontology | https://geneontology.org/ | authority identified; exact process mapping pending | Pathway labels in papers must not be treated as ontology-equivalent without assay review. |
| chemical structure identifiers | PubChem | https://pubchem.ncbi.nlm.nih.gov/ | authority identified; compound-level mapping pending | The supplied Markdown does not consistently provide machine-readable structures. |

