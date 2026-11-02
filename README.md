# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-02 15:43 CST** · **1407 unique papers** · Newest submission: **2026-10-30**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 215 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 208 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 462 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 144 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 203 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 135 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 221 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 117 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 191 |

## Newly indexed · 2026-11-02

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **Flide: Accelerating Decision Inference with Exact State Forking**<br><sub>Bobo Li, Jiajia Song, Hao Fei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42148) · [PDF](https://arxiv.org/pdf/2610.42148) |
| 2026-10-30 | **A Better Critic Matters for Distribution Matching Distillation**<br><sub>Zongze Wu, Xianbang Wang, Zhengyang Geng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42135) · [PDF](https://arxiv.org/pdf/2610.42135) |
| 2026-10-30 | **DecisionRank: On-Policy Distillation for Decision-Model Rerankers**<br><sub>Yanran Wu, Dian Yu, Chongyang Bai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42128) · [PDF](https://arxiv.org/pdf/2610.42128) |
| 2026-10-30 | **ACCT: Asymmetric Cross-LLM Context Transfer**<br><sub>Yuzhe Liu, Haolin Tian, Tonghan Wang</sub> | [arXiv](https://arxiv.org/abs/2610.42116) · [PDF](https://arxiv.org/pdf/2610.42116) |
| 2026-10-30 | **Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation**<br><sub>Jiahua Xu, Yijie Fang, Nannan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42031) · [PDF](https://arxiv.org/pdf/2610.42031) |
| 2026-10-30 | **Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity**<br><sub>Jean Lucien Randrianantenaina, Hung Nguyen, Nasib Ullah et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41968) · [PDF](https://arxiv.org/pdf/2610.41968) |
| 2026-10-30 | **Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning**<br><sub>Zhuguanyu Wu, Congjia Chen, Ruihao Gong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41949) · [PDF](https://arxiv.org/pdf/2610.41949) · [Code](https://github.com/ModelTC/LightX2V/tree/main/lightx2v_rl) |
| 2026-10-30 | **Where KV-Cache Error Lives in Looped Language Models: A Diagnostic Study of Ouro and Huginn**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41825) · [PDF](https://arxiv.org/pdf/2610.41825) |
| 2026-10-30 | **Trainable Vector Quantization for Large Language Models**<br><sub>Anastasiia Prutianova, Alina Bogdanova, Mikhail Shutov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41822) · [PDF](https://arxiv.org/pdf/2610.41822) |
| 2026-10-30 | **Stepwise-Querying: Distilling Reasoning without Access to Teacher Chain-of-Thought**<br><sub>Dicong Yu, Wenhua Wang, Tian Wang</sub> | [arXiv](https://arxiv.org/abs/2610.41769) · [PDF](https://arxiv.org/pdf/2610.41769) |
| 2026-10-30 | **Understanding the Energy Cost of Quantized Agents on Shared GPUs**<br><sub>Stephen Abkin, Alex Flesher, Aldric Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41672) · [PDF](https://arxiv.org/pdf/2610.41672) |
| 2026-10-30 | **Breaking Information Islands in Sparse Tuning via Small-World Connectivity**<br><sub>Xianchao Guan, Zijun Xiong, Yifeng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41665) · [PDF](https://arxiv.org/pdf/2610.41665) · [Code](https://github.com/xianchaoguan/SWIFT) |
| 2026-10-30 | **BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion**<br><sub>Ruurd J. A. Kuiper, Robert A. Bagheri</sub> | [arXiv](https://arxiv.org/abs/2610.41574) · [PDF](https://arxiv.org/pdf/2610.41574) · [Code](https://github.com/RuurdKuiper/BYOD) |
| 2026-10-30 | **HiState: Hierarchical Prefix Cache Management for Hybrid LLM Serving in Agentic Workloads**<br><sub>Zaifeng Pan, Lucas Wang, Xinwei Qiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41508) · [PDF](https://arxiv.org/pdf/2610.41508) |
| 2026-10-30 | **Sparse Text Diffusion under Dual Budgets: Context Connectivity and Expert Activation**<br><sub>Alexandros Christoforos, Chadbourne Davis, Paul Raj</sub> | [arXiv](https://arxiv.org/abs/2610.41487) · [PDF](https://arxiv.org/pdf/2610.41487) |
| 2026-10-30 | **KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise**<br><sub>Jonas Loos, Oliver Eberle</sub> | [arXiv](https://arxiv.org/abs/2610.41480) · [PDF](https://arxiv.org/pdf/2610.41480) |
| 2026-10-30 | **SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models**<br><sub>Haesung Lee, Insu Han</sub> | [arXiv](https://arxiv.org/abs/2610.41408) · [PDF](https://arxiv.org/pdf/2610.41408) |
| 2026-10-30 | **LEAP: Efficient LLM Inference Scheduling with Generalizable Length Prediction**<br><sub>Kwan Yan, Jialun Zhong, Yanzeng Li</sub> | [arXiv](https://arxiv.org/abs/2610.41359) · [PDF](https://arxiv.org/pdf/2610.41359) |
| 2026-10-30 | **In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents**<br><sub>Xuning He, Kai Fan, Runyu Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41291) · [PDF](https://arxiv.org/pdf/2610.41291) · [Code](https://github.com/RISE-X-Lab/Agentic-Soft-Token) |
| 2026-10-30 | **Experts Exhibit Structured Redundancy: Structure-Preserving Expert Pruning for Mixture-of-Experts Large Language Models**<br><sub>Tian Wang, Yongding Tao, Yihong Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41236) · [PDF](https://arxiv.org/pdf/2610.41236) |

[View all 30 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **215 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **Where KV-Cache Error Lives in Looped Language Models: A Diagnostic Study of Ouro and Huginn**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41825) · [PDF](https://arxiv.org/pdf/2610.41825) |
| 2026-10-30 | **Trainable Vector Quantization for Large Language Models**<br><sub>Anastasiia Prutianova, Alina Bogdanova, Mikhail Shutov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41822) · [PDF](https://arxiv.org/pdf/2610.41822) |
| 2026-10-30 | **Understanding the Energy Cost of Quantized Agents on Shared GPUs**<br><sub>Stephen Abkin, Alex Flesher, Aldric Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41672) · [PDF](https://arxiv.org/pdf/2610.41672) |
| 2026-10-30 | **SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models**<br><sub>Haesung Lee, Insu Han</sub> | [arXiv](https://arxiv.org/abs/2610.41408) · [PDF](https://arxiv.org/pdf/2610.41408) |
| 2026-10-30 | **Calibration of Large Model Quantization based on HiFloat4 Format**<br><sub>Jing Huang, Yu Cheng, Ziwei Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41112) · [PDF](https://arxiv.org/pdf/2610.41112) |
| 2026-10-29 | **A Unified Hessian-Guided Framework for Post-Training Quantization**<br><sub>Mads Toftrup, Marco Federici, Boris van Breugel et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40345) · [PDF](https://arxiv.org/pdf/2610.40345) |
| 2026-10-29 | **One Vector or Many? Clustered Optimal-Transport Steering under Quantization**<br><sub>Illia Makarov</sub> | [arXiv](https://arxiv.org/abs/2610.40055) · [PDF](https://arxiv.org/pdf/2610.40055) |
| 2026-10-29 | **KV Cache Quantization for Diffusion Language Models**<br><sub>Yan Tai, Yunan Ding, Guangzhao Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) |
| 2026-10-29 | **LinQuant: Functional Invariances for Low-Precision Linear Recurrences**<br><sub>Neehal Tumma, Philipp Nazari, Rohan Cherukuri et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39418) · [PDF](https://arxiv.org/pdf/2610.39418) · [Code](https://github.com/ntumm120/LinQuant) |
| 2026-10-29 | **Accuracy is not compatibility: two Evo 2 checkpoints hinge on one FP8 matrix multiplication**<br><sub>Xun Ding, Ziyuan Qin</sub> | [arXiv](https://arxiv.org/abs/2610.39415) · [PDF](https://arxiv.org/pdf/2610.39415) · [Code](https://github.com/astding/mmaemu) |
| 2026-10-28 | **The Role of Quantization in Loss Spikes**<br><sub>Zaiqian Chen, Aditya Somasundaram, Sophie Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38277) · [PDF](https://arxiv.org/pdf/2610.38277) |
| 2026-10-28 | **GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices**<br><sub>Yipin Guo, Arun M George, Siddharth Joshi</sub> | [arXiv](https://arxiv.org/abs/2610.38210) · [PDF](https://arxiv.org/pdf/2610.38210) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **208 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity**<br><sub>Jean Lucien Randrianantenaina, Hung Nguyen, Nasib Ullah et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41968) · [PDF](https://arxiv.org/pdf/2610.41968) |
| 2026-10-30 | **Sparse Text Diffusion under Dual Budgets: Context Connectivity and Expert Activation**<br><sub>Alexandros Christoforos, Chadbourne Davis, Paul Raj</sub> | [arXiv](https://arxiv.org/abs/2610.41487) · [PDF](https://arxiv.org/pdf/2610.41487) |
| 2026-10-30 | **In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents**<br><sub>Xuning He, Kai Fan, Runyu Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41291) · [PDF](https://arxiv.org/pdf/2610.41291) · [Code](https://github.com/RISE-X-Lab/Agentic-Soft-Token) |
| 2026-10-30 | **Experts Exhibit Structured Redundancy: Structure-Preserving Expert Pruning for Mixture-of-Experts Large Language Models**<br><sub>Tian Wang, Yongding Tao, Yihong Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41236) · [PDF](https://arxiv.org/pdf/2610.41236) |
| 2026-10-29 | **Fewer Heads, Fewer Memories: Pruning Redundant Attention Heads Suppresses Verbatim Memorisation**<br><sub>Aryan Chowdhury, Riza Batista-Navarro</sub> | [arXiv](https://arxiv.org/abs/2610.40974) · [PDF](https://arxiv.org/pdf/2610.40974) |
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-29 | **Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference**<br><sub>Wenjie Huang, Jun Zhang, Hongyaoxing Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39562) · [PDF](https://arxiv.org/pdf/2610.39562) |
| 2026-10-29 | **Efficient Covariance-Aware Vicinal Latent Diffusion for Continuous Conditional Image Generation**<br><sub>Xin Ding, Shuo Huang, Zhenglong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39277) · [PDF](https://arxiv.org/pdf/2610.39277) |
| 2026-10-28 | **Don&#x27;t Ask the LLM: Visual Token Pruning with Spectral Structure and Semantic Relevance**<br><sub>Intaek Shin, Geuntaek Lim, Sungjune Park et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38303) · [PDF](https://arxiv.org/pdf/2610.38303) · [Code](https://github.com/sejong-rcv/ST-Pruner) |
| 2026-10-27 | **3D-SceneQ: Empowering 3D LLM With Query-Guided Adaptive Pruning and Multi-Modal Feature Enhancement**<br><sub>Yongqi Shan, Lu Zhang, Jiazuo Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37202) · [PDF](https://arxiv.org/pdf/2610.37202) |
| 2026-10-27 | **Mechanistic Failure Modes of Weight Pruning in Transformer Language Models**<br><sub>Nabeelah Faumi, Deshan Sumanathilaka</sub> | [arXiv](https://arxiv.org/abs/2610.37126) · [PDF](https://arxiv.org/pdf/2610.37126) |
| 2026-10-27 | **On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime**<br><sub>Kensuke Sasaki, Issei Sato</sub> | [arXiv](https://arxiv.org/abs/2610.37085) · [PDF](https://arxiv.org/pdf/2610.37085) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **462 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **A Better Critic Matters for Distribution Matching Distillation**<br><sub>Zongze Wu, Xianbang Wang, Zhengyang Geng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42135) · [PDF](https://arxiv.org/pdf/2610.42135) |
| 2026-10-30 | **DecisionRank: On-Policy Distillation for Decision-Model Rerankers**<br><sub>Yanran Wu, Dian Yu, Chongyang Bai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42128) · [PDF](https://arxiv.org/pdf/2610.42128) |
| 2026-10-30 | **Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation**<br><sub>Jiahua Xu, Yijie Fang, Nannan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42031) · [PDF](https://arxiv.org/pdf/2610.42031) |
| 2026-10-30 | **Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning**<br><sub>Zhuguanyu Wu, Congjia Chen, Ruihao Gong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41949) · [PDF](https://arxiv.org/pdf/2610.41949) · [Code](https://github.com/ModelTC/LightX2V/tree/main/lightx2v_rl) |
| 2026-10-30 | **Where KV-Cache Error Lives in Looped Language Models: A Diagnostic Study of Ouro and Huginn**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41825) · [PDF](https://arxiv.org/pdf/2610.41825) |
| 2026-10-30 | **Stepwise-Querying: Distilling Reasoning without Access to Teacher Chain-of-Thought**<br><sub>Dicong Yu, Wenhua Wang, Tian Wang</sub> | [arXiv](https://arxiv.org/abs/2610.41769) · [PDF](https://arxiv.org/pdf/2610.41769) |
| 2026-10-30 | **Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization**<br><sub>Shanglin Yang, Zhan Shi</sub> | [arXiv](https://arxiv.org/abs/2610.41157) · [PDF](https://arxiv.org/pdf/2610.41157) · [Code](https://github.com/shangliy/lineage-is-memory) |
| 2026-10-30 | **MUON-RT Reusing the Teacher&#x27;s Trajectory for Momentum-Free Muon for LLM Self-Distillation**<br><sub>Aryan Das, Vinay Kumar Verma, Aakansha Mishra</sub> | [arXiv](https://arxiv.org/abs/2610.41104) · [PDF](https://arxiv.org/pdf/2610.41104) |
| 2026-10-29 | **WebOverlay: High-Throughput Vision-Only Distillation for Extreme Aspect-Ratio Web Overlay Detection**<br><sub>Jiannan Huang, Jerry Ding, Li Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41037) · [PDF](https://arxiv.org/pdf/2610.41037) |
| 2026-10-29 | **Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation**<br><sub>Yifu Luo, Chuang Ma, Zeyu Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40574) · [PDF](https://arxiv.org/pdf/2610.40574) · [Code](https://github.com/xingzhejun/MTA-OPSD) |
| 2026-10-29 | **LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation**<br><sub>Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40495) · [PDF](https://arxiv.org/pdf/2610.40495) |
| 2026-10-29 | **sDMD: Sinkhorn Distribution Matching Distillation**<br><sub>Jaihoon Kim, Lingxiao Li, Soshi Shimada et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39889) · [PDF](https://arxiv.org/pdf/2610.39889) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **144 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity**<br><sub>Jean Lucien Randrianantenaina, Hung Nguyen, Nasib Ullah et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41968) · [PDF](https://arxiv.org/pdf/2610.41968) |
| 2026-10-30 | **Breaking Information Islands in Sparse Tuning via Small-World Connectivity**<br><sub>Xianchao Guan, Zijun Xiong, Yifeng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41665) · [PDF](https://arxiv.org/pdf/2610.41665) · [Code](https://github.com/xianchaoguan/SWIFT) |
| 2026-10-30 | **BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion**<br><sub>Ruurd J. A. Kuiper, Robert A. Bagheri</sub> | [arXiv](https://arxiv.org/abs/2610.41574) · [PDF](https://arxiv.org/pdf/2610.41574) · [Code](https://github.com/RuurdKuiper/BYOD) |
| 2026-10-30 | **KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise**<br><sub>Jonas Loos, Oliver Eberle</sub> | [arXiv](https://arxiv.org/abs/2610.41480) · [PDF](https://arxiv.org/pdf/2610.41480) |
| 2026-10-28 | **Structure-retained low-rank adapters for weather synthesis**<br><sub>Shunxin Wang, Alexandros Stergiou, Luuk Spreeuwers et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38413) · [PDF](https://arxiv.org/pdf/2610.38413) |
| 2026-10-27 | **Towards Generalizing Pretrained All-Atom Representations to Unified Binder Design**<br><sub>Maojiang Su, Jiale Chen, Qijie Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37994) · [PDF](https://arxiv.org/pdf/2610.37994) |
| 2026-10-27 | **Bi-Phase Training: Learning Efficiently From Scratch**<br><sub>Abel Gurung, Joseph Campbell</sub> | [arXiv](https://arxiv.org/abs/2610.37934) · [PDF](https://arxiv.org/pdf/2610.37934) |
| 2026-10-27 | **EnergyCal: Taming Loss Spikes in Muon-Family Optimizers for Sparse MoE Training**<br><sub>Masato Fujitake</sub> | [arXiv](https://arxiv.org/abs/2610.37062) · [PDF](https://arxiv.org/pdf/2610.37062) |
| 2026-10-27 | **V-LUMEN: Visual Lookup Memory for Embedding Scaling in Vision-Language Models**<br><sub>Miso Choi, Daekeun Kim, Eunji Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37019) · [PDF](https://arxiv.org/pdf/2610.37019) · [Code](https://github.com/miso-choi/V-Lumen) |
| 2026-10-27 | **Provenance Signatures for Low Rank Adaptations of Image Diffusion Models**<br><sub>Tobias Cheung, Mohan Dantam, Marc Juarez et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36933) · [PDF](https://arxiv.org/pdf/2610.36933) |
| 2026-10-27 | **CAMR: Compatibility-Aware Memory Replay for Continual Learning in Large Language Models**<br><sub>Jingpu Yang, Tianhao Li, Fengxian Ji et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36734) · [PDF](https://arxiv.org/pdf/2610.36734) |
| 2026-10-26 | **Synthetic Child-Adult Interactions Are Not Developmentally Plausible**<br><sub>Bastian Bunzeck, Francesca Padovani</sub> | [arXiv](https://arxiv.org/abs/2610.35029) · [PDF](https://arxiv.org/pdf/2610.35029) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **203 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **ACCT: Asymmetric Cross-LLM Context Transfer**<br><sub>Yuzhe Liu, Haolin Tian, Tonghan Wang</sub> | [arXiv](https://arxiv.org/abs/2610.42116) · [PDF](https://arxiv.org/pdf/2610.42116) |
| 2026-10-30 | **Where KV-Cache Error Lives in Looped Language Models: A Diagnostic Study of Ouro and Huginn**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41825) · [PDF](https://arxiv.org/pdf/2610.41825) |
| 2026-10-30 | **KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise**<br><sub>Jonas Loos, Oliver Eberle</sub> | [arXiv](https://arxiv.org/abs/2610.41480) · [PDF](https://arxiv.org/pdf/2610.41480) |
| 2026-10-30 | **In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents**<br><sub>Xuning He, Kai Fan, Runyu Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41291) · [PDF](https://arxiv.org/pdf/2610.41291) · [Code](https://github.com/RISE-X-Lab/Agentic-Soft-Token) |
| 2026-10-30 | **ARK: Avoiding Routing Collisions for KV Cache Transfer in Disaggregated LLM Inference**<br><sub>Hung-Chun Lin, Ting-Wei Hsu, Chung-En Ho et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41160) · [PDF](https://arxiv.org/pdf/2610.41160) |
| 2026-10-29 | **Kernel-based Interpolatory Methods for Context Compression of Attention Mechanisms**<br><sub>Michel Fabrice Serret, Laura Grigori</sub> | [arXiv](https://arxiv.org/abs/2610.40943) · [PDF](https://arxiv.org/pdf/2610.40943) |
| 2026-10-29 | **KV Cache Quantization for Diffusion Language Models**<br><sub>Yan Tai, Yunan Ding, Guangzhao Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) |
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-28 | **GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices**<br><sub>Yipin Guo, Arun M George, Siddharth Joshi</sub> | [arXiv](https://arxiv.org/abs/2610.38210) · [PDF](https://arxiv.org/pdf/2610.38210) |
| 2026-10-27 | **Merge and Branch: Efficient Tree-Structured Supervised Fine-Tuning of LLMs for Recommendation**<br><sub>Yunqin Zhu, Yao Xie</sub> | [arXiv](https://arxiv.org/abs/2610.37973) · [PDF](https://arxiv.org/pdf/2610.37973) |
| 2026-10-27 | **FAD-KV: Adaptive Dictionary KV Caching for Efficient Reasoning Decoding**<br><sub>Yuxuan Zhu, David H. Yang, Parisa Shiravani et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37921) · [PDF](https://arxiv.org/pdf/2610.37921) |
| 2026-10-27 | **Multi-State Linear Attention with Generalized Second-Order Routing**<br><sub>Hee Seung Hwang, Sanghyuk Chun, Xindi Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37645) · [PDF](https://arxiv.org/pdf/2610.37645) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **135 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents**<br><sub>Jihao Zhao, Shuaishuai Zu, Pengfei Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41177) · [PDF](https://arxiv.org/pdf/2610.41177) |
| 2026-10-29 | **Agentic World Modeling for Agent Test-time Scaling without Environment Replica**<br><sub>Wendi Li, Huseyin A. Inan, Wei-Ning Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40927) · [PDF](https://arxiv.org/pdf/2610.40927) |
| 2026-10-29 | **Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets**<br><sub>Bole Ma, Ayesha Afzal, Jan Eitzinger et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40287) · [PDF](https://arxiv.org/pdf/2610.40287) |
| 2026-10-28 | **TableTune: Measured, Self-Correcting Draft-Length Tables for Dynamic Speculative Decoding**<br><sub>Abhishek Malvankar, Paul Castro, Nick Mitchell et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38968) · [PDF](https://arxiv.org/pdf/2610.38968) |
| 2026-10-27 | **FAD-KV: Adaptive Dictionary KV Caching for Efficient Reasoning Decoding**<br><sub>Yuxuan Zhu, David H. Yang, Parisa Shiravani et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37921) · [PDF](https://arxiv.org/pdf/2610.37921) |
| 2026-10-25 | **Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2610.34436) · [PDF](https://arxiv.org/pdf/2610.34436) |
| 2026-10-25 | **T2D: Target-to-Draft Model Pruning &amp; Adaptation for Efficient Speculative Decoding**<br><sub>Shahriar Kabir Nahin, Xiao Ye, Muhao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34103) · [PDF](https://arxiv.org/pdf/2610.34103) |
| 2026-10-25 | **Distributed LLM Inference via Communication-Efficient Speculative Decoding**<br><sub>Joohyun Shin, Byeonghyeon Park, Keumseo Ryum et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35957) · [PDF](https://arxiv.org/pdf/2610.35957) |
| 2026-10-24 | **One Call Ahead: Packed Self-Speculative Decoding with Diffusion Drafting**<br><sub>Yuxiao Chen, Changxiao Cai</sub> | [arXiv](https://arxiv.org/abs/2610.33379) · [PDF](https://arxiv.org/pdf/2610.33379) |
| 2026-10-23 | **NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding**<br><sub>Nilesh Prasad Pandey, Jangseon Park, Jason Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32881) · [PDF](https://arxiv.org/pdf/2610.32881) |
| 2026-10-23 | **MAGIC: Margin-gated Contrastive Debiasing with Evidence Restoration for VLM Test-time Robustness Scaling**<br><sub>Shunshun Gu, Enze Zhang, Ming Pei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32013) · [PDF](https://arxiv.org/pdf/2610.32013) |
| 2026-10-22 | **ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding**<br><sub>Liang He, SiYuan Ma, Qishi Zhan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31338) · [PDF](https://arxiv.org/pdf/2610.31338) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **221 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **Flide: Accelerating Decision Inference with Exact State Forking**<br><sub>Bobo Li, Jiajia Song, Hao Fei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42148) · [PDF](https://arxiv.org/pdf/2610.42148) |
| 2026-10-30 | **HiState: Hierarchical Prefix Cache Management for Hybrid LLM Serving in Agentic Workloads**<br><sub>Zaifeng Pan, Lucas Wang, Xinwei Qiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41508) · [PDF](https://arxiv.org/pdf/2610.41508) |
| 2026-10-30 | **LEAP: Efficient LLM Inference Scheduling with Generalizable Length Prediction**<br><sub>Kwan Yan, Jialun Zhong, Yanzeng Li</sub> | [arXiv](https://arxiv.org/abs/2610.41359) · [PDF](https://arxiv.org/pdf/2610.41359) |
| 2026-10-30 | **ARK: Avoiding Routing Collisions for KV Cache Transfer in Disaggregated LLM Inference**<br><sub>Hung-Chun Lin, Ting-Wei Hsu, Chung-En Ho et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41160) · [PDF](https://arxiv.org/pdf/2610.41160) |
| 2026-10-29 | **Rimuru: Unified Memory Management for Modern LLM Serving via Elastic Expert Offloading**<br><sub>Zhiyuan Fang, Dingyang Li, Jianfeng Zhong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40305) · [PDF](https://arxiv.org/pdf/2610.40305) |
| 2026-10-29 | **DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving**<br><sub>Yishuo Yuan, Shaoyu Yang, Chunrong Fang</sub> | [arXiv](https://arxiv.org/abs/2610.40292) · [PDF](https://arxiv.org/pdf/2610.40292) |
| 2026-10-29 | **Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets**<br><sub>Bole Ma, Ayesha Afzal, Jan Eitzinger et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40287) · [PDF](https://arxiv.org/pdf/2610.40287) |
| 2026-10-29 | **NORmal: Architecting 3D Ferroelectric NOR Flash as Main Memory -- From Co-Fabricated BEOL Arrays to 200B-Class Multi-Agent LLMs in a Smartphone**<br><sub>Zhuoran Li, Chen Gu, Zhuohang Bian et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40000) · [PDF](https://arxiv.org/pdf/2610.40000) |
| 2026-10-29 | **DWISE: Denoising Workload-Informed Scheduling Engine**<br><sub>Lie Li, Wen Li, Junxiao Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39852) · [PDF](https://arxiv.org/pdf/2610.39852) |
| 2026-10-29 | **Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference**<br><sub>Wenjie Huang, Jun Zhang, Hongyaoxing Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39562) · [PDF](https://arxiv.org/pdf/2610.39562) |
| 2026-10-29 | **Learning to Formulate: Agentic Hardware-Software Co-Design of AI Infrastructure through Progressive Optimization and Verification**<br><sub>Yi Ding, Li Shang</sub> | [arXiv](https://arxiv.org/abs/2610.39380) · [PDF](https://arxiv.org/pdf/2610.39380) |
| 2026-10-28 | **FlatCake: A Flat KVCache Storage Architecture for LLM Serving**<br><sub>Xin Huang, Teng Ma, Zhuoran Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38355) · [PDF](https://arxiv.org/pdf/2610.38355) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **117 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-29 | **No Channels Left Behind: Understanding Diffusion Acceleration through Residual Gates**<br><sub>Junha Park, Jaemyung Yu, Jaehui Hwang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40914) · [PDF](https://arxiv.org/pdf/2610.40914) · [Code](https://github.com/naver-ai/radialobj) |
| 2026-10-29 | **UniRA: Unified Representation Alignment and Auto-Encoding for Efficient Diffusion Generation**<br><sub>An Lanji, Dawei Liu, Jin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39948) · [PDF](https://arxiv.org/pdf/2610.39948) |
| 2026-10-29 | **KV Cache Quantization for Diffusion Language Models**<br><sub>Yan Tai, Yunan Ding, Guangzhao Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) |
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-28 | **NAGO: Noise-Aware Generative Operator via Flow Matching**<br><sub>Guanyu Chen, Shengze Xu, Pengwei Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38273) · [PDF](https://arxiv.org/pdf/2610.38273) · [Code](https://github.com/cgymmy/NAGO) |
| 2026-10-27 | **Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs**<br><sub>Donghyeon Cho, Joowon Kim, Seungho Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36671) · [PDF](https://arxiv.org/pdf/2610.36671) |
| 2026-10-26 | **ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing**<br><sub>Caiyi Sun, Yujing Sun, Siu-Ming Yiu</sub> | [arXiv](https://arxiv.org/abs/2610.34782) · [PDF](https://arxiv.org/pdf/2610.34782) · [Code](https://github.com/scy639/ToDoPro) |
| 2026-10-25 | **Freeze What Is Settled, Cache What Is Smooth: Spatial Freezing Keeps Step Caching in Its Low-Error Regime**<br><sub>Baiyan Li, Ganxuan Yang</sub> | [arXiv](https://arxiv.org/abs/2610.34177) · [PDF](https://arxiv.org/pdf/2610.34177) |
| 2026-10-24 | **H-GLow: Accelerating Graph Generation via Hazard-Guided Discrete Flow Matching**<br><sub>Sirine Ayadi, Stephan Günnemann</sub> | [arXiv](https://arxiv.org/abs/2610.33599) · [PDF](https://arxiv.org/pdf/2610.33599) |
| 2026-10-24 | **UltraFlash: Accelerating Megapixel Visual Synthesis**<br><sub>Phuc Lai, Anh Nguyen, Phong Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33581) · [PDF](https://arxiv.org/pdf/2610.33581) |
| 2026-10-23 | **SCDM-HTD: Spectral-Wise Conditional Diffusion Model for Hyperspectral Target Detection**<br><sub>Dunbin Shen, Wenfeng Kong, Jianjun Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.32768) · [PDF](https://arxiv.org/pdf/2610.32768) |
| 2026-10-22 | **CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation**<br><sub>Lifan Jiang, Yibo Zhao, Senlin cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30854) · [PDF](https://arxiv.org/pdf/2610.30854) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **191 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-30 | **A Better Critic Matters for Distribution Matching Distillation**<br><sub>Zongze Wu, Xianbang Wang, Zhengyang Geng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42135) · [PDF](https://arxiv.org/pdf/2610.42135) |
| 2026-10-30 | **Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation**<br><sub>Jiahua Xu, Yijie Fang, Nannan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.42031) · [PDF](https://arxiv.org/pdf/2610.42031) |
| 2026-10-30 | **Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning**<br><sub>Zhuguanyu Wu, Congjia Chen, Ruihao Gong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.41949) · [PDF](https://arxiv.org/pdf/2610.41949) · [Code](https://github.com/ModelTC/LightX2V/tree/main/lightx2v_rl) |
| 2026-10-29 | **L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory**<br><sub>Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40614) · [PDF](https://arxiv.org/pdf/2610.40614) |
| 2026-10-29 | **LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation**<br><sub>Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40495) · [PDF](https://arxiv.org/pdf/2610.40495) |
| 2026-10-29 | **Wizard: Manipulate Any World in Real Time via Agentic Control**<br><sub>Yuzhe Wu, Zijun Lin, Yeying Jin</sub> | [arXiv](https://arxiv.org/abs/2610.40339) · [PDF](https://arxiv.org/pdf/2610.40339) |
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-29 | **FlexTry-On: A Time-Efficient Framework for Multi-Scenario Virtual Try-on**<br><sub>Phuong Dam, Quyen Nguyen Duc, Son Hoang Minh et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39646) · [PDF](https://arxiv.org/pdf/2610.39646) |
| 2026-10-29 | **ROAD: Modern Adversarial Training for Simple One-Step Distillation at Scale**<br><sub>Xiaoou Li, Shan You, Tao Huang</sub> | [arXiv](https://arxiv.org/abs/2610.39539) · [PDF](https://arxiv.org/pdf/2610.39539) |
| 2026-10-29 | **Efficient Covariance-Aware Vicinal Latent Diffusion for Continuous Conditional Image Generation**<br><sub>Xin Ding, Shuo Huang, Zhenglong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39277) · [PDF](https://arxiv.org/pdf/2610.39277) |
| 2026-10-29 | **CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation**<br><sub>Huangchao Song, Lingyun Yu, Cong Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39160) · [PDF](https://arxiv.org/pdf/2610.39160) |
| 2026-10-27 | **ReferStream: Interactive Subject Injection for Streaming Video Generation**<br><sub>Shuolin Xu, Guanyuan Li, Boyu Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37566) · [PDF](https://arxiv.org/pdf/2610.37566) |

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
