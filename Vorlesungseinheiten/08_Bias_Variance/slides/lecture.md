% Vorlesung Unit 08: Bias-Variance Tradeoff

Slide 1: Das Bullseye-Diagramm
- Stellen Sie sich eine Zielscheibe vor.
- Die Mitte ist die wahre Funktion.
- Unsere Modell-Versuche sind Schüsse.

Slide 2: Bias (Systematischer Fehler)
- Die Schüsse liegen eng beieinander, aber weit weg von der Mitte.
- Das Modell ist "stur" und ignoriert die Datenstruktur.
- Underfitting.

Slide 3: Variance (Streuung)
- Die Schüsse sind weit verstreut um die Mitte herum.
- Im Durchschnitt richtig, aber jeder einzelne Schuss ist unzuverlässig.
- Overfitting.

Slide 4: Der Tradeoff
- Einfache Modelle: Hoher Bias, niedrige Variance.
- Komplexe Modelle: Niedriger Bias, hohe Variance.
- Total Error = Bias² + Variance + Noise.
- Wir suchen den "Sweet Spot".

Slide 5: Diagnose
- Wie wissen wir, was wir haben?
- Wenn Training-Error hoch -> Bias Problem.
- Wenn Training-Error niedrig, aber Test-Error hoch -> Variance Problem.
- "More Data" hilft nur bei Variance, nicht bei Bias!