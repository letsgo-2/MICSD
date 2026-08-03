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

### 4.1 领域专家补充：优势光敏剂骨架及特性分析

领域专家已确认当前知识基本无误。基于本轮论文证据，可将“优势骨架”归纳为以下几类。这里的“优势”只表示在当前证据集中有明确结构-性能支持，不等于所有应用场景下都应优先选择。

| 优势骨架/结构策略 | 代表分子或系列 | 主要优势特性 | 关键结构-性能关系 | 适用场景 | 风险/待确认点 | 证据 |
|---|---|---|---|---|---|---|
| 酞菁骨架，尤其锌酞菁 | `1Zn-Et`、`2Zn-Et`、compound 5 | 强吸收、较高单线态氧产率、可通过取代位置调红移、可通过阳离子取代改善水相行为。 | 锌中心相对镁中心显著提高光毒性和单线态氧产率；非周边取代可将 Q-band 红移到 `756 nm`；刚性十六阳离子结构可抑制水相聚集。 | 以 II 型 PDT、深部光照、低暗毒性为主要目标的候选骨架。 | 阳离子数、取代位置和暗毒性存在权衡；非聚集对普通酞菁有利，但不适用于 AIE 体系。 | `jm5014852-114`；`rscccc3cc44609c-35` |
| 卟啉/金属卟啉骨架 | `3-PdTPyP`、Zn(II) N-alkylpyridylporphyrins、Gd-TCPP/Gd-PNPs | 结构成熟、易金属化、可调电荷和脂溶性、可用于 PDT 和成像。 | meta 位四阳离子 Pd(II) 卟啉比 para 异构体抗菌光动力活性更强；阳离子卟啉配合适当脂溶性可增强线粒体摄取和呼吸链光损伤。 | 抗菌 PDT、线粒体靶向 PDT、诊疗一体化体系。 | 金属中心、取代位置、脂溶性和聚集之间需要共同优化；抗菌 MIC 与肿瘤细胞 IC50 不可直接合并。 | `photo-damage-promoted...`；`debpone0108238-19` |
| D-A / D-B-A 有机光敏骨架 | `NI-TA`；triphenylamine-dialkyl fluorene-naphthalimide | 可通过 HOMO/LUMO 分离、三线态能级和电子转移能力调控 I 型 ROS，适合低氧或 superoxide 目标。 | `NI-TA` 的 donor-bridge-acceptor 结构使 LUMO 主要在 naphthalimide acceptor，HOMO 主要在 triphenylamine donor；计算 `ΔET1-S0=1.115 eV`，低于文中用于 singlet oxygen 路径的 `1.610 eV` 阈值，实验上以 superoxide 为主。 | 低氧 PDT、I 型 ROS、光诱导焦亡。 | 需要 DFT/TD-DFT 与 EPR/探针实验校准；不同论文采用的氧激发阈值不完全一致。 | `photocatalytic-superoxide-radical-generator...` |
| AIE 型 donor-acceptor 光敏骨架 | `TBD-1C`、`TBD-2C`、`TBD-3C`、`D1` | 聚集态仍能发光和产 ROS，适合解决传统聚集淬灭问题；可结合膜锚定或自组装。 | TBD-R 为 `D-A'-π-A` 结构，白光下 ABDA 分解速率 `13.5-15.1 nmol/min`，高于 Rose Bengal 的 `10.8 nmol/min`；阳离子链数从 1 到 3 增加时，膜共定位 Pearson 从 `0.75` 提高到 `0.95`。 | 细胞膜定位 PDT、光焦亡、聚集态生物环境。 | AIE 体系的“聚集有利”与普通酞菁“非聚集有利”相冲突，建模时必须区分骨架类别。 | `activation-of-pyroptosis-by-membraneanchoring-aie...` |
| 阳离子 clamping / 线粒体定位结构 | `1d`，pyridinium/imidazolium clamping | 增强线粒体定位、局部 ROS 和 GSDME 相关焦亡。 | 阳离子基团夹持光敏核心，通过静电相互作用增强线粒体内外膜识别；`1d` 的线粒体共定位 Pearson `0.91`，光照后 ROS 高于暗态 `>16` 倍。 | 线粒体靶向光焦亡和免疫激活。 | 阳离子强度过高可能增加非特异结合或暗毒性，需要作为目标范围而非单调最大化。 | `a-general-molecular-structural-design...` |
| 金属配合物/膜锚定骨架 | CA-Re | 低氧下仍保持纳摩尔光毒性，兼具膜定位和混合 ROS。 | CA-Re 通过 CAIX 相关膜锚定，在低氧 MDA-MB-231 中 425 nm 光照 IC50 `20 nM`、PI `5000`；ROS 证据指向 superoxide/peroxynitrite/lipid peroxidation 重要贡献。 | 低氧实体瘤 PDT、膜损伤、免疫原性死亡。 | 需要确认 CAIX 靶向对不同肿瘤模型的适用性；金属配合物可计算成本较高。 | `a-carbonic-anhydrase-ix...` |
| 二聚化/自组装策略 | `D1` vs `M1` | 提高自组装、ROS、光热转换和肿瘤保留。 | D1 相比 M1 具有更高单线态氧产率 `89.4%` vs `84.03%`、更高光热转换效率 `64.19%` vs `44.58%`，并有约 `110.3 nm` 自组装结构和更好肿瘤保留。 | PDT/PTT 协同、肿瘤局部给药、自组装纳米光敏体系。 | 若目标是小分子生成，D1 这类自组装效应不能只靠单分子 DFT 表征，需要加入聚集/形貌层级描述。 | `pyroptosismediated-synergistic...` |

