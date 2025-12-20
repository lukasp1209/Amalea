# Unit 05: Optimierung (Gradient Descent & Co.)

Ein neuronales Netz ist nur so gut wie sein Trainingsalgorithmus. In dieser Einheit schauen wir unter die Haube von `model.fit()`.

## Enthaltene Konzepte

### 1. Gradient Descent (Der Klassiker)
*   Die Analogie des Bergsteigers im Nebel.
*   Lernrate: Schrittweite (zu klein = langsam, zu groß = Absturz).

### 2. Probleme von Vanilla GD
*   Lokale Minima und Sattelpunkte.
*   Oszillationen in engen Tälern ("Ravines").

### 3. Moderne Optimierer
*   **Momentum**: Wie eine schwere Kugel, die Schwung aufnimmt. Hilft durch flache Plateaus.
*   **Adam** (Adaptive Moment Estimation): Der Standard. Passt die Lernrate für jeden Parameter individuell an.

## Start der Demo

```bash
cd Vorlesungseinheiten/05_Optimierung
pip install -r requirements.txt
# python code/lab.py
```

## Lab & Übung

*   `notes/script.md`: Detaillierte Erklärung der Algorithmen.
*   `slides/lecture.md`: Folien.
*   `code/lab.py`: Visualisierung von GD vs. Momentum auf einer 2D-Landschaft.