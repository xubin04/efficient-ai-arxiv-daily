# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-05 15:55 CST** · **1539 unique papers** · Newest submission: **2026-11-04**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 243 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 221 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 497 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 160 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 228 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 150 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 252 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 126 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 209 |

## Newly indexed · 2026-11-05

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **ServerBench: How can your coding agents design specialized LLM serving systems?**<br><sub>Xinrui Zhong, Zhiming Wang, Yongqi Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06841) · [PDF](https://arxiv.org/pdf/2611.06841) |
| 2026-11-04 | **VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation**<br><sub>Yihong Luo, Tianyu Pang, Tianyang Hu</sub> | [arXiv](https://arxiv.org/abs/2611.06796) · [PDF](https://arxiv.org/pdf/2611.06796) · [Code](https://github.com/Luo-Yihong/VA-TDM) |
| 2026-11-04 | **The Behavioral Rate of Fine-Tuning: Compression as a Measure of Useful Information**<br><sub>Joey David, Paul Caillon, Alexandre Allauzen</sub> | [arXiv](https://arxiv.org/abs/2611.06598) · [PDF](https://arxiv.org/pdf/2611.06598) |
| 2026-11-04 | **EvoOPD: Evolving Privileged Information Strategies for Black-Box On-Policy Distillation**<br><sub>Ximo Zhu, Ruiqi Liu, Yi Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06542) · [PDF](https://arxiv.org/pdf/2611.06542) |
| 2026-11-04 | **Tools Need Not Speak in Text: Latent Context Compression for Agents**<br><sub>Yuetong Liu, Zhehao Zhou, Yitong Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06500) · [PDF](https://arxiv.org/pdf/2611.06500) · [Code](https://github.com/THU-Agent/Coca-cola) |
| 2026-11-04 | **SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory**<br><sub>Jizhe Zhang, Ang Li, Chenheng Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06445) · [PDF](https://arxiv.org/pdf/2611.06445) |
| 2026-11-04 | **D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding**<br><sub>Baoyou Chen, Ruiqiao Mei, Guancong Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06425) · [PDF](https://arxiv.org/pdf/2611.06425) · [Code](https://github.com/fudan-generative-vision/D3D) |
| 2026-11-04 | **Unaligned Image Guided Denoising via Cross-modal Conditional Flow Matching**<br><sub>Runmin Zhang, Linshan Li, Si-Yuan Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06422) · [PDF](https://arxiv.org/pdf/2611.06422) |
| 2026-11-04 | **Ruby-OPD: Enhancing Pronunciation Controllability and Accuracy for Flow-Matching Text-to-Speech via On-Policy Distillation**<br><sub>Rui Hu, Xiaolong Lin, Zhenpeng Zhan</sub> | [arXiv](https://arxiv.org/abs/2611.06403) · [PDF](https://arxiv.org/pdf/2611.06403) |
| 2026-11-04 | **Does Context Compression Preserve Refusal Alignment?**<br><sub>Anthony Nguyen, Wenjun Lin</sub> | [arXiv](https://arxiv.org/abs/2611.06380) · [PDF](https://arxiv.org/pdf/2611.06380) |
| 2026-11-04 | **NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation**<br><sub>Jiacheng Lu, Haoyi Zhu, Sipei Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06377) · [PDF](https://arxiv.org/pdf/2611.06377) · [Code](https://github.com/jiacheng-lu03/NanoKV) |
| 2026-11-04 | **Give Up to Get More: Priors, Not Policies, Govern Test-Time Compute Allocation**<br><sub>Jinhyung Bae</sub> | [arXiv](https://arxiv.org/abs/2611.06372) · [PDF](https://arxiv.org/pdf/2611.06372) · [Code](https://github.com/nepersoned/priors-not-policies) |
| 2026-11-04 | **Consistency Learning and Distillation for One-Step MIMO-OFDM Channel Estimation**<br><sub>Fredrik Nguyen, Qiwen Wang</sub> | [arXiv](https://arxiv.org/abs/2611.06271) · [PDF](https://arxiv.org/pdf/2611.06271) |
| 2026-11-04 | **NextGAN: Towards Simple and Scalable GAN Training for Image and Video Generation**<br><sub>Xinhao Lou, Dongye Xie, Peng Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06270) · [PDF](https://arxiv.org/pdf/2611.06270) · [Code](https://github.com/LINs-lab/NextGAN.git) |
| 2026-11-04 | **Learning Noise Optimization for Reward Alignment in Few-Step Generative Models**<br><sub>Hongeun Kim, Jeongsol Kim, Jong Chul Ye</sub> | [arXiv](https://arxiv.org/abs/2611.06255) · [PDF](https://arxiv.org/pdf/2611.06255) |
| 2026-11-04 | **AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment**<br><sub>Pragyan Phukan</sub> | [arXiv](https://arxiv.org/abs/2611.06170) · [PDF](https://arxiv.org/pdf/2611.06170) |
| 2026-11-04 | **CARE-FL: Federated Fine-Tuning of Multimodal LLMs in Resource-Constrained Edge Networks**<br><sub>Tianqi Zong, Baosheng Li, Nuocheng Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06169) · [PDF](https://arxiv.org/pdf/2611.06169) |
| 2026-11-04 | **SafeStart: Mitigating the Overlooked Safety Cost of Active Expert Reduction in MoE LLM Serving**<br><sub>Erfan Baghaei Potraghloo, Saeid Shokoufa, Seyedarmin Azizi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06147) · [PDF](https://arxiv.org/pdf/2611.06147) |
| 2026-11-04 | **Accelerating Long-Context Decoding in Large-Scale Hybrid LLMs Without Retraining**<br><sub>João Eduardo Batista, Emil Vatai, Mohamed Wahib</sub> | [arXiv](https://arxiv.org/abs/2611.06133) · [PDF](https://arxiv.org/pdf/2611.06133) |
| 2026-11-04 | **UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence**<br><sub>Mingkang Liu, Peipei Jiao, Weiming Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06075) · [PDF](https://arxiv.org/pdf/2611.06075) |

[View all 33 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **243 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation**<br><sub>Jiacheng Lu, Haoyi Zhu, Sipei Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06377) · [PDF](https://arxiv.org/pdf/2611.06377) · [Code](https://github.com/jiacheng-lu03/NanoKV) |
| 2026-11-04 | **UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence**<br><sub>Mingkang Liu, Peipei Jiao, Weiming Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06075) · [PDF](https://arxiv.org/pdf/2611.06075) |
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-03 | **Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation**<br><sub>Rohan Agarwal, Robin Andeer, Alex Armbruster et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05642) · [PDF](https://arxiv.org/pdf/2611.05642) |
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving**<br><sub>Junhong Wu, Zedong Liu, Xinyang Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04382) · [PDF](https://arxiv.org/pdf/2611.04382) |
| 2026-11-03 | **Twice as Fast, Until It Isn&#x27;t: Quantized Serving of Mid-Size Open LLMs**<br><sub>Smit Kadvani, Kriti Faujdar, Spurthi Tallam</sub> | [arXiv](https://arxiv.org/abs/2611.04380) · [PDF](https://arxiv.org/pdf/2611.04380) |
| 2026-11-03 | **Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs**<br><sub>Hei Yi Mak, Hoang Le, Mehran Taghian Jazi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04376) · [PDF](https://arxiv.org/pdf/2611.04376) |
| 2026-11-03 | **FP4Quant: Efficient 4-Bit Communication Compression for Model-Parallel LLM Training**<br><sub>Man Liu, Xingchen Liu, Hairui Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04323) · [PDF](https://arxiv.org/pdf/2611.04323) |
| 2026-11-03 | **What Does 4-Bit Microscaling Cost a Wearable Activity Recognizer?**<br><sub>Megan Healy, Hossein Valavi</sub> | [arXiv](https://arxiv.org/abs/2611.04185) · [PDF](https://arxiv.org/pdf/2611.04185) |
| 2026-11-02 | **EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL**<br><sub>Hieu Tran, Hong Yu</sub> | [arXiv](https://arxiv.org/abs/2611.03899) · [PDF](https://arxiv.org/pdf/2611.03899) |
| 2026-11-02 | **PlantVLM-Edge: Quantized Vision-Language Models for On-Device Crop Health Diagnosis**<br><sub>Gaurab Wagle, Bishal Adhikari, Jiajia Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03557) · [PDF](https://arxiv.org/pdf/2611.03557) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **221 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **Tools Need Not Speak in Text: Latent Context Compression for Agents**<br><sub>Yuetong Liu, Zhehao Zhou, Yitong Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06500) · [PDF](https://arxiv.org/pdf/2611.06500) · [Code](https://github.com/THU-Agent/Coca-cola) |
| 2026-11-04 | **RI-Prune: Relation and Information Aware Visual Token Pruning for Multi-Image Vision-Language Models**<br><sub>Dongjin Lee, Eunju Lee, Jinhee Jang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06047) · [PDF](https://arxiv.org/pdf/2611.06047) |
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-04 | **Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models**<br><sub>Donggeun Kim</sub> | [arXiv](https://arxiv.org/abs/2611.05927) · [PDF](https://arxiv.org/pdf/2611.05927) · [Code](https://github.com/nota-github/MAEP) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |
| 2026-11-03 | **BtsPruner: Role-Aware Visual Token Pruning for Large Vision-Language Models**<br><sub>Zihao Qi, Zhibo Zhang, Miaoxin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04537) · [PDF](https://arxiv.org/pdf/2611.04537) |
| 2026-11-02 | **Bagel: A Fast Bayesian Online Changepoint Detection Algorithm for Linear Models via Posterior Merging**<br><sub>Ziyang Yang, Paul Fearnhead, Dan Grose</sub> | [arXiv](https://arxiv.org/abs/2611.03230) · [PDF](https://arxiv.org/pdf/2611.03230) |
| 2026-11-01 | **SVD-Prune: Spectral Vision Token Pruning under Extreme Compression**<br><sub>Yvon Apedo, Martyna Poreba, Michal Szczepanski et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02284) · [PDF](https://arxiv.org/pdf/2611.02284) · [Code](https://github.com/anoncvlab/svdPrune) |
| 2026-10-31 | **Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference**<br><sub>Zhichen Zeng, Xichong Zhang, Junpan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01320) · [PDF](https://arxiv.org/pdf/2611.01320) |
| 2026-10-31 | **Rethinking LLM Pruning via Test-Time Scaling**<br><sub>Mingyang Song, Mao Zheng</sub> | [arXiv](https://arxiv.org/abs/2611.01133) · [PDF](https://arxiv.org/pdf/2611.01133) |
| 2026-10-30 | **Compression Technique Interactions in Small Language Models: A Factorial Ablation Study**<br><sub>Bhushit Nema, Siddharth Krishnamurthy, Anjali Kadiyala</sub> | [arXiv](https://arxiv.org/abs/2611.00464) · [PDF](https://arxiv.org/pdf/2611.00464) |
| 2026-10-30 | **SIEVE: Preserving Cross-Image Evidence via Depth-Aware Token Compression**<br><sub>Nitish Shukla, Surgan Jandial, Nhat-Tan Bui et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00351) · [PDF](https://arxiv.org/pdf/2611.00351) · [Code](https://github.com/nitishshukla86/SIEVE) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **497 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation**<br><sub>Yihong Luo, Tianyu Pang, Tianyang Hu</sub> | [arXiv](https://arxiv.org/abs/2611.06796) · [PDF](https://arxiv.org/pdf/2611.06796) · [Code](https://github.com/Luo-Yihong/VA-TDM) |
| 2026-11-04 | **EvoOPD: Evolving Privileged Information Strategies for Black-Box On-Policy Distillation**<br><sub>Ximo Zhu, Ruiqi Liu, Yi Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06542) · [PDF](https://arxiv.org/pdf/2611.06542) |
| 2026-11-04 | **Unaligned Image Guided Denoising via Cross-modal Conditional Flow Matching**<br><sub>Runmin Zhang, Linshan Li, Si-Yuan Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06422) · [PDF](https://arxiv.org/pdf/2611.06422) |
| 2026-11-04 | **Ruby-OPD: Enhancing Pronunciation Controllability and Accuracy for Flow-Matching Text-to-Speech via On-Policy Distillation**<br><sub>Rui Hu, Xiaolong Lin, Zhenpeng Zhan</sub> | [arXiv](https://arxiv.org/abs/2611.06403) · [PDF](https://arxiv.org/pdf/2611.06403) |
| 2026-11-04 | **Consistency Learning and Distillation for One-Step MIMO-OFDM Channel Estimation**<br><sub>Fredrik Nguyen, Qiwen Wang</sub> | [arXiv](https://arxiv.org/abs/2611.06271) · [PDF](https://arxiv.org/pdf/2611.06271) |
| 2026-11-04 | **NextGAN: Towards Simple and Scalable GAN Training for Image and Video Generation**<br><sub>Xinhao Lou, Dongye Xie, Peng Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06270) · [PDF](https://arxiv.org/pdf/2611.06270) · [Code](https://github.com/LINs-lab/NextGAN.git) |
| 2026-11-04 | **Learning Noise Optimization for Reward Alignment in Few-Step Generative Models**<br><sub>Hongeun Kim, Jeongsol Kim, Jong Chul Ye</sub> | [arXiv](https://arxiv.org/abs/2611.06255) · [PDF](https://arxiv.org/pdf/2611.06255) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |
| 2026-11-04 | **Learning When Human Decisions Matter: Executor-Relative Consultation Value for LLM Agents**<br><sub>Shuli Jiang, Khushbu Pahwa, Yuting Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05814) · [PDF](https://arxiv.org/pdf/2611.05814) |
| 2026-11-03 | **Decompose the Distillation: Interpretable Single-Pass Guidance for Diffusion Models**<br><sub>Wuyang Zhang, Xiaolin Xu</sub> | [arXiv](https://arxiv.org/abs/2611.05755) · [PDF](https://arxiv.org/pdf/2611.05755) |
| 2026-11-03 | **Route to Remember: Adaptive Memory Selection for LLM Agents**<br><sub>Zeyu Fang, Jun Yin, Yongsheng Mei et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05636) · [PDF](https://arxiv.org/pdf/2611.05636) |
| 2026-11-03 | **Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting**<br><sub>Raz Marshanski, Liran Nochumsohn, Mayank Jauhari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04760) · [PDF](https://arxiv.org/pdf/2611.04760) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **160 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **The Behavioral Rate of Fine-Tuning: Compression as a Measure of Useful Information**<br><sub>Joey David, Paul Caillon, Alexandre Allauzen</sub> | [arXiv](https://arxiv.org/abs/2611.06598) · [PDF](https://arxiv.org/pdf/2611.06598) |
| 2026-11-04 | **AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment**<br><sub>Pragyan Phukan</sub> | [arXiv](https://arxiv.org/abs/2611.06170) · [PDF](https://arxiv.org/pdf/2611.06170) |
| 2026-11-04 | **CARE-FL: Federated Fine-Tuning of Multimodal LLMs in Resource-Constrained Edge Networks**<br><sub>Tianqi Zong, Baosheng Li, Nuocheng Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06169) · [PDF](https://arxiv.org/pdf/2611.06169) |
| 2026-11-04 | **UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence**<br><sub>Mingkang Liu, Peipei Jiao, Weiming Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06075) · [PDF](https://arxiv.org/pdf/2611.06075) |
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **Shrinkage prior for implicit generative models**<br><sub>Shreya Sinha-Roy, Christian P. Robert, Ritabrata Dutta</sub> | [arXiv](https://arxiv.org/abs/2611.05241) · [PDF](https://arxiv.org/pdf/2611.05241) |
| 2026-11-03 | **Coarse Semantic Blocks for Efficient Training-Free Sparse Attention**<br><sub>Sosuke Kobayashi, Shoichiro Yamaguchi, Seiya Tokui</sub> | [arXiv](https://arxiv.org/abs/2611.04313) · [PDF](https://arxiv.org/pdf/2611.04313) |
| 2026-11-02 | **EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL**<br><sub>Hieu Tran, Hong Yu</sub> | [arXiv](https://arxiv.org/abs/2611.03899) · [PDF](https://arxiv.org/pdf/2611.03899) |
| 2026-11-01 | **EEG-HealthLLM: Hierarchical Adaptation of Large Language Models for Unified Heterogeneous EEG Health Assessment**<br><sub>Ruidong Ma, Jisheng Dang, Ronghao Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01652) · [PDF](https://arxiv.org/pdf/2611.01652) · [Code](https://github.com/Marui-88/EEG-HealthLLM) |
| 2026-10-31 | **GESTALT: Fast, Generalizable Histopathology Image Synthesis from Gene Expression with Pretrained Pathology Foundation Models**<br><sub>Felix Ho, Alexandros Graikos, Dimitris Samaras</sub> | [arXiv](https://arxiv.org/abs/2611.01141) · [PDF](https://arxiv.org/pdf/2611.01141) · [Code](https://github.com/trongnhandev1011/Gestalt) |
| 2026-10-31 | **Scute: Exact Batched Serving for PEFT Adapters Beyond LoRA**<br><sub>Thomas Walker, Richard Baraniuk</sub> | [arXiv](https://arxiv.org/abs/2611.01089) · [PDF](https://arxiv.org/pdf/2611.01089) |
| 2026-10-31 | **Inference First, Training Underneath: Layer-Granular LoRA Co-Serving with LayerLoom**<br><sub>Zongpu Zhang, Yishu Yin, Xuehai Qian</sub> | [arXiv](https://arxiv.org/abs/2611.00652) · [PDF](https://arxiv.org/pdf/2611.00652) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **228 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **Tools Need Not Speak in Text: Latent Context Compression for Agents**<br><sub>Yuetong Liu, Zhehao Zhou, Yitong Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06500) · [PDF](https://arxiv.org/pdf/2611.06500) · [Code](https://github.com/THU-Agent/Coca-cola) |
| 2026-11-04 | **SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory**<br><sub>Jizhe Zhang, Ang Li, Chenheng Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06445) · [PDF](https://arxiv.org/pdf/2611.06445) |
| 2026-11-04 | **Does Context Compression Preserve Refusal Alignment?**<br><sub>Anthony Nguyen, Wenjun Lin</sub> | [arXiv](https://arxiv.org/abs/2611.06380) · [PDF](https://arxiv.org/pdf/2611.06380) |
| 2026-11-04 | **NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation**<br><sub>Jiacheng Lu, Haoyi Zhu, Sipei Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06377) · [PDF](https://arxiv.org/pdf/2611.06377) · [Code](https://github.com/jiacheng-lu03/NanoKV) |
| 2026-11-04 | **Accelerating Long-Context Decoding in Large-Scale Hybrid LLMs Without Retraining**<br><sub>João Eduardo Batista, Emil Vatai, Mohamed Wahib</sub> | [arXiv](https://arxiv.org/abs/2611.06133) · [PDF](https://arxiv.org/pdf/2611.06133) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |
| 2026-11-03 | **Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation**<br><sub>Rohan Agarwal, Robin Andeer, Alex Armbruster et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05642) · [PDF](https://arxiv.org/pdf/2611.05642) |
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **Asymptotic Optimality of $cμ$-Rule for LLM Inference Scheduling under Memory Constraint**<br><sub>Zhenghao Li, Shengbo Wang, Nian Si</sub> | [arXiv](https://arxiv.org/abs/2611.04807) · [PDF](https://arxiv.org/pdf/2611.04807) |
| 2026-11-03 | **LeanSparse: Memory-Efficient Serving for Native Sparse-Attention LLMs**<br><sub>Zaifeng Pan, Chris Wu, Xinwei Qiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04671) · [PDF](https://arxiv.org/pdf/2611.04671) |
| 2026-11-03 | **Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving**<br><sub>Junhong Wu, Zedong Liu, Xinyang Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04382) · [PDF](https://arxiv.org/pdf/2611.04382) |
| 2026-11-03 | **Coarse Semantic Blocks for Efficient Training-Free Sparse Attention**<br><sub>Sosuke Kobayashi, Shoichiro Yamaguchi, Seiya Tokui</sub> | [arXiv](https://arxiv.org/abs/2611.04313) · [PDF](https://arxiv.org/pdf/2611.04313) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **150 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding**<br><sub>Baoyou Chen, Ruiqiao Mei, Guancong Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06425) · [PDF](https://arxiv.org/pdf/2611.06425) · [Code](https://github.com/fudan-generative-vision/D3D) |
| 2026-11-04 | **Give Up to Get More: Priors, Not Policies, Govern Test-Time Compute Allocation**<br><sub>Jinhyung Bae</sub> | [arXiv](https://arxiv.org/abs/2611.06372) · [PDF](https://arxiv.org/pdf/2611.06372) · [Code](https://github.com/nepersoned/priors-not-policies) |
| 2026-11-04 | **Split-KV: Efficient Context Parallelism for Training Diffusion Drafters**<br><sub>Geng Zhang, Fangzhao Zhang, Cong Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05926) · [PDF](https://arxiv.org/pdf/2611.05926) · [Code](https://github.com/zxgx/verl) |
| 2026-11-04 | **RECAP: Context-Aware Prediction Recycling with Request-Local and Persistent Memories for Multimodal Speculative Decoding**<br><sub>Hengjie Zhu, Dayan Wu, Xinze Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05894) · [PDF](https://arxiv.org/pdf/2611.05894) · [Code](https://github.com/Senmo996/RECAP-official-code) |
| 2026-11-03 | **Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding**<br><sub>Hoang Anh Duy Le, Huibing Dong, Alireza Khadem et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05724) · [PDF](https://arxiv.org/pdf/2611.05724) |
| 2026-11-03 | **Hybrid Spark: Adaptive Speculative Decoding That Lets the Content Choose the Drafter**<br><sub>Ekagra Ranjan, Bharat Venkitesh</sub> | [arXiv](https://arxiv.org/abs/2611.05611) · [PDF](https://arxiv.org/pdf/2611.05611) |
| 2026-11-03 | **PATTS: Parallel-Aware Test-Time Scaling for Thought-Image Generation in Multimodal Discrete Diffusion LLMs**<br><sub>Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04948) · [PDF](https://arxiv.org/pdf/2611.04948) · [Code](https://github.com/Ringo-Star/PATTS.git) |
| 2026-11-03 | **ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning Improvement**<br><sub>Yao Cui, Zhen Yang, Yuandong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04787) · [PDF](https://arxiv.org/pdf/2611.04787) |
| 2026-11-03 | **PACT: Certifying What Is Written in Parallel Decoding of Diffusion Language Models**<br><sub>Yanchao Li, Yusu Zhang, Jiaqing Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04152) · [PDF](https://arxiv.org/pdf/2611.04152) · [Code](https://github.com/LiZaiyuan0619/PACT) |
| 2026-11-02 | **SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding**<br><sub>Tianyu Liu, Jun Zhang, Wenjie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02846) · [PDF](https://arxiv.org/pdf/2611.02846) |
| 2026-11-02 | **SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding**<br><sub>Kunjun Li, Wenhao Chai, Yihao Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02501) · [PDF](https://arxiv.org/pdf/2611.02501) |
| 2026-11-01 | **Seeing What Matters, Verifying What Pays: Load-Adaptive Speculative Decoding for Vision-Language Models**<br><sub>Hong Nie, Zhangchi Gao, Yuqian Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01617) · [PDF](https://arxiv.org/pdf/2611.01617) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **252 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **ServerBench: How can your coding agents design specialized LLM serving systems?**<br><sub>Xinrui Zhong, Zhiming Wang, Yongqi Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06841) · [PDF](https://arxiv.org/pdf/2611.06841) |
| 2026-11-04 | **SafeStart: Mitigating the Overlooked Safety Cost of Active Expert Reduction in MoE LLM Serving**<br><sub>Erfan Baghaei Potraghloo, Saeid Shokoufa, Seyedarmin Azizi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06147) · [PDF](https://arxiv.org/pdf/2611.06147) |
| 2026-11-04 | **A Controlled Experimental Evaluation of Configuration and Cache Architecture in LLM Serving Engines**<br><sub>Muhammad Faizan Anwar, Sina Keshvadi</sub> | [arXiv](https://arxiv.org/abs/2611.05991) · [PDF](https://arxiv.org/pdf/2611.05991) · [Code](https://github.com/FaizanAnwar01/llm-serving-config-eval) |
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **What Sets the Serving Speed of Looped Language Models? Measurements and Optimizations Graded by Exactness**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05150) · [PDF](https://arxiv.org/pdf/2611.05150) |
| 2026-11-03 | **Workload-Static Optical Circuit Switching For Scalable LLM Inference Decode**<br><sub>Maximilian Thürmer, Nicolas Scotto di Perto, Eloise Stein et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05104) · [PDF](https://arxiv.org/pdf/2611.05104) |
| 2026-11-03 | **Asymptotic Optimality of $cμ$-Rule for LLM Inference Scheduling under Memory Constraint**<br><sub>Zhenghao Li, Shengbo Wang, Nian Si</sub> | [arXiv](https://arxiv.org/abs/2611.04807) · [PDF](https://arxiv.org/pdf/2611.04807) |
| 2026-11-03 | **Accelerating Offloading-Based MoE Inference by Interleaving Concurrent Requests**<br><sub>Hongseung Yu, In Gim, Kyunghan Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04794) · [PDF](https://arxiv.org/pdf/2611.04794) |
| 2026-11-03 | **TactiNavi: Serving and Revising an LLM Game Coach with Explicit Strategy Conditions**<br><sub>Qi Liu, Xiaoyang Yuan, Zhuomeng Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04772) · [PDF](https://arxiv.org/pdf/2611.04772) |
| 2026-11-03 | **LeanSparse: Memory-Efficient Serving for Native Sparse-Attention LLMs**<br><sub>Zaifeng Pan, Chris Wu, Xinwei Qiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04671) · [PDF](https://arxiv.org/pdf/2611.04671) |
| 2026-11-03 | **Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving**<br><sub>Junhong Wu, Zedong Liu, Xinyang Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04382) · [PDF](https://arxiv.org/pdf/2611.04382) |
| 2026-11-03 | **Twice as Fast, Until It Isn&#x27;t: Quantized Serving of Mid-Size Open LLMs**<br><sub>Smit Kadvani, Kriti Faujdar, Spurthi Tallam</sub> | [arXiv](https://arxiv.org/abs/2611.04380) · [PDF](https://arxiv.org/pdf/2611.04380) |

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

图像/视频生成的计算、显存与延迟优化 · **209 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-04 | **VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation**<br><sub>Yihong Luo, Tianyu Pang, Tianyang Hu</sub> | [arXiv](https://arxiv.org/abs/2611.06796) · [PDF](https://arxiv.org/pdf/2611.06796) · [Code](https://github.com/Luo-Yihong/VA-TDM) |
| 2026-11-04 | **NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation**<br><sub>Jiacheng Lu, Haoyi Zhu, Sipei Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06377) · [PDF](https://arxiv.org/pdf/2611.06377) · [Code](https://github.com/jiacheng-lu03/NanoKV) |
| 2026-11-04 | **NextGAN: Towards Simple and Scalable GAN Training for Image and Video Generation**<br><sub>Xinhao Lou, Dongye Xie, Peng Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06270) · [PDF](https://arxiv.org/pdf/2611.06270) · [Code](https://github.com/LINs-lab/NextGAN.git) |
| 2026-11-04 | **Learning Noise Optimization for Reward Alignment in Few-Step Generative Models**<br><sub>Hongeun Kim, Jeongsol Kim, Jong Chul Ye</sub> | [arXiv](https://arxiv.org/abs/2611.06255) · [PDF](https://arxiv.org/pdf/2611.06255) |
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |
| 2026-11-03 | **Decompose the Distillation: Interpretable Single-Pass Guidance for Diffusion Models**<br><sub>Wuyang Zhang, Xiaolin Xu</sub> | [arXiv](https://arxiv.org/abs/2611.05755) · [PDF](https://arxiv.org/pdf/2611.05755) |
| 2026-11-03 | **Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation**<br><sub>Rohan Agarwal, Robin Andeer, Alex Armbruster et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05642) · [PDF](https://arxiv.org/pdf/2611.05642) |
| 2026-11-03 | **StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models**<br><sub>Chenru Wang, Xuanyang Zhang, Yucheng Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04386) · [PDF](https://arxiv.org/pdf/2611.04386) |
| 2026-11-02 | **Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models**<br><sub>Siqiao Huang, Partha Kaushik, Michael Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04028) · [PDF](https://arxiv.org/pdf/2611.04028) |
| 2026-11-02 | **OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation**<br><sub>Zihao Fan, Xin Lu, Jie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02803) · [PDF](https://arxiv.org/pdf/2611.02803) |
| 2026-11-01 | **Z-Cache: Accelerating Diffusion Transformers via Self-Reflection**<br><sub>Zegang Cheng, Zhikai Wang, Jiacheng Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01846) · [PDF](https://arxiv.org/pdf/2611.01846) |

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
