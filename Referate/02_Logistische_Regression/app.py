import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Unit 02: Logistic Regression", layout="wide")

st.title("💊 Die Logistische Regression (Sigmoid)")
st.markdown("""
Bei der Klassifikation wollen wir Wahrscheinlichkeiten zwischen 0 und 1 vorhersagen.
Eine Gerade (Lineare Regression) kann beliebig groß oder klein werden. Die **Sigmoid-Funktion** löst das.
""")

# --- Sidebar: Daten ---
st.sidebar.header("1. Datensatz (Lernen vs. Erfolg)")
n_samples = st.sidebar.slider("Anzahl Studenten", 10, 100, 40)
noise = st.sidebar.slider("Überlappung (Noise)", 0.1, 2.0, 0.5)

# Daten generieren: X = Lernstunden, y = Bestanden (0/1)
np.random.seed(42)
X = np.random.uniform(0, 10, n_samples)
X.sort()
# Wahre Logik: Wer > 5h lernt, besteht wahrscheinlich
logits = (X - 5) * 2  
probs = 1 / (1 + np.exp(-logits))
# Labels mit Rauschen
y = np.random.binomial(1, probs)

# --- Sidebar: Modell ---
st.sidebar.header("2. Manuelles Modell")
st.sidebar.latex(r"P(y=1) = \frac{1}{1 + e^{-(wx + b)}}")

w_guess = st.sidebar.slider("Gewicht w (Steilheit)", 0.1, 5.0, 1.0, 0.1)
b_guess = st.sidebar.slider("Bias b (Verschiebung)", -10.0, 10.0, -5.0, 0.5)
threshold = st.sidebar.slider("Entscheidungsgrenze (Threshold)", 0.0, 1.0, 0.5)

# --- Berechnungen ---
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Vorhersage (Wahrscheinlichkeiten)
logits_pred = w_guess * X + b_guess
y_proba = sigmoid(logits_pred)

# Klassifikation (Hart 0 oder 1)
y_pred_class = (y_proba >= threshold).astype(int)

# Accuracy
accuracy = np.mean(y_pred_class == y)

# Scikit-Learn Vergleich
clf = LogisticRegression()
clf.fit(X.reshape(-1, 1), y)
X_plot = np.linspace(0, 10, 200).reshape(-1, 1)
y_opt_proba = clf.predict_proba(X_plot)[:, 1]

# --- Visualisierung ---
col1, col2 = st.columns([3, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 1. Datenpunkte
    # Wir plotten sie leicht vertikal gestreut, damit man sie besser sieht
    jitter = np.random.normal(0, 0.02, size=len(y))
    ax.scatter(X, y + jitter, color='black', alpha=0.6, label='Daten (0=Fail, 1=Pass)')
    
    # 2. Sigmoid Kurve (Manuell)
    ax.plot(X, y_proba, color='blue', linewidth=3, label='Deine Sigmoid-Kurve')
    
    # 3. Decision Boundary (Wo ist y=Threshold?)
    # w*x + b = logit(threshold) -> x = (logit(threshold) - b) / w
    # Für Threshold 0.5 ist logit 0. -> x = -b/w
    if w_guess != 0:
        boundary_x = (np.log(threshold / (1 - threshold)) - b_guess) / w_guess
        ax.axvline(boundary_x, color='red', linestyle='--', alpha=0.5, label=f'Grenze ({boundary_x:.2f}h)')

    # 4. Optimale Kurve
    if st.checkbox("Zeige Scikit-Learn Lösung"):
        ax.plot(X_plot, y_opt_proba, color='green', linestyle=':', linewidth=2, label='Optimal (Sklearn)')

    ax.set_ylabel("Wahrscheinlichkeit P(Bestanden)")
    ax.set_xlabel("Lernstunden")
    ax.set_ylim(-0.1, 1.1)
    ax.legend(loc='center right')
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

with col2:
    st.subheader("Metriken")
    st.metric("Accuracy", f"{accuracy:.1%}")
    
    # Log Loss Berechnung (vereinfacht)
    epsilon = 1e-15
    y_proba_safe = np.clip(y_proba, epsilon, 1 - epsilon)
    log_loss = -np.mean(y * np.log(y_proba_safe) + (1 - y) * np.log(1 - y_proba_safe))
    st.metric("Log Loss", f"{log_loss:.4f}")
    
    st.info("Versuche, die blaue Kurve so zu legen, dass sie bei den Nullen unten und bei den Einsen oben ist.")
    st.latex(r"\sigma(z) = \frac{1}{1+e^{-z}}")