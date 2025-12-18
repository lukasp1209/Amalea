
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import plotly.express as px
from typing import Tuple, Any

st.set_page_config(page_title="Housing Price Predictor", page_icon="🏠")

st.title("🏠💰 Immobilienpreis-Vorhersage")
st.write("Schätze Hauspreise basierend auf verschiedenen Merkmalen")

# === SIMULIERTE HOUSING-DATEN ERSTELLEN ===
@st.cache_data
def create_housing_data() -> pd.DataFrame:
    """Erstellt realistische Beispiel-Immobiliendaten"""
    np.random.seed(42)
    n_samples = 500
    
    # Features erstellen
    rooms = np.random.normal(6, 1.5, n_samples)
    rooms = np.clip(rooms, 3, 10)  # Zwischen 3 und 10 Zimmer
    
    age = np.random.uniform(1, 100, n_samples)
    distance_to_city = np.random.uniform(1, 12, n_samples)
    crime_rate = np.random.exponential(3, n_samples)
    crime_rate = np.clip(crime_rate, 0, 15)  # Max 15
    
    # Target erstellen (mit realistischen Zusammenhängen)
    price = (
        rooms * 50000 +                    # Mehr Zimmer = teurer
        (100 - age) * 1000 +              # Neuer = teurer
        (12 - distance_to_city) * 5000 +  # Näher zur Stadt = teurer
        (-crime_rate * 2000) +            # Mehr Kriminalität = billiger
        np.random.normal(0, 20000, n_samples) +  # Zufälliges Rauschen
        200000                            # Basis-Preis
    )
    
    # Negative Preise vermeiden
    price = np.maximum(price, 50000)
    
    df = pd.DataFrame({
        'rooms': rooms,
        'age': age,
        'distance_to_city': distance_to_city,
        'crime_rate': crime_rate,
        'price': price
    })
    
    return df

# === DATEN LADEN ===
housing_data = create_housing_data()

# Features und Target trennen
feature_columns = ['rooms', 'age', 'distance_to_city', 'crime_rate']
X = housing_data[feature_columns]
y = housing_data['price']

# === SIDEBAR FÜR MODELL-AUSWAHL ===
st.sidebar.header("🔧 Modell-Konfiguration")
model_type = st.sidebar.selectbox(
    "Wähle Algorithmus:", 
    ["Linear Regression", "Random Forest"]
)
test_size = st.sidebar.slider("Test-Datenanteil", 0.1, 0.5, 0.2)

# === MODELL TRAINIEREN ===
@st.cache_data
def train_regression_model(model_type: str, test_size: float) -> Tuple[Any, float, float, float, float, pd.DataFrame, pd.Series]:
    """Trainiert Regressions-Modell"""
    X_train_cached, X_test_cached, y_train_cached, y_test_cached = train_test_split(
        X, y, test_size=test_size, random_state=42)
    
    if model_type == "Linear Regression":
        model = LinearRegression()
    else:
        model = RandomForestRegressor(random_state=42, n_estimators=100)
    
    model.fit(X_train_cached, y_train_cached)
    
    # Vorhersagen
    train_pred = model.predict(X_train_cached)
    test_pred = model.predict(X_test_cached)
    
    # Metriken berechnen
    train_r2 = r2_score(y_train_cached, train_pred)
    test_r2 = r2_score(y_test_cached, test_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train_cached, train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test_cached, test_pred))
    
    return model, train_r2, test_r2, train_rmse, test_rmse, X_test_cached, y_test_cached

model, train_r2, test_r2, train_rmse, test_rmse, X_test, y_test = train_regression_model(model_type, test_size)

# === APP-LAYOUT ===
tab1, tab2, tab3 = st.tabs(["🏠 Preis-Vorhersage", "📈 Modell-Analyse", "📊 Daten-Übersicht"])

# === TAB 1: PREIS-VORHERSAGE ===
with tab1:
    st.header("🏠 Immobilienpreis schätzen")
    
    col1, col2 = st.columns(2)
    
    with col1:
        rooms = st.slider("Anzahl Zimmer", 3.0, 10.0, 6.0, 0.1)
        age = st.slider("Alter des Hauses (Jahre)", 1, 100, 30)
    
    with col2:
        distance = st.slider("Entfernung zur Stadt (km)", 1.0, 12.0, 5.0, 0.1)
        crime_rate = st.slider("Kriminalitätsrate", 0.0, 15.0, 3.0, 0.1)
    
    # Vorhersage
    user_input = np.array([[rooms, age, distance, crime_rate]])
    predicted_price = model.predict(user_input)[0]
    
    st.subheader("💰 Geschätzter Preis:")
    st.success(f"**${predicted_price:,.0f}**")
    
    # Preis-Kategorisierung
    if predicted_price < 300000:
        st.info("🏠 Günstiges Segment")
    elif predicted_price < 600000:
        st.warning("🏘️ Mittleres Segment")
    else:
        st.error("🏰 Luxus-Segment")
    
    # Vergleich mit ähnlichen Häusern
    st.subheader("📊 Vergleich mit ähnlichen Häusern")
    similar_houses = housing_data[
        (abs(housing_data['rooms'] - rooms) < 1) &
        (abs(housing_data['age'] - age) < 10)
    ]
    
    if len(similar_houses) > 0:
        avg_similar_price = similar_houses['price'].mean()
        difference = predicted_price - avg_similar_price
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Durchschnitt ähnlicher Häuser", f"${avg_similar_price:,.0f}")
        with col2:
            st.metric("Unterschied", f"${difference:,.0f}")

