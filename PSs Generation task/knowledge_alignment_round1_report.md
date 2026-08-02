# 科研知识对齐报告：高光敏性能候选分子

生成时间：2026-07-17  
项目目标：开发具有更高光敏性能的候选分子。  
领域：光敏剂分子设计 / 光动力治疗相关光敏分子。  
应用场景：论文证据主要指向肿瘤光动力治疗、缺氧肿瘤微环境、细胞器/膜靶向和焦亡诱导；具体应用场景仍需材料专家确认。

## 1. 项目目标与输入证据

本次对齐以工作区 `markdown/` 下 47 个 Markdown 文献文件为候选证据源，优先使用与光敏剂、PDT、ROS、Type-I/Type-II 光过程、AIE、细胞器靶向、光毒性和结构-性能关系直接相关的论文。核心证据包括：

| evidence_id | 来源 | 证据定位 | 用途 |
|---|---|---|---|
| E001 | `2015_Machacek_Far-Red-Absorbing-Cationic-Phthalocyanine-Photosensitizers.md` | lines 25-31, 96-110 | PDT 三要素、酞菁吸收、聚集、水溶性、Q-band 和结构影响 |
| E002 | `2013_Makhseed_Water-Soluble-Non-Aggregating-Zinc-Phthalocyanine-for-PDT.md` | lines 39-45, 77-107 | 非聚集水溶性 ZnPc、ΦΔ、EC50、暗毒性、摩尔吸收系数 |
| E003 | `Advanced Science - 2024 - Ma - The Current Advances in Design Strategy  Indirect Strategy and Direct Strategy  for Type‐I.md` | lines 19-43 | ISC、SOC、ICT、ΔE_ST、Type-I/II 机制和缺氧适用性 |
| E004 | `2024_Yi_Mitochondria-Targeting-Type-I-Photodrug-for-Pyroptotic-Oncotherapy.md` | lines 45-58 | 660 nm 吸收、Type-I 过氧/超氧自由基、640 nm 照射、线粒体靶向与焦亡 |
| E005 | `2021_Wu_Activation-of-Pyroptosis-by-Membrane-Anchoring-AIE-Photosensitizer.md` | lines 39-55, 61 | AIE、膜锚定、阳离子链数量、膜损伤、焦亡机制 |
| E006 | `2022_Su_CAIX-Anchored-Rhenium-Photosensitizer-Evokes-Pyroptosis.md` | lines 29-33 | CAIX 锚定 Re(I) 光敏剂、缺氧下 Type-I/II PDT、纳摩尔光毒性、GSDMD 焦亡 |
| E007 | `2022_Su_CAIX-Anchored-Rhenium-Photosensitizer-Evokes-Pyroptosis_SI.md` | lines 93-95 | HPLC 光稳定性测试条件，425 nm/525 nm 照射 |

联网术语对齐使用权威来源：IUPAC Gold Book、ChEBI、NCI Thesaurus / NCI Dictionary / MeSH。联网检索只用于术语定义和本体映射，不用于替代论文中的科学关系证据。

## 2. 核心概念体系

