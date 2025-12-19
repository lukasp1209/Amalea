"""
Unit 01 Lab: Lineare Regression from Scratch

Aufgabe:
Wir implementieren MSE und eine einfache Vorhersage manuell, 
um zu verstehen, was Scikit-Learn im Hintergrund macht.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Daten generieren
print("--- 1. Daten generieren ---")
X = np.array([[1], [2], [3], [4], [5]])  # Lernstunden
y = np.array([2, 4, 5, 4, 5])            # Notenpunkte (fiktiv)
print(f"X:\n{X}")
print(f"y: {y}")

# 2. Manuelle Vorhersage
print("\n--- 2. Manuelles Modell ---")
# Wir raten mal: y = 0.5 * x + 2
w_guess = 0.5
b_guess = 2.0

def predict(X, w, b):
    return X.flatten() * w + b

y_pred_manual = predict(X, w_guess, b_guess)
print(f"Vorhersage (Manuell): {y_pred_manual}")

# 3. MSE manuell berechnen
print("\n--- 3. MSE Berechnung ---")
residuals = y - y_pred_manual
mse_manual = np.mean(residuals**2)
print(f"Residuen: {residuals}")
print(f"MSE (Manuell): {mse_manual:.4f}")

# 4. Vergleich mit Scikit-Learn (Die "perfekte" Lösung)
print("\n--- 4. Scikit-Learn Lösung ---")
model = LinearRegression()
model.fit(X, y)

y_pred_sklearn = model.predict(X)
mse_sklearn = mean_squared_error(y, y_pred_sklearn)

print(f"Optimale Parameter: w={model.coef_[0]:.2f}, b={model.intercept_:.2f}")
print(f"MSE (Optimal): {mse_sklearn:.4f}")
print(f"Verbesserung gegenüber manuell: {mse_manual - mse_sklearn:.4f}")