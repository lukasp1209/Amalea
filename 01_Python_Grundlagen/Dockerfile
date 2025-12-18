# Basis-Image: Python 3.11 auf schlankem Linux
FROM python:3.11-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# System-Tools für Healthcheck installieren & Cache bereinigen (hält Image klein)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY . .

# Port für Streamlit freigeben
EXPOSE 8501

# Healthcheck: Prüft alle 30s, ob die App noch reagiert
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Befehl zum Starten der App
CMD ["streamlit", "run", "uebungs_app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
