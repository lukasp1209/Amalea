# Unit 03: Softmax Regression (Multiclass)

Bisher konnten wir nur Ja/Nein entscheiden (Logistische Regression). Was aber, wenn wir zwischen Hund, Katze und Maus unterscheiden wollen? Hier kommt die Softmax-Funktion ins Spiel.

## Enthaltene Konzepte

### 1. Von Binär zu Multiklasse
*   Erweiterung der Logistischen Regression auf $K$ Klassen.
*   **One-Hot Encoding**: Wie wir Kategorien mathematisch darstellen (z.B. `[0, 1, 0]` für Klasse 2).

### 2. Die Softmax-Funktion
*   Formel: $\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$
*   Eigenschaften: Transformiert beliebige Zahlen (Logits) in eine Wahrscheinlichkeitsverteilung (Summe = 1).
*   "Soft"-Max: Der größte Wert gewinnt, aber andere behalten eine Restwahrscheinlichkeit (wichtig für das Lernen!).

### 3. Categorical Cross-Entropy
*   Die Loss-Funktion für Mehrklassen-Probleme.
*   Bestraft das Modell, wenn die Wahrscheinlichkeit für die *richtige* Klasse niedrig ist.

## Start der Demo (Optional)

```bash
cd Referate/03_Softmax_Multiclass
pip install -r requirements.txt
# python code/lab.py  <-- Führt das Lab-Skript aus
```

## Lab & Übung

*   `notes/script.md`: Ausführliche Herleitung und Erklärung der numerischen Stabilität.
*   `slides/lecture.md`: Folien für den Vortrag.
*   `code/lab.py`: Implementierung von Softmax und Cross-Entropy "from scratch" in Python.