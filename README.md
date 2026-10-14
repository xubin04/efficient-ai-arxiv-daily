# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-14 18:02 CST** · **985 unique papers** · Newest submission: **2026-10-13**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 156 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 143 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 331 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 97 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 136 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 97 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 162 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 80 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 129 |

## Newly indexed · 2026-10-14

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs**<br><sub>Aimon Rahman, Joymallya Chakraborty, Vidit Bansal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18858) · [PDF](https://arxiv.org/pdf/2610.18858) |
| 2026-10-13 | **GAD: Geometry Attention Distillation for Consistent Video Generation**<br><sub>Junfeng Ni, Ziyu Zhu, Fan Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18779) · [PDF](https://arxiv.org/pdf/2610.18779) |
| 2026-10-13 | **SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models**<br><sub>Yuqi Huang, Xingyao Li, Yunlong Hou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18735) · [PDF](https://arxiv.org/pdf/2610.18735) |
| 2026-10-13 | **Unlocking Token Rewards via Training-Free Reward Attribution**<br><sub>Sitong Wu, Haoru Tan, Bin Xia et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18704) · [PDF](https://arxiv.org/pdf/2610.18704) · [Code](https://github.com/stonewst/P2T) |
| 2026-10-13 | **Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning**<br><sub>Tianhao Fu, Austin Wang, Charles Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18690) · [PDF](https://arxiv.org/pdf/2610.18690) |
| 2026-10-13 | **MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization**<br><sub>Yangchengyu Zhou, Zhiping Wu, Runchang Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18642) · [PDF](https://arxiv.org/pdf/2610.18642) · [Code](https://github.com/RL-MIND/MultiAlloc) |
| 2026-10-13 | **Recasting DiT for Extreme Image Compression with Hierarchical Visual Priors**<br><sub>Yunuo Chen, Jingnan Gao, Bing He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18607) · [PDF](https://arxiv.org/pdf/2610.18607) |
| 2026-10-13 | **LLM2R: From Large Language Models to 3D Reassemblers**<br><sub>Zhouhan Zhong, Qiuhong Shen, Xingyi Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18604) · [PDF](https://arxiv.org/pdf/2610.18604) |
| 2026-10-13 | **Compare to Correct: Pairwise-Guided Logit Adjustment for LLM Test-Time Scaling**<br><sub>Cong Hua, Qianqian Xu, Zitai Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18583) · [PDF](https://arxiv.org/pdf/2610.18583) |
| 2026-10-13 | **Rethinking Quality in Large Language Model Routing: Security-Conditioned Model-and-Budget Selection**<br><sub>Yichi Zhang, Zhenxiang Huang, Yuyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18566) · [PDF](https://arxiv.org/pdf/2610.18566) |
| 2026-10-13 | **Two For The Price Of One: Curvature-Aware Pruning Preserves Influence Functions Too**<br><sub>Mehdi Makni, Natalia Ponomareva, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2610.18516) · [PDF](https://arxiv.org/pdf/2610.18516) |
| 2026-10-13 | **Simplifying and Improving On-Policy Distillation for Few-Step Diffusion**<br><sub>Jiawei Zhang, Ziyu Wan, Nanye Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18472) · [PDF](https://arxiv.org/pdf/2610.18472) |
| 2026-10-13 | **Readout Scaling Shapes Sparse Feature Recovery**<br><sub>Brain Xiao, Sarah Wilson</sub> | [arXiv](https://arxiv.org/abs/2610.18462) · [PDF](https://arxiv.org/pdf/2610.18462) |
| 2026-10-13 | **FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving**<br><sub>Yunfei Feng, Jingkai He, Shiqi Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18451) · [PDF](https://arxiv.org/pdf/2610.18451) |
| 2026-10-13 | **Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs**<br><sub>Peiran Yin, Hao Wu, Zihao Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18399) · [PDF](https://arxiv.org/pdf/2610.18399) · [Code](https://github.com/EIT-NLP/Bifocal) |
| 2026-10-13 | **Lightweight but Linguistically Fair? Quantisation Robustness across Bavarian, German, and English**<br><sub>Jophin John, Michael Hoffmann, Piroska Lendvai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18343) · [PDF](https://arxiv.org/pdf/2610.18343) |
| 2026-10-13 | **LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout**<br><sub>Ziyu Zhu, Zhaoxu Sun, Fan Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18289) · [PDF](https://arxiv.org/pdf/2610.18289) · [Code](https://github.com/Fantasy-AMAP/LongForcing) |
| 2026-10-13 | **Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation**<br><sub>Yaoli Liu, Guo-Hua Wang, Yiyang Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18284) · [PDF](https://arxiv.org/pdf/2610.18284) |
| 2026-10-13 | **Teach Me After You Learn It: Lookahead Self-Distillation for RLVR**<br><sub>Zepeng Zhai, Meilin Chen</sub> | [arXiv](https://arxiv.org/abs/2610.18256) · [PDF](https://arxiv.org/pdf/2610.18256) |
| 2026-10-13 | **RadixFlow: Filling Execution Bubbles in Prefix-Cached Hybrid LLM Serving**<br><sub>Huihao Jing, Wenbin Hu, Shaojin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18143) · [PDF](https://arxiv.org/pdf/2610.18143) |

[View all 126 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **156 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization**<br><sub>Yangchengyu Zhou, Zhiping Wu, Runchang Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18642) · [PDF](https://arxiv.org/pdf/2610.18642) · [Code](https://github.com/RL-MIND/MultiAlloc) |
| 2026-10-13 | **Lightweight but Linguistically Fair? Quantisation Robustness across Bavarian, German, and English**<br><sub>Jophin John, Michael Hoffmann, Piroska Lendvai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18343) · [PDF](https://arxiv.org/pdf/2610.18343) |
| 2026-10-13 | **Revisiting Error Feedback for Model Quantization**<br><sub>Wai-Yiu Keung, Chi Cui, Wing-Kin Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18139) · [PDF](https://arxiv.org/pdf/2610.18139) |
| 2026-10-13 | **BELT : BEhavior-Aligned Low-Rank KV Cache Compression with Learned Top-k Rank Allocation**<br><sub>Yaoyang Liu, Shuwei Shen, Jincheng Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17966) · [PDF](https://arxiv.org/pdf/2610.17966) |
| 2026-10-13 | **Mixed Precision Scaling Laws for Quantized Pretraining**<br><sub>Jinuk Kim, Rajarshi Saha, Muhammed Fatih Balin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17637) · [PDF](https://arxiv.org/pdf/2610.17637) |
| 2026-10-13 | **Capacity over TFLOPS: Memory-Centric Deployment of Large Clinical Language Models on Consumer CPUs**<br><sub>Eli Yune, Umer Majeed, Mahesh Balan</sub> | [arXiv](https://arxiv.org/abs/2610.17551) · [PDF](https://arxiv.org/pdf/2610.17551) · [Code](https://github.com/balkeumlabs/LLM-on-CPU) |
| 2026-10-13 | **Towards Green AI: Evaluating Energy Efficiency for Quantized LLM Inference**<br><sub>Petar Basta</sub> | [arXiv](https://arxiv.org/abs/2610.17531) · [PDF](https://arxiv.org/pdf/2610.17531) |
| 2026-10-12 | **LoopQuant: Accurate and Efficient Post-Training Quantization for Looped Transformers**<br><sub>Zhixiong Zhao, Zukang Xu, Xing Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16368) · [PDF](https://arxiv.org/pdf/2610.16368) · [Code](https://github.com/Kishon-zzx/LoopQuant%5D) |
| 2026-10-12 | **Fast Quantized Johnson$-$Lindenstrauss Transforms**<br><sub>Angelos Korakitis, Vasileios Nakos</sub> | [arXiv](https://arxiv.org/abs/2610.16289) · [PDF](https://arxiv.org/pdf/2610.16289) |
| 2026-10-11 | **The Price of Precision: A Calibrated Cost Model for Mixed-Precision LLM Serving**<br><sub>Mukund Athmaram, Manoj Rao, Liang Ma</sub> | [arXiv](https://arxiv.org/abs/2610.15629) · [PDF](https://arxiv.org/pdf/2610.15629) |
| 2026-10-11 | **E8 Lattice Key Quantization for Low-Bit KV-Cache Compression**<br><sub>Sasho Nedelkoski, Alexander Acker, Soeren Becker et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15384) · [PDF](https://arxiv.org/pdf/2610.15384) |
| 2026-10-11 | **TempoKV: Predictive KV Cache Quantization for Autoregressive Video Generation**<br><sub>Jiahui Hu, Weile Mo, Peiliang Cai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15324) · [PDF](https://arxiv.org/pdf/2610.15324) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **143 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs**<br><sub>Aimon Rahman, Joymallya Chakraborty, Vidit Bansal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18858) · [PDF](https://arxiv.org/pdf/2610.18858) |
| 2026-10-13 | **Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning**<br><sub>Tianhao Fu, Austin Wang, Charles Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18690) · [PDF](https://arxiv.org/pdf/2610.18690) |
| 2026-10-13 | **Two For The Price Of One: Curvature-Aware Pruning Preserves Influence Functions Too**<br><sub>Mehdi Makni, Natalia Ponomareva, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2610.18516) · [PDF](https://arxiv.org/pdf/2610.18516) |
| 2026-10-13 | **Readout Scaling Shapes Sparse Feature Recovery**<br><sub>Brain Xiao, Sarah Wilson</sub> | [arXiv](https://arxiv.org/abs/2610.18462) · [PDF](https://arxiv.org/pdf/2610.18462) |
| 2026-10-13 | **Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs**<br><sub>Peiran Yin, Hao Wu, Zihao Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18399) · [PDF](https://arxiv.org/pdf/2610.18399) · [Code](https://github.com/EIT-NLP/Bifocal) |
| 2026-10-13 | **TwinPrune: Density-Aware Two-Phase Token Pruning for Vision-Language Models**<br><sub>Kai Liu, Anqi Li, Junxian Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17530) · [PDF](https://arxiv.org/pdf/2610.17530) · [Code](https://github.com/Kai-Liu001/TwinPrune) |
| 2026-10-12 | **FoveaTree: Information-Density Trees for Query-Guided Visual Token Pruning in Video Large Language Models**<br><sub>Zihan Meng, Weidong Chen, Dexiang Hong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16744) · [PDF](https://arxiv.org/pdf/2610.16744) |
| 2026-10-12 | **When 1+1 Backfires: Rethinking Relevance-Diversity Balancing for Sample-Aware Visual Token Reduction**<br><sub>Yihang Huang, Peisong Wen, Chenhao Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16615) · [PDF](https://arxiv.org/pdf/2610.16615) |
| 2026-10-12 | **Elephant in the Fridge: Constant-Memory Frame Packing for Long Video Understanding**<br><sub>Shuo Gao, Chenhao Zheng, Zhongzheng Ren</sub> | [arXiv](https://arxiv.org/abs/2610.16118) · [PDF](https://arxiv.org/pdf/2610.16118) |
| 2026-10-11 | **Heterogeneous Structured Pruning Under Resource Constraints for Hardware-Efficient Large Language Models**<br><sub>Cameron Barker, Andreas Paraskeva, Jan N. van Rijn et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15781) · [PDF](https://arxiv.org/pdf/2610.15781) |
| 2026-10-11 | **The Fragility and Dynamics of LLM Pruning-Recovery Steps**<br><sub>Luis Frentzen Salim, Komang Rinartha, Chia-Chun Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15574) · [PDF](https://arxiv.org/pdf/2610.15574) |
| 2026-10-11 | **SARATHI: Decoupled Data-Free Probing and Adaptive Reconstruction for Structured LLM Pruning**<br><sub>Sankar Behera, Dhruv Singh, Satyadev Ahlawat et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15514) · [PDF](https://arxiv.org/pdf/2610.15514) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **331 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **GAD: Geometry Attention Distillation for Consistent Video Generation**<br><sub>Junfeng Ni, Ziyu Zhu, Fan Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18779) · [PDF](https://arxiv.org/pdf/2610.18779) |
| 2026-10-13 | **Recasting DiT for Extreme Image Compression with Hierarchical Visual Priors**<br><sub>Yunuo Chen, Jingnan Gao, Bing He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18607) · [PDF](https://arxiv.org/pdf/2610.18607) |
| 2026-10-13 | **Simplifying and Improving On-Policy Distillation for Few-Step Diffusion**<br><sub>Jiawei Zhang, Ziyu Wan, Nanye Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18472) · [PDF](https://arxiv.org/pdf/2610.18472) |
| 2026-10-13 | **LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout**<br><sub>Ziyu Zhu, Zhaoxu Sun, Fan Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18289) · [PDF](https://arxiv.org/pdf/2610.18289) · [Code](https://github.com/Fantasy-AMAP/LongForcing) |
| 2026-10-13 | **Teach Me After You Learn It: Lookahead Self-Distillation for RLVR**<br><sub>Zepeng Zhai, Meilin Chen</sub> | [arXiv](https://arxiv.org/abs/2610.18256) · [PDF](https://arxiv.org/pdf/2610.18256) |
| 2026-10-13 | **LinMorph: Learning to Morph Weights for Efficient Video DiT Linearization**<br><sub>Lingyi Long, Congyue Zhao, Xiaoou Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17914) · [PDF](https://arxiv.org/pdf/2610.17914) |
| 2026-10-13 | **DVTR-KD: Distilling Vision-Language Models via Intermediate Visual Token Reconstruction**<br><sub>Haolan Wei, Jiahui Wang, Junli Zha et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17853) · [PDF](https://arxiv.org/pdf/2610.17853) |
| 2026-10-13 | **Explore with Memory, Learn without It: In-Context Exploration and Self-Distillation for LLM Reasoning**<br><sub>Yutong Chen, Zhichao Xu, Rui Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17734) · [PDF](https://arxiv.org/pdf/2610.17734) · [Code](https://github.com/on1262/LEAF) |
| 2026-10-13 | **Facts Don&#x27;t Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation**<br><sub>Yongcan Yu, Jian Liang, Lingxiao He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17607) · [PDF](https://arxiv.org/pdf/2610.17607) · [Code](https://github.com/yuyongcan/Long-CoT-Distillation) |
| 2026-10-13 | **FlashVSR+: Efficient Video Super-Resolution via Hybrid Attention and Reward-Yield Distribution Matching**<br><sub>Ruchang Yao, Shi Guo, Junhao Zhuang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17552) · [PDF](https://arxiv.org/pdf/2610.17552) |
| 2026-10-12 | **Distilling Text LMs into Speech-to-Speech LMs by Matching Internal Text Predictions**<br><sub>Ju-Chieh Chou, Jiawei Zhou, Karen Livescu</sub> | [arXiv](https://arxiv.org/abs/2610.17461) · [PDF](https://arxiv.org/pdf/2610.17461) |
| 2026-10-12 | **World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models**<br><sub>Junyi Wu, Zekun Li, Chenhongyi Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17434) · [PDF](https://arxiv.org/pdf/2610.17434) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **97 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **Unlocking Token Rewards via Training-Free Reward Attribution**<br><sub>Sitong Wu, Haoru Tan, Bin Xia et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18704) · [PDF](https://arxiv.org/pdf/2610.18704) · [Code](https://github.com/stonewst/P2T) |
| 2026-10-13 | **LLM2R: From Large Language Models to 3D Reassemblers**<br><sub>Zhouhan Zhong, Qiuhong Shen, Xingyi Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18604) · [PDF](https://arxiv.org/pdf/2610.18604) |
| 2026-10-12 | **Monarch-Muon: Structure-Aware Muon for Fast and Memory-Efficient Pretraining**<br><sub>Alexander Miasnikov, Ruslan Kabirov, Gleb Molodtsov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17429) · [PDF](https://arxiv.org/pdf/2610.17429) |
| 2026-10-12 | **HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation**<br><sub>Tripti Shukla, Shwetha Somasundaram, Akshat Gupta et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17368) · [PDF](https://arxiv.org/pdf/2610.17368) |
| 2026-10-12 | **MLAfication: Efficiently Enabling High-Fidelity MLA for Modern LLMs**<br><sub>Zile Wang, Zhide Xie, Tao Ji</sub> | [arXiv](https://arxiv.org/abs/2610.17202) · [PDF](https://arxiv.org/pdf/2610.17202) · [Code](https://github.com/JT-Ushio/MLAfication) |
| 2026-10-12 | **Growing to See: Efficient Pretraining of Self-Supervised Vision Transformers**<br><sub>Amir Mohammad Karimi Mamaghan, Ferdinand Kapl, Andrea Dittadi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16817) · [PDF](https://arxiv.org/pdf/2610.16817) |
| 2026-10-12 | **StructZO: Structured Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning**<br><sub>Xuanlin Yang, Jia Li, Zhouchen Lin</sub> | [arXiv](https://arxiv.org/abs/2610.16451) · [PDF](https://arxiv.org/pdf/2610.16451) |
| 2026-10-11 | **Fast and Accurate: Improving Personalized LLM Performance by Semantic Concentration Inspired Workload Split between RAG and Fine-Tuning**<br><sub>Xingke Yang, Sicong Li, Lingfeng Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15921) · [PDF](https://arxiv.org/pdf/2610.15921) |
| 2026-10-11 | **Engram Injection: A Study of Temporal Validity in Parametric Language-Model Memory**<br><sub>Sam Siavoshian, Omar Ramadan, Amir K. Saeed et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15882) · [PDF](https://arxiv.org/pdf/2610.15882) |
| 2026-10-11 | **When Skills Remain But Access Fails: Factorized Skill Memory for Continual Skill Internalization**<br><sub>Haomiao Qiu, Yining Tang, Hongyi Wan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15492) · [PDF](https://arxiv.org/pdf/2610.15492) |
| 2026-10-10 | **Beyond Adjacent Layers: Graph-Guided Layer Fusion for Compressing Large Language Models**<br><sub>Muhammad Usama, Yeoreum Jung</sub> | [arXiv](https://arxiv.org/abs/2610.15159) · [PDF](https://arxiv.org/pdf/2610.15159) · [Code](https://github.com/Usama1002/fcm-layer-fusion) |
| 2026-10-10 | **Toward System One Clinical Intelligence: Parameter-Efficient Fine-Tuning and Counterfactual Explainability of Decision Foundation Models**<br><sub>S. M. Mahbub Uddin Ahmed</sub> | [arXiv](https://arxiv.org/abs/2610.15029) · [PDF](https://arxiv.org/pdf/2610.15029) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **136 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs**<br><sub>Aimon Rahman, Joymallya Chakraborty, Vidit Bansal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18858) · [PDF](https://arxiv.org/pdf/2610.18858) |
| 2026-10-13 | **MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization**<br><sub>Yangchengyu Zhou, Zhiping Wu, Runchang Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18642) · [PDF](https://arxiv.org/pdf/2610.18642) · [Code](https://github.com/RL-MIND/MultiAlloc) |
| 2026-10-13 | **SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware**<br><sub>Jieyun Deng, Keming Hu, Yanghe Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18140) · [PDF](https://arxiv.org/pdf/2610.18140) |
| 2026-10-13 | **H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression**<br><sub>Or Ronai, Vladimir Kulikov, Tomer Michaeli</sub> | [arXiv](https://arxiv.org/abs/2610.18125) · [PDF](https://arxiv.org/pdf/2610.18125) |
| 2026-10-13 | **BELT : BEhavior-Aligned Low-Rank KV Cache Compression with Learned Top-k Rank Allocation**<br><sub>Yaoyang Liu, Shuwei Shen, Jincheng Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17966) · [PDF](https://arxiv.org/pdf/2610.17966) |
| 2026-10-13 | **CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation**<br><sub>Xiaoxue Wu, Xinyu Gao, Fang Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17926) · [PDF](https://arxiv.org/pdf/2610.17926) |
| 2026-10-12 | **Budgeted KV-Cache Repair for Evolving Contexts**<br><sub>Han Yu, Wenhui Zhu, Jincheng Cao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17338) · [PDF](https://arxiv.org/pdf/2610.17338) |
| 2026-10-12 | **Think Before You Speak: Enabling Training-Free Latent Communication Between Language Models**<br><sub>Rishi Khare</sub> | [arXiv](https://arxiv.org/abs/2610.16165) · [PDF](https://arxiv.org/pdf/2610.16165) |
| 2026-10-11 | **E8 Lattice Key Quantization for Low-Bit KV-Cache Compression**<br><sub>Sasho Nedelkoski, Alexander Acker, Soeren Becker et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15384) · [PDF](https://arxiv.org/pdf/2610.15384) |
| 2026-10-11 | **TempoKV: Predictive KV Cache Quantization for Autoregressive Video Generation**<br><sub>Jiahui Hu, Weile Mo, Peiliang Cai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15324) · [PDF](https://arxiv.org/pdf/2610.15324) |
| 2026-10-10 | **DeltaNet-PC: Test-Time Memory Without Backpropagation Through Time**<br><sub>Todd Morrill, Richard Zemel</sub> | [arXiv](https://arxiv.org/abs/2610.15185) · [PDF](https://arxiv.org/pdf/2610.15185) |
| 2026-10-10 | **When Dynamic Scaling Fails: A Scale-State Feedback Governs Recurrent-State Quantization in Linear-Attention and SSM LLMs**<br><sub>Yuhang Jiang</sub> | [arXiv](https://arxiv.org/abs/2610.15139) · [PDF](https://arxiv.org/pdf/2610.15139) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **97 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models**<br><sub>Yuqi Huang, Xingyao Li, Yunlong Hou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18735) · [PDF](https://arxiv.org/pdf/2610.18735) |
| 2026-10-13 | **Compare to Correct: Pairwise-Guided Logit Adjustment for LLM Test-Time Scaling**<br><sub>Cong Hua, Qianqian Xu, Zitai Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18583) · [PDF](https://arxiv.org/pdf/2610.18583) |
| 2026-10-13 | **RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions**<br><sub>Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17867) · [PDF](https://arxiv.org/pdf/2610.17867) |
| 2026-10-13 | **Diff Diffusion: Predicting Edit Paths with Diffusion Models for Efficient Code Editing**<br><sub>Xiaolong Xu, Hao Jiang, Bo Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17831) · [PDF](https://arxiv.org/pdf/2610.17831) |
| 2026-10-12 | **SchemaWeaver: Accelerating On-Device Mobile Agentic AI via Schema-Guided Parallel LLM Decoding**<br><sub>Boyuan Yang, Wei Gao</sub> | [arXiv](https://arxiv.org/abs/2610.17436) · [PDF](https://arxiv.org/pdf/2610.17436) |
| 2026-10-12 | **PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models**<br><sub>Quentin Fruytier, Anton Xue, Sanjay Shakkottai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17375) · [PDF](https://arxiv.org/pdf/2610.17375) · [Code](https://github.com/Quentin-Fruytier/PIG-DLM-release) |
| 2026-10-12 | **Intent-Triggered Anchoring for Multi-Token Format Units in Parallel Decoding of Diffusion Language Models**<br><sub>Junhyeok Lee, Kyu Sung Choi</sub> | [arXiv](https://arxiv.org/abs/2610.16516) · [PDF](https://arxiv.org/pdf/2610.16516) |
| 2026-10-09 | **SWEAR: Section-Wise Efficient Audio Reasoning via Self-Rated Difficulty**<br><sub>Yixuan Li, Minghao Lv, Xuenan Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.13081) · [PDF](https://arxiv.org/pdf/2610.13081) |
| 2026-10-09 | **Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding**<br><sub>Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12939) · [PDF](https://arxiv.org/pdf/2610.12939) |
| 2026-10-09 | **Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training**<br><sub>Suorong Yang, Jiaxin Wang, Jiaming Su et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12933) · [PDF](https://arxiv.org/pdf/2610.12933) |
| 2026-10-08 | **Contextual Correction of Parallel Drafts for Speculative Decoding**<br><sub>Roy Eisenstadt, Harel Lidar, Tal Gonen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12570) · [PDF](https://arxiv.org/pdf/2610.12570) |
| 2026-10-08 | **When Should Agents Think? Adaptive Reasoning via Cross-Turn Estimation**<br><sub>Yiruo Cheng, Shen Huang, Xiaoshuai Song et al.</sub> | [arXiv](https://arxiv.org/abs/2610.12061) · [PDF](https://arxiv.org/pdf/2610.12061) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **162 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **Rethinking Quality in Large Language Model Routing: Security-Conditioned Model-and-Budget Selection**<br><sub>Yichi Zhang, Zhenxiang Huang, Yuyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18566) · [PDF](https://arxiv.org/pdf/2610.18566) |
| 2026-10-13 | **FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving**<br><sub>Yunfei Feng, Jingkai He, Shiqi Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18451) · [PDF](https://arxiv.org/pdf/2610.18451) |
| 2026-10-13 | **RadixFlow: Filling Execution Bubbles in Prefix-Cached Hybrid LLM Serving**<br><sub>Huihao Jing, Wenbin Hu, Shaojin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18143) · [PDF](https://arxiv.org/pdf/2610.18143) |
| 2026-10-13 | **HaloBlock: Faster and Better Decoding for Diffusion Large Language Models**<br><sub>Zhaohui Zheng, Chenhang He, Jinrui Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17948) · [PDF](https://arxiv.org/pdf/2610.17948) · [Code](https://github.com/PolyU-VCLab/HaloBlock) |
| 2026-10-13 | **Batch-Paced: Fixed-Budget Batch Decoding in Discrete Diffusion Language Models**<br><sub>Shuai Zhang, Zhanchao Zhou, Huachuan Qiu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17917) · [PDF](https://arxiv.org/pdf/2610.17917) |
| 2026-10-13 | **Quota-Based Aging for Prediction-Guided Scheduling in LLM Serving**<br><sub>Hanzhi Zhang, Anxuan Che, Hang Qi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17795) · [PDF](https://arxiv.org/pdf/2610.17795) |
| 2026-10-13 | **MemAct: Streaming Spatial Understanding with Memory and Active Exploration**<br><sub>Yuxi Wei, Wei Huang, Qirui Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17640) · [PDF](https://arxiv.org/pdf/2610.17640) |
| 2026-10-12 | **Efficient Resource-Shiftable RL Post-training with Generative Rewards**<br><sub>Yanfeng Zhao, Haoyang Li, Sheng Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16866) · [PDF](https://arxiv.org/pdf/2610.16866) |
| 2026-10-12 | **Prorsa: Unleashing the Potential of Prefill-Decode Disaggregation in Agentic Reinforcement Learning**<br><sub>Chiheng Lou, Xiangwei Deng, Bangjun Xiao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16592) · [PDF](https://arxiv.org/pdf/2610.16592) |
| 2026-10-12 | **LoopQuant: Accurate and Efficient Post-Training Quantization for Looped Transformers**<br><sub>Zhixiong Zhao, Zukang Xu, Xing Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16368) · [PDF](https://arxiv.org/pdf/2610.16368) · [Code](https://github.com/Kishon-zzx/LoopQuant%5D) |
| 2026-10-12 | **A Production-Grade, High-Efficiency Agentic RL Framework for Frontier LLMs with Validated Recipes**<br><sub>LoonSage Team, Bowei Song, Caiwei Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16352) · [PDF](https://arxiv.org/pdf/2610.16352) |
| 2026-10-11 | **Lightweight Scheduling Policies for Continuously Batched LLLM Serving Across GPU Architectures**<br><sub>Ashman Mehra, Akshan Agarwal, Aryeh Carmi</sub> | [arXiv](https://arxiv.org/abs/2610.15899) · [PDF](https://arxiv.org/pdf/2610.15899) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **80 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression**<br><sub>Or Ronai, Vladimir Kulikov, Tomer Michaeli</sub> | [arXiv](https://arxiv.org/abs/2610.18125) · [PDF](https://arxiv.org/pdf/2610.18125) |
| 2026-10-13 | **LinMorph: Learning to Morph Weights for Efficient Video DiT Linearization**<br><sub>Lingyi Long, Congyue Zhao, Xiaoou Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17914) · [PDF](https://arxiv.org/pdf/2610.17914) |
| 2026-10-12 | **PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models**<br><sub>Quentin Fruytier, Anton Xue, Sanjay Shakkottai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17375) · [PDF](https://arxiv.org/pdf/2610.17375) · [Code](https://github.com/Quentin-Fruytier/PIG-DLM-release) |
| 2026-10-12 | **MARS: Systematic Multi-Level Acceleration for World Action Models**<br><sub>Zengyuan Zuo, Yongchang Zhang, Guangyu Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17141) · [PDF](https://arxiv.org/pdf/2610.17141) · [Code](https://github.com/PKU-VaLuE-Lab/MARS) |
| 2026-10-12 | **Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration**<br><sub>Jiyue Jiang, Zhiyu Huo, Yuhan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16545) · [PDF](https://arxiv.org/pdf/2610.16545) · [Code](https://github.com/jiangjyjy/AlignCache) |
| 2026-10-12 | **Tikhonov-Stabilized Bezier Representation Forecasting for Training-free Diffusion Acceleration**<br><sub>Lei Zhu, Mujie Lin, Ruochong Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16448) · [PDF](https://arxiv.org/pdf/2610.16448) |
| 2026-10-11 | **Frequency-Step Cache: Separating Synchronization and Repair for Efficient Autoregressive Video Diffusion**<br><sub>Kerry Xu, Param Misra, Zachary Stenglein et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15922) · [PDF](https://arxiv.org/pdf/2610.15922) |
| 2026-10-11 | **TempoKV: Predictive KV Cache Quantization for Autoregressive Video Generation**<br><sub>Jiahui Hu, Weile Mo, Peiliang Cai et al.</sub> | [arXiv](https://arxiv.org/abs/2610.15324) · [PDF](https://arxiv.org/pdf/2610.15324) |
| 2026-10-10 | **LightVAE: Towards Compact and Efficient Video Autoencoders**<br><sub>Shiqiao Gu, Yang Yong, Fengjun Zhong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.14726) · [PDF](https://arxiv.org/pdf/2610.14726) · [Code](https://github.com/ModelTC/LightVAE) |
| 2026-10-10 | **PixARG: Pixel-Asynchronous Retrieval-Augmented Diffusion for Fast and Realistic Image Generation**<br><sub>Zewei Xin, Qinya Li, Chaoyue Niu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.14713) · [PDF](https://arxiv.org/pdf/2610.14713) |
| 2026-10-10 | **Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering**<br><sub>Hanxin Zhu, Jianqi Ma, Cong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.14685) · [PDF](https://arxiv.org/pdf/2610.14685) |
| 2026-10-10 | **TGuide: Faster Autoregressive Video Diffusion via Historical Trajectory Guidance**<br><sub>Zhuo Chen, Bin Zou, Fanyue Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2610.14657) · [PDF](https://arxiv.org/pdf/2610.14657) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **129 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-13 | **GAD: Geometry Attention Distillation for Consistent Video Generation**<br><sub>Junfeng Ni, Ziyu Zhu, Fan Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18779) · [PDF](https://arxiv.org/pdf/2610.18779) |
| 2026-10-13 | **Recasting DiT for Extreme Image Compression with Hierarchical Visual Priors**<br><sub>Yunuo Chen, Jingnan Gao, Bing He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18607) · [PDF](https://arxiv.org/pdf/2610.18607) |
| 2026-10-13 | **Simplifying and Improving On-Policy Distillation for Few-Step Diffusion**<br><sub>Jiawei Zhang, Ziyu Wan, Nanye Ma et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18472) · [PDF](https://arxiv.org/pdf/2610.18472) |
| 2026-10-13 | **Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs**<br><sub>Peiran Yin, Hao Wu, Zihao Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18399) · [PDF](https://arxiv.org/pdf/2610.18399) · [Code](https://github.com/EIT-NLP/Bifocal) |
| 2026-10-13 | **LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout**<br><sub>Ziyu Zhu, Zhaoxu Sun, Fan Jiang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18289) · [PDF](https://arxiv.org/pdf/2610.18289) · [Code](https://github.com/Fantasy-AMAP/LongForcing) |
| 2026-10-13 | **Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation**<br><sub>Yaoli Liu, Guo-Hua Wang, Yiyang Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.18284) · [PDF](https://arxiv.org/pdf/2610.18284) |
| 2026-10-13 | **CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation**<br><sub>Xiaoxue Wu, Xinyu Gao, Fang Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17926) · [PDF](https://arxiv.org/pdf/2610.17926) |
| 2026-10-13 | **LinMorph: Learning to Morph Weights for Efficient Video DiT Linearization**<br><sub>Lingyi Long, Congyue Zhao, Xiaoou Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17914) · [PDF](https://arxiv.org/pdf/2610.17914) |
| 2026-10-13 | **4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling**<br><sub>Jianhui Zhang, Zuyao Lin, Pengxin Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17625) · [PDF](https://arxiv.org/pdf/2610.17625) |
| 2026-10-12 | **HairFlow: Modeling 3D Hair Strands with Multi-Modal Conditioned Diffusion**<br><sub>Yating Wang, Kui Wu, Ran Yi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17348) · [PDF](https://arxiv.org/pdf/2610.17348) |
| 2026-10-12 | **Scaling Unified Multimodal Models to Long-Horizon Interleaved Generation**<br><sub>Ziqiao Peng, Yutao Cui, Wang Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.17080) · [PDF](https://arxiv.org/pdf/2610.17080) |
| 2026-10-12 | **Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration**<br><sub>Jiyue Jiang, Zhiyu Huo, Yuhan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.16545) · [PDF](https://arxiv.org/pdf/2610.16545) · [Code](https://github.com/jiangjyjy/AlignCache) |

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
