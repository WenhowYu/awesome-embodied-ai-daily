# Manipulation and real-robot transfer

[English](manipulation-transfer.md) | [简体中文](manipulation-transfer.zh-CN.md) | [All topics](README.md)

76 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

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

