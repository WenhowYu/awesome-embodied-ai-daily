# Memory, skills, and continual learning

[English](memory-skills.md) | [简体中文](memory-skills.zh-CN.md) | [All topics](README.md)

95 unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.

## Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy

- [arXiv 2610.35832](https://arxiv.org/abs/2610.35832) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35832)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35832)

EBench profiles Astra direct waypoint control versus selective invocation of frozen VLA/WAM policies under RGB/proprioceptive observations and one annotated demonstration per task. No cross-episode memory. 31/510 episodes use a demonstration from the same test scene. Two tasks allow 3,000 steps direct versus 5,000 hybrid; correcting that changes hybrid means to 52.4%/55.8%. Policy calls cannot receive agent-written subgoals; compute is unbounded and comparisons run once/episode.

## Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent

- [arXiv 2610.35817](https://arxiv.org/abs/2610.35817) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35817)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35817)

ZAP trains a 27B VLM via successful-trace SFT and simulation GRPO to use a shared perception/pose-control tool interface; semantic pretraining and learned motion are tested compositionally without real robot training trajectories. Only 30 real trials/model. Harness supplies SAM3.1 segmentation, calibrated depth-derived 3D readouts and controller feedback; not RGB-only end-to-end control. Real robot calibration informs simulation. Cost assumes one B300 at $7.10/hour; Franka transfer is not real hardware.

## FISRF: Flexible Instructional Scaffolding Reflection Framework for Robotics Task Planning with Large Language Model

- [arXiv 2610.35686](https://arxiv.org/abs/2610.35686) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35686)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35686)

FISRF combines short-term trajectories/reflections with cross-task failure lessons and a fixed RAG mentor knowledge base; measured recovery difficulty and improvement choose which reflection or guidance to request. Quantitative evidence is text simulation; the dual-arm mobile-robot kitchen demonstration has no reported trial count or comparative success rate. Planning epochs are iterative recovery rather than independent seeds. Reported reflection cost is tokens per recovered task, not total deployment dollars; isolated long-term transfer and uncertainty remain unclear.

## RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies

- [arXiv 2610.35604](https://arxiv.org/abs/2610.35604) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.35604)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.35604)

RoboDoctor connects diagnosis, policy/agent control allocation, selective intervention and contact-method revision through persistent records of rationale, attempted methods, outcomes and reuse conditions. Retrospective highest-score selection mixes source runs without uniform versions, checkpoints or inference budgets. Warmup already uses assistance and memory. No matched reset-memory control, consolidated cost analysis or real-robot validation; results do not establish causal memory benefit.

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

## Harness-Model Collaboration for Long-Horizon Continual Learning

- [arXiv 2610.34724](https://arxiv.org/abs/2610.34724) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34724)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34724)

HaMo stores strategy cards extracted from expert trajectories, selects complementary anchors by retrieval coverage, and continually trains one LoRA adapter with experience-conditioned behavior cloning and historical replay. All environments are text-only; ScienceWorld/WebShop scores include partial credit, not binary success. Model-only ablation removes both harness memory and replay, confounding their contributions. Training uses three epochs per stage; optional memory deletion is disabled in every experiment. Within-domain stages introduce new samples, not new task types; multi-seed uncertainty is not established.

## RobotAgentBench: Towards Open-world Robot Autonomy

- [arXiv 2610.34649](https://arxiv.org/abs/2610.34649) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34649)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34649)

RobotAgentBench evaluates task discovery, context reasoning, manipulation, recovery and robustness plus open-ended household scenarios, comparing coding, learned and hybrid planning/execution/verification architectures. Scores are capability/scenario aggregates, not a universal task success rate. Main results are simulation; matched physical subsets cover only selected systems, not the best hybrid/RSI rows. Open-ended scores remain low and standalone versus agents differ in interfaces.

## ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation

- [arXiv 2610.34370](https://arxiv.org/abs/2610.34370) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34370)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34370)

ThinkLocoManip interleaves reasoning and action over perception, navigation, manipulation and whole-body locomotion tools; keyframe thinking retains execution context for recovery. Five task families on one platform, 10–20 trials per task. Tool orchestration includes engineered navigation/grasp/control capabilities; these results do not isolate cross-episode skill acquisition or establish portability of the whole-body controller.

## Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models

- [arXiv 2610.34251](https://arxiv.org/abs/2610.34251) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34251)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34251)

CogMemory adds a 3.45M-parameter history module: a selective state-space encoder, multi-slot temporal aggregation and variational compression, followed by gated cross-attention retrieval into two VLA fusion architectures. Simulation only and appendix specifies one seed (42), without multi-seed uncertainty. Policies and memory are optimized end-to-end for 30k steps on eight L20X GPUs, not an inference-only memory add-on. Best validation checkpoints are selected every 1k steps. Claimed 21.2→12.9s efficiency is task execution time on jointly successful cases, not measured model latency.

## Execution Logs Sway VLM Judges of Robot Progress

- [arXiv 2610.34151](https://arxiv.org/abs/2610.34151) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34151)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34151)

Controlled contradictory execution-log lines test whether VLM robot-progress judges follow text rather than visual evidence; a short unreliability warning is evaluated as mitigation. Conditional selected-clip effects, not population-wide failure rates; completion-claim search differs from the fixed-log test and was not tested on Sol. Warnings reduce misleading-log effects but also reduce benefits from accurate logs.

## RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models

- [arXiv 2610.34108](https://arxiv.org/abs/2610.34108) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.34108)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.34108)

RoboDuo lets a full-task VLA attempt the task, checks completion, then uses a separately trained atomic VLA through generated code to recover unfinished steps while keeping the full-task policy frozen. Not training-free overall: atomic policy and completion-checking coding agent use derived demonstration datasets. Gains shrink with five-suite training; real evaluation is one task family with small counts. Published reference rows use different protocols and are not matched reruns.

## Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents

- [arXiv 2610.33956](https://arxiv.org/abs/2610.33956) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33956)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33956)

CLE organizes 120 professional workflows into five dependent levels each, with persistent files/service state and human-authored rubrics; it measures complete agents under one- versus two-submission budgets. No robot tasks. Backbone parameters and harness implementation remain fixed; mutable context/memory is allowed, so results do not demonstrate recursive code/weight self-improvement. Trial 1/2 change submission budget and feedback, not just learning. One fixed task order, heterogeneous default agent settings and gated progression confound a pure memory-transfer interpretation.

## RoboLongR: Causally Consistent Rewards Teach Robots to Progressively Master Long-Horizon Manipulation

- [arXiv 2610.33863](https://arxiv.org/abs/2610.33863) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33863)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33863)

Learns history-sensitive rewards with recurrent memory, shuffled-stage negatives and terminal correction, then fine-tunes a behavioral-cloning policy with RL. Only 10 real trials per task. Removing memory, stage shuffling or correction yields 28.9%, 24.3% or 28.4%. Online correction is used by RoboLongR and Progress+Mono, but not ReWiND or other baselines; the main comparison tests complete pipelines.

## Memory or a Clock? Auditing a Memory Advantage in XLand-MiniGrid with Seeds, Maps and Evaluation Noise Apart

- [arXiv 2610.33816](https://arxiv.org/abs/2610.33816) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33816)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33816)

Audits recurrent-policy gains by separating training-seed, map and evaluation noise, then adding size-matched memory-free clock controls and recurrent-state resets. One 7×7-grid task, A2C and tiny networks; not a VLA or robot experiment. The 15pp preregistered advantage threshold fails despite a nonzero residual gap. Some no-clock and mechanism arms were added after interim/results inspection, and no time-independent reward control was run.

## RoboJev: An Open Vision-Language Judge for Robot Success Detection

- [arXiv 2610.33718](https://arxiv.org/abs/2610.33718) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33718)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33718)

RoboJev-27B adapts JEV-27B-VL with language-only rank-32 LoRA and source-specific KL anchoring, then predicts success with a calibrated two-token readout from ten primary frames plus available auxiliary final frames. Only 80/268 SO-101 episodes are held-out tasks. API baselines receive four primary frames, so frontier comparisons are not input-matched. Cost excludes media/serving overhead; community labels have one annotator; calibration and safety transfer are unestablished.

## MOON: Learning When to Forget and How to Move On in Vision-and-Language Navigation

- [arXiv 2610.33546](https://arxiv.org/abs/2610.33546) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33546)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33546)

MOON adds a deviation judge and GRPO-trained recovery adapter to a frozen vision-language navigation policy: an alarm clears visual history once, then recovery learns to escape history-induced behavioral inertia. Simulation only; deployment tested on one backbone and trains two adapters, not training-free. Alarm operating levels were selected on the reported evaluation splits. Clearing breaks 5.8%/4.1% of base-success episodes on R2R/RxR; successful forgetting is not evidence that long-term skill memory should be deleted.

## ReSight: Task-Driven Self-Improving Memory for Embodied Agents

- [arXiv 2610.33487](https://arxiv.org/abs/2610.33487) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33487)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33487)

ReSight separates immutable observation evidence from extensible derived fields. Explore–Distill–Mount uses a higher-budget coding agent to create reusable memory builders, tools and skills for a fixed-budget executor, without reference answers. Online savings exclude separate exploration, model preparation and memory-building costs. This is historical-observation QA, not closed-loop manipulation; OC-NaVQA binary accuracy decreases 86.6% to 82.1%. Long-term repeated capability expansion remains untested.

## MOTIO: Agentic Skill Engineering for Reality-Grounded Humanoid Loco-Manipulation

- [arXiv 2610.33446](https://arxiv.org/abs/2610.33446) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33446)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33446)

MOTIO turns human-action videos, metric 3D assets and existing robot-control interfaces into staged humanoid programs, revising them through physics feedback and human approval; generated skills also supervise BC/DAgger distillation. Human approval and task-specific engineering remain central. Physical demonstrations and simulated variation tests are not a randomized real-robot success benchmark; development time includes tool/resource waits. Distillation evidence is simulation-side.

## Tiny Recursive Policy: Recursive Latent Refinement for Visuomotor Control

- [arXiv 2610.33288](https://arxiv.org/abs/2610.33288) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33288)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33288)

A small behavior-cloning policy repeatedly refines two shared latent states within each prediction and carries them between control steps; training detaches temporal gradients. Simulation only; LIBERO-Mem reports subgoal completion, not binary task success. Parameters count only the backbone and do not measure inference cost: the default uses three high-level cycles and six low-level refinements. Perturbation training improves robustness but lowers clean Mem score to 0.480.

## Gaussian Episodic Memory for Long-Term Spatiotemporal Reasoning

- [arXiv 2610.33158](https://arxiv.org/abs/2610.33158) · v1 · [Latest entry](../daily/2026-10-27.md#arxiv-2610.33158)
- Coverage history: [2026-10-27 (v1, new)](../daily/2026-10-27.md#arxiv-2610.33158)

GEMS stores localized changes in a persistent temporal 3D Gaussian map and lets an agent retrieve, render novel views and compare revisits through a finite-state tool interface. Reported QA percentages are rescaled 1–5 judge scores, not binary exact-match accuracy. Three real scenes, pose/depth noise and novel-view artifacts; real score is below all-images. Storage comparison covers one scene per split and does not show online robot-policy gains.

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

## RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data

- [arXiv 2605.13775](https://arxiv.org/abs/2605.13775) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2605.13775)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2605.13775)

v1→v2 adds §5.5: the planner–simulator co-evolution loop is instantiated with action-capable LingBot-VA and LIBERO environment feedback. This is a new low-level-control extension, not a new version of the already reported generative-planning gains. The new extension uses external simulator feedback, unlike the internally supervised VLM–VGM setting. No physical deployment; 500 seeds do not represent the total supervision or interaction budget, and this section does not establish a complete interaction-cost match.

## A Semantic Autonomy Framework for VLM-Integrated Indoor Mobile Robots: Hybrid Deterministic Reasoning and Cross-Robot Adaptive Memory

- [arXiv 2605.02525](https://arxiv.org/abs/2605.02525) · v2 · [Latest entry](../daily/2026-10-27.md#arxiv-2605.02525)
- Coverage history: [2026-10-27 (v2, revised)](../daily/2026-10-27.md#arxiv-2605.02525)

SAS v1→v2 replaces broad cross-robot success framing with a frozen-implementation audit, sealed instruction challenge and controlled memory-on/memory-off/direct-VLM comparisons; recurrent associations are explicitly stability-tested rather than certified true. Two robot configurations in one indoor environment, with shared-workstation reasoning/memory and deliberate digest installation. Familiar-item scoring uses stored associations; unseen items gain no memory benefit. Replay seeds are not independent tasks, diagnostic probes are selected, and sampled consistency does not prove safe semantic transfer.

## RoboGene: Diversity-Driven Agentic Task Generation Framework for VLA Pre-training

- [arXiv 2602.16444](https://arxiv.org/abs/2602.16444) · v3 · [Latest entry](../daily/2026-10-27.md#arxiv-2602.16444)
- Coverage history: [2026-10-27 (v3, revised)](../daily/2026-10-27.md#arxiv-2602.16444)

v2→v3 adds broader real-robot OOD evaluation and human-effort/memory analysis (Appendix H.2/H.4), rather than merely restating the existing task-generation architecture and 18k trajectories. This is not zero-shot task transfer: target-task fine-tuning remains. Labor is estimated using fixed per-task/per-correction durations, including teleoperation and human verification; declining correction rates alone do not isolate memory causality.

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

## RynnUnify: Towards Unified Embodied Brain

- [arXiv 2610.32965](https://arxiv.org/abs/2610.32965) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32965)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32965)

A Cosmos3-based 16B model couples an 8B reasoner and 8B video generator. Cross-chunk scene frames support interleaved visual planning; a separately RL-trained reasoner chooses whether to request generated evidence, and WAM adaptation adds joint video-action learning. Robot adaptation uses roughly 1,600 hours of atomic and 177 hours of composite RoboCasa data. Full-split baseline numbers are imported from reports, whereas Selected-20 is evaluated by the authors. Visual history is within-episode context, not demonstrated lifelong memory; three real tasks do not isolate memory’s contribution.

## Predictive Long-Horizon Progress Modeling with Action-Aware Quantification

- [arXiv 2610.32776](https://arxiv.org/abs/2610.32776) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32776)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32776)

NimCritic couples predictive video learning with separate progress/completion outputs, perturbed progress history, and cross-modal alignment. LOOM contains 300 cross-embodiment trajectories and 19,618 human-calibrated frames. These are offline evaluator metrics, not robot task-success rates. Multi-subtask evaluation relies on offline VLM segmentation, not demonstrated real-time judging. Training uses 800+ hours and 48 accelerators; no closed-loop policy improvement from its reward is established.

## Semantic Representation for Agentic Self-Play in Automated Laboratories

- [arXiv 2610.32755](https://arxiv.org/abs/2610.32755) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32755)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32755)

VERID maintains a persistent semantic laboratory twin with introspection, pre-execution simulation gates, synchronized traces and resumable state. Agents retain physical operating bounds and analytical lessons across runs. These are small case studies, not an isolated causal memory ablation: challenge instances and experimental strategies change. Uses a structured harness, internal Gemini checkpoint and operator approval gates in supervised runs. Biological discoveries and broad robot-policy transfer are not demonstrated.

## $R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design

- [arXiv 2610.32439](https://arxiv.org/abs/2610.32439) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32439)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32439)

Coordinates Explorer, Guardian and Evolver LLM roles around a five-entry elite reward pool, using dynamic candidate allocation for iterative reward-program search. Only simulation and task-specific reward search, not cross-task robot skill accumulation. Elite-pool monotonicity concerns retained search scores, not guaranteed future policy improvement. RL training dominates compute; baseline search/token budgets should not be assumed identical merely because the backbone matches.

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

## RoboCode: Learning Reusable Action Primitives for Robot Manipulation

- [arXiv 2610.32225](https://arxiv.org/abs/2610.32225) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32225)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32225)

Learns a shared soft-compositional primitive codebook from pooled action chunks, then freezes its decoder and trains task-specific state-to-code encoders. Simulation only, with object poses/goals rather than image-language observations. Task-specific encoders are trained for the evaluated tasks; reusable codes are not evidence of online skill growth or unseen-task transfer. No multi-seed uncertainty or closed-loop trial count was established in the checked evaluation section.

## TTT in VLA Models: Exploring Training with Human Demonstrations

- [arXiv 2610.32094](https://arxiv.org/abs/2610.32094) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.32094)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.32094)

Integrates fast-weight TTT into InternVLA-A1 and pi0.5, documenting human-to-robot memory transfer and truncated gradient paths. Negative findings are limited to small cup-selection datasets and tested recipes, not a disproof of TTT. Trial counts are insufficiently reported. Autoregressive-state evaluation still uses recorded images, not closed-loop observations.

## FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation

- [arXiv 2610.31841](https://arxiv.org/abs/2610.31841) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31841)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31841)

A coding agent uses RGB-D and wrist force/torque logs to generate and revise Python contact-probing and force-feedback programs. Experience is retained in executable control logic, without task-specific model training. Five real tasks, one model, small trial counts. Each development run permits 20 physical rollouts and four hours; humans authorize execution, reset scenes and judge final acceptance. The ablation changes access to force feedback and routines together, not just memory. Reasoning costs 4–10 minutes per iteration.

## WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations

- [arXiv 2610.31834](https://arxiv.org/abs/2610.31834) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31834)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31834)

Constructs executable world programs from robot demonstrations, with a coding agent using replay feedback to repair scene geometry, assets, and physical interactions. Results concern recorded-trajectory replay in reconstructed simulation, not new-policy real-robot success or sim-to-real learning. Spatial metrics do not uniformly beat Astra, and component ablations cover one task, offering little evidence of a memory benefit.

## KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations

- [arXiv 2610.31801](https://arxiv.org/abs/2610.31801) · v1 · [Latest entry](../daily/2026-10-26.md#arxiv-2610.31801)
- Coverage history: [2026-10-26 (v1, new)](../daily/2026-10-26.md#arxiv-2610.31801)

Compresses shared 14-D bimanual kinematics into transition-supervised Sparse Motion Tokens at two tokens/second; a LoRA-adapted language model predicts temporal segments and descriptions, with transfer to new robots and human hands. The encoder uses whole-episode normalization and symmetric temporal context, so it is offline. Tokenizer comparisons differ in input representation and reader-training populations, not just objective. Segmentation/semantic transfer does not establish closed-loop robot-policy gains.

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

## WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time

- [arXiv 2607.06988](https://arxiv.org/abs/2607.06988) · v3 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.06988)
- Coverage history: [2026-10-26 (v3, revised)](../daily/2026-10-26.md#arxiv-2607.06988)

Human videos write fast-weight memory in a world-action model; paired human–robot meta-training teaches the video-to-action transfer interface. These are interface variants inside one WAM, not faithful evaluations of the complete original systems. The extra interface test covers one task; FastWAM evidence is qualitative eight-frame prediction over 3.2 s, not closed-loop control transfer. Some alternatives rely on pretrained skill latents absent from meta-training-only insertion.

## GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

- [arXiv 2607.05369](https://arxiv.org/abs/2607.05369) · v2 · [Latest entry](../daily/2026-10-26.md#arxiv-2607.05369)
- Coverage history: [2026-10-26 (v2, revised)](../daily/2026-10-26.md#arxiv-2607.05369)

GaP composes typed robot skill graphs and improves their structure, parameters and throughput through simulation rehearsal before deployment. New throughput evidence is simulation, not a new real-robot productivity result. The paper explicitly says CaP-X is not a fair standalone comparison because available environment geometry differs. MORSL equalizes selected perception/grasp components, not all motion primitives, inference budgets or system choices. The tasks are mostly quasi-static.

## METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

- [arXiv 2610.31656](https://arxiv.org/abs/2610.31656) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31656)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31656)

METTA separates fast gradient-updated within-episode neural memory from compact cross-episode summaries. It reports over 50% success on held-out Meta-World ML10/45 task families and better long-context sparse-reward exploration.

## FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies

- [arXiv 2610.31427](https://arxiv.org/abs/2610.31427) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31427)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31427)

FastHarness schedules GPT-6 Astra reviews of a frozen π0.5 policy using persistent stage and failure memory. Familiar execution skips reviews; risky states and recovery receive closer supervision without additional model training. The 80% comparison baseline is borrowed from another report, with five cases per task and a different scene mix, not a matched rerun. Episodes share memory and are not independent; the first tower episode already has prior experience. Savings are descriptive within-chain changes, not an end-to-end A/B effect. Evaluation is simulation-only and includes missed failures. The 57.2% is the mean of per-task percentage reductions, not the change in aggregate mean tokens. Token counts include input, output and cached inputs; they are not monetary costs.

## PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning

- [arXiv 2610.31299](https://arxiv.org/abs/2610.31299) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31299)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31299)

PiHand distills simulated mocap-tracking experts into a goal-conditioned hand–object latent prior, then learns bounded residual exploration in that latent space. The same interaction prior supports new objects, trajectories, catching and bimanual handovers.

## Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

- [arXiv 2610.31166](https://arxiv.org/abs/2610.31166) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.31166)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.31166)

WholeBodyMem selects historical frames from SAM3 object events and supplies object spatiotemporal tokens and memory attention to a whole-body action expert. This is within-episode perceptual history, not cross-episode skill accumulation. Physical tests have only ten trials per task and no uniform-memory real-robot comparator. Missed SAM3 detections and tracking overhead remain limitations.

## Co^2Gen: Collaboratively Generating Task Plans for Decentralized Multi-Robot and Human Collaboration

- [arXiv 2610.30671](https://arxiv.org/abs/2610.30671) · v1 · [Latest entry](../daily/2026-10-23.md#arxiv-2610.30671)
- Coverage history: [2026-10-23 (v1, new)](../daily/2026-10-23.md#arxiv-2610.30671)

Generates conditional collaborative programs with multi-agent planning, then converts executions into data for decentralized SmolVLA training. The strongest result depends on mixed human single-arm data, so the entire pipeline is not human-free. Generated data alone retains execution bottlenecks. Two tasks and limited trials do not establish general cross-embodiment transfer.

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

## Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- [arXiv 2609.39304](https://arxiv.org/abs/2609.39304) · v4 · [Latest entry](../daily/2026-10-23.md#arxiv-2609.39304)
- Coverage history: [2026-10-23 (v4, revised)](../daily/2026-10-23.md#arxiv-2609.39304)

Scale and Selection evolves a visual-interface robot-agent harness with rollout scaling and champion–challenger acceptance. The revision adds a distillation loop that transfers harness-assisted experience into a standalone robot policy.

## HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation

- [arXiv 2604.07993](https://arxiv.org/abs/2604.07993) · v3 · [Latest entry](../daily/2026-10-23.md#arxiv-2604.07993)
- Coverage history: [2026-10-23 (v3, revised)](../daily/2026-10-23.md#arxiv-2604.07993)

HEX combines canonical body-part states, a mixture-of-experts proprioceptive predictor, compact visual history and flow-matching actions for humanoid whole-body manipulation. This revision adds two household long-horizon tasks, a ψ0 comparison, OOD pretraining tests and data-scaling/sensitivity experiments.

## Agentic World Action Models

- [arXiv 2610.30136](https://arxiv.org/abs/2610.30136) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30136)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30136)

Joint code–video–action denoising connects agent planning and control, but random-domain performance is weaker than π0.5 and the skill library remains frozen.

## Asymmetric On-Policy Distillation Learns In-Context Exploration

- [arXiv 2610.30105](https://arxiv.org/abs/2610.30105) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30105)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30105)

Privileged on-policy distillation learns exploration across episodes sharing hidden conditions; real-robot samples are limited and context is not a permanent skill library.

## AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

- [arXiv 2610.30097](https://arxiv.org/abs/2610.30097) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.30097)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.30097)

Atomic subtask credit assignment and bottleneck exploration improve long-horizon RL; the real-robot gain is 8.0 points over PPO, with training performed in reconstructed simulation.

## GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

- [arXiv 2610.29866](https://arxiv.org/abs/2610.29866) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29866)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29866)

Training-only geometry supervision and temporal memory improve a shared VLA backbone; benchmark-specific adaptation and episode resets bound the generalization and memory claims.

## CausGround: Causal Interaction Grounding for Adaptive Embodied Planning

- [arXiv 2610.29702](https://arxiv.org/abs/2610.29702) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29702)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29702)

An offline causal knowledge base improves planning, but RoboCasa uses replay-based high-level evaluation and the knowledge base does not grow during deployment.

## From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

- [arXiv 2610.29560](https://arxiv.org/abs/2610.29560) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29560)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29560)

Offline harness revision raises RoboMME success from 44.38% to 51.38%; runtime context resets, and the reported repair does not establish new skill discovery.

## Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control

- [arXiv 2610.29329](https://arxiv.org/abs/2610.29329) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29329)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29329)

Executable, episode-local memory improves RoboMME performance, but unequal seeds and frame sampling limit the Astra+VLA comparison; cross-task skill growth is unproven.

## Learning to Absorb Corrections: Critic-Weighted Residual Flow for Vision-Based Insertion

- [arXiv 2610.29117](https://arxiv.org/abs/2610.29117) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.29117)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.29117)

Critic-weighted residual learning is absorbed into ACT: residual-off success improves from 16% to 76%; cross-task forgetting and VLA transfer remain untested.

## inr2action: Encoding Robot Episodes as Neural Implicit Representations for Recall and Action

- [arXiv 2610.28882](https://arxiv.org/abs/2610.28882) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28882)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28882)

Episode videos are stored as INR weight deltas; QA improves over chance, but offline action regression does not establish closed-loop control or scalable retrieval.

## T-WLA: Bridging Slow Vision and Fast Touch

- [arXiv 2610.28814](https://arxiv.org/abs/2610.28814) · v1 · [Latest entry](../daily/2026-10-22.md#arxiv-2610.28814)
- Coverage history: [2026-10-22 (v1, new)](../daily/2026-10-22.md#arxiv-2610.28814)

A fast tactile editor corrects pending actions, but the no-touch variant nearly matches full performance, limiting how much gain can be attributed to touch.

## HarnessPAI: An Evolving Harness for Physical AI

- [arXiv 2609.29166](https://arxiv.org/abs/2609.29166) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2609.29166)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2609.29166)

New DreamZero fine-tuning reuses successful harness trajectories, raising the reported mean from 5.1% to 26.5%; evaluation-based checkpoint selection limits the evidence.

## ASPIRE: Agentic /Skills Discovery for Robotics

- [arXiv 2607.00272](https://arxiv.org/abs/2607.00272) · v2 · [Latest entry](../daily/2026-10-22.md#arxiv-2607.00272)
- Coverage history: [2026-10-22 (v2, revised)](../daily/2026-10-22.md#arxiv-2607.00272)

The revision adds real-robot cross-episode textual skill accumulation; per-rotation time improves, but total cube-solving time is not monotonic and human support remains.

## UniWALM: Unified World Action Language Model for Embodied Robot Control

- [arXiv 2610.28626](https://arxiv.org/abs/2610.28626) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28626)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28626)

Joint video, action, and language denoising feeds textual working memory back into control. Gains on memory tasks and 18 real-robot trials do not isolate memory from other components or establish cross-episode retrieval.

## AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- [arXiv 2610.28589](https://arxiv.org/abs/2610.28589) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28589)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28589)

A 9B robotic planner improves through successful-trajectory SFT and multi-turn RL with a frozen executor. LIBERO-PRO reaches 71.0%, but tasks overlap between training and testing and no real-robot result is reported.

## Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future

- [arXiv 2610.28431](https://arxiv.org/abs/2610.28431) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.28431)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.28431)

Task and causal-state tokens steer world-action predictions through visually ambiguous stages. StageBench rises from 40.9% to 69.4%; real-robot gains require task demonstrations and have small trial counts.

## EventSync: Event-Driven Memory Updates for History-Dependent Manipulation

- [arXiv 2610.27917](https://arxiv.org/abs/2610.27917) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27917)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27917)

An event monitor commits task history only after visual and motion evidence confirms completion. RoboMME reaches 64.5%, but the monitor needs event supervision and the comparisons reuse published baselines.

## When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines

- [arXiv 2610.27714](https://arxiv.org/abs/2610.27714) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27714)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27714)

Resampled experience pools and token-matched controls reveal fragile memory gains in a driving agent. Conclusions are limited to HighwayEnv, gpt-4o-mini, and 1 Hz, rather than all long-term memory.

## More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents

- [arXiv 2610.27406](https://arxiv.org/abs/2610.27406) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.27406)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.27406)

Rebuilding and discarding task abstractions can reduce error reproduction while preserving raw experience. Three-seed ALFWorld gains are agent-specific and do not establish that all persistent memory is harmful.

## SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents

- [arXiv 2610.26995](https://arxiv.org/abs/2610.26995) · v1 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.26995)
- Coverage history: [2026-10-21 (v1, new)](../daily/2026-10-21.md#arxiv-2610.26995)

Skill-DAG memory and state-conditioned Skill-GNN selection reuse successful skill compositions. ALFWorld reaches 87.1%, but the work does not establish new motor-skill acquisition or real-robot transfer.

## HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents

- [arXiv 2610.23479](https://arxiv.org/abs/2610.23479) · v2 · [Latest entry](../daily/2026-10-21.md#arxiv-2610.23479)
- Coverage history: [2026-10-21 (v2, substantive-revision)](../daily/2026-10-21.md#arxiv-2610.23479)

A substantive revision adds official hidden-seed evaluation on 42 RoboDojo tasks. The 46.9% success rate uses a different protocol from v1; released tools do not include the entire evaluation system.

## WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning

- [arXiv 2607.18840](https://arxiv.org/abs/2607.18840) · v3 · [Latest entry](../daily/2026-10-21.md#arxiv-2607.18840)
- Coverage history: [2026-10-21 (v3, numerical-revision)](../daily/2026-10-21.md#arxiv-2607.18840)

Corrected C2R ablations reduce the marginal long-term-memory gain from 3.42 to 0.67 percentage points. Architecture, main results, and real-robot results are unchanged, and the correction is unexplained.

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

## SARAM: Sparse Adapter Allocation with Reuse and Merging for Lifelong Robot Learning

- [arXiv 2610.24804](https://arxiv.org/abs/2610.24804) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24804)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24804)

SARAM reuses old LoRA adapters, sparsely allocates new ones, and penalizes redundancy. It identifies the task at each episode start and merges the selected adapter into the backbone, providing a parameterized lifelong-learning approach.

## DialogMem: Evaluating Dialogue-Grounded Embodied Memory in 3D Environments

- [arXiv 2610.24767](https://arxiv.org/abs/2610.24767) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24767)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24767)

RGB-D, poses, and human dialogue are written to memory for instance navigation and question answering across 142 episodes, 27 scanned scenes, and nine memory representations. The diagnostic separates grounding, retrieval, and action localization.

## Self-Improving Video-to-Action Models

- [arXiv 2610.24177](https://arxiv.org/abs/2610.24177) · v1 · [Latest entry](../daily/2026-10-20.md#arxiv-2610.24177)
- Coverage history: [2026-10-20 (v1, new)](../daily/2026-10-20.md#arxiv-2610.24177)

A video planner proposes goal videos, and a video-to-action model generates video/action training pairs through its own interactions and improves iteratively.

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

## Spatial Memory by Agents, for Agents

- [arXiv 2610.22736](https://arxiv.org/abs/2610.22736) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22736)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22736)

A Designer Agent iterates memory construction and retrieval programs using feedback from a fixed Query Agent, then freezes the implementation for held-out observation histories. The tasks concern spatial/temporal questions, localization, and navigation queries, rather than continual manipulation-skill learning.

## When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

- [arXiv 2610.22556](https://arxiv.org/abs/2610.22556) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22556)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22556)

Disagreement between adjacent action chunks about the same future time supplies a memory-write signal. A bounded visual memory stores key frames and filters duplicates. Memory is cleared at the start of each episode, so this is within-episode memory.

## Scaling Online Exploration for Robot Agents

- [arXiv 2610.22496](https://arxiv.org/abs/2610.22496) · v1 · [Latest entry](../daily/2026-10-19.md#arxiv-2610.22496)
- Coverage history: [2026-10-19 (v1, new)](../daily/2026-10-19.md#arxiv-2610.22496)

A frozen coding agent explores through robot APIs and turns perception, planning, and control into executable programs. Persistent notes and validated skills support reuse across episodes and tasks.

