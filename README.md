# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-19 14:15 CST** · **1103 unique papers** · Newest submission: **2026-10-16**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 170 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 158 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 376 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 108 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 156 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 109 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 173 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 91 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 150 |

## Newly indexed · 2026-10-19

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **DLite: History-free Speculative Decoding for Agentic AI**<br><sub>Jiaming Xu, Hanzhen Wang, Tianlang Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23787) · [PDF](https://arxiv.org/pdf/2610.23787) |
| 2026-10-16 | **Blitz: Accelerating the Diffusion Modules of AlphaFold3 and Boltz-2**<br><sub>Vinay Saji Mathew, Soundar Kumara, Gretta Kellogg et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23703) · [PDF](https://arxiv.org/pdf/2610.23703) |
| 2026-10-16 | **PreciseEdit: Strong Yet Stable Semantic Transport for One-Step Image Editing**<br><sub>Jingyi Wang, Xiao Lu</sub> | [arXiv](https://arxiv.org/abs/2610.23535) · [PDF](https://arxiv.org/pdf/2610.23535) |
| 2026-10-16 | **HBFSim: A Simulator for Exploring HBF in Memory Hierarchies for LLMs**<br><sub>Jinheng Li, Guosheng Wang, Hongchao Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23503) · [PDF](https://arxiv.org/pdf/2610.23503) · [Code](https://github.com/FlashLabAE/HBFSim) |
| 2026-10-16 | **When Evidence Vanishes: Distilling Visual-Evidence Dependency in Medical Vision-Language Models**<br><sub>Qizhen Lan, Yiling Ma, Ruiqi Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23469) · [PDF](https://arxiv.org/pdf/2610.23469) |
| 2026-10-16 | **CatchUp: Depth-Aware Re-Admission of Visual Tokens for Efficient Large Vision-Language Models**<br><sub>Eunju Park, Uiwon Hwang</sub> | [arXiv](https://arxiv.org/abs/2610.23324) · [PDF](https://arxiv.org/pdf/2610.23324) · [Code](https://github.com/pej0918/CatchUp) |
| 2026-10-16 | **Sample, Mix, or Verify? Allocating Test-Time Compute under Imperfect Verifiers**<br><sub>Srinivasan Iyengar</sub> | [arXiv](https://arxiv.org/abs/2610.23255) · [PDF](https://arxiv.org/pdf/2610.23255) |
| 2026-10-16 | **Kingfisher: Fast Personalized Visual Autoregressive Generation via Scale-Aware Prompt-Conditioned Scale Decomposition**<br><sub>Dinh-Khoi Vo, Akihiro Sugimoto, Minh-Triet Tran et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23238) · [PDF](https://arxiv.org/pdf/2610.23238) |
| 2026-10-16 | **MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation**<br><sub>Yuhan Sun, Jiaxin Zhao, Yongdong Luo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23234) · [PDF](https://arxiv.org/pdf/2610.23234) |
| 2026-10-16 | **ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling**<br><sub>Yuki Otsuka, Daisuke Oba, Naoaki Okazaki</sub> | [arXiv](https://arxiv.org/abs/2610.23225) · [PDF](https://arxiv.org/pdf/2610.23225) · [Code](https://github.com/Yuki-Ots/ReLaDrift) |
| 2026-10-16 | **Not All Test-Time Compute Is Evidence: Model-Specific Bias in LLM Reasoning**<br><sub>Ming Shen, Tianjun Yao</sub> | [arXiv](https://arxiv.org/abs/2610.23213) · [PDF](https://arxiv.org/pdf/2610.23213) |
| 2026-10-16 | **A Stronger Teacher Within: Strengthening MoE Models via On-Policy Bidirectional Distillation**<br><sub>Haoyu Chen, Jun Bai, Yang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23185) · [PDF](https://arxiv.org/pdf/2610.23185) |
| 2026-10-16 | **Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning**<br><sub>Heming Zou, Qi Wang, Yixiu Mao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23181) · [PDF](https://arxiv.org/pdf/2610.23181) |
| 2026-10-16 | **Local proxies for memory-efficient training**<br><sub>Wu S. Zihan, Brian A. Yuan, Guillaume Bellec</sub> | [arXiv](https://arxiv.org/abs/2610.23145) · [PDF](https://arxiv.org/pdf/2610.23145) |
| 2026-10-16 | **BaGuaLu-2: Taming Dynamic Memory Fluctuation for Efficient MoE Model Training over 10,000 GPUs**<br><sub>Mingshu Zhai, Minkun Guo, Hongrui Lian et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23064) · [PDF](https://arxiv.org/pdf/2610.23064) |
| 2026-10-16 | **DIFFLET: A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium**<br><sub>Bin Ma, Min Yu, Vijay Kodamalla et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23047) · [PDF](https://arxiv.org/pdf/2610.23047) |
| 2026-10-16 | **Efficient CPU-GPU collaborative MoE inference via Adaptive Expert Assignment**<br><sub>Wenhui Lv, Yunming Liao, Hongli Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23006) · [PDF](https://arxiv.org/pdf/2610.23006) |
| 2026-10-16 | **Prism Attention: Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference**<br><sub>Zhenxu Tian, Kebin Liu, Zhengwu Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22985) · [PDF](https://arxiv.org/pdf/2610.22985) |
| 2026-10-16 | **Sink-Sparse Hybrid Attention for Efficient Inference in T2I/T2V Diffusion Transformers**<br><sub>Bingxin Xing, Yu Zhang, Jiatong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22975) · [PDF](https://arxiv.org/pdf/2610.22975) |
| 2026-10-16 | **Sep-Latent: Separator Tokens as Natural Compression Anchors for Implicit Reasoning**<br><sub>Yinlong Xu, Jianfeng Huang, Zhengdong Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22924) · [PDF](https://arxiv.org/pdf/2610.22924) |

[View all 33 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **170 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **BS-Spec: BFP-Based Bit-Sharing for Self-Speculative LLM Decoding with LUT-Driven Mixed-Precision Acceleration**<br><sub>Jiwoo Kim, Gunho Park, Sunwoo Yoo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22877) · [PDF](https://arxiv.org/pdf/2610.22877) |
| 2026-10-15 | **Noise-shaped Sampling and Annealing for Scalable On-the-edge Training of Binary and Ternary AI Models**<br><sub>Zihao Chen, Zhili Xiao, Rui-Jie Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22621) · [PDF](https://arxiv.org/pdf/2610.22621) |
| 2026-10-15 | **BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks**<br><sub>Max Zhu, Bohang Sun, Pietro Lio et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22256) · [PDF](https://arxiv.org/pdf/2610.22256) |
| 2026-10-15 | **When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill**<br><sub>Muhammad Ibrahim</sub> | [arXiv](https://arxiv.org/abs/2610.21500) · [PDF](https://arxiv.org/pdf/2610.21500) |
| 2026-10-15 | **HyCo: Hybrid Drafting for Cost-Efficient Mobile-Cloud Speculative Decoding**<br><sub>Hanbin Bae, Heejin Choi, Joohyung Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21436) · [PDF](https://arxiv.org/pdf/2610.21436) |
| 2026-10-15 | **Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference**<br><sub>Sunghyun Wee, Geunjae Choi, Hyeonjin Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21257) · [PDF](https://arxiv.org/pdf/2610.21257) |
| 2026-10-14 | **Task-Phase-Conditioned Expert Routing Is Not a Reliable Proxy for Quantization Sensitivity in MoE FFN Tensors**<br><sub>Yifan Liu</sub> | [arXiv](https://arxiv.org/abs/2610.20826) · [PDF](https://arxiv.org/pdf/2610.20826) |
| 2026-10-14 | **Beyond Expert Rankings: Contrast Calibration for Mixed-Precision MoE Quantization**<br><sub>Renjie Xie, Juncheng Yang, Aoting Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20353) · [PDF](https://arxiv.org/pdf/2610.20353) |
| 2026-10-14 | **SpectrumQuant: Spectrum Alignment for LLM Quantization**<br><sub>Dwaipayan Haldar, Indranil Patra, Azhar Yousuf et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20303) · [PDF](https://arxiv.org/pdf/2610.20303) |
| 2026-10-14 | **Multimodal Medical Image Parsing with Task-Specific Low-Rank Adapters**<br><sub>Taha Sabir, Alberto Montero Molina, Thinh Quang Ly et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19901) · [PDF](https://arxiv.org/pdf/2610.19901) · [Code](https://github.com/TahaSabir0/FLARE26-Hexapus) |
| 2026-10-14 | **MFSA: A Multi-Format Systolic Array with Native Micro Scaling Support**<br><sub>Jiayi Wang, Kearnan Bishop, Ang Li</sub> | [arXiv](https://arxiv.org/abs/2610.19645) · [PDF](https://arxiv.org/pdf/2610.19645) |
| 2026-10-14 | **PN-Mix: Pair-Norm Guided Mixed-Precision Key Cache Quantization for Efficient Long-Output LLM Inference**<br><sub>Gil Jae Song, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2610.19605) · [PDF](https://arxiv.org/pdf/2610.19605) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **158 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **CatchUp: Depth-Aware Re-Admission of Visual Tokens for Efficient Large Vision-Language Models**<br><sub>Eunju Park, Uiwon Hwang</sub> | [arXiv](https://arxiv.org/abs/2610.23324) · [PDF](https://arxiv.org/pdf/2610.23324) · [Code](https://github.com/pej0918/CatchUp) |
| 2026-10-16 | **Prism Attention: Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference**<br><sub>Zhenxu Tian, Kebin Liu, Zhengwu Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22985) · [PDF](https://arxiv.org/pdf/2610.22985) |
| 2026-10-16 | **Uncertainty-Aware Budget Allocation for Efficient LLM Tree Search**<br><sub>Jianguo Huang, Zhiyi Lyu, Fuxiang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22858) · [PDF](https://arxiv.org/pdf/2610.22858) |
| 2026-10-16 | **Prune the Leaky Neurons: Mitigating Private Data Leakage in Fine-Tuned LLMs via Joint-Embedding-Guided Pruning**<br><sub>Mohamed Shaaban, Mohamed Elmahallawy</sub> | [arXiv](https://arxiv.org/abs/2610.22792) · [PDF](https://arxiv.org/pdf/2610.22792) |
| 2026-10-15 | **MedSTP: Preserving Subspace and Transition Evidence for Medical VQA Token Pruning**<br><sub>Mengchen Fan, Qizhen Lan, Xi Xiao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22751) · [PDF](https://arxiv.org/pdf/2610.22751) |
| 2026-10-15 | **Pearl-Chat: Engineering a native Luganda language model from first principles in JAX and Flax NNX**<br><sub>Wesley Kambale, Roland Sankara</sub> | [arXiv](https://arxiv.org/abs/2610.22529) · [PDF](https://arxiv.org/pdf/2610.22529) |
| 2026-10-15 | **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**<br><sub>SeungJu Cha, Ye-Chan Kim, HyunGee Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22370) · [PDF](https://arxiv.org/pdf/2610.22370) · [Code](https://github.com/SeungJuCha/DaTMe) |
| 2026-10-15 | **Calibration Language Shapes Block-Influence Pruning in Multilingual Language Models**<br><sub>Vedant Pandhare, Piyush Dhoka</sub> | [arXiv](https://arxiv.org/abs/2610.21383) · [PDF](https://arxiv.org/pdf/2610.21383) · [Code](https://github.com/VedantPandhare/Language-Balanced-Depth-Pruning-of-Small-Multilingual-LLMs.git) |
| 2026-10-15 | **Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search**<br><sub>Yun Dai, Yuyun Chen, Jiarui Wen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21129) · [PDF](https://arxiv.org/pdf/2610.21129) |
| 2026-10-14 | **STP-GUI: Spatially-Aware Token Pruning for Efficient Web-GUI Agents**<br><sub>Shuo Wang, Sifan Zhou, Xiaobo Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20390) · [PDF](https://arxiv.org/pdf/2610.20390) |
| 2026-10-14 | **Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility**<br><sub>Salima Lamsiyah, Adelaide Danilov, Oleksandr Marchenko Breneur et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20139) · [PDF](https://arxiv.org/pdf/2610.20139) |
| 2026-10-14 | **MemDuet: Learning Dual-Process Memory for Long-Context Reasoning**<br><sub>Jiangcheng Song, Haodong Jing, Yulin Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19928) · [PDF](https://arxiv.org/pdf/2610.19928) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **376 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **Blitz: Accelerating the Diffusion Modules of AlphaFold3 and Boltz-2**<br><sub>Vinay Saji Mathew, Soundar Kumara, Gretta Kellogg et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23703) · [PDF](https://arxiv.org/pdf/2610.23703) |
| 2026-10-16 | **PreciseEdit: Strong Yet Stable Semantic Transport for One-Step Image Editing**<br><sub>Jingyi Wang, Xiao Lu</sub> | [arXiv](https://arxiv.org/abs/2610.23535) · [PDF](https://arxiv.org/pdf/2610.23535) |
| 2026-10-16 | **When Evidence Vanishes: Distilling Visual-Evidence Dependency in Medical Vision-Language Models**<br><sub>Qizhen Lan, Yiling Ma, Ruiqi Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23469) · [PDF](https://arxiv.org/pdf/2610.23469) |
| 2026-10-16 | **MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation**<br><sub>Yuhan Sun, Jiaxin Zhao, Yongdong Luo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23234) · [PDF](https://arxiv.org/pdf/2610.23234) |
| 2026-10-16 | **ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling**<br><sub>Yuki Otsuka, Daisuke Oba, Naoaki Okazaki</sub> | [arXiv](https://arxiv.org/abs/2610.23225) · [PDF](https://arxiv.org/pdf/2610.23225) · [Code](https://github.com/Yuki-Ots/ReLaDrift) |
| 2026-10-16 | **A Stronger Teacher Within: Strengthening MoE Models via On-Policy Bidirectional Distillation**<br><sub>Haoyu Chen, Jun Bai, Yang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23185) · [PDF](https://arxiv.org/pdf/2610.23185) |
| 2026-10-16 | **Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning**<br><sub>Heming Zou, Qi Wang, Yixiu Mao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23181) · [PDF](https://arxiv.org/pdf/2610.23181) |
| 2026-10-16 | **Local proxies for memory-efficient training**<br><sub>Wu S. Zihan, Brian A. Yuan, Guillaume Bellec</sub> | [arXiv](https://arxiv.org/abs/2610.23145) · [PDF](https://arxiv.org/pdf/2610.23145) |
| 2026-10-16 | **Sep-Latent: Separator Tokens as Natural Compression Anchors for Implicit Reasoning**<br><sub>Yinlong Xu, Jianfeng Huang, Zhengdong Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22924) · [PDF](https://arxiv.org/pdf/2610.22924) |
| 2026-10-16 | **COMET: Decoupled Distillation, Routing, and Capacity Control for Task-Agnostic Continual Vision--Language Learning**<br><sub>Seungyoon Woo, Keonhee Park, Gunhee Kim</sub> | [arXiv](https://arxiv.org/abs/2610.22907) · [PDF](https://arxiv.org/pdf/2610.22907) |
| 2026-10-15 | **FlashControl: One-Step Controllable Generator via Distillation-Friendly Single-Stream Teachers**<br><sub>Ngan Nguyen, Dung Nguyen, Quan Dao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22537) · [PDF](https://arxiv.org/pdf/2610.22537) |
| 2026-10-15 | **Predicting Privileged Information Effectiveness for On-Policy Self-Distillation**<br><sub>Kaijian Zou, Emiliano Penaloza, MohammadHossein Rezaei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22512) · [PDF](https://arxiv.org/pdf/2610.22512) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **108 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **Kingfisher: Fast Personalized Visual Autoregressive Generation via Scale-Aware Prompt-Conditioned Scale Decomposition**<br><sub>Dinh-Khoi Vo, Akihiro Sugimoto, Minh-Triet Tran et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23238) · [PDF](https://arxiv.org/pdf/2610.23238) |
| 2026-10-16 | **Local proxies for memory-efficient training**<br><sub>Wu S. Zihan, Brian A. Yuan, Guillaume Bellec</sub> | [arXiv](https://arxiv.org/abs/2610.23145) · [PDF](https://arxiv.org/pdf/2610.23145) |
| 2026-10-16 | **BaGuaLu-2: Taming Dynamic Memory Fluctuation for Efficient MoE Model Training over 10,000 GPUs**<br><sub>Mingshu Zhai, Minkun Guo, Hongrui Lian et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23064) · [PDF](https://arxiv.org/pdf/2610.23064) |
| 2026-10-15 | **BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks**<br><sub>Max Zhu, Bohang Sun, Pietro Lio et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22256) · [PDF](https://arxiv.org/pdf/2610.22256) |
| 2026-10-15 | **WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression**<br><sub>Yue Yu, Bowei Kang, Changsheng Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22232) · [PDF](https://arxiv.org/pdf/2610.22232) |
| 2026-10-15 | **Memory as Weights: Internalizing Long-Term History for Streaming Videos**<br><sub>Zhuoming Liu, Jinhong Lin, Lin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22070) · [PDF](https://arxiv.org/pdf/2610.22070) |
| 2026-10-15 | **ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training**<br><sub>Yukun Tian, Junwei Su, Haofeng Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21640) · [PDF](https://arxiv.org/pdf/2610.21640) |
| 2026-10-15 | **Translation Circuit Discovery and Targeted Optimization for Low-Resource Multilingual Translation**<br><sub>Atai Waris Khan, Abdullah Mazhar, Raghu Kumar et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21456) · [PDF](https://arxiv.org/pdf/2610.21456) |
| 2026-10-14 | **Multimodal Medical Image Parsing with Task-Specific Low-Rank Adapters**<br><sub>Taha Sabir, Alberto Montero Molina, Thinh Quang Ly et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19901) · [PDF](https://arxiv.org/pdf/2610.19901) · [Code](https://github.com/TahaSabir0/FLARE26-Hexapus) |
| 2026-10-13 | **DUALVIEW: Leveraging Broad and Output-Specific Evidence for LLM-based Multi-Output Text Regression**<br><sub>Yiheng Su, Junyi Jessy Li, Matthew Lease</sub> | [arXiv](https://arxiv.org/abs/2610.19206) · [PDF](https://arxiv.org/pdf/2610.19206) |
| 2026-10-13 | **Discovering Undisclosed Concepts in LoRA Adapters for Diffusion-Based AIGC Models**<br><sub>Yupeng Qiu, Han Fang, Dhananjai Sharma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18990) · [PDF](https://arxiv.org/pdf/2610.18990) |
| 2026-10-13 | **Unlocking Token Rewards via Training-Free Reward Attribution**<br><sub>Sitong Wu, Haoru Tan, Bin Xia et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18704) · [PDF](https://arxiv.org/pdf/2610.18704) · [Code](https://github.com/stonewst/P2T) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **156 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **HBFSim: A Simulator for Exploring HBF in Memory Hierarchies for LLMs**<br><sub>Jinheng Li, Guosheng Wang, Hongchao Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23503) · [PDF](https://arxiv.org/pdf/2610.23503) · [Code](https://github.com/FlashLabAE/HBFSim) |
| 2026-10-16 | **Prism Attention: Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference**<br><sub>Zhenxu Tian, Kebin Liu, Zhengwu Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22985) · [PDF](https://arxiv.org/pdf/2610.22985) |
| 2026-10-16 | **FederatedBytes: Tokenizer-Free, Byte-Level Small Language Models for Efficient Multimodal Federated Learning**<br><sub>Ali Sarabadani, Massimo Piccardi, Mehran Abolhasan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22906) · [PDF](https://arxiv.org/pdf/2610.22906) |
| 2026-10-16 | **BS-Spec: BFP-Based Bit-Sharing for Self-Speculative LLM Decoding with LUT-Driven Mixed-Precision Acceleration**<br><sub>Jiwoo Kim, Gunho Park, Sunwoo Yoo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22877) · [PDF](https://arxiv.org/pdf/2610.22877) |
| 2026-10-15 | **SAFETYEDIT: Sparse Internal Targets with Prompt-Wide Control for LLM Jailbreak Backdoors**<br><sub>Yutong Ke, Yansu Wang, Zeyu Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22640) · [PDF](https://arxiv.org/pdf/2610.22640) |
| 2026-10-15 | **MemLLM: End-to-end In-Storage Acceleration of On-device Retrieval-Augmented Generation using Precomputed KV Caches**<br><sub>Seungkwan Kang, Hyungseok Ko, Heemin Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22579) · [PDF](https://arxiv.org/pdf/2610.22579) |
| 2026-10-15 | **Velox: Spatial Memory Makes World Models Efficient**<br><sub>Qiuhong Shen, Shizun Wang, Xinchao Wang</sub> | [arXiv](https://arxiv.org/abs/2610.22311) · [PDF](https://arxiv.org/pdf/2610.22311) |
| 2026-10-15 | **Efficient KV Cache Migration for Geo-Distributed LLM Inference in Collaborative Edge Computing**<br><sub>Mingjin Zhang, Jiannong Cao, Tao Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22172) · [PDF](https://arxiv.org/pdf/2610.22172) |
| 2026-10-15 | **DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction**<br><sub>Aozhong Zhang, Selcuk Gurses, Yanxia Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22130) · [PDF](https://arxiv.org/pdf/2610.22130) |
| 2026-10-15 | **Augment the Cache, Replace the Activation: A 2x2 Study of Internal-State Sharing**<br><sub>Adam Deng, Shicheng Liu, Yada Zhu</sub> | [arXiv](https://arxiv.org/abs/2610.22026) · [PDF](https://arxiv.org/pdf/2610.22026) |
| 2026-10-15 | **When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill**<br><sub>Muhammad Ibrahim</sub> | [arXiv](https://arxiv.org/abs/2610.21500) · [PDF](https://arxiv.org/pdf/2610.21500) |
| 2026-10-15 | **FlashAttention with Statistics: Low-Overhead Attention Features for Compact Hallucination Detectors**<br><sub>Andrei Volodichev, Maksim Savichev, Nikita Sviridov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21483) · [PDF](https://arxiv.org/pdf/2610.21483) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **109 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **DLite: History-free Speculative Decoding for Agentic AI**<br><sub>Jiaming Xu, Hanzhen Wang, Tianlang Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23787) · [PDF](https://arxiv.org/pdf/2610.23787) |
| 2026-10-16 | **Sample, Mix, or Verify? Allocating Test-Time Compute under Imperfect Verifiers**<br><sub>Srinivasan Iyengar</sub> | [arXiv](https://arxiv.org/abs/2610.23255) · [PDF](https://arxiv.org/pdf/2610.23255) |
| 2026-10-16 | **ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling**<br><sub>Yuki Otsuka, Daisuke Oba, Naoaki Okazaki</sub> | [arXiv](https://arxiv.org/abs/2610.23225) · [PDF](https://arxiv.org/pdf/2610.23225) · [Code](https://github.com/Yuki-Ots/ReLaDrift) |
| 2026-10-16 | **Not All Test-Time Compute Is Evidence: Model-Specific Bias in LLM Reasoning**<br><sub>Ming Shen, Tianjun Yao</sub> | [arXiv](https://arxiv.org/abs/2610.23213) · [PDF](https://arxiv.org/pdf/2610.23213) |
| 2026-10-16 | **BS-Spec: BFP-Based Bit-Sharing for Self-Speculative LLM Decoding with LUT-Driven Mixed-Precision Acceleration**<br><sub>Jiwoo Kim, Gunho Park, Sunwoo Yoo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22877) · [PDF](https://arxiv.org/pdf/2610.22877) |
| 2026-10-15 | **On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction**<br><sub>Eliezer Shlomi, Eliron Rahimi, Avi Mendelson et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22543) · [PDF](https://arxiv.org/pdf/2610.22543) |
| 2026-10-15 | **Query-Efficient Rejection Sampling for Parallel Masked Diffusion**<br><sub>Shiyuan Zhang, Xuheng Li, Qiwei Di et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22238) · [PDF](https://arxiv.org/pdf/2610.22238) |
| 2026-10-15 | **LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models**<br><sub>Zixuan Liu, Nan Xue, Rui Bao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21594) · [PDF](https://arxiv.org/pdf/2610.21594) |
| 2026-10-15 | **HyCo: Hybrid Drafting for Cost-Efficient Mobile-Cloud Speculative Decoding**<br><sub>Hanbin Bae, Heejin Choi, Joohyung Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21436) · [PDF](https://arxiv.org/pdf/2610.21436) |
| 2026-10-14 | **Speculative Sampling in Interactive Video Generation**<br><sub>Yubo Huang, Yuxuan Zhang, Jiaming Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20556) · [PDF](https://arxiv.org/pdf/2610.20556) |
| 2026-10-14 | **FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding**<br><sub>Shuxuan Li, Jialiang Kang, Yanghao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20392) · [PDF](https://arxiv.org/pdf/2610.20392) |
| 2026-10-14 | **Are We Overthinking One-Step Generation?**<br><sub>Woobin Park, Jaeyeon Kim, Yilun Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20331) · [PDF](https://arxiv.org/pdf/2610.20331) · [Code](https://github.com/JaeyeonKim01/priming) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **173 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **HBFSim: A Simulator for Exploring HBF in Memory Hierarchies for LLMs**<br><sub>Jinheng Li, Guosheng Wang, Hongchao Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23503) · [PDF](https://arxiv.org/pdf/2610.23503) · [Code](https://github.com/FlashLabAE/HBFSim) |
| 2026-10-16 | **Efficient CPU-GPU collaborative MoE inference via Adaptive Expert Assignment**<br><sub>Wenhui Lv, Yunming Liao, Hongli Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23006) · [PDF](https://arxiv.org/pdf/2610.23006) |
| 2026-10-16 | **BS-Spec: BFP-Based Bit-Sharing for Self-Speculative LLM Decoding with LUT-Driven Mixed-Precision Acceleration**<br><sub>Jiwoo Kim, Gunho Park, Sunwoo Yoo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22877) · [PDF](https://arxiv.org/pdf/2610.22877) |
| 2026-10-15 | **Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing**<br><sub>Tianxiang Fei, Jiazheng Kang, Mao Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22196) · [PDF](https://arxiv.org/pdf/2610.22196) |
| 2026-10-15 | **When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill**<br><sub>Muhammad Ibrahim</sub> | [arXiv](https://arxiv.org/abs/2610.21500) · [PDF](https://arxiv.org/pdf/2610.21500) |
| 2026-10-15 | **PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems**<br><sub>Han Shen, Qifu Tyler Sun, Fanyang Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21390) · [PDF](https://arxiv.org/pdf/2610.21390) |
| 2026-10-15 | **From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models**<br><sub>Chaogui Gou</sub> | [arXiv](https://arxiv.org/abs/2610.21165) · [PDF](https://arxiv.org/pdf/2610.21165) |
| 2026-10-14 | **CascadeLedger: Counterfactual Auditing of Information and Resource Integrity in LLM Cascades**<br><sub>Miaobo Hu, Shuhao Hu, Xiaobo Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20668) · [PDF](https://arxiv.org/pdf/2610.20668) |
| 2026-10-14 | **MemDuet: Learning Dual-Process Memory for Long-Context Reasoning**<br><sub>Jiangcheng Song, Haodong Jing, Yulin Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19928) · [PDF](https://arxiv.org/pdf/2610.19928) |
| 2026-10-14 | **JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs**<br><sub>Daijin Hu</sub> | [arXiv](https://arxiv.org/abs/2610.19822) · [PDF](https://arxiv.org/pdf/2610.19822) |
| 2026-10-14 | **Scaling LLM Inference via Parallelism: Throughput-Latency Trade-off**<br><sub>Javad Mirzaei, Jeebak Mitra</sub> | [arXiv](https://arxiv.org/abs/2610.19405) · [PDF](https://arxiv.org/pdf/2610.19405) |
| 2026-10-13 | **Rethinking Quality in Large Language Model Routing: Security-Conditioned Model-and-Budget Selection**<br><sub>Yichi Zhang, Zhenxiang Huang, Yuyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18566) · [PDF](https://arxiv.org/pdf/2610.18566) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **91 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **Blitz: Accelerating the Diffusion Modules of AlphaFold3 and Boltz-2**<br><sub>Vinay Saji Mathew, Soundar Kumara, Gretta Kellogg et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23703) · [PDF](https://arxiv.org/pdf/2610.23703) |
| 2026-10-16 | **DIFFLET: A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium**<br><sub>Bin Ma, Min Yu, Vijay Kodamalla et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23047) · [PDF](https://arxiv.org/pdf/2610.23047) |
| 2026-10-16 | **Sink-Sparse Hybrid Attention for Efficient Inference in T2I/T2V Diffusion Transformers**<br><sub>Bingxin Xing, Yu Zhang, Jiatong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22975) · [PDF](https://arxiv.org/pdf/2610.22975) |
| 2026-10-15 | **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**<br><sub>SeungJu Cha, Ye-Chan Kim, HyunGee Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22370) · [PDF](https://arxiv.org/pdf/2610.22370) · [Code](https://github.com/SeungJuCha/DaTMe) |
| 2026-10-15 | **SoftCache: Adaptive Step Size Caching for Diffusion Transformers**<br><sub>Shimon Malnick, Nadav Orenstein, Ohad Fried et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22369) · [PDF](https://arxiv.org/pdf/2610.22369) |
| 2026-10-15 | **PathFM: Fast Generative Forecasting of Multivariate Trajectories**<br><sub>Jiachen Yao, Xiyuan Zhang, Annan Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22358) · [PDF](https://arxiv.org/pdf/2610.22358) |
| 2026-10-15 | **ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space**<br><sub>Minkyu Kim, Baekseung Kim, Junhoo Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21433) · [PDF](https://arxiv.org/pdf/2610.21433) |
| 2026-10-15 | **Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search**<br><sub>Yun Dai, Yuyun Chen, Jiarui Wen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21129) · [PDF](https://arxiv.org/pdf/2610.21129) |
| 2026-10-14 | **Value-Informed Schedule Trimming for Accelerated Sequential Monte Carlo Guidance in Discrete Diffusion**<br><sub>Jaehyeon Kim, Ziseok Lee, Siyoung Choi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20669) · [PDF](https://arxiv.org/pdf/2610.20669) |
| 2026-10-14 | **ForkGRPO: Efficient Exploration and Fine-Grained Credit Assignment for Diffusion Language Models**<br><sub>Zhaoyan Jia, Chengwei Zhou, Gourav Datta et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19408) · [PDF](https://arxiv.org/pdf/2610.19408) |
| 2026-10-13 | **Long-horizon Video Generation with Slot Memory Addressed By Region Tokens**<br><sub>Eren Cetin, Julius Erbach, Vukasin Bozic et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19257) · [PDF](https://arxiv.org/pdf/2610.19257) |
| 2026-10-13 | **H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression**<br><sub>Or Ronai, Vladimir Kulikov, Tomer Michaeli</sub> | [arXiv](https://arxiv.org/abs/2610.18125) · [PDF](https://arxiv.org/pdf/2610.18125) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **150 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-16 | **PreciseEdit: Strong Yet Stable Semantic Transport for One-Step Image Editing**<br><sub>Jingyi Wang, Xiao Lu</sub> | [arXiv](https://arxiv.org/abs/2610.23535) · [PDF](https://arxiv.org/pdf/2610.23535) |
| 2026-10-16 | **Kingfisher: Fast Personalized Visual Autoregressive Generation via Scale-Aware Prompt-Conditioned Scale Decomposition**<br><sub>Dinh-Khoi Vo, Akihiro Sugimoto, Minh-Triet Tran et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23238) · [PDF](https://arxiv.org/pdf/2610.23238) |
| 2026-10-16 | **DIFFLET: A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium**<br><sub>Bin Ma, Min Yu, Vijay Kodamalla et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23047) · [PDF](https://arxiv.org/pdf/2610.23047) |
| 2026-10-16 | **Sink-Sparse Hybrid Attention for Efficient Inference in T2I/T2V Diffusion Transformers**<br><sub>Bingxin Xing, Yu Zhang, Jiatong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22975) · [PDF](https://arxiv.org/pdf/2610.22975) |
| 2026-10-15 | **FlashControl: One-Step Controllable Generator via Distillation-Friendly Single-Stream Teachers**<br><sub>Ngan Nguyen, Dung Nguyen, Quan Dao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22537) · [PDF](https://arxiv.org/pdf/2610.22537) |
| 2026-10-15 | **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**<br><sub>SeungJu Cha, Ye-Chan Kim, HyunGee Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22370) · [PDF](https://arxiv.org/pdf/2610.22370) · [Code](https://github.com/SeungJuCha/DaTMe) |
| 2026-10-15 | **Speculative Forcing for Efficient Autoregressive Video Generation**<br><sub>Hyunwook Choi, Seungryong Kim, Dongyoon Han et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22347) · [PDF](https://arxiv.org/pdf/2610.22347) |
| 2026-10-15 | **Velox: Spatial Memory Makes World Models Efficient**<br><sub>Qiuhong Shen, Shizun Wang, Xinchao Wang</sub> | [arXiv](https://arxiv.org/abs/2610.22311) · [PDF](https://arxiv.org/pdf/2610.22311) |
| 2026-10-15 | **ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space**<br><sub>Minkyu Kim, Baekseung Kim, Junhoo Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21433) · [PDF](https://arxiv.org/pdf/2610.21433) |
| 2026-10-15 | **FocusOPD: Structure-Guided On-Policy Distillation for Diffusion Models**<br><sub>Xinrui Lin, Shumin Wang, Suqi Song et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21250) · [PDF](https://arxiv.org/pdf/2610.21250) |
| 2026-10-15 | **UltraDiff: Transferring High-Fidelity Priors to Compressed Latent Spaces for High-Resolution Image Generation**<br><sub>Jingjing Ren, Haitian Zheng, Haoyu Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21202) · [PDF](https://arxiv.org/pdf/2610.21202) |
| 2026-10-15 | **Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search**<br><sub>Yun Dai, Yuyun Chen, Jiarui Wen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21129) · [PDF](https://arxiv.org/pdf/2610.21129) |

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
