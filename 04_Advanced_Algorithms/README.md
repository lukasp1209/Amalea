
# 🌳 04 Advanced Algorithms

> 🚀 **Motivation:**
>
> In diesem Modul lernst du die drei wichtigsten Algorithmen des Machine Learning – verständlich, praxisnah und direkt anwendbar für dein Portfolio! Du bekommst Einblicke in MLOps, professionelle Experiment-Workflows und baust eigene ML-Apps.

> 💡 **Warum lohnt sich das?**
> - Wer Decision Trees, KNN und K-Means versteht, kann 80% aller ML-Projekte meistern.
> - Du sammelst praktische Erfahrung mit Tools, die in der Data-Science-Praxis Standard sind.
> - Du kannst eigene ML-Apps bauen und erklären – ein echter Pluspunkt für Bewerbungen.

> 📚 **Glossar-Tipp:** Unklare Begriffe? Schau ins [Glossar](../../Glossar_Alle_Begriffe_erklärt.ipynb) – dort findest du alle wichtigen Erklärungen!

## 📚 Inhalt

- `02_MLFlow_Big3_Tracking.ipynb` – MLOps mit den Big 3 Algorithmen (Decision Trees, KNN, K-Means)
- `03_Bäume_Nachbarn_und_Clustering.ipynb` – Deep Dive: Theorie, Praxis & Streamlit-Apps
- **Portfolio-Tipp:** Nutze die Notebooks als Vorlage für eigene Projekte!

## 🎯 Lernziele

Nach dieser Woche kannst du:
- ✅ Tree-based Algorithms (Decision Trees)
- ✅ Distance-based Methods (KNN)
- ✅ Unsupervised Learning (K-Means Clustering)
- ✅ Algorithm Selection & Vergleich
- ✅ Eigene ML-Apps mit Streamlit bauen

## 🚀 So startest du

```bash
# Umgebung aufsetzen
pip install -r 04_Advanced_Algorithms/requirements.txt

# Notebooks ausführen
jupyter notebook 02_MLFlow_Big3_Tracking.ipynb
jupyter notebook 03_Bäume_Nachbarn_und_Clustering.ipynb
```

### 💡 Tipps für saubere Runs
- **Seeds & Versionen:** Seeds sind in den Notebooks gesetzt, Versionen werden geloggt – behalte das für Repro im Blick.
- **MLflow:** Default ist lokales Tracking (`file:./mlruns`). Falls der MLflow-Server läuft (`docker compose up -d mlflow`), setze `MLFLOW_TRACKING_URI=http://localhost:5001`.
- **Kleine Grids:** Die Hyperparameter-Raster sind schlank gehalten, damit die Demos schnell durchlaufen.
- **Apps/Deploy:** Nutze die Notebooks als Vorlage für Streamlit-Apps; Modelle mit Signaturen/Input-Beispielen loggen erleichtert späteres Serving.

---

**Viel Erfolg beim Vertiefen und Ausprobieren!**
