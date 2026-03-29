```markdown
# Execution DAG

## Purpose

This document moves from static architecture to execution semantics.

A model diagram shows what components exist.  
An execution DAG shows how tokens, compute, and control move through those components at runtime.

The central questions are:
- What blocks are present  
- Which blocks execute  
- In what order they execute  
- For which tokens they execute  
- Under what control they execute  

---

## DAG Layers

- Ingress  
- Interaction  
- Selection  
- Transformation  
- Composition  
- Projection / Decode  

---

## Dense Transformer Runtime

- Token  
- Embedding  
- Positional Encoding  
- Attention  
- FeedForward  
- Residual Add  
- LayerNorm  
- Output  

### Properties
- Deterministic path  
- No routing decisions  
- Uniform batching  

---

## Sparse Mixture of Experts (MoE) Runtime

- Token  
- Embedding  
- Positional Encoding  
- Attention  
- Router  
- Top-K Experts  
- Aggregation  
- Residual Add  
- LayerNorm  
- Output  

### Properties
- Token-level conditional execution  
- Routing introduces load balancing and scheduling complexity  
- Throughput depends on expert packing efficiency  

---

## Hybrid Transformer Runtime

- Token  
- Embedding  
- Positional Encoding  
- Split  
  - Attention Branch  
  - Linear / Delta Branch  
- Mixer  
- Residual Add  
- LayerNorm  
- Output  

### Properties
- Partial parallelism  
- Mixer semantics are as important as branch semantics  

---

## Control Plane vs Data Plane

### Data Plane
- Embeddings  
- Attention activations  
- Expert outputs  
- Mixed outputs  
- Logits  

### Control Plane
- Router decisions  
- Top-K selection  
- Branch gating  
- Cache policy  
- Scheduling and placement policy  

---

## Canonical Execution Contracts

| Component            | Input Contract                | Output Contract              | Execution Mode            |
|---------------------|------------------------------|------------------------------|---------------------------|
| Embedding           | Token IDs                    | Dense vectors                | Sequential                |
| Positional Encoding | Dense vectors                | Position-aware vectors       | Sequential                |
| Attention           | Token vectors and context    | Contextual vectors           | Sequential or windowed    |
| Router              | Token vectors                | Expert indices and weights   | Conditional               |
| Expert              | Routed vectors               | Transformed vectors          | Parallel                  |
| Aggregator          | Expert outputs               | Merged vectors               | Parallel to sequential    |
| Hybrid Path         | Token vectors                | Alternative representation   | Parallel                  |
| Mixer               | Multiple branch outputs      | Merged representation        | Parallel to sequential    |
| Residual Add        | Prior and current state      | Combined vectors             | Sequential                |
| LayerNorm           | Combined vectors             | Stabilized vectors           | Sequential                |
| Output Projection   | Final vectors                | Logits                       | Sequential                |
```
