# Vorlesungsskript: Bias-Variance Tradeoff

## 1. Das Ziel des Lernens
Wir wollen eine Funktion $f(x)$ lernen, die auf **neuen** Daten gut funktioniert (Generalisierung).
Der Fehler auf neuen Daten setzt sich aus drei Komponenten zusammen.

## 2. Die drei Komponenten des Fehlers

### A. Bias (Verzerrung)
*   **Definition**: Der Fehler, der durch zu starke Vereinfachung entsteht.
*   **Beispiel**: Wir versuchen, eine Parabel mit einer geraden Linie zu modellieren. Egal wie viele Daten wir haben, die Gerade wird die Parabel nie perfekt treffen.
*   **Symptom**: Hoher Training-Error (Underfitting).

### B. Variance (Varianz)
*   **Definition**: Der Fehler, der entsteht, weil das Modell zu stark auf die spezifischen Trainingsdaten reagiert.
*   **Beispiel**: Wir verbinden alle Punkte mit einem Zick-Zack-Polynom. Wenn wir neue Datenpunkte ziehen würden, sähe das Polynom komplett anders aus.
*   **Symptom**: Niedriger Training-Error, aber hoher Test-Error (Overfitting).

### C. Irreducible Error (Noise)
*   **Definition**: Rauschen in den Daten (Messfehler, fehlende Informationen).
*   **Eigenschaft**: Kann nicht durch bessere Modelle entfernt werden. Es ist die untere Schranke für den Fehler.

## 3. Die Formel
$$ E[(y - \hat{f}(x))^2] = \text{Bias}[\hat{f}(x)]^2 + \text{Var}[\hat{f}(x)] + \sigma^2 $$

*   $\text{Bias}^2$: Quadratischer Abstand der durchschnittlichen Vorhersage zur Wahrheit.
*   $\text{Var}$: Streuung der Vorhersagen um ihren eigenen Durchschnitt.
*   $\sigma^2$: Das Rauschen.

## 4. Der Tradeoff
Wenn wir die Modellkomplexität erhöhen:
1.  **Bias sinkt**: Das Modell kann die Wahrheit besser abbilden.
2.  **Variance steigt**: Das Modell wird anfälliger für Rauschen.

Wir suchen das Minimum der Summe (U-Kurve).

## 5. Diagnose mit Lernkurven
Wir plotten den Fehler über der Anzahl der Trainingsbeispiele ($m$).

*   **High Bias (Underfitting)**:
    *   Training Error ist hoch.
    *   Validation Error ist hoch.
    *   Beide Kurven nähern sich an, aber auf hohem Niveau.
    *   *Lösung*: Komplexeres Modell, mehr Features.

*   **High Variance (Overfitting)**:
    *   Training Error ist niedrig.
    *   Validation Error ist viel höher.
    *   Große Lücke zwischen den Kurven.
    *   *Lösung*: Mehr Daten, Regularisierung, einfacheres Modell.

## 6. Übungsaufgabe (`code/lab.py`)
Wir führen ein Experiment durch:
1.  Die "Wahrheit" ist eine Sinus-Kurve.
2.  Wir ziehen 100 verschiedene kleine Datensätze aus dieser Wahrheit (mit Rauschen).
3.  Wir trainieren jeweils ein einfaches (Grad 1) und ein komplexes Modell (Grad 9).
4.  Wir visualisieren: Das einfache Modell ist immer ähnlich falsch (Bias). Das komplexe Modell zappelt wild umher (Variance).