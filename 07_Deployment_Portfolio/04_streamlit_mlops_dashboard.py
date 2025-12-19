import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests
from datetime import datetime
from typing import Any, Dict

st.set_page_config(
    page_title="MLOps Monitoring Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🚀 MLOps Monitoring Dashboard")
st.markdown("**Real-time Monitoring für Iris Classification API** — wähle Demo oder Live-API.")

# Sidebar für Konfiguration
st.sidebar.header("⚙️ Konfiguration")
demo_mode = st.sidebar.toggle("Demo-Modus (ohne API)", value=True)
api_url = st.sidebar.text_input("API URL", "http://localhost:8000")
refresh_interval = st.sidebar.slider("Refresh Interval (s)", 5, 60, 10)

if st.sidebar.button("🔄 Refresh"):
    st.rerun()

# API Health Check
def mock_health() -> Dict[str, Any]:
    return {
        "status": "ok (demo)",
        "model_version": "0.1.0-demo",
        "model_loaded": True,
        "target_classes": ["setosa", "versicolor", "virginica"],
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


def mock_predict(payload: Dict[str, float]) -> Dict[str, Any]:
    conf = 0.9
    return {
        "prediction_label": "setosa",
        "confidence": conf,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


def safe_get(url: str):
    return requests.get(url, timeout=5)


def safe_post(url: str, json_payload: Dict[str, Any]):
    return requests.post(url, json=json_payload, timeout=10)


health_data = None
if demo_mode:
    health_data = mock_health()
    st.info("Demo-Modus aktiv: simulierte API-Daten.")
else:
    try:
        resp = safe_get(f"{api_url}/health")
        if resp.status_code == 200:
            health_data = resp.json()
            st.success(f"✅ API Status: {health_data.get('status','ok')}")
        else:
            st.error(f"❌ API nicht erreichbar (Status: {resp.status_code})")
    except Exception as e:
        st.error(f"❌ Verbindung zur API fehlgeschlagen: {e}")

if health_data:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Model Version", health_data.get('model_version', 'N/A'))
    with col2:
        st.metric("Model Loaded", "✅" if health_data.get('model_loaded') else "❌")
    with col3:
        st.metric("Target Classes", len(health_data.get('target_classes', [])))

st.divider()

# Prediction Interface
st.header("🧪 Model Testing")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Features")
    sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.1, 0.1)
    sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5, 0.1)
    petal_length = st.slider("Petal Length", 1.0, 7.0, 1.4, 0.1)
    petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2, 0.1)
    
    if st.button("🔮 Predict", type="primary"):
        prediction_data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }
        try:
            if demo_mode:
                result = mock_predict(prediction_data)
            else:
                response = safe_post(f"{api_url}/predict", prediction_data)
                if response.status_code != 200:
                    st.error(f"Prediction fehlgeschlagen: {response.text}")
                    result = None
                else:
                    result = response.json()
            if result:
                st.success(f"Prediction: **{result['prediction_label']}**")
                st.info(f"Confidence: {result['confidence']:.4f}")
                st.caption(f"Timestamp: {result['timestamp']}")
        except Exception as e:
            st.error(f"Fehler bei Prediction: {e}")

with col2:
    st.subheader("Iris Species")
    st.info("""
    **Iris Dataset Features:**
    - **Sepal Length**: Länge des Kelchblatts (cm)
    - **Sepal Width**: Breite des Kelchblatts (cm)  
    - **Petal Length**: Länge des Kronblatts (cm)
    - **Petal Width**: Breite des Kronblatts (cm)
    
    **Klassen:**
    - **Setosa**: Kleinste Blüten
    - **Versicolor**: Mittlere Größe
    - **Virginica**: Größte Blüten
    """)

st.divider()

# Performance Metriken
st.header("📈 Performance Metriken")

# Simulierte Daten (demo) oder Platzhalter bei Live
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
predictions_per_day = np.random.poisson(100, 30)
avg_response_time = np.random.normal(0.05, 0.01, 30)
avg_confidence = np.random.normal(0.92, 0.05, 30)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Predictions (30d)",
        f"{predictions_per_day.sum():,}",
        delta=f"+{predictions_per_day[-1] - predictions_per_day[-2]}"
    )

with col2:
    st.metric(
        "Avg Response Time",
        f"{avg_response_time[-1]:.3f}s",
        delta=f"{avg_response_time[-1] - avg_response_time[-2]:+.3f}s"
    )

with col3:
    st.metric(
        "Avg Confidence",
        f"{avg_confidence[-1]:.3f}",
        delta=f"{avg_confidence[-1] - avg_confidence[-2]:+.3f}"
    )

with col4:
    error_rate = np.random.uniform(0.001, 0.005)
    st.metric(
        "Error Rate",
        f"{error_rate:.3%}",
        delta="-0.001%"
    )

# Charts
col1, col2 = st.columns(2)

with col1:
    # Predictions over time
    fig_predictions = px.line(
        x=dates, y=predictions_per_day,
        title="📊 Predictions pro Tag",
        labels={'x': 'Datum', 'y': 'Anzahl Predictions'}
    )
    st.plotly_chart(fig_predictions, use_container_width=True)

with col2:
    # Response time over time
    fig_response = px.line(
        x=dates, y=avg_response_time,
        title="⚡ Response Time Trend",
        labels={'x': 'Datum', 'y': 'Response Time (s)'}
    )
    st.plotly_chart(fig_response, use_container_width=True)

# Class Distribution
st.subheader("🎯 Prediction Class Distribution")
class_counts = {
    'setosa': np.random.poisson(200),
    'versicolor': np.random.poisson(180),
    'virginica': np.random.poisson(220)
}

fig_pie = px.pie(
    values=list(class_counts.values()),
    names=list(class_counts.keys()),
    title="Class Distribution (Last 30 Days)"
)
st.plotly_chart(fig_pie, use_container_width=True)

# MLOps Best Practices Info
st.header("📚 MLOps Best Practices")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🔄 CI/CD Pipeline")
    st.info("""
    **Continuous Integration:**
    - Automated Testing
    - Model Validation
    - Code Quality Checks
    
    **Continuous Deployment:**
    - Automated Deployment
    - Rollback Strategies
    - Blue-Green Deployment
    """)

with col2:
    st.subheader("📊 Model Monitoring")
    st.info("""
    **Performance Monitoring:**
    - Accuracy Tracking
    - Latency Monitoring
    - Error Rate Analysis
    
    **Data Drift Detection:**
    - Feature Distribution
    - Target Drift
    - Concept Drift
    """)

with col3:
    st.subheader("🐳 Infrastructure")
    st.info("""
    **Containerization:**
    - Docker Images
    - Kubernetes Orchestration
    - Scalability
    
    **Cloud Deployment:**
    - AWS/Azure/GCP
    - Load Balancing
    - Auto-scaling
    """)

# Footer
st.divider()
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.caption("Built with ❤️ using Streamlit for IU Data Analytics Course")
