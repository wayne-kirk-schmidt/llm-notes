# Archetypes

## Dense Transformer

`Token Input -> Embedding -> Positional Encoding -> Attention -> FeedForward -> Residual/Norm -> Output`

## Sparse MoE

`Token Input -> Embedding -> Positional Encoding -> Attention -> Router -> Experts -> Aggregator -> Residual/Norm -> Output`

## Hybrid Transformer

`Token Input -> Embedding -> Positional Encoding -> [Attention Path + Linear/Delta Path] -> Mixer -> Residual/Norm -> Output`
