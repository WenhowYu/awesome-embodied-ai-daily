# 操作与真实机器人迁移

[English](manipulation-transfer.md) | [简体中文](manipulation-transfer.zh-CN.md) | [所有主题](README.zh-CN.md)

46 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

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

