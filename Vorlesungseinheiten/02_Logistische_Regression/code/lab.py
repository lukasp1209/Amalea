"""
Unit 02 Lab: Logistische Regression from Scratch

Aufgabe:
Wir implementieren die Sigmoid-Funktion und den Cross-Entropy Loss manuell.
"""

import numpy as np
from sklearn.metrics import log_loss

# 1. Die Sigmoid Funktion
print("--- 1. Sigmoid Funktion ---")

def sigmoid(z):
    # TODO: Implementieren Sie die Formel 1 / (1 + e^-z)
    return 1 / (1 + np.exp(-z))

z_values = np.array([-5, -1, 0, 1, 5])
activations = sigmoid(z_values)

print(f"Inputs (z): {z_values}")
print(f"Outputs (p): {activations}")
print("Erwartet bei 0: 0.5")

# 2. Cross-Entropy Loss (Log Loss)
print("\n--- 2. Log Loss Berechnung ---")

y_true = np.array([1, 0, 1, 1])
# Modellvorhersagen (Wahrscheinlichkeiten für Klasse 1)
y_pred_good = np.array([0.9, 0.1, 0.8, 0.95])
y_pred_bad  = np.array([0.1, 0.9, 0.3, 0.4])

def calculate_log_loss(y_true, y_pred):
    # Clipping um log(0) zu vermeiden
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    # Formel: -mean(y * log(p) + (1-y) * log(1-p))
    loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

loss_good = calculate_log_loss(y_true, y_pred_good)
loss_bad = calculate_log_loss(y_true, y_pred_bad)

print(f"Loss (Gutes Modell): {loss_good:.4f}")
print(f"Loss (Schlechtes Modell): {loss_bad:.4f}")

# 3. Vergleich mit Scikit-Learn
print("\n--- 3. Scikit-Learn Check ---")
sklearn_loss = log_loss(y_true, y_pred_good)
print(f"Sklearn Loss: {sklearn_loss:.4f}")
print(f"Differenz: {loss_good - sklearn_loss:.10f}")