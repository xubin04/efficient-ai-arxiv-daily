# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-25 17:53 CST** · **2050 unique papers** · Newest submission: **2026-11-24**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 332 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 293 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 618 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 218 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 330 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 201 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 352 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 164 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 291 |

## Newly indexed · 2026-11-25

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **iWAM: Efficient Action Prediction from World Models without Explicit Future Prediction**<br><sub>Vansh Kapoor, Max Sobol Mark, Sreyas Venkataraman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33141) · [PDF](https://arxiv.org/pdf/2611.33141) |
| 2026-11-24 | **Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions**<br><sub>Yuxing Liu, Wei Zuo, Walid Krichene et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33111) · [PDF](https://arxiv.org/pdf/2611.33111) |
| 2026-11-24 | **Shifter Quantization: Compact Representations for Native Integer Computation**<br><sub>Yufeng Huang</sub> | [arXiv](https://arxiv.org/abs/2611.33080) · [PDF](https://arxiv.org/pdf/2611.33080) |
| 2026-11-24 | **Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?**<br><sub>Steffen Urban</sub> | [arXiv](https://arxiv.org/abs/2611.33031) · [PDF](https://arxiv.org/pdf/2611.33031) · [Code](https://github.com/urbste/weight-space-programming-ptq) |
| 2026-11-24 | **RePix-VFI: Re-rendering Observed Pixels for Video Frame Interpolation with Generative Priors from One-Step Diffusion**<br><sub>Dayeon Kim, Jeonghyeok Do, Munchurl Kim</sub> | [arXiv](https://arxiv.org/abs/2611.33016) · [PDF](https://arxiv.org/pdf/2611.33016) |
| 2026-11-24 | **Leto: Utility-Centric Agent Memory**<br><sub>Shuguang Chen, Salman Paracha</sub> | [arXiv](https://arxiv.org/abs/2611.33005) · [PDF](https://arxiv.org/pdf/2611.33005) |
| 2026-11-24 | **LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training**<br><sub>Hanzhen Wang, Jiaming Xu, Guohao Dai</sub> | [arXiv](https://arxiv.org/abs/2611.33004) · [PDF](https://arxiv.org/pdf/2611.33004) |
| 2026-11-24 | **Eliciting the Recall Capacity of Linear Attention**<br><sub>Johan Lindqvist, Antonio Orvieto</sub> | [arXiv](https://arxiv.org/abs/2611.32969) · [PDF](https://arxiv.org/pdf/2611.32969) |
| 2026-11-24 | **LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving**<br><sub>Wentao Zhu, Ziao Sheng, Peng Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32954) · [PDF](https://arxiv.org/pdf/2611.32954) |
| 2026-11-24 | **Efficient Video Retrieval Augmented Generation via Token Allocation**<br><sub>Ayush Barik, Fan Lai, Francis Y. Yan</sub> | [arXiv](https://arxiv.org/abs/2611.32938) · [PDF](https://arxiv.org/pdf/2611.32938) |
| 2026-11-24 | **Scalable Placement for Disaggregated LLM Serving on Heterogeneous Edge Fleets**<br><sub>Truong-Thanh Le, Hoang-Loc La, Amir Taherkordi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32881) · [PDF](https://arxiv.org/pdf/2611.32881) |
| 2026-11-24 | **MXFP4 for LLM Inference: Complementary Post-Training Quantization Techniques and Their Interactions**<br><sub>Natalia Frumkin, Alireza Khodamoradi, Kristof Denolf et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32873) · [PDF](https://arxiv.org/pdf/2611.32873) |
| 2026-11-24 | **Measurement Artifacts in Trustworthiness Evaluations of Quantized Small Language Models**<br><sub>Tanzeel Abbas, Tehseen Zia, David Windridge</sub> | [arXiv](https://arxiv.org/abs/2611.32848) · [PDF](https://arxiv.org/pdf/2611.32848) |
| 2026-11-24 | **Residual Guidance for Real-Time Interactive Video Generation**<br><sub>NaHyeon Park, Kyeong-Hwan Moon, Youjin Jeon et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32820) · [PDF](https://arxiv.org/pdf/2611.32820) |
| 2026-11-24 | **Scaling Laws of Ensemble Uncertainty in Language Models**<br><sub>Siamak Ravanbakhsh, David Nitchi, Khang Ngo</sub> | [arXiv](https://arxiv.org/abs/2611.32801) · [PDF](https://arxiv.org/pdf/2611.32801) |
| 2026-11-24 | **ReQOR: Operator-Discrepancy Subspace Repair for Quantization-Conditioned Backdoors in Large Language Models**<br><sub>Wonjune Seo, Minkyung Park, Saerom Park</sub> | [arXiv](https://arxiv.org/abs/2611.32755) · [PDF](https://arxiv.org/pdf/2611.32755) |
| 2026-11-24 | **HazeFlux: Few-Step Generative Priors for Real-World Image Dehazing**<br><sub>Yunong Liu, Danna Xue, Javier Vazquez-Corral</sub> | [arXiv](https://arxiv.org/abs/2611.32632) · [PDF](https://arxiv.org/pdf/2611.32632) |
| 2026-11-24 | **HiCal: Offline Calibration for Hierarchical Scale Encoding in Accurate HiF4 Quantization**<br><sub>Zhiyuan Zhang, Yanzhao Li, Hui Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32624) · [PDF](https://arxiv.org/pdf/2611.32624) |
| 2026-11-24 | **Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing**<br><sub>Guoxin Fan, Weilun Feng, Chuanguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32562) · [PDF](https://arxiv.org/pdf/2611.32562) · [Code](https://github.com/FofGofx/sol3) |
| 2026-11-24 | **RePrism: Joint Request and Representation Scheduling for LLM Agent Serving**<br><sub>Xijiang Shen, Aoli Zhu, Yanbo Tan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32545) · [PDF](https://arxiv.org/pdf/2611.32545) |

[View all 50 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **332 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **Shifter Quantization: Compact Representations for Native Integer Computation**<br><sub>Yufeng Huang</sub> | [arXiv](https://arxiv.org/abs/2611.33080) · [PDF](https://arxiv.org/pdf/2611.33080) |
| 2026-11-24 | **Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?**<br><sub>Steffen Urban</sub> | [arXiv](https://arxiv.org/abs/2611.33031) · [PDF](https://arxiv.org/pdf/2611.33031) · [Code](https://github.com/urbste/weight-space-programming-ptq) |
| 2026-11-24 | **LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving**<br><sub>Wentao Zhu, Ziao Sheng, Peng Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32954) · [PDF](https://arxiv.org/pdf/2611.32954) |
| 2026-11-24 | **MXFP4 for LLM Inference: Complementary Post-Training Quantization Techniques and Their Interactions**<br><sub>Natalia Frumkin, Alireza Khodamoradi, Kristof Denolf et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32873) · [PDF](https://arxiv.org/pdf/2611.32873) |
| 2026-11-24 | **Measurement Artifacts in Trustworthiness Evaluations of Quantized Small Language Models**<br><sub>Tanzeel Abbas, Tehseen Zia, David Windridge</sub> | [arXiv](https://arxiv.org/abs/2611.32848) · [PDF](https://arxiv.org/pdf/2611.32848) |
| 2026-11-24 | **ReQOR: Operator-Discrepancy Subspace Repair for Quantization-Conditioned Backdoors in Large Language Models**<br><sub>Wonjune Seo, Minkyung Park, Saerom Park</sub> | [arXiv](https://arxiv.org/abs/2611.32755) · [PDF](https://arxiv.org/pdf/2611.32755) |
| 2026-11-24 | **HiCal: Offline Calibration for Hierarchical Scale Encoding in Accurate HiF4 Quantization**<br><sub>Zhiyuan Zhang, Yanzhao Li, Hui Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32624) · [PDF](https://arxiv.org/pdf/2611.32624) |
| 2026-11-24 | **LRQ-Cache: Compressing Feature Caches in Video Diffusion via Low-Rank Approximation and Quantization**<br><sub>Ruizhe Yao, Zhen Huang, Songpan Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32345) · [PDF](https://arxiv.org/pdf/2611.32345) |
| 2026-11-24 | **Bit-Flip Attacks on Quantized Neural Networks without Knowledge of Model Parameters**<br><sub>Mahmoud Abumandour, Srinija Ramichetty, Guru Venkataramani et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32128) · [PDF](https://arxiv.org/pdf/2611.32128) |
| 2026-11-24 | **Rethinking Post-Training Quantization for Large Vision-Language Models**<br><sub>Minchan Kang, Kyeonghye Park, Seoyoung Cho et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32096) · [PDF](https://arxiv.org/pdf/2611.32096) · [Code](https://github.com/kmc3661/RRQ) |
| 2026-11-24 | **DeCo-Attention: Decompose to Compensate for Low-Precision Attention**<br><sub>Yuhang He, Harrison Zhang, Fanrong Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32035) · [PDF](https://arxiv.org/pdf/2611.32035) |
| 2026-11-24 | **Native Block-Quantized Matrix Multiplication and Explicit K/V Residency with Dual-View Access for LLM Inference on RISC-V Vector Processors**<br><sub>Weiying Wang, Yuanyang Xiang, Zhiwei Zhang</sub> | [arXiv](https://arxiv.org/abs/2611.31937) · [PDF](https://arxiv.org/pdf/2611.31937) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **293 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **Efficient Video Retrieval Augmented Generation via Token Allocation**<br><sub>Ayush Barik, Fan Lai, Francis Y. Yan</sub> | [arXiv](https://arxiv.org/abs/2611.32938) · [PDF](https://arxiv.org/pdf/2611.32938) |
| 2026-11-24 | **Scalable Placement for Disaggregated LLM Serving on Heterogeneous Edge Fleets**<br><sub>Truong-Thanh Le, Hoang-Loc La, Amir Taherkordi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32881) · [PDF](https://arxiv.org/pdf/2611.32881) |
| 2026-11-24 | **Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing**<br><sub>Guoxin Fan, Weilun Feng, Chuanguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32562) · [PDF](https://arxiv.org/pdf/2611.32562) · [Code](https://github.com/FofGofx/sol3) |
| 2026-11-24 | **Pando: Noise-Coupled Parallel Draft Trees for Efficient Edge Speculative Decoding**<br><sub>Joren Dumoulin, Hyoukjun Kwon, Subhankar Pal et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32269) · [PDF](https://arxiv.org/pdf/2611.32269) |
| 2026-11-24 | **LIBRA: Runtime Co-Tuning of Batch Size and Parallelism for Time-Efficient LLM Training**<br><sub>Shengkai Lyu, Hairui Zhao, Daran Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32008) · [PDF](https://arxiv.org/pdf/2611.32008) |
| 2026-11-24 | **Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion**<br><sub>Jian Yang, Zhizhuo Kou, Qiyuan Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31892) · [PDF](https://arxiv.org/pdf/2611.31892) |
| 2026-11-24 | **FN-Prune: Training-Free Expert Pruning with Finite RMSNorm Perturbations**<br><sub>Zeyan Li, Jianfeng Xu</sub> | [arXiv](https://arxiv.org/abs/2611.31747) · [PDF](https://arxiv.org/pdf/2611.31747) |
| 2026-11-23 | **Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action**<br><sub>Seongchan Kim, Soowon Son, Sangoh Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31240) · [PDF](https://arxiv.org/pdf/2611.31240) |
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **Uncovering the Tells: Efficient Black-Box Audits for LLM Data Contamination**<br><sub>Dominik Bernard Lau, Filip Pawlicki, Jan Dubiński et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30639) · [PDF](https://arxiv.org/pdf/2611.30639) |
| 2026-11-23 | **EdgeALM: An Efficient and Unified Edge Accelerator for Large Audio Language Models via Full-Stack Hardware-Software Co-Design and Agent-Driven Recursive Optimization**<br><sub>Chenglin Yang, Feifan Xu, Xingyuan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30216) · [PDF](https://arxiv.org/pdf/2611.30216) |
| 2026-11-23 | **PCC: Pivotal Channel Compensation for Layer Pruning of Large Language Models**<br><sub>Xiangqian Wang, Yucheng Zhang, Zhaohong Jia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30183) · [PDF](https://arxiv.org/pdf/2611.30183) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **618 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **RePix-VFI: Re-rendering Observed Pixels for Video Frame Interpolation with Generative Priors from One-Step Diffusion**<br><sub>Dayeon Kim, Jeonghyeok Do, Munchurl Kim</sub> | [arXiv](https://arxiv.org/abs/2611.33016) · [PDF](https://arxiv.org/pdf/2611.33016) |
| 2026-11-24 | **HazeFlux: Few-Step Generative Priors for Real-World Image Dehazing**<br><sub>Yunong Liu, Danna Xue, Javier Vazquez-Corral</sub> | [arXiv](https://arxiv.org/abs/2611.32632) · [PDF](https://arxiv.org/pdf/2611.32632) |
| 2026-11-24 | **STAR: Counterfactual Dual-World Rollouts and Spatial Target Adaptive Reconstruction for Visual On-Policy Distillation**<br><sub>Yi Zou, Zhuang Yan, Yudong Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32472) · [PDF](https://arxiv.org/pdf/2611.32472) |
| 2026-11-24 | **Describe, Don&#x27;t Ask: Caption-Driven On-Policy Distillation for Fine-Grained Visual Perception**<br><sub>Haozhan Shen, Liangbo He, Jun Lan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32463) · [PDF](https://arxiv.org/pdf/2611.32463) |
| 2026-11-24 | **The Teacher Is Already Inside: Self-Distilling Looped Language Models Beyond Their Last Loop**<br><sub>Linghua Zhang</sub> | [arXiv](https://arxiv.org/abs/2611.32452) · [PDF](https://arxiv.org/pdf/2611.32452) |
| 2026-11-24 | **VC-OPD: Learning to See What Matters via Visual Cue On-Policy Self-Distillation**<br><sub>Qinxuan Wang, Zheyu Zhang, Yijing Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32292) · [PDF](https://arxiv.org/pdf/2611.32292) |
| 2026-11-24 | **Rethinking Reasoning Effort Training in Large Language Models: On-Policy Distillation or Reinforcement Learning?**<br><sub>Tianliang Lv, Hao Li, Xinchao Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32131) · [PDF](https://arxiv.org/pdf/2611.32131) |
| 2026-11-24 | **HuluOPD: Unifying Heterogeneous Medical Specialists into One Lightweight Model with Unlabeled Prompts**<br><sub>Yuncheng Zhang, Songtao Jiang, Yitian Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32021) · [PDF](https://arxiv.org/pdf/2611.32021) |
| 2026-11-24 | **DexOPD: Dual-Extrapolation On-Policy Distillation for Diffusion Models**<br><sub>Yunchao Ke, Yanzhe Hu, Yi Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31969) · [PDF](https://arxiv.org/pdf/2611.31969) |
| 2026-11-24 | **Contrastive On-Policy Self-Distillation for LLM Unlearning**<br><sub>Fangzhou Lin, Shuo Xing, Xin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31932) · [PDF](https://arxiv.org/pdf/2611.31932) |
| 2026-11-24 | **Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion**<br><sub>Jian Yang, Zhizhuo Kou, Qiyuan Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31892) · [PDF](https://arxiv.org/pdf/2611.31892) |
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **218 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training**<br><sub>Hanzhen Wang, Jiaming Xu, Guohao Dai</sub> | [arXiv](https://arxiv.org/abs/2611.33004) · [PDF](https://arxiv.org/pdf/2611.33004) |
| 2026-11-24 | **Scaling Laws of Ensemble Uncertainty in Language Models**<br><sub>Siamak Ravanbakhsh, David Nitchi, Khang Ngo</sub> | [arXiv](https://arxiv.org/abs/2611.32801) · [PDF](https://arxiv.org/pdf/2611.32801) |
| 2026-11-24 | **Improving Character Identity Consistency in Diffusion-Based Visual Story Generation through Identity Memory and Automatic Reranking**<br><sub>Maria-Emilia Grigore, Stelian Spînu</sub> | [arXiv](https://arxiv.org/abs/2611.32383) · [PDF](https://arxiv.org/pdf/2611.32383) · [Code](https://github.com/MerryWex/character-consistency-visual-storytelling) |
| 2026-11-24 | **LIBRA: Runtime Co-Tuning of Batch Size and Parallelism for Time-Efficient LLM Training**<br><sub>Shengkai Lyu, Hairui Zhao, Daran Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32008) · [PDF](https://arxiv.org/pdf/2611.32008) |
| 2026-11-24 | **ET: Efficient Transfer from Softmax to Hybrid Attention**<br><sub>Guangfu Guo, Xiaoqian Lu, Linsey Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31770) · [PDF](https://arxiv.org/pdf/2611.31770) |
| 2026-11-23 | **LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents**<br><sub>Tianyi Huang, Samuel Xu, Ivy Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31105) · [PDF](https://arxiv.org/pdf/2611.31105) |
| 2026-11-23 | **Doc-to-LoRA Analysis: Query Conditioning, Wrong Facts, and Distractor Interference**<br><sub>Jesper Derehag</sub> | [arXiv](https://arxiv.org/abs/2611.30825) · [PDF](https://arxiv.org/pdf/2611.30825) |
| 2026-11-23 | **LiveMirror: Real-Time Diffusion Virtual Try-On on a Consumer GPU and Its Self-Supervised Adaptation to Indian Ethnic Wear**<br><sub>Jigyansha Jeevan Rout, Sukanta Kumar Sabut</sub> | [arXiv](https://arxiv.org/abs/2611.30461) · [PDF](https://arxiv.org/pdf/2611.30461) |
| 2026-11-23 | **Sparse Hodge Preference Optimization: Fine-Tuning Language Models toward Alignment beyond Transitive Preferences**<br><sub>Yiming Liu, Jianwei Ma, Zhongwei Xing et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30135) · [PDF](https://arxiv.org/pdf/2611.30135) |
| 2026-11-23 | **Parameter-Efficient Vocabulary Expansion via Cross-Lingual Embedding Alignment**<br><sub>Andrew Ivan Soegeng, Muhammad Reza Qorib, Weishi Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30123) · [PDF](https://arxiv.org/pdf/2611.30123) |
| 2026-11-21 | **Unlearning Model Identity: Ablating LoRA Weights from Question-Based Identity Tuning**<br><sub>Ming Cheung</sub> | [arXiv](https://arxiv.org/abs/2611.28650) · [PDF](https://arxiv.org/pdf/2611.28650) |
| 2026-11-20 | **Video-as-Weights: Compiling a Video Once into Parametric and Token Memory**<br><sub>Wentao Zhang, Ian Miao, Chen Qu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28221) · [PDF](https://arxiv.org/pdf/2611.28221) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **330 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **Eliciting the Recall Capacity of Linear Attention**<br><sub>Johan Lindqvist, Antonio Orvieto</sub> | [arXiv](https://arxiv.org/abs/2611.32969) · [PDF](https://arxiv.org/pdf/2611.32969) |
| 2026-11-24 | **LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving**<br><sub>Wentao Zhu, Ziao Sheng, Peng Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32954) · [PDF](https://arxiv.org/pdf/2611.32954) |
| 2026-11-24 | **Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing**<br><sub>Guoxin Fan, Weilun Feng, Chuanguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32562) · [PDF](https://arxiv.org/pdf/2611.32562) · [Code](https://github.com/FofGofx/sol3) |
| 2026-11-24 | **Factorized Context Attention: From Emulated to Native Grid Probing**<br><sub>Mohamed Eltahir, Manar Eyad, Yara Alzahrani et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32423) · [PDF](https://arxiv.org/pdf/2611.32423) · [Code](https://github.com/mohammad2012191/FCA) |
| 2026-11-24 | **Norn: Context-Length-Aware Optimization of Weight and KV Cache Placement for Offloaded LLM Inference**<br><sub>Naoto Sugiura, Hiroki Matsutani</sub> | [arXiv](https://arxiv.org/abs/2611.32295) · [PDF](https://arxiv.org/pdf/2611.32295) |
| 2026-11-24 | **Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion**<br><sub>Jian Yang, Zhizhuo Kou, Qiyuan Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31892) · [PDF](https://arxiv.org/pdf/2611.31892) |
| 2026-11-24 | **ET: Efficient Transfer from Softmax to Hybrid Attention**<br><sub>Guangfu Guo, Xiaoqian Lu, Linsey Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31770) · [PDF](https://arxiv.org/pdf/2611.31770) |
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents**<br><sub>Tianyi Huang, Samuel Xu, Ivy Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31105) · [PDF](https://arxiv.org/pdf/2611.31105) |
| 2026-11-23 | **Near-Far Attention: Region-Aware Sparse Retrieval for Long-Context LLM Decoding**<br><sub>YuanShuo Wang, Jianchao Tan, Lei Gong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30554) · [PDF](https://arxiv.org/pdf/2611.30554) |
| 2026-11-23 | **ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy**<br><sub>Hyunsu Ye, Hyunmin Choi, Jaehong Cho et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30417) · [PDF](https://arxiv.org/pdf/2611.30417) |
| 2026-11-23 | **When Does Optical Context Compression Pay Off? A Decode-Aware Cost Analysis of Reasoning VLMs**<br><sub>Ziqing Ge</sub> | [arXiv](https://arxiv.org/abs/2611.30130) · [PDF](https://arxiv.org/pdf/2611.30130) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **201 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions**<br><sub>Yuxing Liu, Wei Zuo, Walid Krichene et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33111) · [PDF](https://arxiv.org/pdf/2611.33111) |
| 2026-11-24 | **LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training**<br><sub>Hanzhen Wang, Jiaming Xu, Guohao Dai</sub> | [arXiv](https://arxiv.org/abs/2611.33004) · [PDF](https://arxiv.org/pdf/2611.33004) |
| 2026-11-24 | **Pando: Noise-Coupled Parallel Draft Trees for Efficient Edge Speculative Decoding**<br><sub>Joren Dumoulin, Hyoukjun Kwon, Subhankar Pal et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32269) · [PDF](https://arxiv.org/pdf/2611.32269) |
| 2026-11-24 | **How Much Dependency Can a Marginal Rule See? Total Correlation in Diffusion LM Parallel Decoding**<br><sub>Dovud Asadov, Rustambek Urokov, Qobiljon Toshnazarov et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31990) · [PDF](https://arxiv.org/pdf/2611.31990) · [Code](https://github.com/DovudAsadov/dllm-total-correlation) |
| 2026-11-23 | **Wavefront: Low-Rank Drafting with Parallel Causal Refinement for Speculative Decoding**<br><sub>Huy Huu Nguyen, Xin Huang</sub> | [arXiv](https://arxiv.org/abs/2611.31638) · [PDF](https://arxiv.org/pdf/2611.31638) |
| 2026-11-23 | **Self-Upgrading Embodied Agents**<br><sub>Jiajun Fan, Neil He, Qinglong Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31117) · [PDF](https://arxiv.org/pdf/2611.31117) |
| 2026-11-23 | **Speculate in the Right Order: Efficient Self-Speculative Decoding for Autoregressive Image Generation**<br><sub>Yihan Chen, Jintao Zhang, Jun Zhu</sub> | [arXiv](https://arxiv.org/abs/2611.30704) · [PDF](https://arxiv.org/pdf/2611.30704) |
| 2026-11-23 | **Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax**<br><sub>Huan Xu, Maosen Zhao, Pengtao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30587) · [PDF](https://arxiv.org/pdf/2611.30587) |
| 2026-11-23 | **CGSpec: Consistency-Guided Speculative Decoding with Overlap-Aware Verification Scheduling for Edge-Cloud Inference**<br><sub>Yuanbing Ouyang, Xiaoli Liu, Shirong Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30455) · [PDF](https://arxiv.org/pdf/2611.30455) |
| 2026-11-23 | **PackLoop: Row-Packed Self-Speculative Decoding for Looped Language Models under Concurrency**<br><sub>Runguo Li, Dezhen Lu</sub> | [arXiv](https://arxiv.org/abs/2611.30205) · [PDF](https://arxiv.org/pdf/2611.30205) |
| 2026-11-21 | **T2ISpec: Benchmarking Speculative Decoding for Text-to-Image Generation**<br><sub>Yifan Zhang, Shatong Zhu, Hui Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29029) · [PDF](https://arxiv.org/pdf/2611.29029) |
| 2026-11-20 | **Speculative Decoding Is Less Speculative Than You Think**<br><sub>Guanning Zeng, Andrea Zanette</sub> | [arXiv](https://arxiv.org/abs/2611.27891) · [PDF](https://arxiv.org/pdf/2611.27891) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **352 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions**<br><sub>Yuxing Liu, Wei Zuo, Walid Krichene et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33111) · [PDF](https://arxiv.org/pdf/2611.33111) |
| 2026-11-24 | **Shifter Quantization: Compact Representations for Native Integer Computation**<br><sub>Yufeng Huang</sub> | [arXiv](https://arxiv.org/abs/2611.33080) · [PDF](https://arxiv.org/pdf/2611.33080) |
| 2026-11-24 | **Leto: Utility-Centric Agent Memory**<br><sub>Shuguang Chen, Salman Paracha</sub> | [arXiv](https://arxiv.org/abs/2611.33005) · [PDF](https://arxiv.org/pdf/2611.33005) |
| 2026-11-24 | **LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving**<br><sub>Wentao Zhu, Ziao Sheng, Peng Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32954) · [PDF](https://arxiv.org/pdf/2611.32954) |
| 2026-11-24 | **Scalable Placement for Disaggregated LLM Serving on Heterogeneous Edge Fleets**<br><sub>Truong-Thanh Le, Hoang-Loc La, Amir Taherkordi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32881) · [PDF](https://arxiv.org/pdf/2611.32881) |
| 2026-11-24 | **RePrism: Joint Request and Representation Scheduling for LLM Agent Serving**<br><sub>Xijiang Shen, Aoli Zhu, Yanbo Tan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32545) · [PDF](https://arxiv.org/pdf/2611.32545) |
| 2026-11-24 | **ViDM: Efficient and Order-Robust Parallel Visual Decision Making**<br><sub>Xudong Tan, Peng Ye, Chenyu Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32461) · [PDF](https://arxiv.org/pdf/2611.32461) |
| 2026-11-24 | **Norn: Context-Length-Aware Optimization of Weight and KV Cache Placement for Offloaded LLM Inference**<br><sub>Naoto Sugiura, Hiroki Matsutani</sub> | [arXiv](https://arxiv.org/abs/2611.32295) · [PDF](https://arxiv.org/pdf/2611.32295) |
| 2026-11-24 | **Generalized Tensor Parallelism: Powering Trillion-Parameter LLM Training at 10+ EFLOP/s**<br><sub>Shiqing Fan, Deepak Narayanan, Jimmy Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32057) · [PDF](https://arxiv.org/pdf/2611.32057) · [Code](https://github.com/NVIDIA/Megatron-LM) |
| 2026-11-24 | **GreenDynaMix: Thermal-Aware Dynamic Mixed-Precision MoE LLM Inference Systems**<br><sub>Han-Yi Lin, Kieran Griperay, Qiang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31737) · [PDF](https://arxiv.org/pdf/2611.31737) |
| 2026-11-23 | **Wavefront: Low-Rank Drafting with Parallel Causal Refinement for Speculative Decoding**<br><sub>Huy Huu Nguyen, Xin Huang</sub> | [arXiv](https://arxiv.org/abs/2611.31638) · [PDF](https://arxiv.org/pdf/2611.31638) |
| 2026-11-23 | **LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents**<br><sub>Tianyi Huang, Samuel Xu, Ivy Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31105) · [PDF](https://arxiv.org/pdf/2611.31105) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **164 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing**<br><sub>Guoxin Fan, Weilun Feng, Chuanguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32562) · [PDF](https://arxiv.org/pdf/2611.32562) · [Code](https://github.com/FofGofx/sol3) |
| 2026-11-24 | **Every Edit Its Own Budget: Per-Instruction Token Freezing for Training-Free Acceleration of Multi-Edit Image Editing**<br><sub>Jyotirmoy Nath, Neeraj Kumar, Brejesh Lall</sub> | [arXiv](https://arxiv.org/abs/2611.32407) · [PDF](https://arxiv.org/pdf/2611.32407) |
| 2026-11-24 | **LRQ-Cache: Compressing Feature Caches in Video Diffusion via Low-Rank Approximation and Quantization**<br><sub>Ruizhe Yao, Zhen Huang, Songpan Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32345) · [PDF](https://arxiv.org/pdf/2611.32345) |
| 2026-11-24 | **Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion**<br><sub>Jian Yang, Zhizhuo Kou, Qiyuan Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31892) · [PDF](https://arxiv.org/pdf/2611.31892) |
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **CHIP: Contrastive Hardware-Image Projection. Can OpenAI CLIP Reconstruct Images from the CPU Computational Footprint?**<br><sub>Debayan Sengupta, Darsh Asher, Kaushal Mhapsekar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30269) · [PDF](https://arxiv.org/pdf/2611.30269) |
| 2026-11-22 | **OnCache: Learning Dynamic Caching Schedules for Efficient Diffusion Inference**<br><sub>Zhikang Xie, Xichen Ye, Yifan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29480) · [PDF](https://arxiv.org/pdf/2611.29480) |
| 2026-11-21 | **RES: Accelerating Diffusion Language Models with Rolling Entropy Sampling**<br><sub>Patrick Pynadath, Nicolas Perez-Nieves, Bobak Shahriari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29066) · [PDF](https://arxiv.org/pdf/2611.29066) |
| 2026-11-21 | **T2ISpec: Benchmarking Speculative Decoding for Text-to-Image Generation**<br><sub>Yifan Zhang, Shatong Zhu, Hui Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29029) · [PDF](https://arxiv.org/pdf/2611.29029) |
| 2026-11-20 | **Plan Big, Paint Small: Semantic-Aware Computation Allocation for Efficient Autoregressive Video Generation**<br><sub>Yixuan Luo, Yanjing Li</sub> | [arXiv](https://arxiv.org/abs/2611.28402) · [PDF](https://arxiv.org/pdf/2611.28402) |
| 2026-11-19 | **Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling**<br><sub>Yuchen Zhou, Lili Zheng, Yuxin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26407) · [PDF](https://arxiv.org/pdf/2611.26407) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **291 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-24 | **iWAM: Efficient Action Prediction from World Models without Explicit Future Prediction**<br><sub>Vansh Kapoor, Max Sobol Mark, Sreyas Venkataraman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33141) · [PDF](https://arxiv.org/pdf/2611.33141) |
| 2026-11-24 | **RePix-VFI: Re-rendering Observed Pixels for Video Frame Interpolation with Generative Priors from One-Step Diffusion**<br><sub>Dayeon Kim, Jeonghyeok Do, Munchurl Kim</sub> | [arXiv](https://arxiv.org/abs/2611.33016) · [PDF](https://arxiv.org/pdf/2611.33016) |
| 2026-11-24 | **Residual Guidance for Real-Time Interactive Video Generation**<br><sub>NaHyeon Park, Kyeong-Hwan Moon, Youjin Jeon et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32820) · [PDF](https://arxiv.org/pdf/2611.32820) |
| 2026-11-24 | **Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing**<br><sub>Guoxin Fan, Weilun Feng, Chuanguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32562) · [PDF](https://arxiv.org/pdf/2611.32562) · [Code](https://github.com/FofGofx/sol3) |
| 2026-11-24 | **LRQ-Cache: Compressing Feature Caches in Video Diffusion via Low-Rank Approximation and Quantization**<br><sub>Ruizhe Yao, Zhen Huang, Songpan Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32345) · [PDF](https://arxiv.org/pdf/2611.32345) |
| 2026-11-24 | **The Old Scene Lives in the Cache: Diagnosing and Shedding Stale History in Streaming Video Generation**<br><sub>Hao Zhou, Ziyang Xu, Chenhan Jin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32116) · [PDF](https://arxiv.org/pdf/2611.32116) |
| 2026-11-24 | **DexOPD: Dual-Extrapolation On-Policy Distillation for Diffusion Models**<br><sub>Yunchao Ke, Yanzhe Hu, Yi Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31969) · [PDF](https://arxiv.org/pdf/2611.31969) |
| 2026-11-24 | **Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion**<br><sub>Jian Yang, Zhizhuo Kou, Qiyuan Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31892) · [PDF](https://arxiv.org/pdf/2611.31892) |
| 2026-11-23 | **PromptSMC: Enabling Particle Exploration in Flow Matching via LLM-Based Prompt Rejuvenation**<br><sub>Wenyi Lian, Zheng Zhao, Thomas B. Schön</sub> | [arXiv](https://arxiv.org/abs/2611.31471) · [PDF](https://arxiv.org/pdf/2611.31471) · [Code](https://github.com/shermanlian/PromptSMC) |
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **Analyzing and Improving FlowMap Distillation of Autoregressive Video Models**<br><sub>Yong-Hyun Park, Guande He, Joon Hyeok Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31164) · [PDF](https://arxiv.org/pdf/2611.31164) |
| 2026-11-23 | **SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning**<br><sub>Kangping Hu, Akshay Mehra, Stephen Mussmann</sub> | [arXiv](https://arxiv.org/abs/2611.31163) · [PDF](https://arxiv.org/pdf/2611.31163) · [Code](https://github.com/ADDAPT-ML/SPROUT) |

## How it works

- Runs daily at **09:17 Asia/Shanghai (01:17 UTC)** using GitHub Actions. Scheduled starts can be delayed by GitHub.
- Queries the official arXiv API across titles and abstracts, then applies domain and efficiency-focus filters. A method or efficiency signal must appear in the title, or a contribution sentence must connect the method to efficiency. No paid AI API is used.
- Initial import: the last **30 days** of new or revised records. Later runs catch up from the previous successful scan, with a **7-day overlap** for delayed indexing.
- Deduplicates arXiv versions, preserves original submission dates, keeps history, and extracts code links when present in abstracts/comments.
- Any failed topic, malformed response, or truncated pagination fails the run before publishing. Empty successful searches do not erase the archive.
- **Automatic discovery, not a completeness or quality guarantee.** Keywords can miss papers or include weak matches. Summaries on the website are original arXiv abstracts.

## Customize or run locally

Requires **Python 3.11+**, with no third-party dependencies.

```bash
python -m unittest discover -s tests -v
python daily_arxiv.py
python daily_arxiv.py --days 60  # explicit backfill
python daily_arxiv.py --render-only  # rebuild from saved data
```

Edit `config.json` to change topic phrases. Within each topic, groups are joined with AND; phrases within a group are joined with OR. The **Actions → Update papers → Run workflow** button also supports a custom backfill window. If the result cap is reached, use a shorter window or raise the configured cap; the collector never silently truncates results.

GitHub may disable scheduled workflows in public repositories after 60 days without repository activity. If disabled, re-enable the workflow in Actions.

## Credits

Inspired by [cv-arxiv-daily](https://github.com/Vincentqyw/cv-arxiv-daily) and [Watermarking-arxiv-daily](https://github.com/ai-kunkun/Watermarking-arxiv-daily). Collector and website implemented independently. Thank you to arXiv for its open metadata API.
