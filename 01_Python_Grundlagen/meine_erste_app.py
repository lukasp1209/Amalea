# Beispiel: So könnte deine erste Streamlit-App aussehen (als Python-Datei speichern, z.B. meine_erste_app.py)

import streamlit as st
import pandas as pd

# Titel der App
st.title("🎉 Meine erste Streamlit App")
st.write("Hallo Welt! Das ist meine erste Web-App.")

# Eingabefeld für den Namen
name = st.text_input("Wie heißt du?")

if name:
    st.write(f"Hallo {name}! Schön dich kennenzulernen! 👋")

# Einfache Daten
daten = {
    'Obst': ['Apfel', 'Banane', 'Orange'],
    'Anzahl': [10, 5, 8]
}
df = pd.DataFrame(daten)

st.subheader("Meine Daten:")
st.dataframe(df)  # Zeigt Tabelle an

# Einfaches Diagramm
st.bar_chart(df.set_index('Obst'))
