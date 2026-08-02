---
name: scientific-performance-evaluation-statistics
version: 0.1.0
language: en
scope: performance-evaluation
purpose: Standardize the statistics of multi-round performance-evaluation outputs for process quantification, round-by-round comparison, and result traceability in the paper.
primary_inputs:
  - performance_evaluation_round<N>.yaml
  - performance_evaluation_report_round<N>.md
  - performance_review_queue_round<N>.yaml
primary_output:
  - performance_evaluation_statistics
---

# Scientific Performance-Evaluation Statistics Rules

## 0. Purpose

This rule file is used to extract reviewable and comparable process statistics from multi-round performance-evaluation outputs, with particular emphasis on the following capabilities:

1. Identifying or inferring analysis concerns when expert information is limited;
2. Registering and organizing domain tools, computational environments, and evaluation protocols;
3. Constructing and updating data-processing, statistical-analysis, and scientific-visualization tasks;
4. Producing quantitative findings based on actual data;
5. Distinguishing Skill recommendations, genuine expert recommendations, and synthesized adjustment plans;
6. Demonstrating the evolution across rounds from analysis planning and result analysis to expert-driven constraint updates.

This rule file does not use the total number of YAML fields, report word count, or software-package dependencies as primary statistical results. All counts are based on objects with independent semantics and traceable IDs.

---

## 1. Input Priority

For each round, read inputs in the following order:

1. `performance_evaluation_round<N>.yaml`: used as the primary counting basis;
2. `performance_evaluation_report_round<N>.md`: used to supplement object definitions, sources, and semantics;
3. `performance_review_queue_round<N>.yaml`: used only to verify unresolved issues and expert requirements and is not included in the current main table of the paper.

When the numbers in the YAML file and the report are inconsistent:

- Prefer the number of objects with independent IDs in the YAML file;
- Split descriptions in the report are used only for explanation and are not counted repeatedly;
- The discrepancy must be recorded in the statistical notes;
- The statistical count must not be enlarged by changing how text is split.

---

## 2. General Counting Principles

### 2.1 Independent-Object Principle

An object is counted as one item only when it has an independent objective, source, role, or output.

The following cases must not be counted repeatedly:

- The version, path, and parameters of the same tool;
- The mean, median, quantiles, and maximum of the same metric;
- The same recommendation repeated in the report and YAML file;
- Objects inherited from the previous round and not modified in the current round;
- Different file formats of the same figure;
- Intermediate files produced by the same analysis task.

### 2.2 New-in-Current-Round Principle

The main table counts objects newly added, actually executed, or substantively updated in each round.

- Fully inherited and unchanged content is not counted as newly added in the current round;
- When expert input leads to revisions of metrics, thresholds, protocols, or figures, the revision is counted as an update in the current round;
- When an item was only planned in the previous round but actual results are obtained in the current round, it is counted as actual analysis in the current round;
- When the status of the same object changes from `planned` to `executed`, it may be counted as an execution result in the current round, but it must not be counted again as a newly added tool.

### 2.3 Status-Distinction Principle

The following statuses must be distinguished:

- `planned`: proposed but not executed;
- `registered`: interface, environment, or protocol has been registered;
- `executed`: executed, or calculations have been completed on existing results;
- `updated`: revised according to new evidence or expert feedback;
- `expert_provided`: directly proposed by a genuine expert;
- `skill_inferred`: inferred by the Skill from upstream files, data, literature, or tool documentation;
- `synthesized`: formed by integrating Skill recommendations and expert recommendations.

### 2.4 Source-Traceability Principle

Each statistical value must record at least:

```yaml
statistic_trace:
  statistic_id: ""
  round: ""
  category: ""
  counted_object_ids: []
  source_files: []
  source_sections: []
  count: null
  counting_basis: ""
  exclusions: []
  notes: ""
```

Content without a clear source or for which duplication cannot be determined must not be included in the formal count.

---

## 3. Main-Table Statistical Metrics

### 3.1 Stage characteristics

**Meaning:** The primary nature of the current round within the performance-evaluation loop.

This item is a categorical description and is not accumulated numerically. It is determined from the main inputs, execution status, and newly added work in the current round.

Fixed wording for this case:

| Round | Stage characteristics |
|---|---|
| Round 1 | Analysis and visualization planning |
| Round 2 | Result-based evidence analysis |
| Round 3 | Expert-driven constraint update |

Decision rules:

- If only workflows, parameters, and plotting plans are formed, with no new result calculations: `Analysis and visualization planning`;
- If statistics, comparisons, or screening are completed based on actual execution outputs: `Result-based evidence analysis`;
- If metrics, thresholds, constraints, and subsequent plans are added or modified according to genuine expert feedback: `Expert-driven constraint update`.

