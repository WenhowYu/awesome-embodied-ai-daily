# 操作与真实机器人迁移

[English](manipulation-transfer.md) | [简体中文](manipulation-transfer.zh-CN.md) | [所有主题](README.zh-CN.md)

113 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

## Learning Force-Reactive Humanoid Loco-Manipulation

- [arXiv 2610.35862](https://arxiv.org/abs/2610.35862) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35862)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35862)

采集无需机器人参与的力感知示范，将扩散位姿/力策略与混合柔顺全身控制结合。 任务及试次数较少，并依赖力传感硬件；消融不能证明任意接触技能迁移。

## OSWAM: An Effective World Action Model with One-Step Action Generation

- [arXiv 2610.35850](https://arxiv.org/abs/2610.35850) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35850)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35850)

利用动作/场景想象token提供结构化扩散初值，并蒸馏带未来条件的特权信息，实现一步动作去噪。 一步是速度/质量取舍，并非全面优越。真机样本小，完成时间只对成功轨迹从视频估计。H20与编译RTX5090延迟设置不同；NAVSIM不是真实道路部署。

## Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent

- [arXiv 2610.35817](https://arxiv.org/abs/2610.35817) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35817)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35817)

ZAP以成功轨迹SFT和仿真GRPO训练27B VLM使用统一感知/位姿控制工具接口，测试语义预训练与动作学习的组合泛化，不用真机训练轨迹。 每模型仅30次真机试验；harness提供SAM3.1分割、校准深度3D读数及控制反馈，非纯RGB端到端控制。仿真使用真机校准；成本按每小时7.10美元单B300计算；Franka迁移并非真机。

## Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies

- [arXiv 2610.35626](https://arxiv.org/abs/2610.35626) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35626)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35626)

从腕部相机采集重建机器人对齐3D高斯场景，渲染可行平滑接近轨迹，微调VLA并以指令条件距离验证器判断停止。 生成轨迹数量为对照十倍；主动采集不足10分钟，但总耗时约200分钟，与150条遥操相当。只学习接触前接近，精度由固定后续抓取例程验证。三目标各25次及中等主板位移不能证明任意布局或接触任务泛化。

## Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data

- [arXiv 2610.35075](https://arxiv.org/abs/2610.35075) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35075)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35075)

通过手机场景重建、Agent仿真构建及运动/环境协同适配，生成无需真实机器人示范的人形操作数据。 主打的20个百分点优势比较了不等量示范；扩展覆盖还改变训练分布，不能解释为等数据提升。

## How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder: A Hierarchical, Matched Sim-Real Benchmark for Physical Interaction

- [arXiv 2610.34527](https://arxiv.org/abs/2610.34527) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34527)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34527)

PhysLadder定义16项仿真/真机匹配接触任务，递进考察接触几何、持续力调节、以及接触重配置与力调节协同。 单模型、每任务极少样本；一致性不等于普适仿真到真机排序有效。仿真接触/材料参数并非实测物理值，模型调用数受不同动作接口影响，不可直接比较。

## Scaling Dexterous Manipulation via Action Representation Pretraining

- [arXiv 2610.34453](https://arxiv.org/abs/2610.34453) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34453)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34453)

ARPG以人类操作数据让动作表示对齐视觉特征，冻结编码器，再在该空间训练130M生成骨干与解码器。 DexJoCo基线沿用原论文；真机仅3项任务、每项30次。同机器人示范不等于等优化预算：π0.5为25k步混合LoRA，ARPG另训编码器/解码器且下游最多120k步。小时数累计片段长度，可能计入重叠；开放语义与夹爪迁移未验证。

## ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation

- [arXiv 2610.34370](https://arxiv.org/abs/2610.34370) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34370)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34370)

ThinkLocoManip交替推理/行动，编排感知、导航、操作及全身运动工具；关键帧思考保留执行上下文以恢复失败。 仅单平台5类任务，每类10–20次；编排依赖工程化导航、抓取及控制工具，未隔离跨回合技能获取，也未证明全身控制器可迁移。

## RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions

- [arXiv 2610.34356](https://arxiv.org/abs/2610.34356) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34356)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34356)

RynnLAM以残差视觉预测、相机补偿3D流及相机运动解耦提取连续潜动作；流匹配VLA先用30.1K小时视频学习，再适配原生动作。 全规模比较不匹配预训练数据/算力，规模实验未隔离优化曝光量。几何为伪标签，并非度量或因果动作识别证据。真机适配用3,850条示范。RoboTwin主表/摘要88.6%，结论88.3%，存在不一致；未测推理速度。

## HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

- [arXiv 2610.34186](https://arxiv.org/abs/2610.34186) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34186)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34186)

以2,087小时人类、仿真及机器人数据训练OFT、GR00T和π式人形策略，输出SONIC全身运动token及手部信号；用仿真补伪本体状态、渲染替换人臂以适配。 仅一项真机任务，固定预训练全身控制器并全参数下游微调。视觉适配仅增加2次成功；伪本体状态因文本截断反而损害OFT。报告前两阶段8张GPU约38+12小时，收益未分离额外数据与预训练算力。

## PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy

- [arXiv 2610.34147](https://arxiv.org/abs/2610.34147) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34147)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34147)

以文本物性先验调节柔性线状物操作策略，并向动作专家蒸馏未来视觉特征。 不同本体分别训练策略；未来观察用于训练，不是部署时在线预测世界模型接口。

## HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model

- [arXiv 2610.34126](https://arxiv.org/abs/2610.34126) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34126)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34126)

以历史本体状态及正运动学监督学习神经动力学，再通过模型梯度微调人形跟踪策略；低频参考扰动用于可部署数据采集。 真机重复次数少，使用任务专属跟踪/完成指标，而非广泛操作成功率。真机基线为直接迁移和可建模情况下的扰动PPO，不包含全部仿真对照。作者将适用范围限为时不变扰动设置；需先采集和训练再部署适配策略。

## RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models

- [arXiv 2610.34108](https://arxiv.org/abs/2610.34108) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34108)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34108)

RoboDuo先让整任务VLA尝试并检查完成情况，再通过生成代码调用另行训练的原子VLA补齐剩余步骤，整任务策略冻结。 整体并非免训练：原子策略及完成检查编码代理使用示范派生数据集。五套件训练时收益缩小；真机仅一个任务族、小样本。公开参考行协议不同，非匹配重跑。

## X-World: Transferring Video Priors to Variable-View Robot Control

- [arXiv 2610.34105](https://arxiv.org/abs/2610.34105) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34105)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34105)

通过残差跨视角注意力、层对齐Q-Former及共享动作专家，将视频骨干迁移到可变视角控制；保留各数据集原生接口。 对比基线预训练数据/算力不匹配；相机、背景、噪声扰动弱于OpenVLA-OFT，LIBERO-Plus汇总权重未说明。只有一种真机平台，未证明未见形态迁移。

## RoboLongR: Causally Consistent Rewards Teach Robots to Progressively Master Long-Horizon Manipulation

- [arXiv 2610.33863](https://arxiv.org/abs/2610.33863) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33863)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33863)

以循环记忆、阶段打乱负样本和终止纠正学习历史敏感奖励，再通过RL微调行为克隆策略。 真机每任务仅10次。去记忆、阶段打乱或纠正后分别为28.9%、24.3%、28.4%。在线纠正仅用于RoboLongR与Progress+Mono，不用于ReWiND等基线；主对比评估完整流程。

## AdaDexTrack: Dynamic Modulation for Adaptive and Generalizable Dexterous Manipulation Tracking

- [arXiv 2610.33852](https://arxiv.org/abs/2610.33852) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33852)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33852)

在蒸馏灵巧跟踪器外增加强化学习的参考、物体隐变量与目标调制。 Completion是各轨迹满足跟踪误差阈值的帧比例再取平均，并非整任务二元成功率。依赖显式物体姿态、网格与可靠姿态估计，对称物体仍有挑战。

## One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation

- [arXiv 2610.33794](https://arxiv.org/abs/2610.33794) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33794)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33794)

将每栋建筑的一次手机扫描转换为高斯场景及指令导航样本，再以已知场景的Pareto效用进行策略后训练，无需人类示范或学习型critic。 无示范不等于无人介入：扫描和评估指令核对仍需人工。基线场景数据预算不同；未扫描区域仍属同建筑，而非未见建筑。真机成功半径1.5米，布局显著变化需重扫。属于场景后训练，非逐步在线TTT。

## Open-World Law-to-Action: Vision-Language Priors and Touch for Parts with Hidden Physics

- [arXiv 2610.33705](https://arxiv.org/abs/2610.33705) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33705)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33705)

结合视觉语言物理规律先验、触觉贝叶斯辨识，以及观察歧义时请求新视角。 没有硬件机器人验证；一个具身协议在两次留出测试之间修改，不应视为干净的验证性对照。

## EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models

- [arXiv 2610.33685](https://arxiv.org/abs/2610.33685) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33685)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33685)

将人类/机器人动作拆为共享位置码与形态专属运动学，再以共享token共训VLM并微调机器人动作。 额外使用8张A800进行50k步tokenizer训练与30k步共训；基线省去这些阶段，并非等算力。真机用2,450条示范、每条件仅10次试验。消融把73.2%一行称作基线，与主表66.8%不一致。

## HA-DiPO: Diffusion Policy Optimization for Heterogeneous Cooperative Transport

- [arXiv 2610.33584](https://arxiv.org/abs/2610.33584) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33584)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33584)

以集中训练、分散执行训练分层多智能体扩散策略，实现协同载荷运输。 93.5%来自仿真而非真机成功率；最佳检查点选择与特定运输控制器限制结论范围。

## RBGA: Residual-Budget Guide Arbitration for Offline-to-Online Safe Reinforcement Learning in Dexterous Manipulation

- [arXiv 2610.33494](https://arxiv.org/abs/2610.33494) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33494)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33494)

依据剩余回合安全预算与代价到达估计，在离线引导和在线探索之间仲裁。 实验将二值代价改为连续代价；理论界依赖估计假设，硬件部分没有定量试验表。

## MDPO: Multi-constraint Dexterous Policy Optimization with Reinforcement Learning

- [arXiv 2610.33480](https://arxiv.org/abs/2610.33480) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33480)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33480)

将累计约束和逐状态约束分别投影，用于灵巧操作强化学习。 真机证据主要为定性展示，不等于定量验证真实安全保证；约束估计假设仍重要。

## MOTIO: Agentic Skill Engineering for Reality-Grounded Humanoid Loco-Manipulation

- [arXiv 2610.33446](https://arxiv.org/abs/2610.33446) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33446)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33446)

MOTIO将人类动作视频、尺度化3D资产及现有控制接口转为分阶段人形程序，通过物理反馈及人工批准修订，并以生成技能监督BC/DAgger蒸馏。 仍依赖人工批准及任务专属工程；真机演示和仿真变化测试并非随机化真机成功率基准。开发时长包含工具/资源等待，蒸馏证据来自仿真。

## Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models

- [arXiv 2610.26179](https://arxiv.org/abs/2610.26179) · v3 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.26179)
- 收录历史: [2026-10-27 (v3, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2610.26179)

v2→v3新增附录J按源状态分组、训练/选点/测试分离的评测：骨干仅在训练组从零训练，head在独立组选择，直接检验原发布资产基准的重叠顾虑；原主结果不是新贡献。 更严格分离下Push-T没有提升。新任务窗不同于原基准（Cube均匀起点、Push-T间隔80而非74步），不可跨协议比较绝对成功率；标准误只覆盖骨干种子，不覆盖任务/源组抽样。仅仿真。

## One-shot Human Video-Guided Adaptation for Vision-Language-Action Models

- [arXiv 2610.19746](https://arxiv.org/abs/2610.19746) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.19746)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2610.19746)

v1→v2新增两种改造后视频条件基线，补齐旧版未填完整的消融结果，并以十次试验真机结果替换原五次表格；主要RoboTwin CapPro表现在v1已存在。 新增基线是适配π0.5后的版本，不是原系统原样比较。真机每任务仅10次，困难分类成功率仅20%。one-shot指目标任务测试时的人类视频指导，不代表总共只用一条示范训练；仍需源任务训练。

## GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation

- [arXiv 2609.05588](https://arxiv.org/abs/2609.05588) · v3 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2609.05588)
- 收录历史: [2026-10-27 (v3, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2609.05588)

v2→v3实质替换附录A.1/表3的RoboTwin评测：六类扰动列改为每任务50条clean示范下的Clean-to-Clean和Clean-to-Random，并扩充榜单基线。这是协议/结果替换，不能作为同条件版本提升。 基线尽可能引用RoboTwin官方榜单及Qwen-RM报告，并非统一受控重跑；主要真机预训练/扩展结果沿用v2。

## What Can One Sentence Fix? A Failure Taxonomy and a Minimal Language Correction for Frozen VLA Policies

- [arXiv 2608.29967](https://arxiv.org/abs/2608.29967) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2608.29967)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2608.29967)

v1→v2将CorrectVLA改题并重构论述，以每条件三组10次真机运行替换旧小样本表，新增长程失败对照，明确区分仅失败重试恢复率与全部回合净成功率。仿真65/139及33/328恢复数沿用旧版。 人工标注失败类型并为失败运行编写带时窗纠正，耗时40–80秒，可追加纠正轮次。仅失败重试的仿真成功率不能证明无条件策略提升。该通道只修幅度/时机，不修语义目标或计划；LIBERO-90是指令OOD而非场景OOD。

## Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL

- [arXiv 2608.12063](https://arxiv.org/abs/2608.12063) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2608.12063)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2608.12063)

v1→v2新增Q5/表2：将稀疏奖励离线到在线学习与FastTD3、IQL、Diffusion Policy直接复用SMPC代价或示范数据比较。原真机结果及稀疏奖励方法并非新增。 基线复用SMPC代价/数据，失败不能证明RL算法普遍较差；作者归因于代价不适配和缺少纠偏样本，并指出并行SMPC的DAgger成本过高。新增对比仅仿真。

## LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies

- [arXiv 2606.15768](https://arxiv.org/abs/2606.15768) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2606.15768)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2606.15768)

v1→v2新增八子任务Clean Table真机任务、光照变化测试、容量/预测接口对照及训练成本/置信区间。98.6% LIBERO与187毫秒主结果在v1已存在。 Clean Table绝对成功率仍低，光照变化下尤甚；真机任务较少。机理对照均去掉第二阶段预训练，不能直接等同完整预训练策略；光照测试复用已做颜色增强的任务检查点。

## PRISM: PRior-guided Imagination Sampling in world Models

- [arXiv 2606.07974](https://arxiv.org/abs/2606.07974) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2606.07974)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2606.07974)

v1→v2新增冻结特征动作预测探针及随机编码器对照、共用融合接口的diffusion先验、十种子主仿真评估及匹配真机无先验对照。高斯先验引导融合和两类真机平台在v1已存在。 diffusion和MLP头采用不同目标约定，不能单独归因于架构。探针分数来自验证集选模而非独立测试集。动作头训练/推理数字排除世界模型预训练及共享编码器/规划器成本。真机净增仅4次和6次，仍需更多试验。

## Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects

- [arXiv 2606.01950](https://arxiv.org/abs/2606.01950) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2606.01950)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2606.01950)

v1→v2新增基于FoundationPose的高斯渲染对比物体跟踪，评估以估计而非真值位姿输入的动力学预测，并新增两段定性真实场景录像。仿真非抓取MPC在v1已存在。 跟踪基准仅5个无连续旋转对称YCB物体、验证集选定的固定视角，并在可见性失败处截断轨迹。定量跟踪/预测仍在仿真，真机仅定性而非真实MPC成功率。重建是独立前置步骤，后段真机预测漏掉接触，训练位姿历史也更干净。

## BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation

- [arXiv 2605.08571](https://arxiv.org/abs/2605.08571) · v3 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2605.08571)
- 收录历史: [2026-10-27 (v3, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2605.08571)

v2→v3新增调优统一权重、源均值差异对照、特征对齐诊断及明确约束理论结论的权重审计；主要BEACON成功率在旧版已有。 理论界用于启发目标函数，不能当作已审计学习权重的有效保证。新增对齐结果是诊断证据；MMD基线也表明差异更小不必然带来更高任务成功率。

## AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation

- [arXiv 2604.11674](https://arxiv.org/abs/2604.11674) · v3 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2604.11674)
- 收录历史: [2026-10-27 (v3, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2604.11674)

v2→v3新增真机域随机化扫描、五形态采集定量评测及等示范预算ACT抓取来源对照。多阶段成功率分解及原四任务sim-to-real评估在v2已存在。 位置扫描示范量从300增至1,200再到2,700，范围与数据量混杂；真机仅单任务、各10次。跨形态结果衡量仿真轨迹采集，不是学习策略迁移。已有主表数字未变，但采集次数文字从30改为100，不能解读为同协议新收益。

## RoboGene: Diversity-Driven Agentic Task Generation Framework for VLA Pre-training

- [arXiv 2602.16444](https://arxiv.org/abs/2602.16444) · v3 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2602.16444)
- 收录历史: [2026-10-27 (v3, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2602.16444)

v2→v3新增更广泛真机OOD评测及人工成本/记忆分析（附录H.2/H.4），不只是重述原任务生成架构和1.8万轨迹。 不是零样本任务迁移，仍需目标任务微调。人工成本按固定单次耗时估算，包含遥操作与人工验证；纠错率下降本身不能单独证明记忆因果贡献。

## FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation

- [arXiv 2602.13444](https://arxiv.org/abs/2602.13444) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2602.13444)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2602.13444)

v1→v2将定性机器人展示补为有次数的基线比较，新增匹配单阶段、抓取前缀预训练、重建及场景粒度分析。40倍推理加速和1.7倍仿真成功率主张在v1已存在。 离线场景重建、重定向及DexTrack修正后开环执行；衡量标称条件可执行性而非抗扰。预训练对照单训练种子，未显示明确物理成功增益。匹配单阶段快40ms且动作识别/仿真成功相当，两阶段优势主要是接触质量，非全面更优。

## UniManip: Open-World Robotic Manipulation via Agentic Operational Graphs

- [arXiv 2602.13086](https://arxiv.org/abs/2602.13086) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2602.13086)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2602.13086)

v1→v2新增LIBERO-Pro评测及明确的UR7e/Robotiq与灵巧手跨本体测试，并形式化有预算上限的AOG恢复。原22.5/25.0个百分点优势不是本次新增收益。 跨本体保留任务级AOG，但仍需替换URDF/关节限位、工具坐标标定、控制器映射及硬件接口适配，不能说完全零配置；灵巧手执行成功率仅53%。

## CRAFT-E: An Interpretable and Editable Neuro-Symbolic Framework for Affordance-Grounded Active Object Retrieval

- [arXiv 2512.04231](https://arxiv.org/abs/2512.04231) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2512.04231)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2512.04231)

CRAFT-E v1→v2新增COCO-Tasks迁移、显式图编辑干预及扩展错误分解；动词—属性—物体图及真机检索流水线并非本次新增。 COCO迁移测图像落地，非实体检索。图编辑在查看同集失败后选择，证明可控性而非留出集自主修复。新文说明完整流水线相对GPT-4o差异不显著；监督COCO方法仅作背景，非匹配对照。

## DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection

- [arXiv 2610.32969](https://arxiv.org/abs/2610.32969) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32969)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32969)

便携接口使用部署时的灵巧手，以参数化抓取和学习式旋转技能采集腕部运动及原生关节指令；模仿策略不接收技能标签。 评估样本少；螺丝刀旋转单独用速度指标，不计入三任务成功率均值。数据量与场景多样性同时变化；采集技能并非自主增长的技能库。

## ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback

- [arXiv 2610.32966](https://arxiv.org/abs/2610.32966) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32966)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32966)

从单目视频直接生成G1参考运动，以跟踪器反馈构造偏好对后训练扩散生成器；自回归版本支持视频遥操作。 百分比为仿真参考运动跟踪率，不是真机任务完成率。未建模精细手部姿态；真机证据以定性示范为主，在线初始化约10秒。

## RynnUnify: Towards Unified Embodied Brain

- [arXiv 2610.32965](https://arxiv.org/abs/2610.32965) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32965)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32965)

基于Cosmos3的16B模型耦合8B推理器和8B视频生成器；跨片段场景帧支撑交错视觉规划，另行RL训练的推理器选择是否调用生成证据，WAM适配联合学习视频与动作。 机器人适配使用约1,600小时原子任务及177小时组合任务数据。完整split的基线数值引用既有报告，精选20任务由作者评估；视觉历史是回合内上下文，不是已验证终身记忆，3项真机任务未隔离记忆贡献。

## If at First You Don’t Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

- [arXiv 2610.32941](https://arxiv.org/abs/2610.32941) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32941)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32941)

用冻结策略rollout训练小型失败头，触发后回放实际已完成机械臂运动的逆序，再交回原策略重试。 仅仿真；汇总结果包含选参种子，留出种子π0.5收益为0.70个百分点。回退不恢复物体或保证安全，失败头仍需标注rollout训练。

## Regularised RL improves sim-to-real transfer

- [arXiv 2610.32855](https://arxiv.org/abs/2610.32855) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32855)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32855)

用缓慢更新参考策略把soft mellowmax扩展到连续控制actor–critic，检验正则化是否改善超越名义训练回报的sim2real鲁棒性。 回报不是成功率；仍需要域随机化，温度参数随任务变化。PPO/FastTD3因未通过预设仿真安全筛查而没有ANYmal扰动部署，空白不能算实测真机失败；MuJoCo调参预算不完全相等。

## Semantic Representation for Agentic Self-Play in Automated Laboratories

- [arXiv 2610.32755](https://arxiv.org/abs/2610.32755) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32755)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32755)

VERID提供持久语义实验室孪生，支持状态查询、执行前仿真门控、同步轨迹及故障续跑；代理跨运行保留物理操作边界和分析经验。 这是小规模案例而非隔离记忆因果效应的消融：挑战实例与实验策略同时变化。使用预设结构化Harness、内部Gemini检查点及受监督运行中的人工批准门控；未证明生物学突破或通用机器人策略迁移。

## Retiming Robot Demonstrations with a Learned Speed Prior

- [arXiv 2610.32676](https://arxiv.org/abs/2610.32676) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32676)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32676)

学习可迁移的示范速度分布，用已观测更快节奏重定时轨迹，并把预测节奏的VLA与约束感知实时轨迹执行层结合。 需要离线策略训练和专门执行控制器，不是直接加速推理的开关。速度先验不能超出已有示范节奏；超时会影响成功率，因此须看同速对照。SAIL对比采用不同机器人与策略。

## DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation

- [arXiv 2610.32330](https://arxiv.org/abs/2610.32330) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32330)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32330)

从点云序列自监督学习时序一致的软槽位、槽位级潜在动作及邻近-运动关系，再为扩散策略提供3D动力学表征。 仿真基线沿用AFRO论文结果，各种子选最好评估检查点，非独立最终测试。真机误差条是布局间标准差，不是训练种子方差；只一个本体且杂物/新物体仅一个任务。

## MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation

- [arXiv 2610.32312](https://arxiv.org/abs/2610.32312) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32312)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32312)

将技能条件LoRA专家与RGB-D轨迹可供性热图结合，以热图偏置动作注意力。 MAST额外使用深度而基线仅RGB，不能将收益全归因于架构。指令逐原语下发，并非自主分解长任务；几何失效和执行漂移仍存在。

## RoboCode: Learning Reusable Action Primitives for Robot Manipulation

- [arXiv 2610.32225](https://arxiv.org/abs/2610.32225) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32225)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32225)

先从多任务动作块学习可软组合的共享原语码本，再冻结解码接口，训练任务专属状态到码本编码器。 仅仿真，使用物体位姿/目标等状态而非图像语言输入；评估任务各自训练编码器，可复用码本不等于在线技能增长或未见任务迁移。已核评测部分未明确多种子不确定性及闭环试验次数。

## Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion

- [arXiv 2610.32143](https://arxiv.org/abs/2610.32143) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32143)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32143)

把紧贴手部的手环穿戴建模为几何插入，结合逐指软插入门控和分阶段课程，通过紧凑几何观测接口迁移到双臂机器人。 手环预抓持、假手静止，真机约减半速度。没有力感知观测/目标，手指偏转不是安全指标；大幅组合姿态扰动使仿真成功降至26/50。

## Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies

- [arXiv 2610.32102](https://arxiv.org/abs/2610.32102) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32102)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32102)

联合研究执行动作长度与flow求解步数，检验浅采样何时有效或有害。 长开环在移动目标上失效；加速指摊销推理成本，不保证任务墙钟加速。论文对仿真任务总数及π0.5动作块配置存在不一致描述。

## DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

- [arXiv 2610.32093](https://arxiv.org/abs/2610.32093) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32093)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32093)

用特权状态、潜变量条件RL、逆向课程和成功门控多样性生成过滤后的示范，再训练视觉π0.5，部署的不是RL生成器。 依赖准确仿真、特权状态、状态重置和成功信号。真机仅4个简单桌面任务、较小迁移差距及1个训练种子；过大多样性会损害任务能力。

## EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions

- [arXiv 2610.31845](https://arxiv.org/abs/2610.31845) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31845)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31845)

以来源可靠性调节噪声与损失权重，将联合视觉-动作流与可见干净未来的EMA教师蒸馏结合，利用带噪人类动作标签。 外部RoboCasa基线取自发表结果、预训练和预算不同。π0.5真机对照重置输入输出层以适配58DoF，不能将差距纯归因方法；仍需动作标注，来源加权不能纠正系统性重定向偏差。

## FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation

- [arXiv 2610.31841](https://arxiv.org/abs/2610.31841) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31841)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31841)

编码代理结合RGB-D与腕部力/力矩日志，生成并修订接触探测和力反馈Python程序；经验保存在可执行控制逻辑中，无需任务专属模型训练。 只有5项真机任务、单模型及少量试验；每次开发最多20个实体rollout和4小时，人类负责执行批准、场景操作及最终验收。对照同时移除力反馈和相关例程，并非单独隔离记忆贡献；每次推理耗时4–10分钟。

## WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations

- [arXiv 2610.31834](https://arxiv.org/abs/2610.31834) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31834)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31834)

把真实演示的数字孪生构建写成可执行世界程序，由编码代理诊断回放失败并定向修复场景、资产与物理交互。 这是已录轨迹在重建仿真中的回放，不是真机新策略成功率或sim2real收益。空间指标并非全面胜过Astra；组件消融限于一个任务，尚不能归因长期记忆收益。

## SEVI: Safe Evidential Real-World Reinforcement Learning

- [arXiv 2610.31829](https://arxiv.org/abs/2610.31829) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31829)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31829)

证据式安全critic同时估计违规风险与认知不确定性，在在线RL中筛查动作并调用离线训练的恢复策略。 仅1项真机、2项仿真任务，无零违规形式保证。真机使用50条成功先验示范、200条恢复示范及验证集阈值；最终成功率与累计训练事件口径不同。

## PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer

- [arXiv 2610.31812](https://arxiv.org/abs/2610.31812) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31812)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31812)

联合学习潜在偏好空间和奖励先验，通过置信度加权最优传输生成目标任务伪偏好，在不新增目标任务人工标签下在线强化学习。 零样本指无需目标人工反馈，并非无目标交互或训练。真机样本少，要求源目标共享偏好维度；PEARL做了在线化与维度补齐，PrefFew处于有限源数据设置并使用100个目标标签。

## KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations

- [arXiv 2610.31801](https://arxiv.org/abs/2610.31801) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31801)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31801)

把统一14维双臂运动学压缩为每秒2个、由转折边界监督的稀疏运动token，再用LoRA语言模型输出时间片段和描述，并测试新机器人及人手迁移。 编码器采用整回合标准化和对称时间上下文，因此是离线模型。tokenizer比较同时存在输入表示及reader训练样本差异，不仅改变目标函数；分段及语义迁移不等于闭环策略收益。

## FLORA: An Open Model Suite for Scaling Robotics Data Engines

- [arXiv 2610.31779](https://arxiv.org/abs/2610.31779) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31779)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31779)

开放标注模型套件提供时序分段、动作意图描述及结果/稠密/规则奖励；分段与描述使用RL后训练，发布的奖励模型仅用SFT。 并非所有指标最优，各系统帧预算及算力不同。约125倍成本优势依赖假定GPU价格和建模吞吐，未含部署开销、生产GPU小时口径未核实，参考标注版本亦未完全匹配；这里未直接证明下游策略学习提升。

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

## WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time

- [arXiv 2607.06988](https://arxiv.org/abs/2607.06988) · v3 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2607.06988)
- 收录历史: [2026-10-26 (v3, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2607.06988)

通过人类视频写入世界动作模型的快权重记忆，配对人类—机器人元训练学习视频到动作的迁移接口。 对照是同一WAM内的接口变体，而非原系统完整复现；新增接口实验仅一个任务。FastWAM证据是3.2秒、8帧预测的定性展示，不是闭环控制迁移；部分对照依赖预训练技能潜变量，元训练阶段直接插入并不具备该先验。

## GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

- [arXiv 2607.05369](https://arxiv.org/abs/2607.05369) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2607.05369)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2607.05369)

GaP组合带类型的机器人技能图，在部署前通过仿真排练优化图结构、参数和吞吐。 新增吞吐证据来自仿真，并非新增真机生产率结果。论文明确承认CaP-X对照因已知环境几何信息不同而不公平；MORSL仅对齐部分感知/抓取组件，并未对齐所有运动原语、推理预算和系统选项。任务仍以准静态为主。

## Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration

- [arXiv 2605.31196](https://arxiv.org/abs/2605.31196) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2605.31196)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2605.31196)

TouchSafeBench在仿真人机共处中评估当前碰撞识别和提前预警，区分机器人—场景与人类接触风险。 真实录像无物理接触，且为人头戴相机；标签是1米阈值的二元接近状态，并非实际碰撞安全。误报统计只有12个难负例。提示测试仅一个模型/条件，单专家按固定顺序看不同视角；未验证闭环安全干预。

## METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

- [arXiv 2610.31656](https://arxiv.org/abs/2610.31656) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31656)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31656)

METTA 将回合内可梯度更新的快速神经记忆与跨回合的紧凑摘要分开。它在 Meta-World ML10/45 未见任务族上报告超过 50% 成功率，并改善长上下文稀疏奖励探索。

## Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models

- [arXiv 2610.31569](https://arxiv.org/abs/2610.31569) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31569)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31569)

将停止与失败两种信号加入动作块，采用结构化注意力和更快的信号去噪，让较干净的状态预测反过来指导动作。训练使用成功、失败及恢复轨迹，无需逐帧进度标注。 真实评分并非成功率；动作监督及训练预算匹配，但Echo额外使用失败状态数据。跨方法比较集中于插花，部分采用适配协议；两任务无失败测试样本。高层自动终止/重规划收益尚未验证。 三秒结果窗口F1并非瞬时故障检测；仿真状态准确率针对指定窗口的进行中/成功帧，并非通用三分类失败检测。

## FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models

- [arXiv 2610.31423](https://arxiv.org/abs/2610.31423) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31423)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31423)

在π0.5上利用当前多模态输入、状态及动作历史预测未来交互意图，动态调节全局/腕部视角；用轨迹自动构造弱监督标签。 真机提升为13.3个百分点；跨本体和多种摄像头配置尚待验证。模块需训练，不是无需训练的推理期补丁。

## PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning

- [arXiv 2610.31299](https://arxiv.org/abs/2610.31299) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31299)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31299)

PiHand 将仿真中的动作捕捉跟踪专家蒸馏为目标条件手–物交互潜变量先验，再在潜空间中学习有界残差探索。同一交互先验可支持新物体、新轨迹、接物和双手交接。

## Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

- [arXiv 2610.31166](https://arxiv.org/abs/2610.31166) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31166)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31166)

WholeBodyMem 用 SAM3 对象事件选择历史关键帧，以对象时空 token 和独立记忆注意力向全身动作专家提供已经消失的线索。 这是回合内感知历史，不是跨回合技能积累；真机每任务仅10次且未给均匀记忆真机对照。SAM3漏检与跟踪成本仍是限制。

## UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry

- [arXiv 2610.30991](https://arxiv.org/abs/2610.30991) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30991)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30991)

将未来视觉、3D 场景流和动作放入三专家联合注意力模型，以 10 个目标联合训练；部署不需场景流输入。 58.9% 是最佳评估种子；87.7% 是最佳已评检查点。实机逐任务训练、初始条件在示范范围内；流伪标签有噪声。

## In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

- [arXiv 2610.30988](https://arxiv.org/abs/2610.30988) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30988)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30988)

部分点云经生成式状态补全，再用上下文条件 Transformer 预测布料动力学，为流匹配动作候选排序；测试时不更新权重。 实机表无对照策略；成功由点云距离阈值定义。PCN 的 CD/EMD 更好；本文优势是对应点 MSE。快速动态操作及闭环重规划仍待验证。

## TEAR: Task-Evidence Authority Routing for Robotic Manipulation

- [arXiv 2610.30819](https://arxiv.org/abs/2610.30819) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30819)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30819)

在机器人本地结合网络质量、CLIP任务语义与历史状态，用因果时序卷积预测稀疏交接事件，切换人类遥操作与本地VLA控制。 真实评估有人监督，两回合共含4次人工切换；不能称完全自动仲裁。仅两种相近搬运任务与合成网络扰动。离线交接F1为0.308、召回0.286，低于规则基线召回0.429。未找到代码链接。 两种设置分别训练路由器。

## Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation

- [arXiv 2610.30810](https://arxiv.org/abs/2610.30810) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30810)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30810)

ALMA 用动作条件未来响应预测训练历史上下文，并让LLM依据失败生成新的机械臂运动结构，扩展RL训练任务。 部署参数冻结，适应来自上下文，非test-time梯度训练；真机只对比PID，不可将79.6%改善当作相对最强仿真基线。接触力控制仍属后续方向。

## DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models

- [arXiv 2610.30781](https://arxiv.org/abs/2610.30781) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30781)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30781)

DeXplicit 先在公制三维空间预测物体运动与形变，再渲染动作条件视频。在相同几何与动作输入下，长时域运动点误差较适配后的 PointWorld 降低 27–40%，显式几何也提高了物体保真度。

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

## The Bitter Lesson Comes to Robotics

- [arXiv 2610.25287](https://arxiv.org/abs/2610.25287) · v2 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.25287)
- 收录历史: [2026-10-23 (v2, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2610.25287)

《The Bitter Lesson Comes to Robotics》比较前沿语言模型在 40 次动作预算下直接控制真机 YAM 机械臂的表现。本次修订把 7 个模型、12 种设置扩展到 9 个模型、15 种设置，并更新历史性能趋势拟合。

## HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation

- [arXiv 2604.07993](https://arxiv.org/abs/2604.07993) · v3 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2604.07993)
- 收录历史: [2026-10-23 (v3, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2604.07993)

HEX 结合标准化身体部位状态、混合专家本体状态预测器、紧凑视觉历史和流匹配动作，完成类人机器人全身操作。本次修订新增两个家庭长时域任务、ψ0 对照、分布外预训练测试及数据规模与超参数实验。

## Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models

- [arXiv 2602.12628](https://arxiv.org/abs/2602.12628) · v5 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2602.12628)
- 收录历史: [2026-10-23 (v5, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2602.12628)

RL-Co 先用仿真与真机示范共同监督预热，再在仿真 RL 中保留真机监督约束。本次修订新增更强的 rollout 蒸馏对照，并明确真机统计评估的范围。

## CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation

- [arXiv 2610.30117](https://arxiv.org/abs/2610.30117) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30117)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30117)

匹配消融支持接触力历史对力敏感操作的作用，但增益手设且部分接触力更大，不能概括为更安全。

## Asymmetric On-Policy Distillation Learns In-Context Exploration

- [arXiv 2610.30105](https://arxiv.org/abs/2610.30105) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30105)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30105)

特权专家的 on-policy 蒸馏支持共享隐变量下的跨回合探索，但真机样本有限，上下文并非永久技能库。

## From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks

- [arXiv 2610.30051](https://arxiv.org/abs/2610.30051) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30051)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30051)

LIBERO-10 工具控制基准评估无操作预训练的前沿模型；44/100 与 43/100 的差距不足以形成可靠排名。

## CausGround: Causal Interaction Grounding for Adaptive Embodied Planning

- [arXiv 2610.29702](https://arxiv.org/abs/2610.29702) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29702)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29702)

离线因果知识库改善规划，但 RoboCasa 采用回放式高层评估，部署时知识库不增长。

## Relational Geometry Forcing for World Action Models

- [arXiv 2610.29282](https://arxiv.org/abs/2610.29282) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29282)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29282)

训练时关系几何监督改善 WAM 泛化，但 LIBERO 增益较小，时间项单独使用反而有害。

## DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation

- [arXiv 2610.29246](https://arxiv.org/abs/2610.29246) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29246)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29246)

深度约束预测表征可迁移到匹配的实机场景，但固定标定、本体专用训练及未计入的搜索时间限制了迁移与速度结论。

## Learning to Absorb Corrections: Critic-Weighted Residual Flow for Vision-Based Insertion

- [arXiv 2610.29117](https://arxiv.org/abs/2610.29117) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29117)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29117)

critic 加权残差学习被 ACT 吸收：关闭残差后的成功率从 16% 提高到 76%，但跨任务遗忘和 VLA 迁移尚未验证。

## COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation

- [arXiv 2610.28948](https://arxiv.org/abs/2610.28948) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28948)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28948)

局部抓取专家支持情境化全身操作，真机成绩较强；但算力未匹配，部署时不进行持续学习。

## Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration

- [arXiv 2610.28880](https://arxiv.org/abs/2610.28880) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28880)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28880)

三维语义扩增将单个人类视频转为机器人数据，控变量实验增益明显，但与遥操作的比较不匹配，仍需人工设置。

## T-WLA: Bridging Slow Vision and Fast Touch

- [arXiv 2610.28814](https://arxiv.org/abs/2610.28814) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28814)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28814)

快速触觉编辑器修正待执行动作，但无触觉版本已接近完整模型表现，限制了可归因于触觉的增益。

## ASPIRE: Agentic /Skills Discovery for Robotics

- [arXiv 2607.00272](https://arxiv.org/abs/2607.00272) · v2 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2607.00272)
- 收录历史: [2026-10-22 (v2, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2607.00272)

修订新增真机跨回合文本技能积累；单次旋转耗时下降，但魔方总解题时间不单调下降，仍需人类支持。

## μ0: A Scalable 3D Interaction-Trace World Model

- [arXiv 2606.13769](https://arxiv.org/abs/2606.13769) · v3 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2606.13769)
- 收录历史: [2026-10-22 (v3, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2606.13769)

v3 揭示长程完成率低、动作块延迟高于 π0.5；原子任务主成绩未变，不能据此宣称组合能力进步。

## Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

- [arXiv 2610.28613](https://arxiv.org/abs/2610.28613) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28613)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28613)

视触觉世界模型支持评测与策略后训练；四项 ARX 任务真机均值从 SFT 的 59.1% 升至 70.8%，但其中一项任务低于 SFT。

## Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future

- [arXiv 2610.28431](https://arxiv.org/abs/2610.28431) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28431)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28431)

任务与因果状态 token 引导世界—动作预测，处理视觉相似阶段；StageBench 从 40.9% 升至 69.4%，真机提升仍依赖任务示范且测试样本较小。

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

## AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies

- [arXiv 2610.27736](https://arxiv.org/abs/2610.27736) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27736)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27736)

优势加权潜在引导在不进行后训练真机 rollout 的条件下改进冻结单步 decoder；真机成功 65/100，只有相对 MeanFlow 的总体提升通过多重比较校正。

## PrismWAM: Decoupling State Representations in World Action Models

- [arXiv 2610.26564](https://arxiv.org/abs/2610.26564) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.26564)
- 收录历史: [2026-10-21 (v1, supplemental-previous-batch)](../daily/2026-10-21.zh-CN.md#arxiv-2610.26564)

补核 2026-10-20 公告：解耦 RGB 目标、深度未来与动作；基础版 RoboTwin C2R 为 70.57%，真机使用 RGB-D，15B 结果另有预训练。

## HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents

- [arXiv 2610.23479](https://arxiv.org/abs/2610.23479) · v2 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.23479)
- 收录历史: [2026-10-21 (v2, substantive-revision)](../daily/2026-10-21.zh-CN.md#arxiv-2610.23479)

实质修订新增 42 项 RoboDojo 任务的官方隐藏 seed 评测；46.9% 成功率与 v1 协议不同，公开工具不包含完整评测系统。

## GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation

- [arXiv 2610.26846](https://arxiv.org/abs/2610.26846) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.26846)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.26846)

触觉 RGB 图像接入视觉接口，结合少样本演示与交互记忆做接触操作。

## PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models

- [arXiv 2610.26813](https://arxiv.org/abs/2610.26813) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.26813)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.26813)

正常外观的 EMA teacher 与扰动观测 student 对齐浅/深层动作表征，推理无额外模型，面向 WAM 后训练与真实环境外观鲁棒性。

## TrajWAM: An Efficient Trajectory-Guided World Action Model for Dynamic Robotic Manipulation

- [arXiv 2610.25763](https://arxiv.org/abs/2610.25763) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.25763)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.25763)

由历史物体 mask 预测轨迹，用 Trajectory ControlNet 引导未来视觉，再通过视频蒸馏、适配器重对齐、动作 rollout 蒸馏保留一步未来条件接口，面向动态操作。

## SARAM: Sparse Adapter Allocation with Reuse and Merging for Lifelong Robot Learning

- [arXiv 2610.24804](https://arxiv.org/abs/2610.24804) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24804)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24804)

复用旧 LoRA、稀疏分配新适配器并惩罚重复；每回合先识别任务，再合并到骨干。为跨任务经验的参数化积累提供与显式技能库不同的对照。

## LIBERO-Dynamic: Benchmarking Robotic Manipulation in Dynamic Environments

- [arXiv 2610.24579](https://arxiv.org/abs/2610.24579) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24579)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24579)

40 个 LIBERO 任务加入 3 类轨迹×3 档速度，推理期间按实测延迟推进物理；6 个策略每配置 1,800 个动态条件，9,000 条动态示范，面向预测、实时性与重规划的公平比较。

## ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation

- [arXiv 2610.23156](https://arxiv.org/abs/2610.23156) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.23156)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.23156)

用旋转等变潜变量编码物体形状，预测并解析施加 SE(3) 变化，使多步世界模型保持刚体几何。

## AnchorQ: Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors

- [arXiv 2610.22852](https://arxiv.org/abs/2610.22852) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22852)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22852)

将粗参考动作通过 flow reversal 转成状态相关的噪声锚点，再以局部粒子和在线 critic 探索，保持基础 VLA 冻结。

## Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations

- [arXiv 2610.22576](https://arxiv.org/abs/2610.22576) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22576)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22576)

以少量校准任务的成功 rollout 训练具身分类器，在 π0 每一步去噪时用分类器梯度引导动作，保持 VLA 参数冻结。

## Scaling Online Exploration for Robot Agents

- [arXiv 2610.22496](https://arxiv.org/abs/2610.22496) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22496)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22496)

冻结编码代理通过机器人接口探索，将感知、规划与控制沉淀为可执行程序；以持久笔记和已验证技能支持跨回合、跨任务复用。

