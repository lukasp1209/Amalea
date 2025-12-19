# Scaled Dot-Product Attention

Formel:

$$\text{Att}(Q,K,V) = \text{softmax}\left(\frac{QK^{\top}}{\sqrt{d_k}}\right) V$$

Kurz: Kernoperation in Transformer‑Modellen; skaliert Dot‑Products vor Softmax.