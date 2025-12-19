% Vorlesung Unit 01: Lineare Regression

Slide 1: Willkommen
- Thema: Lineare Regression & MSE
- Ziel: Verstehen, wie Maschinen "Linien ziehen"

Slide 2: Das Szenario
- Wir haben Datenpunkte (x, y).
- Wir suchen einen Zusammenhang.
- Annahme: Es ist eine Gerade.

Slide 3: Die Mathematik
- Modell: y = wx + b
- Parameter: w (Steigung), b (Verschiebung)
- Das ist alles, woran wir "drehen" können.

Slide 4: Der Fehler (Loss)
- Wie gut ist eine Linie?
- Wir messen den Abstand (Residuum) jedes Punktes zur Linie.
- MSE = Durchschnitt der Quadrate dieser Abstände.

Slide 5: Warum MSE?
- Konvex (hat nur ein Minimum -> gut zu finden).
- Differenzierbar (wichtig für Gradient Descent).
- Bestraft grobe Schnitzer stark.

Slide 6: Zusammenfassung
- Lineare Regression sucht die Linie mit dem kleinsten MSE.
- In Python: `sklearn.linear_model.LinearRegression`.
- Nächster Schritt: Wie finden wir das Minimum automatisch? (Gradient Descent).