# 科研知识对齐报告：第二轮更新

生成时间：2026-07-17  
轮次：round2  
对应第一轮文件：`knowledge_alignment_report.md`、`knowledge_alignment.yaml`、`expert_review_queue.yaml`。  
第二轮目标：在第一轮“知识基本确认无误”的基础上，补充光敏剂优势骨架与特性分析，并为计算机专家提供更清晰、可进入迭代优化框架的 DFT/数值可计算指标、计算方式和 reward 初始阈值建议。

## 1. 项目目标与输入证据

项目目标仍为开发具有更高光敏性能的候选分子。第二轮不覆盖第一轮结果，而是形成独立增量补充。材料专家已确认第一轮知识基本无误，并提出新增需求：

- 补充光敏剂优势骨架及特性分析。
- 将需要生物实验测量的指标与可由 DFT/TD-DFT 或数值计算得到的指标区分。
- 为计算机专家明确哪些性能指标可用于迭代优化框架、如何计算、reward 设计可采用哪些初始阈值。

第二轮新增或强化证据：

| evidence_id | 来源 | 证据定位 | 用途 |
|---|---|---|---|
| R2-E001 | `2015_Machacek_Far-Red-Absorbing-Cationic-Phthalocyanine-Photosensitizers.md` | lines 25-31, 96-116, 276-319 | Pc/ZnPc Q-band、ε、聚集、取代位置、PET 风险 |
| R2-E002 | `2013_Makhseed_Water-Soluble-Non-Aggregating-Zinc-Phthalocyanine-for-PDT.md` | lines 39-45, 77-107 | 水溶性非聚集 ZnPc、ε、ΦΔ、EC50/TC50 |
| R2-E003 | `2021_Wu_Activation-of-Pyroptosis-by-Membrane-Anchoring-AIE-Photosensitizer.md` | lines 39-55, 61 | AIE D-A'-pi-A 骨架、阳离子链、膜锚定 |
| R2-E004 | `2021_Peng_Intramolecular-Charge-Transfer-Conjugated-Oligomer-with-Photodynamic-and-Photothermal-Activities.md` | lines 9-17 | D-A-D 共轭寡聚物、ICT、ISC、ROS、低 bandgap、光热 |
| R2-E005 | `2024_Yi_Mitochondria-Targeting-Type-I-Photodrug-for-Pyroptotic-Oncotherapy.md` | lines 45-58 | Nile-blue Type-I 光药、660 nm 吸收、SOC/FMO、640 nm 自由基、线粒体靶向 |
| R2-E006 | `2022_Su_CAIX-Anchored-Rhenium-Photosensitizer-Evokes-Pyroptosis.md` | lines 29-33 | Re(I) CAIX 锚定光敏剂、缺氧下 Type-I/II PDT、纳摩尔光毒性 |
| R2-E007 | `2022_Su_CAIX-Anchored-Rhenium-Photosensitizer-Evokes-Pyroptosis_SI.md` | lines 93-99 | Re(I) 光稳定性 HPLC 条件、DFT/TDDFT 方法 |
| R2-E008 | `2023_Zhang_Copper-Bacteriochlorin-Nanosheet-as-a-Specific-Pyroptosis-Inducer.md` | lines 9-21 | Cu-bacteriochlorin nanosheet、750 nm、O2.-、OH、1O2、GSH 激活 |
| R2-E009 | `2021_Chen_Gadolinium-Porphyrin-Polymer-Nanotheranostics-for-Imaging-Guided-PDT.md` | lines 15-30 | Gd-porphyrin polymer、FL/MR、1O2、稳定性/分散性/生物相容性 |
| R2-E010 | `2014_Odeh_Targeting-Mitochondria-by-ZnII-N-Alkylpyridylporphyrins.md` | lines 3-10 | Zn-alkylpyridylporphyrin、烷基链长度与线粒体摄取/亚定位/光损伤 |
| R2-O001 | TD-DFT porphyrinoid PDT review, Molecules 2021, DOI 10.3390/molecules26237176 | web evidence | TD-DFT 可预测吸收、ISC、T1-S0、SOC；600-800 nm；0.98/1.13 eV；描述符 |
| R2-O002 | Type-I PS design review, Advanced Science 2024, DOI 10.1002/advs.202413365 | web evidence | Type-I 间接/直接设计、T1 能量、S1-Tn <0.4 eV、ET 策略 |
| R2-O003 | Rational Design of Type-I Photodynamic Agents, Angew. Chem. 2025, DOI 10.1002/anie.202509416 | web evidence | Type-I 热力学/动力学设计、redox potential、K_ET 与 K_EnT |
| R2-O004 | IUPAC Gold Book | O04339, E02250, RT06783, I03199, E01977, RT07472 | oscillator strength、excitation energy、redox potential、ionization energy、electron affinity、Rehm-Weller equation |

