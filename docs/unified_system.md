# Unified LLM System

The unified architecture represents a generalized execution model supporting:

- Dense transformer computation  
- Sparse Mixture of Experts (MoE) routing  
- Hybrid parallel compute paths  

---

## Shared Front-End

- Token Input  
- Embedding  
- Positional Encoding  
- Attention  

---

## Branches

### Dense Path

- Attention  
- FeedForward  
- Residual Add  

---

### Sparse Mixture of Experts (MoE) Path

- Attention  
- Router  
- Experts  
- Aggregation  
- Residual Add  

---

### Hybrid Path

- Positional Encoding  
- Attention  
- Hybrid Path  
- Mixer  
- Residual Add  

---

## Convergence

- Residual Add  
- LayerNorm  
- Output Projection  
