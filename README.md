# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-09 16:00 CST** · **1603 unique papers** · Newest submission: **2026-11-06**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 256 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 231 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 512 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 171 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 243 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 156 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 267 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 127 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 215 |

## Newly indexed · 2026-11-09

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design**<br><sub>Dayou Du, Woon Yee Ng, Guangming Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09825) · [PDF](https://arxiv.org/pdf/2611.09825) · [Code](https://github.com/OpenBitSys/BitDecoding-FP4) |
| 2026-11-06 | **FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding**<br><sub>Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09722) · [PDF](https://arxiv.org/pdf/2611.09722) · [Code](https://github.com/FutureMLS-Lab/FOSCAR) |
| 2026-11-06 | **Intent-Aware Caching for Efficient LLM Serving**<br><sub>Kazi Hasan Ibn Arif, JinYi Yoon, Dimitrios S. Nikolopoulos et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09715) · [PDF](https://arxiv.org/pdf/2611.09715) · [Code](https://github.com/hasanar1f/intent-aware-caching) |
| 2026-11-06 | **Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure**<br><sub>Wajih Hassan Raza, Ahsan Bilal, Yidan Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09700) · [PDF](https://arxiv.org/pdf/2611.09700) |
| 2026-11-06 | **Verifier Noise Is a Temperature: Testing Tilt Predictions in Finite-Budget LLM-Guided Search**<br><sub>Xiaomeng Li</sub> | [arXiv](https://arxiv.org/abs/2611.09699) · [PDF](https://arxiv.org/pdf/2611.09699) |
| 2026-11-06 | **Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters**<br><sub>Constantinos Karouzos, Nikolaos Aletras</sub> | [arXiv](https://arxiv.org/abs/2611.09634) · [PDF](https://arxiv.org/pdf/2611.09634) |
| 2026-11-06 | **Know What You Need: Efficient Activation Checkpointing**<br><sub>Danyal Ahmed, Edouard Oyallon</sub> | [arXiv](https://arxiv.org/abs/2611.09614) · [PDF](https://arxiv.org/pdf/2611.09614) |
| 2026-11-06 | **Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression**<br><sub>Andras Szecsenyi, Thomas L. Lee, Vaisakh Shaj et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09598) · [PDF](https://arxiv.org/pdf/2611.09598) |
| 2026-11-06 | **Nebula: Distributed Position-Independent Caching for LLM Serving**<br><sub>Yifei Liu, Junbin Pan, Junhao Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09474) · [PDF](https://arxiv.org/pdf/2611.09474) |
| 2026-11-06 | **From LoRA to Language: Recovering Skill Documents from Adapters**<br><sub>Saranya Dintakurthy Swadha, Pavan C Shekar, Arpit Jain et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09454) · [PDF](https://arxiv.org/pdf/2611.09454) |
| 2026-11-06 | **MINE: Entropy-coded Memory-efficient Inference for Large Language Models**<br><sub>Emil Schätzle, Markus Püschel</sub> | [arXiv](https://arxiv.org/abs/2611.09424) · [PDF](https://arxiv.org/pdf/2611.09424) |
| 2026-11-06 | **TwinHash: Two-Sided Object Identity Management for Time- and Energy-Efficient Agentic Workflows**<br><sub>Sangbu Yun, Jung Gyu Min, Jin Hyun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09254) · [PDF](https://arxiv.org/pdf/2611.09254) |
| 2026-11-06 | **DUET: Dual-Sparse Inference for Block Diffusion Language Models**<br><sub>Siyuan Yan, Shen Gu, Xiaoxing Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09239) · [PDF](https://arxiv.org/pdf/2611.09239) |
| 2026-11-06 | **Cross-Layer TopK: Dynamically Allocating Sparsity Across Layers in Transcoders**<br><sub>Anyuan Zhuo, Shaohua Zhang, Tianle Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09233) · [PDF](https://arxiv.org/pdf/2611.09233) · [Code](https://huggingface.co/ByteDance-Seed/Cross-Layer-TopK-CLT) |
| 2026-11-06 | **UniExit: A Unified Latency-Aware Early-Exit Runtime for Heterogeneous Edge AI**<br><sub>Yuhang Guan, Huanle Zhang, Xiaomin Ouyang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09159) · [PDF](https://arxiv.org/pdf/2611.09159) |
| 2026-11-06 | **DARIC: A Position-Independent KV Cache Reuse System with Distribution-Aware Recomputation**<br><sub>Weikang Wang, Haiyang Liu, Xin Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09109) · [PDF](https://arxiv.org/pdf/2611.09109) · [Code](https://github.com/Lenovo-ICI/DARIC) |
| 2026-11-06 | **Emo-LiveSync: Real-Time Universal Lip Synchronization with Explicit Emotion Control**<br><sub>Sangjoon Yu, Seungeun Lee, JoonHeyok Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09074) · [PDF](https://arxiv.org/pdf/2611.09074) |
| 2026-11-06 | **Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation**<br><sub>Yijun Zhu, Jianxin Wang, Chengchao Shen</sub> | [arXiv](https://arxiv.org/abs/2611.09042) · [PDF](https://arxiv.org/pdf/2611.09042) · [Code](https://github.com/visresearch/FPRT) |
| 2026-11-06 | **ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization Aware Training**<br><sub>Liqun Ma, Shengkun Tang, Liangyu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08924) · [PDF](https://arxiv.org/pdf/2611.08924) |
| 2026-11-06 | **Inside the Trap: A Renewal Law for Prefix-Cache Collapse in LLM Agent Serving**<br><sub>Akshat Valse, Ali Jannesari</sub> | [arXiv](https://arxiv.org/abs/2611.08902) · [PDF](https://arxiv.org/pdf/2611.08902) |

[View all 27 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **256 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design**<br><sub>Dayou Du, Woon Yee Ng, Guangming Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09825) · [PDF](https://arxiv.org/pdf/2611.09825) · [Code](https://github.com/OpenBitSys/BitDecoding-FP4) |
| 2026-11-06 | **FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding**<br><sub>Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09722) · [PDF](https://arxiv.org/pdf/2611.09722) · [Code](https://github.com/FutureMLS-Lab/FOSCAR) |
| 2026-11-06 | **MINE: Entropy-coded Memory-efficient Inference for Large Language Models**<br><sub>Emil Schätzle, Markus Püschel</sub> | [arXiv](https://arxiv.org/abs/2611.09424) · [PDF](https://arxiv.org/pdf/2611.09424) |
| 2026-11-06 | **ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization Aware Training**<br><sub>Liqun Ma, Shengkun Tang, Liangyu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08924) · [PDF](https://arxiv.org/pdf/2611.08924) |
| 2026-11-05 | **ResServe: Accurate and Efficient FP4 LLM Inference with Residue Compensation**<br><sub>Shuo Rong, Ruibo Fan, Jiawen Wen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08713) · [PDF](https://arxiv.org/pdf/2611.08713) · [Code](https://github.com/ShawRong/resserve) |
| 2026-11-05 | **StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference**<br><sub>Jake Hyun, Ziyu Zhao, Jae-sun Seo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) |
| 2026-11-05 | **ProQuant: Progressive Quantization-aware Training for Edge MLLMs**<br><sub>Yufei Xue, Yushi Huang, Jiawei Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08216) · [PDF](https://arxiv.org/pdf/2611.08216) · [Code](https://github.com/yufeixue-ai/ProQuant/) |
| 2026-11-05 | **Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs**<br><sub>Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani</sub> | [arXiv](https://arxiv.org/abs/2611.07988) · [PDF](https://arxiv.org/pdf/2611.07988) |
| 2026-11-05 | **When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale**<br><sub>Gautam Gupta, Dikshant Kukreja, Unique Kumar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07891) · [PDF](https://arxiv.org/pdf/2611.07891) |
| 2026-11-05 | **TACT-KV: Tri-Axis Cosine Transform for Compressing Volumetric KV Caches in Medical VLMs**<br><sub>Chongyu Qu, Ritchie Zhao, Yufan He et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07593) · [PDF](https://arxiv.org/pdf/2611.07593) |
| 2026-11-05 | **ACSeL: Adaptive Configuration Search for Hardware-Constrained LLM Inference**<br><sub>Bokun Wang, Hung-Yueh Chiang, Diana Marculescu</sub> | [arXiv](https://arxiv.org/abs/2611.07570) · [PDF](https://arxiv.org/pdf/2611.07570) |
| 2026-11-05 | **TriAttention: Unified Sparse Mixed-Precision Attention for Long-Context LLM Inference**<br><sub>Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07256) · [PDF](https://arxiv.org/pdf/2611.07256) · [Code](https://github.com/HanzhiZhang-Ulrica/TriAttention) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **231 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **DUET: Dual-Sparse Inference for Block Diffusion Language Models**<br><sub>Siyuan Yan, Shen Gu, Xiaoxing Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09239) · [PDF](https://arxiv.org/pdf/2611.09239) |
| 2026-11-06 | **Cross-Layer TopK: Dynamically Allocating Sparsity Across Layers in Transcoders**<br><sub>Anyuan Zhuo, Shaohua Zhang, Tianle Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09233) · [PDF](https://arxiv.org/pdf/2611.09233) · [Code](https://huggingface.co/ByteDance-Seed/Cross-Layer-TopK-CLT) |
| 2026-11-06 | **UniExit: A Unified Latency-Aware Early-Exit Runtime for Heterogeneous Edge AI**<br><sub>Yuhang Guan, Huanle Zhang, Xiaomin Ouyang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09159) · [PDF](https://arxiv.org/pdf/2611.09159) |
| 2026-11-06 | **GeoJeV: Unified Spatial Probability for Training-Free Efficient Evidence Acquisition in Ultra-High-Resolution Remote Sensing**<br><sub>Xinyi Niu, Lingfeng Chen, Jiehua Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08879) · [PDF](https://arxiv.org/pdf/2611.08879) |
| 2026-11-05 | **T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models**<br><sub>Mohammed Hassan, Zhenyang Chen, Zheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08413) · [PDF](https://arxiv.org/pdf/2611.08413) |
| 2026-11-05 | **AutoCompress: Automated Hardware-Guided Model Compression**<br><sub>Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08290) · [PDF](https://arxiv.org/pdf/2611.08290) |
| 2026-11-05 | **When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale**<br><sub>Gautam Gupta, Dikshant Kukreja, Unique Kumar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07891) · [PDF](https://arxiv.org/pdf/2611.07891) |
| 2026-11-05 | **SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking**<br><sub>Moonseok Choi, Jongwon Jeong, Minki Kang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07558) · [PDF](https://arxiv.org/pdf/2611.07558) |
| 2026-11-05 | **Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion**<br><sub>Jia Li, Xurui Peng, Xing Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07551) · [PDF](https://arxiv.org/pdf/2611.07551) |
| 2026-11-05 | **TriAttention: Unified Sparse Mixed-Precision Attention for Long-Context LLM Inference**<br><sub>Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07256) · [PDF](https://arxiv.org/pdf/2611.07256) · [Code](https://github.com/HanzhiZhang-Ulrica/TriAttention) |
| 2026-11-04 | **Tools Need Not Speak in Text: Latent Context Compression for Agents**<br><sub>Yuetong Liu, Zhehao Zhou, Yitong Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06500) · [PDF](https://arxiv.org/pdf/2611.06500) · [Code](https://github.com/THU-Agent/Coca-cola) |
| 2026-11-04 | **RI-Prune: Relation and Information Aware Visual Token Pruning for Multi-Image Vision-Language Models**<br><sub>Dongjin Lee, Eunju Lee, Jinhee Jang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06047) · [PDF](https://arxiv.org/pdf/2611.06047) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **512 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **Emo-LiveSync: Real-Time Universal Lip Synchronization with Explicit Emotion Control**<br><sub>Sangjoon Yu, Seungeun Lee, JoonHeyok Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09074) · [PDF](https://arxiv.org/pdf/2611.09074) |
| 2026-11-06 | **Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation**<br><sub>Yijun Zhu, Jianxin Wang, Chengchao Shen</sub> | [arXiv](https://arxiv.org/abs/2611.09042) · [PDF](https://arxiv.org/pdf/2611.09042) · [Code](https://github.com/visresearch/FPRT) |
| 2026-11-05 | **ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding**<br><sub>Selim Aktas, Yusuf Erdem Erdem, Ahmed Zeer et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08669) · [PDF](https://arxiv.org/pdf/2611.08669) |
| 2026-11-05 | **FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning**<br><sub>Haitao Lin, Minsi Ren, Yang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08240) · [PDF](https://arxiv.org/pdf/2611.08240) |
| 2026-11-05 | **Learning Dynamics of On-Policy Distillation**<br><sub>Guan Zhe Hong, Sumeet Ramesh Motwani, Liang Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08016) · [PDF](https://arxiv.org/pdf/2611.08016) |
| 2026-11-05 | **Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs**<br><sub>Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani</sub> | [arXiv](https://arxiv.org/abs/2611.07988) · [PDF](https://arxiv.org/pdf/2611.07988) |
| 2026-11-05 | **Flux as a Codec: Zero-Shot Lossy Compression with Flux**<br><sub>Fuma Kimishima, Jinjia Zhou</sub> | [arXiv](https://arxiv.org/abs/2611.07929) · [PDF](https://arxiv.org/pdf/2611.07929) |
| 2026-11-05 | **EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure**<br><sub>Kwan Yun, Minhyeok Bang, Colette Suhjung Koo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07909) · [PDF](https://arxiv.org/pdf/2611.07909) |
| 2026-11-05 | **Reinforcing What the Student Has Learned: Teacher-Guided On-Policy Distillation**<br><sub>Bozhen Fang, Linhao Zhong, Xuehao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07722) · [PDF](https://arxiv.org/pdf/2611.07722) · [Code](https://github.com/aim-uofa/sd-opd) |
| 2026-11-05 | **FisherDistill: Diffusion Distribution Distillation via Closed-Form Fisher Critics**<br><sub>Mahesh Bhosale, Yuanhao Zhai, Siwei Lyu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07604) · [PDF](https://arxiv.org/pdf/2611.07604) |
| 2026-11-05 | **Guidance Is a Field, Not a Scalar: Interval-Integrated Classifier-Free Guidance for One-Step Video Generation**<br><sub>Zijie Meng, Xixin Cao</sub> | [arXiv](https://arxiv.org/abs/2611.07566) · [PDF](https://arxiv.org/pdf/2611.07566) · [Code](https://github.com/YMlinfeng/AGAVE) |
| 2026-11-05 | **Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion**<br><sub>Jia Li, Xurui Peng, Xing Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07551) · [PDF](https://arxiv.org/pdf/2611.07551) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **171 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters**<br><sub>Constantinos Karouzos, Nikolaos Aletras</sub> | [arXiv](https://arxiv.org/abs/2611.09634) · [PDF](https://arxiv.org/pdf/2611.09634) |
| 2026-11-06 | **Know What You Need: Efficient Activation Checkpointing**<br><sub>Danyal Ahmed, Edouard Oyallon</sub> | [arXiv](https://arxiv.org/abs/2611.09614) · [PDF](https://arxiv.org/pdf/2611.09614) |
| 2026-11-06 | **From LoRA to Language: Recovering Skill Documents from Adapters**<br><sub>Saranya Dintakurthy Swadha, Pavan C Shekar, Arpit Jain et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09454) · [PDF](https://arxiv.org/pdf/2611.09454) |
| 2026-11-06 | **ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization Aware Training**<br><sub>Liqun Ma, Shengkun Tang, Liangyu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08924) · [PDF](https://arxiv.org/pdf/2611.08924) |
| 2026-11-05 | **Towards interpreting any residual stream direction by scaling activation inversion**<br><sub>Celeste De Schamphelaere, Juan J. Vazquez, Ari Spiesberger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08465) · [PDF](https://arxiv.org/pdf/2611.08465) |
| 2026-11-05 | **Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval**<br><sub>Dohoon Kim, Junho Park, Hyunwoong Bae et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07820) · [PDF](https://arxiv.org/pdf/2611.07820) · [Code](https://github.com/dohoonkim-ai/axis-lora) |
| 2026-11-05 | **Embedding-Space Fingerprinting of LoRA Fine-Tunes: Recovering the Training-Data Domain from the Model Artifact Alone**<br><sub>Shivesh Rane</sub> | [arXiv](https://arxiv.org/abs/2611.07610) · [PDF](https://arxiv.org/pdf/2611.07610) |
| 2026-11-05 | **Align Before Aggregation: Basis-Consistent Federated LoRA under Heterogeneous Ranks**<br><sub>Pengpeng Qiao, Yang Cao, Lingling Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07598) · [PDF](https://arxiv.org/pdf/2611.07598) |
| 2026-11-05 | **OptIMerge: Optimization-Based Merging of Diffusion Models**<br><sub>Viraj Shah, Ashwini Pokle, Peyman Milanfar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07543) · [PDF](https://arxiv.org/pdf/2611.07543) |
| 2026-11-04 | **DMuon-2: Scaling Matrix Optimizers in Data Parallelism with Topology-Aware Matrix Ownership and Communication**<br><sub>Starrick Liu, Ruizhi Chengze, Lufang Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07084) · [PDF](https://arxiv.org/pdf/2611.07084) · [Code](https://github.com/X-Square-Robot/dmuon) |
| 2026-11-04 | **SD-LoRA: Training-Time Structural Distillation into LoRA for Few-Shot Vision-Language Adaptation**<br><sub>Mohammed Rahman Sherif Khan Mohammad, Ardhendu Behera, Sandip Pradhan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07063) · [PDF](https://arxiv.org/pdf/2611.07063) · [Code](https://github.com/MR-Sherif/SD-LoRA.git) |
| 2026-11-04 | **The Behavioral Rate of Fine-Tuning: Compression as a Measure of Useful Information**<br><sub>Joey David, Paul Caillon, Alexandre Allauzen</sub> | [arXiv](https://arxiv.org/abs/2611.06598) · [PDF](https://arxiv.org/pdf/2611.06598) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **243 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design**<br><sub>Dayou Du, Woon Yee Ng, Guangming Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09825) · [PDF](https://arxiv.org/pdf/2611.09825) · [Code](https://github.com/OpenBitSys/BitDecoding-FP4) |
| 2026-11-06 | **FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding**<br><sub>Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09722) · [PDF](https://arxiv.org/pdf/2611.09722) · [Code](https://github.com/FutureMLS-Lab/FOSCAR) |
| 2026-11-06 | **Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure**<br><sub>Wajih Hassan Raza, Ahsan Bilal, Yidan Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09700) · [PDF](https://arxiv.org/pdf/2611.09700) |
| 2026-11-06 | **Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression**<br><sub>Andras Szecsenyi, Thomas L. Lee, Vaisakh Shaj et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09598) · [PDF](https://arxiv.org/pdf/2611.09598) |
| 2026-11-06 | **Nebula: Distributed Position-Independent Caching for LLM Serving**<br><sub>Yifei Liu, Junbin Pan, Junhao Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09474) · [PDF](https://arxiv.org/pdf/2611.09474) |
| 2026-11-06 | **DARIC: A Position-Independent KV Cache Reuse System with Distribution-Aware Recomputation**<br><sub>Weikang Wang, Haiyang Liu, Xin Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09109) · [PDF](https://arxiv.org/pdf/2611.09109) · [Code](https://github.com/Lenovo-ICI/DARIC) |
| 2026-11-05 | **AttentionSwitch: Jailbreak Defense for LLMs via Joint Learning of Sparse Attention-Head Selection and Scaling**<br><sub>Doniyorkhon Obidov, Honggang Yu, Xiaolong Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08752) · [PDF](https://arxiv.org/pdf/2611.08752) |
| 2026-11-05 | **InstaGen: Group-Shared Importance Sampling for Fast Video Generation**<br><sub>Kislay Aditya Oj, Kumar Krishna Agrawal, Sri Surya Varma Datla et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08610) · [PDF](https://arxiv.org/pdf/2611.08610) |
| 2026-11-05 | **Just CaloCHILL: fast hadronic shower generation in a learned latent space**<br><sub>Henry Day-Hall, Frank Gaede, Gregor Kasieczka et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08606) · [PDF](https://arxiv.org/pdf/2611.08606) · [Code](https://github.com/FLC-QU-hep/CaloCHILL) |
| 2026-11-05 | **StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference**<br><sub>Jake Hyun, Ziyu Zhao, Jae-sun Seo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) |
| 2026-11-05 | **Beyond K/V Caches: Cross-Model State Handoff in Hybrid Linear-Attention LLMs**<br><sub>Jiacheng Cai, Tao Zhang, Siqi Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08133) · [PDF](https://arxiv.org/pdf/2611.08133) |
| 2026-11-05 | **QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents**<br><sub>Yingjie Tan, Haiquan Qiu, Quanming Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07976) · [PDF](https://arxiv.org/pdf/2611.07976) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **156 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-05 | **ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding**<br><sub>Selim Aktas, Yusuf Erdem Erdem, Ahmed Zeer et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08669) · [PDF](https://arxiv.org/pdf/2611.08669) |
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

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **267 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design**<br><sub>Dayou Du, Woon Yee Ng, Guangming Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09825) · [PDF](https://arxiv.org/pdf/2611.09825) · [Code](https://github.com/OpenBitSys/BitDecoding-FP4) |
| 2026-11-06 | **FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding**<br><sub>Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09722) · [PDF](https://arxiv.org/pdf/2611.09722) · [Code](https://github.com/FutureMLS-Lab/FOSCAR) |
| 2026-11-06 | **Intent-Aware Caching for Efficient LLM Serving**<br><sub>Kazi Hasan Ibn Arif, JinYi Yoon, Dimitrios S. Nikolopoulos et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09715) · [PDF](https://arxiv.org/pdf/2611.09715) · [Code](https://github.com/hasanar1f/intent-aware-caching) |
| 2026-11-06 | **Nebula: Distributed Position-Independent Caching for LLM Serving**<br><sub>Yifei Liu, Junbin Pan, Junhao Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09474) · [PDF](https://arxiv.org/pdf/2611.09474) |
| 2026-11-06 | **MINE: Entropy-coded Memory-efficient Inference for Large Language Models**<br><sub>Emil Schätzle, Markus Püschel</sub> | [arXiv](https://arxiv.org/abs/2611.09424) · [PDF](https://arxiv.org/pdf/2611.09424) |
| 2026-11-06 | **TwinHash: Two-Sided Object Identity Management for Time- and Energy-Efficient Agentic Workflows**<br><sub>Sangbu Yun, Jung Gyu Min, Jin Hyun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09254) · [PDF](https://arxiv.org/pdf/2611.09254) |
| 2026-11-06 | **Inside the Trap: A Renewal Law for Prefix-Cache Collapse in LLM Agent Serving**<br><sub>Akshat Valse, Ali Jannesari</sub> | [arXiv](https://arxiv.org/abs/2611.08902) · [PDF](https://arxiv.org/pdf/2611.08902) |
| 2026-11-05 | **Enabling Retraining-Free Accurate Inference in Analog Compute in Memory Accelerators**<br><sub>George Karfakis, Puneet Gupta</sub> | [arXiv](https://arxiv.org/abs/2611.08693) · [PDF](https://arxiv.org/pdf/2611.08693) |
| 2026-11-05 | **StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference**<br><sub>Jake Hyun, Ziyu Zhao, Jae-sun Seo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) |
| 2026-11-05 | **Should You Split Decode? Disaggregation Across Future Models and Accelerators**<br><sub>Ramyad Hadidi</sub> | [arXiv](https://arxiv.org/abs/2611.08299) · [PDF](https://arxiv.org/pdf/2611.08299) |
| 2026-11-05 | **AutoCompress: Automated Hardware-Guided Model Compression**<br><sub>Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08290) · [PDF](https://arxiv.org/pdf/2611.08290) |
| 2026-11-05 | **ACSeL: Adaptive Configuration Search for Hardware-Constrained LLM Inference**<br><sub>Bokun Wang, Hung-Yueh Chiang, Diana Marculescu</sub> | [arXiv](https://arxiv.org/abs/2611.07570) · [PDF](https://arxiv.org/pdf/2611.07570) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **127 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **Verifier Noise Is a Temperature: Testing Tilt Predictions in Finite-Budget LLM-Guided Search**<br><sub>Xiaomeng Li</sub> | [arXiv](https://arxiv.org/abs/2611.09699) · [PDF](https://arxiv.org/pdf/2611.09699) |
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

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **215 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-06 | **Emo-LiveSync: Real-Time Universal Lip Synchronization with Explicit Emotion Control**<br><sub>Sangjoon Yu, Seungeun Lee, JoonHeyok Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09074) · [PDF](https://arxiv.org/pdf/2611.09074) |
| 2026-11-05 | **InstaGen: Group-Shared Importance Sampling for Fast Video Generation**<br><sub>Kislay Aditya Oj, Kumar Krishna Agrawal, Sri Surya Varma Datla et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08610) · [PDF](https://arxiv.org/pdf/2611.08610) |
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
