# 评测、鲁棒性与安全

[English](evaluation.md) | [简体中文](evaluation.zh-CN.md) | [所有主题](README.zh-CN.md)

42 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

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

