# Acronym Comparison Table

| Acronym | Full Name                          | Category            | Role in System                              | Used In Archetypes                | Notes |
|--------|-----------------------------------|---------------------|---------------------------------------------|----------------------------------|-------|
| LLM    | Large Language Model              | System              | End-to-end language modeling system         | All                              | Umbrella term for architectures |
| FFN    | FeedForward Network               | Transformation      | Token-wise nonlinear transformation         | Dense, MoE, Hybrid               | Often implemented as MLP |
| MLP    | Multi-Layer Perceptron            | Transformation      | Alternative name for FFN                    | Dense, MoE, Hybrid               | Same concept as FFN in transformers |
| MoE    | Mixture of Experts                | Architecture        | Sparse expert-based computation             | MoE, Hybrid                      | Enables conditional execution |
| MHA    | Multi-Head Attention              | Attention           | Parallel attention heads                    | Dense, MoE, Hybrid               | Standard transformer attention |
| GQA    | Grouped Query Attention           | Attention           | Shared key/value across query groups        | Dense, MoE, Hybrid               | Reduces memory footprint |
| MLA    | Multi-Linear Attention            | Attention           | Linearized attention approximation          | Sparse/Efficient, Hybrid         | Improves scaling efficiency |
| SWA    | Sliding Window Attention          | Attention           | Local attention window                      | Sparse/Efficient                 | Reduces compute for long context |
| KV     | Key-Value                         | Memory              | Stores attention state                      | All (inference)                  | Used in KV cache |
| SSM    | State-Space Model                 | Interaction         | Sequence modeling alternative to attention  | State-Space Hybrid               | Examples include Mamba |
| RoPE   | Rotary Positional Encoding        | Position            | Relative position encoding via rotation     | Dense, MoE, Hybrid               | Widely used in modern LLMs |
| NoPE   | No Positional Encoding            | Position            | Implicit positional handling                | Experimental / Hybrid            | Removes explicit position signals |
| BPE    | Byte Pair Encoding                | Tokenization        | Subword tokenization method                 | All                              | Common tokenizer |
| RMSNorm| Root Mean Square Normalization    | Normalization       | Scale normalization without mean centering  | Dense, MoE, Hybrid               | Faster than LayerNorm |
| QK-Norm| Query-Key Normalization           | Normalization       | Stabilizes attention scores                 | Advanced variants                | Applied inside attention |
| Top-K  | Top-K Selection                   | Routing             | Selects K highest scoring experts           | MoE, Hybrid                      | Core gating mechanism |
| SOTA   | State Of The Art                  | General             | Best known performance benchmark            | All                              | Contextual usage, not structural |
