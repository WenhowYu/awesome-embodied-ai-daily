# 视觉—语言—动作模型

[English](vla.md) | [简体中文](vla.zh-CN.md) | [所有主题](README.zh-CN.md)

92 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。

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

## TurboWAM: Learning What Matters for Fast World Action Models

- [arXiv 2610.33941](https://arxiv.org/abs/2610.33941) · v1 · [最新归档](../daily/2026-10-27.zh-CN.md#arxiv-2610.33941)
- 收录历史: [2026-10-27 (v1, new)](../daily/2026-10-27.zh-CN.md#arxiv-2610.33941)

按带噪动作聚合世界模型前层表示，并在训练时调节动作梯度；保留视频联合训练而推理不生成未来视频。 各方法具身预训练不匹配；修正提示结果不可与原协议混为一谈。层结构指架构而非显式3D几何，延迟不等于安全控制。 GPU仅描述为约140GB数据中心卡、未指明型号。文中将真机实验指向补充材料，所核正文未建立其定量结果。

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