| concept_id | 概念 | 定义 | 本体/术语来源 | 映射 | 认证状态 |
|---|---|---|---|---|---|
| C001 | 光敏剂 / photosensitizer | 在光敏化过程中首先吸收辐射并引发另一分子实体发生光化学或光物理变化的分子；在 PDT 医学语境中也指被光激活后杀伤细胞的药物。 | IUPAC photosensitization P04652；NCI Thesaurus C1420 | close | pending |
| C002 | 光动力效应 / PDT 相关效应 | 需要光、光敏剂和分子氧同时存在的光诱导损伤。 | IUPAC photodynamic effect P04600；NCI PDT C15300；MeSH D010778 | exact/close | pending |
| C003 | 活性氧 / ROS | 由氧不完全单电子还原形成的分子或离子，包括超氧、羟基自由基、单线态氧等。 | ChEBI CHEBI:26523 | exact | pending |
| C004 | 单线态氧 / singlet dioxygen | 二氧分子的最低激发态，是一种 ROS。 | ChEBI CHEBI:26689 | exact | pending |
| C005 | 超氧 / superoxide | 公式 O2、净电荷 -1 的二原子氧自由基阴离子，是 ROS。 | ChEBI CHEBI:18421 | exact | pending |
| C006 | 量子产率 / quantum yield | 系统每吸收一个光子所产生的定义事件数。 | IUPAC Q04991 | exact | pending |
| C007 | 摩尔吸收系数 / molar absorption coefficient | 吸光度除以光程和物质的量浓度。 | IUPAC M03972 | exact | pending |
| C008 | 系间窜越 / intersystem crossing, ISC | 不同多重度电子态之间的等能无辐射跃迁。 | IUPAC I03123 | exact | pending |
| C009 | Type-I 光敏过程 | 光激发后三重态 PS 经电子转移产生自由基/自由基离子，进一步产生超氧、过氧化氢、羟基自由基等 ROS。 | IUPAC photooxygenation P04641 + 论文 E003 | close | pending |
| C010 | Type-II 光敏过程 | 光激发后三重态 PS 向氧能量转移，产生单线态氧。 | IUPAC photooxygenation P04641 + 论文 E001/E003 | close | pending |
| C011 | 聚集诱导发光光敏剂 / AIE PS | 在聚集态保持或增强发光并可有效产生活性氧的光敏剂设计类别。 | 论文 E005；未找到完全等价权威本体 | local | pending |
| C012 | 光稳定性 / photostability | 光照及后续孵育条件下分子保持未降解或未转化的能力，本项目用 HPLC 或光谱变化操作化。 | 论文 E007；需标准术语确认 | local | pending |

## 3. 核心指标体系

| indicator_id | 指标 | 定义/单位 | 条件 | 角色 | 方向 | 重要性 | 可计算性 | 数据准备度 | 优先级 |
|---|---|---|---|---|---|---:|---:|---:|---|
| I001 | ROS 生成能力 | ROS 探针信号、总 ROS 产率或相对生成效率；无统一单位 | 光照波长、功率、氧水平、介质 | primary_objective | maximize | 5 | 3 | 3 | P0 |
| I002 | 单线态氧量子产率 ΦΔ | 单线态氧生成事件/吸收光子；无量纲 | 溶剂、氧浓度、激发波长、参比物 | primary_objective for Type-II | maximize | 5 | 4 | 3 | P0 |
| I003 | Type-I 自由基/超氧生成能力 | 超氧或过氧自由基探针响应；可相对量化 | 缺氧/常氧、光照波长、探针体系 | primary_objective for hypoxia | maximize | 5 | 3 | 2 | P1 |
| I004 | 长波长吸收峰 λmax/Q-band | nm | 水/有机溶剂、浓度、聚集状态 | secondary_objective | target_range: 650-800+ nm | 4 | 5 | 4 | P0 |
| I005 | 摩尔吸收系数 ε | M^-1 cm^-1 或 dm3 mol^-1 cm^-1 | λmax、溶剂、光程 | secondary_objective | maximize | 4 | 5 | 3 | P0 |
| I006 | 水溶性 | mM 或定性可溶/不可溶 | 水、缓冲液、血清培养基 | constraint | maximize/minimum_threshold | 4 | 4 | 3 | P0 |
| I007 | 聚集倾向 | 光谱形状、Beer-Lambert 线性、H-aggregate 特征；可定性/半定量 | 水相浓度、pH、离子、血清 | constraint | minimize | 5 | 4 | 3 | P0 |
| I008 | 光毒性 EC50/IC50 | nM/µM | 细胞系、孵育、光剂量、氧状态 | primary_objective | minimize | 5 | 3 | 2 | P1 |
| I009 | 暗毒性 TC50/IC50_dark | µM | 细胞系、孵育时间、无光 | constraint | minimize toxicity / maximize TC50 | 5 | 3 | 2 | P1 |
| I010 | 光毒性选择指数 | TC50_dark / EC50_light 或类似比值 | 与 I008/I009 同条件可比 | secondary_objective | maximize | 5 | 3 | 1 | P1 |
| I011 | ISC 促进能力 | ΦT、SOC、ΔE_ST 或相关计算代理 | 计算方法、溶剂模型、态选择 | intermediate | maximize ISC / minimize ΔE_ST | 4 | 4 | 2 | P1 |
| I012 | 细胞器/膜靶向能力 | 共定位系数、定位类别、膜锚定强度 | 细胞系、染料、成像条件 | secondary_objective | context_dependent | 4 | 2 | 2 | P1 |
| I013 | 光稳定性 | HPLC 主峰保留、降解率、吸收变化 | 照射波长/时长、37 °C 暗孵育 | constraint | maximize | 4 | 3 | 1 | P1 |
| I014 | 缺氧适用性 | 缺氧/常氧 PDT 效果保持率 | O2 浓度、模型体系 | primary/constraint | maximize | 5 | 2 | 1 | P1 |
| I015 | 焦亡诱导能力 | LDH、IL-1β、GSDMD/GSDME 裂解、膜泡 | 细胞系、靶向位点、光照 | diagnostic/secondary | context_dependent | 3 | 2 | 2 | P2 |

