# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-03 15:57 CST** · **1476 unique papers** · Newest submission: **2026-11-02**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 232 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 215 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 481 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 152 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 215 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 141 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 235 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 122 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 199 |

## Newly indexed · 2026-11-03

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-02 | **PlantVLM-Edge: Quantized Vision-Language Models for On-Device Crop Health Diagnosis**<br><sub>Gaurab Wagle, Bishal Adhikari, Jiajia Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03557) · [PDF](https://arxiv.org/pdf/2611.03557) |
| 2026-11-02 | **VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing**<br><sub>Yexin Liu, Yunlong Lin, Zehan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03404) · [PDF](https://arxiv.org/pdf/2611.03404) · [Code](https://github.com/LAW1223/VidDub) |
| 2026-11-02 | **Bagel: A Fast Bayesian Online Changepoint Detection Algorithm for Linear Models via Posterior Merging**<br><sub>Ziyang Yang, Paul Fearnhead, Dan Grose</sub> | [arXiv](https://arxiv.org/abs/2611.03230) · [PDF](https://arxiv.org/pdf/2611.03230) |
| 2026-11-02 | **CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention**<br><sub>Mohammed Dabbah, Izhak Golan, Oren Tropp et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03200) · [PDF](https://arxiv.org/pdf/2611.03200) |
| 2026-11-02 | **SurgPace: Complexity-Aware Progressive Distillation for Surgical Multimodal Large Language Models**<br><sub>Zhicheng He, Xiaohan Xing, Hongqiu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03125) · [PDF](https://arxiv.org/pdf/2611.03125) · [Code](https://github.com/hezhicheng2002/SurgPace) |
| 2026-11-02 | **Efficient Hybrid Distillation: Synergizing Score and Adversarial Objectives for One-Step Diffusion**<br><sub>Fei Peng, Junqiang Wu, Haoxian Tan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03017) · [PDF](https://arxiv.org/pdf/2611.03017) · [Code](https://github.com/pf0607/EASD) |
| 2026-11-02 | **Distilling Literary Sentiment from LLM Annotations into an Ordinal BERT Model**<br><sub>Artem Suslov, Takehiro Hashimoto</sub> | [arXiv](https://arxiv.org/abs/2611.02985) · [PDF](https://arxiv.org/pdf/2611.02985) |
| 2026-11-02 | **Introducing Cluster Efficiency to LLM Serving: Pooling Economical Accelerators over Fast Interconnects**<br><sub>Youhe Jiang, Pavle Glušac, Binhang Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02975) · [PDF](https://arxiv.org/pdf/2611.02975) |
| 2026-11-02 | **SHq: Learnable Grids for LLM Weight Quantization**<br><sub>Michael Helcig, Earl Killian, Dan Alistarh</sub> | [arXiv](https://arxiv.org/abs/2611.02966) · [PDF](https://arxiv.org/pdf/2611.02966) |
| 2026-11-02 | **SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding**<br><sub>Tianyu Liu, Jun Zhang, Wenjie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02846) · [PDF](https://arxiv.org/pdf/2611.02846) |
| 2026-11-02 | **OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation**<br><sub>Zihao Fan, Xin Lu, Jie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02803) · [PDF](https://arxiv.org/pdf/2611.02803) |
| 2026-11-02 | **History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models**<br><sub>Hangyi Kuang, Chengzhi Wang, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02782) · [PDF](https://arxiv.org/pdf/2611.02782) |
| 2026-11-02 | **Replay for LLM Continual Learning with Multi-Teacher On-Policy Distillation**<br><sub>Yiqiao Qiu</sub> | [arXiv](https://arxiv.org/abs/2611.02746) · [PDF](https://arxiv.org/pdf/2611.02746) |
| 2026-11-02 | **Accelerating LLM Pretraining with Zeroth-Order Curvature on Idle Serving Compute**<br><sub>Mingchuan Ma, Dongqi Cai, Daqian Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02688) · [PDF](https://arxiv.org/pdf/2611.02688) |
| 2026-11-02 | **Train the Sampler You Run: Few-Step Masked Diffusion Language Models via Mixture-Likelihood Fine-Tuning**<br><sub>Amin Najafgholizadeh</sub> | [arXiv](https://arxiv.org/abs/2611.02666) · [PDF](https://arxiv.org/pdf/2611.02666) |
| 2026-11-02 | **BasisKV: Value Latents for Communication and Key Routing**<br><sub>Lixun Zhang, Zishan Shao, Kangning Cui et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02583) · [PDF](https://arxiv.org/pdf/2611.02583) · [Code](https://github.com/alexz949/BasisKV) |
| 2026-11-02 | **When Cache Pressure Becomes a Trap: Metastability in Agent Serving**<br><sub>Chengzhi Lu, Boxi Zhou, Yanying Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02543) · [PDF](https://arxiv.org/pdf/2611.02543) |
| 2026-11-02 | **SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding**<br><sub>Kunjun Li, Wenhao Chai, Yihao Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02501) · [PDF](https://arxiv.org/pdf/2611.02501) |
| 2026-11-02 | **Semantic Caches for LLM Web Services Leave Their Error Budget Unspent**<br><sub>Hanshuai Cui, Qianli Ma, Zhiqing Tang</sub> | [arXiv](https://arxiv.org/abs/2611.02498) · [PDF](https://arxiv.org/pdf/2611.02498) |
| 2026-11-02 | **Multi-Teacher Reasoning Distillation for LLM Recommendation with Self-Exploration**<br><sub>Liangbo Ning, Siyuan Liang, Yi Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02457) · [PDF](https://arxiv.org/pdf/2611.02457) |

[View all 69 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **232 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-02 | **PlantVLM-Edge: Quantized Vision-Language Models for On-Device Crop Health Diagnosis**<br><sub>Gaurab Wagle, Bishal Adhikari, Jiajia Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03557) · [PDF](https://arxiv.org/pdf/2611.03557) |
| 2026-11-02 | **SHq: Learnable Grids for LLM Weight Quantization**<br><sub>Michael Helcig, Earl Killian, Dan Alistarh</sub> | [arXiv](https://arxiv.org/abs/2611.02966) · [PDF](https://arxiv.org/pdf/2611.02966) |
| 2026-11-02 | **Beyond Accuracy: How Quantization Affects Coding Agents**<br><sub>Areej Mehboob, Muhammad Ali Shafique, Muhammad Usman Qadeer et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02368) · [PDF](https://arxiv.org/pdf/2611.02368) |
| 2026-11-01 | **MedPsy: State-of-the-Art Small Medical Language Models for Efficient Edge Deployment**<br><sub>Davide Vitabile, Alexandro Buffa, Akshay Nambiar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02011) · [PDF](https://arxiv.org/pdf/2611.02011) |
| 2026-11-01 | **MatMoE: Matryoshka Mixture-of-Experts with Dynamic Mixed-Precision Quantization for Efficient Inference**<br><sub>Renjie Wei, Haochen Huang, Chuyu Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01704) · [PDF](https://arxiv.org/pdf/2611.01704) |
| 2026-11-01 | **Sensitivity Inflation from Cross-Record Precision Routing in Private Quantized Fine-Tuning**<br><sub>Annan Zhang, Shengjie Song, Wenshuai Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01411) · [PDF](https://arxiv.org/pdf/2611.01411) |
| 2026-10-31 | **Jet-QSparse: Accelerating Agentic LLM Inference with 4-Bit Sparse Attention**<br><sub>Haozhan Tang, Hao Kang, Meng Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01022) · [PDF](https://arxiv.org/pdf/2611.01022) |
| 2026-10-31 | **Elastic Precision: Software-Hardware Co-Design of a Mixed-Precision Architecture for Long-Context LLM Inference**<br><sub>Boyang Chen, Xiao Wu, Haoran Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00915) · [PDF](https://arxiv.org/pdf/2611.00915) |
| 2026-10-31 | **Running a 20B Video Diffusion Transformer on Consumer Hardware: A Deployment and Measurement Report for MiniMax H3 on Apple Silicon**<br><sub>Luke Shi, Steven Shi</sub> | [arXiv](https://arxiv.org/abs/2611.00843) · [PDF](https://arxiv.org/pdf/2611.00843) |
| 2026-10-31 | **Density-Aware Calibration for Resource-Efficient Medical Vision-Language Models**<br><sub>Tien-Dat Dam, Huu-Thuan Huynh, Minh-Triet Tran et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00684) · [PDF](https://arxiv.org/pdf/2611.00684) |
| 2026-10-31 | **GateTrim: Adaptive-Rank Quantization for Large Language Models**<br><sub>Hongwei Ren, Jincheng Ren, Yuchuan Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00654) · [PDF](https://arxiv.org/pdf/2611.00654) |
| 2026-10-31 | **When Shards Fly: Cross-Tensor In-Flight Conversion for Low-Latency, Low-Memory Weight Updates in Disaggregated RL**<br><sub>Jiayu Xiao, Ye Wang, Zhi Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00646) · [PDF](https://arxiv.org/pdf/2611.00646) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **215 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
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
| 2026-10-29 | **Fewer Heads, Fewer Memories: Pruning Redundant Attention Heads Suppresses Verbatim Memorisation**<br><sub>Aryan Chowdhury, Riza Batista-Navarro</sub> | [arXiv](https://arxiv.org/abs/2610.40974) · [PDF](https://arxiv.org/pdf/2610.40974) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **481 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-02 | **VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing**<br><sub>Yexin Liu, Yunlong Lin, Zehan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03404) · [PDF](https://arxiv.org/pdf/2611.03404) · [Code](https://github.com/LAW1223/VidDub) |
| 2026-11-02 | **SurgPace: Complexity-Aware Progressive Distillation for Surgical Multimodal Large Language Models**<br><sub>Zhicheng He, Xiaohan Xing, Hongqiu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03125) · [PDF](https://arxiv.org/pdf/2611.03125) · [Code](https://github.com/hezhicheng2002/SurgPace) |
| 2026-11-02 | **Efficient Hybrid Distillation: Synergizing Score and Adversarial Objectives for One-Step Diffusion**<br><sub>Fei Peng, Junqiang Wu, Haoxian Tan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03017) · [PDF](https://arxiv.org/pdf/2611.03017) · [Code](https://github.com/pf0607/EASD) |
| 2026-11-02 | **Distilling Literary Sentiment from LLM Annotations into an Ordinal BERT Model**<br><sub>Artem Suslov, Takehiro Hashimoto</sub> | [arXiv](https://arxiv.org/abs/2611.02985) · [PDF](https://arxiv.org/pdf/2611.02985) |
| 2026-11-02 | **SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding**<br><sub>Tianyu Liu, Jun Zhang, Wenjie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02846) · [PDF](https://arxiv.org/pdf/2611.02846) |
| 2026-11-02 | **OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation**<br><sub>Zihao Fan, Xin Lu, Jie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02803) · [PDF](https://arxiv.org/pdf/2611.02803) |
| 2026-11-02 | **History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models**<br><sub>Hangyi Kuang, Chengzhi Wang, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02782) · [PDF](https://arxiv.org/pdf/2611.02782) |
| 2026-11-02 | **Replay for LLM Continual Learning with Multi-Teacher On-Policy Distillation**<br><sub>Yiqiao Qiu</sub> | [arXiv](https://arxiv.org/abs/2611.02746) · [PDF](https://arxiv.org/pdf/2611.02746) |
| 2026-11-02 | **Train the Sampler You Run: Few-Step Masked Diffusion Language Models via Mixture-Likelihood Fine-Tuning**<br><sub>Amin Najafgholizadeh</sub> | [arXiv](https://arxiv.org/abs/2611.02666) · [PDF](https://arxiv.org/pdf/2611.02666) |
| 2026-11-02 | **Multi-Teacher Reasoning Distillation for LLM Recommendation with Self-Exploration**<br><sub>Liangbo Ning, Siyuan Liang, Yi Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02457) · [PDF](https://arxiv.org/pdf/2611.02457) |
| 2026-11-01 | **Bernoulli On-Policy Distillation: Don&#x27;t Ignore High-Confidence Student Tokens**<br><sub>Mingyu Cao, Yaokai Jin, Shiwei Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02093) · [PDF](https://arxiv.org/pdf/2611.02093) · [Code](https://github.com/duterscmy/Bernoulli-OPD) |
| 2026-11-01 | **RIFT: Residual-Informed Flow Transfer for One-Step Generative Video Compression**<br><sub>Qizhe Wang, Jiaye Fu, Feng Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01791) · [PDF](https://arxiv.org/pdf/2611.01791) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **152 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-01 | **EEG-HealthLLM: Hierarchical Adaptation of Large Language Models for Unified Heterogeneous EEG Health Assessment**<br><sub>Ruidong Ma, Jisheng Dang, Ronghao Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01652) · [PDF](https://arxiv.org/pdf/2611.01652) · [Code](https://github.com/Marui-88/EEG-HealthLLM) |
| 2026-10-31 | **GESTALT: Fast, Generalizable Histopathology Image Synthesis from Gene Expression with Pretrained Pathology Foundation Models**<br><sub>Felix Ho, Alexandros Graikos, Dimitris Samaras</sub> | [arXiv](https://arxiv.org/abs/2611.01141) · [PDF](https://arxiv.org/pdf/2611.01141) · [Code](https://github.com/trongnhandev1011/Gestalt) |
| 2026-10-31 | **Scute: Exact Batched Serving for PEFT Adapters Beyond LoRA**<br><sub>Thomas Walker, Richard Baraniuk</sub> | [arXiv](https://arxiv.org/abs/2611.01089) · [PDF](https://arxiv.org/pdf/2611.01089) |
| 2026-10-31 | **Inference First, Training Underneath: Layer-Granular LoRA Co-Serving with LayerLoom**<br><sub>Zongpu Zhang, Yishu Yin, Xuehai Qian</sub> | [arXiv](https://arxiv.org/abs/2611.00652) · [PDF](https://arxiv.org/pdf/2611.00652) |
| 2026-10-31 | **From Weeks to Hours: Fast and Principled SFT Data Generation for Reasoning LLMs**<br><sub>Hongyi Henry Jin, Wenhan Yang, Meysam Ghaffari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00554) · [PDF](https://arxiv.org/pdf/2611.00554) |
| 2026-10-30 | **Compression Technique Interactions in Small Language Models: A Factorial Ablation Study**<br><sub>Bhushit Nema, Siddharth Krishnamurthy, Anjali Kadiyala</sub> | [arXiv](https://arxiv.org/abs/2611.00464) · [PDF](https://arxiv.org/pdf/2611.00464) |
| 2026-10-30 | **RE-SciVQA: Improving Scientific VQA With Context-Relevant Retrieval and Lightweight MLLM Adaptation**<br><sub>Sheikh Tahmim Mehdi, Muminul Islam Jami</sub> | [arXiv](https://arxiv.org/abs/2611.00242) · [PDF](https://arxiv.org/pdf/2611.00242) |
| 2026-10-30 | **CAPER: Circuit-Aware Parameter-Efficient Reasoning in LLMs for Analog Verification**<br><sub>Saion K. Roy</sub> | [arXiv](https://arxiv.org/abs/2611.00187) · [PDF](https://arxiv.org/pdf/2611.00187) |
| 2026-10-30 | **Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity**<br><sub>Jean Lucien Randrianantenaina, Hung Nguyen, Nasib Ullah et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41968) · [PDF](https://arxiv.org/pdf/2610.41968) |
| 2026-10-30 | **Breaking Information Islands in Sparse Tuning via Small-World Connectivity**<br><sub>Xianchao Guan, Zijun Xiong, Yifeng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41665) · [PDF](https://arxiv.org/pdf/2610.41665) · [Code](https://github.com/xianchaoguan/SWIFT) |
| 2026-10-30 | **BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion**<br><sub>Ruurd J. A. Kuiper, Robert A. Bagheri</sub> | [arXiv](https://arxiv.org/abs/2610.41574) · [PDF](https://arxiv.org/pdf/2610.41574) · [Code](https://github.com/RuurdKuiper/BYOD) |
| 2026-10-30 | **KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise**<br><sub>Jonas Loos, Oliver Eberle</sub> | [arXiv](https://arxiv.org/abs/2610.41480) · [PDF](https://arxiv.org/pdf/2610.41480) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **215 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-02 | **CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention**<br><sub>Mohammed Dabbah, Izhak Golan, Oren Tropp et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03200) · [PDF](https://arxiv.org/pdf/2611.03200) |
| 2026-11-02 | **BasisKV: Value Latents for Communication and Key Routing**<br><sub>Lixun Zhang, Zishan Shao, Kangning Cui et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02583) · [PDF](https://arxiv.org/pdf/2611.02583) · [Code](https://github.com/alexz949/BasisKV) |
| 2026-11-01 | **Fairway: Load-Aware KV Cache Reuse for LLM Prefill Scheduling**<br><sub>Hamidreza Alikhani, Nazmul Takbir, Matin Khajavi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02082) · [PDF](https://arxiv.org/pdf/2611.02082) |
| 2026-11-01 | **MedPsy: State-of-the-Art Small Medical Language Models for Efficient Edge Deployment**<br><sub>Davide Vitabile, Alexandro Buffa, Akshay Nambiar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02011) · [PDF](https://arxiv.org/pdf/2611.02011) |
| 2026-11-01 | **ReWY: Faster Gradient Computation for Delta-Rule Attention Family**<br><sub>Yi Zhang, Zhixin Zhao, Weiwei Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01940) · [PDF](https://arxiv.org/pdf/2611.01940) · [Code](https://github.com/flashserve/ReWY) |
| 2026-11-01 | **Who Asks, Who Answers: Linear Attention Builds the Query in Hybrid Language Models**<br><sub>Wenqi Zeng, Chen Feng, YuAng Chen</sub> | [arXiv](https://arxiv.org/abs/2611.01909) · [PDF](https://arxiv.org/pdf/2611.01909) · [Code](https://github.com/yuang-chen/LinearQuery) |
| 2026-10-31 | **Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference**<br><sub>Zhichen Zeng, Xichong Zhang, Junpan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01320) · [PDF](https://arxiv.org/pdf/2611.01320) |
| 2026-10-31 | **Jet-QSparse: Accelerating Agentic LLM Inference with 4-Bit Sparse Attention**<br><sub>Haozhan Tang, Hao Kang, Meng Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01022) · [PDF](https://arxiv.org/pdf/2611.01022) |
| 2026-10-31 | **BitLLM: Efficient Low-Bit, Conversion-Hiding LLM Decoding on Mobile GPUs**<br><sub>Hangyu Zheng, Zhihao Shu, Kunxiong Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00547) · [PDF](https://arxiv.org/pdf/2611.00547) |
| 2026-10-30 | **CLiS: Plug-and-Play Attention Acceleration for Video Diffusion on TPUs via Certified Stabilization**<br><sub>Elisa Tsai, Shao-yu Huang, Daniel Mandragona et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00444) · [PDF](https://arxiv.org/pdf/2611.00444) |
| 2026-10-30 | **TileWeave: Heterogeneous Tiling for Sparse Prefill on Mobile SoCs**<br><sub>Wentao Ni, Hong Cai, Mingu Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00408) · [PDF](https://arxiv.org/pdf/2611.00408) |
| 2026-10-30 | **Rethinking KV Cache Eviction for Agentic LLM Serving**<br><sub>Jiakun Fan, Han Meng, Yuxuan Xia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00391) · [PDF](https://arxiv.org/pdf/2611.00391) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **141 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-02 | **SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding**<br><sub>Tianyu Liu, Jun Zhang, Wenjie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02846) · [PDF](https://arxiv.org/pdf/2611.02846) |
| 2026-11-02 | **SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding**<br><sub>Kunjun Li, Wenhao Chai, Yihao Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02501) · [PDF](https://arxiv.org/pdf/2611.02501) |
| 2026-11-01 | **Seeing What Matters, Verifying What Pays: Load-Adaptive Speculative Decoding for Vision-Language Models**<br><sub>Hong Nie, Zhangchi Gao, Yuqian Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01617) · [PDF](https://arxiv.org/pdf/2611.01617) |
| 2026-10-31 | **Rethinking LLM Pruning via Test-Time Scaling**<br><sub>Mingyang Song, Mao Zheng</sub> | [arXiv](https://arxiv.org/abs/2611.01133) · [PDF](https://arxiv.org/pdf/2611.01133) |
| 2026-10-31 | **TVP: TV is Almost All You Need for Speculative Decoding**<br><sub>Aaryam Sharma</sub> | [arXiv](https://arxiv.org/abs/2611.00588) · [PDF](https://arxiv.org/pdf/2611.00588) |
| 2026-10-30 | **CAPER: Circuit-Aware Parameter-Efficient Reasoning in LLMs for Analog Verification**<br><sub>Saion K. Roy</sub> | [arXiv](https://arxiv.org/abs/2611.00187) · [PDF](https://arxiv.org/pdf/2611.00187) |
| 2026-10-30 | **TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents**<br><sub>Jihao Zhao, Shuaishuai Zu, Pengfei Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41177) · [PDF](https://arxiv.org/pdf/2610.41177) |
| 2026-10-29 | **Agentic World Modeling for Agent Test-time Scaling without Environment Replica**<br><sub>Wendi Li, Huseyin A. Inan, Wei-Ning Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40927) · [PDF](https://arxiv.org/pdf/2610.40927) |
| 2026-10-29 | **Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets**<br><sub>Bole Ma, Ayesha Afzal, Jan Eitzinger et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40287) · [PDF](https://arxiv.org/pdf/2610.40287) |
| 2026-10-28 | **TableTune: Measured, Self-Correcting Draft-Length Tables for Dynamic Speculative Decoding**<br><sub>Abhishek Malvankar, Paul Castro, Nick Mitchell</sub> | [arXiv](https://arxiv.org/abs/2610.38968) · [PDF](https://arxiv.org/pdf/2610.38968) |
| 2026-10-27 | **FAD-KV: Adaptive Dictionary KV Caching for Efficient Reasoning Decoding**<br><sub>Yuxuan Zhu, David H. Yang, Parisa Shiravani et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37921) · [PDF](https://arxiv.org/pdf/2610.37921) |
| 2026-10-25 | **Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2610.34436) · [PDF](https://arxiv.org/pdf/2610.34436) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **235 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-02 | **CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention**<br><sub>Mohammed Dabbah, Izhak Golan, Oren Tropp et al.</sub> | [arXiv](https://arxiv.org/abs/2611.03200) · [PDF](https://arxiv.org/pdf/2611.03200) |
| 2026-11-02 | **Introducing Cluster Efficiency to LLM Serving: Pooling Economical Accelerators over Fast Interconnects**<br><sub>Youhe Jiang, Pavle Glušac, Binhang Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02975) · [PDF](https://arxiv.org/pdf/2611.02975) |
| 2026-11-02 | **Accelerating LLM Pretraining with Zeroth-Order Curvature on Idle Serving Compute**<br><sub>Mingchuan Ma, Dongqi Cai, Daqian Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02688) · [PDF](https://arxiv.org/pdf/2611.02688) |
| 2026-11-02 | **When Cache Pressure Becomes a Trap: Metastability in Agent Serving**<br><sub>Chengzhi Lu, Boxi Zhou, Yanying Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02543) · [PDF](https://arxiv.org/pdf/2611.02543) |
| 2026-11-02 | **Semantic Caches for LLM Web Services Leave Their Error Budget Unspent**<br><sub>Hanshuai Cui, Qianli Ma, Zhiqing Tang</sub> | [arXiv](https://arxiv.org/abs/2611.02498) · [PDF](https://arxiv.org/pdf/2611.02498) |
| 2026-11-01 | **FactorSpec: Serving Exact Relational Constraints as Speculative Drafts**<br><sub>Jianchang Su, Dawei Xiang, Wei Zhang</sub> | [arXiv](https://arxiv.org/abs/2611.02297) · [PDF](https://arxiv.org/pdf/2611.02297) |
| 2026-11-01 | **Fairway: Load-Aware KV Cache Reuse for LLM Prefill Scheduling**<br><sub>Hamidreza Alikhani, Nazmul Takbir, Matin Khajavi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02082) · [PDF](https://arxiv.org/pdf/2611.02082) |
| 2026-10-31 | **TRIAGE: Reliability- and Load-Conditioned Escalation for Two-Tier LLM Serving with a Semantic Evidence Judge**<br><sub>Basavaraj R M, Aryan Bharat Kumar</sub> | [arXiv](https://arxiv.org/abs/2611.01174) · [PDF](https://arxiv.org/pdf/2611.01174) |
| 2026-10-31 | **Capacity Planning for Resource-Constrained Clinical LLM Serving**<br><sub>Yi Tang, Geoffrey Martin, Yiye Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01152) · [PDF](https://arxiv.org/pdf/2611.01152) |
| 2026-10-31 | **Scute: Exact Batched Serving for PEFT Adapters Beyond LoRA**<br><sub>Thomas Walker, Richard Baraniuk</sub> | [arXiv](https://arxiv.org/abs/2611.01089) · [PDF](https://arxiv.org/pdf/2611.01089) |
| 2026-10-31 | **Multi-Turn Semantic Caching for Low-Cost LLM Serving**<br><sub>Baran Atalar, Selly Beyene, Xutong Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01077) · [PDF](https://arxiv.org/pdf/2611.01077) |
| 2026-10-31 | **Inference First, Training Underneath: Layer-Granular LoRA Co-Serving with LayerLoom**<br><sub>Zongpu Zhang, Yishu Yin, Xuehai Qian</sub> | [arXiv](https://arxiv.org/abs/2611.00652) · [PDF](https://arxiv.org/pdf/2611.00652) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **122 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
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
| 2026-10-26 | **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**<br><sub>Caiyi Sun, Yujing Sun, Siu-Ming Yiu</sub> | [arXiv](https://arxiv.org/abs/2610.34782) · [PDF](https://arxiv.org/pdf/2610.34782) · [Code](https://github.com/scy639/ToDoPro) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **199 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-02 | **OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation**<br><sub>Zihao Fan, Xin Lu, Jie Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.02803) · [PDF](https://arxiv.org/pdf/2611.02803) |
| 2026-11-01 | **Z-Cache: Accelerating Diffusion Transformers via Self-Reflection**<br><sub>Zegang Cheng, Zhikai Wang, Jiacheng Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01846) · [PDF](https://arxiv.org/pdf/2611.01846) |
| 2026-11-01 | **RIFT: Residual-Informed Flow Transfer for One-Step Generative Video Compression**<br><sub>Qizhe Wang, Jiaye Fu, Feng Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01791) · [PDF](https://arxiv.org/pdf/2611.01791) |
| 2026-11-01 | **IMPACT: Image-Conditioned Motion with Physics-Aware Collision and Trajectory Guidance for Video Generation**<br><sub>Shiwei Yang, Yunlong Yu, Zhao Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01372) · [PDF](https://arxiv.org/pdf/2611.01372) |
| 2026-10-31 | **DriftingPlanner: Drifting Generative Models for One-Step Trajectory Planning in End-to-End Autonomous Driving**<br><sub>Ziming Liu, Yizhan Qu, Leichen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01283) · [PDF](https://arxiv.org/pdf/2611.01283) |
| 2026-10-31 | **Wave Forcing: Towards Speed-of-Light Streaming Video Generation**<br><sub>Yijie Jin, Yuxuan Liu, Jiajun Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00859) · [PDF](https://arxiv.org/pdf/2611.00859) |
| 2026-10-31 | **Running a 20B Video Diffusion Transformer on Consumer Hardware: A Deployment and Measurement Report for MiniMax H3 on Apple Silicon**<br><sub>Luke Shi, Steven Shi</sub> | [arXiv](https://arxiv.org/abs/2611.00843) · [PDF](https://arxiv.org/pdf/2611.00843) |
| 2026-10-30 | **CLiS: Plug-and-Play Attention Acceleration for Video Diffusion on TPUs via Certified Stabilization**<br><sub>Elisa Tsai, Shao-yu Huang, Daniel Mandragona et al.</sub> | [arXiv](https://arxiv.org/abs/2611.00444) · [PDF](https://arxiv.org/pdf/2611.00444) |
| 2026-10-30 | **A Better Critic Matters for Distribution Matching Distillation**<br><sub>Zongze Wu, Xianbang Wang, Zhengyang Geng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42135) · [PDF](https://arxiv.org/pdf/2610.42135) |
| 2026-10-30 | **Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation**<br><sub>Jiahua Xu, Yijie Fang, Nannan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42031) · [PDF](https://arxiv.org/pdf/2610.42031) |
| 2026-10-30 | **Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning**<br><sub>Zhuguanyu Wu, Congjia Chen, Ruihao Gong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41949) · [PDF](https://arxiv.org/pdf/2610.41949) · [Code](https://github.com/ModelTC/LightX2V/tree/main/lightx2v_rl) |
| 2026-10-29 | **L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory**<br><sub>Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40614) · [PDF](https://arxiv.org/pdf/2610.40614) |

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
