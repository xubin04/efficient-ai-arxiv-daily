# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-20 16:36 CST** · **1894 unique papers** · Newest submission: **2026-11-19**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 301 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 270 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 582 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 202 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 299 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 187 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 326 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 151 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 259 |

## Newly indexed · 2026-11-20

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Posterior Matching Distillation**<br><sub>Hidir Yesiltepe, Julius Berner, Arash Vahdat et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26629) · [PDF](https://arxiv.org/pdf/2611.26629) |
| 2026-11-19 | **TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming**<br><sub>Jinbin Luo, Xiaozhe Yao, Shang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26619) · [PDF](https://arxiv.org/pdf/2611.26619) |
| 2026-11-19 | **Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models**<br><sub>Chang Yang, Yao Xuan, Wendan Yan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26531) · [PDF](https://arxiv.org/pdf/2611.26531) |
| 2026-11-19 | **GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers**<br><sub>Sahibzada Allahyar, Julia White, Dhruv Atreja et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26509) · [PDF](https://arxiv.org/pdf/2611.26509) |
| 2026-11-19 | **Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware**<br><sub>Víctor Rodrigo González, Pablo M. Olmos, Ignacio Peis et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26437) · [PDF](https://arxiv.org/pdf/2611.26437) · [Code](https://github.com/deeplearningcafe/asuka-fm) |
| 2026-11-19 | **Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue**<br><sub>Rishabh Ravi, Tony Hong, Chen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26435) · [PDF](https://arxiv.org/pdf/2611.26435) |
| 2026-11-19 | **Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling**<br><sub>Yuchen Zhou, Lili Zheng, Yuxin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26407) · [PDF](https://arxiv.org/pdf/2611.26407) |
| 2026-11-19 | **Fast Self-Supervised Generative CT Denoising via Few-Step Sampling**<br><sub>Xingyi Yao, Zhengtao Ma, Zhennong Chen</sub> | [arXiv](https://arxiv.org/abs/2611.26370) · [PDF](https://arxiv.org/pdf/2611.26370) |
| 2026-11-19 | **HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs**<br><sub>Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure</sub> | [arXiv](https://arxiv.org/abs/2611.26363) · [PDF](https://arxiv.org/pdf/2611.26363) · [Code](https://github.com/ambroise-b/hisa) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **StreamEgo: Streaming Exocentric-to-Egocentric Video Generation**<br><sub>Tianyi Xu, Boyang Lyu, Yunkai Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26165) · [PDF](https://arxiv.org/pdf/2611.26165) |
| 2026-11-19 | **ChronoPatch: Black-Box Energy-Latency Attacks on Vision-Language Models**<br><sub>Jiawei Xing, Li Wang, Xiangtao Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26117) · [PDF](https://arxiv.org/pdf/2611.26117) |
| 2026-11-19 | **AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling**<br><sub>Zechun Zhou, Zhiyong Zheng, Xiaomin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26106) · [PDF](https://arxiv.org/pdf/2611.26106) |
| 2026-11-19 | **From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval for Production Content Recommendation**<br><sub>Zhixiong Hu, Meng Li, Maggie Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26096) · [PDF](https://arxiv.org/pdf/2611.26096) |
| 2026-11-19 | **Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency**<br><sub>Zhihao Hu, Jianqi Ma, Jun Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26040) · [PDF](https://arxiv.org/pdf/2611.26040) |
| 2026-11-19 | **FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models**<br><sub>Zekun Wang, Yizhuo Wang</sub> | [arXiv](https://arxiv.org/abs/2611.26020) · [PDF](https://arxiv.org/pdf/2611.26020) |
| 2026-11-19 | **Reinforcing Few-Step Diffusion Models via Shadow Posterior Matching**<br><sub>Jingqiao Xiu, Yicong Li</sub> | [arXiv](https://arxiv.org/abs/2611.25998) · [PDF](https://arxiv.org/pdf/2611.25998) · [Code](https://github.com/shadow-posterior/code) |
| 2026-11-19 | **DTS: Delta-Based Tile Scoring for Efficient Long-Context Sparse Attention**<br><sub>Emre Uğur, Jiawen Qi, Qinyu Chen</sub> | [arXiv](https://arxiv.org/abs/2611.25938) · [PDF](https://arxiv.org/pdf/2611.25938) |
| 2026-11-19 | **Generalist Meets Specialists: An Evolving Multimodal Agent with Persistent Tool Orchestration for Traffic Scenario Understanding**<br><sub>Linjia Kang, Binhan Jiang, Juan Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25868) · [PDF](https://arxiv.org/pdf/2611.25868) |
| 2026-11-19 | **Thinking in Streams: Proactive Spatial Reasoning with Vision-Language Models**<br><sub>Junyoung Hong, Minsu Kim, Jaehyun Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25865) · [PDF](https://arxiv.org/pdf/2611.25865) |

[View all 44 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **301 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling**<br><sub>Zechun Zhou, Zhiyong Zheng, Xiaomin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26106) · [PDF](https://arxiv.org/pdf/2611.26106) |
| 2026-11-19 | **VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin**<br><sub>Samir Khaki, Wei-Chen Wang, Song Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25717) · [PDF](https://arxiv.org/pdf/2611.25717) |
| 2026-11-19 | **Efficient Latent Reasoning for Vision-Language Model via Dynamics-Aware Quantization and Distillation**<br><sub>Yanjing Li, Sheng Xu, Baochang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25670) · [PDF](https://arxiv.org/pdf/2611.25670) |
| 2026-11-19 | **Splice-Core: Low-Order-Bit-Splicing GEMM for Highly Energy-Efficient AI Inference Accelerators**<br><sub>Prabhu Vellaisamy, Hsien-Fu Hung, Andrew Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25617) · [PDF](https://arxiv.org/pdf/2611.25617) |
| 2026-11-19 | **Fold the Loop: Decoding-Time KV Memory for Looped Vision-Language Models**<br><sub>Kun Zhou, Wenmian Yang, Zhensheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25369) · [PDF](https://arxiv.org/pdf/2611.25369) |
| 2026-11-18 | **Hardware Acceleration of Vision-Language-Action Models with Weight Precision Rising over the Flow Steps**<br><sub>Robin Geens, Simon Haepers, Jonas Crols et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24234) · [PDF](https://arxiv.org/pdf/2611.24234) |
| 2026-11-18 | **Compression Effects on Low-Resource Multilingual Translation**<br><sub>Abbas Sani</sub> | [arXiv](https://arxiv.org/abs/2611.24043) · [PDF](https://arxiv.org/pdf/2611.24043) · [Code](https://github.com/avvas200/efficient-multilingual-nmt-pilot%60) |
| 2026-11-18 | **MoMoVL: Modality-Aware Adaptive Compression for On-Device Sparsely-Activated Vision-Language Models**<br><sub>Dongkeun Lee, Wonjun Lee</sub> | [arXiv](https://arxiv.org/abs/2611.23695) · [PDF](https://arxiv.org/pdf/2611.23695) · [Code](https://github.com/sco-edge/MoMoVL) |
| 2026-11-17 | **QDA: Closed-Loop LLM Quantization Design with Agents**<br><sub>Xingyang Li, Tianlang Zhao, Song Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23388) · [PDF](https://arxiv.org/pdf/2611.23388) |
| 2026-11-17 | **HADVQ: Hessian Aware Directional Vector Quantization**<br><sub>Daniil Li, Mars Davletshin, Vadim Klyzhenko et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22721) · [PDF](https://arxiv.org/pdf/2611.22721) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **270 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs**<br><sub>Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure</sub> | [arXiv](https://arxiv.org/abs/2611.26363) · [PDF](https://arxiv.org/pdf/2611.26363) · [Code](https://github.com/ambroise-b/hisa) |
| 2026-11-19 | **What Does Anti-Hallucination Training Buy? Saying Less, Cheap Pruning, and the Rest**<br><sub>Lingkai Bu, Qian Gao</sub> | [arXiv](https://arxiv.org/abs/2611.25814) · [PDF](https://arxiv.org/pdf/2611.25814) |
| 2026-11-19 | **VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin**<br><sub>Samir Khaki, Wei-Chen Wang, Song Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25717) · [PDF](https://arxiv.org/pdf/2611.25717) |
| 2026-11-19 | **VidToC: Rethinking Video Token Compression for Multimodal Large Language Models**<br><sub>Zihan Xiao, Boshen Xu, Pei Fu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25574) · [PDF](https://arxiv.org/pdf/2611.25574) |
| 2026-11-19 | **Query-Aware vs. Query-Agnostic Training-Free Video Token Pruning in Multimodal LLMs**<br><sub>Divya Kothandaraman, Timo Kumkel, Jaclyn Pytlarz</sub> | [arXiv](https://arxiv.org/abs/2611.25537) · [PDF](https://arxiv.org/pdf/2611.25537) |
| 2026-11-19 | **RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression**<br><sub>Payman Behnam, Elaheh Sobhani, Saad Amin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25433) · [PDF](https://arxiv.org/pdf/2611.25433) |
| 2026-11-18 | **Diffusion Models are Provably Efficient Priors for Sparse Recovery**<br><sub>Ivan Lee, Xingyu Xu, Yuejie Chi</sub> | [arXiv](https://arxiv.org/abs/2611.24602) · [PDF](https://arxiv.org/pdf/2611.24602) |
| 2026-11-18 | **Let a Small Model Read First: Faster Prefill for Long Interleaved Image-Text Inputs**<br><sub>Xiaolin Lin, Kai-Chiang Wu, Bing Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24431) · [PDF](https://arxiv.org/pdf/2611.24431) |
| 2026-11-18 | **Inference-Time Scaling in Agentic Hardware Verification Workflows: A Multi-Strategy Characterization Across Protocol Complexity**<br><sub>Vikash Kumar</sub> | [arXiv](https://arxiv.org/abs/2611.23905) · [PDF](https://arxiv.org/pdf/2611.23905) |
| 2026-11-18 | **MoMoVL: Modality-Aware Adaptive Compression for On-Device Sparsely-Activated Vision-Language Models**<br><sub>Dongkeun Lee, Wonjun Lee</sub> | [arXiv](https://arxiv.org/abs/2611.23695) · [PDF](https://arxiv.org/pdf/2611.23695) · [Code](https://github.com/sco-edge/MoMoVL) |
| 2026-11-17 | **Transfer Once, Ask Locally: Compact Audio-Visual Memory for On-Device Question Answering**<br><sub>Qitong Wang, Jihui Jin, Divya Kothandaraman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23085) · [PDF](https://arxiv.org/pdf/2611.23085) |
| 2026-11-17 | **LoopPrune: Recurrent Pruning for Looped Diffusion Transformers**<br><sub>Weizhong Huang, Huaijia Kou, Yan Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22757) · [PDF](https://arxiv.org/pdf/2611.22757) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **582 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Posterior Matching Distillation**<br><sub>Hidir Yesiltepe, Julius Berner, Arash Vahdat et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26629) · [PDF](https://arxiv.org/pdf/2611.26629) |
| 2026-11-19 | **GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers**<br><sub>Sahibzada Allahyar, Julia White, Dhruv Atreja et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26509) · [PDF](https://arxiv.org/pdf/2611.26509) |
| 2026-11-19 | **Fast Self-Supervised Generative CT Denoising via Few-Step Sampling**<br><sub>Xingyi Yao, Zhengtao Ma, Zhennong Chen</sub> | [arXiv](https://arxiv.org/abs/2611.26370) · [PDF](https://arxiv.org/pdf/2611.26370) |
| 2026-11-19 | **Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency**<br><sub>Zhihao Hu, Jianqi Ma, Jun Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26040) · [PDF](https://arxiv.org/pdf/2611.26040) |
| 2026-11-19 | **Reinforcing Few-Step Diffusion Models via Shadow Posterior Matching**<br><sub>Jingqiao Xiu, Yicong Li</sub> | [arXiv](https://arxiv.org/abs/2611.25998) · [PDF](https://arxiv.org/pdf/2611.25998) · [Code](https://github.com/shadow-posterior/code) |
| 2026-11-19 | **TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling**<br><sub>Junchi Zhang, Zihan Gu, Jiangcan Jia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25847) · [PDF](https://arxiv.org/pdf/2611.25847) |
| 2026-11-19 | **Efficient Latent Reasoning for Vision-Language Model via Dynamics-Aware Quantization and Distillation**<br><sub>Yanjing Li, Sheng Xu, Baochang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25670) · [PDF](https://arxiv.org/pdf/2611.25670) |
| 2026-11-19 | **AesDistill: Distilling Generative Aesthetics for Image Color Enhancement**<br><sub>Chuanzhi Xu, Chengkun Yue, Huiqi Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25635) · [PDF](https://arxiv.org/pdf/2611.25635) |
| 2026-11-19 | **TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation**<br><sub>Yijun Liu, Shijia Ge, Tongtong Feng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25553) · [PDF](https://arxiv.org/pdf/2611.25553) · [Code](https://github.com/PlantPotatoOnMoon/TwoPass) |
| 2026-11-19 | **HOPD: Historical On-Policy Distillation for SAR MLLM Continual Learning**<br><sub>Yuxuan Li, Derrick Goh Xin Deik, Zheng-Peng Duan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25391) · [PDF](https://arxiv.org/pdf/2611.25391) · [Code](https://github.com/zcablii/HOPD) |
| 2026-11-18 | **VisAlloc: Allocating Visual Supervision for On-Policy Self-Distillation**<br><sub>Haoran Xu, Tian Chen, Yuhe Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25069) · [PDF](https://arxiv.org/pdf/2611.25069) · [Code](https://github.com/Kaelyn01/VisAlloc) |
| 2026-11-18 | **ProxySearch: Decoupled Inference-Time Scaling for Diffusion Models via Asymmetric Noise-Rank Transfer**<br><sub>Seungwook Kim, Jongmin Lee</sub> | [arXiv](https://arxiv.org/abs/2611.23929) · [PDF](https://arxiv.org/pdf/2611.23929) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **202 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Efficient and Robust Drafting with Multi-Token Prediction**<br><sub>Filippo Galgani, Ziwei Ji, Omri Homburger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25813) · [PDF](https://arxiv.org/pdf/2611.25813) |
| 2026-11-18 | **A Hybrid RAG Framework for Deceptive Review Detection: Integrating RoBERTa-LoRA, FAISS-Based Retrieval, and LLM Reasoning**<br><sub>Andrei Kostin, José Ángel Diaz-Garcia, Karel Gutiérrez-Batista</sub> | [arXiv](https://arxiv.org/abs/2611.24049) · [PDF](https://arxiv.org/pdf/2611.24049) |
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

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **299 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue**<br><sub>Rishabh Ravi, Tony Hong, Chen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26435) · [PDF](https://arxiv.org/pdf/2611.26435) |
| 2026-11-19 | **HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs**<br><sub>Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure</sub> | [arXiv](https://arxiv.org/abs/2611.26363) · [PDF](https://arxiv.org/pdf/2611.26363) · [Code](https://github.com/ambroise-b/hisa) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling**<br><sub>Zechun Zhou, Zhiyong Zheng, Xiaomin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26106) · [PDF](https://arxiv.org/pdf/2611.26106) |
| 2026-11-19 | **FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models**<br><sub>Zekun Wang, Yizhuo Wang</sub> | [arXiv](https://arxiv.org/abs/2611.26020) · [PDF](https://arxiv.org/pdf/2611.26020) |
| 2026-11-19 | **DTS: Delta-Based Tile Scoring for Efficient Long-Context Sparse Attention**<br><sub>Emre Uğur, Jiawen Qi, Qinyu Chen</sub> | [arXiv](https://arxiv.org/abs/2611.25938) · [PDF](https://arxiv.org/pdf/2611.25938) |
| 2026-11-19 | **Thinking in Streams: Proactive Spatial Reasoning with Vision-Language Models**<br><sub>Junyoung Hong, Minsu Kim, Jaehyun Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25865) · [PDF](https://arxiv.org/pdf/2611.25865) |
| 2026-11-19 | **Efficient and Robust Drafting with Multi-Token Prediction**<br><sub>Filippo Galgani, Ziwei Ji, Omri Homburger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25813) · [PDF](https://arxiv.org/pdf/2611.25813) |
| 2026-11-19 | **RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression**<br><sub>Payman Behnam, Elaheh Sobhani, Saad Amin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25433) · [PDF](https://arxiv.org/pdf/2611.25433) |
| 2026-11-18 | **TripleKV: Predict, Prefetch, Protect -- KV Cache Management for AI Agents**<br><sub>Shashwat Jaiswal, Chloe Alverti, Mengmei Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25112) · [PDF](https://arxiv.org/pdf/2611.25112) |
| 2026-11-18 | **Every Query Routes Itself: Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention**<br><sub>Zhen Huang, Shuwei Li, Ruizhe Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24479) · [PDF](https://arxiv.org/pdf/2611.24479) |
| 2026-11-18 | **Spark-H3: Adaptive Block Sparse Attention for Video Diffusion Models**<br><sub>Zecheng Tang, Jiaye Fu, Youtian Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24256) · [PDF](https://arxiv.org/pdf/2611.24256) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **187 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Generalist Meets Specialists: An Evolving Multimodal Agent with Persistent Tool Orchestration for Traffic Scenario Understanding**<br><sub>Linjia Kang, Binhan Jiang, Juan Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25868) · [PDF](https://arxiv.org/pdf/2611.25868) |
| 2026-11-19 | **Efficient and Robust Drafting with Multi-Token Prediction**<br><sub>Filippo Galgani, Ziwei Ji, Omri Homburger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25813) · [PDF](https://arxiv.org/pdf/2611.25813) |
| 2026-11-19 | **Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding**<br><sub>Qishu Hu, Haozhao Wang, Zicong Hong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25436) · [PDF](https://arxiv.org/pdf/2611.25436) |
| 2026-11-18 | **ScaleDiag: Diagnosing the Limits of Test-Time Scaling in GUI Grounding**<br><sub>Chen Liu, Zhen Fang, Xin Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25297) · [PDF](https://arxiv.org/pdf/2611.25297) · [Code](https://github.com/YenanLiu/ScaleDiag) |
| 2026-11-18 | **A Verifier from the Past: Test-Time Compute for Time Series Foundation Models**<br><sub>Arjun Choudhry, Aditya Narayanan, Raghav Mallampalli et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25171) · [PDF](https://arxiv.org/pdf/2611.25171) |
| 2026-11-18 | **Test-Time Symmetrization: Scaling Laws for Model-Agnostic Learning under Structure**<br><sub>Behrooz Tahmasebi, Melanie Weber</sub> | [arXiv](https://arxiv.org/abs/2611.24032) · [PDF](https://arxiv.org/pdf/2611.24032) |
| 2026-11-18 | **NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding**<br><sub>Alagappan Valliappan, Ankit More, Dheevatsa Mudigere et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23835) · [PDF](https://arxiv.org/pdf/2611.23835) |
| 2026-11-17 | **FACT: Fixed-Budget Allocation and Cross-Step Training for Speculative Decoding**<br><sub>Hadi Fares, Mayssa Hajj Hassan, Ali Salman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23463) · [PDF](https://arxiv.org/pdf/2611.23463) · [Code](https://github.com/mrfares11/specdec) |
| 2026-11-17 | **SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding**<br><sub>Selin Yildirim, Ali Zeyrek, Deming Chen</sub> | [arXiv](https://arxiv.org/abs/2611.22296) · [PDF](https://arxiv.org/pdf/2611.22296) |
| 2026-11-16 | **VisHead-Spec: Head-Routed Visual Attention for Multimodal Speculative Decoding**<br><sub>Xin Guo, Arushi Rai, Xiang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21839) · [PDF](https://arxiv.org/pdf/2611.21839) |
| 2026-11-16 | **Sketch, Don&#x27;t Paint: Allocating Test-Time Compute in Generative Visual Reasoning**<br><sub>Sheng Lu, Guangpin Tao, Tong Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21812) · [PDF](https://arxiv.org/pdf/2611.21812) |
| 2026-11-16 | **Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents**<br><sub>NVIDIA, :, Adi Margolin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.20771) · [PDF](https://arxiv.org/pdf/2611.20771) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **326 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming**<br><sub>Jinbin Luo, Xiaozhe Yao, Shang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26619) · [PDF](https://arxiv.org/pdf/2611.26619) |
| 2026-11-19 | **Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models**<br><sub>Chang Yang, Yao Xuan, Wendan Yan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26531) · [PDF](https://arxiv.org/pdf/2611.26531) |
| 2026-11-19 | **Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue**<br><sub>Rishabh Ravi, Tony Hong, Chen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26435) · [PDF](https://arxiv.org/pdf/2611.26435) |
| 2026-11-19 | **ChronoPatch: Black-Box Energy-Latency Attacks on Vision-Language Models**<br><sub>Jiawei Xing, Li Wang, Xiangtao Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26117) · [PDF](https://arxiv.org/pdf/2611.26117) |
| 2026-11-19 | **From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval for Production Content Recommendation**<br><sub>Zhixiong Hu, Meng Li, Maggie Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26096) · [PDF](https://arxiv.org/pdf/2611.26096) |
| 2026-11-19 | **DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents**<br><sub>Licheng Pan, Yuzhou Chen, Zhixuan Chu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25583) · [PDF](https://arxiv.org/pdf/2611.25583) |
| 2026-11-19 | **RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression**<br><sub>Payman Behnam, Elaheh Sobhani, Saad Amin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25433) · [PDF](https://arxiv.org/pdf/2611.25433) |
| 2026-11-18 | **TripleKV: Predict, Prefetch, Protect -- KV Cache Management for AI Agents**<br><sub>Shashwat Jaiswal, Chloe Alverti, Mengmei Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25112) · [PDF](https://arxiv.org/pdf/2611.25112) |
| 2026-11-18 | **eFAIR: Fair LLM Serving under Hourly Electricity Commitments**<br><sub>You Peng, Youhe Jiang, Chen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24119) · [PDF](https://arxiv.org/pdf/2611.24119) |
| 2026-11-18 | **LEDGE: An Efficient Simulator for Distributed LLM Serving on Heterogeneous Edge Devices**<br><sub>Zihao Wang, Ye Tian, Tajana Rosing et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24085) · [PDF](https://arxiv.org/pdf/2611.24085) · [Code](https://github.com/gdfwj/LEDGE) |
| 2026-11-18 | **HETEROVLM: Edge Multi-Request Vision-Language Model Serving on a Heterogeneous Versal SoC with AI Engines and Programmable Logic**<br><sub>Zhiheng Chen, Yu-An Chou, Yifan Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23878) · [PDF](https://arxiv.org/pdf/2611.23878) |
| 2026-11-17 | **Towards Fair Resource Sharing in Agentic LLM Serving**<br><sub>Sehyeon Lee, Yuchen Xia, Zhaoyang Hong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23558) · [PDF](https://arxiv.org/pdf/2611.23558) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **151 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling**<br><sub>Yuchen Zhou, Lili Zheng, Yuxin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26407) · [PDF](https://arxiv.org/pdf/2611.26407) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **D3-Cache: Accelerating Diffusion Models with Dynamic Mode Decomposition**<br><sub>Yanbo Li, An Xiang, Xiaoxin Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25689) · [PDF](https://arxiv.org/pdf/2611.25689) |
| 2026-11-19 | **TRAC: Efficient Diffusion Language Models for Machine Translation via Length-Aware Decoding**<br><sub>Tianyuan Li, Xihan Yang, Chenglong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25643) · [PDF](https://arxiv.org/pdf/2611.25643) |
| 2026-11-19 | **FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash**<br><sub>Yuseon Choi, Sanghyeon Park, Eunjong Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25580) · [PDF](https://arxiv.org/pdf/2611.25580) |
| 2026-11-18 | **CalibCache: Cache-to-Full Feature Dynamics Calibration for Diffusion Transformers**<br><sub>Mingyu Liang, Dingkun Xu, Jingwei Xu</sub> | [arXiv](https://arxiv.org/abs/2611.25296) · [PDF](https://arxiv.org/pdf/2611.25296) |
| 2026-11-18 | **Every Query Routes Itself: Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention**<br><sub>Zhen Huang, Shuwei Li, Ruizhe Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24479) · [PDF](https://arxiv.org/pdf/2611.24479) |
| 2026-11-18 | **Hardware Acceleration of Vision-Language-Action Models with Weight Precision Rising over the Flow Steps**<br><sub>Robin Geens, Simon Haepers, Jonas Crols et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24234) · [PDF](https://arxiv.org/pdf/2611.24234) |
| 2026-11-17 | **FastFrames: Video Generation at Interactive Latency**<br><sub>Gene Chou, Guandao Yang, Fujun Luan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |
| 2026-11-17 | **RISA: Recoverable Sparse Attention for Block-Diffusion Language Models**<br><sub>Xinrui Zhong, Fanjiang Ye, Yuke Wang</sub> | [arXiv](https://arxiv.org/abs/2611.22191) · [PDF](https://arxiv.org/pdf/2611.22191) |
| 2026-11-17 | **BATMoS: Budget-Aware Guidance Allocation for Efficient Video Diffusion**<br><sub>Zhixu Du, Kuo Yang, Jingwei Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22028) · [PDF](https://arxiv.org/pdf/2611.22028) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **259 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Posterior Matching Distillation**<br><sub>Hidir Yesiltepe, Julius Berner, Arash Vahdat et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26629) · [PDF](https://arxiv.org/pdf/2611.26629) |
| 2026-11-19 | **Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware**<br><sub>Víctor Rodrigo González, Pablo M. Olmos, Ignacio Peis et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26437) · [PDF](https://arxiv.org/pdf/2611.26437) · [Code](https://github.com/deeplearningcafe/asuka-fm) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **StreamEgo: Streaming Exocentric-to-Egocentric Video Generation**<br><sub>Tianyi Xu, Boyang Lyu, Yunkai Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26165) · [PDF](https://arxiv.org/pdf/2611.26165) |
| 2026-11-19 | **Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency**<br><sub>Zhihao Hu, Jianqi Ma, Jun Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26040) · [PDF](https://arxiv.org/pdf/2611.26040) |
| 2026-11-19 | **TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling**<br><sub>Junchi Zhang, Zihan Gu, Jiangcan Jia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25847) · [PDF](https://arxiv.org/pdf/2611.25847) |
| 2026-11-19 | **FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash**<br><sub>Yuseon Choi, Sanghyeon Park, Eunjong Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25580) · [PDF](https://arxiv.org/pdf/2611.25580) |
| 2026-11-18 | **Every Query Routes Itself: Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention**<br><sub>Zhen Huang, Shuwei Li, Ruizhe Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24479) · [PDF](https://arxiv.org/pdf/2611.24479) |
| 2026-11-18 | **Spark-H3: Adaptive Block Sparse Attention for Video Diffusion Models**<br><sub>Zecheng Tang, Jiaye Fu, Youtian Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24256) · [PDF](https://arxiv.org/pdf/2611.24256) |
| 2026-11-18 | **Hardware Acceleration of Vision-Language-Action Models with Weight Precision Rising over the Flow Steps**<br><sub>Robin Geens, Simon Haepers, Jonas Crols et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24234) · [PDF](https://arxiv.org/pdf/2611.24234) |
| 2026-11-18 | **ProxySearch: Decoupled Inference-Time Scaling for Diffusion Models via Asymmetric Noise-Rank Transfer**<br><sub>Seungwook Kim, Jongmin Lee</sub> | [arXiv](https://arxiv.org/abs/2611.23929) · [PDF](https://arxiv.org/pdf/2611.23929) |
| 2026-11-17 | **FastFrames: Video Generation at Interactive Latency**<br><sub>Gene Chou, Guandao Yang, Fujun Luan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) |

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