## 4. 领域专家知识视图

| 概念/指标 | 定义 | 科学意义 | 关键条件 | 关系与机制 | 证据 | 认证状态 |
|---|---|---|---|---|---|---|
| PDT 光敏分子 | 光、氧、PS 协同产生细胞毒性 ROS | 项目目标的上位机制 | 光照波长、氧、PS 浓度 | PS 吸光后向氧或底物转移能量/电子 | E001, E003 | pending |
| 长波长吸收 | Pc 通常 >680 nm，目标接近/超过 700 nm | 组织穿透深度更好 | Q-band、溶剂、聚集 | 非外周取代可红移 Q-band；氮 aza 替换可蓝移 | E001 | pending |
| 高 ROS/ΦΔ | 光敏性能核心输出 | 决定 PDT 杀伤效应 | 溶剂、氧、参比和探针 | ZnPc 非聚集水相 ΦΔ >0.33；Pc 闭壳层金属离子常有高单线态氧产率 | E001, E002 | pending |
| Type-I 自由基生成 | 超氧/过氧自由基优先 | 缺氧肿瘤中优先级高 | 缺氧、电子转移能力 | Type-I 经 ET 产生 O2.- 等，较 Type-II 低氧依赖 | E003, E004, E006 | pending |
| 聚集抑制 | 水相非聚集状态 | 聚集会降低光动力效应 | 水、浓度、pH、培养基 | 刚性大位阻 + 阳离子基团、非外周取代可降低聚集 | E001, E002 | pending |
| AIE 与定位 | 聚集态仍有发光/ROS，膜或线粒体局部富集 | 解决传统 PS 聚集淬灭和非特异定位 | 靶向基团、阳离子链数量、细胞系 | 膜锚定损伤膜并促进焦亡；线粒体定位促进特定死亡通路 | E004, E005 | pending |
| ISC/SOC/ΔE_ST | 连接结构与 ROS 的中间机制 | 可作为计算代理指标 | 计算方法、态选择 | 重原子提高 SOC 但可能增加暗毒性；ICT 降低 ΔE_ST 可促进 ISC | E003 | pending |
| 暗毒性与光毒性 | 无光安全性与有光杀伤能力 | 候选分子必须兼顾 | 细胞系、孵育、剂量 | 理想分子低暗毒、高光毒、高选择指数 | E002, E006 | pending |

## 5. 计算机专家优化指标视图

