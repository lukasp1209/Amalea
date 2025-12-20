# Glossar: Alle Begriffe erklärt (W01–W07)

## 🐍 Python
- Datentypen, Kontrollstrukturen, Funktionen, Module, virtuellen Umgebungen, Packaging-Basics.

## 📊 Pandas & NumPy
- DataFrames, Series, Indexing/Selection, Groupby/Aggregation, Joins/Merges, Vektorisierung, Broadcasting.

## 🐳 Docker & Containerisierung
- Images, Container, Dockerfile, Compose, Volumes, Ports, Layer Cache, Multi-Stage Builds.

## 🔄 QUA³CK & ML-Workflow
- QUA³CK-Phasen (Question, Understand, Acquire & Clean, Analyze, App, Conclusion/Kommunikation), Reproduzierbarkeit, Seeds, Experiments.

## 🤖 Machine Learning (klassisch)
- Features/Labels, Train/Test Split, Pipelines, StandardScaler, Regression, Klassifikation, Cross-Validation, Hyperparameter-Tuning.
- **Spezifische Algorithmen:** Decision Trees (Gini/Entropy, Pruning), K-Nearest Neighbors (Distance Metrics, k-Wahl), K-Means Clustering (Elbow Method, Silhouette Score), Random Forest (Bagging, Feature Importance), Gradient Boosting (XGBoost Light).

## 📈 Evaluation & Metriken
- Accuracy/Precision/Recall/F1, ROC-AUC, RMSE/MAE/R², Confusion Matrix, Calibration, Train/Val/Test.

## 🔒 MLOps & Experiment Tracking
- MLflow Tracking/Artifacts/Models, Experiments/Runs, Params/Metrics, Model Registry (Staging/Production Aliases), DVC für Daten/Artefakte-Versionierung.
- **CI/CD:** GitHub Actions, Automated Testing, Deployment Pipelines.
- **Monitoring:** Model Drift (Feature/Prediction), Latency, Error Rates, Prometheus/Grafana.

## 🧠 Deep Learning (Keras/TensorFlow)
- Keras Sequential/Functional API, Dense Layers, Aktivierungen (ReLU, Sigmoid, Softmax), Loss/Optimizer/Scheduler, Regularisierung (Dropout/L2), Transfer Learning Lite.
- **Backpropagation:** Gradient Descent, Chain Rule, Vanishing Gradients.

## 🖼️ Computer Vision (OpenCV/CNN)
- Convolution/Pooling, Feature Maps, Data Augmentation, Edge/Feature-Extraction (Canny/SIFT-ähnliche Patterns), Pretrained Backbones als Feature-Extractor.
- **CNN Architekturen:** Conv2D, MaxPooling, Flatten, Fully Connected.

## 📝 NLP & Transformers
- Tokenization, Embeddings, Encoder/Decoder, HF Pipelines (Sentiment, QA, Text-Generation), kleinere CPU-freundliche Modelle (DistilBERT, Tiny-GPT-2).
- **Attention Mechanism:** Scaled Dot-Product, Multi-Head Attention, Self-Attention.

## 🌐 FastAPI & Serving
- Endpoints, Schemas/Pydantic, Dependency Injection (leicht), Uvicorn, Response Models, Health Checks, Logging/Monitoring Hooks.
- **API Design:** RESTful, Async Support, CORS.

## 🎯 Streamlit (Apps & Dashboards)
- Widgets/State, Caching, Layout/Columns, File Upload, Charting (Plotly/Altair), Deployment-Hinweise (Cloud/Compose).
- **Interaktivität:** Session State, Callbacks, Forms.

## ☁️ Deployment & Cloud
- Compose-Stacks (API + Dashboards), Ports/Env Vars, Secrets, Slim vs. Full Images, Reproduzierbare Envs über Requirements/Locks.
- **Container Orchestration:** Docker Compose Profiles (full/slim).

## ⚙️ Development Tools & Testing
- **Version Control:** Git, GitHub (Issues, PRs, Actions).
- **Code Quality:** Ruff (Linting), Black (Formatting), mypy (Type Checking).
- **Testing:** pytest (Unit/Integration Tests), Coverage, Smoke Tests (nbconvert).
- **Build Tools:** Makefile (install, lint, fmt, test, smoke-notebooks).

## 🔢 Mathematische Grundlagen (ML/DL)
- **Lineare Algebra:** Vektoren/Matrizen, Eigenvalues, SVD.
- **Statistik:** Mean/Variance, Distributions, Hypothesis Testing.
- **Optimierung:** Gradient Descent, Momentum, Adam, Learning Rate Scheduling.
- **Bias-Variance Tradeoff:** Underfitting/Overfitting, Regularization.

## ⚡ Troubleshooting & Best Practices
- Reproduzierbarkeit (Locks/Seeds), Ressourcen-Check (CPU/GPU/RAM), häufige Fehler (Port belegt, fehlende Env Vars), Logging & Monitoring Basics.
- **Security:** Token Management, Secrets Handling, Firewall Rules.
