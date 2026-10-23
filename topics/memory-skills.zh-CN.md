# 记忆、技能与持续学习

[English](memory-skills.md) | [简体中文](memory-skills.zh-CN.md) | [所有主题](README.zh-CN.md)

44 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

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

