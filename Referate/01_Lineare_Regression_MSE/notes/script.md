# Vorlesungsskript: Lineare Regression & MSE

## 1. Einführung
Die Lineare Regression ist der "Hello World"-Algorithmus des Supervised Learning. Ziel ist es, einen kontinuierlichen Zielwert (Target $y$) basierend auf einem Eingabewert (Feature $x$) vorherzusagen.

Beispiele:
*   Wohnfläche ($x$) $\rightarrow$ Hauspreis ($y$)
*   Lernzeit ($x$) $\rightarrow$ Klausurnote ($y$)

## 2. Das Modell
Wir nehmen an, dass der Zusammenhang linear ist. Unsere Hypothese $h(x)$ lautet:

$$ \hat{y} = w \cdot x + b $$

*   $w$ (Weight/Slope): Wie stark ändert sich $y$, wenn $x$ steigt?
*   $b$ (Bias/Intercept): Welchen Wert hat $y$, wenn $x=0$ ist?
*   $\hat{y}$: Die Vorhersage unseres Modells (im Gegensatz zum echten $y$).

## 3. Die Kostenfunktion (Loss Function)
Um die besten Werte für $w$ und $b$ zu finden, müssen wir definieren, was "gut" bedeutet. In der Regression nutzen wir meist den **Mean Squared Error (MSE)**.

### Warum quadrieren?
Der Fehler für einen einzelnen Punkt ist $e_i = y_i - \hat{y}_i$.
1.  **Vorzeichen eliminieren**: Würden wir nur summieren ($\sum (y - \hat{y})$), könnten sich Fehler von +10 und -10 zu 0 aufheben. Das Modell wäre "perfekt", obwohl es falsch liegt.
2.  **Bestrafung großer Fehler**: Durch das Quadrat $(10)^2 = 100$ vs $(1)^2 = 1$ fallen Ausreißer stärker ins Gewicht.

### Die Formel
$$ J(w, b) = \frac{1}{N} \sum_{i=1}^{N} (y_i - (w x_i + b))^2 $$

## 4. Optimierung (Wie lernt die Maschine?)
Wir suchen das Paar $(w, b)$, das $J(w, b)$ minimiert.

### Analytische Lösung (Normal Equation)
Für einfache Lineare Regression gibt es eine geschlossene Formel:
$$ w = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
Das ist schnell für kleine Datenmengen, wird aber bei Millionen von Features (Matrix-Inversion) zu langsam.

### Numerische Lösung (Gradient Descent)
Das ist der Standard für Deep Learning.
1.  Starte mit zufälligem $w, b$.
2.  Berechne den Gradienten (die Steigung der Fehlerlandschaft).
3.  Gehe einen kleinen Schritt entgegen dem Gradienten.
4.  Wiederhole.

## 5. Praxis-Checkliste

| Frage | Antwort |
| :--- | :--- |
| **Wann nutzen?** | Bei einfachen Zusammenhängen, als Baseline-Modell. |
| **Vorteile** | Sehr schnell, leicht interpretierbar ($w$ zeigt Wichtigkeit). |
| **Nachteile** | Kann nur lineare Zusammenhänge lernen (keine Kurven ohne Feature Engineering). |
| **Annahmen** | Homoskedastizität (gleiche Varianz der Fehler), keine Multikollinearität. |

## 6. Übungsaufgabe
Öffnen Sie `code/lab.py` und versuchen Sie:
1.  Das Rauschen (`noise`) in der Datengenerierung zu erhöhen. Wie verändert sich der MSE?
2.  Implementieren Sie eine Funktion `calculate_mae` (Mean Absolute Error) und vergleichen Sie.