领域专家结论：当前证据最支持的设计路线不是单一骨架，而是“骨架 + 光物理机制 + 生物定位”的组合。若目标偏 II 型 PDT，可优先关注锌酞菁/卟啉及其红移、非聚集和高 `ΦΔ`；若目标偏低氧或光焦亡，可优先关注 D-A/D-B-A、I 型 ROS、阳离子化定位和膜/线粒体局部 ROS；若目标偏免疫治疗或协同治疗，可关注 AIE、膜锚定、二聚化、自组装和光热协同。

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

### 5.1 计算机专家补充：可用于 DFT/TD-DFT 的数值指标

当前多数终端性能指标仍需生物实验测量，例如 IC50、MIC、PI、焦亡比例和肿瘤抑制率。为了支持迭代优化框架，应将这些终端指标拆解为一组**可计算代理指标**。这些代理指标不能替代实验标签，但可以作为生成模型、筛选器或 reward 的早期约束。

权威术语对齐：IUPAC Gold Book 将系间窜越定义为不同自旋多重态电子态之间的无辐射跃迁；振子强度是电子跃迁积分强度的量度；摩尔吸收系数为吸光度除以光程和物质的量浓度；氧化还原电位是在标准条件下相对于标准参比半电池测得的还原/氧化电位；单线态分子氧是激发单重态的氧分子。这些定义支撑下面指标的物理含义。  
来源：IUPAC Gold Book intersystem crossing `I03123`、oscillator strength `O04339`、molar absorption coefficient `M03972`、redox potential `RT06783`、singlet molecular oxygen `S05695`。

