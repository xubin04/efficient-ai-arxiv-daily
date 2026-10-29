# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-29 15:09 CST** · **1333 unique papers** · Newest submission: **2026-10-27**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 203 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 198 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 441 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 137 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 192 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 130 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 206 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 112 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 180 |

## Newly indexed · 2026-10-29

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

No newly indexed papers in this scan.

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **203 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-27 | **CoS-VQ: Coordinated Shared-Scale Vector Quantization for Large Language Models**<br><sub>Zukang Xu, Zhixiong Zhao, Xing Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37336) · [PDF](https://arxiv.org/pdf/2610.37336) · [Code](https://github.com/xzktx003/Cos_VQ) |
| 2026-10-27 | **Efficient Quantization Training with Stochastic Rounding via Structured Subspace Randomness**<br><sub>Zeyu Wang, Yiheng Duan, Tao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36587) · [PDF](https://arxiv.org/pdf/2610.36587) |
| 2026-10-26 | **Training-Free Inference Acceleration for Video Large Language Models: Methods, Trade-offs, and Evaluation**<br><sub>Yuqi Li, Chuanyue Yan, Neil Rodrigues et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36327) · [PDF](https://arxiv.org/pdf/2610.36327) |
| 2026-10-26 | **Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs**<br><sub>Tianqi Chen, Xunchao Li, Linchuan Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35985) · [PDF](https://arxiv.org/pdf/2610.35985) |
| 2026-10-26 | **Transporting Quantiles to Codebook: Scalable Vector Quantization without Codebook Collapse**<br><sub>Yuwei Zeng, Zekun Shi</sub> | [arXiv](https://arxiv.org/abs/2610.34828) · [PDF](https://arxiv.org/pdf/2610.34828) |
| 2026-10-26 | **VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware**<br><sub>Borui Xu, Hongshi Tan, Wenqi Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34717) · [PDF](https://arxiv.org/pdf/2610.34717) |
| 2026-10-25 | **ResCom: Activation Residual Compensation for Large Language Model Quantization**<br><sub>Ning Yang, Bohan Cui, Zhuowen Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35955) · [PDF](https://arxiv.org/pdf/2610.35955) |
| 2026-10-25 | **QECGBERT: A Scalable ECG Foundation Model Based on Self-Supervised Language Learning via VQ-VAE Waveform Tokenization**<br><sub>Aruna Mohan, Burcu Ozek, Or Zilbershot et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33964) · [PDF](https://arxiv.org/pdf/2610.33964) |
| 2026-10-24 | **RAQ-MLA: Role-Aware Quantization for Multi-Head Latent Attention Caches**<br><sub>Tianqi Chen, Xunchao Li, Linchuan Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33625) · [PDF](https://arxiv.org/pdf/2610.33625) |
| 2026-10-23 | **Measuring the Energy Cost of Completing Tasks with Quantized Language-Model Agents**<br><sub>Stephen Abkin, Aldric Yang, Alex Flesher et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32417) · [PDF](https://arxiv.org/pdf/2610.32417) |
| 2026-10-23 | **BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization**<br><sub>David Jin, Beshr IslamBouli, Tarushii Goel et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32243) · [PDF](https://arxiv.org/pdf/2610.32243) |
| 2026-10-23 | **MPQ: A Message-Passing View of Post-Training Quantization**<br><sub>Yanshuo Chen, Chenxi Liu, Reza Shirkavand et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32127) · [PDF](https://arxiv.org/pdf/2610.32127) · [Code](https://github.com/poseidonchan/MPQ) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **198 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-27 | **3D-SceneQ: Empowering 3D LLM With Query-Guided Adaptive Pruning and Multi-Modal Feature Enhancement**<br><sub>Yongqi Shan, Lu Zhang, Jiazuo Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37202) · [PDF](https://arxiv.org/pdf/2610.37202) |
| 2026-10-27 | **Mechanistic Failure Modes of Weight Pruning in Transformer Language Models**<br><sub>Nabeelah Faumi, Deshan Sumanathilaka</sub> | [arXiv](https://arxiv.org/abs/2610.37126) · [PDF](https://arxiv.org/pdf/2610.37126) |
| 2026-10-27 | **On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime**<br><sub>Kensuke Sasaki, Issei Sato</sub> | [arXiv](https://arxiv.org/abs/2610.37085) · [PDF](https://arxiv.org/pdf/2610.37085) |
| 2026-10-27 | **LearnPrunerV2: Learnable Progressive Token Pruning for Vision-Language Models**<br><sub>Rinyoichi Takezoe, Yaqian Li, Weiren Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36986) · [PDF](https://arxiv.org/pdf/2610.36986) |
| 2026-10-27 | **Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs**<br><sub>Donghyeon Cho, Joowon Kim, Seungho Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36671) · [PDF](https://arxiv.org/pdf/2610.36671) |
| 2026-10-26 | **TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration**<br><sub>Zhengxin Li, Chongzhen Tian, Hui Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35489) · [PDF](https://arxiv.org/pdf/2610.35489) · [Code](https://github.com/yuanhui0325/TP-JSCC) |
| 2026-10-26 | **Domain-Adapted Latent Diffusion Models for CT-to-PET Image Translation**<br><sub>Yann Bourdé, Lea Bogensperger, Arnela Hadzic et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35132) · [PDF](https://arxiv.org/pdf/2610.35132) |
| 2026-10-26 | **SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference**<br><sub>Yanzhen Zhou, Zhengyu Han, Qunyou Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34824) · [PDF](https://arxiv.org/pdf/2610.34824) |
| 2026-10-26 | **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**<br><sub>Caiyi Sun, Yujing Sun, Siu-Ming Yiu</sub> | [arXiv](https://arxiv.org/abs/2610.34782) · [PDF](https://arxiv.org/pdf/2610.34782) · [Code](https://github.com/scy639/ToDoPro) |
| 2026-10-26 | **Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching**<br><sub>Fei Zuo, Yizhou Huang, Kezhi Wang</sub> | [arXiv](https://arxiv.org/abs/2610.34756) · [PDF](https://arxiv.org/pdf/2610.34756) |
| 2026-10-25 | **VTC-AUDIT: An Interventional Reliability Audit for Visual-Token Compression under Paired Image Shifts**<br><sub>Isaac, Li</sub> | [arXiv](https://arxiv.org/abs/2610.34545) · [PDF](https://arxiv.org/pdf/2610.34545) · [Code](https://github.com/IsaacLi74/VTC-AUDIT) |
| 2026-10-25 | **T2D: Target-to-Draft Model Pruning &amp; Adaptation for Efficient Speculative Decoding**<br><sub>Shahriar Kabir Nahin, Xiao Ye, Muhao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34103) · [PDF](https://arxiv.org/pdf/2610.34103) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **441 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-27 | **ALADDIN: Adversarial Latent Diffusion Distillation for One-Step Identity Swapping**<br><sub>Ivan Shchekotov, Timofei Gritsaev, Viacheslav Pirogov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37503) · [PDF](https://arxiv.org/pdf/2610.37503) |
| 2026-10-27 | **RPSD: Retrieval-Privileged On-Policy Self-Distillation with Optimal Transport**<br><sub>Dongyue Li, Zebang Cheng, Zhongyi Deng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37281) · [PDF](https://arxiv.org/pdf/2610.37281) |
| 2026-10-27 | **What Survives Distillation? A Mechanistic Interpretability Study of GPT-2 and DistilGPT-2**<br><sub>Nabeelah Faumi, Deshan Sumanathilaka</sub> | [arXiv](https://arxiv.org/abs/2610.37157) · [PDF](https://arxiv.org/pdf/2610.37157) |
| 2026-10-27 | **A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation**<br><sub>Wenwu Tang, Dong Wang, Yun Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37110) · [PDF](https://arxiv.org/pdf/2610.37110) |
| 2026-10-27 | **HiLo-RD: Cross-Budget Self-Distillation for Masked Diffusion Language Models**<br><sub>Xiang Li, Chengting Yu, Jungang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36901) · [PDF](https://arxiv.org/pdf/2610.36901) |
| 2026-10-27 | **Haste Makes Waste? Towards Safe Few-Step Text-to-Image Models**<br><sub>Lior Ziv, Mahmood Sharif</sub> | [arXiv](https://arxiv.org/abs/2610.36665) · [PDF](https://arxiv.org/pdf/2610.36665) |
| 2026-10-27 | **Proposing Better Rollouts for On-Policy Distillation**<br><sub>Sirui Chen, Yunzhe Qi, Haobo Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36477) · [PDF](https://arxiv.org/pdf/2610.36477) |
| 2026-10-27 | **Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation**<br><sub>Shufan Li, Hanrong Ye, Greg Heinrich et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36466) · [PDF](https://arxiv.org/pdf/2610.36466) |
| 2026-10-26 | **OSWAM: An Effective World Action Model with One-Step Action Generation**<br><sub>Guowen Zhang, Liyi Chen, Xu Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35850) · [PDF](https://arxiv.org/pdf/2610.35850) |
| 2026-10-26 | **Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models**<br><sub>Aidar Myrzakhan, Zhiqiang Shen</sub> | [arXiv](https://arxiv.org/abs/2610.35804) · [PDF](https://arxiv.org/pdf/2610.35804) · [Code](https://github.com/VILA-Lab/dSpark) |
| 2026-10-26 | **EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation**<br><sub>Yitao Xiao, Xu Zhang, Ye Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35690) · [PDF](https://arxiv.org/pdf/2610.35690) · [Code](https://github.com/CenYangtze/EvoRouter) |
| 2026-10-26 | **Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation**<br><sub>Junyi Chen, Haiyu Zhang, Zhoujie Fu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35594) · [PDF](https://arxiv.org/pdf/2610.35594) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **137 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-27 | **EnergyCal: Taming Loss Spikes in Muon-Family Optimizers for Sparse MoE Training**<br><sub>Masato Fujitake</sub> | [arXiv](https://arxiv.org/abs/2610.37062) · [PDF](https://arxiv.org/pdf/2610.37062) |
| 2026-10-27 | **V-LUMEN: Visual Lookup Memory for Embedding Scaling in Vision-Language Models**<br><sub>Miso Choi, Daekeun Kim, Eunji Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37019) · [PDF](https://arxiv.org/pdf/2610.37019) · [Code](https://github.com/miso-choi/V-Lumen) |
| 2026-10-27 | **Provenance Signatures for Low Rank Adaptations of Image Diffusion Models**<br><sub>Tobias Cheung, Mohan Dantam, Marc Juarez et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36933) · [PDF](https://arxiv.org/pdf/2610.36933) |
| 2026-10-27 | **CAMR: Compatibility-Aware Memory Replay for Continual Learning in Large Language Models**<br><sub>Jingpu Yang, Tianhao Li, Fengxian Ji et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36734) · [PDF](https://arxiv.org/pdf/2610.36734) |
| 2026-10-26 | **Synthetic Child-Adult Interactions Are Not Developmentally Plausible**<br><sub>Bastian Bunzeck, Francesca Padovani</sub> | [arXiv](https://arxiv.org/abs/2610.35029) · [PDF](https://arxiv.org/pdf/2610.35029) |
| 2026-10-26 | **RubriX: A Fast, Fine-Tunable Non-Autoregressive Rubric Judge**<br><sub>Balamurugan Paramasivam, Sudalai Rajkumar</sub> | [arXiv](https://arxiv.org/abs/2610.34875) · [PDF](https://arxiv.org/pdf/2610.34875) · [Code](https://huggingface.co/CobuildX-AI/RubriX-8B) |
| 2026-10-26 | **Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching**<br><sub>Fei Zuo, Yizhou Huang, Kezhi Wang</sub> | [arXiv](https://arxiv.org/abs/2610.34756) · [PDF](https://arxiv.org/pdf/2610.34756) |
| 2026-10-24 | **Task Format as a Factor in Adaptation: A Controlled Comparison of LoRA and Full Fine-Tuning for Prompt-Safety Classification**<br><sub>John Alderete, Srirakshith Betageri, Jennifer Flynn et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33813) · [PDF](https://arxiv.org/pdf/2610.33813) |
| 2026-10-23 | **Rethinking LoRA Initialization for Robust Asymmetric Learning Rates**<br><sub>Disen Liao, Yaoliang Yu</sub> | [arXiv](https://arxiv.org/abs/2610.32142) · [PDF](https://arxiv.org/pdf/2610.32142) |
| 2026-10-22 | **FSVL: Taxonomic Fast-Slow Vision-to-Language Collaborative Framework for Interpretable Confusable Fish Species Identification and Knowledge Generation in the Middle Yangtze River**<br><sub>Meng Liang, Fucheng Wang, Lang Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31880) · [PDF](https://arxiv.org/pdf/2610.31880) |
| 2026-10-22 | **Parameter-Efficient Adaptation of Large Language Models to a Low-Resource Agglutinative Language: A Corpus, Datasets, and a Reproducible Benchmark for the Bashkir Language**<br><sub>Mullosharaf K. Arabov, Svetlana S. Khaybullina</sub> | [arXiv](https://arxiv.org/abs/2610.31397) · [PDF](https://arxiv.org/pdf/2610.31397) |
| 2026-10-21 | **AQL-Lite: Enabling Efficient Knowledge Acquisition for Arabic LLMs via Data-Centric Continual Pretraining**<br><sub>Houssam Eddine Boukhalfa, Mourad Bouache, Mourad Dahmane</sub> | [arXiv](https://arxiv.org/abs/2610.30344) · [PDF](https://arxiv.org/pdf/2610.30344) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **192 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-27 | **Multi-State Linear Attention with Generalized Second-Order Routing**<br><sub>Hee Seung Hwang, Sanghyuk Chun, Xindi Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37645) · [PDF](https://arxiv.org/pdf/2610.37645) |
| 2026-10-27 | **DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models**<br><sub>Egor Maximov, Aleksei Merkelov, Vasiliy Alekseev et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36950) · [PDF](https://arxiv.org/pdf/2610.36950) |
| 2026-10-26 | **WAKMan: Workload Aware KVCache Manager**<br><sub>Suhas Kumar Morisetty, Vaibhavi Lokegaonkar, Sachin Mathew Varghese et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36355) · [PDF](https://arxiv.org/pdf/2610.36355) |
| 2026-10-26 | **SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference**<br><sub>Yanzhen Zhou, Zhengyu Han, Qunyou Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34824) · [PDF](https://arxiv.org/pdf/2610.34824) |
| 2026-10-26 | **MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference**<br><sub>Huaizhi Zhang, Jiacheng Zhu, Xuqi Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34731) · [PDF](https://arxiv.org/pdf/2610.34731) |
| 2026-10-25 | **Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2610.34436) · [PDF](https://arxiv.org/pdf/2610.34436) |
| 2026-10-24 | **ZipFusion: Fusing Lossless KV Decompression with Attention for Efficient LLM Decoding**<br><sub>Yuetao Chen, Peng Wang, Hong Xu</sub> | [arXiv](https://arxiv.org/abs/2610.33719) · [PDF](https://arxiv.org/pdf/2610.33719) |
| 2026-10-23 | **Video-MemComp: Taylor-Guided Sensitivity-Aware Memory Management for Streaming Video Understanding**<br><sub>Yonghui Niu, Yuhao Ji, Chang Nie et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32784) · [PDF](https://arxiv.org/pdf/2610.32784) |
| 2026-10-22 | **LazyFlash: Forward-Dense, Backward-Sparse Attention for Accelerated Long-Context Fine-Tuning**<br><sub>Keqi Deng, Ruchao Fan, Jinyu Li</sub> | [arXiv](https://arxiv.org/abs/2610.31911) · [PDF](https://arxiv.org/pdf/2610.31911) |
| 2026-10-22 | **KVStream: Adaptive Parallel Storage Management for KV Caching in Large-Scale LLM Serving**<br><sub>Avinash Maurya, Jaiaid Mobin, Jie Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31827) · [PDF](https://arxiv.org/pdf/2610.31827) |
| 2026-10-22 | **Rethinking Sequence Compression with Test-time Regression**<br><sub>Sihan Yang, Jie Huang, Hanxuan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31574) · [PDF](https://arxiv.org/pdf/2610.31574) |
| 2026-10-22 | **Drift Says When, Budget Says How Much: Rate-Controlled KV Re-selection for Long-Form Multimodal Generation**<br><sub>Bin Hu, Yingbo Xiao</sub> | [arXiv](https://arxiv.org/abs/2610.31433) · [PDF](https://arxiv.org/pdf/2610.31433) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **130 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-25 | **Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2610.34436) · [PDF](https://arxiv.org/pdf/2610.34436) |
| 2026-10-25 | **T2D: Target-to-Draft Model Pruning &amp; Adaptation for Efficient Speculative Decoding**<br><sub>Shahriar Kabir Nahin, Xiao Ye, Muhao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34103) · [PDF](https://arxiv.org/pdf/2610.34103) |
| 2026-10-25 | **Distributed LLM Inference via Communication-Efficient Speculative Decoding**<br><sub>Joohyun Shin, Byeonghyeon Park, Keumseo Ryum et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35957) · [PDF](https://arxiv.org/pdf/2610.35957) |
| 2026-10-24 | **One Call Ahead: Packed Self-Speculative Decoding with Diffusion Drafting**<br><sub>Yuxiao Chen, Changxiao Cai</sub> | [arXiv](https://arxiv.org/abs/2610.33379) · [PDF](https://arxiv.org/pdf/2610.33379) |
| 2026-10-23 | **NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding**<br><sub>Nilesh Prasad Pandey, Jangseon Park, Jason Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32881) · [PDF](https://arxiv.org/pdf/2610.32881) |
| 2026-10-23 | **MAGIC: Margin-gated Contrastive Debiasing with Evidence Restoration for VLM Test-time Robustness Scaling**<br><sub>Shunshun Gu, Enze Zhang, Ming Pei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32013) · [PDF](https://arxiv.org/pdf/2610.32013) |
| 2026-10-22 | **ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding**<br><sub>Liang He, SiYuan Ma, Qishi Zhan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31338) · [PDF](https://arxiv.org/pdf/2610.31338) |
| 2026-10-21 | **UlaCache: Unified Logical Addressing for Sparse LLM Serving**<br><sub>Isaac Zhu, Alan Cao, Hugh Yin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29820) · [PDF](https://arxiv.org/pdf/2610.29820) |
| 2026-10-21 | **RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding**<br><sub>Mingkang Liu, Weiming Meng, Peipei Jiao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29527) · [PDF](https://arxiv.org/pdf/2610.29527) |
| 2026-10-21 | **Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding**<br><sub>Jungseob Lee, Hogun Seong, Euijun Choi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29013) · [PDF](https://arxiv.org/pdf/2610.29013) · [Code](https://github.com/js-lee-AI/TargetRegeneration) |
| 2026-10-19 | **DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding**<br><sub>Shreyas Kulkarni, Uttam Gurram, Madhav Kanda et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27379) · [PDF](https://arxiv.org/pdf/2610.27379) |
| 2026-10-19 | **TEX: Test-Time Scaling Testing Agents via Execution-based Cross-Validation**<br><sub>Akash Gokul, Srijan Bansal, Yingbo Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27290) · [PDF](https://arxiv.org/pdf/2610.27290) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **206 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-27 | **Request-Adaptive Execution for Efficient Hybrid LLM Inference**<br><sub>Fahao Chen, Xuzhe Yan, Qi Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37432) · [PDF](https://arxiv.org/pdf/2610.37432) |
| 2026-10-27 | **TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving**<br><sub>Shuhuai Li, Shengdong Ye, Dongdong Ge et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37230) · [PDF](https://arxiv.org/pdf/2610.37230) |
| 2026-10-27 | **Is Your LLM Relay Serving What It Claims? A low-cost and high-power test for LLM Relay Auditing**<br><sub>Fangran Miao, Shengjie Niu, Jian Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37086) · [PDF](https://arxiv.org/pdf/2610.37086) |
| 2026-10-26 | **From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn**<br><sub>Jian Sheng, Sriram Vasudevan, Sundara Raman Ramachandran et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36383) · [PDF](https://arxiv.org/pdf/2610.36383) |
| 2026-10-26 | **Training-Free Inference Acceleration for Video Large Language Models: Methods, Trade-offs, and Evaluation**<br><sub>Yuqi Li, Chuanyue Yan, Neil Rodrigues et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36327) · [PDF](https://arxiv.org/pdf/2610.36327) |
| 2026-10-26 | **EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation**<br><sub>Yitao Xiao, Xu Zhang, Ye Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35690) · [PDF](https://arxiv.org/pdf/2610.35690) · [Code](https://github.com/CenYangtze/EvoRouter) |
| 2026-10-26 | **TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration**<br><sub>Zhengxin Li, Chongzhen Tian, Hui Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35489) · [PDF](https://arxiv.org/pdf/2610.35489) · [Code](https://github.com/yuanhui0325/TP-JSCC) |
| 2026-10-26 | **Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs**<br><sub>Tianqi Chen, Xunchao Li, Linchuan Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35985) · [PDF](https://arxiv.org/pdf/2610.35985) |
| 2026-10-26 | **MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference**<br><sub>Huaizhi Zhang, Jiacheng Zhu, Xuqi Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34731) · [PDF](https://arxiv.org/pdf/2610.34731) |
| 2026-10-26 | **Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents**<br><sub>Xinyu Zhang, Weiwei Sun</sub> | [arXiv](https://arxiv.org/abs/2610.34673) · [PDF](https://arxiv.org/pdf/2610.34673) |
| 2026-10-24 | **ZipFusion: Fusing Lossless KV Decompression with Attention for Efficient LLM Decoding**<br><sub>Yuetao Chen, Peng Wang, Hong Xu</sub> | [arXiv](https://arxiv.org/abs/2610.33719) · [PDF](https://arxiv.org/pdf/2610.33719) |
| 2026-10-24 | **DualPace: Decoupled Scheduling and Cooperative GPU--CPU Decoding for LLM Serving**<br><sub>YuXuan Lin, KeQiang Wu, Kingsum Chow</sub> | [arXiv](https://arxiv.org/abs/2610.33501) · [PDF](https://arxiv.org/pdf/2610.33501) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **112 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-27 | **Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs**<br><sub>Donghyeon Cho, Joowon Kim, Seungho Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36671) · [PDF](https://arxiv.org/pdf/2610.36671) |
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

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **180 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-27 | **ReferStream: Interactive Subject Injection for Streaming Video Generation**<br><sub>Shuolin Xu, Guanyuan Li, Boyu Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37566) · [PDF](https://arxiv.org/pdf/2610.37566) |
| 2026-10-27 | **A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation**<br><sub>Wenwu Tang, Dong Wang, Yun Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37110) · [PDF](https://arxiv.org/pdf/2610.37110) |
| 2026-10-27 | **Haste Makes Waste? Towards Safe Few-Step Text-to-Image Models**<br><sub>Lior Ziv, Mahmood Sharif</sub> | [arXiv](https://arxiv.org/abs/2610.36665) · [PDF](https://arxiv.org/pdf/2610.36665) |
| 2026-10-27 | **Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation**<br><sub>Shufan Li, Hanrong Ye, Greg Heinrich et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36466) · [PDF](https://arxiv.org/pdf/2610.36466) |
| 2026-10-26 | **Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation**<br><sub>Junyi Chen, Haiyu Zhang, Zhoujie Fu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35594) · [PDF](https://arxiv.org/pdf/2610.35594) |
| 2026-10-26 | **S$^2$-RL: Sample-Set Dual Reinforcement Learning for Generative Semantic Segmentation Dataset Distillation**<br><sub>Haoyu Wang, Fei Zhou, Qingqing Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35491) · [PDF](https://arxiv.org/pdf/2610.35491) |
| 2026-10-26 | **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**<br><sub>Caiyi Sun, Yujing Sun, Siu-Ming Yiu</sub> | [arXiv](https://arxiv.org/abs/2610.34782) · [PDF](https://arxiv.org/pdf/2610.34782) · [Code](https://github.com/scy639/ToDoPro) |
| 2026-10-25 | **HobbyLM: A Sparse Mixture-of-Experts Model Family on a Hobby Budget**<br><sub>Harish Santhanalakshmi Ganesan, Hariharan M. S., Prabhurajhan R</sub> | [arXiv](https://arxiv.org/abs/2610.34582) · [PDF](https://arxiv.org/pdf/2610.34582) |
| 2026-10-25 | **Timing Matters Twice: When to Query and When to Skip in Flow-Matching On-Policy Distillation**<br><sub>Renye Yan, Junyi Zhan, Jikang Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34191) · [PDF](https://arxiv.org/pdf/2610.34191) |
| 2026-10-25 | **Learning the Autoregressive: Direct Score-Difference Estimation with Amortized Future Credit for Video Distillation**<br><sub>Zixuan Duan, Yabo Chen, Xunzhi Xiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34092) · [PDF](https://arxiv.org/pdf/2610.34092) |
| 2026-10-24 | **TrackTok: Object-Centric Video Tokenization with Semantically Persistent Tokens**<br><sub>Nhi Pham, Christopher Wewer, Bernt Schiele et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33857) · [PDF](https://arxiv.org/pdf/2610.33857) · [Code](https://github.com/phamleyennhi/tracktok) |
| 2026-10-23 | **Fast and Useful: Adapting Distilled Generators for Visual Learning**<br><sub>Patryk Bartkowiak, Dominik Michels, Sören Pirk et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32512) · [PDF](https://arxiv.org/pdf/2610.32512) |

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
