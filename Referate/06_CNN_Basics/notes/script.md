# Vorlesungsskript: CNN Basics

## 1. Warum nicht einfach Dense Layers?
Ein Bild mit $1000 \times 1000$ Pixeln hat 1 Million Eingabewerte.
Verbinden wir das mit einer Hidden Layer von 1000 Neuronen, bräuchten wir $10^6 \times 10^3 = 1$ Milliarde Gewichte. Das ist nicht trainierbar (und speicherintensiv).

Zudem: Ein Dense Layer weiß nicht, dass Pixel (0,0) und Pixel (0,1) Nachbarn sind. Für ihn sind das einfach $x_0$ und $x_1$ ohne räumlichen Bezug.

## 2. Die Convolution (Faltung)
Die Kernidee: Wir suchen nach lokalen Mustern.
Ein **Kernel** (oder Filter) ist eine kleine Matrix (z.B. $3 \times 3$).
Wir schieben diesen Kernel Schritt für Schritt über das Bild.

$$ (I * K)_{x,y} = \sum_{i=0}^{2} \sum_{j=0}^{2} I_{x+i, y+j} \cdot K_{i,j} $$

*   Das ist im Grunde ein Skalarprodukt zwischen dem kleinen Bildausschnitt und dem Filter.
*   Ist das Muster im Bild ähnlich zum Filter, ist das Ergebnis groß (hohe Aktivierung).

## 3. Filter lernen
In der klassischen Bildverarbeitung (Photoshop) hat man Filter fest programmiert (z.B. Sobel-Filter für Kanten).
In CNNs sind die Werte im Kernel **lernbare Gewichte**. Das Netz lernt selbst, welche Filter nützlich sind (Kanten, Kreise, Texturen).

## 4. Wichtige Parameter
*   **Kernel Size**: Meist $3 \times 3$ oder $5 \times 5$.
*   **Stride**: Die Schrittweite. Stride 1 = Pixel für Pixel. Stride 2 = Wir überspringen jeden zweiten (Bild wird kleiner).
*   **Padding**: Rahmen aus Nullen um das Bild, damit es nicht kleiner wird ("Same Padding").

## 5. Pooling
Nach der Convolution folgt oft eine Pooling-Schicht.
Ziel: Datenmenge reduzieren und Abstraktion erhöhen.

**Max Pooling ($2 \times 2$):**
Wir schauen uns $2 \times 2$ Blöcke an und behalten nur den **größten** Wert.
*   Wirft 75% der Daten weg.
*   Behält nur die Info "Hier war irgendwo eine starke Kante", egal wo genau im 2x2 Block.

## 6. Architektur eines CNN
Typischer Aufbau (wie Lego):
1.  Input Image
2.  Conv Layer (findet Features) + ReLU (Aktivierung)
3.  Pool Layer (macht kleiner)
4.  Conv Layer (findet komplexere Features aus den vorherigen) + ReLU
5.  Pool Layer
6.  Flatten (alles in einen Vektor)
7.  Dense Layer (Klassifikation)
8.  Output (Softmax)