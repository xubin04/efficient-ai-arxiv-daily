# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-10 16:27 CST** · **1661 unique papers** · Newest submission: **2026-11-09**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 264 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 239 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 525 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 176 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 255 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 163 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 279 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 132 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 225 |

## Newly indexed · 2026-11-10

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks**<br><sub>Tingcheng Bian, Kangye Gong, Jinchang Luo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12799) · [PDF](https://arxiv.org/pdf/2611.12799) |
| 2026-11-09 | **How Far Does Second-Order Linear Response Predict Quantization Mismatch? Pre-Registered Measurements on Five Language Models**<br><sub>Dezhen Lu, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2611.12634) · [PDF](https://arxiv.org/pdf/2611.12634) |
| 2026-11-09 | **DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees**<br><sub>Zhicheng Zheng, Cheng Zhang, Chenkai Tang</sub> | [arXiv](https://arxiv.org/abs/2611.12356) · [PDF](https://arxiv.org/pdf/2611.12356) · [Code](https://github.com/Perseus037/DForkTree) |
| 2026-11-09 | **Evolving Infra: Agent-Adaptive LLM Serving at Scale**<br><sub>Hao Kang, Weili Xu, Ziyang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12304) · [PDF](https://arxiv.org/pdf/2611.12304) |
| 2026-11-09 | **RecoGEM: A Serving System for Production-Scale Generative Recommendation**<br><sub>Xiangrui Yang, Yunfeng Zhao, Jiawei Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12296) · [PDF](https://arxiv.org/pdf/2611.12296) |
| 2026-11-09 | **Depth as a Candidate Source: Portfolio Allocation for Recurrent Test-Time Scaling in Large Language Models**<br><sub>Chaoyuan Hao, Wentao Yue, Yanyan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12293) · [PDF](https://arxiv.org/pdf/2611.12293) |
| 2026-11-09 | **VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation**<br><sub>Yongxuan Lv, Zhen Fang, Lichen Man et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12286) · [PDF](https://arxiv.org/pdf/2611.12286) |
| 2026-11-09 | **Prune, Don&#x27;t Merge: Expert Compression of Mixture-of-Experts LLMs on Multilingual Production Tasks**<br><sub>Tomas Rasymas, Povilas Kvedaras</sub> | [arXiv](https://arxiv.org/abs/2611.12240) · [PDF](https://arxiv.org/pdf/2611.12240) |
| 2026-11-09 | **Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos**<br><sub>Hai Zhang, Siqi Liang, Yanjun Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12087) · [PDF](https://arxiv.org/pdf/2611.12087) |
| 2026-11-09 | **Translating KV Caches Between Hybrid-Attention Language Models: MLA Latents, Linear-Attention States and Sparse-Attention Indexers**<br><sub>Povilas Kvedaras, Tomas Rasymas</sub> | [arXiv](https://arxiv.org/abs/2611.12062) · [PDF](https://arxiv.org/pdf/2611.12062) |
| 2026-11-09 | **Four-Step Text-Bearing Image Generation via Distillation with Local Response Regularization and Teacher-Guided Training**<br><sub>Kairui Wen, Sheng Ye, Yong-Jin Liu</sub> | [arXiv](https://arxiv.org/abs/2611.12042) · [PDF](https://arxiv.org/pdf/2611.12042) |
| 2026-11-09 | **Speculative Self-Distillation enables Efficient Knowledge Internalization**<br><sub>Shayan Talaei, Agam Bhatia, Arshia Soltani Moakhar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12016) · [PDF](https://arxiv.org/pdf/2611.12016) · [Code](https://github.com/ShayanTalaei/SpeculativeSelfDistillation) |
| 2026-11-09 | **AutoQS: Automated Quantization Strategy Design with Large Language Models**<br><sub>Zhen Liu, Zhiqin Yang, Yonggang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11975) · [PDF](https://arxiv.org/pdf/2611.11975) |
| 2026-11-09 | **Disagreement-Aware Distribution Matching Distillation for Few-Step Diffusion Models**<br><sub>Zikai Zhou, Zhengpeng Xie, Shitong Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11898) · [PDF](https://arxiv.org/pdf/2611.11898) |
| 2026-11-09 | **Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy&#x27;s Misreading**<br><sub>Ali-Adeeb Abbas, Esmaeil Seraj</sub> | [arXiv](https://arxiv.org/abs/2611.11894) · [PDF](https://arxiv.org/pdf/2611.11894) · [Code](https://github.com/adeeb10abbas/weightsmith) |
| 2026-11-09 | **How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens**<br><sub>Yong Hwi Song, Keon Myung Lee</sub> | [arXiv](https://arxiv.org/abs/2611.11887) · [PDF](https://arxiv.org/pdf/2611.11887) · [Code](https://github.com/thddydgnl/nearest-of-m-world-models) |
| 2026-11-09 | **VeilTune: Secure Fine-Tuning of Private LoRA Adapters on Public Pretrained Language Models**<br><sub>Huiyu Xie, Tanping Zhou, Tao Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11817) · [PDF](https://arxiv.org/pdf/2611.11817) |
| 2026-11-09 | **BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation**<br><sub>Payman Behnam, Debopam Sanyal, Pranav Ponnusamy et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11761) · [PDF](https://arxiv.org/pdf/2611.11761) |
| 2026-11-08 | **Language model capabilities fail in a shared, predictable order under compression and perturbation**<br><sub>Zhixiang Wang, Ulas Bagci</sub> | [arXiv](https://arxiv.org/abs/2611.11695) · [PDF](https://arxiv.org/pdf/2611.11695) · [Code](https://github.com/ZhixiangWang-CN/damage-order-artifacts) |
| 2026-11-08 | **ODSA: Orchestrated Discovery and Self-Aggregation**<br><sub>Macardle Meng, Haomin Zhang</sub> | [arXiv](https://arxiv.org/abs/2611.11621) · [PDF](https://arxiv.org/pdf/2611.11621) |

[View all 58 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **264 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **How Far Does Second-Order Linear Response Predict Quantization Mismatch? Pre-Registered Measurements on Five Language Models**<br><sub>Dezhen Lu, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2611.12634) · [PDF](https://arxiv.org/pdf/2611.12634) |
| 2026-11-09 | **AutoQS: Automated Quantization Strategy Design with Large Language Models**<br><sub>Zhen Liu, Zhiqin Yang, Yonggang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11975) · [PDF](https://arxiv.org/pdf/2611.11975) |
| 2026-11-08 | **Language model capabilities fail in a shared, predictable order under compression and perturbation**<br><sub>Zhixiang Wang, Ulas Bagci</sub> | [arXiv](https://arxiv.org/abs/2611.11695) · [PDF](https://arxiv.org/pdf/2611.11695) · [Code](https://github.com/ZhixiangWang-CN/damage-order-artifacts) |
| 2026-11-08 | **SGA-Sparse: Training Native SwiGLU Gates for Activation-Sparse and Low-Bit LLMs**<br><sub>Ruokai Yin, Steven Li</sub> | [arXiv](https://arxiv.org/abs/2611.11223) · [PDF](https://arxiv.org/pdf/2611.11223) |
| 2026-11-08 | **When Calibration Data Matter in Sub-4-Bit Language Model Quantization**<br><sub>Yehong Jiang, Yen-Kuang Chen, Xinmin Tian</sub> | [arXiv](https://arxiv.org/abs/2611.11079) · [PDF](https://arxiv.org/pdf/2611.11079) |
| 2026-11-07 | **MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations**<br><sub>Lorenz K. Muller, Philippe Bich, Chiara Boretti et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10649) · [PDF](https://arxiv.org/pdf/2611.10649) |
| 2026-11-06 | **AutoEMatic: Runtime-Adaptive Mixed-Precision LLM Inference via Automatic Exponent-Mantissa Refinement**<br><sub>Akshat Ramachandran, Reena Elangovan, Rangharajan Venkatesan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10165) · [PDF](https://arxiv.org/pdf/2611.10165) |
| 2026-11-06 | **BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design**<br><sub>Dayou Du, Woon Yee Ng, Guangming Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09825) · [PDF](https://arxiv.org/pdf/2611.09825) · [Code](https://github.com/OpenBitSys/BitDecoding-FP4) |
| 2026-11-06 | **Coordinated Mixed-Precision KV Cache Quantization for Efficient LLM-based Multi-agent Systems**<br><sub>Weizhong Huang, Jinchao Zhang, Xiawu Zheng</sub> | [arXiv](https://arxiv.org/abs/2611.10096) · [PDF](https://arxiv.org/pdf/2611.10096) |
| 2026-11-06 | **FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding**<br><sub>Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09722) · [PDF](https://arxiv.org/pdf/2611.09722) · [Code](https://github.com/FutureMLS-Lab/FOSCAR) |
| 2026-11-06 | **MINE: Entropy-coded Memory-efficient Inference for Large Language Models**<br><sub>Emil Schätzle, Markus Püschel</sub> | [arXiv](https://arxiv.org/abs/2611.09424) · [PDF](https://arxiv.org/pdf/2611.09424) |
| 2026-11-06 | **ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization Aware Training**<br><sub>Liqun Ma, Shengkun Tang, Liangyu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08924) · [PDF](https://arxiv.org/pdf/2611.08924) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **239 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **Prune, Don&#x27;t Merge: Expert Compression of Mixture-of-Experts LLMs on Multilingual Production Tasks**<br><sub>Tomas Rasymas, Povilas Kvedaras</sub> | [arXiv](https://arxiv.org/abs/2611.12240) · [PDF](https://arxiv.org/pdf/2611.12240) |
| 2026-11-08 | **Language model capabilities fail in a shared, predictable order under compression and perturbation**<br><sub>Zhixiang Wang, Ulas Bagci</sub> | [arXiv](https://arxiv.org/abs/2611.11695) · [PDF](https://arxiv.org/pdf/2611.11695) · [Code](https://github.com/ZhixiangWang-CN/damage-order-artifacts) |
| 2026-11-08 | **Decomposing Earth Embeddings with Sparse Autoencoders**<br><sub>Vitus Benson, Fanny Yang, Markus Reichstein</sub> | [arXiv](https://arxiv.org/abs/2611.11398) · [PDF](https://arxiv.org/pdf/2611.11398) · [Code](https://github.com/EarthyScience/geosae) |
| 2026-11-08 | **D3Tree: Learning to Prune Block-Diffusion Draft Trees for Efficient Verification**<br><sub>Hong Nie, Zhangchi Gao, Jun Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11371) · [PDF](https://arxiv.org/pdf/2611.11371) |
| 2026-11-08 | **SGA-Sparse: Training Native SwiGLU Gates for Activation-Sparse and Low-Bit LLMs**<br><sub>Ruokai Yin, Steven Li</sub> | [arXiv](https://arxiv.org/abs/2611.11223) · [PDF](https://arxiv.org/pdf/2611.11223) |
| 2026-11-07 | **Slim Foundation Models for Latency-Critical Recommendation Serving**<br><sub>Danyal Aftab, Anas Zafar, Assadig Abakr et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11013) · [PDF](https://arxiv.org/pdf/2611.11013) |
| 2026-11-07 | **ESTRA: Enabling Extreme Attention Sparsity for Training-Free Video Diffusion Acceleration**<br><sub>Enhuai Liu, Yunke Wang, Yutong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10448) · [PDF](https://arxiv.org/pdf/2611.10448) |
| 2026-11-07 | **Pruning DNA Sequence**<br><sub>Faias Satter, Shaker Islam, Aminul Islam</sub> | [arXiv](https://arxiv.org/abs/2611.10386) · [PDF](https://arxiv.org/pdf/2611.10386) · [Code](https://github.com/FaiasPromit/pruning-dna-sequence) |
| 2026-11-06 | **DUET: Dual-Sparse Inference for Block Diffusion Language Models**<br><sub>Siyuan Yan, Shen Gu, Xiaoxing Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09239) · [PDF](https://arxiv.org/pdf/2611.09239) |
| 2026-11-06 | **Cross-Layer TopK: Dynamically Allocating Sparsity Across Layers in Transcoders**<br><sub>Anyuan Zhuo, Shaohua Zhang, Tianle Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09233) · [PDF](https://arxiv.org/pdf/2611.09233) · [Code](https://huggingface.co/ByteDance-Seed/Cross-Layer-TopK-CLT) |
| 2026-11-06 | **UniExit: A Unified Latency-Aware Early-Exit Runtime for Heterogeneous Edge AI**<br><sub>Yuhang Guan, Huanle Zhang, Xiaomin Ouyang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09159) · [PDF](https://arxiv.org/pdf/2611.09159) |
| 2026-11-06 | **GeoJeV: Unified Spatial Probability for Training-Free Efficient Evidence Acquisition in Ultra-High-Resolution Remote Sensing**<br><sub>Xinyi Niu, Lingfeng Chen, Jiehua Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08879) · [PDF](https://arxiv.org/pdf/2611.08879) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **525 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks**<br><sub>Tingcheng Bian, Kangye Gong, Jinchang Luo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12799) · [PDF](https://arxiv.org/pdf/2611.12799) |
| 2026-11-09 | **VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation**<br><sub>Yongxuan Lv, Zhen Fang, Lichen Man et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12286) · [PDF](https://arxiv.org/pdf/2611.12286) |
| 2026-11-09 | **Four-Step Text-Bearing Image Generation via Distillation with Local Response Regularization and Teacher-Guided Training**<br><sub>Kairui Wen, Sheng Ye, Yong-Jin Liu</sub> | [arXiv](https://arxiv.org/abs/2611.12042) · [PDF](https://arxiv.org/pdf/2611.12042) |
| 2026-11-09 | **Speculative Self-Distillation enables Efficient Knowledge Internalization**<br><sub>Shayan Talaei, Agam Bhatia, Arshia Soltani Moakhar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12016) · [PDF](https://arxiv.org/pdf/2611.12016) · [Code](https://github.com/ShayanTalaei/SpeculativeSelfDistillation) |
| 2026-11-09 | **Disagreement-Aware Distribution Matching Distillation for Few-Step Diffusion Models**<br><sub>Zikai Zhou, Zhengpeng Xie, Shitong Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11898) · [PDF](https://arxiv.org/pdf/2611.11898) |
| 2026-11-09 | **Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy&#x27;s Misreading**<br><sub>Ali-Adeeb Abbas, Esmaeil Seraj</sub> | [arXiv](https://arxiv.org/abs/2611.11894) · [PDF](https://arxiv.org/pdf/2611.11894) · [Code](https://github.com/adeeb10abbas/weightsmith) |
| 2026-11-09 | **How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens**<br><sub>Yong Hwi Song, Keon Myung Lee</sub> | [arXiv](https://arxiv.org/abs/2611.11887) · [PDF](https://arxiv.org/pdf/2611.11887) · [Code](https://github.com/thddydgnl/nearest-of-m-world-models) |
| 2026-11-08 | **Perturbing Inputs Improves Pretraining Distillation**<br><sub>Ziyang Cai, Yihe Dong, Dimitris Papailiopoulos et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11598) · [PDF](https://arxiv.org/pdf/2611.11598) |
| 2026-11-08 | **How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?**<br><sub>Cong Yu, Ziting Wang, Songlin Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11450) · [PDF](https://arxiv.org/pdf/2611.11450) · [Code](https://github.com/benyucong/train-inference-mismatch-opd) |
| 2026-11-08 | **Guidance at Pure Noise Erodes Speaker Similarity in Few-Step Token-Conditioned Flow-Matching TTS**<br><sub>Jaeho Lee, Han-Lim Choi</sub> | [arXiv](https://arxiv.org/abs/2611.11179) · [PDF](https://arxiv.org/pdf/2611.11179) · [Code](https://github.com/16jhlee/FSU) |
| 2026-11-07 | **Horizon-Scalable Q-Learning**<br><sub>Haoran Xu, Pragya Srivastava, Xinjie Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10987) · [PDF](https://arxiv.org/pdf/2611.10987) |
| 2026-11-07 | **CoupledFlow: One-Step Neural Operators for Coupled Multi-Physics PDEs**<br><sub>Trong Khiem Tran, Minh Long Bui, Phi Le Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10945) · [PDF](https://arxiv.org/pdf/2611.10945) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **176 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **VeilTune: Secure Fine-Tuning of Private LoRA Adapters on Public Pretrained Language Models**<br><sub>Huiyu Xie, Tanping Zhou, Tao Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11817) · [PDF](https://arxiv.org/pdf/2611.11817) |
| 2026-11-07 | **Slim Foundation Models for Latency-Critical Recommendation Serving**<br><sub>Danyal Aftab, Anas Zafar, Assadig Abakr et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11013) · [PDF](https://arxiv.org/pdf/2611.11013) |
| 2026-11-07 | **Bayesian Low-Rank Posteriors for Scalable Membership Inference**<br><sub>Khanh Nguyen, Antonio Emanuele Cinà, Andrey Barsky et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10455) · [PDF](https://arxiv.org/pdf/2611.10455) |
| 2026-11-07 | **Reproducible LoRA Inference Through Deterministic Split-K Reduction**<br><sub>Dhayaneshwar Balusamy, Ankur Mohan</sub> | [arXiv](https://arxiv.org/abs/2611.10334) · [PDF](https://arxiv.org/pdf/2611.10334) |
| 2026-11-06 | **FedLoVA: Value-Only Aggregation for Federated LoRA Fine-Tuning of Large Language Models**<br><sub>Ensieh Khazaei, Baturalp Buyukates, Dimitrios Hatzinakos</sub> | [arXiv](https://arxiv.org/abs/2611.10248) · [PDF](https://arxiv.org/pdf/2611.10248) · [Code](https://github.com/EnsiehKhazaei/FedLoVA) |
| 2026-11-06 | **Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters**<br><sub>Constantinos Karouzos, Nikolaos Aletras</sub> | [arXiv](https://arxiv.org/abs/2611.09634) · [PDF](https://arxiv.org/pdf/2611.09634) |
| 2026-11-06 | **Know What You Need: Efficient Activation Checkpointing**<br><sub>Danyal Ahmed, Edouard Oyallon</sub> | [arXiv](https://arxiv.org/abs/2611.09614) · [PDF](https://arxiv.org/pdf/2611.09614) |
| 2026-11-06 | **From LoRA to Language: Recovering Skill Documents from Adapters**<br><sub>Saranya Dintakurthy Swadha, Pavan C Shekar, Arpit Jain et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09454) · [PDF](https://arxiv.org/pdf/2611.09454) |
| 2026-11-06 | **ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization Aware Training**<br><sub>Liqun Ma, Shengkun Tang, Liangyu Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08924) · [PDF](https://arxiv.org/pdf/2611.08924) |
| 2026-11-05 | **Towards interpreting any residual stream direction by scaling activation inversion**<br><sub>Celeste De Schamphelaere, Juan J. Vazquez, Ari Spiesberger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08465) · [PDF](https://arxiv.org/pdf/2611.08465) |
| 2026-11-05 | **Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval**<br><sub>Dohoon Kim, Junho Park, Hyunwoong Bae et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07820) · [PDF](https://arxiv.org/pdf/2611.07820) · [Code](https://github.com/dohoonkim-ai/axis-lora) |
| 2026-11-05 | **Embedding-Space Fingerprinting of LoRA Fine-Tunes: Recovering the Training-Data Domain from the Model Artifact Alone**<br><sub>Shivesh Rane</sub> | [arXiv](https://arxiv.org/abs/2611.07610) · [PDF](https://arxiv.org/pdf/2611.07610) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **255 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **Evolving Infra: Agent-Adaptive LLM Serving at Scale**<br><sub>Hao Kang, Weili Xu, Ziyang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12304) · [PDF](https://arxiv.org/pdf/2611.12304) |
| 2026-11-09 | **Translating KV Caches Between Hybrid-Attention Language Models: MLA Latents, Linear-Attention States and Sparse-Attention Indexers**<br><sub>Povilas Kvedaras, Tomas Rasymas</sub> | [arXiv](https://arxiv.org/abs/2611.12062) · [PDF](https://arxiv.org/pdf/2611.12062) |
| 2026-11-09 | **BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation**<br><sub>Payman Behnam, Debopam Sanyal, Pranav Ponnusamy et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11761) · [PDF](https://arxiv.org/pdf/2611.11761) |
| 2026-11-08 | **Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation**<br><sub>Weizhong Huang, Huaijia Kou, Tianyu Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11452) · [PDF](https://arxiv.org/pdf/2611.11452) |
| 2026-11-08 | **Verify Before You Fetch: Reliable KV Cache Compression for LLM Inference**<br><sub>Devanshu Jha, Gaurav Kumar, Agniva Chowdhury et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11319) · [PDF](https://arxiv.org/pdf/2611.11319) · [Code](https://github.com/epsilon-prime/verifiedKV) |
| 2026-11-07 | **Mirage: Provable Defense Against LLM KV Cache Timing Side Channels with Topology-Aware Isolation**<br><sub>Xiaobei Yan, Tianwei Zhang</sub> | [arXiv](https://arxiv.org/abs/2611.10756) · [PDF](https://arxiv.org/pdf/2611.10756) |
| 2026-11-07 | **Coverage-Verified Sparse Attention: Closed-Loop Quality Control for Long-Context LLM Decoding**<br><sub>Yan-Cheng Li, Chun-Yi Lee</sub> | [arXiv](https://arxiv.org/abs/2611.10634) · [PDF](https://arxiv.org/pdf/2611.10634) |
| 2026-11-07 | **OneReel: Efficient Multi-Scene Video Generation with Scene-Structured Attention**<br><sub>Wei Zhang, Yuchen Wang, Tianrui Feng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10594) · [PDF](https://arxiv.org/pdf/2611.10594) |
| 2026-11-07 | **ESTRA: Enabling Extreme Attention Sparsity for Training-Free Video Diffusion Acceleration**<br><sub>Enhuai Liu, Yunke Wang, Yutong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10448) · [PDF](https://arxiv.org/pdf/2611.10448) |
| 2026-11-06 | **PACE: Keeping the Right Tokens in the KV Cache Is Not Enough for Long-Horizon LLM Agents**<br><sub>Suman Chatterjee</sub> | [arXiv](https://arxiv.org/abs/2611.10240) · [PDF](https://arxiv.org/pdf/2611.10240) |
| 2026-11-06 | **AutoEMatic: Runtime-Adaptive Mixed-Precision LLM Inference via Automatic Exponent-Mantissa Refinement**<br><sub>Akshat Ramachandran, Reena Elangovan, Rangharajan Venkatesan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10165) · [PDF](https://arxiv.org/pdf/2611.10165) |
| 2026-11-06 | **BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design**<br><sub>Dayou Du, Woon Yee Ng, Guangming Sheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09825) · [PDF](https://arxiv.org/pdf/2611.09825) · [Code](https://github.com/OpenBitSys/BitDecoding-FP4) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **163 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees**<br><sub>Zhicheng Zheng, Cheng Zhang, Chenkai Tang</sub> | [arXiv](https://arxiv.org/abs/2611.12356) · [PDF](https://arxiv.org/pdf/2611.12356) · [Code](https://github.com/Perseus037/DForkTree) |
| 2026-11-09 | **Depth as a Candidate Source: Portfolio Allocation for Recurrent Test-Time Scaling in Large Language Models**<br><sub>Chaoyuan Hao, Wentao Yue, Yanyan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12293) · [PDF](https://arxiv.org/pdf/2611.12293) |
| 2026-11-08 | **ODSA: Orchestrated Discovery and Self-Aggregation**<br><sub>Macardle Meng, Haomin Zhang</sub> | [arXiv](https://arxiv.org/abs/2611.11621) · [PDF](https://arxiv.org/pdf/2611.11621) |
| 2026-11-08 | **D3Tree: Learning to Prune Block-Diffusion Draft Trees for Efficient Verification**<br><sub>Hong Nie, Zhangchi Gao, Jun Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11371) · [PDF](https://arxiv.org/pdf/2611.11371) |
| 2026-11-07 | **Coverage-Verified Sparse Attention: Closed-Loop Quality Control for Long-Context LLM Decoding**<br><sub>Yan-Cheng Li, Chun-Yi Lee</sub> | [arXiv](https://arxiv.org/abs/2611.10634) · [PDF](https://arxiv.org/pdf/2611.10634) |
| 2026-11-07 | **Test-Time Scaling for Diffusion Language Models with Frequency-Aware Remasking**<br><sub>Bowen Zuo, Yue Yu, Dongruo Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10486) · [PDF](https://arxiv.org/pdf/2611.10486) |
| 2026-11-06 | **WorldMind: Test-Time Scaling for Visual Spatial Reasoning through Latent World Simulation**<br><sub>Haoming Wang, Yongjian Fu, Ju Ren et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10151) · [PDF](https://arxiv.org/pdf/2611.10151) |
| 2026-11-05 | **ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding**<br><sub>Selim Aktas, Yusuf Erdem Erdem, Ahmed Zeer et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08669) · [PDF](https://arxiv.org/pdf/2611.08669) |
| 2026-11-05 | **Measured Coupling for Parallel Decoding in Diffusion Language Models**<br><sub>Tal Oved, Lior Wolf</sub> | [arXiv](https://arxiv.org/abs/2611.08307) · [PDF](https://arxiv.org/pdf/2611.08307) |
| 2026-11-05 | **Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding**<br><sub>Adrian Baule</sub> | [arXiv](https://arxiv.org/abs/2611.07845) · [PDF](https://arxiv.org/pdf/2611.07845) |
| 2026-11-05 | **FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving**<br><sub>Xuan Wang, Zhuanhao Wu, Tingzhu Fang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.07542) · [PDF](https://arxiv.org/pdf/2611.07542) · [Code](https://github.com/vllm-project/vllm-ascend/tree/releases/v0.30.0) |
| 2026-11-05 | **Latency-Aware Adaptive Best-of-$N$**<br><sub>Alon Jacobson, Qian Xie, Peter I. Frazier</sub> | [arXiv](https://arxiv.org/abs/2611.07453) · [PDF](https://arxiv.org/pdf/2611.07453) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **279 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **Evolving Infra: Agent-Adaptive LLM Serving at Scale**<br><sub>Hao Kang, Weili Xu, Ziyang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12304) · [PDF](https://arxiv.org/pdf/2611.12304) |
| 2026-11-09 | **RecoGEM: A Serving System for Production-Scale Generative Recommendation**<br><sub>Xiangrui Yang, Yunfeng Zhao, Jiawei Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12296) · [PDF](https://arxiv.org/pdf/2611.12296) |
| 2026-11-09 | **Prune, Don&#x27;t Merge: Expert Compression of Mixture-of-Experts LLMs on Multilingual Production Tasks**<br><sub>Tomas Rasymas, Povilas Kvedaras</sub> | [arXiv](https://arxiv.org/abs/2611.12240) · [PDF](https://arxiv.org/pdf/2611.12240) |
| 2026-11-09 | **BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation**<br><sub>Payman Behnam, Debopam Sanyal, Pranav Ponnusamy et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11761) · [PDF](https://arxiv.org/pdf/2611.11761) |
| 2026-11-08 | **Verify Before You Fetch: Reliable KV Cache Compression for LLM Inference**<br><sub>Devanshu Jha, Gaurav Kumar, Agniva Chowdhury et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11319) · [PDF](https://arxiv.org/pdf/2611.11319) · [Code](https://github.com/epsilon-prime/verifiedKV) |
| 2026-11-07 | **Slim Foundation Models for Latency-Critical Recommendation Serving**<br><sub>Danyal Aftab, Anas Zafar, Assadig Abakr et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11013) · [PDF](https://arxiv.org/pdf/2611.11013) |
| 2026-11-07 | **Inference for Reasoning Models: Practical Lessons from Evaluation and Serving**<br><sub>Luv Verma</sub> | [arXiv](https://arxiv.org/abs/2611.10845) · [PDF](https://arxiv.org/pdf/2611.10845) |
| 2026-11-07 | **Mirage: Provable Defense Against LLM KV Cache Timing Side Channels with Topology-Aware Isolation**<br><sub>Xiaobei Yan, Tianwei Zhang</sub> | [arXiv](https://arxiv.org/abs/2611.10756) · [PDF](https://arxiv.org/pdf/2611.10756) |
| 2026-11-07 | **Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed**<br><sub>Peixu Xin, Runchuan Feng, Jiazhen Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10611) · [PDF](https://arxiv.org/pdf/2611.10611) |
| 2026-11-07 | **Efficient LLM Adaptation with Forward-Only Passes**<br><sub>Baichuan Huang, Ananth Balashankar, Amir Aminifar</sub> | [arXiv](https://arxiv.org/abs/2611.10610) · [PDF](https://arxiv.org/pdf/2611.10610) |
| 2026-11-07 | **Beyond Query Similarity: Safety-Conditioned Cache Routing for LLM Response Reuse**<br><sub>Shilong Pan, Zhiliang Tian, Weiguo Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10418) · [PDF](https://arxiv.org/pdf/2611.10418) |
| 2026-11-06 | **PACE: Keeping the Right Tokens in the KV Cache Is Not Enough for Long-Horizon LLM Agents**<br><sub>Suman Chatterjee</sub> | [arXiv](https://arxiv.org/abs/2611.10240) · [PDF](https://arxiv.org/pdf/2611.10240) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **132 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees**<br><sub>Zhicheng Zheng, Cheng Zhang, Chenkai Tang</sub> | [arXiv](https://arxiv.org/abs/2611.12356) · [PDF](https://arxiv.org/pdf/2611.12356) · [Code](https://github.com/Perseus037/DForkTree) |
| 2026-11-08 | **MG-Cache: Multi-Granularity Caching for Accelerating Diffusion Transformer Inference**<br><sub>Zesen Chen, Youxuan Xu, Shigang Li</sub> | [arXiv](https://arxiv.org/abs/2611.11365) · [PDF](https://arxiv.org/pdf/2611.11365) |
| 2026-11-07 | **FADE: Fractional Anomalous Dynamics Extrapolation for Training-Free Diffusion Transformers Acceleration**<br><sub>Jinlong Yang, Lizilin, Jinke Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10514) · [PDF](https://arxiv.org/pdf/2611.10514) |
| 2026-11-07 | **ESTRA: Enabling Extreme Attention Sparsity for Training-Free Video Diffusion Acceleration**<br><sub>Enhuai Liu, Yunke Wang, Yutong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10448) · [PDF](https://arxiv.org/pdf/2611.10448) |
| 2026-11-07 | **IdealCache: Rethinking Cache Scheduling in Diffusion Transformers via Ideal Trajectories**<br><sub>Shang Xue, Li Zhu, Ping Chen</sub> | [arXiv](https://arxiv.org/abs/2611.10340) · [PDF](https://arxiv.org/pdf/2611.10340) |
| 2026-11-06 | **Verifier Noise Is a Temperature: Testing Tilt Predictions in Finite-Budget LLM-Guided Search**<br><sub>Xiaomeng Li</sub> | [arXiv](https://arxiv.org/abs/2611.09699) · [PDF](https://arxiv.org/pdf/2611.09699) |
| 2026-11-04 | **Phantom: Temporal Caching for Diffusion Models**<br><sub>Yuzhe Fu, Cong Guo, Zishan Shao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.06019) · [PDF](https://arxiv.org/pdf/2611.06019) |
| 2026-11-04 | **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**<br><sub>Yanjin Li, Bingbing Qiu, Qiang Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05917) · [PDF](https://arxiv.org/pdf/2611.05917) |
| 2026-11-03 | **Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation**<br><sub>Rohan Agarwal, Robin Andeer, Alex Armbruster et al.</sub> | [arXiv](https://arxiv.org/abs/2611.05642) · [PDF](https://arxiv.org/pdf/2611.05642) |
| 2026-11-02 | **Denoising Is Stein: Moment Access and a Resource Hierarchy for Learning Hidden Structure in Diffusion Models**<br><sub>Rui Wang</sub> | [arXiv](https://arxiv.org/abs/2611.04043) · [PDF](https://arxiv.org/pdf/2611.04043) |
| 2026-11-01 | **Z-Cache: Accelerating Diffusion Transformers via Self-Reflection**<br><sub>Zegang Cheng, Zhikai Wang, Jiacheng Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01846) · [PDF](https://arxiv.org/pdf/2611.01846) |
| 2026-10-31 | **Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference**<br><sub>Zhichen Zeng, Xichong Zhang, Junpan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.01320) · [PDF](https://arxiv.org/pdf/2611.01320) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **225 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-09 | **Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos**<br><sub>Hai Zhang, Siqi Liang, Yanjun Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.12087) · [PDF](https://arxiv.org/pdf/2611.12087) |
| 2026-11-09 | **Four-Step Text-Bearing Image Generation via Distillation with Local Response Regularization and Teacher-Guided Training**<br><sub>Kairui Wen, Sheng Ye, Yong-Jin Liu</sub> | [arXiv](https://arxiv.org/abs/2611.12042) · [PDF](https://arxiv.org/pdf/2611.12042) |
| 2026-11-08 | **ForeAct: Geometry-Guided Action Learning from World Representations**<br><sub>Wei Lu, Jiaxi Zhang, Yunheng Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11500) · [PDF](https://arxiv.org/pdf/2611.11500) |
| 2026-11-08 | **Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation**<br><sub>Weizhong Huang, Huaijia Kou, Tianyu Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11452) · [PDF](https://arxiv.org/pdf/2611.11452) |
| 2026-11-08 | **MG-Cache: Multi-Granularity Caching for Accelerating Diffusion Transformer Inference**<br><sub>Zesen Chen, Youxuan Xu, Shigang Li</sub> | [arXiv](https://arxiv.org/abs/2611.11365) · [PDF](https://arxiv.org/pdf/2611.11365) |
| 2026-11-08 | **Source-Anchored Visual Autoregression for Extreme Image Compression**<br><sub>Bingxin Wang, Yuan Lan, Yang Xiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.11200) · [PDF](https://arxiv.org/pdf/2611.11200) |
| 2026-11-07 | **REDiff-AD: No Training and No Target Masks for Industrial Anomaly Image Generation via Diversity-Driven In-Context MMDiT**<br><sub>Chih-Yu Tsai, Chih-Heng Chang, Jian-Jiun Ding</sub> | [arXiv](https://arxiv.org/abs/2611.10875) · [PDF](https://arxiv.org/pdf/2611.10875) · [Code](https://github.com/efdefe4-droid/REDiff-AD) |
| 2026-11-07 | **MGE: A Membership Guided Data Extraction Attack against Diffusion Models**<br><sub>Yuchang Mei, Longqiang Wang, Haoyang Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10678) · [PDF](https://arxiv.org/pdf/2611.10678) |
| 2026-11-07 | **OneReel: Efficient Multi-Scene Video Generation with Scene-Structured Attention**<br><sub>Wei Zhang, Yuchen Wang, Tianrui Feng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10594) · [PDF](https://arxiv.org/pdf/2611.10594) |
| 2026-11-07 | **ESTRA: Enabling Extreme Attention Sparsity for Training-Free Video Diffusion Acceleration**<br><sub>Enhuai Liu, Yunke Wang, Yutong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.10448) · [PDF](https://arxiv.org/pdf/2611.10448) |
| 2026-11-06 | **Emo-LiveSync: Real-Time Universal Lip Synchronization with Explicit Emotion Control**<br><sub>Sangjoon Yu, Seungeun Lee, JoonHeyok Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.09074) · [PDF](https://arxiv.org/pdf/2611.09074) |
| 2026-11-05 | **InstaGen: Group-Shared Importance Sampling for Fast Video Generation**<br><sub>Kislay Aditya Oj, Kumar Krishna Agrawal, Sri Surya Varma Datla et al.</sub> | [arXiv](https://arxiv.org/abs/2611.08610) · [PDF](https://arxiv.org/pdf/2611.08610) |

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
