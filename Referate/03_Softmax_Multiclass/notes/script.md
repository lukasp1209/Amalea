# Vorlesungsskript: Softmax & Multiclass Classification

## 1. Motivation
Die Logistische Regression (Unit 02) nutzt die Sigmoid-Funktion, um einen Wert zwischen 0 und 1 zu erzeugen ($P(y=1)$). Das funktioniert super für "Spam vs. Ham".

Aber was ist mit der Ziffernerkennung (0-9) oder der Klassifikation von Blumenarten (Iris Setosa, Versicolor, Virginica)? Wir brauchen ein Modell, das $K$ verschiedene Wahrscheinlichkeiten ausgibt, die sich zu 100% (1.0) summieren.

## 2. Das Modell (Logits)
Statt einem Gewichtsvektor $w$ haben wir nun eine Gewichtsmatrix $W$. Man kann sich das so vorstellen, dass wir für jede der $K$ Klassen eine eigene lineare Funktion haben.

Für jede Klasse $k$ berechnen wir einen Score (genannt **Logit**):
$$ z_k = w_k \cdot x + b_k $$

Diese Scores können beliebige Werte annehmen (z.B. -5.0, 12.4, 0.0).

## 3. Die Softmax-Funktion
Um aus den Scores ($z$) interpretierbare Wahrscheinlichkeiten ($\hat{y}$) zu machen, nutzen wir die Softmax-Funktion. Sie verstärkt die Unterschiede (große Werte werden noch größer) und normiert alles.

$$ \hat{y}_i = \text{Softmax}(z)_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}} $$

**Beispiel:** Scores $z = [2.0, 1.0, 0.1]$
1.  Exponenzieren ($e^z$): $[7.39, 2.71, 1.10]$
2.  Summieren: $7.39 + 2.71 + 1.10 = 11.2$
3.  Normieren (Teilen durch Summe): $[0.66, 0.24, 0.10]$

Ergebnis: Klasse 1 hat 66% Wahrscheinlichkeit.

## 4. Loss Funktion: Categorical Cross-Entropy
Wie trainieren wir das? Wir vergleichen den vorhergesagten Wahrscheinlichkeitsvektor $\hat{y}$ mit dem wahren Vektor $y$ (One-Hot Encoded).

Wenn das Bild eine "Klasse 1" (Index 0) ist, sieht $y$ so aus: $[1, 0, 0]$.
Die Formel für den Loss ist:

$$ J = - \sum_{k=1}^K y_k \log(\hat{y}_k) $$

Da im One-Hot-Vektor $y$ überall Nullen stehen außer bei der richtigen Klasse $t$, fällt die Summe weg und es bleibt nur:

$$ J = - \log(\hat{y}_t) $$

Das heißt: Wir schauen uns nur die Wahrscheinlichkeit an, die das Modell für die **richtige** Klasse vorhergesagt hat, und nehmen davon den negativen Logarithmus.
*   Ist $\hat{y}_t \approx 1$ (sicher richtig), ist $-\log(1) = 0$. (Kein Fehler)
*   Ist $\hat{y}_t \approx 0$ (falsch), ist $-\log(0) \to \infty$. (Großer Fehler)

## 5. Numerische Stabilität (Log-Sum-Exp)
Ein technisches Detail für die Implementierung: $e^{1000}$ führt im Computer zu einem Überlauf (Infinity/NaN).

**Der Trick:**
Mathematisch gilt: $\frac{e^{z_i}}{ \sum e^{z_j} } = \frac{e^{z_i - C}}{ \sum e^{z_j - C} }$ für eine Konstante $C$.
Wir wählen $C = \max(z)$. Damit ist der größte Exponent im Vektor genau 0 ($e^0=1$), und alle anderen sind negativ ($e^{-x}$ ist klein, aber stabil).

## 6. Übungsaufgabe (`code/lab.py`)
1.  Implementieren Sie die `softmax` Funktion.
2.  Berechnen Sie manuell den Loss für ein Beispiel.
3.  Beobachten Sie, wie sich der Loss ändert, wenn das Modell "unsicherer" wird.