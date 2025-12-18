# 👁️ 06 Computer Vision & NLP - AMALEA 2025

**CNNs, Deep Learning und moderne Computer Vision für Portfolio-Projekte**

> 🎓 **AMALEA Integration**: Angewandte Machine Learning Algorithmen  
> 📹 **Video-Serie**: 8 strukturierte Lernvideos  
> 🚀 **Portfolio-Ready**: 4 Streamlit Cloud Apps  
> 💼 **IU Assessment**: Optimiert für Bewertungskriterien

---

## 🎯 AMALEA Wochenziele

Nach **Woche 6** beherrschen Sie:
- ✅ **Convolutional Neural Networks** von Grund auf verstehen
- ✅ **Computer Vision Pipelines** mit OpenCV entwickeln
- ✅ **Data Augmentation** für robuste Modelle
- ✅ **Transfer Learning** mit Pre-trained Models
- ✅ **Portfolio Apps** für CV-Projekte erstellen
- ✅ **QUA³CK Integration** für strukturierte CV-Entwicklung

## � AMALEA Video Integration

| Video | Thema | Notebook | Streamlit App |
|-------|-------|----------|---------------|
| **Video 6.1** | CNN-Grundlagen & Filter | `06_01_CNN_Grundlagen.ipynb` | `06_01_streamlit_cnn_filter.py` |
| **Video 6.2** | Computer Vision Pipeline | `06_02_Computer_Vision_Anwendungen.ipynb` | `06_02_streamlit_cv_apps.py` |
| **Video 6.3** | Data Augmentation Strategien | `06_03_Data_Augmentation.ipynb` | `06_03_streamlit_data_augmentation.py` |
| **Video 6.4** | Transfer Learning & Hugging Face | `06_04_Transfer_Learning.ipynb` | `06_04_streamlit_transfer_learning.py` |

---

## �📚 Modernisierte Notebooks (2025)

### 🔍 06.1 CNN Grundlagen (`06_01_CNN_Grundlagen.ipynb`)
**✅ QUA³CK-strukturiert - CNNs verstehen und implementieren**

**🎯 AMALEA Lernziele:**
- **Q**uestion: Warum sind CNNs für Bilder optimal?
- **U**nderstand: CNN-Architektur (Convolution, Pooling, Dense)
- **A**cquire: CIFAR-10 Dataset laden und vorbereiten
- **A**nalyze: TensorFlow/Keras CNN-Implementierung + Feature Maps
- **A**pp: Streamlit-App für interaktive Filter-Experimente
- **C**&**K**: Portfolio-Dokumentation und Deployment

**💻 Portfolio App:** `06_01_streamlit_cnn_filter.py`
- 🎮 Interaktive Filter-Tests mit eigenen Bildern
- 📊 Live Parameter-Anpassung und Performance-Tracking
- 🔍 Konvolutions-Kernel Visualisierung
- 📈 MLFlow Integration für Experiment Tracking

### 📊 06.2 Computer Vision Anwendungen (`06_02_Computer_Vision_Anwendungen.ipynb`)
**✅ QUA³CK-strukturiert - OpenCV Mastery für Portfolio**

**🎯 AMALEA Lernziele:**
- **Q**uestion: Welche CV-Algorithmen lösen reale Probleme?
- **U**nderstand: Convolution mathematisch + Edge Detection
- **A**cquire: Eigene Bilder und OpenCV Integration
- **A**nalyze: Object Detection, Segmentation, Feature Matching
- **A**pp: Multi-Algorithmus CV-Dashboard
- **C**&**K**: Professional CV-Pipeline Dokumentation

**💻 Portfolio App:** `06_02_streamlit_cv_apps.py`
- 🔧 Multiple CV-Algorithmen (Canny, Sobel, SIFT, ORB)
- 📸 Upload eigener Bilder für Analyse
- ⚙️ Real-time Parameter-Tuning
- 📊 Algorithm Performance Comparison

### 🎨 06.3 Data Augmentation (`06_03_Data_Augmentation.ipynb`) 
**✅ QUA³CK-strukturiert - Robuste Modelle durch smarte Datenvergrößerung**

**🎯 AMALEA Lernziele:**
- **Q**uestion: Wie verhindert Data Augmentation Overfitting?
- **U**nderstand: Augmentation Impact auf Model Performance
- **A**cquire: CIFAR-10 + Custom Dataset Augmentation
- **A**nalyze: TensorFlow Layers + Albumentations Library
- **A**pp: Interactive Augmentation Parameter Explorer
- **C**&**K**: Augmentation Strategy für Portfolio

**💻 Portfolio App:** `06_03_streamlit_data_augmentation.py`
- 🎛️ Interactive Augmentation Parameter-Tests
- 📊 Live Performance Impact Visualization
- 🔍 CIFAR-10 Dataset Explorer mit Augmentation Preview
- 📈 Before/After Model Performance Analytics

### ✅ 06.4 Transfer Learning (`06_04_Transfer_Learning.ipynb`)
**✅ QUA³CK-strukturiert - Pre-trained Models mit Hugging Face & TensorFlow**

