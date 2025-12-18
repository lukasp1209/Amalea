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

Der Kurs ist in 7 Wochen gegliedert und umfasst **16 Notebooks** und **8 Streamlit-Apps**, die als Portfolio-Projekte dienen.

| Woche | Thema |
|-------|-------|
| **01** | Python Grundlagen & QUA³CK Framework |
| **02** | Streamlit & Pandas für interaktive Apps |
| **03** | Machine Learning Pipelines |
| **04** | Advanced Algorithms & MLOps |
| **05** | Neuronale Netze |
| **06** | Computer Vision & NLP |
| **07** | Deployment & Portfolio |

### Portfolio-Apps (Beispiele)
1.  **Streamlit Pandas Demo** (`02_Streamlit_und_Pandas/example_app.py`)
2.  **Neural Network Playground** (`05_Neural_Networks/neural_network_playground.py`)
3.  **CNN Filter Explorer** (`06_Computer_Vision_NLP/06_01_streamlit_cnn_filter.py`)
4.  **Computer Vision Apps** (`06_Computer_Vision_NLP/06_02_streamlit_cv_apps.py`)
5.  ... und 4 weitere Apps in den Wochen 6 und 7.

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