# === TAB 2: MODELL-ANALYSE ===
with tab2:
    st.header("📈 Modell-Performance")
    
    # Performance Metriken
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Train R²", f"{train_r2:.3f}")
    with col2:
        st.metric("Test R²", f"{test_r2:.3f}")
    with col3:
        st.metric("Train RMSE", f"${train_rmse:,.0f}")
    with col4:
        st.metric("Test RMSE", f"${test_rmse:,.0f}")
    
    # R² Erklärung
    st.write("**R² (R-Squared) Interpretation:**")
    if test_r2 > 0.8:
        st.success("🎯 Sehr gutes Modell!")
    elif test_r2 > 0.6:
        st.warning("⚠️ OK-es Modell")
    else:
        st.error("❌ Schwaches Modell")
    
    st.write(f"Das Modell erklärt {test_r2:.1%} der Preisvarianz.")
    
    # Vorhersage vs. Realität Plot
    y_pred = model.predict(X_test)
    pred_df = pd.DataFrame({
        'Echte Preise': y_test, 
        'Vorhergesagte Preise': y_pred
    })
    
    fig_pred = px.scatter(
        pred_df, 
        x='Echte Preise', 
        y='Vorhergesagte Preise',
        title="Vorhersage vs. Realität"
    )
    # Perfekte Linie hinzufügen
    min_price = min(pred_df['Echte Preise'].min(), pred_df['Vorhergesagte Preise'].min())
    max_price = max(pred_df['Echte Preise'].max(), pred_df['Vorhergesagte Preise'].max())
    fig_pred.add_shape(
        type="line", 
        x0=min_price, y0=min_price,
        x1=max_price, y1=max_price,
        line=dict(color="red", dash="dash")
    )
    st.plotly_chart(fig_pred, use_container_width=True)
    
    # Feature Importance (nur für Random Forest)
    if model_type == "Random Forest":
        st.subheader("🎯 Feature Wichtigkeit")
        feature_names = ['Zimmer', 'Alter', 'Entfernung zur Stadt', 'Kriminalitätsrate']
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Wichtigkeit': model.feature_importances_
        }).sort_values('Wichtigkeit', ascending=True)
        
        fig_imp = px.bar(
            importance_df, 
            x='Wichtigkeit', 
            y='Feature',
            orientation='h',
            title="Welche Faktoren beeinflussen den Preis am meisten?"
        )
        st.plotly_chart(fig_imp, use_container_width=True)

# === TAB 3: DATEN-ÜBERSICHT ===
with tab3:
    st.header("📊 Datensatz-Übersicht")
    
    # Basis-Statistiken
    st.subheader("📋 Grundlegende Statistiken")
    st.dataframe(housing_data.describe(), use_container_width=True)
    
    # Rohdaten
    st.subheader("🔍 Rohdaten (Erste 20 Zeilen)")
    st.dataframe(housing_data.head(20))
    
    # Verteilungen der Features
    st.subheader("📈 Feature-Verteilungen")
    feature_to_plot = st.selectbox(
        "Feature für Histogramm:", 
        ['rooms', 'age', 'distance_to_city', 'crime_rate', 'price']
    )
    
    fig_hist = px.histogram(
        housing_data, 
        x=feature_to_plot, 
        title=f"Verteilung von {feature_to_plot}",
        nbins=30
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    
    # Korrelations-Matrix
    st.subheader("🔗 Korrelationen")
    corr_matrix = housing_data.corr()
    fig_corr = px.imshow(
        corr_matrix,
        text_auto=True,
        aspect="auto",
        title="Korrelations-Matrix"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

# === FOOTER ===
st.sidebar.markdown("---")
st.sidebar.write("💡 **Regression-Tipp:** R² näher bei 1 = besseres Modell")
st.sidebar.write("🎯 **Ausprobieren:** Verändere die Eingaben und beobachte die Auswirkungen!")
