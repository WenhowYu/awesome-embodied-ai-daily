# 视觉—语言—动作模型

[English](vla.md) | [简体中文](vla.zh-CN.md) | [所有主题](README.zh-CN.md)

207 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

## From Pixels to Actions - Towards Native Vision-Language-Action Policies

- [arXiv 2611.06918](https://arxiv.org/abs/2611.06918) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.06918)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.06918)

NEO-VLA采用轻量图像分块和视觉语言联合计算，让流匹配动作专家读取多个深度的特征，而非固定视觉编码器的最终输出。

## Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement

- [arXiv 2611.06905](https://arxiv.org/abs/2611.06905) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.06905)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.06905)

系统比较直接策略适配、评论器引导的动作筛选和策略提取，以研究通用机器人策略的多任务在线改进。

## Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models

- [arXiv 2611.06817](https://arxiv.org/abs/2611.06817) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.06817)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.06817)

Open-HumanScale以整理后的5万小时人类第一视角语料研究数据规模效应，并将HumanWAM从纯人类预训练扩展到人机联合训练和视觉目标条件控制。

## $A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation

- [arXiv 2611.06447](https://arxiv.org/abs/2611.06447) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.06447)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.06447)

从交互变化产生区域监督，约束VLA注意力及语言区域对齐。

## SurgTransfer: Multi-Step Latent Action Modeling for Action Transfer in Surgical World Model

- [arXiv 2611.05443](https://arxiv.org/abs/2611.05443) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.05443)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.05443)

SurgTransfer从手术视频学习多步、上下文不变的隐动作，以在场景间迁移操作运动，无需运动学动作标签。

## Test-Time Improvement of VLA Policies via Selected Diffusion Noise for Spurious-Robust Action Smoothing

- [arXiv 2606.14084](https://arxiv.org/abs/2606.14084) · v2 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2606.14084)
- 收录历史: [2026-11-05 (v2, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2606.14084)

SDN 根据物体视觉定位和加加速度指标，从冻结 VLA 的动作样本中选择输出。本次修订新增针对机制的证据：任务无关遮罩对照、基于归因的排序分析、BYOVLA 比较及负样本集构建测试。

## Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning

- [arXiv 2606.12109](https://arxiv.org/abs/2606.12109) · v3 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2606.12109)
- 收录历史: [2026-11-05 (v3, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2606.12109)

InDex 将同步的末端执行器/抓取意图预测与扩散式灵巧手解码器结合。更名后的修订版新增留出物体实例评估，并实质性修改训练预算及意图时序干预的试验说明。

## Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection

- [arXiv 2606.09258](https://arxiv.org/abs/2606.09258) · v2 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2606.09258)
- 收录历史: [2026-11-05 (v2, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2606.09258)

B2FF 通过选择预先想象的视觉里程碑帮助冻结的前瞻型 VLA 恢复执行。本次修订直接比较想象未来与历史观测作为恢复目标，并加入恢复数据微调 VLA 的对照及重要评估更正。

## DreamX: Video Diffusion Model is a Universal Latent Action Learner

- [arXiv 2611.05377](https://arxiv.org/abs/2611.05377) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.05377)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.05377)

从预训练视频扩散模型中为每个潜在帧提取四个动作标记，构建人类与机器人视频共享的运动接口。

## Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs

- [arXiv 2611.05249](https://arxiv.org/abs/2611.05249) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.05249)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.05249)

独立消融动作token监督与动作专家梯度耦合/隔离。

## Asynchronous Robot Policies

- [arXiv 2611.05155](https://arxiv.org/abs/2611.05155) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.05155)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.05155)

慢速VLM更新语义记忆，快速视觉动作专家控制；训练显式处理记忆过期和延迟。

## LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models

- [arXiv 2611.05093](https://arxiv.org/abs/2611.05093) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.05093)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.05093)

控制检查点、层及引擎，比较通用与VLA专用量化。

## CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation

- [arXiv 2611.05080](https://arxiv.org/abs/2611.05080) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.05080)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.05080)

评估非回合式VLA强化学习微调和针对性重置分配。

## Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training

- [arXiv 2611.04873](https://arxiv.org/abs/2611.04873) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04873)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04873)

替换行为克隆监督前审计想象轨迹奖励。

## Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots

- [arXiv 2611.04522](https://arxiv.org/abs/2611.04522) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04522)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04522)

通过显式与隐式动作意图对齐人类和机器人域。

## Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs

- [arXiv 2611.04391](https://arxiv.org/abs/2611.04391) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04391)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04391)

H2RB 结合几何约束观测、共享动作潜变量和独立人机解码器，实现非配对迁移。

## RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training

- [arXiv 2611.04368](https://arxiv.org/abs/2611.04368) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04368)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04368)

先用推理标注训练LoRA，再冻结适配器进行动作微调。

## Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs

- [arXiv 2611.04166](https://arxiv.org/abs/2611.04166) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04166)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04166)

诊断语言解释保持不变而动作改变的分离现象。

## Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy

- [arXiv 2611.04006](https://arxiv.org/abs/2611.04006) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04006)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04006)

AdaIE 根据在线估计的动作头敏感度重加权 VLM 通道，不增加可训练参数，推理时冻结统计量。

## AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data

- [arXiv 2611.03815](https://arxiv.org/abs/2611.03815) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.03815)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.03815)

用16,151小时手持夹爪示范学习双臂操作，训练数据采集不需要机器人。

## Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation

- [arXiv 2608.19490](https://arxiv.org/abs/2608.19490) · v2 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2608.19490)
- 收录历史: [2026-11-04 (v2, revised)](../daily/2026-11-04.zh-CN.md#arxiv-2608.19490)

将VLA在目标机器人上的自身交互轨迹与专家示范联合微调，以保留预训练技能。

## CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding

- [arXiv 2607.08974](https://arxiv.org/abs/2607.08974) · v2 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2607.08974)
- 收录历史: [2026-11-04 (v2, revised)](../daily/2026-11-04.zh-CN.md#arxiv-2607.08974)

CLAP在数字动作令牌前加入与动作对应的语言描述，同时保留VLM骨干结构。

## PACE: Phase-Aware Chunk Execution for Robot Policies with Action Chunking

- [arXiv 2606.00537](https://arxiv.org/abs/2606.00537) · v4 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2606.00537)
- 收录历史: [2026-11-04 (v4, revised)](../daily/2026-11-04.zh-CN.md#arxiv-2606.00537)

PACE依据动作序列中的低速谷值选择执行时长，无需重新训练策略。

## DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation

- [arXiv 2605.30350](https://arxiv.org/abs/2605.30350) · v2 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2605.30350)
- 收录历史: [2026-11-04 (v2, revised)](../daily/2026-11-04.zh-CN.md#arxiv-2605.30350)

DynaFLIP对齐图像变化、语言和三维流，预训练与动作相关的视觉表征。

## Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation

- [arXiv 2611.03648](https://arxiv.org/abs/2611.03648) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03648)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03648)

Pixel联合设计轮式人形硬件、示范接口、全身控制与分层策略学习。

## Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations

- [arXiv 2611.03647](https://arxiv.org/abs/2611.03647) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03647)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03647)

Pixel-UMI结合几何感知人类示范重定向、视角掩码与在线DAgger纠正。

## FineCraft: Enhancing VLA Models for Fine-Grained Manipulation

- [arXiv 2611.03163](https://arxiv.org/abs/2611.03163) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03163)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03163)

FineCraft在独立适配DINOv2-DiT与π0.5策略间路由任务，结合局部视觉及专家延续示范。

## VLALagBench: Understanding When and Why VLA Inference Latency Matters

- [arXiv 2611.03103](https://arxiv.org/abs/2611.03103) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03103)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03103)

VLALagBench改变物体速度、任务需求及同步/异步执行，刻画VLA延迟敏感性。

## Beyond Policy Patches: Distilling RL Specialists into Vision-Language-Action Policies

- [arXiv 2611.02777](https://arxiv.org/abs/2611.02777) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02777)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02777)

REPAIR用价值加权专家动作分布与在线策略状态覆盖，将RL专家蒸馏进单一流匹配VLA。

## HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation

- [arXiv 2611.02660](https://arxiv.org/abs/2611.02660) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02660)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02660)

HeLM在共享π0动作策略之上维护事件触发语言记忆，贯穿子任务与回合。

## W2A: Distilling World Priors into Action Models for Real-Time Robotic Control

- [arXiv 2611.02600](https://arxiv.org/abs/2611.02600) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02600)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02600)

W2A把压缩视频去噪特征蒸馏进动作策略，推理时移除视频模型。

## RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild

- [arXiv 2611.02497](https://arxiv.org/abs/2611.02497) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02497)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02497)

RoboColosseum结合分布式盲测真机比较与固定数据微调，覆盖四种本体。

## Gnomon4D: Learning Where and When to Focus for Geometric Motion-Grounded World-Action Modeling

- [arXiv 2611.02474](https://arxiv.org/abs/2611.02474) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02474)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02474)

联合预测视频、动作与 GeoDelta 几何运动；以交互区域注意力和状态转折聚合，将物体与本体运动关系用于控制。

## When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem

- [arXiv 2611.02101](https://arxiv.org/abs/2611.02101) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02101)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02101)

跨层安全研究测试π0.5闭环控制中推理延迟与相机分布偏移的交互。

## ODE Policy: Robot Learning via Action Dynamics, Not Actions

- [arXiv 2611.01729](https://arxiv.org/abs/2611.01729) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01729)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01729)

ODE Policy学习动作导数并从上一动作积分，面向模仿学习和RL连续控制。

## $TF^2$-Steering: Action Refinement with Tactile Forecasts and Feedback via Velocity-Field Steering

- [arXiv 2611.01483](https://arxiv.org/abs/2611.01483) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01483)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01483)

TF²-Steering以预测及观测触觉通过残差专家混合调整flow-matching动作专家。

## Serving Agentic Robot Fleets: Workload Characterization, KV-Cache Thrashing, and Admission Control

- [arXiv 2611.01404](https://arxiv.org/abs/2611.01404) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01404)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01404)

服务系统研究刻画机器人Agent群的brain KV缓存驻留与VLA动作deadline耦合。

## Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency

- [arXiv 2611.01390](https://arxiv.org/abs/2611.01390) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01390)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01390)

Path-preserving Time Scaling分离参考路径重规划与延迟感知执行速度，用于冻结动作块策略。

## Vision-Language Models Are Joint Denoisers in Robotic Action Generation

- [arXiv 2611.01215](https://arxiv.org/abs/2611.01215) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01215)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01215)

JADE每个去噪步把带噪动作latent反馈给VLM，与动作专家共同细化动作。

## Ripple: Deadline-Aware CPU-GPU Sharing for Embodied Inference

- [arXiv 2611.01067](https://arxiv.org/abs/2611.01067) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01067)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01067)

Ripple在统一内存边缘设备上以模型推算流量与完成反馈协调可暂停GPU推理和CPU截止期。

## Leap-VLA: High-Rate Robot Control from a Low-Rate VLM Backbone

- [arXiv 2611.01011](https://arxiv.org/abs/2611.01011) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01011)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01011)

Leap-VLA将低频语义VLM与高频视觉动作专家解耦，并显式以语义缓存年龄作为条件与训练变量。

## Verifying Test-State Identity in Paired Evaluation of Vision-Language-Action Models

- [arXiv 2611.00896](https://arxiv.org/abs/2611.00896) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00896)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00896)

溯源检查器验证向量化重置下配对VLA评估是否实际分配相同初始状态。

## PREM: Prediction-Regulated Memory for Robot Manipulation

- [arXiv 2611.00634](https://arxiv.org/abs/2611.00634) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00634)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00634)

PREM用动作条件预测训练循环视觉记忆，并以预测差异调节空间更新。

## Editing the Goal: Per-Token SAE Steering and Its Depth Limits in π0.5

- [arXiv 2611.00602](https://arxiv.org/abs/2611.00602) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00602)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00602)

保持指令文本不变，交换单个目标词的SAE特征即可重定向π0.5-LIBERO，并用激活替换定位目标信息可编辑的层深。

## Reflex: Fast Robot Policy Serving by Reusing and Correcting Past Actions

- [arXiv 2611.00524](https://arxiv.org/abs/2611.00524) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00524)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00524)

Reflex缓存完整动作块，以动作相似度和残差修正，并按进度刷新原策略。

## Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime

- [arXiv 2611.00522](https://arxiv.org/abs/2611.00522) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00522)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00522)

TinyLoRA通过GRPO或CMA-ES，仅用8–384个可训练参数调整冻结OpenVLA-OFT行为。

## CalVLA: Shaping Native Confidence in Vision-Language-Action Policies with Outcome Supervision

- [arXiv 2611.00394](https://arxiv.org/abs/2611.00394) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00394)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00394)

CalVLA用成功/失败rollout结果训练OpenVLA动作token置信度，无单独失败检测器。

## TurboWAM: Learning What Matters for Fast World Action Models

- [arXiv 2610.33941](https://arxiv.org/abs/2610.33941) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2610.33941)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33941) · [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2610.33941)

TurboWAM限制世界模型层聚合范围并调制训练梯度，以降低动作预测延迟。

## Spotter: Let the Embodied Model Lead, and the VLM Reflect for It

- [arXiv 2609.36808](https://arxiv.org/abs/2609.36808) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2609.36808)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2609.36808)

Spotter让具身策略主导执行，由VLM选择性反思和修复。

## 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation

- [arXiv 2609.11308](https://arxiv.org/abs/2609.11308) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2609.11308)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2609.11308)

Agent侧记忆为动作模型提供结构化指导以执行长时序操作。

## OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation

- [arXiv 2606.22174](https://arxiv.org/abs/2606.22174) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2606.22174)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2606.22174)

OpenHLM研究全身人形VLA的接口设计与异构训练数据。

## GazeVLA: Learning Human Intention for Robotic Manipulation

- [arXiv 2604.22615](https://arxiv.org/abs/2604.22615) · v3 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2604.22615)
- 收录历史: [2026-11-03 (v3, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2604.22615)

GazeVLA通过凝视导出的中间表示和意图-动作推理迁移人类意图。

## CoEnv: Code-Driven Exploration in Real-to-Sim Digital Twins for Multi-Arm Manipulation

- [arXiv 2604.05484](https://arxiv.org/abs/2604.05484) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2604.05484)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2604.05484)

CoEx在部署场景数字孪生中探索完整机器人程序，再将经验证程序转移至真机。

## OmniGuide: Universal Spatial Guidance Fields for Enhancing Generalist Robot Policies

- [arXiv 2603.10052](https://arxiv.org/abs/2603.10052) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2603.10052)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2603.10052)

OmniGuide通过来自几何、语义与示范的空间能量场引导通用机器人策略。

## RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

- [arXiv 2610.42141](https://arxiv.org/abs/2610.42141) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.42141)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.42141)

编码智能体优化冻结策略的控制框架与持久记忆。

## REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control

- [arXiv 2610.42053](https://arxiv.org/abs/2610.42053) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.42053)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.42053)

非阻塞运行时结合历史路由、边界评价、有界恢复。

## Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space

- [arXiv 2610.42021](https://arxiv.org/abs/2610.42021) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.42021)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.42021)

人机联合训练对齐意图、细交互与动作潜变量。

## When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks

- [arXiv 2610.41857](https://arxiv.org/abs/2610.41857) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41857)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41857)

检测接触伪影，支持回放与单参数反事实重跑。

## VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression

- [arXiv 2610.41609](https://arxiv.org/abs/2610.41609) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41609)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41609)

同初态配对指令区分启动与选择。

## MolmoSpaces-CommonSense: Evaluating Commonsense in Robotic Manipulation Policies

- [arXiv 2610.41377](https://arxiv.org/abs/2610.41377) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41377)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41377)

评估杂乱、遮挡、支撑关系、可供性和隐藏物体等操作常识。

## STAR: Steering Action Representations during Inference

- [arXiv 2610.41009](https://arxiv.org/abs/2610.41009) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41009)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41009)

无需训练、单次前向地混合后层残差更新，由近期本体状态控制强度。

## Learning from Fleet Experience: Collective Experience Learning Across 96 Robots

- [arXiv 2610.25736](https://arxiv.org/abs/2610.25736) · v3 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.25736)
- 收录历史: [2026-11-02 (v3, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2610.25736)

v3修正机器人群数据通路：在本地积累完整、经操作员标注的回合，再一次性传输；不再沿用v2所述的轨迹字段流式上传与云端复用推理观测。

## Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models

- [arXiv 2610.03498](https://arxiv.org/abs/2610.03498) · v2 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.03498)
- 收录历史: [2026-11-02 (v2, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2610.03498)

v2修正附录探针诊断数据并补充干预强度调参说明，并非提出新防御方法。

## VEGA: Learning Navigation VLAs from In-the-Wild Egocentric Video with Geometric Trajectory Supervision

- [arXiv 2606.18426](https://arxiv.org/abs/2606.18426) · v3 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2606.18426)
- 收录历史: [2026-11-02 (v3, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2606.18426)

实质修订为视频训练导航新增动态仿真、第四个真机场景以及几何偏差/监督消融，并澄清基线共用执行接口，而非完整原生导航系统对比。

## Specification-Aware Distribution Shaping for Robotics Foundation Models

- [arXiv 2603.17969](https://arxiv.org/abs/2603.17969) · v2 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2603.17969)
- 收录历史: [2026-11-02 (v2, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2603.17969)

实质修订将约束动作分布评估从仅SPOC扩展至三种基础模型和两种STL策略合成方法，展示仿真约束完全满足背后的任务成功率代价。

## π-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs

- [arXiv 2603.02083](https://arxiv.org/abs/2603.02083) · v3 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2603.02083)
- 收录历史: [2026-11-02 (v3, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2603.02083)

实质修订：新增基于评论家时序信用信号的变体和CALVIN诊断，并以透明的共同测试变体协议，将广泛的分布外优势主张收窄为视觉扰动优势。

## BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing

- [arXiv 2610.40532](https://arxiv.org/abs/2610.40532) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40532)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40532)

BURGER 用语言条件机器人绘画，在低成本扩大示范时区分语言定位、空间组合与多模态轨迹选择。

## Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design

- [arXiv 2610.40430](https://arxiv.org/abs/2610.40430) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40430)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40430)

DEED 通过指令与视觉示范扩展、均衡采样以及任务特定动作段执行设计来适配 VLA。

## HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

- [arXiv 2610.40373](https://arxiv.org/abs/2610.40373) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40373)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40373)

HiFOR 通过分层依赖掩码联合预测短期状态、语义里程碑和最终目标；按时间视野、视角和空间组织潜在未来，让动作 token 在去噪时检索所需信息。

## JEDI: Joint-Embedding Demonstration Compression for In-Context Imitation Learning

- [arXiv 2610.40356](https://arxiv.org/abs/2610.40356) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40356)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40356)

JEDI 将示范压缩为潜在槽，用冻结 video-JEPA 空间中的查询阶段未来预测进行训练；任务/过程反事实监督保留执行细节，并从示范库选择上下文。

## TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation

- [arXiv 2610.40349](https://arxiv.org/abs/2610.40349) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40349)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40349)

TouchBridge 协同设计人类与机器人视觉/触觉接口，无需物体网格、位姿或仿真即可重定向指尖接触区域，再以转换的人类示范微调 VLA。

## Gaussian Distillation of Flow Policies

- [arXiv 2610.40271](https://arxiv.org/abs/2610.40271) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40271)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40271)

Gaussian Action Readout 冻结流策略骨干，将输出层改为高斯读出，获得单次前向采样和闭式似然。

## RoboAtom: Large-scale Atomic-Action Supervision for Robot Learning

- [arXiv 2610.40207](https://arxiv.org/abs/2610.40207) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40207)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40207)

RoboAtom 跨机器人数据集统一时间对齐的原子动作标签，结合人工标注、重复技能序列传播与质控，并提供技能识别基准及分层策略训练。

## Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles

- [arXiv 2610.40075](https://arxiv.org/abs/2610.40075) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40075)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40075)

基于二值可行性 oracle 修正不安全流更新，并估计局部边界梯度，无需解析约束即可让训练和推理使用同一防护机制。

## RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence

- [arXiv 2610.40026](https://arxiv.org/abs/2610.40026) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40026)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40026)

RoboSeed 将能力、训练成本、部署成本、本地研究价值证据与复现证据分成明确维度，用固定锚点和预算偏好构建画像。

## LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks

- [arXiv 2610.40016](https://arxiv.org/abs/2610.40016) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40016)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40016)

LOGIV 在现有策略之上加入条件支撑与资源顺序图，持续检查先前动作效果是否仍成立，追踪失效依赖，并联合验证局部修复与保留的未完成计划。

## How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function

- [arXiv 2610.40002](https://arxiv.org/abs/2610.40002) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40002)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40002)

CoC-CFG 将推理条件与去推理条件之间的引导强度作为逐去噪步控制变量；固定专家和噪声后，通过完整 rollout 测得动作价值，训练小型保守引导 critic。

## From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models

- [arXiv 2610.39543](https://arxiv.org/abs/2610.39543) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39543)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39543)

CoRAct 将运动描述和未来路点变成动作对齐奖励；共享 Transformer 建模推理、动作及动作条件未来，并用组相对优化调整初始动作噪声，使执行符合预期后果。

## PRIME W0: Physical Priors from World Models for Embodied Manipulation

- [arXiv 2610.39528](https://arxiv.org/abs/2610.39528) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39528)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39528)

PRIME W0 结合逐层 VLM KV 条件、异步子目标图像预测、冻结 DINOv2 历史编码及自适应 MoE 流动作解码器；动作噪声协方差来自示范相关结构。

## Smooth Action Chunking Via Movement-Primitive Representations for Imitation Learning

- [arXiv 2610.39451](https://arxiv.org/abs/2610.39451) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39451)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39451)

以平滑运动基元系数替代原始动作段，并用推理时经过点修正将新段接上上一条执行动作，无需重新训练。

## Decoding Geometry, Not Tokens: Efficient VLMs for Robot Affordance and Trajectory Prediction

- [arXiv 2610.39416](https://arxiv.org/abs/2610.39416) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39416)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39416)

轻量连续几何头读取冻结VLM中间特征，直接预测可供性框与路径点，避免自回归坐标token。

## UMI-Live for In-The-Wild Bimanual Robotics Data Collection

- [arXiv 2610.39385](https://arxiv.org/abs/2610.39385) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39385)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39385)

UMI-Live把双臂野外示范采集、机载感知、异步SLAM和VLA训练部署串成完整流程。

## Utility-WAM: Correcting Future-Induced Action Changes

- [arXiv 2610.39367](https://arxiv.org/abs/2610.39367) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39367)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39367)

Utility-WAM审计想象未来造成的动作变化，以残差适配器修复有害增量，并由离线效用门控跳过低收益未来生成。

## Cross-Controller Transfer via In-Context Behavior Adaptation

- [arXiv 2610.39280](https://arxiv.org/abs/2610.39280) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39280)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39280)

跨控制器迁移把命令—实际运动历史作为π0.5上下文，使其改变策略而非仅重映射电机命令。

## Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models

- [arXiv 2610.38661](https://arxiv.org/abs/2610.38661) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38661)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38661)

QbD-VLA用短闭环任务试验分配混合精度，优化机器人实际成功而非仅校准误差。

## SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control

- [arXiv 2610.38508](https://arxiv.org/abs/2610.38508) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38508)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38508)

SaiVLA-JEPA区分当前预测编码器特征的收益与未来潜变量训练的收益，并分别审计上下文适配与参数更新。

## Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation

- [arXiv 2610.38199](https://arxiv.org/abs/2610.38199) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38199)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38199)

水下模仿学习揭示泳池与海洋实地部署之间的巨大差距，为通用VLA能力判断提供现实校准。

## Self-Labeled Preference Transfer for Steerable Robot Manipulation

- [arXiv 2610.38000](https://arxiv.org/abs/2610.38000) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38000)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38000)

SPT联合学习偏好识别与条件动作，冻结识别器，为新任务示范补伪标签再适配策略，保留普通微调易遗失的执行偏好。

## What Actually Matters? A Paired Evaluation of Inference Settings for $π_{0.5}$ on BEHAVIOR-1K

- [arXiv 2610.37917](https://arxiv.org/abs/2610.37917) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.37917)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.37917)

配对研究把推理设置当作需要验证的干预，而非可直接迁移的默认值：执行块长度影响显著，去噪次数和重叠修补在该设置下无可检测收益。

## Behavior Spatial Benchmark: Evaluating Spatial Understanding for Robotics

- [arXiv 2610.34051](https://arxiv.org/abs/2610.34051) · v2 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.34051)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34051) · [2026-10-30 (v2, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2610.34051)

BEHAVIOR-Spatial 分开评价空间问答、目标定位和动作执行。v2 修订定位及导航问答数值，主要操作/动作成绩未变。

## ActionUNet: Improving Robustness of VLA Models with Efficient Multi-scale Fine-tuning

- [arXiv 2609.34982](https://arxiv.org/abs/2609.34982) · v2 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2609.34982)
- 收录历史: [2026-10-30 (v2, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2609.34982)

ActionUNet 通过多尺度时序特征与连续动作解码改进 VLA 微调。本次修订缩减而非扩充了补充证据。

## Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment

- [arXiv 2607.13429](https://arxiv.org/abs/2607.13429) · v3 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2607.13429)
- 收录历史: [2026-10-30 (v3, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2607.13429)

Anchor-Align 在 VLA 微调中约束 VLM 表征漂移，并对齐运动与语言。本次修订新增语义标签对照，扩展不同架构与机器人形态的实机证据。

## VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon

- [arXiv 2607.01804](https://arxiv.org/abs/2607.01804) · v2 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2607.01804)
- 收录历史: [2026-10-30 (v2, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2607.01804)

VLA-Corrector 用学习到的潜在动力学监测、事件触发动作块截断及恢复方向梯度引导，在不更新 VLA 主干的情况下纠偏。本次修订新增部署开销核算和异步、近似匹配调用预算的 RTC 对比。

## ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning

- [arXiv 2610.37666](https://arxiv.org/abs/2610.37666) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37666)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37666)

世界想象奖励使人机视频共享运动token推理。

## Ego-CEVR: Learning Cross-Embodiment Visual Representations from Human Egocentric Videos

- [arXiv 2610.37509](https://arxiv.org/abs/2610.37509) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37509)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37509)

分离全局未来预测与局部动作监督改善迁移，但真机对照中等量机器人视频仍强于人类视频。

## Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling

- [arXiv 2610.37393](https://arxiv.org/abs/2610.37393) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37393)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37393)

迭代质量重标注改善成功轨迹质量与真机吞吐量，但须保留在线数据成本与条件指标限制。

## PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations

- [arXiv 2610.37381](https://arxiv.org/abs/2610.37381) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37381)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37381)

世界模型监督物理特征支持VLA取得较高仿真成绩，但尚无真机任务验证。

## VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning

- [arXiv 2610.37378](https://arxiv.org/abs/2610.37378) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37378)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37378)

仿真训练RL执行层改善冻结VLA避障，但依赖结构化感知且真机仍有碰撞。

## Vision-Language-Action or World-Action? Just Action Models

- [arXiv 2610.37219](https://arxiv.org/abs/2610.37219) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37219)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37219)

仅训练期未来特征监督可替代视觉生成，需区分目标选择贡献。

## Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution

- [arXiv 2610.37215](https://arxiv.org/abs/2610.37215) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37215)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37215)

示范图检索增强冻结VLA执行，但另训修正模块且初始化校正贡献重要。

## From 12 to 200 Demonstrations: How ACT, Diffusion Policy, SmolVLA and $π_{0.5}$ Scale on a Low-Cost Arm

- [arXiv 2610.37170](https://arxiv.org/abs/2610.37170) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37170)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37170)

低成本臂扩展实验揭示适配配方与评测波动的重要影响，而非通用策略排名。

## TAPESTRY: A Single Backbone for Video Generation and Robot Control

- [arXiv 2610.36823](https://arxiv.org/abs/2610.36823) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36823)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36823)

共享视频patch动作token实现单步纯动作部署。

## RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions

- [arXiv 2610.36791](https://arxiv.org/abs/2610.36791) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36791)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36791)

统一latent-action视频模型为策略训练提供合成数据。

## Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition

- [arXiv 2610.36765](https://arxiv.org/abs/2610.36765) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36765)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36765)

任务专用 pi0.5 策略结合常规示范、策略状态上的专家纠正，以及评测驱动的示范细化。

## TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation

- [arXiv 2610.36694](https://arxiv.org/abs/2610.36694) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36694)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36694)

任务条件流源塑形改善单步操作策略；主实验与π0.5扩展的评测类别覆盖不同。

## RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning

- [arXiv 2610.36685](https://arxiv.org/abs/2610.36685) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36685)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36685)

镜像单臂示范结合协作约束，在不新增目标双臂采集的条件下训练双臂策略。

## SO-101 Bench: Accessible Spatial Manipulation

- [arXiv 2610.36420](https://arxiv.org/abs/2610.36420) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36420)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36420)

低成本臂基准在控制适配预算并核对真机排序的条件下，直接检验代码Agent与VLA的互补作用。

## ASPEN: Adaptive Semantic Reasoning via Command Persistence Prediction for Efficient Navigation VLAs

- [arXiv 2610.36285](https://arxiv.org/abs/2610.36285) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36285)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36285)

命令持续性调度减少9.5%的冻结导航VLA调用，成功率接近。

## OmniBrain-0: A Unified Agentic Model for Embodied Intelligence

- [arXiv 2610.36013](https://arxiv.org/abs/2610.36013) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36013)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36013)

OmniBrain-0 以 on-policy 蒸馏和 rubric 引导自改进将专家 agent 轨迹整合为统一高层模型，仍保留专用低层技能。

## When Do Discrete Actions Make Good Continuous Controllers?

- [arXiv 2610.20429](https://arxiv.org/abs/2610.20429) · v2 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.20429)
- 收录历史: [2026-10-28 (v2, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2610.20429)

v1→v2按完整运行配置重新解释动作tokenizer结果，并区分有引导与无引导离散回归。

## Where Small Mistakes Matter: Quantifying State Criticality for Imitation Learning

- [arXiv 2610.17709](https://arxiv.org/abs/2610.17709) · v2 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.17709)
- 收录历史: [2026-10-28 (v2, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2610.17709)

v1→v2补充性能差距推导、状态关键性基线定义及真机对抗残差学习实现细节。

## FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation

- [arXiv 2606.13102](https://arxiv.org/abs/2606.13102) · v4 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2606.13102)
- 收录历史: [2026-10-28 (v4, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2606.13102)

v3→v4明确Sharpa的22关节到32槽位动作映射，并补充触觉特征探针及数据/算力共同扩展实验。

## What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction

- [arXiv 2606.07687](https://arxiv.org/abs/2606.07687) · v2 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2606.07687)
- 收录历史: [2026-10-28 (v2, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2606.07687)

v2 在全部 26 个留出 LIBERO 任务增加动作打乱和前向动力学对照，检验重建之外的动作相关性。

## RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models

- [arXiv 2605.09410](https://arxiv.org/abs/2605.09410) · v2 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2605.09410)
- 收录历史: [2026-10-28 (v2, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2605.09410)

v1→v2扩充恢复数据因果混淆分析、等预算价值监督对照，以及真机盲测扰动协议。

## AWARE: Action-Entropy-Weighted and Attention-Guided Retrieval of Observation Evidence for Vision-Language-Action Models

- [arXiv 2602.18020](https://arxiv.org/abs/2602.18020) · v3 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2602.18020)
- 收录历史: [2026-10-28 (v3, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2602.18020)

v2→v3以逐动作元素熵/深度加权观测检索替代粗粒度门控，补充诊断替代方案及匹配checkpoint评估。

## Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation

- [arXiv 2512.23864](https://arxiv.org/abs/2512.23864) · v5 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2512.23864)
- 收录历史: [2026-10-28 (v5, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2512.23864)

v4→v5明确由轻量动作条件MLP预测触觉潜变量、预训练触觉世界模型保持冻结，并补充模型/数据扩展与局限分析。

## OSWAM: An Effective World Action Model with One-Step Action Generation

- [arXiv 2610.35850](https://arxiv.org/abs/2610.35850) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35850)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35850)

利用动作/场景想象token提供结构化扩散初值，并蒸馏带未来条件的特权信息，实现一步动作去噪。 一步是速度/质量取舍，并非全面优越。真机样本小，完成时间只对成功轨迹从视频估计。H20与编译RTX5090延迟设置不同；NAVSIM不是真实道路部署。

## Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy

- [arXiv 2610.35832](https://arxiv.org/abs/2610.35832) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35832)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35832)

EBench在RGB/本体观测及每任务一个标注示范下，对比Astra直接路点控制与选择性调用冻结VLA/WAM。 无跨回合记忆；31/510回合使用同测试场景示范。两任务直接3000步、混合5000步，按3000步对齐混合均值52.4%/55.8%。策略调用不能传代理子目标；计算量无上限，每回合仅一次运行。

## Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent

- [arXiv 2610.35817](https://arxiv.org/abs/2610.35817) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35817)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35817)

ZAP以成功轨迹SFT和仿真GRPO训练27B VLM使用统一感知/位姿控制工具接口，测试语义预训练与动作学习的组合泛化，不用真机训练轨迹。 每模型仅30次真机试验；harness提供SAM3.1分割、校准深度3D读数及控制反馈，非纯RGB端到端控制。仿真使用真机校准；成本按每小时7.10美元单B300计算；Franka迁移并非真机。

## SPECOLA: A Tool for Specification Driven Robot Evaluation

- [arXiv 2610.35730](https://arxiv.org/abs/2610.35730) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35730)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35730)

Specola把仿真信号接入信号时序逻辑监视器，除成功率外测满足余量及持续性，并提供API及9种仿真/基准适配器。 结论依赖特权仿真状态及人工规格，不构成真机安全认证。固定周期监视尚不处理异步、不确定真实传感器。更严格的持续要求改变评测语义，并不改写原基准分数。

## Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies

- [arXiv 2610.35626](https://arxiv.org/abs/2610.35626) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35626)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35626)

从腕部相机采集重建机器人对齐3D高斯场景，渲染可行平滑接近轨迹，微调VLA并以指令条件距离验证器判断停止。 生成轨迹数量为对照十倍；主动采集不足10分钟，但总耗时约200分钟，与150条遥操相当。只学习接触前接近，精度由固定后续抓取例程验证。三目标各25次及中等主板位移不能证明任意布局或接触任务泛化。

## RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies

- [arXiv 2610.35604](https://arxiv.org/abs/2610.35604) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35604)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35604)

RoboDoctor通过持久化理由、尝试方法、结果及复用条件，将诊断、策略/代理控制分配、选择性干预及接触方法修订串联。 回溯性最高分选择混合多个来源运行，版本、checkpoint和推理预算不统一。暖启动已含协助及记忆；无匹配重置记忆对照、完整成本核算或真机验证，不能证明记忆的因果收益。

## Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data

- [arXiv 2610.35075](https://arxiv.org/abs/2610.35075) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35075)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35075)

通过手机场景重建、Agent仿真构建及运动/环境协同适配，生成无需真实机器人示范的人形操作数据。 主打的20个百分点优势比较了不等量示范；扩展覆盖还改变训练分布，不能解释为等数据提升。

## VISTA: Active Exploration for Self-Improvement in Embodied Agents

- [arXiv 2610.35051](https://arxiv.org/abs/2610.35051) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35051)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35051)

VISTA利用版本谱系图、主动诊断交互及冻结候选包的新自主评估迭代可执行机器人harness，不更新模型权重。 仅仿真。任务专属选择及历史最优曲线不证明未见任务泛化或每次候选单调改善。LIBERO-Pro/RoboTwin最多100轮规划、10000物理步；开发计算量巨大，不应默认对照预算匹配。

## JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies

- [arXiv 2610.35010](https://arxiv.org/abs/2610.35010) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35010)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35010)

冻结基础策略，学习79,817参数条件能量；能量值排序离散候选，动作梯度修正连续输出。各基准独立训练适配器权重及编码。 仅仿真，无匹配LoRA对照。成功次数是五种子均值取整，并非原始独立试验计数。增益依赖反馈/专家监督与逐基准验证；小适配器参数不含冻结策略推理及rollout成本。

## VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware

- [arXiv 2610.34717](https://arxiv.org/abs/2610.34717) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34717)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34717)

在Jetson AGX Thor及AMD Ryzen AI Max+ PRO 395上剖析18个公开VLA、19种配置和七阶段推理，分离动作生成、后端及CPU预处理成本。 计时并非闭环成功率基准：共享LIBERO观测及单回合24帧，每配置20–100次计时。模型保留各自chunk/执行配置。编译可改变夹爪命令；低位宽动作相似度不等于任务成功率保持。

## RobotAgentBench: Towards Open-world Robot Autonomy

- [arXiv 2610.34649](https://arxiv.org/abs/2610.34649) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34649)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34649)

RobotAgentBench在家庭场景评估任务发现、情境推理、操作、恢复及鲁棒性，并比较编码、学习及混合规划/执行/验证架构。 这些是能力/场景聚合分数，非统一成功率；主表来自仿真，匹配真机子集仅覆盖部分系统、不含最优混合/RSI行。开放场景得分仍低，独立策略和代理接口不同。

## TRIAGE: Efficient Vision-Language-Action Inference Needs Both Reuse and Pruning

- [arXiv 2610.34519](https://arxiv.org/abs/2610.34519) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34519)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34519)

免训练token分配器固定重算预算、复用低漂移且较新的KV缓存，并剪除其余无效token；漂移阈值按骨干校准。 仅两个OpenVLA系列骨干、仿真成功率及回放流硬件计时，无真机闭环评估。阈值经验调参，SimplerEnv只保留完整重算明显高于地板的任务。48%降幅指预填充，不是整体控制延迟。

## Scaling Dexterous Manipulation via Action Representation Pretraining

- [arXiv 2610.34453](https://arxiv.org/abs/2610.34453) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34453)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34453)

ARPG以人类操作数据让动作表示对齐视觉特征，冻结编码器，再在该空间训练130M生成骨干与解码器。 DexJoCo基线沿用原论文；真机仅3项任务、每项30次。同机器人示范不等于等优化预算：π0.5为25k步混合LoRA，ARPG另训编码器/解码器且下游最多120k步。小时数累计片段长度，可能计入重叠；开放语义与夹爪迁移未验证。

## RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions

- [arXiv 2610.34356](https://arxiv.org/abs/2610.34356) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34356)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34356)

RynnLAM以残差视觉预测、相机补偿3D流及相机运动解耦提取连续潜动作；流匹配VLA先用30.1K小时视频学习，再适配原生动作。 全规模比较不匹配预训练数据/算力，规模实验未隔离优化曝光量。几何为伪标签，并非度量或因果动作识别证据。真机适配用3,850条示范。RoboTwin主表/摘要88.6%，结论88.3%，存在不一致；未测推理速度。

## AdaPolicy: Action-Driven Anticipatory Robot Policies via Next-Chunk Prediction

- [arXiv 2610.34280](https://arxiv.org/abs/2610.34280) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34280)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34280)

增加仅训练使用的EMA动作头，依据演化潜状态预测下一动作块；损失经潜状态回传在线策略，不依赖未来图像监督。 真机精细任务各用1,000/400条示范，其中人工接管纠正占20%，双方使用同一混合数据。结果属于监督学习的前瞻特征，不证明自主在线世界模型适配；零推理开销是相对匹配架构而言。

## Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models

- [arXiv 2610.34251](https://arxiv.org/abs/2610.34251) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34251)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34251)

CogMemory加入3.45M参数历史模块：选择性状态空间编码、多槽时间聚合与变分压缩，再通过门控交叉注意力接入两种VLA融合架构。 仅仿真，附录给单种子42，无多种子不确定性。策略与记忆在8张L20X上端到端训练30k步，并非仅推理时加记忆；每1k步验证选最好checkpoint。21.2→12.9秒是两方法共同成功样本的任务执行时间，不是模型推理延迟。

## HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

- [arXiv 2610.34186](https://arxiv.org/abs/2610.34186) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34186)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34186)

以2,087小时人类、仿真及机器人数据训练OFT、GR00T和π式人形策略，输出SONIC全身运动token及手部信号；用仿真补伪本体状态、渲染替换人臂以适配。 仅一项真机任务，固定预训练全身控制器并全参数下游微调。视觉适配仅增加2次成功；伪本体状态因文本截断反而损害OFT。报告前两阶段8张GPU约38+12小时，收益未分离额外数据与预训练算力。

## PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy

- [arXiv 2610.34147](https://arxiv.org/abs/2610.34147) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34147)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34147)

以文本物性先验调节柔性线状物操作策略，并向动作专家蒸馏未来视觉特征。 不同本体分别训练策略；未来观察用于训练，不是部署时在线预测世界模型接口。

## RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models

- [arXiv 2610.34108](https://arxiv.org/abs/2610.34108) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34108)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34108)

RoboDuo先让整任务VLA尝试并检查完成情况，再通过生成代码调用另行训练的原子VLA补齐剩余步骤，整任务策略冻结。 整体并非免训练：原子策略及完成检查编码代理使用示范派生数据集。五套件训练时收益缩小；真机仅一个任务族、小样本。公开参考行协议不同，非匹配重跑。

## X-World: Transferring Video Priors to Variable-View Robot Control

- [arXiv 2610.34105](https://arxiv.org/abs/2610.34105) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34105)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34105)

通过残差跨视角注意力、层对齐Q-Former及共享动作专家，将视频骨干迁移到可变视角控制；保留各数据集原生接口。 对比基线预训练数据/算力不匹配；相机、背景、噪声扰动弱于OpenVLA-OFT，LIBERO-Plus汇总权重未说明。只有一种真机平台，未证明未见形态迁移。

## Late Breaking Results: Audio-Language-Action Models with Direct Speech Conditioning for Robotic Manipulation

- [arXiv 2610.33866](https://arxiv.org/abs/2610.33866) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33866)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33866)

Speech-π0.5将冻结语音编码器输出池化为32个VLM tokens，分别使用音频/任务LoRA，先做语音–文本蒸馏再训练动作。 两页DAC late-breaking短文，仅仿真及合成声音，每套件/条件500回合。三倍首动作加速伴随低于ASR的成功率，计时未单独交代语音采集及编码器成本。训练含10万合成指令，算力/多种子细节有限。

## POD-RoPE: Rotary Position Encoding over Physical Observation Distributions for Embodied AI

- [arXiv 2610.33745](https://arxiv.org/abs/2610.33745) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33745)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33745)

把token覆盖的相机中心、射线方向与时间表示为分布；期望旋转用于Q/K匹配及相干性引导的V/O聚合，不增加序列长度。 真机每任务仅20次试验，训练使用1,694条轨迹、64张H20及20k步检查点。几何依赖相机标定/运动学；模块计时并非机器人端到端延迟，视觉几何任务收益也非一致。

## EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models

- [arXiv 2610.33685](https://arxiv.org/abs/2610.33685) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33685)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33685)

将人类/机器人动作拆为共享位置码与形态专属运动学，再以共享token共训VLM并微调机器人动作。 额外使用8张A800进行50k步tokenizer训练与30k步共训；基线省去这些阶段，并非等算力。真机用2,450条示范、每条件仅10次试验。消融把73.2%一行称作基线，与主表66.8%不一致。

## Power-of-Two Leaky Integrate-and-Fire Neurons for Event-Driven Vision-Language-Action Inference

- [arXiv 2610.33658](https://arxiv.org/abs/2610.33658) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33658)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33658)

将π0.5部分投影替换为有符号二次幂脉冲及残余膜状态；Heartbeat把事件提取限制在各投影内部，保持外部token/缓存接口。 未测硬件能耗或延迟。86.95%节能是排除存储、控制和编码的示例FP32投影算术模型；匹配FP8且固定搬运预算时，T=1部分能耗估计仅省32.79%。评估单种子且仅仿真；不显著不等于统计等价。

## Tiny Recursive Policy: Recursive Latent Refinement for Visuomotor Control

- [arXiv 2610.33288](https://arxiv.org/abs/2610.33288) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33288)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33288)

小型行为克隆策略在单次预测内递归修订两层共享潜状态，并跨控制步保留状态；训练时截断跨步梯度。 仅仿真；LIBERO-Mem指标是子目标完成分而非整任务成功率。参数仅计骨干，不能代表推理成本：默认三次高层循环、六次低层修订。扰动训练增强鲁棒性，但干净Mem分数降至0.480。

## AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models

- [arXiv 2610.33074](https://arxiv.org/abs/2610.33074) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33074)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33074)

利用动作敏感度与权重恢复成本代理分配矩阵位宽；逐通道校准及分组无损编码降存储，执行时逐块恢复BF16权重。 仅单模型仿真，每套件150回合；10个输入计时不含前后处理。基线来自文献，官方仓库说明96.9%参照实际是FP16，尽管论文标BF16。W1.5*为视觉W4加语言平均W1.5，并非整模1.5bit；压缩增加延迟。

## One-shot Human Video-Guided Adaptation for Vision-Language-Action Models

- [arXiv 2610.19746](https://arxiv.org/abs/2610.19746) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.19746)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2610.19746)

v1→v2新增两种改造后视频条件基线，补齐旧版未填完整的消融结果，并以十次试验真机结果替换原五次表格；主要RoboTwin CapPro表现在v1已存在。 新增基线是适配π0.5后的版本，不是原系统原样比较。真机每任务仅10次，困难分类成功率仅20%。one-shot指目标任务测试时的人类视频指导，不代表总共只用一条示范训练；仍需源任务训练。

## What Can One Sentence Fix? A Failure Taxonomy and a Minimal Language Correction for Frozen VLA Policies

- [arXiv 2608.29967](https://arxiv.org/abs/2608.29967) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2608.29967)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2608.29967)

v1→v2将CorrectVLA改题并重构论述，以每条件三组10次真机运行替换旧小样本表，新增长程失败对照，明确区分仅失败重试恢复率与全部回合净成功率。仿真65/139及33/328恢复数沿用旧版。 人工标注失败类型并为失败运行编写带时窗纠正，耗时40–80秒，可追加纠正轮次。仅失败重试的仿真成功率不能证明无条件策略提升。该通道只修幅度/时机，不修语义目标或计划；LIBERO-90是指令OOD而非场景OOD。

## SentryVLA: Uncertainty-Guided Action Selection and State Monitoring for Vision-Language-Action Robotic Control

- [arXiv 2604.16677](https://arxiv.org/abs/2604.16677) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2604.16677)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2604.16677)

v1→v2新增边际覆盖命题，并把CQR结论严格限定于可交换的帧—候选校准样本，同时补校准诊断及动作评分设计细节。这是可靠性结论的实质澄清，不是新增安全保证。 保证不延伸到自适应选中动作、时间相关闭环状态、分布偏移或任务成功；监测阈值及OOD结果仍是经验性结论。本次未独立复现校准实验。

## ActECC: Action Chunk Temporal Harnessing for Edge-Cloud Collaborative VLA Inference System

- [arXiv 2603.07949](https://arxiv.org/abs/2603.07949) · v3 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2603.07949)
- 收录历史: [2026-10-27 (v3, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2603.07949)

v2→v3从RAPID改为ActECC：重点由端云划分转为运动学引导的动作块可用范围与延迟感知重规划调度，并替换为π0.5/GR00T N1.5系统评测；旧1.73倍速度结论不可直接比较。 指标是相对对齐专家轨迹的偏差，明确不是任务成功率；属于仿真/系统评测，cloud-only延迟可能比ActECC更低。两个最大收益来自不同对比，不能拼成单一配置。

## RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

- [arXiv 2610.32971](https://arxiv.org/abs/2610.32971) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32971)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32971)

统一17种鲁棒/安全RL算法及6种标准对照，提供可复用接口及含延迟、语义的单因素/组合部署扰动。 并非每算法运行每任务；保留各自原生预算，算法族混合均值会混入基础学习器强弱。π0.5实验仅单个微调模型的离线关节示范轨迹跟踪，不是闭环VLA成功率或真机验证。

## RynnUnify: Towards Unified Embodied Brain

- [arXiv 2610.32965](https://arxiv.org/abs/2610.32965) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32965)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32965)

基于Cosmos3的16B模型耦合8B推理器和8B视频生成器；跨片段场景帧支撑交错视觉规划，另行RL训练的推理器选择是否调用生成证据，WAM适配联合学习视频与动作。 机器人适配使用约1,600小时原子任务及177小时组合任务数据。完整split的基线数值引用既有报告，精选20任务由作者评估；视觉历史是回合内上下文，不是已验证终身记忆，3项真机任务未隔离记忆贡献。

## If at First You Don’t Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

- [arXiv 2610.32941](https://arxiv.org/abs/2610.32941) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32941)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32941)

用冻结策略rollout训练小型失败头，触发后回放实际已完成机械臂运动的逆序，再交回原策略重试。 仅仿真；汇总结果包含选参种子，留出种子π0.5收益为0.70个百分点。回退不恢复物体或保证安全，失败头仍需标注rollout训练。

## Retiming Robot Demonstrations with a Learned Speed Prior

- [arXiv 2610.32676](https://arxiv.org/abs/2610.32676) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32676)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32676)

学习可迁移的示范速度分布，用已观测更快节奏重定时轨迹，并把预测节奏的VLA与约束感知实时轨迹执行层结合。 需要离线策略训练和专门执行控制器，不是直接加速推理的开关。速度先验不能超出已有示范节奏；超时会影响成功率，因此须看同速对照。SAIL对比采用不同机器人与策略。

## When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

- [arXiv 2610.32431](https://arxiv.org/abs/2610.32431) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32431)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32431)

MART-GRPO 用微调后冻结的VLM从完整rollout视频定位最后一个未恢复的可见错误，截断其后失败惩罚，同时保留成功轨迹项及原归一化；理想停止理论提供动机，但不认证实际回溯实现。 仅仿真；策略看单相机，VLM审查三视角，另需标注及VLM微调。边界使用完整未来轨迹，不一定满足理想停止条件；一项任务下降1.95个百分点，留出场景种子不等于独立训练种子。

## LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners

- [arXiv 2610.32348](https://arxiv.org/abs/2610.32348) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32348)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32348)

结合不可改写的执行日志、逐字保留的笔记历史、预期变化触发帧及先粗看再细查示范；Astra输出路点或π0.5落地子目标。记忆是推理时接口，而非参数适配。 干净记忆对照主要证明降成本，未显示明确成功率增益；完整系统还改变动作/调用接口。直接控制使用深度、标定及来自成功判定代码的任务说明。仅单仿真基准和闭源模型，无真机；单组件消融差别仅2–4回合。

## MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation

- [arXiv 2610.32312](https://arxiv.org/abs/2610.32312) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32312)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32312)

将技能条件LoRA专家与RGB-D轨迹可供性热图结合，以热图偏置动作注意力。 MAST额外使用深度而基线仅RGB，不能将收益全归因于架构。指令逐原语下发，并非自主分解长任务；几何失效和执行漂移仍存在。

## Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems

- [arXiv 2610.32208](https://arxiv.org/abs/2610.32208) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32208)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32208)

用稀疏自编码器分解OpenVLA内部激活，预测失败并由外部VLM解释与结果相关的行为；通过分支重试估计不可恢复时间点。 仅仿真、单模型；SAE无监督训练使用全部500轨迹，监督预测器才留出。每点4次分支估计粗糙且受剩余预算影响；相关特征并非因果机制或已验证安全干预。

## Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies

- [arXiv 2610.32102](https://arxiv.org/abs/2610.32102) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32102)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32102)

联合研究执行动作长度与flow求解步数，检验浅采样何时有效或有害。 长开环在移动目标上失效；加速指摊销推理成本，不保证任务墙钟加速。论文对仿真任务总数及π0.5动作块配置存在不一致描述。

## TTT in VLA Models: Exploring Training with Human Demonstrations

- [arXiv 2610.32094](https://arxiv.org/abs/2610.32094) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32094)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32094)

在InternVLA-A1和π0.5中加入fast-weight TTT，记录人类示范到机器人阶段的记忆传递及截断梯度路径。 负结果限于小规模选杯数据和所测配方，不是对TTT的普遍否定；试验次数报告不足。自回归状态评估仍使用录制图像，并非闭环观测。

## DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

- [arXiv 2610.32093](https://arxiv.org/abs/2610.32093) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32093)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32093)

用特权状态、潜变量条件RL、逆向课程和成功门控多样性生成过滤后的示范，再训练视觉π0.5，部署的不是RL生成器。 依赖准确仿真、特权状态、状态重置和成功信号。真机仅4个简单桌面任务、较小迁移差距及1个训练种子；过大多样性会损害任务能力。

## Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates

- [arXiv 2610.31859](https://arxiv.org/abs/2610.31859) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31859)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31859)

审计可训练矩阵和AdamW状态保持bf16、无fp32主副本时的更新舍入。 仅一个任务集、缩短训练；未单独消融优化器矩精度。SmolVLA评测器差异限制跨论文比较；不能推断所有bf16计算或JAX训练均受影响。

## EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions

- [arXiv 2610.31845](https://arxiv.org/abs/2610.31845) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31845)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31845)

以来源可靠性调节噪声与损失权重，将联合视觉-动作流与可见干净未来的EMA教师蒸馏结合，利用带噪人类动作标签。 外部RoboCasa基线取自发表结果、预训练和预算不同。π0.5真机对照重置输入输出层以适配58DoF，不能将差距纯归因方法；仍需动作标注，来源加权不能纠正系统性重定向偏差。

## ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

- [arXiv 2610.24512](https://arxiv.org/abs/2610.24512) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.24512)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2610.24512)

包含8类接触丰富技能、36个参考任务及40余可打印资产与配套仿真的基准；在6任务上比较视觉及视触觉学习策略。 四系统的预训练、观测历史及触觉接口不同，并非完全隔离变量的触觉消融；36任务中仅6项做学习策略评估。魔术贴固定使部分原本需另一臂稳定物体的任务可由单臂完成。刚性/关节打印资产不覆盖形变接触；触觉负结果只适用于所测策略与传感器，不能泛化为触觉无用。

## RAPAC-DP: Response-Aligned Pending-Action Compensation for Diffusion Policies under Delayed Execution

- [arXiv 2608.15924](https://arxiv.org/abs/2608.15924) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2608.15924)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2608.15924)

在冻结扩散/流策略上加入待执行动作编码器和LoRA补偿，将动作块对齐计划交接时间，仅用无延迟示范构造延迟条件训练样本。 每方法/任务仅一个检查点，置信区间反映试验抽样而非训练种子鲁棒性。固定传送带速度/起点和离散注入延迟限制其对任意网络抖动的结论；低延迟动态抓取73.3%低于RTC76.7%。需要训练适配器，不是免训练修复。

## Semantic Anchoring for Robotic Action Representations

- [arXiv 2607.13597](https://arxiv.org/abs/2607.13597) · v3 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2607.13597)
- 收录历史: [2026-10-26 (v3, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2607.13597)

以冻结的操作文本编码器为锚，通过共享/私有表征的辅助对齐目标保留VLA微调中的任务语义，推理时移除辅助模块。 相关性不能证明语义侵蚀是分布外失败的唯一原因；各架构沿用不同官方微调方案。冻结语义编码器限制性能，共享/私有因子无可识别性保证；属于下游微调而非部署中的持续适配。

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