## 2. 核心概念体系

第二轮新增概念用于把“骨架选择”和“DFT reward 指标”接入第一轮概念体系。

| concept_id | 概念 | 定义 | 来源 | 映射 | 认证状态 |
|---|---|---|---|---|---|
| R2-C001 | 优势光敏剂骨架 | 在论文证据中反复与长波吸收、高 ROS、低聚集、靶向或低氧适用性相关的分子核心或可修饰平台。 | local；R2-E001 至 R2-E010 | local | pending |
| R2-C002 | Porphyrinoid / 卟啉类光敏骨架 | 包括 porphyrin、phthalocyanine、chlorin、bacteriochlorin 等大环或相关体系，常用于 PDT。 | R2-E001, R2-E002, R2-E008, R2-E009, R2-O001 | close | pending |
| R2-C003 | D-A / D-A-D / D-A-pi-A 光敏骨架 | 由电子给体、受体和共轭桥调控 ICT、吸收、ISC 和 Type-I/II ROS 的有机光敏骨架。 | R2-E003, R2-E004, R2-O002 | local | pending |
| R2-C004 | 计算代理指标 | 不能直接等同于生物实验终点，但可由 DFT/TD-DFT/数值方法计算并用于预测或筛选光敏性能的中间指标。 | R2-O001 至 R2-O004 | local | pending |
| R2-C005 | reward 初始阈值 | 用于迭代优化框架的初始打分边界；来自文献阈值或项目启发式，不等同于已认证验收标准。 | R2-O001 至 R2-O003 | local | pending |

## 3. 核心指标体系

第二轮把指标分为三类：

- **实验终点指标**：例如 ΦΔ、ROS 探针、EC50、暗毒性、细胞定位，需要实验确认。
- **DFT/TD-DFT 可计算代理指标**：可作为生成/筛选循环的主 reward 或中间 reward。
- **数值/规则可计算约束**：例如分子量、形式电荷、cLogP、重原子/金属标记、拓扑平面性代理。

