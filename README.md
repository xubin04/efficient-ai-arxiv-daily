# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-18 16:35 CST** · **1827 unique papers** · Newest submission: **2026-11-17**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 291 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 260 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 568 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 200 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 285 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 179 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 313 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 143 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 247 |

## Newly indexed · 2026-11-18

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching**<br><sub>Giannis Daras, Marios Papachristou, Adam Klivans et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23229) · [PDF](https://arxiv.org/pdf/2611.23229) |
| 2026-11-17 | **Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models**<br><sub>Rui Ning, Om Chabra, Hari Balakrishnan</sub> | [arXiv](https://arxiv.org/abs/2611.23228) · [PDF](https://arxiv.org/pdf/2611.23228) |
| 2026-11-17 | **FastFrames: Video Generation at Interactive Latency**<br><sub>Gene Chou, Guandao Yang, Fujun Luan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) |
| 2026-11-17 | **Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU**<br><sub>Mehmet Altan Toksöz</sub> | [arXiv](https://arxiv.org/abs/2611.23205) · [PDF](https://arxiv.org/pdf/2611.23205) |
| 2026-11-17 | **MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study**<br><sub>Nikit Srivastava, Joel Dag, René Speck et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23158) · [PDF](https://arxiv.org/pdf/2611.23158) |
| 2026-11-17 | **TextSphere: Efficient Text-to-Image Generation via Shared Hyperspherical Alignment and Uniformity**<br><sub>Yixia Zhang, Girish A. Koushik, Xilu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23155) · [PDF](https://arxiv.org/pdf/2611.23155) |
| 2026-11-17 | **Transfer Once, Ask Locally: Compact Audio-Visual Memory for On-Device Question Answering**<br><sub>Qitong Wang, Jihui Jin, Divya Kothandaraman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23085) · [PDF](https://arxiv.org/pdf/2611.23085) |
| 2026-11-17 | **M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with Multi-Teacher On-Policy Distillation**<br><sub>Nguyen Quang Trung, Hoang Phan, Shuo Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23034) · [PDF](https://arxiv.org/pdf/2611.23034) |
| 2026-11-17 | **The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale**<br><sub>Fırat Öncel, Cem Subakan, Mirco Ravanelli et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22947) · [PDF](https://arxiv.org/pdf/2611.22947) · [Code](https://github.com/firatoncel/KernelRealityCheckNeurIPS2026) |
| 2026-11-17 | **Code World Model 2.0: Towards Infinite Controllable Video Generation**<br><sub>Ruoyu Wang, Hao Zhong, Yanming Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22925) · [PDF](https://arxiv.org/pdf/2611.22925) |
| 2026-11-17 | **SilverSpoon-KD: A General-Purpose Toolkit for Knowledge Distillation**<br><sub>Xaver R. Davey, David Broman</sub> | [arXiv](https://arxiv.org/abs/2611.22842) · [PDF](https://arxiv.org/pdf/2611.22842) · [Code](https://github.com/silverspoon-dev/silverspoon-kd) |
| 2026-11-17 | **LoopPrune: Recurrent Pruning for Looped Diffusion Transformers**<br><sub>Weizhong Huang, Huaijia Kou, Yan Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22757) · [PDF](https://arxiv.org/pdf/2611.22757) |
| 2026-11-17 | **LoopZip: Visual Token Compression for Efficient Looped Vision-Language Models**<br><sub>Weizhong Huang, Zhicheng Liu, Yan Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22728) · [PDF](https://arxiv.org/pdf/2611.22728) |
| 2026-11-17 | **HADVQ: Hessian Aware Directional Vector Quantization**<br><sub>Daniil Li, Mars Davletshin, Vadim Klyzhenko et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22721) · [PDF](https://arxiv.org/pdf/2611.22721) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |
| 2026-11-17 | **Semantic-Guided Geometric Decoding for Token-Efficient Visual Grounding**<br><sub>Zhaojie Chen, Junyan Yang, Le Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22577) · [PDF](https://arxiv.org/pdf/2611.22577) |
| 2026-11-17 | **Efficient Self-Supervised Adaptation of 3D Abdominal Vision-Language Model for Institution-Specific HCC Classification via Full Fine-Tuning and PEFT**<br><sub>Febryan Putra Kartika, Cheng-Yu Ma, Ying-Jia Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22504) · [PDF](https://arxiv.org/pdf/2611.22504) |
| 2026-11-17 | **Fast and Strong Image Protection against Diffusion Personalization**<br><sub>Jiwon Park, Jihye Kang, Namhyuk Ahn</sub> | [arXiv](https://arxiv.org/abs/2611.22494) · [PDF](https://arxiv.org/pdf/2611.22494) |
| 2026-11-17 | **BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning**<br><sub>Juyoung Park, Heejun Lee</sub> | [arXiv](https://arxiv.org/abs/2611.22334) · [PDF](https://arxiv.org/pdf/2611.22334) |
| 2026-11-17 | **SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding**<br><sub>Selin Yildirim, Ali Zeyrek, Deming Chen</sub> | [arXiv](https://arxiv.org/abs/2611.22296) · [PDF](https://arxiv.org/pdf/2611.22296) |

[View all 36 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **291 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **HADVQ: Hessian Aware Directional Vector Quantization**<br><sub>Daniil Li, Mars Davletshin, Vadim Klyzhenko et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22721) · [PDF](https://arxiv.org/pdf/2611.22721) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |
| 2026-11-17 | **BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning**<br><sub>Juyoung Park, Heejun Lee</sub> | [arXiv](https://arxiv.org/abs/2611.22334) · [PDF](https://arxiv.org/pdf/2611.22334) |
| 2026-11-17 | **Communicate the Change: Efficient Expert Parallelism via Activation Compression**<br><sub>Fengyuan Liu, Jay Gala, Siva Reddy et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22215) · [PDF](https://arxiv.org/pdf/2611.22215) |
| 2026-11-17 | **TempQuant: Learning Adaptive Temperatures for Quantized Language Models**<br><sub>Mukund Athmaram, Liang Ma, Manoj Rao</sub> | [arXiv](https://arxiv.org/abs/2611.22128) · [PDF](https://arxiv.org/pdf/2611.22128) |
| 2026-11-17 | **Computed Permutation Trellis Coding: Near-Optimal Quantization from Two Multiplications and a 64-Byte Table**<br><sub>Muhammed Fatih Balın</sub> | [arXiv](https://arxiv.org/abs/2611.22019) · [PDF](https://arxiv.org/pdf/2611.22019) |
| 2026-11-16 | **Beyond Bitwidth: Deployment-Constrained Mixed-Precision Quantization for Multilingual LLM Inference on NVIDIA Blackwell**<br><sub>Hyojung Han</sub> | [arXiv](https://arxiv.org/abs/2611.21974) · [PDF](https://arxiv.org/pdf/2611.21974) |
| 2026-11-16 | **Watermark Evidence under Open-Weight LLM Modification: Exact Bounds for Low-Rank Output Watermarks**<br><sub>Prashant Shekhar, Dumindu Samaraweera, Caroline Howard</sub> | [arXiv](https://arxiv.org/abs/2611.21702) · [PDF](https://arxiv.org/pdf/2611.21702) |
| 2026-11-16 | **MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression**<br><sub>Ofir Gordon, Lior Dikstein, Paul Balanca et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21216) · [PDF](https://arxiv.org/pdf/2611.21216) |
| 2026-11-16 | **JointQ: Joint Scale-and-Integer Quantization for Large Language Models**<br><sub>Keiji Kimura, Yuma Ichikawa</sub> | [arXiv](https://arxiv.org/abs/2611.20384) · [PDF](https://arxiv.org/pdf/2611.20384) · [Code](https://github.com/FujitsuResearch/OneCompression) |
| 2026-11-15 | **Offline-First Quantized AI: Design and Evaluation of an On-Device Maternal-Health Assistant for Low-Connectivity Environments**<br><sub>Okenla AbdulQahhar Abimbola, Maurice Abraham John, Adepoju Jeremiah Moyondafoluwa et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20012) · [PDF](https://arxiv.org/pdf/2611.20012) |
| 2026-11-13 | **NVFP4-MLA: Unified FP4 KV-Cache Storage and Attention Computation for Multi-Head Latent Attention**<br><sub>Chao Ni, Qi Zhang, Xiao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18972) · [PDF](https://arxiv.org/pdf/2611.18972) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **260 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **Transfer Once, Ask Locally: Compact Audio-Visual Memory for On-Device Question Answering**<br><sub>Qitong Wang, Jihui Jin, Divya Kothandaraman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23085) · [PDF](https://arxiv.org/pdf/2611.23085) |
| 2026-11-17 | **LoopPrune: Recurrent Pruning for Looped Diffusion Transformers**<br><sub>Weizhong Huang, Huaijia Kou, Yan Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22757) · [PDF](https://arxiv.org/pdf/2611.22757) |
| 2026-11-17 | **LoopZip: Visual Token Compression for Efficient Looped Vision-Language Models**<br><sub>Weizhong Huang, Zhicheng Liu, Yan Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22728) · [PDF](https://arxiv.org/pdf/2611.22728) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |
| 2026-11-17 | **The Fragility of Reasoning-Importance Attribution for Pruning Language Models**<br><sub>Himanshu Mishra</sub> | [arXiv](https://arxiv.org/abs/2611.22234) · [PDF](https://arxiv.org/pdf/2611.22234) |
| 2026-11-16 | **Representational Change Under Self-Consuming Training: A Sparse Autoencoder Analysis**<br><sub>Suchit Gupte, Zhongteng Cai, Xueru Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21348) · [PDF](https://arxiv.org/pdf/2611.21348) |
| 2026-11-16 | **Watermark Evidence under Open-Weight LLM Modification: Exact Bounds for Low-Rank Output Watermarks**<br><sub>Prashant Shekhar, Dumindu Samaraweera, Caroline Howard</sub> | [arXiv](https://arxiv.org/abs/2611.21702) · [PDF](https://arxiv.org/pdf/2611.21702) |
| 2026-11-16 | **QASK-Edit: Adaptive Sparse Attention Across Queries and Key Sources for Efficient Video Editing**<br><sub>Hengrui Liu, Wenbo Xu, Ziqi Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20704) · [PDF](https://arxiv.org/pdf/2611.20704) |
| 2026-11-16 | **RoShift: Lazy Shift and Weight-aware Rotation for Activation Sparsity in LLM Inference**<br><sub>Geunsoo Song, Jiwon Seo, Hoeseok Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20549) · [PDF](https://arxiv.org/pdf/2611.20549) · [Code](https://github.com/hulahula3247/RoShift) |
| 2026-11-16 | **How Reliable Is Visual Token Selection? Rethinking Pruning in Multimodal LLMs**<br><sub>Chaehee Song, Seokil Ham, KiHyun Seol et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20505) · [PDF](https://arxiv.org/pdf/2611.20505) |
| 2026-11-15 | **PoCoAttn: Position-Content Collaborative Sparse Attention for Fast and High-Fidelity Video Generation**<br><sub>Jianwen Wu, Meiling Wang, Junkang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20307) · [PDF](https://arxiv.org/pdf/2611.20307) |
| 2026-11-15 | **Glance, then Select: Evidence-Tempered Visual Token Selection for Extremely Compressed Multimodal LLMs**<br><sub>Yuxuan Wang, Guangxiang Zhao, Yuxuan Tian et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20006) · [PDF](https://arxiv.org/pdf/2611.20006) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **568 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching**<br><sub>Giannis Daras, Marios Papachristou, Adam Klivans et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23229) · [PDF](https://arxiv.org/pdf/2611.23229) |
| 2026-11-17 | **M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with Multi-Teacher On-Policy Distillation**<br><sub>Nguyen Quang Trung, Hoang Phan, Shuo Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23034) · [PDF](https://arxiv.org/pdf/2611.23034) |
| 2026-11-17 | **The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale**<br><sub>Fırat Öncel, Cem Subakan, Mirco Ravanelli et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22947) · [PDF](https://arxiv.org/pdf/2611.22947) · [Code](https://github.com/firatoncel/KernelRealityCheckNeurIPS2026) |
| 2026-11-17 | **SilverSpoon-KD: A General-Purpose Toolkit for Knowledge Distillation**<br><sub>Xaver R. Davey, David Broman</sub> | [arXiv](https://arxiv.org/abs/2611.22842) · [PDF](https://arxiv.org/pdf/2611.22842) · [Code](https://github.com/silverspoon-dev/silverspoon-kd) |
| 2026-11-16 | **KVUse: Reusable-KV User Memory for Efficient LLM Recommenders**<br><sub>Xin Guo, Qiang Zhang, Xiang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21920) · [PDF](https://arxiv.org/pdf/2611.21920) |
| 2026-11-16 | **The Limits of Closed-Form Couplings for Few-Step Generation**<br><sub>Tobias Höppe, Stefan Bauer, Qiang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21119) · [PDF](https://arxiv.org/pdf/2611.21119) |
| 2026-11-16 | **Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization**<br><sub>Jing Yi, Cehao Yang, Hualei Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21094) · [PDF](https://arxiv.org/pdf/2611.21094) |
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-16 | **An Efficient Training Paradigm for Image Restoration via Improved Fréchet Loss**<br><sub>Shanyuan Jie, Wu Shi, Xinqi Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20805) · [PDF](https://arxiv.org/pdf/2611.20805) |
| 2026-11-16 | **Fast at the Frontier, Wrong at the Fallback: A Commit-Level Analysis of Threshold Decoding in Diffusion Language Models**<br><sub>Roman Makarov, Zhe Xu, Jian Kang</sub> | [arXiv](https://arxiv.org/abs/2611.20693) · [PDF](https://arxiv.org/pdf/2611.20693) · [Code](https://github.com/rmakarovv/fast-at-the-frontier) |
| 2026-11-16 | **LEAF-OPD: Learning to Forget from Privileged Contexts via On-Policy Distillation**<br><sub>Zirui Pang, Zhijie Deng, Yuancheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20674) · [PDF](https://arxiv.org/pdf/2611.20674) |
| 2026-11-15 | **FastGRN: Few-Step Generative Refinement Networks**<br><sub>Haoyang Hu, Masataka Seo, Liang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20021) · [PDF](https://arxiv.org/pdf/2611.20021) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **200 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU**<br><sub>Mehmet Altan Toksöz</sub> | [arXiv](https://arxiv.org/abs/2611.23205) · [PDF](https://arxiv.org/pdf/2611.23205) |
| 2026-11-17 | **MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study**<br><sub>Nikit Srivastava, Joel Dag, René Speck et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23158) · [PDF](https://arxiv.org/pdf/2611.23158) |
| 2026-11-17 | **Efficient Self-Supervised Adaptation of 3D Abdominal Vision-Language Model for Institution-Specific HCC Classification via Full Fine-Tuning and PEFT**<br><sub>Febryan Putra Kartika, Cheng-Yu Ma, Ying-Jia Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22504) · [PDF](https://arxiv.org/pdf/2611.22504) |
| 2026-11-17 | **BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning**<br><sub>Juyoung Park, Heejun Lee</sub> | [arXiv](https://arxiv.org/abs/2611.22334) · [PDF](https://arxiv.org/pdf/2611.22334) |
| 2026-11-17 | **SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding**<br><sub>Selin Yildirim, Ali Zeyrek, Deming Chen</sub> | [arXiv](https://arxiv.org/abs/2611.22296) · [PDF](https://arxiv.org/pdf/2611.22296) |
| 2026-11-16 | **KVUse: Reusable-KV User Memory for Efficient LLM Recommenders**<br><sub>Xin Guo, Qiang Zhang, Xiang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21920) · [PDF](https://arxiv.org/pdf/2611.21920) |
| 2026-11-16 | **FaceRiff: Data-Efficient Unified Text-to-3D Face Asset Synthesis via Geometric Conditioning**<br><sub>Elly Akhoundi, Mathieu Lamarre, Thibault Goyallon et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21867) · [PDF](https://arxiv.org/pdf/2611.21867) |
| 2026-11-16 | **Watermark Evidence under Open-Weight LLM Modification: Exact Bounds for Low-Rank Output Watermarks**<br><sub>Prashant Shekhar, Dumindu Samaraweera, Caroline Howard</sub> | [arXiv](https://arxiv.org/abs/2611.21702) · [PDF](https://arxiv.org/pdf/2611.21702) |
| 2026-11-16 | **MORE: Merge Once, Route Early for Training-Free Multi-Subject Composition from Large LoRA Pools**<br><sub>Tian Xia</sub> | [arXiv](https://arxiv.org/abs/2611.21077) · [PDF](https://arxiv.org/pdf/2611.21077) |
| 2026-11-16 | **EDITORS Know Your Style! Editing LoRA Subspaces for Stylistic Attribution and Imitation**<br><sub>Zixuan Wang, Gregory Kang Ruey Lau, Xiao Tian et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20846) · [PDF](https://arxiv.org/pdf/2611.20846) |
| 2026-11-16 | **An Efficient Training Paradigm for Image Restoration via Improved Fréchet Loss**<br><sub>Shanyuan Jie, Wu Shi, Xinqi Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20805) · [PDF](https://arxiv.org/pdf/2611.20805) |
| 2026-11-15 | **Protecting Safety during Reasoning Training with Low-Rank Fisher Regularisation**<br><sub>Neel Rajani, Ivan Titov</sub> | [arXiv](https://arxiv.org/abs/2611.20288) · [PDF](https://arxiv.org/pdf/2611.20288) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **285 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **FastFrames: Video Generation at Interactive Latency**<br><sub>Gene Chou, Guandao Yang, Fujun Luan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) |
| 2026-11-17 | **The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale**<br><sub>Fırat Öncel, Cem Subakan, Mirco Ravanelli et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22947) · [PDF](https://arxiv.org/pdf/2611.22947) · [Code](https://github.com/firatoncel/KernelRealityCheckNeurIPS2026) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |
| 2026-11-17 | **XM-Sparse: High-Throughput Sparse-Attention LLM Serving over Scale-up Memory Pools**<br><sub>Yijun Sun, Xudong Liao, Zhuobin Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22280) · [PDF](https://arxiv.org/pdf/2611.22280) |
| 2026-11-17 | **From Token Changes to Task Failures: Bit Flips in a Shared KV-Cache Block**<br><sub>Yuji Yamamoto, Satoshi Matsuura</sub> | [arXiv](https://arxiv.org/abs/2611.22243) · [PDF](https://arxiv.org/pdf/2611.22243) |
| 2026-11-17 | **TAILROLL: Tail-Aware Rollout Acceleration for RL-Based LLM Post-Training**<br><sub>Niloofar Gholipour, Marcos Assuncao, Timothy Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22206) · [PDF](https://arxiv.org/pdf/2611.22206) |
| 2026-11-17 | **RISA: Recoverable Sparse Attention for Block-Diffusion Language Models**<br><sub>Xinrui Zhong, Fanjiang Ye, Yuke Wang</sub> | [arXiv](https://arxiv.org/abs/2611.22191) · [PDF](https://arxiv.org/pdf/2611.22191) |
| 2026-11-16 | **KVUse: Reusable-KV User Memory for Efficient LLM Recommenders**<br><sub>Xin Guo, Qiang Zhang, Xiang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21920) · [PDF](https://arxiv.org/pdf/2611.21920) |
| 2026-11-16 | **SURMA: Efficient Fine-Grained Communication Offload for SuperPOD**<br><sub>Haoran Shang, Weifeng Zhang, Mengzhu Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21274) · [PDF](https://arxiv.org/pdf/2611.21274) |
| 2026-11-16 | **MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression**<br><sub>Ofir Gordon, Lior Dikstein, Paul Balanca et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21216) · [PDF](https://arxiv.org/pdf/2611.21216) |
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-16 | **Sparse Attention for Visual Generation: Toward Algorithm-System Co-Design**<br><sub>Majun Zhang, Yuan Guo, Decheng Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21029) · [PDF](https://arxiv.org/pdf/2611.21029) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **179 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding**<br><sub>Selin Yildirim, Ali Zeyrek, Deming Chen</sub> | [arXiv](https://arxiv.org/abs/2611.22296) · [PDF](https://arxiv.org/pdf/2611.22296) |
| 2026-11-16 | **VisHead-Spec: Head-Routed Visual Attention for Multimodal Speculative Decoding**<br><sub>Xin Guo, Arushi Rai, Xiang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21839) · [PDF](https://arxiv.org/pdf/2611.21839) |
| 2026-11-16 | **Sketch, Don&#x27;t Paint: Allocating Test-Time Compute in Generative Visual Reasoning**<br><sub>Sheng Lu, Guangpin Tao, Tong Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21812) · [PDF](https://arxiv.org/pdf/2611.21812) |
| 2026-11-16 | **Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents**<br><sub>NVIDIA, :, Adi Margolin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20771) · [PDF](https://arxiv.org/pdf/2611.20771) |
| 2026-11-16 | **ToolGraph as a Q-Function for Test-Time Scaling of Tool-Use Agents**<br><sub>Ke Shen, Ankita Bhaumik, Li Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20569) · [PDF](https://arxiv.org/pdf/2611.20569) |
| 2026-11-15 | **PlanDiv: Test-Time Scaling with Latent Plans for Vision-Language-Action Models**<br><sub>Hanbo Zhang, Lianlei Shan, Liuhaichen Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20010) · [PDF](https://arxiv.org/pdf/2611.20010) |
| 2026-11-15 | **LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models**<br><sub>Muhan Xiao, Shijian Li</sub> | [arXiv](https://arxiv.org/abs/2611.19896) · [PDF](https://arxiv.org/pdf/2611.19896) |
| 2026-11-14 | **LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers**<br><sub>Siqi Zhu, Suozhi Huang, Yi Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19649) · [PDF](https://arxiv.org/pdf/2611.19649) |
| 2026-11-13 | **SpecRelay: Amortize or Avoid the Round Trip in Edge-Cloud Speculative Decoding**<br><sub>Jai Jain, Chihyo Ahn, Yong Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18963) · [PDF](https://arxiv.org/pdf/2611.18963) |
| 2026-11-13 | **Exstill: The Most Efficient Single-Chip Processor for the Next Token**<br><sub>Valavan Manohararajah, Vithursan Thangarasa</sub> | [arXiv](https://arxiv.org/abs/2611.18859) · [PDF](https://arxiv.org/pdf/2611.18859) |
| 2026-11-13 | **MMFlash: Faster Speculative Decoding for Vision-Language Models**<br><sub>Sicheng Feng, Zigeng Chen, Song Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18482) · [PDF](https://arxiv.org/pdf/2611.18482) |
| 2026-11-13 | **More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs**<br><sub>Seyed Mahmoud Sajjadi Mohammadabadi</sub> | [arXiv](https://arxiv.org/abs/2611.17610) · [PDF](https://arxiv.org/pdf/2611.17610) · [Code](https://github.com/mahmoudsajjadi/pace) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **313 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models**<br><sub>Rui Ning, Om Chabra, Hari Balakrishnan</sub> | [arXiv](https://arxiv.org/abs/2611.23228) · [PDF](https://arxiv.org/pdf/2611.23228) |
| 2026-11-17 | **Transfer Once, Ask Locally: Compact Audio-Visual Memory for On-Device Question Answering**<br><sub>Qitong Wang, Jihui Jin, Divya Kothandaraman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23085) · [PDF](https://arxiv.org/pdf/2611.23085) |
| 2026-11-17 | **LoopZip: Visual Token Compression for Efficient Looped Vision-Language Models**<br><sub>Weizhong Huang, Zhicheng Liu, Yan Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22728) · [PDF](https://arxiv.org/pdf/2611.22728) |
| 2026-11-17 | **Semantic-Guided Geometric Decoding for Token-Efficient Visual Grounding**<br><sub>Zhaojie Chen, Junyan Yang, Le Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22577) · [PDF](https://arxiv.org/pdf/2611.22577) |
| 2026-11-17 | **BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning**<br><sub>Juyoung Park, Heejun Lee</sub> | [arXiv](https://arxiv.org/abs/2611.22334) · [PDF](https://arxiv.org/pdf/2611.22334) |
| 2026-11-17 | **SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding**<br><sub>Selin Yildirim, Ali Zeyrek, Deming Chen</sub> | [arXiv](https://arxiv.org/abs/2611.22296) · [PDF](https://arxiv.org/pdf/2611.22296) |
| 2026-11-17 | **XM-Sparse: High-Throughput Sparse-Attention LLM Serving over Scale-up Memory Pools**<br><sub>Yijun Sun, Xudong Liao, Zhuobin Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22280) · [PDF](https://arxiv.org/pdf/2611.22280) |
| 2026-11-17 | **From Token Changes to Task Failures: Bit Flips in a Shared KV-Cache Block**<br><sub>Yuji Yamamoto, Satoshi Matsuura</sub> | [arXiv](https://arxiv.org/abs/2611.22243) · [PDF](https://arxiv.org/pdf/2611.22243) |
| 2026-11-17 | **Communicate the Change: Efficient Expert Parallelism via Activation Compression**<br><sub>Fengyuan Liu, Jay Gala, Siva Reddy et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22215) · [PDF](https://arxiv.org/pdf/2611.22215) |
| 2026-11-16 | **KVUse: Reusable-KV User Memory for Efficient LLM Recommenders**<br><sub>Xin Guo, Qiang Zhang, Xiang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21920) · [PDF](https://arxiv.org/pdf/2611.21920) |
| 2026-11-16 | **SURMA: Efficient Fine-Grained Communication Offload for SuperPOD**<br><sub>Haoran Shang, Weifeng Zhang, Mengzhu Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21274) · [PDF](https://arxiv.org/pdf/2611.21274) |
| 2026-11-16 | **A Matter of Stages: Energy-Latency Trade-offs in Multimodal LLM Serving**<br><sub>Yifan Sun, Jiantong Jiang, Zhexiang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21165) · [PDF](https://arxiv.org/pdf/2611.21165) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **143 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **FastFrames: Video Generation at Interactive Latency**<br><sub>Gene Chou, Guandao Yang, Fujun Luan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |
| 2026-11-17 | **RISA: Recoverable Sparse Attention for Block-Diffusion Language Models**<br><sub>Xinrui Zhong, Fanjiang Ye, Yuke Wang</sub> | [arXiv](https://arxiv.org/abs/2611.22191) · [PDF](https://arxiv.org/pdf/2611.22191) |
| 2026-11-17 | **BATMoS: Budget-Aware Guidance Allocation for Efficient Video Diffusion**<br><sub>Zhixu Du, Kuo Yang, Jingwei Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22028) · [PDF](https://arxiv.org/pdf/2611.22028) |
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-15 | **TileCache: Serving Multi-Round Diffusion Image Editing with Compressed Activation Caches**<br><sub>Yuyang Tian, Desen Sun, Shuncheng Jie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20246) · [PDF](https://arxiv.org/pdf/2611.20246) |
| 2026-11-15 | **Cache or Denoise Less? Residual Reuse in a Flow-Matching World Action Model**<br><sub>Abhinav Gupta, Nissan Pow</sub> | [arXiv](https://arxiv.org/abs/2611.19709) · [PDF](https://arxiv.org/pdf/2611.19709) · [Code](https://github.com/gabhinav001/cache-or-denoise-less) |
| 2026-11-13 | **D2ToF: One-Step Diffusion for Depth Super-Resolution from Lightweight Single-Photon LiDAR Waveforms**<br><sub>Pallabjyoti Deka, Lewis Wilson, Stephen McLaughlin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18243) · [PDF](https://arxiv.org/pdf/2611.18243) |
| 2026-11-12 | **DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models**<br><sub>Yi-Hsin Hung, Fangfu Liu, Shao-Yuan Lo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16345) · [PDF](https://arxiv.org/pdf/2611.16345) |
| 2026-11-10 | **Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models**<br><sub>Amir Mann, Jonathan Fhima, Shaked Brody et al.</sub> | [arXiv](https://arxiv.org/abs/2611.14387) · [PDF](https://arxiv.org/pdf/2611.14387) |
| 2026-11-10 | **AdjointFlow: Accelerating Scientific Inverse Problems with Physics-Based Transport**<br><sub>Ethan Hanold, Nicholas M. Boffi, Qin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13389) · [PDF](https://arxiv.org/pdf/2611.13389) |
| 2026-11-09 | **DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees**<br><sub>Zhicheng Zheng, Cheng Zhang, Chenkai Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12356) · [PDF](https://arxiv.org/pdf/2611.12356) · [Code](https://github.com/Perseus037/DForkTree) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **247 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-17 | **FastFrames: Video Generation at Interactive Latency**<br><sub>Gene Chou, Guandao Yang, Fujun Luan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) |
| 2026-11-17 | **TextSphere: Efficient Text-to-Image Generation via Shared Hyperspherical Alignment and Uniformity**<br><sub>Yixia Zhang, Girish A. Koushik, Xilu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23155) · [PDF](https://arxiv.org/pdf/2611.23155) |
| 2026-11-17 | **Code World Model 2.0: Towards Infinite Controllable Video Generation**<br><sub>Ruoyu Wang, Hao Zhong, Yanming Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22925) · [PDF](https://arxiv.org/pdf/2611.22925) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |
| 2026-11-17 | **Fast and Strong Image Protection against Diffusion Personalization**<br><sub>Jiwon Park, Jihye Kang, Namhyuk Ahn</sub> | [arXiv](https://arxiv.org/abs/2611.22494) · [PDF](https://arxiv.org/pdf/2611.22494) |
| 2026-11-17 | **BATMoS: Budget-Aware Guidance Allocation for Efficient Video Diffusion**<br><sub>Zhixu Du, Kuo Yang, Jingwei Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22028) · [PDF](https://arxiv.org/pdf/2611.22028) |
| 2026-11-16 | **AR-WAM: efficient streaming world-action modeling for autonomous driving**<br><sub>Baiting Luo, Shatadal Mishra, Ahmadreza Moradipari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21851) · [PDF](https://arxiv.org/pdf/2611.21851) |
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-16 | **Sparse Attention for Visual Generation: Toward Algorithm-System Co-Design**<br><sub>Majun Zhang, Yuan Guo, Decheng Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21029) · [PDF](https://arxiv.org/pdf/2611.21029) |
| 2026-11-16 | **QASK-Edit: Adaptive Sparse Attention Across Queries and Key Sources for Efficient Video Editing**<br><sub>Hengrui Liu, Wenbo Xu, Ziqi Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20704) · [PDF](https://arxiv.org/pdf/2611.20704) |
| 2026-11-16 | **Counterfactual Feature Steering for Adjacency-Preserving Identity Unlearning**<br><sub>FNU Shivam, Layth Sliman, Ramana Reddy et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20637) · [PDF](https://arxiv.org/pdf/2611.20637) |
| 2026-11-15 | **PoCoAttn: Position-Content Collaborative Sparse Attention for Fast and High-Fidelity Video Generation**<br><sub>Jianwen Wu, Meiling Wang, Junkang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20307) · [PDF](https://arxiv.org/pdf/2611.20307) |

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
