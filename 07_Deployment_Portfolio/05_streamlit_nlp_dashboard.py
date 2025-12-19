import streamlit as st
import os
import requests
from datetime import datetime
from typing import Any, Dict

st.set_page_config(
    page_title="Modern NLP Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Modern NLP Dashboard")
st.markdown("**Transformer-basierte NLP Services**")


def mock_generate(prompt: str, max_length: int) -> Dict[str, Any]:
    return {
        "generated_texts": [(prompt + " ... (demo completion)")[:max_length]]
    }


def mock_sentiment(text: str) -> Dict[str, Any]:
    label = "POSITIVE" if "good" in text.lower() else "NEUTRAL"
    return {"sentiment": {"label": label, "confidence": 0.8}}


def mock_qa(context: str, question: str) -> Dict[str, Any]:
    return {"answer": {"answer": context.split(" ")[0] if context else "N/A", "confidence": 0.3}}


def normalize_sentiment(payload: Dict[str, Any]) -> Dict[str, Any]:
    # Accept both nested (demo) and flat (FastAPI) schemas
    if isinstance(payload.get("sentiment"), dict):
        return payload["sentiment"]
    if {"label", "confidence"}.issubset(payload.keys()):
        return {"label": payload["label"], "confidence": payload["confidence"]}
    raise ValueError("Unexpected sentiment payload shape")


def normalize_answer(payload: Dict[str, Any]) -> Dict[str, Any]:
    # Accept both nested (demo) and flat (FastAPI) schemas
    if isinstance(payload.get("answer"), dict):
        return payload["answer"]
    if {"answer", "confidence"}.issubset(payload.keys()):
        return {"answer": payload["answer"], "confidence": payload["confidence"]}
    raise ValueError("Unexpected QA payload shape")


def safe_post(url: str, payload: Dict[str, Any]):
    return requests.post(url, json=payload, timeout=15)

# Sidebar
st.sidebar.header("⚙️ Konfiguration")
demo_mode = st.sidebar.toggle("Demo-Modus (ohne API)", value=True)
default_api = os.getenv("API_URL", "http://localhost:8000")
api_url = st.sidebar.text_input("NLP API URL", default_api)

# Main Content
tab1, tab2, tab3 = st.tabs(["✍️ Text Generation", "😊 Sentiment", "❓ Q&A"])

with tab1:
    st.header("✍️ Text Generation")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        prompt = st.text_area("Prompt eingeben:", "Once upon a time")
        
    with col2:
        max_length = st.slider("Max Length", 50, 200, 100)
        temperature = st.slider("Temperature", 0.1, 1.0, 0.7)
        
    st.caption("Begrenzt auf 400 Zeichen; Demo-Modus liefert Stub-Text.")
    if st.button("🚀 Generate Text", type="primary"):
        with st.spinner("Generiere Text..."):
            try:
                if demo_mode:
                    result = mock_generate(prompt, max_length)
                else:
                    response = safe_post(
                        f"{api_url}/generate",
                        {
                            "prompt": prompt,
                            "max_length": max_length,
                            "temperature": temperature,
                        },
                    )
                    if response.status_code != 200:
                        st.error(f"API Fehler: {response.status_code}")
                        result = None
                    else:
                        result = response.json()

                if result:
                    st.success("Text erfolgreich generiert!")
                    st.write("**Generated Text:**")
                    st.write(result["generated_texts"][0])
            except Exception as e:
                st.error(f"Verbindungsfehler: {e}")

with tab2:
    st.header("😊 Sentiment Analysis")
    
    text_input = st.text_area("Text für Sentiment Analysis:")
    
    if st.button("🔍 Analyze Sentiment", type="primary"):
        if text_input:
            with st.spinner("Analysiere Sentiment..."):
                try:
                    if demo_mode:
                        result = mock_sentiment(text_input)
                    else:
                        response = safe_post(
                            f"{api_url}/sentiment",
                            {"text": text_input},
                        )
                        if response.status_code != 200:
                            st.error(f"API Fehler: {response.status_code}")
                            result = None
                        else:
                            result = response.json()

                    if result:
                        sentiment = normalize_sentiment(result)
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Sentiment", sentiment["label"])
                        with col2:
                            st.metric("Confidence", f"{sentiment['confidence']:.2%}")
                        emoji = "😊" if sentiment["label"] == "POSITIVE" else "😔"
                        st.write(f"## {emoji} {sentiment['label']}")
                except Exception as e:
                    st.error(f"Verbindungsfehler: {e}")
        else:
            st.warning("Bitte Text eingeben")

with tab3:
    st.header("❓ Question Answering")
    
    context = st.text_area("Kontext:", height=150)
    question = st.text_input("Frage:")
    
    st.caption("Demo-Modus liefert einfache Heuristik; Kontext max. 2000 Zeichen.")
    if st.button("💡 Answer Question", type="primary"):
        if context and question:
            with st.spinner("Beantworte Frage..."):
                try:
                    if demo_mode:
                        result = mock_qa(context, question)
                    else:
                        response = safe_post(
                            f"{api_url}/qa",
                            {
                                "context": context,
                                "question": question,
                            },
                        )
                        if response.status_code != 200:
                            st.error(f"API Fehler: {response.status_code}")
                            result = None
                        else:
                            result = response.json()
                    if result:
                        answer = normalize_answer(result)
                        st.success("Antwort gefunden!")
                        st.write(f"**Antwort:** {answer['answer']}")
                        st.write(f"**Confidence:** {answer['confidence']:.2%}")
                except Exception as e:
                    st.error(f"Verbindungsfehler: {e}")
        else:
            st.warning("Bitte Kontext und Frage eingeben")

# Footer
st.divider()
st.caption(f"Modern NLP Dashboard - {datetime.now().strftime('%H:%M:%S')}")
