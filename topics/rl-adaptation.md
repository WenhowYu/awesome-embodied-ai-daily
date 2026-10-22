# Reinforcement learning and adaptation

[English](rl-adaptation.md) | [简体中文](rl-adaptation.zh-CN.md) | [All topics](README.md)

21 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

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