| 指标 | 优化角色 | 方向 | 重要性 | 可计算性 | 数据准备度 | 获取方式 | 条件 | 优先级 |
|---|---|---|---:|---:|---:|---|---|---|
| ROS 生成能力 | primary_objective | maximize | 5 | 3 | 3 | measure, estimate, machine_learn | 光照/氧/介质必须入样本条件 | P0 |
| ΦΔ | primary_objective | maximize | 5 | 4 | 3 | measure, physics_compute, machine_learn | Type-II 或混合机制；参比体系一致 | P0 |
| Type-I 自由基生成 | primary_objective | maximize | 5 | 3 | 2 | measure, estimate, machine_learn | 尤其缺氧；不要与总 ROS 直接合并 | P1 |
| λmax/Q-band | secondary_objective | target_range | 4 | 5 | 4 | measure, physics_compute, machine_learn | 溶剂/聚集态分开建模 | P0 |
| ε | secondary_objective | maximize | 4 | 5 | 3 | measure, physics_compute, machine_learn | 指定波长和溶剂 | P0 |
| 水溶性 | constraint | maximize/min threshold | 4 | 4 | 3 | measure, estimate, machine_learn | pH/盐/培养基影响大 | P0 |
| 聚集倾向 | constraint | minimize | 5 | 4 | 3 | measure, derive, machine_learn | 浓度依赖，建议分子-条件级样本 | P0 |
| EC50/IC50_light | primary_objective | minimize | 5 | 3 | 2 | measure, machine_learn | 细胞系和光剂量必须显式编码 | P1 |
| TC50/IC50_dark | constraint | maximize TC50 | 5 | 3 | 2 | measure, machine_learn | 同细胞系/孵育时间 | P1 |
| 光毒性选择指数 | secondary_objective | maximize | 5 | 3 | 1 | derive | 只有 light/dark 条件一致才可比 | P1 |
| ΦT/SOC/ΔE_ST | intermediate | maximize ΦT/SOC; minimize ΔE_ST | 4 | 4 | 2 | physics_compute | 方法学统一后可建模 | P1 |
| 靶向/共定位 | secondary_objective | context_dependent | 4 | 2 | 2 | measure, expert_only, machine_learn | 按应用位点分别建模 | P1 |
| 光稳定性 | constraint | maximize | 4 | 3 | 1 | measure, estimate | 照射条件需标准化 | P1 |
| 缺氧保持率 | primary_objective/constraint | maximize | 5 | 2 | 1 | measure, derive | 需要明确 O2 浓度 | P1 |
| 焦亡标志物 | diagnostic | context_dependent | 3 | 2 | 2 | measure | 不应作为通用光敏性能主目标 | P2 |

机器学习样本建议：不要只以“分子”为样本单位。至少应采用“分子-条件”或“分子-实验条件”样本，因为 ROS、光毒性、聚集、ΦΔ、光稳定性均依赖溶剂、氧浓度、光照波长/功率/剂量、细胞系和孵育条件。

```yaml
optimization_targets:
  primary:
    - I001
    - I002
    - I003
    - I008
    - I014
  secondary:
    - I004
    - I005
    - I010
    - I012
  constraints:
    - I006
    - I007
    - I009
    - I013
  intermediate:
    - I011
  diagnostic:
    - I015
  not_ready:
    - I010
    - I014
```

## 6. 结构-性质-机制-性能关系

| claim_id | 主体 | 关系 | 客体 | 类型 | 条件 | 证据 | 置信度 | 认证 |
|---|---|---|---|---|---|---|---|---|
| K001 | 长波长吸收 | promotes | PDT 组织穿透适用性 | mechanism/expert_rule | 接近或超过 700 nm | E001, IUPAC/NCI context | medium | pending |
| K002 | 酞菁聚集 | decreases | 光动力效应 | causal | 水相/极性介质 | E001, E002 | high | pending |
| K003 | 刚性大位阻阳离子取代 | inhibits | ZnPc 水相聚集 | causal | ZnPc，水相 | E002 | high | pending |
| K004 | 非外周取代 | increases | Q-band 红移 | correlation/causal | 酞菁系列内 | E001 | medium | pending |
| K005 | aza 替换 | decreases | Q-band 波长 | correlation | Pc 类比体系 | E001 | medium | pending |
| K006 | 高 ISC 效率 | increases | ROS 生成 | mechanism | 光照、氧/底物存在 | E003 | high | pending |
| K007 | 重原子引入 | increases | SOC/ISC | mechanism | 卤素/硒等 | E003 | medium | pending |
| K008 | 重原子引入 | increases | 暗毒性风险 | hypothesis/expert_rule | PDT 应用 | E003 | medium | pending |
| K009 | ICT 增强/ΔE_ST 降低 | promotes | ISC 和 ROS 生成 | mechanism | D-A 分子 | E003, E005 | medium | pending |
| K010 | Type-I 电子转移 | promotes | 缺氧下 ROS/PDT 效率 | mechanism | 低氧环境 | E003, E004, E006 | high | pending |
| K011 | 阳离子链数量增加 | increases | 膜锚定能力 | correlation | TBD-1C/2C/3C 系列 | E005 | medium | pending |
| K012 | 膜/线粒体定位 | promotes | 局部光损伤和特定细胞死亡通路 | mechanism | 细胞模型依赖 | E004, E005 | medium | pending |

