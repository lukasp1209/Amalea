% Vorlesung Unit 02: Logistische Regression

Slide 1: Von Regression zu Klassifikation
- Bisher: "Wie viel?" (Preis, Temperatur) -> Lineare Regression.
- Jetzt: "Ja oder Nein?" (Kauf, Spam, Tumor) -> Logistische Regression.
- Ziel: Wahrscheinlichkeiten vorhersagen.

Slide 2: Das Problem mit der Geraden
- Eine Gerade geht von -unendlich bis +unendlich.
- Wahrscheinlichkeiten müssen zwischen 0 und 1 liegen.
- Lösung: Wir biegen die Gerade zu einem "S".

Slide 3: Die Sigmoid-Funktion
- Formel: $\sigma(z) = 1 / (1 + e^{-z})$
- Wandelt jede Zahl (Logit) in einen Wert zwischen 0 und 1 um.
- 0 wird zu 0.5 (unsicher).
- Große positive Zahlen -> fast 1.
- Große negative Zahlen -> fast 0.

Slide 4: Decision Boundary
- Wo entscheiden wir uns? Meist bei 0.5.
- Das entspricht $z = 0$ bzw. $w \cdot x + b = 0$.
- Die Grenze selbst ist immer noch eine gerade Linie (linearer Klassifikator)!

Slide 5: Log Loss (Cross Entropy)
- MSE ist hier schlecht (nicht konvex).
- Log Loss bestraft "selbstbewusste Fehler" extrem hart.
- Beispiel: Vorhersage 100% "Sicher", aber falsch -> Loss unendlich.

Slide 6: Zusammenfassung
- LogReg ist der Standard für binäre Klassifikation.
- Output sind Wahrscheinlichkeiten (sehr nützlich!).
- Optimierung erfolgt wieder über Gradient Descent.