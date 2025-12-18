
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import make_regression, make_classification, load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix
import seaborn as sns

# 🎯 Streamlit App Configuration
st.set_page_config(
    page_title="🧠 Neural Network Playground - AMALEA 2025",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 📊 Title and Introduction
st.title("🧠 Neural Network Playground")
st.markdown("**Interaktive Demo der AMALEA Neural Network Konzepte**")

# Sidebar für Navigation
st.sidebar.title("🎛️ Navigation")
app_mode = st.sidebar.selectbox(
    "Wähle einen Bereich:",
    ["🧠 Einfachstes Neuron", "📈 Aktivierungsfunktionen", "🎯 Regression Demo", 
     "🏷️ Klassifikation Demo", "🎮 Interaktiver Playground"]
)

# ============================================================================
# 🧠 BEREICH 1: Einfachstes Neuron (aus AMALEA "Jetzt geht's in die Tiefe")
# ============================================================================

if app_mode == "🧠 Einfachstes Neuron":
    st.header("🧠 Einfachstes Neuron verstehen")
    st.markdown("**Aus dem ursprünglichen AMALEA-Kurs: 'Jetzt geht's in die Tiefe'**")
    
    # Interaktive Parameter
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎛️ Neuron-Parameter")
        w = st.slider("Gewicht (w)", -5.0, 5.0, -1.0, 0.1)
        b = st.slider("Bias (b)", -5.0, 5.0, 1.0, 0.1)
        
        # Formel anzeigen
        st.latex(f"f(x) = w \cdot x + b = {w} \cdot x + {b}")
        
    with col2:
        st.subheader("📊 Neuron-Verhalten")
        x_values = np.linspace(-10, 10, 100)
        y_values = w * x_values + b
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='Neuron Output'))
        fig.update_layout(
            title="Einfachstes Neuron: f(x) = w*x + b",
            xaxis_title="Input (x)",
            yaxis_title="Output f(x)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Beispielberechnung
    st.subheader("🧮 Beispiel-Berechnung")
    test_input = st.number_input("Teste Input-Wert:", value=5.0)
    result = w * test_input + b
    st.success(f"f({test_input}) = {w} × {test_input} + {b} = **{result:.2f}**")
    
    # AMALEA-Originale
    st.info("💡 **AMALEA-Original**: Mit w=-1, b=1 ergibt f(5) = -4")

# ============================================================================
# 📈 BEREICH 2: Aktivierungsfunktionen (AMALEA Deep Learning Grundlagen)
# ============================================================================

elif app_mode == "📈 Aktivierungsfunktionen":
    st.header("📈 Aktivierungsfunktionen verstehen")
    st.markdown("**Herzstück des Deep Learning - aus den ursprünglichen AMALEA-Notebooks**")
    
    # Funktionen definieren
    def relu(x):
        return np.maximum(0, x)
    
    def sigmoid(x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))  # Clip für numerische Stabilität
    
    def tanh_func(x):
        return np.tanh(x)
    
    def leaky_relu(x, alpha=0.01):
        return np.where(x > 0, x, alpha * x)
    
    # Interaktive Auswahl
    x = np.linspace(-5, 5, 1000)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎛️ Funktions-Parameter")
        
        show_relu = st.checkbox("ReLU", value=True)
        show_sigmoid = st.checkbox("Sigmoid", value=True)
        show_tanh = st.checkbox("Tanh", value=True)
        show_leaky = st.checkbox("Leaky ReLU", value=False)
        
        if show_leaky:
            alpha = st.slider("Leaky ReLU α", 0.01, 0.3, 0.01, 0.01)
    
    with col2:
        st.subheader("📊 Aktivierungsfunktionen")
        
        fig = go.Figure()
        
        if show_relu:
            fig.add_trace(go.Scatter(x=x, y=relu(x), mode='lines', name='ReLU: max(0,x)', line=dict(color='blue')))
        if show_sigmoid:
            fig.add_trace(go.Scatter(x=x, y=sigmoid(x), mode='lines', name='Sigmoid: 1/(1+e^(-x))', line=dict(color='red')))
        if show_tanh:
            fig.add_trace(go.Scatter(x=x, y=tanh_func(x), mode='lines', name='Tanh: tanh(x)', line=dict(color='green')))
        if show_leaky:
            fig.add_trace(go.Scatter(x=x, y=leaky_relu(x, alpha), mode='lines', name=f'Leaky ReLU (α={alpha})', line=dict(color='orange')))
        
        fig.update_layout(
            title="Aktivierungsfunktionen im Vergleich",
            xaxis_title="Input (x)",
            yaxis_title="Output f(x)",
            height=500,
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Verwendungszwecke
    st.subheader("🎯 Wann welche Funktion verwenden?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🔵 ReLU**
        - ✅ Standard für Hidden Layers
        - ✅ Schnell zu berechnen
        - ❌ "Dying ReLU" Problem
        """)
    
    with col2:
        st.markdown("""
        **🔴 Sigmoid**
        - ✅ Binäre Klassifikation (Output)
        - ✅ Werte zwischen 0 und 1
        - ❌ Vanishing Gradient Problem
        """)
    
    with col3:
        st.markdown("""
        **🟢 Tanh**
        - ✅ Werte zwischen -1 und 1
        - ✅ Zero-centered
        - ❌ Auch Vanishing Gradient
        """)

# ============================================================================
# 🎯 BEREICH 3: Regression Demo (aus AMALEA "Regression II")
# ============================================================================

elif app_mode == "🎯 Regression Demo":
    st.header("🎯 Neural Network Regression")
    st.markdown("**Aus dem ursprünglichen AMALEA-Kurs: 'Regression II - Künstliche Gehirne'**")
    
    # Daten generieren
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎛️ Daten-Parameter")
        n_samples = st.slider("Anzahl Samples", 50, 500, 200)
        noise_level = st.slider("Noise Level", 0.0, 50.0, 10.0)
        
        st.subheader("🧠 Netzwerk-Parameter")
        hidden_layers = st.selectbox("Hidden Layer", [(10,), (20,), (10, 5), (20, 10)])
        activation = st.selectbox("Aktivierung", ['relu', 'tanh', 'logistic'])
        learning_rate = st.selectbox("Learning Rate", [0.001, 0.01, 0.1])
        
        train_button = st.button("🚀 Trainiere Neural Network!")
    
    with col2:
        if train_button:
            # Daten erstellen
            X, y = make_regression(n_samples=n_samples, n_features=1, noise=noise_level, random_state=42)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Skalierung
            scaler_X = StandardScaler()
            scaler_y = StandardScaler()
            X_train_scaled = scaler_X.fit_transform(X_train)
            X_test_scaled = scaler_X.transform(X_test)
            y_train_scaled = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()
            
            # Neural Network trainieren
            with st.spinner("Training Neural Network..."):
                nn = MLPRegressor(
                    hidden_layer_sizes=hidden_layers,
                    activation=activation,
                    learning_rate_init=learning_rate,
                    max_iter=1000,
                    random_state=42
                )
                nn.fit(X_train_scaled, y_train_scaled)
                
                # Vorhersagen
                y_pred_scaled = nn.predict(X_test_scaled)
                y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()
            
            # Visualisierung
            fig = go.Figure()
            
            # Trainingsdaten
            fig.add_trace(go.Scatter(
                x=X_train.ravel(), y=y_train, mode='markers', 
                name='Training Data', opacity=0.6, marker=dict(color='blue')
            ))
            
            # Testdaten
            fig.add_trace(go.Scatter(
                x=X_test.ravel(), y=y_test, mode='markers', 
                name='Test Data (True)', marker=dict(color='red')
            ))
            
            # Vorhersagen
            fig.add_trace(go.Scatter(
                x=X_test.ravel(), y=y_pred, mode='markers', 
                name='Predictions', marker=dict(color='green', symbol='x', size=10)
            ))
            
            fig.update_layout(
                title="Neural Network Regression Results",
                xaxis_title="X",
                yaxis_title="y",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Metriken
            mse = mean_squared_error(y_test, y_pred)
            st.success(f"🎯 Mean Squared Error: **{mse:.2f}**")

# ============================================================================
# 🏷️ BEREICH 4: Klassifikation Demo (aus AMALEA "Classification Softmax")
# ============================================================================

elif app_mode == "🏷️ Klassifikation Demo":
    st.header("🏷️ Neural Network Klassifikation")
    st.markdown("**Aus dem ursprünglichen AMALEA-Kurs: 'Classification Softmax-Eis'**")
    
    # Dataset Auswahl
    dataset_choice = st.selectbox(
        "📊 Dataset wählen:",
        ["Iris (AMALEA-Klassiker)", "Künstliche Daten", "Kreise (Non-linear)"]
    )
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🧠 Netzwerk-Konfiguration")
        
        if dataset_choice == "Iris (AMALEA-Klassiker)":
            # Iris Dataset
            iris = load_iris()
            X, y = iris.data, iris.target
            feature_names = iris.feature_names
            target_names = iris.target_names
            
            # Feature Auswahl
            feature_1 = st.selectbox("Feature 1", feature_names, index=0)
            feature_2 = st.selectbox("Feature 2", feature_names, index=1)
            
            X_viz = X[:, [feature_names.index(feature_1), feature_names.index(feature_2)]]
            
        elif dataset_choice == "Künstliche Daten":
            n_samples = st.slider("Anzahl Samples", 100, 1000, 300)
            n_classes = st.slider("Anzahl Klassen", 2, 4, 3)
            X_viz, y = make_classification(
                n_samples=n_samples, n_features=2, n_redundant=0, 
                n_informative=2, n_clusters_per_class=1, n_classes=n_classes,
                random_state=42
            )
            target_names = [f"Klasse {i}" for i in range(n_classes)]
            
        else:  # Kreise
            from sklearn.datasets import make_circles
            n_samples = st.slider("Anzahl Samples", 100, 1000, 300)
            noise = st.slider("Noise", 0.0, 0.3, 0.1)
            X_viz, y = make_circles(n_samples=n_samples, noise=noise, random_state=42)
            target_names = ["Innen", "Außen"]
        
        # Netzwerk Parameter
        hidden_layers = st.selectbox("Hidden Layers", [(10,), (20,), (10, 5), (50, 20)])
        activation = st.selectbox("Aktivierung", ['relu', 'tanh', 'logistic'])
        solver = st.selectbox("Optimizer", ['adam', 'sgd', 'lbfgs'])
        
        train_classification = st.button("🚀 Trainiere Klassifikator!")
    
    with col2:
        if train_classification:
            # Daten aufteilen
            X_train, X_test, y_train, y_test = train_test_split(
                X_viz, y, test_size=0.2, stratify=y, random_state=42
            )
            
            # Skalierung
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Neural Network trainieren
            with st.spinner("Training Classifier..."):
                nn_clf = MLPClassifier(
                    hidden_layer_sizes=hidden_layers,
                    activation=activation,
                    solver=solver,
                    max_iter=1000,
                    random_state=42
                )
                nn_clf.fit(X_train_scaled, y_train)
                y_pred = nn_clf.predict(X_test_scaled)
            
            # Entscheidungsgrenze visualisieren
            h = 0.02
            x_min, x_max = X_viz[:, 0].min() - 1, X_viz[:, 0].max() + 1
            y_min, y_max = X_viz[:, 1].min() - 1, X_viz[:, 1].max() + 1
            xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                               np.arange(y_min, y_max, h))
            
            mesh_points = np.c_[xx.ravel(), yy.ravel()]
            mesh_points_scaled = scaler.transform(mesh_points)
            Z = nn_clf.predict(mesh_points_scaled)
            Z = Z.reshape(xx.shape)
            
            # Plot erstellen
            fig = go.Figure()
            
            # Entscheidungsgrenze
            fig.add_trace(go.Contour(
                x=np.arange(x_min, x_max, h),
                y=np.arange(y_min, y_max, h),
                z=Z,
                showscale=False,
                opacity=0.3,
                colorscale='Viridis'
            ))
            
            # Datenpunkte
            colors = ['red', 'blue', 'green', 'orange']
            for i, target_name in enumerate(target_names):
                mask = y == i
                fig.add_trace(go.Scatter(
                    x=X_viz[mask, 0], y=X_viz[mask, 1],
                    mode='markers', name=target_name,
                    marker=dict(color=colors[i % len(colors)], size=8)
                ))
            
            fig.update_layout(
                title="Neural Network Classification + Decision Boundary",
                xaxis_title="Feature 1",
                yaxis_title="Feature 2",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Accuracy
            accuracy = accuracy_score(y_test, y_pred)
            st.success(f"🎯 Test Accuracy: **{accuracy:.2%}**")
            
            # Confusion Matrix
            cm = confusion_matrix(y_test, y_pred)
            fig_cm = px.imshow(cm, text_auto=True, aspect="auto",
                             x=target_names[:len(np.unique(y))], 
                             y=target_names[:len(np.unique(y))],
                             title="Confusion Matrix")
            st.plotly_chart(fig_cm, use_container_width=True)

# ============================================================================
# 🎮 BEREICH 5: Interaktiver Playground
# ============================================================================

else:  # Interaktiver Playground
    st.header("🎮 Neural Network Playground")
    st.markdown("**Experimentiere mit verschiedenen Architekturen!**")
    
    # Zwei-Spalten Layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🏗️ Netzwerk-Architektur")
        
        # Layer Konfiguration
        n_layers = st.slider("Anzahl Hidden Layers", 1, 5, 2)
        
        layers = []
        for i in range(n_layers):
            neurons = st.slider(f"Layer {i+1} Neuronen", 1, 100, 10*(i+1))
            layers.append(neurons)
        
        # Aktivierungsfunktion
        activation = st.selectbox("Aktivierungsfunktion", ['relu', 'tanh', 'logistic'])
        
        # Trainings-Parameter
        st.subheader("🎯 Training")
        learning_rate = st.select_slider("Learning Rate", [0.001, 0.01, 0.1, 1.0])
        max_iter = st.slider("Max Iterations", 100, 2000, 500)
        
        # Problem Type
        problem_type = st.radio("Problem Type", ["Regression", "Classification"])
        
        st.info(f"🧠 **Architektur**: {layers}\n📊 **Aktivierung**: {activation}")
    
    with col2:
        st.subheader("🎯 Live Training")
        
        if st.button("🚀 Starte Training!"):
            if problem_type == "Regression":
                # Regression Problem
                X, y = make_regression(n_samples=300, n_features=1, noise=15, random_state=42)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                
                scaler_X = StandardScaler()
                scaler_y = StandardScaler()
                X_train_scaled = scaler_X.fit_transform(X_train)
                X_test_scaled = scaler_X.transform(X_test)
                y_train_scaled = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()
                
                # Model
                model = MLPRegressor(
                    hidden_layer_sizes=tuple(layers),
                    activation=activation,
                    learning_rate_init=learning_rate,
                    max_iter=max_iter,
                    random_state=42
                )
                
                # Training mit Progress
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                model.fit(X_train_scaled, y_train_scaled)
                progress_bar.progress(100)
                status_text.text("Training completed!")
                
                # Vorhersagen
                y_pred_scaled = model.predict(X_test_scaled)
                y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()
                
                # Plot
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=X_test.ravel(), y=y_test, mode='markers', name='True'))
                fig.add_trace(go.Scatter(x=X_test.ravel(), y=y_pred, mode='markers', name='Predicted'))
                fig.update_layout(title="Regression Results", height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                mse = mean_squared_error(y_test, y_pred)
                st.metric("MSE", f"{mse:.2f}")
                
            else:
                # Classification Problem
                X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, 
                                         n_informative=2, n_clusters_per_class=1, random_state=42)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                
                # Model
                model = MLPClassifier(
                    hidden_layer_sizes=tuple(layers),
                    activation=activation,
                    learning_rate_init=learning_rate,
                    max_iter=max_iter,
                    random_state=42
                )
                
                # Training
                progress_bar = st.progress(0)
                model.fit(X_train_scaled, y_train)
                progress_bar.progress(100)
                
                y_pred = model.predict(X_test_scaled)
                
                # Plot
                fig = go.Figure()
                colors = ['red', 'blue']
                for i in [0, 1]:
                    mask = y_test == i
                    fig.add_trace(go.Scatter(
                        x=X_test[mask, 0], y=X_test[mask, 1],
                        mode='markers', name=f'Class {i} (True)',
                        marker=dict(color=colors[i])
                    ))
                    
                    mask_pred = y_pred == i
                    fig.add_trace(go.Scatter(
                        x=X_test[mask_pred, 0], y=X_test[mask_pred, 1],
                        mode='markers', name=f'Class {i} (Pred)',
                        marker=dict(color=colors[i], symbol='x', size=10)
                    ))
                
                fig.update_layout(title="Classification Results", height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                accuracy = accuracy_score(y_test, y_pred)
                st.metric("Accuracy", f"{accuracy:.2%}")

# ============================================================================
# Footer
# ============================================================================

st.markdown("---")
st.markdown("**🎓 AMALEA 2025 - Neural Networks modernisiert mit Streamlit**")
st.markdown("Alle ursprünglichen AMALEA-Konzepte interaktiv erlebbar!")
