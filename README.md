# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-04 15:31 CST** · **1506 unique papers** · Newest submission: **2026-11-03**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 239 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 216 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 486 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 156 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 221 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 144 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 249 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 123 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 201 |

## Newly indexed · 2026-11-04

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **Shrinkage prior for implicit generative models**<br><sub>Shreya Sinha-Roy, Christian P. Robert, Ritabrata Dutta</sub> | [arXiv](https://arxiv.org/abs/2611.05241) · [PDF](https://arxiv.org/pdf/2611.05241) |
| 2026-11-03 | **What Sets the Serving Speed of Looped Language Models? Measurements and Optimizations Graded by Exactness**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05150) · [PDF](https://arxiv.org/pdf/2611.05150) |
| 2026-11-03 | **Workload-Static Optical Circuit Switching For Scalable LLM Inference Decode**<br><sub>Maximilian Thürmer, Nicolas Scotto di Perto, Eloise Stein et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05104) · [PDF](https://arxiv.org/pdf/2611.05104) |
| 2026-11-03 | **PATTS: Parallel-Aware Test-Time Scaling for Thought-Image Generation in Multimodal Discrete Diffusion LLMs**<br><sub>Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04948) · [PDF](https://arxiv.org/pdf/2611.04948) · [Code](https://github.com/Ringo-Star/PATTS.git) |
| 2026-11-03 | **Asymptotic Optimality of $cμ$-Rule for LLM Inference Scheduling under Memory Constraint**<br><sub>Zhenghao Li, Shengbo Wang, Nian Si</sub> | [arXiv](https://arxiv.org/abs/2611.04807) · [PDF](https://arxiv.org/pdf/2611.04807) |
| 2026-11-03 | **Accelerating Offloading-Based MoE Inference by Interleaving Concurrent Requests**<br><sub>Hongseung Yu, In Gim, Kyunghan Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04794) · [PDF](https://arxiv.org/pdf/2611.04794) |
| 2026-11-03 | **ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning Improvement**<br><sub>Yao Cui, Zhen Yang, Yuandong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04787) · [PDF](https://arxiv.org/pdf/2611.04787) |
| 2026-11-03 | **TactiNavi: Serving and Revising an LLM Game Coach with Explicit Strategy Conditions**<br><sub>Qi Liu, Xiaoyang Yuan, Zhuomeng Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04772) · [PDF](https://arxiv.org/pdf/2611.04772) |
| 2026-11-03 | **Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting**<br><sub>Raz Marshanski, Liran Nochumsohn, Mayank Jauhari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04760) · [PDF](https://arxiv.org/pdf/2611.04760) |
| 2026-11-03 | **LeanSparse: Memory-Efficient Serving for Native Sparse-Attention LLMs**<br><sub>Zaifeng Pan, Chris Wu, Xinwei Qiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04671) · [PDF](https://arxiv.org/pdf/2611.04671) |
| 2026-11-03 | **BtsPruner: Role-Aware Visual Token Pruning for Large Vision-Language Models**<br><sub>Zihao Qi, Zhibo Zhang, Miaoxin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04537) · [PDF](https://arxiv.org/pdf/2611.04537) |
| 2026-11-03 | **CogniLife: Continuous Cognitive Distillation for Deployed Multi-Expert Agent Marketplaces**<br><sub>Xuwei Tan, Jingchun Huang, Ming Cai et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04483) · [PDF](https://arxiv.org/pdf/2611.04483) |
| 2026-11-03 | **Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware**<br><sub>Yeonseok Lee</sub> | [arXiv](https://arxiv.org/abs/2611.04392) · [PDF](https://arxiv.org/pdf/2611.04392) · [Code](https://github.com/ylee-sling/Aero-VPA) |
| 2026-11-03 | **StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models**<br><sub>Chenru Wang, Xuanyang Zhang, Yucheng Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04386) · [PDF](https://arxiv.org/pdf/2611.04386) |
| 2026-11-03 | **Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving**<br><sub>Junhong Wu, Zedong Liu, Xinyang Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04382) · [PDF](https://arxiv.org/pdf/2611.04382) |
| 2026-11-03 | **Twice as Fast, Until It Isn&#x27;t: Quantized Serving of Mid-Size Open LLMs**<br><sub>Smit Kadvani, Kriti Faujdar, Spurthi Tallam</sub> | [arXiv](https://arxiv.org/abs/2611.04380) · [PDF](https://arxiv.org/pdf/2611.04380) |
| 2026-11-03 | **Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs**<br><sub>Hei Yi Mak, Hoang Le, Mehran Taghian Jazi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04376) · [PDF](https://arxiv.org/pdf/2611.04376) |
| 2026-11-03 | **FP4Quant: Efficient 4-Bit Communication Compression for Model-Parallel LLM Training**<br><sub>Man Liu, Xingchen Liu, Hairui Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04323) · [PDF](https://arxiv.org/pdf/2611.04323) |
| 2026-11-03 | **Coarse Semantic Blocks for Efficient Training-Free Sparse Attention**<br><sub>Sosuke Kobayashi, Shoichiro Yamaguchi, Seiya Tokui</sub> | [arXiv](https://arxiv.org/abs/2611.04313) · [PDF](https://arxiv.org/pdf/2611.04313) |

[View all 30 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **239 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving**<br><sub>Junhong Wu, Zedong Liu, Xinyang Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04382) · [PDF](https://arxiv.org/pdf/2611.04382) |
| 2026-11-03 | **Twice as Fast, Until It Isn&#x27;t: Quantized Serving of Mid-Size Open LLMs**<br><sub>Smit Kadvani, Kriti Faujdar, Spurthi Tallam</sub> | [arXiv](https://arxiv.org/abs/2611.04380) · [PDF](https://arxiv.org/pdf/2611.04380) |
| 2026-11-03 | **Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs**<br><sub>Hei Yi Mak, Hoang Le, Mehran Taghian Jazi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04376) · [PDF](https://arxiv.org/pdf/2611.04376) |
| 2026-11-03 | **FP4Quant: Efficient 4-Bit Communication Compression for Model-Parallel LLM Training**<br><sub>Man Liu, Xingchen Liu, Hairui Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04323) · [PDF](https://arxiv.org/pdf/2611.04323) |
| 2026-11-03 | **What Does 4-Bit Microscaling Cost a Wearable Activity Recognizer?**<br><sub>Megan Healy, Hossein Valavi</sub> | [arXiv](https://arxiv.org/abs/2611.04185) · [PDF](https://arxiv.org/pdf/2611.04185) |
| 2026-11-02 | **EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL**<br><sub>Hieu Tran, Hong Yu</sub> | [arXiv](https://arxiv.org/abs/2611.03899) · [PDF](https://arxiv.org/pdf/2611.03899) |
| 2026-11-02 | **PlantVLM-Edge: Quantized Vision-Language Models for On-Device Crop Health Diagnosis**<br><sub>Gaurab Wagle, Bishal Adhikari, Jiajia Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03557) · [PDF](https://arxiv.org/pdf/2611.03557) |
| 2026-11-02 | **SHq: Learnable Grids for LLM Weight Quantization**<br><sub>Michael Helcig, Earl Killian, Dan Alistarh</sub> | [arXiv](https://arxiv.org/abs/2611.02966) · [PDF](https://arxiv.org/pdf/2611.02966) |
| 2026-11-02 | **Beyond Accuracy: How Quantization Affects Coding Agents**<br><sub>Areej Mehboob, Muhammad Ali Shafique, Muhammad Usman Qadeer et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02368) · [PDF](https://arxiv.org/pdf/2611.02368) |
| 2026-11-01 | **MedPsy: State-of-the-Art Small Medical Language Models for Efficient Edge Deployment**<br><sub>Davide Vitabile, Alexandro Buffa, Akshay Nambiar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02011) · [PDF](https://arxiv.org/pdf/2611.02011) |
| 2026-11-01 | **MatMoE: Matryoshka Mixture-of-Experts with Dynamic Mixed-Precision Quantization for Efficient Inference**<br><sub>Renjie Wei, Haochen Huang, Chuyu Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01704) · [PDF](https://arxiv.org/pdf/2611.01704) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **216 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **BtsPruner: Role-Aware Visual Token Pruning for Large Vision-Language Models**<br><sub>Zihao Qi, Zhibo Zhang, Miaoxin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04537) · [PDF](https://arxiv.org/pdf/2611.04537) |
| 2026-11-02 | **Bagel: A Fast Bayesian Online Changepoint Detection Algorithm for Linear Models via Posterior Merging**<br><sub>Ziyang Yang, Paul Fearnhead, Dan Grose</sub> | [arXiv](https://arxiv.org/abs/2611.03230) · [PDF](https://arxiv.org/pdf/2611.03230) |
| 2026-11-01 | **SVD-Prune: Spectral Vision Token Pruning under Extreme Compression**<br><sub>Yvon Apedo, Martyna Poreba, Michal Szczepanski et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02284) · [PDF](https://arxiv.org/pdf/2611.02284) · [Code](https://github.com/anoncvlab/svdPrune) |
| 2026-10-31 | **Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference**<br><sub>Zhichen Zeng, Xichong Zhang, Junpan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01320) · [PDF](https://arxiv.org/pdf/2611.01320) |
| 2026-10-31 | **Rethinking LLM Pruning via Test-Time Scaling**<br><sub>Mingyang Song, Mao Zheng</sub> | [arXiv](https://arxiv.org/abs/2611.01133) · [PDF](https://arxiv.org/pdf/2611.01133) |
| 2026-10-30 | **Compression Technique Interactions in Small Language Models: A Factorial Ablation Study**<br><sub>Bhushit Nema, Siddharth Krishnamurthy, Anjali Kadiyala</sub> | [arXiv](https://arxiv.org/abs/2611.00464) · [PDF](https://arxiv.org/pdf/2611.00464) |
| 2026-10-30 | **SIEVE: Preserving Cross-Image Evidence via Depth-Aware Token Compression**<br><sub>Nitish Shukla, Surgan Jandial, Nhat-Tan Bui et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00351) · [PDF](https://arxiv.org/pdf/2611.00351) · [Code](https://github.com/nitishshukla86/SIEVE) |
| 2026-10-30 | **Quantization of Large Models with Weight Outliers and Sparsity**<br><sub>Leonidas Tsigkounakis, Abraham Jaeger Mountain, Yilang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00286) · [PDF](https://arxiv.org/pdf/2611.00286) |
| 2026-10-30 | **Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity**<br><sub>Jean Lucien Randrianantenaina, Hung Nguyen, Nasib Ullah et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41968) · [PDF](https://arxiv.org/pdf/2610.41968) |
| 2026-10-30 | **Sparse Text Diffusion under Dual Budgets: Context Connectivity and Expert Activation**<br><sub>Alexandros Christoforos, Chadbourne Davis, Paul Raj</sub> | [arXiv](https://arxiv.org/abs/2610.41487) · [PDF](https://arxiv.org/pdf/2610.41487) |
| 2026-10-30 | **In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents**<br><sub>Xuning He, Kai Fan, Runyu Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41291) · [PDF](https://arxiv.org/pdf/2610.41291) · [Code](https://github.com/RISE-X-Lab/Agentic-Soft-Token) |
| 2026-10-30 | **Experts Exhibit Structured Redundancy: Structure-Preserving Expert Pruning for Mixture-of-Experts Large Language Models**<br><sub>Tian Wang, Yongding Tao, Yihong Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41236) · [PDF](https://arxiv.org/pdf/2610.41236) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **486 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting**<br><sub>Raz Marshanski, Liran Nochumsohn, Mayank Jauhari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04760) · [PDF](https://arxiv.org/pdf/2611.04760) |
| 2026-11-03 | **CogniLife: Continuous Cognitive Distillation for Deployed Multi-Expert Agent Marketplaces**<br><sub>Xuwei Tan, Jingchun Huang, Ming Cai et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04483) · [PDF](https://arxiv.org/pdf/2611.04483) |
| 2026-11-03 | **Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware**<br><sub>Yeonseok Lee</sub> | [arXiv](https://arxiv.org/abs/2611.04392) · [PDF](https://arxiv.org/pdf/2611.04392) · [Code](https://github.com/ylee-sling/Aero-VPA) |
| 2026-11-03 | **StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models**<br><sub>Chenru Wang, Xuanyang Zhang, Yucheng Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04386) · [PDF](https://arxiv.org/pdf/2611.04386) |
| 2026-11-03 | **Bidirectional Centered Score Matching for Discrete Diffusion Distillation**<br><sub>Peng Tu, Baoyou Chen, Haoyuan Xia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04279) · [PDF](https://arxiv.org/pdf/2611.04279) |
| 2026-11-02 | **VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing**<br><sub>Yexin Liu, Yunlong Lin, Zehan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03404) · [PDF](https://arxiv.org/pdf/2611.03404) · [Code](https://github.com/LAW1223/VidDub) |
| 2026-11-02 | **SurgPace: Complexity-Aware Progressive Distillation for Surgical Multimodal Large Language Models**<br><sub>Zhicheng He, Xiaohan Xing, Hongqiu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03125) · [PDF](https://arxiv.org/pdf/2611.03125) · [Code](https://github.com/hezhicheng2002/SurgPace) |
| 2026-11-02 | **Efficient Hybrid Distillation: Synergizing Score and Adversarial Objectives for One-Step Diffusion**<br><sub>Fei Peng, Junqiang Wu, Haoxian Tan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03017) · [PDF](https://arxiv.org/pdf/2611.03017) · [Code](https://github.com/pf0607/EASD) |
| 2026-11-02 | **Distilling Literary Sentiment from LLM Annotations into an Ordinal BERT Model**<br><sub>Artem Suslov, Takehiro Hashimoto</sub> | [arXiv](https://arxiv.org/abs/2611.02985) · [PDF](https://arxiv.org/pdf/2611.02985) |
| 2026-11-02 | **SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding**<br><sub>Tianyu Liu, Jun Zhang, Wenjie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02846) · [PDF](https://arxiv.org/pdf/2611.02846) |
| 2026-11-02 | **OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation**<br><sub>Zihao Fan, Xin Lu, Jie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02803) · [PDF](https://arxiv.org/pdf/2611.02803) |
| 2026-11-02 | **History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models**<br><sub>Hangyi Kuang, Chengzhi Wang, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02782) · [PDF](https://arxiv.org/pdf/2611.02782) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **156 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **Shrinkage prior for implicit generative models**<br><sub>Shreya Sinha-Roy, Christian P. Robert, Ritabrata Dutta</sub> | [arXiv](https://arxiv.org/abs/2611.05241) · [PDF](https://arxiv.org/pdf/2611.05241) |
| 2026-11-03 | **Coarse Semantic Blocks for Efficient Training-Free Sparse Attention**<br><sub>Sosuke Kobayashi, Shoichiro Yamaguchi, Seiya Tokui</sub> | [arXiv](https://arxiv.org/abs/2611.04313) · [PDF](https://arxiv.org/pdf/2611.04313) |
| 2026-11-02 | **EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL**<br><sub>Hieu Tran, Hong Yu</sub> | [arXiv](https://arxiv.org/abs/2611.03899) · [PDF](https://arxiv.org/pdf/2611.03899) |
| 2026-11-01 | **EEG-HealthLLM: Hierarchical Adaptation of Large Language Models for Unified Heterogeneous EEG Health Assessment**<br><sub>Ruidong Ma, Jisheng Dang, Ronghao Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01652) · [PDF](https://arxiv.org/pdf/2611.01652) · [Code](https://github.com/Marui-88/EEG-HealthLLM) |
| 2026-10-31 | **GESTALT: Fast, Generalizable Histopathology Image Synthesis from Gene Expression with Pretrained Pathology Foundation Models**<br><sub>Felix Ho, Alexandros Graikos, Dimitris Samaras</sub> | [arXiv](https://arxiv.org/abs/2611.01141) · [PDF](https://arxiv.org/pdf/2611.01141) · [Code](https://github.com/trongnhandev1011/Gestalt) |
| 2026-10-31 | **Scute: Exact Batched Serving for PEFT Adapters Beyond LoRA**<br><sub>Thomas Walker, Richard Baraniuk</sub> | [arXiv](https://arxiv.org/abs/2611.01089) · [PDF](https://arxiv.org/pdf/2611.01089) |
| 2026-10-31 | **Inference First, Training Underneath: Layer-Granular LoRA Co-Serving with LayerLoom**<br><sub>Zongpu Zhang, Yishu Yin, Xuehai Qian</sub> | [arXiv](https://arxiv.org/abs/2611.00652) · [PDF](https://arxiv.org/pdf/2611.00652) |
| 2026-10-31 | **From Weeks to Hours: Fast and Principled SFT Data Generation for Reasoning LLMs**<br><sub>Hongyi Henry Jin, Wenhan Yang, Meysam Ghaffari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00554) · [PDF](https://arxiv.org/pdf/2611.00554) |
| 2026-10-30 | **Compression Technique Interactions in Small Language Models: A Factorial Ablation Study**<br><sub>Bhushit Nema, Siddharth Krishnamurthy, Anjali Kadiyala</sub> | [arXiv](https://arxiv.org/abs/2611.00464) · [PDF](https://arxiv.org/pdf/2611.00464) |
| 2026-10-30 | **RE-SciVQA: Improving Scientific VQA With Context-Relevant Retrieval and Lightweight MLLM Adaptation**<br><sub>Sheikh Tahmim Mehdi, Muminul Islam Jami</sub> | [arXiv](https://arxiv.org/abs/2611.00242) · [PDF](https://arxiv.org/pdf/2611.00242) |
| 2026-10-30 | **CAPER: Circuit-Aware Parameter-Efficient Reasoning in LLMs for Analog Verification**<br><sub>Saion K. Roy</sub> | [arXiv](https://arxiv.org/abs/2611.00187) · [PDF](https://arxiv.org/pdf/2611.00187) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **221 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **Asymptotic Optimality of $cμ$-Rule for LLM Inference Scheduling under Memory Constraint**<br><sub>Zhenghao Li, Shengbo Wang, Nian Si</sub> | [arXiv](https://arxiv.org/abs/2611.04807) · [PDF](https://arxiv.org/pdf/2611.04807) |
| 2026-11-03 | **LeanSparse: Memory-Efficient Serving for Native Sparse-Attention LLMs**<br><sub>Zaifeng Pan, Chris Wu, Xinwei Qiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04671) · [PDF](https://arxiv.org/pdf/2611.04671) |
| 2026-11-03 | **Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving**<br><sub>Junhong Wu, Zedong Liu, Xinyang Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04382) · [PDF](https://arxiv.org/pdf/2611.04382) |
| 2026-11-03 | **Coarse Semantic Blocks for Efficient Training-Free Sparse Attention**<br><sub>Sosuke Kobayashi, Shoichiro Yamaguchi, Seiya Tokui</sub> | [arXiv](https://arxiv.org/abs/2611.04313) · [PDF](https://arxiv.org/pdf/2611.04313) |
| 2026-11-02 | **Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse Attention**<br><sub>Serdarcan Dilbaz, Arjun Krishna, Kiran Kamble et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03768) · [PDF](https://arxiv.org/pdf/2611.03768) · [Code](https://github.com/ArjunKrishnak/dsa-multi-layer-indexer) |
| 2026-11-02 | **CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention**<br><sub>Mohammed Dabbah, Izhak Golan, Oren Tropp et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03200) · [PDF](https://arxiv.org/pdf/2611.03200) |
| 2026-11-02 | **BasisKV: Value Latents for Communication and Key Routing**<br><sub>Lixun Zhang, Zishan Shao, Kangning Cui et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02583) · [PDF](https://arxiv.org/pdf/2611.02583) · [Code](https://github.com/alexz949/BasisKV) |
| 2026-11-01 | **Fairway: Load-Aware KV Cache Reuse for LLM Prefill Scheduling**<br><sub>Hamidreza Alikhani, Nazmul Takbir, Matin Khajavi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02082) · [PDF](https://arxiv.org/pdf/2611.02082) |
| 2026-11-01 | **MedPsy: State-of-the-Art Small Medical Language Models for Efficient Edge Deployment**<br><sub>Davide Vitabile, Alexandro Buffa, Akshay Nambiar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02011) · [PDF](https://arxiv.org/pdf/2611.02011) |
| 2026-11-01 | **ReWY: Faster Backpropagation for Delta-Rule Attention - From 7 to 3 Matrix Multiplications**<br><sub>Yi Zhang, Zhixin Zhao, Weiwei Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01940) · [PDF](https://arxiv.org/pdf/2611.01940) · [Code](https://github.com/flashserve/ReWY) |
| 2026-11-01 | **Who Asks, Who Answers: Linear Attention Builds the Query in Hybrid Language Models**<br><sub>Wenqi Zeng, Chen Feng, YuAng Chen</sub> | [arXiv](https://arxiv.org/abs/2611.01909) · [PDF](https://arxiv.org/pdf/2611.01909) · [Code](https://github.com/yuang-chen/LinearQuery) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **144 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **PATTS: Parallel-Aware Test-Time Scaling for Thought-Image Generation in Multimodal Discrete Diffusion LLMs**<br><sub>Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04948) · [PDF](https://arxiv.org/pdf/2611.04948) · [Code](https://github.com/Ringo-Star/PATTS.git) |
| 2026-11-03 | **ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning Improvement**<br><sub>Yao Cui, Zhen Yang, Yuandong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04787) · [PDF](https://arxiv.org/pdf/2611.04787) |
| 2026-11-03 | **PACT: Certifying What Is Written in Parallel Decoding of Diffusion Language Models**<br><sub>Yanchao Li, Yusu Zhang, Jiaqing Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04152) · [PDF](https://arxiv.org/pdf/2611.04152) · [Code](https://github.com/LiZaiyuan0619/PACT) |
| 2026-11-02 | **SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding**<br><sub>Tianyu Liu, Jun Zhang, Wenjie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02846) · [PDF](https://arxiv.org/pdf/2611.02846) |
| 2026-11-02 | **SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding**<br><sub>Kunjun Li, Wenhao Chai, Yihao Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02501) · [PDF](https://arxiv.org/pdf/2611.02501) |
| 2026-11-01 | **Seeing What Matters, Verifying What Pays: Load-Adaptive Speculative Decoding for Vision-Language Models**<br><sub>Hong Nie, Zhangchi Gao, Yuqian Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01617) · [PDF](https://arxiv.org/pdf/2611.01617) |
| 2026-10-31 | **Rethinking LLM Pruning via Test-Time Scaling**<br><sub>Mingyang Song, Mao Zheng</sub> | [arXiv](https://arxiv.org/abs/2611.01133) · [PDF](https://arxiv.org/pdf/2611.01133) |
| 2026-10-31 | **TVP: TV is Almost All You Need for Speculative Decoding**<br><sub>Aaryam Sharma</sub> | [arXiv](https://arxiv.org/abs/2611.00588) · [PDF](https://arxiv.org/pdf/2611.00588) |
| 2026-10-30 | **CAPER: Circuit-Aware Parameter-Efficient Reasoning in LLMs for Analog Verification**<br><sub>Saion K. Roy</sub> | [arXiv](https://arxiv.org/abs/2611.00187) · [PDF](https://arxiv.org/pdf/2611.00187) |
| 2026-10-30 | **TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents**<br><sub>Jihao Zhao, Shuaishuai Zu, Pengfei Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41177) · [PDF](https://arxiv.org/pdf/2610.41177) |
| 2026-10-29 | **Agentic World Modeling for Agent Test-time Scaling without Environment Replica**<br><sub>Wendi Li, Huseyin A. Inan, Wei-Ning Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40927) · [PDF](https://arxiv.org/pdf/2610.40927) |
| 2026-10-29 | **Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets**<br><sub>Bole Ma, Ayesha Afzal, Jan Eitzinger et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40287) · [PDF](https://arxiv.org/pdf/2610.40287) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **249 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers**<br><sub>Minsoo Cheong, Sungjoo Yoo</sub> | [arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) |
| 2026-11-03 | **What Sets the Serving Speed of Looped Language Models? Measurements and Optimizations Graded by Exactness**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05150) · [PDF](https://arxiv.org/pdf/2611.05150) |
| 2026-11-03 | **Workload-Static Optical Circuit Switching For Scalable LLM Inference Decode**<br><sub>Maximilian Thürmer, Nicolas Scotto di Perto, Eloise Stein et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05104) · [PDF](https://arxiv.org/pdf/2611.05104) |
| 2026-11-03 | **Asymptotic Optimality of $cμ$-Rule for LLM Inference Scheduling under Memory Constraint**<br><sub>Zhenghao Li, Shengbo Wang, Nian Si</sub> | [arXiv](https://arxiv.org/abs/2611.04807) · [PDF](https://arxiv.org/pdf/2611.04807) |
| 2026-11-03 | **Accelerating Offloading-Based MoE Inference by Interleaving Concurrent Requests**<br><sub>Hongseung Yu, In Gim, Kyunghan Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04794) · [PDF](https://arxiv.org/pdf/2611.04794) |
| 2026-11-03 | **TactiNavi: Serving and Revising an LLM Game Coach with Explicit Strategy Conditions**<br><sub>Qi Liu, Xiaoyang Yuan, Zhuomeng Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04772) · [PDF](https://arxiv.org/pdf/2611.04772) |
| 2026-11-03 | **LeanSparse: Memory-Efficient Serving for Native Sparse-Attention LLMs**<br><sub>Zaifeng Pan, Chris Wu, Xinwei Qiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04671) · [PDF](https://arxiv.org/pdf/2611.04671) |
| 2026-11-03 | **Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving**<br><sub>Junhong Wu, Zedong Liu, Xinyang Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04382) · [PDF](https://arxiv.org/pdf/2611.04382) |
| 2026-11-03 | **Twice as Fast, Until It Isn&#x27;t: Quantized Serving of Mid-Size Open LLMs**<br><sub>Smit Kadvani, Kriti Faujdar, Spurthi Tallam</sub> | [arXiv](https://arxiv.org/abs/2611.04380) · [PDF](https://arxiv.org/pdf/2611.04380) |
| 2026-11-03 | **UMLoad: Fast On-Demand Model Loading on Unified Memory Architecture**<br><sub>Zimeng Wang, Jinrong Yang, Rong Chen</sub> | [arXiv](https://arxiv.org/abs/2611.04253) · [PDF](https://arxiv.org/pdf/2611.04253) |
| 2026-11-03 | **Navigating Runtime Dynamism in Semantic Query Serving**<br><sub>Hengrui Zhang, Xupeng Miao</sub> | [arXiv](https://arxiv.org/abs/2611.04248) · [PDF](https://arxiv.org/pdf/2611.04248) |
| 2026-11-02 | **ROCm InferaSim: Cut LLM Serving Trial Costs and Deploy the Best Configuration**<br><sub>Anshu Raina, Yao Fu, Zhang Jiejing et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04032) · [PDF](https://arxiv.org/pdf/2611.04032) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **123 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-02 | **Denoising Is Stein: Moment Access and a Resource Hierarchy for Learning Hidden Structure in Diffusion Models**<br><sub>Rui Wang</sub> | [arXiv](https://arxiv.org/abs/2611.04043) · [PDF](https://arxiv.org/pdf/2611.04043) |
| 2026-11-01 | **Z-Cache: Accelerating Diffusion Transformers via Self-Reflection**<br><sub>Zegang Cheng, Zhikai Wang, Jiacheng Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01846) · [PDF](https://arxiv.org/pdf/2611.01846) |
| 2026-10-31 | **Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference**<br><sub>Zhichen Zeng, Xichong Zhang, Junpan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01320) · [PDF](https://arxiv.org/pdf/2611.01320) |
| 2026-10-31 | **Accelerating posterior sampling in Bayesian inverse problems with diffusion models: an online-offline perspective**<br><sub>Duc-Lam Duong</sub> | [arXiv](https://arxiv.org/abs/2611.01300) · [PDF](https://arxiv.org/pdf/2611.01300) |
| 2026-10-31 | **Wave Forcing: Towards Speed-of-Light Streaming Video Generation**<br><sub>Yijie Jin, Yuxuan Liu, Jiajun Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00859) · [PDF](https://arxiv.org/pdf/2611.00859) |
| 2026-10-30 | **CLiS: Plug-and-Play Attention Acceleration for Video Diffusion on TPUs via Certified Stabilization**<br><sub>Elisa Tsai, Shao-yu Huang, Daniel Mandragona et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00444) · [PDF](https://arxiv.org/pdf/2611.00444) |
| 2026-10-29 | **No Channels Left Behind: Understanding Diffusion Acceleration through Residual Gates**<br><sub>Junha Park, Jaemyung Yu, Jaehui Hwang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40914) · [PDF](https://arxiv.org/pdf/2610.40914) · [Code](https://github.com/naver-ai/radialobj) |
| 2026-10-29 | **UniRA: Unified Representation Alignment and Auto-Encoding for Efficient Diffusion Generation**<br><sub>An Lanji, Dawei Liu, Jin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39948) · [PDF](https://arxiv.org/pdf/2610.39948) |
| 2026-10-29 | **KV Cache Quantization for Diffusion Language Models**<br><sub>Yan Tai, Yunan Ding, Guangzhao Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) |
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-28 | **NAGO: Noise-Aware Generative Operator via Flow Matching**<br><sub>Guanyu Chen, Shengze Xu, Pengwei Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38273) · [PDF](https://arxiv.org/pdf/2610.38273) · [Code](https://github.com/cgymmy/NAGO) |
| 2026-10-27 | **Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs**<br><sub>Donghyeon Cho, Joowon Kim, Seungho Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36671) · [PDF](https://arxiv.org/pdf/2610.36671) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **201 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-03 | **StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models**<br><sub>Chenru Wang, Xuanyang Zhang, Yucheng Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04386) · [PDF](https://arxiv.org/pdf/2611.04386) |
| 2026-11-02 | **Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models**<br><sub>Siqiao Huang, Partha Kaushik, Michael Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.04028) · [PDF](https://arxiv.org/pdf/2611.04028) |
| 2026-11-02 | **OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation**<br><sub>Zihao Fan, Xin Lu, Jie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02803) · [PDF](https://arxiv.org/pdf/2611.02803) |
| 2026-11-01 | **Z-Cache: Accelerating Diffusion Transformers via Self-Reflection**<br><sub>Zegang Cheng, Zhikai Wang, Jiacheng Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01846) · [PDF](https://arxiv.org/pdf/2611.01846) |
| 2026-11-01 | **RIFT: Residual-Informed Flow Transfer for One-Step Generative Video Compression**<br><sub>Qizhe Wang, Jiaye Fu, Feng Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01791) · [PDF](https://arxiv.org/pdf/2611.01791) |
| 2026-11-01 | **IMPACT: Image-Conditioned Motion with Physics-Aware Collision and Trajectory Guidance for Video Generation**<br><sub>Shiwei Yang, Yunlong Yu, Zhao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01372) · [PDF](https://arxiv.org/pdf/2611.01372) |
| 2026-10-31 | **DriftingPlanner: Drifting Generative Models for One-Step Trajectory Planning in End-to-End Autonomous Driving**<br><sub>Ziming Liu, Yizhan Qu, Leichen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01283) · [PDF](https://arxiv.org/pdf/2611.01283) |
| 2026-10-31 | **Wave Forcing: Towards Speed-of-Light Streaming Video Generation**<br><sub>Yijie Jin, Yuxuan Liu, Jiajun Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00859) · [PDF](https://arxiv.org/pdf/2611.00859) |
| 2026-10-31 | **Running a 20B Video Diffusion Transformer on Consumer Hardware: A Deployment and Measurement Report for MiniMax H3 on Apple Silicon**<br><sub>Zhenzhou, Shi, Yizhe et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00843) · [PDF](https://arxiv.org/pdf/2611.00843) |
| 2026-10-30 | **CLiS: Plug-and-Play Attention Acceleration for Video Diffusion on TPUs via Certified Stabilization**<br><sub>Elisa Tsai, Shao-yu Huang, Daniel Mandragona et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00444) · [PDF](https://arxiv.org/pdf/2611.00444) |
| 2026-10-30 | **A Better Critic Matters for Distribution Matching Distillation**<br><sub>Zongze Wu, Xianbang Wang, Zhengyang Geng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42135) · [PDF](https://arxiv.org/pdf/2610.42135) |
| 2026-10-30 | **Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation**<br><sub>Jiahua Xu, Yijie Fang, Nannan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42031) · [PDF](https://arxiv.org/pdf/2610.42031) |

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
