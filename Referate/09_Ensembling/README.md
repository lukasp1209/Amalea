# Unit 09: Ensemble Learning Methoden

Diese Vorlesungseinheit behandelt die Theorie und Praxis von Ensemble-Methoden. Sie erklärt, wie die Kombination mehrerer "schwacher" Lerner zu einem starken Prädiktor führt und visualisiert die Unterschiede zwischen Bagging, Boosting und Stacking.

## Enthaltene Konzepte

### 1. Bagging (Bootstrap Aggregating)
*   **Prinzip**: Trainiert mehrere Modelle parallel auf zufälligen Teilmengen der Daten (mit Zurücklegen).
*   **Ziel**: Reduktion der Varianz (gegen Overfitting).
*   **Beispiel**: Random Forest.

### 2. Boosting
*   **Prinzip**: Trainiert Modelle sequenziell, wobei jedes neue Modell versucht, die Fehler des Vorgängers zu korrigieren.
*   **Ziel**: Reduktion des Bias (gegen Underfitting) und der Varianz.
*   **Beispiel**: Gradient Boosting, AdaBoost.

### 3. Stacking / Voting
*   **Prinzip**: Kombiniert die Vorhersagen verschiedener Modelltypen (z.B. SVM + Decision Tree + KNN) durch einen Meta-Lerner oder Mehrheitsentscheid.
*   **Ziel**: Nutzung der Stärken verschiedener Algorithmen.

## Installation & Start

```bash
# In diesen Ordner wechseln
cd Referate/09_Ensembling

# Abhängigkeiten installieren
pip install -r requirements.txt

# App starten
streamlit run app.py
```

## Experimente

Nutzen Sie die Sidebar der App, um:
1.  Die Komplexität des Datasets (Noise) zu erhöhen.
2.  Einen einfachen Decision Tree gegen einen Random Forest antreten zu lassen.
3.  Zu beobachten, wie Gradient Boosting komplexe Grenzen zieht.
4.  Die "Decision Boundary" (Entscheidungsgrenze) live zu visualisieren.