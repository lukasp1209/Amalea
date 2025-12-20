% Vorlesung Unit 06: CNN Basics

Slide 1: Das Problem mit Bildern
- Bilder sind groß (viele Pixel).
- Dense Networks explodieren (zu viele Parameter).
- Räumliche Struktur geht verloren ("Flattening").

Slide 2: Die Lösung - Convolution
- Wir scannen das Bild mit einem kleinen Fenster ("Kernel").
- Wir teilen die Gewichte ("Parameter Sharing").
- Wenn der Filter eine Kante oben links findet, kann er sie auch unten rechts finden.

Slide 3: Was ist ein Filter?
- Eine kleine Matrix (z.B. 3x3).
- Beispiel "Vertikale Kante":
  [[1, 0, -1],
   [1, 0, -1],
   [1, 0, -1]]
- Reagiert stark, wenn links hell und rechts dunkel ist.

Slide 4: Pooling (Max Pooling)
- Wir wollen das Bild verkleinern ("Downsampling").
- Wir nehmen das Maximum aus einem 2x2 Bereich.
- Macht das Netz unempfindlicher gegen kleine Verschiebungen.

Slide 5: Hierarchie der Features
- Erste Layer: Lernt Kanten und Linien.
- Mittlere Layer: Lernt Formen (Augen, Räder).
- Letzte Layer: Lernt Objekte (Gesichter, Autos).