---

### 3.2 Expert concerns

**Meaning:** The number of independent analysis questions directly proposed by genuine experts or explicitly inferred by the Skill in the current round.

Count separately:

```yaml
expert_concerns:
  expert_provided: 0
  skill_inferred: 0
```

Counting rules:

- If one expert message contains two independent requirements, it may be counted as two items;
- Tool names and computational environments may be counted separately when they correspond to different analysis requirements;
- Skill inference must be supported by data, upstream files, literature, or tool documentation;
- The priority, status, and explanation of the same issue are not counted separately;
- Inherited concerns that are not updated are not counted as newly added in the current round.

Counting convention for this case:

| Round | Count |
|---|---|
| Round 1 | 2 expert-provided concerns |
| Round 2 | 5 Skill-inferred concerns |
| Round 3 | 1 expert-provided concern and 4 Skill-inferred concerns |

---

### 3.3 Tool/protocol modules

**Meaning:** Domain tools, computational environments, and independent evaluation protocols registered, confirmed, or substantively updated in the current round.

To avoid ambiguity, divide them into two subitems:

```yaml
tool_protocol_modules:
  tool_or_environment_modules: 0
  evaluation_or_computational_protocols: 0
```

#### Tool or Environment Modules

Each of the following independent functional-module types counts as one item:

- Domain computational software;
- Data-processing or cheminformatics tools;
- Scheduling or cluster environments;
- Model or predictor interfaces;
- Statistical or visualization toolchains;
- Repository components with independent input-output contracts.

Dependencies, version numbers, and multiple commands of the same software are not counted separately.

#### Evaluation or Computational Protocols

A protocol with an independent scientific objective, method configuration, or scope of application counts as one item, for example:

- Geometry optimization and frequency analysis;
- TD/SOC for conventional systems;
- TD/SOC for heavy-element systems;
- Model-calibration protocol;
- Synthesizability-screening protocol.

Basis sets, core counts, memory settings, and threshold parameters within the same protocol are not counted separately.

Counting convention for this case:

| Round | Count |
|---|---|
| Round 1 | 4 tool/environment modules and 3 evaluation protocols |
| Round 2 | 10 toolchain components and 4 computational protocols |
| Round 3 | 1 additional synthesizability-evaluation protocol |

The RDKit, ORCA, and Slurm tools inherited in Round 3 are not counted again because no new toolchain was added in that round.

---

### 3.4 Analysis and visualization tasks

**Meaning:** Data-processing, statistical, comparative, and scientific-plotting tasks planned, executed, or substantively updated in the current round.

Report separately rather than merging them into one total:

```yaml
analysis_and_visualization_tasks:
  analysis_or_workflow_stages: 0
  planned_or_updated_visualizations: 0
```

#### Analysis or Workflow Stages

A step with independent inputs, actions, and outputs counts as one item, for example:

- Data loading or cleaning;
- Structural screening;
- Quantum-chemical calculation;
- Result parsing;
- Data merging;
- Descriptor calculation;
- Statistical analysis;
- Pareto analysis;
- Candidate selection.

Multiple commands or parameters within the same stage are not counted separately.

#### Planned or Updated Figures

Each figure with an independent scientific question and graphical purpose counts as one item.

- PNG, PDF, and SVG formats of the same figure count as one item;
- Merely changing a title, color, or size does not constitute a new figure;
- Adding a new metric, screening layer, expert perspective, or interpretive purpose counts as one updated figure;
- Planned figures and actually generated figures must be recorded separately;
- The current paper table uses the “number of planned or updated figures,” which does not represent the number of images actually generated.

Counting convention for this case:

| Round | Count |
|---|---|
| Round 1 | 7 analysis stages and 9 planned figures |
| Round 2 | 16 analysis stages and 5 visualization tasks |
| Round 3 | 7 analysis stages and 4 visualization updates |

---

### 3.5 Quantitative findings

**Meaning:** Categories of independent statistical, comparative, or screening results supported by actual data in the current round.

Counting rules:

- The mean, median, standard deviation, quantiles, and extreme values of the same metric are merged into one result category;
- Pass counts for the same threshold over the full sample and a subset are merged into one result;
- Different threshold conditions are counted separately;
- Different joint-screening expressions are counted separately;
- Pareto results involving different objective dimensions are counted as one explicitly defined analysis category;
- If only an analysis plan exists and no actual data are available, the count is 0;
- Figures not yet generated do not affect the counting of quantitative findings completed from tabular data;
- Pure textual speculation, literature background, or expert judgment is not counted as a quantitative finding.

