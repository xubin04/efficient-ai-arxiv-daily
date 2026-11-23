# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-23 17:09 CST** · **1924 unique papers** · Newest submission: **2026-11-20**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 311 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 274 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 586 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 206 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 306 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 190 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 329 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 151 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 262 |

## Newly indexed · 2026-11-23

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **MemOnce: A Scalable Memory Architecture for Large Language Models**<br><sub>Chang Nie, Chaoyou Fu, Songlin Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27973) · [PDF](https://arxiv.org/pdf/2611.27973) |
| 2026-11-20 | **QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers**<br><sub>Zunhai Su, Keyu Fan, Ruishan Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27901) · [PDF](https://arxiv.org/pdf/2611.27901) |
| 2026-11-20 | **Speculative Decoding Is Less Speculative Than You Think**<br><sub>Guanning Zeng, Andrea Zanette</sub> | [arXiv](https://arxiv.org/abs/2611.27891) · [PDF](https://arxiv.org/pdf/2611.27891) |
| 2026-11-20 | **FOREST: Coordinating Tree-based HBF, RRAM, and HBM for Efficient Speculative LLM Inference**<br><sub>Hao Ding, Zheng Shi, Dongxue Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27701) · [PDF](https://arxiv.org/pdf/2611.27701) |
| 2026-11-20 | **Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models**<br><sub>Nan Tang, Han-Tao Zhang, Jing-Cheng Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27645) · [PDF](https://arxiv.org/pdf/2611.27645) |
| 2026-11-20 | **Isonomy: Isolating Every Request from Timing Side Channels at Nearly Full-Sharing Throughput in Multi-Instance LLM Prefill**<br><sub>Bowen Sun, Chaowei Xiao</sub> | [arXiv](https://arxiv.org/abs/2611.27596) · [PDF](https://arxiv.org/pdf/2611.27596) |
| 2026-11-20 | **Exploring the Potential of Ultra-Low-Bit Inference on LLM Accelerators**<br><sub>Hao Wang, Yang Shi, Jiageng Shi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27561) · [PDF](https://arxiv.org/pdf/2611.27561) |
| 2026-11-20 | **Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI**<br><sub>Oliver Schön, Adrien Banse, John Lygeros et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27489) · [PDF](https://arxiv.org/pdf/2611.27489) |
| 2026-11-20 | **Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization**<br><sub>Ramneek Agnihotri, Yingte Xu, Hans Vath</sub> | [arXiv](https://arxiv.org/abs/2611.27424) · [PDF](https://arxiv.org/pdf/2611.27424) · [Code](https://github.com/LucianoXu/QuantBeyoundEfficiency) |
| 2026-11-20 | **Reasoning in Fewer Tokens: Concept-Normalized Multilingual Scratchpads and Reversible Model-Adaptive Reasoning Codes**<br><sub>Rabimba Karanjai, Suryabhan Singh Hada, Hemanth Hegadehalli Madhavarao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27326) · [PDF](https://arxiv.org/pdf/2611.27326) |
| 2026-11-20 | **Do Language Models Know Which Words Steer Their Reasoning?**<br><sub>Yanbei Jiang, Chao Lei, Jey Han Lau et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27317) · [PDF](https://arxiv.org/pdf/2611.27317) |
| 2026-11-20 | **PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation**<br><sub>Junyi He, Xu Peng, Chengming Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27266) · [PDF](https://arxiv.org/pdf/2611.27266) |
| 2026-11-20 | **Parameter-Efficient Adaptation of Qwen3-VL for Handwritten Mathematical Expression Recognition**<br><sub>Manh Tuan Ha, Xuan Bao Viet Tran, Vo Minh Dat Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27208) · [PDF](https://arxiv.org/pdf/2611.27208) |
| 2026-11-20 | **The Vulnerability Window: Decision Instability in Quantized Reward Models**<br><sub>Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav</sub> | [arXiv](https://arxiv.org/abs/2611.27155) · [PDF](https://arxiv.org/pdf/2611.27155) |
| 2026-11-20 | **When Students Fail to Learn from Teachers: Learning Dynamics of On-Policy Distillation**<br><sub>Xinnan Zhang, Zeyi Liao, Siliang Zeng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27125) · [PDF](https://arxiv.org/pdf/2611.27125) |
| 2026-11-20 | **PLoQ: A Prompt-Specific Low-Rank Basis for 4-bit Quantization of LLM Activations**<br><sub>Faraz Tahmasebi, Michael Pellauer, Hyoukjun Kwon et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27092) · [PDF](https://arxiv.org/pdf/2611.27092) |
| 2026-11-20 | **Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation**<br><sub>Yalin Yang, Xiao Huang, Yanan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27089) · [PDF](https://arxiv.org/pdf/2611.27089) |
| 2026-11-20 | **Dynamic Token Merging for Efficient Vision-Language Models**<br><sub>Chris Gu, Marco Andono Sie, Nathan Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27064) · [PDF](https://arxiv.org/pdf/2611.27064) |
| 2026-11-20 | **A Continuous Relaxation of Quantization-Aware Training**<br><sub>Kartikeya Bhardwaj, Mohammed Almousa, Chaitanya Mullapudi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27056) · [PDF](https://arxiv.org/pdf/2611.27056) |
| 2026-11-20 | **Mind the Delta: Early Pruning of RTL Variants for Agentic Hardware Optimization**<br><sub>Siyang Cai, Cangyuan Li, Haoyu Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27035) · [PDF](https://arxiv.org/pdf/2611.27035) |

[View all 30 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **311 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers**<br><sub>Zunhai Su, Keyu Fan, Ruishan Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27901) · [PDF](https://arxiv.org/pdf/2611.27901) |
| 2026-11-20 | **Exploring the Potential of Ultra-Low-Bit Inference on LLM Accelerators**<br><sub>Hao Wang, Yang Shi, Jiageng Shi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27561) · [PDF](https://arxiv.org/pdf/2611.27561) |
| 2026-11-20 | **Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization**<br><sub>Ramneek Agnihotri, Yingte Xu, Hans Vath</sub> | [arXiv](https://arxiv.org/abs/2611.27424) · [PDF](https://arxiv.org/pdf/2611.27424) · [Code](https://github.com/LucianoXu/QuantBeyoundEfficiency) |
| 2026-11-20 | **Parameter-Efficient Adaptation of Qwen3-VL for Handwritten Mathematical Expression Recognition**<br><sub>Manh Tuan Ha, Xuan Bao Viet Tran, Vo Minh Dat Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27208) · [PDF](https://arxiv.org/pdf/2611.27208) |
| 2026-11-20 | **The Vulnerability Window: Decision Instability in Quantized Reward Models**<br><sub>Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav</sub> | [arXiv](https://arxiv.org/abs/2611.27155) · [PDF](https://arxiv.org/pdf/2611.27155) |
| 2026-11-20 | **PLoQ: A Prompt-Specific Low-Rank Basis for 4-bit Quantization of LLM Activations**<br><sub>Faraz Tahmasebi, Michael Pellauer, Hyoukjun Kwon et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27092) · [PDF](https://arxiv.org/pdf/2611.27092) |
| 2026-11-20 | **A Continuous Relaxation of Quantization-Aware Training**<br><sub>Kartikeya Bhardwaj, Mohammed Almousa, Chaitanya Mullapudi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27056) · [PDF](https://arxiv.org/pdf/2611.27056) |
| 2026-11-20 | **MixFold: Sub-4-Bit Mixed-Precision LLM Inference via Output-Channel Grouping on Mobile NPUs**<br><sub>Vinnam Kim, Seong Hoon Seo, Junhan Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26976) · [PDF](https://arxiv.org/pdf/2611.26976) |
| 2026-11-19 | **CarrierKV: An Edge LLM Accelerator with Positional Carrier Decomposition for Low-Bit KV Cache**<br><sub>Junyi Luo, Xinting Jiang, Ruichen Qi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26857) · [PDF](https://arxiv.org/pdf/2611.26857) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling**<br><sub>Zechun Zhou, Zhiyong Zheng, Xiaomin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26106) · [PDF](https://arxiv.org/pdf/2611.26106) |
| 2026-11-19 | **VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin**<br><sub>Samir Khaki, Wei-Chen Wang, Song Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25717) · [PDF](https://arxiv.org/pdf/2611.25717) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **274 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers**<br><sub>Zunhai Su, Keyu Fan, Ruishan Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27901) · [PDF](https://arxiv.org/pdf/2611.27901) |
| 2026-11-20 | **Dynamic Token Merging for Efficient Vision-Language Models**<br><sub>Chris Gu, Marco Andono Sie, Nathan Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27064) · [PDF](https://arxiv.org/pdf/2611.27064) |
| 2026-11-20 | **Mind the Delta: Early Pruning of RTL Variants for Agentic Hardware Optimization**<br><sub>Siyang Cai, Cangyuan Li, Haoyu Gao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27035) · [PDF](https://arxiv.org/pdf/2611.27035) |
| 2026-11-20 | **Tokenize Moments, Not Frames: Tokenizer-Aware Budget Allocation for Training-Free Video LLM Acceleration**<br><sub>Zirui Zhao, Kai Liu, Linghe Kong</sub> | [arXiv](https://arxiv.org/abs/2611.26933) · [PDF](https://arxiv.org/pdf/2611.26933) · [Code](https://github.com/zhkandsrz/ESSENCE) |
| 2026-11-19 | **HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs**<br><sub>Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure</sub> | [arXiv](https://arxiv.org/abs/2611.26363) · [PDF](https://arxiv.org/pdf/2611.26363) · [Code](https://github.com/ambroise-b/hisa) |
| 2026-11-19 | **What Does Anti-Hallucination Training Buy? Saying Less, Cheap Pruning, and the Rest**<br><sub>Lingkai Bu, Qian Gao</sub> | [arXiv](https://arxiv.org/abs/2611.25814) · [PDF](https://arxiv.org/pdf/2611.25814) |
| 2026-11-19 | **VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin**<br><sub>Samir Khaki, Wei-Chen Wang, Song Han et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25717) · [PDF](https://arxiv.org/pdf/2611.25717) |
| 2026-11-19 | **VidToC: Rethinking Video Token Compression for Multimodal Large Language Models**<br><sub>Zihan Xiao, Boshen Xu, Pei Fu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25574) · [PDF](https://arxiv.org/pdf/2611.25574) |
| 2026-11-19 | **Query-Aware vs. Query-Agnostic Training-Free Video Token Pruning in Multimodal LLMs**<br><sub>Divya Kothandaraman, Timo Kumkel, Jaclyn Pytlarz</sub> | [arXiv](https://arxiv.org/abs/2611.25537) · [PDF](https://arxiv.org/pdf/2611.25537) |
| 2026-11-19 | **RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression**<br><sub>Payman Behnam, Elaheh Sobhani, Saad Amin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25433) · [PDF](https://arxiv.org/pdf/2611.25433) |
| 2026-11-18 | **Diffusion Models are Provably Efficient Priors for Sparse Recovery**<br><sub>Ivan Lee, Xingyu Xu, Yuejie Chi</sub> | [arXiv](https://arxiv.org/abs/2611.24602) · [PDF](https://arxiv.org/pdf/2611.24602) |
| 2026-11-18 | **Let a Small Model Read First: Faster Prefill for Long Interleaved Image-Text Inputs**<br><sub>Xiaolin Lin, Kai-Chiang Wu, Bing Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24431) · [PDF](https://arxiv.org/pdf/2611.24431) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **586 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers**<br><sub>Zunhai Su, Keyu Fan, Ruishan Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27901) · [PDF](https://arxiv.org/pdf/2611.27901) |
| 2026-11-20 | **PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation**<br><sub>Junyi He, Xu Peng, Chengming Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27266) · [PDF](https://arxiv.org/pdf/2611.27266) |
| 2026-11-20 | **When Students Fail to Learn from Teachers: Learning Dynamics of On-Policy Distillation**<br><sub>Xinnan Zhang, Zeyi Liao, Siliang Zeng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27125) · [PDF](https://arxiv.org/pdf/2611.27125) |
| 2026-11-20 | **Learning Video Foresight Reasoning from Unlabeled Videos via On-Policy Self-Distillation**<br><sub>Jingchen Sun, Jiaxing Zhang, Qingqiao Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26954) · [PDF](https://arxiv.org/pdf/2611.26954) |
| 2026-11-19 | **Posterior Matching Distillation**<br><sub>Hidir Yesiltepe, Julius Berner, Arash Vahdat et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26629) · [PDF](https://arxiv.org/pdf/2611.26629) |
| 2026-11-19 | **GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers**<br><sub>Sahibzada Allahyar, Julia White, Dhruv Atreja et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26509) · [PDF](https://arxiv.org/pdf/2611.26509) |
| 2026-11-19 | **Fast Self-Supervised Generative CT Denoising via Few-Step Sampling**<br><sub>Xingyi Yao, Zhengtao Ma, Zhennong Chen</sub> | [arXiv](https://arxiv.org/abs/2611.26370) · [PDF](https://arxiv.org/pdf/2611.26370) |
| 2026-11-19 | **Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency**<br><sub>Zhihao Hu, Jianqi Ma, Jun Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26040) · [PDF](https://arxiv.org/pdf/2611.26040) |
| 2026-11-19 | **Reinforcing Few-Step Diffusion Models via Shadow Posterior Matching**<br><sub>Jingqiao Xiu, Yicong Li</sub> | [arXiv](https://arxiv.org/abs/2611.25998) · [PDF](https://arxiv.org/pdf/2611.25998) · [Code](https://github.com/shadow-posterior/code) |
| 2026-11-19 | **TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling**<br><sub>Junchi Zhang, Zihan Gu, Jiangcan Jia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25847) · [PDF](https://arxiv.org/pdf/2611.25847) |
| 2026-11-19 | **Efficient Latent Reasoning for Vision-Language Model via Dynamics-Aware Quantization and Distillation**<br><sub>Yanjing Li, Sheng Xu, Baochang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25670) · [PDF](https://arxiv.org/pdf/2611.25670) |
| 2026-11-19 | **AesDistill: Distilling Generative Aesthetics for Image Color Enhancement**<br><sub>Chuanzhi Xu, Chengkun Yue, Huiqi Liang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25635) · [PDF](https://arxiv.org/pdf/2611.25635) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **206 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models**<br><sub>Nan Tang, Han-Tao Zhang, Jing-Cheng Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27645) · [PDF](https://arxiv.org/pdf/2611.27645) |
| 2026-11-20 | **Parameter-Efficient Adaptation of Qwen3-VL for Handwritten Mathematical Expression Recognition**<br><sub>Manh Tuan Ha, Xuan Bao Viet Tran, Vo Minh Dat Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27208) · [PDF](https://arxiv.org/pdf/2611.27208) |
| 2026-11-20 | **Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation**<br><sub>Yalin Yang, Xiao Huang, Yanan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27089) · [PDF](https://arxiv.org/pdf/2611.27089) |
| 2026-11-19 | **Rethinking Full-Weight LoRA with Domain and Task Adapter Scaling for Question Answering over Portuguese Well Drilling Reports**<br><sub>Luan B. Guerra, Diogo M. Paes, Marcelo N. Grimberg et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26833) · [PDF](https://arxiv.org/pdf/2611.26833) |
| 2026-11-19 | **Efficient and Robust Drafting with Multi-Token Prediction**<br><sub>Filippo Galgani, Ziwei Ji, Omri Homburger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25813) · [PDF](https://arxiv.org/pdf/2611.25813) |
| 2026-11-18 | **A Hybrid RAG Framework for Deceptive Review Detection: Integrating RoBERTa-LoRA, FAISS-Based Retrieval, and LLM Reasoning**<br><sub>Andrei Kostin, José Ángel Diaz-Garcia, Karel Gutiérrez-Batista</sub> | [arXiv](https://arxiv.org/abs/2611.24049) · [PDF](https://arxiv.org/pdf/2611.24049) |
| 2026-11-17 | **Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU**<br><sub>Mehmet Altan Toksöz</sub> | [arXiv](https://arxiv.org/abs/2611.23205) · [PDF](https://arxiv.org/pdf/2611.23205) |
| 2026-11-17 | **MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study**<br><sub>Nikit Srivastava, Joel Dag, René Speck et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23158) · [PDF](https://arxiv.org/pdf/2611.23158) |
| 2026-11-17 | **Efficient Self-Supervised Adaptation of 3D Abdominal Vision-Language Model for Institution-Specific HCC Classification via Full Fine-Tuning and PEFT**<br><sub>Febryan Putra Kartika, Cheng-Yu Ma, Ying-Jia Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22504) · [PDF](https://arxiv.org/pdf/2611.22504) |
| 2026-11-17 | **BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning**<br><sub>Juyoung Park, Heejun Lee</sub> | [arXiv](https://arxiv.org/abs/2611.22334) · [PDF](https://arxiv.org/pdf/2611.22334) |
| 2026-11-17 | **SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding**<br><sub>Selin Yildirim, Ali Zeyrek, Deming Chen</sub> | [arXiv](https://arxiv.org/abs/2611.22296) · [PDF](https://arxiv.org/pdf/2611.22296) |
| 2026-11-16 | **KVUse: Reusable-KV User Memory for Efficient LLM Recommenders**<br><sub>Xin Guo, Qiang Zhang, Xiang Zhou et al.</sub> | [arXiv](https://arxiv.org/abs/2611.21920) · [PDF](https://arxiv.org/pdf/2611.21920) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **306 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **MemOnce: A Scalable Memory Architecture for Large Language Models**<br><sub>Chang Nie, Chaoyou Fu, Songlin Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27973) · [PDF](https://arxiv.org/pdf/2611.27973) |
| 2026-11-20 | **QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers**<br><sub>Zunhai Su, Keyu Fan, Ruishan Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27901) · [PDF](https://arxiv.org/pdf/2611.27901) |
| 2026-11-20 | **Do Language Models Know Which Words Steer Their Reasoning?**<br><sub>Yanbei Jiang, Chao Lei, Jey Han Lau et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27317) · [PDF](https://arxiv.org/pdf/2611.27317) |
| 2026-11-20 | **Contexture: Runtime Context Eviction for High-Throughput Agent Serving**<br><sub>Colin Hong, Bryan Shan, Wei Siong Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26980) · [PDF](https://arxiv.org/pdf/2611.26980) |
| 2026-11-20 | **Run One, Get Two: Near-Free Streaming Safety Checks for Local LLMs**<br><sub>Soheil Zibakhsh, Pedram Aghazadeh, Farinaz Koushanfar</sub> | [arXiv](https://arxiv.org/abs/2611.26975) · [PDF](https://arxiv.org/pdf/2611.26975) |
| 2026-11-19 | **Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs**<br><sub>Qiang Zhou, Jianing Deng, Siyan Dong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26902) · [PDF](https://arxiv.org/pdf/2611.26902) |
| 2026-11-19 | **CarrierKV: An Edge LLM Accelerator with Positional Carrier Decomposition for Low-Bit KV Cache**<br><sub>Junyi Luo, Xinting Jiang, Ruichen Qi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26857) · [PDF](https://arxiv.org/pdf/2611.26857) |
| 2026-11-19 | **Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue**<br><sub>Rishabh Ravi, Tony Hong, Chen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26435) · [PDF](https://arxiv.org/pdf/2611.26435) |
| 2026-11-19 | **HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs**<br><sub>Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure</sub> | [arXiv](https://arxiv.org/abs/2611.26363) · [PDF](https://arxiv.org/pdf/2611.26363) · [Code](https://github.com/ambroise-b/hisa) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling**<br><sub>Zechun Zhou, Zhiyong Zheng, Xiaomin Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26106) · [PDF](https://arxiv.org/pdf/2611.26106) |
| 2026-11-19 | **FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models**<br><sub>Zekun Wang, Yizhuo Wang</sub> | [arXiv](https://arxiv.org/abs/2611.26020) · [PDF](https://arxiv.org/pdf/2611.26020) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **190 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **Speculative Decoding Is Less Speculative Than You Think**<br><sub>Guanning Zeng, Andrea Zanette</sub> | [arXiv](https://arxiv.org/abs/2611.27891) · [PDF](https://arxiv.org/pdf/2611.27891) |
| 2026-11-20 | **FOREST: Coordinating Tree-based HBF, RRAM, and HBM for Efficient Speculative LLM Inference**<br><sub>Hao Ding, Zheng Shi, Dongxue Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27701) · [PDF](https://arxiv.org/pdf/2611.27701) |
| 2026-11-20 | **Reasoning in Fewer Tokens: Concept-Normalized Multilingual Scratchpads and Reversible Model-Adaptive Reasoning Codes**<br><sub>Rabimba Karanjai, Suryabhan Singh Hada, Hemanth Hegadehalli Madhavarao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27326) · [PDF](https://arxiv.org/pdf/2611.27326) |
| 2026-11-19 | **Generalist Meets Specialists: An Evolving Multimodal Agent with Persistent Tool Orchestration for Traffic Scenario Understanding**<br><sub>Linjia Kang, Binhan Jiang, Juan Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25868) · [PDF](https://arxiv.org/pdf/2611.25868) |
| 2026-11-19 | **Efficient and Robust Drafting with Multi-Token Prediction**<br><sub>Filippo Galgani, Ziwei Ji, Omri Homburger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25813) · [PDF](https://arxiv.org/pdf/2611.25813) |
| 2026-11-19 | **Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding**<br><sub>Qishu Hu, Haozhao Wang, Zicong Hong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25436) · [PDF](https://arxiv.org/pdf/2611.25436) |
| 2026-11-18 | **ScaleDiag: Diagnosing the Limits of Test-Time Scaling in GUI Grounding**<br><sub>Chen Liu, Zhen Fang, Xin Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25297) · [PDF](https://arxiv.org/pdf/2611.25297) · [Code](https://github.com/YenanLiu/ScaleDiag) |
| 2026-11-18 | **A Verifier from the Past: Test-Time Compute for Time Series Foundation Models**<br><sub>Arjun Choudhry, Aditya Narayanan, Raghav Mallampalli et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25171) · [PDF](https://arxiv.org/pdf/2611.25171) |
| 2026-11-18 | **Test-Time Symmetrization: Scaling Laws for Model-Agnostic Learning under Structure**<br><sub>Behrooz Tahmasebi, Melanie Weber</sub> | [arXiv](https://arxiv.org/abs/2611.24032) · [PDF](https://arxiv.org/pdf/2611.24032) |
| 2026-11-18 | **NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding**<br><sub>Alagappan Valliappan, Ankit More, Dheevatsa Mudigere et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23835) · [PDF](https://arxiv.org/pdf/2611.23835) |
| 2026-11-17 | **FACT: Fixed-Budget Allocation and Cross-Step Training for Speculative Decoding**<br><sub>Hadi Fares, Mayssa Hajj Hassan, Ali Salman et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23463) · [PDF](https://arxiv.org/pdf/2611.23463) · [Code](https://github.com/mrfares11/specdec) |
| 2026-11-17 | **SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding**<br><sub>Selin Yildirim, Ali Zeyrek, Deming Chen</sub> | [arXiv](https://arxiv.org/abs/2611.22296) · [PDF](https://arxiv.org/pdf/2611.22296) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **329 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **Isonomy: Isolating Every Request from Timing Side Channels at Nearly Full-Sharing Throughput in Multi-Instance LLM Prefill**<br><sub>Bowen Sun, Chaowei Xiao</sub> | [arXiv](https://arxiv.org/abs/2611.27596) · [PDF](https://arxiv.org/pdf/2611.27596) |
| 2026-11-20 | **Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI**<br><sub>Oliver Schön, Adrien Banse, John Lygeros et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27489) · [PDF](https://arxiv.org/pdf/2611.27489) |
| 2026-11-20 | **Contexture: Runtime Context Eviction for High-Throughput Agent Serving**<br><sub>Colin Hong, Bryan Shan, Wei Siong Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26980) · [PDF](https://arxiv.org/pdf/2611.26980) |
| 2026-11-19 | **TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming**<br><sub>Jinbin Luo, Xiaozhe Yao, Shang Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26619) · [PDF](https://arxiv.org/pdf/2611.26619) |
| 2026-11-19 | **Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models**<br><sub>Chang Yang, Yao Xuan, Wendan Yan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26531) · [PDF](https://arxiv.org/pdf/2611.26531) |
| 2026-11-19 | **Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue**<br><sub>Rishabh Ravi, Tony Hong, Chen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26435) · [PDF](https://arxiv.org/pdf/2611.26435) |
| 2026-11-19 | **ChronoPatch: Black-Box Energy-Latency Attacks on Vision-Language Models**<br><sub>Jiawei Xing, Li Wang, Xiangtao Meng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26117) · [PDF](https://arxiv.org/pdf/2611.26117) |
| 2026-11-19 | **From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval for Production Content Recommendation**<br><sub>Zhixiong Hu, Meng Li, Maggie Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26096) · [PDF](https://arxiv.org/pdf/2611.26096) |
| 2026-11-19 | **DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents**<br><sub>Licheng Pan, Yuzhou Chen, Zhixuan Chu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25583) · [PDF](https://arxiv.org/pdf/2611.25583) |
| 2026-11-19 | **RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression**<br><sub>Payman Behnam, Elaheh Sobhani, Saad Amin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25433) · [PDF](https://arxiv.org/pdf/2611.25433) |
| 2026-11-18 | **TripleKV: Predict, Prefetch, Protect -- KV Cache Management for AI Agents**<br><sub>Shashwat Jaiswal, Chloe Alverti, Mengmei Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25112) · [PDF](https://arxiv.org/pdf/2611.25112) |
| 2026-11-18 | **eFAIR: Fair LLM Serving under Hourly Electricity Commitments**<br><sub>You Peng, Youhe Jiang, Chen Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24119) · [PDF](https://arxiv.org/pdf/2611.24119) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **151 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-19 | **Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling**<br><sub>Yuchen Zhou, Lili Zheng, Yuxin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26407) · [PDF](https://arxiv.org/pdf/2611.26407) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **D3-Cache: Accelerating Diffusion Models with Dynamic Mode Decomposition**<br><sub>Yanbo Li, An Xiang, Xiaoxin Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25689) · [PDF](https://arxiv.org/pdf/2611.25689) |
| 2026-11-19 | **TRAC: Efficient Diffusion Language Models for Machine Translation via Length-Aware Decoding**<br><sub>Tianyuan Li, Xihan Yang, Chenglong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25643) · [PDF](https://arxiv.org/pdf/2611.25643) |
| 2026-11-19 | **FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash**<br><sub>Yuseon Choi, Sanghyeon Park, Eunjong Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25580) · [PDF](https://arxiv.org/pdf/2611.25580) |
| 2026-11-18 | **CalibCache: Cache-to-Full Feature Dynamics Calibration for Diffusion Transformers**<br><sub>Mingyu Liang, Dingkun Xu, Jingwei Xu</sub> | [arXiv](https://arxiv.org/abs/2611.25296) · [PDF](https://arxiv.org/pdf/2611.25296) |
| 2026-11-18 | **Every Query Routes Itself: Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention**<br><sub>Zhen Huang, Shuwei Li, Ruizhe Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24479) · [PDF](https://arxiv.org/pdf/2611.24479) |
| 2026-11-18 | **Hardware Acceleration of Vision-Language-Action Models with Weight Precision Rising over the Flow Steps**<br><sub>Robin Geens, Simon Haepers, Jonas Crols et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24234) · [PDF](https://arxiv.org/pdf/2611.24234) |
| 2026-11-17 | **FastFrames: Video Generation at Interactive Latency**<br><sub>Gene Chou, Guandao Yang, Fujun Luan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) |
| 2026-11-17 | **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**<br><sub>Siyuan Wang, Haoran Li, Yi Yue et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22717) · [PDF](https://arxiv.org/pdf/2611.22717) |
| 2026-11-17 | **RISA: Recoverable Sparse Attention for Block-Diffusion Language Models**<br><sub>Xinrui Zhong, Fanjiang Ye, Yuke Wang</sub> | [arXiv](https://arxiv.org/abs/2611.22191) · [PDF](https://arxiv.org/pdf/2611.22191) |
| 2026-11-17 | **BATMoS: Budget-Aware Guidance Allocation for Efficient Video Diffusion**<br><sub>Zhixu Du, Kuo Yang, Jingwei Sun et al.</sub> | [arXiv](https://arxiv.org/abs/2611.22028) · [PDF](https://arxiv.org/pdf/2611.22028) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **262 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-20 | **Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models**<br><sub>Nan Tang, Han-Tao Zhang, Jing-Cheng Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27645) · [PDF](https://arxiv.org/pdf/2611.27645) |
| 2026-11-20 | **PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation**<br><sub>Junyi He, Xu Peng, Chengming Xu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27266) · [PDF](https://arxiv.org/pdf/2611.27266) |
| 2026-11-19 | **A High-Compression Transformer VAE for Efficient and Controllable 3D Medical Image Generation with Diffusion Transformers**<br><sub>Bo Liu, Bingliang Zhang, Yubo Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26907) · [PDF](https://arxiv.org/pdf/2611.26907) · [Code](https://github.com/OncoMMAI/brainmri-vit-vae3d) |
| 2026-11-19 | **Posterior Matching Distillation**<br><sub>Hidir Yesiltepe, Julius Berner, Arash Vahdat et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26629) · [PDF](https://arxiv.org/pdf/2611.26629) |
| 2026-11-19 | **Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware**<br><sub>Víctor Rodrigo González, Pablo M. Olmos, Ignacio Peis et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26437) · [PDF](https://arxiv.org/pdf/2611.26437) · [Code](https://github.com/deeplearningcafe/asuka-fm) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **StreamEgo: Streaming Exocentric-to-Egocentric Video Generation**<br><sub>Tianyi Xu, Boyang Lyu, Yunkai Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26165) · [PDF](https://arxiv.org/pdf/2611.26165) |
| 2026-11-19 | **Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency**<br><sub>Zhihao Hu, Jianqi Ma, Jun Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26040) · [PDF](https://arxiv.org/pdf/2611.26040) |
| 2026-11-19 | **TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling**<br><sub>Junchi Zhang, Zihan Gu, Jiangcan Jia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25847) · [PDF](https://arxiv.org/pdf/2611.25847) |
| 2026-11-19 | **FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash**<br><sub>Yuseon Choi, Sanghyeon Park, Eunjong Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25580) · [PDF](https://arxiv.org/pdf/2611.25580) |
| 2026-11-18 | **Every Query Routes Itself: Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention**<br><sub>Zhen Huang, Shuwei Li, Ruizhe Yao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24479) · [PDF](https://arxiv.org/pdf/2611.24479) |
| 2026-11-18 | **Spark-H3: Adaptive Block Sparse Attention for Video Diffusion Models**<br><sub>Zecheng Tang, Jiaye Fu, Youtian Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.24256) · [PDF](https://arxiv.org/pdf/2611.24256) |

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
