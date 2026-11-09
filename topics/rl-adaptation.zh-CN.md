# 强化学习与适应

[English](rl-adaptation.md) | [简体中文](rl-adaptation.zh-CN.md) | [所有主题](README.zh-CN.md)

235 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

## Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation

- [arXiv 2611.09864](https://arxiv.org/abs/2611.09864) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09864)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09864)

将多抓取 PPO critic 蒸馏为效用网络，按后续重排目标选择抓取点。

## Autonomous Particle Image Velocimetry Using Zero-Shot Sim-to-Real Reinforcement Learning

- [arXiv 2611.09679](https://arxiv.org/abs/2611.09679) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09679)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09679)

强化学习策略控制六自由度机械臂相机，通过流场估计与不确定性定位和解析水翼尾流。

## Goodhart in the Planner: Sampling-Based Control Exploits Rewards Learned from Human Preferences

- [arXiv 2611.09670](https://arxiv.org/abs/2611.09670) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09670)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09670)

研究更强搜索如何在偏好标签准确率较高时仍利用奖励模型误差，并提出校准正则化。

## Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning

- [arXiv 2611.09625](https://arxiv.org/abs/2611.09625) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09625)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09625)

TT-MBRL 在测试时更新世界模型参数以编码当前回合的记忆，而不只依赖循环状态或上下文。论文在二维和三维 Memory Maze 中提升了多种架构的表现，同时在 DeepMind Control 与 Atari 100k 上保持较强性能。该方向与长时程导航和部分可观测具身任务相关。

## DKWBC: Decoupling Motion Tracking and Balancing for Humanoid Whole-Body Control

- [arXiv 2611.09605](https://arxiv.org/abs/2611.09605) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09605)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09605)

将逆动力学与 PD 跟踪结合，并用学习残差专门处理平衡。

## DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning

- [arXiv 2611.09433](https://arxiv.org/abs/2611.09433) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09433)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09433)

DexDICE 将遵守安全规范但可能次优的示范与高性能但可能不安全的示范分开建模，通过分布校正和安全支持集约束学习策略。论文评估了重新整理的 38 个 DSRL 任务及使用遥操作数据训练的实体移动机器人；实体实验 10 次均到达目标，未观察到安全违规。适用于混合质量示范下的机器人策略学习。

## Can LLMs Debug Robots by Editing Their Weights?

- [arXiv 2611.09376](https://arxiv.org/abs/2611.09376) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09376)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09376)

LLM利用有限仿真反馈直接编辑65个词嵌入行，无梯度更新或新增示范，修复指令词汇绑定。

## Probably Safe Sim-to-Real Transfer with Lifetime Validity

- [arXiv 2611.09344](https://arxiv.org/abs/2611.09344) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09344)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09344)

Dejavu 仅利用已部署安全基线策略收集的轨迹，在候选仿真策略部署前进行认证。方法结合逐决策重要性采样、投注置信序列及可求和失败概率预算，使无界次数的策略升级仍具有统计有效性。其目标是持续更新策略过程中的安全认证，而不只是一次性的仿真到现实迁移。

## Horizon-Coupled Obstacle Guidance for Relative-Action Diffusion Policies

- [arXiv 2611.09340](https://arxiv.org/abs/2611.09340) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09340)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09340)

将相对动作累积成轨迹，并在去噪时把SDF障碍反馈传播到整个动作时域，无需重训。

## SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References

- [arXiv 2611.09266](https://arxiv.org/abs/2611.09266) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09266)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09266)

用可复用模板合成交互参考，再以特权教师、视觉蒸馏与强化学习获得全身移动操作技能。

## Safe Reinforcement Learning via Probabilistic Option Shielding

- [arXiv 2611.09197](https://arxiv.org/abs/2611.09197) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.09197)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.09197)

概率选项屏蔽从单步逻辑屏蔽信号学习选项安全评价器，预测具有时间延展的行为能否安全完成。在 LogiCity 导航变体中，它改善训练安全性并保持任务表现，为缺乏完整环境模型的系统提供长时程安全机制。

## PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation

- [arXiv 2611.08917](https://arxiv.org/abs/2611.08917) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.08917)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.08917)

将技能保存为冻结低秩动作适配器，用逐动作块路由组合技能。

## Localizing and Editing the Goal Representation of a Vision-Language-Action Model

- [arXiv 2611.08895](https://arxiv.org/abs/2611.08895) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.08895)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.08895)

分析 OpenVLA 对否定指令的失效，并定位可编辑的目标表征。

## STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards

- [arXiv 2611.08857](https://arxiv.org/abs/2611.08857) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.08857)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.08857)

采用只需 IMU 的加速度奖励，结合离策略 RL、高增益控制与左右对称增强。

## It Takes Two to Tangram: Multi-Agent Object Centric Reinforcement Learning for Assembly

- [arXiv 2611.08814](https://arxiv.org/abs/2611.08814) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.08814)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.08814)

将每个拼块视为协作智能体，用图网络策略协调平面装配。

## ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing

- [arXiv 2611.08664](https://arxiv.org/abs/2611.08664) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.08664)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.08664)

两阶段强化学习从机载观测推断力与状态潜变量，协调全身残差控制。

## CS-Pi: Constraint-Satisfying Flow Policy Sampling

- [arXiv 2611.08654](https://arxiv.org/abs/2611.08654) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.08654)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.08654)

通过采样、投影、重新加噪，在不重训流策略的情况下施加部署时约束。

## Q-OIL: Optimistic Exploration in Learning from Human Interventions

- [arXiv 2611.08576](https://arxiv.org/abs/2611.08576) · v1 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2611.08576)
- 收录历史: [2026-11-09 (v1, new)](../daily/2026-11-09.zh-CN.md#arxiv-2611.08576)

利用进度感知的人工干预模型和解耦 critic，将不完美纠错用作探索指引。

## RoboFQE: Rollout-Free Evaluation of Visual Robot Policies from Offline Trajectories

- [arXiv 2610.18699](https://arxiv.org/abs/2610.18699) · v2 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2610.18699)
- 收录历史: [2026-11-09 (v2, revised)](../daily/2026-11-09.zh-CN.md#arxiv-2610.18699)

通过拟合 Q 评估估计机器人策略表现，以减少完整在线评测需求。

## Spectral Alignment in Forward-Backward Representations via Temporal Abstraction

- [arXiv 2603.20103](https://arxiv.org/abs/2603.20103) · v5 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2603.20103)
- 收录历史: [2026-11-09 (v5, revised)](../daily/2026-11-09.zh-CN.md#arxiv-2603.20103)

通过时间抽象改善前向-后向表征的谱对齐，以支持无奖励强化学习。

## VLD: Visual Learned Distance as an Interface for Reinforcement Learning Navigation

- [arXiv 2512.07976](https://arxiv.org/abs/2512.07976) · v3 · [最新归档](../daily/2026-11-09.zh-CN.md#arxiv-2512.07976)
- 收录历史: [2026-11-09 (v3, revised)](../daily/2026-11-09.zh-CN.md#arxiv-2512.07976)

将视频训练的视觉目标距离预测器与基于几何条件噪声训练的强化学习导航器解耦。

## OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions

- [arXiv 2611.08462](https://arxiv.org/abs/2611.08462) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08462)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08462)

OopsieRecover从干预中溯因学习语义空间纠正程序，仅在需要时引导冻结VLA。

## Latent RL Priors for Data-Efficient Dexterous Manipulation

- [arXiv 2611.08458](https://arxiv.org/abs/2611.08458) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08458)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08458)

Latent RL Prior冻结由特权状态强化学习得来的动作解码器，再由示范学习图像到潜在接口。

## SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing

- [arXiv 2611.08364](https://arxiv.org/abs/2611.08364) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08364)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08364)

SHORE将稳定性概率与稳定条件收益结合，用于在线装箱。

## RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines

- [arXiv 2611.08308](https://arxiv.org/abs/2611.08308) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08308)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08308)

RM-VLM把语言任务分解为奖励机命题，用冻结VLM落地视觉状态，并以概率自动机状态处理非马尔可夫奖励学习。

## Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated Users in Interactive Worlds

- [arXiv 2611.08286](https://arxiv.org/abs/2611.08286) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08286)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08286)

Interactive Visual Gym在烹饪、家居和手机界面仿真中闭环评估助手，引入带个性的模拟用户及可控失误。

## Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning

- [arXiv 2611.08144](https://arxiv.org/abs/2611.08144) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08144)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08144)

逐步账本检查环境—训练器通信协议，以发现静默强化学习数据故障。

## Reinforcing End-to-End Autonomous Driving Safety via Negative-Aware Planning in a Unified World-Action Model

- [arXiv 2611.08111](https://arxiv.org/abs/2611.08111) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08111)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08111)

NegWAM 用接近专家但危险的轨迹后训练驾驶 WAM；推理时丢弃辅助安全分支。

## STEP: Spatiotemporal Training with Explicit Prediction for Perceptive Humanoid Locomotion

- [arXiv 2611.08097](https://arxiv.org/abs/2611.08097) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08097)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08097)

STEP 结合跨模态掩码预测及动作条件潜在下一状态预测，训练人形控制表示。

## Leave It Better Than Found: Value-Guided Cooperation in Sequential Tasks

- [arXiv 2611.08075](https://arxiv.org/abs/2611.08075) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08075)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08075)

机器人共享价值函数并使用 KNN 不确定性过滤，实现无需共同训练的顺序协作。

## Terrain-Indexed Motion Priors and Geometric Support for Extreme Humanoid Parkour

- [arXiv 2611.08056](https://arxiv.org/abs/2611.08056) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.08056)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.08056)

渐进模仿先学习跑酷技能，再减弱动作先验以适配手膝支撑。

## WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation

- [arXiv 2611.07939](https://arxiv.org/abs/2611.07939) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07939)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07939)

WAM-Sim以姿态对齐道路结构、地理定位背景记忆和一次写入的物体身份令牌约束驾驶视频生成，再用在线流匹配强化学习后训练。

## GuidedWAM: Training-Free Energy Guidance for World Action Models in Autonomous Driving

- [arXiv 2611.07912](https://arxiv.org/abs/2611.07912) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07912)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07912)

GuidedWAM在冻结驾驶WAM采样时，对干净动作估计施加可微目标能量。

## TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

- [arXiv 2611.07881](https://arxiv.org/abs/2611.07881) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07881)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07881)

TactileLab 以刚体仿真的触觉流近似剪切，并将真实传感图像转换到仿真表示。

## Learning Robotic World Models with Semantic and Visual Feedback

- [arXiv 2611.07850](https://arxiv.org/abs/2611.07850) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07850)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07850)

RoboImagine 通过多样候选未来和语义、视觉偏好反馈后训练机器人视觉世界模型。

## Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes

- [arXiv 2611.07730](https://arxiv.org/abs/2611.07730) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07730)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07730)

训练时由社交与语义世界模型评价动作，将前瞻能力蒸馏进单次前向导航策略。

## PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion

- [arXiv 2611.07679](https://arxiv.org/abs/2611.07679) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07679)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07679)

PhySA 将 VLM 审美奖励与基于状态的物理平滑度修正分离。

## Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation

- [arXiv 2611.07532](https://arxiv.org/abs/2611.07532) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07532)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07532)

S2C 将 VLM 语义定位与带力反馈的人在环残差强化学习分开。

## How do Transformers Perform Low-Level Control In-Context?

- [arXiv 2611.07291](https://arxiv.org/abs/2611.07291) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07291)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07291)

GPT-2式控制器以无外力轨迹作为上下文，在未知非线性系统参数下学习稳定控制。

## Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging

- [arXiv 2611.07275](https://arxiv.org/abs/2611.07275) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07275)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07275)

LARBRID 对齐动作空间与初始噪声空间价值表示，以适配扩散或流策略。

## An Empirical Study of Reinforcement Learning for Keypoint Positioning of Deformable Linear Objects

- [arXiv 2611.07261](https://arxiv.org/abs/2611.07261) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07261)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07261)

研究可变形线状物操作的强化学习训练栈、相对关键点观测与随机化。

## MAC-v2: Long-horizon model-based value expansion from pixels

- [arXiv 2611.07245](https://arxiv.org/abs/2611.07245) · v1 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.07245)
- 收录历史: [2026-11-06 (v1, new)](../daily/2026-11-06.zh-CN.md#arxiv-2611.07245)

MAC-v2结合无需图像重建的潜在动力学与动作分块，在像素输入的离线强化学习中进行长时域模型价值扩展。

## ZipDrift: Generating Multimodal Short-Horizon MPC Costs with One-Step Drifting Models

- [arXiv 2611.05793](https://arxiv.org/abs/2611.05793) · v2 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.05793)
- 收录历史: [2026-11-06 (v2, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2611.05793)

此记录为内容或状态修正，不代表新的研究进展。

## Why Koopman Structure Does Not Help Differentiable World Models for Humanoid Whole-Body Tracking

- [arXiv 2611.00951](https://arxiv.org/abs/2611.00951) · v2 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2611.00951)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00951) · [2026-11-06 (v2, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2611.00951)

在仿真 G1 动作跟踪中，对比用想象轨迹梯度训练的双线性 Koopman 与 MLP 世界模型。

## SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU

- [arXiv 2610.39327](https://arxiv.org/abs/2610.39327) · v3 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2610.39327)
- 收录历史: [2026-11-06 (v3, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2610.39327)

新增面向真实机器人的后训练配方，以及同设置下新旧检查点对比。从 v0.1 跟踪器出发，v1.0 再训练 4,000 轮，加入部署扭矩限制、0–40 ms 执行延迟、增益随机化及接近扭矩上限的惩罚；单张 RTX PRO 6000 约需 9.2 GPU 小时。

## VIGOR: Zero-Shot Visual Generalization via Latent-Space Consistency in Model-Based Reinforcement Learning

- [arXiv 2610.02801](https://arxiv.org/abs/2610.02801) · v2 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2610.02801)
- 收录历史: [2026-11-06 (v2, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2610.02801)

VIGOR结合弱强增强、动力学一致性与编码器稳定化，改善潜在世界模型强化学习的零样本视觉泛化。

## PFM-HR: Pose Flow Matching for Humanoid Robots

- [arXiv 2608.03227](https://arxiv.org/abs/2608.03227) · v4 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2608.03227)
- 收录历史: [2026-11-06 (v4, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2608.03227)

PFM-HR从无序姿态学习冻结流匹配先验，用雅可比响应塑造人形机器人跟踪奖励。

## DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation

- [arXiv 2607.13033](https://arxiv.org/abs/2607.13033) · v2 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2607.13033)
- 收录历史: [2026-11-06 (v2, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2607.13033)

DenseReward用2.7万成功/失败轨迹学习视觉语言进度评分，为机器人策略强化学习补充稀疏完成奖励。

## World Models as Adversaries: Multi-Agent Self-Play Fine-Tuning for Robust Motion Planning

- [arXiv 2607.10630](https://arxiv.org/abs/2607.10630) · v2 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2607.10630)
- 收录历史: [2026-11-06 (v2, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2607.10630)

角色条件对抗交通世界模型学习稀疏协作攻击，再冻结用于regret-CVaR自车规划器适应。

## CoDiMAD: Diffusion-Based Privileged Distillation for Communication-Free Multi-Robot Coordination

- [arXiv 2607.09587](https://arxiv.org/abs/2607.09587) · v2 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2607.09587)
- 收录历史: [2026-11-06 (v2, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2607.09587)

CoDiMAD把特权MAPPO蒸馏为局部历史条件的扩散策略，避免对不同协作动作模式取平均。

## EmboTeam: Asymmetric State Grounding for Heterogeneous Multi-Robot Collaboration

- [arXiv 2601.11063](https://arxiv.org/abs/2601.11063) · v3 · [最新归档](../daily/2026-11-06.zh-CN.md#arxiv-2601.11063)
- 收录历史: [2026-11-06 (v3, revised)](../daily/2026-11-06.zh-CN.md#arxiv-2601.11063)

LLM生成状态预期，经PDDL验证后用并行行为树、反应式检查和同步协调异构机器人技能。

## Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement

- [arXiv 2611.06905](https://arxiv.org/abs/2611.06905) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.06905)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.06905)

系统比较直接策略适配、评论器引导的动作筛选和策略提取，以研究通用机器人策略的多任务在线改进。

## TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics

- [arXiv 2611.06442](https://arxiv.org/abs/2611.06442) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.06442)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.06442)

数字孪生提供策略初始化和稠密视觉奖励监督，用于真机在线优化。

## Online Adaptation to Latent Physical Properties for Learning from Demonstration

- [arXiv 2611.06118](https://arxiv.org/abs/2611.06118) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.06118)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.06118)

根据预测误差在线更新物理属性隐变量，策略及动力学模型权重保持不变。

## Diversity-Aware Experience Replay via Statistical Leverage Scores

- [arXiv 2611.05929](https://arxiv.org/abs/2611.05929) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.05929)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.05929)

基于统计杠杆值的回放突出稀有经验，目标相对轨迹窗口识别关系型稀有事件。

## Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning

- [arXiv 2611.05667](https://arxiv.org/abs/2611.05667) · v1 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2611.05667)
- 收录历史: [2026-11-05 (v1, new)](../daily/2026-11-05.zh-CN.md#arxiv-2611.05667)

PHIL在XR中预览未来轨迹，将提前干预转化为偏好训练对。

## Warp: Structured Output-Space Adaptation for Frozen Robot Policies

- [arXiv 2606.31043](https://arxiv.org/abs/2606.31043) · v4 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2606.31043)
- 收录历史: [2026-11-05 (v4, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2606.31043)

用结构化单调样条适配冻结机器人策略；本次新增匹配SplineRes对照和诊断，区分参数化优势与非线性动作重塑。

## Provably Safe, Yet Scalable Reinforcement Learning

- [arXiv 2606.14536](https://arxiv.org/abs/2606.14536) · v2 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2606.14536)
- 收录历史: [2026-11-05 (v2, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2606.14536)

PS2-RL结合学习备用策略与可微控制不变投影；v2新增多约束机器人控制测试并分析安全与性能来源。

## FLAG: Flow Policy MaxEnt-RL by Latent Augmented Guidance

- [arXiv 2605.30749](https://arxiv.org/abs/2605.30749) · v2 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2605.30749)
- 收录历史: [2026-11-05 (v2, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2605.30749)

FLAG用局部重要性采样训练最大熵强化学习流策略；v2新增理论近似的实证检查并收窄性能主张。

## AcroRL: Learning Aggressive Quadrotor Inversion using Bidirectional Thrust

- [arXiv 2605.24301](https://arxiv.org/abs/2605.24301) · v2 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2605.24301)
- 收录历史: [2026-11-05 (v2, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2605.24301)

AcroRL学习双向推力四旋翼翻转的参考轨迹调制；v2扩展仿真可靠性报告并明确小规模真机证据。

## Learning Soft Robotic Dynamics with Active Exploration

- [arXiv 2510.27428](https://arxiv.org/abs/2510.27428) · v2 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2510.27428)
- 收录历史: [2026-11-05 (v2, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2510.27428)

SoftAE 通过不确定性驱动的乐观探索学习可复用的软体机器人动力学。本次修订新增软体与刚体接触实验及更强的探索/控制对照；原有跨平台验证和真机 2 毫米到达误差并非新增结果。

## MARLIN: Multi-Agent Reinforcement Learning Guided by Language-Based Inter-Robot Negotiation

- [arXiv 2410.14383](https://arxiv.org/abs/2410.14383) · v5 · [最新归档](../daily/2026-11-05.zh-CN.md#arxiv-2410.14383)
- 收录历史: [2026-11-05 (v5, revised)](../daily/2026-11-05.zh-CN.md#arxiv-2410.14383)

MARLIN 将 MAPPO 与机器人之间基于语言的两两协商结合。本次修订主要是方法表述和结论范围的更正，并非新增性能结果。

## GSBR: Geometric Support Behavior Regularization for Online RL

- [arXiv 2611.05295](https://arxiv.org/abs/2611.05295) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.05295)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.05295)

按动作偏离基础策略采样支撑集的距离惩罚，同时保留高价值模式。

## Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs

- [arXiv 2611.05249](https://arxiv.org/abs/2611.05249) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.05249)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.05249)

独立消融动作token监督与动作专家梯度耦合/隔离。

## CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation

- [arXiv 2611.05080](https://arxiv.org/abs/2611.05080) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.05080)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.05080)

评估非回合式VLA强化学习微调和针对性重置分配。

## LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation

- [arXiv 2611.04974](https://arxiv.org/abs/2611.04974) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04974)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04974)

ARPG按依赖关系构建MDP并局部验证，再模块化实现模拟器。

## Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training

- [arXiv 2611.04873](https://arxiv.org/abs/2611.04873) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04873)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04873)

替换行为克隆监督前审计想象轨迹奖励。

## PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations

- [arXiv 2611.04870](https://arxiv.org/abs/2611.04870) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04870)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04870)

多视角动作条件模拟器，采用快视频/慢记忆后训练。

## RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training

- [arXiv 2611.04368](https://arxiv.org/abs/2611.04368) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04368)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04368)

先用推理标注训练LoRA，再冻结适配器进行动作微调。

## Physical Experience Builds Continual Spatial World Models

- [arXiv 2611.04016](https://arxiv.org/abs/2611.04016) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.04016)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.04016)

跨回合空间变化记忆学习重复环境变换，同时保留可修正性。

## EvoMemState: Evolving Memory State for Personal Agents

- [arXiv 2611.03743](https://arxiv.org/abs/2611.03743) · v1 · [最新归档](../daily/2026-11-04.zh-CN.md#arxiv-2611.03743)
- 收录历史: [2026-11-04 (v1, new)](../daily/2026-11-04.zh-CN.md#arxiv-2611.03743)

在持久记忆中加入表示事实有效性、适用范围和冲突的关系状态，以及由强化学习生成的请求特定推理状态。

## D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models

- [arXiv 2611.03622](https://arxiv.org/abs/2611.03622) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03622)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03622)

通过提示让视觉语言模型先描述视频动态，再依据显式成功标准评估进度，无需训练奖励模型，可输出进度和语言反馈。

## Finite-Memory Control of POMDPs: Fundamental Limits and Efficient Design

- [arXiv 2611.03414](https://arxiv.org/abs/2611.03414) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03414)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03414)

RECAP按决策相关差异量化信念状态，并给出有限记忆POMDP控制损失的上下界。

## KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL

- [arXiv 2611.03138](https://arxiv.org/abs/2611.03138) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03138)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03138)

开源桌面对抗机器人平台，提供 Isaac Lab 数字孪生和学习式执行器模型。

## KlaskTron-IL: A Contact-Rich Adversarial Imitation Learning Benchmark with a Validated Sim-to-Real Bridge

- [arXiv 2611.03091](https://arxiv.org/abs/2611.03091) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03091)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03091)

为双人对抗真机平台提供分层模仿学习数据集与诊断基线。

## BeyondContact: A Reinforcement Learning Framework for Airflow-Based Non-Contact Manipulation

- [arXiv 2611.03059](https://arxiv.org/abs/2611.03059) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.03059)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.03059)

BeyondContact向Isaac Lab加入辨识气流物理，学习推吹混合及纯气流转向策略。

## A Universal Policy Wrapper With Guarantees

- [arXiv 2611.02888](https://arxiv.org/abs/2611.02888) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02888)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02888)

CALF-Wrapper利用已学习critic在预训练RL策略与备用控制器间选择，以继承目标到达保证。

## Beyond Policy Patches: Distilling RL Specialists into Vision-Language-Action Policies

- [arXiv 2611.02777](https://arxiv.org/abs/2611.02777) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02777)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02777)

REPAIR用价值加权专家动作分布与在线策略状态覆盖，将RL专家蒸馏进单一流匹配VLA。

## MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking

- [arXiv 2611.02613](https://arxiv.org/abs/2611.02613) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02613)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02613)

MAPO交替优化路由与专家，改善混合专家策略梯度中的散度估计。

## Sequential Recovery Updates for Learned Controllers under Successful-Trajectory Preservation

- [arXiv 2611.02555](https://arxiv.org/abs/2611.02555) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02555)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02555)

顺序恢复更新约束技能入口以保留既有成功轨迹，而不只冻结参数。

## Energy-Based Policy Orchestration

- [arXiv 2611.02546](https://arxiv.org/abs/2611.02546) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02546)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02546)

EPO用策略专属可行性与跟踪能量选择并细化策略—目标对；添加专家只需训练其能量模型。

## Iterative Gumbel Planning for Continuous Control

- [arXiv 2611.02236](https://arxiv.org/abs/2611.02236) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02236)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02236)

Iterative Gumbel Planning以分维度类别策略匹配有限动作搜索候选，并迭代执行Gumbel/MPPI式精修。

## Beyond Ensemble Disagreement: Predictive STL Monitoring of RL Locomotion under Distribution Shift

- [arXiv 2611.02218](https://arxiv.org/abs/2611.02218) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02218)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02218)

预测式STL监控检验世界模型rollout与集成分歧在运动分布偏移下能否增加安全排序价值。

## ANCHOR: KL-Anchored Adaptation for Stable Offline-to-Online RL

- [arXiv 2611.02177](https://arxiv.org/abs/2611.02177) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02177)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02177)

ANCHOR在不回放离线数据的离线转在线RL中，先以KL约束将actor锚定预训练策略，再逐步退火。

## GoalDex: Learning Image-Goal-Conditioned Policies for Dexterous In-Hand Manipulation

- [arXiv 2611.02171](https://arxiv.org/abs/2611.02171) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02171)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02171)

GoalDex把特权教师蒸馏为RGB/本体感知、图像目标条件灵巧重定向策略，无显式姿态估计。

## Value Forcing: Aligning Return Distributions at All Noise Levels

- [arXiv 2611.02160](https://arxiv.org/abs/2611.02160) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.02160)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.02160)

Value Forcing以流匹配学习回报分布，并在所有噪声层级施加Bellman一致性，形成VF和IVF。

## CompliantBot: Learning Whole-Body Compliance across Task Interfaces for Humanoid Control

- [arXiv 2611.01748](https://arxiv.org/abs/2611.01748) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01748)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01748)

CompliantBot通过交互力场与负载相关奖励权重训练全身顺应与任务恢复。

## Evolving Memory, Learning to Meta-Control: Test-Time Adaptation for Experience-augmented LLM Agents

- [arXiv 2611.01747](https://arxiv.org/abs/2611.01747) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01747)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01747)

OMCE同时演化经验记忆和在线上下文bandit控制器，在直接执行、回合经验、指导及蒸馏四种模式间选择。

## ODE Policy: Robot Learning via Action Dynamics, Not Actions

- [arXiv 2611.01729](https://arxiv.org/abs/2611.01729) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01729)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01729)

ODE Policy学习动作导数并从上一动作积分，面向模仿学习和RL连续控制。

## HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception

- [arXiv 2611.01659](https://arxiv.org/abs/2611.01659) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01659)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01659)

HuG耦合主动视点选择、全身抓取可供性与控制器在环可行性过滤。

## Recursive Self-Improvement of Exoskeleton Assistance Policies through Human-in-the-Loop Feedback

- [arXiv 2611.01581](https://arxiv.org/abs/2611.01581) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01581)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01581)

Agent依据主观反馈、运动结果和肌肉测量修订可执行外骨骼辅助代码。

## Beyond Validation Loss: Coverage and Reliability Dynamics in Robot Policy Pretraining

- [arXiv 2611.01565](https://arxiv.org/abs/2611.01565) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01565)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01565)

闭环pass@k区分单次可靠性与重复采样可达成功覆盖，用于策略预训练评估。

## Learning Agile Humanoid Dodgeball with Onboard Monocular Vision

- [arXiv 2611.01197](https://arxiv.org/abs/2611.01197) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01197)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01197)

单目人形躲避球系统将时序威胁估计与学习的躲避、恢复、目标重捕获策略组合。

## World Models Need Not Be Right to Rank Policies Right: Relative Bounds and Audit Limits

- [arXiv 2611.01139](https://arxiv.org/abs/2611.01139) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.01139)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.01139)

RAVEL区分世界模型内策略排序准确与成对真实环境审计是否提供有效信息。

## Toward Counterfactual Learning for Selective Re-Examination in Agentic Visual Search

- [arXiv 2611.00848](https://arxiv.org/abs/2611.00848) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00848)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00848)

CARE从同一视觉搜索状态的成对续程估计带成本反事实收益，将RL信用分配给提交/重看决策；ReSee标注额外观察价值。

## Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime

- [arXiv 2611.00522](https://arxiv.org/abs/2611.00522) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00522)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00522)

TinyLoRA通过GRPO或CMA-ES，仅用8–384个可训练参数调整冻结OpenVLA-OFT行为。

## Compositional Self-Improvement: Promises and Pitfalls

- [arXiv 2611.00452](https://arxiv.org/abs/2611.00452) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00452)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00452)

研究何时可组合简单子问题解答，为更难任务提供可靠自生成监督。

## OmniPiano: Diverse Dexterous Piano-Playing Challenges for Standard, Robust, Safe, and Multi-Agent RL

- [arXiv 2611.00243](https://arxiv.org/abs/2611.00243) · v1 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2611.00243)
- 收录历史: [2026-11-03 (v1, new)](../daily/2026-11-03.zh-CN.md#arxiv-2611.00243)

OmniPiano用1至5只Shadow Hand统一灵巧钢琴演奏的标准、鲁棒、安全及协作强化学习。

## RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent

- [arXiv 2610.21791](https://arxiv.org/abs/2610.21791) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2610.21791)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2610.21791)

RSIFlow依据执行反馈选择模型、Harness或产物干预，并更新元Harness。

## Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation

- [arXiv 2607.15880](https://arxiv.org/abs/2607.15880) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2607.15880)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2607.15880)

DAMI基于参考交互进行元模仿学习，适配新操作任务。

## Hyperagents

- [arXiv 2603.19461](https://arxiv.org/abs/2603.19461) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2603.19461)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2603.19461)

Hyperagents同时允许修改任务求解代码和生成修改的元agent。

## How to Peel with a Knife: Aligning Fine-Grained Manipulation with Human Preference

- [arXiv 2603.03280](https://arxiv.org/abs/2603.03280) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2603.03280)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2603.03280)

力感知模仿策略通过结合削皮厚度标签与专家偏好的奖励进一步优化。

## ReWorld: Multi-Dimensional Reward Modeling for Embodied Video Generation

- [arXiv 2601.12428](https://arxiv.org/abs/2601.12428) · v2 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2601.12428)
- 收录历史: [2026-11-03 (v2, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2601.12428)

ReWorld训练多维奖励模型，并用基于flow的PPO代理目标后训练具身视频生成器。

## InTAct: Interval-based Task Activation Consolidation for Continual Learning

- [arXiv 2511.17439](https://arxiv.org/abs/2511.17439) · v3 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2511.17439)
- 收录历史: [2026-11-03 (v3, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2511.17439)

InTAct保护旧域对应的激活区间，而非冻结参数或回放旧数据。

## Functional Critics for Off-Policy Actor-Critic: From Stability to Exploration

- [arXiv 2509.22964](https://arxiv.org/abs/2509.22964) · v5 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2509.22964)
- 收录历史: [2026-11-03 (v5, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2509.22964)

以策略为条件的函数型 critic 将离策略稳定性与策略空间探索联系起来。

## Tactile MNIST: Benchmarking Active Tactile Perception

- [arXiv 2506.06361](https://arxiv.org/abs/2506.06361) · v3 · [最新归档](../daily/2026-11-03.zh-CN.md#arxiv-2506.06361)
- 收录历史: [2026-11-03 (v3, revised)](../daily/2026-11-03.zh-CN.md#arxiv-2506.06361)

Tactile MNIST评估主动触觉感知与信息收集策略。

## Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments

- [arXiv 2610.42100](https://arxiv.org/abs/2610.42100) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.42100)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.42100)

研究观测／动作噪声与SAC可塑性干预的交互，区分渐进学习能力丧失和TD更新失稳。

## Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise Loco-Manipulation

- [arXiv 2610.41892](https://arxiv.org/abs/2610.41892) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41892)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41892)

污染高斯与随机特征GP学习冻结行走策略动力学。

## Continual Reinforcement Learning Is an Integration Problem

- [arXiv 2610.41809](https://arxiv.org/abs/2610.41809) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41809)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41809)

用十项系统要求组织持续强化学习，建议在同一持续生命周期内检验这些能力是否共存。

## ResMerge: Residual Policy Learning and Merging for Continual Adaptation of Pre-trained Robot Policies

- [arXiv 2610.41663](https://arxiv.org/abs/2610.41663) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41663)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41663)

残差RL适应冻结基座，一致性筛选可合并LoRA专家。

## KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents

- [arXiv 2610.41482](https://arxiv.org/abs/2610.41482) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41482)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41482)

在统一递归文本记忆接口中比较四种辅助监督目标，区分任务表现与记忆可靠性。

## HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos

- [arXiv 2610.41336](https://arxiv.org/abs/2610.41336) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41336)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41336)

利用对应特征与手物交互先验，从RGB-D示范学习物体中心灵巧技能。

## Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation

- [arXiv 2610.41320](https://arxiv.org/abs/2610.41320) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41320)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41320)

LEXP通过规划及带适用条件的交互经验调整冻结模型上下文，并非更新权重的强化学习。

## TalentRL: Strategy-Guided Reinforcement Learning for Hierarchical Skill Routing

- [arXiv 2610.41143](https://arxiv.org/abs/2610.41143) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41143)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41143)

高层策略指导技能检索，匹配干预轨迹区分路由与执行贡献。

## Before We Adapt: The Zero-Shot Generalization Bottleneck in Continual World Models

- [arXiv 2610.41041](https://arxiv.org/abs/2610.41041) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41041)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41041)

区分物理与行为上下文变化，在持续适应之前诊断世界模型零样本复用。

## Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning

- [arXiv 2610.41022](https://arxiv.org/abs/2610.41022) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41022)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41022)

在DreamerV3想象回报中加入密度代理驱动的硬/软bootstrap边界，不替换世界模型转移过程。

## STAR: Steering Action Representations during Inference

- [arXiv 2610.41009](https://arxiv.org/abs/2610.41009) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.41009)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.41009)

无需训练、单次前向地混合后层残差更新，由近期本体状态控制强度。

## Agentic World Modeling for Agent Test-time Scaling without Environment Replica

- [arXiv 2610.40927](https://arxiv.org/abs/2610.40927) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.40927)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.40927)

利用只读证据和可执行计算模拟假想观测，无需复制或修改共享环境。

## Frozen in Time: How a Physics Foundation Model Forgets Under Sim-to-Real Adaptation

- [arXiv 2610.40857](https://arxiv.org/abs/2610.40857) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.40857)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.40857)

研究Walrus-1.3B从PDE预训练转向圆柱流仿真及真实流体实验时的遗忘。

## CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

- [arXiv 2610.40799](https://arxiv.org/abs/2610.40799) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.40799)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.40799)

通过合成SFT与多轮RL训练4B代码策略机器人，利用特权物理状态评论家分配信用。

## AutoHebb: Self-Modifying Neural Networks that Zero-Shot Infer and Continually Learn

- [arXiv 2610.40757](https://arxiv.org/abs/2610.40757) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.40757)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.40757)

AutoHebb元学习固定权重，自主调节在线Hebbian可塑性，不依赖外部提供学习阶段信号。

## Certified Behavioral Retention for Continual Adaptation with Held-Out Anchors

- [arXiv 2610.40740](https://arxiv.org/abs/2610.40740) · v1 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.40740)
- 收录历史: [2026-11-02 (v1, new)](../daily/2026-11-02.zh-CN.md#arxiv-2610.40740)

CABA用保留历史锚点上的最坏前向KL筛选候选更新，选择满足行为保留预算的最大已测试插值步长。

## Do Earth-Trained Humanoid Controllers Walk on the Moon? Gravity, Terrain, and Soil Transfer

- [arXiv 2610.30080](https://arxiv.org/abs/2610.30080) · v2 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.30080)
- 收录历史: [2026-11-02 (v2, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2610.30080)

v2新增不使用土壤训练的重力随机化粗糙地形对照、跌倒时间分析，以及跨随机种子的结论审计，强化并收窄迁移结论。

## Learning from Fleet Experience: Collective Experience Learning Across 96 Robots

- [arXiv 2610.25736](https://arxiv.org/abs/2610.25736) · v3 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2610.25736)
- 收录历史: [2026-11-02 (v3, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2610.25736)

v3修正机器人群数据通路：在本地积累完整、经操作员标注的回合，再一次性传输；不再沿用v2所述的轨迹字段流式上传与云端复用推理观测。

## UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis

- [arXiv 2607.28198](https://arxiv.org/abs/2607.28198) · v3 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2607.28198)
- 收录历史: [2026-11-02 (v3, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2607.28198)

实质修订新增更困难的未见物体和未见目标定量测试，并以专家切换对照区分统一任务表述的技能兼容性与单策略蒸馏本身的收益。

## Cyclical Entropy Eruption: Entropy Dynamics of Agent Reinforcement Learning

- [arXiv 2605.27954](https://arxiv.org/abs/2605.27954) · v2 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2605.27954)
- 收录历史: [2026-11-02 (v2, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2605.27954)

v2新增SEAL表征分离辅助损失的多种子验证，用于稳定智能体强化学习；核心熵周期性喷发解释与原始基准表格已存在于v1。

## π-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs

- [arXiv 2603.02083](https://arxiv.org/abs/2603.02083) · v3 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2603.02083)
- 收录历史: [2026-11-02 (v3, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2603.02083)

实质修订：新增基于评论家时序信用信号的变体和CALVIN诊断，并以透明的共同测试变体协议，将广泛的分布外优势主张收窄为视觉扰动优势。

## Shared Modular Recurrence in Contextual MDPs for Universal Morphology Control

- [arXiv 2506.08630](https://arxiv.org/abs/2506.08630) · v4 · [最新归档](../daily/2026-11-02.zh-CN.md#arxiv-2506.08630)
- 收录历史: [2026-11-02 (v4, revised)](../daily/2026-11-02.zh-CN.md#arxiv-2506.08630)

v4新增对照，区分共享递归记忆与固定近期观测窗口、以及额外训练时间的作用，强化未见形态泛化的证据。

## world2vec: Mechanistic world models through latent dynamics learning

- [arXiv 2610.40637](https://arxiv.org/abs/2610.40637) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40637)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40637)

不使用奖励信息学习动作条件潜在动力学，目标是兼顾紧凑性和长期预测保真度。

## Gym-Anything for Robotics: Scaling physical simulations with digital agents

- [arXiv 2610.40565](https://arxiv.org/abs/2610.40565) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40565)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40565)

Gym-Anything 通过编码代理和对抗审计生成物理仿真与任务，用 Markdown 经验积累改进后续构建。RoboWorld 包含 25 仿真、25 测试任务和 175 训练环境，覆盖液体、布料和化学。

## Gaussian Distillation of Flow Policies

- [arXiv 2610.40271](https://arxiv.org/abs/2610.40271) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40271)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40271)

Gaussian Action Readout 冻结流策略骨干，将输出层改为高斯读出，获得单次前向采样和闭式似然。

## Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning

- [arXiv 2610.40130](https://arxiv.org/abs/2610.40130) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40130)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40130)

用分支感知图规划避免随机分支导致的离线虚假成功轨迹。

## Coupled Guidance for Flow Matching

- [arXiv 2610.40109](https://arxiv.org/abs/2610.40109) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40109)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40109)

Coupled Guidance 从训练耦合结构推导流匹配专用采样引导，而非直接移植扩散引导，避免破坏耦合稳定性。

## How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function

- [arXiv 2610.40002](https://arxiv.org/abs/2610.40002) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.40002)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.40002)

CoC-CFG 将推理条件与去推理条件之间的引导强度作为逐去噪步控制变量；固定专家和噪声后，通过完整 rollout 测得动作价值，训练小型保守引导 critic。

## Teaching a Tree to Recover: Online Distillation of an LLM Supervisor with Counterfactual Replay

- [arXiv 2610.39775](https://arxiv.org/abs/2610.39775) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39775)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39775)

将 LLM 恢复监督器在线蒸馏为决策树，利用回合反事实重放识别多余或有害干预并淘汰规则，使熟悉状态无需反复调用 LLM。

## From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models

- [arXiv 2610.39543](https://arxiv.org/abs/2610.39543) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39543)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39543)

CoRAct 将运动描述和未来路点变成动作对齐奖励；共享 Transformer 建模推理、动作及动作条件未来，并用组相对优化调整初始动作噪声，使执行符合预期后果。

## Before the Next Rollout: Diagnosing Skill Utility Shifts from Policy Updates

- [arXiv 2610.39358](https://arxiv.org/abs/2610.39358) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39358)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39358)

在已有上下文上读取策略变化，优先修订效用下降的技能。

## Event2Reward: Learning Robotic Rewards from Progress Relations

- [arXiv 2610.39212](https://arxiv.org/abs/2610.39212) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39212)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39212)

Event2Reward利用停滞、倒退、恢复的相对进度关系，防止奖励模型鼓励倒退，并用时间标签锚定总进度尺度。

## Generating Critic-Guided Synthetic Experience in Latent World Models

- [arXiv 2610.39100](https://arxiv.org/abs/2610.39100) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39100)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39100)

用 critic 改进的合成动作微调离线 flow actor，冻结 LeWM 动力学与 critic。存储单步转移，但生成可串联至 40 个模型步。

## Robotic Data Inoculation

- [arXiv 2610.39054](https://arxiv.org/abs/2610.39054) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39054)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39054)

Data Inoculation在人类遥操作中学习残差扰动，使人类纠正覆盖未来策略可能访问的偏离状态。

## Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand

- [arXiv 2610.39044](https://arxiv.org/abs/2610.39044) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.39044)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.39044)

Catch It All通过抓取奖励及安全课程在仿真学习视觉灵巧接物，免真机策略微调部署。

## Force-Driven Hook Disassembly via Constraint-Aware Object-Centric Reinforcement Learning

- [arXiv 2610.38513](https://arxiv.org/abs/2610.38513) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38513)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38513)

与机器人无关的物体中心RL策略结合力历史及粒子滤波信念，推断隐藏卡钩约束的可行拔出方向。

## SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control

- [arXiv 2610.38508](https://arxiv.org/abs/2610.38508) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38508)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38508)

SaiVLA-JEPA区分当前预测编码器特征的收益与未来潜变量训练的收益，并分别审计上下文适配与参数更新。

## ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation

- [arXiv 2610.38388](https://arxiv.org/abs/2610.38388) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38388)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38388)

ELEVATE在任务程序持续失败后让编码智能体训练缺失控制器、验证并加入技能库，扩展动作能力而非在固定工具上反复规划。

## CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization

- [arXiv 2610.38357](https://arxiv.org/abs/2610.38357) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38357)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38357)

CSO两阶段后训练离散技能策略：先用成功在线轨迹对齐技能分布，再冻结观察编码器进行技能粒度裁剪比率优化。

## Recursive Self-Improvement in Physical AI: Mechanisms, Evidence, and Evaluation

- [arXiv 2610.38266](https://arxiv.org/abs/2610.38266) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38266)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38266)

综述区分学习者能力改善与继承改进流程；L0–L3框架分别对应任务内适配、持久能力、流程修订继承及验证过的改进器收益。

## ParaTTT: Parallelizing Test-Time Training Layers with Deep Memories

- [arXiv 2610.38255](https://arxiv.org/abs/2610.38255) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38255)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38255)

通过迭代细化在线梯度轨迹，并行计算非线性神经记忆。

## Learning from Relative Action Credit for Escaping Local Minima

- [arXiv 2610.38034](https://arxiv.org/abs/2610.38034) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.38034)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.38034)

相对动作信用在 PPO 中加入动作条件 critic，比较同一状态下执行动作与替代动作，以突破局部解平台。

## Echo: Scaling Visual Reinforcement Learning with Off-policy Experience

- [arXiv 2610.37865](https://arxiv.org/abs/2610.37865) · v1 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2610.37865)
- 收录历史: [2026-10-30 (v1, new)](../daily/2026-10-30.zh-CN.md#arxiv-2610.37865)

Echo 让状态辅助策略模仿视觉策略并采集无需渲染的离策略经验，共享特权critic以降低视觉RL成本。

## VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon

- [arXiv 2607.01804](https://arxiv.org/abs/2607.01804) · v2 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2607.01804)
- 收录历史: [2026-10-30 (v2, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2607.01804)

VLA-Corrector 用学习到的潜在动力学监测、事件触发动作块截断及恢复方向梯度引导，在不更新 VLA 主干的情况下纠偏。本次修订新增部署开销核算和异步、近似匹配调用预算的 RTC 对比。

## GUI-AC: Enhancing Continual Learning in GUI Agents

- [arXiv 2606.10522](https://arxiv.org/abs/2606.10522) · v3 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2606.10522)
- 收录历史: [2026-10-30 (v3, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2606.10522)

GUI-AC 针对界面领域及分辨率变化，通过逐轨迹优势与裁剪更新实现持续定位学习。 v2 对低确定性组整体降权；v3 仅放大高概率失败的负优势，仅对低概率正优势探索放宽上裁剪界，下界固定；概率比改用旧采样策略而非参考策略。

## Train the Agent, Not the Expert: Learning to Harness Heterogeneous Experts for Multi-Turn Visual Reasoning

- [arXiv 2605.29894](https://arxiv.org/abs/2605.29894) · v2 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2605.29894)
- 收录历史: [2026-10-30 (v2, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2605.29894)

VisHarness v2 补充 RL-only、视觉记忆归档和交互轮数消融，并修订训练智能体调用固定视觉专家的评估。

## Latent Policy Steering through One-Step Flow Policies

- [arXiv 2603.05296](https://arxiv.org/abs/2603.05296) · v3 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2603.05296)
- 收录历史: [2026-10-30 (v3, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2603.05296)

LPS 利用动作空间 Q 梯度引导单步 MeanFlow 先验。v3 修订离线到在线学习的解释及详细成绩，并移除辅助 LPSD 蒸馏附录。

## Combining Constrained Sampling and Reinforcement Learning for Manipulation

- [arXiv 2602.08557](https://arxiv.org/abs/2602.08557) · v3 · [最新归档](../daily/2026-10-30.zh-CN.md#arxiv-2602.08557)
- 收录历史: [2026-10-30 (v3, revised)](../daily/2026-10-30.zh-CN.md#arxiv-2602.08557)

用约束采样提供接触可行的重置与目标状态，辅助目标条件 RL。v3 扩展到 Allegro 手内及倒置操作，并更新训练设置及方块任务结果。

## Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well

- [arXiv 2610.37652](https://arxiv.org/abs/2610.37652) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37652)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37652)

仿真训练LEAP手内位姿到达策略，采用多样抓取重置与摩擦课程，并叠加可调学习式残差安全滤波器。

## When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies

- [arXiv 2610.37547](https://arxiv.org/abs/2610.37547) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37547)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37547)

人工时机与纠正几何约束冻结ACT外围残差RL，针对局部精度修复。

## Predict the Swing, Match the Speed: Robotic Pipe Stabbing With Learned Stereo Vision and Residual Reinforcement Learning

- [arXiv 2610.37535](https://arxiv.org/abs/2610.37535) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37535)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37535)

StabBot结合双目摆动估计、速度匹配截获与残差RL处理悬挂管件插入。

## Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling

- [arXiv 2610.37393](https://arxiv.org/abs/2610.37393) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37393)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37393)

迭代质量重标注改善成功轨迹质量与真机吞吐量，但须保留在线数据成本与条件指标限制。

## VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning

- [arXiv 2610.37378](https://arxiv.org/abs/2610.37378) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.37378)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.37378)

仿真训练RL执行层改善冻结VLA避障，但依赖结构化感知且真机仍有碰撞。

## Vision-Language Agents Can Learn in Their Own Latent Worlds

- [arXiv 2610.36925](https://arxiv.org/abs/2610.36925) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36925)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36925)

冻结VLM内部的潜在世界模型策略改进，证据来自仿真交互Agent。

## When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate

- [arXiv 2610.36852](https://arxiv.org/abs/2610.36852) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36852)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36852)

结构化传感器诊断改善仿真修复，但干净预测拟合不等于有效修复。

## When the Critic Falls Behind: Co-Evolving Rubrics and Harnesses for Continual Agent Self-Improvement

- [arXiv 2610.36826](https://arxiv.org/abs/2610.36826) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36826)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36826)

RuHarness 在固定任务目标下共同演化诊断 rubric 与可执行 harness。

## Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time Training

- [arXiv 2610.36794](https://arxiv.org/abs/2610.36794) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36794)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36794)

Select-TTT 用冻结语言模型输出头评估查询相关性，重加权原位 fast-weight 更新，不增加参数。

## GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers

- [arXiv 2610.36507](https://arxiv.org/abs/2610.36507) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36507)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36507)

几何感知残差适应保持全身基础跟踪器冻结，学习地形执行，再将特权地形观测蒸馏为机载深度适配器。

## CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning

- [arXiv 2610.36469](https://arxiv.org/abs/2610.36469) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36469)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36469)

CoHARL 在固定评估器和动作族下共同训练共享策略并演化可执行 harness 种群。

## Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning

- [arXiv 2610.36309](https://arxiv.org/abs/2610.36309) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36309)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36309)

分析将PPO高斯探索方差塌缩与尖锐/低秩损失几何及可塑性丧失联系，并用方差重置改善适应。

## Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization

- [arXiv 2610.36270](https://arxiv.org/abs/2610.36270) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36270)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36270)

通过阶段条件critic、阶段门控奖励和多阶段重置，在无需人类动作示范的条件下训练统一移动操作策略。

## Rollback: Experience Backtracking in World Models for Policy Improvement

- [arXiv 2610.36068](https://arxiv.org/abs/2610.36068) · v1 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.36068)
- 收录历史: [2026-10-28 (v1, new)](../daily/2026-10-28.zh-CN.md#arxiv-2610.36068)

世界模型反事实树搜索改善三项真机单任务策略。

## Where Small Mistakes Matter: Quantifying State Criticality for Imitation Learning

- [arXiv 2610.17709](https://arxiv.org/abs/2610.17709) · v2 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2610.17709)
- 收录历史: [2026-10-28 (v2, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2610.17709)

v1→v2补充性能差距推导、状态关键性基线定义及真机对抗残差学习实现细节。

## When Does Test-Time Physical Diagnosis Pay?

- [arXiv 2609.22299](https://arxiv.org/abs/2609.22299) · v2 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2609.22299)
- 收录历史: [2026-10-28 (v2, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2609.22299)

v1→v2重新定位迁移失败原因：完整轨迹部署输入超出冻结解码器训练范围，使其输出塌缩为常数答案。

## RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models

- [arXiv 2605.09410](https://arxiv.org/abs/2605.09410) · v2 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2605.09410)
- 收录历史: [2026-10-28 (v2, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2605.09410)

v1→v2扩充恢复数据因果混淆分析、等预算价值监督对照，以及真机盲测扰动协议。

## TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration

- [arXiv 2512.15773](https://arxiv.org/abs/2512.15773) · v2 · [最新归档](../daily/2026-10-28.zh-CN.md#arxiv-2512.15773)
- 收录历史: [2026-10-28 (v2, revised)](../daily/2026-10-28.zh-CN.md#arxiv-2512.15773)

实质性v2新增实时操作与保真证据，并明确区分NFE计量和实测时延。

## Learning Force-Reactive Humanoid Loco-Manipulation

- [arXiv 2610.35862](https://arxiv.org/abs/2610.35862) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35862)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35862)

采集无需机器人参与的力感知示范，将扩散位姿/力策略与混合柔顺全身控制结合。 任务及试次数较少，并依赖力传感硬件；消融不能证明任意接触技能迁移。

## Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation

- [arXiv 2610.35636](https://arxiv.org/abs/2610.35636) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35636)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35636)

OpTTA以已观测转移预测损失加规划候选轨迹的乐观到达目标代价适配潜在世界模型，不增加交互。 仅模拟推物、到达和导航；每任务重置适配、最多30次重规划。LeWM TwoRoom可能下降。是面向规划的参数适配，尚非持续学习或真机能力证据。

## JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies

- [arXiv 2610.35010](https://arxiv.org/abs/2610.35010) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.35010)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.35010)

冻结基础策略，学习79,817参数条件能量；能量值排序离散候选，动作梯度修正连续输出。各基准独立训练适配器权重及编码。 仅仿真，无匹配LoRA对照。成功次数是五种子均值取整，并非原始独立试验计数。增益依赖反馈/专家监督与逐基准验证；小适配器参数不含冻结策略推理及rollout成本。

## PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds

- [arXiv 2610.34921](https://arxiv.org/abs/2610.34921) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34921)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34921)

共享VLM提出可执行物理场景并解题；固定模拟器验证场景、运行配对物体移除干预并绑定答案，避免提议者自行标注任务。 仅问答而非机器人控制；各配置单次训练、四张GPU，并使用24个人工示范程序。分支消融同时去除任务族且改变保留rollout数（8,668对7,960），未在等曝光条件下隔离分支执行。广域迁移收益较小且不均。

## HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model

- [arXiv 2610.34126](https://arxiv.org/abs/2610.34126) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.34126)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.34126)

以历史本体状态及正运动学监督学习神经动力学，再通过模型梯度微调人形跟踪策略；低频参考扰动用于可部署数据采集。 真机重复次数少，使用任务专属跟踪/完成指标，而非广泛操作成功率。真机基线为直接迁移和可建模情况下的扰动PPO，不包含全部仿真对照。作者将适用范围限为时不变扰动设置；需先采集和训练再部署适配策略。

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

## HA-DiPO: Diffusion Policy Optimization for Heterogeneous Cooperative Transport

- [arXiv 2610.33584](https://arxiv.org/abs/2610.33584) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33584)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33584)

以集中训练、分散执行训练分层多智能体扩散策略，实现协同载荷运输。 93.5%来自仿真而非真机成功率；最佳检查点选择与特定运输控制器限制结论范围。

## Distilling Dense Trajectory Teachers For Large-Motion Video World Models

- [arXiv 2610.33566](https://arxiv.org/abs/2610.33566) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33566)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33566)

DTTD插值稀疏相机路径，以冻结基础模型在密集路径生成的视频作位姿对齐教师，再结合教师/几何奖励构建离线Flow-DPO偏好及累进运动课程。 仅相机条件Wan1.3B骨干与单室内数据集，无机器人规划/控制结果。10k偏好对、每条件12个学生候选和4个教师视频，各40去噪步；等优化步不等于等数据生成算力。几何奖励依赖估计深度/位姿，也并非所有几何指标最优。

## RBGA: Residual-Budget Guide Arbitration for Offline-to-Online Safe Reinforcement Learning in Dexterous Manipulation

- [arXiv 2610.33494](https://arxiv.org/abs/2610.33494) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33494)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33494)

依据剩余回合安全预算与代价到达估计，在离线引导和在线探索之间仲裁。 实验将二值代价改为连续代价；理论界依赖估计假设，硬件部分没有定量试验表。

## MDPO: Multi-constraint Dexterous Policy Optimization with Reinforcement Learning

- [arXiv 2610.33480](https://arxiv.org/abs/2610.33480) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33480)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33480)

将累计约束和逐状态约束分别投影，用于灵巧操作强化学习。 真机证据主要为定性展示，不等于定量验证真实安全保证；约束估计假设仍重要。

## Expert-Play Contouring Control: Faster-than-Demonstration Planning from Slow Expert and Fast Play

- [arXiv 2609.22798](https://arxiv.org/abs/2609.22798) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2609.22798)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2609.22798)

v1→v2补充大量实现/评测附录，实质限定超示范速度结论：摩擦扫描的重训练、仅成功样本的分阶段计时、控制器搜索预算及play混合来源。真机13秒对22秒例子在v1已存在。 该扫描不隔离单个固定模型的零样本鲁棒性；各方法成功子集不同会影响计时比较。本次未建立新增真机汇总成功结果，实体速度提升仍为示例rollout。

## Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL

- [arXiv 2608.12063](https://arxiv.org/abs/2608.12063) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2608.12063)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2608.12063)

v1→v2新增Q5/表2：将稀疏奖励离线到在线学习与FastTD3、IQL、Diffusion Policy直接复用SMPC代价或示范数据比较。原真机结果及稀疏奖励方法并非新增。 基线复用SMPC代价/数据，失败不能证明RL算法普遍较差；作者归因于代价不适配和缺少纠偏样本，并指出并行SMPC的DAgger成本过高。新增对比仅仿真。

## WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform

- [arXiv 2605.17912](https://arxiv.org/abs/2605.17912) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2605.17912)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2605.17912)

v1→v2新增真机触觉消融、详细RL/解码接口、统计不确定性和扩展真机任务文档；视触觉/RL/跨平台基准整体构想在v1已存在。 真机样本少、区间宽；各条件Wilson区间不是配对显著性检验。世界模型效用包含分别训练的解码器，不等于单独动力学精度；扩展定性任务不能算作新增定量榜单。

## RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data

- [arXiv 2605.13775](https://arxiv.org/abs/2605.13775) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2605.13775)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2605.13775)

v1→v2新增§5.5：将规划器—模拟器共同演化循环接入可输出动作的LingBot-VA及LIBERO环境反馈。这是新增低层控制扩展，原有生成式规划收益并非本次新结果。 新增扩展依赖外部仿真反馈，不同于内部监督的VLM–VGM设置；未真机部署。500张种子不代表总监督量或交互预算，该节未建立完整交互成本匹配。

## Does "Do Differentiable Simulators Give Better Policy Gradients?" Give Better Policy Gradients?

- [arXiv 2604.18161](https://arxiv.org/abs/2604.18161) · v2 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2604.18161)
- 收录历史: [2026-10-27 (v2, revised)](../daily/2026-10-27.zh-CN.md#arxiv-2604.18161)

v1→v2修正附录D中DDCG对AoBG检验统计量的维度精度分析及蒙特卡洛表，并明确该结论针对统计量精度而非优化性能。 这是线性高斯玩具统计量的修正，不能证明梯度估计误差或机器人学习性能具有相同尺度规律；已有优化/RL结果不能算新增证据。

## RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

- [arXiv 2610.32971](https://arxiv.org/abs/2610.32971) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32971)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32971)

统一17种鲁棒/安全RL算法及6种标准对照，提供可复用接口及含延迟、语义的单因素/组合部署扰动。 并非每算法运行每任务；保留各自原生预算，算法族混合均值会混入基础学习器强弱。π0.5实验仅单个微调模型的离线关节示范轨迹跟踪，不是闭环VLA成功率或真机验证。

## ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback

- [arXiv 2610.32966](https://arxiv.org/abs/2610.32966) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32966)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32966)

从单目视频直接生成G1参考运动，以跟踪器反馈构造偏好对后训练扩散生成器；自回归版本支持视频遥操作。 百分比为仿真参考运动跟踪率，不是真机任务完成率。未建模精细手部姿态；真机证据以定性示范为主，在线初始化约10秒。

## Regularised RL improves sim-to-real transfer

- [arXiv 2610.32855](https://arxiv.org/abs/2610.32855) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32855)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32855)

用缓慢更新参考策略把soft mellowmax扩展到连续控制actor–critic，检验正则化是否改善超越名义训练回报的sim2real鲁棒性。 回报不是成功率；仍需要域随机化，温度参数随任务变化。PPO/FastTD3因未通过预设仿真安全筛查而没有ANYmal扰动部署，空白不能算实测真机失败；MuJoCo调参预算不完全相等。

## $R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design

- [arXiv 2610.32439](https://arxiv.org/abs/2610.32439) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32439)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32439)

以5项精英奖励池协调Explorer、Guardian、Evolver三类LLM角色，动态分配候选预算进行奖励程序迭代搜索。 仅仿真与任务内奖励搜索，不是跨任务机器人技能积累。精英池单调性针对保留搜索分数，不保证未来策略持续提升；RL训练主导成本，同骨干不等于所有基线搜索/token预算相同。

## When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

- [arXiv 2610.32431](https://arxiv.org/abs/2610.32431) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32431)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32431)

MART-GRPO 用微调后冻结的VLM从完整rollout视频定位最后一个未恢复的可见错误，截断其后失败惩罚，同时保留成功轨迹项及原归一化；理想停止理论提供动机，但不认证实际回溯实现。 仅仿真；策略看单相机，VLM审查三视角，另需标注及VLM微调。边界使用完整未来轨迹，不一定满足理想停止条件；一项任务下降1.95个百分点，留出场景种子不等于独立训练种子。

## ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences

- [arXiv 2610.32222](https://arxiv.org/abs/2610.32222) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32222)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32222)

结合动作错配和视频错配偏好，训练无需奖励计算时参考视频的模型，联合评价视觉质量与动作跟随；构建AVM-Eval（67.2k对）和AVM-Pref（506.3k对）。 RL证据限于一个2B世界模型与AgiBotWorld，不是机器人任务成功率。未直接监督物理一致性，评分依赖VLM；奖励计算无需参考不等于数据构建无需参考，成对排序也不保证物理正确。

## Ψ-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model

- [arXiv 2610.32177](https://arxiv.org/abs/2610.32177) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32177)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32177)

统一token接口生成及理解文字、图像、几何和运动，通过自适应思维流选择中间表示；以GRPO在视觉问答上验证如何选择推理流。 这里的sim-to-real是已录机器人视频上的视觉问答，不是真机部署。光流和轨迹是代理动作而非执行器命令；未隔离统一能力训练时的正负迁移，物理控制仍属未来工作。

## Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion

- [arXiv 2610.32143](https://arxiv.org/abs/2610.32143) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32143)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32143)

把紧贴手部的手环穿戴建模为几何插入，结合逐指软插入门控和分阶段课程，通过紧凑几何观测接口迁移到双臂机器人。 手环预抓持、假手静止，真机约减半速度。没有力感知观测/目标，手指偏转不是安全指标；大幅组合姿态扰动使仿真成功降至26/50。

## DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

- [arXiv 2610.32093](https://arxiv.org/abs/2610.32093) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.32093)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.32093)

用特权状态、潜变量条件RL、逆向课程和成功门控多样性生成过滤后的示范，再训练视觉π0.5，部署的不是RL生成器。 依赖准确仿真、特权状态、状态重置和成功信号。真机仅4个简单桌面任务、较小迁移差距及1个训练种子；过大多样性会损害任务能力。

## SEVI: Safe Evidential Real-World Reinforcement Learning

- [arXiv 2610.31829](https://arxiv.org/abs/2610.31829) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31829)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31829)

证据式安全critic同时估计违规风险与认知不确定性，在在线RL中筛查动作并调用离线训练的恢复策略。 仅1项真机、2项仿真任务，无零违规形式保证。真机使用50条成功先验示范、200条恢复示范及验证集阈值；最终成功率与累计训练事件口径不同。

## PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer

- [arXiv 2610.31812](https://arxiv.org/abs/2610.31812) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31812)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31812)

联合学习潜在偏好空间和奖励先验，通过置信度加权最优传输生成目标任务伪偏好，在不新增目标任务人工标签下在线强化学习。 零样本指无需目标人工反馈，并非无目标交互或训练。真机样本少，要求源目标共享偏好维度；PEARL做了在线化与维度补齐，PrefFew处于有限源数据设置并使用100个目标标签。

## FLORA: An Open Model Suite for Scaling Robotics Data Engines

- [arXiv 2610.31779](https://arxiv.org/abs/2610.31779) · v1 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2610.31779)
- 收录历史: [2026-10-26 (v1, new)](../daily/2026-10-26.zh-CN.md#arxiv-2610.31779)

开放标注模型套件提供时序分段、动作意图描述及结果/稠密/规则奖励；分段与描述使用RL后训练，发布的奖励模型仅用SFT。 并非所有指标最优，各系统帧预算及算力不同。约125倍成本优势依赖假定GPU价格和建模吞吐，未含部署开销、生产GPU小时口径未核实，参考标注版本亦未完全匹配；这里未直接证明下游策略学习提升。

## Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning

- [arXiv 2608.24885](https://arxiv.org/abs/2608.24885) · v2 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2608.24885)
- 收录历史: [2026-10-26 (v2, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2608.24885)

WorldEcho以视觉筛查与末端轨迹对齐评估非专家动作跟随；WorldSync结合更广动作数据、动力学表征约束及干预效果监督。 主表微小门控差距仅为点估计，未证明显著；视觉筛查不保证完整性，人工核验每维仅15段。视频指标使用重建参考和独立生成批次；不同预训练语料及基线历史不能支持受控数据效率结论。

## WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time

- [arXiv 2607.06988](https://arxiv.org/abs/2607.06988) · v3 · [最新归档](../daily/2026-10-26.zh-CN.md#arxiv-2607.06988)
- 收录历史: [2026-10-26 (v3, revised)](../daily/2026-10-26.zh-CN.md#arxiv-2607.06988)

通过人类视频写入世界动作模型的快权重记忆，配对人类—机器人元训练学习视频到动作的迁移接口。 对照是同一WAM内的接口变体，而非原系统完整复现；新增接口实验仅一个任务。FastWAM证据是3.2秒、8帧预测的定性展示，不是闭环控制迁移；部分对照依赖预训练技能潜变量，元训练阶段直接插入并不具备该先验。

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

