# Vision-language-action models

[English](vla.md) | [简体中文](vla.zh-CN.md) | [All topics](README.md)

45 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

## Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

- [arXiv 2610.31670](https://arxiv.org/abs/2610.31670) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31670)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31670)

A training-free CKNNA measure aligns sensory representations with DTW trajectory neighborhoods for offline policy/backbone screening. Real-robot r=.831 uses exploratory h=110; prespecified h=7 gives r=.429, p=.236. Correlation does not demonstrate training benefit or replace closed-loop testing.

## Progress Probes P²: Lightweight Runtime Monitoring for Vision-Language-Action Models

- [arXiv 2610.31613](https://arxiv.org/abs/2610.31613) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31613)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31613)

P² learns a linear progress readout from π0.5 activations using successful demonstrations, then detects execution that lags nominal progress. It needs neither an external foundation-model monitor nor failure examples for training. Only π0.5 is tested; subtle spills can evade detection. The all-task hardware table reports a 0.78 average, but its displayed six values average 0.72, requiring aggregation clarification. Latency excludes VLA inference. No official code link was located. “Unseen” means unseen to the probe training, not necessarily to the underlying fine-tuned VLA.

## Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models

- [arXiv 2610.31569](https://arxiv.org/abs/2610.31569) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31569)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31569)

Echo jointly denoises actions plus stop/failure signals. Structured attention and faster signal denoising let cleaner status estimates guide action generation. Success, failure and recovery trajectories supply supervision without frame-level progress labels. Real-world scores are not success rates. Action supervision and training budgets are matched, but Echo receives extra failure-status data. Cross-method comparisons focus on flower insertion with adapted protocols; two tasks have no failed evaluation episodes. Benefits from higher-level stopping or replanning integration remain untested. The three-second outcome-window F1 does not imply instantaneous failure detection; simulation status accuracy covers ongoing/success frames under a specified window, not general three-class failure detection.

## FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies

- [arXiv 2610.31427](https://arxiv.org/abs/2610.31427) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31427)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31427)

FastHarness schedules GPT-6 Astra reviews of a frozen π0.5 policy using persistent stage and failure memory. Familiar execution skips reviews; risky states and recovery receive closer supervision without additional model training. The 80% comparison baseline is borrowed from another report, with five cases per task and a different scene mix, not a matched rerun. Episodes share memory and are not independent; the first tower episode already has prior experience. Savings are descriptive within-chain changes, not an end-to-end A/B effect. Evaluation is simulation-only and includes missed failures. The 57.2% is the mean of per-task percentage reductions, not the change in aggregate mean tokens. Token counts include input, output and cached inputs; they are not monetary costs.

## FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models

- [arXiv 2610.31423](https://arxiv.org/abs/2610.31423) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31423)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31423)

Predicts future interaction intent from multimodal observations, state and action history to route global and wrist views in π0.5, using trajectory-derived weak labels. The real-robot gain is 13.3 percentage points. Cross-embodiment and diverse camera configurations remain untested; the added module requires training.

## Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

- [arXiv 2610.31166](https://arxiv.org/abs/2610.31166) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31166)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31166)

WholeBodyMem selects historical frames from SAM3 object events and supplies object spatiotemporal tokens and memory attention to a whole-body action expert. This is within-episode perceptual history, not cross-episode skill accumulation. Physical tests have only ten trials per task and no uniform-memory real-robot comparator. Missed SAM3 detections and tracking overhead remain limitations.

## UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry

- [arXiv 2610.30991](https://arxiv.org/abs/2610.30991) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30991)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30991)

Three experts jointly model future vision, 3D scene flow and actions under ten objectives; deployment requires no flow input. 58.9% is the best evaluation seed; 87.7% uses the best evaluated checkpoint. Real policies are task-specific and starts remain within demonstration coverage; flow pseudo-labels are noisy.

## TEAR: Task-Evidence Authority Routing for Robotic Manipulation

- [arXiv 2610.30819](https://arxiv.org/abs/2610.30819) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30819)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30819)

TEAR combines network measurements, CLIP task cues and recent robot state in a causal temporal router that allocates authority between human teleoperation and local VLA control. Real trials were supervised: four manual switches occurred across two episodes. Evidence covers two related tasks and synthetic network impairment, with separately trained routers. Offline handoff F1 is 0.308 but recall only 0.286, below the rule baseline's 0.429. No official code link was located.

## DRILL: Training World Models to Improve Policies, Not Predict Pixels

- [arXiv 2610.30814](https://arxiv.org/abs/2610.30814) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30814)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30814)

DRILL trains a world model for the policy improvement its imagined rollouts produce. A cheaper visitation/advantage/confidence-weighted surrogate and a bilevel meta-gradient variant target downstream return instead of pixel fidelity.

## When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies

- [arXiv 2610.30735](https://arxiv.org/abs/2610.30735) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30735)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30735)

Tests one Euler step using existing flow-matching checkpoints across six VLAs and a DiT, without additional one-step distillation. Similar aggregates do not establish per-task real-world equivalence: close-oven falls from 87% to 74%, and the physical evaluation cannot resolve its preregistered equivalence margins. Smaller models can degrade on long horizons; one-step RL updates are untested.

## SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation

- [arXiv 2610.30732](https://arxiv.org/abs/2610.30732) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30732)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30732)

SmolVLA-MoE adds token-routed sparse FFN experts and a shared expert to the action module while freezing the VLM. It reports 84.25% mean LIBERO success versus 82.75% for dense SmolVLA, with about 500M activated and 800M stored parameters.

## Co^2Gen: Collaboratively Generating Task Plans for Decentralized Multi-Robot and Human Collaboration

- [arXiv 2610.30671](https://arxiv.org/abs/2610.30671) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30671)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30671)

Generates conditional collaborative programs with multi-agent planning, then converts executions into data for decentralized SmolVLA training. The strongest result depends on mixed human single-arm data, so the entire pipeline is not human-free. Generated data alone retains execution bottlenecks. Two tasks and limited trials do not establish general cross-embodiment transfer.

## Self-Distilling Future Video Representations for World Action Models

- [arXiv 2610.30320](https://arxiv.org/abs/2610.30320) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30320)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30320)

Observation history and EMA self-distillation improve future representations from one video-denoising pass for an action decoder. Appendices allow partial credit, so scores are not uniformly binary full-task success. Transfer instruction following is zero without human videos; cross-embodiment correspondence is implicit.

## Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- [arXiv 2609.39304](https://arxiv.org/abs/2609.39304) · v4 · [Latest entry](../daily/2026-10-23.md#arxiv-2609.39304)
- Coverage history: [2026-10-23 (v4, revised)](../daily/2026-10-23.md#arxiv-2609.39304)

Scale and Selection evolves a visual-interface robot-agent harness with rollout scaling and champion–challenger acceptance. The revision adds a distillation loop that transfers harness-assisted experience into a standalone robot policy.

## FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence

- [arXiv 2609.17210](https://arxiv.org/abs/2609.17210) · v2 · [Latest entry](../daily/2026-10-23.md#arxiv-2609.17210)
- Coverage history: [2026-10-23 (v2, revised)](../daily/2026-10-23.md#arxiv-2609.17210)

FluxVLA standardizes policy data, training, evaluation and robot execution. Its expanded revision adds an RLinf online PPO frontend, wider simulation/real-robot integrations and paired post-training evidence, rather than introducing a new base policy.

## HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation

- [arXiv 2604.07993](https://arxiv.org/abs/2604.07993) · v3 · [Latest entry](../daily/2026-10-23.md#arxiv-2604.07993)
- Coverage history: [2026-10-23 (v3, revised)](../daily/2026-10-23.md#arxiv-2604.07993)

HEX combines canonical body-part states, a mixture-of-experts proprioceptive predictor, compact visual history and flow-matching actions for humanoid whole-body manipulation. This revision adds two household long-horizon tasks, a ψ0 comparison, OOD pretraining tests and data-scaling/sensitivity experiments.

## Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models

- [arXiv 2602.12628](https://arxiv.org/abs/2602.12628) · v5 · [Latest entry](../daily/2026-10-23.md#arxiv-2602.12628)
- Coverage history: [2026-10-23 (v5, revised)](../daily/2026-10-23.md#arxiv-2602.12628)

RL-Co combines sim/real supervised warm-starting with simulator RL anchored by real-data supervision. The new revision adds a stronger rollout-distillation control and makes the limited real-world statistical protocol explicit.

## Agentic World Action Models

- [arXiv 2610.30136](https://arxiv.org/abs/2610.30136) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30136)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30136)

Joint code–video–action denoising connects agent planning and control, but random-domain performance is weaker than π0.5 and the skill library remains frozen.

## AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

- [arXiv 2610.30097](https://arxiv.org/abs/2610.30097) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30097)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30097)

Atomic subtask credit assignment and bottleneck exploration improve long-horizon RL; the real-robot gain is 8.0 points over PPO, with training performed in reconstructed simulation.

## GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

- [arXiv 2610.29866](https://arxiv.org/abs/2610.29866) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29866)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29866)

Training-only geometry supervision and temporal memory improve a shared VLA backbone; benchmark-specific adaptation and episode resets bound the generalization and memory claims.

## From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

- [arXiv 2610.29560](https://arxiv.org/abs/2610.29560) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29560)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29560)

Offline harness revision raises RoboMME success from 44.38% to 51.38%; runtime context resets, and the reported repair does not establish new skill discovery.

## Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control

- [arXiv 2610.29329](https://arxiv.org/abs/2610.29329) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29329)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29329)

Executable, episode-local memory improves RoboMME performance, but unequal seeds and frame sampling limit the Astra+VLA comparison; cross-task skill growth is unproven.

## SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training

- [arXiv 2610.29161](https://arxiv.org/abs/2610.29161) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29161)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29161)

Automated intervention collection enables controlled VLA post-training comparisons; real-robot gains transfer an algorithmic change, not a simulation policy zero-shot.

## inr2action: Encoding Robot Episodes as Neural Implicit Representations for Recall and Action

- [arXiv 2610.28882](https://arxiv.org/abs/2610.28882) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28882)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28882)

Episode videos are stored as INR weight deltas; QA improves over chance, but offline action regression does not establish closed-loop control or scalable retrieval.

## Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration

- [arXiv 2610.28880](https://arxiv.org/abs/2610.28880) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28880)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28880)

Semantic 3D augmentation turns one human video into robot data with strong controlled gains, but teleoperation comparisons are unmatched and setup remains manual.

## T-WLA: Bridging Slow Vision and Fast Touch

- [arXiv 2610.28814](https://arxiv.org/abs/2610.28814) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28814)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28814)

A fast tactile editor corrects pending actions, but the no-touch variant nearly matches full performance, limiting how much gain can be attributed to touch.

## SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model

- [arXiv 2606.20698](https://arxiv.org/abs/2606.20698) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2606.20698)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2606.20698)

The revision validates safety-head calibration rather than changing headline success results; small Level II gains and proxy costs do not establish real-world safety.

## UniWALM: Unified World Action Language Model for Embodied Robot Control

- [arXiv 2610.28626](https://arxiv.org/abs/2610.28626) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28626)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28626)

Joint video, action, and language denoising feeds textual working memory back into control. Gains on memory tasks and 18 real-robot trials do not isolate memory from other components or establish cross-episode retrieval.

## AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- [arXiv 2610.28589](https://arxiv.org/abs/2610.28589) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28589)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28589)

A 9B robotic planner improves through successful-trajectory SFT and multi-turn RL with a frozen executor. LIBERO-PRO reaches 71.0%, but tasks overlap between training and testing and no real-robot result is reported.

## De-Diffusing WAMs: Action-Sufficient Direct Prediction for Robot Control

- [arXiv 2610.28122](https://arxiv.org/abs/2610.28122) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28122)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28122)

A frozen one-step action expert supervises direct future prediction through action error. DirectWAM achieves 97.1% on LIBERO and 85.4% on RoboTwin; the 28× speedup is model-side and teacher superiority is not established.

## PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations

- [arXiv 2610.28019](https://arxiv.org/abs/2610.28019) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28019)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28019)

Newer pre-commit observations verify speculative action chunks from a frozen flow policy. Real-robot success rises from 60% to 82%, with added latency and no calibrated safety guarantee.

## EventSync: Event-Driven Memory Updates for History-Dependent Manipulation

- [arXiv 2610.27917](https://arxiv.org/abs/2610.27917) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27917)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27917)

An event monitor commits task history only after visual and motion evidence confirms completion. RoboMME reaches 64.5%, but the monitor needs event supervision and the comparisons reuse published baselines.

## LaLa-World: Scaling Latent World Models with Natural Language Actions

- [arXiv 2610.27851](https://arxiv.org/abs/2610.27851) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27851)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27851)

Natural-language action representations unify latent world-model pretraining and joint action/future prediction. LIBERO reaches 97.7%; DROID action-prediction scores are not real-robot success rates.

## VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs

- [arXiv 2610.27698](https://arxiv.org/abs/2610.27698) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27698)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27698)

A paired benchmark measures target gains and cross-dimension retention after VLA vision tuning. Non-target averages decline in 8 of 10 settings; the study concerns targeted fine-tuning rather than online continual learning.

## DEFLECT: Temporal Counterfactual Preference Learning for Delay-Robust Asynchronous VLAs

- [arXiv 2605.19294](https://arxiv.org/abs/2605.19294) · v3 · [Latest entry](../daily/2026-10-21.md#arxiv-2605.19294)
- Coverage history: [2026-10-21 (v3, substantive-revision)](../daily/2026-10-21.md#arxiv-2605.19294)

The revision adds cross-backbone and continued-training controls for delay-robust VLA preference learning. GR00T reaches 73.10% at four-step delay, but protocol changes prevent direct headline comparisons to earlier versions.

## SteerAct: Unlocking Action Models through Few-Shot Temporal Steering

- [arXiv 2610.25632](https://arxiv.org/abs/2610.25632) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.25632)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.25632)

A per-task bank of 24 success/failure-labeled rollouts supplies temporal feature references. Online steering chooses intervention timing, direction, and strength while π0.5/Fast-WAM stay frozen. It does not update the main model weights at test time.

## SARAM: Sparse Adapter Allocation with Reuse and Merging for Lifelong Robot Learning

- [arXiv 2610.24804](https://arxiv.org/abs/2610.24804) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24804)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24804)

SARAM reuses old LoRA adapters, sparsely allocates new ones, and penalizes redundancy. It identifies the task at each episode start and merges the selected adapter into the backbone, providing a parameterized lifelong-learning approach.

## LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models

- [arXiv 2610.24587](https://arxiv.org/abs/2610.24587) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24587)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24587)

The benchmark evaluates 17 policies, including VLAs and WAMs, using 22 static perturbation types, 20 runtime interventions, and 1,648 valid task variants. It probes feedback use, recovery, and combined perturbations.

## LIBERO-Dynamic: Benchmarking Robotic Manipulation in Dynamic Environments

- [arXiv 2610.24579](https://arxiv.org/abs/2610.24579) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24579)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24579)

Forty LIBERO tasks receive three trajectory types at three speed levels, with physics advancing during inference according to measured latency. Six policies each face 1,800 dynamic conditions, supported by 9,000 dynamic demonstrations.

## Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems

- [arXiv 2610.23372](https://arxiv.org/abs/2610.23372) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.23372)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.23372)

Key-fact replacement, fact-preserving replacement, and numerical perturbation controls test whether robot systems causally use memory content, separating memory effects from general system sensitivity.

## LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence

- [arXiv 2610.23334](https://arxiv.org/abs/2610.23334) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.23334)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.23334)

Semantic subtask progress connects VLM planning, state assessment, and world-action-model action generation, with hierarchical visual memory and subtask value learning.

## NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models

- [arXiv 2610.23271](https://arxiv.org/abs/2610.23271) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.23271)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.23271)

Skills are trained separately and then a task-conditioned hypernetwork generates action-expert parameters, reducing conflicts from directly merging weights. This is a parameterized skill-consolidation approach.

## AnchorQ: Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors

- [arXiv 2610.22852](https://arxiv.org/abs/2610.22852) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22852)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22852)

Flow reversal maps rough reference actions to state-dependent noise anchors. Local particles and an online critic guide exploration while the base VLA remains frozen.

## Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations

- [arXiv 2610.22576](https://arxiv.org/abs/2610.22576) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22576)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22576)

An embodiment classifier is trained using successful rollouts from a small set of calibration tasks. Its gradients guide each π0 denoising step while the VLA stays frozen, connecting test-time action guidance with dynamics adaptation.

## When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

- [arXiv 2610.22556](https://arxiv.org/abs/2610.22556) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22556)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22556)

Disagreement between adjacent action chunks about the same future time supplies a memory-write signal. A bounded visual memory stores key frames and filters duplicates. Memory is cleared at the start of each episode, so this is within-episode memory.

