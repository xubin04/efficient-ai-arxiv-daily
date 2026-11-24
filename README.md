# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-11-24 18:59 CST** · **2000 unique papers** · Newest submission: **2026-11-23**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 318 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 286 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 607 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 213 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 323 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 196 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 341 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 160 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 282 |

## Newly indexed · 2026-11-24

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action**<br><sub>Seongchan Kim, Soowon Son, Sangoh Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31240) · [PDF](https://arxiv.org/pdf/2611.31240) |
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **Analyzing and Improving FlowMap Distillation of Autoregressive Video Models**<br><sub>Yong-Hyun Park, Guande He, Joon Hyeok Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31164) · [PDF](https://arxiv.org/pdf/2611.31164) |
| 2026-11-23 | **SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning**<br><sub>Kangping Hu, Akshay Mehra, Stephen Mussmann</sub> | [arXiv](https://arxiv.org/abs/2611.31163) · [PDF](https://arxiv.org/pdf/2611.31163) · [Code](https://github.com/ADDAPT-ML/SPROUT) |
| 2026-11-23 | **Self-Upgrading Embodied Agents**<br><sub>Jiajun Fan, Neil He, Qinglong Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31117) · [PDF](https://arxiv.org/pdf/2611.31117) |
| 2026-11-23 | **LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents**<br><sub>Tianyi Huang, Samuel Xu, Ivy Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31105) · [PDF](https://arxiv.org/pdf/2611.31105) |
| 2026-11-23 | **Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer Weight Compression**<br><sub>Anindya Roy Chowdhury, Atanu Barai, Nandakishore Santhi</sub> | [arXiv](https://arxiv.org/abs/2611.31089) · [PDF](https://arxiv.org/pdf/2611.31089) |
| 2026-11-23 | **Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching**<br><sub>Yihong Luo</sub> | [arXiv](https://arxiv.org/abs/2611.30986) · [PDF](https://arxiv.org/pdf/2611.30986) · [Code](https://github.com/Luo-Yihong/iTDM) |
| 2026-11-23 | **DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers**<br><sub>Lernie Li, Yuanliu Liu, Pengfei Xiong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30844) · [PDF](https://arxiv.org/pdf/2611.30844) |
| 2026-11-23 | **Doc-to-LoRA Analysis: Query Conditioning, Wrong Facts, and Distractor Interference**<br><sub>Jesper Derehag</sub> | [arXiv](https://arxiv.org/abs/2611.30825) · [PDF](https://arxiv.org/pdf/2611.30825) |
| 2026-11-23 | **Same Seed, Different Picture? Deciding Early at Low Resolution for Seed-Faithful Few-Step Flow Sampling**<br><sub>Huiran Duan, Weilun Feng, Yuqi Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30728) · [PDF](https://arxiv.org/pdf/2611.30728) |
| 2026-11-23 | **LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation**<br><sub>Yuxuan Jiang, Zehua Chen, Yusheng Dai et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30714) · [PDF](https://arxiv.org/pdf/2611.30714) |
| 2026-11-23 | **Speculate in the Right Order: Efficient Self-Speculative Decoding for Autoregressive Image Generation**<br><sub>Yihan Chen, Jintao Zhang, Jun Zhu</sub> | [arXiv](https://arxiv.org/abs/2611.30704) · [PDF](https://arxiv.org/pdf/2611.30704) |
| 2026-11-23 | **Uncovering the Tells: Efficient Black-Box Audits for LLM Data Contamination**<br><sub>Dominik Bernard Lau, Filip Pawlicki, Jan Dubiński et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30639) · [PDF](https://arxiv.org/pdf/2611.30639) |
| 2026-11-23 | **Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax**<br><sub>Huan Xu, Maosen Zhao, Pengtao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30587) · [PDF](https://arxiv.org/pdf/2611.30587) |
| 2026-11-23 | **Near-Far Attention: Region-Aware Sparse Retrieval for Long-Context LLM Decoding**<br><sub>YuanShuo Wang, Jianchao Tan, Lei Gong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30554) · [PDF](https://arxiv.org/pdf/2611.30554) |
| 2026-11-23 | **LiveMirror: Real-Time Diffusion Virtual Try-On on a Consumer GPU and Its Self-Supervised Adaptation to Indian Ethnic Wear**<br><sub>Jigyansha Jeevan Rout, Sukanta Kumar Sabut</sub> | [arXiv](https://arxiv.org/abs/2611.30461) · [PDF](https://arxiv.org/pdf/2611.30461) |
| 2026-11-23 | **CGSpec: Consistency-Guided Speculative Decoding with Overlap-Aware Verification Scheduling for Edge-Cloud Inference**<br><sub>Yuanbing Ouyang, Xiaoli Liu, Shirong Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30455) · [PDF](https://arxiv.org/pdf/2611.30455) |
| 2026-11-23 | **ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy**<br><sub>Hyunsu Ye, Hyunmin Choi, Jaehong Cho et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30417) · [PDF](https://arxiv.org/pdf/2611.30417) |
| 2026-11-23 | **Learning Teacher Output Preferences from Final Responses for Reasoning Distillation**<br><sub>Hongli Shen, Shaopeng Fu, Qinbo Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30338) · [PDF](https://arxiv.org/pdf/2611.30338) |

[View all 76 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **318 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer Weight Compression**<br><sub>Anindya Roy Chowdhury, Atanu Barai, Nandakishore Santhi</sub> | [arXiv](https://arxiv.org/abs/2611.31089) · [PDF](https://arxiv.org/pdf/2611.31089) |
| 2026-11-23 | **Quantization for Action, Execution for Deployment: Joint Precision and Execution Selection for World Action Models**<br><sub>Tianqi Li, Xin He, Xue Geng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30195) · [PDF](https://arxiv.org/pdf/2611.30195) |
| 2026-11-22 | **Estimating Silenced Tokens in Quantized LLMs**<br><sub>Giuseppe Pappalardo</sub> | [arXiv](https://arxiv.org/abs/2611.29536) · [PDF](https://arxiv.org/pdf/2611.29536) |
| 2026-11-22 | **Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs**<br><sub>Feng Cheng, Cong Guo, Junyao Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29497) · [PDF](https://arxiv.org/pdf/2611.29497) |
| 2026-11-22 | **BQDNA: Multi-Head Binary Spherical Quantization for Genomic Sequence Modeling**<br><sub>Xudong Wang, Siwei Cheng, Haozhe Hu</sub> | [arXiv](https://arxiv.org/abs/2611.29395) · [PDF](https://arxiv.org/pdf/2611.29395) · [Code](https://github.com/Sophie10001b/BQDNA) |
| 2026-11-21 | **SANA-Robot: Efficient World Action Model with Hybrid Memory**<br><sub>Yuyang Zhao, Zekai Li, Yicheng Pan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28943) · [PDF](https://arxiv.org/pdf/2611.28943) |
| 2026-11-20 | **Selection Policies for Equal-Byte Mixed-Precision Quantization of Small Language Models**<br><sub>Smit Anand</sub> | [arXiv](https://arxiv.org/abs/2611.28318) · [PDF](https://arxiv.org/pdf/2611.28318) |
| 2026-11-20 | **QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers**<br><sub>Zunhai Su, Keyu Fan, Ruishan Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27901) · [PDF](https://arxiv.org/pdf/2611.27901) |
| 2026-11-20 | **Exploring the Potential of Ultra-Low-Bit Inference on LLM Accelerators**<br><sub>Hao Wang, Yang Shi, Jiageng Shi et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27561) · [PDF](https://arxiv.org/pdf/2611.27561) |
| 2026-11-20 | **Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization**<br><sub>Ramneek Agnihotri, Yingte Xu, Hans Vath</sub> | [arXiv](https://arxiv.org/abs/2611.27424) · [PDF](https://arxiv.org/pdf/2611.27424) · [Code](https://github.com/LucianoXu/QuantBeyoundEfficiency) |
| 2026-11-20 | **Parameter-Efficient Adaptation of Qwen3-VL for Handwritten Mathematical Expression Recognition**<br><sub>Manh Tuan Ha, Xuan Bao Viet Tran, Vo Minh Dat Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27208) · [PDF](https://arxiv.org/pdf/2611.27208) |
| 2026-11-20 | **The Vulnerability Window: Decision Instability in Quantized Reward Models**<br><sub>Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav</sub> | [arXiv](https://arxiv.org/abs/2611.27155) · [PDF](https://arxiv.org/pdf/2611.27155) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **286 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action**<br><sub>Seongchan Kim, Soowon Son, Sangoh Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31240) · [PDF](https://arxiv.org/pdf/2611.31240) |
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **Uncovering the Tells: Efficient Black-Box Audits for LLM Data Contamination**<br><sub>Dominik Bernard Lau, Filip Pawlicki, Jan Dubiński et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30639) · [PDF](https://arxiv.org/pdf/2611.30639) |
| 2026-11-23 | **EdgeALM: An Efficient and Unified Edge Accelerator for Large Audio Language Models via Full-Stack Hardware-Software Co-Design and Agent-Driven Recursive Optimization**<br><sub>Chenglin Yang, Feifan Xu, Xingyuan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30216) · [PDF](https://arxiv.org/pdf/2611.30216) |
| 2026-11-23 | **PCC: Pivotal Channel Compensation for Layer Pruning of Large Language Models**<br><sub>Xiangqian Wang, Yucheng Zhang, Zhaohong Jia et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30183) · [PDF](https://arxiv.org/pdf/2611.30183) |
| 2026-11-22 | **Grammar Sparsity Sets How Transformers Learn Random Languages**<br><sub>Edgar Andres Hernandez Moreno, Francesco Cagnetta</sub> | [arXiv](https://arxiv.org/abs/2611.29692) · [PDF](https://arxiv.org/pdf/2611.29692) |
| 2026-11-22 | **CAR: Reducing Decoder Output Shift in Visual Token Pruning via Coverage Selection and Attention Reallocation**<br><sub>Xixi Jiang, Pingcheng Dong, Chen Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29489) · [PDF](https://arxiv.org/pdf/2611.29489) |
| 2026-11-22 | **FP-Prune: Rethinking Visual Token Pruning from an Information Gain Perspective**<br><sub>Haozhe Zhao, Junxiang Zhang, Junxin Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29327) · [PDF](https://arxiv.org/pdf/2611.29327) |
| 2026-11-22 | **RVLM: Fewer Tokens, Better Resolution Scaling, Fine-Grained Spatial Grounding**<br><sub>Savya Khosla, Chris Dongjoo Kim, Alex Schwing et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29146) · [PDF](https://arxiv.org/pdf/2611.29146) |
| 2026-11-21 | **DisSparse: Pipelined Top-$p$ Sparse Attention for Long-Context LLM Serving**<br><sub>Nurlan Nazaraliyev, Elaheh Sadredini, Nael Abu-Ghazaleh</sub> | [arXiv](https://arxiv.org/abs/2611.28522) · [PDF](https://arxiv.org/pdf/2611.28522) · [Code](https://github.com/nnurlan008/DisSparse) |
| 2026-11-20 | **Video-as-Weights: Compiling a Video Once into Parametric and Token Memory**<br><sub>Wentao Zhang, Ian Miao, Chen Qu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28221) · [PDF](https://arxiv.org/pdf/2611.28221) |
| 2026-11-20 | **QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers**<br><sub>Zunhai Su, Keyu Fan, Ruishan Guo et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27901) · [PDF](https://arxiv.org/pdf/2611.27901) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **607 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **Analyzing and Improving FlowMap Distillation of Autoregressive Video Models**<br><sub>Yong-Hyun Park, Guande He, Joon Hyeok Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31164) · [PDF](https://arxiv.org/pdf/2611.31164) |
| 2026-11-23 | **Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching**<br><sub>Yihong Luo</sub> | [arXiv](https://arxiv.org/abs/2611.30986) · [PDF](https://arxiv.org/pdf/2611.30986) · [Code](https://github.com/Luo-Yihong/iTDM) |
| 2026-11-23 | **Same Seed, Different Picture? Deciding Early at Low Resolution for Seed-Faithful Few-Step Flow Sampling**<br><sub>Huiran Duan, Weilun Feng, Yuqi Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30728) · [PDF](https://arxiv.org/pdf/2611.30728) |
| 2026-11-23 | **LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation**<br><sub>Yuxuan Jiang, Zehua Chen, Yusheng Dai et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30714) · [PDF](https://arxiv.org/pdf/2611.30714) |
| 2026-11-23 | **Learning Teacher Output Preferences from Final Responses for Reasoning Distillation**<br><sub>Hongli Shen, Shaopeng Fu, Qinbo Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30338) · [PDF](https://arxiv.org/pdf/2611.30338) |
| 2026-11-23 | **Verifiable On-Policy Distillation**<br><sub>Juntong Shi, Stefano Ermon, Jure Leskovec et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30325) · [PDF](https://arxiv.org/pdf/2611.30325) · [Code](https://github.com/juntongshi48/VOPD) |
| 2026-11-23 | **Preserve to Compress: Beyond Low-Dimensional Latents in One-Step Diffusion Codec**<br><sub>Chuqin Zhou, Xiaoyue Ling, Yuhang Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30154) · [PDF](https://arxiv.org/pdf/2611.30154) |
| 2026-11-22 | **Reasoning Beyond Imitation: Observation Conditioned Distillation for Video LLMs**<br><sub>Junzhou Chen, Jindong Wang, Gang Zhou</sub> | [arXiv](https://arxiv.org/abs/2611.29728) · [PDF](https://arxiv.org/pdf/2611.29728) |
| 2026-11-22 | **Mass Forcing: On-Policy Mass-Aware Distillation for Autoregressive Video Generation**<br><sub>Yiyu Li, Fei Wei, Yong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29618) · [PDF](https://arxiv.org/pdf/2611.29618) |
| 2026-11-22 | **Align the Pair, Not the Sample: Representation Alignment for Faster and Better One-Step Generato**<br><sub>Mingxiao Li, Xuantuo Huang, Encheng Su et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29547) · [PDF](https://arxiv.org/pdf/2611.29547) |
| 2026-11-22 | **HorizonFlow: Few-Step Video Distillation in 600 Iterations**<br><sub>Xianglong Guo, Haobo Xu, Zanyi Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29431) · [PDF](https://arxiv.org/pdf/2611.29431) · [Code](https://github.com/XIANGLONGGUO/HorizonFlow-repo) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **213 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents**<br><sub>Tianyi Huang, Samuel Xu, Ivy Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31105) · [PDF](https://arxiv.org/pdf/2611.31105) |
| 2026-11-23 | **Doc-to-LoRA Analysis: Query Conditioning, Wrong Facts, and Distractor Interference**<br><sub>Jesper Derehag</sub> | [arXiv](https://arxiv.org/abs/2611.30825) · [PDF](https://arxiv.org/pdf/2611.30825) |
| 2026-11-23 | **LiveMirror: Real-Time Diffusion Virtual Try-On on a Consumer GPU and Its Self-Supervised Adaptation to Indian Ethnic Wear**<br><sub>Jigyansha Jeevan Rout, Sukanta Kumar Sabut</sub> | [arXiv](https://arxiv.org/abs/2611.30461) · [PDF](https://arxiv.org/pdf/2611.30461) |
| 2026-11-23 | **Sparse Hodge Preference Optimization: Fine-Tuning Language Models toward Alignment beyond Transitive Preferences**<br><sub>Yiming Liu, Jianwei Ma, Zhongwei Xing et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30135) · [PDF](https://arxiv.org/pdf/2611.30135) |
| 2026-11-23 | **Parameter-Efficient Vocabulary Expansion via Cross-Lingual Embedding Alignment**<br><sub>Andrew Ivan Soegeng, Muhammad Reza Qorib, Weishi Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30123) · [PDF](https://arxiv.org/pdf/2611.30123) |
| 2026-11-21 | **Unlearning Model Identity: Ablating LoRA Weights from Question-Based Identity Tuning**<br><sub>Ming Cheung</sub> | [arXiv](https://arxiv.org/abs/2611.28650) · [PDF](https://arxiv.org/pdf/2611.28650) |
| 2026-11-20 | **Video-as-Weights: Compiling a Video Once into Parametric and Token Memory**<br><sub>Wentao Zhang, Ian Miao, Chen Qu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28221) · [PDF](https://arxiv.org/pdf/2611.28221) |
| 2026-11-20 | **Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models**<br><sub>Nan Tang, Han-Tao Zhang, Jing-Cheng Pang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27645) · [PDF](https://arxiv.org/pdf/2611.27645) |
| 2026-11-20 | **Parameter-Efficient Adaptation of Qwen3-VL for Handwritten Mathematical Expression Recognition**<br><sub>Manh Tuan Ha, Xuan Bao Viet Tran, Vo Minh Dat Nguyen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27208) · [PDF](https://arxiv.org/pdf/2611.27208) |
| 2026-11-20 | **Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation**<br><sub>Yalin Yang, Xiao Huang, Yanan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27089) · [PDF](https://arxiv.org/pdf/2611.27089) |
| 2026-11-19 | **Rethinking Full-Weight LoRA with Domain and Task Adapter Scaling for Question Answering over Portuguese Well Drilling Reports**<br><sub>Luan B. Guerra, Diogo M. Paes, Marcelo N. Grimberg et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26833) · [PDF](https://arxiv.org/pdf/2611.26833) |
| 2026-11-19 | **Efficient and Robust Drafting with Multi-Token Prediction**<br><sub>Filippo Galgani, Ziwei Ji, Omri Homburger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25813) · [PDF](https://arxiv.org/pdf/2611.25813) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **323 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents**<br><sub>Tianyi Huang, Samuel Xu, Ivy Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31105) · [PDF](https://arxiv.org/pdf/2611.31105) |
| 2026-11-23 | **Near-Far Attention: Region-Aware Sparse Retrieval for Long-Context LLM Decoding**<br><sub>YuanShuo Wang, Jianchao Tan, Lei Gong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30554) · [PDF](https://arxiv.org/pdf/2611.30554) |
| 2026-11-23 | **ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy**<br><sub>Hyunsu Ye, Hyunmin Choi, Jaehong Cho et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30417) · [PDF](https://arxiv.org/pdf/2611.30417) |
| 2026-11-23 | **When Does Optical Context Compression Pay Off? A Decode-Aware Cost Analysis of Reasoning VLMs**<br><sub>Ziqing Ge</sub> | [arXiv](https://arxiv.org/abs/2611.30130) · [PDF](https://arxiv.org/pdf/2611.30130) |
| 2026-11-22 | **Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs**<br><sub>Feng Cheng, Cong Guo, Junyao Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29497) · [PDF](https://arxiv.org/pdf/2611.29497) |
| 2026-11-22 | **HGDNA: Overlapping k-mer Tokenization for Efficient Autoregressive Genomic Language Models**<br><sub>Xudong Wang, Siwei Cheng, Haozhe Hu</sub> | [arXiv](https://arxiv.org/abs/2611.29400) · [PDF](https://arxiv.org/pdf/2611.29400) · [Code](https://github.com/Sophie10001b/HGDNA) |
| 2026-11-22 | **QASparse: Query-Adaptive Sparse Attention with Tailored Budgets and Tokens**<br><sub>Zhiyuan Chen, Zihao Yang, Quanjiang Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29280) · [PDF](https://arxiv.org/pdf/2611.29280) |
| 2026-11-21 | **RES: Accelerating Diffusion Language Models with Rolling Entropy Sampling**<br><sub>Patrick Pynadath, Nicolas Perez-Nieves, Bobak Shahriari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29066) · [PDF](https://arxiv.org/pdf/2611.29066) |
| 2026-11-21 | **SANA-Robot: Efficient World Action Model with Hybrid Memory**<br><sub>Yuyang Zhao, Zekai Li, Yicheng Pan et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28943) · [PDF](https://arxiv.org/pdf/2611.28943) |
| 2026-11-21 | **IndexerStage: Staging Indexer-K across Memory Tiers for Sparse-Attention LLM Serving**<br><sub>Xin Zhang, Weifeng Zhang, Xianyan Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28625) · [PDF](https://arxiv.org/pdf/2611.28625) |
| 2026-11-21 | **DisSparse: Pipelined Top-$p$ Sparse Attention for Long-Context LLM Serving**<br><sub>Nurlan Nazaraliyev, Elaheh Sadredini, Nael Abu-Ghazaleh</sub> | [arXiv](https://arxiv.org/abs/2611.28522) · [PDF](https://arxiv.org/pdf/2611.28522) · [Code](https://github.com/nnurlan008/DisSparse) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **196 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **Self-Upgrading Embodied Agents**<br><sub>Jiajun Fan, Neil He, Qinglong Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31117) · [PDF](https://arxiv.org/pdf/2611.31117) |
| 2026-11-23 | **Speculate in the Right Order: Efficient Self-Speculative Decoding for Autoregressive Image Generation**<br><sub>Yihan Chen, Jintao Zhang, Jun Zhu</sub> | [arXiv](https://arxiv.org/abs/2611.30704) · [PDF](https://arxiv.org/pdf/2611.30704) |
| 2026-11-23 | **Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax**<br><sub>Huan Xu, Maosen Zhao, Pengtao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30587) · [PDF](https://arxiv.org/pdf/2611.30587) |
| 2026-11-23 | **CGSpec: Consistency-Guided Speculative Decoding with Overlap-Aware Verification Scheduling for Edge-Cloud Inference**<br><sub>Yuanbing Ouyang, Xiaoli Liu, Shirong Wei et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30455) · [PDF](https://arxiv.org/pdf/2611.30455) |
| 2026-11-23 | **PackLoop: Row-Packed Self-Speculative Decoding for Looped Language Models under Concurrency**<br><sub>Runguo Li, Dezhen Lu</sub> | [arXiv](https://arxiv.org/abs/2611.30205) · [PDF](https://arxiv.org/pdf/2611.30205) |
| 2026-11-21 | **T2ISpec: Benchmarking Speculative Decoding for Text-to-Image Generation**<br><sub>Yifan Zhang, Shatong Zhu, Hui Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29029) · [PDF](https://arxiv.org/pdf/2611.29029) |
| 2026-11-20 | **Speculative Decoding Is Less Speculative Than You Think**<br><sub>Guanning Zeng, Andrea Zanette</sub> | [arXiv](https://arxiv.org/abs/2611.27891) · [PDF](https://arxiv.org/pdf/2611.27891) |
| 2026-11-20 | **FOREST: Coordinating Tree-based HBF, RRAM, and HBM for Efficient Speculative LLM Inference**<br><sub>Hao Ding, Zheng Shi, Dongxue Zhao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27701) · [PDF](https://arxiv.org/pdf/2611.27701) |
| 2026-11-20 | **Reasoning in Fewer Tokens: Concept-Normalized Multilingual Scratchpads and Reversible Model-Adaptive Reasoning Codes**<br><sub>Rabimba Karanjai, Suryabhan Singh Hada, Hemanth Hegadehalli Madhavarao et al.</sub> | [arXiv](https://arxiv.org/abs/2611.27326) · [PDF](https://arxiv.org/pdf/2611.27326) |
| 2026-11-19 | **Generalist Meets Specialists: An Evolving Multimodal Agent with Persistent Tool Orchestration for Traffic Scenario Understanding**<br><sub>Linjia Kang, Binhan Jiang, Juan Yang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25868) · [PDF](https://arxiv.org/pdf/2611.25868) |
| 2026-11-19 | **Efficient and Robust Drafting with Multi-Token Prediction**<br><sub>Filippo Galgani, Ziwei Ji, Omri Homburger et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25813) · [PDF](https://arxiv.org/pdf/2611.25813) |
| 2026-11-19 | **Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding**<br><sub>Qishu Hu, Haozhao Wang, Zicong Hong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25436) · [PDF](https://arxiv.org/pdf/2611.25436) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **341 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents**<br><sub>Tianyi Huang, Samuel Xu, Ivy Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31105) · [PDF](https://arxiv.org/pdf/2611.31105) |
| 2026-11-23 | **ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy**<br><sub>Hyunsu Ye, Hyunmin Choi, Jaehong Cho et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30417) · [PDF](https://arxiv.org/pdf/2611.30417) |
| 2026-11-23 | **EdgeALM: An Efficient and Unified Edge Accelerator for Large Audio Language Models via Full-Stack Hardware-Software Co-Design and Agent-Driven Recursive Optimization**<br><sub>Chenglin Yang, Feifan Xu, Xingyuan Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30216) · [PDF](https://arxiv.org/pdf/2611.30216) |
| 2026-11-22 | **Exact on Paper: Which LLM Serving Shortcuts Flip Graded Answers, Measured Against the Noise of Reordering the Same Requests**<br><sub>Sharven Rane</sub> | [arXiv](https://arxiv.org/abs/2611.29663) · [PDF](https://arxiv.org/pdf/2611.29663) |
| 2026-11-22 | **Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs**<br><sub>Feng Cheng, Cong Guo, Junyao Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29497) · [PDF](https://arxiv.org/pdf/2611.29497) |
| 2026-11-22 | **When Does Decomposition Help? Empirical Study on Workload-Architecture Affinity in LLM Inference Serving**<br><sub>Jihui Yang, Wentai Wu, Jiahua Huang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29104) · [PDF](https://arxiv.org/pdf/2611.29104) |
| 2026-11-21 | **Analytical Modeling and Optimal GPU Provisioning for Disaggregated LLM Inference**<br><sub>Akshat Pandey, Dominic Cheng, Sidharth Sharma et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28760) · [PDF](https://arxiv.org/pdf/2611.28760) |
| 2026-11-21 | **HiPerfCC-KVCache: Accelerating Confidential LLM Serving with Hierarchical KV Caching**<br><sub>Haoxuan Xu, Shaoyu Wang, Minghao Lin et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28702) · [PDF](https://arxiv.org/pdf/2611.28702) |
| 2026-11-21 | **The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates**<br><sub>Haoyuan Zheng, Dongting Li, Hancheng Ye et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28671) · [PDF](https://arxiv.org/pdf/2611.28671) · [Code](https://github.com/MAS-Sys-Bench/MAS-Sys) |
| 2026-11-21 | **IndexerStage: Staging Indexer-K across Memory Tiers for Sparse-Attention LLM Serving**<br><sub>Xin Zhang, Weifeng Zhang, Xianyan Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28625) · [PDF](https://arxiv.org/pdf/2611.28625) |
| 2026-11-21 | **DisSparse: Pipelined Top-$p$ Sparse Attention for Long-Context LLM Serving**<br><sub>Nurlan Nazaraliyev, Elaheh Sadredini, Nael Abu-Ghazaleh</sub> | [arXiv](https://arxiv.org/abs/2611.28522) · [PDF](https://arxiv.org/pdf/2611.28522) · [Code](https://github.com/nnurlan008/DisSparse) |
| 2026-11-21 | **Shoonya: Zero-Socket In-Process Small Language Models for Graph Databases with Schema-Epoch KV Caching, Live Catalog Logit Masking, and Verifier-Advantage Distillation**<br><sub>Madhulatha Mandarapu, Sandeep Kunkunuru</sub> | [arXiv](https://arxiv.org/abs/2611.28502) · [PDF](https://arxiv.org/pdf/2611.28502) · [Code](https://huggingface.co/VaidhyaMegha/Shoonya) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **160 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **CHIP: Contrastive Hardware-Image Projection. Can OpenAI CLIP Reconstruct Images from the CPU Computational Footprint?**<br><sub>Debayan Sengupta, Darsh Asher, Kaushal Mhapsekar et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30269) · [PDF](https://arxiv.org/pdf/2611.30269) |
| 2026-11-22 | **OnCache: Learning Dynamic Caching Schedules for Efficient Diffusion Inference**<br><sub>Zhikang Xie, Xichen Ye, Yifan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29480) · [PDF](https://arxiv.org/pdf/2611.29480) |
| 2026-11-21 | **RES: Accelerating Diffusion Language Models with Rolling Entropy Sampling**<br><sub>Patrick Pynadath, Nicolas Perez-Nieves, Bobak Shahriari et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29066) · [PDF](https://arxiv.org/pdf/2611.29066) |
| 2026-11-21 | **T2ISpec: Benchmarking Speculative Decoding for Text-to-Image Generation**<br><sub>Yifan Zhang, Shatong Zhu, Hui Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29029) · [PDF](https://arxiv.org/pdf/2611.29029) |
| 2026-11-20 | **Plan Big, Paint Small: Semantic-Aware Computation Allocation for Efficient Autoregressive Video Generation**<br><sub>Yixuan Luo, Yanjing Li</sub> | [arXiv](https://arxiv.org/abs/2611.28402) · [PDF](https://arxiv.org/pdf/2611.28402) |
| 2026-11-19 | **Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling**<br><sub>Yuchen Zhou, Lili Zheng, Yuxin Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2611.26407) · [PDF](https://arxiv.org/pdf/2611.26407) |
| 2026-11-19 | **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**<br><sub>Ryan Lucas, Petros Prastakos, Rahul Mazumder</sub> | [arXiv](https://arxiv.org/abs/2611.26334) · [PDF](https://arxiv.org/pdf/2611.26334) |
| 2026-11-19 | **D3-Cache: Accelerating Diffusion Models with Dynamic Mode Decomposition**<br><sub>Yanbo Li, An Xiang, Xiaoxin Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25689) · [PDF](https://arxiv.org/pdf/2611.25689) |
| 2026-11-19 | **TRAC: Efficient Diffusion Language Models for Machine Translation via Length-Aware Decoding**<br><sub>Tianyuan Li, Xihan Yang, Chenglong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25643) · [PDF](https://arxiv.org/pdf/2611.25643) |
| 2026-11-19 | **FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash**<br><sub>Yuseon Choi, Sanghyeon Park, Eunjong Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2611.25580) · [PDF](https://arxiv.org/pdf/2611.25580) |
| 2026-11-19 | **Choose What Returns: Object-Aware KV Memory for Selective Recall in Interactive Video Generation**<br><sub>Hyunwook Kang, Junoh Park, Hyunggyu Lim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.28137) · [PDF](https://arxiv.org/pdf/2611.28137) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **282 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-11-23 | **On-Policy Codec Distillation for Efficient All-in-One Video Generation**<br><sub>Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) |
| 2026-11-23 | **Analyzing and Improving FlowMap Distillation of Autoregressive Video Models**<br><sub>Yong-Hyun Park, Guande He, Joon Hyeok Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2611.31164) · [PDF](https://arxiv.org/pdf/2611.31164) |
| 2026-11-23 | **SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning**<br><sub>Kangping Hu, Akshay Mehra, Stephen Mussmann</sub> | [arXiv](https://arxiv.org/abs/2611.31163) · [PDF](https://arxiv.org/pdf/2611.31163) · [Code](https://github.com/ADDAPT-ML/SPROUT) |
| 2026-11-23 | **DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers**<br><sub>Lernie Li, Yuanliu Liu, Pengfei Xiong et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30844) · [PDF](https://arxiv.org/pdf/2611.30844) |
| 2026-11-23 | **Same Seed, Different Picture? Deciding Early at Low Resolution for Seed-Faithful Few-Step Flow Sampling**<br><sub>Huiran Duan, Weilun Feng, Yuqi Li et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30728) · [PDF](https://arxiv.org/pdf/2611.30728) |
| 2026-11-23 | **Speculate in the Right Order: Efficient Self-Speculative Decoding for Autoregressive Image Generation**<br><sub>Yihan Chen, Jintao Zhang, Jun Zhu</sub> | [arXiv](https://arxiv.org/abs/2611.30704) · [PDF](https://arxiv.org/pdf/2611.30704) |
| 2026-11-23 | **What Remains After Concept Erasure? Sparse Autoencoder Probes for Auditing Diffusion Models**<br><sub>Zhuan Shi, Lu Wei, Yuta Nakashima et al.</sub> | [arXiv](https://arxiv.org/abs/2611.30117) · [PDF](https://arxiv.org/pdf/2611.30117) |
| 2026-11-22 | **Mass Forcing: On-Policy Mass-Aware Distillation for Autoregressive Video Generation**<br><sub>Yiyu Li, Fei Wei, Yong Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29618) · [PDF](https://arxiv.org/pdf/2611.29618) |
| 2026-11-22 | **OnCache: Learning Dynamic Caching Schedules for Efficient Diffusion Inference**<br><sub>Zhikang Xie, Xichen Ye, Yifan Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29480) · [PDF](https://arxiv.org/pdf/2611.29480) |
| 2026-11-22 | **Seeing Through Preferences: Recovering Hidden Local Preference Neighborhoods for Text-to-Image Alignment**<br><sub>Pulkit Bansal, Vivek Srivastava, Shirish Karande</sub> | [arXiv](https://arxiv.org/abs/2611.29436) · [PDF](https://arxiv.org/pdf/2611.29436) |
| 2026-11-22 | **HorizonFlow: Few-Step Video Distillation in 600 Iterations**<br><sub>Xianglong Guo, Haobo Xu, Zanyi Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29431) · [PDF](https://arxiv.org/pdf/2611.29431) · [Code](https://github.com/XIANGLONGGUO/HorizonFlow-repo) |
| 2026-11-22 | **PINE: Point, Instance and Normal Estimation in One-Step Diffusion Model**<br><sub>Zeyu Ren, Jie Ni, Rui Qian et al.</sub> | [arXiv](https://arxiv.org/abs/2611.29389) · [PDF](https://arxiv.org/pdf/2611.29389) |

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
