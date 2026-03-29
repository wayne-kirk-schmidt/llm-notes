# LLaMA-Style Mapping

## Purpose

This document maps the unified LLM system to a LLaMA-style architecture.

The goal is to show how an efficient, open-weight dense transformer system is implemented with:

- Strong normalization strategy (RMSNorm)  
- Rotary positional encoding (RoPE)  
- Efficient attention variants (GQA in later versions)  
- Simplicity and reproducibility as first-class constraints  

LLaMA-style systems represent a **clean, minimal, and highly efficient dense transformer design**.

---

## High-Level Characteristics

LLaMA-style systems are defined by:

- Dense transformer architecture (no Mixture of Experts routing)  
- RMSNorm instead of LayerNorm  
- Rotary Positional Encoding (RoPE)  
- FeedForward variants using gated activations (e.g., SwiGLU)  
- Increasing use of Grouped Query Attention (GQA) in newer versions  

---

## Mapping to Unified LLM System

### Shared Front-End

- Token Input  
- Embedding  
- Positional Encoding (Rotary Positional Encoding)  
- Attention  

This layer is standard but emphasizes efficiency and stability.

---

### Transform and Composition

#### Unified Model View

- Transform  
- Merge  
- Residual  
- Normalization  

#### LLaMA Instantiation

- Attention  
- FeedForward (gated MLP, e.g., SwiGLU)  
- Residual Add  
- RMSNorm  

---

## Execution Flow (LLaMA Style)

- Token Input  
- Embedding  
- Positional Encoding (RoPE)  
- Transformer Block repeated N times  
  - Attention (Multi-Head or Grouped Query Attention)  
  - FeedForward (SwiGLU or gated MLP)  
  - Residual Add  
  - RMSNorm  
- Output Projection  
- Decoding  

---

## Key Characteristics

### 1. Dense Compute

- All parameters active per token  
- No routing or conditional execution  

Effect:
- Predictable compute  
- Simpler infrastructure  
- Easier reproducibility  

---

### 2. Rotary Positional Encoding (RoPE)

- Encodes position via rotation in embedding space  
- Naturally supports extrapolation to longer contexts  

Effect:
- Better generalization across sequence lengths  
- Efficient integration into attention  

---

### 3. RMSNorm Instead of LayerNorm

- Normalizes based on magnitude, not mean  

Effect:
- Lower computational overhead  
- Stable training for deep models  

---

### 4. FeedForward Optimization

- Uses gated activations such as SwiGLU  

Effect:
- Improved expressiveness  
- Better parameter efficiency  

---

### 5. Attention Evolution

- Early versions: Multi-Head Attention (MHA)  
- Later versions: Grouped Query Attention (GQA)  

Effect:
- Reduced KV cache size  
- Improved inference efficiency  

---

## Control Plane vs Data Plane Mapping

### Data Plane

- Embeddings  
- Attention activations  
- FeedForward outputs  
- Residual states  
- Final logits  

### Control Plane

- Batch construction  
- KV cache management  
- Attention masking  
- Execution scheduling  

---

## Structural Mapping

| Unified Layer   | LLaMA Equivalent                      |
|----------------|--------------------------------------|
| Representation | Embedding + RoPE                     |
| Interaction    | Attention                            |
| Selection      | None                                 |
| Transformation | Gated FeedForward (SwiGLU)           |
| Composition    | Residual Add + RMSNorm               |
| Projection     | Output Projection                    |

---

## Key Insight

LLaMA-style systems are best understood as:

- Minimal, efficient dense transformers  
- Designed for openness and reproducibility  
- Optimized through **careful component choices rather than architectural complexity**

---

## Practical Interpretation

If you are building toward a LLaMA-style system:

- Focus on:
  - normalization strategy (RMSNorm)  
  - positional encoding (RoPE)  
  - efficient attention (GQA)  
  - clean, reproducible architecture  

- Avoid:
  - unnecessary architectural branching  
  - premature optimization through sparsity  

---

## Summary

LLaMA-style mapping can be reduced to:

- Dense transform layer  
- No selection layer  
- Efficient normalization and encoding choices  
- Balanced system-level optimization  

The innovation is in **simplicity, stability, and efficiency**, not structural complexity.
