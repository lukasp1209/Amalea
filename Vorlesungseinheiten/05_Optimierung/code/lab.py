import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    """Eine Funktion mit einem engen Tal: f(x,y) = x^2 + 10y^2"""
    return x**2 + 10 * y**2

def grad_f(x, y):
    """Der Gradient von f: [2x, 20y]"""
    return np.array([2*x, 20*y])

def run_gd(start_pos, lr, steps=20):
    path = [start_pos]
    pos = np.array(start_pos)
    for _ in range(steps):
        grad = grad_f(pos[0], pos[1])
        pos = pos - lr * grad
        path.append(pos)
    return np.array(path)

def run_momentum(start_pos, lr, gamma=0.9, steps=20):
    path = [start_pos]
    pos = np.array(start_pos)
    velocity = np.zeros_like(pos)
    for _ in range(steps):
        grad = grad_f(pos[0], pos[1])
        velocity = gamma * velocity + lr * grad
        pos = pos - velocity
        path.append(pos)
    return np.array(path)

# --- Visualisierung ---
def plot_paths():
    # Gitter für Contour Plot
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-4, 4, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    start = [-9.0, 3.0] # Startpunkt weit außen
    
    # 1. Vanilla Gradient Descent
    # LR 0.08 ist hier kritisch: für x okay, für y (Faktor 10 steiler) fast zu viel
    path_gd = run_gd(start, lr=0.08, steps=30)
    
    # 2. Momentum
    path_mom = run_momentum(start, lr=0.01, gamma=0.9, steps=30)

    plt.figure(figsize=(10, 6))
    plt.contour(X, Y, Z, levels=20, cmap='viridis', alpha=0.6)
    
    # Plot GD
    plt.plot(path_gd[:, 0], path_gd[:, 1], 'o-', color='red', label='Vanilla GD (LR=0.08)')
    
    # Plot Momentum
    plt.plot(path_mom[:, 0], path_mom[:, 1], 'o-', color='blue', label='Momentum (LR=0.01, g=0.9)')
    
    plt.title("Optimierung in einem engen Tal (x^2 + 10y^2)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    
    print("Plot wird erstellt...")
    plt.show()
    print("Beobachtung: GD oszilliert stark (Zick-Zack), Momentum läuft geschmeidiger zur Mitte (0,0).")

if __name__ == "__main__":
    plot_paths()