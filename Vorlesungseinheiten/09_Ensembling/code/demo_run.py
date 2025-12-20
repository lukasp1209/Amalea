#!/usr/bin/env python3
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score

BASE = os.path.dirname(__file__)
ASSETS = os.path.abspath(os.path.join(BASE, '..', 'assets'))
os.makedirs(ASSETS, exist_ok=True)

data = load_iris()
X = data.data
y = data.target
feature_names = data.feature_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)

rf = RandomForestClassifier(n_estimators=200, random_state=0)
gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, random_state=0)

rf.fit(X_train, y_train)
gb.fit(X_train, y_train)

out_lines = []
for name, model in [("RandomForest", rf), ("GradientBoosting", gb)]:
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    cv = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    out_lines.append(f"{name} accuracy (test): {acc:.3f}")
    out_lines.append(f"{name} accuracy (5-fold CV mean): {cv.mean():.3f} (std {cv.std():.3f})")

importances = pd.DataFrame({
    'feature': feature_names,
    'rf_importance': rf.feature_importances_,
    'gb_importance': gb.feature_importances_
})
out_lines.append('\nFeature importances (RF sorted):')
out_lines += list(importances.sort_values('rf_importance', ascending=False).to_string(index=False).splitlines())

# plot and save feature importances
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(data=importances.melt(id_vars='feature', value_vars=['rf_importance','gb_importance'], var_name='model', value_name='importance'), x='feature', y='importance', hue='model', ax=ax)
plt.xticks(rotation=20)
plt.tight_layout()
png_path = os.path.join(ASSETS, 'feature_importances.png')
fig.savefig(png_path, dpi=200)
plt.close(fig)
out_lines.append(f"\nSaved plot: {png_path}")

# learning curve for RandomForest (example)
train_sizes, train_scores, test_scores = learning_curve(rf, X, y, cv=5, train_sizes=[0.2,0.4,0.6,0.8,1.0], scoring='accuracy')
train_mean = train_scores.mean(axis=1)
test_mean = test_scores.mean(axis=1)
fig2, ax2 = plt.subplots()
ax2.plot(train_sizes, train_mean, 'o-', label='Train')
ax2.plot(train_sizes, test_mean, 'o-', label='Validation')
ax2.set_xlabel('Training set size')
ax2.set_ylabel('Accuracy')
ax2.legend()
ax2.grid(True)
lc_path = os.path.join(ASSETS, 'learning_curve_rf.png')
fig2.savefig(lc_path, dpi=200)
plt.close(fig2)
out_lines.append(f"Saved learning curve: {lc_path}")

results_file = os.path.join(BASE, 'results.txt')
with open(results_file, 'w') as f:
    f.write('\n'.join(out_lines))

print('\n'.join(out_lines))
print('\nWrote results to', results_file)