Counting convention for this case:

#### Round 1

No new candidate-level results were obtained; only plans were formed:

```yaml
quantitative_findings: 0
```

#### Round 2

Count the following eight result categories:

1. Imaginary-frequency-free stable structures;
2. Absorption wavelength;
3. T1 energy;
4. S1--Ti gap;
5. Three-objective Pareto analysis;
6. LogP;
7. Molecular weight;
8. SA Score.

```yaml
quantitative_findings: 8
```

Note: The sample size, proportion, mean, median, or threshold pass rate within each category is not split further to increase the count.

#### Round 3

Count explicitly calculated thresholds or joint-screening conditions:

- SA Score thresholds: three items, `<=6.0`, `<=6.5`, and `<=7.0`;
- Molecular-weight thresholds: four items, `<=900`, `<=1000`, `<=1100`, and `<=1200`;
- Joint-screening conditions: four items.

```yaml
quantitative_findings: 11
```

The joint-screening conditions are:

1. No imaginary frequencies, `SA Score <= 6.5`, and `MW <= 1100`;
2. No imaginary frequencies, `SA Score <= 7.0`, and `MW <= 1200`;
3. No imaginary frequencies, `SA Score <= 6.5`, and absorption wavelength of 600--800 nm;
4. Add `min_positive_S1-Ti < 0.4 eV` to Condition 3.

---

### 3.6 Adjustment recommendations

**Meaning:** The number of Skill recommendations, genuine expert recommendations, and synthesized adjustment plans formed in the current round.

They must be counted separately:

```yaml
adjustment_recommendations:
  skill_generated: 0
  expert_provided: 0
  synthesized_plans: 0
```

#### Skill-Generated Recommendation

Count one item when all of the following conditions are satisfied:

- A clear adjustment objective is specified;
- An independent recommended action is specified;
- The recommendation is supported by results, figures, records, or evidence;
- It can be mapped to parameters, models, datasets, metrics, constraints, tools, workflows, or additional calculations.

The same recommendation repeated in the YAML file, report, and main-text table counts only once.

#### Expert-Provided Recommendation

A clearly stated adjustment request from a genuine expert counts as one item. The Skill’s interpretation of that request, metric mapping, and threshold derivation are not counted again as expert recommendations.

#### Synthesized Plan

Count one item when multiple recommendations are organized into a comprehensive plan with a sequence, scope of application, success criteria, or approval requirements. A simple restatement of recommendations does not count as a synthesized plan.

Counting convention for this case:

| Round | Count |
|---|---|
| Round 1 | 6 Skill-generated recommendations and 1 synthesized plan |
| Round 2 | 6 Skill-generated recommendations and 1 synthesized plan |
| Round 3 | 5 Skill-generated recommendations, 1 expert recommendation, and 1 synthesized plan |

---

## 4. Statistics Excluded from the Current Main Table

`Review items` may be counted in the appendix or internal quality checks, but they are not included in the current main table of the paper.

Reasons:

- They mainly reflect unresolved issues and the expert-review burden;
- Their number is sensitive to the granularity at which issues are split;
- The current table focuses on the proactive analysis and feedback capabilities of performance evaluation.

When counting is needed, count objects in `performance_review_queue_round<N>.yaml` that have a unique `issue_id` and a status of `open` or `deferred`; the number of high-priority issues may be reported separately.

---

## 5. Two Cross-Column Statements

Add two descriptions spanning all four columns after the main table, rather than splitting them into separate Round 1, Round 2, and Round 3 cells.

### 5.1 Round 2 autonomous computation and analysis

Fixed English wording:

> **Round 2 autonomous computation and analysis:** The Skill quantitatively analyzed 222 candidate molecules in terms of imaginary-frequency-free stable structures, absorption wavelengths, T1 energies, S1--Ti gaps, three-objective Pareto performance, LogP, molecular weight, SA Score, and the corresponding distributions and filtering results.

Meaning in Chinese:

> The Skill quantitatively analyzed the distributions and filtering results of 222 candidate molecules in terms of imaginary-frequency-free stable structures, absorption wavelengths, T1 energies, S1--Ti gaps, three-objective Pareto performance, LogP, molecular weight, and SA Score.

### 5.2 Round 3 autonomous plan formulation

Fixed English wording:

> **Round 3 autonomous plan formulation:** For the synthesizability objective, the Skill analyzed candidate-retention results under different SA Score and molecular-weight thresholds, formulated strict, relaxed, combined, and expert-exception screening schemes, and proposed synthesizability constraints for the next optimization round.

Meaning in Chinese:

