% Vorlesung Unit 05: Optimierung

Slide 1: Der Bergsteiger im Nebel
- Wir wollen den Loss minimieren.
- Wir sehen nicht die ganze Landschaft, nur die Steigung unter unseren Füßen.
- Strategie: Gehe immer bergab (Gradient Descent).

Slide 2: Learning Rate (Schrittweite)
- Zu klein: Wir brauchen ewig, um anzukommen.
- Zu groß: Wir überspringen das Tal und landen auf der anderen Seite (Divergenz).
- Just Right: Schneller Abstieg, langsame Konvergenz am Ende.

Slide 3: SGD vs. Batch
- Batch GD: Nutzt alle Daten für einen Schritt. (Präzise, langsam).
- SGD: Nutzt ein Beispiel pro Schritt. (Rauschig, schnell).
- Mini-Batch: Der Kompromiss (z.B. 32 Beispiele). Standard im Deep Learning.

Slide 4: Das Problem mit Tälern
- In engen Tälern oszilliert GD stark zwischen den Wänden.
- Lösung: **Momentum**.
- Wir nehmen Schwung mit. Das glättet die Oszillationen und beschleunigt die Richtung zum Ziel.

Slide 5: Adam
- Der "Alleskönner".
- Kombiniert Momentum mit adaptiven Lernraten.
- Muss man fast nie tunen (Standard LR = 0.001).
- Funktioniert "out of the box" für die meisten Probleme gut.