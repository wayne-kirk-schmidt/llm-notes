# Archetypes

## Core Execution Template (Baseline)

- Input  
- Embedding  
- Positional Encoding  
- Transform  
- Merge  
- Residual Add  
- LayerNorm  
- Output  

---

## Dense Transformer

- Input  
- Embedding  
- Positional Encoding  
- Attention  
- FeedForward  
- Residual Add  
- LayerNorm  
- Output  

### Notes
- Transform  
  - Sequential (Attention then FeedForward)  
- Merge  
  - Implicit (no branching)  
- Characteristics  
  - Dense compute  
  - No routing  
  - Single path  

---

## Sparse Mixture of Experts (MoE) Transformer

- Input  
- Embedding  
- Positional Encoding  
- Attention  
- Router  
- Experts (Top-K)  
- Aggregation (Weighted Sum)  
- Residual Add  
- LayerNorm  
- Output  

### Notes
- Transform  
  - Attention plus conditional expert selection  
- Merge  
  - Explicit aggregation  
- Characteristics  
  - Sparse compute  
  - Conditional execution  
  - Routing policy driven  

---

## Hybrid Transformer

- Input  
- Embedding  
- Positional Encoding  
- Split  
  - Attention Path  
  - Linear / Delta Path  
- Mixer (Fusion)  
- Residual Add  
- LayerNorm  
- Output  

### Notes
- Transform  
  - Parallel paths  
- Merge  
  - Learned mixer  
- Characteristics  
  - Parallel dense compute  
  - No routing  
  - Fusion-driven integration  

---

## Structural Alignment

- Transform Type  
  - Dense: Sequential  
  - Sparse Mixture of Experts (MoE): Conditional (sparse)  
  - Hybrid: Parallel  

- Routing  
  - Dense: None  
  - Sparse Mixture of Experts (MoE): Router (Top-K)  
  - Hybrid: None  

- Parallelism  
  - Dense: Low  
  - Sparse Mixture of Experts (MoE): High (sparse)  
  - Hybrid: High (dense parallel)  

- Merge Mechanism  
  - Dense: Implicit  
  - Sparse Mixture of Experts (MoE): Weighted aggregation  
  - Hybrid: Learned mixer  

- Compute Pattern  
  - Dense: Dense  
  - Sparse Mixture of Experts (MoE): Sparse  
  - Hybrid: Mixed  

---

## Generalized Transform Block

- Compute Paths  
- Routing (optional)  
- Merge Strategy  

### Instantiation

- Dense  
  - One path  
  - No routing  
  - Identity merge  

- Sparse Mixture of Experts (MoE)  
  - Multiple paths  
  - Routed (Top-K)  
  - Weighted merge  

- Hybrid  
  - Multiple paths  
  - No routing  
  - Learned merge  
