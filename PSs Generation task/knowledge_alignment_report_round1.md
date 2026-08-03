# 知识对齐报告

## 1. 项目目标与输入证据

本轮实验目标是：**开发具有更高光敏性能的候选分子**。本阶段只做知识对齐，不选择具体算法，也不直接给出最终候选分子。

主要证据来自项目内已编译的 llm-wiki 知识库：`ka-wiki/wiki`。检索重点包括光敏剂、光动力治疗、光毒性、暗毒性、治疗指数、单线态氧、活性氧、I 型/II 型光敏机制、聚集、水溶性、低氧活性、光热转换、亚细胞定位以及结构-性能关系。

检索状态说明：`llmwiki get_context_pack` 提示 embedding index outdated，语义上下文包没有返回 primary pages；因此本轮改用 `llmwiki search_pages`、`rg` 全文检索和直接读取 wiki concept 页来抽取证据。当前结果应视为**第一版可审核知识对齐结果**，不是专家认证后的最终版本。

对定义不清或需要标准化的重要术语，已联网检索权威来源进行概念对齐，包括 NCI、MeSH、ChEBI/AmiGO 和 IUPAC Gold Book。注意：这些权威来源只用于术语定义和概念对齐，不用于证明论文里的结构-性能关系。

## 2. 核心概念体系

| 概念 | 中文说明 | 权威来源/本体 | 映射状态 | 备注 |
|---|---|---|---|---|
| 光动力治疗（Photodynamic therapy, PDT） | 使用光激活光敏剂，在局部产生杀伤性光化学效应的治疗方式。 | MeSH D010778；NCI PDT 页面 | exact | 作为治疗模式概念。 |
| 光敏剂/光敏化剂（Photosensitizer / Photosensitizing agent） | 光照后产生活性反应并介导治疗或杀伤效应的化合物。 | MeSH D017319 | close | 论文中常写作 photosensitizer 或 PS。 |
| 活性氧（Reactive oxygen species, ROS） | 与氧相关的高反应性物种，包括单线态氧、超氧阴离子、过氧化氢、羟基自由基等。 | ChEBI:26523 | exact | 用于统一 ROS 相关指标。 |
| 单线态氧（Singlet oxygen, 1O2） | 电子激发态氧，是 II 型 PDT 中常见的关键杀伤物种。 | ChEBI + 论文证据 | close | 论文中常用量子产率表征。 |
| 量子产率（Quantum yield） | 每个被吸收光子产生的指定事件数。 | IUPAC Gold Book Q04991 | exact | 用于 singlet oxygen quantum yield。 |
| I 型光敏机制（Type-I photosensitization） | 以电子转移为主，产生超氧阴离子及后续过氧化物/羟基自由基等 ROS。 | 项目级 local 概念 | local | 与低氧 PDT 关系密切。 |
| 光诱导焦亡（Photopyroptosis） | 光激活光敏剂后诱导焦亡样细胞死亡，常涉及 ROS-caspase-gasdermin 通路。 | 项目级 local 概念 | local | 需要专家确认适用范围。 |

权威来源链接：

- NCI PDT: https://www.cancer.gov/about-cancer/treatment/types/photodynamic-therapy
- MeSH Photochemotherapy / PDT: http://id.nlm.nih.gov/mesh/D010778
- MeSH Photosensitizing Agents: https://meshb.nlm.nih.gov/record/ui?ui=D017319
- IUPAC quantum yield: https://doi.org/10.1351/goldbook.Q04991
- ChEBI ROS: https://amigo.geneontology.org/amigo/term/CHEBI:26523

## 3. 核心指标体系

