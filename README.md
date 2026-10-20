# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-20 14:04 CST** · **1159 unique papers** · Newest submission: **2026-10-19**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 175 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 167 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 390 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 118 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 168 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 117 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 178 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 99 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 158 |

## Newly indexed · 2026-10-20

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **LatComm: Reusable Context Compression for Latent Communication between Large Language Models**<br><sub>Huawei Lin, Jinting Liu, Tan Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26840) · [PDF](https://arxiv.org/pdf/2610.26840) |
| 2026-10-19 | **SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration**<br><sub>Javad Rajabi, Hakki Can Karaimer, David B. Lindell et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26837) · [PDF](https://arxiv.org/pdf/2610.26837) |
| 2026-10-19 | **TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning**<br><sub>Liana Patel, Rishabh Ranjan, Ion Stoica et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26754) · [PDF](https://arxiv.org/pdf/2610.26754) · [Code](https://github.com/tokengate-models/TokenGate) |
| 2026-10-19 | **ReAnchor: Reusing Rejected Verifier States for Diffusion Drafting**<br><sub>Sanghyun Lee, Wonjin Nam, Seungho Jang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26531) · [PDF](https://arxiv.org/pdf/2610.26531) |
| 2026-10-19 | **SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models**<br><sub>Shenli Zheng, Zhou Fang, Yuan Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26487) · [PDF](https://arxiv.org/pdf/2610.26487) |
| 2026-10-19 | **An Empirical Study of Parameter-Efficient Fine-Tuning for Mixture-of-Experts LLMs**<br><sub>Minglei Li, Peng Ye, Haonan He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26370) · [PDF](https://arxiv.org/pdf/2610.26370) |
| 2026-10-19 | **Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion**<br><sub>Yuanyu He, Zhuokun Chen, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26262) · [PDF](https://arxiv.org/pdf/2610.26262) |
| 2026-10-19 | **RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion**<br><sub>Tiange Xu, Kai Liu, Linghe Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26244) · [PDF](https://arxiv.org/pdf/2610.26244) · [Code](https://github.com/lyraxtg/RECAP) |
| 2026-10-19 | **TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation**<br><sub>Jia Li, Xurui Peng, Haowei Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26165) · [PDF](https://arxiv.org/pdf/2610.26165) |
| 2026-10-19 | **A Hybrid GPU and Processing-Near-Memory Architecture with Shared DRAM for Efficient Prefill-Decode Disaggregation**<br><sub>Sanghyeok Han, Inseong Choi, Byungkuk Yoon et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26131) · [PDF](https://arxiv.org/pdf/2610.26131) |
| 2026-10-19 | **Provable Adversarial Detection: Prime Quantization meets Gromov--Wasserstein**<br><sub>Manohar Kaul, Sadbhavana Babar, Aditya Ramesh et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26102) · [PDF](https://arxiv.org/pdf/2610.26102) |
| 2026-10-19 | **MX-Like Tensor Core for LLM Inference with NPU Integration via Hardware-Software Co-Design Exploration**<br><sub>Zijun Zhao, Ruichu Ao, Stef Cuyckens et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26083) · [PDF](https://arxiv.org/pdf/2610.26083) |
| 2026-10-19 | **TamedFlow: Trajectory-Aware Distillation\\for Teacher-Assisted Diffusion Sampling**<br><sub>Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26025) · [PDF](https://arxiv.org/pdf/2610.26025) |
| 2026-10-19 | **Correctness-Dependent Asymmetric Target Distributions for Self-Distillation Policy Optimization**<br><sub>Suwan Yoon, Seongryong Jung, Changhee Lee</sub> | [arXiv](https://arxiv.org/abs/2610.25973) · [PDF](https://arxiv.org/pdf/2610.25973) |
| 2026-10-19 | **LEAP: Accelerating ODE-based Diffusion Sampling with Optimal Linear Leaps**<br><sub>Haowei Zheng, Zhenyu Zhou, Jiawei Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25918) · [PDF](https://arxiv.org/pdf/2610.25918) · [Code](https://github.com/zju-pi/LEAP) |
| 2026-10-19 | **CALM: Consistency-Aware Logit Masking in Decoding Space for Mitigating Overthinking of Large Reasoning Models**<br><sub>Shengjing Liu, Feiyang Li, Yuxuan Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25908) · [PDF](https://arxiv.org/pdf/2610.25908) |
| 2026-10-19 | **Asynchronous On-Policy Self-Distillation**<br><sub>Xidong Wu, Qi Qi, Yuqiong Ji et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25880) · [PDF](https://arxiv.org/pdf/2610.25880) |
| 2026-10-19 | **DeltaTrace: Efficient Signed Attribution for Reasoning Language Models**<br><sub>Chen Liang, Daoping Wu, Donghua Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25877) · [PDF](https://arxiv.org/pdf/2610.25877) |
| 2026-10-19 | **Hihaze: One-Step Diffusion for High-Resolution Real-World Image Dehazing**<br><sub>Zheng Chen, Yuchen Huang, Xiaoyang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25832) · [PDF](https://arxiv.org/pdf/2610.25832) · [Code](https://github.com/zhengchen1999/Hihaze) |
| 2026-10-19 | **Communication-Efficient Federated Domain Generalization in Edge Networks via Dynamic Prototype Regulation**<br><sub>Yuankun Xia, Hui Wang, Ling Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25810) · [PDF](https://arxiv.org/pdf/2610.25810) |

[View all 56 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **175 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **Provable Adversarial Detection: Prime Quantization meets Gromov--Wasserstein**<br><sub>Manohar Kaul, Sadbhavana Babar, Aditya Ramesh et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26102) · [PDF](https://arxiv.org/pdf/2610.26102) |
| 2026-10-19 | **MX-Like Tensor Core for LLM Inference with NPU Integration via Hardware-Software Co-Design Exploration**<br><sub>Zijun Zhao, Ruichu Ao, Stef Cuyckens et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26083) · [PDF](https://arxiv.org/pdf/2610.26083) |
| 2026-10-19 | **LIRQuant: An Efficient Locally Isolated Rotation Quantization Method for Large Language Models**<br><sub>Desheng Xu, Hanglin Li, Tianchen Song et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25675) · [PDF](https://arxiv.org/pdf/2610.25675) |
| 2026-10-18 | **Certified Sparse Attention via Perturbed Retrieval**<br><sub>Runguo Li</sub> | [arXiv](https://arxiv.org/abs/2610.24991) · [PDF](https://arxiv.org/pdf/2610.24991) |
| 2026-10-17 | **What Matters for NVFP4 Training? A Comparative Study of Low-Precision Pretraining Recipes**<br><sub>Anjulie Agrusa, Andrei Panferov, Elizabeth Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24343) · [PDF](https://arxiv.org/pdf/2610.24343) |
| 2026-10-16 | **BS-Spec: BFP-Based Bit-Sharing for Self-Speculative LLM Decoding with LUT-Driven Mixed-Precision Acceleration**<br><sub>Jiwoo Kim, Gunho Park, Sunwoo Yoo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22877) · [PDF](https://arxiv.org/pdf/2610.22877) |
| 2026-10-15 | **Noise-shaped Sampling and Annealing for Scalable On-the-edge Training of Binary and Ternary AI Models**<br><sub>Zihao Chen, Zhili Xiao, Rui-Jie Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22621) · [PDF](https://arxiv.org/pdf/2610.22621) |
| 2026-10-15 | **BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks**<br><sub>Max Zhu, Bohang Sun, Pietro Lio et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22256) · [PDF](https://arxiv.org/pdf/2610.22256) |
| 2026-10-15 | **When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill**<br><sub>Muhammad Ibrahim</sub> | [arXiv](https://arxiv.org/abs/2610.21500) · [PDF](https://arxiv.org/pdf/2610.21500) |
| 2026-10-15 | **HyCo: Hybrid Drafting for Cost-Efficient Mobile-Cloud Speculative Decoding**<br><sub>Hanbin Bae, Heejin Choi, Joohyung Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21436) · [PDF](https://arxiv.org/pdf/2610.21436) |
| 2026-10-15 | **Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference**<br><sub>Sunghyun Wee, Geunjae Choi, Hyeonjin Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21257) · [PDF](https://arxiv.org/pdf/2610.21257) |
| 2026-10-14 | **Task-Phase-Conditioned Expert Routing Is Not a Reliable Proxy for Quantization Sensitivity in MoE FFN Tensors**<br><sub>Yifan Liu</sub> | [arXiv](https://arxiv.org/abs/2610.20826) · [PDF](https://arxiv.org/pdf/2610.20826) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **167 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning**<br><sub>Liana Patel, Rishabh Ranjan, Ion Stoica et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26754) · [PDF](https://arxiv.org/pdf/2610.26754) · [Code](https://github.com/tokengate-models/TokenGate) |
| 2026-10-19 | **SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models**<br><sub>Shenli Zheng, Zhou Fang, Yuan Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26487) · [PDF](https://arxiv.org/pdf/2610.26487) |
| 2026-10-19 | **How Much Does One Wrong Answer Cost? Error Propagation in Constraint Pruning with Noisy LLM Oracles**<br><sub>Zhengtao Gui, Weining Shen</sub> | [arXiv](https://arxiv.org/abs/2610.25739) · [PDF](https://arxiv.org/pdf/2610.25739) |
| 2026-10-19 | **LOOP: Recovery-Aligned Iterative Layer Pruning via On-Policy Distillation**<br><sub>Liang Xu, Shufan Shen, Zhongni Hou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25679) · [PDF](https://arxiv.org/pdf/2610.25679) |
| 2026-10-18 | **ReTrace: Visual Backtracking for Efficient Multimodal Large Language Models**<br><sub>Guangzong Si, Dong Wang, Yifan Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25005) · [PDF](https://arxiv.org/pdf/2610.25005) |
| 2026-10-17 | **FlowMaker: From Tasks to Cost-Efficient Generative AI Workflow Deployments**<br><sub>Dimitrios Liakopoulos, Prasoon Sinha, Neeraja J. Yadwadkar</sub> | [arXiv](https://arxiv.org/abs/2610.24861) · [PDF](https://arxiv.org/pdf/2610.24861) |
| 2026-10-16 | **Hierarchical and Query-Aware Visual Token Pruning for High-Resolution LVLMs**<br><sub>Luther Wei, Ling Zou, Kang-Yang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24102) · [PDF](https://arxiv.org/pdf/2610.24102) |
| 2026-10-16 | **CatchUp: Depth-Aware Re-Admission of Visual Tokens for Efficient Large Vision-Language Models**<br><sub>Eunju Park, Uiwon Hwang</sub> | [arXiv](https://arxiv.org/abs/2610.23324) · [PDF](https://arxiv.org/pdf/2610.23324) · [Code](https://github.com/pej0918/CatchUp) |
| 2026-10-16 | **Prism Attention: Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference**<br><sub>Zhenxu Tian, Kebin Liu, Zhengwu Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22985) · [PDF](https://arxiv.org/pdf/2610.22985) |
| 2026-10-16 | **Uncertainty-Aware Budget Allocation for Efficient LLM Tree Search**<br><sub>Jianguo Huang, Zhiyi Lyu, Fuxiang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22858) · [PDF](https://arxiv.org/pdf/2610.22858) |
| 2026-10-16 | **Prune the Leaky Neurons: Mitigating Private Data Leakage in Fine-Tuned LLMs via Joint-Embedding-Guided Pruning**<br><sub>Mohamed Shaaban, Mohamed Elmahallawy</sub> | [arXiv](https://arxiv.org/abs/2610.22792) · [PDF](https://arxiv.org/pdf/2610.22792) |
| 2026-10-15 | **MedSTP: Preserving Subspace and Transition Evidence for Medical VQA Token Pruning**<br><sub>Mengchen Fan, Qizhen Lan, Xi Xiao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22751) · [PDF](https://arxiv.org/pdf/2610.22751) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **390 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion**<br><sub>Yuanyu He, Zhuokun Chen, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26262) · [PDF](https://arxiv.org/pdf/2610.26262) |
| 2026-10-19 | **TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation**<br><sub>Jia Li, Xurui Peng, Haowei Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26165) · [PDF](https://arxiv.org/pdf/2610.26165) |
| 2026-10-19 | **TamedFlow: Trajectory-Aware Distillation\\for Teacher-Assisted Diffusion Sampling**<br><sub>Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26025) · [PDF](https://arxiv.org/pdf/2610.26025) |
| 2026-10-19 | **Correctness-Dependent Asymmetric Target Distributions for Self-Distillation Policy Optimization**<br><sub>Suwan Yoon, Seongryong Jung, Changhee Lee</sub> | [arXiv](https://arxiv.org/abs/2610.25973) · [PDF](https://arxiv.org/pdf/2610.25973) |
| 2026-10-19 | **Asynchronous On-Policy Self-Distillation**<br><sub>Xidong Wu, Qi Qi, Yuqiong Ji et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25880) · [PDF](https://arxiv.org/pdf/2610.25880) |
| 2026-10-19 | **Hihaze: One-Step Diffusion for High-Resolution Real-World Image Dehazing**<br><sub>Zheng Chen, Yuchen Huang, Xiaoyang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25832) · [PDF](https://arxiv.org/pdf/2610.25832) · [Code](https://github.com/zhengchen1999/Hihaze) |
| 2026-10-19 | **Functional Cross-layer Experts Routing for One-step Diffusion Distillation**<br><sub>Zile Huang, Ser-nam Lim</sub> | [arXiv](https://arxiv.org/abs/2610.25742) · [PDF](https://arxiv.org/pdf/2610.25742) · [Code](https://github.com/toffeecat/demoe-ttt-router) |
| 2026-10-19 | **LOOP: Recovery-Aligned Iterative Layer Pruning via On-Policy Distillation**<br><sub>Liang Xu, Shufan Shen, Zhongni Hou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25679) · [PDF](https://arxiv.org/pdf/2610.25679) |
| 2026-10-19 | **OPDArena: Understanding Learning and Forgetting in On-Policy Distillation**<br><sub>Yuanze Xu, Tianzhu Ye, Hui Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25651) · [PDF](https://arxiv.org/pdf/2610.25651) · [Code](https://github.com/StellarCurtain/OPDArena) |
| 2026-10-19 | **Think, Compress, Answer: Reinforcement Learning for Multimodal Grounding via Reasoning Compression**<br><sub>Jinbae Seo, Hyeongjun Kwon, Jiyoung Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25640) · [PDF](https://arxiv.org/pdf/2610.25640) |
| 2026-10-18 | **A failure of Imagination: VLMs fail to use visual representations for text, but self-distillation can help**<br><sub>Shashwat Singh, He He, Tal Linzen</sub> | [arXiv](https://arxiv.org/abs/2610.25470) · [PDF](https://arxiv.org/pdf/2610.25470) |
| 2026-10-17 | **ReTRACE: Feedback-Guided LLM Agent in a Chemistry Harness for Retrosynthesis Planning**<br><sub>Jinxiang Xie, Yijian Zhang, Qingyuan Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24744) · [PDF](https://arxiv.org/pdf/2610.24744) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **118 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning**<br><sub>Liana Patel, Rishabh Ranjan, Ion Stoica et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26754) · [PDF](https://arxiv.org/pdf/2610.26754) · [Code](https://github.com/tokengate-models/TokenGate) |
| 2026-10-19 | **An Empirical Study of Parameter-Efficient Fine-Tuning for Mixture-of-Experts LLMs**<br><sub>Minglei Li, Peng Ye, Haonan He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26370) · [PDF](https://arxiv.org/pdf/2610.26370) |
| 2026-10-19 | **Communication-Efficient Federated Domain Generalization in Edge Networks via Dynamic Prototype Regulation**<br><sub>Yuankun Xia, Hui Wang, Ling Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25810) · [PDF](https://arxiv.org/pdf/2610.25810) |
| 2026-10-18 | **System X: An LLM Decision Model That Replies from Its Own KV Cache**<br><sub>Syed Usama Khalid Bukhari, Syed Safwan Khalid, Muhammad Aamir</sub> | [arXiv](https://arxiv.org/abs/2610.25456) · [PDF](https://arxiv.org/pdf/2610.25456) |
| 2026-10-18 | **BatchParScale: Sparse Batch-Mixing for Sequence Models**<br><sub>Hans Peter Lyngsøe Raaschou-jensen, M. Onurcan Kaya, Desmond Elliott</sub> | [arXiv](https://arxiv.org/abs/2610.25254) · [PDF](https://arxiv.org/pdf/2610.25254) |
| 2026-10-18 | **PACT: NVFP4 Data-Flow LoRA Fine-Tuning on Consumer GPUs**<br><sub>Lei Gao, Hossein Entezari Zarch, Chaoyi Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25048) · [PDF](https://arxiv.org/pdf/2610.25048) |
| 2026-10-17 | **Efficiency Measured in English: Tokeniser Coverage Bounds Small Language Models on Indic Scripts**<br><sub>Anna Pramod</sub> | [arXiv](https://arxiv.org/abs/2610.24818) · [PDF](https://arxiv.org/pdf/2610.24818) |
| 2026-10-17 | **First-Order LoRA Training with Phone NPUs**<br><sub>Xu Zheng, Wei Cheng, Zhuomin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24816) · [PDF](https://arxiv.org/pdf/2610.24816) |
| 2026-10-17 | **AdamPM: Memory-Efficient LLM Optimization via Moment Pooling**<br><sub>Xiaowei Ji, Lishan Xu, Jianing An et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24598) · [PDF](https://arxiv.org/pdf/2610.24598) · [Code](https://github.com/jixiaowei95/AdamPM) |
| 2026-10-16 | **Cache2LoRA: Understanding and Improving Context Internalization**<br><sub>Yi Fang, Gaurav Srivastava, Zhenyu Bi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24107) · [PDF](https://arxiv.org/pdf/2610.24107) |
| 2026-10-16 | **Kingfisher: Fast Personalized Visual Autoregressive Generation via Scale-Aware Prompt-Conditioned Scale Decomposition**<br><sub>Dinh-Khoi Vo, Akihiro Sugimoto, Minh-Triet Tran et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23238) · [PDF](https://arxiv.org/pdf/2610.23238) |
| 2026-10-16 | **Local proxies for memory-efficient training**<br><sub>Wu S. Zihan, Brian A. Yuan, Guillaume Bellec</sub> | [arXiv](https://arxiv.org/abs/2610.23145) · [PDF](https://arxiv.org/pdf/2610.23145) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **168 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **LatComm: Reusable Context Compression for Latent Communication between Large Language Models**<br><sub>Huawei Lin, Jinting Liu, Tan Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26840) · [PDF](https://arxiv.org/pdf/2610.26840) |
| 2026-10-19 | **Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion**<br><sub>Yuanyu He, Zhuokun Chen, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26262) · [PDF](https://arxiv.org/pdf/2610.26262) |
| 2026-10-19 | **RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion**<br><sub>Tiange Xu, Kai Liu, Linghe Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26244) · [PDF](https://arxiv.org/pdf/2610.26244) · [Code](https://github.com/lyraxtg/RECAP) |
| 2026-10-19 | **TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation**<br><sub>Jia Li, Xurui Peng, Haowei Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26165) · [PDF](https://arxiv.org/pdf/2610.26165) |
| 2026-10-19 | **DeltaTrace: Efficient Signed Attribution for Reasoning Language Models**<br><sub>Chen Liang, Daoping Wu, Donghua Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25877) · [PDF](https://arxiv.org/pdf/2610.25877) |
| 2026-10-19 | **Think, Compress, Answer: Reinforcement Learning for Multimodal Grounding via Reasoning Compression**<br><sub>Jinbae Seo, Hyeongjun Kwon, Jiyoung Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25640) · [PDF](https://arxiv.org/pdf/2610.25640) |
| 2026-10-18 | **System X: An LLM Decision Model That Replies from Its Own KV Cache**<br><sub>Syed Usama Khalid Bukhari, Syed Safwan Khalid, Muhammad Aamir</sub> | [arXiv](https://arxiv.org/abs/2610.25456) · [PDF](https://arxiv.org/pdf/2610.25456) |
| 2026-10-18 | **MOSAIC: Multi-Objective Search for Allocating Inference Cache Across LLM Decoder Layers**<br><sub>Sravanth Kodavanti, Manjunath Arveti</sub> | [arXiv](https://arxiv.org/abs/2610.25431) · [PDF](https://arxiv.org/pdf/2610.25431) |
| 2026-10-18 | **ReTrace: Visual Backtracking for Efficient Multimodal Large Language Models**<br><sub>Guangzong Si, Dong Wang, Yifan Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25005) · [PDF](https://arxiv.org/pdf/2610.25005) |
| 2026-10-18 | **Certified Sparse Attention via Perturbed Retrieval**<br><sub>Runguo Li</sub> | [arXiv](https://arxiv.org/abs/2610.24991) · [PDF](https://arxiv.org/pdf/2610.24991) |
| 2026-10-17 | **TideKV: Delayed KV Eviction via Layer-Wise Chunked Prefill for Memory-Efficient Long-Context LLM Inference**<br><sub>Yu Wang, Zhu Wang, Ning Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24499) · [PDF](https://arxiv.org/pdf/2610.24499) |
| 2026-10-16 | **KVCompass: A Discovery Plane for Internet-Scale Prefix Cache Sharing in LLM Serving**<br><sub>Shiyi Ling, Fei Fang, Chen Qian</sub> | [arXiv](https://arxiv.org/abs/2610.24179) · [PDF](https://arxiv.org/pdf/2610.24179) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **117 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **CALM: Consistency-Aware Logit Masking in Decoding Space for Mitigating Overthinking of Large Reasoning Models**<br><sub>Shengjing Liu, Feiyang Li, Yuxuan Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25908) · [PDF](https://arxiv.org/pdf/2610.25908) |
| 2026-10-19 | **Think, Compress, Answer: Reinforcement Learning for Multimodal Grounding via Reasoning Compression**<br><sub>Jinbae Seo, Hyeongjun Kwon, Jiyoung Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25640) · [PDF](https://arxiv.org/pdf/2610.25640) |
| 2026-10-18 | **ATEST: Adaptive Resource-Aware Test-Time Scaling for LLM Inference**<br><sub>Mobina Kashaniyan, Ali Jannesari</sub> | [arXiv](https://arxiv.org/abs/2610.25519) · [PDF](https://arxiv.org/pdf/2610.25519) |
| 2026-10-18 | **Test-Time Scaling of Text-to-Image Flow Matching Models with Noise-Rejuvenated Sequential Monte Carlo**<br><sub>Wenyi Lian, Zheng Zhao, Thomas B. Sch{ö}n</sub> | [arXiv](https://arxiv.org/abs/2610.25479) · [PDF](https://arxiv.org/pdf/2610.25479) · [Code](https://github.com/shermanlian/NR-SMC) |
| 2026-10-18 | **GeoART: Geometry-Aware Refinement via Test-Time Scaling for Camera-Conditioned Video Diffusion**<br><sub>Liudi Yang, Ziyuan Liu</sub> | [arXiv](https://arxiv.org/abs/2610.25273) · [PDF](https://arxiv.org/pdf/2610.25273) |
| 2026-10-18 | **BatchParScale: Sparse Batch-Mixing for Sequence Models**<br><sub>Hans Peter Lyngsøe Raaschou-jensen, M. Onurcan Kaya, Desmond Elliott</sub> | [arXiv](https://arxiv.org/abs/2610.25254) · [PDF](https://arxiv.org/pdf/2610.25254) |
| 2026-10-18 | **Conjugate Compilation: Self-Improving Agentic Co-Compilation for Speculative Decoding**<br><sub>Annabelle Sujun Tang, Rohan Mahapatra, Christopher Priebe et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25012) · [PDF](https://arxiv.org/pdf/2610.25012) |
| 2026-10-17 | **FlashMap: Flow Map Speculative Decoding**<br><sub>Jeff Shen, Zhejian Zhou, Ryan Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24365) · [PDF](https://arxiv.org/pdf/2610.24365) · [Code](https://github.com/al-jshen/flashmap) |
| 2026-10-16 | **DLite: History-free Speculative Decoding for Agentic AI**<br><sub>Jiaming Xu, Hanzhen Wang, Tianlang Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23787) · [PDF](https://arxiv.org/pdf/2610.23787) |
| 2026-10-16 | **Sample, Mix, or Verify? Allocating Test-Time Compute under Imperfect Verifiers**<br><sub>Srinivasan Iyengar</sub> | [arXiv](https://arxiv.org/abs/2610.23255) · [PDF](https://arxiv.org/pdf/2610.23255) |
| 2026-10-16 | **ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling**<br><sub>Yuki Otsuka, Daisuke Oba, Naoaki Okazaki</sub> | [arXiv](https://arxiv.org/abs/2610.23225) · [PDF](https://arxiv.org/pdf/2610.23225) · [Code](https://github.com/Yuki-Ots/ReLaDrift) |
| 2026-10-16 | **Not All Test-Time Compute Is Evidence: Model-Specific Bias in LLM Reasoning**<br><sub>Ming Shen, Tianjun Yao</sub> | [arXiv](https://arxiv.org/abs/2610.23213) · [PDF](https://arxiv.org/pdf/2610.23213) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **178 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **A Hybrid GPU and Processing-Near-Memory Architecture with Shared DRAM for Efficient Prefill-Decode Disaggregation**<br><sub>Sanghyeok Han, Inseong Choi, Byungkuk Yoon et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26131) · [PDF](https://arxiv.org/pdf/2610.26131) |
| 2026-10-18 | **From Label Priors to Task Evidence: Efficient Long-Video Frame Selection via Bayesian GRPO**<br><sub>Shuochen Chang, Bingjie Gao, Qingyang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25418) · [PDF](https://arxiv.org/pdf/2610.25418) |
| 2026-10-17 | **FlowMaker: From Tasks to Cost-Efficient Generative AI Workflow Deployments**<br><sub>Dimitrios Liakopoulos, Prasoon Sinha, Neeraja J. Yadwadkar</sub> | [arXiv](https://arxiv.org/abs/2610.24861) · [PDF](https://arxiv.org/pdf/2610.24861) |
| 2026-10-16 | **KVCompass: A Discovery Plane for Internet-Scale Prefix Cache Sharing in LLM Serving**<br><sub>Shiyi Ling, Fei Fang, Chen Qian</sub> | [arXiv](https://arxiv.org/abs/2610.24179) · [PDF](https://arxiv.org/pdf/2610.24179) |
| 2026-10-16 | **HBFSim: A Simulator for Exploring HBF in Memory Hierarchies for LLMs**<br><sub>Jinheng Li, Guosheng Wang, Hongchao Du et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23503) · [PDF](https://arxiv.org/pdf/2610.23503) · [Code](https://github.com/FlashLabAE/HBFSim) |
| 2026-10-16 | **Efficient CPU-GPU collaborative MoE inference via Adaptive Expert Assignment**<br><sub>Wenhui Lv, Yunming Liao, Hongli Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23006) · [PDF](https://arxiv.org/pdf/2610.23006) |
| 2026-10-16 | **BS-Spec: BFP-Based Bit-Sharing for Self-Speculative LLM Decoding with LUT-Driven Mixed-Precision Acceleration**<br><sub>Jiwoo Kim, Gunho Park, Sunwoo Yoo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22877) · [PDF](https://arxiv.org/pdf/2610.22877) |
| 2026-10-15 | **PACE: Pareto-Adaptive Compression for Efficient Native MLLMs**<br><sub>Lei Tian, Chunzheng Zhu, Kai Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.24005) · [PDF](https://arxiv.org/pdf/2610.24005) |
| 2026-10-15 | **Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing**<br><sub>Tianxiang Fei, Jiazheng Kang, Mao Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22196) · [PDF](https://arxiv.org/pdf/2610.22196) |
| 2026-10-15 | **When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill**<br><sub>Muhammad Ibrahim</sub> | [arXiv](https://arxiv.org/abs/2610.21500) · [PDF](https://arxiv.org/pdf/2610.21500) |
| 2026-10-15 | **PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems**<br><sub>Han Shen, Qifu Tyler Sun, Fanyang Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.21390) · [PDF](https://arxiv.org/pdf/2610.21390) |
| 2026-10-15 | **From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models**<br><sub>Chaogui Gou</sub> | [arXiv](https://arxiv.org/abs/2610.21165) · [PDF](https://arxiv.org/pdf/2610.21165) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **99 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration**<br><sub>Javad Rajabi, Hakki Can Karaimer, David B. Lindell et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26837) · [PDF](https://arxiv.org/pdf/2610.26837) |
| 2026-10-19 | **ReAnchor: Reusing Rejected Verifier States for Diffusion Drafting**<br><sub>Sanghyun Lee, Wonjin Nam, Seungho Jang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26531) · [PDF](https://arxiv.org/pdf/2610.26531) |
| 2026-10-19 | **Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion**<br><sub>Yuanyu He, Zhuokun Chen, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26262) · [PDF](https://arxiv.org/pdf/2610.26262) |
| 2026-10-19 | **RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion**<br><sub>Tiange Xu, Kai Liu, Linghe Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26244) · [PDF](https://arxiv.org/pdf/2610.26244) · [Code](https://github.com/lyraxtg/RECAP) |
| 2026-10-19 | **TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation**<br><sub>Jia Li, Xurui Peng, Haowei Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26165) · [PDF](https://arxiv.org/pdf/2610.26165) |
| 2026-10-19 | **LEAP: Accelerating ODE-based Diffusion Sampling with Optimal Linear Leaps**<br><sub>Haowei Zheng, Zhenyu Zhou, Jiawei Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25918) · [PDF](https://arxiv.org/pdf/2610.25918) · [Code](https://github.com/zju-pi/LEAP) |
| 2026-10-19 | **PoSTCache: From Forecasting to Postdictive Smoothing for Revisable Diffusion Caching**<br><sub>Liwei Lan, Hui Chen, Jungong Han et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25664) · [PDF](https://arxiv.org/pdf/2610.25664) |
| 2026-10-18 | **VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse**<br><sub>Sicheng He, Yi Pan, Qiuting Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25043) · [PDF](https://arxiv.org/pdf/2610.25043) |
| 2026-10-16 | **Blitz: Accelerating the Diffusion Modules of AlphaFold3 and Boltz-2**<br><sub>Vinay Saji Mathew, Soundar Kumara, Gretta Kellogg et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23703) · [PDF](https://arxiv.org/pdf/2610.23703) |
| 2026-10-16 | **DIFFLET: A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium**<br><sub>Bin Ma, Min Yu, Vijay Kodamalla et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23047) · [PDF](https://arxiv.org/pdf/2610.23047) |
| 2026-10-16 | **Sink-Sparse Hybrid Attention for Efficient Inference in T2I/T2V Diffusion Transformers**<br><sub>Bingxin Xing, Yu Zhang, Jiatong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22975) · [PDF](https://arxiv.org/pdf/2610.22975) |
| 2026-10-15 | **Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation**<br><sub>SeungJu Cha, Ye-Chan Kim, HyunGee Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22370) · [PDF](https://arxiv.org/pdf/2610.22370) · [Code](https://github.com/SeungJuCha/DaTMe) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **158 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-19 | **SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration**<br><sub>Javad Rajabi, Hakki Can Karaimer, David B. Lindell et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26837) · [PDF](https://arxiv.org/pdf/2610.26837) |
| 2026-10-19 | **Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion**<br><sub>Yuanyu He, Zhuokun Chen, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26262) · [PDF](https://arxiv.org/pdf/2610.26262) |
| 2026-10-19 | **RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion**<br><sub>Tiange Xu, Kai Liu, Linghe Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26244) · [PDF](https://arxiv.org/pdf/2610.26244) · [Code](https://github.com/lyraxtg/RECAP) |
| 2026-10-19 | **TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation**<br><sub>Jia Li, Xurui Peng, Haowei Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26165) · [PDF](https://arxiv.org/pdf/2610.26165) |
| 2026-10-19 | **TamedFlow: Trajectory-Aware Distillation\\for Teacher-Assisted Diffusion Sampling**<br><sub>Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26025) · [PDF](https://arxiv.org/pdf/2610.26025) |
| 2026-10-19 | **LEAP: Accelerating ODE-based Diffusion Sampling with Optimal Linear Leaps**<br><sub>Haowei Zheng, Zhenyu Zhou, Jiawei Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25918) · [PDF](https://arxiv.org/pdf/2610.25918) · [Code](https://github.com/zju-pi/LEAP) |
| 2026-10-19 | **PoSTCache: From Forecasting to Postdictive Smoothing for Revisable Diffusion Caching**<br><sub>Liwei Lan, Hui Chen, Jungong Han et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25664) · [PDF](https://arxiv.org/pdf/2610.25664) |
| 2026-10-18 | **Meta Inverse Prompting for Video Generative Models**<br><sub>Yerin Jung, Jongheon Jeong</sub> | [arXiv](https://arxiv.org/abs/2610.24965) · [PDF](https://arxiv.org/pdf/2610.24965) · [Code](https://github.com/ueriniuno/MVIP) |
| 2026-10-16 | **PreciseEdit: Strong Yet Stable Semantic Transport for One-Step Image Editing**<br><sub>Jingyi Wang, Xiao Lu</sub> | [arXiv](https://arxiv.org/abs/2610.23535) · [PDF](https://arxiv.org/pdf/2610.23535) |
| 2026-10-16 | **Kingfisher: Fast Personalized Visual Autoregressive Generation via Scale-Aware Prompt-Conditioned Scale Decomposition**<br><sub>Dinh-Khoi Vo, Akihiro Sugimoto, Minh-Triet Tran et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23238) · [PDF](https://arxiv.org/pdf/2610.23238) |
| 2026-10-16 | **DIFFLET: A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium**<br><sub>Bin Ma, Min Yu, Vijay Kodamalla et al.</sub> | [arXiv](https://arxiv.org/abs/2610.23047) · [PDF](https://arxiv.org/pdf/2610.23047) |
| 2026-10-16 | **Sink-Sparse Hybrid Attention for Efficient Inference in T2I/T2V Diffusion Transformers**<br><sub>Bingxin Xing, Yu Zhang, Jiatong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.22975) · [PDF](https://arxiv.org/pdf/2610.22975) |

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