> For the synthesizability objective, the Skill analyzed candidate-retention results under different SA Score and molecular-weight thresholds, formulated strict screening, relaxed screening, joint screening, and expert-exception review schemes, and proposed synthesizability-constraint recommendations for the next round.

---

## 6. Final Statistical Results for This Case

```yaml
performance_evaluation_statistics:
  round1:
    stage_characteristics: analysis_and_visualization_planning
    expert_concerns:
      expert_provided: 2
      skill_inferred: 0
    tool_protocol_modules:
      tool_or_environment_modules: 4
      evaluation_or_computational_protocols: 3
    analysis_and_visualization_tasks:
      analysis_or_workflow_stages: 7
      planned_or_updated_visualizations: 9
    quantitative_findings: 0
    adjustment_recommendations:
      skill_generated: 6
      expert_provided: 0
      synthesized_plans: 1

  round2:
    stage_characteristics: result_based_evidence_analysis
    expert_concerns:
      expert_provided: 0
      skill_inferred: 5
    tool_protocol_modules:
      tool_or_environment_modules: 10
      evaluation_or_computational_protocols: 4
    analysis_and_visualization_tasks:
      analysis_or_workflow_stages: 16
      planned_or_updated_visualizations: 5
    quantitative_findings: 8
    adjustment_recommendations:
      skill_generated: 6
      expert_provided: 0
      synthesized_plans: 1

  round3:
    stage_characteristics: expert_driven_constraint_update
    expert_concerns:
      expert_provided: 1
      skill_inferred: 4
    tool_protocol_modules:
      tool_or_environment_modules: 0
      evaluation_or_computational_protocols: 1
    analysis_and_visualization_tasks:
      analysis_or_workflow_stages: 7
      planned_or_updated_visualizations: 4
    quantitative_findings: 11
    adjustment_recommendations:
      skill_generated: 5
      expert_provided: 1
      synthesized_plans: 1
```

When displayed in the main table, write the Round 3 tool item as:

> 1 additional synthesizability-evaluation protocol

instead of displaying `0 tool modules`.

---

## 7. Main-Table Output Template

| Metric | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| Stage characteristics | Analysis and visualization planning | Result-based evidence analysis | Expert-driven constraint update |
| Expert concerns | 2 expert-provided concerns | 5 Skill-inferred concerns | 1 expert-provided concern and 4 Skill-inferred concerns |
| Tool/protocol modules | 4 tool or environment modules and 3 evaluation protocols | 10 toolchain components and 4 computational protocols | 1 additional synthesizability-evaluation protocol |
| Analysis and visualization tasks | 7 analysis stages and 9 planned figures | 16 analysis stages and 5 visualization tasks | 7 analysis stages and 4 visualization updates |
| Quantitative findings | 0 | 8 categories of quantitative results | 11 threshold-based or combined-filtering results |
| Adjustment recommendations | 6 Skill-generated recommendations and 1 synthesized plan | 6 Skill-generated recommendations and 1 synthesized plan | 5 Skill-generated recommendations, 1 expert recommendation, and 1 synthesized plan |

Append the two cross-column descriptions specified in Section 5 after the table.

---

## 8. Checklist

Before outputting statistics, confirm all of the following:

- [ ] Every count can be traced to a YAML object or an explicit item in the report;
- [ ] Inherited content has not been counted repeatedly as newly added in the current round;
- [ ] Planned tasks and actual results have been distinguished;
- [ ] Skill inference and genuine expert opinions have been separated;
- [ ] Tool modules and computational protocols have not been merged into an uninterpretable total;
- [ ] The number of planned figures has not been described as the number of images actually generated;
- [ ] Multiple descriptive statistics for the same metric have not been counted repeatedly to inflate `quantitative_findings`;
- [ ] The eight Round 2 result categories use the fixed classification;
- [ ] The eleven Round 3 results are counted as three SA thresholds, four molecular-weight thresholds, and four joint-screening conditions;
- [ ] Adjustment recommendations are counted separately as Skill-generated, expert-provided, and synthesized plans;
- [ ] The numerical values in the table are consistent with the descriptions in the main text;
- [ ] Any change in the counting convention records the version number and reason for the change.

---

## 9. Version-Update Rules

When the statistical convention changes, the version number must be updated and the change must be recorded:

```yaml
version_history:
  - version: "0.1.0"
    changes:
      - established six main paper statistics
      - excluded review items from the main table
      - fixed Round 2 quantitative findings at eight categories
      - fixed Round 3 quantitative findings at eleven threshold or combined-filtering results
      - added two cross-column explanatory rows
    reason: align statistics with the intended performance-evaluation workflow and expert-feedback design
```

The decomposition of independent objects must not be changed without updating the version and providing an explanation.
