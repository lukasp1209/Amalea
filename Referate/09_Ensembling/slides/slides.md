% Vorlesung — Ensembling: Random Forests & Gradient Boosting

Slide 1 — Titel
- Titel, Name, Datum, Lernziele (3 Ziele: Intuition, Formeln, kurzes Demo‑Ergebnis)

Slide 2 — Motivation
- Warum Ensembling? Beispiele: Rauschen reduzieren, Stabilität erhöhen, bessere Generalisierung.

Slide 3 — Random Forest (Kernidee)
- Bootstrap + Decision Trees → Aggregation (Majority voting / Averaging).
- Vorteil: robust, wenig Tuning; Nachteil: weniger interpretierbar als Einzelbaum.

Slide 4 — Random Forest (Technische Details)
- OOB‑Schätzung (Out‑of‑Bag), `max_features`, `n_estimators`, Feature Importance Grundlagen.

Slide 5 — Gradient Boosting (Kernidee)
- Additive Modellbildung; jeder Baum approximiert Residuen des vorherigen.
- Update‑Formel: $F_{t+1}=F_t+\eta h_t$; Bedeutung von $\eta$ (learning rate).

Slide 6 — Gradient Boosting (Praktische Aspekte)
- Hyperparameter: `learning_rate`, `n_estimators`, `max_depth`, `subsample`.
- Regularisierung und early stopping.

Slide 7 — Experiment: Setup
- Datensatz, Metriken, Cross‑Validation, Darstellung der Plots (Feature importances, learning curve).

Slide 8 — Ergebnisse (Beispieltabellen)
- Accuracy (Test), kurze Confusion Matrix oder Klassifikationsmetriken.

Slide 9 — Visuals
- Feature importance (RF vs GB), Lernkurven (Training vs Validation).

Slide 10 — Praxis‑Tipps & Checkliste
- Schritt‑für‑Schritt: Baseline → RF → GB + Tuning → CV & early stopping.

Slide 11 — Häufige Fehler & Troubleshooting
- Overfitting bei zu vielen Bäumen/hoher `max_depth`, falsche CV‑Strategie, Datenlecks.

Slide 12 — Quellen & Kontakt
- scikit‑learn, ESL (Hastie et al.), Repo‑Pfad und Hinweis auf `code/demo.ipynb`.
