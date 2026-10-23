# Evaluation, robustness, and safety

[English](evaluation.md) | [简体中文](evaluation.zh-CN.md) | [All topics](README.md)

42 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

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

## Skeleton-Grounded Latent Action Model for Robot World Models

- [arXiv 2610.31474](https://arxiv.org/abs/2610.31474) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31474)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31474)

Skeleton supervision separates kinematic and residual latent actions; swap reconstruction, branch dropout and an adapter enable action-conditioned video prediction. DROID prediction spans 0.8 seconds; valid-trajectory subsets differ. Human transfer comprises two generated-video examples. Policy evaluation has only nine real successes and cannot replace closed-loop validation.

## FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies

- [arXiv 2610.31427](https://arxiv.org/abs/2610.31427) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31427)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31427)

FastHarness schedules GPT-6 Astra reviews of a frozen π0.5 policy using persistent stage and failure memory. Familiar execution skips reviews; risky states and recovery receive closer supervision without additional model training. The 80% comparison baseline is borrowed from another report, with five cases per task and a different scene mix, not a matched rerun. Episodes share memory and are not independent; the first tower episode already has prior experience. Savings are descriptive within-chain changes, not an end-to-end A/B effect. Evaluation is simulation-only and includes missed failures. The 57.2% is the mean of per-task percentage reductions, not the change in aggregate mean tokens. Token counts include input, output and cached inputs; they are not monetary costs.

## Learning Robot Behavior Priors from Non-Robotic Synthetic Data

- [arXiv 2610.31275](https://arxiv.org/abs/2610.31275) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31275)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31275)

Pretrains a Transformer on procedural non-robotic MDP, contextual-bandit and linear-dynamical-system data, then predicts unseen robot actions from in-context examples. Evaluation is offline open-loop state-conditioned action prediction, not visual control or physical task success. “Zero-shot” still uses task-specific state-action examples as context.

## RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation

- [arXiv 2610.31121](https://arxiv.org/abs/2610.31121) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31121)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31121)

Temporal scene graphs compare generated/reference objects, relation changes and 3D paths; introduces the 1,000-scene ShareRobot-SG dataset. Correlation across only three generator means does not establish per-video reliability; object F1 trails SG-Ego. Single-reference/object assumptions and extraction errors can penalize valid alternatives; executable actions are not certified.

## TEAR: Task-Evidence Authority Routing for Robotic Manipulation

- [arXiv 2610.30819](https://arxiv.org/abs/2610.30819) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30819)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30819)

TEAR combines network measurements, CLIP task cues and recent robot state in a causal temporal router that allocates authority between human teleoperation and local VLA control. Real trials were supervised: four manual switches occurred across two episodes. Evidence covers two related tasks and synthetic network impairment, with separately trained routers. Offline handoff F1 is 0.308 but recall only 0.286, below the rule baseline's 0.429. No official code link was located.

## When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies

- [arXiv 2610.30735](https://arxiv.org/abs/2610.30735) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30735)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30735)

Tests one Euler step using existing flow-matching checkpoints across six VLAs and a DiT, without additional one-step distillation. Similar aggregates do not establish per-task real-world equivalence: close-oven falls from 87% to 74%, and the physical evaluation cannot resolve its preregistered equivalence margins. Smaller models can degrade on long horizons; one-step RL updates are untested.

## Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation

- [arXiv 2610.30643](https://arxiv.org/abs/2610.30643) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30643)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30643)

FETA makes test-time navigation updates from one binary feedback label on a selected action. It selects unstable trajectories, locates high entropy-gradient steps, and weights updates by policy–feedback disagreement.

## Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents

- [arXiv 2610.30587](https://arxiv.org/abs/2610.30587) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30587)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30587)

CARE uses a critic to transfer execution from a local model to a stronger cloud model, retains cloud control through recovery, and shares persistent handoff memory across executors. These are simulated decision-layer results, not physical robot response times. Local execution and criticism run on H200 GPUs. Thresholds are benchmark-tuned, and cloud-request ratios exclude critic calls. Network variability, sensing noise and hardware failures remain untested; no official code link was located. On EmbodiedBench, CARE remains below cloud-only success (75% versus 80%); the cloud-request ratio is not total compute cost.

## Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live

- [arXiv 2610.30478](https://arxiv.org/abs/2610.30478) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30478)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30478)

A preregistered study compares LoRA consolidation with inference-time retrieval of visual episodic lessons. Its cleanest comparison toggles a frozen memory buffer while keeping policy weights fixed. The distillation null is underpowered, not evidence that parametric memory cannot work. Scope is narrow; retrieval combines text and images, and reset/logging defects require sensitivity analyses. The public repository is verified, but its claimed artifact release was absent when checked.

## Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation

- [arXiv 2610.30197](https://arxiv.org/abs/2610.30197) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30197)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30197)

Injects faults at perception, actuation, kinematics and serialization boundaries, using a seed-matched scripted oracle to localize failures. Only one tabletop task and one model are tested, with five trials per fault-intensity cell. Realized perception lag saturates at 0.5s. Results do not establish general absence of reasoning deficits or real-robot safety.

## The Bitter Lesson Comes to Robotics

- [arXiv 2610.25287](https://arxiv.org/abs/2610.25287) · v2 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.25287)
- Coverage history: [2026-10-23 (v2, revised)](../daily/2026-10-23.md#arxiv-2610.25287)

The Bitter Lesson Comes to Robotics compares frontier language models directly controlling physical YAM arms under a 40-action budget. The revision expands seven models/twelve settings to nine models/fifteen settings and updates the historical performance fit.

## Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- [arXiv 2609.39304](https://arxiv.org/abs/2609.39304) · v4 · [Latest entry](../daily/2026-10-23.md#arxiv-2609.39304)
- Coverage history: [2026-10-23 (v4, revised)](../daily/2026-10-23.md#arxiv-2609.39304)

Scale and Selection evolves a visual-interface robot-agent harness with rollout scaling and champion–challenger acceptance. The revision adds a distillation loop that transfers harness-assisted experience into a standalone robot policy.

## From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks

- [arXiv 2610.30051](https://arxiv.org/abs/2610.30051) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30051)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30051)

A tool-based LIBERO-10 benchmark measures frontier models without manipulation pretraining; a 44/100 versus 43/100 result is too close for a robust ranking.

## From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

- [arXiv 2610.29560](https://arxiv.org/abs/2610.29560) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29560)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29560)

Offline harness revision raises RoboMME success from 44.38% to 51.38%; runtime context resets, and the reported repair does not establish new skill discovery.

## How Representational Priors Shape Generalization in World Action Models

- [arXiv 2610.29168](https://arxiv.org/abs/2610.29168) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29168)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29168)

Representation geometry correlates with WAM robustness across backbones, but unmatched pretraining and architectures prevent a causal interpretation.

## SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training

- [arXiv 2610.29161](https://arxiv.org/abs/2610.29161) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29161)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29161)

Automated intervention collection enables controlled VLA post-training comparisons; real-robot gains transfer an algorithmic change, not a simulation policy zero-shot.

## SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model

- [arXiv 2606.20698](https://arxiv.org/abs/2606.20698) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2606.20698)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2606.20698)

The revision validates safety-head calibration rather than changing headline success results; small Level II gains and proxy costs do not establish real-world safety.

## μ0: A Scalable 3D Interaction-Trace World Model

- [arXiv 2606.13769](https://arxiv.org/abs/2606.13769) · v3 · [Latest entry](../daily/2026-10-22.md#arxiv-2606.13769)
- Coverage history: [2026-10-22 (v3, revised)](../daily/2026-10-22.md#arxiv-2606.13769)

Version 3 exposes weak long-horizon completion and greater action-chunk latency than π0.5; unchanged atomic-task scores should not be mistaken for compositional progress.

## Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

- [arXiv 2610.28613](https://arxiv.org/abs/2610.28613) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28613)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28613)

A vision-tactile world model supports evaluation and policy post-training. Mean real-robot success reaches 70.8% from a 59.1% SFT baseline on four ARX tasks, with one task below SFT.

## PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations

- [arXiv 2610.28019](https://arxiv.org/abs/2610.28019) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28019)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28019)

Newer pre-commit observations verify speculative action chunks from a frozen flow policy. Real-robot success rises from 60% to 82%, with added latency and no calibrated safety guarantee.

## When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines

- [arXiv 2610.27714](https://arxiv.org/abs/2610.27714) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27714)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27714)

Resampled experience pools and token-matched controls reveal fragile memory gains in a driving agent. Conclusions are limited to HighwayEnv, gpt-4o-mini, and 1 Hz, rather than all long-term memory.

## VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs

- [arXiv 2610.27698](https://arxiv.org/abs/2610.27698) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27698)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27698)

A paired benchmark measures target gains and cross-dimension retention after VLA vision tuning. Non-target averages decline in 8 of 10 settings; the study concerns targeted fine-tuning rather than online continual learning.

## More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents

- [arXiv 2610.27406](https://arxiv.org/abs/2610.27406) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27406)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27406)

Rebuilding and discarding task abstractions can reduce error reproduction while preserving raw experience. Three-seed ALFWorld gains are agent-specific and do not establish that all persistent memory is harmful.

## Training Controllable World Models via Action Influence Maximization

- [arXiv 2610.27387](https://arxiv.org/abs/2610.27387) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27387)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27387)

Action-influence objectives guide active data collection for controllable world models. A Push-T controllability result yields an 85× data-volume ratio, with evidence limited to two simulated environments.

## SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents

- [arXiv 2610.26995](https://arxiv.org/abs/2610.26995) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.26995)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.26995)

Skill-DAG memory and state-conditioned Skill-GNN selection reuse successful skill compositions. ALFWorld reaches 87.1%, but the work does not establish new motor-skill acquisition or real-robot transfer.

## PrismWAM: Decoupling State Representations in World Action Models

- [arXiv 2610.26564](https://arxiv.org/abs/2610.26564) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.26564)
- Coverage history: [2026-10-21 (v1, supplemental-previous-batch)](../daily/2026-10-21.md#arxiv-2610.26564)

Supplemental review of a 2026-10-20 announcement: RGB goals, depth futures, and actions are decoupled. Base RoboTwin C2R reaches 70.57%; real deployment requires RGB-D, and the 15B result uses additional pretraining.

## HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents

- [arXiv 2610.23479](https://arxiv.org/abs/2610.23479) · v2 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.23479)
- Coverage history: [2026-10-21 (v2, substantive-revision)](../daily/2026-10-21.md#arxiv-2610.23479)

A substantive revision adds official hidden-seed evaluation on 42 RoboDojo tasks. The 46.9% success rate uses a different protocol from v1; released tools do not include the entire evaluation system.

## WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning

- [arXiv 2607.18840](https://arxiv.org/abs/2607.18840) · v3 · [Latest entry](../daily/2026-10-21.md#arxiv-2607.18840)
- Coverage history: [2026-10-21 (v3, numerical-revision)](../daily/2026-10-21.md#arxiv-2607.18840)

Corrected C2R ablations reduce the marginal long-term-memory gain from 3.42 to 0.67 percentage points. Architecture, main results, and real-robot results are unchanged, and the correction is unexplained.

## DEFLECT: Temporal Counterfactual Preference Learning for Delay-Robust Asynchronous VLAs

- [arXiv 2605.19294](https://arxiv.org/abs/2605.19294) · v3 · [Latest entry](../daily/2026-10-21.md#arxiv-2605.19294)
- Coverage history: [2026-10-21 (v3, substantive-revision)](../daily/2026-10-21.md#arxiv-2605.19294)

The revision adds cross-backbone and continued-training controls for delay-robust VLA preference learning. GR00T reaches 73.10% at four-step delay, but protocol changes prevent direct headline comparisons to earlier versions.

## Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy

- [arXiv 2610.26848](https://arxiv.org/abs/2610.26848) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.26848)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.26848)

The study measures initial capability, improvement rate, success, and recovery separately over 18 RoboDojo tasks and up to 17 interaction rounds. History and workspace ablations probe which retained experience supports improvement.

## GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation

- [arXiv 2610.26846](https://arxiv.org/abs/2610.26846) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.26846)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.26846)

Tactile RGB images are supplied through a visual interface for contact-rich manipulation, together with few-shot demonstrations and interaction memory.

## RoboValue: A Fine-Grained Sim-and-Real Benchmark for Unified Evaluation of Robotic Value Models

- [arXiv 2610.26663](https://arxiv.org/abs/2610.26663) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.26663)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.26663)

RoboValue evaluates robotic value models on task state, progress, failure recovery, and value consistency using 15 simulated and 20 real tasks, beyond binary success/failure classification.

## Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds

- [arXiv 2610.25114](https://arxiv.org/abs/2610.25114) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.25114)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.25114)

A strong model writes, repairs, and freezes skills offline for execution by code or a cheaper model. The work studies executable experience, validation, inheritance, and deployment cost.

## DialogMem: Evaluating Dialogue-Grounded Embodied Memory in 3D Environments

- [arXiv 2610.24767](https://arxiv.org/abs/2610.24767) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24767)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24767)

RGB-D, poses, and human dialogue are written to memory for instance navigation and question answering across 142 episodes, 27 scanned scenes, and nine memory representations. The diagnostic separates grounding, retrieval, and action localization.

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

## Spatial Memory by Agents, for Agents

- [arXiv 2610.22736](https://arxiv.org/abs/2610.22736) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22736)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22736)

A Designer Agent iterates memory construction and retrieval programs using feedback from a fixed Query Agent, then freezes the implementation for held-out observation histories. The tasks concern spatial/temporal questions, localization, and navigation queries, rather than continual manipulation-skill learning.

## When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

- [arXiv 2610.22556](https://arxiv.org/abs/2610.22556) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22556)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22556)

Disagreement between adjacent action chunks about the same future time supplies a memory-write signal. A bounded visual memory stores key frames and filters duplicates. Memory is cleared at the start of each episode, so this is within-episode memory.

