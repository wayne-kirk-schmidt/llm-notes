# LLM Machine Blueprint

| Component | Inputs | Outputs | Variants | Required | Notes |
|----------|--------|---------|----------|----------|-------|
| Token Input | Raw text / tokens | Token IDs | BPE, SentencePiece | Yes | External to model, but defines vocab boundary |
| Embedding Layer | Token IDs | Dense vectors | Learned embeddings | Yes | Maps discrete tokens → continuous space |
| Positional Encoding | Token embeddings | Position-aware embeddings | Absolute, RoPE, NoPE, Hybrid | Yes | Injects order; may be implicit (NoPE variants) |
| Transformer Block | Embeddings | Updated embeddings | Pre-norm, Post-norm | Yes | Container for attention + feedforward |
| Attention Layer | Token embeddings | Contextualized embeddings | MHA, GQA, MLA, SWA, Delta, Linear | Yes | Core sequence interaction mechanism |
| KV Cache | Attention inputs | Cached keys/values | Standard, compressed, sparse | No | Inference optimization, not always explicit |
| Routing Layer | Token embeddings | Routing weights / indices | Top-k gating, soft routing | No | Only present in MoE / hybrid systems |
| Expert Layer (FFN) | Routed embeddings | Transformed embeddings | Dense FFN, Sparse experts | Yes* | Always present; sparse in MoE |
| Expert Aggregation | Expert outputs | Combined embeddings | Weighted sum, concat | No | Only for MoE |
| Residual Connection | Layer input/output | Stabilized embeddings | Add, scaled add | Yes | Required for deep stacking |
| Normalization | Embeddings | Normalized embeddings | LayerNorm, RMSNorm, QK-Norm | Yes | Placement varies (pre/post) |
| Context Window Control | Attention scope | Masked attention | Full, sliding window, sparse | Yes | Controls compute scaling |
| Hybrid Mixing Layer | Multiple paths | Combined representation | Gated mixing, additive | No | Present in hybrid architectures |
| State-Space Layer | Sequence input | Sequence output | Mamba, SSM | No | Replaces attention in hybrids |
| Output Projection | Final embeddings | Logits | Linear projection | Yes | Maps back to vocab space |
| Sampling / Decoding | Logits | Tokens | Greedy, top-k, nucleus | Yes | Outside core model but required for generation |
