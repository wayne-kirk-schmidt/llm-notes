# Execution DAG

## Purpose

This document moves from static architecture to execution semantics.

A model diagram shows what components exist.
An execution DAG shows how tokens, compute, and control move through those components at runtime.

The central question is not only:
- What blocks are present?
- Which blocks execute, in what order, for which tokens, under what control?

## DAG Layers

1. Ingress
2. Interaction
3. Selection
4. Transformation
5. Composition
6. Projection / Decode

## Dense Transformer Runtime

`Token -> Embed -> Position -> Attention -> FFN -> Residual/Norm -> Output`

Properties:
- deterministic path
- no route decision
- easiest to batch uniformly

## Sparse MoE Runtime

`Token -> Embed -> Position -> Attention -> Router -> Top-k Experts -> Aggregate -> Residual/Norm -> Output`

Properties:
- token-level conditional execution
- routing introduces load-balancing and scheduling concerns
- throughput depends on expert packing efficiency

## Hybrid Transformer Runtime

`Token -> Embed -> Position -> [Attention Branch || Linear/Delta Branch] -> Mixer -> Residual/Norm -> Output`

Properties:
- partial parallelism
- mixer semantics matter as much as branch semantics

## Control Plane vs Data Plane

### Data Plane
- embeddings
- attention activations
- expert outputs
- mixed outputs
- logits

### Control Plane
- router decisions
- top-k selection
- branch gating
- cache policy
- scheduling and placement policy

## Canonical Execution Contracts

| Component | Input Contract | Output Contract | Execution Mode |
|----------|----------------|-----------------|----------------|
| Embedding | token IDs | dense vectors | sequential |
| Position | dense vectors | position-aware vectors | sequential |
| Attention | token vectors + context | contextual vectors | sequential or windowed |
| Router | token vectors | expert indices + weights | conditional |
| Expert | routed vectors | transformed vectors | parallel |
| Aggregator | expert outputs | merged vectors | parallel-to-sequential |
| Hybrid Path | token vectors | alternative representation | parallel |
| Mixer | multiple branch outputs | merged representation | parallel-to-sequential |
| Residual/Norm | prior + current state | stabilized vectors | sequential |
| Output Projection | final vectors | logits | sequential |
