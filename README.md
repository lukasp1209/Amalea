# 🎓 AMALEA 2025 - Data Analytics & Big Data

<div align="center">
  <img src="./kurs-logo.png" alt="AMALEA 2025 Logo" width="400">
  <br><br>
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/MLflow-Tracking-orange?logo=mlflow&logoColor=white" alt="MLflow">
  <img src="https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?logo=tensorflow&logoColor=white" alt="TensorFlow">
  <img src="https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?logo=huggingface&logoColor=white" alt="Hugging Face">
</div>

**Der modernisierte Data-Science-Kurs für Entwickler & Analysten**

> 🚀 **Dein Ziel:**
>
> Von Python-Basics zu **Production-Grade ML-Systemen**.
> In 7 Wochen baust du ein Portfolio aus **8 interaktiven Apps**, trainierst neuronale Netze und deployest alles in die Cloud.
>
> **Kein "Spaghetti-Code" in Notebooks, sondern sauberes Software-Engineering für Daten.**

## 🧭 Worum es geht (Kurzüberblick)

AMALEA führt dich in 7 Wochen von Python-Grundlagen bis zum Deployment einer ML-API mit Dashboards. Das Repo ist in Wochen gegliedert:
- **Notebooks**: Schritt-für-Schritt-Anleitungen mit Erklärungen, Übungen und Executed-Versionen, damit du sofort Ergebnisse siehst.
- **Streamlit-Apps**: Interaktive Demos pro Woche, um Modelle, Visualisierungen und Workflows auszuprobieren.
- **Backend & MLOps** (W07): Eine FastAPI-Demo mit MLflow-Integration und zwei Dashboards (Monitoring, NLP), plus Compose-Stack für lokalen Start.
- **Requirements pro Woche**: Schlanke Installationen, damit du nur das lädst, was du brauchst (W01–W03 leicht, W04 MLOps, W05 DL, W06 CV/NLP, W07 Deployment).

So nutzt du den Kurs:
1) **Woche starten:** Lies das Kernnotebook der Woche (Executed-Version als Referenz), danach selbst ausführen und Übungen lösen.  
2) **App ausprobieren:** Öffne die passende Streamlit-App für schnelles Experimentieren (Features schieben, Modelle testen).  
3) **Variieren & dokumentieren:** Ändere Hyperparameter/Features, logge Ergebnisse (W04/W07 mit MLflow) und notiere Learnings in kurzen Markdown-Notizen.  
4) **Deployment üben (W07):** Starte die FastAPI + Dashboards lokal oder via Compose, spiele den Demo/Live-Schalter durch und inspiziere Requests/Responses.  
5) **Portfolio bauen:** Sammle Screenshots, kurze Beschreibungen und Metrikvergleiche; jedes Wochenziel ergibt einen Baustein für dein Portfolio.

## 📚 Pädagogische Einführung: Themen, Konzepte, Tools

AMALEA ist so gebaut, dass du in jeder Woche ein in sich geschlossenes Lernpaket aus Notebook und App bekommst. In W01–W02 übst du sauberen Python-Code, den QUA³CK-Prozess und Daten-Transformationen mit Pandas/NumPy; Streamlit dient als Brücke, um sofort interaktive Ergebnisse zu sehen. W03–W04 vertiefen klassisches ML: Sklearn-Pipelines, Klassifikation/Regression, Ensembles, Clustering und Anomalie-Detektion. Hier lernst du, Metriken zu interpretieren, mit MLflow zu tracken und erste Versionierung von Daten/Artefakten mit DVC zu probieren. W05 führt dich in Deep Learning mit Keras (Sequential/Functional API), Initialisierung/Regularisierung und leichtem Transfer Learning; du übst, Overfitting zu erkennen und Seeds konsistent zu halten. In W06 folgen Computer Vision und NLP: CNN-Grundlagen, Augmentation, OpenCV-Feature-Extraction, Transfer-Learning-Patterns sowie eine CPU-freundliche Transformers-Demo für Text. W07 bündelt alles in einem Deployment-Modul: FastAPI für Inference, leichte HF-Pipelines für Sentiment/QA/Generate, zwei Streamlit-Dashboards für Monitoring/NLP und ein Compose-Stack. Durch Week-Requirements und Lockfiles bleiben Umgebungen reproduzierbar; jede Woche liefert ein lauffähiges Notebook plus App, Executed-Versionen erleichtern den Einstieg, und mit MLflow dokumentierst du deine Experimente. So entsteht Schritt für Schritt ein konsistentes Portfolio.

