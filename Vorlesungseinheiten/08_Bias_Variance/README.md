# Unit 08: Bias-Variance Tradeoff

Warum ist ein "perfektes" Modell auf Trainingsdaten oft nutzlos? In dieser Einheit zerlegen wir den Fehler eines Modells in seine mathematischen Bestandteile und lernen, wie wir die Balance finden.

## Enthaltene Konzepte

### 1. Fehler-Zerlegung
*   $Error = Bias^2 + Variance + Noise$
*   **Bias (Verzerrung)**: Fehler durch falsche Annahmen (z.B. Gerade statt Kurve). Führt zu Underfitting.
*   **Variance (Varianz)**: Fehler durch Empfindlichkeit gegenüber kleinen Schwankungen im Training. Führt zu Overfitting.
*   **Noise (Rauschen)**: Der unvermeidbare Fehler in den Daten selbst.

### 2. Der Tradeoff
*   Komplexe Modelle haben wenig Bias, aber hohe Varianz.
*   Einfache Modelle haben wenig Varianz, aber hohen Bias.
*   Das Ziel: Der "Sweet Spot" in der Mitte (Total Error Minimum).

### 3. Lernkurven (Learning Curves)
*   Wie verhalten sich Training- und Test-Error, wenn wir mehr Daten hinzufügen?
*   Diagnose-Tool: Haben wir ein Bias- oder ein Varianz-Problem?

## Start der Demo

```bash
cd Vorlesungseinheiten/08_Bias_Variance
pip install -r requirements.txt
# python code/lab.py
```

## Lab & Übung

*   `notes/script.md`: Mathematische Intuition hinter der Fehlerzerlegung.
*   `slides/lecture.md`: Grafische Darstellung des Tradeoffs (Bullseye-Diagramm).
*   `code/lab.py`: Simulation: Wir ziehen viele Datensätze aus der gleichen Verteilung und sehen, wie unterschiedliche Modelle (linear vs. polynom) schwanken.