# Manipulation and real-robot transfer

[English](manipulation-transfer.md) | [简体中文](manipulation-transfer.zh-CN.md) | [All topics](README.md)

113 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

## Learning Force-Reactive Humanoid Loco-Manipulation

- [arXiv 2610.35862](https://arxiv.org/abs/2610.35862) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35862)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35862)

Collects robot-free force-aware demonstrations and combines a diffusion pose/force policy with hybrid-compliance whole-body control. Small task/trial coverage and force-sensing hardware requirements limit generality; the ablations do not establish unrestricted contact-skill transfer.

## OSWAM: An Effective World Action Model with One-Step Action Generation

- [arXiv 2610.35850](https://arxiv.org/abs/2610.35850) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35850)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35850)

Uses action/scene imagination tokens for structured diffusion initialization and privileged future-conditioned distillation to generate actions in one denoising step. One-step is a speed/quality trade-off, not uniform superiority. Real tests are small; completion time is video-estimated on successes only. H20 and compiled RTX5090 latency numbers use different setups; NAVSIM is not real-road deployment.

## Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent

- [arXiv 2610.35817](https://arxiv.org/abs/2610.35817) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35817)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35817)

ZAP trains a 27B VLM via successful-trace SFT and simulation GRPO to use a shared perception/pose-control tool interface; semantic pretraining and learned motion are tested compositionally without real robot training trajectories. Only 30 real trials/model. Harness supplies SAM3.1 segmentation, calibrated depth-derived 3D readouts and controller feedback; not RGB-only end-to-end control. Real robot calibration informs simulation. Cost assumes one B300 at $7.10/hour; Franka transfer is not real hardware.

## Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies

- [arXiv 2610.35626](https://arxiv.org/abs/2610.35626) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35626)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35626)

Builds a robot-aligned 3 D Gaussian scene from wrist-camera captures, renders feasible smooth reaching trajectories, and fine-tunes a VLA with an instruction-conditioned proximity verifier for termination. Ten times more synthetic trajectories; under 10 min active capture still entails about 200 min total, comparable to 150-demo teleoperation. Only pre-contact reaching is learned; precision is validated by a fixed downstream grasp routine. Three targets, 25 trials each and moderate motherboard repositioning do not establish arbitrary layout or contact-task generalization.

## Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data

- [arXiv 2610.35075](https://arxiv.org/abs/2610.35075) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35075)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35075)

Uses smartphone scene reconstruction, agentic simulation construction and motion/environment co-adaptation to generate humanoid manipulation data without real robot demonstrations. The headline 20-point advantage compares unequal demonstration counts. Broader coverage also changes training distribution; it is not a matched-data improvement.

## How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder: A Hierarchical, Matched Sim-Real Benchmark for Physical Interaction

- [arXiv 2610.34527](https://arxiv.org/abs/2610.34527) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34527)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34527)

PhysLadder defines 16 matched sim/real contact-rich tasks at three cumulative levels: contact geometry, sustained force regulation, and force regulation coordinated with contact reconfiguration. One model and very small per-task samples; agreement does not establish universal sim-to-real ranking validity. Simulation contact/material parameters are not measured physical properties; real and simulated model-call counts use different action interfaces.

## Scaling Dexterous Manipulation via Action Representation Pretraining

- [arXiv 2610.34453](https://arxiv.org/abs/2610.34453) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34453)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34453)

ARPG pretrains action representations against visual features on human manipulation data, freezes the encoder, and trains a 130M generative backbone plus decoder in that representation space. DexJoCo baselines are taken from its original paper; real evaluation has three tasks and 30 trials each. Same robot demos do not imply matched optimization: π0.5 uses 25k-step mixed LoRA, while ARPG has separate encoder/decoder training and up to 120k downstream steps. Hours sum clip durations, potentially counting overlaps; open-world semantics and gripper transfer remain untested.

## ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation

- [arXiv 2610.34370](https://arxiv.org/abs/2610.34370) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34370)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34370)

ThinkLocoManip interleaves reasoning and action over perception, navigation, manipulation and whole-body locomotion tools; keyframe thinking retains execution context for recovery. Five task families on one platform, 10–20 trials per task. Tool orchestration includes engineered navigation/grasp/control capabilities; these results do not isolate cross-episode skill acquisition or establish portability of the whole-body controller.

## RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions

- [arXiv 2610.34356](https://arxiv.org/abs/2610.34356) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34356)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34356)

RynnLAM extracts continuous latent actions using residual visual prediction, camera-compensated 3D flow and camera-motion decoupling; a flow-matching VLA learns from 30.1K video hours before native-action adaptation. Full-scale comparisons do not match pretraining data/compute; scaling does not isolate optimization exposure. Geometry is pseudo-labeled, not proof of metric or causal action identification. Real adaptation uses 3,850 demos. Main RoboTwin table/abstract say 88.6%, while the conclusion says 88.3%; no inference-speed benchmark is provided.

## HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

- [arXiv 2610.34186](https://arxiv.org/abs/2610.34186) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34186)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34186)

Trains OFT-, GR00T- and π-style humanoid policies on 2,087 hours of human/simulated/robot data, predicting SONIC whole-body motion tokens plus hand signals; simulation supplies pseudo-proprioception and rendering replaces human arms during adaptation. One real task, fixed pretrained whole-body controller and full-parameter downstream tuning. Visual adaptation adds only two successful trials; pseudo-proprioception hurts OFT because its text state is truncated. Reported stages 1–2 take about 38+12 hours on eight GPUs; gains do not isolate additional data from pretraining compute.

## PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy

- [arXiv 2610.34147](https://arxiv.org/abs/2610.34147) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34147)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34147)

Conditions deformable-linear-object policies on textual physical-property priors and distills future visual features into an action expert. Separate policies are trained for different embodiments. Future observations are used in training, not an online predictive world-model interface.

## HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model

- [arXiv 2610.34126](https://arxiv.org/abs/2610.34126) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34126)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34126)

Learns a history-based proprioceptive neural dynamics model with forward-kinematics supervision, then fine-tunes humanoid tracking policies through model gradients; low-frequency reference perturbations collect deployment-viable data. Small physical repetition counts and task-specific tracking/completion metrics, not broad manipulation success. Real-world baselines are direct transfer and disturbance-aware PPO where feasible, not the full simulation baseline set. Authors limit the method to time-invariant disturbance settings; collection/training precede adapted deployment.

## RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models

- [arXiv 2610.34108](https://arxiv.org/abs/2610.34108) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34108)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34108)

RoboDuo lets a full-task VLA attempt the task, checks completion, then uses a separately trained atomic VLA through generated code to recover unfinished steps while keeping the full-task policy frozen. Not training-free overall: atomic policy and completion-checking coding agent use derived demonstration datasets. Gains shrink with five-suite training; real evaluation is one task family with small counts. Published reference rows use different protocols and are not matched reruns.

## X-World: Transferring Video Priors to Variable-View Robot Control

- [arXiv 2610.34105](https://arxiv.org/abs/2610.34105) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34105)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34105)

Transfers a video backbone to variable-view control with residual cross-view attention, a layer-aligned Q-Former and shared action expert with native dataset interfaces. Reference baselines do not match pretraining data/compute. Camera, background and noise shifts remain weaker than OpenVLA-OFT; LIBERO-Plus weighting is unspecified. One physical platform, no demonstrated unseen-embodiment transfer.

## RoboLongR: Causally Consistent Rewards Teach Robots to Progressively Master Long-Horizon Manipulation

- [arXiv 2610.33863](https://arxiv.org/abs/2610.33863) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33863)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33863)

Learns history-sensitive rewards with recurrent memory, shuffled-stage negatives and terminal correction, then fine-tunes a behavioral-cloning policy with RL. Only 10 real trials per task. Removing memory, stage shuffling or correction yields 28.9%, 24.3% or 28.4%. Online correction is used by RoboLongR and Progress+Mono, but not ReWiND or other baselines; the main comparison tests complete pipelines.

## AdaDexTrack: Dynamic Modulation for Adaptive and Generalizable Dexterous Manipulation Tracking

- [arXiv 2610.33852](https://arxiv.org/abs/2610.33852) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33852)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33852)

Adds reinforcement-learned reference, object-latent and target modulation around a distilled dexterous tracker. Completion is the average fraction of frames satisfying tracking-error thresholds, not binary whole-task success. Explicit object poses/meshes and reliable pose estimation are required; symmetric objects are challenging.

## One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation

- [arXiv 2610.33794](https://arxiv.org/abs/2610.33794) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33794)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33794)

Converts one phone scan per building into a Gaussian-splat navigation environment and grounded instruction episodes; known-scene Pareto utilities guide policy post-training without human demonstrations or a learned critic. Demonstration-free is not human-free: scanning and evaluation-instruction checking require people. Baselines have different scene-specific data budgets; unscanned means same buildings, not unseen buildings. Real success uses a 1.5m radius, and changed layouts require rescanning. This is offline scene post-training, not online per-step TTT.

## Open-World Law-to-Action: Vision-Language Priors and Touch for Parts with Hidden Physics

- [arXiv 2610.33705](https://arxiv.org/abs/2610.33705) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33705)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33705)

Combines vision-language physical-law priors, Bayesian touch-based identification and requests for additional views when observations remain ambiguous. No hardware robot validation. One embodied protocol was changed between held-out tests, so its comparison should not be treated as a clean confirmatory result.

## EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models

- [arXiv 2610.33685](https://arxiv.org/abs/2610.33685) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33685)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33685)

Factorizes human/robot actions into shared position codes and embodiment-specific kinematics, then co-trains a VLM on shared tokens before robot-action fine-tuning. Adds 50k tokenizer and 30k co-training steps on eight A800s; the baseline omits these stages, so compute is not matched. Real evaluation uses 2,450 demonstrations and only 10 trials per condition. The ablation section inconsistently calls a 73.2% row the same baseline reported as 66.8% in the main table.

## HA-DiPO: Diffusion Policy Optimization for Heterogeneous Cooperative Transport

- [arXiv 2610.33584](https://arxiv.org/abs/2610.33584) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33584)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33584)

Trains a hierarchical multi-agent diffusion policy for cooperative payload transport with centralized training and decentralized execution. The 93.5% figure is simulation, not real-robot success. Best-checkpoint selection and a narrowly defined transport controller constrain interpretation.

## RBGA: Residual-Budget Guide Arbitration for Offline-to-Online Safe Reinforcement Learning in Dexterous Manipulation

- [arXiv 2610.33494](https://arxiv.org/abs/2610.33494) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33494)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33494)

Arbitrates offline guidance and online exploration using estimated cost-to-go and remaining within-episode safety budget. The experiments replace binary costs with continuous costs. Bounds depend on estimator assumptions; hardware lacks a quantitative trial table.

## MDPO: Multi-constraint Dexterous Policy Optimization with Reinforcement Learning

- [arXiv 2610.33480](https://arxiv.org/abs/2610.33480) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33480)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33480)

Separately projects cumulative and state-wise constraints in reinforcement learning for dexterous manipulation. Hardware evidence is qualitative, not a quantified real-world safety guarantee; constraint-estimation assumptions still matter.

## MOTIO: Agentic Skill Engineering for Reality-Grounded Humanoid Loco-Manipulation

- [arXiv 2610.33446](https://arxiv.org/abs/2610.33446) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33446)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33446)

MOTIO turns human-action videos, metric 3D assets and existing robot-control interfaces into staged humanoid programs, revising them through physics feedback and human approval; generated skills also supervise BC/DAgger distillation. Human approval and task-specific engineering remain central. Physical demonstrations and simulated variation tests are not a randomized real-robot success benchmark; development time includes tool/resource waits. Distillation evidence is simulation-side.

## Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models

- [arXiv 2610.26179](https://arxiv.org/abs/2610.26179) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.26179)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2610.26179)

v2→v3 adds Appendix J disjoint-source-group evaluations: backbones are trained from scratch on training-only groups and heads selected on separate groups. This directly probes overlap concerns in the released-asset benchmarks; original headline gains are not new. Push-T shows no improvement in this stronger separation test. New task windows differ from the original benchmark (uniform Cube starts; 80-step rather than 74-step Push-T gaps); do not compare absolute rates across protocols. SE covers backbone seeds, not sampled tasks/source groups. Simulation only.

## One-shot Human Video-Guided Adaptation for Vision-Language-Action Models

- [arXiv 2610.19746](https://arxiv.org/abs/2610.19746) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.19746)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2610.19746)

v1→v2 adds two adapted video-conditioning baselines, fills previously incomplete ablation results, and replaces the five-trial real-robot table with ten-trial results. Main RoboTwin CapPro performance was already in v1. The added baselines are adaptations to π0.5, not unchanged original systems. Ten trials per physical task remain small; hard sorting succeeds only 20%. One-shot refers to target-time human-video guidance, not training from one demonstration overall; source-task training remains.

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

## BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation

- [arXiv 2605.08571](https://arxiv.org/abs/2605.08571) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2605.08571)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2605.08571)

v2→v3 adds tuned-uniform and source-mean discrepancy controls, feature-alignment diagnostics and a weight audit that explicitly limits the theory claim. The main BEACON success values mostly predate this revision. The theoretical bound motivates the objective but is not an applicable guarantee for the audited learned weights. New feature alignment is diagnostic; lower discrepancy itself does not imply higher task success, as the MMD baseline demonstrates.

## AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation

- [arXiv 2604.11674](https://arxiv.org/abs/2604.11674) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2604.11674)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2604.11674)

v2→v3 adds a real-world domain-randomization sweep, quantitative five-embodiment collection evaluation, and fixed-demo-budget ACT grasp-source controls. The multi-stage success breakdown and original four-task sim-to-real evaluation already appeared in v2. The pose sweep increases demonstrations from 300 to 1,200 to 2,700, so range and data volume are confounded; only one real task and ten trials per setting. Cross-embodiment results concern simulator trajectory collection, not learned policy transfer. Existing headline tables remain unchanged despite collection-count wording changing from 30 to 100 rollouts.

## RoboGene: Diversity-Driven Agentic Task Generation Framework for VLA Pre-training

- [arXiv 2602.16444](https://arxiv.org/abs/2602.16444) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2602.16444)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2602.16444)

v2→v3 adds broader real-robot OOD evaluation and human-effort/memory analysis (Appendix H.2/H.4), rather than merely restating the existing task-generation architecture and 18k trajectories. This is not zero-shot task transfer: target-task fine-tuning remains. Labor is estimated using fixed per-task/per-correction durations, including teleoperation and human verification; declining correction rates alone do not isolate memory causality.

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

## DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection

- [arXiv 2610.32969](https://arxiv.org/abs/2610.32969) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32969)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32969)

A portable interface uses the deployed dexterous hand, parameterized grasp skills and a learned rotation skill to collect wrist motion and native joint commands; the imitation policy receives no skill labels. Small evaluation samples; screwdriver rotation uses a separate speed metric, not the three-task success mean. Demonstration quantity and scene diversity change together. Collection skills are not an autonomously growing skill library.

## ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback

- [arXiv 2610.32966](https://arxiv.org/abs/2610.32966) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32966)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32966)

Generates G1 reference motion directly from monocular video and post-trains the diffusion generator with tracker-derived preference pairs; an autoregressive variant enables video teleoperation. These percentages measure simulated reference tracking, not real-world task completion. Fine hand poses are not modeled; real deployment evidence is qualitative, and online initialization takes about ten seconds.

## RynnUnify: Towards Unified Embodied Brain

- [arXiv 2610.32965](https://arxiv.org/abs/2610.32965) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32965)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32965)

A Cosmos3-based 16B model couples an 8B reasoner and 8B video generator. Cross-chunk scene frames support interleaved visual planning; a separately RL-trained reasoner chooses whether to request generated evidence, and WAM adaptation adds joint video-action learning. Robot adaptation uses roughly 1,600 hours of atomic and 177 hours of composite RoboCasa data. Full-split baseline numbers are imported from reports, whereas Selected-20 is evaluated by the authors. Visual history is within-episode context, not demonstrated lifelong memory; three real tasks do not isolate memory’s contribution.

## If at First You Don’t Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

- [arXiv 2610.32941](https://arxiv.org/abs/2610.32941) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32941)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32941)

Trains a small failure head on frozen-policy rollouts and reverses achieved arm motion before retrying. Simulation only; pooled results include configuration-selection seeds. Held-out pi0.5 uplift is 0.70 points. Reversal does not restore objects or guarantee safety, and the head requires labeled rollouts.

## Regularised RL improves sim-to-real transfer

- [arXiv 2610.32855](https://arxiv.org/abs/2610.32855) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32855)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32855)

Extends soft mellowmax to continuous-control actor–critic with a slowly updated reference policy and tests whether regularization improves sim-to-real robustness beyond nominal training return. Return is not success rate. Domain randomization remains necessary, and temperatures vary by task. PPO/FastTD3 are excluded from ANYmal perturbation deployment after failing a prespecified simulation safety check, so those cells are missing, not observed hardware failures. MuJoCo tuning budgets are unequal.

## Semantic Representation for Agentic Self-Play in Automated Laboratories

- [arXiv 2610.32755](https://arxiv.org/abs/2610.32755) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32755)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32755)

VERID maintains a persistent semantic laboratory twin with introspection, pre-execution simulation gates, synchronized traces and resumable state. Agents retain physical operating bounds and analytical lessons across runs. These are small case studies, not an isolated causal memory ablation: challenge instances and experimental strategies change. Uses a structured harness, internal Gemini checkpoint and operator approval gates in supervised runs. Biological discoveries and broad robot-policy transfer are not demonstrated.

## Retiming Robot Demonstrations with a Learned Speed Prior

- [arXiv 2610.32676](https://arxiv.org/abs/2610.32676) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32676)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32676)

Learns a transferable distribution over demonstration speed, retimes trajectories to faster observed paces, and pairs a tempo-predicting VLA with constraint-aware real-time trajectory execution. Needs offline policy training and a specialized execution controller, not a drop-in inference-speed tweak. The prior cannot exceed demonstrated paces. Some success gains can arise from timeouts; the authors use matched speed to control this. SAIL numbers use a different robot and policy.

## DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation

- [arXiv 2610.32330](https://arxiv.org/abs/2610.32330) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32330)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32330)

Learns temporally aligned soft slots, slot-level latent actions, and proximity–motion relations from point-cloud sequences, supplying dynamics-aware 3D representations to a diffusion policy. Simulation baselines are inherited from AFRO, and each seed selects its best evaluated checkpoint rather than an independent final test. Real error bars reflect layout variability, not training seeds; one embodiment and one task underpin the robustness tests.

## MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation

- [arXiv 2610.32312](https://arxiv.org/abs/2610.32312) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32312)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32312)

Combines skill-conditioned LoRA experts with RGB-D trajectory-affordance heatmaps that bias action attention. MAST additionally receives depth, unlike RGB-only baselines; gains cannot isolate architecture alone. Instructions arrive per primitive, not as an autonomously decomposed long task. Geometry failures and execution drift remain.

## RoboCode: Learning Reusable Action Primitives for Robot Manipulation

- [arXiv 2610.32225](https://arxiv.org/abs/2610.32225) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32225)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32225)

Learns a shared soft-compositional primitive codebook from pooled action chunks, then freezes its decoder and trains task-specific state-to-code encoders. Simulation only, with object poses/goals rather than image-language observations. Task-specific encoders are trained for the evaluated tasks; reusable codes are not evidence of online skill growth or unseen-task transfer. No multi-seed uncertainty or closed-loop trial count was established in the checked evaluation section.

## Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion

- [arXiv 2610.32143](https://arxiv.org/abs/2610.32143) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32143)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32143)

Formulates close-fitting bracelet dressing as geometric insertion and combines a finger-wise soft insertion gate with a staged curriculum, transferring a compact geometric observation interface to a bimanual robot. Bracelet is pregrasped and the mannequin stationary; deployment is slowed by about half. No force-aware observation or objective, so finger deflection is not a safety measurement. Large combined pose shifts reduce simulated success to 26/50.

## Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies

- [arXiv 2610.32102](https://arxiv.org/abs/2610.32102) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32102)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32102)

Jointly studies executed action horizon and flow-solver depth, testing when shallow sampling helps or harms. Long open-loop execution fails on moving targets; speedup is amortized inference cost, not guaranteed wall-clock task acceleration. The paper inconsistently describes simulation task totals and pi0.5 chunk configurations.

## DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

- [arXiv 2610.32093](https://arxiv.org/abs/2610.32093) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32093)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32093)

Uses privileged, latent-conditioned RL with a reverse curriculum and success-gated diversity to generate filtered demonstration datasets, then trains a visuomotor π0.5 policy rather than deploying the RL generator. Requires accurate simulation, privileged states, reset access and task success signals. Hardware evidence covers four simple tabletop tasks with modest transfer gaps and only one training seed; excessive diversity can hurt competence.

## EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions

- [arXiv 2610.31845](https://arxiv.org/abs/2610.31845) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31845)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31845)

Combines reliability-dependent corruption and loss weighting with joint vision–action flow and privileged-future EMA distillation to learn from noisy human action labels. External RoboCasa baselines use published results with different pretraining and budgets. The real π0.5 baseline replaces input/output projections for 58 DoF, confounding attribution. Action labels remain required, and source weighting does not correct systematic retargeting bias.

## FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation

- [arXiv 2610.31841](https://arxiv.org/abs/2610.31841) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31841)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31841)

A coding agent uses RGB-D and wrist force/torque logs to generate and revise Python contact-probing and force-feedback programs. Experience is retained in executable control logic, without task-specific model training. Five real tasks, one model, small trial counts. Each development run permits 20 physical rollouts and four hours; humans authorize execution, reset scenes and judge final acceptance. The ablation changes access to force feedback and routines together, not just memory. Reasoning costs 4–10 minutes per iteration.

## WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations

- [arXiv 2610.31834](https://arxiv.org/abs/2610.31834) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31834)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31834)

Constructs executable world programs from robot demonstrations, with a coding agent using replay feedback to repair scene geometry, assets, and physical interactions. Results concern recorded-trajectory replay in reconstructed simulation, not new-policy real-robot success or sim-to-real learning. Spatial metrics do not uniformly beat Astra, and component ablations cover one task, offering little evidence of a memory benefit.

## SEVI: Safe Evidential Real-World Reinforcement Learning

- [arXiv 2610.31829](https://arxiv.org/abs/2610.31829) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31829)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31829)

Adds an evidential safety critic that gates task actions using predicted violation risk and epistemic uncertainty, invoking a shared offline-trained recovery policy during online RL. Only one hardware task and two simulated tasks; no formal zero-violation guarantee. Hardware learning uses 50 successful prior demonstrations, 200 recovery demonstrations and validation-based thresholds. Final success and cumulative training incidents have different denominators.

## PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer

- [arXiv 2610.31812](https://arxiv.org/abs/2610.31812) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31812)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31812)

Transfers a jointly learned latent preference space and reward prior from labeled source tasks, then generates confidence-weighted optimal-transport pseudo-preferences for online target-task RL without target human labels. Zero-shot refers to target human feedback, not zero target interaction or training. Real trials are small; transfer assumes related preference dimensions. PEARL is modified for online learning and dimension mismatch; PrefFew receives limited source data and 100 target labels.

## KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations

- [arXiv 2610.31801](https://arxiv.org/abs/2610.31801) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31801)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31801)

Compresses shared 14-D bimanual kinematics into transition-supervised Sparse Motion Tokens at two tokens/second; a LoRA-adapted language model predicts temporal segments and descriptions, with transfer to new robots and human hands. The encoder uses whole-episode normalization and symmetric temporal context, so it is offline. Tokenizer comparisons differ in input representation and reader-training populations, not just objective. Segmentation/semantic transfer does not establish closed-loop robot-policy gains.

## FLORA: An Open Model Suite for Scaling Robotics Data Engines

- [arXiv 2610.31779](https://arxiv.org/abs/2610.31779) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31779)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31779)

An open labeling suite supplies temporal segments, intended-action captions and outcome/dense/rubric rewards for robotic data pipelines; segmentation/captioning use RL post-training, while the released reward model uses SFT. Not uniformly best across metrics; systems use different frame budgets/compute. The approximately 125× cost claim assumes GPU pricing and modeled throughput, omits deployment overhead, has unverified production GPU-hour accounting, and is not fully reference-version matched. No direct downstream policy-learning improvement is established here.

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

## WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time

- [arXiv 2607.06988](https://arxiv.org/abs/2607.06988) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.06988)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2607.06988)

Human videos write fast-weight memory in a world-action model; paired human–robot meta-training teaches the video-to-action transfer interface. These are interface variants inside one WAM, not faithful evaluations of the complete original systems. The extra interface test covers one task; FastWAM evidence is qualitative eight-frame prediction over 3.2 s, not closed-loop control transfer. Some alternatives rely on pretrained skill latents absent from meta-training-only insertion.

## GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

- [arXiv 2607.05369](https://arxiv.org/abs/2607.05369) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.05369)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2607.05369)

GaP composes typed robot skill graphs and improves their structure, parameters and throughput through simulation rehearsal before deployment. New throughput evidence is simulation, not a new real-robot productivity result. The paper explicitly says CaP-X is not a fair standalone comparison because available environment geometry differs. MORSL equalizes selected perception/grasp components, not all motion primitives, inference budgets or system choices. The tasks are mostly quasi-static.

## Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration

- [arXiv 2605.31196](https://arxiv.org/abs/2605.31196) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2605.31196)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2605.31196)

TouchSafeBench evaluates current collision recognition and early warning in simulated human–robot co-presence, separating robot–scene and human-contact risks. The real recordings contain no physical contact and use a human head-mounted camera; labels are binary proximity at a 1 m threshold, not actual collision safety. False-alarm estimates use only 12 hard negatives. Prompt tests repeat one model/condition; one expert saw viewpoint conditions in fixed order. No closed-loop safety intervention is validated.

## METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

- [arXiv 2610.31656](https://arxiv.org/abs/2610.31656) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31656)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31656)

METTA separates fast gradient-updated within-episode neural memory from compact cross-episode summaries. It reports over 50% success on held-out Meta-World ML10/45 task families and better long-context sparse-reward exploration.

## Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models

- [arXiv 2610.31569](https://arxiv.org/abs/2610.31569) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31569)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31569)

Echo jointly denoises actions plus stop/failure signals. Structured attention and faster signal denoising let cleaner status estimates guide action generation. Success, failure and recovery trajectories supply supervision without frame-level progress labels. Real-world scores are not success rates. Action supervision and training budgets are matched, but Echo receives extra failure-status data. Cross-method comparisons focus on flower insertion with adapted protocols; two tasks have no failed evaluation episodes. Benefits from higher-level stopping or replanning integration remain untested. The three-second outcome-window F1 does not imply instantaneous failure detection; simulation status accuracy covers ongoing/success frames under a specified window, not general three-class failure detection.

## FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models

- [arXiv 2610.31423](https://arxiv.org/abs/2610.31423) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31423)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31423)

Predicts future interaction intent from multimodal observations, state and action history to route global and wrist views in π0.5, using trajectory-derived weak labels. The real-robot gain is 13.3 percentage points. Cross-embodiment and diverse camera configurations remain untested; the added module requires training.

## PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning

- [arXiv 2610.31299](https://arxiv.org/abs/2610.31299) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31299)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31299)

PiHand distills simulated mocap-tracking experts into a goal-conditioned hand–object latent prior, then learns bounded residual exploration in that latent space. The same interaction prior supports new objects, trajectories, catching and bimanual handovers.

## Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

- [arXiv 2610.31166](https://arxiv.org/abs/2610.31166) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31166)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31166)

WholeBodyMem selects historical frames from SAM3 object events and supplies object spatiotemporal tokens and memory attention to a whole-body action expert. This is within-episode perceptual history, not cross-episode skill accumulation. Physical tests have only ten trials per task and no uniform-memory real-robot comparator. Missed SAM3 detections and tracking overhead remain limitations.

## UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry

- [arXiv 2610.30991](https://arxiv.org/abs/2610.30991) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30991)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30991)

Three experts jointly model future vision, 3D scene flow and actions under ten objectives; deployment requires no flow input. 58.9% is the best evaluation seed; 87.7% uses the best evaluated checkpoint. Real policies are task-specific and starts remain within demonstration coverage; flow pseudo-labels are noisy.

## In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

- [arXiv 2610.30988](https://arxiv.org/abs/2610.30988) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30988)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30988)

Generative point-cloud completion feeds context-conditioned Transformer dynamics that rank flow-matching action proposals, without test-time weight updates. No real-robot policy comparator; success uses point-cloud-distance thresholds. PCN has better CD/EMD, whereas this method favors correspondence MSE. Dynamic motions and closed-loop replanning remain untested.

## TEAR: Task-Evidence Authority Routing for Robotic Manipulation

- [arXiv 2610.30819](https://arxiv.org/abs/2610.30819) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30819)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30819)

TEAR combines network measurements, CLIP task cues and recent robot state in a causal temporal router that allocates authority between human teleoperation and local VLA control. Real trials were supervised: four manual switches occurred across two episodes. Evidence covers two related tasks and synthetic network impairment, with separately trained routers. Offline handoff F1 is 0.308 but recall only 0.286, below the rule baseline's 0.429. No official code link was located.

## Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation

- [arXiv 2610.30810](https://arxiv.org/abs/2610.30810) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30810)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30810)

ALMA trains historical context with action-conditioned future-response prediction and uses LLM-generated arm-motion structures to expand RL training tasks based on failures. Deployment weights are fixed; adaptation is contextual, not test-time gradient training. Physical comparison is only against PID, so the 79.6% reduction is not relative to the strongest simulation baseline. Contact-force control remains future work.

## DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models

- [arXiv 2610.30781](https://arxiv.org/abs/2610.30781) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30781)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30781)

DeXplicit predicts object-centric motion and deformation in metric 3D before rendering action-conditioned video. Matched-input comparisons reduce long-horizon moved-point error 27–40% versus adapted PointWorld; explicit geometry improves object fidelity.

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

## The Bitter Lesson Comes to Robotics

- [arXiv 2610.25287](https://arxiv.org/abs/2610.25287) · v2 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.25287)
- Coverage history: [2026-10-23 (v2, revised)](../daily/2026-10-23.md#arxiv-2610.25287)

The Bitter Lesson Comes to Robotics compares frontier language models directly controlling physical YAM arms under a 40-action budget. The revision expands seven models/twelve settings to nine models/fifteen settings and updates the historical performance fit.

## HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation

- [arXiv 2604.07993](https://arxiv.org/abs/2604.07993) · v3 · [Latest entry](../daily/2026-10-23.md#arxiv-2604.07993)
- Coverage history: [2026-10-23 (v3, revised)](../daily/2026-10-23.md#arxiv-2604.07993)

HEX combines canonical body-part states, a mixture-of-experts proprioceptive predictor, compact visual history and flow-matching actions for humanoid whole-body manipulation. This revision adds two household long-horizon tasks, a ψ0 comparison, OOD pretraining tests and data-scaling/sensitivity experiments.

## Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models

- [arXiv 2602.12628](https://arxiv.org/abs/2602.12628) · v5 · [Latest entry](../daily/2026-10-23.md#arxiv-2602.12628)
- Coverage history: [2026-10-23 (v5, revised)](../daily/2026-10-23.md#arxiv-2602.12628)

RL-Co combines sim/real supervised warm-starting with simulator RL anchored by real-data supervision. The new revision adds a stronger rollout-distillation control and makes the limited real-world statistical protocol explicit.

## CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation

- [arXiv 2610.30117](https://arxiv.org/abs/2610.30117) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30117)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30117)

Contact-wrench history improves force-sensitive manipulation under matched ablations, but hand-set gains and larger contact forces prevent a general safety claim.

## Asymmetric On-Policy Distillation Learns In-Context Exploration

- [arXiv 2610.30105](https://arxiv.org/abs/2610.30105) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30105)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30105)

Privileged on-policy distillation learns exploration across episodes sharing hidden conditions; real-robot samples are limited and context is not a permanent skill library.

## From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks

- [arXiv 2610.30051](https://arxiv.org/abs/2610.30051) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30051)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30051)

A tool-based LIBERO-10 benchmark measures frontier models without manipulation pretraining; a 44/100 versus 43/100 result is too close for a robust ranking.

## CausGround: Causal Interaction Grounding for Adaptive Embodied Planning

- [arXiv 2610.29702](https://arxiv.org/abs/2610.29702) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29702)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29702)

An offline causal knowledge base improves planning, but RoboCasa uses replay-based high-level evaluation and the knowledge base does not grow during deployment.

## Relational Geometry Forcing for World Action Models

- [arXiv 2610.29282](https://arxiv.org/abs/2610.29282) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29282)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29282)

Training-only relational geometry supervision improves WAM generalization, although LIBERO gains are small and the temporal term alone is harmful.

## DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation

- [arXiv 2610.29246](https://arxiv.org/abs/2610.29246) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29246)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29246)

Depth-grounded predictive representations transfer to matched real scenes, but fixed calibration, embodiment-specific training, and excluded search time limit transfer and speed claims.

## Learning to Absorb Corrections: Critic-Weighted Residual Flow for Vision-Based Insertion

- [arXiv 2610.29117](https://arxiv.org/abs/2610.29117) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29117)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29117)

Critic-weighted residual learning is absorbed into ACT: residual-off success improves from 16% to 76%; cross-task forgetting and VLA transfer remain untested.

## COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation

- [arXiv 2610.28948](https://arxiv.org/abs/2610.28948) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28948)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28948)

Local grasping experts support contextual whole-body manipulation, with strong real-robot results; compute is unmatched and the system does not learn continually in deployment.

## Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration

- [arXiv 2610.28880](https://arxiv.org/abs/2610.28880) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28880)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28880)

Semantic 3D augmentation turns one human video into robot data with strong controlled gains, but teleoperation comparisons are unmatched and setup remains manual.

## T-WLA: Bridging Slow Vision and Fast Touch

- [arXiv 2610.28814](https://arxiv.org/abs/2610.28814) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28814)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28814)

A fast tactile editor corrects pending actions, but the no-touch variant nearly matches full performance, limiting how much gain can be attributed to touch.

## ASPIRE: Agentic /Skills Discovery for Robotics

- [arXiv 2607.00272](https://arxiv.org/abs/2607.00272) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2607.00272)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2607.00272)

The revision adds real-robot cross-episode textual skill accumulation; per-rotation time improves, but total cube-solving time is not monotonic and human support remains.

## μ0: A Scalable 3D Interaction-Trace World Model

- [arXiv 2606.13769](https://arxiv.org/abs/2606.13769) · v3 · [Latest entry](../daily/2026-10-22.md#arxiv-2606.13769)
- Coverage history: [2026-10-22 (v3, revised)](../daily/2026-10-22.md#arxiv-2606.13769)

Version 3 exposes weak long-horizon completion and greater action-chunk latency than π0.5; unchanged atomic-task scores should not be mistaken for compositional progress.

## Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

- [arXiv 2610.28613](https://arxiv.org/abs/2610.28613) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28613)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28613)

A vision-tactile world model supports evaluation and policy post-training. Mean real-robot success reaches 70.8% from a 59.1% SFT baseline on four ARX tasks, with one task below SFT.

## Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future

- [arXiv 2610.28431](https://arxiv.org/abs/2610.28431) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28431)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28431)

Task and causal-state tokens steer world-action predictions through visually ambiguous stages. StageBench rises from 40.9% to 69.4%; real-robot gains require task demonstrations and have small trial counts.

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

## AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies

- [arXiv 2610.27736](https://arxiv.org/abs/2610.27736) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27736)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27736)

Advantage-weighted latent steering improves a frozen one-step decoder without post-training robot rollouts. AWLS achieves 65/100 real-robot successes; only its aggregate gain over MeanFlow survives multiple-comparison correction.

## PrismWAM: Decoupling State Representations in World Action Models

- [arXiv 2610.26564](https://arxiv.org/abs/2610.26564) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.26564)
- Coverage history: [2026-10-21 (v1, supplemental-previous-batch)](../daily/2026-10-21.md#arxiv-2610.26564)

Supplemental review of a 2026-10-20 announcement: RGB goals, depth futures, and actions are decoupled. Base RoboTwin C2R reaches 70.57%; real deployment requires RGB-D, and the 15B result uses additional pretraining.

## HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents

- [arXiv 2610.23479](https://arxiv.org/abs/2610.23479) · v2 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.23479)
- Coverage history: [2026-10-21 (v2, substantive-revision)](../daily/2026-10-21.md#arxiv-2610.23479)

A substantive revision adds official hidden-seed evaluation on 42 RoboDojo tasks. The 46.9% success rate uses a different protocol from v1; released tools do not include the entire evaluation system.

## GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation

- [arXiv 2610.26846](https://arxiv.org/abs/2610.26846) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.26846)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.26846)

Tactile RGB images are supplied through a visual interface for contact-rich manipulation, together with few-shot demonstrations and interaction memory.

## PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models

- [arXiv 2610.26813](https://arxiv.org/abs/2610.26813) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.26813)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.26813)

An EMA teacher under normal appearance aligns shallow/deep action representations with a student receiving perturbed observations. No extra model is needed at inference.

## TrajWAM: An Efficient Trajectory-Guided World Action Model for Dynamic Robotic Manipulation

- [arXiv 2610.25763](https://arxiv.org/abs/2610.25763) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.25763)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.25763)

Historical object masks predict trajectories; a Trajectory ControlNet guides future vision. Video distillation, adapter realignment, and action-rollout distillation preserve a one-step future-conditioned interface for dynamic manipulation.

## SARAM: Sparse Adapter Allocation with Reuse and Merging for Lifelong Robot Learning

- [arXiv 2610.24804](https://arxiv.org/abs/2610.24804) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24804)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24804)

SARAM reuses old LoRA adapters, sparsely allocates new ones, and penalizes redundancy. It identifies the task at each episode start and merges the selected adapter into the backbone, providing a parameterized lifelong-learning approach.

## LIBERO-Dynamic: Benchmarking Robotic Manipulation in Dynamic Environments

- [arXiv 2610.24579](https://arxiv.org/abs/2610.24579) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24579)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24579)

Forty LIBERO tasks receive three trajectory types at three speed levels, with physics advancing during inference according to measured latency. Six policies each face 1,800 dynamic conditions, supported by 9,000 dynamic demonstrations.

## ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation

- [arXiv 2610.23156](https://arxiv.org/abs/2610.23156) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.23156)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.23156)

Rotation-equivariant latents encode object shape; predicted SE(3) transformations are applied analytically to preserve rigid geometry over multistep world-model rollouts.

## AnchorQ: Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors

- [arXiv 2610.22852](https://arxiv.org/abs/2610.22852) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22852)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22852)

Flow reversal maps rough reference actions to state-dependent noise anchors. Local particles and an online critic guide exploration while the base VLA remains frozen.

## Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations

- [arXiv 2610.22576](https://arxiv.org/abs/2610.22576) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22576)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22576)

An embodiment classifier is trained using successful rollouts from a small set of calibration tasks. Its gradients guide each π0 denoising step while the VLA stays frozen, connecting test-time action guidance with dynamics adaptation.

## Scaling Online Exploration for Robot Agents

- [arXiv 2610.22496](https://arxiv.org/abs/2610.22496) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22496)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22496)

A frozen coding agent explores through robot APIs and turns perception, planning, and control into executable programs. Persistent notes and validated skills support reuse across episodes and tasks.

