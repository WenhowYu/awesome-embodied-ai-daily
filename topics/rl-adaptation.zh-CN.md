# 强化学习与适应

[English](rl-adaptation.md) | [简体中文](rl-adaptation.zh-CN.md) | [所有主题](README.zh-CN.md)

31 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

## METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

- [arXiv 2610.31656](https://arxiv.org/abs/2610.31656) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31656)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31656)

METTA 将回合内可梯度更新的快速神经记忆与跨回合的紧凑摘要分开。它在 Meta-World ML10/45 未见任务族上报告超过 50% 成功率，并改善长上下文稀疏奖励探索。

## PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning

- [arXiv 2610.31299](https://arxiv.org/abs/2610.31299) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31299)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31299)

PiHand 将仿真中的动作捕捉跟踪专家蒸馏为目标条件手–物交互潜变量先验，再在潜空间中学习有界残差探索。同一交互先验可支持新物体、新轨迹、接物和双手交接。

## Learning Robot Behavior Priors from Non-Robotic Synthetic Data

- [arXiv 2610.31275](https://arxiv.org/abs/2610.31275) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.31275)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.31275)

用MDP、上下文bandit和线性动力系统等程序化非机器人数据预训练Transformer，通过示例上下文预测未见机器人动作。 仅离线开环动作预测，输入是状态而非视觉，不是真机执行成功率；“零样本”仍使用任务内状态动作上下文。

## In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

- [arXiv 2610.30988](https://arxiv.org/abs/2610.30988) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30988)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30988)

部分点云经生成式状态补全，再用上下文条件 Transformer 预测布料动力学，为流匹配动作候选排序；测试时不更新权重。 实机表无对照策略；成功由点云距离阈值定义。PCN 的 CD/EMD 更好；本文优势是对应点 MSE。快速动态操作及闭环重规划仍待验证。

## DRILL: Training World Models to Improve Policies, Not Predict Pixels

- [arXiv 2610.30814](https://arxiv.org/abs/2610.30814) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30814)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30814)

DRILL 直接优化世界模型生成的想象 rollout 对策略学习的帮助。其低成本加权代理目标与双层元梯度方案，把下游回报作为目标，而非仅追求像素预测精度。

## Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation

- [arXiv 2610.30810](https://arxiv.org/abs/2610.30810) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30810)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30810)

ALMA 用动作条件未来响应预测训练历史上下文，并让LLM依据失败生成新的机械臂运动结构，扩展RL训练任务。 部署参数冻结，适应来自上下文，非test-time梯度训练；真机只对比PID，不可将79.6%改善当作相对最强仿真基线。接触力控制仍属后续方向。

## Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation

- [arXiv 2610.30643](https://arxiv.org/abs/2610.30643) · v1 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2610.30643)
- 收录历史: [2026-10-23 (v1, new)](../daily/2026-10-23.zh-CN.md#arxiv-2610.30643)

FETA 在测试时只对选中的关键动作索取一次二元反馈，并据此更新导航策略。它先筛选不稳定轨迹，再定位熵梯度大的决策步骤，按策略与反馈的分歧加权更新。

## Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- [arXiv 2609.39304](https://arxiv.org/abs/2609.39304) · v4 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2609.39304)
- 收录历史: [2026-10-23 (v4, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2609.39304)

Scale and Selection 通过增加 rollout 样本量及优胜者–挑战者筛选改进视觉接口机器人代理。本次修订新增蒸馏闭环，将代理辅助执行经验转化为独立机器人策略。

## FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence

- [arXiv 2609.17210](https://arxiv.org/abs/2609.17210) · v2 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2609.17210)
- 收录历史: [2026-10-23 (v2, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2609.17210)

FluxVLA 统一策略数据、训练、评估与机器人执行接口。本次大幅扩展的修订新增 RLinf 在线 PPO 接口、更广泛的仿真与真机集成，以及成对后训练实验；它是一套工程平台，而非新的基础策略。

## Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models

- [arXiv 2602.12628](https://arxiv.org/abs/2602.12628) · v5 · [最新归档](../daily/2026-10-23.zh-CN.md#arxiv-2602.12628)
- 收录历史: [2026-10-23 (v5, revised)](../daily/2026-10-23.zh-CN.md#arxiv-2602.12628)

RL-Co 先用仿真与真机示范共同监督预热，再在仿真 RL 中保留真机监督约束。本次修订新增更强的 rollout 蒸馏对照，并明确真机统计评估的范围。

## PhysiCalWorld: In-Context Physics Calibration for World Models

- [arXiv 2610.30125](https://arxiv.org/abs/2610.30125) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30125)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30125)

交互提取的紧凑物理 token 无需梯度更新即可改善部分规划结果，但仅有仿真证据，且并非始终优于上下文或有监督基线。

## Asymmetric On-Policy Distillation Learns In-Context Exploration

- [arXiv 2610.30105](https://arxiv.org/abs/2610.30105) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30105)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30105)

特权专家的 on-policy 蒸馏支持共享隐变量下的跨回合探索，但真机样本有限，上下文并非永久技能库。

## AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

- [arXiv 2610.30097](https://arxiv.org/abs/2610.30097) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.30097)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.30097)

原子子任务信用分配和瓶颈探索改善长程 RL；真机相对 PPO 提高 8.0 个百分点，训练在重建仿真中完成。

## Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation

- [arXiv 2610.29264](https://arxiv.org/abs/2610.29264) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29264)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29264)

人类参与部署使 WAM 能在会话内更新，但最终成绩接近预算匹配的固定策略，尚无跨任务持续学习证据。

## SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training

- [arXiv 2610.29161](https://arxiv.org/abs/2610.29161) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29161)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29161)

自动干预采集支持控变量的 VLA 后训练比较；真机提升体现算法改动迁移，并非仿真策略零样本转真机。

## Learning to Absorb Corrections: Critic-Weighted Residual Flow for Vision-Based Insertion

- [arXiv 2610.29117](https://arxiv.org/abs/2610.29117) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.29117)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.29117)

critic 加权残差学习被 ACT 吸收：关闭残差后的成功率从 16% 提高到 76%，但跨任务遗忘和 VLA 迁移尚未验证。

## COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation

- [arXiv 2610.28948](https://arxiv.org/abs/2610.28948) · v1 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2610.28948)
- 收录历史: [2026-10-22 (v1, new)](../daily/2026-10-22.zh-CN.md#arxiv-2610.28948)

局部抓取专家支持情境化全身操作，真机成绩较强；但算力未匹配，部署时不进行持续学习。

## HarnessPAI: An Evolving Harness for Physical AI

- [arXiv 2609.29166](https://arxiv.org/abs/2609.29166) · v2 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2609.29166)
- 收录历史: [2026-10-22 (v2, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2609.29166)

新增 DreamZero 微调复用 harness 成功轨迹，报告均值从 5.1% 提高到 26.5%；按评估成绩选 checkpoint 限制了证据强度。

## SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model

- [arXiv 2606.20698](https://arxiv.org/abs/2606.20698) · v2 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2606.20698)
- 收录历史: [2026-10-22 (v2, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2606.20698)

修订验证安全评估头校准，主成功率表未变；Level II 增益很小，代理成本不能保证真实部署安全。

## Feedback World Model Enables Precise Guidance of Diffusion Policy

- [arXiv 2605.15705](https://arxiv.org/abs/2605.15705) · v2 · [最新归档](../daily/2026-10-22.zh-CN.md#arxiv-2605.15705)
- 收录历史: [2026-10-22 (v2, revised)](../daily/2026-10-22.zh-CN.md#arxiv-2605.15705)

残差反馈无需参数更新即可适配冻结 WAM；适中 gain 改善 OOD 成功率，而 gain 1 使预测误差恶化。

## Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

- [arXiv 2610.28613](https://arxiv.org/abs/2610.28613) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28613)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28613)

视触觉世界模型支持评测与策略后训练；四项 ARX 任务真机均值从 SFT 的 59.1% 升至 70.8%，但其中一项任务低于 SFT。

## AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- [arXiv 2610.28589](https://arxiv.org/abs/2610.28589) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.28589)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.28589)

以成功轨迹 SFT 和多轮 RL 训练 9B 机器人规划器，保持执行器冻结；LIBERO-PRO 达 71.0%，但训练测试共享任务，且无真机结果。

## AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies

- [arXiv 2610.27736](https://arxiv.org/abs/2610.27736) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27736)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27736)

优势加权潜在引导在不进行后训练真机 rollout 的条件下改进冻结单步 decoder；真机成功 65/100，只有相对 MeanFlow 的总体提升通过多重比较校正。

## VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs

- [arXiv 2610.27698](https://arxiv.org/abs/2610.27698) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27698)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27698)

成对评测 VLA 视觉调优的目标收益与跨维度保留；10 个设置中 8 个非目标均值下降，研究干预是定向微调而非在线持续学习。

## Training Controllable World Models via Action Influence Maximization

- [arXiv 2610.27387](https://arxiv.org/abs/2610.27387) · v1 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2610.27387)
- 收录历史: [2026-10-21 (v1, new)](../daily/2026-10-21.zh-CN.md#arxiv-2610.27387)

动作影响力目标引导可控世界模型的主动数据采集；Push-T 特定可控性指标对应 85 倍数据量比，证据仅覆盖两个仿真环境。

## DEFLECT: Temporal Counterfactual Preference Learning for Delay-Robust Asynchronous VLAs

- [arXiv 2605.19294](https://arxiv.org/abs/2605.19294) · v3 · [最新归档](../daily/2026-10-21.zh-CN.md#arxiv-2605.19294)
- 收录历史: [2026-10-21 (v3, substantive-revision)](../daily/2026-10-21.zh-CN.md#arxiv-2605.19294)

修订为抗延迟 VLA 偏好学习补充跨骨干及继续训练对照；GR00T 在四步延迟下达 73.10%，协议变化使新旧版 headline 数字不可直接比较。

## PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models

- [arXiv 2610.26813](https://arxiv.org/abs/2610.26813) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.26813)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.26813)

正常外观的 EMA teacher 与扰动观测 student 对齐浅/深层动作表征，推理无额外模型，面向 WAM 后训练与真实环境外观鲁棒性。

## SteerAct: Unlocking Action Models through Few-Shot Temporal Steering

- [arXiv 2610.25632](https://arxiv.org/abs/2610.25632) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.25632)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.25632)

用每任务 24 条带成败标签的 rollout 建立时序特征参考库，在线选择干预时机、方向和强度，冻结 π0.5／Fast-WAM。连接经验参考与测试时适应，不更新主模型权重。

## Self-Improving Video-to-Action Models

- [arXiv 2610.24177](https://arxiv.org/abs/2610.24177) · v1 · [最新归档](../daily/2026-10-20.zh-CN.md#arxiv-2610.24177)
- 收录历史: [2026-10-20 (v1, new)](../daily/2026-10-20.zh-CN.md#arxiv-2610.24177)

视频规划器提出目标视频，V2A 模型以自身交互生成视频—动作训练对并反复改进。

## AnchorQ: Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors

- [arXiv 2610.22852](https://arxiv.org/abs/2610.22852) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22852)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22852)

将粗参考动作通过 flow reversal 转成状态相关的噪声锚点，再以局部粒子和在线 critic 探索，保持基础 VLA 冻结。

## Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations

- [arXiv 2610.22576](https://arxiv.org/abs/2610.22576) · v1 · [最新归档](../daily/2026-10-19.zh-CN.md#arxiv-2610.22576)
- 收录历史: [2026-10-19 (v1, new)](../daily/2026-10-19.zh-CN.md#arxiv-2610.22576)

以少量校准任务的成功 rollout 训练具身分类器，在 π0 每一步去噪时用分类器梯度引导动作，保持 VLA 参数冻结。