| 可计算指标 | 推荐计算方式 | 物理/化学含义 | 与终端性能的关系 | 初始 reward 方向与阈值建议 | 证据强度 |
|---|---|---|---|---|---|
| 最大吸收波长 `λmax` | TD-DFT 垂直激发能：`λ(nm)=1240/E(eV)`；记录主要跃迁。 | 决定分子是否能被治疗窗口光源激发。 | 更长波长通常有利组织穿透；论文中 `2Zn-Et` Q-band `756 nm` 被认为有利。 | 约束/奖励：优先 `λmax >= 650 nm`；强奖励 `700-800 nm`；若当前体系只支持可见光，可临时放宽到 `>= 520 nm`。 | 中-高 |
| 振子强度 `f` | TD-DFT 输出主要吸收跃迁的 oscillator strength。 | 近似反映吸收强度，IUPAC 定义为电子跃迁积分强度量度。 | 低 `f` 可能导致难以有效激发；但高 `f` 不等于高 ROS。 | 约束：主要治疗窗口跃迁 `f > 0.05`；奖励随 `f` 增大到 `0.3` 后饱和。阈值需按方法校准。 | 中 |
| S1-Tn 能隙 `ΔE(S1-Tn)` | TD-DFT 计算 S1 与邻近三重态 Tn 能级差。 | 衡量是否存在可行 ISC 通道。 | Type-I review 指出有效 ISC 常要求 S1 到某个 Tn 的能隙小，文中给出 `<0.4 eV` 经验阈值。 | 奖励：`min ΔE(S1-Tn) < 0.4 eV`；强奖励 `<0.2 eV`；若无接近 Tn，降低 ISC 代理分。 | 中-高 |
| 自旋轨道耦合 `SOC(S1,Tn)` | ORCA、Q-Chem、Gaussian 等计算 SOC，单位 `cm^-1`。 | 辅助判断 ISC 概率；El-Sayed 规则提示轨道类型改变可提高 ISC。 | PDIPy 例中 `SOC(S1,T2)=0.25 cm^-1` 被用于支持 ISC。 | 奖励：相同骨架内相对最大化；不建议设绝对硬阈值。若必须初始化，可用 `>0.1 cm^-1` 作为弱通过线。 | 中 |
| 最低三重态能量 `E(T1)` 或 `ΔE(T1-S0)` | TD-DFT/TDA 或优化 T1 后计算 T1-S0 能量。 | 判断 II 型 singlet oxygen 路径是否热力学可行，以及是否偏向 I 型。 | 间接 I 型策略希望 T1 低于氧敏化阈值以抑制 II 型；综述中常见阈值 `0.98 eV`，也出现 `1.12/1.75 eV` 方法差异。 | 若目标是 II 型：奖励 `E(T1) > 0.98 eV` 且保留 ISC；若目标是 I 型：奖励 `E(T1) < 0.98 eV` 或低于所选方法阈值。必须按目标机制二选一。 | 中 |
| 单重-三重态能隙 `ΔE(S1-T1)` | TD-DFT 输出 S1 与 T1 能量差。 | 影响 ISC 和三重态形成倾向。 | `NI-TA` 论文用较小 `ΔES1-T1` 支持更有效 ISC；但间接 I 型又需要兼顾低 T1 和高 ISC。 | 奖励：相对同系列更小；初始目标 `<0.5 eV` 可作为软约束，但不能跨骨架硬比较。 | 中 |
| 前线轨道分离/重叠 | DFT 计算 HOMO/LUMO 空间分布、overlap、CT distance、hole-electron analysis。 | 描述 D-A/D-B-A 电荷转移特征。 | `NI-TA` 中 HOMO 位于 triphenylamine donor，LUMO 位于 naphthalimide acceptor，有利 superoxide 路径；间接 I 型例子又显示较大 HOMO-LUMO overlap 可降低 T1。 | 目标依策略而变：D-B-A 直接 I 型奖励 HOMO/LUMO 分离；间接 T1-lowering 策略可奖励较高 overlap。需先选设计路线。 | 中 |
| 氧化/还原电位 `Eox/Ered` | DFT 计算绝热/垂直电离势和电子亲和势；用溶剂模型估算电位；或校准到 CV 数据。 | 衡量电子给受能力和电子转移驱动力。 | I 型直接策略依赖电子转移；综述中用循环伏安、Rehm-Weller 分析支持 ET 可行性。 | 奖励：电子转移自由能 `ΔG_ET < 0`；若缺参照，可相对奖励更易供电子/受电子的候选。阈值必须依电子供体/受体和环境定义。 | 中 |
| 电子转移自由能 `ΔG_ET` | Rehm-Weller 型计算：由氧化/还原电位、激发能和库仑项估算。 | 判断激发态向氧或中继体电子转移是否热力学有利。 | Type-I direct strategy 的核心代理指标。 | 主 reward：`ΔG_ET < 0 eV`；`-0.1` 到 `-0.5 eV` 可作为温和有利区间，过强驱动力可能增加副反应，需专家校准。 | 中 |
| 偶极矩/电荷/静电势 | DFT 电荷、偶极矩、分子静电势、形式电荷数。 | 描述阳离子定位、膜相互作用和水相分散倾向。 | cation-clamping、TBD-R、3-PdTPyP 均显示阳离子结构与定位/水溶性相关。 | 约束而非单调最大化：保留 `+1` 到 `+4` 或按骨架定义的阳离子数；超过范围可能暗毒性或非特异结合增加。 | 中 |
| 脂溶性代理 `logP/logD` | 可用 RDKit/经验模型；DFT 可补充溶剂化自由能。 | 影响膜穿透、线粒体摄取和聚集。 | Zn N-alkylpyridylporphyrin 中链长增加提高脂溶性和线粒体定位，但需避免过度疏水。 | 目标范围：不建议单调最大化；初始可设 `0 < cLogP < 5` 作为小分子软范围，阳离子盐和纳米体系需另设规则。 | 中 |
| 分子平面性/扭转角 | 优化构型后计算核心平面 RMSD、关键二面角。 | 影响 π 共轭、吸收红移、聚集和非辐射衰减。 | 酞菁/卟啉依赖大 π 共轭；D1 dimerization 和 AIE 体系又需要考虑非辐射/聚集效应。 | 依骨架设置：酞菁/卟啉奖励稳定共轭；AIE 分子不宜简单奖励全平面。 | 中 |
| 重原子/金属中心效应代理 | 结构标签 + SOC 计算；金属中心类型编码。 | 重原子或金属中心可增强 ISC 和 ROS。 | 锌酞菁相对镁酞菁更高 `ΦΔ` 和光毒性；CA-Re 为金属配合物低氧活性例子。 | 约束/类别变量：Zn/Re/Pd 等可作为优势类别，但需同时惩罚暗毒性和计算不稳定。 | 中-高 |