| indicator_id | 指标 | 计算方式 | 优化角色 | 方向 | 初始阈值/打分建议 | 重要性 | 可计算性 | 数据准备度 | 优先级 |
|---|---|---|---|---|---|---:|---:|---:|---|
| R2-I001 | S0->S1 吸收波长 λabs | TD-DFT 垂直激发能换算 λ=1240/E(eV)，取主要可见/NIR跃迁 | primary/secondary | target_range | 600-800 nm 给高分；650-750 nm 可作为 PDT 初始甜点区；>800 nm 需检查 f 和 T 能级 | 5 | 5 | 4 | P0 |
| R2-I002 | oscillator strength f | TD-DFT 输出主要跃迁 f | secondary_objective | maximize | 同一骨架内排序；f 接近 0 的暗态不宜作为吸收主峰 reward | 4 | 5 | 4 | P0 |
| R2-I003 | T1-S0 能隙 E(T1) | TD-DFT/TDA 或 ΔSCF；同一方法比较 | branch_objective | context_dependent | Type-II: >0.98 eV，溶液保守用 >1.13 eV；Type-I 抑制 Type-II 可考虑 <0.98 eV | 5 | 4 | 3 | P0 |
| R2-I004 | S1-Tn 能隙 ΔE(S1,Tn) | TD-DFT 多态计算，找与 S1 能量接近且 SOC 非零的 Tn | intermediate | minimize | <0.4 eV 作为高 ISC 候选启发式；必须结合 SOC | 5 | 4 | 3 | P0 |
| R2-I005 | SOC(S1,Tn) | ORCA/Q-Chem/Gaussian 等自旋轨道耦合计算 | intermediate | maximize | 不设通用绝对阈值；同一方法/骨架内越大越好 | 5 | 3 | 2 | P1 |
| R2-I006 | 估算 ISC 倾向分数 | combine: small ΔE(S1,Tn), high SOC, orbital-type change | intermediate | maximize | reward = rank(SOC) + penalty(ΔE>0.4 eV)；需专家校准 | 5 | 3 | 2 | P1 |
| R2-I007 | HOMO/LUMO 能级与 gap | DFT frontier orbitals | feature/intermediate | context_dependent | gap 对 λabs 作粗代理；不可单独作为性能目标 | 3 | 5 | 4 | P2 |
| R2-I008 | 电荷转移程度 / ICT 指标 | NTO、hole-electron distance、CT number、HOMO-LUMO 分离 | intermediate | target_range | 适度 ICT 促进红移/ISC/Type-I；过强 ICT 可能降低 f 或增加非辐射衰减 | 4 | 3 | 2 | P1 |
| R2-I009 | 电子转移自由能 ΔG_ET | redox potentials + excitation energy；Rehm-Weller 近似 | primary for Type-I | minimize / negative | ΔG_ET < 0 作为热力学可行；过负可能不等于高效，需动力学校准 | 5 | 3 | 2 | P1 |
| R2-I010 | 氧还原/底物氧化匹配 | excited-state redox potential vs O2/substrate potentials | constraint/intermediate | satisfy | Type-I 需 PS* 能抽取电子且后续可将电子转给 O2；具体阈值需指定参比电极/介质 | 5 | 2 | 1 | P1 |
| R2-I011 | 溶剂化自由能/偶极矩 | implicit solvent DFT 或快速物性估算 | constraint/feature | target_range | 用作水相可用性/极性代理；不能替代实验水溶性 | 3 | 4 | 2 | P2 |
| R2-I012 | cLogP/logS 估算 | RDKit/ADMET 工具/经验模型 | constraint | target_range | 初始筛选用，阈值需按给药方式确认；避免极端疏水导致聚集 | 4 | 5 | 3 | P1 |
| R2-I013 | 平面性/π-π聚集风险代理 | 共轭核心平面性、SASA、长轴面积、芳香环数、二聚相互作用能 | constraint | minimize risk | Pc/porphyrinoid 需惩罚高平面疏水未取代结构；可用取代位阻/电荷抵消 | 4 | 3 | 2 | P1 |
| R2-I014 | 形式电荷/阳离子基团数 | 结构规则计数 | scaffold_constraint | context_dependent | 阳离子可提高水溶性/膜或线粒体定位，但过多可能增暗毒性 | 4 | 5 | 4 | P1 |
| R2-I015 | 重原子/金属风险标记 | 元素/金属中心规则 | constraint/diagnostic | context_dependent | Br/I/Se/Re/Gd/Cu 可提升 SOC/功能，但暗毒性和转化风险需惩罚或分支处理 | 4 | 5 | 4 | P1 |

## 4. 领域专家知识视图

### 4.1 优势骨架及特性分析

