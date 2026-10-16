# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-16 13:54 CST** · **1070 unique papers** · Newest submission: **2026-10-15**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 168 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 152 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 364 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 105 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 150 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 103 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 170 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 88 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 145 |

## Newly indexed · 2026-10-16

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**<br><sub>SeungJu Cha, Ye-Chan Kim, HyunGee Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22370) · [PDF](https://arxiv.org/pdf/2610.22370) · [Code](https://github.com/SeungJuCha/DaTMe) |
| 2026-10-15 | **SoftCache: Adaptive Step Size Caching for Diffusion Transformers**<br><sub>Shimon Malnick, Nadav Orenstein, Ohad Fried et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22369) · [PDF](https://arxiv.org/pdf/2610.22369) |
| 2026-10-15 | **PathFM: Fast Generative Forecasting of Multivariate Trajectories**<br><sub>Jiachen Yao, Xiyuan Zhang, Annan Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22358) · [PDF](https://arxiv.org/pdf/2610.22358) |
| 2026-10-15 | **Speculative Forcing for Efficient Autoregressive Video Generation**<br><sub>Hyunwook Choi, Seungryong Kim, Dongyoon Han et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22347) · [PDF](https://arxiv.org/pdf/2610.22347) |
| 2026-10-15 | **Velox: Spatial Memory Makes World Models Efficient**<br><sub>Qiuhong Shen, Shizun Wang, Xinchao Wang</sub> | [arXiv](https://arxiv.org/abs/2610.22311) · [PDF](https://arxiv.org/pdf/2610.22311) |
| 2026-10-15 | **BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks**<br><sub>Max Zhu, Bohang Sun, Pietro Lio et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22256) · [PDF](https://arxiv.org/pdf/2610.22256) |
| 2026-10-15 | **Query-Efficient Rejection Sampling for Parallel Masked Diffusion**<br><sub>Shiyuan Zhang, Xuheng Li, Qiwei Di et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22238) · [PDF](https://arxiv.org/pdf/2610.22238) |
| 2026-10-15 | **WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression**<br><sub>Yue Yu, Bowei Kang, Changsheng Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22232) · [PDF](https://arxiv.org/pdf/2610.22232) |
| 2026-10-15 | **Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models**<br><sub>Yuqi Xiong, Chunyi Peng, Zhipeng Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22217) · [PDF](https://arxiv.org/pdf/2610.22217) · [Code](https://github.com/NEUIR/SCOPED) |
| 2026-10-15 | **Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing**<br><sub>Tianxiang Fei, Jiazheng Kang, Mao Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22196) · [PDF](https://arxiv.org/pdf/2610.22196) |
| 2026-10-15 | **Efficient KV Cache Migration for Geo-Distributed LLM Inference in Collaborative Edge Computing**<br><sub>Mingjin Zhang, Jiannong Cao, Tao Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22172) · [PDF](https://arxiv.org/pdf/2610.22172) |
| 2026-10-15 | **DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction**<br><sub>Aozhong Zhang, Selcuk Gurses, Yanxia Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22130) · [PDF](https://arxiv.org/pdf/2610.22130) |
| 2026-10-15 | **Learning from Unverified Peers via Shared Residual Distillation**<br><sub>Feiyang Chen, Runze Ma, Zichen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22080) · [PDF](https://arxiv.org/pdf/2610.22080) |
| 2026-10-15 | **Memory as Weights: Internalizing Long-Term History for Streaming Videos**<br><sub>Zhuoming Liu, Jinhong Lin, Lin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22070) · [PDF](https://arxiv.org/pdf/2610.22070) |
| 2026-10-15 | **Augment the Cache, Replace the Activation: A 2x2 Study of Internal-State Sharing**<br><sub>Adam Deng, Shicheng Liu, Yada Zhu</sub> | [arXiv](https://arxiv.org/abs/2610.22026) · [PDF](https://arxiv.org/pdf/2610.22026) |
| 2026-10-15 | **Bias Mitigation in Audio-Enabled LLMs through Adversarial Training and Distillation Methods**<br><sub>Adnan Al Ali, Jindřich Libovický, Anne Lauscher</sub> | [arXiv](https://arxiv.org/abs/2610.21763) · [PDF](https://arxiv.org/pdf/2610.21763) |
| 2026-10-15 | **Conditional Mean Flows: Few-Step Densities for Simulation-Based Inference**<br><sub>Jonas Arruda, Jan Hasenauer, Stefan T. Radev</sub> | [arXiv](https://arxiv.org/abs/2610.21657) · [PDF](https://arxiv.org/pdf/2610.21657) |
| 2026-10-15 | **ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training**<br><sub>Yukun Tian, Junwei Su, Haofeng Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21640) · [PDF](https://arxiv.org/pdf/2610.21640) |
| 2026-10-15 | **LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models**<br><sub>Zixuan Liu, Nan Xue, Rui Bao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21594) · [PDF](https://arxiv.org/pdf/2610.21594) |
| 2026-10-15 | **When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill**<br><sub>Muhammad Ibrahim</sub> | [arXiv](https://arxiv.org/abs/2610.21500) · [PDF](https://arxiv.org/pdf/2610.21500) |

[View all 42 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **168 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
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
| 2026-10-14 | **What You Sign Is Not What You Run: The Verifiability Gap in Quantized LLM Supply Chains**<br><sub>Wei-Liang Liu, Cheng-Yen Tsai</sub> | [arXiv](https://arxiv.org/abs/2610.19498) · [PDF](https://arxiv.org/pdf/2610.19498) · [Code](https://github.com/Rlonglong/gguf-verifiability-artifact) |
| 2026-10-14 | **MemCode: Discrete Semantic Representations for Long-Term Agent Memory**<br><sub>Xin Li, Liang Hu, Duoqian Miao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19472) · [PDF](https://arxiv.org/pdf/2610.19472) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **152 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**<br><sub>SeungJu Cha, Ye-Chan Kim, HyunGee Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22370) · [PDF](https://arxiv.org/pdf/2610.22370) · [Code](https://github.com/SeungJuCha/DaTMe) |
| 2026-10-15 | **Calibration Language Shapes Block-Influence Pruning in Multilingual Language Models**<br><sub>Vedant Pandhare, Piyush Dhoka</sub> | [arXiv](https://arxiv.org/abs/2610.21383) · [PDF](https://arxiv.org/pdf/2610.21383) · [Code](https://github.com/VedantPandhare/Language-Balanced-Depth-Pruning-of-Small-Multilingual-LLMs.git) |
| 2026-10-15 | **Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search**<br><sub>Yun Dai, Yuyun Chen, Jiarui Wen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21129) · [PDF](https://arxiv.org/pdf/2610.21129) |
| 2026-10-14 | **STP-GUI: Spatially-Aware Token Pruning for Efficient Web-GUI Agents**<br><sub>Shuo Wang, Sifan Zhou, Xiaobo Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20390) · [PDF](https://arxiv.org/pdf/2610.20390) |
| 2026-10-14 | **Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility**<br><sub>Salima Lamsiyah, Adelaide Danilov, Oleksandr Marchenko Breneur et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20139) · [PDF](https://arxiv.org/pdf/2610.20139) |
| 2026-10-14 | **MemDuet: Learning Dual-Process Memory for Long-Context Reasoning**<br><sub>Jiangcheng Song, Haodong Jing, Yulin Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19928) · [PDF](https://arxiv.org/pdf/2610.19928) |
| 2026-10-13 | **Unlocking Structured Pruning for Reasoning Language Models via Attention-Preserving MLP Trimming**<br><sub>Woosang Lim, Haneul Yoo, Vincent-Daniel Yun et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19121) · [PDF](https://arxiv.org/pdf/2610.19121) |
| 2026-10-13 | **Focus, Align, and Diffuse: Time-Series-Aware Keyframe Diffusion for Cardiac Dynamic Synthesis from Sparse Observations**<br><sub>Junkai Liu, Haofan Wu, Nay Aung et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19050) · [PDF](https://arxiv.org/pdf/2610.19050) |
| 2026-10-13 | **Discrete Diffusion Models are Minimax Optimal Under Sparsity**<br><sub>Luca Blunda, Tyler Farghly, Umut Simsekli et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19020) · [PDF](https://arxiv.org/pdf/2610.19020) |
| 2026-10-13 | **Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs**<br><sub>Aimon Rahman, Joymallya Chakraborty, Vidit Bansal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18858) · [PDF](https://arxiv.org/pdf/2610.18858) |
| 2026-10-13 | **Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning**<br><sub>Tianhao Fu, Austin Wang, Charles Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18690) · [PDF](https://arxiv.org/pdf/2610.18690) |
| 2026-10-13 | **Two For The Price Of One: Curvature-Aware Pruning Preserves Influence Functions Too**<br><sub>Mehdi Makni, Natalia Ponomareva, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2610.18516) · [PDF](https://arxiv.org/pdf/2610.18516) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **364 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **Speculative Forcing for Efficient Autoregressive Video Generation**<br><sub>Hyunwook Choi, Seungryong Kim, Dongyoon Han et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22347) · [PDF](https://arxiv.org/pdf/2610.22347) |
| 2026-10-15 | **Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models**<br><sub>Yuqi Xiong, Chunyi Peng, Zhipeng Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22217) · [PDF](https://arxiv.org/pdf/2610.22217) · [Code](https://github.com/NEUIR/SCOPED) |
| 2026-10-15 | **Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing**<br><sub>Tianxiang Fei, Jiazheng Kang, Mao Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22196) · [PDF](https://arxiv.org/pdf/2610.22196) |
| 2026-10-15 | **Learning from Unverified Peers via Shared Residual Distillation**<br><sub>Feiyang Chen, Runze Ma, Zichen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22080) · [PDF](https://arxiv.org/pdf/2610.22080) |
| 2026-10-15 | **Bias Mitigation in Audio-Enabled LLMs through Adversarial Training and Distillation Methods**<br><sub>Adnan Al Ali, Jindřich Libovický, Anne Lauscher</sub> | [arXiv](https://arxiv.org/abs/2610.21763) · [PDF](https://arxiv.org/pdf/2610.21763) |
| 2026-10-15 | **Conditional Mean Flows: Few-Step Densities for Simulation-Based Inference**<br><sub>Jonas Arruda, Jan Hasenauer, Stefan T. Radev</sub> | [arXiv](https://arxiv.org/abs/2610.21657) · [PDF](https://arxiv.org/pdf/2610.21657) |
| 2026-10-15 | **Learning from Interaction Experience via Localized Context Distillation**<br><sub>Zhezheng Hao, Yongkang Yang, Xilin Xia et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21427) · [PDF](https://arxiv.org/pdf/2610.21427) |
| 2026-10-15 | **ReState: Noise-Level-Aware State Correction for Training-Free Object Removal in Few-Step Diffusion Models**<br><sub>Donghwan Lee, Sanghyun Jo, Sihyun Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21287) · [PDF](https://arxiv.org/pdf/2610.21287) |
| 2026-10-15 | **FocusOPD: Structure-Guided On-Policy Distillation for Diffusion Models**<br><sub>Xinrui Lin, Shumin Wang, Suqi Song et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21250) · [PDF](https://arxiv.org/pdf/2610.21250) |
| 2026-10-15 | **UltraDiff: Transferring High-Fidelity Priors to Compressed Latent Spaces for High-Resolution Image Generation**<br><sub>Jingjing Ren, Haitian Zheng, Haoyu Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21202) · [PDF](https://arxiv.org/pdf/2610.21202) |
| 2026-10-15 | **Condition-Contrastive Extrapolation for On-Policy Distillation of Language Models**<br><sub>Wenxuan Luo, Chenxi Li, Haoyue Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21195) · [PDF](https://arxiv.org/pdf/2610.21195) |
| 2026-10-15 | **ControlFlow3D: Distilling Multi-View Knowledge into Latent Flow Matching for Point Cloud Upsampling**<br><sub>Yuang Liu, Zhi Zuo, Zhengkai Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21190) · [PDF](https://arxiv.org/pdf/2610.21190) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **105 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks**<br><sub>Max Zhu, Bohang Sun, Pietro Lio et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22256) · [PDF](https://arxiv.org/pdf/2610.22256) |
| 2026-10-15 | **WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression**<br><sub>Yue Yu, Bowei Kang, Changsheng Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22232) · [PDF](https://arxiv.org/pdf/2610.22232) |
| 2026-10-15 | **Memory as Weights: Internalizing Long-Term History for Streaming Videos**<br><sub>Zhuoming Liu, Jinhong Lin, Lin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22070) · [PDF](https://arxiv.org/pdf/2610.22070) |
| 2026-10-15 | **ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training**<br><sub>Yukun Tian, Junwei Su, Haofeng Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21640) · [PDF](https://arxiv.org/pdf/2610.21640) |
| 2026-10-15 | **Translation Circuit Discovery and Targeted Optimization for Low-Resource Multilingual Translation**<br><sub>Atai Waris Khan, Abdullah Mazhar, Raghu Kumar et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21456) · [PDF](https://arxiv.org/pdf/2610.21456) |
| 2026-10-14 | **Multimodal Medical Image Parsing with Task-Specific Low-Rank Adapters**<br><sub>Taha Sabir, Alberto Montero Molina, Thinh Quang Ly et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19901) · [PDF](https://arxiv.org/pdf/2610.19901) · [Code](https://github.com/TahaSabir0/FLARE26-Hexapus) |
| 2026-10-13 | **DUALVIEW: Leveraging Broad and Output-Specific Evidence for LLM-based Multi-Output Text Regression**<br><sub>Yiheng Su, Junyi Jessy Li, Matthew Lease</sub> | [arXiv](https://arxiv.org/abs/2610.19206) · [PDF](https://arxiv.org/pdf/2610.19206) |
| 2026-10-13 | **Discovering Undisclosed Concepts in LoRA Adapters for Diffusion-Based AIGC Models**<br><sub>Yupeng Qiu, Han Fang, Dhananjai Sharma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18990) · [PDF](https://arxiv.org/pdf/2610.18990) |
| 2026-10-13 | **Unlocking Token Rewards via Training-Free Reward Attribution**<br><sub>Sitong Wu, Haoru Tan, Bin Xia et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18704) · [PDF](https://arxiv.org/pdf/2610.18704) · [Code](https://github.com/stonewst/P2T) |
| 2026-10-13 | **LLM2R: From Large Language Models to 3D Reassemblers**<br><sub>Zhouhan Zhong, Qiuhong Shen, Xingyi Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18604) · [PDF](https://arxiv.org/pdf/2610.18604) |
| 2026-10-12 | **Monarch-Muon: Structure-Aware Muon for Fast and Memory-Efficient Pretraining**<br><sub>Alexander Miasnikov, Ruslan Kabirov, Gleb Molodtsov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17429) · [PDF](https://arxiv.org/pdf/2610.17429) |
| 2026-10-12 | **HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation**<br><sub>Tripti Shukla, Shwetha Somasundaram, Akshat Gupta et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17368) · [PDF](https://arxiv.org/pdf/2610.17368) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **150 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **Velox: Spatial Memory Makes World Models Efficient**<br><sub>Qiuhong Shen, Shizun Wang, Xinchao Wang</sub> | [arXiv](https://arxiv.org/abs/2610.22311) · [PDF](https://arxiv.org/pdf/2610.22311) |
| 2026-10-15 | **Efficient KV Cache Migration for Geo-Distributed LLM Inference in Collaborative Edge Computing**<br><sub>Mingjin Zhang, Jiannong Cao, Tao Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22172) · [PDF](https://arxiv.org/pdf/2610.22172) |
| 2026-10-15 | **DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction**<br><sub>Aozhong Zhang, Selcuk Gurses, Yanxia Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22130) · [PDF](https://arxiv.org/pdf/2610.22130) |
| 2026-10-15 | **Augment the Cache, Replace the Activation: A 2x2 Study of Internal-State Sharing**<br><sub>Adam Deng, Shicheng Liu, Yada Zhu</sub> | [arXiv](https://arxiv.org/abs/2610.22026) · [PDF](https://arxiv.org/pdf/2610.22026) |
| 2026-10-15 | **When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill**<br><sub>Muhammad Ibrahim</sub> | [arXiv](https://arxiv.org/abs/2610.21500) · [PDF](https://arxiv.org/pdf/2610.21500) |
| 2026-10-15 | **FlashAttention with Statistics: Low-Overhead Attention Features for Compact Hallucination Detectors**<br><sub>Andrei Volodichev, Maksim Savichev, Nikita Sviridov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21483) · [PDF](https://arxiv.org/pdf/2610.21483) |
| 2026-10-15 | **PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems**<br><sub>Han Shen, Qifu Tyler Sun, Fanyang Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21390) · [PDF](https://arxiv.org/pdf/2610.21390) |
| 2026-10-15 | **From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models**<br><sub>Chaogui Gou</sub> | [arXiv](https://arxiv.org/abs/2610.21165) · [PDF](https://arxiv.org/pdf/2610.21165) |
| 2026-10-15 | **Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search**<br><sub>Yun Dai, Yuyun Chen, Jiarui Wen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21129) · [PDF](https://arxiv.org/pdf/2610.21129) |
| 2026-10-14 | **ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models**<br><sub>Bohan Sun, Zunhai Su, Xialie Zhuang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20503) · [PDF](https://arxiv.org/pdf/2610.20503) · [Code](https://github.com/StartLuxLabs/ReaDy) |
| 2026-10-14 | **FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding**<br><sub>Shuxuan Li, Jialiang Kang, Yanghao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20392) · [PDF](https://arxiv.org/pdf/2610.20392) |
| 2026-10-14 | **StreamErase: Towards Ultra-Fast Streaming Video Erasing**<br><sub>Zhuobai Dong, Xiaobing Tu, Xiantao Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20137) · [PDF](https://arxiv.org/pdf/2610.20137) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **103 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **Query-Efficient Rejection Sampling for Parallel Masked Diffusion**<br><sub>Shiyuan Zhang, Xuheng Li, Qiwei Di et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22238) · [PDF](https://arxiv.org/pdf/2610.22238) |
| 2026-10-15 | **LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models**<br><sub>Zixuan Liu, Nan Xue, Rui Bao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21594) · [PDF](https://arxiv.org/pdf/2610.21594) |
| 2026-10-15 | **HyCo: Hybrid Drafting for Cost-Efficient Mobile-Cloud Speculative Decoding**<br><sub>Hanbin Bae, Heejin Choi, Joohyung Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21436) · [PDF](https://arxiv.org/pdf/2610.21436) |
| 2026-10-14 | **Speculative Sampling in Interactive Video Generation**<br><sub>Yubo Huang, Yuxuan Zhang, Jiaming Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20556) · [PDF](https://arxiv.org/pdf/2610.20556) |
| 2026-10-14 | **FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding**<br><sub>Shuxuan Li, Jialiang Kang, Yanghao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20392) · [PDF](https://arxiv.org/pdf/2610.20392) |
| 2026-10-14 | **Are We Overthinking One-Step Generation?**<br><sub>Woobin Park, Jaeyeon Kim, Yilun Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20331) · [PDF](https://arxiv.org/pdf/2610.20331) · [Code](https://github.com/JaeyeonKim01/priming) |
| 2026-10-13 | **SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models**<br><sub>Yuqi Huang, Xingyao Li, Yunlong Hou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18735) · [PDF](https://arxiv.org/pdf/2610.18735) |
| 2026-10-13 | **Compare to Correct: Pairwise-Guided Logit Adjustment for LLM Test-Time Scaling**<br><sub>Cong Hua, Qianqian Xu, Zitai Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18583) · [PDF](https://arxiv.org/pdf/2610.18583) |
| 2026-10-13 | **RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions**<br><sub>Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17867) · [PDF](https://arxiv.org/pdf/2610.17867) |
| 2026-10-13 | **Diff Diffusion: Predicting Edit Paths with Diffusion Models for Efficient Code Editing**<br><sub>Xiaolong Xu, Hao Jiang, Bo Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17831) · [PDF](https://arxiv.org/pdf/2610.17831) |
| 2026-10-12 | **SchemaWeaver: Accelerating On-Device Mobile Agentic AI via Schema-Guided Parallel LLM Decoding**<br><sub>Boyuan Yang, Wei Gao</sub> | [arXiv](https://arxiv.org/abs/2610.17436) · [PDF](https://arxiv.org/pdf/2610.17436) |
| 2026-10-12 | **PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models**<br><sub>Quentin Fruytier, Anton Xue, Sanjay Shakkottai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17375) · [PDF](https://arxiv.org/pdf/2610.17375) · [Code](https://github.com/Quentin-Fruytier/PIG-DLM-release) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **170 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing**<br><sub>Tianxiang Fei, Jiazheng Kang, Mao Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22196) · [PDF](https://arxiv.org/pdf/2610.22196) |
| 2026-10-15 | **When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill**<br><sub>Muhammad Ibrahim</sub> | [arXiv](https://arxiv.org/abs/2610.21500) · [PDF](https://arxiv.org/pdf/2610.21500) |
| 2026-10-15 | **PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems**<br><sub>Han Shen, Qifu Tyler Sun, Fanyang Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21390) · [PDF](https://arxiv.org/pdf/2610.21390) |
| 2026-10-15 | **From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models**<br><sub>Chaogui Gou</sub> | [arXiv](https://arxiv.org/abs/2610.21165) · [PDF](https://arxiv.org/pdf/2610.21165) |
| 2026-10-14 | **CascadeLedger: Counterfactual Auditing of Information and Resource Integrity in LLM Cascades**<br><sub>Miaobo Hu, Shuhao Hu, Xiaobo Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20668) · [PDF](https://arxiv.org/pdf/2610.20668) |
| 2026-10-14 | **MemDuet: Learning Dual-Process Memory for Long-Context Reasoning**<br><sub>Jiangcheng Song, Haodong Jing, Yulin Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19928) · [PDF](https://arxiv.org/pdf/2610.19928) |
| 2026-10-14 | **JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs**<br><sub>Daijin Hu</sub> | [arXiv](https://arxiv.org/abs/2610.19822) · [PDF](https://arxiv.org/pdf/2610.19822) |
| 2026-10-14 | **Scaling LLM Inference via Parallelism: Throughput-Latency Trade-off**<br><sub>Javad Mirzaei, Jeebak Mitra</sub> | [arXiv](https://arxiv.org/abs/2610.19405) · [PDF](https://arxiv.org/pdf/2610.19405) |
| 2026-10-13 | **Rethinking Quality in Large Language Model Routing: Security-Conditioned Model-and-Budget Selection**<br><sub>Yichi Zhang, Zhenxiang Huang, Yuyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18566) · [PDF](https://arxiv.org/pdf/2610.18566) |
| 2026-10-13 | **FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving**<br><sub>Yunfei Feng, Jingkai He, Shiqi Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18451) · [PDF](https://arxiv.org/pdf/2610.18451) |
| 2026-10-13 | **RadixFlow: Filling Execution Bubbles in Prefix-Cached Hybrid LLM Serving**<br><sub>Huihao Jing, Wenbin Hu, Shaojin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18143) · [PDF](https://arxiv.org/pdf/2610.18143) |
| 2026-10-13 | **HaloBlock: Faster and Better Decoding for Diffusion Large Language Models**<br><sub>Zhaohui Zheng, Chenhang He, Jinrui Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17948) · [PDF](https://arxiv.org/pdf/2610.17948) · [Code](https://github.com/PolyU-VCLab/HaloBlock) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **88 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**<br><sub>SeungJu Cha, Ye-Chan Kim, HyunGee Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22370) · [PDF](https://arxiv.org/pdf/2610.22370) · [Code](https://github.com/SeungJuCha/DaTMe) |
| 2026-10-15 | **SoftCache: Adaptive Step Size Caching for Diffusion Transformers**<br><sub>Shimon Malnick, Nadav Orenstein, Ohad Fried et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22369) · [PDF](https://arxiv.org/pdf/2610.22369) |
| 2026-10-15 | **PathFM: Fast Generative Forecasting of Multivariate Trajectories**<br><sub>Jiachen Yao, Xiyuan Zhang, Annan Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22358) · [PDF](https://arxiv.org/pdf/2610.22358) |
| 2026-10-15 | **ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space**<br><sub>Minkyu Kim, Baekseung Kim, Junhoo Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21433) · [PDF](https://arxiv.org/pdf/2610.21433) |
| 2026-10-15 | **Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search**<br><sub>Yun Dai, Yuyun Chen, Jiarui Wen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21129) · [PDF](https://arxiv.org/pdf/2610.21129) |
| 2026-10-14 | **Value-Informed Schedule Trimming for Accelerated Sequential Monte Carlo Guidance in Discrete Diffusion**<br><sub>Jaehyeon Kim, Ziseok Lee, Siyoung Choi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20669) · [PDF](https://arxiv.org/pdf/2610.20669) |
| 2026-10-14 | **ForkGRPO: Efficient Exploration and Fine-Grained Credit Assignment for Diffusion Language Models**<br><sub>Zhaoyan Jia, Chengwei Zhou, Gourav Datta et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19408) · [PDF](https://arxiv.org/pdf/2610.19408) |
| 2026-10-13 | **Long-horizon Video Generation with Slot Memory Addressed By Region Tokens**<br><sub>Eren Cetin, Julius Erbach, Vukasin Bozic et al.</sub> | [arXiv](https://arxiv.org/abs/2610.19257) · [PDF](https://arxiv.org/pdf/2610.19257) |
| 2026-10-13 | **H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression**<br><sub>Or Ronai, Vladimir Kulikov, Tomer Michaeli</sub> | [arXiv](https://arxiv.org/abs/2610.18125) · [PDF](https://arxiv.org/pdf/2610.18125) |
| 2026-10-13 | **LinMorph: Learning to Morph Weights for Efficient Video DiT Linearization**<br><sub>Lingyi Long, Congyue Zhao, Xiaoou Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17914) · [PDF](https://arxiv.org/pdf/2610.17914) |
| 2026-10-12 | **PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models**<br><sub>Quentin Fruytier, Anton Xue, Sanjay Shakkottai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17375) · [PDF](https://arxiv.org/pdf/2610.17375) · [Code](https://github.com/Quentin-Fruytier/PIG-DLM-release) |
| 2026-10-12 | **MARS: Systematic Multi-Level Acceleration for World Action Models**<br><sub>Zengyuan Zuo, Yongchang Zhang, Guangyu Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17141) · [PDF](https://arxiv.org/pdf/2610.17141) · [Code](https://github.com/PKU-VaLuE-Lab/MARS) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **145 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-15 | **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**<br><sub>SeungJu Cha, Ye-Chan Kim, HyunGee Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22370) · [PDF](https://arxiv.org/pdf/2610.22370) · [Code](https://github.com/SeungJuCha/DaTMe) |
| 2026-10-15 | **Speculative Forcing for Efficient Autoregressive Video Generation**<br><sub>Hyunwook Choi, Seungryong Kim, Dongyoon Han et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22347) · [PDF](https://arxiv.org/pdf/2610.22347) |
| 2026-10-15 | **Velox: Spatial Memory Makes World Models Efficient**<br><sub>Qiuhong Shen, Shizun Wang, Xinchao Wang</sub> | [arXiv](https://arxiv.org/abs/2610.22311) · [PDF](https://arxiv.org/pdf/2610.22311) |
| 2026-10-15 | **ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space**<br><sub>Minkyu Kim, Baekseung Kim, Junhoo Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21433) · [PDF](https://arxiv.org/pdf/2610.21433) |
| 2026-10-15 | **FocusOPD: Structure-Guided On-Policy Distillation for Diffusion Models**<br><sub>Xinrui Lin, Shumin Wang, Suqi Song et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21250) · [PDF](https://arxiv.org/pdf/2610.21250) |
| 2026-10-15 | **UltraDiff: Transferring High-Fidelity Priors to Compressed Latent Spaces for High-Resolution Image Generation**<br><sub>Jingjing Ren, Haitian Zheng, Haoyu Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21202) · [PDF](https://arxiv.org/pdf/2610.21202) |
| 2026-10-15 | **Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search**<br><sub>Yun Dai, Yuyun Chen, Jiarui Wen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21129) · [PDF](https://arxiv.org/pdf/2610.21129) |
| 2026-10-14 | **Speculative Sampling in Interactive Video Generation**<br><sub>Yubo Huang, Yuxuan Zhang, Jiaming Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20556) · [PDF](https://arxiv.org/pdf/2610.20556) |
| 2026-10-14 | **Generative Representation Learning for Scalable Latent Tokenization**<br><sub>Alan Baade, Kyle Sargent, Vincent Sitzmann et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20533) · [PDF](https://arxiv.org/pdf/2610.20533) |
| 2026-10-14 | **Are We Overthinking One-Step Generation?**<br><sub>Woobin Park, Jaeyeon Kim, Yilun Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20331) · [PDF](https://arxiv.org/pdf/2610.20331) · [Code](https://github.com/JaeyeonKim01/priming) |
| 2026-10-14 | **StreamErase: Towards Ultra-Fast Streaming Video Erasing**<br><sub>Zhuobai Dong, Xiaobing Tu, Xiantao Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20137) · [PDF](https://arxiv.org/pdf/2610.20137) |
| 2026-10-14 | **RepForcing: Representation-Space Initialization for Autoregressive Video Distillation**<br><sub>Siming Fu, Zheming Fu, Lianrui Mu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.20111) · [PDF](https://arxiv.org/pdf/2610.20111) |

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
