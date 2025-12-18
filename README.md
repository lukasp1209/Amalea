# 🎓 AMALEA 2025 - Data Analytics & Big Data

**Der modernisierte Data-Science-Kurs für Entwickler & Analysten**

> 🚀 **Dein Ziel:**
>
> Von Python-Basics zu **Production-Grade ML-Systemen**.
> In 7 Wochen baust du ein Portfolio aus **8 interaktiven Apps**, trainierst neuronale Netze und deployest alles in die Cloud.
>
> **Kein "Spaghetti-Code" in Notebooks, sondern sauberes Software-Engineering für Daten.**

---

## 💡 Der Tech-Stack (Industrie-Standard)

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

Der Kurs ist in 7 Wochen gegliedert. **Stand Februar 2025**: Die Wochen **01–03** sind vollständig überarbeitet (6 Kern-Notebooks + 6 Streamlit-Apps); die Inhalte zu Woche 04–07 werden aktuell migriert.

| Woche | Thema |
|-------|-------|
| **01** | Python Grundlagen & QUA³CK Framework |
| **02** | Streamlit & Pandas für interaktive Apps |
| **03** | Machine Learning Pipelines |
| **04** | Advanced Algorithms & MLOps |
| **05** | Neuronale Netze |
| **06** | Computer Vision & NLP |
| **07** | Deployment & Portfolio |

### Aktueller Stand im Repo (Ordner 01–03)

| Woche | Kern-Notebooks | Apps / Skripte | Status |
|-------|----------------|----------------|--------|
| 01 | `00_Python_in_3_Stunden.ipynb`, `01_Docker_für_Data_Science.ipynb`, `02_Glossar_Alle_Begriffe_erklärt.ipynb`, `03_QUA3CK_Prozessmodell.ipynb` | `01_Python_Grundlagen/uebungs_app.py`, `01_Python_Grundlagen/meine_erste_app.py`, `01_Python_Grundlagen/streamlit_komponenten.py` | ✅ Fertig |
| 02 | `02_Streamlit_und_Pandas/01_Erste_Streamlit_App_fixed.ipynb` | `02_Streamlit_und_Pandas/example_app.py`, `02_Streamlit_und_Pandas/hello_streamlit.py`, `02_Streamlit_und_Pandas/streamlit_komponenten.py` | ✅ Fertig |
| 03 | `03_Machine_Learning/02_ML_in_Streamlit_fixed.ipynb` | `03_Machine_Learning/iris_ml_app.py`, `03_Machine_Learning/housing_regression_app.py` | ✅ Fertig |

> ℹ️ Für Woche 04–07 existieren bereits Platzhalter-Ordner. Inhalte werden sukzessive veröffentlicht und hier ergänzt.

### Portfolio-Apps (Beispiele)

**Bereits lauffähig (W01–W03):**
1.  **Python Fundamentals Dashboard** (`01_Python_Grundlagen/uebungs_app.py`)
2.  **Streamlit Starter** (`01_Python_Grundlagen/meine_erste_app.py`)
3.  **Streamlit Pandas Demo** (`02_Streamlit_und_Pandas/example_app.py`)
4.  **Hello Streamlit Widgets** (`02_Streamlit_und_Pandas/hello_streamlit.py`)
5.  **Iris ML Playground** (`03_Machine_Learning/iris_ml_app.py`)
6.  **Housing Regression Explorer** (`03_Machine_Learning/housing_regression_app.py`)

**In Vorbereitung (W04–W07):** Weitere ML-, CV- und Deployment-Apps folgen, sobald die entsprechenden Wochen migriert sind.

---

## 🛠️ Technischer Stack

- **Sprache**: Python 3.11+
- **Data Science**: Pandas, NumPy, Scikit-learn
- **Deep Learning**: TensorFlow/Keras, Hugging Face
- **Web-Apps**: Streamlit
- **Entwicklungsumgebung**: Docker
- **MLOps**: MLflow

---

## 👨‍🏫 Support

Bei Fragen oder Problemen:
1.  Prüfe die Dokumentation in den jeweiligen Wochen-Ordnern.
2.  Nutze das Kurs-Forum für fachliche Fragen.
3.  Kontaktiere den Instructor für weiterführende Probleme.
