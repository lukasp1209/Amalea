# Unit 06: Convolutional Neural Networks (Basics)

Wenn wir Bilder in ein normales neuronales Netz (Dense Layer) füttern, zerstören wir ihre Struktur, indem wir sie in einen langen Vektor flachklopfen. CNNs (Convolutional Neural Networks) lösen dieses Problem.

## Enthaltene Konzepte

### 1. Convolution (Faltung)
*   Statt jedes Pixel mit jedem Neuron zu verbinden, schieben wir einen kleinen Filter (Kernel) über das Bild.
*   **Parameter Sharing**: Der gleiche Filter sucht überall im Bild nach dem gleichen Muster (z.B. einer Kante).

### 2. Filter & Feature Maps
*   Ein Filter lernt einfache Merkmale (Kanten, Ecken).
*   Das Ergebnis der Faltung ist eine **Feature Map**.

### 3. Pooling
*   Reduziert die Bildgröße (Downsampling).
*   Macht das Netz robuster gegen kleine Verschiebungen (Translation Invariance).
*   Max-Pooling ist der Standard.

## Start der Demo

```bash
cd Referate/06_CNN_Basics
pip install -r requirements.txt
# python code/lab.py
```

## Lab & Übung

*   `notes/script.md`: Wie Computer "sehen".
*   `slides/lecture.md`: Visuelle Erklärung von Kernel und Stride.
*   `code/lab.py`: Wir bauen eine Convolution "von Hand" und wenden Kantenerkennungs-Filter auf ein Testbild an.