# 🐍 Woche 1: Python & Data Science Fundamentals

> 🚀 **Dein Ziel:**
>
> Vom "Skript-Bastler" zum **Data Science Engineer**.
> In dieser Woche legst du das Fundament für professionelle Daten-Projekte: Reproduzierbar, strukturiert und bereit für die Cloud.

## 💡 Warum dieser Tech-Stack?

Wir setzen auf den **Industrie-Standard**:
1.  **Python & Pandas:** Das "Excel auf Steroiden" für Datenanalyse.
2.  **Streamlit:** Der schnellste Weg von Daten zur Web-App (ohne HTML/CSS!).
3.  **Docker:** Damit deine App überall läuft (nie wieder "It works on my machine").
4.  **QUA³CK:** Ein Prozessmodell, das Chaos in Struktur verwandelt.

---

## 🗺️ Deine Roadmap

Arbeite die Inhalte in dieser Reihenfolge durch:

### 1️⃣ Die Basics (Theorie & Praxis)
- **`00_Python_in_3_Stunden.ipynb`**
  - *Lernziel:* Python-Syntax auffrischen und Daten mit Pandas bändigen.
  - *Highlight:* Visualisierung mit Plotly vs. Matplotlib.

### 2️⃣ Die Infrastruktur (DevOps)
- **`01_Docker_für_Data_Science.ipynb`**
  - *Lernziel:* Verstehen, wie man Data-Science-Umgebungen containerisiert.
  - *Output:* Ein `Dockerfile` und `docker-compose.yml` für dieses Projekt.

### 3️⃣ Die Methodik (Process)
- **`03_QUA3CK_Prozessmodell.ipynb`**
  - *Lernziel:* ML-Projekte professionell planen (Question -> Understand -> ...).
  - *Highlight:* Integration von MLFlow und Experiment-Tracking.

### 4️⃣ Das Produkt (Deployment)
- **`uebungs_app.py`**
  - *Was:* Deine erste Streamlit-App (Dashboard).
  - *Aufgabe:* Starte sie und passe sie an!

> 📚 **Cheat-Sheet:** Nutze `02_Glossar_Alle_Begriffe_erklärt.ipynb` als dein ständiges Nachschlagewerk für Fachbegriffe.

---

## 🛠️ Setup & Start

Du hast zwei Möglichkeiten, mit diesem Repo zu arbeiten:

### Option A: Die App starten (via Docker) 🐳
Perfekt, um das Endergebnis zu sehen und die Umgebung zu testen.

```bash
# 1. Container bauen und starten
docker-compose up --build

# 2. App im Browser öffnen
# http://localhost:8501
```

### Option B: Notebooks bearbeiten (Lokal) 💻
Um die `.ipynb` Dateien interaktiv zu lernen:

```bash
# 1. Abhängigkeiten installieren
pip install -r requirements.txt

# 2. Jupyter Lab starten
jupyter lab

# 3. Tests ausführen (optional)
make test
```

### Option C: Makefile-Befehle verwenden 🛠️
Für häufige Aufgaben stehen Makefile-Befehle zur Verfügung:

```bash
make help          # Zeige alle verfügbaren Befehle
make install       # Abhängigkeiten installieren
make run           # Übungs-App starten
make test          # Tests ausführen
make clean         # Temporäre Dateien aufräumen
make docker-build  # Docker-Image bauen
```

---

## ⚠️ Wichtige Hinweise

1.  **Streamlit vs. Notebooks:**
    Streamlit-Code (`st.write`, etc.) funktioniert **nicht** in Jupyter Notebooks. Schreibe ihn immer in `.py` Dateien (wie `uebungs_app.py`) und führe sie via Terminal aus.

2.  **Docker Troubleshooting:**
    Falls Ports belegt sind, stoppe andere Container mit `docker stop $(docker ps -q)`.

---

## 🧪 Qualitätssicherung

### Code-Standards
- Alle Python-Dateien folgen **PEP 8** Konventionen
- Umfassende **Docstrings** für bessere Dokumentation
- **Type Hints** wo sinnvoll (in zukünftigen Versionen)

### Tests
Führe die Unit-Tests aus:
```bash
make test
# oder
python -m pytest tests/
```

### Linting & Formatierung
```bash
# Installation (einmalig)
pip install flake8 black isort

# Code formatieren
black *.py tests/
isort *.py tests/

# Linting
flake8 *.py tests/
```
