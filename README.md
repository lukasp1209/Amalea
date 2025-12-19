# 🎓 AMALEA 2025 - Data Analytics & Big Data

<div align="center">
  <img src="./kurs-logo.png" alt="AMALEA 2025 Logo" width="400">
  <br><br>
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white" alt="Docker">
</div>

**Der modernisierte Data-Science-Kurs für Entwickler & Analysten**

> 🚀 **Dein Ziel:**
>
> Von Python-Basics zu **Production-Grade ML-Systemen**.
> In 7 Wochen baust du ein Portfolio aus **8 interaktiven Apps**, trainierst neuronale Netze und deployest alles in die Cloud.
>
> **Kein "Spaghetti-Code" in Notebooks, sondern sauberes Software-Engineering für Daten.**

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
Enthält alles (inkl. TensorFlow, MLflow).

```bash
# 1. Starten
docker-compose up --build

# 2. Services öffnen
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

---

## 📦 Dependencies (nach Wochen)

- Schnellstart (alles, W01–W07): `python -m venv .venv && source .venv/bin/activate && pip install --upgrade pip && pip install -r requirements-week06.txt -r requirements-week07.txt`
- Standard (W01–W03): `pip install -r requirements-week03.txt` (leichtgewichtig, inkl. Streamlit + Sklearn).
- Advanced/MLOps (W04): `pip install -r requirements-week04.txt` (duckdb/polars/pyarrow + mlflow/dvc).
- Deep Learning (W05): `pip install -r requirements-week05.txt` (TF + Torch, schwer).
- CV & NLP (W06): `pip install -r requirements-week06.txt` (fügt OpenCV, scikit-image, Transformers hinzu).
- Deployment (W07): `pip install -r requirements-week07.txt` (nutzt `07_Deployment_Portfolio/requirements.cloud.txt` mit `requirements-07.lock.txt` als Constraints).
- Dev-Tools: `pip install -r requirements-dev.txt` (zieht W07-Stack + ruff/pytest/black).
- Docker Compose (Full): nutzt `requirements-week06.txt` + `requirements-week07.txt` für `jupyter-lab`, `requirements-week07.txt` für `streamlit-dev` (Build-Args in `docker-compose.yml`).

> Hinweis: `requirements.txt` zeigt auf den leichten W01–W03-Stack. Installiere nur, was du pro Woche brauchst, um Downloads klein zu halten.

---

## ▶️ Run Cheatsheet (lokal)

- **W07 Backend**: `cd 07_Deployment_Portfolio && export PYTHONPATH=$(pwd) && uvicorn backend.main:app --host 127.0.0.1 --port 8000`
- **W07 Dashboards lokal**: `API_URL=http://127.0.0.1:8000 streamlit run 04_streamlit_mlops_dashboard.py --server.port 8505` und `...05_streamlit_nlp_dashboard.py --server.port 8506`
- **Compose (API + beide Dashboards)**: `cd 07_Deployment_Portfolio && docker compose up --build`
- **Streamlit Cloud**: `requirements.cloud.txt` nutzen, `API_URL` als Secret setzen (Demo-Modus ohne Backend möglich).
- **Pinned Stack (07)**: `make install` nutzt `requirements-07.lock.txt` als Constraints für reproduzierbare Versionsstände (FastAPI/Streamlit/Sklearn).

---

## 📁 Repository-Struktur

Das Repository ist nach den Kurswochen gegliedert:

```text
amalea/
├── 📂 01_Python_Grundlagen/
├── 📂 02_Streamlit_und_Pandas/
├── 📂 03_Machine_Learning/
├── 📂 04_Advanced_Algorithms/
├── 📂 05_Neural_Networks/
├── 📂 06_Computer_Vision_NLP/
├── 📂 07_Deployment_Portfolio/
├── 🐳 docker-compose.yml
├── 🐳 Dockerfile.*
├── 📋 requirements*.txt
├── 📄 README.md
└── 📄 DEVELOPER_GUIDE.md
```

---

## 📚 Kursinhalte & Portfolio-Projekte

Der Kurs ist in 7 Wochen gegliedert. **Stand 19.12.2025**: Wochen **01–07** sind production-ready mit überarbeiteten Inhalten, Backend, Dashboards und Executed-Notebooks.

| Woche | Thema |
|-------|-------|
| **01** | Python Grundlagen & QUA³CK Framework |
| **02** | Streamlit & Pandas für interaktive Apps |
| **03** | Machine Learning Pipelines |
| **04** | Advanced Algorithms & MLOps |
| **05** | Neuronale Netze |
| **06** | Computer Vision & NLP |
| **07** | Deployment & Portfolio |

### Aktueller Stand im Repo (Auszug; Wochen 01–07 production-ready)

