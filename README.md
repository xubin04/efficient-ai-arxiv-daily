# ⚡ Efficient AI · arXiv Daily

**Efficient LLMs · Efficient Visual Generation**

自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。

[![Daily update](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/xubin04/efficient-ai-arxiv-daily/actions/workflows/daily.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)

**[Browse & search papers ↗](https://xubin04.github.io/efficient-ai-arxiv-daily/)** · [Atom feed](https://xubin04.github.io/efficient-ai-arxiv-daily/feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)

Last successful scan: **2026-10-30 15:12 CST** · **1377 unique papers** · Newest submission: **2026-10-29**

> Dates below are original arXiv submission dates. The scan time is shown separately. A paper can belong to multiple topics; topic counts overlap.

## Topics

| Topic | Scope | Papers |
|:---|:---|---:|
| [Quantization & Low Precision](#quantization) | 量化、低比特推理与低精度训练 | 210 |
| [Pruning & Sparsity](#pruning) | 模型剪枝、结构化稀疏与 Token 压缩 | 203 |
| [Distillation & Few-Step Generation](#distillation) | 知识蒸馏、分布匹配与少步/单步生成 | 453 |
| [Efficient Training & Fine-Tuning](#efficient-training) | LoRA/PEFT、显存优化与高效训练 | 140 |
| [Efficient Attention & KV Cache](#attention-kv-cache) | 高效 Attention、长上下文与 KV Cache 压缩 | 197 |
| [Speculative Decoding & Efficient Reasoning](#decoding-reasoning) | 推测解码、并行解码与推理预算优化 | 133 |
| [LLM Serving & Systems](#llm-systems) | LLM 推理服务、调度、卸载与分布式系统 | 217 |
| [Diffusion Caching & Acceleration](#diffusion-acceleration) | 扩散模型/DiT 的特征缓存、复用与采样加速 | 116 |
| [Efficient Image & Video Generation](#visual-generation) | 图像/视频生成的计算、显存与延迟优化 | 188 |

## Newly indexed · 2026-10-30

These papers were first added to this repository today. The initial import includes older papers within the backfill window.

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-29 | **L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory**<br><sub>Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40614) · [PDF](https://arxiv.org/pdf/2610.40614) |
| 2026-10-29 | **Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation**<br><sub>Yifu Luo, Chuang Ma, Zeyu Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40574) · [PDF](https://arxiv.org/pdf/2610.40574) · [Code](https://github.com/xingzhejun/MTA-OPSD) |
| 2026-10-29 | **LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation**<br><sub>Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40495) · [PDF](https://arxiv.org/pdf/2610.40495) |
| 2026-10-29 | **A Unified Hessian-Guided Framework for Post-Training Quantization**<br><sub>Mads Toftrup, Marco Federici, Boris van Breugel et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40345) · [PDF](https://arxiv.org/pdf/2610.40345) |
| 2026-10-29 | **Wizard: Manipulate Any World in Real Time via Agentic Control**<br><sub>Yuzhe Wu, Zijun Lin, Yeying Jin</sub> | [arXiv](https://arxiv.org/abs/2610.40339) · [PDF](https://arxiv.org/pdf/2610.40339) |
| 2026-10-29 | **Rimuru: Unified Memory Management for Modern LLM Serving via Elastic Expert Offloading**<br><sub>Zhiyuan Fang, Dingyang Li, Jianfeng Zhong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40305) · [PDF](https://arxiv.org/pdf/2610.40305) |
| 2026-10-29 | **DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving**<br><sub>Yishuo Yuan, Shaoyu Yang, Chunrong Fang</sub> | [arXiv](https://arxiv.org/abs/2610.40292) · [PDF](https://arxiv.org/pdf/2610.40292) |
| 2026-10-29 | **Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets**<br><sub>Bole Ma, Ayesha Afzal, Jan Eitzinger et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40287) · [PDF](https://arxiv.org/pdf/2610.40287) |
| 2026-10-29 | **One Vector or Many? Clustered Optimal-Transport Steering under Quantization**<br><sub>Illia Makarov</sub> | [arXiv](https://arxiv.org/abs/2610.40055) · [PDF](https://arxiv.org/pdf/2610.40055) |
| 2026-10-29 | **NORmal: Architecting 3D Ferroelectric NOR Flash as Main Memory -- From Co-Fabricated BEOL Arrays to 200B-Class Multi-Agent LLMs in a Smartphone**<br><sub>Zhuoran Li, Chen Gu, Zhuohang Bian et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40000) · [PDF](https://arxiv.org/pdf/2610.40000) |
| 2026-10-29 | **UniRA: Unified Representation Alignment and Auto-Encoding for Efficient Diffusion Generation**<br><sub>An Lanji, Dawei Liu, Jin Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39948) · [PDF](https://arxiv.org/pdf/2610.39948) |
| 2026-10-29 | **sDMD: Sinkhorn Distribution Matching Distillation**<br><sub>Jaihoon Kim, Lingxiao Li, Soshi Shimada et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39889) · [PDF](https://arxiv.org/pdf/2610.39889) |
| 2026-10-29 | **Turing LLM Post-Training: Calibrated Distillation and Efficient Dynamic-MoE Execution**<br><sub>Yue He, Jiahui Hu, Shaman Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39876) · [PDF](https://arxiv.org/pdf/2610.39876) |
| 2026-10-29 | **KV Cache Quantization for Diffusion Language Models**<br><sub>Yan Tai, Yunan Ding, Guangzhao Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) |
| 2026-10-29 | **DWISE: Denoising Workload-Informed Scheduling Engine**<br><sub>Lie Li, Wen Li, Junxiao Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39852) · [PDF](https://arxiv.org/pdf/2610.39852) |
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-29 | **FlexTry-On: A Time-Efficient Framework for Multi-Scenario Virtual Try-on**<br><sub>Phuong Dam, Quyen Nguyen Duc, Son Hoang Minh et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39646) · [PDF](https://arxiv.org/pdf/2610.39646) |
| 2026-10-29 | **Intrinsic Distribution Matching**<br><sub>Deyuan Liu, Yansen Han, Kaiwen Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39633) · [PDF](https://arxiv.org/pdf/2610.39633) · [Code](https://github.com/inclusionAI/IDM) |
| 2026-10-29 | **Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference**<br><sub>Wenjie Huang, Jun Zhang, Hongyaoxing Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39562) · [PDF](https://arxiv.org/pdf/2610.39562) |
| 2026-10-29 | **ROAD: Modern Adversarial Training for Simple One-Step Distillation at Scale**<br><sub>Xiaoou Li, Shan You, Tao Huang</sub> | [arXiv](https://arxiv.org/abs/2610.39539) · [PDF](https://arxiv.org/pdf/2610.39539) |

[View all 44 newly indexed papers](https://xubin04.github.io/efficient-ai-arxiv-daily/?new=1).

<a id="quantization"></a>

## Quantization & Low Precision

量化、低比特推理与低精度训练 · **210 papers** · [Full archive](papers/quantization.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-29 | **A Unified Hessian-Guided Framework for Post-Training Quantization**<br><sub>Mads Toftrup, Marco Federici, Boris van Breugel et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40345) · [PDF](https://arxiv.org/pdf/2610.40345) |
| 2026-10-29 | **One Vector or Many? Clustered Optimal-Transport Steering under Quantization**<br><sub>Illia Makarov</sub> | [arXiv](https://arxiv.org/abs/2610.40055) · [PDF](https://arxiv.org/pdf/2610.40055) |
| 2026-10-29 | **KV Cache Quantization for Diffusion Language Models**<br><sub>Yan Tai, Yunan Ding, Guangzhao Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) |
| 2026-10-29 | **LinQuant: Functional Invariances for Low-Precision Linear Recurrences**<br><sub>Neehal Tumma, Philipp Nazari, Rohan Cherukuri et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39418) · [PDF](https://arxiv.org/pdf/2610.39418) · [Code](https://github.com/ntumm120/LinQuant) |
| 2026-10-29 | **Accuracy is not compatibility: two Evo 2 checkpoints hinge on one FP8 matrix multiplication**<br><sub>Xun Ding, Ziyuan Qin</sub> | [arXiv](https://arxiv.org/abs/2610.39415) · [PDF](https://arxiv.org/pdf/2610.39415) · [Code](https://github.com/astding/mmaemu) |
| 2026-10-28 | **The Role of Quantization in Loss Spikes**<br><sub>Zaiqian Chen, Aditya Somasundaram, Sophie Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38277) · [PDF](https://arxiv.org/pdf/2610.38277) |
| 2026-10-28 | **GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices**<br><sub>Yipin Guo, Arun M George, Siddharth Joshi</sub> | [arXiv](https://arxiv.org/abs/2610.38210) · [PDF](https://arxiv.org/pdf/2610.38210) |
| 2026-10-27 | **CoS-VQ: Coordinated Shared-Scale Vector Quantization for Large Language Models**<br><sub>Zukang Xu, Zhixiong Zhao, Xing Hu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37336) · [PDF](https://arxiv.org/pdf/2610.37336) · [Code](https://github.com/xzktx003/Cos_VQ) |
| 2026-10-27 | **Efficient Quantization Training with Stochastic Rounding via Structured Subspace Randomness**<br><sub>Zeyu Wang, Yiheng Duan, Tao Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36587) · [PDF](https://arxiv.org/pdf/2610.36587) |
| 2026-10-26 | **Training-Free Inference Acceleration for Video Large Language Models: Methods, Trade-offs, and Evaluation**<br><sub>Yuqi Li, Chuanyue Yan, Neil Rodrigues et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36327) · [PDF](https://arxiv.org/pdf/2610.36327) |
| 2026-10-26 | **Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs**<br><sub>Tianqi Chen, Xunchao Li, Linchuan Xie et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35985) · [PDF](https://arxiv.org/pdf/2610.35985) |
| 2026-10-26 | **Transporting Quantiles to Codebook: Scalable Vector Quantization without Codebook Collapse**<br><sub>Yuwei Zeng, Zekun Shi</sub> | [arXiv](https://arxiv.org/abs/2610.34828) · [PDF](https://arxiv.org/pdf/2610.34828) |

<a id="pruning"></a>

## Pruning & Sparsity

模型剪枝、结构化稀疏与 Token 压缩 · **203 papers** · [Full archive](papers/pruning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-29 | **Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference**<br><sub>Wenjie Huang, Jun Zhang, Hongyaoxing Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39562) · [PDF](https://arxiv.org/pdf/2610.39562) |
| 2026-10-29 | **Efficient Covariance-Aware Vicinal Latent Diffusion for Continuous Conditional Image Generation**<br><sub>Xin Ding, Shuo Huang, Zhenglong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39277) · [PDF](https://arxiv.org/pdf/2610.39277) |
| 2026-10-28 | **Don&#x27;t Ask the LLM: Visual Token Pruning with Spectral Structure and Semantic Relevance**<br><sub>Intaek Shin, Geuntaek Lim, Sungjune Park et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38303) · [PDF](https://arxiv.org/pdf/2610.38303) · [Code](https://github.com/sejong-rcv/ST-Pruner) |
| 2026-10-27 | **3D-SceneQ: Empowering 3D LLM With Query-Guided Adaptive Pruning and Multi-Modal Feature Enhancement**<br><sub>Yongqi Shan, Lu Zhang, Jiazuo Yu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37202) · [PDF](https://arxiv.org/pdf/2610.37202) |
| 2026-10-27 | **Mechanistic Failure Modes of Weight Pruning in Transformer Language Models**<br><sub>Nabeelah Faumi, Deshan Sumanathilaka</sub> | [arXiv](https://arxiv.org/abs/2610.37126) · [PDF](https://arxiv.org/pdf/2610.37126) |
| 2026-10-27 | **On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime**<br><sub>Kensuke Sasaki, Issei Sato</sub> | [arXiv](https://arxiv.org/abs/2610.37085) · [PDF](https://arxiv.org/pdf/2610.37085) |
| 2026-10-27 | **LearnPrunerV2: Learnable Progressive Token Pruning for Vision-Language Models**<br><sub>Rinyoichi Takezoe, Yaqian Li, Weiren Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36986) · [PDF](https://arxiv.org/pdf/2610.36986) |
| 2026-10-27 | **Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs**<br><sub>Donghyeon Cho, Joowon Kim, Seungho Shin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36671) · [PDF](https://arxiv.org/pdf/2610.36671) |
| 2026-10-26 | **TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration**<br><sub>Zhengxin Li, Chongzhen Tian, Hui Yuan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35489) · [PDF](https://arxiv.org/pdf/2610.35489) · [Code](https://github.com/yuanhui0325/TP-JSCC) |
| 2026-10-26 | **Domain-Adapted Latent Diffusion Models for CT-to-PET Image Translation**<br><sub>Yann Bourdé, Lea Bogensperger, Arnela Hadzic et al.</sub> | [arXiv](https://arxiv.org/abs/2610.35132) · [PDF](https://arxiv.org/pdf/2610.35132) |
| 2026-10-26 | **SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference**<br><sub>Yanzhen Zhou, Zhengyu Han, Qunyou Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34824) · [PDF](https://arxiv.org/pdf/2610.34824) |

<a id="distillation"></a>

## Distillation & Few-Step Generation

知识蒸馏、分布匹配与少步/单步生成 · **453 papers** · [Full archive](papers/distillation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-29 | **Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation**<br><sub>Yifu Luo, Chuang Ma, Zeyu Chen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40574) · [PDF](https://arxiv.org/pdf/2610.40574) · [Code](https://github.com/xingzhejun/MTA-OPSD) |
| 2026-10-29 | **LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation**<br><sub>Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40495) · [PDF](https://arxiv.org/pdf/2610.40495) |
| 2026-10-29 | **sDMD: Sinkhorn Distribution Matching Distillation**<br><sub>Jaihoon Kim, Lingxiao Li, Soshi Shimada et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39889) · [PDF](https://arxiv.org/pdf/2610.39889) |
| 2026-10-29 | **Turing LLM Post-Training: Calibrated Distillation and Efficient Dynamic-MoE Execution**<br><sub>Yue He, Jiahui Hu, Shaman Tang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39876) · [PDF](https://arxiv.org/pdf/2610.39876) |
| 2026-10-29 | **Intrinsic Distribution Matching**<br><sub>Deyuan Liu, Yansen Han, Kaiwen Zheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39633) · [PDF](https://arxiv.org/pdf/2610.39633) · [Code](https://github.com/inclusionAI/IDM) |
| 2026-10-29 | **ROAD: Modern Adversarial Training for Simple One-Step Distillation at Scale**<br><sub>Xiaoou Li, Shan You, Tao Huang</sub> | [arXiv](https://arxiv.org/abs/2610.39539) · [PDF](https://arxiv.org/pdf/2610.39539) |
| 2026-10-29 | **Efficient Covariance-Aware Vicinal Latent Diffusion for Continuous Conditional Image Generation**<br><sub>Xin Ding, Shuo Huang, Zhenglong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39277) · [PDF](https://arxiv.org/pdf/2610.39277) |
| 2026-10-28 | **Distilling the Shape of Uncertainty: What On-Policy Distillation Learns and How to Predict It**<br><sub>Shiping Yang, Chuanqi Tang, Hossein Hajimirsadeghi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39020) · [PDF](https://arxiv.org/pdf/2610.39020) · [Code](https://github.com/maybenotime/opd-esc) |
| 2026-10-28 | **Adversarial Self-Distillation**<br><sub>Mohammad Sadegh Akhondzadeh, Soroush H. Zargarbashi, Aleksandar Bojchevski</sub> | [arXiv](https://arxiv.org/abs/2610.38732) · [PDF](https://arxiv.org/pdf/2610.38732) |
| 2026-10-28 | **SCOPE: Selective Critical-Step On-Policy Self-Distillation for Agentic Reinforcement Learning**<br><sub>Qirui Liu, Wei Cao, Yu Mi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38391) · [PDF](https://arxiv.org/pdf/2610.38391) |
| 2026-10-28 | **Knowledge-structured and evidence-aware semantic self-distillation for glomerular pathology foundation model**<br><sub>Qiming He, Jing Li, Zihan Wang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38346) · [PDF](https://arxiv.org/pdf/2610.38346) |
| 2026-10-27 | **Multi-Draft On-Policy Distillation for Diffusion Drafters**<br><sub>Petr Molodyk, Yuchen Zhu, Jaemoo Choi et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37778) · [PDF](https://arxiv.org/pdf/2610.37778) |

<a id="efficient-training"></a>

## Efficient Training & Fine-Tuning

LoRA/PEFT、显存优化与高效训练 · **140 papers** · [Full archive](papers/efficient-training.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-28 | **Structure-retained low-rank adapters for weather synthesis**<br><sub>Shunxin Wang, Alexandros Stergiou, Luuk Spreeuwers et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38413) · [PDF](https://arxiv.org/pdf/2610.38413) |
| 2026-10-27 | **Towards Generalizing Pretrained All-Atom Representations to Unified Binder Design**<br><sub>Maojiang Su, Jiale Chen, Qijie Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37994) · [PDF](https://arxiv.org/pdf/2610.37994) |
| 2026-10-27 | **Bi-Phase Training: Learning Efficiently From Scratch**<br><sub>Abel Gurung, Joseph Campbell</sub> | [arXiv](https://arxiv.org/abs/2610.37934) · [PDF](https://arxiv.org/pdf/2610.37934) |
| 2026-10-27 | **EnergyCal: Taming Loss Spikes in Muon-Family Optimizers for Sparse MoE Training**<br><sub>Masato Fujitake</sub> | [arXiv](https://arxiv.org/abs/2610.37062) · [PDF](https://arxiv.org/pdf/2610.37062) |
| 2026-10-27 | **V-LUMEN: Visual Lookup Memory for Embedding Scaling in Vision-Language Models**<br><sub>Miso Choi, Daekeun Kim, Eunji Kim et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37019) · [PDF](https://arxiv.org/pdf/2610.37019) · [Code](https://github.com/miso-choi/V-Lumen) |
| 2026-10-27 | **Provenance Signatures for Low Rank Adaptations of Image Diffusion Models**<br><sub>Tobias Cheung, Mohan Dantam, Marc Juarez et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36933) · [PDF](https://arxiv.org/pdf/2610.36933) |
| 2026-10-27 | **CAMR: Compatibility-Aware Memory Replay for Continual Learning in Large Language Models**<br><sub>Jingpu Yang, Tianhao Li, Fengxian Ji et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36734) · [PDF](https://arxiv.org/pdf/2610.36734) |
| 2026-10-26 | **Synthetic Child-Adult Interactions Are Not Developmentally Plausible**<br><sub>Bastian Bunzeck, Francesca Padovani</sub> | [arXiv](https://arxiv.org/abs/2610.35029) · [PDF](https://arxiv.org/pdf/2610.35029) |
| 2026-10-26 | **RubriX: A Fast, Fine-Tunable Non-Autoregressive Rubric Judge**<br><sub>Balamurugan Paramasivam, Sudalai Rajkumar</sub> | [arXiv](https://arxiv.org/abs/2610.34875) · [PDF](https://arxiv.org/pdf/2610.34875) · [Code](https://huggingface.co/CobuildX-AI/RubriX-8B) |
| 2026-10-26 | **Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching**<br><sub>Fei Zuo, Yizhou Huang, Kezhi Wang</sub> | [arXiv](https://arxiv.org/abs/2610.34756) · [PDF](https://arxiv.org/pdf/2610.34756) |
| 2026-10-24 | **Task Format as a Factor in Adaptation: A Controlled Comparison of LoRA and Full Fine-Tuning for Prompt-Safety Classification**<br><sub>John Alderete, Srirakshith Betageri, Jennifer Flynn et al.</sub> | [arXiv](https://arxiv.org/abs/2610.33813) · [PDF](https://arxiv.org/pdf/2610.33813) |
| 2026-10-23 | **Rethinking LoRA Initialization for Robust Asymmetric Learning Rates**<br><sub>Disen Liao, Yaoliang Yu</sub> | [arXiv](https://arxiv.org/abs/2610.32142) · [PDF](https://arxiv.org/pdf/2610.32142) |

<a id="attention-kv-cache"></a>

## Efficient Attention & KV Cache

高效 Attention、长上下文与 KV Cache 压缩 · **197 papers** · [Full archive](papers/attention-kv-cache.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-29 | **KV Cache Quantization for Diffusion Language Models**<br><sub>Yan Tai, Yunan Ding, Guangzhao Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) |
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-28 | **GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices**<br><sub>Yipin Guo, Arun M George, Siddharth Joshi</sub> | [arXiv](https://arxiv.org/abs/2610.38210) · [PDF](https://arxiv.org/pdf/2610.38210) |
| 2026-10-27 | **Merge and Branch: Efficient Tree-Structured Supervised Fine-Tuning of LLMs for Recommendation**<br><sub>Yunqin Zhu, Yao Xie</sub> | [arXiv](https://arxiv.org/abs/2610.37973) · [PDF](https://arxiv.org/pdf/2610.37973) |
| 2026-10-27 | **FAD-KV: Adaptive Dictionary KV Caching for Efficient Reasoning Decoding**<br><sub>Yuxuan Zhu, David H. Yang, Parisa Shiravani et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37921) · [PDF](https://arxiv.org/pdf/2610.37921) |
| 2026-10-27 | **Multi-State Linear Attention with Generalized Second-Order Routing**<br><sub>Hee Seung Hwang, Sanghyuk Chun, Xindi Wu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37645) · [PDF](https://arxiv.org/pdf/2610.37645) |
| 2026-10-27 | **DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models**<br><sub>Egor Maximov, Aleksei Merkelov, Vasiliy Alekseev et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36950) · [PDF](https://arxiv.org/pdf/2610.36950) |
| 2026-10-26 | **WAKMan: Workload Aware KVCache Manager**<br><sub>Suhas Kumar Morisetty, Vaibhavi Lokegaonkar, Sachin Mathew Varghese et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36355) · [PDF](https://arxiv.org/pdf/2610.36355) |
| 2026-10-26 | **SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference**<br><sub>Yanzhen Zhou, Zhengyu Han, Qunyou Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34824) · [PDF](https://arxiv.org/pdf/2610.34824) |
| 2026-10-26 | **MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference**<br><sub>Huaizhi Zhang, Jiacheng Zhu, Xuqi Zhu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.34731) · [PDF](https://arxiv.org/pdf/2610.34731) |
| 2026-10-25 | **Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models**<br><sub>Dezhen Lu, Runguo Li, Zixiang Ni</sub> | [arXiv](https://arxiv.org/abs/2610.34436) · [PDF](https://arxiv.org/pdf/2610.34436) |
| 2026-10-24 | **ZipFusion: Fusing Lossless KV Decompression with Attention for Efficient LLM Decoding**<br><sub>Yuetao Chen, Peng Wang, Hong Xu</sub> | [arXiv](https://arxiv.org/abs/2610.33719) · [PDF](https://arxiv.org/pdf/2610.33719) |

<a id="decoding-reasoning"></a>

## Speculative Decoding & Efficient Reasoning

推测解码、并行解码与推理预算优化 · **133 papers** · [Full archive](papers/decoding-reasoning.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
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
| 2026-10-21 | **UlaCache: Unified Logical Addressing for Sparse LLM Serving**<br><sub>Isaac Zhu, Alan Cao, Hugh Yin et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29820) · [PDF](https://arxiv.org/pdf/2610.29820) |
| 2026-10-21 | **RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding**<br><sub>Mingkang Liu, Weiming Meng, Peipei Jiao et al.</sub> | [arXiv](https://arxiv.org/abs/2610.29527) · [PDF](https://arxiv.org/pdf/2610.29527) |

<a id="llm-systems"></a>

## LLM Serving & Systems

LLM 推理服务、调度、卸载与分布式系统 · **217 papers** · [Full archive](papers/llm-systems.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-29 | **Rimuru: Unified Memory Management for Modern LLM Serving via Elastic Expert Offloading**<br><sub>Zhiyuan Fang, Dingyang Li, Jianfeng Zhong et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40305) · [PDF](https://arxiv.org/pdf/2610.40305) |
| 2026-10-29 | **DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving**<br><sub>Yishuo Yuan, Shaoyu Yang, Chunrong Fang</sub> | [arXiv](https://arxiv.org/abs/2610.40292) · [PDF](https://arxiv.org/pdf/2610.40292) |
| 2026-10-29 | **Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets**<br><sub>Bole Ma, Ayesha Afzal, Jan Eitzinger et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40287) · [PDF](https://arxiv.org/pdf/2610.40287) |
| 2026-10-29 | **NORmal: Architecting 3D Ferroelectric NOR Flash as Main Memory -- From Co-Fabricated BEOL Arrays to 200B-Class Multi-Agent LLMs in a Smartphone**<br><sub>Zhuoran Li, Chen Gu, Zhuohang Bian et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40000) · [PDF](https://arxiv.org/pdf/2610.40000) |
| 2026-10-29 | **DWISE: Denoising Workload-Informed Scheduling Engine**<br><sub>Lie Li, Wen Li, Junxiao Shen et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39852) · [PDF](https://arxiv.org/pdf/2610.39852) |
| 2026-10-29 | **Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference**<br><sub>Wenjie Huang, Jun Zhang, Hongyaoxing Gu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39562) · [PDF](https://arxiv.org/pdf/2610.39562) |
| 2026-10-29 | **Learning to Formulate: Agentic Hardware-Software Co-Design of AI Infrastructure through Progressive Optimization and Verification**<br><sub>Yi Ding, Li Shang</sub> | [arXiv](https://arxiv.org/abs/2610.39380) · [PDF](https://arxiv.org/pdf/2610.39380) |
| 2026-10-28 | **FlatCake: A Flat KVCache Storage Architecture for LLM Serving**<br><sub>Xin Huang, Teng Ma, Zhuoran Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.38355) · [PDF](https://arxiv.org/pdf/2610.38355) |
| 2026-10-28 | **GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices**<br><sub>Yipin Guo, Arun M George, Siddharth Joshi</sub> | [arXiv](https://arxiv.org/abs/2610.38210) · [PDF](https://arxiv.org/pdf/2610.38210) |
| 2026-10-27 | **GAUSS: A Workload-Aware Analytical and Monte-Carlo Simulator for LLM Inference Serving**<br><sub>Srikant Bharadwaj, Ankur Mallick, Spyridon Mastorakis et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37989) · [PDF](https://arxiv.org/pdf/2610.37989) |
| 2026-10-27 | **ConfluxServe: Reconciling Resource Utilization and Parallelism Efficiency across Prefill and Decode in LLM Serving**<br><sub>Wenhao Chen, Hong Zhang</sub> | [arXiv](https://arxiv.org/abs/2610.37810) · [PDF](https://arxiv.org/pdf/2610.37810) |
| 2026-10-27 | **Request-Adaptive Execution for Efficient Hybrid LLM Inference**<br><sub>Fahao Chen, Xuzhe Yan, Qi Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37432) · [PDF](https://arxiv.org/pdf/2610.37432) |

<a id="diffusion-acceleration"></a>

## Diffusion Caching & Acceleration

扩散模型/DiT 的特征缓存、复用与采样加速 · **116 papers** · [Full archive](papers/diffusion-acceleration.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
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
| 2026-10-22 | **ParaLin++: Accelerating Parallel Diffusion Integrator via Intrinsic Partially Linear Structure**<br><sub>Jianrong Lu, Zhiyu Zhu, Hui Liu et al.</sub> | [arXiv](https://arxiv.org/abs/2610.30704) · [PDF](https://arxiv.org/pdf/2610.30704) |

<a id="visual-generation"></a>

## Efficient Image & Video Generation

图像/视频生成的计算、显存与延迟优化 · **188 papers** · [Full archive](papers/visual-generation.md)

| Published | Paper & authors | Links |
|:---|:---|:---|
| 2026-10-29 | **L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory**<br><sub>Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40614) · [PDF](https://arxiv.org/pdf/2610.40614) |
| 2026-10-29 | **LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation**<br><sub>Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan et al.</sub> | [arXiv](https://arxiv.org/abs/2610.40495) · [PDF](https://arxiv.org/pdf/2610.40495) |
| 2026-10-29 | **Wizard: Manipulate Any World in Real Time via Agentic Control**<br><sub>Yuzhe Wu, Zijun Lin, Yeying Jin</sub> | [arXiv](https://arxiv.org/abs/2610.40339) · [PDF](https://arxiv.org/pdf/2610.40339) |
| 2026-10-29 | **AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers**<br><sub>Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [Code](https://github.com/InfRec-Cardinal/AB-Attention) |
| 2026-10-29 | **FlexTry-On: A Time-Efficient Framework for Multi-Scenario Virtual Try-on**<br><sub>Phuong Dam, Quyen Nguyen Duc, Son Hoang Minh et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39646) · [PDF](https://arxiv.org/pdf/2610.39646) |
| 2026-10-29 | **ROAD: Modern Adversarial Training for Simple One-Step Distillation at Scale**<br><sub>Xiaoou Li, Shan You, Tao Huang</sub> | [arXiv](https://arxiv.org/abs/2610.39539) · [PDF](https://arxiv.org/pdf/2610.39539) |
| 2026-10-29 | **Efficient Covariance-Aware Vicinal Latent Diffusion for Continuous Conditional Image Generation**<br><sub>Xin Ding, Shuo Huang, Zhenglong Ding et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39277) · [PDF](https://arxiv.org/pdf/2610.39277) |
| 2026-10-29 | **CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation**<br><sub>Huangchao Song, Lingyun Yu, Cong Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.39160) · [PDF](https://arxiv.org/pdf/2610.39160) |
| 2026-10-27 | **ReferStream: Interactive Subject Injection for Streaming Video Generation**<br><sub>Shuolin Xu, Guanyuan Li, Boyu Li et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37566) · [PDF](https://arxiv.org/pdf/2610.37566) |
| 2026-10-27 | **A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation**<br><sub>Wenwu Tang, Dong Wang, Yun Cheng et al.</sub> | [arXiv](https://arxiv.org/abs/2610.37110) · [PDF](https://arxiv.org/pdf/2610.37110) |
| 2026-10-27 | **Haste Makes Waste? Towards Safe Few-Step Text-to-Image Models**<br><sub>Lior Ziv, Mahmood Sharif</sub> | [arXiv](https://arxiv.org/abs/2610.36665) · [PDF](https://arxiv.org/pdf/2610.36665) |
| 2026-10-27 | **Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation**<br><sub>Shufan Li, Hanrong Ye, Greg Heinrich et al.</sub> | [arXiv](https://arxiv.org/abs/2610.36466) · [PDF](https://arxiv.org/pdf/2610.36466) |

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
