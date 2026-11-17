# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-17 17:15 CST** · **1791 unique papers** · Newest submission: **2026-11-16**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 283 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 254 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 563 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 192 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 277 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 176 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 303 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 139 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 240 |

## Newly indexed · 2026-11-17

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **Representational Change Under Self-Consuming Training: A Sparse Autoencoder Analysis**<br><sub>Suchit Gupte, Zhongteng Cai, Xueru Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21348) · [PDF](https://arxiv.org/pdf/2611.21348) |
| 2026-11-16 | **SURMA: Efficient Fine-Grained Communication Offload for SuperPOD**<br><sub>Haoran Shang, Weifeng Zhang, Mengzhu Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21274) · [PDF](https://arxiv.org/pdf/2611.21274) |
| 2026-11-16 | **MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression**<br><sub>Ofir Gordon, Lior Dikstein, Paul Balanca et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21216) · [PDF](https://arxiv.org/pdf/2611.21216) |
| 2026-11-16 | **A Matter of Stages: Energy-Latency Trade-offs in Multimodal LLM Serving**<br><sub>Yifan Sun, Jiantong Jiang, Zhexiang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21165) · [PDF](https://arxiv.org/pdf/2611.21165) |
| 2026-11-16 | **The Limits of Closed-Form Couplings for Few-Step Generation**<br><sub>Tobias Höppe, Stefan Bauer, Qiang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21119) · [PDF](https://arxiv.org/pdf/2611.21119) |
| 2026-11-16 | **Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization**<br><sub>Jing Yi, Cehao Yang, Hualei Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21094) · [PDF](https://arxiv.org/pdf/2611.21094) |
| 2026-11-16 | **MORE: Merge Once, Route Early for Training-Free Multi-Subject Composition from Large LoRA Pools**<br><sub>Tian Xia</sub> | [arXiv](https://arxiv.org/abs/2611.21077) · [PDF](https://arxiv.org/pdf/2611.21077) |
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-16 | **Sparse Attention for Visual Generation: Toward Algorithm-System Co-Design**<br><sub>Majun Zhang, Yuan Guo, Decheng Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21029) · [PDF](https://arxiv.org/pdf/2611.21029) |
| 2026-11-16 | **EDITORS Know Your Style! Editing LoRA Subspaces for Stylistic Attribution and Imitation**<br><sub>Zixuan Wang, Gregory Kang Ruey Lau, Xiao Tian et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20846) · [PDF](https://arxiv.org/pdf/2611.20846) |
| 2026-11-16 | **An Efficient Training Paradigm for Image Restoration via Improved Fréchet Loss**<br><sub>Shanyuan Jie, Wu Shi, Xinqi Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20805) · [PDF](https://arxiv.org/pdf/2611.20805) |
| 2026-11-16 | **Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents**<br><sub>NVIDIA, :, Adi Margolin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20771) · [PDF](https://arxiv.org/pdf/2611.20771) |
| 2026-11-16 | **Instant Weight-Space Consolidation for Long-Term Memory in LLMs**<br><sub>Manan Suri, Dinesh Manocha</sub> | [arXiv](https://arxiv.org/abs/2611.20759) · [PDF](https://arxiv.org/pdf/2611.20759) |
| 2026-11-16 | **QASK-Edit: Adaptive Sparse Attention Across Queries and Key Sources for Efficient Video Editing**<br><sub>Hengrui Liu, Wenbo Xu, Ziqi Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20704) · [PDF](https://arxiv.org/pdf/2611.20704) |
| 2026-11-16 | **Fast at the Frontier, Wrong at the Fallback: A Commit-Level Analysis of Threshold Decoding in Diffusion Language Models**<br><sub>Roman Makarov, Zhe Xu, Jian Kang</sub> | [arXiv](https://arxiv.org/abs/2611.20693) · [PDF](https://arxiv.org/pdf/2611.20693) · [Code](https://github.com/rmakarovv/fast-at-the-frontier) |
| 2026-11-16 | **LEAF-OPD: Learning to Forget from Privileged Contexts via On-Policy Distillation**<br><sub>Zirui Pang, Zhijie Deng, Yuancheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20674) · [PDF](https://arxiv.org/pdf/2611.20674) |
| 2026-11-16 | **Counterfactual Feature Steering for Adjacency-Preserving Identity Unlearning**<br><sub>FNU Shivam, Layth Sliman, Ramana Reddy et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20637) · [PDF](https://arxiv.org/pdf/2611.20637) |
| 2026-11-16 | **ToolGraph as a Q-Function for Test-Time Scaling of Tool-Use Agents**<br><sub>Ke Shen, Ankita Bhaumik, Li Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20569) · [PDF](https://arxiv.org/pdf/2611.20569) |
| 2026-11-16 | **RoShift: Lazy Shift and Weight-aware Rotation for Activation Sparsity in LLM Inference**<br><sub>Geunsoo Song, Jiwon Seo, Hoeseok Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20549) · [PDF](https://arxiv.org/pdf/2611.20549) · [Code](https://github.com/hulahula3247/RoShift) |
| 2026-11-16 | **How Reliable Is Visual Token Selection? Rethinking Pruning in Multimodal LLMs**<br><sub>Chaehee Song, Seokil Ham, KiHyun Seol et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20505) · [PDF](https://arxiv.org/pdf/2611.20505) |

[View all 56 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **283 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression**<br><sub>Ofir Gordon, Lior Dikstein, Paul Balanca et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21216) · [PDF](https://arxiv.org/pdf/2611.21216) |
| 2026-11-16 | **JointQ: Joint Scale-and-Integer Quantization for Large Language Models**<br><sub>Keiji Kimura, Yuma Ichikawa</sub> | [arXiv](https://arxiv.org/abs/2611.20384) · [PDF](https://arxiv.org/pdf/2611.20384) · [Code](https://github.com/FujitsuResearch/OneCompression) |
| 2026-11-15 | **Offline-First Quantized AI: Design and Evaluation of an On-Device Maternal-Health Assistant for Low-Connectivity Environments**<br><sub>Okenla AbdulQahhar Abimbola, Maurice Abraham John, Adepoju Jeremiah Moyondafoluwa et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20012) · [PDF](https://arxiv.org/pdf/2611.20012) |
| 2026-11-13 | **NVFP4-MLA: Unified FP4 KV-Cache Storage and Attention Computation for Multi-Head Latent Attention**<br><sub>Chao Ni, Qi Zhang, Xiao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18972) · [PDF](https://arxiv.org/pdf/2611.18972) |
| 2026-11-13 | **CHARMING: Parallel Edge AI Acceleration Across Tensor Processing and In-Memory Computation**<br><sub>Md Omar Faruque, Jingang Jin, João Paulo C. de Lima et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17785) · [PDF](https://arxiv.org/pdf/2611.17785) |
| 2026-11-13 | **Choosing Quantized Code LLMs by File Size and Energy per Solved Task**<br><sub>Aditi Patodiya</sub> | [arXiv](https://arxiv.org/abs/2611.17605) · [PDF](https://arxiv.org/pdf/2611.17605) |
| 2026-11-12 | **User-Schedulable Approximations for Quantized Tensor Programs**<br><sub>Alex Reinking</sub> | [arXiv](https://arxiv.org/abs/2611.17526) · [PDF](https://arxiv.org/pdf/2611.17526) |
| 2026-11-12 | **Advancing Quantization for R&amp;R Models with Microscaling Formats**<br><sub>Yavuz Yetim, Bor-Yiing Su, Zhe Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17501) · [PDF](https://arxiv.org/pdf/2611.17501) |
| 2026-11-12 | **Lara Mini Base: Language Diversity as a Resource, Not a Trade-off**<br><sub>Translated, Maria Pia Adinolfi, Isabelle Andrieu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16956) · [PDF](https://arxiv.org/pdf/2611.16956) · [Code](https://huggingface.co/translated/Lara-4-Mini-Base) |
| 2026-11-12 | **STEALTH: Steganographic Text Encoding Agnostic to Low-Level Tensor Hardware**<br><sub>William Fleshman</sub> | [arXiv](https://arxiv.org/abs/2611.16928) · [PDF](https://arxiv.org/pdf/2611.16928) |
| 2026-11-12 | **SignRot: LLM Quantization with Massive Outlier-Aware Sign-Adjusted Rotation**<br><sub>Jaehun Gim, Jaewoo Kim, Gyuwan Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16502) · [PDF](https://arxiv.org/pdf/2611.16502) · [Code](https://github.com/HYU-ARK-Lab/SignRot) |
| 2026-11-12 | **One Model, Two Precisions: Does Disagreement Between Quantized Copies Tell You When a Small Model Is Wrong?**<br><sub>Mohammed Nayeem Khan, Allan Kevin T</sub> | [arXiv](https://arxiv.org/abs/2611.16478) · [PDF](https://arxiv.org/pdf/2611.16478) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **254 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **Representational Change Under Self-Consuming Training: A Sparse Autoencoder Analysis**<br><sub>Suchit Gupte, Zhongteng Cai, Xueru Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21348) · [PDF](https://arxiv.org/pdf/2611.21348) |
| 2026-11-16 | **QASK-Edit: Adaptive Sparse Attention Across Queries and Key Sources for Efficient Video Editing**<br><sub>Hengrui Liu, Wenbo Xu, Ziqi Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20704) · [PDF](https://arxiv.org/pdf/2611.20704) |
| 2026-11-16 | **RoShift: Lazy Shift and Weight-aware Rotation for Activation Sparsity in LLM Inference**<br><sub>Geunsoo Song, Jiwon Seo, Hoeseok Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20549) · [PDF](https://arxiv.org/pdf/2611.20549) · [Code](https://github.com/hulahula3247/RoShift) |
| 2026-11-16 | **How Reliable Is Visual Token Selection? Rethinking Pruning in Multimodal LLMs**<br><sub>Chaehee Song, Seokil Ham, KiHyun Seol et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20505) · [PDF](https://arxiv.org/pdf/2611.20505) |
| 2026-11-15 | **PoCoAttn: Position-Content Collaborative Sparse Attention for Fast and High-Fidelity Video Generation**<br><sub>Jianwen Wu, Meiling Wang, Junkang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20307) · [PDF](https://arxiv.org/pdf/2611.20307) |
| 2026-11-15 | **Glance, then Select: Evidence-Tempered Visual Token Selection for Extremely Compressed Multimodal LLMs**<br><sub>Yuxuan Wang, Guangxiang Zhao, Yuxuan Tian et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20006) · [PDF](https://arxiv.org/pdf/2611.20006) |
| 2026-11-15 | **Interactive Structured Environment Scaling for Large Language Model Agentic Reasoning**<br><sub>Peng Yu, Luoyi Fu, Xinbing Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19871) · [PDF](https://arxiv.org/pdf/2611.19871) |
| 2026-11-15 | **EfficientSkill: Learning Skills for Token-Efficient Multi-Turn Agents**<br><sub>Deep Shah, Sanket Badhe, Nehal Kathrotia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19823) · [PDF](https://arxiv.org/pdf/2611.19823) |
| 2026-11-14 | **SMELL: Sparsity-aware Memory Efficient Federated Fine-tuning for Long-context LLMs**<br><sub>Yin Xu, Yongbo Yang, He Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19349) · [PDF](https://arxiv.org/pdf/2611.19349) |
| 2026-11-14 | **dit.xpu : Taming DiT Sparse Inference on Mobile SoCs**<br><sub>Jiayu Chen, Jinye Hu, Maoliang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19261) · [PDF](https://arxiv.org/pdf/2611.19261) · [Code](https://github.com/IF-LAB-PKU/dit.xpu) |
| 2026-11-13 | **Token2Tile: Token-Wise Sparse Attention with Tile Execution through a Low-Rank Space for Video DiTs**<br><sub>Xuecheng Wu, Aichen Feng, Jinyan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17930) · [PDF](https://arxiv.org/pdf/2611.17930) |
| 2026-11-12 | **DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models**<br><sub>Yi-Hsin Hung, Fangfu Liu, Shao-Yuan Lo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16345) · [PDF](https://arxiv.org/pdf/2611.16345) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **563 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **The Limits of Closed-Form Couplings for Few-Step Generation**<br><sub>Tobias Höppe, Stefan Bauer, Qiang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21119) · [PDF](https://arxiv.org/pdf/2611.21119) |
| 2026-11-16 | **Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization**<br><sub>Jing Yi, Cehao Yang, Hualei Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21094) · [PDF](https://arxiv.org/pdf/2611.21094) |
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-16 | **An Efficient Training Paradigm for Image Restoration via Improved Fréchet Loss**<br><sub>Shanyuan Jie, Wu Shi, Xinqi Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20805) · [PDF](https://arxiv.org/pdf/2611.20805) |
| 2026-11-16 | **Fast at the Frontier, Wrong at the Fallback: A Commit-Level Analysis of Threshold Decoding in Diffusion Language Models**<br><sub>Roman Makarov, Zhe Xu, Jian Kang</sub> | [arXiv](https://arxiv.org/abs/2611.20693) · [PDF](https://arxiv.org/pdf/2611.20693) · [Code](https://github.com/rmakarovv/fast-at-the-frontier) |
| 2026-11-16 | **LEAF-OPD: Learning to Forget from Privileged Contexts via On-Policy Distillation**<br><sub>Zirui Pang, Zhijie Deng, Yuancheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20674) · [PDF](https://arxiv.org/pdf/2611.20674) |
| 2026-11-15 | **FastGRN: Few-Step Generative Refinement Networks**<br><sub>Haoyang Hu, Masataka Seo, Liang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20021) · [PDF](https://arxiv.org/pdf/2611.20021) |
| 2026-11-15 | **Glance, then Select: Evidence-Tempered Visual Token Selection for Extremely Compressed Multimodal LLMs**<br><sub>Yuxuan Wang, Guangxiang Zhao, Yuxuan Tian et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20006) · [PDF](https://arxiv.org/pdf/2611.20006) |
| 2026-11-14 | **Program Distillation: Transferring LLM Capability from System 2 to System 0**<br><sub>Pujun Zheng, Wanying Ren, Guoxiu He</sub> | [arXiv](https://arxiv.org/abs/2611.19461) · [PDF](https://arxiv.org/pdf/2611.19461) |
| 2026-11-14 | **Do Pretraining Optimizer Gains Transfer to KL Distillation?**<br><sub>Lavinia Ghita, Dhruv Desai</sub> | [arXiv](https://arxiv.org/abs/2611.19419) · [PDF](https://arxiv.org/pdf/2611.19419) |
| 2026-11-14 | **Staged Semantic Distillation: Preserving Free-Form Semantics in a Low-Compute Non-LLM Surrogate of a Staged LLM Agent**<br><sub>Zhiyang Niu, Huayuan Shen, Chuanjie Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19299) · [PDF](https://arxiv.org/pdf/2611.19299) |
| 2026-11-14 | **Agentic On-Policy Distillation Implicitly Reshapes LLMs&#x27; ReAct Patterns**<br><sub>Deyang Kong, Zhaoyi Li, Sijian Ren et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19244) · [PDF](https://arxiv.org/pdf/2611.19244) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **192 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **MORE: Merge Once, Route Early for Training-Free Multi-Subject Composition from Large LoRA Pools**<br><sub>Tian Xia</sub> | [arXiv](https://arxiv.org/abs/2611.21077) · [PDF](https://arxiv.org/pdf/2611.21077) |
| 2026-11-16 | **EDITORS Know Your Style! Editing LoRA Subspaces for Stylistic Attribution and Imitation**<br><sub>Zixuan Wang, Gregory Kang Ruey Lau, Xiao Tian et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20846) · [PDF](https://arxiv.org/pdf/2611.20846) |
| 2026-11-16 | **An Efficient Training Paradigm for Image Restoration via Improved Fréchet Loss**<br><sub>Shanyuan Jie, Wu Shi, Xinqi Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20805) · [PDF](https://arxiv.org/pdf/2611.20805) |
| 2026-11-15 | **Protecting Safety during Reasoning Training with Low-Rank Fisher Regularisation**<br><sub>Neel Rajani, Ivan Titov</sub> | [arXiv](https://arxiv.org/abs/2611.20288) · [PDF](https://arxiv.org/pdf/2611.20288) |
| 2026-11-14 | **SMELL: Sparsity-aware Memory Efficient Federated Fine-tuning for Long-context LLMs**<br><sub>Yin Xu, Yongbo Yang, He Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19349) · [PDF](https://arxiv.org/pdf/2611.19349) |
| 2026-11-14 | **Can an Agent Rethink What It Knows? Selective Scene Memory Updates in a Changing World**<br><sub>Zhekai Ren, Jiaming Wu</sub> | [arXiv](https://arxiv.org/abs/2611.19227) · [PDF](https://arxiv.org/pdf/2611.19227) |
| 2026-11-14 | **Incremental Learning of Vision-Language Models via Task Subspace Projection and Dynamic LoRA**<br><sub>Hao Fu, Qian Feng, Hanbin Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19213) · [PDF](https://arxiv.org/pdf/2611.19213) · [Code](https://github.com/FerdinandZJU/TSP-DLoRA) |
| 2026-11-14 | **MarineSparkLM-4B: A Lightweight Language Model for Marine and Offshore Engineering Built by Parameter-Efficient Adaptation**<br><sub>Cheng Siong Chin</sub> | [arXiv](https://arxiv.org/abs/2611.19151) · [PDF](https://arxiv.org/pdf/2611.19151) |
| 2026-11-13 | **CARET: Clinical Assertion-Aware Residual Calibration for Medical Image-Text Alignment**<br><sub>Yifan Jin, Tao Liu</sub> | [arXiv](https://arxiv.org/abs/2611.18811) · [PDF](https://arxiv.org/pdf/2611.18811) |
| 2026-11-12 | **Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models**<br><sub>Tanzeel Abbas, Ahmad Kamran Malik, Nafees Qamar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17128) · [PDF](https://arxiv.org/pdf/2611.17128) |
| 2026-11-12 | **Predicting Ethanol Drinking Status from Nonhuman Primate Liver Histology: A Proof of Concept for Parameter-efficient Fine-tuning in Few-Shot Vision-Language Modeling**<br><sub>Amirmohammad Mohammadi, Rupak Khadka, Kathleen A. Grant et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17105) · [PDF](https://arxiv.org/pdf/2611.17105) · [Code](https://github.com/Advanced-Vision-and-Learning-Lab/ALD_VLM) |
| 2026-11-12 | **Factored One-sided Adam-Moment for Practical and Scalable SOAP**<br><sub>Jaemyung Yu, Byeongho Heo, Sangdoo Yun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16905) · [PDF](https://arxiv.org/pdf/2611.16905) · [Code](https://github.com/naver-ai/foam) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **277 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **SURMA: Efficient Fine-Grained Communication Offload for SuperPOD**<br><sub>Haoran Shang, Weifeng Zhang, Mengzhu Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21274) · [PDF](https://arxiv.org/pdf/2611.21274) |
| 2026-11-16 | **MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression**<br><sub>Ofir Gordon, Lior Dikstein, Paul Balanca et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21216) · [PDF](https://arxiv.org/pdf/2611.21216) |
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-16 | **Sparse Attention for Visual Generation: Toward Algorithm-System Co-Design**<br><sub>Majun Zhang, Yuan Guo, Decheng Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21029) · [PDF](https://arxiv.org/pdf/2611.21029) |
| 2026-11-16 | **QASK-Edit: Adaptive Sparse Attention Across Queries and Key Sources for Efficient Video Editing**<br><sub>Hengrui Liu, Wenbo Xu, Ziqi Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20704) · [PDF](https://arxiv.org/pdf/2611.20704) |
| 2026-11-15 | **PoCoAttn: Position-Content Collaborative Sparse Attention for Fast and High-Fidelity Video Generation**<br><sub>Jianwen Wu, Meiling Wang, Junkang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20307) · [PDF](https://arxiv.org/pdf/2611.20307) |
| 2026-11-15 | **Multi-Branch Transformer**<br><sub>Gaotang Li, Lingjie Chen, Chunyuan Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19800) · [PDF](https://arxiv.org/pdf/2611.19800) |
| 2026-11-14 | **Rethinking KV Caching for LLM Decode: Free-Space Optical KV Regeneration for Reduction of Memory Traffic**<br><sub>Aritra Bagchi, Bin Gao, James Spall et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19279) · [PDF](https://arxiv.org/pdf/2611.19279) |
| 2026-11-14 | **dit.xpu : Taming DiT Sparse Inference on Mobile SoCs**<br><sub>Jiayu Chen, Jinye Hu, Maoliang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19261) · [PDF](https://arxiv.org/pdf/2611.19261) · [Code](https://github.com/IF-LAB-PKU/dit.xpu) |
| 2026-11-13 | **Bilateral Log-Linear Attention**<br><sub>Kazi Ashik Islam, Guojing Cong</sub> | [arXiv](https://arxiv.org/abs/2611.18974) · [PDF](https://arxiv.org/pdf/2611.18974) |
| 2026-11-13 | **NVFP4-MLA: Unified FP4 KV-Cache Storage and Attention Computation for Multi-Head Latent Attention**<br><sub>Chao Ni, Qi Zhang, Xiao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18972) · [PDF](https://arxiv.org/pdf/2611.18972) |
| 2026-11-13 | **Exstill: The Most Efficient Single-Chip Processor for the Next Token**<br><sub>Valavan Manohararajah, Vithursan Thangarasa</sub> | [arXiv](https://arxiv.org/abs/2611.18859) · [PDF](https://arxiv.org/pdf/2611.18859) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **176 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents**<br><sub>NVIDIA, :, Adi Margolin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20771) · [PDF](https://arxiv.org/pdf/2611.20771) |
| 2026-11-16 | **ToolGraph as a Q-Function for Test-Time Scaling of Tool-Use Agents**<br><sub>Ke Shen, Ankita Bhaumik, Li Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20569) · [PDF](https://arxiv.org/pdf/2611.20569) |
| 2026-11-15 | **PlanDiv: Test-Time Scaling with Latent Plans for Vision-Language-Action Models**<br><sub>Hanbo Zhang, Lianlei Shan, Liuhaichen Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20010) · [PDF](https://arxiv.org/pdf/2611.20010) |
| 2026-11-15 | **LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models**<br><sub>Muhan Xiao, Shijian Li</sub> | [arXiv](https://arxiv.org/abs/2611.19896) · [PDF](https://arxiv.org/pdf/2611.19896) |
| 2026-11-14 | **LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers**<br><sub>Siqi Zhu, Suozhi Huang, Yi Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19649) · [PDF](https://arxiv.org/pdf/2611.19649) |
| 2026-11-13 | **SpecRelay: Amortize or Avoid the Round Trip in Edge-Cloud Speculative Decoding**<br><sub>Jai Jain, Chihyo Ahn, Yong Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18963) · [PDF](https://arxiv.org/pdf/2611.18963) |
| 2026-11-13 | **Exstill: The Most Efficient Single-Chip Processor for the Next Token**<br><sub>Valavan Manohararajah, Vithursan Thangarasa</sub> | [arXiv](https://arxiv.org/abs/2611.18859) · [PDF](https://arxiv.org/pdf/2611.18859) |
| 2026-11-13 | **MMFlash: Faster Speculative Decoding for Vision-Language Models**<br><sub>Sicheng Feng, Zigeng Chen, Song Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18482) · [PDF](https://arxiv.org/pdf/2611.18482) |
| 2026-11-13 | **More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs**<br><sub>Seyed Mahmoud Sajjadi Mohammadabadi</sub> | [arXiv](https://arxiv.org/abs/2611.17610) · [PDF](https://arxiv.org/pdf/2611.17610) · [Code](https://github.com/mahmoudsajjadi/pace) |
| 2026-11-12 | **Towards Green Text Generation: Memory-Based Speculative Decoding**<br><sub>Antal van den Bosch</sub> | [arXiv](https://arxiv.org/abs/2611.16714) · [PDF](https://arxiv.org/pdf/2611.16714) · [Code](https://github.com/antalvdb/olifant-speculative) |
| 2026-11-11 | **Early Signals, Strong Decisions: Prefix-Guided Sampling for Parallel Test-Time Scaling**<br><sub>Jie Ren, Jonathan Rosenfeld, Neil Thompson</sub> | [arXiv](https://arxiv.org/abs/2611.14965) · [PDF](https://arxiv.org/pdf/2611.14965) |
| 2026-11-10 | **REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding**<br><sub>Yu Tian</sub> | [arXiv](https://arxiv.org/abs/2611.14399) · [PDF](https://arxiv.org/pdf/2611.14399) · [Code](https://github.com/King-ty/speculators/tree/real-loss) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **303 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **SURMA: Efficient Fine-Grained Communication Offload for SuperPOD**<br><sub>Haoran Shang, Weifeng Zhang, Mengzhu Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21274) · [PDF](https://arxiv.org/pdf/2611.21274) |
| 2026-11-16 | **A Matter of Stages: Energy-Latency Trade-offs in Multimodal LLM Serving**<br><sub>Yifan Sun, Jiantong Jiang, Zhexiang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21165) · [PDF](https://arxiv.org/pdf/2611.21165) |
| 2026-11-16 | **Instant Weight-Space Consolidation for Long-Term Memory in LLMs**<br><sub>Manan Suri, Dinesh Manocha</sub> | [arXiv](https://arxiv.org/abs/2611.20759) · [PDF](https://arxiv.org/pdf/2611.20759) |
| 2026-11-15 | **CECAR: Cache &amp; Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs**<br><sub>Byeongju Kim, Hoonki Lee, Byungjun Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20119) · [PDF](https://arxiv.org/pdf/2611.20119) · [Code](https://github.com/hoonki2002/CECAR) |
| 2026-11-15 | **Making Preemption Productive in Long-Output LLM Serving**<br><sub>Ziji Shi, Xinyi Wan, Chaoyi Ruan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20106) · [PDF](https://arxiv.org/pdf/2611.20106) |
| 2026-11-15 | **EfficientSkill: Learning Skills for Token-Efficient Multi-Turn Agents**<br><sub>Deep Shah, Sanket Badhe, Nehal Kathrotia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19823) · [PDF](https://arxiv.org/pdf/2611.19823) |
| 2026-11-15 | **Multi-Branch Transformer**<br><sub>Gaotang Li, Lingjie Chen, Chunyuan Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19800) · [PDF](https://arxiv.org/pdf/2611.19800) |
| 2026-11-13 | **NVFP4-MLA: Unified FP4 KV-Cache Storage and Attention Computation for Multi-Head Latent Attention**<br><sub>Chao Ni, Qi Zhang, Xiao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18972) · [PDF](https://arxiv.org/pdf/2611.18972) |
| 2026-11-13 | **Exstill: The Most Efficient Single-Chip Processor for the Next Token**<br><sub>Valavan Manohararajah, Vithursan Thangarasa</sub> | [arXiv](https://arxiv.org/abs/2611.18859) · [PDF](https://arxiv.org/pdf/2611.18859) |
| 2026-11-12 | **Broadcast, Don&#x27;t Replicate: Eliminating Weight HBM in Datacenter LLM Serving**<br><sub>Hannah Atmer, Yuan Yao, Thiemo Voigt et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17097) · [PDF](https://arxiv.org/pdf/2611.17097) |
| 2026-11-12 | **Discovering Effective Agent Memory Designs through Program Evolution**<br><sub>Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17068) · [PDF](https://arxiv.org/pdf/2611.17068) · [Code](https://github.com/ash-ding/MAPE) |
| 2026-11-12 | **DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models**<br><sub>Yi-Hsin Hung, Fangfu Liu, Shao-Yuan Lo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16345) · [PDF](https://arxiv.org/pdf/2611.16345) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **139 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-15 | **TileCache: Serving Multi-Round Diffusion Image Editing with Compressed Activation Caches**<br><sub>Yuyang Tian, Desen Sun, Shuncheng Jie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20246) · [PDF](https://arxiv.org/pdf/2611.20246) |
| 2026-11-15 | **Cache or Denoise Less? Residual Reuse in a Flow-Matching World Action Model**<br><sub>Abhinav Gupta, Nissan Pow</sub> | [arXiv](https://arxiv.org/abs/2611.19709) · [PDF](https://arxiv.org/pdf/2611.19709) · [Code](https://github.com/gabhinav001/cache-or-denoise-less) |
| 2026-11-13 | **D2ToF: One-Step Diffusion for Depth Super-Resolution from Lightweight Single-Photon LiDAR Waveforms**<br><sub>Pallabjyoti Deka, Lewis Wilson, Stephen McLaughlin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.18243) · [PDF](https://arxiv.org/pdf/2611.18243) |
| 2026-11-12 | **DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models**<br><sub>Yi-Hsin Hung, Fangfu Liu, Shao-Yuan Lo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.16345) · [PDF](https://arxiv.org/pdf/2611.16345) |
| 2026-11-10 | **Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models**<br><sub>Amir Mann, Jonathan Fhima, Shaked Brody et al.</sub> | [arXiv](https://arxiv.org/abs/2611.14387) · [PDF](https://arxiv.org/pdf/2611.14387) |
| 2026-11-10 | **AdjointFlow: Accelerating Scientific Inverse Problems with Physics-Based Transport**<br><sub>Ethan Hanold, Nicholas M. Boffi, Qin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.13389) · [PDF](https://arxiv.org/pdf/2611.13389) |
| 2026-11-09 | **DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees**<br><sub>Zhicheng Zheng, Cheng Zhang, Chenkai Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12356) · [PDF](https://arxiv.org/pdf/2611.12356) · [Code](https://github.com/Perseus037/DForkTree) |
| 2026-11-08 | **MG-Cache: Multi-Granularity Caching for Accelerating Diffusion Transformer Inference**<br><sub>Zesen Chen, Youxuan Xu, Shigang Li</sub> | [arXiv](https://arxiv.org/abs/2611.11365) · [PDF](https://arxiv.org/pdf/2611.11365) |
| 2026-11-07 | **FADE: Fractional Anomalous Dynamics Extrapolation for Training-Free Diffusion Transformers Acceleration**<br><sub>Jinlong Yang, Lizilin, Jinke Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10514) · [PDF](https://arxiv.org/pdf/2611.10514) |
| 2026-11-07 | **ESTRA: Enabling Extreme Attention Sparsity for Training-Free Video Diffusion Acceleration**<br><sub>Enhuai Liu, Yunke Wang, Yutong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10448) · [PDF](https://arxiv.org/pdf/2611.10448) |
| 2026-11-07 | **IdealCache: Rethinking Cache Scheduling in Diffusion Transformers via Ideal Trajectories**<br><sub>Shang Xue, Li Zhu, Ping Chen</sub> | [arXiv](https://arxiv.org/abs/2611.10340) · [PDF](https://arxiv.org/pdf/2611.10340) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **240 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-16 | **ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching**<br><sub>Hao Tan, Jinghui Qin, Xuming Hu</sub> | [arXiv](https://arxiv.org/abs/2611.21038) · [PDF](https://arxiv.org/pdf/2611.21038) |
| 2026-11-16 | **Sparse Attention for Visual Generation: Toward Algorithm-System Co-Design**<br><sub>Majun Zhang, Yuan Guo, Decheng Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21029) · [PDF](https://arxiv.org/pdf/2611.21029) |
| 2026-11-16 | **QASK-Edit: Adaptive Sparse Attention Across Queries and Key Sources for Efficient Video Editing**<br><sub>Hengrui Liu, Wenbo Xu, Ziqi Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20704) · [PDF](https://arxiv.org/pdf/2611.20704) |
| 2026-11-16 | **Counterfactual Feature Steering for Adjacency-Preserving Identity Unlearning**<br><sub>FNU Shivam, Layth Sliman, Ramana Reddy et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20637) · [PDF](https://arxiv.org/pdf/2611.20637) |
| 2026-11-15 | **PoCoAttn: Position-Content Collaborative Sparse Attention for Fast and High-Fidelity Video Generation**<br><sub>Jianwen Wu, Meiling Wang, Junkang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20307) · [PDF](https://arxiv.org/pdf/2611.20307) |
| 2026-11-15 | **FastGRN: Few-Step Generative Refinement Networks**<br><sub>Haoyang Hu, Masataka Seo, Liang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20021) · [PDF](https://arxiv.org/pdf/2611.20021) |
| 2026-11-14 | **dit.xpu : Taming DiT Sparse Inference on Mobile SoCs**<br><sub>Jiayu Chen, Jinye Hu, Maoliang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.19261) · [PDF](https://arxiv.org/pdf/2611.19261) · [Code](https://github.com/IF-LAB-PKU/dit.xpu) |
| 2026-11-13 | **Role-Separated Diffusion Transformers: Global Rule Isolation and Deterministic Sampling Manifold Compression**<br><sub>Zhiguang Liu, Yi Shang</sub> | [arXiv](https://arxiv.org/abs/2611.19009) · [PDF](https://arxiv.org/pdf/2611.19009) · [Code](https://github.com/lz7fd/RoSeDiT) |
| 2026-11-13 | **Token2Tile: Token-Wise Sparse Attention with Tile Execution through a Low-Rank Space for Video DiTs**<br><sub>Xuecheng Wu, Aichen Feng, Jinyan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17930) · [PDF](https://arxiv.org/pdf/2611.17930) |
| 2026-11-13 | **Speed-Variation Distillation for Generative Modeling**<br><sub>Sukit Seripanitkarn, Phonphrm Thawatdamrongkit, Supasorn Suwajanakorn</sub> | [arXiv](https://arxiv.org/abs/2611.17868) · [PDF](https://arxiv.org/pdf/2611.17868) |
| 2026-11-13 | **CHARMING: Parallel Edge AI Acceleration Across Tensor Processing and In-Memory Computation**<br><sub>Md Omar Faruque, Jingang Jin, João Paulo C. de Lima et al.</sub> | [arXiv](https://arxiv.org/abs/2611.17785) · [PDF](https://arxiv.org/pdf/2611.17785) |
| 2026-11-10 | **Location Matters: Sparse Latent-Variance Attacks for Face Privacy against Diffusion Personalization**<br><sub>Shuting Yang, Shuxin Li, Linyan Dai et al.</sub> | [arXiv](https://arxiv.org/abs/2611.14254) · [PDF](https://arxiv.org/pdf/2611.14254) · [Code](https://github.com/Lvxan/SEAL) |

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
