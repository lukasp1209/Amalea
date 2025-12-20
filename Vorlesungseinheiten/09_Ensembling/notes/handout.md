# Vorlesungsskript — Ensembling: Random Forests & Gradient Boosting

Dieses Skript begleitet die Vorlesungseinheit "Ensembling". Es vertieft die mathematischen Grundlagen, bietet Intuitionen zu den Algorithmen und fasst Best Practices für den produktiven Einsatz zusammen.

## 1. Kernaussagen & Motivation

- Ziel: Ensembling kombiniert mehrere Modelle, um Gesamtleistung und Robustheit zu verbessern (Varianz- und/oder Bias‑Reduktion).
- Random Forest (RF): Bagging (Bootstrap + Aggregation) von Entscheidungsbäumen → primär Varianzreduktion; robust gegenüber Rauschen und wenig Feature‑Engineering.
- Gradient Boosting (GB): sequentielle Fehleranpassung (Additive Modelle) → reduziert Bias, erfordert mehr Hyperparametertuning und Regularisierung.

## 2. Zentrale Formeln & Intuitionen

- Bagging‑Ensemble (Vorhersage):
	$$\hat{f}(x)=\frac{1}{M}\sum_{m=1}^{M} f_m(x)$$

- Gradient Boosting (Update‑Skizze):
	$$F_{0}(x)=\arg\min_{\gamma}\sum_i L(y_i,\gamma),\\
	F_{t+1}(x)=F_t(x)+\eta\,h_t(x)$$
	wobei $h_t$ auf den negativen Gradienten (Residuen) approximiert wird und $\eta$ die Lernrate ist.

- Feature Importance (RF): mittlere Reduktion der Impurity; Permutation Importance als robustere Alternative.

## 3. Experiment: Aufbau & Ergebnisse

- Datensatz: `sklearn.datasets.load_iris` (oder `load_breast_cancer` für binäre Klassifikation).
- Vorgehen: Train/Test‑Split (70/30), RF und GB mit Standard‑Hyperparametern (z.B. 100 Bäume), Accuracy & Classification Report; zusätzlich Cross‑Validation (5‑fold).
- Wichtige Visualisierungen: Feature importances (Barplot), Lernkurve (Training/Validation Accuracy vs. Trainingsgröße), Vergleichs‑Metriken (Accuracy, Precision, Recall, ggf. ROC/AUC für binär).

## 4. Praktische Hinweise & Empfehlungen

- Hyperparameter (Kurz):
	- RF: `n_estimators`, `max_depth`, `max_features`.
	- GB: `n_estimators`, `learning_rate`, `max_depth`, `subsample`.
- Vermeidung von Overfitting: frühes Stoppen (early_stopping_rounds bei GB), reduzierte `max_depth`, Subsampling.
- Wann welches Modell?: RF als schnelle, robuste Baseline; GB für höhere Performance nach sorgfältigem Tuning.

Weiterführende Links

- scikit‑learn: https://scikit-learn.org/stable/modules/ensemble.html
- Friedman, Hastie, Tibshirani — The Elements of Statistical Learning

Praktischer Zusatz: Das beiliegende `code/demo.ipynb` und `code/demo_run.py` führen das kleine Experiment aus und speichern Plots in `assets/`.
