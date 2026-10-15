# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-15 13:55 CST** · **1028 unique papers** · Newest submission: **2026-10-14**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 163 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 149 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 348 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 100 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 141 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 100 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 165 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 82 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 137 |

## Newly indexed · 2026-10-15

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **Speculative Sampling in Interactive Video Generation**<br><sub>Yubo Huang, Yuxuan Zhang, Jiaming Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20556) · [PDF](https://arxiv.org/pdf/2610.20556) |
| 2026-10-14 | **Generative Representation Learning for Scalable Latent Tokenization**<br><sub>Alan Baade, Kyle Sargent, Vincent Sitzmann et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20533) · [PDF](https://arxiv.org/pdf/2610.20533) |
| 2026-10-14 | **ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models**<br><sub>Bohan Sun, Zunhai Su, Xialie Zhuang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20503) · [PDF](https://arxiv.org/pdf/2610.20503) · [Code](https://github.com/StartLuxLabs/ReaDy) |
| 2026-10-14 | **FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding**<br><sub>Shuxuan Li, Jialiang Kang, Yanghao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20392) · [PDF](https://arxiv.org/pdf/2610.20392) |
| 2026-10-14 | **STP-GUI: Spatially-Aware Token Pruning for Efficient Web-GUI Agents**<br><sub>Shuo Wang, Sifan Zhou, Xiaobo Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20390) · [PDF](https://arxiv.org/pdf/2610.20390) |
| 2026-10-14 | **Beyond Expert Rankings: Contrast Calibration for Mixed-Precision MoE Quantization**<br><sub>Renjie Xie, Juncheng Yang, Aoting Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20353) · [PDF](https://arxiv.org/pdf/2610.20353) |
| 2026-10-14 | **Are We Overthinking One-Step Generation?**<br><sub>Woobin Park, Jaeyeon Kim, Yilun Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20331) · [PDF](https://arxiv.org/pdf/2610.20331) · [Code](https://github.com/JaeyeonKim01/priming) |
| 2026-10-14 | **SpectrumQuant: Spectrum Alignment for LLM Quantization**<br><sub>Dwaipayan Haldar, Indranil Patra, Azhar Yousuf et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20303) · [PDF](https://arxiv.org/pdf/2610.20303) |
| 2026-10-14 | **Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance**<br><sub>Zhuobai Dong, Junchao Yi, Hu Jian Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20220) · [PDF](https://arxiv.org/pdf/2610.20220) |
| 2026-10-14 | **Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility**<br><sub>Salima Lamsiyah, Adelaide Danilov, Oleksandr Marchenko Breneur et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20139) · [PDF](https://arxiv.org/pdf/2610.20139) |
| 2026-10-14 | **StreamErase: Towards Ultra-Fast Streaming Video Erasing**<br><sub>Zhuobai Dong, Xiaobing Tu, Xiantao Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20137) · [PDF](https://arxiv.org/pdf/2610.20137) |
| 2026-10-14 | **RepForcing: Representation-Space Initialization for Autoregressive Video Distillation**<br><sub>Siming Fu, Zheming Fu, Lianrui Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20111) · [PDF](https://arxiv.org/pdf/2610.20111) |
| 2026-10-14 | **MemDuet: Learning Dual-Process Memory for Long-Context Reasoning**<br><sub>Jiangcheng Song, Haodong Jing, Yulin Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19928) · [PDF](https://arxiv.org/pdf/2610.19928) |
| 2026-10-14 | **Sparse Transformer: a Controlled Testbed for Mechanistic Interpretability**<br><sub>Anton Korznikov, Alexey Dontsov, Elena Tutubalina</sub> | [arXiv](https://arxiv.org/abs/2610.19907) · [PDF](https://arxiv.org/pdf/2610.19907) |
| 2026-10-14 | **Multimodal Medical Image Parsing with Task-Specific Low-Rank Adapters**<br><sub>Taha Sabir, Alberto Montero Molina, Thinh Quang Ly et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19901) · [PDF](https://arxiv.org/pdf/2610.19901) · [Code](https://github.com/TahaSabir0/FLARE26-Hexapus) |
| 2026-10-14 | **Occupancy Modeling via Drifting: One-Step Generation Enables Direct Policy Extraction**<br><sub>Robin Uhrich, Marco Bagatella, Núria Armengol Urpí et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19883) · [PDF](https://arxiv.org/pdf/2610.19883) |
| 2026-10-14 | **Rationale Distribution Distillation via Flow Matching for Distributional Continuous Latent Reasoning**<br><sub>Mingyeong Kim, Gyusang Cho, Juho Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19871) · [PDF](https://arxiv.org/pdf/2610.19871) |
| 2026-10-14 | **JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs**<br><sub>Daijin Hu</sub> | [arXiv](https://arxiv.org/abs/2610.19822) · [PDF](https://arxiv.org/pdf/2610.19822) |
| 2026-10-14 | **ActionOPD: Distilling Decisions, Not Tokens**<br><sub>Huining Yuan, Xiangmin Yi, Zelai Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19820) · [PDF](https://arxiv.org/pdf/2610.19820) |
| 2026-10-14 | **Qwen-MT-Lumen at WMT2026: Instruction-Specialized Translation via Quality-Aware Training and On-Policy Distillation**<br><sub>Hao Wang, Yangyang Liu, Xiaohu Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19758) · [PDF](https://arxiv.org/pdf/2610.19758) |

[View all 43 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **163 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **Beyond Expert Rankings: Contrast Calibration for Mixed-Precision MoE Quantization**<br><sub>Renjie Xie, Juncheng Yang, Aoting Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20353) · [PDF](https://arxiv.org/pdf/2610.20353) |
| 2026-10-14 | **SpectrumQuant: Spectrum Alignment for LLM Quantization**<br><sub>Dwaipayan Haldar, Indranil Patra, Azhar Yousuf et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20303) · [PDF](https://arxiv.org/pdf/2610.20303) |
| 2026-10-14 | **Multimodal Medical Image Parsing with Task-Specific Low-Rank Adapters**<br><sub>Taha Sabir, Alberto Montero Molina, Thinh Quang Ly et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19901) · [PDF](https://arxiv.org/pdf/2610.19901) · [Code](https://github.com/TahaSabir0/FLARE26-Hexapus) |
| 2026-10-14 | **MFSA: A Multi-Format Systolic Array with Native Micro Scaling Support**<br><sub>Jiayi Wang, Kearnan Bishop, Ang Li</sub> | [arXiv](https://arxiv.org/abs/2610.19645) · [PDF](https://arxiv.org/pdf/2610.19645) |
| 2026-10-14 | **PN-Mix: Pair-Norm Guided Mixed-Precision Key Cache Quantization for Efficient Long-Output LLM Inference**<br><sub>Gil Jae Song, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2610.19605) · [PDF](https://arxiv.org/pdf/2610.19605) |
| 2026-10-14 | **What You Sign Is Not What You Run: The Verifiability Gap in Quantized LLM Supply Chains**<br><sub>Wei-Liang Liu, Cheng-Yen Tsai</sub> | [arXiv](https://arxiv.org/abs/2610.19498) · [PDF](https://arxiv.org/pdf/2610.19498) · [Code](https://github.com/Rlonglong/gguf-verifiability-artifact) |
| 2026-10-14 | **MemCode: Discrete Semantic Representations for Long-Term Agent Memory**<br><sub>Xin Li, Liang Hu, Duoqian Miao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19472) · [PDF](https://arxiv.org/pdf/2610.19472) |
| 2026-10-13 | **MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization**<br><sub>Yangchengyu Zhou, Zhiping Wu, Runchang Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18642) · [PDF](https://arxiv.org/pdf/2610.18642) · [Code](https://github.com/RL-MIND/MultiAlloc) |
| 2026-10-13 | **Lightweight but Linguistically Fair? Quantisation Robustness across Bavarian, German, and English**<br><sub>Jophin John, Michael Hoffmann, Piroska Lendvai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18343) · [PDF](https://arxiv.org/pdf/2610.18343) |
| 2026-10-13 | **Revisiting Error Feedback for Model Quantization**<br><sub>Wai-Yiu Keung, Chi Cui, Wing-Kin Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18139) · [PDF](https://arxiv.org/pdf/2610.18139) |
| 2026-10-13 | **BELT : BEhavior-Aligned Low-Rank KV Cache Compression with Learned Top-k Rank Allocation**<br><sub>Yaoyang Liu, Shuwei Shen, Jincheng Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17966) · [PDF](https://arxiv.org/pdf/2610.17966) |
| 2026-10-13 | **Mixed Precision Scaling Laws for Quantized Pretraining**<br><sub>Jinuk Kim, Rajarshi Saha, Muhammed Fatih Balin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17637) · [PDF](https://arxiv.org/pdf/2610.17637) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **149 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **STP-GUI: Spatially-Aware Token Pruning for Efficient Web-GUI Agents**<br><sub>Shuo Wang, Sifan Zhou, Xiaobo Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20390) · [PDF](https://arxiv.org/pdf/2610.20390) |
| 2026-10-14 | **Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility**<br><sub>Salima Lamsiyah, Adelaide Danilov, Oleksandr Marchenko Breneur et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20139) · [PDF](https://arxiv.org/pdf/2610.20139) |
| 2026-10-14 | **MemDuet: Learning Dual-Process Memory for Long-Context Reasoning**<br><sub>Jiangcheng Song, Haodong Jing, Yulin Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19928) · [PDF](https://arxiv.org/pdf/2610.19928) |
| 2026-10-13 | **Unlocking Structured Pruning for Reasoning Language Models via Attention-Preserving MLP Trimming**<br><sub>Woosang Lim, Haneul Yoo, Vincent-Daniel Yun et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19121) · [PDF](https://arxiv.org/pdf/2610.19121) |
| 2026-10-13 | **Focus, Align, and Diffuse: Time-Series-Aware Keyframe Diffusion for Cardiac Dynamic Synthesis from Sparse Observations**<br><sub>Junkai Liu, Haofan Wu, Nay Aung et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19050) · [PDF](https://arxiv.org/pdf/2610.19050) |
| 2026-10-13 | **Discrete Diffusion Models are Minimax Optimal Under Sparsity**<br><sub>Luca Blunda, Tyler Farghly, Umut Simsekli et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19020) · [PDF](https://arxiv.org/pdf/2610.19020) |
| 2026-10-13 | **Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs**<br><sub>Aimon Rahman, Joymallya Chakraborty, Vidit Bansal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18858) · [PDF](https://arxiv.org/pdf/2610.18858) |
| 2026-10-13 | **Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning**<br><sub>Tianhao Fu, Austin Wang, Charles Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18690) · [PDF](https://arxiv.org/pdf/2610.18690) |
| 2026-10-13 | **Two For The Price Of One: Curvature-Aware Pruning Preserves Influence Functions Too**<br><sub>Mehdi Makni, Natalia Ponomareva, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2610.18516) · [PDF](https://arxiv.org/pdf/2610.18516) |
| 2026-10-13 | **Readout Scaling Shapes Sparse Feature Recovery**<br><sub>Brian Xiao, Sarah Wilson</sub> | [arXiv](https://arxiv.org/abs/2610.18462) · [PDF](https://arxiv.org/pdf/2610.18462) |
| 2026-10-13 | **Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs**<br><sub>Peiran Yin, Hao Wu, Zihao Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18399) · [PDF](https://arxiv.org/pdf/2610.18399) · [Code](https://github.com/EIT-NLP/Bifocal) |
| 2026-10-13 | **TwinPrune: Density-Aware Two-Phase Token Pruning for Vision-Language Models**<br><sub>Kai Liu, Anqi Li, Junxian Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17530) · [PDF](https://arxiv.org/pdf/2610.17530) · [Code](https://github.com/Kai-Liu001/TwinPrune) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **348 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **Are We Overthinking One-Step Generation?**<br><sub>Woobin Park, Jaeyeon Kim, Yilun Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20331) · [PDF](https://arxiv.org/pdf/2610.20331) · [Code](https://github.com/JaeyeonKim01/priming) |
| 2026-10-14 | **Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance**<br><sub>Zhuobai Dong, Junchao Yi, Hu Jian Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20220) · [PDF](https://arxiv.org/pdf/2610.20220) |
| 2026-10-14 | **RepForcing: Representation-Space Initialization for Autoregressive Video Distillation**<br><sub>Siming Fu, Zheming Fu, Lianrui Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20111) · [PDF](https://arxiv.org/pdf/2610.20111) |
| 2026-10-14 | **Sparse Transformer: a Controlled Testbed for Mechanistic Interpretability**<br><sub>Anton Korznikov, Alexey Dontsov, Elena Tutubalina</sub> | [arXiv](https://arxiv.org/abs/2610.19907) · [PDF](https://arxiv.org/pdf/2610.19907) |
| 2026-10-14 | **Occupancy Modeling via Drifting: One-Step Generation Enables Direct Policy Extraction**<br><sub>Robin Uhrich, Marco Bagatella, Núria Armengol Urpí et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19883) · [PDF](https://arxiv.org/pdf/2610.19883) |
| 2026-10-14 | **Rationale Distribution Distillation via Flow Matching for Distributional Continuous Latent Reasoning**<br><sub>Mingyeong Kim, Gyusang Cho, Juho Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19871) · [PDF](https://arxiv.org/pdf/2610.19871) |
| 2026-10-14 | **ActionOPD: Distilling Decisions, Not Tokens**<br><sub>Huining Yuan, Xiangmin Yi, Zelai Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19820) · [PDF](https://arxiv.org/pdf/2610.19820) |
| 2026-10-14 | **Qwen-MT-Lumen at WMT2026: Instruction-Specialized Translation via Quality-Aware Training and On-Policy Distillation**<br><sub>Hao Wang, Yangyang Liu, Xiaohu Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19758) · [PDF](https://arxiv.org/pdf/2610.19758) |
| 2026-10-14 | **Function-Space Temporal Self-Distillation for Policy Optimization**<br><sub>Aryan Das, Arnab Bhattacharya, Vinay Kumar Verma</sub> | [arXiv](https://arxiv.org/abs/2610.19687) · [PDF](https://arxiv.org/pdf/2610.19687) |
| 2026-10-14 | **PA1-OPD: One-Step Prefix-Augmented On-Policy Distillation for Language Model Pretraining**<br><sub>Zhenhe Wu, Jian Yang, Yaping Jin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19601) · [PDF](https://arxiv.org/pdf/2610.19601) |
| 2026-10-14 | **Divergence-Routed On-Policy Distillation for Language Models**<br><sub>Tiantian Peng, Guannan Lv, Hongyang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19572) · [PDF](https://arxiv.org/pdf/2610.19572) |
| 2026-10-14 | **Learning Visual Speech Representations via Cross-Modal Distillation and Joint Face-Lip Modeling**<br><sub>Jing-Xuan Zhang, Genshun Wan, Jianqing Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19559) · [PDF](https://arxiv.org/pdf/2610.19559) · [Code](https://github.com/jxzhanggg/FLARE) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **100 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **Multimodal Medical Image Parsing with Task-Specific Low-Rank Adapters**<br><sub>Taha Sabir, Alberto Montero Molina, Thinh Quang Ly et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19901) · [PDF](https://arxiv.org/pdf/2610.19901) · [Code](https://github.com/TahaSabir0/FLARE26-Hexapus) |
| 2026-10-13 | **DUALVIEW: Leveraging Broad and Output-Specific Evidence for LLM-based Multi-Output Text Regression**<br><sub>Yiheng Su, Junyi Jessy Li, Matthew Lease</sub> | [arXiv](https://arxiv.org/abs/2610.19206) · [PDF](https://arxiv.org/pdf/2610.19206) |
| 2026-10-13 | **Discovering Undisclosed Concepts in LoRA Adapters for Diffusion-Based AIGC Models**<br><sub>Yupeng Qiu, Han Fang, Dhananjai Sharma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18990) · [PDF](https://arxiv.org/pdf/2610.18990) |
| 2026-10-13 | **Unlocking Token Rewards via Training-Free Reward Attribution**<br><sub>Sitong Wu, Haoru Tan, Bin Xia et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18704) · [PDF](https://arxiv.org/pdf/2610.18704) · [Code](https://github.com/stonewst/P2T) |
| 2026-10-13 | **LLM2R: From Large Language Models to 3D Reassemblers**<br><sub>Zhouhan Zhong, Qiuhong Shen, Xingyi Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18604) · [PDF](https://arxiv.org/pdf/2610.18604) |
| 2026-10-12 | **Monarch-Muon: Structure-Aware Muon for Fast and Memory-Efficient Pretraining**<br><sub>Alexander Miasnikov, Ruslan Kabirov, Gleb Molodtsov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17429) · [PDF](https://arxiv.org/pdf/2610.17429) |
| 2026-10-12 | **HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation**<br><sub>Tripti Shukla, Shwetha Somasundaram, Akshat Gupta et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17368) · [PDF](https://arxiv.org/pdf/2610.17368) |
| 2026-10-12 | **MLAfication: Efficiently Enabling High-Fidelity MLA for Modern LLMs**<br><sub>Zile Wang, Zhide Xie, Tao Ji</sub> | [arXiv](https://arxiv.org/abs/2610.17202) · [PDF](https://arxiv.org/pdf/2610.17202) · [Code](https://github.com/JT-Ushio/MLAfication) |
| 2026-10-12 | **Growing to See: Efficient Pretraining of Self-Supervised Vision Transformers**<br><sub>Amir Mohammad Karimi Mamaghan, Ferdinand Kapl, Andrea Dittadi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16817) · [PDF](https://arxiv.org/pdf/2610.16817) |
| 2026-10-12 | **StructZO: Structured Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning**<br><sub>Xuanlin Yang, Jia Li, Zhouchen Lin</sub> | [arXiv](https://arxiv.org/abs/2610.16451) · [PDF](https://arxiv.org/pdf/2610.16451) |
| 2026-10-11 | **Fast and Accurate: Improving Personalized LLM Performance by Semantic Concentration Inspired Workload Split between RAG and Fine-Tuning**<br><sub>Xingke Yang, Sicong Li, Lingfeng Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15921) · [PDF](https://arxiv.org/pdf/2610.15921) |
| 2026-10-11 | **Engram Injection: A Study of Temporal Validity in Parametric Language-Model Memory**<br><sub>Sam Siavoshian, Omar Ramadan, Amir K. Saeed et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15882) · [PDF](https://arxiv.org/pdf/2610.15882) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **141 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models**<br><sub>Bohan Sun, Zunhai Su, Xialie Zhuang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20503) · [PDF](https://arxiv.org/pdf/2610.20503) · [Code](https://github.com/StartLuxLabs/ReaDy) |
| 2026-10-14 | **FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding**<br><sub>Shuxuan Li, Jialiang Kang, Yanghao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20392) · [PDF](https://arxiv.org/pdf/2610.20392) |
| 2026-10-14 | **StreamErase: Towards Ultra-Fast Streaming Video Erasing**<br><sub>Zhuobai Dong, Xiaobing Tu, Xiantao Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20137) · [PDF](https://arxiv.org/pdf/2610.20137) |
| 2026-10-14 | **PN-Mix: Pair-Norm Guided Mixed-Precision Key Cache Quantization for Efficient Long-Output LLM Inference**<br><sub>Gil Jae Song, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2610.19605) · [PDF](https://arxiv.org/pdf/2610.19605) |
| 2026-10-13 | **Joint Subspace Sparse Attention for Efficient Long-Context Decoding**<br><sub>Jiwon Song, Yoongon Kim, Jae-Joon Kim</sub> | [arXiv](https://arxiv.org/abs/2610.19026) · [PDF](https://arxiv.org/pdf/2610.19026) |
| 2026-10-13 | **Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs**<br><sub>Aimon Rahman, Joymallya Chakraborty, Vidit Bansal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18858) · [PDF](https://arxiv.org/pdf/2610.18858) |
| 2026-10-13 | **MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization**<br><sub>Yangchengyu Zhou, Zhiping Wu, Runchang Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18642) · [PDF](https://arxiv.org/pdf/2610.18642) · [Code](https://github.com/RL-MIND/MultiAlloc) |
| 2026-10-13 | **SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware**<br><sub>Jieyun Deng, Keming Hu, Yanghe Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18140) · [PDF](https://arxiv.org/pdf/2610.18140) |
| 2026-10-13 | **H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression**<br><sub>Or Ronai, Vladimir Kulikov, Tomer Michaeli</sub> | [arXiv](https://arxiv.org/abs/2610.18125) · [PDF](https://arxiv.org/pdf/2610.18125) |
| 2026-10-13 | **BELT : BEhavior-Aligned Low-Rank KV Cache Compression with Learned Top-k Rank Allocation**<br><sub>Yaoyang Liu, Shuwei Shen, Jincheng Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17966) · [PDF](https://arxiv.org/pdf/2610.17966) |
| 2026-10-13 | **CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation**<br><sub>Xiaoxue Wu, Xinyu Gao, Fang Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17926) · [PDF](https://arxiv.org/pdf/2610.17926) |
| 2026-10-12 | **Budgeted KV-Cache Repair for Evolving Contexts**<br><sub>Han Yu, Wenhui Zhu, Jincheng Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17338) · [PDF](https://arxiv.org/pdf/2610.17338) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **100 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **Speculative Sampling in Interactive Video Generation**<br><sub>Yubo Huang, Yuxuan Zhang, Jiaming Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20556) · [PDF](https://arxiv.org/pdf/2610.20556) |
| 2026-10-14 | **FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding**<br><sub>Shuxuan Li, Jialiang Kang, Yanghao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20392) · [PDF](https://arxiv.org/pdf/2610.20392) |
| 2026-10-14 | **Are We Overthinking One-Step Generation?**<br><sub>Woobin Park, Jaeyeon Kim, Yilun Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20331) · [PDF](https://arxiv.org/pdf/2610.20331) · [Code](https://github.com/JaeyeonKim01/priming) |
| 2026-10-13 | **SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models**<br><sub>Yuqi Huang, Xingyao Li, Yunlong Hou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18735) · [PDF](https://arxiv.org/pdf/2610.18735) |
| 2026-10-13 | **Compare to Correct: Pairwise-Guided Logit Adjustment for LLM Test-Time Scaling**<br><sub>Cong Hua, Qianqian Xu, Zitai Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18583) · [PDF](https://arxiv.org/pdf/2610.18583) |
| 2026-10-13 | **RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions**<br><sub>Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17867) · [PDF](https://arxiv.org/pdf/2610.17867) |
| 2026-10-13 | **Diff Diffusion: Predicting Edit Paths with Diffusion Models for Efficient Code Editing**<br><sub>Xiaolong Xu, Hao Jiang, Bo Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17831) · [PDF](https://arxiv.org/pdf/2610.17831) |
| 2026-10-12 | **SchemaWeaver: Accelerating On-Device Mobile Agentic AI via Schema-Guided Parallel LLM Decoding**<br><sub>Boyuan Yang, Wei Gao</sub> | [arXiv](https://arxiv.org/abs/2610.17436) · [PDF](https://arxiv.org/pdf/2610.17436) |
| 2026-10-12 | **PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models**<br><sub>Quentin Fruytier, Anton Xue, Sanjay Shakkottai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17375) · [PDF](https://arxiv.org/pdf/2610.17375) · [Code](https://github.com/Quentin-Fruytier/PIG-DLM-release) |
| 2026-10-12 | **Intent-Triggered Anchoring for Multi-Token Format Units in Parallel Decoding of Diffusion Language Models**<br><sub>Junhyeok Lee, Kyu Sung Choi</sub> | [arXiv](https://arxiv.org/abs/2610.16516) · [PDF](https://arxiv.org/pdf/2610.16516) |
| 2026-10-09 | **SWEAR: Section-Wise Efficient Audio Reasoning via Self-Rated Difficulty**<br><sub>Yixuan Li, Minghao Lv, Xuenan Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13081) · [PDF](https://arxiv.org/pdf/2610.13081) |
| 2026-10-09 | **Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding**<br><sub>Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12939) · [PDF](https://arxiv.org/pdf/2610.12939) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **165 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **MemDuet: Learning Dual-Process Memory for Long-Context Reasoning**<br><sub>Jiangcheng Song, Haodong Jing, Yulin Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19928) · [PDF](https://arxiv.org/pdf/2610.19928) |
| 2026-10-14 | **JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs**<br><sub>Daijin Hu</sub> | [arXiv](https://arxiv.org/abs/2610.19822) · [PDF](https://arxiv.org/pdf/2610.19822) |
| 2026-10-14 | **Scaling LLM Inference via Parallelism: Throughput-Latency Trade-off**<br><sub>Javad Mirzaei, Jeebak Mitra</sub> | [arXiv](https://arxiv.org/abs/2610.19405) · [PDF](https://arxiv.org/pdf/2610.19405) |
| 2026-10-13 | **Rethinking Quality in Large Language Model Routing: Security-Conditioned Model-and-Budget Selection**<br><sub>Yichi Zhang, Zhenxiang Huang, Yuyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18566) · [PDF](https://arxiv.org/pdf/2610.18566) |
| 2026-10-13 | **FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving**<br><sub>Yunfei Feng, Jingkai He, Shiqi Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18451) · [PDF](https://arxiv.org/pdf/2610.18451) |
| 2026-10-13 | **RadixFlow: Filling Execution Bubbles in Prefix-Cached Hybrid LLM Serving**<br><sub>Huihao Jing, Wenbin Hu, Shaojin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18143) · [PDF](https://arxiv.org/pdf/2610.18143) |
| 2026-10-13 | **HaloBlock: Faster and Better Decoding for Diffusion Large Language Models**<br><sub>Zhaohui Zheng, Chenhang He, Jinrui Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17948) · [PDF](https://arxiv.org/pdf/2610.17948) · [Code](https://github.com/PolyU-VCLab/HaloBlock) |
| 2026-10-13 | **Batch-Paced: Fixed-Budget Batch Decoding in Discrete Diffusion Language Models**<br><sub>Shuai Zhang, Zhanchao Zhou, Huachuan Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17917) · [PDF](https://arxiv.org/pdf/2610.17917) |
| 2026-10-13 | **Quota-Based Aging for Prediction-Guided Scheduling in LLM Serving**<br><sub>Hanzhi Zhang, Anxuan Che, Hang Qi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17795) · [PDF](https://arxiv.org/pdf/2610.17795) |
| 2026-10-13 | **MemAct: Streaming Spatial Understanding with Memory and Active Exploration**<br><sub>Yuxi Wei, Wei Huang, Qirui Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17640) · [PDF](https://arxiv.org/pdf/2610.17640) |
| 2026-10-12 | **Efficient Resource-Shiftable RL Post-training with Generative Rewards**<br><sub>Yanfeng Zhao, Haoyang Li, Sheng Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16866) · [PDF](https://arxiv.org/pdf/2610.16866) |
| 2026-10-12 | **Prorsa: Unleashing the Potential of Prefill-Decode Disaggregation in Agentic Reinforcement Learning**<br><sub>Chiheng Lou, Xiangwei Deng, Bangjun Xiao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16592) · [PDF](https://arxiv.org/pdf/2610.16592) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **82 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **ForkGRPO: Efficient Exploration and Fine-Grained Credit Assignment for Diffusion Language Models**<br><sub>Zhaoyan Jia, Chengwei Zhou, Gourav Datta et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19408) · [PDF](https://arxiv.org/pdf/2610.19408) |
| 2026-10-13 | **Long-horizon Video Generation with Slot Memory Addressed By Region Tokens**<br><sub>Eren Cetin, Julius Erbach, Vukasin Bozic et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19257) · [PDF](https://arxiv.org/pdf/2610.19257) |
| 2026-10-13 | **H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression**<br><sub>Or Ronai, Vladimir Kulikov, Tomer Michaeli</sub> | [arXiv](https://arxiv.org/abs/2610.18125) · [PDF](https://arxiv.org/pdf/2610.18125) |
| 2026-10-13 | **LinMorph: Learning to Morph Weights for Efficient Video DiT Linearization**<br><sub>Lingyi Long, Congyue Zhao, Xiaoou Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17914) · [PDF](https://arxiv.org/pdf/2610.17914) |
| 2026-10-12 | **PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models**<br><sub>Quentin Fruytier, Anton Xue, Sanjay Shakkottai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17375) · [PDF](https://arxiv.org/pdf/2610.17375) · [Code](https://github.com/Quentin-Fruytier/PIG-DLM-release) |
| 2026-10-12 | **MARS: Systematic Multi-Level Acceleration for World Action Models**<br><sub>Zengyuan Zuo, Yongchang Zhang, Guangyu Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17141) · [PDF](https://arxiv.org/pdf/2610.17141) · [Code](https://github.com/PKU-VaLuE-Lab/MARS) |
| 2026-10-12 | **Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration**<br><sub>Jiyue Jiang, Zhiyu Huo, Yuhan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16545) · [PDF](https://arxiv.org/pdf/2610.16545) · [Code](https://github.com/jiangjyjy/AlignCache) |
| 2026-10-12 | **Tikhonov-Stabilized Bezier Representation Forecasting for Training-free Diffusion Acceleration**<br><sub>Lei Zhu, Mujie Lin, Ruochong Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16448) · [PDF](https://arxiv.org/pdf/2610.16448) |
| 2026-10-11 | **Frequency-Step Cache: Separating Synchronization and Repair for Efficient Autoregressive Video Diffusion**<br><sub>Kerry Xu, Param Misra, Zachary Stenglein et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15922) · [PDF](https://arxiv.org/pdf/2610.15922) |
| 2026-10-11 | **TempoKV: Predictive KV Cache Quantization for Autoregressive Video Generation**<br><sub>Jiahui Hu, Weile Mo, Peiliang Cai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15324) · [PDF](https://arxiv.org/pdf/2610.15324) |
| 2026-10-10 | **LightVAE: Towards Compact and Efficient Video Autoencoders**<br><sub>Shiqiao Gu, Yang Yong, Fengjun Zhong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.14726) · [PDF](https://arxiv.org/pdf/2610.14726) · [Code](https://github.com/ModelTC/LightVAE) |
| 2026-10-10 | **PixARG: Pixel-Asynchronous Retrieval-Augmented Diffusion for Fast and Realistic Image Generation**<br><sub>Zewei Xin, Qinya Li, Chaoyue Niu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.14713) · [PDF](https://arxiv.org/pdf/2610.14713) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **137 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-14 | **Speculative Sampling in Interactive Video Generation**<br><sub>Yubo Huang, Yuxuan Zhang, Jiaming Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20556) · [PDF](https://arxiv.org/pdf/2610.20556) |
| 2026-10-14 | **Generative Representation Learning for Scalable Latent Tokenization**<br><sub>Alan Baade, Kyle Sargent, Vincent Sitzmann et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20533) · [PDF](https://arxiv.org/pdf/2610.20533) |
| 2026-10-14 | **Are We Overthinking One-Step Generation?**<br><sub>Woobin Park, Jaeyeon Kim, Yilun Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20331) · [PDF](https://arxiv.org/pdf/2610.20331) · [Code](https://github.com/JaeyeonKim01/priming) |
| 2026-10-14 | **StreamErase: Towards Ultra-Fast Streaming Video Erasing**<br><sub>Zhuobai Dong, Xiaobing Tu, Xiantao Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20137) · [PDF](https://arxiv.org/pdf/2610.20137) |
| 2026-10-14 | **RepForcing: Representation-Space Initialization for Autoregressive Video Distillation**<br><sub>Siming Fu, Zheming Fu, Lianrui Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20111) · [PDF](https://arxiv.org/pdf/2610.20111) |
| 2026-10-14 | **DeBoneDiT: Depth-Driven Conditional Bridge Diffusion Transformers for Bone Suppression in Chest X-Ray Images**<br><sub>Yifei Sun, Fenglei Fan, Junhao Jia et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19466) · [PDF](https://arxiv.org/pdf/2610.19466) |
| 2026-10-13 | **Data-free Multistep Diffusion Distillation**<br><sub>Ngoc Duy Tran, Kien Do, Duc Thanh Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19305) · [PDF](https://arxiv.org/pdf/2610.19305) |
| 2026-10-13 | **Long-horizon Video Generation with Slot Memory Addressed By Region Tokens**<br><sub>Eren Cetin, Julius Erbach, Vukasin Bozic et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19257) · [PDF](https://arxiv.org/pdf/2610.19257) |
| 2026-10-13 | **GAD: Geometry Attention Distillation for Consistent Video Generation**<br><sub>Junfeng Ni, Ziyu Zhu, Fan Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18779) · [PDF](https://arxiv.org/pdf/2610.18779) |
| 2026-10-13 | **Recasting DiT for Extreme Image Compression with Hierarchical Visual Priors**<br><sub>Yunuo Chen, Jingnan Gao, Bing He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18607) · [PDF](https://arxiv.org/pdf/2610.18607) |
| 2026-10-13 | **Simplifying and Improving On-Policy Distillation for Few-Step Diffusion**<br><sub>Jiawei Zhang, Ziyu Wan, Nanye Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18472) · [PDF](https://arxiv.org/pdf/2610.18472) |
| 2026-10-13 | **Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs**<br><sub>Peiran Yin, Hao Wu, Zihao Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18399) · [PDF](https://arxiv.org/pdf/2610.18399) · [Code](https://github.com/EIT-NLP/Bifocal) |

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
