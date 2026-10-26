# Evaluation, robustness, and safety

[English](evaluation.md) | [简体中文](evaluation.zh-CN.md) | [All topics](README.md)

73 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

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

