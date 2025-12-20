import numpy as np

def softmax(z):
    """
    Berechnet die Softmax-Funktion für einen Vektor z.
    Nutzt den max(z) Trick für numerische Stabilität.
    """
    # 1. Shift z um max(z) abzuziehen (verhindert Overflow bei exp)
    shift_z = z - np.max(z)
    
    # 2. Exponenzieren
    exp_z = np.exp(shift_z)
    
    # 3. Normalisieren
    return exp_z / np.sum(exp_z)

def cross_entropy_loss(y_pred, target_class_index):
    """
    Berechnet den Cross-Entropy Loss für ein einzelnes Beispiel.
    y_pred: Vektor der vorhergesagten Wahrscheinlichkeiten.
    target_class_index: Der Index der wahren Klasse (Integer).
    """
    # Vermeidung von log(0) durch Clipping
    epsilon = 1e-12
    p = np.clip(y_pred[target_class_index], epsilon, 1.0)
    
    return -np.log(p)

# --- DEMO ---

print("--- Softmax Demo ---")
# Beispiel-Logits (Scores) vom Modell
logits = np.array([2.0, 1.0, 0.1])
print(f"Logits (Scores): {logits}")

probs = softmax(logits)
print(f"Wahrscheinlichkeiten (Softmax): {probs}")
print(f"Summe der Wahrscheinlichkeiten: {np.sum(probs):.2f}")

print("\n--- Loss Demo ---")
# Szenario 1: Die wahre Klasse ist 0 (der höchste Score)
loss_good = cross_entropy_loss(probs, 0)
print(f"Loss wenn Klasse 0 richtig ist (Modell hatte Recht): {loss_good:.4f}")

# Szenario 2: Die wahre Klasse ist 2 (der niedrigste Score)
loss_bad = cross_entropy_loss(probs, 2)
print(f"Loss wenn Klasse 2 richtig ist (Modell lag falsch):  {loss_bad:.4f}")
print("-> Der Loss bestraft den Fehler stark!")