| 指标 | 定义 | 单位/类型 | 关键实验条件 | 主要证据 |
|---|---|---|---|---|
| 光照条件下光毒性效力 | 光照后杀伤细胞或微生物所需浓度，常用 IC50、EC50 或 MIC 表示。 | nM、uM、ug/mL | 细胞/菌株、波长、功率密度、照射时间、光剂量、氧条件 | 1Zn-Et、3-PdTPyP、CA-Re |
| 暗毒性 | 无光照条件下的固有毒性，常用 TC50 或 dark IC50 表示。 | nM、uM | 同一模型、同一培养时间 | 1Zn-Et、compound 5、CA-Re |
| 光毒性指数/治疗指数 | 暗毒性阈值与光照毒性阈值的比值，例如 TC50/IC50。 | 无量纲 | 必须同一细胞系和可比条件配对计算 | 1Zn-Et、compound 5、CA-Re |
| 单线态氧量子产率 | 光吸收后产生单线态氧的效率。 | 无量纲或 % | 溶剂、氧浓度、激发波长、聚集状态、参比物 | compound 5、D1 |
| I 型 ROS 生成能力 | 产生超氧阴离子、过氧化氢、羟基自由基、脂质过氧化等的能力。 | 探针信号、EPR 信号、相对倍数 | ROS 探针、氧条件、光剂量、清除剂实验 | I 型设计综述、CA-Re |
| 低氧保留光毒性 | 低氧条件下仍保持的光毒性和光毒性指数。 | IC50 + PI | 氧浓度、细胞系、光照条件 | CA-Re |
| 治疗窗口吸收 | 是否能在红光/近红外等更适合组织穿透的窗口被有效激发。 | nm；M^-1 cm^-1 | 溶剂、生物介质、聚集状态 | 1d、compound 5 |
| 聚集/水相单体性 | 分子在水相是否非聚集，或是否形成有利的 AIE/自组装状态。 | 光谱、DLS、NMR、定性判断 | 浓度、pH、离子、血清、介质 | compound 5、D1 |
| 水溶性/分散性 | 在水或生物介质中溶解、分散并保持光活性的能力。 | uM、mg/mL、定性 | 介质、pH、血清、浓度 | compound 5、3-PdTPyP |
| 亚细胞定位 | 分子定位到线粒体、细胞膜、溶酶体或肿瘤膜等位置的程度。 | Pearson 相关系数、摄取比、共定位分数 | 细胞系、探针、孵育时间 | 1d、CA-Re、Zn porphyrins |
| 静电/阳离子靶向强度 | 阳离子结构与阴离子模型或膜结构的相互作用强度。 | M^-1、mV、电荷数 | 离子强度、模型体系 | 1d、D1、3-PdTPyP |
| 光热转换效率 | 吸收光能转化为热的效率。 | % | 波长、功率、浓度、升降温循环 | D1 |
| 光诱导焦亡效率 | 光照后焦亡发生的程度和速度。 | 细胞比例、倍数、时间、蛋白信号 | gasdermin 状态、细胞系、光剂量 | 1d、TBD-3C、CA-Re |
| 肿瘤保留/富集 | 光敏剂在肿瘤部位的保留或富集程度。 | 荧光强度比、保留时间 | 给药方式、模型、检测时间 | 1d、D1 |

## 4. 领域专家知识视图

| 概念/指标 | 科学意义 | 关键条件 | 关系与机制 | 证据 | 认证状态 |
|---|---|---|---|---|---|
| 光毒性 IC50/EC50/MIC | 最直接反映光敏杀伤效力。 | 波长、功率、照射时间、光剂量、模型必须记录。 | 1Zn-Et 在 `lambda >570 nm`、`12.4 mW cm^-2`、`15 min` 下 HeLa IC50 为 `0.54 uM`；3-PdTPyP 在白光 LED `400-800 nm`、`270 J cm^-2` 下 MIC 为 `1.21-2.43 uM`。 | jm5014852-114；photo-damage-promoted... | pending |
| 暗毒性 | 决定安全窗口，避免只优化强杀伤而牺牲安全性。 | 应与光毒性在同一模型下配对。 | 1Zn-Et 的 HeLa TC50 为 `1639 uM`；compound 5 的 HeLa TC50 为 `628 uM`。 | jm5014852-114；rscccc3cc44609c-35 | pending |
| 治疗指数/光毒性指数 | 综合衡量“强光毒性 + 低暗毒性”。 | 跨论文、跨细胞系不能直接比较。 | 1Zn-Et 的 HeLa TC50/IC50 为 `3035`；compound 5 的治疗指数 `>10000`；CA-Re 在低氧 425 nm 下 PI 为 `5000`。 | 相关论文页 | pending |
| 单线态氧量子产率 | II 型 PDT 的核心光物理指标。 | 受溶剂、氧浓度、聚集状态影响。 | compound 5 在 DMF 中 `Phi_D=0.61`，在水/D2O 中 `0.33-0.37`；D1 为 `89.4%`。 | rscccc3cc44609c-35；D1 paper | pending |
| I 型 ROS | 对低氧或混合机制 PDT 很重要。 | ROS 探针和清除剂实验需要谨慎解释。 | I 型设计综述强调电子转移增强；CA-Re 中 superoxide/peroxynitrite/lipid peroxidation 贡献较大。 | Type-I review；CA-Re | pending |
| 聚集/水溶性 | 影响实际生物环境中的有效光活性。 | 非 AIE 分子通常需抑制聚集；AIE/自组装体系可能相反。 | compound 5 通过刚性十六阳离子结构抑制水相聚集；D1 通过 dimerization 提高自组装和 AIE。 | compound 5；D1 | pending |
| 亚细胞定位 | ROS 作用半径短，定位决定损伤对象和死亡机制。 | 需记录细胞系、探针、孵育时间。 | 1d 线粒体共定位 Pearson `0.91`；CA-Re 细胞膜锚定；Zn porphyrin 中 hexyl 链增强线粒体摄取。 | 1d；CA-Re；debpone0108238-19 | pending |
| 光诱导焦亡 | 若目标是免疫激活，这可能是终端性能而非辅助机制。 | 依赖 gasdermin 表达、caspase 轴和细胞类型。 | 1d 可经 ROS-caspase-3-GSDME 通路，在 `10 s`、`0.4 J cm^-2` 下触发焦亡；TBD-3C 证据偏向 GSDMD/caspase-1。 | 1d；TBD-3C | pending |

