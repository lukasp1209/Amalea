import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from models import get_dataset, get_classifier, calculate_metrics

# Page Config
st.set_page_config(page_title="Thema 9: Ensembling", layout="wide")

st.title("🤖 Visualisierung von Ensemble-Methoden")
st.markdown("""
Vergleich von **Single Models** (Decision Tree) gegen **Ensembles** (Random Forest, Gradient Boosting).
Beobachten Sie, wie Ensembles glattere Entscheidungsgrenzen ziehen und robuster gegen Rauschen sind.
""")

# --- Sidebar: Konfiguration ---
st.sidebar.header("1. Datensatz")
dataset_name = st.sidebar.selectbox("Form", ["Moons", "Circles", "Linear"])
noise_level = st.sidebar.slider("Rauschen (Noise)", 0.0, 1.0, 0.3, 0.05)

st.sidebar.header("2. Algorithmus")
algo_type = st.sidebar.selectbox(
    "Modell-Typ",
    ["Decision Tree (Single)", "Random Forest (Bagging)", "Gradient Boosting (Boosting)", "Voting Classifier (Stacking-Light)"]
)

# Dynamische Hyperparameter basierend auf Auswahl
params = {}
if algo_type in ["Decision Tree (Single)", "Random Forest (Bagging)", "Gradient Boosting (Boosting)"]:
    params["max_depth"] = st.sidebar.slider("Max Depth (Baumtiefe)", 1, 15, 5)

if algo_type in ["Random Forest (Bagging)", "Gradient Boosting (Boosting)"]:
    params["n_estimators"] = st.sidebar.slider("Anzahl Bäume (Estimators)", 10, 500, 100, 10)

if algo_type == "Gradient Boosting (Boosting)":
    params["learning_rate"] = st.sidebar.slider("Learning Rate", 0.01, 1.0, 0.1, 0.01)

# --- Main: Training & Plotting ---

# 1. Daten laden
X_train, X_test, y_train, y_test = get_dataset(dataset_name, noise=noise_level)

# 2. Modell trainieren
clf = get_classifier(algo_type, params)
clf.fit(X_train, y_train)

# 3. Metriken
metrics = calculate_metrics(clf, X_test, y_test)

# Layout Spalten
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Performance")
    st.metric("Accuracy (Test)", f"{metrics['accuracy']:.2%}")
    st.metric("Error Rate", f"{metrics['error_rate']:.2%}")
    
    st.info(f"""
    **Modell-Details:**
    *   Typ: {algo_type}
    *   Trainingsdaten: {len(X_train)} Samples
    *   Testdaten: {len(X_test)} Samples
    """)
    
    if algo_type == "Decision Tree (Single)":
        st.warning("Ein einzelner Baum neigt bei hoher Tiefe zu Overfitting (sehr zackige Grenzen).")
    elif algo_type == "Random Forest (Bagging)":
        st.success("Random Forest glättet die Grenzen durch Mittelwertbildung vieler Bäume (Reduzierte Varianz).")
    elif algo_type == "Gradient Boosting (Boosting)":
        st.success("Boosting fokussiert sich auf schwer klassifizierbare Punkte (Reduzierter Bias).")

with col2:
    st.subheader("Entscheidungsgrenze (Decision Boundary)")
    
    # Plotting Logic
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Meshgrid für Hintergrundfarbe
    h = .02
    x_min, x_max = X_train[:, 0].min() - .5, X_train[:, 0].max() + .5
    y_min, y_max = X_train[:, 1].min() - .5, X_train[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    # Vorhersage für jeden Punkt im Grid
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
        
    Z = Z.reshape(xx.shape)
    
    # Contour Plot
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    
    ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)
    
    # Trainingspunkte plotten
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
               edgecolors='k', alpha=0.6, s=40, label="Train")
    # Testpunkte plotten
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
               edgecolors='k', alpha=1.0, s=80, marker='*', label="Test")
    
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
    ax.legend()
    ax.set_title(f"Decision Boundary: {algo_type}")
    
    st.pyplot(fig)