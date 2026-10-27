# Vision-language-action models

[English](vla.md) | [简体中文](vla.zh-CN.md) | [All topics](README.md)

92 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

## OSWAM: An Effective World Action Model with One-Step Action Generation

- [arXiv 2610.35850](https://arxiv.org/abs/2610.35850) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35850)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35850)

Uses action/scene imagination tokens for structured diffusion initialization and privileged future-conditioned distillation to generate actions in one denoising step. One-step is a speed/quality trade-off, not uniform superiority. Real tests are small; completion time is video-estimated on successes only. H20 and compiled RTX5090 latency numbers use different setups; NAVSIM is not real-road deployment.

## Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy

- [arXiv 2610.35832](https://arxiv.org/abs/2610.35832) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35832)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35832)

EBench profiles Astra direct waypoint control versus selective invocation of frozen VLA/WAM policies under RGB/proprioceptive observations and one annotated demonstration per task. No cross-episode memory. 31/510 episodes use a demonstration from the same test scene. Two tasks allow 3,000 steps direct versus 5,000 hybrid; correcting that changes hybrid means to 52.4%/55.8%. Policy calls cannot receive agent-written subgoals; compute is unbounded and comparisons run once/episode.

## Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent

- [arXiv 2610.35817](https://arxiv.org/abs/2610.35817) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35817)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35817)

ZAP trains a 27B VLM via successful-trace SFT and simulation GRPO to use a shared perception/pose-control tool interface; semantic pretraining and learned motion are tested compositionally without real robot training trajectories. Only 30 real trials/model. Harness supplies SAM3.1 segmentation, calibrated depth-derived 3D readouts and controller feedback; not RGB-only end-to-end control. Real robot calibration informs simulation. Cost assumes one B300 at $7.10/hour; Franka transfer is not real hardware.

## SPECOLA: A Tool for Specification Driven Robot Evaluation

- [arXiv 2610.35730](https://arxiv.org/abs/2610.35730) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35730)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35730)

Specola exposes simulator signals to Signal Temporal Logic monitors, measuring satisfaction margins and persistence alongside task success; provides APIs and adapters for nine simulators/benchmarks. Privileged simulator state and user-written predicates define the conclusions; results do not certify physical safety. Fixed-period monitoring does not yet handle asynchronous, uncertain real sensors. A stricter persistence requirement changes evaluation semantics, not the original benchmark score.

## Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies

- [arXiv 2610.35626](https://arxiv.org/abs/2610.35626) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35626)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35626)

Builds a robot-aligned 3 D Gaussian scene from wrist-camera captures, renders feasible smooth reaching trajectories, and fine-tunes a VLA with an instruction-conditioned proximity verifier for termination. Ten times more synthetic trajectories; under 10 min active capture still entails about 200 min total, comparable to 150-demo teleoperation. Only pre-contact reaching is learned; precision is validated by a fixed downstream grasp routine. Three targets, 25 trials each and moderate motherboard repositioning do not establish arbitrary layout or contact-task generalization.

## RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies

- [arXiv 2610.35604](https://arxiv.org/abs/2610.35604) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35604)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35604)

RoboDoctor connects diagnosis, policy/agent control allocation, selective intervention and contact-method revision through persistent records of rationale, attempted methods, outcomes and reuse conditions. Retrospective highest-score selection mixes source runs without uniform versions, checkpoints or inference budgets. Warmup already uses assistance and memory. No matched reset-memory control, consolidated cost analysis or real-robot validation; results do not establish causal memory benefit.

## Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data

- [arXiv 2610.35075](https://arxiv.org/abs/2610.35075) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35075)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35075)

Uses smartphone scene reconstruction, agentic simulation construction and motion/environment co-adaptation to generate humanoid manipulation data without real robot demonstrations. The headline 20-point advantage compares unequal demonstration counts. Broader coverage also changes training distribution; it is not a matched-data improvement.

## VISTA: Active Exploration for Self-Improvement in Embodied Agents

- [arXiv 2610.35051](https://arxiv.org/abs/2610.35051) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35051)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35051)

VISTA evolves executable robot-agent harnesses using an ancestry graph, active diagnostic interactions and fresh autonomous evaluation of frozen candidate packages, without updating model weights. Simulation only. Task-specific selection and best-so-far curves do not prove unseen-task generalization or monotonic candidate improvement. Up to 100 planner turns and 10,000 physics steps on LIBERO-Pro/RoboTwin; development compute is substantial and baseline budgets must not be assumed matched.

## JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies

- [arXiv 2610.35010](https://arxiv.org/abs/2610.35010) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35010)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35010)

Freezes the base policy and learns a 79, 817-parameter conditional energy; values rank discrete proposals and action gradients refine continuous outputs. Each benchmark trains separate adapter weights and encodings. Simulation only; no matched LoRA comparison. Reported counts are rounded averages over five seeds, not raw independent trial counts. Gains require feedback/expert-derived supervision and benchmark-specific validation; the compact adapter excludes frozen-policy inference and rollout costs.

## VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware

- [arXiv 2610.34717](https://arxiv.org/abs/2610.34717) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34717)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34717)

Profiles 18 released VLA models, 19 configurations and seven inference stages on Jetson AGX Thor and AMD Ryzen AI Max+ PRO 395, separating action generation, backends and host preprocessing. Timing is not a closed-loop success benchmark: inputs are a shared LIBERO observation plus 24 frames from one episode, with 20–100 timed calls. Models retain different native chunk/execution settings. Compilation can change gripper commands; low-bit action similarity does not establish preserved task success.

## RobotAgentBench: Towards Open-world Robot Autonomy

- [arXiv 2610.34649](https://arxiv.org/abs/2610.34649) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34649)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34649)

RobotAgentBench evaluates task discovery, context reasoning, manipulation, recovery and robustness plus open-ended household scenarios, comparing coding, learned and hybrid planning/execution/verification architectures. Scores are capability/scenario aggregates, not a universal task success rate. Main results are simulation; matched physical subsets cover only selected systems, not the best hybrid/RSI rows. Open-ended scores remain low and standalone versus agents differ in interfaces.

## TRIAGE: Efficient Vision-Language-Action Inference Needs Both Reuse and Pruning

- [arXiv 2610.34519](https://arxiv.org/abs/2610.34519) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34519)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34519)

A training-free token allocator recomputes a fixed budget, reuses low-drift young KV caches and prunes invalid leftovers; drift thresholds are calibrated per backbone. Two OpenVLA-family backbones, simulation success tests and replay-stream hardware timings; no real-robot closed-loop test. Thresholds are empirically tuned; selected SimplerEnv tasks exclude floor-level full-recompute performance. The 48% headline reduction is prefill, not total control latency.

## Scaling Dexterous Manipulation via Action Representation Pretraining

- [arXiv 2610.34453](https://arxiv.org/abs/2610.34453) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34453)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34453)

ARPG pretrains action representations against visual features on human manipulation data, freezes the encoder, and trains a 130M generative backbone plus decoder in that representation space. DexJoCo baselines are taken from its original paper; real evaluation has three tasks and 30 trials each. Same robot demos do not imply matched optimization: π0.5 uses 25k-step mixed LoRA, while ARPG has separate encoder/decoder training and up to 120k downstream steps. Hours sum clip durations, potentially counting overlaps; open-world semantics and gripper transfer remain untested.

## RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions

- [arXiv 2610.34356](https://arxiv.org/abs/2610.34356) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34356)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34356)

RynnLAM extracts continuous latent actions using residual visual prediction, camera-compensated 3D flow and camera-motion decoupling; a flow-matching VLA learns from 30.1K video hours before native-action adaptation. Full-scale comparisons do not match pretraining data/compute; scaling does not isolate optimization exposure. Geometry is pseudo-labeled, not proof of metric or causal action identification. Real adaptation uses 3,850 demos. Main RoboTwin table/abstract say 88.6%, while the conclusion says 88.3%; no inference-speed benchmark is provided.

## AdaPolicy: Action-Driven Anticipatory Robot Policies via Next-Chunk Prediction

- [arXiv 2610.34280](https://arxiv.org/abs/2610.34280) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34280)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34280)

Adds a training-only EMA action head that predicts the next action chunk from an evolved latent state; its loss backpropagates through that state into the online policy, without future-image supervision. Real precision tasks use 1, 000/400 demonstrations, with human takeover corrections comprising 20% of each dataset; both methods use the same combined data. These are supervised anticipatory features, not evidence of autonomous online world-model adaptation; zero inference overhead is relative to the matched architecture.

## Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models

- [arXiv 2610.34251](https://arxiv.org/abs/2610.34251) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34251)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34251)

CogMemory adds a 3.45M-parameter history module: a selective state-space encoder, multi-slot temporal aggregation and variational compression, followed by gated cross-attention retrieval into two VLA fusion architectures. Simulation only and appendix specifies one seed (42), without multi-seed uncertainty. Policies and memory are optimized end-to-end for 30k steps on eight L20X GPUs, not an inference-only memory add-on. Best validation checkpoints are selected every 1k steps. Claimed 21.2→12.9s efficiency is task execution time on jointly successful cases, not measured model latency.

## HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

- [arXiv 2610.34186](https://arxiv.org/abs/2610.34186) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34186)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34186)

Trains OFT-, GR00T- and π-style humanoid policies on 2,087 hours of human/simulated/robot data, predicting SONIC whole-body motion tokens plus hand signals; simulation supplies pseudo-proprioception and rendering replaces human arms during adaptation. One real task, fixed pretrained whole-body controller and full-parameter downstream tuning. Visual adaptation adds only two successful trials; pseudo-proprioception hurts OFT because its text state is truncated. Reported stages 1–2 take about 38+12 hours on eight GPUs; gains do not isolate additional data from pretraining compute.

## PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy

- [arXiv 2610.34147](https://arxiv.org/abs/2610.34147) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34147)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34147)

Conditions deformable-linear-object policies on textual physical-property priors and distills future visual features into an action expert. Separate policies are trained for different embodiments. Future observations are used in training, not an online predictive world-model interface.

## RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models

- [arXiv 2610.34108](https://arxiv.org/abs/2610.34108) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34108)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34108)

RoboDuo lets a full-task VLA attempt the task, checks completion, then uses a separately trained atomic VLA through generated code to recover unfinished steps while keeping the full-task policy frozen. Not training-free overall: atomic policy and completion-checking coding agent use derived demonstration datasets. Gains shrink with five-suite training; real evaluation is one task family with small counts. Published reference rows use different protocols and are not matched reruns.

## X-World: Transferring Video Priors to Variable-View Robot Control

- [arXiv 2610.34105](https://arxiv.org/abs/2610.34105) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34105)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34105)

Transfers a video backbone to variable-view control with residual cross-view attention, a layer-aligned Q-Former and shared action expert with native dataset interfaces. Reference baselines do not match pretraining data/compute. Camera, background and noise shifts remain weaker than OpenVLA-OFT; LIBERO-Plus weighting is unspecified. One physical platform, no demonstrated unseen-embodiment transfer.

## TurboWAM: Learning What Matters for Fast World Action Models

- [arXiv 2610.33941](https://arxiv.org/abs/2610.33941) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33941)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33941)

Selectively aggregates early world-model layers conditioned on noisy actions and modulates action gradients during training, retaining video co-training without test-time video generation. Benchmarks have unmatched embodied pretraining across methods. Prompt-corrected results must not be conflated with the original protocol. Layer structure is architectural, not explicit 3D geometry; latency alone does not establish safe control. GPU model is unspecified (approximately 140GB data-center GPU). Physical-robot experiments are referred to supplementary material; their quantitative results were not established in the checked text.

## Late Breaking Results: Audio-Language-Action Models with Direct Speech Conditioning for Robotic Manipulation

- [arXiv 2610.33866](https://arxiv.org/abs/2610.33866) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33866)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33866)

Speech-π0.5 pools a frozen speech encoder into 32 VLM tokens and uses separate audio/task LoRA adapters, with speech–text distillation followed by action training. Two-page DAC late-breaking report; simulation and synthetic voices only, 500 episodes per suite/condition. The 3× latency gain trades off lower success than ASR, and timing does not separately account for speech capture or encoder cost. Training uses 100k synthesized instructions; compute/multi-seed details are limited.

## POD-RoPE: Rotary Position Encoding over Physical Observation Distributions for Embodied AI

- [arXiv 2610.33745](https://arxiv.org/abs/2610.33745) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33745)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33745)

Encodes each token’s camera-center, ray-direction and time footprint as a distribution; expected rotations affect attention Q/K matching and coherence-aware V/O aggregation without expanding sequence length. Real evaluation has only 20 trials per task and uses 1, 694 training trajectories, 64 H20 GPUs and the 20 k-step checkpoint. Geometry depends on camera calibration/kinematics; block timing is not robot end-to-end latency, and visual geometry gains are not uniform across tasks.

## EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models

- [arXiv 2610.33685](https://arxiv.org/abs/2610.33685) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33685)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33685)

Factorizes human/robot actions into shared position codes and embodiment-specific kinematics, then co-trains a VLM on shared tokens before robot-action fine-tuning. Adds 50k tokenizer and 30k co-training steps on eight A800s; the baseline omits these stages, so compute is not matched. Real evaluation uses 2,450 demonstrations and only 10 trials per condition. The ablation section inconsistently calls a 73.2% row the same baseline reported as 66.8% in the main table.

## Power-of-Two Leaky Integrate-and-Fire Neurons for Event-Driven Vision-Language-Action Inference

- [arXiv 2610.33658](https://arxiv.org/abs/2610.33658) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33658)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33658)

Replaces selected π0.5 projections with signed power-of-two spiking events and residual membrane state; Heartbeat confines event extraction to each projection while preserving external token/cache interfaces. No measured hardware energy or latency. The 86.95% saving is an illustrative FP32 projection-arithmetic model excluding memory, control and encoding; a matched FP8 model with fixed movement budget estimates only 32.79% subtotal saving at T=1. Evaluation uses one seed and simulation; nonsignificance does not establish equivalence.

## Tiny Recursive Policy: Recursive Latent Refinement for Visuomotor Control

- [arXiv 2610.33288](https://arxiv.org/abs/2610.33288) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33288)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33288)

A small behavior-cloning policy repeatedly refines two shared latent states within each prediction and carries them between control steps; training detaches temporal gradients. Simulation only; LIBERO-Mem reports subgoal completion, not binary task success. Parameters count only the backbone and do not measure inference cost: the default uses three high-level cycles and six low-level refinements. Perturbation training improves robustness but lowers clean Mem score to 0.480.

## AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models

- [arXiv 2610.33074](https://arxiv.org/abs/2610.33074) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33074)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33074)

Allocates matrix-level bitwidths using action sensitivity and a measured weight-recovery cost proxy; per-channel calibration and grouped lossless coding reduce storage while weights are recovered to BF16 block by block. One model, simulation only; 150 episodes per suite and timing over ten inputs excludes preprocessing/postprocessing. Baselines are literature reports; the official repository clarifies its 96.9% reference is FP16 despite the paper’s BF16 label. W1.5* means W4 vision plus average-W1.5 language, not a 1.5-bit complete model. Compression increases latency.

## One-shot Human Video-Guided Adaptation for Vision-Language-Action Models

- [arXiv 2610.19746](https://arxiv.org/abs/2610.19746) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.19746)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2610.19746)

v1→v2 adds two adapted video-conditioning baselines, fills previously incomplete ablation results, and replaces the five-trial real-robot table with ten-trial results. Main RoboTwin CapPro performance was already in v1. The added baselines are adaptations to π0.5, not unchanged original systems. Ten trials per physical task remain small; hard sorting succeeds only 20%. One-shot refers to target-time human-video guidance, not training from one demonstration overall; source-task training remains.

## What Can One Sentence Fix? A Failure Taxonomy and a Minimal Language Correction for Frozen VLA Policies

- [arXiv 2608.29967](https://arxiv.org/abs/2608.29967) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2608.29967)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2608.29967)

v1→v2 retitles/reframes CorrectVLA and replaces the small real-robot table with three 10-trial runs per condition, adds long-horizon negative controls, and explicitly separates failure-only retry recovery from all-episode net success. Simulation recoveries of 65/139 and 33/328 are inherited. A person labels the failure mode and writes a timed correction per failing run, taking 40–80 seconds; additional correction rounds may be used. Retry-only simulation success does not establish unconditional policy improvement. The channel fixes magnitude/timing, not missing semantic targets or plans; LIBERO-90 is instruction-OOD, not scene-OOD.

## SentryVLA: Uncertainty-Guided Action Selection and State Monitoring for Vision-Language-Action Robotic Control

- [arXiv 2604.16677](https://arxiv.org/abs/2604.16677) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2604.16677)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2604.16677)

v1→v2 adds a formal marginal-coverage proposition and sharply scopes CQR claims to exchangeable frame–candidate calibration samples; it also adds explicit calibration diagnostics and action-score design details. This is a substantive reliability-claim clarification, not a new safety guarantee. The guarantee does not extend to adaptive selected actions, temporally correlated closed-loop states, shifted distributions or task success. Monitoring thresholds and OOD findings remain empirical. No independent reproduction of the calibration experiment.

## ActECC: Action Chunk Temporal Harnessing for Edge-Cloud Collaborative VLA Inference System

- [arXiv 2603.07949](https://arxiv.org/abs/2603.07949) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2603.07949)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2603.07949)

v2→v3 changes RAPID into ActECC: the emphasis shifts from edge–cloud partitioning to kinematics-guided usable action-chunk ranges and delay-aware replanning scheduling. It replaces the evaluation with π0.5/GR00T N1.5 system results; the prior 1.73× headline is not directly comparable. Evaluation measures deviation from aligned expert trajectories, explicitly not task success. It is a simulation/system study; cloud-only can have lower latency than ActECC. The two headline maxima arise from different comparisons, and should not be combined into one configuration.

## RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

- [arXiv 2610.32971](https://arxiv.org/abs/2610.32971) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32971)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32971)

Unifies 17 robust/safe RL algorithms and six standard references, with reusable interfaces and individual/compound deployment shifts including latency and semantics. Not every algorithm runs every task. Methods retain native budgets, and pooled-family comparisons mix backbone strength with robustness mechanisms. The π0.5 study uses one fine-tuned model and offline joint-space demonstration tracking, not closed-loop VLA task success or real-robot validation.

## RynnUnify: Towards Unified Embodied Brain

- [arXiv 2610.32965](https://arxiv.org/abs/2610.32965) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32965)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32965)

A Cosmos3-based 16B model couples an 8B reasoner and 8B video generator. Cross-chunk scene frames support interleaved visual planning; a separately RL-trained reasoner chooses whether to request generated evidence, and WAM adaptation adds joint video-action learning. Robot adaptation uses roughly 1,600 hours of atomic and 177 hours of composite RoboCasa data. Full-split baseline numbers are imported from reports, whereas Selected-20 is evaluated by the authors. Visual history is within-episode context, not demonstrated lifelong memory; three real tasks do not isolate memory’s contribution.

## If at First You Don’t Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

- [arXiv 2610.32941](https://arxiv.org/abs/2610.32941) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32941)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32941)

Trains a small failure head on frozen-policy rollouts and reverses achieved arm motion before retrying. Simulation only; pooled results include configuration-selection seeds. Held-out pi0.5 uplift is 0.70 points. Reversal does not restore objects or guarantee safety, and the head requires labeled rollouts.

## Retiming Robot Demonstrations with a Learned Speed Prior

- [arXiv 2610.32676](https://arxiv.org/abs/2610.32676) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32676)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32676)

Learns a transferable distribution over demonstration speed, retimes trajectories to faster observed paces, and pairs a tempo-predicting VLA with constraint-aware real-time trajectory execution. Needs offline policy training and a specialized execution controller, not a drop-in inference-speed tweak. The prior cannot exceed demonstrated paces. Some success gains can arise from timeouts; the authors use matched speed to control this. SAIL numbers use a different robot and policy.

## When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

- [arXiv 2610.32431](https://arxiv.org/abs/2610.32431) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32431)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32431)

MART-GRPO uses a fine-tuned, then frozen VLM to locate the last visible unrecovered error in full rollout videos and truncate subsequent failure penalties, retaining successful-rollout terms and original normalization. Ideal stopping results motivate, but do not certify, the retrospective implementation. Simulation only. The actor sees one camera while the VLM reviews three; additional annotations and VLM fine-tuning are required. Boundaries use future rollout information and need not satisfy ideal stopping assumptions. One task declines by 1.95 points; held-out scene seeds are not independent training seeds.

## LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners

- [arXiv 2610.32348](https://arxiv.org/abs/2610.32348) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32348)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32348)

Pairs an immutable execution log and verbatim note history with expectation-gated action frames and skim-then-inspect demonstrations. GPT-6 Astra plans either waypoints or grounded π0.5 subgoals; the memory is an inference-time interface, not parameter adaptation. The clean memory comparison demonstrates cost savings, not a clear success gain. Full-system gains also change action/call interfaces; direct control uses depth, calibration and task notes derived from success-checking code. One simulated benchmark and proprietary model, no real robot. Single-component failures differ by only 2–4 episodes.

## MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation

- [arXiv 2610.32312](https://arxiv.org/abs/2610.32312) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32312)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32312)

Combines skill-conditioned LoRA experts with RGB-D trajectory-affordance heatmaps that bias action attention. MAST additionally receives depth, unlike RGB-only baselines; gains cannot isolate architecture alone. Instructions arrive per primitive, not as an autonomously decomposed long task. Geometry failures and execution drift remain.

## Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems

- [arXiv 2610.32208](https://arxiv.org/abs/2610.32208) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32208)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32208)

Uses sparse autoencoder features of OpenVLA activations for failure prediction and VLM-generated behavioral interpretations, with branching rollouts estimating a point of no return. Simulation and one policy only. Unsupervised SAE fitting uses all 500 trajectories; supervised predictors use held-out splits. Four branches per probe give coarse, remaining-budget-dependent recoverability. Outcome associations are not causal failure mechanisms or validated safety interventions.

## Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies

- [arXiv 2610.32102](https://arxiv.org/abs/2610.32102) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32102)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32102)

Jointly studies executed action horizon and flow-solver depth, testing when shallow sampling helps or harms. Long open-loop execution fails on moving targets; speedup is amortized inference cost, not guaranteed wall-clock task acceleration. The paper inconsistently describes simulation task totals and pi0.5 chunk configurations.

## TTT in VLA Models: Exploring Training with Human Demonstrations

- [arXiv 2610.32094](https://arxiv.org/abs/2610.32094) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32094)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32094)

Integrates fast-weight TTT into InternVLA-A1 and pi0.5, documenting human-to-robot memory transfer and truncated gradient paths. Negative findings are limited to small cup-selection datasets and tested recipes, not a disproof of TTT. Trial counts are insufficiently reported. Autoregressive-state evaluation still uses recorded images, not closed-loop observations.

## DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

- [arXiv 2610.32093](https://arxiv.org/abs/2610.32093) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32093)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32093)

Uses privileged, latent-conditioned RL with a reverse curriculum and success-gated diversity to generate filtered demonstration datasets, then trains a visuomotor π0.5 policy rather than deploying the RL generator. Requires accurate simulation, privileged states, reset access and task success signals. Hardware evidence covers four simple tabletop tasks with modest transfer gaps and only one training seed; excessive diversity can hurt competence.

## Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates

- [arXiv 2610.31859](https://arxiv.org/abs/2610.31859) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31859)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31859)

Audits update rounding when trainable matrices and AdamW state remain bf16 without fp32 master weights. One suite and shortened schedules; precision of optimizer moments is not separately ablated. SmolVLA scorer discrepancies restrict cross-paper comparisons. This does not show every bf16 computation or JAX training setup is affected.

## EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions

- [arXiv 2610.31845](https://arxiv.org/abs/2610.31845) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31845)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31845)

Combines reliability-dependent corruption and loss weighting with joint vision–action flow and privileged-future EMA distillation to learn from noisy human action labels. External RoboCasa baselines use published results with different pretraining and budgets. The real π0.5 baseline replaces input/output projections for 58 DoF, confounding attribution. Action labels remain required, and source weighting does not correct systematic retargeting bias.

## ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

- [arXiv 2610.24512](https://arxiv.org/abs/2610.24512) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.24512)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2610.24512)

A benchmark of eight contact-rich skill categories, 36 reference tasks and over 40 printable assets with corresponding simulation components; six tasks evaluate vision-only and visual-tactile learned policies. The four systems differ in pretraining, observation histories and tactile interfaces, so this is not a perfectly isolated tactile-modality ablation. Only six of 36 tasks receive learned-policy evaluation. Velcro stabilization enables one-arm tasks that could otherwise require another arm. Rigid/articulated printed assets do not cover deformable contact; negative tactile results apply to the tested policies and sensors, not touch in general.

## RAPAC-DP: Response-Aligned Pending-Action Compensation for Diffusion Policies under Delayed Execution

- [arXiv 2608.15924](https://arxiv.org/abs/2608.15924) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2608.15924)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2608.15924)

A frozen diffusion/flow policy gains a pending-action encoder and LoRA compensation that aligns each output chunk to its scheduled execution time, trained using delay-conditioned samples from delay-free demonstrations. Only one checkpoint per method/task is tested, so confidence intervals describe trial variation rather than training-seed robustness. Fixed conveyor speed/starts and injected discrete delays limit claims about arbitrary network jitter. At low delay it trails RTC on dynamic grasping (73.3% versus 76.7%); the method requires training an adapter.

## Semantic Anchoring for Robotic Action Representations

- [arXiv 2607.13597](https://arxiv.org/abs/2607.13597) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.13597)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2607.13597)

An auxiliary alignment objective preserves task-level semantics during VLA fine-tuning through shared/private representations anchored to a frozen manipulation-text encoder; auxiliary modules are removed at inference. Correlations do not establish semantic erosion as the sole cause of OOD failure. Architectures use different official fine-tuning recipes. The fixed semantic encoder bounds the method, shared/private factors are not identifiable, and this is downstream fine-tuning rather than continual deployment adaptation.

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