## 5. 计算机专家优化指标视图

| 指标 | 优化角色 | 优化方向 | 重要性 | 可计算性 | 数据准备度 | 获取方式 | 条件 | 优先级 |
|---|---|---|---:|---:|---:|---|---|---|
| 光照条件下光毒性效力 | 主优化目标 | 最小化 | 5 | 3 | 4 | 实验测量、机器学习 | assay + light + oxygen | P0 |
| 光毒性指数/治疗指数 | 主优化目标 | 最大化 | 5 | 4 | 4 | 配对数据计算、机器学习 | paired dark/light data | P0 |
| I 型 ROS 生成能力 | 主优化目标 | 最大化 | 5 | 3 | 3 | 实验、物理计算、机器学习 | probe + oxygen + light | P1 |
| 低氧保留光毒性 | 主优化目标 | 最小化 IC50，最大化 PI | 5 | 2 | 2 | 实验、机器学习 | oxygen %, light, cell | P1 |
| 暗毒性 | 硬约束 | 最大化毒性阈值 | 5 | 3 | 4 | 实验、机器学习 | same model | P0 |
| 治疗窗口吸收 | 硬约束 | 目标范围 | 5 | 5 | 3 | UV-vis、TD-DFT | medium, aggregation | P0 |
| 聚集/水相单体性 | 约束 | 依体系决定 | 4 | 3 | 3 | 光谱、DLS、NMR | medium, concentration | P1 |
| 水溶性/分散性 | 约束 | 最大化 | 4 | 3 | 3 | 实验、机器学习 | medium, pH, serum | P1 |
| 肿瘤保留/富集 | 约束 | 最大化 | 4 | 1 | 2 | 体内成像 | route, model, time | P2 |
| 单线态氧量子产率 | 次优化目标/诊断指标 | 最大化 | 4 | 4 | 3 | 发光法、探针、计算 | solvent, wavelength | P1 |
| 光热转换效率 | 次优化目标 | 最大化 | 3 | 3 | 2 | 升温曲线 | wavelength, power | P2 |
| 光诱导焦亡效率 | 次优化目标 | 最大化 | 4 | 1 | 2 | LDH、gasdermin、成像 | cell/gasdermin/light | P2 |
| 亚细胞定位 | 中间指标 | 目标范围 | 4 | 2 | 3 | 成像、摄取、机器学习 | cell, probe, time | P2 |
| 静电/阳离子靶向强度 | 中间指标 | 目标范围 | 4 | 4 | 3 | 描述符、zeta、结合常数 | ionic strength | P2 |

```yaml
optimization_targets:
  primary:
    - 光照条件下光毒性效力
    - 光毒性指数/治疗指数
    - I 型 ROS 生成能力
    - 低氧保留光毒性
  secondary:
    - 单线态氧量子产率
    - 光热转换效率
    - 光诱导焦亡效率
  constraints:
    - 暗毒性
    - 治疗窗口吸收
    - 聚集/水相单体性
    - 水溶性/分散性
    - 肿瘤保留/富集
  intermediate:
    - 亚细胞定位
    - 静电/阳离子靶向强度
  diagnostic:
    - 单线态氧量子产率
    - I 型 ROS 生成能力
    - 聚集/水相单体性
    - 亚细胞定位
    - 光诱导焦亡效率
  not_ready: []
```

## 6. 结构-性质-机制-性能关系

1. **外周取代八阳离子锌酞菁可以兼顾低暗毒性和高光动力选择性。**  
   1Zn-Et 并不总是系列中光毒性最强的分子，但因暗毒性极低，其治疗指数最高。

2. **meta 位四阳离子 Pd(II) 卟啉 3-PdTPyP 优于 para 异构体 4-PdTPyP。**  
   论文将其优势与正电荷、水溶性、与带负电微生物结构的相互作用、较低聚集倾向以及单线态氧主导的 II 型机制联系起来。

