# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-06 15:57 CST** · **1576 unique papers** · Newest submission: **2026-11-05**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 251 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 227 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 509 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 167 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 234 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 155 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 259 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 126 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 213 |

## Newly indexed · 2026-11-06

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **Towards interpreting any residual stream direction by scaling activation inversion**<br><sub>Celeste De Schamphelaere, Juan J. Vazquez, Ari Spiesberger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08465) · [PDF](https://arxiv.org/pdf/2611.08465) |
| 2026-11-05 | **T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models**<br><sub>Mohammed Hassan, Zhenyang Chen, Zheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08413) · [PDF](https://arxiv.org/pdf/2611.08413) |
| 2026-11-05 | **StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference**<br><sub>Jake Hyun, Ziyu Zhao, Jae-sun Seo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) |
| 2026-11-05 | **Measured Coupling for Parallel Decoding in Diffusion Language Models**<br><sub>Tal Oved, Lior Wolf</sub> | [arXiv](https://arxiv.org/abs/2611.08307) · [PDF](https://arxiv.org/pdf/2611.08307) |
| 2026-11-05 | **Should You Split Decode? Disaggregation Across Future Models and Accelerators**<br><sub>Ramyad Hadidi</sub> | [arXiv](https://arxiv.org/abs/2611.08299) · [PDF](https://arxiv.org/pdf/2611.08299) |
| 2026-11-05 | **AutoCompress: Automated Hardware-Guided Model Compression**<br><sub>Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08290) · [PDF](https://arxiv.org/pdf/2611.08290) |
| 2026-11-05 | **FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning**<br><sub>Haitao Lin, Minsi Ren, Yang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08240) · [PDF](https://arxiv.org/pdf/2611.08240) |
| 2026-11-05 | **ProQuant: Progressive Quantization-aware Training for Edge MLLMs**<br><sub>Yufei Xue, Yushi Huang, Jiawei Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08216) · [PDF](https://arxiv.org/pdf/2611.08216) · [Code](https://github.com/yufeixue-ai/ProQuant/) |
| 2026-11-05 | **Beyond K/V Caches: Cross-Model State Handoff in Hybrid Linear-Attention LLMs**<br><sub>Jiacheng Cai, Tao Zhang, Siqi Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08133) · [PDF](https://arxiv.org/pdf/2611.08133) |
| 2026-11-05 | **Learning Dynamics of On-Policy Distillation**<br><sub>Guan Zhe Hong, Sumeet Ramesh Motwani, Liang Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08016) · [PDF](https://arxiv.org/pdf/2611.08016) |
| 2026-11-05 | **Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs**<br><sub>Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani</sub> | [arXiv](https://arxiv.org/abs/2611.07988) · [PDF](https://arxiv.org/pdf/2611.07988) |
| 2026-11-05 | **QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents**<br><sub>Yingjie Tan, Haiquan Qiu, Quanming Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07976) · [PDF](https://arxiv.org/pdf/2611.07976) |
| 2026-11-05 | **Flux as a Codec: Zero-Shot Lossy Compression with Flux**<br><sub>Fuma Kimishima, Jinjia Zhou</sub> | [arXiv](https://arxiv.org/abs/2611.07929) · [PDF](https://arxiv.org/pdf/2611.07929) |
| 2026-11-05 | **EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure**<br><sub>Kwan Yun, Minhyeok Bang, Colette Suhjung Koo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07909) · [PDF](https://arxiv.org/pdf/2611.07909) |
| 2026-11-05 | **When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale**<br><sub>Gautam Gupta, Dikshant Kukreja, Unique Kumar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07891) · [PDF](https://arxiv.org/pdf/2611.07891) |
| 2026-11-05 | **Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding**<br><sub>Adrian Baule</sub> | [arXiv](https://arxiv.org/abs/2611.07845) · [PDF](https://arxiv.org/pdf/2611.07845) |
| 2026-11-05 | **Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval**<br><sub>Dohoon Kim, Junho Park, Hyunwoong Bae et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07820) · [PDF](https://arxiv.org/pdf/2611.07820) · [Code](https://github.com/dohoonkim-ai/axis-lora) |
| 2026-11-05 | **Reinforcing What the Student Has Learned: Teacher-Guided On-Policy Distillation**<br><sub>Bozhen Fang, Linhao Zhong, Xuehao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07722) · [PDF](https://arxiv.org/pdf/2611.07722) · [Code](https://github.com/aim-uofa/sd-opd) |
| 2026-11-05 | **Embedding-Space Fingerprinting of LoRA Fine-Tunes: Recovering the Training-Data Domain from the Model Artifact Alone**<br><sub>Shivesh Rane</sub> | [arXiv](https://arxiv.org/abs/2611.07610) · [PDF](https://arxiv.org/pdf/2611.07610) |
| 2026-11-05 | **FisherDistill: Diffusion Distribution Distillation via Closed-Form Fisher Critics**<br><sub>Mahesh Bhosale, Yuanhao Zhai, Siwei Lyu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07604) · [PDF](https://arxiv.org/pdf/2611.07604) |

[View all 37 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **251 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference**<br><sub>Jake Hyun, Ziyu Zhao, Jae-sun Seo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) |
| 2026-11-05 | **ProQuant: Progressive Quantization-aware Training for Edge MLLMs**<br><sub>Yufei Xue, Yushi Huang, Jiawei Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08216) · [PDF](https://arxiv.org/pdf/2611.08216) · [Code](https://github.com/yufeixue-ai/ProQuant/) |
| 2026-11-05 | **Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs**<br><sub>Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani</sub> | [arXiv](https://arxiv.org/abs/2611.07988) · [PDF](https://arxiv.org/pdf/2611.07988) |
| 2026-11-05 | **When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale**<br><sub>Gautam Gupta, Dikshant Kukreja, Unique Kumar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07891) · [PDF](https://arxiv.org/pdf/2611.07891) |
| 2026-11-05 | **TACT-KV: Tri-Axis Cosine Transform for Compressing Volumetric KV Caches in Medical VLMs**<br><sub>Chongyu Qu, Ritchie Zhao, Yufan He et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07593) · [PDF](https://arxiv.org/pdf/2611.07593) |
| 2026-11-05 | **ACSeL: Adaptive Configuration Search for Hardware-Constrained LLM Inference**<br><sub>Bokun Wang, Hung-Yueh Chiang, Diana Marculescu</sub> | [arXiv](https://arxiv.org/abs/2611.07570) · [PDF](https://arxiv.org/pdf/2611.07570) |
| 2026-11-05 | **TriAttention: Unified Sparse Mixed-Precision Attention for Long-Context LLM Inference**<br><sub>Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07256) · [PDF](https://arxiv.org/pdf/2611.07256) · [Code](https://github.com/HanzhiZhang-Ulrica/TriAttention) |
| 2026-11-04 | **TileQuant: Tile as the Precision-Allocation Unit for LLM Mixed-Precision Post-Training Quantization**<br><sub>Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07217) · [PDF](https://arxiv.org/pdf/2611.07217) · [Code](https://github.com/HanzhiZhang-Ulrica/TileQuant) |
| 2026-11-04 | **NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation**<br><sub>Jiacheng Lu, Haoyi Zhu, Sipei Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06377) · [PDF](https://arxiv.org/pdf/2611.06377) · [Code](https://github.com/jiacheng-lu03/NanoKV) |
| 2026-11-04 | **UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence**<br><sub>Mingkang Liu, Peipei Jiao, Weiming Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06075) · [PDF](https://arxiv.org/pdf/2611.06075) |
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-03 | **Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation**<br><sub>Rohan Agarwal, Robin Andeer, Alex Armbruster et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05642) · [PDF](https://arxiv.org/pdf/2611.05642) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **227 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models**<br><sub>Mohammed Hassan, Zhenyang Chen, Zheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08413) · [PDF](https://arxiv.org/pdf/2611.08413) |
| 2026-11-05 | **AutoCompress: Automated Hardware-Guided Model Compression**<br><sub>Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08290) · [PDF](https://arxiv.org/pdf/2611.08290) |
| 2026-11-05 | **When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale**<br><sub>Gautam Gupta, Dikshant Kukreja, Unique Kumar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07891) · [PDF](https://arxiv.org/pdf/2611.07891) |
| 2026-11-05 | **SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking**<br><sub>Moonseok Choi, Jongwon Jeong, Minki Kang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07558) · [PDF](https://arxiv.org/pdf/2611.07558) |
| 2026-11-05 | **Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion**<br><sub>Jia Li, Xurui Peng, Xing Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07551) · [PDF](https://arxiv.org/pdf/2611.07551) |
| 2026-11-05 | **TriAttention: Unified Sparse Mixed-Precision Attention for Long-Context LLM Inference**<br><sub>Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07256) · [PDF](https://arxiv.org/pdf/2611.07256) · [Code](https://github.com/HanzhiZhang-Ulrica/TriAttention) |
| 2026-11-04 | **Tools Need Not Speak in Text: Latent Context Compression for Agents**<br><sub>Yuetong Liu, Zhehao Zhou, Yitong Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06500) · [PDF](https://arxiv.org/pdf/2611.06500) · [Code](https://github.com/THU-Agent/Coca-cola) |
| 2026-11-04 | **RI-Prune: Relation and Information Aware Visual Token Pruning for Multi-Image Vision-Language Models**<br><sub>Dongjin Lee, Eunju Lee, Jinhee Jang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06047) · [PDF](https://arxiv.org/pdf/2611.06047) |
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-04 | **Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models**<br><sub>Donggeun Kim</sub> | [arXiv](https://arxiv.org/abs/2611.05927) · [PDF](https://arxiv.org/pdf/2611.05927) · [Code](https://github.com/nota-github/MAEP) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |
| 2026-11-03 | **BtsPruner: Role-Aware Visual Token Pruning for Large Vision-Language Models**<br><sub>Zihao Qi, Zhibo Zhang, Miaoxin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04537) · [PDF](https://arxiv.org/pdf/2611.04537) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **509 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning**<br><sub>Haitao Lin, Minsi Ren, Yang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08240) · [PDF](https://arxiv.org/pdf/2611.08240) |
| 2026-11-05 | **Learning Dynamics of On-Policy Distillation**<br><sub>Guan Zhe Hong, Sumeet Ramesh Motwani, Liang Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08016) · [PDF](https://arxiv.org/pdf/2611.08016) |
| 2026-11-05 | **Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs**<br><sub>Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani</sub> | [arXiv](https://arxiv.org/abs/2611.07988) · [PDF](https://arxiv.org/pdf/2611.07988) |
| 2026-11-05 | **Flux as a Codec: Zero-Shot Lossy Compression with Flux**<br><sub>Fuma Kimishima, Jinjia Zhou</sub> | [arXiv](https://arxiv.org/abs/2611.07929) · [PDF](https://arxiv.org/pdf/2611.07929) |
| 2026-11-05 | **EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure**<br><sub>Kwan Yun, Minhyeok Bang, Colette Suhjung Koo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07909) · [PDF](https://arxiv.org/pdf/2611.07909) |
| 2026-11-05 | **Reinforcing What the Student Has Learned: Teacher-Guided On-Policy Distillation**<br><sub>Bozhen Fang, Linhao Zhong, Xuehao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07722) · [PDF](https://arxiv.org/pdf/2611.07722) · [Code](https://github.com/aim-uofa/sd-opd) |
| 2026-11-05 | **FisherDistill: Diffusion Distribution Distillation via Closed-Form Fisher Critics**<br><sub>Mahesh Bhosale, Yuanhao Zhai, Siwei Lyu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07604) · [PDF](https://arxiv.org/pdf/2611.07604) |
| 2026-11-05 | **Guidance Is a Field, Not a Scalar: Interval-Integrated Classifier-Free Guidance for One-Step Video Generation**<br><sub>Zijie Meng, Xixin Cao</sub> | [arXiv](https://arxiv.org/abs/2611.07566) · [PDF](https://arxiv.org/pdf/2611.07566) · [Code](https://github.com/YMlinfeng/AGAVE) |
| 2026-11-05 | **Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion**<br><sub>Jia Li, Xurui Peng, Xing Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07551) · [PDF](https://arxiv.org/pdf/2611.07551) |
| 2026-11-05 | **CST-Bench: Benchmarking Counterfactual Spatial Transition Reasoning with Causal Transition On-Policy Self-Distillation**<br><sub>Ying Li, Yongle Cheng, Jing Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07541) · [PDF](https://arxiv.org/pdf/2611.07541) |
| 2026-11-04 | **Depth or Description? When a One-Step Latent Score Replaces Lookahead in Proactive Information Acquisition**<br><sub>Biswa Sengupta</sub> | [arXiv](https://arxiv.org/abs/2611.07155) · [PDF](https://arxiv.org/pdf/2611.07155) |
| 2026-11-04 | **SD-LoRA: Training-Time Structural Distillation into LoRA for Few-Shot Vision-Language Adaptation**<br><sub>Mohammed Rahman Sherif Khan Mohammad, Ardhendu Behera, Sandip Pradhan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07063) · [PDF](https://arxiv.org/pdf/2611.07063) · [Code](https://github.com/MR-Sherif/SD-LoRA.git) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **167 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **Towards interpreting any residual stream direction by scaling activation inversion**<br><sub>Celeste De Schamphelaere, Juan J. Vazquez, Ari Spiesberger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08465) · [PDF](https://arxiv.org/pdf/2611.08465) |
| 2026-11-05 | **Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval**<br><sub>Dohoon Kim, Junho Park, Hyunwoong Bae et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07820) · [PDF](https://arxiv.org/pdf/2611.07820) · [Code](https://github.com/dohoonkim-ai/axis-lora) |
| 2026-11-05 | **Embedding-Space Fingerprinting of LoRA Fine-Tunes: Recovering the Training-Data Domain from the Model Artifact Alone**<br><sub>Shivesh Rane</sub> | [arXiv](https://arxiv.org/abs/2611.07610) · [PDF](https://arxiv.org/pdf/2611.07610) |
| 2026-11-05 | **Align Before Aggregation: Basis-Consistent Federated LoRA under Heterogeneous Ranks**<br><sub>Pengpeng Qiao, Yang Cao, Lingling Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07598) · [PDF](https://arxiv.org/pdf/2611.07598) |
| 2026-11-05 | **OptIMerge: Optimization-Based Merging of Diffusion Models**<br><sub>Viraj Shah, Ashwini Pokle, Peyman Milanfar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07543) · [PDF](https://arxiv.org/pdf/2611.07543) |
| 2026-11-04 | **DMuon: Scaling Matrix Optimizers in Data Parallelism with Topology-Aware Matrix Ownership and Communication**<br><sub>Starrick Liu, Ruizhi Chengze, Lufang Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07084) · [PDF](https://arxiv.org/pdf/2611.07084) · [Code](https://github.com/X-Square-Robot/dmuon) |
| 2026-11-04 | **SD-LoRA: Training-Time Structural Distillation into LoRA for Few-Shot Vision-Language Adaptation**<br><sub>Mohammed Rahman Sherif Khan Mohammad, Ardhendu Behera, Sandip Pradhan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07063) · [PDF](https://arxiv.org/pdf/2611.07063) · [Code](https://github.com/MR-Sherif/SD-LoRA.git) |
| 2026-11-04 | **The Behavioral Rate of Fine-Tuning: Compression as a Measure of Useful Information**<br><sub>Joey David, Paul Caillon, Alexandre Allauzen</sub> | [arXiv](https://arxiv.org/abs/2611.06598) · [PDF](https://arxiv.org/pdf/2611.06598) |
| 2026-11-04 | **AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment**<br><sub>Pragyan Phukan</sub> | [arXiv](https://arxiv.org/abs/2611.06170) · [PDF](https://arxiv.org/pdf/2611.06170) |
| 2026-11-04 | **CARE-FL: Federated Fine-Tuning of Multimodal LLMs in Resource-Constrained Edge Networks**<br><sub>Tianqi Zong, Baosheng Li, Nuocheng Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06169) · [PDF](https://arxiv.org/pdf/2611.06169) |
| 2026-11-04 | **UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence**<br><sub>Mingkang Liu, Peipei Jiao, Weiming Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06075) · [PDF](https://arxiv.org/pdf/2611.06075) |
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **234 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference**<br><sub>Jake Hyun, Ziyu Zhao, Jae-sun Seo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) |
| 2026-11-05 | **Beyond K/V Caches: Cross-Model State Handoff in Hybrid Linear-Attention LLMs**<br><sub>Jiacheng Cai, Tao Zhang, Siqi Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08133) · [PDF](https://arxiv.org/pdf/2611.08133) |
| 2026-11-05 | **QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents**<br><sub>Yingjie Tan, Haiquan Qiu, Quanming Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07976) · [PDF](https://arxiv.org/pdf/2611.07976) |
| 2026-11-05 | **TACT-KV: Tri-Axis Cosine Transform for Compressing Volumetric KV Caches in Medical VLMs**<br><sub>Chongyu Qu, Ritchie Zhao, Yufan He et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07593) · [PDF](https://arxiv.org/pdf/2611.07593) |
| 2026-11-05 | **FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving**<br><sub>Xuan Wang, Zhuanhao Wu, Tingzhu Fang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07542) · [PDF](https://arxiv.org/pdf/2611.07542) · [Code](https://github.com/vllm-project/vllm-ascend/tree/releases/v0.30.0) |
| 2026-11-05 | **TriAttention: Unified Sparse Mixed-Precision Attention for Long-Context LLM Inference**<br><sub>Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07256) · [PDF](https://arxiv.org/pdf/2611.07256) · [Code](https://github.com/HanzhiZhang-Ulrica/TriAttention) |
| 2026-11-04 | **Tools Need Not Speak in Text: Latent Context Compression for Agents**<br><sub>Yuetong Liu, Zhehao Zhou, Yitong Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06500) · [PDF](https://arxiv.org/pdf/2611.06500) · [Code](https://github.com/THU-Agent/Coca-cola) |
| 2026-11-04 | **SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory**<br><sub>Jizhe Zhang, Ang Li, Chenheng Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06445) · [PDF](https://arxiv.org/pdf/2611.06445) |
| 2026-11-04 | **Does Context Compression Preserve Refusal Alignment?**<br><sub>Anthony Nguyen, Wenjun Lin</sub> | [arXiv](https://arxiv.org/abs/2611.06380) · [PDF](https://arxiv.org/pdf/2611.06380) |
| 2026-11-04 | **NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation**<br><sub>Jiacheng Lu, Haoyi Zhu, Sipei Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06377) · [PDF](https://arxiv.org/pdf/2611.06377) · [Code](https://github.com/jiacheng-lu03/NanoKV) |
| 2026-11-04 | **Accelerating Long-Context Decoding in Large-Scale Hybrid LLMs Without Retraining**<br><sub>João Eduardo Batista, Emil Vatai, Mohamed Wahib</sub> | [arXiv](https://arxiv.org/abs/2611.06133) · [PDF](https://arxiv.org/pdf/2611.06133) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **155 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **Measured Coupling for Parallel Decoding in Diffusion Language Models**<br><sub>Tal Oved, Lior Wolf</sub> | [arXiv](https://arxiv.org/abs/2611.08307) · [PDF](https://arxiv.org/pdf/2611.08307) |
| 2026-11-05 | **Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding**<br><sub>Adrian Baule</sub> | [arXiv](https://arxiv.org/abs/2611.07845) · [PDF](https://arxiv.org/pdf/2611.07845) |
| 2026-11-05 | **FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving**<br><sub>Xuan Wang, Zhuanhao Wu, Tingzhu Fang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07542) · [PDF](https://arxiv.org/pdf/2611.07542) · [Code](https://github.com/vllm-project/vllm-ascend/tree/releases/v0.30.0) |
| 2026-11-05 | **Latency-Aware Adaptive Best-of-$N$**<br><sub>Alon Jacobson, Qian Xie, Peter I. Frazier</sub> | [arXiv](https://arxiv.org/abs/2611.07453) · [PDF](https://arxiv.org/pdf/2611.07453) |
| 2026-11-05 | **Test-Time Self-Play: Scaling without a Verifier**<br><sub>Akira Yoshiyama, Akmal Ashirmatov, Jonas Hübotter et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07367) · [PDF](https://arxiv.org/pdf/2611.07367) |
| 2026-11-04 | **D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding**<br><sub>Baoyou Chen, Ruiqiao Mei, Guancong Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06425) · [PDF](https://arxiv.org/pdf/2611.06425) · [Code](https://github.com/fudan-generative-vision/D3D) |
| 2026-11-04 | **Give Up to Get More: Priors, Not Policies, Govern Test-Time Compute Allocation**<br><sub>Jinhyung Bae</sub> | [arXiv](https://arxiv.org/abs/2611.06372) · [PDF](https://arxiv.org/pdf/2611.06372) · [Code](https://github.com/nepersoned/priors-not-policies) |
| 2026-11-04 | **Split-KV: Efficient Context Parallelism for Training Diffusion Drafters**<br><sub>Geng Zhang, Fangzhao Zhang, Cong Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05926) · [PDF](https://arxiv.org/pdf/2611.05926) · [Code](https://github.com/zxgx/verl) |
| 2026-11-04 | **RECAP: Context-Aware Prediction Recycling with Request-Local and Persistent Memories for Multimodal Speculative Decoding**<br><sub>Hengjie Zhu, Dayan Wu, Xinze Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05894) · [PDF](https://arxiv.org/pdf/2611.05894) · [Code](https://github.com/Senmo996/RECAP-official-code) |
| 2026-11-03 | **Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding**<br><sub>Hoang Anh Duy Le, Huibing Dong, Alireza Khadem et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05724) · [PDF](https://arxiv.org/pdf/2611.05724) |
| 2026-11-03 | **Hybrid Spark: Adaptive Speculative Decoding That Lets the Content Choose the Drafter**<br><sub>Ekagra Ranjan, Bharat Venkitesh</sub> | [arXiv](https://arxiv.org/abs/2611.05611) · [PDF](https://arxiv.org/pdf/2611.05611) |
| 2026-11-03 | **PATTS: Parallel-Aware Test-Time Scaling for Thought-Image Generation in Multimodal Discrete Diffusion LLMs**<br><sub>Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04948) · [PDF](https://arxiv.org/pdf/2611.04948) · [Code](https://github.com/Ringo-Star/PATTS.git) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **259 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference**<br><sub>Jake Hyun, Ziyu Zhao, Jae-sun Seo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) |
| 2026-11-05 | **Should You Split Decode? Disaggregation Across Future Models and Accelerators**<br><sub>Ramyad Hadidi</sub> | [arXiv](https://arxiv.org/abs/2611.08299) · [PDF](https://arxiv.org/pdf/2611.08299) |
| 2026-11-05 | **AutoCompress: Automated Hardware-Guided Model Compression**<br><sub>Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08290) · [PDF](https://arxiv.org/pdf/2611.08290) |
| 2026-11-05 | **ACSeL: Adaptive Configuration Search for Hardware-Constrained LLM Inference**<br><sub>Bokun Wang, Hung-Yueh Chiang, Diana Marculescu</sub> | [arXiv](https://arxiv.org/abs/2611.07570) · [PDF](https://arxiv.org/pdf/2611.07570) |
| 2026-11-05 | **FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving**<br><sub>Xuan Wang, Zhuanhao Wu, Tingzhu Fang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07542) · [PDF](https://arxiv.org/pdf/2611.07542) · [Code](https://github.com/vllm-project/vllm-ascend/tree/releases/v0.30.0) |
| 2026-11-05 | **Latency-Aware Adaptive Best-of-$N$**<br><sub>Alon Jacobson, Qian Xie, Peter I. Frazier</sub> | [arXiv](https://arxiv.org/abs/2611.07453) · [PDF](https://arxiv.org/pdf/2611.07453) |
| 2026-11-04 | **ServerBench: How can your coding agents design specialized LLM serving systems?**<br><sub>Xinrui Zhong, Zhiming Wang, Yongqi Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06841) · [PDF](https://arxiv.org/pdf/2611.06841) |
| 2026-11-04 | **Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism**<br><sub>Jia Wei, Ziyi Qiu, Yi Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06984) · [PDF](https://arxiv.org/pdf/2611.06984) |
| 2026-11-04 | **SafeStart: Mitigating the Overlooked Safety Cost of Active Expert Reduction in MoE LLM Serving**<br><sub>Erfan Baghaei Potraghloo, Saeid Shokoufa, Seyedarmin Azizi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06147) · [PDF](https://arxiv.org/pdf/2611.06147) |
| 2026-11-04 | **A Controlled Experimental Evaluation of Configuration and Cache Architecture in LLM Serving Engines**<br><sub>Muhammad Faizan Anwar, Sina Keshvadi</sub> | [arXiv](https://arxiv.org/abs/2611.05991) · [PDF](https://arxiv.org/pdf/2611.05991) · [Code](https://github.com/FaizanAnwar01/llm-serving-config-eval) |
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **What Sets the Serving Speed of Looped Language Models? Measurements and Optimizations Graded by Exactness**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05150) · [PDF](https://arxiv.org/pdf/2611.05150) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **126 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |
| 2026-11-03 | **Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation**<br><sub>Rohan Agarwal, Robin Andeer, Alex Armbruster et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05642) · [PDF](https://arxiv.org/pdf/2611.05642) |
| 2026-11-02 | **Denoising Is Stein: Moment Access and a Resource Hierarchy for Learning Hidden Structure in Diffusion Models**<br><sub>Rui Wang</sub> | [arXiv](https://arxiv.org/abs/2611.04043) · [PDF](https://arxiv.org/pdf/2611.04043) |
| 2026-11-01 | **Z-Cache: Accelerating Diffusion Transformers via Self-Reflection**<br><sub>Zegang Cheng, Zhikai Wang, Jiacheng Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01846) · [PDF](https://arxiv.org/pdf/2611.01846) |
| 2026-10-31 | **Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference**<br><sub>Zhichen Zeng, Xichong Zhang, Junpan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01320) · [PDF](https://arxiv.org/pdf/2611.01320) |
| 2026-10-31 | **Accelerating posterior sampling in Bayesian inverse problems with diffusion models: an online-offline perspective**<br><sub>Duc-Lam Duong</sub> | [arXiv](https://arxiv.org/abs/2611.01300) · [PDF](https://arxiv.org/pdf/2611.01300) |
| 2026-10-31 | **Wave Forcing: Towards Speed-of-Light Streaming Video Generation**<br><sub>Yijie Jin, Yuxuan Liu, Jiajun Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00859) · [PDF](https://arxiv.org/pdf/2611.00859) |
| 2026-10-30 | **CLiS: Plug-and-Play Attention Acceleration for Video Diffusion on TPUs via Certified Stabilization**<br><sub>Elisa Tsai, Shao-yu Huang, Daniel Mandragona et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00444) · [PDF](https://arxiv.org/pdf/2611.00444) |
| 2026-10-29 | **No Channels Left Behind: Understanding Diffusion Acceleration through Residual Gates**<br><sub>Junha Park, Jaemyung Yu, Jaehui Hwang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40914) · [PDF](https://arxiv.org/pdf/2610.40914) · [Code](https://github.com/naver-ai/radialobj) |
| 2026-10-29 | **UniRA: Unified Representation Alignment and Auto-Encoding for Efficient Diffusion Generation**<br><sub>An Lanji, Dawei Liu, Jin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39948) · [PDF](https://arxiv.org/pdf/2610.39948) |
| 2026-10-29 | **KV Cache Quantization for Diffusion Language Models**<br><sub>Yan Tai, Yunan Ding, Guangzhao Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **213 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **FisherDistill: Diffusion Distribution Distillation via Closed-Form Fisher Critics**<br><sub>Mahesh Bhosale, Yuanhao Zhai, Siwei Lyu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07604) · [PDF](https://arxiv.org/pdf/2611.07604) |
| 2026-11-05 | **Guidance Is a Field, Not a Scalar: Interval-Integrated Classifier-Free Guidance for One-Step Video Generation**<br><sub>Zijie Meng, Xixin Cao</sub> | [arXiv](https://arxiv.org/abs/2611.07566) · [PDF](https://arxiv.org/pdf/2611.07566) · [Code](https://github.com/YMlinfeng/AGAVE) |
| 2026-11-05 | **Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion**<br><sub>Jia Li, Xurui Peng, Xing Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07551) · [PDF](https://arxiv.org/pdf/2611.07551) |
| 2026-11-05 | **OptIMerge: Optimization-Based Merging of Diffusion Models**<br><sub>Viraj Shah, Ashwini Pokle, Peyman Milanfar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07543) · [PDF](https://arxiv.org/pdf/2611.07543) |
| 2026-11-04 | **VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation**<br><sub>Yihong Luo, Tianyu Pang, Tianyang Hu</sub> | [arXiv](https://arxiv.org/abs/2611.06796) · [PDF](https://arxiv.org/pdf/2611.06796) · [Code](https://github.com/Luo-Yihong/VA-TDM) |
| 2026-11-04 | **NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation**<br><sub>Jiacheng Lu, Haoyi Zhu, Sipei Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06377) · [PDF](https://arxiv.org/pdf/2611.06377) · [Code](https://github.com/jiacheng-lu03/NanoKV) |
| 2026-11-04 | **NextGAN: Towards Simple and Scalable GAN Training for Image and Video Generation**<br><sub>Xinhao Lou, Dongye Xie, Peng Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06270) · [PDF](https://arxiv.org/pdf/2611.06270) · [Code](https://github.com/LINs-lab/NextGAN.git) |
| 2026-11-04 | **Learning Noise Optimization for Reward Alignment in Few-Step Generative Models**<br><sub>Hongeun Kim, Jeongsol Kim, Jong Chul Ye</sub> | [arXiv](https://arxiv.org/abs/2611.06255) · [PDF](https://arxiv.org/pdf/2611.06255) |
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |
| 2026-11-03 | **Decompose the Distillation: Interpretable Single-Pass Guidance for Diffusion Models**<br><sub>Wuyang Zhang, Xiaolin Xu</sub> | [arXiv](https://arxiv.org/abs/2611.05755) · [PDF](https://arxiv.org/pdf/2611.05755) |
| 2026-11-03 | **Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation**<br><sub>Rohan Agarwal, Robin Andeer, Alex Armbruster et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05642) · [PDF](https://arxiv.org/pdf/2611.05642) |

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
