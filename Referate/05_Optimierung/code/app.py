import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Unit 05: Optimierer im Vergleich")
st.markdown("Vergleichen Sie **SGD**, **Momentum** und **Adam** auf einer schwierigen Fehlerlandschaft.")

# --- Sidebar ---
st.sidebar.header("Parameter")
lr = st.sidebar.slider("Learning Rate", 0.001, 0.5, 0.02, step=0.001)
steps = st.sidebar.slider("Anzahl Schritte", 10, 200, 50)

st.sidebar.subheader("Momentum Settings")
gamma = st.sidebar.slider("Momentum (Gamma)", 0.0, 0.99, 0.9)

st.sidebar.subheader("Landschaft")
func_type = st.sidebar.selectbox("Funktion", ["Tal (Valley)", "Schüssel (Bowl)"])

# --- Funktionen ---
def get_function(name):
    if name == "Tal (Valley)":
        # x^2 + 10y^2 (Enges Tal)
        f = lambda x, y: x**2 + 10*y**2
        grad = lambda x, y: np.array([2*x, 20*y])
        start = np.array([-8.0, 2.0])
        levels = 20
    else:
        # x^2 + y^2 (Einfache Schüssel)
        f = lambda x, y: x**2 + y**2
        grad = lambda x, y: np.array([2*x, 2*y])
        start = np.array([-8.0, 6.0])
        levels = 15
    return f, grad, start, levels

f, grad_f, start_pos, levels = get_function(func_type)

# --- Optimierer Implementierung ---
def run_sgd(start, lr, steps):
    path = [start]
    pos = start.copy()
    for _ in range(steps):
        g = grad_f(pos[0], pos[1])
        pos = pos - lr * g
        path.append(pos)
    return np.array(path)

def run_momentum(start, lr, steps, gamma):
    path = [start]
    pos = start.copy()
    vel = np.zeros_like(pos)
    for _ in range(steps):
        g = grad_f(pos[0], pos[1])
        vel = gamma * vel + lr * g
        pos = pos - vel
        path.append(pos)
    return np.array(path)

def run_adam(start, lr, steps, beta1=0.9, beta2=0.999, eps=1e-8):
    path = [start]
    pos = start.copy()
    m = np.zeros_like(pos)
    v = np.zeros_like(pos)
    t = 0
    for _ in range(steps):
        t += 1
        g = grad_f(pos[0], pos[1])
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * (g**2)
        
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        
        pos = pos - lr * m_hat / (np.sqrt(v_hat) + eps)
        path.append(pos)
    return np.array(path)

# --- Berechnung ---
path_sgd = run_sgd(start_pos, lr, steps)
path_mom = run_momentum(start_pos, lr, steps, gamma)
path_adam = run_adam(start_pos, lr, steps) # Adam braucht oft kleinere LR, aber wir nutzen hier dieselbe zum Vergleich

# --- Plotting ---
x_range = np.linspace(-10, 10, 100)
y_range = np.linspace(-5, 8, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = f(X, Y)

fig, ax = plt.subplots(figsize=(10, 6))
ax.contour(X, Y, Z, levels=levels, cmap='gray', alpha=0.4)

ax.plot(path_sgd[:, 0], path_sgd[:, 1], 'o-', label='SGD', color='red', markersize=4, alpha=0.7)
ax.plot(path_mom[:, 0], path_mom[:, 1], 'o-', label=f'Momentum (g={gamma})', color='blue', markersize=4, alpha=0.7)
ax.plot(path_adam[:, 0], path_adam[:, 1], 'o-', label='Adam', color='green', markersize=4, alpha=0.7)

ax.set_title(f"Optimierung auf {func_type}")
ax.legend()
ax.grid(True, linestyle=':', alpha=0.3)

st.pyplot(fig)

st.info("""
**Beobachtungen:**
*   **SGD** zick-zackt stark in Tälern.
*   **Momentum** schießt manchmal über das Ziel hinaus, korrigiert sich aber.
*   **Adam** wählt oft einen sehr direkten Weg, da er die Schrittweite pro Dimension anpasst.
""")