3. **刚性、庞大、高电荷取代可以抑制酞菁水相聚集，同时保留单线态氧生成能力。**  
   compound 5 是最直接证据：水中符合 Beer-Lambert 行为，pH/离子/缓冲液/血清不引起明显光谱扰动，且水相仍有较高 `Phi_D`。

4. **阳离子 clamping 设计可以增强线粒体定位和局部 ROS 生成。**  
   1a-1d/1d 证据显示，pyridinium 或 imidazolium 与光敏核心结合后，可增强静电相互作用、线粒体定位、光照后 ROS 信号，并触发 GSDME 相关焦亡。

5. **阳离子电荷本身不够，脂溶性需要调谐。**  
   Zn(II) N-alkylpyridylporphyrin 系列显示，延长烷基链可增强脂溶性、线粒体摄取、呼吸抑制和 cytochrome c oxidase 光失活。

6. **电子转移增强是 I 型、低氧相关光敏剂设计路线。**  
   综述证据支持通过富电子微环境、缺电子中继体、分子阳离子化和 quinone 类电子转移基元来促进 superoxide/hydroxyl radical 生成；但纯 I 型行为和 ROS 检测标准化仍需专家确认。

7. **二聚化可以提高自组装、ROS、光热转换和肿瘤保留。**  
   D1 相比 M1 具有更高单线态氧量子产率、更高光热转换效率、更强 AIE/自组装和更好肿瘤部位保留。

## 7. 证据与冲突

较强证据：

- 1Zn-Et、3-PdTPyP、compound 5、CA-Re 和 D1 均有具体数值和实验条件。
- 多数关键证据来自同一论文内的系列比较，优于跨论文直接比较。
- 光照条件、细胞/菌株模型和部分 ROS 机制均有明确记录。

冲突或不可直接合并之处：

- 细胞 IC50/EC50、抗菌 MIC、肿瘤抑制率和焦亡比例不是同一个标签，不能直接合并训练。
- 单线态氧量子产率对 II 型 PDT 很关键，但不能代表 I 型或低氧活性体系的全部性能。
- 聚集通常会削弱普通酞菁的水相光活性，但 AIE 或自组装体系可能反而利用聚集。
- 阳离子电荷有助于定位和水溶性，但可能增加非特异相互作用或暗毒性。

## 8. 指标重要性与优先级

P0：建议优先进入后续任务编排，但仍需专家确认条件。

- 光照条件下光毒性效力
- 光毒性指数/治疗指数
- 暗毒性
- 治疗窗口吸收

P1：重要，但需要先补数据、统一实验条件或明确应用场景。

- I 型 ROS 生成能力
- 低氧保留光毒性
- 单线态氧量子产率
- 聚集/水相单体性
- 水溶性/分散性

P2：辅助、中间或机制解释指标。

- 亚细胞定位
- 静电/阳离子靶向强度
- 光热转换效率
- 光诱导焦亡效率
- 肿瘤保留/富集

P3：本轮暂未指定。若专家缩小应用场景，部分 P2 指标可能降为 P3。

## 9. 专家认证状态

当前所有概念、指标和关系均为 `pending`。本轮未产生专家 approve、revise、reject 或 dispute 记录。

## 10. 待补证据与待决问题

详细问题见 `expert_review_queue.yaml`。最高优先级问题包括：

- 明确最终应用场景：肿瘤 PDT、光焦亡免疫治疗、抗菌 PDT，还是一般光敏材料筛选。
- 明确终端性能标签：IC50/EC50、MIC、肿瘤抑制率、焦亡比例是否拆分。
- 决定 I 型 ROS 和低氧保留光毒性是否为主目标。
- 建立统一光照条件和 assay 元数据格式。
- 区分非 AIE 分子与 AIE/自组装分子的聚集优化方向。

## 11. 可进入任务编排阶段的指标清单

可条件进入：

- 光照条件下光毒性效力：仅限固定 assay family 和光照条件 schema。
- 光毒性指数/治疗指数：仅限同一模型配对的 dark/light 数据。
- 暗毒性：可作为硬安全约束。
- 治疗窗口吸收：可作为计算可行性较高的结构/光谱约束。

暂不建议直接作为最终任务目标：

- I 型 ROS 生成能力：需要标准化检测方法。
- 低氧保留光毒性：需要确认应用场景并补充数据。
- 光诱导焦亡效率：需要确认是否为终端治疗目标。
- 肿瘤保留/富集：受给药方式、制剂和模型影响大，不能只由分子结构直接决定。
