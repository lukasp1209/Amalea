
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import plotly.express as px
import seaborn as sns
from typing import Tuple

st.set_page_config(page_title="Iris ML Predictor", page_icon="🌸")

st.title("🌸🤖 Iris ML Vorhersage-App")
st.write("Trainiere ein ML-Modell und mache Vorhersagen!")

# === DATEN LADEN UND VORBEREITEN ===
@st.cache_data
def load_and_prepare_data() -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
    """Lädt Iris-Daten und bereitet sie für ML vor"""
    iris = sns.load_dataset('iris')
    
    # Features (X) und Target (y) trennen
    X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = iris['species']
    
    return X, y, iris

X, y, iris_data = load_and_prepare_data()

# === SIDEBAR FÜR MODELL-EINSTELLUNGEN ===
st.sidebar.header("🔧 Modell-Einstellungen")
test_size = st.sidebar.slider("Test-Datenanteil", 0.1, 0.5, 0.2)
random_state = st.sidebar.number_input("Random State", 0, 100, 42)

# === DATEN AUFTEILEN ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state
)

# === MODELL TRAINIEREN ===
@st.cache_data
def train_model(test_size: float, random_state: int):
    """Trainiert das ML-Modell mit gegebenen Parametern"""
    X_train_cached, X_test_cached, y_train_cached, y_test_cached = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Random Forest Classifier erstellen und trainieren
    model = RandomForestClassifier(random_state=random_state, n_estimators=100)
    model.fit(X_train_cached, y_train_cached)
    
    # Performance berechnen
    train_accuracy = accuracy_score(y_train_cached, model.predict(X_train_cached))
    test_accuracy = accuracy_score(y_test_cached, model.predict(X_test_cached))
    
    return model, train_accuracy, test_accuracy

model, train_acc, test_acc = train_model(test_size, random_state)

# === HAUPTBEREICH IN TABS ===
tab1, tab2, tab3 = st.tabs(["🎯 Vorhersage", "📊 Modell-Performance", "📋 Daten-Explorer"])

# === TAB 1: VORHERSAGE ===
with tab1:
    st.header("🎯 Mache eine Vorhersage")
    st.write("Gib die Merkmale einer Iris-Blume ein und lass das Modell die Art vorhersagen:")
    
    # Eingabe-Widgets für Features
    col1, col2 = st.columns(2)
    
    with col1:
        sepal_length = st.number_input(
            "Kelchblatt Länge (cm)", 
            min_value=4.0, max_value=8.0, value=5.8, step=0.1
        )
        sepal_width = st.number_input(
            "Kelchblatt Breite (cm)", 
            min_value=2.0, max_value=4.5, value=3.0, step=0.1
        )
    
    with col2:
        petal_length = st.number_input(
            "Blütenblatt Länge (cm)", 
            min_value=1.0, max_value=7.0, value=4.3, step=0.1
        )
        petal_width = st.number_input(
            "Blütenblatt Breite (cm)", 
            min_value=0.1, max_value=2.5, value=1.3, step=0.1
        )
    
    # Vorhersage machen
    user_input = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(user_input)[0]
    prediction_proba = model.predict_proba(user_input)[0]
    
    # Ergebnis anzeigen
    st.subheader("🔮 Vorhersage-Ergebnis:")
    st.success(f"Die Iris-Art ist wahrscheinlich: **{prediction}**")
    
    # Wahrscheinlichkeiten visualisieren
    prob_df = pd.DataFrame({
        'Art': model.classes_,
        'Wahrscheinlichkeit': prediction_proba
    })
    
    fig = px.bar(prob_df, x='Art', y='Wahrscheinlichkeit', 
                title="Vorhersage-Wahrscheinlichkeiten",
                color='Wahrscheinlichkeit',
                color_continuous_scale='viridis')
    st.plotly_chart(fig, use_container_width=True)
    
    # Interpretation
    confidence = max(prediction_proba)
    if confidence > 0.8:
        st.success(f"🎯 Sehr sicher! Confidence: {confidence:.1%}")
    elif confidence > 0.6:
        st.warning(f"⚠️ Mäßig sicher. Confidence: {confidence:.1%}")
    else:
        st.error(f"❌ Unsicher. Confidence: {confidence:.1%}")

# === TAB 2: MODELL-PERFORMANCE ===
with tab2:
    st.header("📊 Modell-Performance")
    
    # Key Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Training Genauigkeit", f"{train_acc:.1%}")
    with col2:
        st.metric("Test Genauigkeit", f"{test_acc:.1%}")
    with col3:
        overfitting = train_acc - test_acc
        st.metric("Overfitting", f"{overfitting:.1%}")
    
    # Overfitting-Warnung
    if overfitting > 0.1:
        st.warning("⚠️ Mögliches Overfitting! Modell könnte auf neuen Daten schlechter sein.")
    else:
        st.success("✅ Gute Generalisierung!")
    
    # Feature Importance
    st.subheader("🎯 Feature Wichtigkeit")
    importance_df = pd.DataFrame({
        'Feature': ['Kelchblatt Länge', 'Kelchblatt Breite', 'Blütenblatt Länge', 'Blütenblatt Breite'],
        'Wichtigkeit': model.feature_importances_
    }).sort_values('Wichtigkeit', ascending=True)
    
    fig_importance = px.bar(importance_df, x='Wichtigkeit', y='Feature', 
                           orientation='h', title="Welche Features sind am wichtigsten?",
                           color='Wichtigkeit', color_continuous_scale='blues')
    st.plotly_chart(fig_importance, use_container_width=True)
    
    # Erklärung
    most_important = importance_df.iloc[-1]['Feature']
    st.write(f"💡 **{most_important}** ist das wichtigste Merkmal für die Klassifikation!")
    
    # Confusion Matrix (vereinfacht)
    y_pred = model.predict(X_test)
    st.subheader("🔍 Detaillierte Performance")
    
    # Classification Report als DataFrame
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    st.dataframe(report_df.round(3))

# === TAB 3: DATEN-EXPLORER ===
with tab3:
    st.header("📋 Daten-Explorer")
    
    # Trainings- vs Test-Daten
    st.subheader("📊 Datenaufteilung")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Trainings-Samples", len(X_train))
    with col2:
        st.metric("Test-Samples", len(X_test))
    
    # Originaledaten anzeigen
    st.subheader("🔍 Original-Dataset")
    st.dataframe(iris_data)
    
    # Korrelations-Heatmap
    st.subheader("🔗 Feature-Korrelationen")
    correlation_matrix = X.corr()
    fig_corr = px.imshow(correlation_matrix, text_auto=True, aspect="auto",
                        title="Wie hängen die Features zusammen?",
                        color_continuous_scale='RdBu')
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Scatter Plot Matrix
    st.subheader("📈 Feature-Beziehungen")
    fig_scatter = px.scatter_matrix(iris_data, 
                                   dimensions=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
                                   color='species')
    st.plotly_chart(fig_scatter, use_container_width=True)

# === FOOTER ===
st.sidebar.markdown("---")
st.sidebar.write("💡 **ML-Tipp:** Je mehr gute Daten, desto besser das Modell!")
st.sidebar.write("🎯 **Nächster Schritt:** Probiere verschiedene Modell-Parameter aus!")
