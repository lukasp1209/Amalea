# 🧑‍💻 Developer Guide

Konzentrierte technische Doku für Aufbau & Betrieb der Umgebung. Der Haupt-`README.md` bleibt schlanker (Kurs & Überblick).

## Inhalt
- Architektur & Module
- Lokale Entwicklung (ohne Docker)
- Container & Services (Docker Compose)
- MLflow Nutzung
- Ports, Volumes, Umgebungsvariablen
- Tests & Qualität
- Troubleshooting (technisch)

---
## Architektur (Kurz)

| Ebene | Beschreibung |
|-------|--------------|
| Kurs Notebooks | Lern- & Demonstrationsinhalte (01_.. bis 07_..) |
| Streamlit Apps | Interaktive UIs (Übungen, ML, CV, NLP) |

---
## Lokale Entwicklung (ohne Docker)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
# Start Jupyter
jupyter lab
# Start Beispiel-App
streamlit run 02_Streamlit_und_Pandas/example_app.py
```

Optionale Kernel-Registrierung:
```bash
python -m ipykernel install --user --name amalea-venv \
  --display-name "Python (amalea)"
```

---
## Docker & Services

`docker-compose.yml` definiert Full + Slim Services.

| Service | Zweck | Port (Host) | Profil |
|---------|------|-------------|--------|
| jupyter-lab | Volle Data/ML Umgebung | 8888 | Full |
| jupyter-lab-slim | Leichtgewicht (kein TF/Torch/CV) | 8889 | Slim |
| streamlit-dev | Full Streamlit (alle Deps) | 8501 | Full |
| streamlit-slim | Schnellstart / MC-Test | 8502 | Slim |
| mlflow | Tracking Server | 5001 (→ 5000) | Full |
| postgres (falls aktiviert) | Persistenz (optional) | 5432 | Full |

Start (alle):
```bash
docker compose up -d
```

Gezielt (nur Slim):
```bash
docker compose up -d jupyter-lab-slim streamlit-slim
```

Logs:
```bash
docker compose logs -f --tail=120 streamlit-slim
```

Neu bauen (Dependency-Change):
```bash
docker compose build --no-cache streamlit-dev
```

Stop & Clean:
```bash
docker compose down
```

---
## Ports & Volumes

| Ressource | Mount / Volume | Zweck |
|----------|----------------|-------|
| Code | `./:/app` oder `./:/workspace` | Live Code Sync |
| MLflow DB | `mlflow-data` | SQLite + Artefakte |
| Jupyter Data | `jupyter-data` | User Settings / Workdir |
| Postgres Data | `postgres-data` | Persistente DB |

Prüfen:
```bash
docker volume ls
```

Löschen einzelnes Volume (Achtung Datenverlust):
```bash
docker volume rm mlflow-data
```

---
## Umgebungsvariablen / Secrets

`.env` (automatisch von Compose geladen):
```
MC_TEST_ADMIN_USER=Admin
MC_TEST_ADMIN_KEY=Admin
```

Streamlit Cloud: `.streamlit/secrets.toml` (alle Schlüssel als Strings empfohlen).

---
## MLflow Nutzung (kompakt)

Tracking URIs:
| Kontext | URI |
|---------|-----|
| Host | http://localhost:5001 |
| Container | http://mlflow:5000 |

Minimal:
```python
import mlflow
mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("demo")
with mlflow.start_run():
    mlflow.log_param("model","rf")
    mlflow.log_metric("accuracy",0.91)
```

Artefakte: Volume `mlflow-data` → Ordner `/mlflow/artifacts`.

Reset aller Runs:
```bash
docker compose down mlflow
docker volume rm $(docker volume ls -q | grep mlflow)
docker compose up -d mlflow
```

---
## Tests & Qualität

Tests ausführen:
```bash
pip install -r requirements.txt
PYTHONPATH=. pytest mc_test_app/tests -q
```

Einzelnen Test:
```bash
pytest mc_test_app/tests/test_core.py::test_append_row -q
```

Code-Blöcke / Lint (optional): markdownlint, ruff/flake8 integrierbar.

---
## Troubleshooting (technisch)

| Problem | Diagnose | Lösung |
|---------|----------|--------|
| Kein Auto-Reload | File Events langsam (Host) | Manuell reload / Full statt Slim |
| Port belegt | Prozess blockiert | `lsof -i :8501` → Prozess killen |
| MLflow leer | Falsche URI | `mlflow.get_tracking_uri()` prüfen |
| Schreibfehler CSV | Lock Konflikt | Wiederholen; Lock-Datei löschen (letztes Mittel) |
| Admin nicht sichtbar | User/Key mismatch | `.env` prüfen + App neu laden |

Logs prüfen (alle Services):
```bash
docker compose ps
docker compose logs --tail=60 streamlit-dev
```

---
## Release / Deployment (MC-Test)

Subtree Push (nur App):
```bash
git subtree push --prefix mc_test_app github main
```

Streamlit Cloud: Neues Repo mit Inhalt aus `mc_test_app/` erstellen, dann Deploy.

---
## Roadmap (Kurz)
- Gamification Modularisierung (`gamification.py`)
- Optional: Score Floor (min 0) konfigurieren
- Frage-Metadaten: Tags, Schwierigkeitsgrad
- API-Modus (REST oder Websocket) für externe Clients

---
**Letzte Aktualisierung:** 2025-09-22
