# Vorlesungsskript: Optimierung

## 1. Die Loss-Landschaft
Das Training eines Modells ist im Grunde die Suche nach dem tiefsten Punkt in einer riesigen Gebirgslandschaft.
*   **Koordinaten**: Die Gewichte $w$ des Modells.
*   **Höhe**: Der Loss $J(w)$.
*   **Ziel**: Finde $w$, wo $J(w)$ minimal ist.

## 2. Gradient Descent (GD)
Da wir die Landschaft nicht komplett sehen (zu viele Dimensionen), tasten wir uns vor.
Der **Gradient** $\nabla J(w)$ zeigt immer in die Richtung des steilsten Anstiegs. Wir gehen also in die entgegengesetzte Richtung.

$$ w_{neu} = w_{alt} - \eta \cdot \nabla J(w_{alt}) $$

*   $\eta$ (Eta): Die **Learning Rate**. Einer der wichtigsten Hyperparameter.

## 3. Stochastic Gradient Descent (SGD)
Berechnet man den Gradienten über *alle* Daten (Batch GD), ist das sehr präzise, aber extrem langsam.
**SGD** nimmt nur ein einziges Beispiel (oder eine kleine Mini-Batch) pro Schritt.
*   Vorteil: Viel schneller, weniger Speicher.
*   Nachteil: Der Weg ist sehr "zittrig" (stochastisch). Das Rauschen kann aber helfen, aus flachen lokalen Minima zu entkommen.

## 4. Momentum
In engen Tälern (Ravines) springt SGD oft wild hin und her, ohne vorwärts zu kommen.
**Momentum** löst das, indem es eine "Geschwindigkeit" $v$ einführt.

$$ v_{neu} = \gamma \cdot v_{alt} + \eta \cdot \nabla J(w) $$
$$ w_{neu} = w_{alt} - v_{neu} $$

*   $\gamma$ (Gamma): Reibung (meist 0.9).
*   Effekt: Wenn der Gradient immer in die gleiche Richtung zeigt, werden wir schneller. Bei Zick-Zack-Bewegungen mitteln sich die Querschläger raus.

## 5. Adam (Adaptive Moment Estimation)
Adam kombiniert die besten Ideen:
1.  **Momentum**: (Wie oben) für die Richtung.
2.  **RMSProp**: Skaliert die Lernrate basierend auf der Varianz der Gradienten.

Das bedeutet: Parameter, die selten Updates bekommen, erhalten größere Schritte. Parameter, die stark schwanken, werden gebremst.
Adam ist heute der "Default"-Optimierer für fast alle Deep Learning Aufgaben.

## 6. Übungsaufgabe (`code/lab.py`)
Wir simulieren eine einfache 2D-Funktion $f(x, y) = x^2 + 10y^2$. Das ist ein enges Tal.
*   Beobachten Sie, wie "Vanilla GD" hin und her springt.
*   Beobachten Sie, wie "Momentum" direkt zur Mitte steuert.