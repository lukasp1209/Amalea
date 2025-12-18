# Übersicht über Streamlit-Komponenten (neue Datei erstellen)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("🧰 Streamlit Komponenten-Guide")

# 1. TEXT-ELEMENTE
st.header("1️⃣ Text-Elemente")
st.subheader("Untertitel")
st.write("Universeller Ausgabe-Befehl")
st.markdown("**Markdown** funktioniert auch!")
st.text("Einfacher Text ohne Formatierung")
st.caption("Kleine Beschriftung")

# 2. EINGABE-WIDGETS
st.header("2️⃣ Eingabe-Widgets")

col1, col2 = st.columns(2)

with col1:
    st.write("**Zahlen-Eingaben:**")
    zahl = st.slider("Schieberegler:", 0, 100, 50)
    nummer = st.number_input("Zahl eingeben:", 0, 1000, 42)
    
with col2:
    st.write("**Text-Eingaben:**")
    text = st.text_input("Textfeld:", "Hallo Welt")
    auswahl = st.selectbox("Dropdown:", ["Option A", "Option B", "Option C"])

# Radio-Buttons und Checkboxes
radio = st.radio("Radio-Buttons:", ["Ja", "Nein", "Vielleicht"])
checkbox = st.checkbox("Checkbox aktiviert?")

# 3. DATEN-ANZEIGE
st.header("3️⃣ Daten anzeigen")

# Beispieldaten erstellen
beispiel_daten = pd.DataFrame({
    'Spalte 1': np.random.randn(20),
    'Spalte 2': np.random.randn(20),
    'Kategorie': np.random.choice(['A', 'B'], 20)
})

# Verschiedene Anzeige-Methoden
st.write("**DataFrame:**")
st.dataframe(beispiel_daten)

st.write("**Statische Tabelle:**")
st.table(beispiel_daten.head())

st.write("**JSON:**")
st.json({'name': 'Anna', 'alter': 25, 'stadt': 'Berlin'})

# 4. DIAGRAMME
st.header("4️⃣ Diagramme")

col1, col2 = st.columns(2)

with col1:
    st.write("**Einfache Diagramme:**")
    st.line_chart(beispiel_daten[['Spalte 1', 'Spalte 2']])
    
with col2:
    st.write("**Plotly-Diagramm:**")
    fig = px.scatter(beispiel_daten, x='Spalte 1', y='Spalte 2', 
                    color='Kategorie')
    st.plotly_chart(fig, use_container_width=True)

# 5. LAYOUT
st.header("5️⃣ Layout-Optionen")

# Sidebar-Beispiele
st.sidebar.header("Sidebar-Bereich")
sidebar_option = st.sidebar.radio("Sidebar-Radio:", ["A", "B", "C"])

# Columns
st.write("**Spalten-Layout:**")
col1, col2, col3 = st.columns(3)
col1.metric("Wert 1", "1234")
col2.metric("Wert 2", "5678")
col3.metric("Wert 3", "91011")

# Tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Inhalt von Tab 1")
with tab2:
    st.write("Inhalt von Tab 2")
with tab3:
    st.write("Inhalt von Tab 3")

# 6. STATUS-MELDUNGEN
st.header("6️⃣ Status-Meldungen")
st.success("✅ Erfolgsmeldung")
st.info("ℹ️ Informations-Box")
st.warning("⚠️ Warnung")
st.error("❌ Fehlermeldung")

# 7. INTERAKTIVE ELEMENTE
st.header("7️⃣ Interaktive Elemente")

if st.button("Klick mich!"):
    st.balloons()  # Konfetti-Animation
    st.write("Button wurde geklickt! 🎉")

# File Uploader
uploaded_file = st.file_uploader("Datei hochladen:", type=['csv', 'txt'])
if uploaded_file:
    st.success("Datei erfolgreich hochgeladen!")
