# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-16 16:01 CST** · **1735 unique papers** · Newest submission: **2026-11-13**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 278 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 244 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 548 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 183 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 265 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 169 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 293 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 136 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 232 |

## Newly indexed · 2026-11-16

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-13 | **MMFlash: Faster Speculative Decoding for Vision-Language Models**<br><sub>Sicheng Feng, Zigeng Chen, Song Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18482) · [PDF](https://arxiv.org/pdf/2611.18482) |
| 2026-11-13 | **D2ToF: One-Step Diffusion for Depth Super-Resolution from Lightweight Single-Photon LiDAR Waveforms**<br><sub>Pallabjyoti Deka, Lewis Wilson, Stephen McLaughlin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18243) · [PDF](https://arxiv.org/pdf/2611.18243) |
| 2026-11-13 | **Token2Tile: Token-Wise Sparse Attention with Tile Execution through a Low-Rank Space for Video DiTs**<br><sub>Xuecheng Wu, Aichen Feng, Jinyan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17930) · [PDF](https://arxiv.org/pdf/2611.17930) |
| 2026-11-13 | **DiffusionSSD: Achieving Extreme Visual Compression with Dual-stage Diffusion and Cross-level Near-Data Processing**<br><sub>Kuai Yu, Wen Li, Shengwen Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17908) · [PDF](https://arxiv.org/pdf/2611.17908) |
| 2026-11-13 | **Speed-Variation Distillation for Generative Modeling**<br><sub>Sukit Seripanitkarn, Phonphrm Thawatdamrongkit, Supasorn Suwajanakorn</sub> | [arXiv](https://arxiv.org/abs/2611.17868) · [PDF](https://arxiv.org/pdf/2611.17868) |
| 2026-11-13 | **CHARMING: Parallel Edge AI Acceleration Across Tensor Processing and In-Memory Computation**<br><sub>Md Omar Faruque, Jingang Jin, João Paulo C. de Lima et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17785) · [PDF](https://arxiv.org/pdf/2611.17785) |
| 2026-11-13 | **Antidistillation is Cheap: Lightweight Distillation-Resistance via Stylistic Corruption**<br><sub>Anh Tu Ngo, Anupam Chattopadhyay</sub> | [arXiv](https://arxiv.org/abs/2611.17772) · [PDF](https://arxiv.org/pdf/2611.17772) |
| 2026-11-13 | **More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs**<br><sub>Seyed Mahmoud Sajjadi Mohammadabadi</sub> | [arXiv](https://arxiv.org/abs/2611.17610) · [PDF](https://arxiv.org/pdf/2611.17610) · [Code](https://github.com/mahmoudsajjadi/pace) |
| 2026-11-13 | **Choosing Quantized Code LLMs by File Size and Energy per Solved Task**<br><sub>Aditi Patodiya</sub> | [arXiv](https://arxiv.org/abs/2611.17605) · [PDF](https://arxiv.org/pdf/2611.17605) |
| 2026-11-12 | **User-Schedulable Approximations for Quantized Tensor Programs**<br><sub>Alex Reinking</sub> | [arXiv](https://arxiv.org/abs/2611.17526) · [PDF](https://arxiv.org/pdf/2611.17526) |
| 2026-11-12 | **Advancing Quantization for R&amp;R Models with Microscaling Formats**<br><sub>Yavuz Yetim, Bor-Yiing Su, Zhe Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17501) · [PDF](https://arxiv.org/pdf/2611.17501) |

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **278 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-13 | **CHARMING: Parallel Edge AI Acceleration Across Tensor Processing and In-Memory Computation**<br><sub>Md Omar Faruque, Jingang Jin, João Paulo C. de Lima et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17785) · [PDF](https://arxiv.org/pdf/2611.17785) |
| 2026-11-13 | **Choosing Quantized Code LLMs by File Size and Energy per Solved Task**<br><sub>Aditi Patodiya</sub> | [arXiv](https://arxiv.org/abs/2611.17605) · [PDF](https://arxiv.org/pdf/2611.17605) |
| 2026-11-12 | **User-Schedulable Approximations for Quantized Tensor Programs**<br><sub>Alex Reinking</sub> | [arXiv](https://arxiv.org/abs/2611.17526) · [PDF](https://arxiv.org/pdf/2611.17526) |
| 2026-11-12 | **Advancing Quantization for R&amp;R Models with Microscaling Formats**<br><sub>Yavuz Yetim, Bor-Yiing Su, Zhe Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17501) · [PDF](https://arxiv.org/pdf/2611.17501) |
| 2026-11-12 | **Lara Mini Base: Language Diversity as a Resource, Not a Trade-off**<br><sub>Translated, Maria Pia Adinolfi, Isabelle Andrieu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16956) · [PDF](https://arxiv.org/pdf/2611.16956) · [Code](https://huggingface.co/translated/Lara-4-Mini-Base) |
| 2026-11-12 | **STEALTH: Steganographic Text Encoding Agnostic to Low-Level Tensor Hardware**<br><sub>William Fleshman</sub> | [arXiv](https://arxiv.org/abs/2611.16928) · [PDF](https://arxiv.org/pdf/2611.16928) |
| 2026-11-12 | **SignRot: LLM Quantization with Massive Outlier-Aware Sign-Adjusted Rotation**<br><sub>Jaehun Gim, Jaewoo Kim, Gyuwan Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16502) · [PDF](https://arxiv.org/pdf/2611.16502) · [Code](https://github.com/HYU-ARK-Lab/SignRot) |
| 2026-11-12 | **One Model, Two Precisions: Does Disagreement Between Quantized Copies Tell You When a Small Model Is Wrong?**<br><sub>Mohammed Nayeem Khan, Allan Kevin T</sub> | [arXiv](https://arxiv.org/abs/2611.16478) · [PDF](https://arxiv.org/pdf/2611.16478) |
| 2026-11-12 | **SoScale: Second-Order Scale Search for FP4 Quantization**<br><sub>Pengxiang Zhao, Xing Li, Hui-Ling Zhen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16426) · [PDF](https://arxiv.org/pdf/2611.16426) |
| 2026-11-11 | **TraceKV: Policy-Preserving Low-Rank KV Cache Compression for Reasoning Vision-Language Models**<br><sub>Ke Li, Zishan Shao, Yiran Chen</sub> | [arXiv](https://arxiv.org/abs/2611.15569) · [PDF](https://arxiv.org/pdf/2611.15569) · [Code](https://github.com/AK-DREAM/TraceKV) |
| 2026-11-11 | **TQIR: Trellis Quantization with Integer Reconstruction for Bandwidth-Efficient Edge LLM Acceleration**<br><sub>Kuang-Ting Huang, Tian-Sheuan Chang</sub> | [arXiv](https://arxiv.org/abs/2611.15231) · [PDF](https://arxiv.org/pdf/2611.15231) |
| 2026-11-10 | **Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models**<br><sub>Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri</sub> | [arXiv](https://arxiv.org/abs/2611.14413) · [PDF](https://arxiv.org/pdf/2611.14413) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **244 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-13 | **Token2Tile: Token-Wise Sparse Attention with Tile Execution through a Low-Rank Space for Video DiTs**<br><sub>Xuecheng Wu, Aichen Feng, Jinyan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17930) · [PDF](https://arxiv.org/pdf/2611.17930) |
| 2026-11-12 | **DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models**<br><sub>Yi-Hsin Hung, Fangfu Liu, Shao-Yuan Lo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16345) · [PDF](https://arxiv.org/pdf/2611.16345) |
| 2026-11-12 | **Wanda-Guided Sparse Perturbations for Efficient Zeroth-Order Optimization**<br><sub>Ziqing Wen, Xiaohui Song, Jiahuan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16317) · [PDF](https://arxiv.org/pdf/2611.16317) |
| 2026-11-11 | **DiFiT: Distribution-Fidelity-guided Visual Token Pruning for Multimodal Large Language Models**<br><sub>Jingyuan Zhang, Nihao Niu, Xinyang Lv et al.</sub> | [arXiv](https://arxiv.org/abs/2611.15069) · [PDF](https://arxiv.org/pdf/2611.15069) |
| 2026-11-09 | **F3-AGI v4.0: Bioenergetically-Gated Active Inference, Metaplastic Preconditioning, and Residual Program Synthesis for Sample-Efficient Abstract Reasoning**<br><sub>Henrique Oliveira</sub> | [arXiv](https://arxiv.org/abs/2611.13325) · [PDF](https://arxiv.org/pdf/2611.13325) · [Code](https://github.com/henrique-polybee/f3-agi-v4) |
| 2026-11-09 | **Prune, Don&#x27;t Merge: Expert Compression of Mixture-of-Experts LLMs on Multilingual Production Tasks**<br><sub>Tomas Rasymas, Povilas Kvedaras</sub> | [arXiv](https://arxiv.org/abs/2611.12240) · [PDF](https://arxiv.org/pdf/2611.12240) |
| 2026-11-08 | **Language model capabilities fail in a shared, predictable order under compression and perturbation**<br><sub>Zhixiang Wang, Ulas Bagci</sub> | [arXiv](https://arxiv.org/abs/2611.11695) · [PDF](https://arxiv.org/pdf/2611.11695) · [Code](https://github.com/ZhixiangWang-CN/damage-order-artifacts) |
| 2026-11-08 | **Decomposing Earth Embeddings with Sparse Autoencoders**<br><sub>Vitus Benson, Fanny Yang, Markus Reichstein</sub> | [arXiv](https://arxiv.org/abs/2611.11398) · [PDF](https://arxiv.org/pdf/2611.11398) · [Code](https://github.com/EarthyScience/geosae) |
| 2026-11-08 | **D3Tree: Learning to Prune Block-Diffusion Draft Trees for Efficient Verification**<br><sub>Hong Nie, Zhangchi Gao, Jun Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11371) · [PDF](https://arxiv.org/pdf/2611.11371) |
| 2026-11-08 | **SGA-Sparse: Training Native SwiGLU Gates for Activation-Sparse and Low-Bit LLMs**<br><sub>Ruokai Yin, Steven Li</sub> | [arXiv](https://arxiv.org/abs/2611.11223) · [PDF](https://arxiv.org/pdf/2611.11223) |
| 2026-11-07 | **Slim Foundation Models for Latency-Critical Recommendation Serving**<br><sub>Danyal Aftab, Anas Zafar, Assadig Abakr et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11013) · [PDF](https://arxiv.org/pdf/2611.11013) |
| 2026-11-07 | **ESTRA: Enabling Extreme Attention Sparsity for Training-Free Video Diffusion Acceleration**<br><sub>Enhuai Liu, Yunke Wang, Yutong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10448) · [PDF](https://arxiv.org/pdf/2611.10448) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **548 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-13 | **D2ToF: One-Step Diffusion for Depth Super-Resolution from Lightweight Single-Photon LiDAR Waveforms**<br><sub>Pallabjyoti Deka, Lewis Wilson, Stephen McLaughlin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18243) · [PDF](https://arxiv.org/pdf/2611.18243) |
| 2026-11-13 | **DiffusionSSD: Achieving Extreme Visual Compression with Dual-stage Diffusion and Cross-level Near-Data Processing**<br><sub>Kuai Yu, Wen Li, Shengwen Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17908) · [PDF](https://arxiv.org/pdf/2611.17908) |
| 2026-11-13 | **Speed-Variation Distillation for Generative Modeling**<br><sub>Sukit Seripanitkarn, Phonphrm Thawatdamrongkit, Supasorn Suwajanakorn</sub> | [arXiv](https://arxiv.org/abs/2611.17868) · [PDF](https://arxiv.org/pdf/2611.17868) |
| 2026-11-13 | **Antidistillation is Cheap: Lightweight Distillation-Resistance via Stylistic Corruption**<br><sub>Anh Tu Ngo, Anupam Chattopadhyay</sub> | [arXiv](https://arxiv.org/abs/2611.17772) · [PDF](https://arxiv.org/pdf/2611.17772) |
| 2026-11-12 | **eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation**<br><sub>Tong Zhao, Xianfang Zeng, Yucheng Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17194) · [PDF](https://arxiv.org/pdf/2611.17194) · [Code](https://github.com/Westlake-AGI-Lab/eDMD) |
| 2026-11-12 | **Teach with Blinks: Breaking Linguistic Momentum in On-Policy Distillation for Fine-Grained Multimodal Perception**<br><sub>Tangzheng Lian, Hang Zhang, Guanyu Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16402) · [PDF](https://arxiv.org/pdf/2611.16402) · [Code](https://github.com/Supltz/BlinkOPD) |
| 2026-11-12 | **From Large Language Models to Efficient System One Models via Adaptive Computation**<br><sub>Minh-Anh Nguyen</sub> | [arXiv](https://arxiv.org/abs/2611.16321) · [PDF](https://arxiv.org/pdf/2611.16321) |
| 2026-11-12 | **What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation**<br><sub>Jinze Tao, Yuxiao Han, Kangkang Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16246) · [PDF](https://arxiv.org/pdf/2611.16246) |
| 2026-11-12 | **Disentangled Embedding Optimization for Diffusion-Based Dataset Distillation**<br><sub>Hongcheng Li, Yucan Zhou, Yibin Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16224) · [PDF](https://arxiv.org/pdf/2611.16224) |
| 2026-11-12 | **Turning Multi-Agent Communication into Token-Level Credit with On Policy Self Distillation**<br><sub>Zixu Wang, Yu Zhao, Xing Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16206) · [PDF](https://arxiv.org/pdf/2611.16206) · [Code](https://github.com/Camel-Prince/OPSD4MAS) |
| 2026-11-11 | **Prior-as-Skill: Remember Outside and Read Inside with On-Policy Self-Distillation for Self-Evolving VLM Agents**<br><sub>Yan Lin, Jingyu Sun, Yifei Qian et al.</sub> | [arXiv](https://arxiv.org/abs/2611.15766) · [PDF](https://arxiv.org/pdf/2611.15766) |
| 2026-11-11 | **WaveFlow-UIE: A Single-Pipeline Wavelet-Domain Flow Model for Efficient Underwater Image Restoration**<br><sub>Abdulaziz Alfaraj, Mohammed Al Naser, Hassan Al Nasser et al.</sub> | [arXiv](https://arxiv.org/abs/2611.15457) · [PDF](https://arxiv.org/pdf/2611.15457) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **183 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-12 | **Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models**<br><sub>Tanzeel Abbas, Ahmad Kamran Malik, Nafees Qamar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17128) · [PDF](https://arxiv.org/pdf/2611.17128) |
| 2026-11-12 | **Predicting Ethanol Drinking Status from Nonhuman Primate Liver Histology: A Proof of Concept for Parameter-efficient Fine-tuning in Few-Shot Vision-Language Modeling**<br><sub>Amirmohammad Mohammadi, Rupak Khadka, Kathleen A. Grant et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17105) · [PDF](https://arxiv.org/pdf/2611.17105) · [Code](https://github.com/Advanced-Vision-and-Learning-Lab/ALD_VLM) |
| 2026-11-12 | **Factored One-sided Adam-Moment for Practical and Scalable SOAP**<br><sub>Jaemyung Yu, Byeongho Heo, Sangdoo Yun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16905) · [PDF](https://arxiv.org/pdf/2611.16905) · [Code](https://github.com/naver-ai/foam) |
| 2026-11-12 | **TokenStream: Multi-Subject Personalized Video Generation with Token-wise LoRA and Guided Attention**<br><sub>Hung Nguyen, Quang Qui-Vinh Nguyen, Khoi Nguyen</sub> | [arXiv](https://arxiv.org/abs/2611.16897) · [PDF](https://arxiv.org/pdf/2611.16897) |
| 2026-11-12 | **Sustainable Federated Fine-Tuning with LoRA: Environmental Impact and Performance Footprint**<br><sub>Pedro Augusto Londe Ribeiro, Rodrigo Moreira, Larissa Ferreira Rodrigues Moreira et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16856) · [PDF](https://arxiv.org/pdf/2611.16856) |
| 2026-11-12 | **SS-HSDP: Efficient and Flexible Sharded Data Parallelism via Runtime-Update Decoupling**<br><sub>Chendong Xiang, Pengle Zhang, Jinliang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16467) · [PDF](https://arxiv.org/pdf/2611.16467) |
| 2026-11-10 | **Sckwoky at SHROOM-Visions: Character-Level Hallucination-Span Detection in Image-Conditioned VLMs via Dual-Prompted LoRA Decoders**<br><sub>Mikhail Kulakov, Ruslan Solikhov, Ivan Bondarenko</sub> | [arXiv](https://arxiv.org/abs/2611.14100) · [PDF](https://arxiv.org/pdf/2611.14100) |
| 2026-11-09 | **VeilTune: Secure Fine-Tuning of Private LoRA Adapters on Public Pretrained Language Models**<br><sub>Huiyu Xie, Tanping Zhou, Tao Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11817) · [PDF](https://arxiv.org/pdf/2611.11817) |
| 2026-11-07 | **Slim Foundation Models for Latency-Critical Recommendation Serving**<br><sub>Danyal Aftab, Anas Zafar, Assadig Abakr et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11013) · [PDF](https://arxiv.org/pdf/2611.11013) |
| 2026-11-07 | **Bayesian Low-Rank Posteriors for Scalable Membership Inference**<br><sub>Khanh Nguyen, Antonio Emanuele Cinà, Andrey Barsky et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10455) · [PDF](https://arxiv.org/pdf/2611.10455) |
| 2026-11-07 | **Reproducible LoRA Inference Through Deterministic Split-K Reduction**<br><sub>Dhayaneshwar Balusamy, Ankur Mohan</sub> | [arXiv](https://arxiv.org/abs/2611.10334) · [PDF](https://arxiv.org/pdf/2611.10334) |
| 2026-11-06 | **FedLoVA: Value-Only Aggregation for Federated LoRA Fine-Tuning of Large Language Models**<br><sub>Ensieh Khazaei, Baturalp Buyukates, Dimitrios Hatzinakos</sub> | [arXiv](https://arxiv.org/abs/2611.10248) · [PDF](https://arxiv.org/pdf/2611.10248) · [Code](https://github.com/EnsiehKhazaei/FedLoVA) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **265 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-13 | **MMFlash: Faster Speculative Decoding for Vision-Language Models**<br><sub>Sicheng Feng, Zigeng Chen, Song Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18482) · [PDF](https://arxiv.org/pdf/2611.18482) |
| 2026-11-13 | **Token2Tile: Token-Wise Sparse Attention with Tile Execution through a Low-Rank Space for Video DiTs**<br><sub>Xuecheng Wu, Aichen Feng, Jinyan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17930) · [PDF](https://arxiv.org/pdf/2611.17930) |
| 2026-11-12 | **Towards Green Text Generation: Memory-Based Speculative Decoding**<br><sub>Antal van den Bosch</sub> | [arXiv](https://arxiv.org/abs/2611.16714) · [PDF](https://arxiv.org/pdf/2611.16714) · [Code](https://github.com/antalvdb/olifant-speculative) |
| 2026-11-12 | **Beyond Compressing Everything: Contrastive Memory Learning for Selective Context Compression**<br><sub>Sikui Zhang, Haowei Liu, Ziyun Gan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16384) · [PDF](https://arxiv.org/pdf/2611.16384) · [Code](https://github.com/scar-on/CoMem) |
| 2026-11-11 | **TraceKV: Policy-Preserving Low-Rank KV Cache Compression for Reasoning Vision-Language Models**<br><sub>Ke Li, Zishan Shao, Yiran Chen</sub> | [arXiv](https://arxiv.org/abs/2611.15569) · [PDF](https://arxiv.org/pdf/2611.15569) · [Code](https://github.com/AK-DREAM/TraceKV) |
| 2026-11-10 | **SinkState: On-the-Fly SVD of Recurrent States for Efficient Hybrid LLM Serving**<br><sub>Haolin Jiang, Weihang Li, Zhongzhu Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.14246) · [PDF](https://arxiv.org/pdf/2611.14246) |
| 2026-11-10 | **Can KV Cache Be Reused Across Model Updates? A DeepSeek-V4-Flash Case Study**<br><sub>Zhikun Tao, Fangyong Jin, Junping Zhao</sub> | [arXiv](https://arxiv.org/abs/2611.14051) · [PDF](https://arxiv.org/pdf/2611.14051) |
| 2026-11-10 | **POEM: Output-Relative Block-Sparse Attention for Long-Context Prefilling**<br><sub>Haoyi Wu, Yunkai Dang, Wanyu Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13578) · [PDF](https://arxiv.org/pdf/2611.13578) |
| 2026-11-09 | **Looping Deeper Without Growing the KV Cache: Recurrent Depth for Causal Encoder-Decoders**<br><sub>Jiaqi Leng, Minshen Zhang, Zhaofeng Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13378) · [PDF](https://arxiv.org/pdf/2611.13378) |
| 2026-11-09 | **Decode Token Parallelism: Memory-Efficient Distributed Attention Parallelism for Scalable LLM Decoding**<br><sub>Susav Shrestha, Brad Settlemyer, Narasimha Reddy</sub> | [arXiv](https://arxiv.org/abs/2611.13293) · [PDF](https://arxiv.org/pdf/2611.13293) |
| 2026-11-09 | **Evolving Infra: Agent-Adaptive LLM Serving at Scale**<br><sub>Hao Kang, Weili Xu, Ziyang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12304) · [PDF](https://arxiv.org/pdf/2611.12304) · [Code](https://github.com/mit-han-lab/EvolvingInfra) |
| 2026-11-09 | **Translating KV Caches Between Hybrid-Attention Language Models: MLA Latents, Linear-Attention States and Sparse-Attention Indexers**<br><sub>Povilas Kvedaras, Tomas Rasymas</sub> | [arXiv](https://arxiv.org/abs/2611.12062) · [PDF](https://arxiv.org/pdf/2611.12062) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **169 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-13 | **MMFlash: Faster Speculative Decoding for Vision-Language Models**<br><sub>Sicheng Feng, Zigeng Chen, Song Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18482) · [PDF](https://arxiv.org/pdf/2611.18482) |
| 2026-11-13 | **More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs**<br><sub>Seyed Mahmoud Sajjadi Mohammadabadi</sub> | [arXiv](https://arxiv.org/abs/2611.17610) · [PDF](https://arxiv.org/pdf/2611.17610) · [Code](https://github.com/mahmoudsajjadi/pace) |
| 2026-11-12 | **Towards Green Text Generation: Memory-Based Speculative Decoding**<br><sub>Antal van den Bosch</sub> | [arXiv](https://arxiv.org/abs/2611.16714) · [PDF](https://arxiv.org/pdf/2611.16714) · [Code](https://github.com/antalvdb/olifant-speculative) |
| 2026-11-11 | **Early Signals, Strong Decisions: Prefix-Guided Sampling for Parallel Test-Time Scaling**<br><sub>Jie Ren, Jonathan Rosenfeld, Neil Thompson</sub> | [arXiv](https://arxiv.org/abs/2611.14965) · [PDF](https://arxiv.org/pdf/2611.14965) |
| 2026-11-10 | **REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding**<br><sub>Yu Tian</sub> | [arXiv](https://arxiv.org/abs/2611.14399) · [PDF](https://arxiv.org/pdf/2611.14399) · [Code](https://github.com/King-ty/speculators/tree/real-loss) |
| 2026-11-10 | **ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding**<br><sub>Jaeyong Song, Daniel Wang, Pratyush Patel et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13442) · [PDF](https://arxiv.org/pdf/2611.13442) · [Code](https://github.com/facebookresearch/ForeSpark) |
| 2026-11-09 | **DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees**<br><sub>Zhicheng Zheng, Cheng Zhang, Chenkai Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12356) · [PDF](https://arxiv.org/pdf/2611.12356) · [Code](https://github.com/Perseus037/DForkTree) |
| 2026-11-09 | **Depth as a Candidate Source: Portfolio Allocation for Recurrent Test-Time Scaling in Large Language Models**<br><sub>Chaoyuan Hao, Wentao Yue, Yanyan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12293) · [PDF](https://arxiv.org/pdf/2611.12293) |
| 2026-11-08 | **ODSA: Orchestrated Discovery and Self-Aggregation**<br><sub>Macardle Meng, Haomin Zhang</sub> | [arXiv](https://arxiv.org/abs/2611.11621) · [PDF](https://arxiv.org/pdf/2611.11621) |
| 2026-11-08 | **D3Tree: Learning to Prune Block-Diffusion Draft Trees for Efficient Verification**<br><sub>Hong Nie, Zhangchi Gao, Jun Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11371) · [PDF](https://arxiv.org/pdf/2611.11371) |
| 2026-11-07 | **Coverage-Verified Sparse Attention: Closed-Loop Quality Control for Long-Context LLM Decoding**<br><sub>Yan-Cheng Li, Chun-Yi Lee</sub> | [arXiv](https://arxiv.org/abs/2611.10634) · [PDF](https://arxiv.org/pdf/2611.10634) |
| 2026-11-07 | **Test-Time Scaling for Diffusion Language Models with Frequency-Aware Remasking**<br><sub>Bowen Zuo, Yue Yu, Dongruo Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10486) · [PDF](https://arxiv.org/pdf/2611.10486) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **293 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-12 | **Broadcast, Don&#x27;t Replicate: Eliminating Weight HBM in Datacenter LLM Serving**<br><sub>Hannah Atmer, Yuan Yao, Thiemo Voigt et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17097) · [PDF](https://arxiv.org/pdf/2611.17097) |
| 2026-11-12 | **Discovering Effective Agent Memory Designs through Program Evolution**<br><sub>Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17068) · [PDF](https://arxiv.org/pdf/2611.17068) · [Code](https://github.com/ash-ding/MAPE) |
| 2026-11-12 | **DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models**<br><sub>Yi-Hsin Hung, Fangfu Liu, Shao-Yuan Lo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16345) · [PDF](https://arxiv.org/pdf/2611.16345) |
| 2026-11-12 | **Fast Serverless LLM Cold Starts by Sharing and Prewarming Startup Work**<br><sub>Hongjin Kim, Igjae Kim, Kwanghoon Choi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16180) · [PDF](https://arxiv.org/pdf/2611.16180) |
| 2026-11-11 | **Fewer Expert Transfers Without Changing Routing: Expert Eviction for MoE Offloading**<br><sub>Pierre-Luc Bacon, Diego Calanzone, Jean-Maxime Larouche</sub> | [arXiv](https://arxiv.org/abs/2611.15842) · [PDF](https://arxiv.org/pdf/2611.15842) · [Code](https://github.com/carbonforgeAI/moe-expert-eviction) |
| 2026-11-10 | **SinkState: On-the-Fly SVD of Recurrent States for Efficient Hybrid LLM Serving**<br><sub>Haolin Jiang, Weihang Li, Zhongzhu Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.14246) · [PDF](https://arxiv.org/pdf/2611.14246) |
| 2026-11-10 | **Scaling Shapley Energy Attribution to Large LLM Batches**<br><sub>Qi Luo, Ziwen Wang, Kunlin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13802) · [PDF](https://arxiv.org/pdf/2611.13802) |
| 2026-11-10 | **Exploiting What NVIDIA Profilers Hide: Fast and Accurate Analytical GPU Performance Modeling**<br><sub>Ziwen Wang, Qi Luo, Kunlin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13762) · [PDF](https://arxiv.org/pdf/2611.13762) |
| 2026-11-10 | **ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding**<br><sub>Jaeyong Song, Daniel Wang, Pratyush Patel et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13442) · [PDF](https://arxiv.org/pdf/2611.13442) · [Code](https://github.com/facebookresearch/ForeSpark) |
| 2026-11-10 | **Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving**<br><sub>Wen Huang, Jack Liu</sub> | [arXiv](https://arxiv.org/abs/2611.13412) · [PDF](https://arxiv.org/pdf/2611.13412) |
| 2026-11-09 | **Looping Deeper Without Growing the KV Cache: Recurrent Depth for Causal Encoder-Decoders**<br><sub>Jiaqi Leng, Minshen Zhang, Zhaofeng Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13378) · [PDF](https://arxiv.org/pdf/2611.13378) |
| 2026-11-09 | **Decode Token Parallelism: Memory-Efficient Distributed Attention Parallelism for Scalable LLM Decoding**<br><sub>Susav Shrestha, Brad Settlemyer, Narasimha Reddy</sub> | [arXiv](https://arxiv.org/abs/2611.13293) · [PDF](https://arxiv.org/pdf/2611.13293) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **136 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-13 | **D2ToF: One-Step Diffusion for Depth Super-Resolution from Lightweight Single-Photon LiDAR Waveforms**<br><sub>Pallabjyoti Deka, Lewis Wilson, Stephen McLaughlin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18243) · [PDF](https://arxiv.org/pdf/2611.18243) |
| 2026-11-12 | **DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models**<br><sub>Yi-Hsin Hung, Fangfu Liu, Shao-Yuan Lo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16345) · [PDF](https://arxiv.org/pdf/2611.16345) |
| 2026-11-10 | **Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models**<br><sub>Amir Mann, Jonathan Fhima, Shaked Brody et al.</sub> | [arXiv](https://arxiv.org/abs/2611.14387) · [PDF](https://arxiv.org/pdf/2611.14387) |
| 2026-11-10 | **AdjointFlow: Accelerating Scientific Inverse Problems with Physics-Based Transport**<br><sub>Ethan Hanold, Nicholas M. Boffi, Qin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13389) · [PDF](https://arxiv.org/pdf/2611.13389) |
| 2026-11-09 | **DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees**<br><sub>Zhicheng Zheng, Cheng Zhang, Chenkai Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12356) · [PDF](https://arxiv.org/pdf/2611.12356) · [Code](https://github.com/Perseus037/DForkTree) |
| 2026-11-08 | **MG-Cache: Multi-Granularity Caching for Accelerating Diffusion Transformer Inference**<br><sub>Zesen Chen, Youxuan Xu, Shigang Li</sub> | [arXiv](https://arxiv.org/abs/2611.11365) · [PDF](https://arxiv.org/pdf/2611.11365) |
| 2026-11-07 | **FADE: Fractional Anomalous Dynamics Extrapolation for Training-Free Diffusion Transformers Acceleration**<br><sub>Jinlong Yang, Lizilin, Jinke Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10514) · [PDF](https://arxiv.org/pdf/2611.10514) |
| 2026-11-07 | **ESTRA: Enabling Extreme Attention Sparsity for Training-Free Video Diffusion Acceleration**<br><sub>Enhuai Liu, Yunke Wang, Yutong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10448) · [PDF](https://arxiv.org/pdf/2611.10448) |
| 2026-11-07 | **IdealCache: Rethinking Cache Scheduling in Diffusion Transformers via Ideal Trajectories**<br><sub>Shang Xue, Li Zhu, Ping Chen</sub> | [arXiv](https://arxiv.org/abs/2611.10340) · [PDF](https://arxiv.org/pdf/2611.10340) |
| 2026-11-06 | **Verifier Noise Is a Temperature: Testing Tilt Predictions in Finite-Budget LLM-Guided Search**<br><sub>Xiaomeng Li</sub> | [arXiv](https://arxiv.org/abs/2611.09699) · [PDF](https://arxiv.org/pdf/2611.09699) |
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **232 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-13 | **Token2Tile: Token-Wise Sparse Attention with Tile Execution through a Low-Rank Space for Video DiTs**<br><sub>Xuecheng Wu, Aichen Feng, Jinyan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17930) · [PDF](https://arxiv.org/pdf/2611.17930) |
| 2026-11-13 | **Speed-Variation Distillation for Generative Modeling**<br><sub>Sukit Seripanitkarn, Phonphrm Thawatdamrongkit, Supasorn Suwajanakorn</sub> | [arXiv](https://arxiv.org/abs/2611.17868) · [PDF](https://arxiv.org/pdf/2611.17868) |
| 2026-11-13 | **CHARMING: Parallel Edge AI Acceleration Across Tensor Processing and In-Memory Computation**<br><sub>Md Omar Faruque, Jingang Jin, João Paulo C. de Lima et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17785) · [PDF](https://arxiv.org/pdf/2611.17785) |
| 2026-11-10 | **Location Matters: Sparse Latent-Variance Attacks for Face Privacy against Diffusion Personalization**<br><sub>Shuting Yang, Shuxin Li, Linyan Dai et al.</sub> | [arXiv](https://arxiv.org/abs/2611.14254) · [PDF](https://arxiv.org/pdf/2611.14254) · [Code](https://github.com/Lvxan/SEAL) |
| 2026-11-10 | **Few-Step Streaming Video Generation via Condition Shifting**<br><sub>Deyuan Liu, Jungang Li, Kaiwen Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.14033) · [PDF](https://arxiv.org/pdf/2611.14033) |
| 2026-11-10 | **When to Start Denoising? Adaptive Denoising Entry for Generative Video Compression**<br><sub>Zifu Zhang, Yuqiao Li, Ding Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13620) · [PDF](https://arxiv.org/pdf/2611.13620) |
| 2026-11-09 | **Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos**<br><sub>Hai Zhang, Siqi Liang, Yanjun Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12087) · [PDF](https://arxiv.org/pdf/2611.12087) |
| 2026-11-09 | **Four-Step Text-Bearing Image Generation via Distillation with Local Response Regularization and Teacher-Guided Training**<br><sub>Kairui Wen, Sheng Ye, Yong-Jin Liu</sub> | [arXiv](https://arxiv.org/abs/2611.12042) · [PDF](https://arxiv.org/pdf/2611.12042) |
| 2026-11-08 | **ForeAct: Geometry-Guided Action Learning from World Representations**<br><sub>Wei Lu, Jiaxi Zhang, Yunheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11500) · [PDF](https://arxiv.org/pdf/2611.11500) |
| 2026-11-08 | **G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation**<br><sub>Xu Huang, Ye Huang, Xiaotong Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13004) · [PDF](https://arxiv.org/pdf/2611.13004) |
| 2026-11-08 | **Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation**<br><sub>Weizhong Huang, Huaijia Kou, Tianyu Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11452) · [PDF](https://arxiv.org/pdf/2611.11452) |
| 2026-11-08 | **MG-Cache: Multi-Granularity Caching for Accelerating Diffusion Transformer Inference**<br><sub>Zesen Chen, Youxuan Xu, Shigang Li</sub> | [arXiv](https://arxiv.org/abs/2611.11365) · [PDF](https://arxiv.org/pdf/2611.11365) |

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
