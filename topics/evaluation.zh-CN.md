# 评测、鲁棒性与安全

[English](evaluation.md) | [简体中文](evaluation.zh-CN.md) | [所有主题](README.zh-CN.md)

73 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

## UniAction: Unified Action Conditioning for World Models

- [arXiv 2610.32977](https://arxiv.org/abs/2610.32977) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32977)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32977)

把力、相机、手部及机器人位姿动作表示为带语义身份与连续时空坐标的稀疏元素，映射到视频骨干原生RoPE几何；用基数校准attention补偿不同动作token数量。 这是视频生成动作跟随得分，不是闭环机器人成功率；不同条件分支可训练参数量不同。联合训练并非所有指标更好：相机LPIPS .4863，高于专家.4780。四种预设动作不证明任意动作或未见本体泛化。

## RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

- [arXiv 2610.32971](https://arxiv.org/abs/2610.32971) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32971)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32971)

统一17种鲁棒/安全RL算法及6种标准对照，提供可复用接口及含延迟、语义的单因素/组合部署扰动。 并非每算法运行每任务；保留各自原生预算，算法族混合均值会混入基础学习器强弱。π0.5实验仅单个微调模型的离线关节示范轨迹跟踪，不是闭环VLA成功率或真机验证。

## If at First You Don’t Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

- [arXiv 2610.32941](https://arxiv.org/abs/2610.32941) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32941)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32941)

用冻结策略rollout训练小型失败头，触发后回放实际已完成机械臂运动的逆序，再交回原策略重试。 仅仿真；汇总结果包含选参种子，留出种子π0.5收益为0.70个百分点。回退不恢复物体或保证安全，失败头仍需标注rollout训练。

## Regularised RL improves sim-to-real transfer

- [arXiv 2610.32855](https://arxiv.org/abs/2610.32855) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32855)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32855)

用缓慢更新参考策略把soft mellowmax扩展到连续控制actor–critic，检验正则化是否改善超越名义训练回报的sim2real鲁棒性。 回报不是成功率；仍需要域随机化，温度参数随任务变化。PPO/FastTD3因未通过预设仿真安全筛查而没有ANYmal扰动部署，空白不能算实测真机失败；MuJoCo调参预算不完全相等。

## Predictive Long-Horizon Progress Modeling with Action-Aware Quantification

- [arXiv 2610.32776](https://arxiv.org/abs/2610.32776) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32776)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32776)

NimCritic以视频预测训练约束进度/完成度双输出，结合历史进度扰动与跨模态对齐；LOOM评测包含300条跨本体轨迹、19,618个人工校准帧。 上述是离线评价，不是机器人任务成功率。多子任务依赖离线VLM分段，非直接证明在线实时裁判可用；训练800余小时、48加速器，未报告用奖励后训练策略的闭环收益。

## Semantic Representation for Agentic Self-Play in Automated Laboratories

- [arXiv 2610.32755](https://arxiv.org/abs/2610.32755) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32755)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32755)

VERID提供持久语义实验室孪生，支持状态查询、执行前仿真门控、同步轨迹及故障续跑；代理跨运行保留物理操作边界和分析经验。 这是小规模案例而非隔离记忆因果效应的消融：挑战实例与实验策略同时变化。使用预设结构化Harness、内部Gemini检查点及受监督运行中的人工批准门控；未证明生物学突破或通用机器人策略迁移。

## When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

- [arXiv 2610.32431](https://arxiv.org/abs/2610.32431) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32431)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32431)

MART-GRPO 用微调后冻结的VLM从完整rollout视频定位最后一个未恢复的可见错误，截断其后失败惩罚，同时保留成功轨迹项及原归一化；理想停止理论提供动机，但不认证实际回溯实现。 仅仿真；策略看单相机，VLM审查三视角，另需标注及VLM微调。边界使用完整未来轨迹，不一定满足理想停止条件；一项任务下降1.95个百分点，留出场景种子不等于独立训练种子。

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

## ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences

- [arXiv 2610.32222](https://arxiv.org/abs/2610.32222) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32222)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32222)

结合动作错配和视频错配偏好，训练无需奖励计算时参考视频的模型，联合评价视觉质量与动作跟随；构建AVM-Eval（67.2k对）和AVM-Pref（506.3k对）。 RL证据限于一个2B世界模型与AgiBotWorld，不是机器人任务成功率。未直接监督物理一致性，评分依赖VLM；奖励计算无需参考不等于数据构建无需参考，成对排序也不保证物理正确。

## Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems

- [arXiv 2610.32208](https://arxiv.org/abs/2610.32208) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32208)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32208)

用稀疏自编码器分解OpenVLA内部激活，预测失败并由外部VLM解释与结果相关的行为；通过分支重试估计不可恢复时间点。 仅仿真、单模型；SAE无监督训练使用全部500轨迹，监督预测器才留出。每点4次分支估计粗糙且受剩余预算影响；相关特征并非因果机制或已验证安全干预。

## Ψ-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model

- [arXiv 2610.32177](https://arxiv.org/abs/2610.32177) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32177)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32177)

统一token接口生成及理解文字、图像、几何和运动，通过自适应思维流选择中间表示；以GRPO在视觉问答上验证如何选择推理流。 这里的sim-to-real是已录机器人视频上的视觉问答，不是真机部署。光流和轨迹是代理动作而非执行器命令；未隔离统一能力训练时的正负迁移，物理控制仍属未来工作。

## Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies

- [arXiv 2610.32102](https://arxiv.org/abs/2610.32102) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32102)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32102)

联合研究执行动作长度与flow求解步数，检验浅采样何时有效或有害。 长开环在移动目标上失效；加速指摊销推理成本，不保证任务墙钟加速。论文对仿真任务总数及π0.5动作块配置存在不一致描述。

## TTT in VLA Models: Exploring Training with Human Demonstrations

- [arXiv 2610.32094](https://arxiv.org/abs/2610.32094) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32094)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32094)

在InternVLA-A1和π0.5中加入fast-weight TTT，记录人类示范到机器人阶段的记忆传递及截断梯度路径。 负结果限于小规模选杯数据和所测配方，不是对TTT的普遍否定；试验次数报告不足。自回归状态评估仍使用录制图像，并非闭环观测。

## Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates

- [arXiv 2610.31859](https://arxiv.org/abs/2610.31859) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31859)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31859)

审计可训练矩阵和AdamW状态保持bf16、无fp32主副本时的更新舍入。 仅一个任务集、缩短训练；未单独消融优化器矩精度。SmolVLA评测器差异限制跨论文比较；不能推断所有bf16计算或JAX训练均受影响。

## FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation

- [arXiv 2610.31841](https://arxiv.org/abs/2610.31841) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31841)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31841)

编码代理结合RGB-D与腕部力/力矩日志，生成并修订接触探测和力反馈Python程序；经验保存在可执行控制逻辑中，无需任务专属模型训练。 只有5项真机任务、单模型及少量试验；每次开发最多20个实体rollout和4小时，人类负责执行批准、场景操作及最终验收。对照同时移除力反馈和相关例程，并非单独隔离记忆贡献；每次推理耗时4–10分钟。

## SEVI: Safe Evidential Real-World Reinforcement Learning

- [arXiv 2610.31829](https://arxiv.org/abs/2610.31829) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31829)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31829)

证据式安全critic同时估计违规风险与认知不确定性，在在线RL中筛查动作并调用离线训练的恢复策略。 仅1项真机、2项仿真任务，无零违规形式保证。真机使用50条成功先验示范、200条恢复示范及验证集阈值；最终成功率与累计训练事件口径不同。

## KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations

- [arXiv 2610.31801](https://arxiv.org/abs/2610.31801) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31801)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31801)

把统一14维双臂运动学压缩为每秒2个、由转折边界监督的稀疏运动token，再用LoRA语言模型输出时间片段和描述，并测试新机器人及人手迁移。 编码器采用整回合标准化和对称时间上下文，因此是离线模型。tokenizer比较同时存在输入表示及reader训练样本差异，不仅改变目标函数；分段及语义迁移不等于闭环策略收益。

## FLORA: An Open Model Suite for Scaling Robotics Data Engines

- [arXiv 2610.31779](https://arxiv.org/abs/2610.31779) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31779)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31779)

开放标注模型套件提供时序分段、动作意图描述及结果/稠密/规则奖励；分段与描述使用RL后训练，发布的奖励模型仅用SFT。 并非所有指标最优，各系统帧预算及算力不同。约125倍成本优势依赖假定GPU价格和建模吞吐，未含部署开销、生产GPU小时口径未核实，参考标注版本亦未完全匹配；这里未直接证明下游策略学习提升。

## See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space

- [arXiv 2610.31762](https://arxiv.org/abs/2610.31762) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31762)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31762)

RepresentNav从多个冻结视觉骨干的多层特征构造策略导向表征，在同空间以JEPA训练预测未来的潜在推理，再生成路点。 外部基线来自原论文且观测设置不全相同。真机导航演示不能证明操作迁移；作者明确尚未验证操作、灵巧手或全身控制。

## ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

- [arXiv 2610.24512](https://arxiv.org/abs/2610.24512) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.24512)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2610.24512)

包含8类接触丰富技能、36个参考任务及40余可打印资产与配套仿真的基准；在6任务上比较视觉及视触觉学习策略。 四系统的预训练、观测历史及触觉接口不同，并非完全隔离变量的触觉消融；36任务中仅6项做学习策略评估。魔术贴固定使部分原本需另一臂稳定物体的任务可由单臂完成。刚性/关节打印资产不覆盖形变接触；触觉负结果只适用于所测策略与传感器，不能泛化为触觉无用。

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

## Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning

- [arXiv 2608.24885](https://arxiv.org/abs/2608.24885) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2608.24885)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2608.24885)

WorldEcho以视觉筛查与末端轨迹对齐评估非专家动作跟随；WorldSync结合更广动作数据、动力学表征约束及干预效果监督。 主表微小门控差距仅为点估计，未证明显著；视觉筛查不保证完整性，人工核验每维仅15段。视频指标使用重建参考和独立生成批次；不同预训练语料及基线历史不能支持受控数据效率结论。

## PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views

- [arXiv 2608.19188](https://arxiv.org/abs/2608.19188) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2608.19188)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2608.19188)

利用占据条件的全局与局部几何表征，从带分割的单视角RGB-D观测生成并细化双臂抓取对。 真机只评本方法，无同协议真机基线成功率；成功定义为抬起，不是完成后续操作。候选先经无碰撞及运动学可达过滤。另一个真实RGB-D数据集表使用数字孪生仿真指标，并非真机成功率，81.54%的GS不可与39/54抬起率混淆。

## RAPAC-DP: Response-Aligned Pending-Action Compensation for Diffusion Policies under Delayed Execution

- [arXiv 2608.15924](https://arxiv.org/abs/2608.15924) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2608.15924)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2608.15924)

在冻结扩散/流策略上加入待执行动作编码器和LoRA补偿，将动作块对齐计划交接时间，仅用无延迟示范构造延迟条件训练样本。 每方法/任务仅一个检查点，置信区间反映试验抽样而非训练种子鲁棒性。固定传送带速度/起点和离散注入延迟限制其对任意网络抖动的结论；低延迟动态抓取73.3%低于RTC76.7%。需要训练适配器，不是免训练修复。

## Semantic Anchoring for Robotic Action Representations

- [arXiv 2607.13597](https://arxiv.org/abs/2607.13597) · v3 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2607.13597)
- 收录历史: [2026-10-26 (v3, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2607.13597)

以冻结的操作文本编码器为锚，通过共享/私有表征的辅助对齐目标保留VLA微调中的任务语义，推理时移除辅助模块。 相关性不能证明语义侵蚀是分布外失败的唯一原因；各架构沿用不同官方微调方案。冻结语义编码器限制性能，共享/私有因子无可识别性保证；属于下游微调而非部署中的持续适配。

## GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

- [arXiv 2607.05369](https://arxiv.org/abs/2607.05369) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2607.05369)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2607.05369)

GaP组合带类型的机器人技能图，在部署前通过仿真排练优化图结构、参数和吞吐。 新增吞吐证据来自仿真，并非新增真机生产率结果。论文明确承认CaP-X对照因已知环境几何信息不同而不公平；MORSL仅对齐部分感知/抓取组件，并未对齐所有运动原语、推理预算和系统选项。任务仍以准静态为主。

## Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration

- [arXiv 2605.31196](https://arxiv.org/abs/2605.31196) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2605.31196)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2605.31196)

TouchSafeBench在仿真人机共处中评估当前碰撞识别和提前预警，区分机器人—场景与人类接触风险。 真实录像无物理接触，且为人头戴相机；标签是1米阈值的二元接近状态，并非实际碰撞安全。误报统计只有12个难负例。提示测试仅一个模型/条件，单专家按固定顺序看不同视角；未验证闭环安全干预。

## Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

- [arXiv 2610.31670](https://arxiv.org/abs/2610.31670) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31670)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31670)

无需训练，以 DTW 轨迹邻域与感知表征的 CKNNA 对齐，离线筛选策略及 VLM 骨干。 真实机器人 r=.831 使用探索性 h=110；预设 h=7 仅 r=.429、p=.236。相关不代表优化该指标会提高成功率；不能替代闭环测试。

## Progress Probes P²: Lightweight Runtime Monitoring for Vision-Language-Action Models

- [arXiv 2610.31613](https://arxiv.org/abs/2610.31613) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31613)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31613)

仅用成功示范训练线性探针，从π0.5内部激活估计任务进度；执行落后于名义进度时报警，无需外部基础模型或失败训练样本。 仅测试π0.5，细微洒落可能漏检。PDF全任务硬件表声称平均0.78，但六项显示值算术均值为0.72，汇总口径需澄清。0.026毫秒不含VLA推理；未找到官方代码链接。 “未见”指探针训练未见，不一定是底层微调VLA未见。

## Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models

- [arXiv 2610.31569](https://arxiv.org/abs/2610.31569) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31569)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31569)

将停止与失败两种信号加入动作块，采用结构化注意力和更快的信号去噪，让较干净的状态预测反过来指导动作。训练使用成功、失败及恢复轨迹，无需逐帧进度标注。 真实评分并非成功率；动作监督及训练预算匹配，但Echo额外使用失败状态数据。跨方法比较集中于插花，部分采用适配协议；两任务无失败测试样本。高层自动终止/重规划收益尚未验证。 三秒结果窗口F1并非瞬时故障检测；仿真状态准确率针对指定窗口的进行中/成功帧，并非通用三分类失败检测。

## Skeleton-Grounded Latent Action Model for Robot World Models

- [arXiv 2610.31474](https://arxiv.org/abs/2610.31474) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31474)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31474)

骨架监督将潜动作拆成运动学与残差；交换重建、分支 dropout 和动作适配器支持可控视频预测。 DROID 预测跨度 0.8 秒；不同方法有效轨迹子集不完全相同。人→机器人仅两个生成视频例子。策略评估只有 9 次真实成功，不能代替闭环验证。

## FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies

- [arXiv 2610.31427](https://arxiv.org/abs/2610.31427) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31427)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31427)

固定π0.5，用持续阶段记忆安排GPT-6 Astra审核：熟悉阶段少审核，风险、历史失败与恢复阶段集中审核，无需训练新模型。 80%比较基线来自外部报告，每任务仅5例且场景混合不同，并非匹配重跑。共享记忆使回合不独立，搭塔首个评估回合已有经验；节省比例不是端到端A/B因果效应。仅仿真，且存在漏检失败。 57.2%是逐任务下降比例的均值，并非总平均token的下降比例；统计含输入、输出与缓存输入，不能等同费用下降。

## Learning Robot Behavior Priors from Non-Robotic Synthetic Data

- [arXiv 2610.31275](https://arxiv.org/abs/2610.31275) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31275)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31275)

用MDP、上下文bandit和线性动力系统等程序化非机器人数据预训练Transformer，通过示例上下文预测未见机器人动作。 仅离线开环动作预测，输入是状态而非视觉，不是真机执行成功率；“零样本”仍使用任务内状态动作上下文。

## RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation

- [arXiv 2610.31121](https://arxiv.org/abs/2610.31121) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31121)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31121)

用统一时序场景图比较生成与参考视频的物体、关系变化和 3D 路径；引入 1,000 场景的 ShareRobot-SG。 小样本相关不能证明逐视频可靠性；物体 F1 不及 SG-Ego。单参考、单被操作物体和提取错误会惩罚有效替代方案；不认证动作可执行性。

## TEAR: Task-Evidence Authority Routing for Robotic Manipulation

- [arXiv 2610.30819](https://arxiv.org/abs/2610.30819) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30819)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30819)

在机器人本地结合网络质量、CLIP任务语义与历史状态，用因果时序卷积预测稀疏交接事件，切换人类遥操作与本地VLA控制。 真实评估有人监督，两回合共含4次人工切换；不能称完全自动仲裁。仅两种相近搬运任务与合成网络扰动。离线交接F1为0.308、召回0.286，低于规则基线召回0.429。未找到代码链接。 两种设置分别训练路由器。

## When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies

- [arXiv 2610.30735](https://arxiv.org/abs/2610.30735) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30735)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30735)

直接用既有流匹配策略做一次 Euler 推理，跨六个 VLA 和一个 DiT 检查是否必须多步采样；无需为单步额外蒸馏。 不能把总体接近等同真机逐任务等价：关烤箱87%→74%，真机预算不足以确认预设等价界限；较小模型长程任务会退化，也未验证单步 RL 更新。

## Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation

- [arXiv 2610.30643](https://arxiv.org/abs/2610.30643) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30643)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30643)

FETA 在测试时只对选中的关键动作索取一次二元反馈，并据此更新导航策略。它先筛选不稳定轨迹，再定位熵梯度大的决策步骤，按策略与反馈的分歧加权更新。

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

## The Bitter Lesson Comes to Robotics

- [arXiv 2610.25287](https://arxiv.org/abs/2610.25287) · v2 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.25287)
- 收录历史: [2026-10-23 (v2, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2610.25287)

《The Bitter Lesson Comes to Robotics》比较前沿语言模型在 40 次动作预算下直接控制真机 YAM 机械臂的表现。本次修订把 7 个模型、12 种设置扩展到 9 个模型、15 种设置，并更新历史性能趋势拟合。

## Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- [arXiv 2609.39304](https://arxiv.org/abs/2609.39304) · v4 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2609.39304)
- 收录历史: [2026-10-23 (v4, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2609.39304)

Scale and Selection 通过增加 rollout 样本量及优胜者–挑战者筛选改进视觉接口机器人代理。本次修订新增蒸馏闭环，将代理辅助执行经验转化为独立机器人策略。

## From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks

- [arXiv 2610.30051](https://arxiv.org/abs/2610.30051) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30051)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30051)

LIBERO-10 工具控制基准评估无操作预训练的前沿模型；44/100 与 43/100 的差距不足以形成可靠排名。

## From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

- [arXiv 2610.29560](https://arxiv.org/abs/2610.29560) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29560)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29560)

离线修订 harness 将 RoboMME 成功率从 44.38% 提高到 51.38%；运行上下文重置，所述修复不构成新技能发现。

## How Representational Priors Shape Generalization in World Action Models

- [arXiv 2610.29168](https://arxiv.org/abs/2610.29168) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29168)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29168)

跨骨干的表征几何与 WAM 鲁棒性相关，但预训练和架构未完全匹配，不能作因果解释。

## SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training

- [arXiv 2610.29161](https://arxiv.org/abs/2610.29161) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29161)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29161)

自动干预采集支持控变量的 VLA 后训练比较；真机提升体现算法改动迁移，并非仿真策略零样本转真机。

## SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model

- [arXiv 2606.20698](https://arxiv.org/abs/2606.20698) · v2 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2606.20698)
- 收录历史: [2026-10-22 (v2, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2606.20698)

修订验证安全评估头校准，主成功率表未变；Level II 增益很小，代理成本不能保证真实部署安全。

## μ0: A Scalable 3D Interaction-Trace World Model

- [arXiv 2606.13769](https://arxiv.org/abs/2606.13769) · v3 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2606.13769)
- 收录历史: [2026-10-22 (v3, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2606.13769)

v3 揭示长程完成率低、动作块延迟高于 π0.5；原子任务主成绩未变，不能据此宣称组合能力进步。

## Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

- [arXiv 2610.28613](https://arxiv.org/abs/2610.28613) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28613)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28613)

视触觉世界模型支持评测与策略后训练；四项 ARX 任务真机均值从 SFT 的 59.1% 升至 70.8%，但其中一项任务低于 SFT。

## PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations

- [arXiv 2610.28019](https://arxiv.org/abs/2610.28019) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28019)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28019)

用较新的提交前观测验证冻结 flow 策略的候选动作块；真机成功率从 60% 升至 82%，同时增加延迟，且不提供校准的安全保证。

## When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines

- [arXiv 2610.27714](https://arxiv.org/abs/2610.27714) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27714)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27714)

重采样经验池与等 token 控制揭示驾驶 agent 的记忆收益不稳；结论限于 HighwayEnv、gpt-4o-mini 和 1 Hz，不能泛化到所有长期记忆。

## VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs

- [arXiv 2610.27698](https://arxiv.org/abs/2610.27698) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27698)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27698)

成对评测 VLA 视觉调优的目标收益与跨维度保留；10 个设置中 8 个非目标均值下降，研究干预是定向微调而非在线持续学习。

## More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents

- [arXiv 2610.27406](https://arxiv.org/abs/2610.27406) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27406)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27406)

保留原始经验、重建并丢弃任务抽象可减少错误复现；三种子的 ALFWorld 提升限于特定 agent，不能说明所有持久记忆有害。

## Training Controllable World Models via Action Influence Maximization

- [arXiv 2610.27387](https://arxiv.org/abs/2610.27387) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27387)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27387)

动作影响力目标引导可控世界模型的主动数据采集；Push-T 特定可控性指标对应 85 倍数据量比，证据仅覆盖两个仿真环境。

## SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents

- [arXiv 2610.26995](https://arxiv.org/abs/2610.26995) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.26995)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.26995)

Skill-DAG 记忆与按状态选择的 Skill-GNN 复用成功技能组合；ALFWorld 达 87.1%，未验证新运动技能获取或真机迁移。

## PrismWAM: Decoupling State Representations in World Action Models

- [arXiv 2610.26564](https://arxiv.org/abs/2610.26564) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.26564)
- 收录历史: [2026-10-21 (v1, supplemental-previous-batch)](../daily/2026-10-21.zh-CN.md#arxiv-2610.26564)

补核 2026-10-20 公告：解耦 RGB 目标、深度未来与动作；基础版 RoboTwin C2R 为 70.57%，真机使用 RGB-D，15B 结果另有预训练。

## HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents

- [arXiv 2610.23479](https://arxiv.org/abs/2610.23479) · v2 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.23479)
- 收录历史: [2026-10-21 (v2, substantive-revision)](../daily/2026-10-21.zh-CN.md#arxiv-2610.23479)

实质修订新增 42 项 RoboDojo 任务的官方隐藏 seed 评测；46.9% 成功率与 v1 协议不同，公开工具不包含完整评测系统。

## WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning

- [arXiv 2607.18840](https://arxiv.org/abs/2607.18840) · v3 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2607.18840)
- 收录历史: [2026-10-21 (v3, numerical-revision)](../daily/2026-10-21.zh-CN.md#arxiv-2607.18840)

更正后的 C2R 消融将长期记忆边际收益从 3.42 缩至 0.67 个百分点；架构、主表及真机结果未变，修改原因未说明。

## DEFLECT: Temporal Counterfactual Preference Learning for Delay-Robust Asynchronous VLAs

- [arXiv 2605.19294](https://arxiv.org/abs/2605.19294) · v3 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2605.19294)
- 收录历史: [2026-10-21 (v3, substantive-revision)](../daily/2026-10-21.zh-CN.md#arxiv-2605.19294)

修订为抗延迟 VLA 偏好学习补充跨骨干及继续训练对照；GR00T 在四步延迟下达 73.10%，协议变化使新旧版 headline 数字不可直接比较。

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

## DialogMem: Evaluating Dialogue-Grounded Embodied Memory in 3D Environments

- [arXiv 2610.24767](https://arxiv.org/abs/2610.24767) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24767)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24767)

将 RGB-D／位姿／人类对话写入记忆，测试实例导航和问答；142 回合、27 个扫描场景、9 类记忆表征，分层诊断对象扎根、检索与行动定位。

## LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models

- [arXiv 2610.24587](https://arxiv.org/abs/2610.24587) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24587)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24587)

22 类静态扰动、20 类运行时干预、1,648 个有效变体任务；17 种 VLA/WAM 等策略统一评估，覆盖反馈利用、失败恢复和组合扰动。

## LIBERO-Dynamic: Benchmarking Robotic Manipulation in Dynamic Environments

- [arXiv 2610.24579](https://arxiv.org/abs/2610.24579) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24579)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24579)

40 个 LIBERO 任务加入 3 类轨迹×3 档速度，推理期间按实测延迟推进物理；6 个策略每配置 1,800 个动态条件，9,000 条动态示范，面向预测、实时性与重规划的公平比较。

## Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems

- [arXiv 2610.23372](https://arxiv.org/abs/2610.23372) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.23372)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.23372)

以关键事实替换、保事实替换和数值扰动对照，因果检验机器人是否真正使用记忆内容。

## Spatial Memory by Agents, for Agents

- [arXiv 2610.22736](https://arxiv.org/abs/2610.22736) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22736)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22736)

Designer Agent 根据固定 Query Agent 的反馈迭代记忆构建和检索程序，再冻结实现，在留出的观测历史上评估。

## When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

- [arXiv 2610.22556](https://arxiv.org/abs/2610.22556) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22556)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22556)

把相邻动作块对同一未来时刻的预测分歧作为记忆写入信号，用有限视觉槽位保存关键帧，并过滤重复画面。

