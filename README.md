# 🎓 AMALEA 2025 - Data Analytics & Big Data

**Modernisierter Kurs für IU Studierende - 5. Semester**

> 🚀 **Vollständig modernisiert**: 16 Core Notebooks + 8 Streamlit Apps + QUA³CK Framework + MLOps Integration

👉 Technische Details zur Entwicklungsumgebung (Docker, MLflow, Ports, Volumes) sind im **`DEVELOPER_GUIDE.md`** zu finden.

---

## 🎯 Was ist AMALEA?

**AMALEA** steht für **"Angewandte Machine Learning Algorithmen"** und ist ein praxisorientierter Kurs, der drei Kernbereiche kombiniert:
* **📚 Theoretische Fundamente**: Strukturiert durch das QUA³CK Prozessmodell.
* **🛠️ Praktische Umsetzung**: Hands-on-Coding mit modernen Tools wie Pandas, Scikit-learn und TensorFlow.
* **☁️ Interaktive Anwendungen**: Entwicklung und Deployment von produktionsreifen Streamlit-Apps.

### 🔄 Das QUA³CK Prozessmodell
Alle Projekte folgen dem systematischen **QUA³CK Framework**, einem Prozessmodell für Data-Science-Projekte:
- **Q**uestion: Problemdefinition
- **U**nderstand: Datenexploration und -analyse
- **A**cquire & Clean: Datenaufbereitung und -verarbeitung
- **A**nalyze: Modellentwicklung und -evaluierung
- **A**pp: Interaktive Streamlit-Anwendung
- **C**onclusion & **K**ommunikation: Dokumentation und Präsentation

---

## 🚀 Quick Start

Die empfohlene Methode zur Nutzung dieses Repositorys ist Docker.

### Mit Docker starten
1.  **Repository klonen:**
    ```bash
    git clone <repo-url>
    cd amalea
    ```
2.  **Entwicklungsumgebung starten:**
    ```bash
    docker-compose up
    ```
3.  **Services nutzen:**
    *   **JupyterLab**: [http://localhost:8888](http://localhost:8888) (für die Bearbeitung der Notebooks)
    *   **Streamlit**: [http://localhost:8501](http://localhost:8501) (zeigt die `example_app.py`)
    *   **MLflow**: [http://localhost:5001](http://localhost:5001) (zum Tracken von ML-Experimenten)

### Leichtgewichtige Umgebung (Slim Images)
Für schnellere Ladezeiten ohne Deep-Learning-Bibliotheken (TensorFlow, PyTorch) können die "Slim"-Services verwendet werden:
```bash
# Nur die schlanken Services für Jupyter und Streamlit starten
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