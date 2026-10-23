# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-23 14:03 CST** · **1240 unique papers** · Newest submission: **2026-10-22**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 191 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 181 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 415 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 127 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 182 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 124 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 187 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 106 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 165 |

## Newly indexed · 2026-10-23

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **Low-Bit N-Gram Embeddings for Language Models**<br><sub>Stephen Chung, Wenyu Du</sub> | [arXiv](https://arxiv.org/abs/2610.31646) · [PDF](https://arxiv.org/pdf/2610.31646) |
| 2026-10-22 | **Rethinking Sequence Compression with Test-time Regression**<br><sub>Sihan Yang, Jie Huang, Hanxuan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31574) · [PDF](https://arxiv.org/pdf/2610.31574) |
| 2026-10-22 | **Drift Says When, Budget Says How Much: Rate-Controlled KV Re-selection for Long-Form Multimodal Generation**<br><sub>Bin Hu, Yingbo Xiao</sub> | [arXiv](https://arxiv.org/abs/2610.31433) · [PDF](https://arxiv.org/pdf/2610.31433) |
| 2026-10-22 | **SQuAT: Spherical Lattice Vector Quantization-Aware Training**<br><sub>Sebastian Loeschcke, Ivan Koryakovskiy, Tycho F. A. van der Ouderaa et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31412) · [PDF](https://arxiv.org/pdf/2610.31412) |
| 2026-10-22 | **Parameter-Efficient Adaptation of Large Language Models to a Low-Resource Agglutinative Language: A Corpus, Datasets, and a Reproducible Benchmark for the Bashkir Language**<br><sub>Mullosharaf K. Arabov, Svetlana S. Khaybullina</sub> | [arXiv](https://arxiv.org/abs/2610.31397) · [PDF](https://arxiv.org/pdf/2610.31397) |
| 2026-10-22 | **ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding**<br><sub>Liang He, SiYuan Ma, Qishi Zhan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31338) · [PDF](https://arxiv.org/pdf/2610.31338) |
| 2026-10-22 | **Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization**<br><sub>Jiacheng Liu, Yaxin Luo, Xiaohan Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31309) · [PDF](https://arxiv.org/pdf/2610.31309) · [Code](https://github.com/VILA-Lab/optic) |
| 2026-10-22 | **A Systematic Comparison of Search Space Complexity and Efficiency for Time-Synchronous End-to-End ASR Models**<br><sub>Simon Berger, Larissa Kleppel, Ralf Schlüter</sub> | [arXiv](https://arxiv.org/abs/2610.31259) · [PDF](https://arxiv.org/pdf/2610.31259) |
| 2026-10-22 | **GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching**<br><sub>Ariel Lapid, Yuval Haitman, Reuven Peretz et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31222) · [PDF](https://arxiv.org/pdf/2610.31222) |
| 2026-10-22 | **Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for Diffusion Language Models**<br><sub>Ofek Avivi, Eliron Rahimi, Avi Mendelson et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31198) · [PDF](https://arxiv.org/pdf/2610.31198) |
| 2026-10-22 | **SetCommit: Coordinated Token Commitments for Few-Step Diffusion Language Model Decoding**<br><sub>Yuannuo Feng, Yubing Ye, Wenshuai Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31120) · [PDF](https://arxiv.org/pdf/2610.31120) · [Code](https://github.com/Kissmetothemoon/SetCommit) |
| 2026-10-22 | **ResGVC: Residual Coding for High-fidelity Generative Video Compression**<br><sub>Ding Ding, Daowen Li, Ying Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31039) · [PDF](https://arxiv.org/pdf/2610.31039) |
| 2026-10-22 | **Low-Latency MoE Inference in Space Data Centers: A Wireless-Power-Transfer Perspective**<br><sub>Haotian Zheng, Zhanwei Wang, Kaibin Huang</sub> | [arXiv](https://arxiv.org/abs/2610.30923) · [PDF](https://arxiv.org/pdf/2610.30923) |
| 2026-10-22 | **Direct Forcing: A Single-Stage Training Recipe for Few-Step Autoregressive Text-to-Video Generation**<br><sub>Haojun Xu, Jie Huang, Xin Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30861) · [PDF](https://arxiv.org/pdf/2610.30861) |
| 2026-10-22 | **CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation**<br><sub>Lifan Jiang, Yibo Zhao, Senlin cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30854) · [PDF](https://arxiv.org/pdf/2610.30854) |
| 2026-10-22 | **Reverse-KL Policy Distillation: Statistical Guarantees and Limits**<br><sub>Haolin Liu, Chen-Yu Wei, Julian Zimmert</sub> | [arXiv](https://arxiv.org/abs/2610.30844) · [PDF](https://arxiv.org/pdf/2610.30844) |
| 2026-10-22 | **Amplifying Latency and Cost of LLM Inference via Rowhammer Attack**<br><sub>Mrityunjay Shukla, Shubham Roy, Biswabandan Panda</sub> | [arXiv](https://arxiv.org/abs/2610.30798) · [PDF](https://arxiv.org/pdf/2610.30798) |
| 2026-10-22 | **GIFT: Gradient Informed Filtering for Distillation Augmented Reasoning RL**<br><sub>Shijie Li, Yilin Gao, Tieyuan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30796) · [PDF](https://arxiv.org/pdf/2610.30796) · [Code](https://github.com/lilifree/GIFT) |
| 2026-10-22 | **Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving**<br><sub>Maharani A. P. Irawan, Kuntai Du, Jiayi Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30791) · [PDF](https://arxiv.org/pdf/2610.30791) |
| 2026-10-22 | **ProQuant: Preserving Expert Quality over Quantity in Ultra-Low-Bit Quantization of Mixture-of-Experts Models**<br><sub>Jiaqi Chen, Xianglong Yan, Chengzhu Bao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30779) · [PDF](https://arxiv.org/pdf/2610.30779) · [Code](https://github.com/ThrowBug/ProQuant.git) |

[View all 28 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **191 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **Low-Bit N-Gram Embeddings for Language Models**<br><sub>Stephen Chung, Wenyu Du</sub> | [arXiv](https://arxiv.org/abs/2610.31646) · [PDF](https://arxiv.org/pdf/2610.31646) |
| 2026-10-22 | **SQuAT: Spherical Lattice Vector Quantization-Aware Training**<br><sub>Sebastian Loeschcke, Ivan Koryakovskiy, Tycho F. A. van der Ouderaa et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31412) · [PDF](https://arxiv.org/pdf/2610.31412) |
| 2026-10-22 | **Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization**<br><sub>Jiacheng Liu, Yaxin Luo, Xiaohan Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31309) · [PDF](https://arxiv.org/pdf/2610.31309) · [Code](https://github.com/VILA-Lab/optic) |
| 2026-10-22 | **Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for Diffusion Language Models**<br><sub>Ofek Avivi, Eliron Rahimi, Avi Mendelson et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31198) · [PDF](https://arxiv.org/pdf/2610.31198) |
| 2026-10-22 | **ProQuant: Preserving Expert Quality over Quantity in Ultra-Low-Bit Quantization of Mixture-of-Experts Models**<br><sub>Jiaqi Chen, Xianglong Yan, Chengzhu Bao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30779) · [PDF](https://arxiv.org/pdf/2610.30779) · [Code](https://github.com/ThrowBug/ProQuant.git) |
| 2026-10-21 | **FIGFLEX: A Mixed-Precision FP-INT GEMM Accelerator Co-Designed with Low-Bit LLM Quantization**<br><sub>Faraz Tahmasebi, Haocheng Xu, Andrew Trauger et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30480) · [PDF](https://arxiv.org/pdf/2610.30480) |
| 2026-10-21 | **Efficient Generative Image Compression with Quantized Latents Refinement**<br><sub>Hao Cao, Yinhuan Huang, Wenqi Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29691) · [PDF](https://arxiv.org/pdf/2610.29691) |
| 2026-10-21 | **Effects of Model Scale and Quantization on Social Bias and Abstention in Question Answering**<br><sub>Kuniko Paxton, Ifeoluwa Wuraola, Dhavalkumar Thakker</sub> | [arXiv](https://arxiv.org/abs/2610.29657) · [PDF](https://arxiv.org/pdf/2610.29657) |
| 2026-10-21 | **Right On Q: Recovering Reasoning under Quantization via Self-Generated Trajectories**<br><sub>Boyuan Zheng, Jing Xiong, Chenwei Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29378) · [PDF](https://arxiv.org/pdf/2610.29378) |
| 2026-10-21 | **Compressing Onboard Language Models for Space Robots under a Behavioral-Fidelity Requirement**<br><sub>Jia Deng, Zizhe Wang, Xin Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29302) · [PDF](https://arxiv.org/pdf/2610.29302) |
| 2026-10-20 | **Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference**<br><sub>Xiuyi Qin</sub> | [arXiv](https://arxiv.org/abs/2610.28947) · [PDF](https://arxiv.org/pdf/2610.28947) |
| 2026-10-20 | **BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models**<br><sub>Ning Zhang, Shihao Wang, Jinrui Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28500) · [PDF](https://arxiv.org/pdf/2610.28500) · [Code](https://github.com/PolyU-VCLab/BitMTP) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **181 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **Rethinking Sequence Compression with Test-time Regression**<br><sub>Sihan Yang, Jie Huang, Hanxuan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31574) · [PDF](https://arxiv.org/pdf/2610.31574) |
| 2026-10-22 | **A Systematic Comparison of Search Space Complexity and Efficiency for Time-Synchronous End-to-End ASR Models**<br><sub>Simon Berger, Larissa Kleppel, Ralf Schlüter</sub> | [arXiv](https://arxiv.org/abs/2610.31259) · [PDF](https://arxiv.org/pdf/2610.31259) |
| 2026-10-22 | **Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference**<br><sub>Amirhossein Aghaei, Liangyan Li, Shiyi Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30611) · [PDF](https://arxiv.org/pdf/2610.30611) |
| 2026-10-22 | **Repair Changes Which Layers to Remove: Exact Optima for Depth Pruning of Language Models**<br><sub>Jianchang Su, Dawei Xiang, Yifan Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30552) · [PDF](https://arxiv.org/pdf/2610.30552) |
| 2026-10-21 | **Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers**<br><sub>Tianze Xia, Xiaoling Zhou, Ruya Lan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29441) · [PDF](https://arxiv.org/pdf/2610.29441) |
| 2026-10-20 | **Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference**<br><sub>Xiuyi Qin</sub> | [arXiv](https://arxiv.org/abs/2610.28947) · [PDF](https://arxiv.org/pdf/2610.28947) |
| 2026-10-20 | **Building a Nested LADDER for LLM Unstructured Post-Training Pruning**<br><sub>Nicolás Mauricio Cuadrado Ávila, Ivo Gollini Navarrete, Martin Takáč et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28773) · [PDF](https://arxiv.org/pdf/2610.28773) |
| 2026-10-20 | **GazeLens for Efficient Egocentric Video Question Answering with Simple Gaze-Driven Adaptive Token Reduction**<br><sub>Trong-Thang Pham, Anh Nguyen, Hien Van Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28502) · [PDF](https://arxiv.org/pdf/2610.28502) |
| 2026-10-20 | **Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity**<br><sub>Sahil Joshi, Prithvi Dixit, Aryan Katiyar et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28441) · [PDF](https://arxiv.org/pdf/2610.28441) · [Code](https://github.com/skylight-org/SSA-Paper-Code) |
| 2026-10-20 | **Offline Makes Online Better: Calibrated Cache Compression for Video Generation**<br><sub>Zhen Wang, Ning Lai, Qingtao Yu</sub> | [arXiv](https://arxiv.org/abs/2610.28192) · [PDF](https://arxiv.org/pdf/2610.28192) |
| 2026-10-20 | **ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models**<br><sub>Jiahui Ning, Liang Chen, Yuchen Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27913) · [PDF](https://arxiv.org/pdf/2610.27913) · [Code](https://github.com/gaffeyn03/ACE-Compression) |
| 2026-10-20 | **SliMOO: Interpretable Multi-Objective Evolutionary Search for LLM Depth Pruning**<br><sub>Guanchen Li, Yixing Xu, Xuanwu Yin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27812) · [PDF](https://arxiv.org/pdf/2610.27812) · [Code](https://github.com/AMD-AGI/SliMOO) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **415 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching**<br><sub>Ariel Lapid, Yuval Haitman, Reuven Peretz et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31222) · [PDF](https://arxiv.org/pdf/2610.31222) |
| 2026-10-22 | **SetCommit: Coordinated Token Commitments for Few-Step Diffusion Language Model Decoding**<br><sub>Yuannuo Feng, Yubing Ye, Wenshuai Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31120) · [PDF](https://arxiv.org/pdf/2610.31120) · [Code](https://github.com/Kissmetothemoon/SetCommit) |
| 2026-10-22 | **Direct Forcing: A Single-Stage Training Recipe for Few-Step Autoregressive Text-to-Video Generation**<br><sub>Haojun Xu, Jie Huang, Xin Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30861) · [PDF](https://arxiv.org/pdf/2610.30861) |
| 2026-10-22 | **Reverse-KL Policy Distillation: Statistical Guarantees and Limits**<br><sub>Haolin Liu, Chen-Yu Wei, Julian Zimmert</sub> | [arXiv](https://arxiv.org/abs/2610.30844) · [PDF](https://arxiv.org/pdf/2610.30844) |
| 2026-10-22 | **GIFT: Gradient Informed Filtering for Distillation Augmented Reasoning RL**<br><sub>Shijie Li, Yilin Gao, Tieyuan Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30796) · [PDF](https://arxiv.org/pdf/2610.30796) · [Code](https://github.com/lilifree/GIFT) |
| 2026-10-22 | **ParaLin++: Accelerating Parallel Diffusion Integrator via Intrinsic Partially Linear Structure**<br><sub>Jianrong Lu, Zhiyu Zhu, Hui Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30704) · [PDF](https://arxiv.org/pdf/2610.30704) |
| 2026-10-21 | **Self-Distilling Future Video Representations for World Action Models**<br><sub>Huiwon Jang, Suhyeok Jang, Hyeonmo Kang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30320) · [PDF](https://arxiv.org/pdf/2610.30320) |
| 2026-10-21 | **Edit, Don&#x27;t Imitate: Minimal-Edit On-Policy Distillation for Multimodal Reasoning**<br><sub>Wen Ye, Ailin Deng, Zirui Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30231) · [PDF](https://arxiv.org/pdf/2610.30231) |
| 2026-10-21 | **GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation**<br><sub>Quang Anh Kiet Tran, Nam Anh Tran, Manh Hung Trinh et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30067) · [PDF](https://arxiv.org/pdf/2610.30067) · [Code](https://github.com/Nhantran65/GoiBERT.git) |
| 2026-10-21 | **TraceForge: Distilling with Your Own Thinking**<br><sub>Yan Wang</sub> | [arXiv](https://arxiv.org/abs/2610.29680) · [PDF](https://arxiv.org/pdf/2610.29680) |
| 2026-10-21 | **AdvFidelity: Unifying Preference Alignment and Few-Step Image Generation within Reinforcement Learning**<br><sub>Sicong Kang, Fangao Zeng, Yuhan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29380) · [PDF](https://arxiv.org/pdf/2610.29380) |
| 2026-10-21 | **Seeing through Denoising: Frequency-guided One-step Denoising for Infrared Small Target Detection**<br><sub>Xuelin Qian, Zixuan Wang, Chang Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29361) · [PDF](https://arxiv.org/pdf/2610.29361) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **127 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **Parameter-Efficient Adaptation of Large Language Models to a Low-Resource Agglutinative Language: A Corpus, Datasets, and a Reproducible Benchmark for the Bashkir Language**<br><sub>Mullosharaf K. Arabov, Svetlana S. Khaybullina</sub> | [arXiv](https://arxiv.org/abs/2610.31397) · [PDF](https://arxiv.org/pdf/2610.31397) |
| 2026-10-21 | **AQL-Lite: Enabling Efficient Knowledge Acquisition for Arabic LLMs via Data-Centric Continual Pretraining**<br><sub>Houssam Eddine Boukhalfa, Mourad Bouache, Mourad Dahmane</sub> | [arXiv](https://arxiv.org/abs/2610.30344) · [PDF](https://arxiv.org/pdf/2610.30344) |
| 2026-10-21 | **Our Own Jev: Typed Decisions in One Forward Pass, from an In-House Judge to Open LoRA Models**<br><sub>Yuchuan Weng, Chi Liu, Xin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29052) · [PDF](https://arxiv.org/pdf/2610.29052) |
| 2026-10-20 | **Complexity-Aware Surgical Video Reasoning Segmentation with Digital Twin and Context Memory**<br><sub>Yiqing Shen, Mathias Unberath</sub> | [arXiv](https://arxiv.org/abs/2610.28776) · [PDF](https://arxiv.org/pdf/2610.28776) |
| 2026-10-20 | **MuPACE: Learning to Pace Muon for LoRA Fine-Tuning**<br><sub>Jan Kobiolka, Christian Frey, Josif Grabocka</sub> | [arXiv](https://arxiv.org/abs/2610.28072) · [PDF](https://arxiv.org/pdf/2610.28072) |
| 2026-10-20 | **Building Telecom Language Models with RSOD: Domain Data, Specialist Post-Training, Memory-Conscious Distillation, and Networking Evaluation**<br><sub>Anil Srirangapatna Nagesh, Nitin Gupta, Anuj Taneja et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27993) · [PDF](https://arxiv.org/pdf/2610.27993) |
| 2026-10-20 | **E8-QAT: Efficient 2-Bit Quantization-Aware Training with Implicit Lattice Codebooks**<br><sub>Xinyu Lei, Hong Huang, Jiebin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27699) · [PDF](https://arxiv.org/pdf/2610.27699) |
| 2026-10-20 | **LoRASpace: A Pool-Wide Shared Substrate for Static and Dynamic Multi-LoRA Composition**<br><sub>Thamirawaran Sathiyalogeswaran, Navindu De Silva, Chamikara Siriwardane et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27444) · [PDF](https://arxiv.org/pdf/2610.27444) · [Code](https://github.com/Thamirawaran/loraspace) |
| 2026-10-20 | **Scaling Graph Reasoning in Language Models with Learnable Graph Positional Encodings**<br><sub>Javier Porras-Valenzuela, Arush Arora, Alejandro Ribeiro</sub> | [arXiv](https://arxiv.org/abs/2610.27439) · [PDF](https://arxiv.org/pdf/2610.27439) |
| 2026-10-19 | **TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning**<br><sub>Liana Patel, Rishabh Ranjan, Ion Stoica et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26754) · [PDF](https://arxiv.org/pdf/2610.26754) · [Code](https://github.com/tokengate-models/TokenGate) |
| 2026-10-19 | **An Empirical Study of Parameter-Efficient Fine-Tuning for Mixture-of-Experts LLMs**<br><sub>Minglei Li, Peng Ye, Haonan He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26370) · [PDF](https://arxiv.org/pdf/2610.26370) |
| 2026-10-19 | **Communication-Efficient Federated Domain Generalization in Edge Networks via Dynamic Prototype Regulation**<br><sub>Yuankun Xia, Hui Wang, Ling Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25810) · [PDF](https://arxiv.org/pdf/2610.25810) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **182 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **Rethinking Sequence Compression with Test-time Regression**<br><sub>Sihan Yang, Jie Huang, Hanxuan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31574) · [PDF](https://arxiv.org/pdf/2610.31574) |
| 2026-10-22 | **Drift Says When, Budget Says How Much: Rate-Controlled KV Re-selection for Long-Form Multimodal Generation**<br><sub>Bin Hu, Yingbo Xiao</sub> | [arXiv](https://arxiv.org/abs/2610.31433) · [PDF](https://arxiv.org/pdf/2610.31433) |
| 2026-10-22 | **Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization**<br><sub>Jiacheng Liu, Yaxin Luo, Xiaohan Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31309) · [PDF](https://arxiv.org/pdf/2610.31309) · [Code](https://github.com/VILA-Lab/optic) |
| 2026-10-22 | **Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving**<br><sub>Maharani A. P. Irawan, Kuntai Du, Jiayi Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30791) · [PDF](https://arxiv.org/pdf/2610.30791) |
| 2026-10-21 | **HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference**<br><sub>Junhyeok Park, Jungeun Yoon, Kyungmin Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29873) · [PDF](https://arxiv.org/pdf/2610.29873) |
| 2026-10-21 | **UlaCache: Unified Logical Addressing for Sparse LLM Serving**<br><sub>Isaac Zhu, Alan Cao, Hugh Yin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29820) · [PDF](https://arxiv.org/pdf/2610.29820) |
| 2026-10-21 | **MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs**<br><sub>Minsang Kim, Seungjun Baek</sub> | [arXiv](https://arxiv.org/abs/2610.30206) · [PDF](https://arxiv.org/pdf/2610.30206) |
| 2026-10-21 | **RISK-KV: Quality-Aware Selective KV Cache Reconstruction for Distributed LLM Inference**<br><sub>Wang Yuekai</sub> | [arXiv](https://arxiv.org/abs/2610.29544) · [PDF](https://arxiv.org/pdf/2610.29544) |
| 2026-10-21 | **Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers**<br><sub>Tianze Xia, Xiaoling Zhou, Ruya Lan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29441) · [PDF](https://arxiv.org/pdf/2610.29441) |
| 2026-10-20 | **Cache Engineering for Agents**<br><sub>Tianyu Fu, Ruoxi Wang, Zihan Min et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28577) · [PDF](https://arxiv.org/pdf/2610.28577) · [Code](https://github.com/thu-nics/AKV) |
| 2026-10-20 | **Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity**<br><sub>Sahil Joshi, Prithvi Dixit, Aryan Katiyar et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28441) · [PDF](https://arxiv.org/pdf/2610.28441) · [Code](https://github.com/skylight-org/SSA-Paper-Code) |
| 2026-10-20 | **Offline Makes Online Better: Calibrated Cache Compression for Video Generation**<br><sub>Zhen Wang, Ning Lai, Qingtao Yu</sub> | [arXiv](https://arxiv.org/abs/2610.28192) · [PDF](https://arxiv.org/pdf/2610.28192) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **124 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding**<br><sub>Liang He, SiYuan Ma, Qishi Zhan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31338) · [PDF](https://arxiv.org/pdf/2610.31338) |
| 2026-10-21 | **UlaCache: Unified Logical Addressing for Sparse LLM Serving**<br><sub>Isaac Zhu, Alan Cao, Hugh Yin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29820) · [PDF](https://arxiv.org/pdf/2610.29820) |
| 2026-10-21 | **RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding**<br><sub>Mingkang Liu, Weiming Meng, Peipei Jiao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29527) · [PDF](https://arxiv.org/pdf/2610.29527) |
| 2026-10-21 | **Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding**<br><sub>Jungseob Lee, Hogun Seong, Euijun Choi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29013) · [PDF](https://arxiv.org/pdf/2610.29013) · [Code](https://github.com/js-lee-AI/TargetRegeneration) |
| 2026-10-19 | **DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding**<br><sub>Shreyas Kulkarni, Uttam Gurram, Madhav Kanda et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27379) · [PDF](https://arxiv.org/pdf/2610.27379) |
| 2026-10-19 | **TEX: Test-Time Scaling Testing Agents via Execution-based Cross-Validation**<br><sub>Akash Gokul, Srijan Bansal, Yingbo Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27290) · [PDF](https://arxiv.org/pdf/2610.27290) |
| 2026-10-19 | **CALM: Consistency-Aware Logit Masking in Decoding Space for Mitigating Overthinking of Large Reasoning Models**<br><sub>Shengjing Liu, Feiyang Li, Yuxuan Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25908) · [PDF](https://arxiv.org/pdf/2610.25908) |
| 2026-10-19 | **Think, Compress, Answer: Reinforcement Learning for Multimodal Grounding via Reasoning Compression**<br><sub>Jinbae Seo, Hyeongjun Kwon, Jiyoung Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25640) · [PDF](https://arxiv.org/pdf/2610.25640) |
| 2026-10-18 | **ATEST: Adaptive Resource-Aware Test-Time Scaling for LLM Inference**<br><sub>Mobina Kashaniyan, Ali Jannesari</sub> | [arXiv](https://arxiv.org/abs/2610.25519) · [PDF](https://arxiv.org/pdf/2610.25519) |
| 2026-10-18 | **Test-Time Scaling of Text-to-Image Flow Matching Models with Noise-Rejuvenated Sequential Monte Carlo**<br><sub>Wenyi Lian, Zheng Zhao, Thomas B. Sch{ö}n</sub> | [arXiv](https://arxiv.org/abs/2610.25479) · [PDF](https://arxiv.org/pdf/2610.25479) · [Code](https://github.com/shermanlian/NR-SMC) |
| 2026-10-18 | **GeoART: Geometry-Aware Refinement via Test-Time Scaling for Camera-Conditioned Video Diffusion**<br><sub>Liudi Yang, Ziyuan Liu</sub> | [arXiv](https://arxiv.org/abs/2610.25273) · [PDF](https://arxiv.org/pdf/2610.25273) |
| 2026-10-18 | **BatchParScale: Sparse Batch-Mixing for Sequence Models**<br><sub>Hans Peter Lyngsøe Raaschou-jensen, M. Onurcan Kaya, Desmond Elliott</sub> | [arXiv](https://arxiv.org/abs/2610.25254) · [PDF](https://arxiv.org/pdf/2610.25254) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **187 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **Low-Latency MoE Inference in Space Data Centers: A Wireless-Power-Transfer Perspective**<br><sub>Haotian Zheng, Zhanwei Wang, Kaibin Huang</sub> | [arXiv](https://arxiv.org/abs/2610.30923) · [PDF](https://arxiv.org/pdf/2610.30923) |
| 2026-10-22 | **Amplifying Latency and Cost of LLM Inference via Rowhammer Attack**<br><sub>Mrityunjay Shukla, Shubham Roy, Biswabandan Panda</sub> | [arXiv](https://arxiv.org/abs/2610.30798) · [PDF](https://arxiv.org/pdf/2610.30798) |
| 2026-10-22 | **Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving**<br><sub>Maharani A. P. Irawan, Kuntai Du, Jiayi Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30791) · [PDF](https://arxiv.org/pdf/2610.30791) |
| 2026-10-21 | **HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference**<br><sub>Junhyeok Park, Jungeun Yoon, Kyungmin Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29873) · [PDF](https://arxiv.org/pdf/2610.29873) |
| 2026-10-21 | **UlaCache: Unified Logical Addressing for Sparse LLM Serving**<br><sub>Isaac Zhu, Alan Cao, Hugh Yin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29820) · [PDF](https://arxiv.org/pdf/2610.29820) |
| 2026-10-20 | **Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference**<br><sub>Xiuyi Qin</sub> | [arXiv](https://arxiv.org/abs/2610.28947) · [PDF](https://arxiv.org/pdf/2610.28947) |
| 2026-10-20 | **Cache Engineering for Agents**<br><sub>Tianyu Fu, Ruoxi Wang, Zihan Min et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28577) · [PDF](https://arxiv.org/pdf/2610.28577) · [Code](https://github.com/thu-nics/AKV) |
| 2026-10-20 | **Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity**<br><sub>Sahil Joshi, Prithvi Dixit, Aryan Katiyar et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28441) · [PDF](https://arxiv.org/pdf/2610.28441) · [Code](https://github.com/skylight-org/SSA-Paper-Code) |
| 2026-10-19 | **A Hybrid GPU and Processing-Near-Memory Architecture with Shared DRAM for Efficient Prefill-Decode Disaggregation**<br><sub>Sanghyeok Han, Inseong Choi, Byungkuk Yoon et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26131) · [PDF](https://arxiv.org/pdf/2610.26131) |
| 2026-10-19 | **3D-MoE: Complementarity-Guided Hardware-Software Co-Design for MoE Decode on 3D-Stacked NMP**<br><sub>Yudong Pan, Lian Liu, Shixin Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26991) · [PDF](https://arxiv.org/pdf/2610.26991) |
| 2026-10-18 | **From Label Priors to Task Evidence: Efficient Long-Video Frame Selection via Bayesian GRPO**<br><sub>Shuochen Chang, Bingjie Gao, Qingyang Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.25418) · [PDF](https://arxiv.org/pdf/2610.25418) |
| 2026-10-17 | **FlowMaker: From Tasks to Cost-Efficient Generative AI Workflow Deployments**<br><sub>Dimitrios Liakopoulos, Prasoon Sinha, Neeraja J. Yadwadkar</sub> | [arXiv](https://arxiv.org/abs/2610.24861) · [PDF](https://arxiv.org/pdf/2610.24861) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **106 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation**<br><sub>Lifan Jiang, Yibo Zhao, Senlin cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30854) · [PDF](https://arxiv.org/pdf/2610.30854) |
| 2026-10-22 | **ParaLin++: Accelerating Parallel Diffusion Integrator via Intrinsic Partially Linear Structure**<br><sub>Jianrong Lu, Zhiyu Zhu, Hui Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30704) · [PDF](https://arxiv.org/pdf/2610.30704) |
| 2026-10-21 | **SAKURA: Serving Attention Key-Value State Under Rate Adaptation for Private Image Editing on Phones**<br><sub>Shuncheng Jie, Desen Sun, Ri Hong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29733) · [PDF](https://arxiv.org/pdf/2610.29733) |
| 2026-10-20 | **DiffResearch: Accelerating Deep Research with Diffusion Language Models**<br><sub>Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov et al.</sub> | [arXiv](https://arxiv.org/abs/2610.28909) · [PDF](https://arxiv.org/pdf/2610.28909) |
| 2026-10-20 | **Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks**<br><sub>Ivan Listopadov, Maksim Nakhodnov, Aibek Alanov</sub> | [arXiv](https://arxiv.org/abs/2610.28889) · [PDF](https://arxiv.org/pdf/2610.28889) |
| 2026-10-20 | **TeCoP: Accelerating Diffusion Large Language Model Decoding via Tentative Context Pipelining**<br><sub>Jui-Chien Tsou, Hsuan-Chi Liu, Wei-Chin Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27583) · [PDF](https://arxiv.org/pdf/2610.27583) |
| 2026-10-19 | **DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding**<br><sub>Shreyas Kulkarni, Uttam Gurram, Madhav Kanda et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27379) · [PDF](https://arxiv.org/pdf/2610.27379) |
| 2026-10-19 | **SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration**<br><sub>Javad Rajabi, Hakki Can Karaimer, David B. Lindell et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26837) · [PDF](https://arxiv.org/pdf/2610.26837) |
| 2026-10-19 | **ReAnchor: Reusing Rejected Verifier States for Diffusion Drafting**<br><sub>Sanghyun Lee, Wonjin Nam, Seungho Jang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26531) · [PDF](https://arxiv.org/pdf/2610.26531) |
| 2026-10-19 | **Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion**<br><sub>Yuanyu He, Zhuokun Chen, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26262) · [PDF](https://arxiv.org/pdf/2610.26262) |
| 2026-10-19 | **RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion**<br><sub>Tiange Xu, Kai Liu, Linghe Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26244) · [PDF](https://arxiv.org/pdf/2610.26244) · [Code](https://github.com/lyraxtg/RECAP) |
| 2026-10-19 | **TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation**<br><sub>Jia Li, Xurui Peng, Haowei Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26165) · [PDF](https://arxiv.org/pdf/2610.26165) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **165 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-22 | **ResGVC: Residual Coding for High-fidelity Generative Video Compression**<br><sub>Ding Ding, Daowen Li, Ying Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.31039) · [PDF](https://arxiv.org/pdf/2610.31039) |
| 2026-10-22 | **Direct Forcing: A Single-Stage Training Recipe for Few-Step Autoregressive Text-to-Video Generation**<br><sub>Haojun Xu, Jie Huang, Xin Lu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30861) · [PDF](https://arxiv.org/pdf/2610.30861) |
| 2026-10-21 | **Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers**<br><sub>Tianze Xia, Xiaoling Zhou, Ruya Lan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29441) · [PDF](https://arxiv.org/pdf/2610.29441) |
| 2026-10-21 | **AdvFidelity: Unifying Preference Alignment and Few-Step Image Generation within Reinforcement Learning**<br><sub>Sicong Kang, Fangao Zeng, Yuhan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29380) · [PDF](https://arxiv.org/pdf/2610.29380) |
| 2026-10-20 | **Offline Makes Online Better: Calibrated Cache Compression for Video Generation**<br><sub>Zhen Wang, Ning Lai, Qingtao Yu</sub> | [arXiv](https://arxiv.org/abs/2610.28192) · [PDF](https://arxiv.org/pdf/2610.28192) |
| 2026-10-20 | **LaLa-World: Scaling Latent World Models with Natural Language Actions**<br><sub>Junha Song, Geonmo Gu, Jeongeun Park et al.</sub> | [arXiv](https://arxiv.org/abs/2610.27851) · [PDF](https://arxiv.org/pdf/2610.27851) · [Code](https://github.com/junha1125/LaLa-World) |
| 2026-10-19 | **PRIMFLOW: Learning Trajectory Primitives for Few-Step Distillation**<br><sub>Hongyi Fang, Benjia Zhou</sub> | [arXiv](https://arxiv.org/abs/2610.27146) · [PDF](https://arxiv.org/pdf/2610.27146) |
| 2026-10-19 | **SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration**<br><sub>Javad Rajabi, Hakki Can Karaimer, David B. Lindell et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26837) · [PDF](https://arxiv.org/pdf/2610.26837) |
| 2026-10-19 | **Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion**<br><sub>Yuanyu He, Zhuokun Chen, Yefei He et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26262) · [PDF](https://arxiv.org/pdf/2610.26262) |
| 2026-10-19 | **RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion**<br><sub>Tiange Xu, Kai Liu, Linghe Kong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26244) · [PDF](https://arxiv.org/pdf/2610.26244) · [Code](https://github.com/lyraxtg/RECAP) |
| 2026-10-19 | **TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation**<br><sub>Jia Li, Xurui Peng, Haowei Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26165) · [PDF](https://arxiv.org/pdf/2610.26165) |
| 2026-10-19 | **TamedFlow: Trajectory-Aware Distillation for Teacher-Assisted Diffusion Sampling**<br><sub>Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.26025) · [PDF](https://arxiv.org/pdf/2610.26025) |

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
