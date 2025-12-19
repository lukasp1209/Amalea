# 06 Computer Vision & NLP (neu)

Aktualisierte, schlanke Notebooks für schnelle CPU-Runs und klare Lernpfade. Vier Kern-Notebooks plus ein fünftes Bild-Sampler-Notebook für die bereitliegenden Assets.

## Inhalte & Lernziele
- **06_01_neu_CNN_Basics.ipynb**: Mini-CNN auf CIFAR-Subset, Feature-Maps, manueller Conv-Check gegen `tf.nn.conv2d`.
- **06_02_neu_OpenCV_Edge_Features.ipynb**: Dtype-sichere Edge/Contour-Pipeline (Canny, Sobel, Laplacian) und ORB-Keypoints.
- **06_03_neu_Data_Augmentation_Practice.ipynb**: Overfitting sichtbar machen, Keras-Aug vs. optional Albumentations, Vergleich der Accuracy.
- **06_04_neu_Transfer_Learning_Lite.ipynb**: EfficientNetB0 als Feature-Extractor, kleiner Head, optional leichtes Fine-Tuning, SavedModel-Export.
- **06_05_neu_Image_Sampler.ipynb**: Schneller Browser für die mitgelieferten Bilder; Edge/Contour/ORB/kleine Augmentations als Demo.

## Lernpfad & Ressourcen
| Notebook | Profil (Minimal/Standard/Vertiefung) | Laufzeit CPU (ca.) | RAM-Bedarf | Hinweise |
|---|---|---|---|---|
| 06_01_neu_CNN_Basics | 1 Epoch / 5k Samples / 64 Batch | 3-6 min | 2-3 GB | Für Deep: 5-10 Epochs; GPU beschleunigt stark |
| 06_02_neu_OpenCV_Edge_Features | Default | <2 min | <1 GB | Bilder kleiner skalieren (256px) für schwache Rechner |
| 06_03_neu_Data_Augmentation_Practice | 2 Epochs / 1.5k Samples / 128 Batch | 4-8 min | 3-4 GB | Deep: Albumentations aktivieren, 5 Epochs |
| 06_04_neu_Transfer_Learning_Lite | 2+1 Epochs / 2k Samples / 64 Batch | 8-15 min | 4-6 GB | Laden der ImageNet-Gewichte einmalig; GPU sehr empfohlen |
| 06_05_neu_Image_Sampler | Interaktiv | <2 min | <1 GB | Fällt auf synthetische Demo-Bilder zurück |

- **Minimal**: nur Kernzellen laufen lassen, reduzierte Samples/ Epochen wie oben; gut für CPU-Laptops.
- **Standard**: Voreinstellungen im Notebook nutzen.
- **Vertiefung**: mehr Epochen/Samples, zusätzliche Visuals (ggf. GPU verwenden).

## Schnellstart
```bash
# Umgebung
pip install -r ../requirements.txt

cd 06_Computer_Vision_NLP

# Notebooks öffnen (Beispiele)
jupyter notebook 06_01_neu_CNN_Basics.ipynb
jupyter notebook 06_02_neu_OpenCV_Edge_Features.ipynb
jupyter notebook 06_03_neu_Data_Augmentation_Practice.ipynb
jupyter notebook 06_04_neu_Transfer_Learning_Lite.ipynb
jupyter notebook 06_05_neu_Image_Sampler.ipynb
```

## Hinweise
- Alle neuen Notebooks sind CPU-freundlich ausgelegt; Epochen/Sample-Größen können weiter reduziert werden.
- Vortrainierte Gewichte (Transfer Learning) werden beim ersten Lauf geladen und gecacht.
- ORB wird als lizenzfreundliche Feature-Alternative genutzt; SIFT kann ergänzt werden, falls verfügbar.

## Assets
- Legacy-Notebooks, Streamlit-Skripte und Altdaten wurden entfernt.
- Der Ordner `images/` bleibt für Demos erhalten (wird im Image Sampler genutzt); fehlt er, fällt das Notebook automatisch auf synthetische Beispiele zurück.

## QUA³CK-Mapping (Notebook-Einstiege)
- **Q**uestion: 06_05 (Use-Case-Story) + 06_02 (Welche Features/Kanten warum?).
- **U**nderstand: 06_01 (Feature-Maps) + 06_03 (EDA/Augmentation-Vergleiche).
- **A**cquire & Clean: 06_02 (Dtype/Resize/Gray) + 06_03 (Aug-Pipelines).
- **A**nalyze: 06_01 (CNN) + 06_04 (Transfer Learning) + 06_03 (Aug vs. Baseline).
- **A**pp: 06_05 (interaktive Pipeline-Vorschau) + Export in 06_04.
- **C**&**K**: Selbstchecks/FAQs in jedem Notebook (siehe Abschlusszellen).
### 🔄 **QUA³CK-zentrierte Entwicklung**
1. 🎯 **Q**uestion: CV Business Problems definieren
2. 📊 **U**nderstand: Dataset Analysis mit modernen Tools
3. 🧹 **A**cquire & Clean: Automated Data Pipelines
4. 🤖 **A**nalyze: CNN + Transfer Learning + Evaluation
5. � **A**pp: Streamlit Cloud Portfolio Deployment
6. 📋 **C**&**K**: Professional Documentation + Presentation

### 🎮 **Hands-on Learning Experience**
- **Interactive Notebooks**: Real-time Code Execution
- **Visual Learning**: Extensive Plots und Animations
- **Parameter Exploration**: Streamlit Widgets für Experimentation
- **Portfolio Building**: Assessment-optimierte Projekt-Struktur

### 📈 **Progressive Complexity**
- **Beginner**: CNN Basics mit CIFAR-10
- **Intermediate**: Custom CV Pipelines mit OpenCV
- **Advanced**: Transfer Learning mit Hugging Face
- **Expert**: Production Deployment auf Streamlit Cloud

### 🤝 **Community & Support**
- **Code Repository**: Vollständig dokumentiert auf GitHub
- **Video Integration**: 8 strukturierte AMALEA Lernvideos
- **Office Hours**: Q&A Sessions für Portfolio Development
- **Peer Learning**: Collaborative Development Approaches

---

## 🌟 Computer Vision Excellence Achieved

**Nach AMALEA Woche 6 sind Sie bereit für:**
- 🏢 **Industry CV Projects** mit modernen Deep Learning Tools
- 🎓 **Academic Excellence** durch systematic QUA³CK Application
- 💼 **Portfolio Distinction** mit Professional-Grade CV Applications
- 🚀 **Career Advancement** durch demonstrable CV Expertise

**AMALEA Computer Vision: Where Theory Meets Practice! 👁️🧠**
