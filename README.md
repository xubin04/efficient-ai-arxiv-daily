# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-27 17:42 CST** · **2082 unique papers** · Newest submission: **2026-11-25**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 335 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 299 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 632 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 219 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 335 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 204 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 355 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 168 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 301 |

## Newly indexed · 2026-11-27

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

No newly indexed papers in this scan.

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **335 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **A Differential Computing Accelerator for LLM Inference Leveraging Bit-Slice Transition Sparsity**<br><sub>Yifan Wang, Zetao Guo, You Xiao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34630) · [PDF](https://arxiv.org/pdf/2611.34630) |
| 2026-11-25 | **Any-Rate: Half-Bit Multi-Precision LLM Quantization with Coded Bit-Planes**<br><sub>Hoonki Lee, Haechan Shin, Hyuntaek Jung et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34402) · [PDF](https://arxiv.org/pdf/2611.34402) · [Code](https://github.com/hoonki2002/Any-Rate) |
| 2026-11-24 | **JetDiffusion: Pushing the Speed Limits of Video Generation with NVFP4 Sparse Attention**<br><sub>Yulun Wu, Zihan Min, Minshen Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33268) · [PDF](https://arxiv.org/pdf/2611.33268) |
| 2026-11-24 | **Shifter Quantization: Compact Representations for Native Integer Computation**<br><sub>Yufeng Huang</sub> | [arXiv](https://arxiv.org/abs/2611.33080) · [PDF](https://arxiv.org/pdf/2611.33080) |
| 2026-11-24 | **Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?**<br><sub>Steffen Urban</sub> | [arXiv](https://arxiv.org/abs/2611.33031) · [PDF](https://arxiv.org/pdf/2611.33031) · [Code](https://github.com/urbste/weight-space-programming-ptq) |
| 2026-11-24 | **LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving**<br><sub>Wentao Zhu, Ziao Sheng, Peng Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32954) · [PDF](https://arxiv.org/pdf/2611.32954) |
| 2026-11-24 | **MXFP4 for LLM Inference: Complementary Post-Training Quantization Techniques and Their Interactions**<br><sub>Natalia Frumkin, Alireza Khodamoradi, Kristof Denolf et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32873) · [PDF](https://arxiv.org/pdf/2611.32873) |
| 2026-11-24 | **Measurement Artifacts in Trustworthiness Evaluations of Quantized Small Language Models**<br><sub>Tanzeel Abbas, Tehseen Zia, David Windridge</sub> | [arXiv](https://arxiv.org/abs/2611.32848) · [PDF](https://arxiv.org/pdf/2611.32848) |
| 2026-11-24 | **ReQOR: Operator-Discrepancy Subspace Repair for Quantization-Conditioned Backdoors in Large Language Models**<br><sub>Wonjune Seo, Minkyung Park, Saerom Park</sub> | [arXiv](https://arxiv.org/abs/2611.32755) · [PDF](https://arxiv.org/pdf/2611.32755) |
| 2026-11-24 | **HiCal: Offline Calibration for Hierarchical Scale Encoding in Accurate HiF4 Quantization**<br><sub>Zhiyuan Zhang, Yanzhao Li, Hui Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32624) · [PDF](https://arxiv.org/pdf/2611.32624) |
| 2026-11-24 | **LRQ-Cache: Compressing Feature Caches in Video Diffusion via Low-Rank Approximation and Quantization**<br><sub>Ruizhe Yao, Zhen Huang, Songpan Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32345) · [PDF](https://arxiv.org/pdf/2611.32345) |
| 2026-11-24 | **Bit-Flip Attacks on Quantized Neural Networks without Knowledge of Model Parameters**<br><sub>Mahmoud Abumandour, Srinija Ramichetty, Guru Venkataramani et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32128) · [PDF](https://arxiv.org/pdf/2611.32128) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **299 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator**<br><sub>Xiang Li, Hongyu Zhou, Ya-Li Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34750) · [PDF](https://arxiv.org/pdf/2611.34750) |
| 2026-11-25 | **A Differential Computing Accelerator for LLM Inference Leveraging Bit-Slice Transition Sparsity**<br><sub>Yifan Wang, Zetao Guo, You Xiao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34630) · [PDF](https://arxiv.org/pdf/2611.34630) |
| 2026-11-25 | **PURA: Video Token Pruning via Unified Spatiotemporal Redundancy Assessment**<br><sub>Yuyao Sun, Hongli Yuan, Shuang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34521) · [PDF](https://arxiv.org/pdf/2611.34521) |
| 2026-11-25 | **SPARC: Geometry-Guided Attention Pruning for Long-Horizon Camera-Controlled Video Generation**<br><sub>Zesong Yang, Weikai Chen, Liyuan Cui et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34064) · [PDF](https://arxiv.org/pdf/2611.34064) |
| 2026-11-24 | **Scalpel and Brush: Pruning and Targeted Weight Editing of a Small Language Model by a Single LLM Agent**<br><sub>Sergei Koltcov, Vera Ignatenko, Anton Surkov et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33426) · [PDF](https://arxiv.org/pdf/2611.33426) |
| 2026-11-24 | **JetDiffusion: Pushing the Speed Limits of Video Generation with NVFP4 Sparse Attention**<br><sub>Yulun Wu, Zihan Min, Minshen Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33268) · [PDF](https://arxiv.org/pdf/2611.33268) |
| 2026-11-24 | **Efficient Video Retrieval Augmented Generation via Token Allocation**<br><sub>Ayush Barik, Fan Lai, Francis Y. Yan</sub> | [arXiv](https://arxiv.org/abs/2611.32938) · [PDF](https://arxiv.org/pdf/2611.32938) |
| 2026-11-24 | **Scalable Placement for Disaggregated LLM Serving on Heterogeneous Edge Fleets**<br><sub>Truong-Thanh Le, Hoang-Loc La, Amir Taherkordi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32881) · [PDF](https://arxiv.org/pdf/2611.32881) |
| 2026-11-24 | **Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing**<br><sub>Guoxin Fan, Weilun Feng, Chuanguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32562) · [PDF](https://arxiv.org/pdf/2611.32562) · [Code](https://github.com/FofGofx/sol3) |
| 2026-11-24 | **Pando: Noise-Coupled Parallel Draft Trees for Efficient Edge Speculative Decoding**<br><sub>Joren Dumoulin, Hyoukjun Kwon, Subhankar Pal et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32269) · [PDF](https://arxiv.org/pdf/2611.32269) |
| 2026-11-24 | **LIBRA: Runtime Co-Tuning of Batch Size and Parallelism for Time-Efficient LLM Training**<br><sub>Shengkai Lyu, Hairui Zhao, Daran Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32008) · [PDF](https://arxiv.org/pdf/2611.32008) |
| 2026-11-24 | **Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion**<br><sub>Jian Yang, Zhizhuo Kou, Qiyuan Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31892) · [PDF](https://arxiv.org/pdf/2611.31892) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **632 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of 3D Intrinsic Proxies**<br><sub>Yipengjing Sun, Chenyang Wang, Boyao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34940) · [PDF](https://arxiv.org/pdf/2611.34940) |
| 2026-11-25 | **LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE**<br><sub>Jiachen An, Sijie Zhao, Le Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34912) · [PDF](https://arxiv.org/pdf/2611.34912) · [Code](https://github.com/MeiGen-AI/LiveVAE) |
| 2026-11-25 | **SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator**<br><sub>Xiang Li, Hongyu Zhou, Ya-Li Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34750) · [PDF](https://arxiv.org/pdf/2611.34750) |
| 2026-11-25 | **Seeing the Right Context: Grounded On-Policy Distillation for Remote Sensing**<br><sub>Yichang Luo, Hourun Zhu, Shixiong Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34700) · [PDF](https://arxiv.org/pdf/2611.34700) · [Code](https://github.com/YeeCharm/GeOPD) |
| 2026-11-25 | **WebVibe: Multimodal Interactive Website Generation via Reverse Synthesis and Visual Self-Distillation**<br><sub>Tianxiang Jiang, Sheng Xia, Yilin Long et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34292) · [PDF](https://arxiv.org/pdf/2611.34292) |
| 2026-11-25 | **OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction**<br><sub>Gen Li, Maoxin Chen, Yao Xiao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34155) · [PDF](https://arxiv.org/pdf/2611.34155) |
| 2026-11-25 | **Spe3DUp: Faithful Trajectory Distillation for Fast Image-to-3D Generation**<br><sub>Liangchao Xu, Jiaye Fu, Youtian Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34141) · [PDF](https://arxiv.org/pdf/2611.34141) |
| 2026-11-25 | **Understanding Diffusion Acceleration: Methods, Trade-Offs, and Open Questions**<br><sub>Xiaofeng Mao, Fu-yun Wang, Le Zhuo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34056) · [PDF](https://arxiv.org/pdf/2611.34056) |
| 2026-11-25 | **InstructTTS-OPD: On-Policy Distillation for Multi-Objective Instruction-Following TTS**<br><sub>Haitao Li, Tian Tan, Yuguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33937) · [PDF](https://arxiv.org/pdf/2611.33937) |
| 2026-11-25 | **X-Matte: VAE-Free Pixel-Space Flow Matching for Single-Step Image Matting**<br><sub>Zanyi Wang, Jiaang Li, Dengyang Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33874) · [PDF](https://arxiv.org/pdf/2611.33874) |
| 2026-11-25 | **Hybrid Reinforcement Learning for One-step Degraded Infrared and Visible Image Fusion**<br><sub>Hongwei Yu, Daoqing Zha, Jiawei Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33857) · [PDF](https://arxiv.org/pdf/2611.33857) |
| 2026-11-25 | **DriftWAM: Faster World-Action Models via Action-Aware Video Drifting**<br><sub>Minyang Li, Siyu Xu, Yunke Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33797) · [PDF](https://arxiv.org/pdf/2611.33797) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **219 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **Looped Models are Fast Multi-Token Predictors**<br><sub>Ayhan Suleymanzade, Sean McLeish, Sehoon Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33896) · [PDF](https://arxiv.org/pdf/2611.33896) |
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

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **335 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE**<br><sub>Jiachen An, Sijie Zhao, Le Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34912) · [PDF](https://arxiv.org/pdf/2611.34912) · [Code](https://github.com/MeiGen-AI/LiveVAE) |
| 2026-11-25 | **VAPOR: Improving Multimodal Reasoning with Sparse Visual Updates**<br><sub>Mingyu Su, Wei Wu, Erle Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33751) · [PDF](https://arxiv.org/pdf/2611.33751) · [Code](https://github.com/Su-my/VAPOR) |
| 2026-11-25 | **L2C2: Enhancing Large-scale Chiplets for Agent Long-Context LLM Inference with Sparse and Distributed Attention**<br><sub>Kangbo Bai, Zhonghua Mu, Hongze Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33691) · [PDF](https://arxiv.org/pdf/2611.33691) |
| 2026-11-25 | **State Space Attention: Learning Context-Dependent Memory Retention**<br><sub>Ege Çakar, Cengiz Pehlevan</sub> | [arXiv](https://arxiv.org/abs/2611.33625) · [PDF](https://arxiv.org/pdf/2611.33625) · [Code](https://github.com/Ege-Cakar/State-Space-Attention) |
| 2026-11-24 | **JetDiffusion: Pushing the Speed Limits of Video Generation with NVFP4 Sparse Attention**<br><sub>Yulun Wu, Zihan Min, Minshen Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33268) · [PDF](https://arxiv.org/pdf/2611.33268) |
| 2026-11-24 | **Eliciting the Recall Capacity of Linear Attention**<br><sub>Johan Lindqvist, Antonio Orvieto</sub> | [arXiv](https://arxiv.org/abs/2611.32969) · [PDF](https://arxiv.org/pdf/2611.32969) |
| 2026-11-24 | **LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving**<br><sub>Wentao Zhu, Ziao Sheng, Peng Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32954) · [PDF](https://arxiv.org/pdf/2611.32954) |
| 2026-11-24 | **Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing**<br><sub>Guoxin Fan, Weilun Feng, Chuanguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32562) · [PDF](https://arxiv.org/pdf/2611.32562) · [Code](https://github.com/FofGofx/sol3) |
| 2026-11-24 | **Factorized Context Attention: From Emulated to Native Grid Probing**<br><sub>Mohamed Eltahir, Manar Eyad, Yara Alzahrani et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32423) · [PDF](https://arxiv.org/pdf/2611.32423) · [Code](https://github.com/mohammad2012191/FCA) |
| 2026-11-24 | **Norn: Context-Length-Aware Optimization of Weight and KV Cache Placement for Offloaded LLM Inference**<br><sub>Naoto Sugiura, Hiroki Matsutani</sub> | [arXiv](https://arxiv.org/abs/2611.32295) · [PDF](https://arxiv.org/pdf/2611.32295) |
| 2026-11-24 | **Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion**<br><sub>Jian Yang, Zhizhuo Kou, Qiyuan Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31892) · [PDF](https://arxiv.org/pdf/2611.31892) |
| 2026-11-24 | **ET: Efficient Transfer from Softmax to Hybrid Attention**<br><sub>Guangfu Guo, Xiaoqian Lu, Linsey Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31770) · [PDF](https://arxiv.org/pdf/2611.31770) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **204 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **Asymmetric Speculative Decoding: Unlocking In-Context Learning in Draft Models**<br><sub>Guang Huang, Zeyi Wen</sub> | [arXiv](https://arxiv.org/abs/2611.34010) · [PDF](https://arxiv.org/pdf/2611.34010) |
| 2026-11-25 | **Looped Models are Fast Multi-Token Predictors**<br><sub>Ayhan Suleymanzade, Sean McLeish, Sehoon Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33896) · [PDF](https://arxiv.org/pdf/2611.33896) |
| 2026-11-25 | **ScanAR: Parallel Row-Scan Decoding for Efficient Image Generation in Unified Autoregressive Models**<br><sub>Jingen Qu, Xi Chen, Yingbo Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33761) · [PDF](https://arxiv.org/pdf/2611.33761) |
| 2026-11-24 | **Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions**<br><sub>Yuxing Liu, Wei Zuo, Walid Krichene et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33111) · [PDF](https://arxiv.org/pdf/2611.33111) |
| 2026-11-24 | **LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training**<br><sub>Hanzhen Wang, Jiaming Xu, Guohao Dai</sub> | [arXiv](https://arxiv.org/abs/2611.33004) · [PDF](https://arxiv.org/pdf/2611.33004) |
| 2026-11-24 | **Pando: Noise-Coupled Parallel Draft Trees for Efficient Edge Speculative Decoding**<br><sub>Joren Dumoulin, Hyoukjun Kwon, Subhankar Pal et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32269) · [PDF](https://arxiv.org/pdf/2611.32269) |
| 2026-11-24 | **How Much Dependency Can a Marginal Rule See? Total Correlation in Diffusion LM Parallel Decoding**<br><sub>Dovud Asadov, Rustambek Urokov, Qobiljon Toshnazarov et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31990) · [PDF](https://arxiv.org/pdf/2611.31990) · [Code](https://github.com/DovudAsadov/dllm-total-correlation) |
| 2026-11-23 | **Wavefront: Low-Rank Drafting with Parallel Causal Refinement for Speculative Decoding**<br><sub>Huy Huu Nguyen, Xin Huang</sub> | [arXiv](https://arxiv.org/abs/2611.31638) · [PDF](https://arxiv.org/pdf/2611.31638) |
| 2026-11-23 | **Self-Upgrading Embodied Agents**<br><sub>Jiajun Fan, Neil He, Qinglong Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31117) · [PDF](https://arxiv.org/pdf/2611.31117) |
| 2026-11-23 | **Speculate in the Right Order: Efficient Self-Speculative Decoding for Autoregressive Image Generation**<br><sub>Yihan Chen, Jintao Zhang, Jun Zhu</sub> | [arXiv](https://arxiv.org/abs/2611.30704) · [PDF](https://arxiv.org/pdf/2611.30704) |
| 2026-11-23 | **Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax**<br><sub>Huan Xu, Maosen Zhao, Pengtao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30587) · [PDF](https://arxiv.org/pdf/2611.30587) |
| 2026-11-23 | **CGSpec: Consistency-Guided Speculative Decoding with Overlap-Aware Verification Scheduling for Edge-Cloud Inference**<br><sub>Yuanbing Ouyang, Xiaoli Liu, Shirong Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30455) · [PDF](https://arxiv.org/pdf/2611.30455) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **355 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **PipeAxes: Decoupling Compute and Communication Granularities for Pipeline-Parallel LLM Serving**<br><sub>Xiaoqiang Guo, Yifan Lin, Yang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34615) · [PDF](https://arxiv.org/pdf/2611.34615) |
| 2026-11-25 | **Do We Really Need an LLM for Weight-Space Programming? A Deterministic Forward-Only Paradigm and Its Capability Boundaries**<br><sub>Lin Yao</sub> | [arXiv](https://arxiv.org/abs/2611.34612) · [PDF](https://arxiv.org/pdf/2611.34612) |
| 2026-11-24 | **RankCast: Phase-Aware Rank Balancing in MoE Serving**<br><sub>Kaidi Fu, Xu-Hao Lu, Pingwei Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33542) · [PDF](https://arxiv.org/pdf/2611.33542) |
| 2026-11-24 | **Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions**<br><sub>Yuxing Liu, Wei Zuo, Walid Krichene et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33111) · [PDF](https://arxiv.org/pdf/2611.33111) |
| 2026-11-24 | **Shifter Quantization: Compact Representations for Native Integer Computation**<br><sub>Yufeng Huang</sub> | [arXiv](https://arxiv.org/abs/2611.33080) · [PDF](https://arxiv.org/pdf/2611.33080) |
| 2026-11-24 | **Leto: Utility-Centric Agent Memory**<br><sub>Shuguang Chen, Salman Paracha</sub> | [arXiv](https://arxiv.org/abs/2611.33005) · [PDF](https://arxiv.org/pdf/2611.33005) |
| 2026-11-24 | **LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving**<br><sub>Wentao Zhu, Ziao Sheng, Peng Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32954) · [PDF](https://arxiv.org/pdf/2611.32954) |
| 2026-11-24 | **Scalable Placement for Disaggregated LLM Serving on Heterogeneous Edge Fleets**<br><sub>Truong-Thanh Le, Hoang-Loc La, Amir Taherkordi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32881) · [PDF](https://arxiv.org/pdf/2611.32881) |
| 2026-11-24 | **RePrism: Joint Request and Representation Scheduling for LLM Agent Serving**<br><sub>Xijiang Shen, Aoli Zhu, Yanbo Tan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32545) · [PDF](https://arxiv.org/pdf/2611.32545) |
| 2026-11-24 | **ViDM: Efficient and Order-Robust Parallel Visual Decision Making**<br><sub>Xudong Tan, Peng Ye, Chenyu Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32461) · [PDF](https://arxiv.org/pdf/2611.32461) |
| 2026-11-24 | **Norn: Context-Length-Aware Optimization of Weight and KV Cache Placement for Offloaded LLM Inference**<br><sub>Naoto Sugiura, Hiroki Matsutani</sub> | [arXiv](https://arxiv.org/abs/2611.32295) · [PDF](https://arxiv.org/pdf/2611.32295) |
| 2026-11-24 | **Generalized Tensor Parallelism: Powering Trillion-Parameter LLM Training at 10+ EFLOP/s**<br><sub>Shiqing Fan, Deepak Narayanan, Jimmy Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32057) · [PDF](https://arxiv.org/pdf/2611.32057) · [Code](https://github.com/NVIDIA/Megatron-LM) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **168 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE**<br><sub>Jiachen An, Sijie Zhao, Le Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34912) · [PDF](https://arxiv.org/pdf/2611.34912) · [Code](https://github.com/MeiGen-AI/LiveVAE) |
| 2026-11-25 | **TORE: Token-Wise Taylor Order Selection via Decomposed Residual Error Estimation for Diffusion Acceleration**<br><sub>Lei Tang, Baoquan Zhang, Yakun Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34261) · [PDF](https://arxiv.org/pdf/2611.34261) |
| 2026-11-25 | **Understanding Diffusion Acceleration: Methods, Trade-Offs, and Open Questions**<br><sub>Xiaofeng Mao, Fu-yun Wang, Le Zhuo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34056) · [PDF](https://arxiv.org/pdf/2611.34056) |
| 2026-11-25 | **FasterGRN: Reducing the Refinement Redundancy for Accelerating Generative Refinement Networks**<br><sub>Ziqian Zhang, Pengcheng Wang, Yulong Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33982) · [PDF](https://arxiv.org/pdf/2611.33982) |
| 2026-11-24 | **Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing**<br><sub>Guoxin Fan, Weilun Feng, Chuanguang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32562) · [PDF](https://arxiv.org/pdf/2611.32562) · [Code](https://github.com/FofGofx/sol3) |
| 2026-11-24 | **Every Edit Its Own Budget: Per-Instruction Token Freezing for Training-Free Acceleration of Multi-Edit Image Editing**<br><sub>Jyotirmoy Nath, Neeraj Kumar, Brejesh Lall</sub> | [arXiv](https://arxiv.org/abs/2611.32407) · [PDF](https://arxiv.org/pdf/2611.32407) |
| 2026-11-24 | **LRQ-Cache: Compressing Feature Caches in Video Diffusion via Low-Rank Approximation and Quantization**<br><sub>Ruizhe Yao, Zhen Huang, Songpan Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.32345) · [PDF](https://arxiv.org/pdf/2611.32345) |
| 2026-11-24 | **Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion**<br><sub>Jian Yang, Zhizhuo Kou, Qiyuan Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31892) · [PDF](https://arxiv.org/pdf/2611.31892) |
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **CHIP: Contrastive Hardware-Image Projection. Can OpenAI CLIP Reconstruct Images from the CPU Computational Footprint?**<br><sub>Debayan Sengupta, Darsh Asher, Kaushal Mhapsekar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30269) · [PDF](https://arxiv.org/pdf/2611.30269) |
| 2026-11-22 | **OnCache: Learning Dynamic Caching Schedules for Efficient Diffusion Inference**<br><sub>Zhikang Xie, Xichen Ye, Yifan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29480) · [PDF](https://arxiv.org/pdf/2611.29480) |
| 2026-11-21 | **RES: Accelerating Diffusion Language Models with Rolling Entropy Sampling**<br><sub>Patrick Pynadath, Nicolas Perez-Nieves, Bobak Shahriari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29066) · [PDF](https://arxiv.org/pdf/2611.29066) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **301 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-25 | **LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of 3D Intrinsic Proxies**<br><sub>Yipengjing Sun, Chenyang Wang, Boyao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34940) · [PDF](https://arxiv.org/pdf/2611.34940) |
| 2026-11-25 | **LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE**<br><sub>Jiachen An, Sijie Zhao, Le Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34912) · [PDF](https://arxiv.org/pdf/2611.34912) · [Code](https://github.com/MeiGen-AI/LiveVAE) |
| 2026-11-25 | **Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation**<br><sub>Shaoteng Liu, Shuai Yang, Wei Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34907) · [PDF](https://arxiv.org/pdf/2611.34907) |
| 2026-11-25 | **Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics**<br><sub>Chengzhi Zhao, Juelin Li, Zhennan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34644) · [PDF](https://arxiv.org/pdf/2611.34644) |
| 2026-11-25 | **TORE: Token-Wise Taylor Order Selection via Decomposed Residual Error Estimation for Diffusion Acceleration**<br><sub>Lei Tang, Baoquan Zhang, Yakun Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34261) · [PDF](https://arxiv.org/pdf/2611.34261) |
| 2026-11-25 | **SPARC: Geometry-Guided Attention Pruning for Long-Horizon Camera-Controlled Video Generation**<br><sub>Zesong Yang, Weikai Chen, Liyuan Cui et al.</sub> | [arXiv](https://arxiv.org/abs/2611.34064) · [PDF](https://arxiv.org/pdf/2611.34064) |
| 2026-11-25 | **FasterGRN: Reducing the Refinement Redundancy for Accelerating Generative Refinement Networks**<br><sub>Ziqian Zhang, Pengcheng Wang, Yulong Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33982) · [PDF](https://arxiv.org/pdf/2611.33982) |
| 2026-11-25 | **DriftWAM: Faster World-Action Models via Action-Aware Video Drifting**<br><sub>Minyang Li, Siyu Xu, Yunke Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33797) · [PDF](https://arxiv.org/pdf/2611.33797) |
| 2026-11-25 | **ScanAR: Parallel Row-Scan Decoding for Efficient Image Generation in Unified Autoregressive Models**<br><sub>Jingen Qu, Xi Chen, Yingbo Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33761) · [PDF](https://arxiv.org/pdf/2611.33761) |
| 2026-11-24 | **JetDiffusion: Pushing the Speed Limits of Video Generation with NVFP4 Sparse Attention**<br><sub>Yulun Wu, Zihan Min, Minshen Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33268) · [PDF](https://arxiv.org/pdf/2611.33268) |
| 2026-11-24 | **iWAM: Efficient Action Prediction from World Models without Explicit Future Prediction**<br><sub>Vansh Kapoor, Max Sobol Mark, Sreyas Venkataraman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.33141) · [PDF](https://arxiv.org/pdf/2611.33141) |
| 2026-11-24 | **RePix-VFI: Re-rendering Observed Pixels for Video Frame Interpolation with Generative Priors from One-Step Diffusion**<br><sub>Dayeon Kim, Jeonghyeok Do, Munchurl Kim</sub> | [arXiv](https://arxiv.org/abs/2611.33016) · [PDF](https://arxiv.org/pdf/2611.33016) |

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