**🎯 AMALEA Lernziele:**
- **Q**uestion: Warum ist Transfer Learning so effektiv?
- **U**nderstand: Pre-trained Models (ResNet, EfficientNet, ViT)
- **A**cquire: Custom Dataset für Fine-tuning
- **A**nalyze: Hugging Face Transformers + TensorFlow Hub
- **A**pp: Transfer Learning Comparison Dashboard
- **C**&**K**: Production-Ready Model Deployment

**💻 Portfolio App:** `06_04_streamlit_transfer_learning.py`
- 🤖 Multiple Pre-trained Model Comparison
- 🎯 Custom Dataset Fine-tuning Interface
- 📊 Performance Benchmarking Dashboard
- 🚀 One-Click Model Deployment

## 🚀 AMALEA Schnellstart

```bash
# Umgebung
pip install -r ../requirements.txt  # oder gezielt: pip install -r requirements.streamlit.txt

# Ordner
cd 06_Computer_Vision_NLP

# Streamlit Apps (Auswahl)
streamlit run 06_01_streamlit_cnn_filter.py          # CNN Filter Demo
streamlit run 06_02_streamlit_cv_apps.py             # CV Applications Suite  
streamlit run 06_03_streamlit_data_augmentation.py   # Augmentation Explorer
streamlit run 06_04_streamlit_transfer_learning.py   # Transfer Learning Hub

# Notebooks
jupyter notebook 06_01_CNN_Grundlagen.ipynb
jupyter notebook 06_02_Computer_Vision_Anwendungen.ipynb
jupyter notebook 06_03_Data_Augmentation.ipynb
jupyter notebook 06_04_Transfer_Learning.ipynb

# MLflow (optional)
mlflow ui --port 5000  # http://localhost:5000
```

## 📁 AMALEA Struktur (Stand)

```
06_Computer_Vision_NLP/
├── 06_01_CNN_Grundlagen.ipynb
├── 06_02_Computer_Vision_Anwendungen.ipynb
├── 06_03_Data_Augmentation.ipynb
├── 06_04_Transfer_Learning.ipynb
├── 06_01_streamlit_cnn_filter.py
├── 06_02_streamlit_cv_apps.py
├── 06_03_streamlit_data_augmentation.py
├── 06_04_streamlit_transfer_learning.py
├── utils.py
├── data/ (Datasets/NPY)
└── images/ (Visualisierungen)
```

## � AMALEA Portfolio Integration

### 💼 IU Assessment Kriterien

| Kriterium | CV Notebook Coverage | Portfolio App | QUA³CK Phase |
|-----------|---------------------|---------------|--------------|
| **Problemdefinition** | Business Use Cases für CV | Interactive Problem Selection | **Q**uestion |
| **Datenverständnis** | CIFAR-10 + Custom Dataset EDA | Data Upload & Exploration | **U**nderstand |
| **Datenaufbereitung** | Augmentation + Preprocessing | Real-time Data Pipeline | **A**cquire & Clean |
| **Modellierung** | CNN, Transfer Learning | Interactive Model Training | **A**nalyze |
| **Evaluation** | Performance Metrics & Visualizations | Live Model Comparison | **A**nalyze |
| **Deployment** | Model Export & Optimization | Streamlit Cloud Apps | **A**pp |
| **Dokumentation** | Comprehensive QUA³CK Documentation | Portfolio Presentation | **C**&**K** |

### 🌟 Portfolio Differentiators

#### 🚀 **Technical Excellence**
- **State-of-the-Art Models**: EfficientNet, Vision Transformers, CLIP
- **Modern Tools**: TensorFlow 2.15+, Hugging Face Transformers, OpenCV 4.9+
- **MLOps Integration**: MLFlow Tracking, Model Registry, Automated Deployment
- **Cloud Ready**: Streamlit Cloud, Docker, GitHub Actions

#### 📊 **Professional Presentation**
- **Interactive Dashboards**: Real-time Parameter Tuning
- **Performance Analytics**: Comprehensive Model Evaluation
- **Visual Storytelling**: Effective Data Visualization
- **Business Context**: Real-world Problem Solving

#### 🔬 **Research Quality**
- **Reproducible Experiments**: Seed Control, Environment Specification
- **A/B Testing**: Model Comparison Frameworks
- **Ablation Studies**: Feature Impact Analysis
- **Literature Integration**: Current Research References

---

## 🎯 Wochenziele (AMALEA Certified)

### ✅ **Woche 6 Milestones**
- [ ] **CNN Mastery**: Implementierung und Verständnis von Grund auf
- [ ] **CV Pipeline**: End-to-End Computer Vision Workflow
- [ ] **Data Augmentation**: Robuste Modell-Entwicklung
- [ ] **Transfer Learning**: Production-Ready Model Development
- [ ] **Portfolio Apps**: 4 Streamlit Cloud Deployments
- [ ] **MLOps Integration**: Experiment Tracking und Model Management

### 🏆 **Portfolio Outcomes**
- **Technical Depth**: Advanced CV Concepts demonstriert
- **Practical Skills**: Real-world Computer Vision Applications
- **Professional Tools**: Industry-Standard Development Workflow
- **Assessment Ready**: Alle IU Kriterien systematisch erfüllt

---

## 💡 AMALEA Didaktischer Ansatz (2025)

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
