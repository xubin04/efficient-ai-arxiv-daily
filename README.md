# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-13 21:04 CST** · **859 unique papers** · Newest submission: **2026-10-09**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 137 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 125 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 300 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 82 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 118 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 90 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 140 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 68 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 101 |

## Newly indexed · 2026-10-13

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **LapMerge: Differentiable Exact-Budget Token Merging in Linear Time**<br><sub>Magdalena Trędowicz, Aleksandra Nowak, Tomasz Steifer et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13858) · [PDF](https://arxiv.org/pdf/2610.13858) |
| 2026-10-09 | **DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs**<br><sub>Mahsa Salmani, Sayeh Sharify, Hesham Mostafa</sub> | [arXiv](https://arxiv.org/abs/2610.13767) · [PDF](https://arxiv.org/pdf/2610.13767) |
| 2026-10-09 | **zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss**<br><sub>Saibo Geng, Andrea Gentilini, Xinxian Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13605) · [PDF](https://arxiv.org/pdf/2610.13605) · [Code](https://github.com/epfl-dlab/zip2zip-plus-plus) |
| 2026-10-09 | **AudioTETRIS: Token Elimination via Transitional Importance Signals for Efficient Audio LLMs**<br><sub>Shreya Sajid, Anna Vettoruzzo, Joaquin Vanschoren</sub> | [arXiv](https://arxiv.org/abs/2610.13600) · [PDF](https://arxiv.org/pdf/2610.13600) |
| 2026-10-09 | **Defence against the dark arts of distillation: Unsupervised discovery of subliminal learning**<br><sub>Joseph Egan, Ciarán M. Gilligan-Lee, Michael O&#x27;Riordan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13536) · [PDF](https://arxiv.org/pdf/2610.13536) |
| 2026-10-09 | **VideoAWR: Reinforcing Video Flow Models with Decoupled-Timestep Advantage-Weighted Rectification**<br><sub>Zheming Fu, Wenbin Ning, Ruizhe He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13338) · [PDF](https://arxiv.org/pdf/2610.13338) · [Code](https://github.com/Fuzm7/FlowAWR) |
| 2026-10-09 | **Taking Tokenization off the Host for Agentic LLM Serving**<br><sub>Mohammad Siavashi, Pascal Schwinte, Ali Banaei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13325) · [PDF](https://arxiv.org/pdf/2610.13325) |
| 2026-10-09 | **BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain Reasoning Distillation**<br><sub>Jiaming Su, Suorong Yang, Xudong Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13285) · [PDF](https://arxiv.org/pdf/2610.13285) |
| 2026-10-09 | **SheafPrune: Sheaf-Guided Graph Propagation for Visual Token Pruning**<br><sub>Xiaoyang Ma, Chi Wang, Hong Sun</sub> | [arXiv](https://arxiv.org/abs/2610.13263) · [PDF](https://arxiv.org/pdf/2610.13263) · [Code](https://github.com/Bob0817912/SheafPrune_ICLR_2027) |
| 2026-10-09 | **High-Throughput Generative Video Super-Resolution on a Single Consumer GPU**<br><sub>Georgios Panaretou, Sotirios Chatzis</sub> | [arXiv](https://arxiv.org/abs/2610.13179) · [PDF](https://arxiv.org/pdf/2610.13179) |
| 2026-10-09 | **PreCoG: Preview-Edit for Efficient Video Correction in Generation-Time**<br><sub>Yilai Liu, Wenqi Pei, Zhifeng Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13174) · [PDF](https://arxiv.org/pdf/2610.13174) |
| 2026-10-09 | **PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling**<br><sub>Nan Jiang, Panagiotis Theodoropoulos, Wei Deng</sub> | [arXiv](https://arxiv.org/abs/2610.13171) · [PDF](https://arxiv.org/pdf/2610.13171) |
| 2026-10-09 | **When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows**<br><sub>Yuchen Ling, Shengcheng Yu, Zhenyu Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13092) · [PDF](https://arxiv.org/pdf/2610.13092) |
| 2026-10-09 | **SWEAR: Section-Wise Efficient Audio Reasoning via Self-Rated Difficulty**<br><sub>Yixuan Li, Minghao Lv, Xuenan Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13081) · [PDF](https://arxiv.org/pdf/2610.13081) |
| 2026-10-09 | **KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse**<br><sub>Taiga Ikeda, Daisuke Miyashita, Jun Deguchi</sub> | [arXiv](https://arxiv.org/abs/2610.13060) · [PDF](https://arxiv.org/pdf/2610.13060) · [Code](https://github.com/taiga333/eval-kv-repurpose) |
| 2026-10-09 | **Redirecting Teacher Supervision: Temporal-Response-Guided Latent Distillation for Video-Language Models**<br><sub>Xinkai Lu, Junli Zha, Haolan Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13045) · [PDF](https://arxiv.org/pdf/2610.13045) |
| 2026-10-09 | **RAMP: Recurrent Adaptive Mixed Precision for Efficient Prefill in Recurrent-Depth Language Models**<br><sub>Ke Wan, Chen Chen</sub> | [arXiv](https://arxiv.org/abs/2610.13041) · [PDF](https://arxiv.org/pdf/2610.13041) |
| 2026-10-09 | **GeoGR: Spatial-Semantic Token Compression and Group Routing for Efficient 3D VLMs**<br><sub>Yongxin Zheng, Hao Wu, Fang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13035) · [PDF](https://arxiv.org/pdf/2610.13035) · [Code](https://github.com/EIT-NLP/GeoGR) |
| 2026-10-09 | **Unified Generative Video Compression with Autoregressive and Bidirectional Video Diffusion**<br><sub>Tianyu Zhang, Shuai Huo, Dengchao Jin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13023) · [PDF](https://arxiv.org/pdf/2610.13023) |
| 2026-10-09 | **Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics**<br><sub>O. Ozan Koyluoglu</sub> | [arXiv](https://arxiv.org/abs/2610.13000) · [PDF](https://arxiv.org/pdf/2610.13000) |

[View all 859 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **137 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs**<br><sub>Mahsa Salmani, Sayeh Sharify, Hesham Mostafa</sub> | [arXiv](https://arxiv.org/abs/2610.13767) · [PDF](https://arxiv.org/pdf/2610.13767) |
| 2026-10-09 | **RAMP: Recurrent Adaptive Mixed Precision for Efficient Prefill in Recurrent-Depth Language Models**<br><sub>Ke Wan, Chen Chen</sub> | [arXiv](https://arxiv.org/abs/2610.13041) · [PDF](https://arxiv.org/pdf/2610.13041) |
| 2026-10-08 | **VFold: Symmetry-Aware Cross-Layer Value Cache Compression**<br><sub>Neha Verma, Sungwon Kim, Kenton Murray et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12338) · [PDF](https://arxiv.org/pdf/2610.12338) |
| 2026-10-08 | **DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception**<br><sub>Jinghua Hou, Zhe Liu, Hengshuang Zhao</sub> | [arXiv](https://arxiv.org/abs/2610.12266) · [PDF](https://arxiv.org/pdf/2610.12266) |
| 2026-10-08 | **Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers**<br><sub>Shiwen Wang, Pengxiang Zhao, Xiaoming Yuan</sub> | [arXiv](https://arxiv.org/abs/2610.11315) · [PDF](https://arxiv.org/pdf/2610.11315) |
| 2026-10-08 | **When Lower Reconstruction Loss Hurts: Distributionally Robust Refinement for Low-Bit LLM Quantization**<br><sub>Yanlong Zhao, Xiaoyuan Cheng, Huihang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11226) · [PDF](https://arxiv.org/pdf/2610.11226) |
| 2026-10-07 | **CORAL-KV: Compact Cross-Layer Prediction and Residual Coding for Autoregressive Video KV Caches**<br><sub>Albert Ge, Akash Haridas, Utkarsh Saxena et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12514) · [PDF](https://arxiv.org/pdf/2610.12514) |
| 2026-10-07 | **OrBIT: Structure-Guided Embedding Compression**<br><sub>Yunied Puig, Amit Kumar Jaiswal</sub> | [arXiv](https://arxiv.org/abs/2610.10385) · [PDF](https://arxiv.org/pdf/2610.10385) |
| 2026-10-07 | **Real-Time Joint Audio-Video Generation by Parallel Adapter Composition**<br><sub>Jingyu Li, Xiaoxiao Xiang, Yiwen Guo</sub> | [arXiv](https://arxiv.org/abs/2610.10343) · [PDF](https://arxiv.org/pdf/2610.10343) |
| 2026-10-07 | **Cache the Encoder Within:Compact, Reusable Memory across LLM Queries**<br><sub>Hanzuo Liu, Chunyu Liu, Chaofan Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.10058) · [PDF](https://arxiv.org/pdf/2610.10058) |
| 2026-10-07 | **Layerwise Error Attribution for Fast and Robust Mixed-Precision Post-Training Quantization**<br><sub>Samy Houache, Yann Traonmilin, Jean-François Aujol</sub> | [arXiv](https://arxiv.org/abs/2610.09877) · [PDF](https://arxiv.org/pdf/2610.09877) |
| 2026-10-07 | **OnlineQAT: On-Policy Distillation for Ultra-Low-Bit Large Language Models**<br><sub>Wenjun Wang, Heng Li, Yanggan Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.09346) · [PDF](https://arxiv.org/pdf/2610.09346) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **125 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **LapMerge: Differentiable Exact-Budget Token Merging in Linear Time**<br><sub>Magdalena Trędowicz, Aleksandra Nowak, Tomasz Steifer et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13858) · [PDF](https://arxiv.org/pdf/2610.13858) |
| 2026-10-09 | **zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss**<br><sub>Saibo Geng, Andrea Gentilini, Xinxian Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13605) · [PDF](https://arxiv.org/pdf/2610.13605) · [Code](https://github.com/epfl-dlab/zip2zip-plus-plus) |
| 2026-10-09 | **AudioTETRIS: Token Elimination via Transitional Importance Signals for Efficient Audio LLMs**<br><sub>Shreya Sajid, Anna Vettoruzzo, Joaquin Vanschoren</sub> | [arXiv](https://arxiv.org/abs/2610.13600) · [PDF](https://arxiv.org/pdf/2610.13600) |
| 2026-10-09 | **SheafPrune: Sheaf-Guided Graph Propagation for Visual Token Pruning**<br><sub>Xiaoyang Ma, Chi Wang, Hong Sun</sub> | [arXiv](https://arxiv.org/abs/2610.13263) · [PDF](https://arxiv.org/pdf/2610.13263) · [Code](https://github.com/Bob0817912/SheafPrune_ICLR_2027) |
| 2026-10-09 | **GeoGR: Spatial-Semantic Token Compression and Group Routing for Efficient 3D VLMs**<br><sub>Yongxin Zheng, Hao Wu, Fang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13035) · [PDF](https://arxiv.org/pdf/2610.13035) · [Code](https://github.com/EIT-NLP/GeoGR) |
| 2026-10-09 | **Video Codec-Guided Training-Free Token Compression for Video Large Language Models**<br><sub>Xihua Sheng, Ruijie Liu, Chang Wen Chen</sub> | [arXiv](https://arxiv.org/abs/2610.12959) · [PDF](https://arxiv.org/pdf/2610.12959) |
| 2026-10-08 | **VFold: Symmetry-Aware Cross-Layer Value Cache Compression**<br><sub>Neha Verma, Sungwon Kim, Kenton Murray et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12338) · [PDF](https://arxiv.org/pdf/2610.12338) |
| 2026-10-08 | **SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference**<br><sub>Qitong Wang, Xinwei Niu, Mingluo Su et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12327) · [PDF](https://arxiv.org/pdf/2610.12327) |
| 2026-10-08 | **Look Back, Think Ahead: Visual Memory on Demand for Efficient Multimodal Reasoning**<br><sub>Yicheng Xue, Han Wu, Jufeng Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12060) · [PDF](https://arxiv.org/pdf/2610.12060) |
| 2026-10-08 | **MAP4CS: A Multi-dimensional Data Pruning Framework for Efficient Code Retriever Fine-tuning**<br><sub>Yuxuan Chen, Mingwei Liu, Guangsheng Ou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11727) · [PDF](https://arxiv.org/pdf/2610.11727) |
| 2026-10-08 | **ReCal: Calibrating Structured Pruning for On-Policy Distillation Recovery**<br><sub>Houcheng Jiang, Mao Zheng, Mingyang Song et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11332) · [PDF](https://arxiv.org/pdf/2610.11332) |
| 2026-10-08 | **iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity**<br><sub>Chengfeng Han, Baole Ai, Xianlu Bian et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11302) · [PDF](https://arxiv.org/pdf/2610.11302) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **300 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **Defence against the dark arts of distillation: Unsupervised discovery of subliminal learning**<br><sub>Joseph Egan, Ciarán M. Gilligan-Lee, Michael O&#x27;Riordan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13536) · [PDF](https://arxiv.org/pdf/2610.13536) |
| 2026-10-09 | **BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain Reasoning Distillation**<br><sub>Jiaming Su, Suorong Yang, Xudong Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13285) · [PDF](https://arxiv.org/pdf/2610.13285) |
| 2026-10-09 | **High-Throughput Generative Video Super-Resolution on a Single Consumer GPU**<br><sub>Georgios Panaretou, Sotirios Chatzis</sub> | [arXiv](https://arxiv.org/abs/2610.13179) · [PDF](https://arxiv.org/pdf/2610.13179) |
| 2026-10-09 | **PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling**<br><sub>Nan Jiang, Panagiotis Theodoropoulos, Wei Deng</sub> | [arXiv](https://arxiv.org/abs/2610.13171) · [PDF](https://arxiv.org/pdf/2610.13171) |
| 2026-10-09 | **Redirecting Teacher Supervision: Temporal-Response-Guided Latent Distillation for Video-Language Models**<br><sub>Xinkai Lu, Junli Zha, Haolan Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13045) · [PDF](https://arxiv.org/pdf/2610.13045) |
| 2026-10-09 | **Unified Generative Video Compression with Autoregressive and Bidirectional Video Diffusion**<br><sub>Tianyu Zhang, Shuai Huo, Dengchao Jin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13023) · [PDF](https://arxiv.org/pdf/2610.13023) |
| 2026-10-09 | **Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics**<br><sub>O. Ozan Koyluoglu</sub> | [arXiv](https://arxiv.org/abs/2610.13000) · [PDF](https://arxiv.org/pdf/2610.13000) |
| 2026-10-09 | **A Lightweight Velocity Correction Framework for Improving Instruction Following in Few-Step Text-to-Image Generation**<br><sub>Yating Gao, Zhenlong Zhu, Wen Zihao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12899) · [PDF](https://arxiv.org/pdf/2610.12899) |
| 2026-10-09 | **One-Step Text Generation by Seq-Drifting**<br><sub>Jiayu Liu, Ruizhi Zhao, Tianyun Ji et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12879) · [PDF](https://arxiv.org/pdf/2610.12879) · [Code](https://github.com/jyliu-ai/Seq-Drifting) |
| 2026-10-09 | **COFFEQA: Counterfactual-Guided Few-Shot Distillation for LLM Question Answering**<br><sub>Kavinda Kehelella, Sanghamitra Dutta</sub> | [arXiv](https://arxiv.org/abs/2610.12837) · [PDF](https://arxiv.org/pdf/2610.12837) |
| 2026-10-08 | **Amortised Inference through One-Step Implicit Sampling**<br><sub>Vincent Pauline, Kirill Tamogashev, Arran Carter et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12679) · [PDF](https://arxiv.org/pdf/2610.12679) |
| 2026-10-08 | **ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion**<br><sub>Zekai Gu, Peng Wang, Jiahao Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12625) · [PDF](https://arxiv.org/pdf/2610.12625) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **82 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **Personalized Federated Direct Preference Optimization via LoRA Adapters**<br><sub>Zhanhong Jiang, Soumik Sarkar</sub> | [arXiv](https://arxiv.org/abs/2610.12885) · [PDF](https://arxiv.org/pdf/2610.12885) |
| 2026-10-08 | **DPPM: Dual-Path Parametric Memory for Personalized Language Models**<br><sub>Yuhao Chen, Shuochen Liu, Jiayao Shi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11776) · [PDF](https://arxiv.org/pdf/2610.11776) |
| 2026-10-08 | **V-CoLA: Vision Token Compression with Linear Attention**<br><sub>Hao Jiang, Yiru Mao, Tianpeng Bu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11251) · [PDF](https://arxiv.org/pdf/2610.11251) |
| 2026-10-08 | **Breaking the Group Size Barrier: Parameter-Efficient Group Dance Generation with Chain-of-Dancers**<br><sub>Jing Xu, Cunjian Chen, Qiuhong Ke</sub> | [arXiv](https://arxiv.org/abs/2610.11237) · [PDF](https://arxiv.org/pdf/2610.11237) |
| 2026-10-08 | **LadderEdit: Edit-Level Residual Compression for Memory-Efficient Lifelong Editing of LLMs**<br><sub>Xiaobing Yu, Peijie Qiu, Jin Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11160) · [PDF](https://arxiv.org/pdf/2610.11160) |
| 2026-10-08 | **Stability-Plasticity Balance via Singular-Vector Selection in LLM Continual Learning**<br><sub>Lingxiang Wang, Hainan Zhang, Liang Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11076) · [PDF](https://arxiv.org/pdf/2610.11076) |
| 2026-10-07 | **Marrying Pricing and Advertising with LLMs**<br><sub>Alessandro Barro, Francesco Bacchiocchi, Francesco Emanuele Stradi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.09985) · [PDF](https://arxiv.org/pdf/2610.09985) |
| 2026-10-06 | **Are Parameter-Efficient Fine-tuning Methods Really Different?**<br><sub>Yikuan Li, Pinyan Lu, Fanghui Liu</sub> | [arXiv](https://arxiv.org/abs/2610.09122) · [PDF](https://arxiv.org/pdf/2610.09122) · [Code](https://github.com/Kuaaannn/PEFT_methods) |
| 2026-10-06 | **CoDe-LoRA: Mitigating the Orthogonality Dilemma in Continual Learning of LLMs via Knowledge Consolidation and Decoupling**<br><sub>Maoqi Liu, Quan Fang, Yufei He</sub> | [arXiv](https://arxiv.org/abs/2610.08312) · [PDF](https://arxiv.org/pdf/2610.08312) · [Code](https://github.com/Estrellajer/CoDe-LoRA) |
| 2026-10-06 | **Dynamic Positional Attention Modulation for Parameter-Efficient Fine-Tuning of Large Language Models**<br><sub>Dayan Pan, Jingyuan Wang, Xie Yu</sub> | [arXiv](https://arxiv.org/abs/2610.07848) · [PDF](https://arxiv.org/pdf/2610.07848) |
| 2026-10-05 | **Conditional Rank Allocation for Taxonomy-Aware Medical Language Model Adaptation**<br><sub>Guangyuan Dong, Ziwei Hong, Xuehao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.06765) · [PDF](https://arxiv.org/pdf/2610.06765) |
| 2026-10-05 | **Scaling Down the Scaling Laws: Parameter Efficiency and Compute-Optimal Training in Resource-Constrained Large Language Models**<br><sub>Joe Dwyer</sub> | [arXiv](https://arxiv.org/abs/2610.06387) · [PDF](https://arxiv.org/pdf/2610.06387) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **118 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse**<br><sub>Taiga Ikeda, Daisuke Miyashita, Jun Deguchi</sub> | [arXiv](https://arxiv.org/abs/2610.13060) · [PDF](https://arxiv.org/pdf/2610.13060) · [Code](https://github.com/taiga333/eval-kv-repurpose) |
| 2026-10-08 | **Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation**<br><sub>Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11756) · [PDF](https://arxiv.org/pdf/2610.11756) |
| 2026-10-08 | **BioBigBird: A Sparse Attention Model for Long-Range Dependency Processing in Biomedical Text**<br><sub>Roshan Balaji, Pavan Kumar S, Vasudev Gupta et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11430) · [PDF](https://arxiv.org/pdf/2610.11430) · [Code](https://huggingface.co/collections/bisectgroup/biobigbird) |
| 2026-10-08 | **RaReCache: Bridging the Gap in Cross-Model KV Cache Reuse via Rank disagreement-based Selective Recomputation**<br><sub>Sreetama Sarkar, Saptarshi Mitra, Sitao Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11358) · [PDF](https://arxiv.org/pdf/2610.11358) |
| 2026-10-08 | **iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity**<br><sub>Chengfeng Han, Baole Ai, Xianlu Bian et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11302) · [PDF](https://arxiv.org/pdf/2610.11302) |
| 2026-10-08 | **V-CoLA: Vision Token Compression with Linear Attention**<br><sub>Hao Jiang, Yiru Mao, Tianpeng Bu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11251) · [PDF](https://arxiv.org/pdf/2610.11251) |
| 2026-10-08 | **Emergent Inverse-Depth Scaling From Nonlinearity In Attention**<br><sub>Zirui Peng, Yizhou Liu, Ziming Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11063) · [PDF](https://arxiv.org/pdf/2610.11063) |
| 2026-10-07 | **Sparse Attention Is Matrix Approximation, Not Choosing from a Bag of Values**<br><sub>Fang Wan, Xufeng Liu, Fan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.10871) · [PDF](https://arxiv.org/pdf/2610.10871) |
| 2026-10-07 | **CORAL-KV: Compact Cross-Layer Prediction and Residual Coding for Autoregressive Video KV Caches**<br><sub>Albert Ge, Akash Haridas, Utkarsh Saxena et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12514) · [PDF](https://arxiv.org/pdf/2610.12514) |
| 2026-10-06 | **A Self-Pruning Transformer: Extreme KV-Cache Compression with Universal Attention**<br><sub>Davis Wertheimer, Haochen Shen, Ahan Gupta et al.</sub> | [arXiv](https://arxiv.org/abs/2610.09051) · [PDF](https://arxiv.org/pdf/2610.09051) |
| 2026-10-06 | **Visual Memory Attacks Can Persist Through The KV Cache**<br><sub>David Dobre, Leo Schwinn, Gauthier Gidel et al.</sub> | [arXiv](https://arxiv.org/abs/2610.09027) · [PDF](https://arxiv.org/pdf/2610.09027) |
| 2026-10-06 | **Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation**<br><sub>Liao Ma, Jiayi Song, Yunfeng Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.08772) · [PDF](https://arxiv.org/pdf/2610.08772) · [Code](https://github.com/lama0110/BASA) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **90 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **SWEAR: Section-Wise Efficient Audio Reasoning via Self-Rated Difficulty**<br><sub>Yixuan Li, Minghao Lv, Xuenan Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13081) · [PDF](https://arxiv.org/pdf/2610.13081) |
| 2026-10-09 | **Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding**<br><sub>Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12939) · [PDF](https://arxiv.org/pdf/2610.12939) |
| 2026-10-09 | **Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training**<br><sub>Suorong Yang, Jiaxin Wang, Jiaming Su et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12933) · [PDF](https://arxiv.org/pdf/2610.12933) |
| 2026-10-08 | **Contextual Correction of Parallel Draftsfor Speculative Decoding**<br><sub>Roy Eisenstadt, Harel Lidar, Tal Gonen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12570) · [PDF](https://arxiv.org/pdf/2610.12570) |
| 2026-10-08 | **When Should Agents Think? Adaptive Reasoning via Cross-Turn Estimation**<br><sub>Yiruo Cheng, Shen Huang, Xiaoshuai Song et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12061) · [PDF](https://arxiv.org/pdf/2610.12061) |
| 2026-10-07 | **Speedbumps: Rejection Attacks on Speculative Decoding**<br><sub>Adam Y. J. Jones, Yu Yuan, Sergio Maffeis</sub> | [arXiv](https://arxiv.org/abs/2610.10929) · [PDF](https://arxiv.org/pdf/2610.10929) |
| 2026-10-07 | **From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic Policy Discovery**<br><sub>Xinglin Wang, Zishen Liu, Tong Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.09684) · [PDF](https://arxiv.org/pdf/2610.09684) |
| 2026-10-07 | **Efficient Reasoning with Flow Language Models**<br><sub>Hanru Bai, Faissal Izermine, Oscar Davis et al.</sub> | [arXiv](https://arxiv.org/abs/2610.09416) · [PDF](https://arxiv.org/pdf/2610.09416) |
| 2026-10-06 | **AdaGuard: Enhancing Safety and Policy Compliance with Reasoning-Enabled LLM-As-A-Judge Guardrails**<br><sub>Melissa Kazemi Rad, Sihui Dai, Isha Slavin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.08923) · [PDF](https://arxiv.org/pdf/2610.08923) |
| 2026-10-06 | **Secure Speculative Decoding for Large Language Models**<br><sub>Yichi Zhang, Zhiqi Wang, Neil Gong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.08678) · [PDF](https://arxiv.org/pdf/2610.08678) |
| 2026-10-06 | **DLoop: Looped Speculative Decoding**<br><sub>Geonmo Gu, Byeongho Heo, HeeJae Jun et al.</sub> | [arXiv](https://arxiv.org/abs/2610.07659) · [PDF](https://arxiv.org/pdf/2610.07659) · [Code](https://github.com/naver-ai/DLoop) |
| 2026-10-05 | **CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling**<br><sub>Yifan Zhang, Yutong Dai, Viraj Prabhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.06829) · [PDF](https://arxiv.org/pdf/2610.06829) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **140 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **Taking Tokenization off the Host for Agentic LLM Serving**<br><sub>Mohammad Siavashi, Pascal Schwinte, Ali Banaei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13325) · [PDF](https://arxiv.org/pdf/2610.13325) |
| 2026-10-09 | **When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows**<br><sub>Yuchen Ling, Shengcheng Yu, Zhenyu Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13092) · [PDF](https://arxiv.org/pdf/2610.13092) |
| 2026-10-09 | **KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse**<br><sub>Taiga Ikeda, Daisuke Miyashita, Jun Deguchi</sub> | [arXiv](https://arxiv.org/abs/2610.13060) · [PDF](https://arxiv.org/pdf/2610.13060) · [Code](https://github.com/taiga333/eval-kv-repurpose) |
| 2026-10-09 | **Video Codec-Guided Training-Free Token Compression for Video Large Language Models**<br><sub>Xihua Sheng, Ruijie Liu, Chang Wen Chen</sub> | [arXiv](https://arxiv.org/abs/2610.12959) · [PDF](https://arxiv.org/pdf/2610.12959) |
| 2026-10-08 | **TokenRouter: Efficient Serving System for Token-Level LLM Routing**<br><sub>Tianyu Fu, Tengxuan Liu, Ruoxi Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12242) · [PDF](https://arxiv.org/pdf/2610.12242) · [Code](https://github.com/thu-nics/TokenRouter) |
| 2026-10-08 | **RaReCache: Bridging the Gap in Cross-Model KV Cache Reuse via Rank disagreement-based Selective Recomputation**<br><sub>Sreetama Sarkar, Saptarshi Mitra, Sitao Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11358) · [PDF](https://arxiv.org/pdf/2610.11358) |
| 2026-10-08 | **From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-Term Dialogue**<br><sub>Zirui Liao, Zhengxian Wu, Zhuohong Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11314) · [PDF](https://arxiv.org/pdf/2610.11314) · [Code](https://github.com/Silent-Rain02/CogMem) |
| 2026-10-07 | **Real Long-Term Memory for AI: A 50-Million-Token Window That Is Faster and Cheaper Than Recompute**<br><sub>Sietse Schelpe</sub> | [arXiv](https://arxiv.org/abs/2610.10845) · [PDF](https://arxiv.org/pdf/2610.10845) |
| 2026-10-07 | **Stale, Misattributed, or Late: Where Personal Memory Fails Before Generation**<br><sub>Haonan Deng, Park Sinchaisri</sub> | [arXiv](https://arxiv.org/abs/2610.10265) · [PDF](https://arxiv.org/pdf/2610.10265) |
| 2026-10-07 | **Shared Low-rank Basis Factorization for Data-free Mixture-of-Experts Compression**<br><sub>Tianxiao Cao, Jiahe Shao, Yuning Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.09342) · [PDF](https://arxiv.org/pdf/2610.09342) |
| 2026-10-07 | **vLLM-Omni Technical Report: A Unified Serving Runtime for Omni-Modality Generation**<br><sub>vLLM-Omni Team</sub> | [arXiv](https://arxiv.org/abs/2610.09307) · [PDF](https://arxiv.org/pdf/2610.09307) |
| 2026-10-06 | **RACER: Reflective Agent Coupling Query Interpretation and Tool-Based Retrieval for Frame Selection in Long Video Understanding**<br><sub>Yiyang Huang, Yitian Zhang, Yizhou Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.08954) · [PDF](https://arxiv.org/pdf/2610.08954) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **68 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-08 | **DiffuPlex: Accelerating Full-Duplex Spoken Dialog Models via Rolling Masked Diffusion**<br><sub>Heeseung Kim</sub> | [arXiv](https://arxiv.org/abs/2610.12214) · [PDF](https://arxiv.org/pdf/2610.12214) |
| 2026-10-08 | **Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation**<br><sub>Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11756) · [PDF](https://arxiv.org/pdf/2610.11756) |
| 2026-10-08 | **CacheScope: Exact-Compute Allocation for Training-Free Diffusion Acceleration**<br><sub>Qinhan Lyu, Jusheng Zhang, Zhixing Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12530) · [PDF](https://arxiv.org/pdf/2610.12530) |
| 2026-10-08 | **WAM-Cache: Staleness-Bounded KV Reuse for Efficient World Action Models**<br><sub>Kai Ding, Yang He, Ruijie Quan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11401) · [PDF](https://arxiv.org/pdf/2610.11401) |
| 2026-10-08 | **iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity**<br><sub>Chengfeng Han, Baole Ai, Xianlu Bian et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11302) · [PDF](https://arxiv.org/pdf/2610.11302) |
| 2026-10-08 | **DynaTE: Accelerating Diffusion LLMs via Dynamic Token Execution**<br><sub>Minghan Jiang, Jiayi Wang, Shuaiting Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11284) · [PDF](https://arxiv.org/pdf/2610.11284) |
| 2026-10-07 | **CORAL-KV: Compact Cross-Layer Prediction and Residual Coding for Autoregressive Video KV Caches**<br><sub>Albert Ge, Akash Haridas, Utkarsh Saxena et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12514) · [PDF](https://arxiv.org/pdf/2610.12514) |
| 2026-10-07 | **MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration**<br><sub>Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.10457) · [PDF](https://arxiv.org/pdf/2610.10457) · [Code](https://github.com/x10ngyx/MORCA) |
| 2026-10-07 | **Seq-Flow: Efficient Probabilistic Forecasting with Self-Rollout Error Control**<br><sub>Yinan Huang, Shitij Govil, Bo Dai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.10440) · [PDF](https://arxiv.org/pdf/2610.10440) · [Code](https://github.com/Graph-COM/Seq-Flow) |
| 2026-10-07 | **Koopman Observers for Diffusion Acceleration: Correcting Feature Forecasts with Shallow Measurements**<br><sub>Hanru Bai, Yuanchao Xu, Fengyi Li</sub> | [arXiv](https://arxiv.org/abs/2610.10366) · [PDF](https://arxiv.org/pdf/2610.10366) |
| 2026-10-07 | **Kinetic Langevin Meets Split Gibbs: Accelerated Posterior Sampling for Imaging Inverse Problems with Diffusion Priors**<br><sub>Dai Hai Nguyen, Duc Dung Nguyen</sub> | [arXiv](https://arxiv.org/abs/2610.10187) · [PDF](https://arxiv.org/pdf/2610.10187) |
| 2026-10-06 | **Consistent Distribution Matching for Data-Free Diffusion Distillation**<br><sub>Yuxiang Fu, Qi Yan, Zike Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.09221) · [PDF](https://arxiv.org/pdf/2610.09221) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **101 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-09 | **VideoAWR: Reinforcing Video Flow Models with Decoupled-Timestep Advantage-Weighted Rectification**<br><sub>Zheming Fu, Wenbin Ning, Ruizhe He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13338) · [PDF](https://arxiv.org/pdf/2610.13338) · [Code](https://github.com/Fuzm7/FlowAWR) |
| 2026-10-09 | **PreCoG: Preview-Edit for Efficient Video Correction in Generation-Time**<br><sub>Yilai Liu, Wenqi Pei, Zhifeng Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13174) · [PDF](https://arxiv.org/pdf/2610.13174) |
| 2026-10-09 | **Unified Generative Video Compression with Autoregressive and Bidirectional Video Diffusion**<br><sub>Tianyu Zhang, Shuai Huo, Dengchao Jin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13023) · [PDF](https://arxiv.org/pdf/2610.13023) |
| 2026-10-09 | **A Lightweight Velocity Correction Framework for Improving Instruction Following in Few-Step Text-to-Image Generation**<br><sub>Yating Gao, Zhenlong Zhu, Wen Zihao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12899) · [PDF](https://arxiv.org/pdf/2610.12899) |
| 2026-10-08 | **ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion**<br><sub>Zekai Gu, Peng Wang, Jiahao Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12625) · [PDF](https://arxiv.org/pdf/2610.12625) |
| 2026-10-08 | **DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models**<br><sub>Zhenglin Wan, Jiayu Chen, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12572) · [PDF](https://arxiv.org/pdf/2610.12572) · [Code](https://github.com/vanzll/DiffusionART) |
| 2026-10-08 | **From Prompting to Composing: A Spatial Canvas Interface for Poster Generation**<br><sub>Yitong Wang, Fangyun Wei, Jinjing Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12230) · [PDF](https://arxiv.org/pdf/2610.12230) · [Code](https://github.com/snowflakewang/Compo) |
| 2026-10-08 | **Connected Self Forcing: Beyond Local Learning in Video Autoregression**<br><sub>Dongbin Zhang, Chaoda Zheng, Kangjie Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12156) · [PDF](https://arxiv.org/pdf/2610.12156) |
| 2026-10-08 | **VEDJE: Video-Efficient Discriminative Joint Encoder for Scalable Video-Text Retrieval**<br><sub>Shahaf Wagner, Gabriele Serussi, Dan Ben Ami et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11850) · [PDF](https://arxiv.org/pdf/2610.11850) |
| 2026-10-08 | **Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation**<br><sub>Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11756) · [PDF](https://arxiv.org/pdf/2610.11756) |
| 2026-10-08 | **CacheScope: Exact-Compute Allocation for Training-Free Diffusion Acceleration**<br><sub>Qinhan Lyu, Jusheng Zhang, Zhixing Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12530) · [PDF](https://arxiv.org/pdf/2610.12530) |
| 2026-10-08 | **Parametric Trajectory Distillation for Few-Step Video Generation**<br><sub>Lan Feng, Peter Karkus, Maximilian Igl et al.</sub> | [arXiv](https://arxiv.org/abs/2610.11498) · [PDF](https://arxiv.org/pdf/2610.11498) |

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
