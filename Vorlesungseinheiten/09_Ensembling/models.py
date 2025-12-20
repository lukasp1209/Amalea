import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.model_selection import train_test_split

def get_dataset(name, n_samples=500, noise=0.3):
    """Erzeugt synthetische Datensätze für Klassifikation."""
    if name == "Moons":
        X, y = make_moons(n_samples=n_samples, noise=noise, random_state=42)
    elif name == "Circles":
        X, y = make_circles(n_samples=n_samples, noise=noise, factor=0.5, random_state=42)
    else:
        X, y = make_classification(n_samples=n_samples, n_features=2, n_redundant=0, 
                                   n_informative=2, random_state=42, n_clusters_per_class=1)
        # Verschieben für bessere Visualisierung
        X += 2 
        
    return train_test_split(X, y, test_size=0.3, random_state=42)

def get_classifier(type_name, params):
    """Factory für verschiedene Classifier-Typen."""
    if type_name == "Decision Tree (Single)":
        return DecisionTreeClassifier(
            max_depth=params.get("max_depth", 5),
            random_state=42
        )
        
    elif type_name == "Random Forest (Bagging)":
        return RandomForestClassifier(
            n_estimators=params.get("n_estimators", 100),
            max_depth=params.get("max_depth", 5),
            random_state=42
        )
        
    elif type_name == "Gradient Boosting (Boosting)":
        return GradientBoostingClassifier(
            n_estimators=params.get("n_estimators", 100),
            learning_rate=params.get("learning_rate", 0.1),
            max_depth=params.get("max_depth", 3),
            random_state=42
        )
        
    elif type_name == "Voting Classifier (Stacking-Light)":
        # Heterogenes Ensemble
        clf1 = LogisticRegression(random_state=1)
        clf2 = RandomForestClassifier(n_estimators=50, random_state=1)
        clf3 = SVC(probability=True, random_state=1)
        
        return VotingClassifier(
            estimators=[('lr', clf1), ('rf', clf2), ('svc', clf3)],
            voting='soft'
        )
    
    return DecisionTreeClassifier()

def calculate_metrics(model, X_test, y_test):
    """Berechnet Accuracy und gibt sie formatiert zurück."""
    score = model.score(X_test, y_test)
    return {
        "accuracy": score,
        "error_rate": 1 - score
    }