## 7. 证据与冲突

明确证据：

- PDT 高性能分子需同时考虑光吸收、ROS 产生、氧依赖性、聚集、水溶性、暗毒性、光毒性和稳定性。
- Pc/ZnPc 证据明确支持“水相聚集降低光动力效应”和“非聚集、水溶性、高 ΦΔ 有利”。
- Type-I 文献明确支持缺氧条件下应提高自由基/超氧生成，而不能只优化单线态氧。
- AIE 和靶向策略在上传论文中多用于解决聚集态光敏化、定位和细胞死亡机制控制。

潜在冲突或不可合并项：

- Type-I 指标和 Type-II ΦΔ 不应无条件合并为一个 ROS 总分；不同机制、探针和氧条件会改变排序。
- 重原子提高 ISC/SOC 但可能带来暗毒性风险，不能只最大化 SOC。
- 焦亡诱导是特定治疗场景的诊断/次目标，不等价于普适“光敏性能”。
- λmax 需要目标范围，不是越长越好；过长波长可能降低激发能或与可用光源/探针不匹配，需专家认证。

## 8. 指标重要性与优先级

P0 可立即作为后续任务候选指标或约束：I001、I002、I004、I005、I006、I007。它们定义较明确、可测或可计算、论文证据较强。

P1 重要但需补条件标准化或数据整理：I003、I008、I009、I010、I011、I012、I013、I014。主要阻塞点是光照条件、氧浓度、细胞系、探针体系和实验条件不可直接比较。

P2 作为机制诊断或场景目标：I015。适合肿瘤免疫/焦亡场景，不应在“高光敏性能候选分子”的通用阶段作为唯一主目标。

## 9. 专家认证状态

所有概念、指标和关系当前均为 `pending`，因为尚未收到材料专家、实验专家和计算专家的正式审核记录。需要特别认证：

- 材料专家：Type-I 与 Type-II 在本项目中的权重；目标应用是否为 PDT/肿瘤/焦亡免疫治疗。
- 实验专家：光照波长、功率密度、光剂量、氧浓度、探针和细胞系的标准化方案。
- 计算专家：ΦΔ、Type-I 自由基、SOC、ΔE_ST、水溶性、聚集倾向的可计算路线和成本。
- 计算机专家：样本单位、不可合并变量、任务编排输入字段。

## 10. 待补证据与待决问题

- 项目最终应用是否限定为肿瘤 PDT，还是泛化为“高光敏/光催化/光诊疗分子”。
- “更高光敏性能”的主指标是总 ROS、Type-I 自由基、ΦΔ、光毒性 EC50，还是多目标组合。
- 是否必须要求缺氧适用性；若是，应将 Type-I 自由基和缺氧保持率升为 P0。
- 是否允许含重原子或金属配合物；若暗毒性/生物安全限制严格，需要加入硬约束。
- 是否以焦亡作为目标机制；若不是，焦亡标志物只保留为诊断指标。

## 11. 可进入任务编排阶段的指标清单

在未完成专家认证前，不应声称任何指标“完全进入任务编排”。可作为候选进入下一阶段草案的指标为：

- I001 ROS 生成能力：需绑定光照、氧和介质条件。
- I002 单线态氧量子产率 ΦΔ：适合 Type-II 或混合机制分支。
- I004 λmax/Q-band：目标范围暂定 650-800+ nm，需专家确认。
- I005 摩尔吸收系数 ε：需统一溶剂和波长。
- I006 水溶性：作为硬约束候选。
- I007 聚集倾向：作为硬约束候选。

其余指标进入专家认证清单后再决定是否提升到任务编排阶段。
