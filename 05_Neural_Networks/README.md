# 🧠 05 Neural Networks

**Neural Networks und Deep Learning Grundlagen**

## 📚 Inhalt

- `04_Neural_Networks_in_Streamlit.ipynb` - Neural Networks interaktiv erkundet
- `neural_network_playground.py` - Interaktive Streamlit-App für NN-Experimente

### 🔄 AMALEA-Integration

| Original AMALEA Notebook | Integrierte Konzepte |
|--------------------------|---------------------|
| 🧠 "Jetzt geht's in die Tiefe" | Neuron-Grundlagen, Gewichte & Bias, erste Architektur |
| 🏔️ "Wir trainieren nur bergab" | Backpropagation, Gradient Descent, Optimizer |
| 📊 "Regression II" | Neural Networks für kontinuierliche Vorhersagen |
| 🍦 "Classification Softmax" | Multi-Class Klassifikation, One-Hot Encoding |

## 📁 Verzeichnisinhalt

```
Woche_4_Deep_Learning/
├── 04_Neural_Networks_in_Streamlit.ipynb  # Hauptnotebook mit allen Konzepten
├── neural_network_playground.py           # Interaktive Streamlit-App
└── README.md                              # Diese Dokumentation
```

## 🚀 Getting Started

```bash
# Umgebung vorbereiten
pip install -r 05_Neural_Networks/requirements.txt

# Notebook ausführen
jupyter notebook 04_Neural_Networks_in_Streamlit.ipynb

# Streamlit-App (optional)
streamlit run neural_network_playground.py
# Standard: http://localhost:8501
```

## 🧠 Lernziele

Nach Abschluss dieser Woche kannst du:

- ✅ **Neuronale Netzwerke** von Grund auf verstehen und implementieren
- ✅ **Aktivierungsfunktionen** (ReLU, Sigmoid, Tanh) richtig einsetzen  
- ✅ **Backpropagation** und Gradient Descent erklären
- ✅ **Hyperparameter** (Learning Rate, Architecture) intelligent wählen
- ✅ **Regression** und **Klassifikation** mit Neural Networks
- ✅ **Softmax** und **One-Hot Encoding** für Multi-Class Probleme
- ✅ **Interaktive Streamlit-Apps** für Machine Learning erstellen
- ✅ **Training-Probleme** debuggen und Performance evaluieren

## 🎮 Interaktive Features

Die Streamlit-App bietet 6 interaktive Bereiche:

1. **🧠 Einfachstes Neuron** - Verstehe die Grundlagen
2. **📈 Aktivierungsfunktionen** - Visualisiere und vergleiche
3. **🎯 Regression Demo** - Trainiere Networks live
4. **🏷️ Klassifikation Demo** - Entscheidungsgrenzen sehen
5. **🍦 Softmax Explorer** - Multi-Class Klassifikation verstehen
6. **🎮 Interaktiver Playground** - Experimentiere frei

## 🛠️ Technische Anforderungen

- Installiere die Pakete über `pip install -r 05_Neural_Networks/requirements.txt` (oder die Repo-`requirements.txt`, falls du den vollen Stack brauchst).
- TensorFlow ist schwergewichtig; auf schwächerer Hardware ggf. CPU-Only oder Slim-Umgebung nutzen.
- Seeds und Versionen werden im Notebook geloggt (Reproduzierbarkeit).

## 📝 Übungen & Projekte

### Grundübungen
1. **Eigenes Neuron implementieren** - XOR-Problem lösen
2. **Aktivierungsfunktionen vergleichen** - Performance analysieren
3. **Learning Rate Experiment** - Konvergenz dokumentieren
4. **Softmax von Hand** - Mathematisches Verständnis

### Portfolio-Projekt
**Ziel**: Erstelle eine eigene Neural Network Streamlit-App

**Anforderungen**:
- 📊 Eigener Datensatz (CSV Upload)
- 🎛️ Interaktive Hyperparameter
- ⚡ Live-Training mit Progress
- 📈 Performance-Visualisierung
- 🎯 Vorhersagen für neue Eingaben

## 🔧 Troubleshooting

### Häufige Probleme

1. **Import Errors**: Installiere requirements-2025.txt
   ```bash
   pip install -r ../requirements-2025.txt
   ```

2. **Streamlit startet nicht**: Port bereits belegt
   ```bash
   streamlit run neural_network_playground.py --server.port 8502
   ```

3. **Slow Training**: Reduziere Datenmenge oder max_iter

4. **Poor Performance**: 
   - Check Daten-Skalierung (StandardScaler)
   - Adjust Learning Rate (0.001-0.1)
   - More Hidden Units für komplexere Probleme

## 🎯 Bewertungskriterien

Für Portfolio-Projekte:

- **📊 Datenqualität** (20%): Saubere, relevante Daten
- **🧠 Neural Network** (30%): Angemessene Architektur & Hyperparameter
- **🎨 UI/UX** (20%): Benutzerfreundliche Streamlit-App
- **📈 Evaluation** (20%): Aussagekräftige Metriken & Visualisierung
- **📝 Dokumentation** (10%): Code-Kommentare & README

## 🔮 Ausblick: Woche 5

**Next Level: Convolutional Neural Networks**
- 🖼️ Computer Vision Grundlagen
- 🔍 Convolution & Pooling verstehen
- 👁️ Image Classification praktisch
- 🎨 Data Augmentation Techniken
- 📱 Transfer Learning für echte Projekte

## 📚 Zusätzliche Ressourcen

### Weitere Lernmaterialien
- 📖 **"Deep Learning"** - Ian Goodfellow (Standardwerk)
- 🎓 **CS231n** - Stanford Convolutional Networks Course
- 🧠 **Neural Network Playground** - playground.tensorflow.org
- 📺 **3Blue1Brown** - Neural Networks Serie (YouTube)

### Tools für größere Projekte
- 🔧 **TensorFlow/Keras** - Industry Standard
- ⚡ **PyTorch** - Research & Flexibilität
- 📊 **Weights & Biases** - Experiment Tracking
- 🐳 **Docker** - Reproduzierbare Umgebungen

---

## 📞 Support

Bei Fragen oder Problemen:
1. 📖 Konsultiere das Jupyter Notebook
2. 🎮 Teste verschiedene Parameter in der Streamlit-App
3. 💬 Nutze die Diskussionsforen des Kurses
4. 🔍 Google ist dein Freund für spezifische Errors

---

### 💡 Praktische Tipps
- Epochen sind im Notebook reduziert, damit Demos schnell laufen; für bessere Performance Epochen schrittweise erhöhen.
- Bei Streamlit-Apps: Modelle mit `model.save(...)` speichern und im App-Code laden, um Bootzeiten kurz zu halten.
- Ports belegt? `streamlit run neural_network_playground.py --server.port 8502` nutzen.
- Für reproduzierbare Runs: Seeds setzen (numpy, tensorflow) und Versionen im Notebook mitloggen (bereits vorbereitet).

---

**🎉 Viel Erfolg beim Lernen von Neural Networks!**

*AMALEA 2025 - Modernisiert für die Zukunft* 🚀
