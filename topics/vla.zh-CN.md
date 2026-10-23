# 视觉—语言—动作模型

[English](vla.md) | [简体中文](vla.zh-CN.md) | [所有主题](README.zh-CN.md)

45 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

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

## FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies

- [arXiv 2610.31427](https://arxiv.org/abs/2610.31427) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31427)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31427)

固定π0.5，用持续阶段记忆安排GPT-6 Astra审核：熟悉阶段少审核，风险、历史失败与恢复阶段集中审核，无需训练新模型。 80%比较基线来自外部报告，每任务仅5例且场景混合不同，并非匹配重跑。共享记忆使回合不独立，搭塔首个评估回合已有经验；节省比例不是端到端A/B因果效应。仅仿真，且存在漏检失败。 57.2%是逐任务下降比例的均值，并非总平均token的下降比例；统计含输入、输出与缓存输入，不能等同费用下降。

## FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models

- [arXiv 2610.31423](https://arxiv.org/abs/2610.31423) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31423)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31423)

在π0.5上利用当前多模态输入、状态及动作历史预测未来交互意图，动态调节全局/腕部视角；用轨迹自动构造弱监督标签。 真机提升为13.3个百分点；跨本体和多种摄像头配置尚待验证。模块需训练，不是无需训练的推理期补丁。

## Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

- [arXiv 2610.31166](https://arxiv.org/abs/2610.31166) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31166)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31166)

WholeBodyMem 用 SAM3 对象事件选择历史关键帧，以对象时空 token 和独立记忆注意力向全身动作专家提供已经消失的线索。 这是回合内感知历史，不是跨回合技能积累；真机每任务仅10次且未给均匀记忆真机对照。SAM3漏检与跟踪成本仍是限制。

## UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry

- [arXiv 2610.30991](https://arxiv.org/abs/2610.30991) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30991)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30991)

将未来视觉、3D 场景流和动作放入三专家联合注意力模型，以 10 个目标联合训练；部署不需场景流输入。 58.9% 是最佳评估种子；87.7% 是最佳已评检查点。实机逐任务训练、初始条件在示范范围内；流伪标签有噪声。

## TEAR: Task-Evidence Authority Routing for Robotic Manipulation

- [arXiv 2610.30819](https://arxiv.org/abs/2610.30819) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30819)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30819)

在机器人本地结合网络质量、CLIP任务语义与历史状态，用因果时序卷积预测稀疏交接事件，切换人类遥操作与本地VLA控制。 真实评估有人监督，两回合共含4次人工切换；不能称完全自动仲裁。仅两种相近搬运任务与合成网络扰动。离线交接F1为0.308、召回0.286，低于规则基线召回0.429。未找到代码链接。 两种设置分别训练路由器。

## DRILL: Training World Models to Improve Policies, Not Predict Pixels

- [arXiv 2610.30814](https://arxiv.org/abs/2610.30814) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30814)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30814)

DRILL 直接优化世界模型生成的想象 rollout 对策略学习的帮助。其低成本加权代理目标与双层元梯度方案，把下游回报作为目标，而非仅追求像素预测精度。

## When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies

- [arXiv 2610.30735](https://arxiv.org/abs/2610.30735) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30735)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30735)

直接用既有流匹配策略做一次 Euler 推理，跨六个 VLA 和一个 DiT 检查是否必须多步采样；无需为单步额外蒸馏。 不能把总体接近等同真机逐任务等价：关烤箱87%→74%，真机预算不足以确认预设等价界限；较小模型长程任务会退化，也未验证单步 RL 更新。

## SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation

- [arXiv 2610.30732](https://arxiv.org/abs/2610.30732) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30732)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30732)

SmolVLA-MoE 在动作模块中加入按 token 路由的稀疏 FFN 专家与共享专家，并冻结 VLM。LIBERO 平均成功率为 84.25%，对比稠密 SmolVLA 的 82.75%；约激活 5 亿参数、存储 8 亿参数。

## Co^2Gen: Collaboratively Generating Task Plans for Decentralized Multi-Robot and Human Collaboration

- [arXiv 2610.30671](https://arxiv.org/abs/2610.30671) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30671)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30671)

通过多智能体规划生成带条件检查的协作程序，将执行轨迹用于分散式SmolVLA训练；把程序级协作经验转成动作策略数据。 最强结论依赖混合人工单臂数据，不能说全流程无人工；自动生成数据单独训练仍有执行瓶颈。仅两任务和有限试次，尚非跨本体普遍结论。

## Self-Distilling Future Video Representations for World Action Models

- [arXiv 2610.30320](https://arxiv.org/abs/2610.30320) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30320)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30320)

用观测历史与 EMA 教师自蒸馏，改善单次视频去噪产生的未来表征，再供动作解码器使用。 附录说明成功评分允许部分得分，不能都理解为完整成功率。未加入人类视频时，迁移指令遵循为 0%；跨具身对应是隐式学习。

## Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- [arXiv 2609.39304](https://arxiv.org/abs/2609.39304) · v4 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2609.39304)
- 收录历史: [2026-10-23 (v4, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2609.39304)

Scale and Selection 通过增加 rollout 样本量及优胜者–挑战者筛选改进视觉接口机器人代理。本次修订新增蒸馏闭环，将代理辅助执行经验转化为独立机器人策略。

## FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence

- [arXiv 2609.17210](https://arxiv.org/abs/2609.17210) · v2 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2609.17210)
- 收录历史: [2026-10-23 (v2, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2609.17210)

FluxVLA 统一策略数据、训练、评估与机器人执行接口。本次大幅扩展的修订新增 RLinf 在线 PPO 接口、更广泛的仿真与真机集成，以及成对后训练实验；它是一套工程平台，而非新的基础策略。

## HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation

- [arXiv 2604.07993](https://arxiv.org/abs/2604.07993) · v3 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2604.07993)
- 收录历史: [2026-10-23 (v3, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2604.07993)

HEX 结合标准化身体部位状态、混合专家本体状态预测器、紧凑视觉历史和流匹配动作，完成类人机器人全身操作。本次修订新增两个家庭长时域任务、ψ0 对照、分布外预训练测试及数据规模与超参数实验。

## Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models

- [arXiv 2602.12628](https://arxiv.org/abs/2602.12628) · v5 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2602.12628)
- 收录历史: [2026-10-23 (v5, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2602.12628)

RL-Co 先用仿真与真机示范共同监督预热，再在仿真 RL 中保留真机监督约束。本次修订新增更强的 rollout 蒸馏对照，并明确真机统计评估的范围。

## Agentic World Action Models

- [arXiv 2610.30136](https://arxiv.org/abs/2610.30136) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30136)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30136)

代码、视频与动作联合去噪连接 agent 规划和控制，但随机域成绩低于 π0.5，技能库仍冻结。

## AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

- [arXiv 2610.30097](https://arxiv.org/abs/2610.30097) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30097)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30097)

原子子任务信用分配和瓶颈探索改善长程 RL；真机相对 PPO 提高 8.0 个百分点，训练在重建仿真中完成。

## GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

- [arXiv 2610.29866](https://arxiv.org/abs/2610.29866) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29866)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29866)

仅训练时使用的几何监督与时序记忆改善了同底座 VLA；各基准专门适配且记忆逐回合清空，限制了泛化与记忆结论。

## From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

- [arXiv 2610.29560](https://arxiv.org/abs/2610.29560) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29560)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29560)

离线修订 harness 将 RoboMME 成功率从 44.38% 提高到 51.38%；运行上下文重置，所述修复不构成新技能发现。

## Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control

- [arXiv 2610.29329](https://arxiv.org/abs/2610.29329) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29329)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29329)

可执行回合内记忆提高了 RoboMME 成绩，但与 Astra+VLA 的种子数和抽帧不同，尚无跨任务技能扩展证据。

## SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training

- [arXiv 2610.29161](https://arxiv.org/abs/2610.29161) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29161)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29161)

自动干预采集支持控变量的 VLA 后训练比较；真机提升体现算法改动迁移，并非仿真策略零样本转真机。

## inr2action: Encoding Robot Episodes as Neural Implicit Representations for Recall and Action

- [arXiv 2610.28882](https://arxiv.org/abs/2610.28882) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28882)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28882)

用 INR 权重差存储回合视频，问答优于随机水平；离线动作回归尚不能证明闭环控制或可扩展检索。

## Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration

- [arXiv 2610.28880](https://arxiv.org/abs/2610.28880) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28880)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28880)

三维语义扩增将单个人类视频转为机器人数据，控变量实验增益明显，但与遥操作的比较不匹配，仍需人工设置。

## T-WLA: Bridging Slow Vision and Fast Touch

- [arXiv 2610.28814](https://arxiv.org/abs/2610.28814) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28814)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28814)

快速触觉编辑器修正待执行动作，但无触觉版本已接近完整模型表现，限制了可归因于触觉的增益。

## SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model

- [arXiv 2606.20698](https://arxiv.org/abs/2606.20698) · v2 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2606.20698)
- 收录历史: [2026-10-22 (v2, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2606.20698)

修订验证安全评估头校准，主成功率表未变；Level II 增益很小，代理成本不能保证真实部署安全。

## UniWALM: Unified World Action Language Model for Embodied Robot Control

- [arXiv 2610.28626](https://arxiv.org/abs/2610.28626) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28626)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28626)

联合去噪视频、动作与语言，并将文字工作记忆反馈到控制；记忆任务和 18 次真机测试的提升未单独隔离记忆贡献，也未验证跨回合检索。

## AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- [arXiv 2610.28589](https://arxiv.org/abs/2610.28589) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28589)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28589)

以成功轨迹 SFT 和多轮 RL 训练 9B 机器人规划器，保持执行器冻结；LIBERO-PRO 达 71.0%，但训练测试共享任务，且无真机结果。

## De-Diffusing WAMs: Action-Sufficient Direct Prediction for Robot Control

- [arXiv 2610.28122](https://arxiv.org/abs/2610.28122) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28122)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28122)

冻结单步动作专家，以动作误差监督直接未来预测；LIBERO 为 97.1%、RoboTwin 为 85.4%，28 倍为模型侧加速，未证明普遍超越 teacher。

## PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations

- [arXiv 2610.28019](https://arxiv.org/abs/2610.28019) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28019)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28019)

用较新的提交前观测验证冻结 flow 策略的候选动作块；真机成功率从 60% 升至 82%，同时增加延迟，且不提供校准的安全保证。

## EventSync: Event-Driven Memory Updates for History-Dependent Manipulation

- [arXiv 2610.27917](https://arxiv.org/abs/2610.27917) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27917)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27917)

事件监控器在视觉和运动证据确认完成后才写入任务历史；RoboMME 达 64.5%，但需要事件监督，且对照沿用已发表基线。

## LaLa-World: Scaling Latent World Models with Natural Language Actions

- [arXiv 2610.27851](https://arxiv.org/abs/2610.27851) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27851)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27851)

自然语言动作表征统一潜在世界模型预训练及动作／未来联合预测；LIBERO 达 97.7%，DROID 动作预测评分不等于真机成功率。

## VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs

- [arXiv 2610.27698](https://arxiv.org/abs/2610.27698) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27698)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27698)

成对评测 VLA 视觉调优的目标收益与跨维度保留；10 个设置中 8 个非目标均值下降，研究干预是定向微调而非在线持续学习。

## DEFLECT: Temporal Counterfactual Preference Learning for Delay-Robust Asynchronous VLAs

- [arXiv 2605.19294](https://arxiv.org/abs/2605.19294) · v3 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2605.19294)
- 收录历史: [2026-10-21 (v3, substantive-revision)](../daily/2026-10-21.zh-CN.md#arxiv-2605.19294)

修订为抗延迟 VLA 偏好学习补充跨骨干及继续训练对照；GR00T 在四步延迟下达 73.10%，协议变化使新旧版 headline 数字不可直接比较。

## SteerAct: Unlocking Action Models through Few-Shot Temporal Steering

- [arXiv 2610.25632](https://arxiv.org/abs/2610.25632) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.25632)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.25632)

用每任务 24 条带成败标签的 rollout 建立时序特征参考库，在线选择干预时机、方向和强度，冻结 π0.5／Fast-WAM。连接经验参考与测试时适应，不更新主模型权重。

## SARAM: Sparse Adapter Allocation with Reuse and Merging for Lifelong Robot Learning

- [arXiv 2610.24804](https://arxiv.org/abs/2610.24804) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24804)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24804)

复用旧 LoRA、稀疏分配新适配器并惩罚重复；每回合先识别任务，再合并到骨干。为跨任务经验的参数化积累提供与显式技能库不同的对照。

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

## LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence

- [arXiv 2610.23334](https://arxiv.org/abs/2610.23334) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.23334)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.23334)

以语义子任务进度连接 VLM 规划、状态判断与 WAM 动作生成，加入分层视觉记忆和子任务价值学习。

## NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models

- [arXiv 2610.23271](https://arxiv.org/abs/2610.23271) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.23271)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.23271)

先分别训练技能，再用任务条件超网络生成 action expert 参数，减少直接合并权重的冲突。

## AnchorQ: Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors

- [arXiv 2610.22852](https://arxiv.org/abs/2610.22852) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22852)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22852)

将粗参考动作通过 flow reversal 转成状态相关的噪声锚点，再以局部粒子和在线 critic 探索，保持基础 VLA 冻结。

## Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations

- [arXiv 2610.22576](https://arxiv.org/abs/2610.22576) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22576)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22576)

以少量校准任务的成功 rollout 训练具身分类器，在 π0 每一步去噪时用分类器梯度引导动作，保持 VLA 参数冻结。

## When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

- [arXiv 2610.22556](https://arxiv.org/abs/2610.22556) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22556)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22556)

把相邻动作块对同一未来时刻的预测分歧作为记忆写入信号，用有限视觉槽位保存关键帧，并过滤重复画面。