### 5.2 可进入迭代优化框架的 reward 设计草案

建议将 reward 分为三层：**硬约束层、光物理代理层、机制偏好层**。终端生物实验指标暂不直接进入早期 reward，除非已有同一 assay 的训练数据。

| reward 项 | 类型 | 计算方式 | 建议方向/阈值 | 作用 |
|---|---|---|---|---|
| 治疗窗口吸收 | 硬约束 + reward | TD-DFT `λmax`、`f` | `λmax >= 650 nm` 通过；`700-800 nm` 加分；`f > 0.05` 通过，`f >= 0.3` 饱和 | 保证候选可被有效光源激发。 |
| ISC 可达性 | 光物理代理 | `min ΔE(S1-Tn)` + SOC | `ΔE < 0.4 eV` 加分；SOC 同系列相对越大越好 | 促进三重态形成。 |
| II 型 ROS 候选能力 | 机制 reward | `E(T1)` + ISC | `E(T1) > 0.98 eV` 且 ISC 可达；适合 singlet oxygen 路线 | 对应高 `ΦΔ` 的早期代理。 |
| I 型 ROS 候选能力 | 机制 reward | `E(T1)`、`ΔG_ET`、HOMO/LUMO 分布 | `E(T1) < 0.98 eV` 或低于所选阈值；`ΔG_ET < 0` | 对应低氧/superoxide 路线。 |
| D-A/D-B-A 电荷转移 | 结构-电子代理 | HOMO/LUMO 分布、CT distance、dipole | D-B-A 路线奖励 donor/acceptor 分离；间接 I 型路线不强制分离 | 连接骨架设计与电子转移机制。 |
| 暗毒性风险代理 | 软惩罚 | 过高形式电荷、极端 logP、反应性强 ET 驱动力、PAINS/结构警报 | 超出结构族经验范围扣分；不可替代暗毒性实验 | 降低明显不安全候选。 |
| 水相/聚集风险代理 | 软约束 | logP、平面性、阳离子数、聚集倾向模型 | 普通酞菁/卟啉惩罚强聚集；AIE 体系单独建模 | 避免把不同骨架的聚集规则混用。 |

推荐初始总分形式：

```text
Reward = W_abs * R_abs
       + W_ISC * R_ISC
       + W_ROS * max(R_typeI, R_typeII)
       + W_design * R_scaffold
       - W_risk * P_dark_toxicity_risk
       - W_out * P_out_of_domain
```