| 骨架/平台 | 优势特性 | 主要风险 | 可调结构位点 | 论文证据 | 认证状态 |
|---|---|---|---|---|---|
| ZnPc / phthalocyanine | 强 Q-band、长波吸收、可高 ΦΔ、ε 高；非外周取代可红移 | 水溶性差、π-π 聚集降低 PDT；某些 PET 会淬灭激发态 | 非外周/外周取代、阳离子基团、刚性大位阻、中心金属 | R2-E001, R2-E002 | confirmed_by_domain_basic; thresholds pending |
| 水溶性非聚集 ZnPc | 兼具水溶、非聚集、高 ε、高 ΦΔ、低 nM EC50 和低暗毒性案例 | 合成复杂；同一策略对其他 Pc 是否通用需确认 | 十六阳离子咪唑、刚性 bulky 取代 | R2-E002 | pending |
| Porphyrin / metalloporphyrin polymer | 成熟 PDT 大环平台，可与金属/聚合物形成 theranostic 系统；FL/MR/1O2 | 纳米化后结构-性质归因复杂；生物分布需实验 | 金属中心、meso 取代、聚合/自组装、亲水壳层 | R2-E009, R2-E010 | pending |
| Bacteriochlorin / Cu-bacteriochlorin | 长波/750 nm 激活潜力，Cu/GSH 激活可组合化学 ROS 与 PDT | 纳米片/金属释放机制不等价于小分子光敏剂；安全性需审查 | 金属中心、GSH 响应、纳米片组装 | R2-E008 | pending |
| Nile-blue Type-I photodrug | 660 nm NIR 吸收、640 nm 下 Type-I 自由基；可端基功能化靶向线粒体 | 结构空间较窄；Type-I 指标需自由基探针确认 | 端基靶向基团、线粒体阳离子/亲脂调控 | R2-E005 | pending |
| Re(I) 金属配合物 | 金属中心促进激发态/ROS；CAIX 锚定、缺氧下 Type-I/II、高光毒性 | 金属相关暗毒性、代谢和转化风险；合成/配位稳定性 | 配体、靶向基团、金属中心、光稳定性 | R2-E006, R2-E007 | pending |
| AIE D-A / D-A-pi-A | 聚集态仍可发光/产 ROS；D-A 结构调控 ICT/ISC；阳离子链增强膜锚定 | 过强阳离子/膜锚定可能增加暗毒性；焦亡机制非通用目标 | donor/acceptor、π桥、阳离子链数、扭曲程度 | R2-E003 | pending |
| D-A-D 共轭寡聚物 | ICT 导致红光发射、增强 ISC 和 ROS；低 bandgap 可带来光热协同 | 光热与光动力贡献需分开；抗菌场景与肿瘤场景不同 | donor/acceptor 强度、共轭长度、BODIPY 核 | R2-E004 | pending |

领域专家补充结论：

- 若项目目标偏 **Type-II PDT**，优先从 ZnPc/Pc、porphyrin/chlorin/bacteriochlorin 类骨架出发，主看 λabs、ε、ΦΔ、聚集和水相稳定性。
- 若项目目标偏 **缺氧 Type-I PDT**，优先考虑 D-A/AIE、Nile-blue、低 T1 能级或 ET 增强骨架，主看 T1-S0、S1-Tn、SOC、redox/ΔG_ET、Type-I 自由基实验确认。
- 若项目目标偏 **焦亡/免疫治疗**，靶向膜/线粒体/CAIX 的定位能力和局部 ROS 释放是场景指标，不应直接作为通用“高光敏性能”唯一目标。

## 5. 计算机专家优化指标视图

### 5.1 可直接进入迭代优化框架的 DFT reward 草案

| reward_name | 输入 | 计算方式 | reward 方向 | 初始阈值 | 是否可立即使用 | 注意事项 |
|---|---|---|---|---|---|---|
| R_abs_window | TD-DFT excitation energy, oscillator strength | 对主要跃迁换算 λ；筛选 f 非零跃迁 | target_range | 600-800 nm；650-750 nm 高分区 | yes | >800 nm 需确认光源和 f；<600 nm 组织穿透弱 |
| R_abs_intensity | oscillator strength f | 同一方法/骨架内 rank-normalize | maximize | 无绝对阈值；f 过低惩罚 | yes | f 与 ε 相关但不等同实验 ε |
| R_typeII_energy | E(T1)-E(S0) | T1-S0 能量 | target/min threshold | >0.98 eV；溶液保守 >1.13 eV | yes for Type-II branch | 需同一方法校准；不同泛函不可混排 |
| R_typeI_block_EET | E(T1)-E(S0) | 判断是否低于氧敏化阈值 | maximize Type-I selectivity | <0.98 eV 倾向抑制 Type-II | yes for Type-I branch | 低 T1 可能增加非辐射衰减，需配合 ET/SOC |
| R_ISC_gap | min ΔE(S1,Tn) | TD-DFT 多态搜索 | minimize | <0.4 eV 给高分 | yes | 必须结合 SOC，否则可能是假阳性 |
| R_SOC | SOC(S1,Tn) | SOC 计算 | maximize | 无通用阈值；同骨架排名 | partial | 计算成本较高，先用于 top candidates |
| R_ET_thermo | ΔG_ET | Rehm-Weller 或 redox + excitation energy | negative/favorable | ΔG_ET < 0 | partial | 需定义 donor/acceptor/substrate、介质和电极参比 |
| R_CT_balance | NTO/hole-electron/CT descriptor | 电荷转移强度 | target_range | 适中；过低不利 ICT，过高可能降 f | partial | 需项目数据校准 |
| R_solubility_proxy | logS/cLogP/dipole/solvation | 快速数值模型或 DFT 溶剂化 | target_range | 暂不设硬阈值 | partial | 只作实验水溶性代理 |
| R_aggregation_penalty | planarity/aromatic area/charge/bulky substituent | 规则或二聚相互作用 | minimize risk | 平面疏水大环未带位阻/电荷时惩罚 | partial | 聚集需实验光谱确认 |
| R_toxicity_risk | heavy atom/metal/formal charge/reactive group | 结构规则 | minimize risk | I/Br/Se/Re/Gd/Cu 标记；高阳离子数标记 | yes as diagnostic | 不等同真实毒性 |

