import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

st.title("Unit 08: Bias-Variance Tradeoff")
st.markdown("Finden Sie den 'Sweet Spot' zwischen Underfitting (Bias) und Overfitting (Variance).")

# --- Sidebar ---
st.sidebar.header("Datengenerierung")
n_samples = st.sidebar.slider("Anzahl Datenpunkte", 10, 100, 30)
noise_level = st.sidebar.slider("Rauschen (Noise)", 0.0, 0.5, 0.15)

st.sidebar.header("Modell")
degree = st.sidebar.slider("Polynom-Grad (Komplexität)", 1, 15, 1)

# --- Daten ---
np.random.seed(42)
def true_fun(X):
    return np.cos(1.5 * np.pi * X)

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * noise_level

# Split in Train und Test (wichtig für Bias-Variance Analyse)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- Training ---
polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
linear_regression = LinearRegression()
pipeline = Pipeline([("polynomial_features", polynomial_features),
                     ("linear_regression", linear_regression)])

pipeline.fit(X_train[:, np.newaxis], y_train)

# --- Vorhersage & Fehler ---
X_plot = np.linspace(0, 1, 100)
y_plot = pipeline.predict(X_plot[:, np.newaxis])

train_pred = pipeline.predict(X_train[:, np.newaxis])
test_pred = pipeline.predict(X_test[:, np.newaxis])

train_mse = mean_squared_error(y_train, train_pred)
test_mse = mean_squared_error(y_test, test_pred)

# --- Visualisierung ---
col1, col2 = st.columns([3, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(X_plot, true_fun(X_plot), label="Wahre Funktion", color="green", linestyle="--", alpha=0.6)
    ax.scatter(X_train, y_train, edgecolor='b', s=40, label="Training Data")
    ax.scatter(X_test, y_test, edgecolor='r', s=40, label="Test Data", marker="x")
    ax.plot(X_plot, y_plot, label=f"Modell (Grad {degree})", color="orange", linewidth=2)
    
    ax.set_ylim(-2, 2)
    ax.set_title("Modell-Fit")
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Fehler-Metriken")
    st.metric("Training MSE", f"{train_mse:.4f}")
    st.metric("Test MSE", f"{test_mse:.4f}")
    
    if train_mse > 0.1 and test_mse > 0.1:
        st.warning("⚠️ High Bias (Underfitting)")
    elif train_mse < 0.05 and test_mse > 0.15:
        st.error("⚠️ High Variance (Overfitting)")
    elif test_mse < 0.1:
        st.success("✅ Sweet Spot!")

st.info("""
**Anleitung:**
1.  Starten Sie mit **Grad 1** (Gerade). Beobachten Sie den hohen Fehler bei Training und Test (Underfitting).
2.  Erhöhen Sie auf **Grad 4-5**. Der Test-Fehler sollte sinken (Guter Fit).
3.  Gehen Sie auf **Grad 15**. Der Trainings-Fehler geht gegen 0, aber der Test-Fehler explodiert (Overfitting).
""")