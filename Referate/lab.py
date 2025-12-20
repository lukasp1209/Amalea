import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def softmax(x):
    """Berechnet Softmax entlang der letzten Achse."""
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / np.sum(e_x, axis=-1, keepdims=True)

def scaled_dot_product_attention(Q, K, V):
    """
    Berechnet die Attention Scores und den Output.
    Q, K, V: Matrizen der Form (seq_len, d_k)
    """
    d_k = Q.shape[-1]
    
    # 1. Scores berechnen: Q * K^T
    scores = np.dot(Q, K.T)
    
    # 2. Skalieren (für stabilere Gradienten)
    scaled_scores = scores / np.sqrt(d_k)
    
    # 3. Softmax (Attention Weights)
    attention_weights = softmax(scaled_scores)
    
    # 4. Gewichtete Summe der Values
    output = np.dot(attention_weights, V)
    
    return output, attention_weights

# --- DEMO ---

# Wir simulieren 4 Wörter mit Embedding-Dimension 8
# Satz: "Die Katze schläft hier"
np.random.seed(42)
seq_len = 4
d_model = 8

# Zufällige Embeddings als Input (in echt wären das trainierte Vektoren)
X = np.random.randn(seq_len, d_model)

# In echten Transformern werden Q, K, V durch lineare Layer aus X erzeugt.
# Hier vereinfachen wir und nehmen an: Q = K = V = X (naive Self-Attention)
Q = X
K = X
V = X

output, weights = scaled_dot_product_attention(Q, K, V)

print("Input Shape:", X.shape)
print("Output Shape:", output.shape)
print("\nAttention Weights Matrix (wer schaut auf wen?):")
print(np.round(weights, 2))

# Visualisierung
words = ["Die", "Katze", "schläft", "hier"]

plt.figure(figsize=(8, 6))
sns.heatmap(weights, annot=True, cmap='viridis', 
            xticklabels=words, yticklabels=words)
plt.title("Self-Attention Heatmap")
plt.xlabel("Key (Source)")
plt.ylabel("Query (Target)")

print("Plot wird erstellt...")
plt.show()
print("Beobachtung: In diesem zufälligen Beispiel achten Wörter auf sich selbst und andere.")
print("In einem trainierten Modell würde 'schläft' stark auf 'Katze' achten.")