| Woche | Kern-Notebooks | Apps / Skripte | Status |
|-------|----------------|----------------|--------|
| 01 | `00_Python_in_3_Stunden.ipynb`, `01_Docker_für_Data_Science.ipynb`, `02_Glossar_Alle_Begriffe_erklärt.ipynb`, `03_QUA3CK_Prozessmodell.ipynb` | `01_Python_Grundlagen/uebungs_app.py`, `01_Python_Grundlagen/meine_erste_app.py`, `01_Python_Grundlagen/streamlit_komponenten.py` | ✅ Fertig |
| 02 | `02_Streamlit_und_Pandas/01_Erste_Streamlit_App_fixed.ipynb` | `02_Streamlit_und_Pandas/example_app.py`, `02_Streamlit_und_Pandas/hello_streamlit.py`, `02_Streamlit_und_Pandas/streamlit_komponenten.py` | ✅ Fertig |
| 03 | `03_Machine_Learning/02_ML_in_Streamlit_fixed.ipynb` | `03_Machine_Learning/iris_ml_app.py`, `03_Machine_Learning/housing_regression_app.py` | ✅ Fertig |
| 07 | `07_Deployment_Portfolio/01_MLOps_und_Deployment.ipynb`, `02_NLP_und_Text_Generation.ipynb`, `03_QUA3CK_MLOps_Integration.ipynb` (ausgeführt unter `executed/`) | FastAPI-Demo-API (`backend/main.py`), Streamlit-Dashboards (`04_streamlit_mlops_dashboard.py`, `05_streamlit_nlp_dashboard.py`), Compose-Stack (`docker-compose.yml`) | ✅ Fertig |

**Neu (Woche 06 – Computer Vision & NLP, CPU-freundlich):**
- Fünf schlanke "neu"-Notebooks in `06_Computer_Vision_NLP`: `06_01_neu_CNN_Basics`, `06_02_neu_OpenCV_Edge_Features`, `06_03_neu_Data_Augmentation_Practice`, `06_04_neu_Transfer_Learning_Lite`, `06_05_neu_Image_Sampler`.
- Fokus: klar geführte Didaktik, kleine Subsets, Seeds gesetzt. Läuft auf CPU in wenigen Minuten; GPU beschleunigt Trainingszellen.
- Runner: `bash run_cv_notebooks.sh` (aus Repo-Root) erzeugt Executed-Notebooks unter `06_Computer_Vision_NLP/executed`.

**Neu (Woche 07 – Deployment & Portfolio, CPU-freundlich):**
- FastAPI-Demo-Backend (`backend/main.py`) mit `/health`, `/predict`, `/sentiment`, `/qa`, `/generate`; läuft auf CPU.
- Zwei Streamlit-Dashboards mit Demo/Live-Schalter: `04_streamlit_mlops_dashboard.py` (Iris-Predict/Monitoring) und `05_streamlit_nlp_dashboard.py` (Gen/Sentiment/Q&A).
- Drei kurze Notebooks mit "So nutzt du..."-Guides, Executed-Versionen unter `07_Deployment_Portfolio/executed/`.
- Compose-Setup (`07_Deployment_Portfolio/docker-compose.yml`) und `requirements.cloud.txt` für lokalen Start oder Streamlit Cloud (API-URL via Sidebar/Secrets konfigurierbar).

> ℹ️ Alle Wochen (01–07) sind production-ready; CV/NLP und Deployment laufen CPU-freundlich.

### Portfolio-Apps (Beispiele)

**Bereits lauffähig (Auszug, W01–W07):**
1.  **Python Fundamentals Dashboard** (`01_Python_Grundlagen/uebungs_app.py`)
2.  **Streamlit Starter** (`01_Python_Grundlagen/meine_erste_app.py`)
3.  **Streamlit Pandas Demo** (`02_Streamlit_und_Pandas/example_app.py`)
4.  **Hello Streamlit Widgets** (`02_Streamlit_und_Pandas/hello_streamlit.py`)
5.  **Iris ML Playground** (`03_Machine_Learning/iris_ml_app.py`)
6.  **Housing Regression Explorer** (`03_Machine_Learning/housing_regression_app.py`)
7.  **MLOps Monitoring Dashboard** (`07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py`)
8.  **NLP Demo Dashboard** (`07_Deployment_Portfolio/05_streamlit_nlp_dashboard.py`)

**Weitere Apps (W04–W07):** ML-, CV- und Deployment-Demos stehen in den jeweiligen Wochenordnern bereit.

---

---

## 👨‍🏫 Support

Bei Fragen oder Problemen:
1.  Prüfe die Dokumentation in den jeweiligen Wochen-Ordnern.
2.  Nutze das Kurs-Forum für fachliche Fragen.
3.  Kontaktiere den Instructor für weiterführende Probleme.
