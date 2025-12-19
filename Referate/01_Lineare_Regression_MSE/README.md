# Unit 01: Lineare Regression & Mean Squared Error (MSE)

Diese Einheit bildet das Fundament des maschinellen Lernens. Wir betrachten das einfachste Modell (eine Gerade) und die wichtigste Fehlerfunktion (MSE), um zu verstehen, wie Maschinen "lernen" (nämlich durch Minimierung von Fehlern).

## Enthaltene Konzepte

### 1. Das Modell (Hypothese)
*   Wie beschreiben wir Zusammenhänge mathematisch?
*   Formel: $y = w \cdot x + b$ (Steigung & Achsenabschnitt).

### 2. Der Fehler (Loss Function)
*   Wie messen wir, wie "falsch" das Modell liegt?
*   Residuen: Der vertikale Abstand zwischen Datenpunkt und Gerade.
*   **MSE (Mean Squared Error)**: Warum quadrieren wir die Fehler?

### 3. Die Optimierung
*   Wie finden wir die beste Linie? (Intuitiver Einstieg in Gradient Descent).

## Start der Demo-App

Die App erlaubt es, **manuell** eine Regressionsgerade durch eine Punktwolke zu legen und live zu sehen, wie sich der MSE verändert.

```bash
cd Referate/01_Lineare_Regression_MSE
pip install -r requirements.txt
streamlit run app.py
```

## Lab & Übung

*   `notes/script.md`: Ausführliches Skript mit Herleitungen.
*   `code/lab.py`: Python-Implementierung von MSE "from scratch" vs. `scikit-learn`.