初始权重建议：

| 目标场景 | `W_abs` | `W_ISC` | `W_ROS` | `W_design` | `W_risk` | 说明 |
|---|---:|---:|---:|---:|---:|---|
| 通用高光敏小分子 | 0.25 | 0.20 | 0.30 | 0.10 | 0.15 | 平衡吸收、ISC、ROS 和安全风险。 |
| II 型 PDT | 0.25 | 0.25 | 0.30 | 0.05 | 0.15 | `R_ROS` 选 `R_typeII`，重视 `E(T1)>0.98 eV`。 |
| I 型/低氧 PDT | 0.20 | 0.20 | 0.40 | 0.05 | 0.15 | `R_ROS` 选 `R_typeI`，重视 `ΔG_ET<0` 和低氧相关机制。 |
| 光焦亡/免疫治疗 | 0.20 | 0.20 | 0.30 | 0.15 | 0.15 | 额外奖励阳离子定位、膜/线粒体定位或 AIE 骨架。 |

这些阈值是**第一版 reward 初始化建议**，不是最终科学结论。进入主动学习或生成优化后，应使用同一实验条件下的 IC50/PI/ROS/暗毒性数据回归校准。

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

8. **D-B-A 骨架可作为 I 型 ROS 的可计算设计入口。**  
   `NI-TA` 论文把 triphenylamine donor、fluorene bridge 和 naphthalimide acceptor 连接起来，形成 HOMO/LUMO 空间分离和较低 triplet-ground-state 能量，实验上主要产生 superoxide 而非 singlet oxygen。这为计算机专家提供了明确的 DFT/TD-DFT 代理指标：HOMO/LUMO 分布、`ΔES1-T1`、`ΔET1-S0`、`ΔG_ET`。

9. **间接 I 型设计需要同时满足低 T1 和有效 ISC。**  
   综述证据表明，仅降低 `T1` 不够；如果 `S1-Tn` 能隙过大，ISC 受阻，ROS 仍可能不足。因此 reward 不能只优化 `E(T1)`，必须联合 `min ΔE(S1-Tn)` 和 SOC。

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
- TD-DFT 吸收窗口代理：`λmax` 与 oscillator strength
- ISC 可达性代理：`min ΔE(S1-Tn)` 与 SOC

P1：重要，但需要先补数据、统一实验条件或明确应用场景。

- I 型 ROS 生成能力
- 低氧保留光毒性
- 单线态氧量子产率
- 聚集/水相单体性
- 水溶性/分散性
- Type-I/Type-II 机制代理：`E(T1)`、`ΔG_ET`、HOMO/LUMO 分布

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
- 由计算专家确认 DFT/TD-DFT 方法学：泛函、基组、溶剂模型、TDA 与否、金属配合物处理方式、SOC 计算软件和 benchmark 数据。
- 由计算机专家确认 reward 采用“II 型路线”“I 型/低氧路线”还是二者并行，不应把 `E(T1)>0.98 eV` 和 `E(T1)<0.98 eV` 同时作为同一候选的硬目标。

## 11. 可进入任务编排阶段的指标清单

可条件进入：

- 光照条件下光毒性效力：仅限固定 assay family 和光照条件 schema。
- 光毒性指数/治疗指数：仅限同一模型配对的 dark/light 数据。
- 暗毒性：可作为硬安全约束。
- 治疗窗口吸收：可作为计算可行性较高的结构/光谱约束。
- `λmax`、oscillator strength、`min ΔE(S1-Tn)`、SOC、`E(T1)`、`ΔG_ET`、HOMO/LUMO 分布：可进入计算机专家的早期迭代优化框架，作为 DFT/TD-DFT 代理 reward。

暂不建议直接作为最终任务目标：

- I 型 ROS 生成能力：需要标准化检测方法。
- 低氧保留光毒性：需要确认应用场景并补充数据。
- 光诱导焦亡效率：需要确认是否为终端治疗目标。
- 肿瘤保留/富集：受给药方式、制剂和模型影响大，不能只由分子结构直接决定。
- DFT 代理指标不能直接声明为真实 IC50、PI 或暗毒性；必须在后续通过同一实验体系校准。
