# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-27 14:20 CST** · **1302 unique papers** · Newest submission: **2026-10-26**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 198 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 193 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 433 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 133 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 189 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 129 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 200 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 111 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 176 |

## Newly indexed · 2026-10-27

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **OSWAM: An Effective World Action Model with One-Step Action Generation**<br><sub>Guowen Zhang, Liyi Chen, Xu Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35850) · [PDF](https://arxiv.org/pdf/2610.35850) |
| 2026-10-26 | **Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models**<br><sub>Aidar Myrzakhan, Zhiqiang Shen</sub> | [arXiv](https://arxiv.org/abs/2610.35804) · [PDF](https://arxiv.org/pdf/2610.35804) · [Code](https://github.com/VILA-Lab/dSpark) |
| 2026-10-26 | **EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation**<br><sub>Yitao Xiao, Xu Zhang, Ye Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35690) · [PDF](https://arxiv.org/pdf/2610.35690) · [Code](https://github.com/CenYangtze/EvoRouter) |
| 2026-10-26 | **Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation**<br><sub>Junyi Chen, Haiyu Zhang, Zhoujie Fu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35594) · [PDF](https://arxiv.org/pdf/2610.35594) |
| 2026-10-26 | **S$^2$-RL: Sample-Set Dual Reinforcement Learning for Generative Semantic Segmentation Dataset Distillation**<br><sub>Haoyu Wang, Fei Zhou, Qingqing Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35491) · [PDF](https://arxiv.org/pdf/2610.35491) |
| 2026-10-26 | **TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration**<br><sub>Zhengxin Li, Chongzhen Tian, Hui Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35489) · [PDF](https://arxiv.org/pdf/2610.35489) · [Code](https://github.com/yuanhui0325/TP-JSCC) |
| 2026-10-26 | **Domain-Adapted Latent Diffusion Models for CT-to-PET Image Translation**<br><sub>Yann Bourdé, Lea Bogensperger, Arnela Hadzic et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35132) · [PDF](https://arxiv.org/pdf/2610.35132) |
| 2026-10-26 | **Synthetic Child-Adult Interactions Are Not Developmentally Plausible**<br><sub>Bastian Bunzeck, Francesca Padovani</sub> | [arXiv](https://arxiv.org/abs/2610.35029) · [PDF](https://arxiv.org/pdf/2610.35029) |
| 2026-10-26 | **RubriX: A Fast, Fine-Tunable Non-Autoregressive Rubric Judge**<br><sub>Balamurugan Paramasivam, Sudalai Rajkumar</sub> | [arXiv](https://arxiv.org/abs/2610.34875) · [PDF](https://arxiv.org/pdf/2610.34875) · [Code](https://huggingface.co/CobuildX-AI/RubriX-8B) |
| 2026-10-26 | **Transporting Quantiles to Codebook: Scalable Vector Quantization without Codebook Collapse**<br><sub>Yuwei Zeng, Zekun Shi</sub> | [arXiv](https://arxiv.org/abs/2610.34828) · [PDF](https://arxiv.org/pdf/2610.34828) |
| 2026-10-26 | **SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference**<br><sub>Yanzhen Zhou, Zhengyu Han, Qunyou Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34824) · [PDF](https://arxiv.org/pdf/2610.34824) |
| 2026-10-26 | **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**<br><sub>Caiyi Sun, Yujing Sun, Siu-Ming Yiu</sub> | [arXiv](https://arxiv.org/abs/2610.34782) · [PDF](https://arxiv.org/pdf/2610.34782) · [Code](https://github.com/scy639/ToDoPro) |
| 2026-10-26 | **Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching**<br><sub>Fei Zuo, Yizhou Huang, Kezhi Wang</sub> | [arXiv](https://arxiv.org/abs/2610.34756) · [PDF](https://arxiv.org/pdf/2610.34756) |
| 2026-10-26 | **MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference**<br><sub>Huaizhi Zhang, Jiacheng Zhu, Xuqi Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34731) · [PDF](https://arxiv.org/pdf/2610.34731) |
| 2026-10-26 | **VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware**<br><sub>Borui Xu, Hongshi Tan, Wenqi Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34717) · [PDF](https://arxiv.org/pdf/2610.34717) |
| 2026-10-26 | **Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents**<br><sub>Xinyu Zhang, Weiwei Sun</sub> | [arXiv](https://arxiv.org/abs/2610.34673) · [PDF](https://arxiv.org/pdf/2610.34673) |
| 2026-10-25 | **HobbyLM: A Sparse Mixture-of-Experts Model Family on a Hobby Budget**<br><sub>Harish Santhanalakshmi Ganesan, Hariharan M. S., Prabhurajhan R</sub> | [arXiv](https://arxiv.org/abs/2610.34582) · [PDF](https://arxiv.org/pdf/2610.34582) |
| 2026-10-25 | **Cumulative Marginal Matching for One-Step Diffusion**<br><sub>Paribesh Regmi, Rui Li</sub> | [arXiv](https://arxiv.org/abs/2610.34575) · [PDF](https://arxiv.org/pdf/2610.34575) |
| 2026-10-25 | **Recursive CLIP: Vision-Language Distillation with Looped Transformer Blocks**<br><sub>Szymon Mazurek, Alberto Presta, Michał Byra</sub> | [arXiv](https://arxiv.org/abs/2610.34563) · [PDF](https://arxiv.org/pdf/2610.34563) |
| 2026-10-25 | **VTC-AUDIT: An Interventional Reliability Audit for Visual-Token Compression under Paired Image Shifts**<br><sub>Isaac, Li</sub> | [arXiv](https://arxiv.org/abs/2610.34545) · [PDF](https://arxiv.org/pdf/2610.34545) · [Code](https://github.com/IsaacLi74/VTC-AUDIT) |

[View all 41 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **198 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **Transporting Quantiles to Codebook: Scalable Vector Quantization without Codebook Collapse**<br><sub>Yuwei Zeng, Zekun Shi</sub> | [arXiv](https://arxiv.org/abs/2610.34828) · [PDF](https://arxiv.org/pdf/2610.34828) |
| 2026-10-26 | **VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware**<br><sub>Borui Xu, Hongshi Tan, Wenqi Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34717) · [PDF](https://arxiv.org/pdf/2610.34717) |
| 2026-10-25 | **QECGBERT: A Scalable ECG Foundation Model Based on Self-Supervised Language Learning via VQ-VAE Waveform Tokenization**<br><sub>Aruna Mohan, Burcu Ozek, Or Zilbershot et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33964) · [PDF](https://arxiv.org/pdf/2610.33964) |
| 2026-10-24 | **RAQ-MLA: Role-Aware Quantization for Multi-Head Latent Attention Caches**<br><sub>Tianqi Chen, Xunchao Li, Linchuan Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33625) · [PDF](https://arxiv.org/pdf/2610.33625) |
| 2026-10-23 | **Measuring the Energy Cost of Completing Tasks with Quantized Language-Model Agents**<br><sub>Stephen Abkin, Aldric Yang, Alex Flesher et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32417) · [PDF](https://arxiv.org/pdf/2610.32417) |
| 2026-10-23 | **BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization**<br><sub>David Jin, Beshr IslamBouli, Tarushii Goel et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32243) · [PDF](https://arxiv.org/pdf/2610.32243) |
| 2026-10-23 | **MPQ: A Message-Passing View of Post-Training Quantization**<br><sub>Yanshuo Chen, Chenxi Liu, Reza Shirkavand et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32127) · [PDF](https://arxiv.org/pdf/2610.32127) · [Code](https://github.com/poseidonchan/MPQ) |
| 2026-10-22 | **Low-Bit N-Gram Embeddings for Language Models**<br><sub>Stephen Chung, Wenyu Du</sub> | [arXiv](https://arxiv.org/abs/2610.31646) · [PDF](https://arxiv.org/pdf/2610.31646) |
| 2026-10-22 | **SQuAT: Spherical Lattice Vector Quantization-Aware Training**<br><sub>Sebastian Loeschcke, Ivan Koryakovskiy, Tycho F. A. van der Ouderaa et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31412) · [PDF](https://arxiv.org/pdf/2610.31412) |
| 2026-10-22 | **Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization**<br><sub>Jiacheng Liu, Yaxin Luo, Xiaohan Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31309) · [PDF](https://arxiv.org/pdf/2610.31309) · [Code](https://github.com/VILA-Lab/optic) |
| 2026-10-22 | **Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for Diffusion Language Models**<br><sub>Ofek Avivi, Eliron Rahimi, Avi Mendelson et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31198) · [PDF](https://arxiv.org/pdf/2610.31198) |
| 2026-10-22 | **ProQuant: Preserving Expert Quality over Quantity in Ultra-Low-Bit Quantization of Mixture-of-Experts Models**<br><sub>Jiaqi Chen, Xianglong Yan, Chengzhu Bao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30779) · [PDF](https://arxiv.org/pdf/2610.30779) · [Code](https://github.com/ThrowBug/ProQuant.git) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **193 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration**<br><sub>Zhengxin Li, Chongzhen Tian, Hui Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35489) · [PDF](https://arxiv.org/pdf/2610.35489) · [Code](https://github.com/yuanhui0325/TP-JSCC) |
| 2026-10-26 | **Domain-Adapted Latent Diffusion Models for CT-to-PET Image Translation**<br><sub>Yann Bourdé, Lea Bogensperger, Arnela Hadzic et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35132) · [PDF](https://arxiv.org/pdf/2610.35132) |
| 2026-10-26 | **SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference**<br><sub>Yanzhen Zhou, Zhengyu Han, Qunyou Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34824) · [PDF](https://arxiv.org/pdf/2610.34824) |
| 2026-10-26 | **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**<br><sub>Caiyi Sun, Yujing Sun, Siu-Ming Yiu</sub> | [arXiv](https://arxiv.org/abs/2610.34782) · [PDF](https://arxiv.org/pdf/2610.34782) · [Code](https://github.com/scy639/ToDoPro) |
| 2026-10-26 | **Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching**<br><sub>Fei Zuo, Yizhou Huang, Kezhi Wang</sub> | [arXiv](https://arxiv.org/abs/2610.34756) · [PDF](https://arxiv.org/pdf/2610.34756) |
| 2026-10-25 | **VTC-AUDIT: An Interventional Reliability Audit for Visual-Token Compression under Paired Image Shifts**<br><sub>Isaac, Li</sub> | [arXiv](https://arxiv.org/abs/2610.34545) · [PDF](https://arxiv.org/pdf/2610.34545) · [Code](https://github.com/IsaacLi74/VTC-AUDIT) |
| 2026-10-25 | **T2D: Target-to-Draft Model Pruning &amp; Adaptation for Efficient Speculative Decoding**<br><sub>Shahriar Kabir Nahin, Xiao Ye, Muhao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34103) · [PDF](https://arxiv.org/pdf/2610.34103) |
| 2026-10-24 | **Rescuing Your Pruning: Rethinking Visual Token Pruning and Post-Training Recovery in MLLMs**<br><sub>Peiran Yin, Hao Wu, Zihao Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33688) · [PDF](https://arxiv.org/pdf/2610.33688) |
| 2026-10-23 | **Vision Token Pruning via Query-Vision Interaction Decomposition**<br><sub>Harshithanjani Athi, Sravan Kumar Ankireddy, Jianzhong Charlie Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33215) · [PDF](https://arxiv.org/pdf/2610.33215) |
| 2026-10-23 | **LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents**<br><sub>Shen Liu, Ze Zhou, Zhenguo Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32412) · [PDF](https://arxiv.org/pdf/2610.32412) |
| 2026-10-22 | **LazyFlash: Forward-Dense, Backward-Sparse Attention for Accelerated Long-Context Fine-Tuning**<br><sub>Keqi Deng, Ruchao Fan, Jinyu Li</sub> | [arXiv](https://arxiv.org/abs/2610.31911) · [PDF](https://arxiv.org/pdf/2610.31911) |
| 2026-10-22 | **Nested Sparsity for Scalable Pretraining and Continual Learning**<br><sub>Tianzhe Chu, Druv Pai, Yi Ma</sub> | [arXiv](https://arxiv.org/abs/2610.31818) · [PDF](https://arxiv.org/pdf/2610.31818) · [Code](https://github.com/Ma-Lab-Berkeley/Nestor) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **433 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **OSWAM: An Effective World Action Model with One-Step Action Generation**<br><sub>Guowen Zhang, Liyi Chen, Xu Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35850) · [PDF](https://arxiv.org/pdf/2610.35850) |
| 2026-10-26 | **Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models**<br><sub>Aidar Myrzakhan, Zhiqiang Shen</sub> | [arXiv](https://arxiv.org/abs/2610.35804) · [PDF](https://arxiv.org/pdf/2610.35804) · [Code](https://github.com/VILA-Lab/dSpark) |
| 2026-10-26 | **EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation**<br><sub>Yitao Xiao, Xu Zhang, Ye Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35690) · [PDF](https://arxiv.org/pdf/2610.35690) · [Code](https://github.com/CenYangtze/EvoRouter) |
| 2026-10-26 | **Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation**<br><sub>Junyi Chen, Haiyu Zhang, Zhoujie Fu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35594) · [PDF](https://arxiv.org/pdf/2610.35594) |
| 2026-10-26 | **S$^2$-RL: Sample-Set Dual Reinforcement Learning for Generative Semantic Segmentation Dataset Distillation**<br><sub>Haoyu Wang, Fei Zhou, Qingqing Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35491) · [PDF](https://arxiv.org/pdf/2610.35491) |
| 2026-10-25 | **Cumulative Marginal Matching for One-Step Diffusion**<br><sub>Paribesh Regmi, Rui Li</sub> | [arXiv](https://arxiv.org/abs/2610.34575) · [PDF](https://arxiv.org/pdf/2610.34575) |
| 2026-10-25 | **Recursive CLIP: Vision-Language Distillation with Looped Transformer Blocks**<br><sub>Szymon Mazurek, Alberto Presta, Michał Byra</sub> | [arXiv](https://arxiv.org/abs/2610.34563) · [PDF](https://arxiv.org/pdf/2610.34563) |
| 2026-10-25 | **CoLink: Global Compression and Knowledge Linking for Multi-Turn Dialogue Modeling**<br><sub>Lian Yan, Zhenbo Xia, Haotian Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34335) · [PDF](https://arxiv.org/pdf/2610.34335) |
| 2026-10-25 | **Timing Matters Twice: When to Query and When to Skip in Flow-Matching On-Policy Distillation**<br><sub>Renye Yan, Junyi Zhan, Jikang Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34191) · [PDF](https://arxiv.org/pdf/2610.34191) |
| 2026-10-25 | **Freeze What Is Settled, Cache What Is Smooth: Spatial Freezing Keeps Step Caching in Its Low-Error Regime**<br><sub>Baiyan Li, Ganxuan Yang</sub> | [arXiv](https://arxiv.org/abs/2610.34177) · [PDF](https://arxiv.org/pdf/2610.34177) |
| 2026-10-25 | **T2D: Target-to-Draft Model Pruning &amp; Adaptation for Efficient Speculative Decoding**<br><sub>Shahriar Kabir Nahin, Xiao Ye, Muhao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34103) · [PDF](https://arxiv.org/pdf/2610.34103) |
| 2026-10-25 | **Learning the Autoregressive: Direct Score-Difference Estimation with Amortized Future Credit for Video Distillation**<br><sub>Zixuan Duan, Yabo Chen, Xunzhi Xiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34092) · [PDF](https://arxiv.org/pdf/2610.34092) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **133 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **Synthetic Child-Adult Interactions Are Not Developmentally Plausible**<br><sub>Bastian Bunzeck, Francesca Padovani</sub> | [arXiv](https://arxiv.org/abs/2610.35029) · [PDF](https://arxiv.org/pdf/2610.35029) |
| 2026-10-26 | **RubriX: A Fast, Fine-Tunable Non-Autoregressive Rubric Judge**<br><sub>Balamurugan Paramasivam, Sudalai Rajkumar</sub> | [arXiv](https://arxiv.org/abs/2610.34875) · [PDF](https://arxiv.org/pdf/2610.34875) · [Code](https://huggingface.co/CobuildX-AI/RubriX-8B) |
| 2026-10-26 | **Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching**<br><sub>Fei Zuo, Yizhou Huang, Kezhi Wang</sub> | [arXiv](https://arxiv.org/abs/2610.34756) · [PDF](https://arxiv.org/pdf/2610.34756) |
| 2026-10-24 | **Task Format as a Factor in Adaptation: A Controlled Comparison of LoRA and Full Fine-Tuning for Prompt-Safety Classification**<br><sub>John Alderete, Srirakshith Betageri, Jennifer Flynn et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33813) · [PDF](https://arxiv.org/pdf/2610.33813) |
| 2026-10-23 | **Rethinking LoRA Initialization for Robust Asymmetric Learning Rates**<br><sub>Disen Liao, Yaoliang Yu</sub> | [arXiv](https://arxiv.org/abs/2610.32142) · [PDF](https://arxiv.org/pdf/2610.32142) |
| 2026-10-22 | **FSVL: Taxonomic Fast-Slow Vision-to-Language Collaborative Framework for Interpretable Confusable Fish Species Identification and Knowledge Generation in the Middle Yangtze River**<br><sub>Meng Liang, Fucheng Wang, Lang Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31880) · [PDF](https://arxiv.org/pdf/2610.31880) |
| 2026-10-22 | **Parameter-Efficient Adaptation of Large Language Models to a Low-Resource Agglutinative Language: A Corpus, Datasets, and a Reproducible Benchmark for the Bashkir Language**<br><sub>Mullosharaf K. Arabov, Svetlana S. Khaybullina</sub> | [arXiv](https://arxiv.org/abs/2610.31397) · [PDF](https://arxiv.org/pdf/2610.31397) |
| 2026-10-21 | **AQL-Lite: Enabling Efficient Knowledge Acquisition for Arabic LLMs via Data-Centric Continual Pretraining**<br><sub>Houssam Eddine Boukhalfa, Mourad Bouache, Mourad Dahmane</sub> | [arXiv](https://arxiv.org/abs/2610.30344) · [PDF](https://arxiv.org/pdf/2610.30344) |
| 2026-10-21 | **Our Own Jev: Typed Decisions in One Forward Pass, from an In-House Judge to Open LoRA Models**<br><sub>Yuchuan Weng, Chi Liu, Xin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29052) · [PDF](https://arxiv.org/pdf/2610.29052) |
| 2026-10-20 | **Complexity-Aware Surgical Video Reasoning Segmentation with Digital Twin and Context Memory**<br><sub>Yiqing Shen, Mathias Unberath</sub> | [arXiv](https://arxiv.org/abs/2610.28776) · [PDF](https://arxiv.org/pdf/2610.28776) |
| 2026-10-20 | **MuPACE: Learning to Pace Muon for LoRA Fine-Tuning**<br><sub>Jan Kobiolka, Christian Frey, Josif Grabocka</sub> | [arXiv](https://arxiv.org/abs/2610.28072) · [PDF](https://arxiv.org/pdf/2610.28072) |
| 2026-10-20 | **Building Telecom Language Models with RSOD: Domain Data, Specialist Post-Training, Memory-Conscious Distillation, and Networking Evaluation**<br><sub>Anil Srirangapatna Nagesh, Nitin Gupta, Anuj Taneja et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27993) · [PDF](https://arxiv.org/pdf/2610.27993) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **189 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference**<br><sub>Yanzhen Zhou, Zhengyu Han, Qunyou Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34824) · [PDF](https://arxiv.org/pdf/2610.34824) |
| 2026-10-26 | **MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference**<br><sub>Huaizhi Zhang, Jiacheng Zhu, Xuqi Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34731) · [PDF](https://arxiv.org/pdf/2610.34731) |
| 2026-10-25 | **Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2610.34436) · [PDF](https://arxiv.org/pdf/2610.34436) |
| 2026-10-24 | **ZipFusion: Fusing Lossless KV Decompression with Attention for Efficient LLM Decoding**<br><sub>Yuetao Chen, Peng Wang, Hong Xu</sub> | [arXiv](https://arxiv.org/abs/2610.33719) · [PDF](https://arxiv.org/pdf/2610.33719) |
| 2026-10-23 | **Video-MemComp: Taylor-Guided Sensitivity-Aware Memory Management for Streaming Video Understanding**<br><sub>Yonghui Niu, Yuhao Ji, Chang Nie et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32784) · [PDF](https://arxiv.org/pdf/2610.32784) |
| 2026-10-22 | **LazyFlash: Forward-Dense, Backward-Sparse Attention for Accelerated Long-Context Fine-Tuning**<br><sub>Keqi Deng, Ruchao Fan, Jinyu Li</sub> | [arXiv](https://arxiv.org/abs/2610.31911) · [PDF](https://arxiv.org/pdf/2610.31911) |
| 2026-10-22 | **KVStream: Adaptive Parallel Storage Management for KV Caching in Large-Scale LLM Serving**<br><sub>Avinash Maurya, Jaiaid Mobin, Jie Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31827) · [PDF](https://arxiv.org/pdf/2610.31827) |
| 2026-10-22 | **Rethinking Sequence Compression with Test-time Regression**<br><sub>Sihan Yang, Jie Huang, Hanxuan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31574) · [PDF](https://arxiv.org/pdf/2610.31574) |
| 2026-10-22 | **Drift Says When, Budget Says How Much: Rate-Controlled KV Re-selection for Long-Form Multimodal Generation**<br><sub>Bin Hu, Yingbo Xiao</sub> | [arXiv](https://arxiv.org/abs/2610.31433) · [PDF](https://arxiv.org/pdf/2610.31433) |
| 2026-10-22 | **Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization**<br><sub>Jiacheng Liu, Yaxin Luo, Xiaohan Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31309) · [PDF](https://arxiv.org/pdf/2610.31309) · [Code](https://github.com/VILA-Lab/optic) |
| 2026-10-22 | **Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving**<br><sub>Maharani A. P. Irawan, Kuntai Du, Jiayi Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30791) · [PDF](https://arxiv.org/pdf/2610.30791) |
| 2026-10-21 | **HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference**<br><sub>Junhyeok Park, Jungeun Yoon, Kyungmin Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29873) · [PDF](https://arxiv.org/pdf/2610.29873) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **129 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-25 | **Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2610.34436) · [PDF](https://arxiv.org/pdf/2610.34436) |
| 2026-10-25 | **T2D: Target-to-Draft Model Pruning &amp; Adaptation for Efficient Speculative Decoding**<br><sub>Shahriar Kabir Nahin, Xiao Ye, Muhao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34103) · [PDF](https://arxiv.org/pdf/2610.34103) |
| 2026-10-24 | **One Call Ahead: Packed Self-Speculative Decoding with Diffusion Drafting**<br><sub>Yuxiao Chen, Changxiao Cai</sub> | [arXiv](https://arxiv.org/abs/2610.33379) · [PDF](https://arxiv.org/pdf/2610.33379) |
| 2026-10-23 | **NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding**<br><sub>Nilesh Prasad Pandey, Jangseon Park, Jason Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32881) · [PDF](https://arxiv.org/pdf/2610.32881) |
| 2026-10-23 | **MAGIC: Margin-gated Contrastive Debiasing with Evidence Restoration for VLM Test-time Robustness Scaling**<br><sub>Shunshun Gu, Enze Zhang, Ming Pei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32013) · [PDF](https://arxiv.org/pdf/2610.32013) |
| 2026-10-22 | **ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding**<br><sub>Liang He, SiYuan Ma, Qishi Zhan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31338) · [PDF](https://arxiv.org/pdf/2610.31338) |
| 2026-10-21 | **UlaCache: Unified Logical Addressing for Sparse LLM Serving**<br><sub>Isaac Zhu, Alan Cao, Hugh Yin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29820) · [PDF](https://arxiv.org/pdf/2610.29820) |
| 2026-10-21 | **RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding**<br><sub>Mingkang Liu, Weiming Meng, Peipei Jiao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29527) · [PDF](https://arxiv.org/pdf/2610.29527) |
| 2026-10-21 | **Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding**<br><sub>Jungseob Lee, Hogun Seong, Euijun Choi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29013) · [PDF](https://arxiv.org/pdf/2610.29013) · [Code](https://github.com/js-lee-AI/TargetRegeneration) |
| 2026-10-19 | **DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding**<br><sub>Shreyas Kulkarni, Uttam Gurram, Madhav Kanda et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27379) · [PDF](https://arxiv.org/pdf/2610.27379) |
| 2026-10-19 | **TEX: Test-Time Scaling Testing Agents via Execution-based Cross-Validation**<br><sub>Akash Gokul, Srijan Bansal, Yingbo Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27290) · [PDF](https://arxiv.org/pdf/2610.27290) |
| 2026-10-19 | **CALM: Consistency-Aware Logit Masking in Decoding Space for Mitigating Overthinking of Large Reasoning Models**<br><sub>Shengjing Liu, Feiyang Li, Yuxuan Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25908) · [PDF](https://arxiv.org/pdf/2610.25908) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **200 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation**<br><sub>Yitao Xiao, Xu Zhang, Ye Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35690) · [PDF](https://arxiv.org/pdf/2610.35690) · [Code](https://github.com/CenYangtze/EvoRouter) |
| 2026-10-26 | **TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration**<br><sub>Zhengxin Li, Chongzhen Tian, Hui Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35489) · [PDF](https://arxiv.org/pdf/2610.35489) · [Code](https://github.com/yuanhui0325/TP-JSCC) |
| 2026-10-26 | **MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference**<br><sub>Huaizhi Zhang, Jiacheng Zhu, Xuqi Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34731) · [PDF](https://arxiv.org/pdf/2610.34731) |
| 2026-10-26 | **Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents**<br><sub>Xinyu Zhang, Weiwei Sun</sub> | [arXiv](https://arxiv.org/abs/2610.34673) · [PDF](https://arxiv.org/pdf/2610.34673) |
| 2026-10-24 | **ZipFusion: Fusing Lossless KV Decompression with Attention for Efficient LLM Decoding**<br><sub>Yuetao Chen, Peng Wang, Hong Xu</sub> | [arXiv](https://arxiv.org/abs/2610.33719) · [PDF](https://arxiv.org/pdf/2610.33719) |
| 2026-10-24 | **DualPace: Decoupled Scheduling and Cooperative GPU--CPU Decoding for LLM Serving**<br><sub>YuXuan Lin, KeQiang Wu, Kingsum Chow</sub> | [arXiv](https://arxiv.org/abs/2610.33501) · [PDF](https://arxiv.org/pdf/2610.33501) |
| 2026-10-24 | **COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies**<br><sub>Hanming Zhang, Erhu Feng</sub> | [arXiv](https://arxiv.org/abs/2610.33404) · [PDF](https://arxiv.org/pdf/2610.33404) |
| 2026-10-24 | **Fast Instinct, Slow Reason: A Dual-Speed Agentic Framework for Self-Configuring Multi-Object Tracking in Satellite Video**<br><sub>Fan He, Baining Wu, Yan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33396) · [PDF](https://arxiv.org/pdf/2610.33396) |
| 2026-10-23 | **KnitTrans: Coordinated Trajectory Transfer for Effective and Efficient LLM Reinforcement Learning**<br><sub>Bangjun Xiao, Chiheng Lou, Xiaodong Ji et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32389) · [PDF](https://arxiv.org/pdf/2610.32389) |
| 2026-10-23 | **Lifelong Context Adaptation through Bidirectional Memory-Skill Learning**<br><sub>Tianyi Xu, Huazheng Wang</sub> | [arXiv](https://arxiv.org/abs/2610.32295) · [PDF](https://arxiv.org/pdf/2610.32295) · [Code](https://github.com/tianyi0216/Memcryst.git) |
| 2026-10-22 | **LazyFlash: Forward-Dense, Backward-Sparse Attention for Accelerated Long-Context Fine-Tuning**<br><sub>Keqi Deng, Ruchao Fan, Jinyu Li</sub> | [arXiv](https://arxiv.org/abs/2610.31911) · [PDF](https://arxiv.org/pdf/2610.31911) |
| 2026-10-22 | **FSVL: Taxonomic Fast-Slow Vision-to-Language Collaborative Framework for Interpretable Confusable Fish Species Identification and Knowledge Generation in the Middle Yangtze River**<br><sub>Meng Liang, Fucheng Wang, Lang Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31880) · [PDF](https://arxiv.org/pdf/2610.31880) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **111 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**<br><sub>Caiyi Sun, Yujing Sun, Siu-Ming Yiu</sub> | [arXiv](https://arxiv.org/abs/2610.34782) · [PDF](https://arxiv.org/pdf/2610.34782) · [Code](https://github.com/scy639/ToDoPro) |
| 2026-10-25 | **Freeze What Is Settled, Cache What Is Smooth: Spatial Freezing Keeps Step Caching in Its Low-Error Regime**<br><sub>Baiyan Li, Ganxuan Yang</sub> | [arXiv](https://arxiv.org/abs/2610.34177) · [PDF](https://arxiv.org/pdf/2610.34177) |
| 2026-10-24 | **H-GLow: Accelerating Graph Generation via Hazard-Guided Discrete Flow Matching**<br><sub>Sirine Ayadi, Stephan Günnemann</sub> | [arXiv](https://arxiv.org/abs/2610.33599) · [PDF](https://arxiv.org/pdf/2610.33599) |
| 2026-10-24 | **UltraFlash: Accelerating Megapixel Visual Synthesis**<br><sub>Phuc Lai, Anh Nguyen, Phong Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33581) · [PDF](https://arxiv.org/pdf/2610.33581) |
| 2026-10-23 | **SCDM-HTD: Spectral-Wise Conditional Diffusion Model for Hyperspectral Target Detection**<br><sub>Dunbin Shen, Wenfeng Kong, Jianjun Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32768) · [PDF](https://arxiv.org/pdf/2610.32768) |
| 2026-10-22 | **CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation**<br><sub>Lifan Jiang, Yibo Zhao, Senlin cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30854) · [PDF](https://arxiv.org/pdf/2610.30854) |
| 2026-10-22 | **ParaLin++: Accelerating Parallel Diffusion Integrator via Intrinsic Partially Linear Structure**<br><sub>Jianrong Lu, Zhiyu Zhu, Hui Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30704) · [PDF](https://arxiv.org/pdf/2610.30704) |
| 2026-10-21 | **SAKURA: Serving Attention Key-Value State Under Rate Adaptation for Private Image Editing on Phones**<br><sub>Shuncheng Jie, Desen Sun, Ri Hong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29733) · [PDF](https://arxiv.org/pdf/2610.29733) |
| 2026-10-20 | **DiffResearch: Accelerating Deep Research with Diffusion Language Models**<br><sub>Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28909) · [PDF](https://arxiv.org/pdf/2610.28909) |
| 2026-10-20 | **Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks**<br><sub>Ivan Listopadov, Maksim Nakhodnov, Aibek Alanov</sub> | [arXiv](https://arxiv.org/abs/2610.28889) · [PDF](https://arxiv.org/pdf/2610.28889) |
| 2026-10-20 | **TeCoP: Accelerating Diffusion Large Language Model Decoding via Tentative Context Pipelining**<br><sub>Jui-Chien Tsou, Hsuan-Chi Liu, Wei-Chin Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27583) · [PDF](https://arxiv.org/pdf/2610.27583) |
| 2026-10-19 | **DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding**<br><sub>Shreyas Kulkarni, Uttam Gurram, Madhav Kanda et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27379) · [PDF](https://arxiv.org/pdf/2610.27379) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **176 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-26 | **Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation**<br><sub>Junyi Chen, Haiyu Zhang, Zhoujie Fu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35594) · [PDF](https://arxiv.org/pdf/2610.35594) |
| 2026-10-26 | **S$^2$-RL: Sample-Set Dual Reinforcement Learning for Generative Semantic Segmentation Dataset Distillation**<br><sub>Haoyu Wang, Fei Zhou, Qingqing Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35491) · [PDF](https://arxiv.org/pdf/2610.35491) |
| 2026-10-26 | **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**<br><sub>Caiyi Sun, Yujing Sun, Siu-Ming Yiu</sub> | [arXiv](https://arxiv.org/abs/2610.34782) · [PDF](https://arxiv.org/pdf/2610.34782) · [Code](https://github.com/scy639/ToDoPro) |
| 2026-10-25 | **HobbyLM: A Sparse Mixture-of-Experts Model Family on a Hobby Budget**<br><sub>Harish Santhanalakshmi Ganesan, Hariharan M. S., Prabhurajhan R</sub> | [arXiv](https://arxiv.org/abs/2610.34582) · [PDF](https://arxiv.org/pdf/2610.34582) |
| 2026-10-25 | **Timing Matters Twice: When to Query and When to Skip in Flow-Matching On-Policy Distillation**<br><sub>Renye Yan, Junyi Zhan, Jikang Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34191) · [PDF](https://arxiv.org/pdf/2610.34191) |
| 2026-10-25 | **Learning the Autoregressive: Direct Score-Difference Estimation with Amortized Future Credit for Video Distillation**<br><sub>Zixuan Duan, Yabo Chen, Xunzhi Xiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34092) · [PDF](https://arxiv.org/pdf/2610.34092) |
| 2026-10-24 | **TrackTok: Object-Centric Video Tokenization with Semantically Persistent Tokens**<br><sub>Nhi Pham, Christopher Wewer, Bernt Schiele et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33857) · [PDF](https://arxiv.org/pdf/2610.33857) · [Code](https://github.com/phamleyennhi/tracktok) |
| 2026-10-23 | **Fast and Useful: Adapting Distilled Generators for Visual Learning**<br><sub>Patryk Bartkowiak, Dominik Michels, Sören Pirk et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32512) · [PDF](https://arxiv.org/pdf/2610.32512) |
| 2026-10-23 | **UniWorld: A Unified World Model for Real-Time Visual World Simulation**<br><sub>Xin Zhang, Yabo Chen, Shuaiwei Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32381) · [PDF](https://arxiv.org/pdf/2610.32381) |
| 2026-10-23 | **Concept Acupuncturist: An Efficient and Precise Concept Erasure Method for Diffusion Models via Sparse Autoencoders**<br><sub>Yiran Xiahou, Siliang Qin, Kai Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32059) · [PDF](https://arxiv.org/pdf/2610.32059) · [Code](https://github.com/Eran-Xia/ConceptACP) |
| 2026-10-22 | **ResGVC: Residual Coding for High-fidelity Generative Video Compression**<br><sub>Ding Ding, Daowen Li, Ying Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31039) · [PDF](https://arxiv.org/pdf/2610.31039) |
| 2026-10-22 | **Direct Forcing: Single-Stage Training with Representation-Space Supervision for Few-Step Autoregressive Video Generation**<br><sub>Haojun Xu, Jie Huang, Chuyang Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30861) · [PDF](https://arxiv.org/pdf/2610.30861) |

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
