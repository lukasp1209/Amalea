# 🚀 Deployment auf Streamlit Cloud: Eine Schritt-für-Schritt-Anleitung

Dieses Dokument erklärt, wie du eine Streamlit-Anwendung aus diesem Kurs auf der Streamlit Cloud veröffentlichst.

---

## 📋 Schritt 1: Voraussetzungen

Stelle sicher, dass du Folgendes hast:

1.  **Ein GitHub-Konto**.
2.  **Ein öffentliches GitHub-Repository**, das deinen App-Code enthält.
3.  **Eine `requirements.txt`-Datei** in deinem Repository, die alle notwendigen Pakete auflistet.

---

## ⚙️ Schritt 2: Die `requirements.txt`-Datei

Diese Datei ist entscheidend. Sie sagt Streamlit Cloud, welche Pakete es installieren muss. Für die meisten Apps hier genügt eine einfache Datei, da viele Pakete vorinstalliert sind.

**Beispielinhalt für `requirements.cloud.txt`:**
```
streamlit>=1.32
pandas>=2.2
numpy
plotly
scikit-learn
```

> **Wichtig**: Wenn deine App spezielle Bibliotheken wie `tensorflow` oder `transformers` benötigt, musst du diese hier explizit aufführen.

---

## 🚀 Schritt 3: Der Deployment-Prozess

1.  **Anmelden**: Gehe zu [share.streamlit.io](https://share.streamlit.io/) und melde dich mit deinem GitHub-Konto an.
2.  **Neue App**: Klicke in deinem Workspace auf den Button **"New app"**.
3.  **Repository verbinden**: Wähle dein GitHub-Repository, den Branch (z.B. `main`) und den genauen Pfad zu deiner App-Datei (z.B. `07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py`).
4.  **Deploy**: Klicke auf **"Deploy!"**. Deine App wird nach wenigen Minuten online sein. 🎉

---

## 🔑 Schritt 4: Secrets Management

Gib niemals API-Schlüssel oder Passwörter direkt in deinen Code. Nutze stattdessen das Secrets Management von Streamlit Cloud.

-   Gehe in den App-Einstellungen zu **Settings -> Secrets**.
-   Füge deine Geheimnisse dort ein.
-   Greife im Code sicher darauf zu mit `st.secrets["DEIN_GEHEIMNIS"]`.

---

## 🔧 Schritt 5: Troubleshooting

-   **`ModuleNotFoundError`**: Ein Paket fehlt in der `requirements.txt`.
-   **App startet nicht**: Überprüfe die Logs in der Streamlit Cloud auf Fehlermeldungen.
-   **`Slug size too large`**: Dein Repository ist zu groß. Lagere große Datendateien aus (z.B. mit Git LFS).

---

## 🏆 Zusammenfassung

Du hast gelernt, wie man eine Streamlit-Anwendung auf der Streamlit Cloud bereitstellt. Dies ist der wichtigste Schritt, um deine Projekte in einem professionellen Portfolio zu präsentieren. Füge den Link zu deiner Live-App deinem Lebenslauf und Portfolio hinzu!
