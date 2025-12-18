# 📊 Woche 2: Interactive Data Apps

> 🚀 **Dein Ziel:**
>
> Datenanalyse ist gut, **Data Apps** sind besser.
> In dieser Woche lernst du, wie du deine Python-Skripte in interaktive Web-Anwendungen verwandelst, die jeder im Browser nutzen kann.

## 💡 Der Tech-Stack

1.  **Pandas:** Deine In-Memory Datenbank. Wir schauen uns an, wie man Daten *vektorisiert* verarbeitet (statt langsamer Loops).
2.  **Streamlit:** Das Frontend. Wir lernen das *Execution Model* (Rerun-Loop) und *State Management* kennen.
3.  **Plotly:** Für interaktive Grafiken, die in der Web-App zoombare sind.

---

## 🗺️ Deine Roadmap

### 1️⃣ Theorie & Deep Dive
- **`01_Erste_Streamlit_App_fixed.ipynb`**
  - *Lernziel:* Verstehen, wie Streamlit "unter der Haube" funktioniert.
  - *Highlight:* Pandas Vektorisierung vs. Loops.
  - *Output:* Generiert automatisch `Dockerfile` und `requirements.txt`.

### 2️⃣ Praxis & Code
- **`example_app.py`**
  - *Was:* Eine Referenz-Implementierung einer Streamlit-App.
  - *Features:* Caching (`@st.cache_data`), Type Hints, Layouts.
  - *Aufgabe:* Starte sie und analysiere den Code.

---

## 🛠️ Setup & Start

### Option A: Via Docker (Empfohlen) 🐳

```bash
# Startet die App im Container
docker-compose up --build

# App öffnen: http://localhost:8501
```

### Option B: Lokal 💻

```bash
# 1. Dependencies installieren
pip install -r 02_Streamlit_und_Pandas/requirements.txt

# 2. App starten
streamlit run example_app.py
```

---

**Happy Coding!** 🚀
