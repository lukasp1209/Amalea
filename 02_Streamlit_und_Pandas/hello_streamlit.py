# Erstelle deine erste App-Datei

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# App-Titel und Beschreibung
st.title("🎯 Meine erste ML-Data App")
st.write("Willkommen zur IU Data Analytics & Big Data Fallstudie!")

# Sidebar für Eingaben
st.sidebar.header("🔧 Einstellungen")
name = st.sidebar.text_input("Wie heißt du?", "Student")
anzahl_datenpunkte = st.sidebar.slider("Anzahl Datenpunkte", 10, 1000, 100)

# Hauptbereich
st.write(f"Hallo **{name}**! 👋")

# Erstelle Beispiel-Daten
np.random.seed(42)  # Für reproduzierbare Zufallszahlen
data = pd.DataFrame({
    'x': np.random.randn(anzahl_datenpunkte),
    'y': np.random.randn(anzahl_datenpunkte),
    'kategorie': np.random.choice(['A', 'B', 'C'], anzahl_datenpunkte)
})

# Zeige die Daten
st.subheader("📊 Unsere Beispiel-Daten")
st.write(f"Dataset mit {len(data)} Datenpunkten:")
st.dataframe(data.head(10))  # Zeigt nur erste 10 Zeilen

# Einfache Visualisierung
st.subheader("📈 Interaktive Visualisierung")
fig = px.scatter(data, x='x', y='y', color='kategorie', 
                title="Scatter Plot der Beispiel-Daten")
st.plotly_chart(fig, use_container_width=True)

# Einfache Statistiken
st.subheader("📋 Grundlegende Statistiken")
st.write(data.describe())

# Info-Box
st.info("💡 Tipp: Verändere die Einstellungen in der Sidebar und beobachte, wie sich die App aktualisiert!")

# 📊 Pandas-Demo: Vektorisierung vs. Loops
# Warum wir in Data Science keine For-Schleifen nutzen

print("🐼 Pandas Performance Demo")
print("=" * 60)

# CSV-Daten simulieren (wie im ursprünglichen Kurs erklärt)
print("1️⃣ CSV-Struktur verstehen:")
csv_content = """Name,Alter,Stadt,Gehalt
Anna,25,Berlin,45000
Max,30,Hamburg,52000
Lisa,28,München,48000
Tom,35,Köln,55000
Sarah,22,Frankfurt,38000"""

print(csv_content)

# DataFrame erstellen (zentral in allen AMALEA-Notebooks)
print("\n2️⃣ CSV in pandas DataFrame konvertieren:")
from io import StringIO
df = pd.read_csv(StringIO(csv_content))
print(df)

# Vektorisierte Operationen (SQL-Style)
print("\n3️⃣ Vektorisierung (The Fast Way):")
# Statt durch jede Zeile zu loopen, operieren wir auf der ganzen Spalte
df['Gehalt_Netto_Est'] = df['Gehalt'] * 0.6  # Eine Zeile, C-Speed
print(df[['Name', 'Gehalt', 'Gehalt_Netto_Est']])

# Filtering (WHERE Clause)
high_earners = df[df['Gehalt'] > 50000]
print(f"\n💰 High Earners (>50k):\n{high_earners['Name'].tolist()}")

print(f"📏 Anzahl Zeilen und Spalten: {df.shape}")

# Datentypen prüfen (wichtig für ML!)
print(f"\n🔍 Datentypen (wichtig für Machine Learning):")
print(df.dtypes)

# Features vs. Labels identifizieren (ML-Konzept aus AMALEA)
print(f"\n🎯 Features vs. Labels (ML-Konzepte):")
features = ['Alter', 'Stadt']  # Input-Variablen
target = 'Gehalt'              # Zielvariable
print(f"Features (Input): {features}")
print(f"Target (Output): {target}")

# Einfache Datenanalyse
print(f"\n📊 Einfache Analyse:")
print(f"Durchschnittsalter: {df['Alter'].mean():.1f} Jahre")
print(f"Durchschnittsgehalt: {df['Gehalt'].mean():,.0f} €")
print(f"Städte: {df['Stadt'].unique()}")

print(f"\n✅ Das sind die Pandas-Grundlagen, die du für Streamlit brauchst!")
print(f"🚀 Jetzt erstellen wir daraus eine interaktive Streamlit-App...")
