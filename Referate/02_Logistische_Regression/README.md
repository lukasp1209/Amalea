# Unit 02: Logistische Regression (Klassifikation)

Nachdem wir gelernt haben, Zahlen vorherzusagen (Regression), wollen wir nun Entscheidungen treffen: Ja oder Nein? Spam oder Ham? Krank oder Gesund?

## Enthaltene Konzepte

### 1. Das Problem mit der Geraden
*   Warum Lineare Regression für Klassifikation (0 oder 1) scheitert.
*   Der Bedarf nach einer Funktion, die Werte zwischen 0 und 1 ausgibt.

### 2. Die Sigmoid-Funktion (Aktivierung)
*   Die S-Kurve: $\sigma(z) = \frac{1}{1 + e^{-z}}$
*   Interpretation als Wahrscheinlichkeit $P(y=1|x)$.

### 3. Cross-Entropy Loss (Log Loss)
*   Warum MSE hier nicht gut funktioniert (nicht konvex).
*   Die Bestrafung von "sicheren, aber falschen" Vorhersagen.

## Start der Demo-App

Visualisieren Sie die "S-Kurve" und versuchen Sie, Datenpunkte (Bestanden/Durchgefallen) manuell zu trennen.

```bash
cd Referate/02_Logistische_Regression
pip install -r requirements.txt
streamlit run app.py
```

## Lab & Übung

*   `notes/script.md`: Herleitung der Formeln und Gradienten-Update-Regeln.
*   `code/lab.py`: Implementierung der Sigmoid-Funktion und des Log-Loss "from scratch".