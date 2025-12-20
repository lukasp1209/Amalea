% Vorlesung Unit 03: Softmax & Multiclass

Slide 1: Mehr als zwei Klassen
- Die Welt ist selten binär (Ja/Nein).
- Beispiele: Ziffernerkennung (0-9), Bildklassifikation (ImageNet: 1000 Klassen).
- Ziel: Wir brauchen eine Wahrscheinlichkeitsverteilung über $K$ Klassen.

Slide 2: Von Scores zu Wahrscheinlichkeiten
- Das Modell liefert pro Klasse einen "Score" (Logit) $z$.
- Scores sind schwer zu interpretieren (können negativ sein, summieren nicht zu 1).
- Wir brauchen eine Funktion, die "aufräumt".

Slide 3: Die Softmax-Funktion
- Formel: $\sigma(z)_i = \frac{e^{z_i}}{\sum e^{z_j}}$
- Schritt 1: $e^z$ macht alles positiv.
- Schritt 2: $/ \sum$ sorgt dafür, dass die Summe 1 ist.
- Name "Softmax": Es ist wie eine Maximum-Funktion, aber differenzierbar ("soft").

Slide 4: One-Hot Encoding
- Wie sehen die Labels aus?
- Klasse "Rot" $\rightarrow [1, 0, 0]$
- Klasse "Grün" $\rightarrow [0, 1, 0]$
- Klasse "Blau" $\rightarrow [0, 0, 1]$

Slide 5: Cross-Entropy Loss
- Wir wollen die Wahrscheinlichkeit der *korrekten* Klasse maximieren.
- Loss = $- \log(\text{Wahrscheinlichkeit der richtigen Klasse})$.
- Perfektes Modell: Loss = 0. Schlechtes Modell: Loss = riesig.