# Evaluation, robustness, and safety

[English](evaluation.md) | [简体中文](evaluation.zh-CN.md) | [All topics](README.md)

132 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

## Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy

- [arXiv 2610.35832](https://arxiv.org/abs/2610.35832) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35832)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35832)

EBench profiles Astra direct waypoint control versus selective invocation of frozen VLA/WAM policies under RGB/proprioceptive observations and one annotated demonstration per task. No cross-episode memory. 31/510 episodes use a demonstration from the same test scene. Two tasks allow 3,000 steps direct versus 5,000 hybrid; correcting that changes hybrid means to 52.4%/55.8%. Policy calls cannot receive agent-written subgoals; compute is unbounded and comparisons run once/episode.

## SPECOLA: A Tool for Specification Driven Robot Evaluation

- [arXiv 2610.35730](https://arxiv.org/abs/2610.35730) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35730)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35730)

Specola exposes simulator signals to Signal Temporal Logic monitors, measuring satisfaction margins and persistence alongside task success; provides APIs and adapters for nine simulators/benchmarks. Privileged simulator state and user-written predicates define the conclusions; results do not certify physical safety. Fixed-period monitoring does not yet handle asynchronous, uncertain real sensors. A stricter persistence requirement changes evaluation semantics, not the original benchmark score.

## FISRF: Flexible Instructional Scaffolding Reflection Framework for Robotics Task Planning with Large Language Model

- [arXiv 2610.35686](https://arxiv.org/abs/2610.35686) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35686)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35686)

FISRF combines short-term trajectories/reflections with cross-task failure lessons and a fixed RAG mentor knowledge base; measured recovery difficulty and improvement choose which reflection or guidance to request. Quantitative evidence is text simulation; the dual-arm mobile-robot kitchen demonstration has no reported trial count or comparative success rate. Planning epochs are iterative recovery rather than independent seeds. Reported reflection cost is tokens per recovered task, not total deployment dollars; isolated long-term transfer and uncertainty remain unclear.

## Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation

- [arXiv 2610.35636](https://arxiv.org/abs/2610.35636) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35636)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35636)

OpTTA adapts a latent world model with observed-transition prediction loss plus an optimistic goal-reaching cost on planner candidate rollouts, without extra interactions. Simulated pushing, reaching and navigation only; adaptation resets per task and uses at most 30 replans. LeWM TwoRoom can degrade. This is parameter adaptation for planning, not an established continual or real-robot capability.

## Preemptive Instruction Following with Resumption

- [arXiv 2610.35576](https://arxiv.org/abs/2610.35576) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35576)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35576)

Introduces navigation episodes with single, repeated and nested task interruptions; a candidate-ranking objective emphasizes re-grounding when a suspended task resumes. Interruptions occur after completion of the current atomic task. Simulation navigation, not manipulation or VLA motor control. Reported SR averages atomic navigation segments, not whole interrupted sequence completion; improvements vary by interruption setting. Resume weighting helps stage metrics but does not dominate simpler BCE on aggregate SR.

## WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU

- [arXiv 2610.35529](https://arxiv.org/abs/2610.35529) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35529)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35529)

WorldPager keeps int4 world-model KV across GPU, pinned DRAM and NVMe; it prefetches pose-predicted retrievals, reuses stale entries instead of waiting on misses, writes back asynchronously and remaps positions beyond the native horizon. “Zero stall” excludes dequantization/write-back and permits stale retrieval; it is not zero overhead or real-time 16fps. Timing uses one scene/seed and one physical drive; slower drives are software-emulated. Quality evidence is MG2-only, with three scenes/five seeds for long-gap tests; texture drift remains. Baselines are reimplementations, not original systems.

## EmbodiedLab: Benchmarking Embodied Agents That Act to Know

- [arXiv 2610.35385](https://arxiv.org/abs/2610.35385) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35385)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35385)

EmbodiedLab requires agents to discover unknown quantitative properties through physically operating simulated instruments; success checks answers, episode-grounded measurements and required physical state. Entirely simulated science apparatus; evaluates model plus native coding harness rather than model alone. Skill recipients differ from teacher agents, and small experiment counts limit precision. Reference solvability does not imply physical-lab transfer.

## RetroNav: Scene-Grounded Retrospection and Retry for Self-Evolving Lifelong Navigation

- [arXiv 2610.35172](https://arxiv.org/abs/2610.35172) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35172)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35172)

RetroNav links geometric/semantic scene evidence to historical decisions, uses an independent evaluator to request retries, and writes evidence-grounded retry briefs without model training. Benchmark subsets, not full splits: IR2R 299 episodes/three scenes, GOAT 307 subtasks/five scenes. Retries reset to the original pose with a renewed step budget; reset travel is uncharged. Cross-task memory is disabled on three episodic benchmarks.

## MemVLN: Streaming Episodic Memory for Vision-Language Navigation

- [arXiv 2610.35066](https://arxiv.org/abs/2610.35066) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35066)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35066)

MemVLN compresses episode-local visual features with timestamps and action-derived poses into a bounded bank and 300 cross-attention memory tokens, combining a frozen geometry encoder with trained memory, adapters and trajectory-summarization supervision. Memory is episode-local, not cross-task skill accumulation. Real tests share one scene with 24 post-training demonstrations; only six distinct test instructions, no cross-scene validation. Gains combine geometry and auxiliary training; RxR geometry-only success (56.3%) exceeds the full model. Fixed-input RTX4090 latency rises 503.2→691.0 ms.

## VISTA: Active Exploration for Self-Improvement in Embodied Agents

- [arXiv 2610.35051](https://arxiv.org/abs/2610.35051) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35051)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35051)

VISTA evolves executable robot-agent harnesses using an ancestry graph, active diagnostic interactions and fresh autonomous evaluation of frozen candidate packages, without updating model weights. Simulation only. Task-specific selection and best-so-far curves do not prove unseen-task generalization or monotonic candidate improvement. Up to 100 planner turns and 10,000 physics steps on LIBERO-Pro/RoboTwin; development compute is substantial and baseline budgets must not be assumed matched.

## Behavioural Quality Is Not Learning Utility: Objective Mismatch in Human Behaviour Models for Robot Learning

- [arXiv 2610.34839](https://arxiv.org/abs/2610.34839) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34839)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34839)

Tests whether human-behavior generative metrics predict their usefulness as simulated training partners for robot RL. Policy tests are simulated, including simulated human partners—not physical human-robot trials. Findings depend on these model families, representations and RL training protocols; they do not imply realistic behavior is unnecessary for safety.

## SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments

- [arXiv 2610.34745](https://arxiv.org/abs/2610.34745) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34745)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34745)

An agentic pipeline reconstructs interactive simulators from 3D/4D captures, inspects and repairs scenes, and produces digital-sister variants and scripted demonstrations. Geometry/IoU improvements are not calibrated contact dynamics. Physical parameters are unmeasured estimates; static evaluation uses very few scenes and single conversions. Real transfer is preliminary and non-monotonic with simulated data scale.

## VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware

- [arXiv 2610.34717](https://arxiv.org/abs/2610.34717) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34717)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34717)

Profiles 18 released VLA models, 19 configurations and seven inference stages on Jetson AGX Thor and AMD Ryzen AI Max+ PRO 395, separating action generation, backends and host preprocessing. Timing is not a closed-loop success benchmark: inputs are a shared LIBERO observation plus 24 frames from one episode, with 20–100 timed calls. Models retain different native chunk/execution settings. Compilation can change gripper commands; low-bit action similarity does not establish preserved task success.

## Video World Models Need Predictable Latents

- [arXiv 2610.34663](https://arxiv.org/abs/2610.34663) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34663)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34663)

Fine-tunes autoencoder latents for temporal predictability and uses a past-conditioned decoder to preserve reconstruction while simplifying world-model dynamics. Main evidence concerns video prediction and policy-evaluation agreement, not improved robot policy success. Studies 2D spatial autoencoders fine-tuned from pretrained models; broader domains and spatiotemporal autoencoders are untested.

## RobotAgentBench: Towards Open-world Robot Autonomy

- [arXiv 2610.34649](https://arxiv.org/abs/2610.34649) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34649)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34649)

RobotAgentBench evaluates task discovery, context reasoning, manipulation, recovery and robustness plus open-ended household scenarios, comparing coding, learned and hybrid planning/execution/verification architectures. Scores are capability/scenario aggregates, not a universal task success rate. Main results are simulation; matched physical subsets cover only selected systems, not the best hybrid/RSI rows. Open-ended scores remain low and standalone versus agents differ in interfaces.

## What Does World Modeling Actually Improve in Robot Action Learning?

- [arXiv 2610.34593](https://arxiv.org/abs/2610.34593) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34593)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34593)

Controlled future-video-loss removal within FastWAM and OpenWAM tests what predictive supervision changes; a training-only lightweight video predictor extends the test to π0.5. Simulation-only; gains under unseen tasks are inconsistent and environmental randomization leaves low success without a consistent prediction-loss advantage. Single training seed; rollout repeats do not establish training-seed robustness. Wan extension changes multiple factors.

## How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder: A Hierarchical, Matched Sim-Real Benchmark for Physical Interaction

- [arXiv 2610.34527](https://arxiv.org/abs/2610.34527) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34527)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34527)

PhysLadder defines 16 matched sim/real contact-rich tasks at three cumulative levels: contact geometry, sustained force regulation, and force regulation coordinated with contact reconfiguration. One model and very small per-task samples; agreement does not establish universal sim-to-real ranking validity. Simulation contact/material parameters are not measured physical properties; real and simulated model-call counts use different action interfaces.

## TRIAGE: Efficient Vision-Language-Action Inference Needs Both Reuse and Pruning

- [arXiv 2610.34519](https://arxiv.org/abs/2610.34519) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34519)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34519)

A training-free token allocator recomputes a fixed budget, reuses low-drift young KV caches and prunes invalid leftovers; drift thresholds are calibrated per backbone. Two OpenVLA-family backbones, simulation success tests and replay-stream hardware timings; no real-robot closed-loop test. Thresholds are empirically tuned; selected SimplerEnv tasks exclude floor-level full-recompute performance. The 48% headline reduction is prefill, not total control latency.

## AuRA: From Atoms to Bits through Autonomous Robot Interaction

- [arXiv 2610.34452](https://arxiv.org/abs/2610.34452) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34452)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34452)

Automates deformable digital-twin acquisition with feasible grasp selection, robot-state-derived gripper trajectories and registered pre-interaction geometry/appearance. Collection accounting excludes processing/reconstruction and untimed backup trials; expert collection is faster (100.6s) than AuRA. Prediction uses known gripper motion; unseen tests use selected assets and manual alignment. No policy-learning gain demonstrated.

## EAST: Embodied AI Safety Testing via Systematic Fault Injection in Digital Twins

- [arXiv 2610.34358](https://arxiv.org/abs/2610.34358) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34358)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34358)

Maps documented safety hazards to eight executable fault operators, verifies realized interventions and separately records safety violations and task outcomes. Simulation only; safety is limited to simulator-state predicates. Challenge exposure is close to Random-Legal and Rule-Based, not a blanket superiority result; unsafe-success counts diagnose metric mismatch rather than rank methods.

## Execution Logs Sway VLM Judges of Robot Progress

- [arXiv 2610.34151](https://arxiv.org/abs/2610.34151) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34151)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34151)

Controlled contradictory execution-log lines test whether VLM robot-progress judges follow text rather than visual evidence; a short unreliability warning is evaluated as mitigation. Conditional selected-clip effects, not population-wide failure rates; completion-claim search differs from the fixed-log test and was not tested on Sol. Warnings reduce misleading-log effects but also reduce benefits from accurate logs.

## Behavior Spatial Benchmark: Evaluating Spatial Understanding for Robotics

- [arXiv 2610.34051](https://arxiv.org/abs/2610.34051) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34051)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34051)

Connects spatial VQA, target grounding and VLA execution while separating target-selection intention from strict task completion. Entirely simulated. Headline abstract rates are soft intention measures, not task completion. Oracle grounding is privileged; task timeouts and hand-target correlations affect interpretation.

## Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents

- [arXiv 2610.33956](https://arxiv.org/abs/2610.33956) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33956)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33956)

CLE organizes 120 professional workflows into five dependent levels each, with persistent files/service state and human-authored rubrics; it measures complete agents under one- versus two-submission budgets. No robot tasks. Backbone parameters and harness implementation remain fixed; mutable context/memory is allowed, so results do not demonstrate recursive code/weight self-improvement. Trial 1/2 change submission budget and feedback, not just learning. One fixed task order, heterogeneous default agent settings and gated progression confound a pure memory-transfer interpretation.

## WMEval: Evaluating Interactive World Models Grounded on Physical Simulations

- [arXiv 2610.33894](https://arxiv.org/abs/2610.33894) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33894)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33894)

Evaluates interactive world models against matched Unity action trajectories and physical-state/causal references across six dimensions. Controlled generated-video evaluation, not robot policy training or real physics validation. Different interfaces allow different model subsets per metric; learned vision/VLM evaluators remain imperfect despite calibration.

## Memory or a Clock? Auditing a Memory Advantage in XLand-MiniGrid with Seeds, Maps and Evaluation Noise Apart

- [arXiv 2610.33816](https://arxiv.org/abs/2610.33816) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33816)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33816)

Audits recurrent-policy gains by separating training-seed, map and evaluation noise, then adding size-matched memory-free clock controls and recurrent-state resets. One 7×7-grid task, A2C and tiny networks; not a VLA or robot experiment. The 15pp preregistered advantage threshold fails despite a nonzero residual gap. Some no-clock and mechanism arms were added after interim/results inspection, and no time-independent reward control was run.

## RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models

- [arXiv 2610.33807](https://arxiv.org/abs/2610.33807) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33807)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33807)

Introduces hardware-prior-based KIVA kinematic stability and RIGIS multi-view geometry metrics, plus a world-model acceleration audit. Measures generated-video consistency, not downstream control success. Metrics do not establish contact physics, deformable behavior or force dynamics; some long-horizon comparisons confound rollout depth and non-Markovian regime.

## RoboJev: An Open Vision-Language Judge for Robot Success Detection

- [arXiv 2610.33718](https://arxiv.org/abs/2610.33718) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33718)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33718)

RoboJev-27B adapts JEV-27B-VL with language-only rank-32 LoRA and source-specific KL anchoring, then predicts success with a calibrated two-token readout from ten primary frames plus available auxiliary final frames. Only 80/268 SO-101 episodes are held-out tasks. API baselines receive four primary frames, so frontier comparisons are not input-matched. Cost excludes media/serving overhead; community labels have one annotator; calibration and safety transfer are unestablished.

## Power-of-Two Leaky Integrate-and-Fire Neurons for Event-Driven Vision-Language-Action Inference

- [arXiv 2610.33658](https://arxiv.org/abs/2610.33658) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33658)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33658)

Replaces selected π0.5 projections with signed power-of-two spiking events and residual membrane state; Heartbeat confines event extraction to each projection while preserving external token/cache interfaces. No measured hardware energy or latency. The 86.95% saving is an illustrative FP32 projection-arithmetic model excluding memory, control and encoding; a matched FP8 model with fixed movement budget estimates only 32.79% subtotal saving at T=1. Evaluation uses one seed and simulation; nonsignificance does not establish equivalence.

## Mix Forcing: Causal Pre-Training via Mixture Attention for Interactive World Models

- [arXiv 2610.33589](https://arxiv.org/abs/2610.33589) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33589)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33589)

Mix Forcing jointly trains teacher-forced causal and bidirectional video objectives with chunk-local prompt attention, then distills a four-step autoregressive generator. Camera/text-conditioned video generation only: no action-policy success, physical fidelity or robot transfer test. Public global-prompt benchmarks mismatch its local-prompt training; 14B training uses substantial compute.

## Replicate What Varies: Resource Sharing for Domain-Randomized Embodied Simulation

- [arXiv 2610.33582](https://arxiv.org/abs/2610.33582) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33582)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33582)

Patchwork represents environments as shared templates plus private mutation patches, sharing compiled MuJoCo structure and immutable assets while isolating state and randomized parameters. Infrastructure/resource results, not improved policy learning. Main headline excludes camera/object observation processing; camera path has Python GIL bottlenecks. Reuse diminishes with template/asset diversity, mutations are backend-restricted, and comparison with asynchronous GPU-vectorized execution remains future work.

## Distilling Dense Trajectory Teachers For Large-Motion Video World Models

- [arXiv 2610.33566](https://arxiv.org/abs/2610.33566) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33566)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33566)

DTTD interpolates sparse camera paths, uses the frozen base model’s dense-path videos as pose-aligned teachers, and combines teacher/geometry rewards to form offline Flow-DPO preferences with a cumulative motion curriculum. One camera-conditioned Wan1.3B backbone and one indoor dataset; no robot planning/control outcomes. Uses 10k preference pairs, 12 student candidates and four teacher videos per condition, each generated with 40 denoising steps; matching optimizer steps does not establish equal data-generation compute. Geometry rewards rely on estimated depth/poses; DTTD is not best on every geometric metric.

## WorldFailBench: Do World Models Understand Policy Failures?

- [arXiv 2610.33565](https://arxiv.org/abs/2610.33565) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33565)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33565)

Evaluates whether world models reproduce policy failure reasons, stages and success-to-failure boundaries, rather than only final outcomes. Real-robot coverage is two tasks; boundary interventions are simulation-only. Boundary discovery selects adjacent conditions with a ≥30-point success gap, then independently re-estimates endpoints; this is not an unbiased estimate over all scene changes.

## MOON: Learning When to Forget and How to Move On in Vision-and-Language Navigation

- [arXiv 2610.33546](https://arxiv.org/abs/2610.33546) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33546)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33546)

MOON adds a deviation judge and GRPO-trained recovery adapter to a frozen vision-language navigation policy: an alarm clears visual history once, then recovery learns to escape history-induced behavioral inertia. Simulation only; deployment tested on one backbone and trains two adapters, not training-free. Alarm operating levels were selected on the reported evaluation splits. Clearing breaks 5.8%/4.1% of base-success episodes on R2R/RxR; successful forgetting is not evidence that long-term skill memory should be deleted.

## ReSight: Task-Driven Self-Improving Memory for Embodied Agents

- [arXiv 2610.33487](https://arxiv.org/abs/2610.33487) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33487)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33487)

ReSight separates immutable observation evidence from extensible derived fields. Explore–Distill–Mount uses a higher-budget coding agent to create reusable memory builders, tools and skills for a fixed-budget executor, without reference answers. Online savings exclude separate exploration, model preparation and memory-building costs. This is historical-observation QA, not closed-loop manipulation; OC-NaVQA binary accuracy decreases 86.6% to 82.1%. Long-term repeated capability expansion remains untested.

## World-in-Context: Interactive Video World Modeling with In-Context Conditioning

- [arXiv 2610.33169](https://arxiv.org/abs/2610.33169) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33169)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33169)

World-in-Context places view, character-action and camera controls in shared self-attention as explicit tokens; Interaction-Transport RoPE incorporates accumulated control transitions into temporal attention. Navigation score is a composite video metric, not robot task success. Main model uses bidirectional fine-tuning on 100k navigation clips plus 500 switching sequences; the final 93.8% result is not single-view-only training. Cross-system data/compute are not matched; controlled architecture comparisons share its data. No embodied manipulation or physical-control validation.

## Gaussian Episodic Memory for Long-Term Spatiotemporal Reasoning

- [arXiv 2610.33158](https://arxiv.org/abs/2610.33158) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33158)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33158)

GEMS stores localized changes in a persistent temporal 3D Gaussian map and lets an agent retrieve, render novel views and compare revisits through a finite-state tool interface. Reported QA percentages are rescaled 1–5 judge scores, not binary exact-match accuracy. Three real scenes, pose/depth noise and novel-view artifacts; real score is below all-images. Storage comparison covers one scene per split and does not show online robot-policy gains.

## AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models

- [arXiv 2610.33074](https://arxiv.org/abs/2610.33074) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33074)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33074)

Allocates matrix-level bitwidths using action sensitivity and a measured weight-recovery cost proxy; per-channel calibration and grouped lossless coding reduce storage while weights are recovered to BF16 block by block. One model, simulation only; 150 episodes per suite and timing over ten inputs excludes preprocessing/postprocessing. Baselines are literature reports; the official repository clarifies its 96.9% reference is FP16 despite the paper’s BF16 label. W1.5* means W4 vision plus average-W1.5 language, not a 1.5-bit complete model. Compression increases latency.

## EKT-Router: Expert-Evidence Alignment for Embodied Vision-Language Models

- [arXiv 2610.33044](https://arxiv.org/abs/2610.33044) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33044)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33044)

EKT-Router jointly selects one of three frozen Qwen3-VL-8B capability experts, optional knowledge and perceptual tools under a call budget; a verifier filters returned evidence before a single final answer with original-input fallback. Embodied QA, not robot execution or active perception. Three experts require separate two-epoch adaptations; routing uses 1,020 fitting and 180 held-out media-disjoint cases. Cross-system scores mix reproduced, API and reported results. Single-round packet validity does not prove answer correctness, action safety or stable online learning.

## Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation

- [arXiv 2610.33024](https://arxiv.org/abs/2610.33024) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33024)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33024)

Skill Adaptation turns diagnosed executor weaknesses into a meta-skill for rewriting procedural skills, then compares one-shot rewriting and five rounds of feedback-driven self-evolution across executor capacities. Non-robotic STEM/document/developer tasks, selected from 607 tasks for skill sensitivity. Each evolution round runs once; small gaps have no repeated-run uncertainty estimate. Skills are already in context, so retrieval, progressive disclosure and closed-loop physical transfer are untested.

## The Value of Memory in Language Agents

- [arXiv 2610.31303](https://arxiv.org/abs/2610.31303) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.31303)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2610.31303)

v1→v2 tightens the memory value/resource-accounting framework and adds explicit amortized write-cost and ledger/recovery token accounting. The LoCoMo F1 values were already in v1; this revision changes how costs and claims should be interpreted, not the benchmark score. Only a twelve-question diagnostic, not a robot or online-skill-growth benchmark. Archive storage/local-search costs are unmeasured; monetary comparison requires deployment-specific prices. Existing recovery F1 0.329 versus ledger 0.016 must not be advertised as newly added evidence.

## Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models

- [arXiv 2610.26179](https://arxiv.org/abs/2610.26179) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.26179)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2610.26179)

v2→v3 adds Appendix J disjoint-source-group evaluations: backbones are trained from scratch on training-only groups and heads selected on separate groups. This directly probes overlap concerns in the released-asset benchmarks; original headline gains are not new. Push-T shows no improvement in this stronger separation test. New task windows differ from the original benchmark (uniform Cube starts; 80-step rather than 74-step Push-T gaps); do not compare absolute rates across protocols. SE covers backbone seeds, not sampled tasks/source groups. Simulation only.

## One-shot Human Video-Guided Adaptation for Vision-Language-Action Models

- [arXiv 2610.19746](https://arxiv.org/abs/2610.19746) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.19746)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2610.19746)

v1→v2 adds two adapted video-conditioning baselines, fills previously incomplete ablation results, and replaces the five-trial real-robot table with ten-trial results. Main RoboTwin CapPro performance was already in v1. The added baselines are adaptations to π0.5, not unchanged original systems. Ten trials per physical task remain small; hard sorting succeeds only 20%. One-shot refers to target-time human-video guidance, not training from one demonstration overall; source-task training remains.

## Expert-Play Contouring Control: Faster-than-Demonstration Planning from Slow Expert and Fast Play

- [arXiv 2609.22798](https://arxiv.org/abs/2609.22798) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2609.22798)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2609.22798)

v1→v2 adds extensive implementation/evaluation appendices that materially qualify the faster-than-demonstration claims: friction-sweep retraining, success-conditioned phase timing, controller/search budgets and play-mixture provenance. The 13s versus22s real example already appears in v1. The sweep does not isolate zero-shot robustness of one fixed model, and method-specific success subsets can change the timing comparison. No new real-robot aggregate success result was established in this revision; the physical speedup remains an illustrative rollout.

## GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation

- [arXiv 2609.05588](https://arxiv.org/abs/2609.05588) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2609.05588)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2609.05588)

v2→v3 substantively replaces Appendix A.1/Table 3 RoboTwin evaluation: six named perturbation columns become Clean-to-Clean and Clean-to-Random under 50 clean demonstrations per task, with additional leaderboard baselines. This is a protocol/result replacement, not a directly comparable version-to-version gain. Baselines are drawn from the official RoboTwin leaderboard where available and the Qwen-RM report, rather than all being rerun in a controlled study. The main real-robot pretraining/scaling findings are inherited from v2.

## What Can One Sentence Fix? A Failure Taxonomy and a Minimal Language Correction for Frozen VLA Policies

- [arXiv 2608.29967](https://arxiv.org/abs/2608.29967) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2608.29967)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2608.29967)

v1→v2 retitles/reframes CorrectVLA and replaces the small real-robot table with three 10-trial runs per condition, adds long-horizon negative controls, and explicitly separates failure-only retry recovery from all-episode net success. Simulation recoveries of 65/139 and 33/328 are inherited. A person labels the failure mode and writes a timed correction per failing run, taking 40–80 seconds; additional correction rounds may be used. Retry-only simulation success does not establish unconditional policy improvement. The channel fixes magnitude/timing, not missing semantic targets or plans; LIBERO-90 is instruction-OOD, not scene-OOD.

## Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL

- [arXiv 2608.12063](https://arxiv.org/abs/2608.12063) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2608.12063)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2608.12063)

v1→v2 adds Q5/Table 2 comparing sparse offline-to-online learning against directly reusing the SMPC expert cost or demonstration data with FastTD3, IQL and Diffusion Policy. The original hardware results and sparse-reward method are inherited. These baselines reuse the SMPC cost/data, so failure is not evidence that the RL algorithms are generally inferior. The authors attribute it to cost incompatibility and absent corrective examples; SMPC-assisted DAgger is described as too expensive. New comparison is simulation-only.

## LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies

- [arXiv 2606.15768](https://arxiv.org/abs/2606.15768) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2606.15768)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2606.15768)

v1→v2 adds an eight-subtask Clean Table real-robot task, lighting-shift tests, capacity/predictive-interface controls, and training-cost/confidence-interval reporting. The 98.6% LIBERO and 187 ms headline results already appear in v1. Clean Table success remains modest, especially under lighting shift; comparisons use few real tasks. Mechanism controls omit Stage-2 pretraining and should not be equated with the fully pretrained policy. The lighting tests reuse color-augmented task checkpoints.

## PRISM: PRior-guided Imagination Sampling in world Models

- [arXiv 2606.07974](https://arxiv.org/abs/2606.07974) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2606.07974)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2606.07974)

v1→v2 adds frozen-feature action-prediction probes with random-encoder controls, a diffusion prior using the same fusion interface, ten-seed main simulation evaluation, and matched real-robot prior-free comparisons. Prior-guided Gaussian fusion and the two robot platforms were already in v1. The diffusion and MLP heads use different goal conventions, so their comparison does not isolate architecture. Probe scores come from validation-selected fits, not an independent test split. Head-training/inference figures exclude world-model pretraining and shared encoder/planner costs. Real success gains are four and six episodes; more trials are needed.

## Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects

- [arXiv 2606.01950](https://arxiv.org/abs/2606.01950) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2606.01950)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2606.01950)

v1→v2 adds Gaussian render-and-compare object tracking via FoundationPose, evaluates dynamics prediction from estimated rather than ground-truth poses, and adds two qualitative real-world recordings. Simulated non-prehensile MPC was already present in v1. Tracking benchmark uses five YCB objects without continuous rotational symmetry, a validation-selected fixed viewpoint and trajectories truncated at visibility failure. Quantitative tracking/prediction remains simulated; real evidence is qualitative, not real MPC success. Reconstruction is a separate prerequisite, and later real predictions miss a contact; training still uses cleaner pose histories.

## WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform

- [arXiv 2605.17912](https://arxiv.org/abs/2605.17912) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2605.17912)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2605.17912)

v1→v2 adds a physical tactile ablation, detailed RL/decoder interfaces, uncertainty reporting and expanded real-robot task documentation. The broad visuotactile/RL/cross-platform benchmark concept was already in v1. Small physical samples yield wide intervals; separate Wilson intervals are not a paired significance test. World-model utility includes separately trained decoders, so it is not isolated transition fidelity. Expanded qualitative tasks must not be counted as a new quantitative leaderboard.

## BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation

- [arXiv 2605.08571](https://arxiv.org/abs/2605.08571) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2605.08571)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2605.08571)

v2→v3 adds tuned-uniform and source-mean discrepancy controls, feature-alignment diagnostics and a weight audit that explicitly limits the theory claim. The main BEACON success values mostly predate this revision. The theoretical bound motivates the objective but is not an applicable guarantee for the audited learned weights. New feature alignment is diagnostic; lower discrepancy itself does not imply higher task success, as the MMD baseline demonstrates.

## A Semantic Autonomy Framework for VLM-Integrated Indoor Mobile Robots: Hybrid Deterministic Reasoning and Cross-Robot Adaptive Memory

- [arXiv 2605.02525](https://arxiv.org/abs/2605.02525) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2605.02525)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2605.02525)

SAS v1→v2 replaces broad cross-robot success framing with a frozen-implementation audit, sealed instruction challenge and controlled memory-on/memory-off/direct-VLM comparisons; recurrent associations are explicitly stability-tested rather than certified true. Two robot configurations in one indoor environment, with shared-workstation reasoning/memory and deliberate digest installation. Familiar-item scoring uses stored associations; unseen items gain no memory benefit. Replay seeds are not independent tasks, diagnostic probes are selected, and sampled consistency does not prove safe semantic transfer.

## Does "Do Differentiable Simulators Give Better Policy Gradients?" Give Better Policy Gradients?

- [arXiv 2604.18161](https://arxiv.org/abs/2604.18161) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2604.18161)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2604.18161)

v1→v2 corrects Appendix D’s dimensional-precision analysis and Monte Carlo table for the DDCG versus AoBG test statistics, and clarifies that the result concerns statistic precision rather than optimizer performance. This is a linear-Gaussian toy-statistic correction, not proof of equal scaling in gradient-estimation error or robotics learning performance. Existing optimization/RL results should not be presented as newly added evidence.

## SentryVLA: Uncertainty-Guided Action Selection and State Monitoring for Vision-Language-Action Robotic Control

- [arXiv 2604.16677](https://arxiv.org/abs/2604.16677) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2604.16677)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2604.16677)

v1→v2 adds a formal marginal-coverage proposition and sharply scopes CQR claims to exchangeable frame–candidate calibration samples; it also adds explicit calibration diagnostics and action-score design details. This is a substantive reliability-claim clarification, not a new safety guarantee. The guarantee does not extend to adaptive selected actions, temporally correlated closed-loop states, shifted distributions or task success. Monitoring thresholds and OOD findings remain empirical. No independent reproduction of the calibration experiment.

## AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation

- [arXiv 2604.11674](https://arxiv.org/abs/2604.11674) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2604.11674)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2604.11674)

v2→v3 adds a real-world domain-randomization sweep, quantitative five-embodiment collection evaluation, and fixed-demo-budget ACT grasp-source controls. The multi-stage success breakdown and original four-task sim-to-real evaluation already appeared in v2. The pose sweep increases demonstrations from 300 to 1,200 to 2,700, so range and data volume are confounded; only one real task and ten trials per setting. Cross-embodiment results concern simulator trajectory collection, not learned policy transfer. Existing headline tables remain unchanged despite collection-count wording changing from 30 to 100 rollouts.

## ActECC: Action Chunk Temporal Harnessing for Edge-Cloud Collaborative VLA Inference System

- [arXiv 2603.07949](https://arxiv.org/abs/2603.07949) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2603.07949)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2603.07949)

v2→v3 changes RAPID into ActECC: the emphasis shifts from edge–cloud partitioning to kinematics-guided usable action-chunk ranges and delay-aware replanning scheduling. It replaces the evaluation with π0.5/GR00T N1.5 system results; the prior 1.73× headline is not directly comparable. Evaluation measures deviation from aligned expert trajectories, explicitly not task success. It is a simulation/system study; cloud-only can have lower latency than ActECC. The two headline maxima arise from different comparisons, and should not be combined into one configuration.

## FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation

- [arXiv 2602.13444](https://arxiv.org/abs/2602.13444) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2602.13444)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2602.13444)

v1→v2 turns qualitative robot showcases into a counted baseline comparison and adds matched single-stage, grasp-prefix pretraining, reconstruction and scene-granularity analyses. The 40× inference and 1.7× simulation-success headlines already appeared in v1. Execution is open-loop after offline scene reconstruction, retargeting and DexTrack refinement; these are nominal-condition executability results, not disturbance robustness. Pretraining controls use one training seed and show no clear physical-success gain. Matched single-stage control is 40ms faster with comparable action recognition/simulation success: two-stage gains concern contact quality, not universal superiority.

## UniManip: Open-World Robotic Manipulation via Agentic Operational Graphs

- [arXiv 2602.13086](https://arxiv.org/abs/2602.13086) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2602.13086)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2602.13086)

v1→v2 adds LIBERO-Pro evaluation and explicit cross-embodiment UR7e/Robotiq and dexterous-hand tests, alongside formalized bounded AOG recovery. The original 22.5/25.0-point advantages are inherited, not new revision gains. Cross-embodiment transfer retains task-level AOG but requires a new URDF/limits, tool-frame calibration, controller mapping and hardware-facing adaptation. Do not describe it as literally configuration-free; dexterous execution success is only 53%.

## CRAFT-E: An Interpretable and Editable Neuro-Symbolic Framework for Affordance-Grounded Active Object Retrieval

- [arXiv 2512.04231](https://arxiv.org/abs/2512.04231) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2512.04231)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2512.04231)

CRAFT-E v1→v2 adds COCO-Tasks transfer, explicit graph-edit interventions and expanded error decomposition. Its verb–property–object graph and real-robot retrieval pipeline predate this revision. COCO transfer measures image grounding, not physical retrieval. Graph edits are selected after inspecting failures on the same set: controllability, not held-out autonomous repair. New text acknowledges full-pipeline differences versus GPT-4o are not significant; supervised COCO methods are contextual, not matched comparators.

## UniAction: Unified Action Conditioning for World Models

- [arXiv 2610.32977](https://arxiv.org/abs/2610.32977) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32977)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32977)

UniAction represents force, camera, hand and robot-pose actions as sparse semantic elements with continuous spatiotemporal coordinates, mapped into the video backbone’s native RoPE geometry. Cardinality-calibrated attention compensates for different action-token counts. These are video-generation action-following scores, not closed-loop robot success. Conditioning branches differ in trainable parameter counts. Joint training does not improve every metric: camera LPIPS is .4863 versus expert .4780. Four specified action forms do not establish arbitrary-action or unseen-embodiment generalization.

## RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

- [arXiv 2610.32971](https://arxiv.org/abs/2610.32971) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32971)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32971)

Unifies 17 robust/safe RL algorithms and six standard references, with reusable interfaces and individual/compound deployment shifts including latency and semantics. Not every algorithm runs every task. Methods retain native budgets, and pooled-family comparisons mix backbone strength with robustness mechanisms. The π0.5 study uses one fine-tuned model and offline joint-space demonstration tracking, not closed-loop VLA task success or real-robot validation.

## If at First You Don’t Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

- [arXiv 2610.32941](https://arxiv.org/abs/2610.32941) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32941)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32941)

Trains a small failure head on frozen-policy rollouts and reverses achieved arm motion before retrying. Simulation only; pooled results include configuration-selection seeds. Held-out pi0.5 uplift is 0.70 points. Reversal does not restore objects or guarantee safety, and the head requires labeled rollouts.

## Regularised RL improves sim-to-real transfer

- [arXiv 2610.32855](https://arxiv.org/abs/2610.32855) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32855)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32855)

Extends soft mellowmax to continuous-control actor–critic with a slowly updated reference policy and tests whether regularization improves sim-to-real robustness beyond nominal training return. Return is not success rate. Domain randomization remains necessary, and temperatures vary by task. PPO/FastTD3 are excluded from ANYmal perturbation deployment after failing a prespecified simulation safety check, so those cells are missing, not observed hardware failures. MuJoCo tuning budgets are unequal.

## Predictive Long-Horizon Progress Modeling with Action-Aware Quantification

- [arXiv 2610.32776](https://arxiv.org/abs/2610.32776) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32776)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32776)

NimCritic couples predictive video learning with separate progress/completion outputs, perturbed progress history, and cross-modal alignment. LOOM contains 300 cross-embodiment trajectories and 19,618 human-calibrated frames. These are offline evaluator metrics, not robot task-success rates. Multi-subtask evaluation relies on offline VLM segmentation, not demonstrated real-time judging. Training uses 800+ hours and 48 accelerators; no closed-loop policy improvement from its reward is established.

## Semantic Representation for Agentic Self-Play in Automated Laboratories

- [arXiv 2610.32755](https://arxiv.org/abs/2610.32755) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32755)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32755)

VERID maintains a persistent semantic laboratory twin with introspection, pre-execution simulation gates, synchronized traces and resumable state. Agents retain physical operating bounds and analytical lessons across runs. These are small case studies, not an isolated causal memory ablation: challenge instances and experimental strategies change. Uses a structured harness, internal Gemini checkpoint and operator approval gates in supervised runs. Biological discoveries and broad robot-policy transfer are not demonstrated.

## When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

- [arXiv 2610.32431](https://arxiv.org/abs/2610.32431) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32431)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32431)

MART-GRPO uses a fine-tuned, then frozen VLM to locate the last visible unrecovered error in full rollout videos and truncate subsequent failure penalties, retaining successful-rollout terms and original normalization. Ideal stopping results motivate, but do not certify, the retrospective implementation. Simulation only. The actor sees one camera while the VLM reviews three; additional annotations and VLM fine-tuning are required. Boundaries use future rollout information and need not satisfy ideal stopping assumptions. One task declines by 1.95 points; held-out scene seeds are not independent training seeds.

## LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents

- [arXiv 2610.32412](https://arxiv.org/abs/2610.32412) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32412)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32412)

An external retrieve–bind–select layer reuses leaf-level action grounding while retaining the original recursive planner. A LoRA-trained 1.7B selector chooses an admissible bound action or defers to the unchanged host. Cost savings are conditional on common successes and concern host-model inference, not total system cost. Evidence covers one planner/host and two discrete-action simulations; ALFWorld success differences are not significant. Library growth demonstrates read-time adoption, not monotonic success improvement or continuous robot control.

## LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners

- [arXiv 2610.32348](https://arxiv.org/abs/2610.32348) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32348)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32348)

Pairs an immutable execution log and verbatim note history with expectation-gated action frames and skim-then-inspect demonstrations. GPT-6 Astra plans either waypoints or grounded π0.5 subgoals; the memory is an inference-time interface, not parameter adaptation. The clean memory comparison demonstrates cost savings, not a clear success gain. Full-system gains also change action/call interfaces; direct control uses depth, calibration and task notes derived from success-checking code. One simulated benchmark and proprietary model, no real robot. Single-component failures differ by only 2–4 episodes.

## Lifelong Context Adaptation through Bidirectional Memory-Skill Learning

- [arXiv 2610.32295](https://arxiv.org/abs/2610.32295) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32295)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32295)

MemCryst freezes the language model and co-evolves external episodic/factual memory and conditional skills. Repeated episodes support skill creation/revision; task outcomes adjust future retrieval weights without rewriting served records. Text-based simulation, not real robot control. Skill-only serving still retains internal memory for learning skills. Outcome credit is shared by all served records, not individual causal attribution; feedback noise and transfer to unseen domains are untested. Task order matters.

## ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences

- [arXiv 2610.32222](https://arxiv.org/abs/2610.32222) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32222)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32222)

A reward model combines action-mismatch and video-mismatch preferences to judge visual quality and action following without reference videos at reward-computation time. It introduces AVM-Eval (67.2k pairs) and AVM-Pref (506.3k pairs). RL evidence is restricted to one 2B world model and AgiBotWorld, not robot task success. Physical consistency is not directly supervised and ratings rely on a VLM. Reference-free reward computation does not mean reference-free dataset construction; pairwise ranking is not a guarantee of physical validity.

## Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems

- [arXiv 2610.32208](https://arxiv.org/abs/2610.32208) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32208)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32208)

Uses sparse autoencoder features of OpenVLA activations for failure prediction and VLM-generated behavioral interpretations, with branching rollouts estimating a point of no return. Simulation and one policy only. Unsupervised SAE fitting uses all 500 trajectories; supervised predictors use held-out splits. Four branches per probe give coarse, remaining-budget-dependent recoverability. Outcome associations are not causal failure mechanisms or validated safety interventions.

## Ψ-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model

- [arXiv 2610.32177](https://arxiv.org/abs/2610.32177) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32177)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32177)

A unified token interface generates and interprets text, images, geometry and motion; adaptive streams of thought select intermediate representations. GRPO provides a proof of concept for choosing reasoning streams on visual question answering. The reported sim-to-real transfer concerns visual question answering over recorded robot videos, not robot deployment. Optical flow and tracks are proxy actions rather than actuator commands. Training-time positive/negative transfer among unified capabilities is not isolated; physical control remains future work.

## Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies

- [arXiv 2610.32102](https://arxiv.org/abs/2610.32102) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32102)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32102)

Jointly studies executed action horizon and flow-solver depth, testing when shallow sampling helps or harms. Long open-loop execution fails on moving targets; speedup is amortized inference cost, not guaranteed wall-clock task acceleration. The paper inconsistently describes simulation task totals and pi0.5 chunk configurations.

## TTT in VLA Models: Exploring Training with Human Demonstrations

- [arXiv 2610.32094](https://arxiv.org/abs/2610.32094) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32094)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32094)

Integrates fast-weight TTT into InternVLA-A1 and pi0.5, documenting human-to-robot memory transfer and truncated gradient paths. Negative findings are limited to small cup-selection datasets and tested recipes, not a disproof of TTT. Trial counts are insufficiently reported. Autoregressive-state evaluation still uses recorded images, not closed-loop observations.

## Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates

- [arXiv 2610.31859](https://arxiv.org/abs/2610.31859) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31859)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31859)

Audits update rounding when trainable matrices and AdamW state remain bf16 without fp32 master weights. One suite and shortened schedules; precision of optimizer moments is not separately ablated. SmolVLA scorer discrepancies restrict cross-paper comparisons. This does not show every bf16 computation or JAX training setup is affected.

## FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation

- [arXiv 2610.31841](https://arxiv.org/abs/2610.31841) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31841)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31841)

A coding agent uses RGB-D and wrist force/torque logs to generate and revise Python contact-probing and force-feedback programs. Experience is retained in executable control logic, without task-specific model training. Five real tasks, one model, small trial counts. Each development run permits 20 physical rollouts and four hours; humans authorize execution, reset scenes and judge final acceptance. The ablation changes access to force feedback and routines together, not just memory. Reasoning costs 4–10 minutes per iteration.

## SEVI: Safe Evidential Real-World Reinforcement Learning

- [arXiv 2610.31829](https://arxiv.org/abs/2610.31829) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31829)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31829)

Adds an evidential safety critic that gates task actions using predicted violation risk and epistemic uncertainty, invoking a shared offline-trained recovery policy during online RL. Only one hardware task and two simulated tasks; no formal zero-violation guarantee. Hardware learning uses 50 successful prior demonstrations, 200 recovery demonstrations and validation-based thresholds. Final success and cumulative training incidents have different denominators.

## KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations

- [arXiv 2610.31801](https://arxiv.org/abs/2610.31801) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31801)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31801)

Compresses shared 14-D bimanual kinematics into transition-supervised Sparse Motion Tokens at two tokens/second; a LoRA-adapted language model predicts temporal segments and descriptions, with transfer to new robots and human hands. The encoder uses whole-episode normalization and symmetric temporal context, so it is offline. Tokenizer comparisons differ in input representation and reader-training populations, not just objective. Segmentation/semantic transfer does not establish closed-loop robot-policy gains.

## FLORA: An Open Model Suite for Scaling Robotics Data Engines

- [arXiv 2610.31779](https://arxiv.org/abs/2610.31779) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31779)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31779)

An open labeling suite supplies temporal segments, intended-action captions and outcome/dense/rubric rewards for robotic data pipelines; segmentation/captioning use RL post-training, while the released reward model uses SFT. Not uniformly best across metrics; systems use different frame budgets/compute. The approximately 125× cost claim assumes GPU pricing and modeled throughput, omits deployment overhead, has unverified production GPU-hour accounting, and is not fully reference-version matched. No direct downstream policy-learning improvement is established here.

## See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space

- [arXiv 2610.31762](https://arxiv.org/abs/2610.31762) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31762)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31762)

RepresentNav constructs policy-oriented representations from multiple layers of frozen vision backbones, then learns a JEPA-style latent future prediction before waypoint generation. External baselines are taken from their papers with differing observation settings. Physical navigation demonstrations do not establish manipulation transfer; dexterous and whole-body control remain untested.

## ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

- [arXiv 2610.24512](https://arxiv.org/abs/2610.24512) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.24512)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2610.24512)

A benchmark of eight contact-rich skill categories, 36 reference tasks and over 40 printable assets with corresponding simulation components; six tasks evaluate vision-only and visual-tactile learned policies. The four systems differ in pretraining, observation histories and tactile interfaces, so this is not a perfectly isolated tactile-modality ablation. Only six of 36 tasks receive learned-policy evaluation. Velcro stabilization enables one-arm tasks that could otherwise require another arm. Rigid/articulated printed assets do not cover deformable contact; negative tactile results apply to the tested policies and sensors, not touch in general.

## RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation

- [arXiv 2610.05414](https://arxiv.org/abs/2610.05414) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.05414)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2610.05414)

A MuJoCo mobile-manipulation benchmark separates task success, subgoal progress, spatial grounding and repeated-action recovery through a fixed skill interface. Simulation only, three episodes per task, discretized grid navigation and a fixed skill library. Grasp candidates include expert-verified ground-truth fallback annotations as well as GraspNet outputs; the evaluation does not demonstrate end-to-end low-level control or autonomous skill expansion. Execution efficiency is computed only on successful trajectories and reflection scores only on episodes containing repeated-action loops.

## Are Frontier VLM Agents Ready to Be Robot Generalists? An Empirical Study with the Embodied Agent Arena

- [arXiv 2610.00854](https://arxiv.org/abs/2610.00854) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.00854)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2610.00854)

A unified arena separates geometric prediction, affordance grounding, intermediate subgoals and native complete-task success across 1,000 cases. The union is retrospective coverage, not a deployed ensemble success rate. Source interfaces and budgets are retained rather than identical across all tasks; some supplementary episodes and missing records are explicitly separate. Error-free code and low latency must not be equated with physical task completion; this is benchmark evidence rather than new real-robot validation.

## Metro-WM: Long-Horizon Latent Planning with Realisable Sub-Goals

- [arXiv 2609.31868](https://arxiv.org/abs/2609.31868) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2609.31868)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2609.31868)

A nonparametric macro planner retrieves observed states from an offline trajectory graph and uses shortest-path subgoals with repeated graph re-entry. All added tests are simulated. Metro uses a fixed rather than shrinking horizon and tunes horizon/subgoal distance plus executed-block count on separate tuning tasks; baselines use released configurations. Retrieved states are real, but this does not certify every connecting transition. Diverse layouts absent from the corpus may break stitching.

## Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning

- [arXiv 2608.24885](https://arxiv.org/abs/2608.24885) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2608.24885)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2608.24885)

WorldEcho evaluates off-expert action following using visual screening and end-effector trajectory alignment; WorldSync combines broader action data with dynamics grounding and intervention-effect supervision. The small headline gated-error difference is a point estimate, not established significance. Visual screening does not guarantee integrity; its human checks use only 15 clips per dimension. Video metrics use reconstructed references and separate generation batches. Pretraining corpora and baseline histories differ; the expanded-data advantage is not a controlled data-efficiency claim.

## PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views

- [arXiv 2608.19188](https://arxiv.org/abs/2608.19188) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2608.19188)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2608.19188)

Occupancy-conditioned global and local geometry representations generate and refine bimanual grasp pairs from a segmented single-view RGB-D observation. Hardware trials evaluate only this method, without matched real-robot baseline rates, and success means lifting rather than completing a downstream manipulation task. Candidates are filtered for collision-free kinematic reachability. The separate real-world RGB-D dataset table uses digital-twin simulation metrics, not hardware success; its 81.54% GS must not be confused with the 39/54 lift rate.

## RAPAC-DP: Response-Aligned Pending-Action Compensation for Diffusion Policies under Delayed Execution

- [arXiv 2608.15924](https://arxiv.org/abs/2608.15924) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2608.15924)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2608.15924)

A frozen diffusion/flow policy gains a pending-action encoder and LoRA compensation that aligns each output chunk to its scheduled execution time, trained using delay-conditioned samples from delay-free demonstrations. Only one checkpoint per method/task is tested, so confidence intervals describe trial variation rather than training-seed robustness. Fixed conveyor speed/starts and injected discrete delays limit claims about arbitrary network jitter. At low delay it trails RTC on dynamic grasping (73.3% versus 76.7%); the method requires training an adapter.

## Semantic Anchoring for Robotic Action Representations

- [arXiv 2607.13597](https://arxiv.org/abs/2607.13597) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.13597)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2607.13597)

An auxiliary alignment objective preserves task-level semantics during VLA fine-tuning through shared/private representations anchored to a frozen manipulation-text encoder; auxiliary modules are removed at inference. Correlations do not establish semantic erosion as the sole cause of OOD failure. Architectures use different official fine-tuning recipes. The fixed semantic encoder bounds the method, shared/private factors are not identifiable, and this is downstream fine-tuning rather than continual deployment adaptation.

## GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

- [arXiv 2607.05369](https://arxiv.org/abs/2607.05369) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.05369)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2607.05369)

GaP composes typed robot skill graphs and improves their structure, parameters and throughput through simulation rehearsal before deployment. New throughput evidence is simulation, not a new real-robot productivity result. The paper explicitly says CaP-X is not a fair standalone comparison because available environment geometry differs. MORSL equalizes selected perception/grasp components, not all motion primitives, inference budgets or system choices. The tasks are mostly quasi-static.

## Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration

- [arXiv 2605.31196](https://arxiv.org/abs/2605.31196) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2605.31196)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2605.31196)

TouchSafeBench evaluates current collision recognition and early warning in simulated human–robot co-presence, separating robot–scene and human-contact risks. The real recordings contain no physical contact and use a human head-mounted camera; labels are binary proximity at a 1 m threshold, not actual collision safety. False-alarm estimates use only 12 hard negatives. Prompt tests repeat one model/condition; one expert saw viewpoint conditions in fixed order. No closed-loop safety intervention is validated.

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

