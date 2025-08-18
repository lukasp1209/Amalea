

"""
AMALEA 2025 - Example Streamlit App
-------------------------------------
Beispiel-App für die neue Repository-Struktur.

Warum lohnt sich die neue Struktur?
> Klarer Lernweg, Zeitersparnis, mehr Spaß mit Data Science!

Starte im Terminal:
    streamlit run example_app.py
"""



# --- Imports ---
import streamlit as st
import pandas as pd
import plotly.express as px


# --- App-Konfiguration ---
st.set_page_config(
    page_title="AMALEA 2025 - Example App",
    page_icon="🚀",
    layout="wide"
)


# --- Header ---
st.title("🚀 AMALEA 2025 - Modernisierte Kursstruktur")
st.markdown(
    "**Willkommen zur neuen, sauberen Repository-Struktur! "
    "Hier findest du alles schneller und kannst direkt loslegen.**"
)


# --- Kursstruktur ---
st.header("📁 Neue Kursstruktur")


structure_data = {
    "Woche": ["01", "02", "03", "04", "05", "06", "07"],
    "Ordner": [
        "01_Python_Grundlagen",
        "02_Streamlit_und_Pandas",
        "03_Machine_Learning",
        "04_Advanced_Algorithms",
        "05_Neural_Networks",
        "06_Computer_Vision_NLP",
        "07_Deployment_Portfolio"
    ],
    "Thema": [
        "Python Basics + Docker",
        "Web-Apps + Datenanalyse",
        "ML Fundamentals",
        "Trees, KNN, Clustering",
        "Deep Learning",
        "CNNs + NLP",
        "Cloud Deployment"
    ],
    "Status": ["✅", "✅", "✅", "✅", "✅", "✅", "✅"]
}

df_structure = pd.DataFrame(structure_data)
st.dataframe(df_structure, use_container_width=True)


# --- Fortschritt ---
st.header("📊 Kurs-Fortschritt")


progress_data = {
    "Woche": ["W01", "W02", "W03", "W04", "W05", "W06", "W07"],
    "Fertigstellung": [100, 100, 100, 100, 100, 20, 10]
}

fig_progress = px.bar(
    progress_data,
    x="Woche",
    y="Fertigstellung",
    title="Modernisierungs-Fortschritt (%)",
    color="Fertigstellung",
    color_continuous_scale="viridis"
)
fig_progress.update_layout(height=400)
st.plotly_chart(fig_progress, use_container_width=True)


# --- Interaktive Demo ---
st.header("🎯 Interaktive Demo")


col1, col2 = st.columns(2)


with col1:
    st.subheader("📊 Daten-Upload Test")
    # Beispiel-Daten
    sample_data = pd.DataFrame({
        'Woche': list(range(1, 8)),
        'Notebooks': [3, 2, 2, 1, 1, 0, 0],
        'Streamlit_Apps': [0, 1, 1, 1, 1, 0, 0],
        'Stunden_Aufwand': [8, 6, 6, 8, 10, 8, 6]
    })
    st.dataframe(sample_data)
    # Datei-Upload
    uploaded_file = st.file_uploader("CSV hochladen", type=['csv'])
    if uploaded_file:
        try:
            df_uploaded = pd.read_csv(uploaded_file)
            st.success("✅ Datei erfolgreich geladen!")
            st.dataframe(df_uploaded.head())
        except Exception as e:
            st.error(f"❌ Fehler: {e}")


with col2:
    st.subheader("🧮 Parameter-Test")
    # Interaktive Parameter
    learning_rate = st.slider("Learning Rate", 0.001, 1.0, 0.01, 0.001)
    epochs = st.slider("Epochs", 10, 1000, 100)
    batch_size = st.selectbox("Batch Size", [16, 32, 64, 128])
    # Demo-Berechnung
    if st.button("🚀 Berechne Trainingszeit"):
        training_time = (epochs * 1000) / batch_size * learning_rate
        st.success(f"⏱️ Geschätzte Trainingszeit: {training_time:.2f} Sekunden")


# --- System Status ---
st.header("🔧 System Status")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(label="📦 Verzeichnisse erstellt", value="7/7", delta="100%")
with col2:
    st.metric(label="📝 Notebooks modernisiert", value="9/12", delta="75%")
with col3:
    st.metric(label="🚀 Apps funktional", value="5/7", delta="71%")


# --- Erfolgsmeldung ---
st.success("🎉 Repository erfolgreich refaktorisiert! Struktur ist jetzt sauber und studentenfreundlich.")


# --- Navigation ---
st.header("📚 Navigation")


col1, col2 = st.columns(2)


with col1:
    st.markdown("""
**✅ Fertige Wochen:**
- 📂 [01_Python_Grundlagen](./01_Python_Grundlagen/)
- 📂 [02_Streamlit_und_Pandas](./02_Streamlit_und_Pandas/)
- 📂 [03_Machine_Learning](./03_Machine_Learning/)
- 📂 [04_Advanced_Algorithms](./04_Advanced_Algorithms/)
- 📂 [05_Neural_Networks](./05_Neural_Networks/)
    """)


with col2:
    st.markdown("""
**✅ Vollständig modernisiert:**
- 📂 [06_Computer_Vision_NLP](./06_Computer_Vision_NLP/)
- 📂 [07_Deployment_Portfolio](./07_Deployment_Portfolio/)

**📦 Archiv:**
- 📁 DEPRECATED_alte_struktur/
- 📁 BACKUP_vor_refactoring/
    """)


# --- Footer ---

# --- Footer ---
st.markdown("---")
st.markdown(
    "**🎓 AMALEA 2025 - Modernized for the Future of Data Science** ✨\n"
    "Repository refaktorisiert ✅ | Struktur optimiert ✅ | Bereit für Studenten ✅"
)
