# Vorlesungsskript: Logistische Regression

## 1. Motivation: Warum nicht einfach eine Gerade?
Angenommen, wir wollen vorhersagen, ob ein Kunde kauft ($y=1$) oder nicht ($y=0$).
Wenn wir Lineare Regression ($y = wx+b$) nutzen, kann das Modell Werte wie 1.5 oder -0.3 ausgeben.

*   Was bedeutet eine Kaufwahrscheinlichkeit von -30%?
*   Was bedeutet 150%?

Wir brauchen eine Funktion, die beliebige Eingaben auf das Intervall $[0, 1]$ "quetscht".

## 2. Die Sigmoid-Funktion
Die Lösung ist die logistische Funktion (Sigmoid):

$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

*   Wenn $z$ sehr groß ist ($z \to \infty$), wird $e^{-z} \to 0$, also $\sigma(z) \to 1$.
*   Wenn $z$ sehr klein ist ($z \to -\infty$), wird $e^{-z} \to \infty$, der Nenner riesig, also $\sigma(z) \to 0$.
*   Wenn $z = 0$, ist $e^0 = 1$, also $\sigma(0) = 0.5$.

Unser Modell wird also:
$$ \hat{y} = \sigma(w \cdot x + b) $$

## 3. Interpretation
Wir interpretieren $\hat{y}$ als die bedingte Wahrscheinlichkeit, dass die Klasse 1 ist:
$$ \hat{y} = P(y=1 | x) $$

Die Entscheidung (Klassifikation) treffen wir meist bei 0.5:
*   Wenn $\hat{y} \ge 0.5 \rightarrow$ Klasse 1
*   Wenn $\hat{y} < 0.5 \rightarrow$ Klasse 0

## 4. Die Kostenfunktion: Log Loss (Cross-Entropy)
Bei der Linearen Regression nutzten wir MSE (quadratischer Fehler). Würden wir das hier tun, bekämen wir eine "wellige" Fehlerlandschaft (nicht-konvex), in der der Gradient Descent stecken bleiben kann.

Stattdessen nutzen wir die **Binary Cross-Entropy**:

$$ J(w,b) = - \frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i)] $$

### Intuition
Betrachten wir einen einzelnen Fall:
*   Wenn das wahre Label $y=1$ ist, fällt der zweite Term weg. Wir wollen $\log(\hat{y})$ maximieren (also $\hat{y}$ nahe 1).
*   Wenn das wahre Label $y=0$ ist, fällt der erste Term weg. Wir wollen $\log(1-\hat{y})$ maximieren (also $\hat{y}$ nahe 0).
*   $\log(0)$ geht gegen $-\infty$. Das bedeutet: Wenn das Modell sich "sicher" ist (z.B. $\hat{y}=0.99$), aber falsch liegt ($y=0$), ist die Strafe (Loss) extrem hoch.

## 5. Praxis-Checkliste

| Eigenschaft | Logistische Regression |
| :--- | :--- |
| **Typ** | Klassifikation (binär, erweiterbar auf Multiclass via Softmax). |
| **Linearität** | Die Entscheidungsgrenze (Decision Boundary) ist linear! |
| **Output** | Kalibrierte Wahrscheinlichkeiten. |
| **Wichtig** | Features sollten skaliert sein (StandardScaler), da $w$ direkt in den Exponenten eingeht. |

## 6. Übungsaufgabe (`code/lab.py`)
1.  Implementieren Sie die `sigmoid` Funktion manuell.
2.  Berechnen Sie den Log Loss für folgende Vorhersage:
    *   Wahrheit: [1, 0, 1]
    *   Modell A: [0.9, 0.1, 0.8] (Gut)
    *   Modell B: [0.6, 0.4, 0.6] (Unsicher)
    *   Modell C: [0.1, 0.9, 0.1] (Falsch und sicher -> Katastrophe)