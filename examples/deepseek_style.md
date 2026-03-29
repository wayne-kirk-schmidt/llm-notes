# DeepSeek-Style Mapping

## Purpose

This document maps the unified LLM system to a DeepSeek-style architecture.

The goal is to show how a real-world system instantiates the abstract model:

- Transform  
- Selection  
- Composition  

DeepSeek is not a new paradigm.  
It is a **specific optimization of the Mixture of Experts (MoE) pattern combined with efficient attention and system-level scheduling discipline**.

---

## High-Level Characteristics

DeepSeek-style systems are defined by:

- Sparse Mixture of Experts (MoE) at scale  
- Aggressive routing efficiency  
- Attention optimizations (memory and compute)  
- Strong separation of data plane and control plane  

---

## Mapping to Unified LLM System

### Shared Front-End

- Token Input  
- Embedding  
- Positional Encoding  
- Attention  

DeepSeek does not change the front-end.  
Most optimizations occur after attention.

---

### Transform and Selection (Core Innovation Zone)

#### Unified Model View

- Transform  
- Optional Routing  
- Merge  

#### DeepSeek Instantiation

- Attention  
- Router (Top-K gating)  
- Experts (sparse activation)  
- Aggregation (weighted merge)  

---

## Execution Flow (DeepSeek Style)

- Token Input  
- Embedding  
- Positional Encoding  
- Attention  
- Router  
- Top-K Expert Selection  
- Expert Execution (parallel, sparse)  
- Aggregation  
- Residual Add  
- LayerNorm  
- Output Projection  

---

## Key Differences from Standard MoE

### 1. Routing Efficiency

Standard MoE:
- Router selects experts  
- Often suffers from imbalance and token skew  

DeepSeek-style:
- Stronger routing constraints  
- Better load balancing  
- Improved token-to-expert distribution  

Effect:
- Higher hardware utilization  
- Reduced stragglers  

---

### 2. Expert Utilization

Standard MoE:
- Experts underutilized  
- Capacity mismatch  

DeepSeek-style:
- More uniform expert usage  
- Better packing of tokens per expert  

Effect:
- Improved throughput  
- Lower wasted compute  

---

### 3. Attention Efficiency

DeepSeek-style systems often incorporate:

- Multi-Linear Attention (MLA)  
- Memory-efficient attention variants  

Effect:
- Lower memory bandwidth pressure  
- Better scaling to long contexts  

---

### 4. System-Level Scheduling

This is where DeepSeek differs most from academic MoE.

DeepSeek-style systems treat:

- Routing  
- Expert placement  
- Execution timing  

as **system problems**, not just model problems.

Control plane responsibilities include:

- Token routing decisions  
- Expert placement across devices  
- Scheduling execution batches  
- Managing KV cache locality  

---

## Control Plane vs Data Plane Mapping

### Data Plane

- Embeddings  
- Attention activations  
- Expert outputs  
- Aggregated outputs  
- Final logits  

### Control Plane

- Router decisions  
- Top-K selection  
- Load balancing policies  
- Expert placement  
- Scheduling and batching  
- Cache management  

---

## Structural Mapping

| Unified Layer        | DeepSeek Equivalent                  |
|---------------------|-------------------------------------|
| Representation      | Embedding + Positional Encoding     |
| Interaction         | Attention                           |
| Selection           | Router (Top-K gating)               |
| Transformation      | Experts (FFN variants)              |
| Composition         | Aggregation + Residual + Norm       |
| Projection          | Output Projection                   |

---

## Key Insight

DeepSeek is best understood as:

- Not a new architecture  
- Not just a Mixture of Experts  

It is:

- A **system-optimized sparse transformer**  
- Where routing, compute, and scheduling are co-designed  

---

## Practical Interpretation

If you are building toward a DeepSeek-style system:

- Focus less on adding experts  
- Focus more on:
  - routing quality  
  - expert balance  
  - scheduling efficiency  
  - memory locality  

---

## Summary

DeepSeek-style mapping can be reduced to:

- Same front-end  
- Sparse transform layer  
- Strong control plane  

The innovation is not in the blocks.  
It is in **how the blocks are executed at scale**.
