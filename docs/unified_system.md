# Unified LLM System

The unified architecture represents a generalized execution model supporting:

- dense transformer computation
- sparse mixture-of-experts routing
- hybrid parallel compute paths

## Shared Front-End

1. Token Input
2. Embedding
3. Positional Encoding
4. Attention

## Branches

### Dense Path
`Attention -> FeedForward -> Residual`

### MoE Path
`Attention -> Router -> Experts -> Aggregator -> Residual`

### Hybrid Path
`Positional Encoding + Attention -> Hybrid Path -> Mixer -> Residual`

## Convergence

`Residual -> Normalization -> Output Projection`
