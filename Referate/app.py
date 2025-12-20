import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Unit 07: Attention Mechanismus")
st.markdown("Visualisierung der **Scaled Dot-Product Attention**: $Attention(Q, K, V) = softmax(\\frac{QK^T}{\\sqrt{d_k}})V$")

# --- Sidebar ---
st.sidebar.header("Parameter")
seq_len = st.sidebar.slider("Sequenzlänge (Anzahl Wörter)", 2, 6, 4)
d_k = st.sidebar.slider("Embedding Dimension (d_k)", 2, 10, 4)

st.sidebar.markdown("---")
st.sidebar.write("**Werte bearbeiten:**")
seed = st.sidebar.number_input("Random Seed", 0, 100, 42)

# --- Berechnung ---
np.random.seed(seed)

# Wir generieren zufällige Q, K, V Matrizen
# In der Praxis kommen diese aus linearen Layern
Q = np.random.randn(seq_len, d_k)
K = np.random.randn(seq_len, d_k)
V = np.random.randn(seq_len, d_k)

# 1. Dot Product (Scores)
scores = np.dot(Q, K.T)

# 2. Scaling
scaled_scores = scores / np.sqrt(d_k)

# 3. Softmax
def softmax(x):
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / np.sum(e_x, axis=-1, keepdims=True)

attention_weights = softmax(scaled_scores)

# 4. Output
output = np.dot(attention_weights, V)

# --- Visualisierung ---

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Query (Q) & Key (K)")
    st.write("Ähnlichkeit berechnen ($Q \\cdot K^T$)")
    fig, ax = plt.subplots(figsize=(4,3))
    sns.heatmap(scores, annot=True, fmt=".1f", cmap="coolwarm", cbar=False, ax=ax)
    ax.set_title("Raw Scores (Dot Product)")
    ax.set_xlabel("Key Index")
    ax.set_ylabel("Query Index")
    st.pyplot(fig)

with col2:
    st.subheader("2. Attention Weights")
    st.write("Nach Scaling & Softmax (Summe pro Zeile = 1)")
    fig, ax = plt.subplots(figsize=(4,3))
    sns.heatmap(attention_weights, annot=True, fmt=".2f", cmap="viridis", cbar=False, ax=ax)
    ax.set_title("Attention Weights (Wahrscheinlichkeiten)")
    ax.set_xlabel("Key Index")
    ax.set_ylabel("Query Index")
    st.pyplot(fig)

st.markdown("---")
st.subheader("3. Ergebnis (Weighted Sum)")
st.write("Der Output ist eine Mischung der Values ($V$), gewichtet mit den Attention Weights.")

c1, c2 = st.columns([1, 2])
with c1:
    st.write("**Values (V)**")
    st.dataframe(np.round(V, 2))

with c2:
    st.write("**Output (Z)**")
    # Visualisierung des Outputs als Heatmap
    fig, ax = plt.subplots(figsize=(6, 2))
    sns.heatmap(output, annot=True, fmt=".2f", cmap="Blues", cbar=False, ax=ax)
    ax.set_title("Finaler Output Vektor pro Wort")
    st.pyplot(fig)

st.info("""
**Interpretation:** Jede Zeile in der 'Attention Weights' Matrix zeigt, wie stark ein Wort (Query) auf andere Wörter (Keys) achtet. Ist der Wert hoch (gelb), fließt viel Information vom entsprechenden Value in den Output.
""")