**Wie du lernen kannst**
- Folge Woche für Woche; jede Woche hat ein klares Ziel, ein Kernnotebook und eine kleine App.
- Starte mit den Executed-Notebooks, führe dann selbst aus und variiere Parameter.
- Baue jede Woche mindestens einen kleinen "Try it" Task (siehe Notebook-Übungen) und dokumentiere dein Ergebnis kurz im Repo (Markdown).
- Nutze Streamlit-Apps zum schnellen Experimentieren, bevor du Code ins Notebook überträgst.
- Verwende `mlflow` (W04/W07) für Metrik-Vergleiche und halte Seed-Konfigurationen bei.

---

## 📋 Inhaltsverzeichnis

- [Der Tech-Stack](#-der-tech-stack-industrie-standard)
- [Deine Roadmap](#-deine-roadmap-7-wochen)
- [Quick Start](#-quick-start-docker)
- [Repository-Struktur](#-repository-struktur)
- [Kursinhalte & Portfolio](#-kursinhalte--portfolio-projekte)
- [Support](#-support)

---

##  Der Tech-Stack (Industrie-Standard)

Wir nutzen Tools, die du auch im Job finden wirst:

| Kategorie | Tools | Warum? |
|---|---|---|
| **Core** | 🐍 Python 3.11+, Pandas, NumPy | Der Gold-Standard für Data Science. |
| **ML & AI** | 🤖 Scikit-Learn, TensorFlow, Hugging Face | Von klassischem ML bis zu modernen Transformern. |
| **App** | 🎈 Streamlit | Der schnellste Weg von Daten zur Web-App. |
| **Ops** | 🐳 Docker, MLflow | Reproduzierbare Umgebungen & Experiment-Tracking. |
| **Process** | 🦆 QUA³CK | Ein Framework, das Chaos in Struktur verwandelt. |

---

## 🗺️ Deine Roadmap (7 Wochen)

Der Kurs ist modular aufgebaut. Jede Woche liefert ein fertiges Projekt für dein Portfolio.

### Phase 1: Foundations & Engineering
*   **📂 Woche 01: Python & QUA³CK**
    *   *Focus:* Clean Code, Docker-Setup, Projekt-Strukturierung.
*   **📂 Woche 02: Data Apps**
    *   *Focus:* Interaktive Dashboards mit Streamlit & Pandas.

### Phase 2: Machine Learning Core
*   **📂 Woche 03: ML Engineering**
    *   *Focus:* Scikit-Learn Pipelines, Klassifikation & Regression.
*   **📂 Woche 04: Advanced Algorithms**
    *   *Focus:* Ensemble Methods, Unsupervised Learning, MLOps.

### Phase 3: Deep Learning & AI
*   **📂 Woche 05: Neural Networks**
    *   *Focus:* TensorFlow/Keras, Deep Learning Grundlagen.
*   **📂 Woche 06: Computer Vision & NLP**
    *   *Focus:* CNNs, Transformer, Hugging Face.

### Phase 4: Production
*   **📂 Woche 07: Deployment**
    *   *Focus:* Cloud-Deployment, Model Serving, Finales Portfolio.

---

## 🛠️ Quick Start (Docker)

### Voraussetzungen
*   [Docker Desktop](https://www.docker.com/products/docker-desktop) installiert und laufend.
*   [Git](https://git-scm.com/) installiert.

Die einfachste Art zu starten. Wir bieten zwei Varianten an:

### Option A: Full Experience (Empfohlen) 🐳
Enthält alles (inkl. TensorFlow, MLflow, Hugging Face).

```bash
# 1. Repository klonen
git clone <repository-url>
cd amalea

# 2. Services starten
docker-compose up --build

# 3. Services öffnen
# Jupyter Lab: http://localhost:8888
# Streamlit App: http://localhost:8501
# MLflow UI:     http://localhost:5001
```

### Option B: Slim & Fast 🚀
Ohne schwere Deep-Learning-Bibliotheken. Schneller Download.

```bash
docker compose up -d jupyter-lab-slim streamlit-slim
```
- **Jupyter Slim**: [http://localhost:8889](http://localhost:8889)
- **Streamlit Slim**: [http://localhost:8502](http://localhost:8502)

### Option C: Einzelne Services 🏗️
Baue nur das, was du brauchst:

```bash
# Nur Jupyter für Notebooks
docker build -f Dockerfile.jupyter -t amalea-jupyter .
docker run -p 8888:8888 amalea-jupyter

# Nur Streamlit für Apps
docker build -f Dockerfile.streamlit -t amalea-streamlit .
docker run -p 8501:8501 amalea-streamlit
```

---

## 📦 Dependencies (nach Wochen)

Das Repository verwendet modulare Requirements-Dateien für effiziente Installationen:

### Core Requirements
- **`requirements-core.txt`**: Grundlegende Abhängigkeiten (Python, Datenbibliotheken)
- **`requirements-dev.txt`**: Entwicklungs-Tools (pytest, black, ruff, etc.)

### Wochen-spezifische Requirements
- **W01-W03**: `requirements-week01.txt` bis `requirements-week03.txt` (Python Basics, Streamlit, ML Grundlagen)
- **W04**: `requirements-week04.txt` (MLOps, MLflow, DVC)
- **W05**: `requirements-week05.txt` (TensorFlow, PyTorch)
- **W06**: `requirements-week06.txt` (OpenCV, Transformers, Computer Vision)
- **W07**: `requirements-week07.txt` (FastAPI, Deployment-Tools)

### Spezielle Setups
- **Cloud Deployment**: `requirements.cloud.txt` (optimiert für Streamlit Cloud)
- **Locked Versions**: `requirements-*.lock.txt` (pinned Versionen für Reproduzierbarkeit)

### Installation Beispiele

```bash
# Schnellstart (alles, W01–W07)
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-week06.txt -r requirements-week07.txt

# Standard (W01–W03)
pip install -r requirements-week03.txt

# Mit Dev-Tools
pip install -r requirements-dev.txt

# Reproduzierbare Installation (W07)
pip install -r requirements-07.lock.txt
```

> 💡 **Tipp**: Nutze `requirements.txt` als Alias für den leichten W01–W03-Stack. Installiere nur, was du pro Woche brauchst!

---

## ▶️ Run Cheatsheet (lokal)

### Docker Compose (Empfohlen)
```bash
# Volles Setup starten
docker-compose up --build

# Einzelne Services
docker compose up jupyter-lab-slim streamlit-slim
```

### Lokale Entwicklung
```bash
# W07 Backend starten
cd 07_Deployment_Portfolio && export PYTHONPATH=$(pwd)
uvicorn backend.main:app --host 127.0.0.1 --port 8000

# W07 Dashboards lokal
API_URL=http://127.0.0.1:8000 streamlit run 07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py --server.port 8505
API_URL=http://127.0.0.1:8000 streamlit run 07_Deployment_Portfolio/05_streamlit_nlp_dashboard.py --server.port 8506

# Compose für W07 (API + beide Dashboards)
cd 07_Deployment_Portfolio && docker compose up --build
```

### Notebook Execution
```bash
# CV/NLP Notebooks automatisch ausführen
./run_cv_notebooks.sh

# Einzelne Woche starten
cd 01_Python_Grundlagen && jupyter lab
```

### Tests & Qualität
```bash
# Alle Tests ausführen
pytest

# Code-Qualität prüfen
make lint

# Formatierung
make format
```

> 🔧 **Makefile**: Nutze `make install`, `make test`, `make lint` für automatisierte Tasks.

---

## 📁 Repository-Struktur

Das Repository ist nach den Kurswochen gegliedert und enthält alle notwendigen Ressourcen für einen vollständigen Data-Science-Kurs:

```text
amalea/
├── 📂 01_Python_Grundlagen/           # Python Basics & QUA³CK Framework
│   ├── 📄 *.ipynb                     # Notebooks (inkl. executed Versionen)
│   ├── 🐍 *.py                        # Streamlit Apps & Skripte
│   ├── 🐳 Dockerfile                  # Lokaler Docker Build
│   ├── 📋 requirements.txt            # Abhängigkeiten
│   └── 📄 README.md                   # Wochen-Dokumentation
├── 📂 02_Streamlit_und_Pandas/        # Interaktive Data Apps
├── 📂 03_Machine_Learning/            # ML Pipelines & Modelle
├── 📂 04_Advanced_Algorithms/         # Ensembles & Unsupervised Learning
├── 📂 05_Neural_Networks/             # Deep Learning mit TensorFlow
├── 📂 06_Computer_Vision_NLP/         # CV & NLP mit Transformers
├── 📂 07_Deployment_Portfolio/        # Production Deployment & APIs
├── 📂 executed_notebooks/             # Ausgeführte Notebook-Versionen
├── 📂 datasets/                       # Kurs-Datensätze
├── 📂 Referate/                       # Studentische Präsentationen
├── 📂 tests/                          # Test-Suite
├── 📂 BACKUP_Original_AMALEA_Notebooks/ # Backup der Originale
├── 🐳 docker-compose.yml              # Multi-Service Setup
├── 🐳 Dockerfile.*                    # Verschiedene Docker-Konfigurationen
├── 📋 requirements*.txt               # Modular requirements pro Woche
├── 🔧 Makefile                        # Build & Development Tasks
├── ⚙️ pytest.ini                       # Test-Konfiguration
├── 🌐 nightwatch.conf.js              # E2E Testing
├── 📄 README.md                       # Diese Datei
├── 📄 DEVELOPER_GUIDE.md              # Entwicklungsrichtlinien
├── 📄 KURSBESCHREIBUNG.md             # Kurs-Details
├── 📄 02_Glossar_Alle_Begriffe_erklärt.ipynb # Fachbegriffe erklärt
├── 📄 ML_DL_Mathematik.ipynb          # Mathematische Grundlagen
└── 📄 LICENSE.md                      # Lizenz-Informationen
```

---

## 📚 Kursinhalte & Portfolio-Projekte

Der Kurs ist in 7 Wochen gegliedert; alle Inhalte sind production-ready mit Executed-Notebooks, Backend und Dashboards.

| Woche | Thema |
|-------|-------|
| **01** | Python Grundlagen & QUA³CK Framework |
| **02** | Streamlit & Pandas für interaktive Apps |
| **03** | Machine Learning Pipelines |
| **04** | Advanced Algorithms & MLOps |
| **05** | Neuronale Netze |
| **06** | Computer Vision & NLP |
| **07** | Deployment & Portfolio |

### Aktueller Stand im Repo (Auszug; production-ready)

| Woche | Kern-Notebooks | Apps / Skripte | Status |
|-------|----------------|----------------|--------|
| 01 | `00_Python_in_3_Stunden.ipynb`, `01_Docker_für_Data_Science.ipynb`, `02_Glossar_Alle_Begriffe_erklärt.ipynb`, `03_QUA3CK_Prozessmodell.ipynb` | `01_Python_Grundlagen/uebungs_app.py`, `01_Python_Grundlagen/meine_erste_app.py`, `01_Python_Grundlagen/streamlit_komponenten.py` | ✅ Fertig |
| 02 | `02_Streamlit_und_Pandas/01_Erste_Streamlit_App_fixed.ipynb` | `02_Streamlit_und_Pandas/example_app.py`, `02_Streamlit_und_Pandas/hello_streamlit.py`, `02_Streamlit_und_Pandas/streamlit_komponenten.py` | ✅ Fertig |
| 03 | `03_Machine_Learning/02_ML_in_Streamlit_fixed.ipynb` | `03_Machine_Learning/iris_ml_app.py`, `03_Machine_Learning/housing_regression_app.py` | ✅ Fertig |
| 04 | `04_Advanced_Algorithms/02_MLFlow_Big3_Tracking.ipynb`, `04_Advanced_Algorithms/03_Bäume_Nachbarn_und_Clustering.ipynb` | `04_Advanced_Algorithms/streamlit_komponenten.py` | ✅ Fertig |
| 05 | `05_Neural_Networks/` (mehrere Notebooks) | `05_Neural_Networks/streamlit_komponenten.py` | ✅ Fertig |
| 06 | `06_Computer_Vision_NLP/06_01_neu_CNN_Basics.ipynb` u.a. | Runner: `run_cv_notebooks.sh` erzeugt Executed-Notebooks in `executed_notebooks/` | ✅ Fertig |
| 07 | `07_Deployment_Portfolio/` (Notebooks in `executed_notebooks/`) | FastAPI-Demo-API (`backend/main.py`), Streamlit-Dashboards, Compose-Stack | ✅ Fertig |

> ℹ️ **Executed Notebooks**: Alle wichtigen Notebooks liegen in `executed_notebooks/` als HTML/PDF für schnelle Referenz.
> 🔧 **Docker Setup**: Mehrere Dockerfile-Varianten (jupyter, streamlit, slim/full) für verschiedene Use-Cases.
> 📊 **MLflow Tracking**: Experiment-Logs in `mlruns/` für Reproduzierbarkeit.

### Portfolio-Apps (Beispiele)

**Auszug (W01–W07):**
1.  **Python Fundamentals Dashboard** (`01_Python_Grundlagen/uebungs_app.py`)
2.  **Streamlit Starter** (`01_Python_Grundlagen/meine_erste_app.py`)
3.  **Streamlit Pandas Demo** (`02_Streamlit_und_Pandas/example_app.py`)
4.  **Hello Streamlit Widgets** (`02_Streamlit_und_Pandas/hello_streamlit.py`)
5.  **Iris ML Playground** (`03_Machine_Learning/iris_ml_app.py`)
6.  **Housing Regression Explorer** (`03_Machine_Learning/housing_regression_app.py`)
7.  **MLOps Monitoring Dashboard** (`07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py`)
8.  **NLP Demo Dashboard** (`07_Deployment_Portfolio/05_streamlit_nlp_dashboard.py`)

**Weitere Apps:** ML-, CV- und Deployment-Demos stehen in den jeweiligen Wochenordnern bereit.

---

---

## 👨‍🏫 Support & Ressourcen

### Dokumentation
- 📖 **[DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)**: Detaillierte Entwicklungsrichtlinien und Best Practices
- 📚 **[KURSBESCHREIBUNG.md](KURSBESCHREIBUNG.md)**: Vollständige Kursbeschreibung und Lernziele
- 🔧 **[Makefile](Makefile)**: Automatisierte Build- und Development-Tasks
- 🧪 **Tests**: Vollständige Test-Suite in `tests/` mit pytest-Konfiguration

### Bei Problemen
1. **Dokumentation prüfen**: Schaue in den Wochen-Ordnern nach READMEs und der DEVELOPER_GUIDE.md
2. **Executed Notebooks**: Nutze `executed_notebooks/` für funktionierende Beispiele
3. **Docker Issues**: Mehrere Dockerfile-Varianten verfügbar (slim/full)
4. **Dependencies**: Modulare requirements-Dateien für verschiedene Setups

### Kurs-Forum & Community
- Nutze das Kurs-Forum für fachliche Fragen
- Teile deine Lösungen in `Referate/` für andere Lernende
- Bei technischen Problemen: Issues im Repository erstellen

### Zusätzliche Ressourcen
- 📊 **Glossar**: `02_Glossar_Alle_Begriffe_erklärt.ipynb` - Alle Fachbegriffe erklärt
- 🔢 **Mathematik**: `ML_DL_Mathematik.ipynb` - Mathematische Grundlagen für ML/DL
- 📁 **Datasets**: Kurs-Datensätze in `datasets/` für praktische Übungen
