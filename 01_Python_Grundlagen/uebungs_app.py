"""
Advanced Analytics Dashboard
---------------------------
Eine professionelle Streamlit-App zur Datenanalyse.
Starten mit: streamlit run uebungs_app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfiguration & State Management
st.set_page_config(page_title="Pro Data App", layout="wide")

if 'warenkorb' not in st.session_state:
    st.session_state.warenkorb = []

# 2. Daten laden (Cached & Typed)
@st.cache_data
def lade_daten() -> pd.DataFrame:
    data = {
        'Produkt': ['Laptop X1', 'Phone 15', 'Tablet Pro', 'Headset QC', 'Maus MX', 'Monitor 4K'],
        'Kategorie': ['Electronics', 'Electronics', 'Electronics', 'Audio', 'Peripherals', 'Peripherals'],
        'Preis': [1200, 999, 850, 299, 99, 450],
        'Lagerbestand': [5, 12, 8, 25, 50, 10],
        'Bewertung': [4.8, 4.5, 4.3, 4.7, 4.6, 4.4]
    }
    return pd.DataFrame(data)

df = lade_daten()

# 3. Sidebar: Advanced Filters
st.sidebar.header("🔍 Filter & Einstellungen")
kategorien = st.sidebar.multiselect(
    "Kategorien filtern:", 
    options=df['Kategorie'].unique(),
    default=df['Kategorie'].unique()
)

preis_range = st.sidebar.slider(
    "Preisrahmen (€):", 
    min_value=int(df['Preis'].min()), 
    max_value=int(df['Preis'].max()),
    value=(0, 2000)
)

# Filter-Logik (Vektorisierung)
maske = (df['Kategorie'].isin(kategorien)) & (df['Preis'].between(preis_range[0], preis_range[1]))
df_filtered = df[maske]

# 4. Haupt-Layout mit Tabs
st.title("🚀 Advanced Analytics Dashboard")
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📋 Rohdaten", "🛒 Warenkorb"])

with tab1:
    # KPI Row
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Produkte", len(df_filtered))
    col2.metric("Ø Preis", f"{df_filtered['Preis'].mean():.2f} €")
    col3.metric("Gesamtwert (Lager)", f"{(df_filtered['Preis'] * df_filtered['Lagerbestand']).sum():,.0f} €")
    
    # Bestes Produkt (Pandas Magic)
    best_product = df_filtered.loc[df_filtered['Bewertung'].idxmax()]
    col4.metric("Top Produkt", best_product['Produkt'], f"{best_product['Bewertung']} ⭐")

    # Charts
    c1, c2 = st.columns(2)
    with c1:
        fig_bar = px.bar(df_filtered, x='Produkt', y='Lagerbestand', color='Kategorie', title="Lagerbestand")
        st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        fig_scat = px.scatter(df_filtered, x='Preis', y='Bewertung', size='Lagerbestand', hover_name='Produkt', title="Preis-Leistungs-Matrix")
        st.plotly_chart(fig_scat, use_container_width=True)

with tab2:
    st.dataframe(df_filtered, use_container_width=True)
    
    # Interaktion: Produkt zum Warenkorb hinzufügen
    produkt_wahl = st.selectbox("Produkt zum Merken wählen:", df_filtered['Produkt'])
    if st.button("In den Warenkorb legen"):
        if produkt_wahl not in st.session_state.warenkorb:
            st.session_state.warenkorb.append(produkt_wahl)
            st.success(f"{produkt_wahl} hinzugefügt!")
        else:
            st.warning("Schon drin!")

with tab3:
    st.subheader("Deine Merkliste (Session State Demo)")
    if st.session_state.warenkorb:
        st.write(st.session_state.warenkorb)
        if st.button("Warenkorb leeren"):
            st.session_state.warenkorb = []
            st.rerun()
    else:
        st.info("Der Warenkorb ist leer.")

# Debugging Info für Entwickler
with st.expander("🤓 Developer Info (State)"):
    st.write(st.session_state)