### 5.2 推荐 reward 分支

不要把所有候选分子放入一个单一 reward。建议按机制分支：

```yaml
reward_profiles:
  type_II_PDT:
    primary: [R_abs_window, R_abs_intensity, R_typeII_energy, R_ISC_gap]
    secondary: [R_SOC, R_solubility_proxy]
    penalties: [R_aggregation_penalty, R_toxicity_risk]
  hypoxia_type_I_PDT:
    primary: [R_abs_window, R_ISC_gap, R_ET_thermo, R_typeI_block_EET]
    secondary: [R_SOC, R_CT_balance]
    penalties: [R_aggregation_penalty, R_toxicity_risk]
  scaffold_refinement:
    primary: [R_abs_window, R_abs_intensity]
    secondary: [R_ISC_gap, R_CT_balance, R_solubility_proxy]
    penalties: [R_aggregation_penalty]
```

### 5.3 计算流程建议

第一层快速筛选：

- 结构合法性、分子量、形式电荷、重原子/金属标记、芳香平面性、cLogP/logS。
- 半经验或轻量 DFT 几何优化。

第二层 TD-DFT 主筛选：

- S0 几何优化。
- TD-DFT 计算低能 singlet/triplet states。
- 输出 λabs、f、E(T1)、ΔE(S1,Tn)、NTO/CT 描述符。

第三层高成本复核：

- 对 top candidates 计算 SOC、redox potentials、ΔG_ET、溶剂效应。
- 对机制分支分别排序，不跨机制直接比较综合分。

## 6. 结构-性质-机制-性能关系

| claim_id | 主体 | 关系 | 客体 | 类型 | 证据 | 置信度 | 认证 |
|---|---|---|---|---|---|---|---|
| R2-K001 | 非聚集水溶性 ZnPc | promotes | 高 PDT 活性 | causal | R2-E002 | high | pending |
| R2-K002 | Pc 非外周取代 | promotes | Q-band 红移 | correlation/mechanism | R2-E001 | medium | pending |
| R2-K003 | PET 供体取代 | inhibits | ΦΔ/ΦF | mechanism | R2-E001 | medium | pending |
| R2-K004 | AIE D-A-pi-A + 阳离子链 | promotes | 聚集态 ROS 与膜锚定 | causal/correlation | R2-E003 | medium | pending |
| R2-K005 | ICT D-A-D 共轭骨架 | promotes | ISC、ROS 和长波发射 | mechanism | R2-E004 | medium | pending |
| R2-K006 | Nile-blue Type-I 骨架端基靶向 | promotes | 线粒体定位与 Type-I 光损伤 | causal/correlation | R2-E005 | medium | pending |
| R2-K007 | T1-S0 高于氧单线态阈值 | enables | Type-II 1O2 生成 | mechanism | R2-O001 | high | pending |
| R2-K008 | T1-S0 低于氧单线态阈值 | inhibits | Type-II EET 并偏向 Type-I | mechanism | R2-O002, R2-O003 | medium | pending |
| R2-K009 | ΔE(S1,Tn) <0.4 eV + SOC | promotes | ISC | heuristic/mechanism | R2-O002 | medium | pending |
| R2-K010 | ΔG_ET <0 | indicates | Type-I ET 热力学可行 | mechanism | R2-O002, R2-O003, R2-O004 | medium | pending |

