# Weitere Streamlit-Beispiele (als Python-Datei speichern, z.B. streamlit_komponenten.py)

import streamlit as st
import pandas as pd
import numpy as np

st.title("🧰 Streamlit Komponenten-Übersicht")

# Text-Elemente
st.header("1. Text-Elemente")
st.subheader("Das ist ein Untertitel")
st.write("Normaler Text mit **fett** und *kursiv*")
st.markdown("### Markdown funktioniert auch!")

# Eingabe-Widgets
st.header("2. Eingabe-Widgets")
zahl = st.slider("Wähle eine Zahl:", 0, 100, 50)
st.write(f"Du hast {zahl} gewählt")

auswahl = st.selectbox("Lieblingsfrucht:", ["Apfel", "Banane", "Orange"])
st.write(f"Du magst {auswahl}")

# Sidebar (seitliche Leiste)
st.sidebar.header("Einstellungen")
farbe = st.sidebar.radio("Wähle Farbe:", ["Rot", "Grün", "Blau"])

# Daten anzeigen
st.header("3. Daten-Anzeige")
beispiel_daten = pd.DataFrame({
    'x': np.random.randn(50),
    'y': np.random.randn(50)
})

st.line_chart(beispiel_daten)

# Spalten-Layout
col1, col2 = st.columns(2)
with col1:
    st.write("Linke Spalte")
with col2:
    st.write("Rechte Spalte")
