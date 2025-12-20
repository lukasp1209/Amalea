# 🏗️ Production-Ready Dockerfile
# 1. Basis-Image: Slim Variante für minimale Angriffsfläche & Größe
FROM python:3.11-slim

# 2. Best Practices: Bytecode verhindern & Output unbuffered (für Logs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Arbeitsverzeichnis setzen
WORKDIR /app

# 4. System-Dependencies installieren & Cache bereinigen (Layer-Optimierung!)
# Wir installieren curl für Healthchecks
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 5. Security: Nicht als Root laufen!
# Wir erstellen einen dedizierten User 'appuser'
RUN useradd -m -u 1000 appuser
USER appuser

# 6. Python-Dependencies installieren
# Erst requirements kopieren (nutzt Docker Layer Caching wenn sich Code ändert aber reqs nicht)
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    python -c "import streamlit; print('Streamlit version:', streamlit.__version__)"

# 7. Code kopieren
COPY --chown=appuser:appuser . .

# 8. Metadaten & Healthcheck
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# 9. Start-Befehl (verwende python -m für bessere Kompatibilität)
CMD ["python", "-m", "streamlit", "run", "uebungs_app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
