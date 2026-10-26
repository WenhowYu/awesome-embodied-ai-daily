# 记忆、技能与持续学习

[English](memory-skills.md) | [简体中文](memory-skills.zh-CN.md) | [所有主题](README.zh-CN.md)

62 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

## DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection

- [arXiv 2610.32969](https://arxiv.org/abs/2610.32969) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32969)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32969)

便携接口使用部署时的灵巧手，以参数化抓取和学习式旋转技能采集腕部运动及原生关节指令；模仿策略不接收技能标签。 评估样本少；螺丝刀旋转单独用速度指标，不计入三任务成功率均值。数据量与场景多样性同时变化；采集技能并非自主增长的技能库。

## RynnUnify: Towards Unified Embodied Brain

- [arXiv 2610.32965](https://arxiv.org/abs/2610.32965) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32965)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32965)

基于Cosmos3的16B模型耦合8B推理器和8B视频生成器；跨片段场景帧支撑交错视觉规划，另行RL训练的推理器选择是否调用生成证据，WAM适配联合学习视频与动作。 机器人适配使用约1,600小时原子任务及177小时组合任务数据。完整split的基线数值引用既有报告，精选20任务由作者评估；视觉历史是回合内上下文，不是已验证终身记忆，3项真机任务未隔离记忆贡献。

## Predictive Long-Horizon Progress Modeling with Action-Aware Quantification

- [arXiv 2610.32776](https://arxiv.org/abs/2610.32776) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32776)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32776)

NimCritic以视频预测训练约束进度/完成度双输出，结合历史进度扰动与跨模态对齐；LOOM评测包含300条跨本体轨迹、19,618个人工校准帧。 上述是离线评价，不是机器人任务成功率。多子任务依赖离线VLM分段，非直接证明在线实时裁判可用；训练800余小时、48加速器，未报告用奖励后训练策略的闭环收益。

## Semantic Representation for Agentic Self-Play in Automated Laboratories

- [arXiv 2610.32755](https://arxiv.org/abs/2610.32755) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32755)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32755)

VERID提供持久语义实验室孪生，支持状态查询、执行前仿真门控、同步轨迹及故障续跑；代理跨运行保留物理操作边界和分析经验。 这是小规模案例而非隔离记忆因果效应的消融：挑战实例与实验策略同时变化。使用预设结构化Harness、内部Gemini检查点及受监督运行中的人工批准门控；未证明生物学突破或通用机器人策略迁移。

## $R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design

- [arXiv 2610.32439](https://arxiv.org/abs/2610.32439) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32439)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32439)

以5项精英奖励池协调Explorer、Guardian、Evolver三类LLM角色，动态分配候选预算进行奖励程序迭代搜索。 仅仿真与任务内奖励搜索，不是跨任务机器人技能积累。精英池单调性针对保留搜索分数，不保证未来策略持续提升；RL训练主导成本，同骨干不等于所有基线搜索/token预算相同。

## LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents

- [arXiv 2610.32412](https://arxiv.org/abs/2610.32412) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32412)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32412)

外部检索–绑定–选择层复用叶级动作grounding，保留原递归规划器；经LoRA训练的1.7B选择器选出合法绑定动作，或交回未修改的上层模型。 成本节省以共同成功任务为条件，仅计上层模型而非完整系统成本。仅一个规划器/上层模型、两个离散动作仿真；ALFWorld成功率差异不显著。扩库证明读时采用新技能，不证明成功率单调增长或连续机器人控制。

## LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners

- [arXiv 2610.32348](https://arxiv.org/abs/2610.32348) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32348)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32348)

结合不可改写的执行日志、逐字保留的笔记历史、预期变化触发帧及先粗看再细查示范；Astra输出路点或π0.5落地子目标。记忆是推理时接口，而非参数适配。 干净记忆对照主要证明降成本，未显示明确成功率增益；完整系统还改变动作/调用接口。直接控制使用深度、标定及来自成功判定代码的任务说明。仅单仿真基准和闭源模型，无真机；单组件消融差别仅2–4回合。

## Lifelong Context Adaptation through Bidirectional Memory-Skill Learning

- [arXiv 2610.32295](https://arxiv.org/abs/2610.32295) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32295)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32295)

MemCryst 冻结语言模型，使外部情景/事实记忆与条件技能双向演化：重复经历支持技能生成和修订，任务结果调整后续检索权重，不重写已服务记录。 这是文本仿真而非真机控制；“技能单独服务”仍保留用于技能学习的内部记忆。结果反馈分摊给全部服务记录，不是逐条因果归因；未检验错误反馈或未见领域迁移，任务顺序也影响结果。

## RoboCode: Learning Reusable Action Primitives for Robot Manipulation

- [arXiv 2610.32225](https://arxiv.org/abs/2610.32225) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32225)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32225)

先从多任务动作块学习可软组合的共享原语码本，再冻结解码接口，训练任务专属状态到码本编码器。 仅仿真，使用物体位姿/目标等状态而非图像语言输入；评估任务各自训练编码器，可复用码本不等于在线技能增长或未见任务迁移。已核评测部分未明确多种子不确定性及闭环试验次数。

## TTT in VLA Models: Exploring Training with Human Demonstrations

- [arXiv 2610.32094](https://arxiv.org/abs/2610.32094) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32094)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32094)

在InternVLA-A1和π0.5中加入fast-weight TTT，记录人类示范到机器人阶段的记忆传递及截断梯度路径。 负结果限于小规模选杯数据和所测配方，不是对TTT的普遍否定；试验次数报告不足。自回归状态评估仍使用录制图像，并非闭环观测。

## FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation

- [arXiv 2610.31841](https://arxiv.org/abs/2610.31841) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31841)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31841)

编码代理结合RGB-D与腕部力/力矩日志，生成并修订接触探测和力反馈Python程序；经验保存在可执行控制逻辑中，无需任务专属模型训练。 只有5项真机任务、单模型及少量试验；每次开发最多20个实体rollout和4小时，人类负责执行批准、场景操作及最终验收。对照同时移除力反馈和相关例程，并非单独隔离记忆贡献；每次推理耗时4–10分钟。

## WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations

- [arXiv 2610.31834](https://arxiv.org/abs/2610.31834) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31834)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31834)

把真实演示的数字孪生构建写成可执行世界程序，由编码代理诊断回放失败并定向修复场景、资产与物理交互。 这是已录轨迹在重建仿真中的回放，不是真机新策略成功率或sim2real收益。空间指标并非全面胜过Astra；组件消融限于一个任务，尚不能归因长期记忆收益。

## KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations

- [arXiv 2610.31801](https://arxiv.org/abs/2610.31801) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31801)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31801)

把统一14维双臂运动学压缩为每秒2个、由转折边界监督的稀疏运动token，再用LoRA语言模型输出时间片段和描述，并测试新机器人及人手迁移。 编码器采用整回合标准化和对称时间上下文，因此是离线模型。tokenizer比较同时存在输入表示及reader训练样本差异，不仅改变目标函数；分段及语义迁移不等于闭环策略收益。

## RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation

- [arXiv 2610.05414](https://arxiv.org/abs/2610.05414) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.05414)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2610.05414)

基于MuJoCo的移动操作基准，通过固定技能接口分别评估任务成功、子目标进展、空间定位及重复动作后的恢复。 仅仿真、每任务3回合、离散网格导航及固定技能库；抓取候选同时包含GraspNet输出与专家核验的真值兜底标注，不能证明端到端低层控制或自主技能扩展。执行效率仅在成功轨迹统计，反思分数仅在含重复动作循环的回合统计。

## Are Frontier VLM Agents Ready to Be Robot Generalists? An Empirical Study with the Embodied Agent Arena

- [arXiv 2610.00854](https://arxiv.org/abs/2610.00854) · v3 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.00854)
- 收录历史: [2026-10-26 (v3, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2610.00854)

统一评测在1,000个案例中区分几何预测、可供性定位、中间子目标和原生完整任务成功。 并集是事后覆盖，并非已部署集成策略成功率。各源任务保留接口与预算而非全部一致，部分补充回合及缺失记录单独处理。无代码错误和低延迟不能等同物理任务完成；本次是基准证据而非新增真机验证。

## Metro-WM: Long-Horizon Latent Planning with Realisable Sub-Goals

- [arXiv 2609.31868](https://arxiv.org/abs/2609.31868) · v3 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2609.31868)
- 收录历史: [2026-10-26 (v3, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2609.31868)

非参数宏观规划器从离线轨迹图检索真实观测状态，以最短路径子目标和动态重新入图支持长程控制。 新增实验均为仿真。Metro采用固定而非递减时域，并在独立调参任务上选择时域、子目标距离和执行块数；基线使用公开配置。检索状态真实不等于每条连接转移都可保证；语料中罕见的多样布局可能破坏轨迹拼接。

## WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time

- [arXiv 2607.06988](https://arxiv.org/abs/2607.06988) · v3 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2607.06988)
- 收录历史: [2026-10-26 (v3, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2607.06988)

通过人类视频写入世界动作模型的快权重记忆，配对人类—机器人元训练学习视频到动作的迁移接口。 对照是同一WAM内的接口变体，而非原系统完整复现；新增接口实验仅一个任务。FastWAM证据是3.2秒、8帧预测的定性展示，不是闭环控制迁移；部分对照依赖预训练技能潜变量，元训练阶段直接插入并不具备该先验。

## GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

- [arXiv 2607.05369](https://arxiv.org/abs/2607.05369) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2607.05369)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2607.05369)

GaP组合带类型的机器人技能图，在部署前通过仿真排练优化图结构、参数和吞吐。 新增吞吐证据来自仿真，并非新增真机生产率结果。论文明确承认CaP-X对照因已知环境几何信息不同而不公平；MORSL仅对齐部分感知/抓取组件，并未对齐所有运动原语、推理预算和系统选项。任务仍以准静态为主。

## METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

- [arXiv 2610.31656](https://arxiv.org/abs/2610.31656) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31656)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31656)

METTA 将回合内可梯度更新的快速神经记忆与跨回合的紧凑摘要分开。它在 Meta-World ML10/45 未见任务族上报告超过 50% 成功率，并改善长上下文稀疏奖励探索。

## FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies

- [arXiv 2610.31427](https://arxiv.org/abs/2610.31427) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31427)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31427)

固定π0.5，用持续阶段记忆安排GPT-6 Astra审核：熟悉阶段少审核，风险、历史失败与恢复阶段集中审核，无需训练新模型。 80%比较基线来自外部报告，每任务仅5例且场景混合不同，并非匹配重跑。共享记忆使回合不独立，搭塔首个评估回合已有经验；节省比例不是端到端A/B因果效应。仅仿真，且存在漏检失败。 57.2%是逐任务下降比例的均值，并非总平均token的下降比例；统计含输入、输出与缓存输入，不能等同费用下降。

## PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning

- [arXiv 2610.31299](https://arxiv.org/abs/2610.31299) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31299)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31299)

PiHand 将仿真中的动作捕捉跟踪专家蒸馏为目标条件手–物交互潜变量先验，再在潜空间中学习有界残差探索。同一交互先验可支持新物体、新轨迹、接物和双手交接。

## Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

- [arXiv 2610.31166](https://arxiv.org/abs/2610.31166) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31166)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31166)

WholeBodyMem 用 SAM3 对象事件选择历史关键帧，以对象时空 token 和独立记忆注意力向全身动作专家提供已经消失的线索。 这是回合内感知历史，不是跨回合技能积累；真机每任务仅10次且未给均匀记忆真机对照。SAM3漏检与跟踪成本仍是限制。

## Co^2Gen: Collaboratively Generating Task Plans for Decentralized Multi-Robot and Human Collaboration

- [arXiv 2610.30671](https://arxiv.org/abs/2610.30671) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30671)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30671)

通过多智能体规划生成带条件检查的协作程序，将执行轨迹用于分散式SmolVLA训练；把程序级协作经验转成动作策略数据。 最强结论依赖混合人工单臂数据，不能说全流程无人工；自动生成数据单独训练仍有执行瓶颈。仅两任务和有限试次，尚非跨本体普遍结论。

## Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents

- [arXiv 2610.30587](https://arxiv.org/abs/2610.30587) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30587)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30587)

CARE 用评论器判断何时从本地执行器升级到云端，并保持云端接管直到恢复；双向共享交接记忆保留任务进度。 纯仿真决策层评估；本地模型和评论器使用H200，并非实测端侧机器人延迟。阈值按基准调节；云请求比例不包含评论器调用。无真实网络、传感或硬件故障验证。 EmbodiedBench上仍低于纯云端成功率（75%对80%）；云请求比例不等于总计算成本。

## Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live

- [arXiv 2610.30478](https://arxiv.org/abs/2610.30478) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30478)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30478)

预注册对照研究比较将具身经验蒸馏进 LoRA 与推理时检索图文经历；核心实验在同一组权重上开关冻结记忆库。 蒸馏检验功效不足，不能证明经验无法写入权重；只测试窄任务及一种训练方案。图文贡献未分离，自动重置和日志缺陷虽有敏感性分析仍须注意。公开仓库已核实，论文所称制品 release 暂未查到。

## Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation

- [arXiv 2610.30197](https://arxiv.org/abs/2610.30197) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30197)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30197)

在感知、执行、运动学与规划序列化边界注入故障，以匹配种子Oracle区分物理失败和规划接口失败。 只有一个桌面任务、一个模型，每故障强度5次；感知延迟实际均饱和0.5s。不能据此泛化“LLM没有推理缺陷”或实际机器人安全性。

## Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- [arXiv 2609.39304](https://arxiv.org/abs/2609.39304) · v4 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2609.39304)
- 收录历史: [2026-10-23 (v4, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2609.39304)

Scale and Selection 通过增加 rollout 样本量及优胜者–挑战者筛选改进视觉接口机器人代理。本次修订新增蒸馏闭环，将代理辅助执行经验转化为独立机器人策略。

## HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation

- [arXiv 2604.07993](https://arxiv.org/abs/2604.07993) · v3 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2604.07993)
- 收录历史: [2026-10-23 (v3, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2604.07993)

HEX 结合标准化身体部位状态、混合专家本体状态预测器、紧凑视觉历史和流匹配动作，完成类人机器人全身操作。本次修订新增两个家庭长时域任务、ψ0 对照、分布外预训练测试及数据规模与超参数实验。

## Agentic World Action Models

- [arXiv 2610.30136](https://arxiv.org/abs/2610.30136) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30136)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30136)

代码、视频与动作联合去噪连接 agent 规划和控制，但随机域成绩低于 π0.5，技能库仍冻结。

## Asymmetric On-Policy Distillation Learns In-Context Exploration

- [arXiv 2610.30105](https://arxiv.org/abs/2610.30105) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30105)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30105)

特权专家的 on-policy 蒸馏支持共享隐变量下的跨回合探索，但真机样本有限，上下文并非永久技能库。

## AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

- [arXiv 2610.30097](https://arxiv.org/abs/2610.30097) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30097)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30097)

原子子任务信用分配和瓶颈探索改善长程 RL；真机相对 PPO 提高 8.0 个百分点，训练在重建仿真中完成。

## GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

- [arXiv 2610.29866](https://arxiv.org/abs/2610.29866) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29866)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29866)

仅训练时使用的几何监督与时序记忆改善了同底座 VLA；各基准专门适配且记忆逐回合清空，限制了泛化与记忆结论。

## CausGround: Causal Interaction Grounding for Adaptive Embodied Planning

- [arXiv 2610.29702](https://arxiv.org/abs/2610.29702) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29702)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29702)

离线因果知识库改善规划，但 RoboCasa 采用回放式高层评估，部署时知识库不增长。

## From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

- [arXiv 2610.29560](https://arxiv.org/abs/2610.29560) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29560)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29560)

离线修订 harness 将 RoboMME 成功率从 44.38% 提高到 51.38%；运行上下文重置，所述修复不构成新技能发现。

## Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control

- [arXiv 2610.29329](https://arxiv.org/abs/2610.29329) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29329)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29329)

可执行回合内记忆提高了 RoboMME 成绩，但与 Astra+VLA 的种子数和抽帧不同，尚无跨任务技能扩展证据。

## Learning to Absorb Corrections: Critic-Weighted Residual Flow for Vision-Based Insertion

- [arXiv 2610.29117](https://arxiv.org/abs/2610.29117) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29117)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29117)

critic 加权残差学习被 ACT 吸收：关闭残差后的成功率从 16% 提高到 76%，但跨任务遗忘和 VLA 迁移尚未验证。

## inr2action: Encoding Robot Episodes as Neural Implicit Representations for Recall and Action

- [arXiv 2610.28882](https://arxiv.org/abs/2610.28882) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28882)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28882)

用 INR 权重差存储回合视频，问答优于随机水平；离线动作回归尚不能证明闭环控制或可扩展检索。

## T-WLA: Bridging Slow Vision and Fast Touch

- [arXiv 2610.28814](https://arxiv.org/abs/2610.28814) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28814)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28814)

快速触觉编辑器修正待执行动作，但无触觉版本已接近完整模型表现，限制了可归因于触觉的增益。

## HarnessPAI: An Evolving Harness for Physical AI

- [arXiv 2609.29166](https://arxiv.org/abs/2609.29166) · v2 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2609.29166)
- 收录历史: [2026-10-22 (v2, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2609.29166)

新增 DreamZero 微调复用 harness 成功轨迹，报告均值从 5.1% 提高到 26.5%；按评估成绩选 checkpoint 限制了证据强度。

## ASPIRE: Agentic /Skills Discovery for Robotics

- [arXiv 2607.00272](https://arxiv.org/abs/2607.00272) · v2 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2607.00272)
- 收录历史: [2026-10-22 (v2, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2607.00272)

修订新增真机跨回合文本技能积累；单次旋转耗时下降，但魔方总解题时间不单调下降，仍需人类支持。

## UniWALM: Unified World Action Language Model for Embodied Robot Control

- [arXiv 2610.28626](https://arxiv.org/abs/2610.28626) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28626)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28626)

联合去噪视频、动作与语言，并将文字工作记忆反馈到控制；记忆任务和 18 次真机测试的提升未单独隔离记忆贡献，也未验证跨回合检索。

## AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- [arXiv 2610.28589](https://arxiv.org/abs/2610.28589) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28589)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28589)

以成功轨迹 SFT 和多轮 RL 训练 9B 机器人规划器，保持执行器冻结；LIBERO-PRO 达 71.0%，但训练测试共享任务，且无真机结果。

## Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future

- [arXiv 2610.28431](https://arxiv.org/abs/2610.28431) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28431)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28431)

任务与因果状态 token 引导世界—动作预测，处理视觉相似阶段；StageBench 从 40.9% 升至 69.4%，真机提升仍依赖任务示范且测试样本较小。

## EventSync: Event-Driven Memory Updates for History-Dependent Manipulation

- [arXiv 2610.27917](https://arxiv.org/abs/2610.27917) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27917)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27917)

事件监控器在视觉和运动证据确认完成后才写入任务历史；RoboMME 达 64.5%，但需要事件监督，且对照沿用已发表基线。

## When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines

- [arXiv 2610.27714](https://arxiv.org/abs/2610.27714) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27714)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27714)

重采样经验池与等 token 控制揭示驾驶 agent 的记忆收益不稳；结论限于 HighwayEnv、gpt-4o-mini 和 1 Hz，不能泛化到所有长期记忆。

## More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents

- [arXiv 2610.27406](https://arxiv.org/abs/2610.27406) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27406)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27406)

保留原始经验、重建并丢弃任务抽象可减少错误复现；三种子的 ALFWorld 提升限于特定 agent，不能说明所有持久记忆有害。

## SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents

- [arXiv 2610.26995](https://arxiv.org/abs/2610.26995) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.26995)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.26995)

Skill-DAG 记忆与按状态选择的 Skill-GNN 复用成功技能组合；ALFWorld 达 87.1%，未验证新运动技能获取或真机迁移。

## HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents

- [arXiv 2610.23479](https://arxiv.org/abs/2610.23479) · v2 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.23479)
- 收录历史: [2026-10-21 (v2, substantive-revision)](../daily/2026-10-21.zh-CN.md#arxiv-2610.23479)

实质修订新增 42 项 RoboDojo 任务的官方隐藏 seed 评测；46.9% 成功率与 v1 协议不同，公开工具不包含完整评测系统。

## WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning

- [arXiv 2607.18840](https://arxiv.org/abs/2607.18840) · v3 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2607.18840)
- 收录历史: [2026-10-21 (v3, numerical-revision)](../daily/2026-10-21.zh-CN.md#arxiv-2607.18840)

更正后的 C2R 消融将长期记忆边际收益从 3.42 缩至 0.67 个百分点；架构、主表及真机结果未变，修改原因未说明。

## Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy

- [arXiv 2610.26848](https://arxiv.org/abs/2610.26848) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.26848)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.26848)

18 个 RoboDojo 任务、最多 17 轮交互，将起始能力、改进速度、成功和恢复分开衡量；通过历史与工作区剥离对照分析经验积累来源。

## GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation

- [arXiv 2610.26846](https://arxiv.org/abs/2610.26846) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.26846)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.26846)

触觉 RGB 图像接入视觉接口，结合少样本演示与交互记忆做接触操作。

## RoboValue: A Fine-Grained Sim-and-Real Benchmark for Unified Evaluation of Robotic Value Models

- [arXiv 2610.26663](https://arxiv.org/abs/2610.26663) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.26663)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.26663)

15 个模拟和 20 个真实任务，从任务状态、进度、失败恢复和价值一致性评估 value model，超出成功/失败二分类。

## Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds

- [arXiv 2610.25114](https://arxiv.org/abs/2610.25114) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.25114)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.25114)

强模型离线编写、修补并冻结技能，再由纯代码或廉价模型执行。重点是可执行经验的积累、验证、继承与部署成本。

## SARAM: Sparse Adapter Allocation with Reuse and Merging for Lifelong Robot Learning

- [arXiv 2610.24804](https://arxiv.org/abs/2610.24804) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24804)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24804)

复用旧 LoRA、稀疏分配新适配器并惩罚重复；每回合先识别任务，再合并到骨干。为跨任务经验的参数化积累提供与显式技能库不同的对照。

## DialogMem: Evaluating Dialogue-Grounded Embodied Memory in 3D Environments

- [arXiv 2610.24767](https://arxiv.org/abs/2610.24767) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24767)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24767)

将 RGB-D／位姿／人类对话写入记忆，测试实例导航和问答；142 回合、27 个扫描场景、9 类记忆表征，分层诊断对象扎根、检索与行动定位。

## Self-Improving Video-to-Action Models

- [arXiv 2610.24177](https://arxiv.org/abs/2610.24177) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24177)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24177)

视频规划器提出目标视频，V2A 模型以自身交互生成视频—动作训练对并反复改进。

## Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems

- [arXiv 2610.23372](https://arxiv.org/abs/2610.23372) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.23372)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.23372)

以关键事实替换、保事实替换和数值扰动对照，因果检验机器人是否真正使用记忆内容。

## LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence

- [arXiv 2610.23334](https://arxiv.org/abs/2610.23334) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.23334)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.23334)

以语义子任务进度连接 VLM 规划、状态判断与 WAM 动作生成，加入分层视觉记忆和子任务价值学习。

## NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models

- [arXiv 2610.23271](https://arxiv.org/abs/2610.23271) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.23271)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.23271)

先分别训练技能，再用任务条件超网络生成 action expert 参数，减少直接合并权重的冲突。

## Spatial Memory by Agents, for Agents

- [arXiv 2610.22736](https://arxiv.org/abs/2610.22736) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22736)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22736)

Designer Agent 根据固定 Query Agent 的反馈迭代记忆构建和检索程序，再冻结实现，在留出的观测历史上评估。

## When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

- [arXiv 2610.22556](https://arxiv.org/abs/2610.22556) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22556)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22556)

把相邻动作块对同一未来时刻的预测分歧作为记忆写入信号，用有限视觉槽位保存关键帧，并过滤重复画面。

## Scaling Online Exploration for Robot Agents

- [arXiv 2610.22496](https://arxiv.org/abs/2610.22496) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22496)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22496)

冻结编码代理通过机器人接口探索，将感知、规划与控制沉淀为可执行程序；以持久笔记和已验证技能支持跨回合、跨任务复用。

