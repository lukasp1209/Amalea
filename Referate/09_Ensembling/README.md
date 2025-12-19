# 09_Ensembling — Random Forests & Gradient Boosting

Kurzbeschreibung

Dieses Muster‑Referat behandelt Ensembling‑Methoden mit Fokus auf Random Forests und Gradient Boosting. Ziel ist eine kurze Einführung in die Ideen, typische Einsatzfälle, Vor‑ und Nachteile sowie eine kompakte Demo mit sklearn.

Was enthalten ist

- `slides/` — Stichwort‑Folien als `slides.md` (Stub).
- `notes/handout.md` — 4‑Seiten‑Handout‑Template (Markdown).
- `code/demo.ipynb` — lauffähiges Demo‑Notebook (Iris/Breast Cancer, RF vs GB).
- `code/requirements.txt` — benötigte Python‑Pakete.
- `assets/` — Grafiken/Plots, falls benötigt.

Vorschlag zur Demonstration

- Datensatz: `sklearn.datasets.load_iris` (kurze Demo) oder `load_breast_cancer` für einen binären Use‑Case.
- Modelle: `RandomForestClassifier`, `GradientBoostingClassifier` (sklearn implementation).
- Experimente: Train/Test accuracy, 5‑fold Cross‑Validation, Feature importances, Lernkurve (Training vs Validation), kurze Discussion der Hyperparameter‑Einflüsse.

Lieferumfang (jetzt ausführlich):

- `slides/slides.md`: ausgearbeitete Folienstruktur (≤12 Folien).
- `notes/handout.md` + `notes/handout.pdf`: vollständiges 4‑Seiten‑Handout.
- `code/demo.ipynb`: ausführliches Notebook (EDA, Training, CV, Plots) — speichert Plots in `assets/`.
- `code/demo_run.py`: skriptfähige Version, erzeugt dieselben Plots und ein `results.txt`.
- `code/requirements.txt`: benötigte Pakete.
- `assets/`: generierte PNGs (feature_importances.png, learning_curve_rf.png).

Lizenz / Quellen

- Implementierung: scikit‑learn Beispiele, modifiziert und dokumentiert für Lehrzwecke.

Reproduzieren der Ergebnisse

1) Mit dem Skript (headless, empfohlen):

```
cd Referate/09_Ensembling/code
python demo_run.py
```

Das Skript erzeugt Plots in `Referate/09_Ensembling/assets/` (z. B. `feature_importances.png`, `learning_curve_rf.png`) und schreibt `code/results.txt` mit den wichtigsten Kennzahlen.

2) Notebook interaktiv / ausgeführt:

Wenn du das Notebook interaktiv ausführen möchtest, kannst du die ausgeführte Version öffnen: `Referate/09_Ensembling/code/executed_demo.ipynb` (wurde via `nbconvert --execute` erstellt). Falls du selbst ausführen willst, aktiviere die Projekt‑venv und starte Jupyter:

```
source .venv/bin/activate
jupyter notebook Referate/09_Ensembling/code/demo.ipynb
```

Hinweis: für die automatische Ausführung mit `nbconvert` habe ich im venv einen Kernel (`amalea-venv`) registriert; falls du die Ausführung auf einem anderen System machst, registriere ggf. den Kernel entsprechend oder nutze `demo_run.py`.