## 7. 证据与冲突

第二轮确认：骨架选择不能只按“哪类文献效果最好”排序，而应按机制分支排序。

- Pc/ZnPc/porphyrinoid 类：证据强，适合 Type-II 或混合 PDT，计算上有成熟 TD-DFT 评价路径。
- AIE D-A 类：适合解决聚集和定位问题，也适合 Type-I/缺氧方向，但 reward 必须纳入 CT、ET 和聚集态效应。
- 金属配合物/金属纳米平台：性能强但安全性、代谢和可生成性风险更高，应与纯有机小分子分开评分。
- 焦亡相关性能是治疗机制指标，不是普适光敏性能指标；用于特定应用分支。

冲突与限制：

- `T1-S0 >0.98/1.13 eV` 与 `T1-S0 <0.98 eV` 分别服务 Type-II 和 Type-I 分支，不能同时作为同一 reward 的硬目标。
- `SOC 越大越好` 只在其他条件满足时成立；重原子/金属提升 SOC 也可能提升暗毒性风险。
- `ICT 越强越好` 不成立；过强 CT 可能降低 oscillator strength 或增加非辐射衰减。
- cLogP/logS/偶极矩不能替代实验水溶性和聚集测试，只能作为早期代理。

## 8. 指标重要性与优先级

P0：可立即进入计算迭代框架的指标：R2-I001、R2-I002、R2-I003、R2-I004。它们可由 TD-DFT 直接得到，有明确物理含义，并有文献阈值或强排序意义。

P1：建议进入第二层或 top-candidate 复核：R2-I005、R2-I006、R2-I008、R2-I009、R2-I012、R2-I013、R2-I014、R2-I015。它们重要，但需要方法、阈值或机制分支确认。

P2：作为辅助特征而非单独 reward：R2-I007、R2-I011。HOMO/LUMO gap、偶极和溶剂化可解释趋势，但不能单独定义高光敏性能。

## 9. 专家认证状态

领域专家已确认第一轮知识基本无误。第二轮新增内容仍需认证：

- 材料专家：优势骨架排序、是否允许金属/重原子、Type-I 与 Type-II 分支权重。
- 计算专家：DFT 方法、泛函/基组、溶剂模型、SOC/redox 计算软件和成本。
- 计算机专家：reward 是否按机制分支拆分、阈值是否作为软 reward 而非硬过滤。
- 实验专家：λabs、ΦΔ、Type-I ROS、聚集、水溶性和光毒性实验校准数据。

## 10. 待补证据与待决问题

- 确定项目主分支：Type-II 高 1O2、缺氧 Type-I、双 Type-I/II，还是焦亡免疫治疗。
- 确定候选空间是否包含 Re/Gd/Cu 等金属配合物或纳米平台。
- 用一小批已知分子校准 TD-DFT 方法误差，尤其 λabs、T1-S0、SOC。
- 为 cLogP/logS、形式电荷、阳离子数、平面性代理设置项目阈值。
- 明确 reward 阈值是软打分、硬过滤还是仅用于排序解释。

## 11. 可进入任务编排阶段的指标清单

可进入下一阶段任务编排的计算指标草案：

```yaml
ready_for_orchestration:
  P0_computable:
    - R2-I001: TD-DFT absorption wavelength / excitation energy
    - R2-I002: oscillator strength
    - R2-I003: T1-S0 energy gap, branch-specific threshold
    - R2-I004: minimum S1-Tn energy gap
  P1_computable_after_method_setup:
    - R2-I005: SOC
    - R2-I009: electron-transfer free energy
    - R2-I012: cLogP/logS proxy
    - R2-I013: aggregation-risk proxy
  not_as_single_objective:
    - R2-I007: HOMO/LUMO gap
    - R2-I011: dipole/solvation alone
```

结论：第二轮建议把后续迭代优化拆成至少两个 reward profile：`type_II_PDT` 和 `hypoxia_type_I_PDT`。若继续使用单一综合 reward，会把互相冲突的 T1-S0 目标、ROS 机制和实验终点混在一起，导致优化方向不稳定。
