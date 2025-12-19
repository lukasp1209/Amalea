# Code — Kurzanleitung

Kurz: Zwei Wege, die Demo auszuführen — headless (empfohlen) oder interaktiv (Notebook).

Voraussetzung

- Aktiviere das Projekt‑venv und installiere Abhängigkeiten:

```
source .venv/bin/activate
pip install -r requirements.txt
```

1) Headless (empfohlen)

```
python demo_run.py
```

Erwartete Outputs (im Ordner `../assets/` bzw. `.`):
- `../assets/feature_importances.png`
- `../assets/learning_curve_rf.png`
- `results.txt` (zusammenfassende Kennzahlen, im selben Ordner wie `demo_run.py`)

2) Interaktiv (Notebook)

```
jupyter notebook demo.ipynb
```

- Optional: die ausgeführte Kopie `executed_demo.ipynb` liegt bereits im Ordner und zeigt die erzeugten Outputs.

Hinweis

- Wenn `nbconvert --execute` benutzt wird, muss ein Jupyter‑Kernel für die venv vorhanden sein (ich habe `amalea-venv` installiert). Falls Probleme auftreten, nutze den headless‑Modus.
