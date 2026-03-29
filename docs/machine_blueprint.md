# LLM Machine Blueprint and Architecture Flows

## Machine Blueprint Table

| Component               | Inputs                   | Outputs                    | Variants                                      | Required | Notes |
|------------------------|--------------------------|----------------------------|-----------------------------------------------|----------|-------|
| Token Input            | Raw text or tokens       | Token IDs                  | BPE, SentencePiece                            | Yes      | External to model, defines vocabulary boundary |
| Embedding Layer        | Token IDs                | Dense vectors              | Learned embeddings                            | Yes      | Maps discrete tokens to continuous space |
| Positional Encoding    | Token embeddings         | Position-aware embeddings  | Absolute, RoPE, NoPE, Hybrid                  | Yes      | Injects order; may be implicit in some variants |
| Transformer Block      | Embeddings               | Updated embeddings         | Pre-norm, Post-norm                           | Yes      | Container for attention and feedforward |
| Attention Layer        | Token embeddings         | Contextualized embeddings  | MHA, GQA, MLA, SWA, Delta, Linear             | Yes      | Core sequence interaction mechanism |
| KV Cache               | Attention inputs         | Cached keys and values     | Standard, compressed, sparse                  | No       | Inference optimization |
| Routing Layer          | Token embeddings         | Routing weights and indices| Top-k gating, soft routing                    | No       | Present in Mixture of Experts and hybrid systems |
| Expert Layer (FFN)     | Routed embeddings        | Transformed embeddings     | Dense FFN, sparse experts                     | Yes*     | Always present; sparse in Mixture of Experts |
| Expert Aggregation     | Expert outputs           | Combined embeddings        | Weighted sum, concatenation                   | No       | Only used in Mixture of Experts |
| Residual Connection    | Layer input and output   | Stabilized embeddings      | Add, scaled add                               | Yes      | Required for deep stacking |
| Normalization          | Embeddings               | Normalized embeddings      | LayerNorm, RMSNorm, QK-Norm                   | Yes      | Placement varies |
| Context Window Control | Attention scope          | Masked attention           | Full, sliding window, sparse                  | Yes      | Controls compute scaling |
| Hybrid Mixing Layer    | Multiple paths           | Combined representation    | Gated mixing, additive                        | No       | Present in hybrid architectures |
| State-Space Layer      | Sequence input           | Sequence output            | Mamba, SSM                                    | No       | Alternative to attention |
| Output Projection      | Final embeddings         | Logits                     | Linear projection                             | Yes      | Maps to vocabulary space |
| Sampling and Decoding  | Logits                   | Tokens                     | Greedy, top-k, nucleus                        | Yes      | Outside core model but required for generation |

---

## Canonical Architecture Flows

### Dense Transformer

- Token Input  
- Embedding  
- Positional Encoding  
- Transformer Block repeated N times  
  - Attention  
  - Feedforward (FFN)  
  - Residual Add  
  - LayerNorm  
- Output Projection  
- Decoding  

---

### Sparse Mixture of Experts (MoE) Transformer

- Token Input  
- Embedding  
- Positional Encoding  
- Optional Dense Prefix  
- Mixture of Experts Block repeated N times  
  - Attention  
  - Routing Layer (Top-K)  
  - Expert Layers (subset activated)  
  - Expert Aggregation  
  - Residual Add  
  - LayerNorm  
- Output Projection  
- Decoding  

---

### Sparse and Efficient Attention

- Token Input  
- Embedding  
- Positional Encoding  
- Mixture of Experts Block repeated N times  
  - Multi-Linear Attention (MLA)  
  - Sparse Attention (optional)  
  - Routing  
  - Experts  
- Output  

---

### Hybrid Transformer

- Token Input  
- Embedding  
- Positional Encoding  
- Hybrid Block repeated N times  
  - Attention Path  
  - Linear or Delta Path  
  - Hybrid Mixing  
  - Optional Routing and Experts  
- Output  

---

### State-Space Hybrid

- Token Input  
- Embedding  
- State-Space Blocks repeated N times  
  - Sequence modeling  
  - Occasional attention  
- Output  

---

## Structural Reduction

- Representation Layer  
  - Embedding  
  - Positional Encoding  

- Interaction Layer  
  - Attention or State-Space  

- Selection Layer  
  - Routing (optional)  

- Transformation Layer  
  - Feedforward or Experts  

- Composition Layer  
  - Residual Add  
  - LayerNorm  

- Projection Layer  
  - Output Projection  

---

## Component Contracts

| Component | Contract                          |
|-----------|-----------------------------------|
| Attention | Token to contextual token         |
| Router    | Token to expert indices           |
| Expert    | Token to transformed token        |
| Mixer     | Multiple paths to single token    |
