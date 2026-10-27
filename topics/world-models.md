# World models and world-action models

[English](world-models.md) | [简体中文](world-models.zh-CN.md) | [All topics](README.md)

80 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

## OSWAM: An Effective World Action Model with One-Step Action Generation

- [arXiv 2610.35850](https://arxiv.org/abs/2610.35850) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35850)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35850)

Uses action/scene imagination tokens for structured diffusion initialization and privileged future-conditioned distillation to generate actions in one denoising step. One-step is a speed/quality trade-off, not uniform superiority. Real tests are small; completion time is video-estimated on successes only. H20 and compiled RTX5090 latency numbers use different setups; NAVSIM is not real-road deployment.

## Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation

- [arXiv 2610.35636](https://arxiv.org/abs/2610.35636) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35636)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35636)

OpTTA adapts a latent world model with observed-transition prediction loss plus an optimistic goal-reaching cost on planner candidate rollouts, without extra interactions. Simulated pushing, reaching and navigation only; adaptation resets per task and uses at most 30 replans. LeWM TwoRoom can degrade. This is parameter adaptation for planning, not an established continual or real-robot capability.

## WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU

- [arXiv 2610.35529](https://arxiv.org/abs/2610.35529) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35529)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35529)

WorldPager keeps int4 world-model KV across GPU, pinned DRAM and NVMe; it prefetches pose-predicted retrievals, reuses stale entries instead of waiting on misses, writes back asynchronously and remaps positions beyond the native horizon. “Zero stall” excludes dequantization/write-back and permits stale retrieval; it is not zero overhead or real-time 16fps. Timing uses one scene/seed and one physical drive; slower drives are software-emulated. Quality evidence is MG2-only, with three scenes/five seeds for long-gap tests; texture drift remains. Baselines are reimplementations, not original systems.

## PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds

- [arXiv 2610.34921](https://arxiv.org/abs/2610.34921) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34921)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34921)

A shared VLM proposes executable physical scenes and solves questions; a fixed simulator validates scenes, runs matched body-removal interventions and binds answers, rather than letting the proposer label its own tasks. Question answering, not robot control. One training run per configuration on four GPUs; uses 24 hand-provided demonstration programs. Branch ablation also removes task families and changes retained rollout count (8,668 versus 7,960), so it does not isolate branch execution under matched exposure. Broad transfer gains are small and uneven.

## Behavioural Quality Is Not Learning Utility: Objective Mismatch in Human Behaviour Models for Robot Learning

- [arXiv 2610.34839](https://arxiv.org/abs/2610.34839) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34839)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34839)

Tests whether human-behavior generative metrics predict their usefulness as simulated training partners for robot RL. Policy tests are simulated, including simulated human partners—not physical human-robot trials. Findings depend on these model families, representations and RL training protocols; they do not imply realistic behavior is unnecessary for safety.

## SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments

- [arXiv 2610.34745](https://arxiv.org/abs/2610.34745) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34745)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34745)

An agentic pipeline reconstructs interactive simulators from 3D/4D captures, inspects and repairs scenes, and produces digital-sister variants and scripted demonstrations. Geometry/IoU improvements are not calibrated contact dynamics. Physical parameters are unmeasured estimates; static evaluation uses very few scenes and single conversions. Real transfer is preliminary and non-monotonic with simulated data scale.

## Video World Models Need Predictable Latents

- [arXiv 2610.34663](https://arxiv.org/abs/2610.34663) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34663)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34663)

Fine-tunes autoencoder latents for temporal predictability and uses a past-conditioned decoder to preserve reconstruction while simplifying world-model dynamics. Main evidence concerns video prediction and policy-evaluation agreement, not improved robot policy success. Studies 2D spatial autoencoders fine-tuned from pretrained models; broader domains and spatiotemporal autoencoders are untested.

## What Does World Modeling Actually Improve in Robot Action Learning?

- [arXiv 2610.34593](https://arxiv.org/abs/2610.34593) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34593)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34593)

Controlled future-video-loss removal within FastWAM and OpenWAM tests what predictive supervision changes; a training-only lightweight video predictor extends the test to π0.5. Simulation-only; gains under unseen tasks are inconsistent and environmental randomization leaves low success without a consistent prediction-loss advantage. Single training seed; rollout repeats do not establish training-seed robustness. Wan extension changes multiple factors.

## AuRA: From Atoms to Bits through Autonomous Robot Interaction

- [arXiv 2610.34452](https://arxiv.org/abs/2610.34452) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34452)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34452)

Automates deformable digital-twin acquisition with feasible grasp selection, robot-state-derived gripper trajectories and registered pre-interaction geometry/appearance. Collection accounting excludes processing/reconstruction and untimed backup trials; expert collection is faster (100.6s) than AuRA. Prediction uses known gripper motion; unseen tests use selected assets and manual alignment. No policy-learning gain demonstrated.

## EAST: Embodied AI Safety Testing via Systematic Fault Injection in Digital Twins

- [arXiv 2610.34358](https://arxiv.org/abs/2610.34358) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34358)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34358)

Maps documented safety hazards to eight executable fault operators, verifies realized interventions and separately records safety violations and task outcomes. Simulation only; safety is limited to simulator-state predicates. Challenge exposure is close to Random-Legal and Rule-Based, not a blanket superiority result; unsafe-success counts diagnose metric mismatch rather than rank methods.

## AdaPolicy: Action-Driven Anticipatory Robot Policies via Next-Chunk Prediction

- [arXiv 2610.34280](https://arxiv.org/abs/2610.34280) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34280)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34280)

Adds a training-only EMA action head that predicts the next action chunk from an evolved latent state; its loss backpropagates through that state into the online policy, without future-image supervision. Real precision tasks use 1, 000/400 demonstrations, with human takeover corrections comprising 20% of each dataset; both methods use the same combined data. These are supervised anticipatory features, not evidence of autonomous online world-model adaptation; zero inference overhead is relative to the matched architecture.

## HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model

- [arXiv 2610.34126](https://arxiv.org/abs/2610.34126) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34126)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34126)

Learns a history-based proprioceptive neural dynamics model with forward-kinematics supervision, then fine-tunes humanoid tracking policies through model gradients; low-frequency reference perturbations collect deployment-viable data. Small physical repetition counts and task-specific tracking/completion metrics, not broad manipulation success. Real-world baselines are direct transfer and disturbance-aware PPO where feasible, not the full simulation baseline set. Authors limit the method to time-invariant disturbance settings; collection/training precede adapted deployment.

## X-World: Transferring Video Priors to Variable-View Robot Control

- [arXiv 2610.34105](https://arxiv.org/abs/2610.34105) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34105)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34105)

Transfers a video backbone to variable-view control with residual cross-view attention, a layer-aligned Q-Former and shared action expert with native dataset interfaces. Reference baselines do not match pretraining data/compute. Camera, background and noise shifts remain weaker than OpenVLA-OFT; LIBERO-Plus weighting is unspecified. One physical platform, no demonstrated unseen-embodiment transfer.

## Behavior Spatial Benchmark: Evaluating Spatial Understanding for Robotics

- [arXiv 2610.34051](https://arxiv.org/abs/2610.34051) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34051)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34051)

Connects spatial VQA, target grounding and VLA execution while separating target-selection intention from strict task completion. Entirely simulated. Headline abstract rates are soft intention measures, not task completion. Oracle grounding is privileged; task timeouts and hand-target correlations affect interpretation.

## TurboWAM: Learning What Matters for Fast World Action Models

- [arXiv 2610.33941](https://arxiv.org/abs/2610.33941) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33941)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33941)

Selectively aggregates early world-model layers conditioned on noisy actions and modulates action gradients during training, retaining video co-training without test-time video generation. Benchmarks have unmatched embodied pretraining across methods. Prompt-corrected results must not be conflated with the original protocol. Layer structure is architectural, not explicit 3D geometry; latency alone does not establish safe control. GPU model is unspecified (approximately 140GB data-center GPU). Physical-robot experiments are referred to supplementary material; their quantitative results were not established in the checked text.

## WMEval: Evaluating Interactive World Models Grounded on Physical Simulations

- [arXiv 2610.33894](https://arxiv.org/abs/2610.33894) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33894)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33894)

Evaluates interactive world models against matched Unity action trajectories and physical-state/causal references across six dimensions. Controlled generated-video evaluation, not robot policy training or real physics validation. Different interfaces allow different model subsets per metric; learned vision/VLM evaluators remain imperfect despite calibration.

## RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models

- [arXiv 2610.33807](https://arxiv.org/abs/2610.33807) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33807)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33807)

Introduces hardware-prior-based KIVA kinematic stability and RIGIS multi-view geometry metrics, plus a world-model acceleration audit. Measures generated-video consistency, not downstream control success. Metrics do not establish contact physics, deformable behavior or force dynamics; some long-horizon comparisons confound rollout depth and non-Markovian regime.

## One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation

- [arXiv 2610.33794](https://arxiv.org/abs/2610.33794) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33794)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33794)

Converts one phone scan per building into a Gaussian-splat navigation environment and grounded instruction episodes; known-scene Pareto utilities guide policy post-training without human demonstrations or a learned critic. Demonstration-free is not human-free: scanning and evaluation-instruction checking require people. Baselines have different scene-specific data budgets; unscanned means same buildings, not unseen buildings. Real success uses a 1.5m radius, and changed layouts require rescanning. This is offline scene post-training, not online per-step TTT.

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

## World-in-Context: Interactive Video World Modeling with In-Context Conditioning

- [arXiv 2610.33169](https://arxiv.org/abs/2610.33169) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33169)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33169)

World-in-Context places view, character-action and camera controls in shared self-attention as explicit tokens; Interaction-Transport RoPE incorporates accumulated control transitions into temporal attention. Navigation score is a composite video metric, not robot task success. Main model uses bidirectional fine-tuning on 100k navigation clips plus 500 switching sequences; the final 93.8% result is not single-view-only training. Cross-system data/compute are not matched; controlled architecture comparisons share its data. No embodied manipulation or physical-control validation.

## Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models

- [arXiv 2610.26179](https://arxiv.org/abs/2610.26179) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.26179)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2610.26179)

v2→v3 adds Appendix J disjoint-source-group evaluations: backbones are trained from scratch on training-only groups and heads selected on separate groups. This directly probes overlap concerns in the released-asset benchmarks; original headline gains are not new. Push-T shows no improvement in this stronger separation test. New task windows differ from the original benchmark (uniform Cube starts; 80-step rather than 74-step Push-T gaps); do not compare absolute rates across protocols. SE covers backbone seeds, not sampled tasks/source groups. Simulation only.

## Expert-Play Contouring Control: Faster-than-Demonstration Planning from Slow Expert and Fast Play

- [arXiv 2609.22798](https://arxiv.org/abs/2609.22798) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2609.22798)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2609.22798)

v1→v2 adds extensive implementation/evaluation appendices that materially qualify the faster-than-demonstration claims: friction-sweep retraining, success-conditioned phase timing, controller/search budgets and play-mixture provenance. The 13s versus22s real example already appears in v1. The sweep does not isolate zero-shot robustness of one fixed model, and method-specific success subsets can change the timing comparison. No new real-robot aggregate success result was established in this revision; the physical speedup remains an illustrative rollout.

## GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation

- [arXiv 2609.05588](https://arxiv.org/abs/2609.05588) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2609.05588)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2609.05588)

v2→v3 substantively replaces Appendix A.1/Table 3 RoboTwin evaluation: six named perturbation columns become Clean-to-Clean and Clean-to-Random under 50 clean demonstrations per task, with additional leaderboard baselines. This is a protocol/result replacement, not a directly comparable version-to-version gain. Baselines are drawn from the official RoboTwin leaderboard where available and the Qwen-RM report, rather than all being rerun in a controlled study. The main real-robot pretraining/scaling findings are inherited from v2.

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

## RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data

- [arXiv 2605.13775](https://arxiv.org/abs/2605.13775) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2605.13775)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2605.13775)

v1→v2 adds §5.5: the planner–simulator co-evolution loop is instantiated with action-capable LingBot-VA and LIBERO environment feedback. This is a new low-level-control extension, not a new version of the already reported generative-planning gains. The new extension uses external simulator feedback, unlike the internally supervised VLM–VGM setting. No physical deployment; 500 seeds do not represent the total supervision or interaction budget, and this section does not establish a complete interaction-cost match.

## UniAction: Unified Action Conditioning for World Models

- [arXiv 2610.32977](https://arxiv.org/abs/2610.32977) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32977)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32977)

UniAction represents force, camera, hand and robot-pose actions as sparse semantic elements with continuous spatiotemporal coordinates, mapped into the video backbone’s native RoPE geometry. Cardinality-calibrated attention compensates for different action-token counts. These are video-generation action-following scores, not closed-loop robot success. Conditioning branches differ in trainable parameter counts. Joint training does not improve every metric: camera LPIPS is .4863 versus expert .4780. Four specified action forms do not establish arbitrary-action or unseen-embodiment generalization.

## RynnUnify: Towards Unified Embodied Brain

- [arXiv 2610.32965](https://arxiv.org/abs/2610.32965) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32965)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32965)

A Cosmos3-based 16B model couples an 8B reasoner and 8B video generator. Cross-chunk scene frames support interleaved visual planning; a separately RL-trained reasoner chooses whether to request generated evidence, and WAM adaptation adds joint video-action learning. Robot adaptation uses roughly 1,600 hours of atomic and 177 hours of composite RoboCasa data. Full-split baseline numbers are imported from reports, whereas Selected-20 is evaluated by the authors. Visual history is within-episode context, not demonstrated lifelong memory; three real tasks do not isolate memory’s contribution.

## Predictive Long-Horizon Progress Modeling with Action-Aware Quantification

- [arXiv 2610.32776](https://arxiv.org/abs/2610.32776) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32776)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32776)

NimCritic couples predictive video learning with separate progress/completion outputs, perturbed progress history, and cross-modal alignment. LOOM contains 300 cross-embodiment trajectories and 19,618 human-calibrated frames. These are offline evaluator metrics, not robot task-success rates. Multi-subtask evaluation relies on offline VLM segmentation, not demonstrated real-time judging. Training uses 800+ hours and 48 accelerators; no closed-loop policy improvement from its reward is established.

## DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation

- [arXiv 2610.32330](https://arxiv.org/abs/2610.32330) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32330)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32330)

Learns temporally aligned soft slots, slot-level latent actions, and proximity–motion relations from point-cloud sequences, supplying dynamics-aware 3D representations to a diffusion policy. Simulation baselines are inherited from AFRO, and each seed selects its best evaluated checkpoint rather than an independent final test. Real error bars reflect layout variability, not training seeds; one embodiment and one task underpin the robustness tests.

## ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences

- [arXiv 2610.32222](https://arxiv.org/abs/2610.32222) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32222)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32222)

A reward model combines action-mismatch and video-mismatch preferences to judge visual quality and action following without reference videos at reward-computation time. It introduces AVM-Eval (67.2k pairs) and AVM-Pref (506.3k pairs). RL evidence is restricted to one 2B world model and AgiBotWorld, not robot task success. Physical consistency is not directly supervised and ratings rely on a VLM. Reference-free reward computation does not mean reference-free dataset construction; pairwise ranking is not a guarantee of physical validity.

## Ψ-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model

- [arXiv 2610.32177](https://arxiv.org/abs/2610.32177) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32177)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32177)

A unified token interface generates and interprets text, images, geometry and motion; adaptive streams of thought select intermediate representations. GRPO provides a proof of concept for choosing reasoning streams on visual question answering. The reported sim-to-real transfer concerns visual question answering over recorded robot videos, not robot deployment. Optical flow and tracks are proxy actions rather than actuator commands. Training-time positive/negative transfer among unified capabilities is not isolated; physical control remains future work.

## EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions

- [arXiv 2610.31845](https://arxiv.org/abs/2610.31845) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31845)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31845)

Combines reliability-dependent corruption and loss weighting with joint vision–action flow and privileged-future EMA distillation to learn from noisy human action labels. External RoboCasa baselines use published results with different pretraining and budgets. The real π0.5 baseline replaces input/output projections for 58 DoF, confounding attribution. Action labels remain required, and source weighting does not correct systematic retargeting bias.

## WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations

- [arXiv 2610.31834](https://arxiv.org/abs/2610.31834) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31834)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31834)

Constructs executable world programs from robot demonstrations, with a coding agent using replay feedback to repair scene geometry, assets, and physical interactions. Results concern recorded-trajectory replay in reconstructed simulation, not new-policy real-robot success or sim-to-real learning. Spatial metrics do not uniformly beat Astra, and component ablations cover one task, offering little evidence of a memory benefit.

## See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space

- [arXiv 2610.31762](https://arxiv.org/abs/2610.31762) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31762)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31762)

RepresentNav constructs policy-oriented representations from multiple layers of frozen vision backbones, then learns a JEPA-style latent future prediction before waypoint generation. External baselines are taken from their papers with differing observation settings. Physical navigation demonstrations do not establish manipulation transfer; dexterous and whole-body control remain untested.

## Metro-WM: Long-Horizon Latent Planning with Realisable Sub-Goals

- [arXiv 2609.31868](https://arxiv.org/abs/2609.31868) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2609.31868)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2609.31868)

A nonparametric macro planner retrieves observed states from an offline trajectory graph and uses shortest-path subgoals with repeated graph re-entry. All added tests are simulated. Metro uses a fixed rather than shrinking horizon and tunes horizon/subgoal distance plus executed-block count on separate tuning tasks; baselines use released configurations. Retrieved states are real, but this does not certify every connecting transition. Diverse layouts absent from the corpus may break stitching.

## Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning

- [arXiv 2608.24885](https://arxiv.org/abs/2608.24885) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2608.24885)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2608.24885)

WorldEcho evaluates off-expert action following using visual screening and end-effector trajectory alignment; WorldSync combines broader action data with dynamics grounding and intervention-effect supervision. The small headline gated-error difference is a point estimate, not established significance. Visual screening does not guarantee integrity; its human checks use only 15 clips per dimension. Video metrics use reconstructed references and separate generation batches. Pretraining corpora and baseline histories differ; the expanded-data advantage is not a controlled data-efficiency claim.

## WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time

- [arXiv 2607.06988](https://arxiv.org/abs/2607.06988) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.06988)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2607.06988)

Human videos write fast-weight memory in a world-action model; paired human–robot meta-training teaches the video-to-action transfer interface. These are interface variants inside one WAM, not faithful evaluations of the complete original systems. The extra interface test covers one task; FastWAM evidence is qualitative eight-frame prediction over 3.2 s, not closed-loop control transfer. Some alternatives rely on pretrained skill latents absent from meta-training-only insertion.

## Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

- [arXiv 2610.31670](https://arxiv.org/abs/2610.31670) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31670)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31670)

A training-free CKNNA measure aligns sensory representations with DTW trajectory neighborhoods for offline policy/backbone screening. Real-robot r=.831 uses exploratory h=110; prespecified h=7 gives r=.429, p=.236. Correlation does not demonstrate training benefit or replace closed-loop testing.

## Skeleton-Grounded Latent Action Model for Robot World Models

- [arXiv 2610.31474](https://arxiv.org/abs/2610.31474) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31474)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31474)

Skeleton supervision separates kinematic and residual latent actions; swap reconstruction, branch dropout and an adapter enable action-conditioned video prediction. DROID prediction spans 0.8 seconds; valid-trajectory subsets differ. Human transfer comprises two generated-video examples. Policy evaluation has only nine real successes and cannot replace closed-loop validation.

## RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation

- [arXiv 2610.31121](https://arxiv.org/abs/2610.31121) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31121)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31121)

Temporal scene graphs compare generated/reference objects, relation changes and 3D paths; introduces the 1,000-scene ShareRobot-SG dataset. Correlation across only three generator means does not establish per-video reliability; object F1 trails SG-Ego. Single-reference/object assumptions and extraction errors can penalize valid alternatives; executable actions are not certified.

## UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry

- [arXiv 2610.30991](https://arxiv.org/abs/2610.30991) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30991)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30991)

Three experts jointly model future vision, 3D scene flow and actions under ten objectives; deployment requires no flow input. 58.9% is the best evaluation seed; 87.7% uses the best evaluated checkpoint. Real policies are task-specific and starts remain within demonstration coverage; flow pseudo-labels are noisy.

## In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

- [arXiv 2610.30988](https://arxiv.org/abs/2610.30988) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30988)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30988)

Generative point-cloud completion feeds context-conditioned Transformer dynamics that rank flow-matching action proposals, without test-time weight updates. No real-robot policy comparator; success uses point-cloud-distance thresholds. PCN has better CD/EMD, whereas this method favors correspondence MSE. Dynamic motions and closed-loop replanning remain untested.

## DRILL: Training World Models to Improve Policies, Not Predict Pixels

- [arXiv 2610.30814](https://arxiv.org/abs/2610.30814) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30814)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30814)

DRILL trains a world model for the policy improvement its imagined rollouts produce. A cheaper visitation/advantage/confidence-weighted surrogate and a bilevel meta-gradient variant target downstream return instead of pixel fidelity.

## DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models

- [arXiv 2610.30781](https://arxiv.org/abs/2610.30781) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30781)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30781)

DeXplicit predicts object-centric motion and deformation in metric 3D before rendering action-conditioned video. Matched-input comparisons reduce long-horizon moved-point error 27–40% versus adapted PointWorld; explicit geometry improves object fidelity.

## Self-Distilling Future Video Representations for World Action Models

- [arXiv 2610.30320](https://arxiv.org/abs/2610.30320) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30320)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30320)

Observation history and EMA self-distillation improve future representations from one video-denoising pass for an action decoder. Appendices allow partial credit, so scores are not uniformly binary full-task success. Transfer instruction following is zero without human videos; cross-embodiment correspondence is implicit.

## FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence

- [arXiv 2609.17210](https://arxiv.org/abs/2609.17210) · v2 · [Latest entry](../daily/2026-10-23.md#arxiv-2609.17210)
- Coverage history: [2026-10-23 (v2, revised)](../daily/2026-10-23.md#arxiv-2609.17210)

FluxVLA standardizes policy data, training, evaluation and robot execution. Its expanded revision adds an RLinf online PPO frontend, wider simulation/real-robot integrations and paired post-training evidence, rather than introducing a new base policy.

## Agentic World Action Models

- [arXiv 2610.30136](https://arxiv.org/abs/2610.30136) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30136)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30136)

Joint code–video–action denoising connects agent planning and control, but random-domain performance is weaker than π0.5 and the skill library remains frozen.

## PhysiCalWorld: In-Context Physics Calibration for World Models

- [arXiv 2610.30125](https://arxiv.org/abs/2610.30125) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30125)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30125)

A compact interaction-derived physics token improves several planning results without gradient updates, but simulation-only gains do not consistently beat all context or supervised baselines.

## CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation

- [arXiv 2610.30117](https://arxiv.org/abs/2610.30117) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30117)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30117)

Contact-wrench history improves force-sensitive manipulation under matched ablations, but hand-set gains and larger contact forces prevent a general safety claim.

## GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

- [arXiv 2610.29866](https://arxiv.org/abs/2610.29866) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29866)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29866)

Training-only geometry supervision and temporal memory improve a shared VLA backbone; benchmark-specific adaptation and episode resets bound the generalization and memory claims.

## Relational Geometry Forcing for World Action Models

- [arXiv 2610.29282](https://arxiv.org/abs/2610.29282) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29282)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29282)

Training-only relational geometry supervision improves WAM generalization, although LIBERO gains are small and the temporal term alone is harmful.

## Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation

- [arXiv 2610.29264](https://arxiv.org/abs/2610.29264) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29264)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29264)

Human-in-the-loop deployment updates WAM checkpoints within a session; final performance is close to a budget-matched fixed policy and cross-task continual learning is untested.

## DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation

- [arXiv 2610.29246](https://arxiv.org/abs/2610.29246) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29246)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29246)

Depth-grounded predictive representations transfer to matched real scenes, but fixed calibration, embodiment-specific training, and excluded search time limit transfer and speed claims.

## How Representational Priors Shape Generalization in World Action Models

- [arXiv 2610.29168](https://arxiv.org/abs/2610.29168) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29168)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29168)

Representation geometry correlates with WAM robustness across backbones, but unmatched pretraining and architectures prevent a causal interpretation.

## HarnessPAI: An Evolving Harness for Physical AI

- [arXiv 2609.29166](https://arxiv.org/abs/2609.29166) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2609.29166)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2609.29166)

New DreamZero fine-tuning reuses successful harness trajectories, raising the reported mean from 5.1% to 26.5%; evaluation-based checkpoint selection limits the evidence.

## SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model

- [arXiv 2606.20698](https://arxiv.org/abs/2606.20698) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2606.20698)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2606.20698)

The revision validates safety-head calibration rather than changing headline success results; small Level II gains and proxy costs do not establish real-world safety.

## μ0: A Scalable 3D Interaction-Trace World Model

- [arXiv 2606.13769](https://arxiv.org/abs/2606.13769) · v3 · [Latest entry](../daily/2026-10-22.md#arxiv-2606.13769)
- Coverage history: [2026-10-22 (v3, revised)](../daily/2026-10-22.md#arxiv-2606.13769)

Version 3 exposes weak long-horizon completion and greater action-chunk latency than π0.5; unchanged atomic-task scores should not be mistaken for compositional progress.

## Feedback World Model Enables Precise Guidance of Diffusion Policy

- [arXiv 2605.15705](https://arxiv.org/abs/2605.15705) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2605.15705)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2605.15705)

Residual feedback adapts a frozen WAM without parameter updates; a moderate gain helps OOD success, while gain 1 worsens prediction errors.

## UniWALM: Unified World Action Language Model for Embodied Robot Control

- [arXiv 2610.28626](https://arxiv.org/abs/2610.28626) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28626)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28626)

Joint video, action, and language denoising feeds textual working memory back into control. Gains on memory tasks and 18 real-robot trials do not isolate memory from other components or establish cross-episode retrieval.

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

## LaLa-World: Scaling Latent World Models with Natural Language Actions

- [arXiv 2610.27851](https://arxiv.org/abs/2610.27851) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27851)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27851)

Natural-language action representations unify latent world-model pretraining and joint action/future prediction. LIBERO reaches 97.7%; DROID action-prediction scores are not real-robot success rates.

## Training Controllable World Models via Action Influence Maximization

- [arXiv 2610.27387](https://arxiv.org/abs/2610.27387) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27387)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27387)

Action-influence objectives guide active data collection for controllable world models. A Push-T controllability result yields an 85× data-volume ratio, with evidence limited to two simulated environments.

## PrismWAM: Decoupling State Representations in World Action Models

- [arXiv 2610.26564](https://arxiv.org/abs/2610.26564) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.26564)
- Coverage history: [2026-10-21 (v1, supplemental-previous-batch)](../daily/2026-10-21.md#arxiv-2610.26564)

Supplemental review of a 2026-10-20 announcement: RGB goals, depth futures, and actions are decoupled. Base RoboTwin C2R reaches 70.57%; real deployment requires RGB-D, and the 15B result uses additional pretraining.

## WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning

- [arXiv 2607.18840](https://arxiv.org/abs/2607.18840) · v3 · [Latest entry](../daily/2026-10-21.md#arxiv-2607.18840)
- Coverage history: [2026-10-21 (v3, numerical-revision)](../daily/2026-10-21.md#arxiv-2607.18840)

Corrected C2R ablations reduce the marginal long-term-memory gain from 3.42 to 0.67 percentage points. Architecture, main results, and real-robot results are unchanged, and the correction is unexplained.

## PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models

- [arXiv 2610.26813](https://arxiv.org/abs/2610.26813) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.26813)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.26813)

An EMA teacher under normal appearance aligns shallow/deep action representations with a student receiving perturbed observations. No extra model is needed at inference.

## TrajWAM: An Efficient Trajectory-Guided World Action Model for Dynamic Robotic Manipulation

- [arXiv 2610.25763](https://arxiv.org/abs/2610.25763) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.25763)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.25763)

Historical object masks predict trajectories; a Trajectory ControlNet guides future vision. Video distillation, adapter realignment, and action-rollout distillation preserve a one-step future-conditioned interface for dynamic manipulation.

## SteerAct: Unlocking Action Models through Few-Shot Temporal Steering

- [arXiv 2610.25632](https://arxiv.org/abs/2610.25632) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.25632)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.25632)

A per-task bank of 24 success/failure-labeled rollouts supplies temporal feature references. Online steering chooses intervention timing, direction, and strength while π0.5/Fast-WAM stay frozen. It does not update the main model weights at test time.

## LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models

- [arXiv 2610.24587](https://arxiv.org/abs/2610.24587) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24587)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24587)

The benchmark evaluates 17 policies, including VLAs and WAMs, using 22 static perturbation types, 20 runtime interventions, and 1,648 valid task variants. It probes feedback use, recovery, and combined perturbations.

## LIBERO-Dynamic: Benchmarking Robotic Manipulation in Dynamic Environments

- [arXiv 2610.24579](https://arxiv.org/abs/2610.24579) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24579)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24579)

Forty LIBERO tasks receive three trajectory types at three speed levels, with physics advancing during inference according to measured latency. Six policies each face 1,800 dynamic conditions, supported by 9,000 dynamic demonstrations.

## Self-Improving Video-to-Action Models

- [arXiv 2610.24177](https://arxiv.org/abs/2610.24177) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24177)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24177)

A video planner proposes goal videos, and a video-to-action model generates video/action training pairs through its own interactions and improves iteratively.

## LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence

- [arXiv 2610.23334](https://arxiv.org/abs/2610.23334) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.23334)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.23334)

Semantic subtask progress connects VLM planning, state assessment, and world-action-model action generation, with hierarchical visual memory and subtask value learning.

## ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation

- [arXiv 2610.23156](https://arxiv.org/abs/2610.23156) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.23156)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.23156)

Rotation-equivariant latents encode object shape; predicted SE(3) transformations are applied analytically to preserve rigid geometry over multistep world-model rollouts.

