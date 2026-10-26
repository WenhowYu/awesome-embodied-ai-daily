# Reinforcement learning and adaptation

[English](rl-adaptation.md) | [简体中文](rl-adaptation.zh-CN.md) | [All topics](README.md)

45 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

## RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

- [arXiv 2610.32971](https://arxiv.org/abs/2610.32971) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32971)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32971)

Unifies 17 robust/safe RL algorithms and six standard references, with reusable interfaces and individual/compound deployment shifts including latency and semantics. Not every algorithm runs every task. Methods retain native budgets, and pooled-family comparisons mix backbone strength with robustness mechanisms. The π0.5 study uses one fine-tuned model and offline joint-space demonstration tracking, not closed-loop VLA task success or real-robot validation.

## ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback

- [arXiv 2610.32966](https://arxiv.org/abs/2610.32966) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32966)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32966)

Generates G1 reference motion directly from monocular video and post-trains the diffusion generator with tracker-derived preference pairs; an autoregressive variant enables video teleoperation. These percentages measure simulated reference tracking, not real-world task completion. Fine hand poses are not modeled; real deployment evidence is qualitative, and online initialization takes about ten seconds.

## Regularised RL improves sim-to-real transfer

- [arXiv 2610.32855](https://arxiv.org/abs/2610.32855) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32855)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32855)

Extends soft mellowmax to continuous-control actor–critic with a slowly updated reference policy and tests whether regularization improves sim-to-real robustness beyond nominal training return. Return is not success rate. Domain randomization remains necessary, and temperatures vary by task. PPO/FastTD3 are excluded from ANYmal perturbation deployment after failing a prespecified simulation safety check, so those cells are missing, not observed hardware failures. MuJoCo tuning budgets are unequal.

## $R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design

- [arXiv 2610.32439](https://arxiv.org/abs/2610.32439) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32439)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32439)

Coordinates Explorer, Guardian and Evolver LLM roles around a five-entry elite reward pool, using dynamic candidate allocation for iterative reward-program search. Only simulation and task-specific reward search, not cross-task robot skill accumulation. Elite-pool monotonicity concerns retained search scores, not guaranteed future policy improvement. RL training dominates compute; baseline search/token budgets should not be assumed identical merely because the backbone matches.

## When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

- [arXiv 2610.32431](https://arxiv.org/abs/2610.32431) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32431)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32431)

MART-GRPO uses a fine-tuned, then frozen VLM to locate the last visible unrecovered error in full rollout videos and truncate subsequent failure penalties, retaining successful-rollout terms and original normalization. Ideal stopping results motivate, but do not certify, the retrospective implementation. Simulation only. The actor sees one camera while the VLM reviews three; additional annotations and VLM fine-tuning are required. Boundaries use future rollout information and need not satisfy ideal stopping assumptions. One task declines by 1.95 points; held-out scene seeds are not independent training seeds.

## ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences

- [arXiv 2610.32222](https://arxiv.org/abs/2610.32222) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32222)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32222)

A reward model combines action-mismatch and video-mismatch preferences to judge visual quality and action following without reference videos at reward-computation time. It introduces AVM-Eval (67.2k pairs) and AVM-Pref (506.3k pairs). RL evidence is restricted to one 2B world model and AgiBotWorld, not robot task success. Physical consistency is not directly supervised and ratings rely on a VLM. Reference-free reward computation does not mean reference-free dataset construction; pairwise ranking is not a guarantee of physical validity.

## Ψ-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model

- [arXiv 2610.32177](https://arxiv.org/abs/2610.32177) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32177)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32177)

A unified token interface generates and interprets text, images, geometry and motion; adaptive streams of thought select intermediate representations. GRPO provides a proof of concept for choosing reasoning streams on visual question answering. The reported sim-to-real transfer concerns visual question answering over recorded robot videos, not robot deployment. Optical flow and tracks are proxy actions rather than actuator commands. Training-time positive/negative transfer among unified capabilities is not isolated; physical control remains future work.

## Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion

- [arXiv 2610.32143](https://arxiv.org/abs/2610.32143) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32143)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32143)

Formulates close-fitting bracelet dressing as geometric insertion and combines a finger-wise soft insertion gate with a staged curriculum, transferring a compact geometric observation interface to a bimanual robot. Bracelet is pregrasped and the mannequin stationary; deployment is slowed by about half. No force-aware observation or objective, so finger deflection is not a safety measurement. Large combined pose shifts reduce simulated success to 26/50.

## DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

- [arXiv 2610.32093](https://arxiv.org/abs/2610.32093) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32093)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32093)

Uses privileged, latent-conditioned RL with a reverse curriculum and success-gated diversity to generate filtered demonstration datasets, then trains a visuomotor π0.5 policy rather than deploying the RL generator. Requires accurate simulation, privileged states, reset access and task success signals. Hardware evidence covers four simple tabletop tasks with modest transfer gaps and only one training seed; excessive diversity can hurt competence.

## SEVI: Safe Evidential Real-World Reinforcement Learning

- [arXiv 2610.31829](https://arxiv.org/abs/2610.31829) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31829)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31829)

Adds an evidential safety critic that gates task actions using predicted violation risk and epistemic uncertainty, invoking a shared offline-trained recovery policy during online RL. Only one hardware task and two simulated tasks; no formal zero-violation guarantee. Hardware learning uses 50 successful prior demonstrations, 200 recovery demonstrations and validation-based thresholds. Final success and cumulative training incidents have different denominators.

## PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer

- [arXiv 2610.31812](https://arxiv.org/abs/2610.31812) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31812)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31812)

Transfers a jointly learned latent preference space and reward prior from labeled source tasks, then generates confidence-weighted optimal-transport pseudo-preferences for online target-task RL without target human labels. Zero-shot refers to target human feedback, not zero target interaction or training. Real trials are small; transfer assumes related preference dimensions. PEARL is modified for online learning and dimension mismatch; PrefFew receives limited source data and 100 target labels.

## FLORA: An Open Model Suite for Scaling Robotics Data Engines

- [arXiv 2610.31779](https://arxiv.org/abs/2610.31779) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31779)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31779)

An open labeling suite supplies temporal segments, intended-action captions and outcome/dense/rubric rewards for robotic data pipelines; segmentation/captioning use RL post-training, while the released reward model uses SFT. Not uniformly best across metrics; systems use different frame budgets/compute. The approximately 125× cost claim assumes GPU pricing and modeled throughput, omits deployment overhead, has unverified production GPU-hour accounting, and is not fully reference-version matched. No direct downstream policy-learning improvement is established here.

## Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning

- [arXiv 2608.24885](https://arxiv.org/abs/2608.24885) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2608.24885)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2608.24885)

WorldEcho evaluates off-expert action following using visual screening and end-effector trajectory alignment; WorldSync combines broader action data with dynamics grounding and intervention-effect supervision. The small headline gated-error difference is a point estimate, not established significance. Visual screening does not guarantee integrity; its human checks use only 15 clips per dimension. Video metrics use reconstructed references and separate generation batches. Pretraining corpora and baseline histories differ; the expanded-data advantage is not a controlled data-efficiency claim.

## WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time

- [arXiv 2607.06988](https://arxiv.org/abs/2607.06988) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.06988)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2607.06988)

Human videos write fast-weight memory in a world-action model; paired human–robot meta-training teaches the video-to-action transfer interface. These are interface variants inside one WAM, not faithful evaluations of the complete original systems. The extra interface test covers one task; FastWAM evidence is qualitative eight-frame prediction over 3.2 s, not closed-loop control transfer. Some alternatives rely on pretrained skill latents absent from meta-training-only insertion.

## METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

- [arXiv 2610.31656](https://arxiv.org/abs/2610.31656) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31656)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31656)

METTA separates fast gradient-updated within-episode neural memory from compact cross-episode summaries. It reports over 50% success on held-out Meta-World ML10/45 task families and better long-context sparse-reward exploration.

## PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning

- [arXiv 2610.31299](https://arxiv.org/abs/2610.31299) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31299)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31299)

PiHand distills simulated mocap-tracking experts into a goal-conditioned hand–object latent prior, then learns bounded residual exploration in that latent space. The same interaction prior supports new objects, trajectories, catching and bimanual handovers.

## Learning Robot Behavior Priors from Non-Robotic Synthetic Data

- [arXiv 2610.31275](https://arxiv.org/abs/2610.31275) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31275)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31275)

Pretrains a Transformer on procedural non-robotic MDP, contextual-bandit and linear-dynamical-system data, then predicts unseen robot actions from in-context examples. Evaluation is offline open-loop state-conditioned action prediction, not visual control or physical task success. “Zero-shot” still uses task-specific state-action examples as context.

## In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

- [arXiv 2610.30988](https://arxiv.org/abs/2610.30988) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30988)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30988)

Generative point-cloud completion feeds context-conditioned Transformer dynamics that rank flow-matching action proposals, without test-time weight updates. No real-robot policy comparator; success uses point-cloud-distance thresholds. PCN has better CD/EMD, whereas this method favors correspondence MSE. Dynamic motions and closed-loop replanning remain untested.

## DRILL: Training World Models to Improve Policies, Not Predict Pixels

- [arXiv 2610.30814](https://arxiv.org/abs/2610.30814) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30814)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30814)

DRILL trains a world model for the policy improvement its imagined rollouts produce. A cheaper visitation/advantage/confidence-weighted surrogate and a bilevel meta-gradient variant target downstream return instead of pixel fidelity.

## Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation

- [arXiv 2610.30810](https://arxiv.org/abs/2610.30810) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30810)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30810)

ALMA trains historical context with action-conditioned future-response prediction and uses LLM-generated arm-motion structures to expand RL training tasks based on failures. Deployment weights are fixed; adaptation is contextual, not test-time gradient training. Physical comparison is only against PID, so the 79.6% reduction is not relative to the strongest simulation baseline. Contact-force control remains future work.

## Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation

- [arXiv 2610.30643](https://arxiv.org/abs/2610.30643) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30643)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30643)

FETA makes test-time navigation updates from one binary feedback label on a selected action. It selects unstable trajectories, locates high entropy-gradient steps, and weights updates by policy–feedback disagreement.

## Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- [arXiv 2609.39304](https://arxiv.org/abs/2609.39304) · v4 · [Latest entry](../daily/2026-10-23.md#arxiv-2609.39304)
- Coverage history: [2026-10-23 (v4, revised)](../daily/2026-10-23.md#arxiv-2609.39304)

Scale and Selection evolves a visual-interface robot-agent harness with rollout scaling and champion–challenger acceptance. The revision adds a distillation loop that transfers harness-assisted experience into a standalone robot policy.

## FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence

- [arXiv 2609.17210](https://arxiv.org/abs/2609.17210) · v2 · [Latest entry](../daily/2026-10-23.md#arxiv-2609.17210)
- Coverage history: [2026-10-23 (v2, revised)](../daily/2026-10-23.md#arxiv-2609.17210)

FluxVLA standardizes policy data, training, evaluation and robot execution. Its expanded revision adds an RLinf online PPO frontend, wider simulation/real-robot integrations and paired post-training evidence, rather than introducing a new base policy.

## Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models

- [arXiv 2602.12628](https://arxiv.org/abs/2602.12628) · v5 · [Latest entry](../daily/2026-10-23.md#arxiv-2602.12628)
- Coverage history: [2026-10-23 (v5, revised)](../daily/2026-10-23.md#arxiv-2602.12628)

RL-Co combines sim/real supervised warm-starting with simulator RL anchored by real-data supervision. The new revision adds a stronger rollout-distillation control and makes the limited real-world statistical protocol explicit.

## PhysiCalWorld: In-Context Physics Calibration for World Models

- [arXiv 2610.30125](https://arxiv.org/abs/2610.30125) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30125)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30125)

A compact interaction-derived physics token improves several planning results without gradient updates, but simulation-only gains do not consistently beat all context or supervised baselines.

## Asymmetric On-Policy Distillation Learns In-Context Exploration

- [arXiv 2610.30105](https://arxiv.org/abs/2610.30105) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30105)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30105)

Privileged on-policy distillation learns exploration across episodes sharing hidden conditions; real-robot samples are limited and context is not a permanent skill library.

## AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

- [arXiv 2610.30097](https://arxiv.org/abs/2610.30097) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30097)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30097)

Atomic subtask credit assignment and bottleneck exploration improve long-horizon RL; the real-robot gain is 8.0 points over PPO, with training performed in reconstructed simulation.

## Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation

- [arXiv 2610.29264](https://arxiv.org/abs/2610.29264) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29264)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29264)

Human-in-the-loop deployment updates WAM checkpoints within a session; final performance is close to a budget-matched fixed policy and cross-task continual learning is untested.

## SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training

- [arXiv 2610.29161](https://arxiv.org/abs/2610.29161) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29161)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29161)

Automated intervention collection enables controlled VLA post-training comparisons; real-robot gains transfer an algorithmic change, not a simulation policy zero-shot.

## Learning to Absorb Corrections: Critic-Weighted Residual Flow for Vision-Based Insertion

- [arXiv 2610.29117](https://arxiv.org/abs/2610.29117) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29117)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29117)

Critic-weighted residual learning is absorbed into ACT: residual-off success improves from 16% to 76%; cross-task forgetting and VLA transfer remain untested.

## COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation

- [arXiv 2610.28948](https://arxiv.org/abs/2610.28948) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28948)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28948)

Local grasping experts support contextual whole-body manipulation, with strong real-robot results; compute is unmatched and the system does not learn continually in deployment.

## HarnessPAI: An Evolving Harness for Physical AI

- [arXiv 2609.29166](https://arxiv.org/abs/2609.29166) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2609.29166)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2609.29166)

New DreamZero fine-tuning reuses successful harness trajectories, raising the reported mean from 5.1% to 26.5%; evaluation-based checkpoint selection limits the evidence.

## SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model

- [arXiv 2606.20698](https://arxiv.org/abs/2606.20698) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2606.20698)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2606.20698)

The revision validates safety-head calibration rather than changing headline success results; small Level II gains and proxy costs do not establish real-world safety.

## Feedback World Model Enables Precise Guidance of Diffusion Policy

- [arXiv 2605.15705](https://arxiv.org/abs/2605.15705) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2605.15705)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2605.15705)

Residual feedback adapts a frozen WAM without parameter updates; a moderate gain helps OOD success, while gain 1 worsens prediction errors.

## Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

- [arXiv 2610.28613](https://arxiv.org/abs/2610.28613) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28613)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28613)

A vision-tactile world model supports evaluation and policy post-training. Mean real-robot success reaches 70.8% from a 59.1% SFT baseline on four ARX tasks, with one task below SFT.

## AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- [arXiv 2610.28589](https://arxiv.org/abs/2610.28589) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28589)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28589)

A 9B robotic planner improves through successful-trajectory SFT and multi-turn RL with a frozen executor. LIBERO-PRO reaches 71.0%, but tasks overlap between training and testing and no real-robot result is reported.

## AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies

- [arXiv 2610.27736](https://arxiv.org/abs/2610.27736) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27736)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27736)

Advantage-weighted latent steering improves a frozen one-step decoder without post-training robot rollouts. AWLS achieves 65/100 real-robot successes; only its aggregate gain over MeanFlow survives multiple-comparison correction.

## VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs

- [arXiv 2610.27698](https://arxiv.org/abs/2610.27698) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27698)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27698)

A paired benchmark measures target gains and cross-dimension retention after VLA vision tuning. Non-target averages decline in 8 of 10 settings; the study concerns targeted fine-tuning rather than online continual learning.

## Training Controllable World Models via Action Influence Maximization

- [arXiv 2610.27387](https://arxiv.org/abs/2610.27387) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27387)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27387)

Action-influence objectives guide active data collection for controllable world models. A Push-T controllability result yields an 85× data-volume ratio, with evidence limited to two simulated environments.

## DEFLECT: Temporal Counterfactual Preference Learning for Delay-Robust Asynchronous VLAs

- [arXiv 2605.19294](https://arxiv.org/abs/2605.19294) · v3 · [Latest entry](../daily/2026-10-21.md#arxiv-2605.19294)
- Coverage history: [2026-10-21 (v3, substantive-revision)](../daily/2026-10-21.md#arxiv-2605.19294)

The revision adds cross-backbone and continued-training controls for delay-robust VLA preference learning. GR00T reaches 73.10% at four-step delay, but protocol changes prevent direct headline comparisons to earlier versions.

## PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models

- [arXiv 2610.26813](https://arxiv.org/abs/2610.26813) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.26813)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.26813)

An EMA teacher under normal appearance aligns shallow/deep action representations with a student receiving perturbed observations. No extra model is needed at inference.

## SteerAct: Unlocking Action Models through Few-Shot Temporal Steering

- [arXiv 2610.25632](https://arxiv.org/abs/2610.25632) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.25632)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.25632)

A per-task bank of 24 success/failure-labeled rollouts supplies temporal feature references. Online steering chooses intervention timing, direction, and strength while π0.5/Fast-WAM stay frozen. It does not update the main model weights at test time.

## Self-Improving Video-to-Action Models

- [arXiv 2610.24177](https://arxiv.org/abs/2610.24177) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24177)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24177)

A video planner proposes goal videos, and a video-to-action model generates video/action training pairs through its own interactions and improves iteratively.

## AnchorQ: Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors

- [arXiv 2610.22852](https://arxiv.org/abs/2610.22852) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22852)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22852)

Flow reversal maps rough reference actions to state-dependent noise anchors. Local particles and an online critic guide exploration while the base VLA remains frozen.

## Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations

- [arXiv 2610.22576](https://arxiv.org/abs/2610.22576) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22576)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22576)

An embodiment classifier is trained using successful rollouts from a small set of calibration tasks. Its gradients guide each π0 denoising step while the VLA stays frozen, connecting test-time action guidance with dynamics adaptation.

