import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def true_fun(X):
    return np.cos(1.5 * np.pi * X)

def run_simulation():
    np.random.seed(0)
    n_samples = 20
    n_simulations = 20 # Wie oft wir das Experiment wiederholen
    
    # Wir vergleichen zwei Modelle
    degrees = [1, 9] # Grad 1 (Linear, High Bias), Grad 9 (Komplex, High Variance)
    
    X_plot = np.linspace(0, 1, 100)
    
    plt.figure(figsize=(12, 5))
    
    for i, degree in enumerate(degrees):
        ax = plt.subplot(1, 2, i + 1)
        
        # Speicher für die Vorhersagen aller Simulationen
        all_predictions = []
        
        for _ in range(n_simulations):
            # 1. Wir ziehen jedes Mal NEUE Daten aus der gleichen Verteilung
            X = np.sort(np.random.rand(n_samples))
            y = true_fun(X) + np.random.randn(n_samples) * 0.1
            
            # 2. Modell trainieren
            polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
            linear_regression = LinearRegression()
            pipeline = Pipeline([("polynomial_features", polynomial_features),
                                 ("linear_regression", linear_regression)])
            pipeline.fit(X[:, np.newaxis], y)
            
            # 3. Vorhersage speichern
            y_pred = pipeline.predict(X_plot[:, np.newaxis])
            all_predictions.append(y_pred)
            
            # Plotten der einzelnen Modell-Kurve (dünn)
            plt.plot(X_plot, y_pred, color='grey', alpha=0.2)
            
        # Durchschnittliche Vorhersage über alle Simulationen
        avg_prediction = np.mean(all_predictions, axis=0)
        
        # Wahre Funktion
        plt.plot(X_plot, true_fun(X_plot), label="Wahre Funktion", color='green', linewidth=2)
        
        # Durchschnitts-Modell
        plt.plot(X_plot, avg_prediction, label="Durchschnitts-Modell", color='red', linestyle='--', linewidth=2)
        
        if degree == 1:
            plt.title(f"Grad {degree}: High Bias (Underfitting)\nModelle sind stabil, aber falsch.")
        else:
            plt.title(f"Grad {degree}: High Variance (Overfitting)\nModelle schwanken stark, treffen im Mittel aber gut.")
            
        plt.ylim(-2, 2)
        plt.legend()

    print("Plot wird erstellt...")
    plt.tight_layout()
    plt.show()
    
    print("\n--- Erklärung ---")
    print("Links (Grad 1): Die grauen Linien liegen alle eng beieinander (niedrige Varianz).")
    print("Aber sie können die Kurve nicht abbilden (hoher Bias/Fehler).")
    print("\nRechts (Grad 9): Die grauen Linien zappeln wild (hohe Varianz).")
    print("Jedes einzelne Modell ist stark vom Zufall der Daten abhängig.")
    print("Interessant: Der Durchschnitt (rot) ist fast perfekt, aber wir haben in der Praxis meist nur EINEN Datensatz (eine graue Linie).")

if __name__ == "__main__":
    run_simulation()