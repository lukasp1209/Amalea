# 🚀 Deployment auf Streamlit Cloud (MLOps/NLP Dashboards)

Dieses Dokument erklärt, wie du die Dashboards aus `07_Deployment_Portfolio` auf Streamlit Cloud veröffentlichst – inklusive Hinweis, wie du mit Demo-Modus oder externem API-Endpoint arbeitest.

---

## 📋 Schritt 1: Voraussetzungen

Stelle sicher, dass du Folgendes hast:

1.  **Ein GitHub-Konto**.
2.  **Ein öffentliches GitHub-Repository**, das deinen App-Code enthält.
3.  **Eine `requirements.txt`-Datei** in deinem Repository, die alle notwendigen Pakete auflistet.

---

## ⚙️ Schritt 2: Dependencies (`requirements.cloud.txt`)

Nutze die vorhandene `requirements.cloud.txt` im Ordner `07_Deployment_Portfolio`. Sie enthält Streamlit, sklearn und FastAPI/uvicorn (für lokale Tests). Auf Streamlit Cloud wird nur die App selbst ausgeführt; das Backend musst du extern bereitstellen oder den Demo-Modus nutzen.

---

## 🚀 Schritt 3: Der Deployment-Prozess (Dashboard-only)

1.  **Anmelden**: Gehe zu [share.streamlit.io](https://share.streamlit.io/) und melde dich mit deinem GitHub-Konto an.
2.  **Neue App**: Klicke in deinem Workspace auf den Button **"New app"**.
3.  **Repository verbinden**: Wähle dein GitHub-Repository, den Branch (z.B. `main`) und den genauen Pfad zu deiner App-Datei (z.B. `07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py` oder `07_Deployment_Portfolio/05_streamlit_nlp_dashboard.py`).
4.  **Deploy**: Klicke auf **"Deploy!"**. Deine App wird nach wenigen Minuten online sein. 🎉

---

## 🔑 Schritt 4: API-URL & Secrets

- Dashboards unterstützen Demo-Mode (ohne Backend). Für Live-Mode brauchst du eine öffentlich erreichbare API (z.B. dein FastAPI-Backend auf Render/Fly/Heroku/Azure). Setze `API_URL` unter **Settings → Secrets**:

```
API_URL="https://dein-backend.example.com"
```

- Keine API-Keys nötig im Demo-Modus. Falls dein Backend Auth benötigt, lege Schlüssel ebenso in `Secrets` ab und lies sie in der App.

---

## 🔧 Schritt 5: Troubleshooting

- **Backend nicht erreichbar**: Schalte auf Demo-Modus oder setze `API_URL` korrekt auf dein gehostetes FastAPI.
- **`ModuleNotFoundError`**: Abhängigkeit in `requirements.cloud.txt` ergänzen.
- **Langsame Builds/Slug zu groß**: Halte das Repo schlank (keine großen Daten). Wir haben `data/` und `images/` bereits entfernt.
- **Timeouts**: In Streamlit Cloud sind Requests limitiert; halte API-Calls kurz oder nutze Demo-Modus.

---

## 🏆 Zusammenfassung

Du hast gelernt, wie man eine Streamlit-Anwendung auf der Streamlit Cloud bereitstellt. Dies ist der wichtigste Schritt, um deine Projekte in einem professionellen Portfolio zu präsentieren. Füge den Link zu deiner Live-App deinem Lebenslauf und Portfolio hinzu!
