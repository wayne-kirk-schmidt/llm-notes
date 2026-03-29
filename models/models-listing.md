# LLM Architecture Normalized Table

| Model | Family | Scale (Total/Active) | Decoder | Attention | Routing | Context Strategy | Positional | Key Pattern |
|------|--------|----------------------|---------|----------|---------|------------------|------------|------------|
| GPT-2 XL | Dense | 1.5B | Dense | MHA | None | Full | Absolute | Classic baseline |
| Llama 3 | Dense | 8B | Dense | GQA | None | Full | RoPE | Modern dense baseline |
| OLMo 2 | Dense | 7B | Dense | MHA + QK-Norm | None | Full | RoPE | Post-norm variant |
| Gemma 3 | Dense | 27B | Dense | GQA + QK-Norm | None | SWA + Global | RoPE | Local-heavy attention |
| Mistral Small 3.1 | Dense | 24B | Dense | GQA | None | Full | RoPE | Latency optimized |
| Qwen3 (32B) | Dense | 32B | Dense | GQA + QK-Norm | None | Full | RoPE | Dense reference |
| SmolLM3 | Dense | 3B | Dense | GQA + NoPE | None | Full | Partial NoPE | Positional experiment |
| Tiny Aya | Dense | 3.35B | Dense | GQA + SWA | None | SWA | RoPE + NoPE | Parallel blocks |

| DeepSeek V3 | Sparse MoE | 671B / 37B | Sparse | MLA | Top-k | Full | RoPE | Dense prefix + shared expert |
| DeepSeek R1 | Sparse MoE | 671B / 37B | Sparse | MLA | Top-k | Full | RoPE | Reasoning tuned |
| DeepSeek V3.2 | Sparse MoE | 671B / 37B | Sparse | MLA + Sparse Attn | Top-k | Sparse + Full | RoPE | Efficiency evolution |
| Mistral 3 Large | Sparse MoE | 673B / 41B | Sparse | MLA | Top-k | Full | RoPE | DeepSeek-like |
| GPT-OSS (120B) | Sparse MoE | 120B | Sparse | GQA + SWA | Top-k | SWA + Global | RoPE | Alternating attention |
| GPT-OSS (20B) | Sparse MoE | 20B / 3.6B | Sparse | GQA + SWA | Top-k | SWA + Global | RoPE | Wide shallow |
| Grok 2.5 | Sparse MoE | 270B | Sparse | GQA | Top-k | Full | RoPE | SwiGLU shared path |
| Qwen3 (235B) | Sparse MoE | 235B / 22B | Sparse | GQA + QK-Norm | Top-k | Full | RoPE | No shared expert |
| MiniMax M2 | Sparse MoE | 230B / 10B | Sparse | GQA + QK-Norm | Top-k | Full | RoPE | Sparse routing |
| GLM-5 | Sparse MoE | 744B / 40B | Sparse | MLA + Sparse Attn | Top-k | Sparse + Full | RoPE | Large-scale MLA |

| Qwen3 Next | Hybrid | 80B / 3B | Hybrid | DeltaNet + Gated Attn | Top-k | Long-context | RoPE | Hybrid attention |
| Qwen3.5 | Hybrid | 397B / 17B | Hybrid | DeltaNet + Gated Attn | Top-k | Long-context | RoPE | Hybrid mainstream |
| Kimi Linear | Hybrid | 48B / 3B | Hybrid | Delta + MLA | Top-k | Long-context | NoPE | Linear attention |
| Nemotron Nano | Hybrid | 30B / 3B | Hybrid | Mamba-2 + GQA | Top-k | Long-context | None | State-space hybrid |
