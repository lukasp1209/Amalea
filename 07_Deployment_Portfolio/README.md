# 🚀 07 Deployment & Portfolio

**MLOps, Modern NLP und Production-Ready Deployment (Stand: Work-in-Progress)**

## 📚 Notebooks (Status)

- **01_MLOps_und_Deployment.ipynb** – Kurze CPU-Demo: Iris-LogReg + Export (`artifacts/iris_lr.pkl`), Hinweis auf Serving via FastAPI.
- **02_NLP_und_Text_Generation.ipynb** – Kurze CPU-Demo: einfache Sentiment-Heuristik + Stub-Text-Gen (kein großes Modell).
- **03_QUA3CK_MLOps_Integration.ipynb** – QUA³CK-Mini-Flow, Health/Predict-Check gegen das Backend.

### Geführter Ablauf
1) Backend starten (Demo oder Live) oder im Dashboard Demo-Modus lassen.
2) 01_Notebook: Mini-Train + Export (Artefakt anlegbar für Serving).
3) 02_Notebook: Sentiment/Gen-Stubs verstehen (schnell, CPU).
4) 03_Notebook: Health/Predict gegen API prüfen (oder Hinweis lesen, wenn API aus ist).
5) Dashboards öffnen: erst Demo, dann Live mit `API_URL` setzen. Optional per `docker compose up --build` alles gemeinsam starten.

## 🚀 Streamlit Apps (Status)

- **04_streamlit_mlops_dashboard.py** – Dashboard für Iris-Predict-API (`/health`, `/predict`). Demo-Modus integriert (simulierte Metriken), Live-Modus erwartet API.
- **05_streamlit_nlp_dashboard.py** – UI für Text-Gen/Sentiment/Q&A (`/generate`, `/sentiment`, `/qa`). Demo-Modus integriert, Live-Modus erwartet NLP-API.

## 🎯 Lernziele (Zielbild)

- 🔄 **MLOps Pipeline**: Model Training bis Production Deployment (noch zu verifizieren)
- 🐳 **Containerization**: Docker für reproduzierbare ML-Services (siehe Ergänzungen unten)
- 🌐 **API Development**: FastAPI für ML Model Serving (API wird aktuell vorausgesetzt, nicht bereitgestellt)
- 📊 **Model Monitoring**: Performance Tracking in Production (Dashboard nutzt simulierte Daten)
- 🤖 **Modern NLP**: Transformer-basierte Text Processing (Backend-Service nötig)
- 🚀 **Production Deployment**: Skalierbare ML-Anwendungen (Deployment-Schritte noch zu ergänzen/kürzen)

## 📡 Backend (neu, leichtgewichtig)

- **FastAPI-Demo-API** unter `backend/main.py`
	- Endpunkte: `/health`, `/predict` (Iris), `/sentiment`, `/qa`, `/generate`
	- Läuft vollständig CPU-basiert, keine großen Modelle.

Start (lokal):
```bash
cd 07_Deployment_Portfolio
pip install -r requirements.cloud.txt
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Start (Docker Compose, API + beide Dashboards):
```bash
cd 07_Deployment_Portfolio
docker compose up --build
```
URLs:
- API: http://localhost:8000
- MLOps Dashboard: http://localhost:8505
- NLP Dashboard: http://localhost:8506

## 📱 Streamlit Apps (Starten)

```bash
cd 07_Deployment_Portfolio
pip install -r requirements.cloud.txt

# MLOps Dashboard (Demo- oder Live-Modus wählbar)
streamlit run 04_streamlit_mlops_dashboard.py --server.port 8505

# NLP Dashboard (Demo- oder Live-Modus wählbar)
streamlit run 05_streamlit_nlp_dashboard.py --server.port 8506
```

Hinweise:
- Demo-Modus funktioniert ohne Backend; Live-Modus erwartet API auf `http://localhost:8000` (anpassbar in der Sidebar).
- Ports nach Bedarf anpassen.

## 🛠️ Technologie-Stack (geplant/teilweise vorhanden)

### MLOps & Deployment
- **MLflow** - Experiment Tracking & Model Registry
- **FastAPI** - High-performance API Framework
- **Docker** - Containerization & Deployment
- **Streamlit** - Interactive Dashboards

### Modern NLP
- **Transformers** - State-of-the-art NLP Models
- **Hugging Face** - Pre-trained Model Hub
- **Text Generation** - GPT-style Language Models
- **Multi-task NLP** - Sentiment, Q&A, Summarization

## 🗺️ Nächste Schritte (Empfohlen)
- Backend: einfache Tests für Endpunkte ergänzen; optional kleinere Modelle anstelle der Stubs.
- MLOps/NLP Dashboards: echte Monitoring-Metriken anbinden, Prompt-Limits/Safety weiter ausbauen.
- Falls nötig: eigene Assets hinzufügen; ungenutzte Beispiel-Daten/Images wurden entfernt.
