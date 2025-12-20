# Deep Learning Curriculum (Modulkatalog)

Willkommen im Repository für die Deep Learning Vorlesungseinheiten.
Dieser Ordner enthält detaillierte Lehrmaterialien, Skripte und interaktive Labs.

## Übersicht der Einheiten

### Grundlagen (Supervised Learning)
*   **[Unit 01: Lineare Regression](01_Lineare_Regression_MSE/)** - Das Fundament: Modelle, Loss-Funktionen (MSE) und Fitting.
*   **[Unit 02: Logistische Regression](02_Logistische_Regression/)** - Klassifikation, Sigmoid und Cross-Entropy.
*   **[Unit 03: Softmax & Multiclass](03_Softmax_Multiclass/)** - Erweiterung auf $K$ Klassen (z.B. Ziffernerkennung).

### Training & Tuning
*   **[Unit 04: Regularisierung](04_Regularisierung/)** - Kampf dem Overfitting: L1 (Lasso) und L2 (Ridge).
*   **[Unit 05: Optimierung](05_Optimierung/)** - Wie Netze lernen: Gradient Descent, Momentum und Adam.
*   **[Unit 08: Bias-Variance Tradeoff](08_Bias_Variance/)** - Theorie: Fehlerzerlegung und Lernkurven-Diagnose.
*   **[Unit 09: Ensembling](09_Ensembling/)** - Teamwork: Random Forests und Gradient Boosting.

### Deep Learning Architekturen
*   **[Unit 06: CNN Basics](06_CNN_Basics/)** - Computer Vision: Convolution, Filter und Pooling.
*   **[Unit 07: Attention & Transformer](07_Attention/)** - NLP: Der Mechanismus hinter ChatGPT & Co.

## Nutzung

Jede Unit folgt der gleichen Struktur:
1.  `README.md`: Einführung und Start-Anleitung.
2.  `notes/script.md`: Ausführliches Vorlesungsskript.
3.  `slides/lecture.md`: Folien für den Vortrag.
4.  `code/lab.py`: Python-Skript für Experimente ("Lab").
5.  `code/app.py`: Interaktive Streamlit-App (Starten mit `streamlit run code/app.py`).
6.  `requirements.txt`: Benötigte Python-Bibliotheken.