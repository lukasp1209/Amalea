from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


@dataclass
class IrisService:
    pipeline: Pipeline
    target_names: List[str]
    version: str = "0.1.0"

    @classmethod
    def create(cls) -> "IrisService":
        iris = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=42
        )
        pipe = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("clf", LogisticRegression(max_iter=200)),
            ]
        )
        pipe.fit(X_train, y_train)
        return cls(pipeline=pipe, target_names=list(iris.target_names))

    def predict(self, features: List[float]) -> dict:
        arr = np.array(features, dtype=float).reshape(1, -1)
        probs = self.pipeline.predict_proba(arr)[0]
        idx = int(np.argmax(probs))
        # Use timezone-aware UTC datetime
        from datetime import timezone
        now_utc = datetime.now(timezone.utc)
        return {
            "prediction_label": self.target_names[idx],
            "confidence": float(probs[idx]),
            "timestamp": now_utc.isoformat(),
            "target_classes": self.target_names,
            "model_version": self.version,
        }


class PredictRequest(BaseModel):
    sepal_length: float = Field(..., ge=0)
    sepal_width: float = Field(..., ge=0)
    petal_length: float = Field(..., ge=0)
    petal_width: float = Field(..., ge=0)


class PredictResponse(BaseModel):
    prediction_label: str
    confidence: float
    timestamp: str
    target_classes: List[str]
    model_version: str


class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)


class SentimentResponse(BaseModel):
    label: str
    confidence: float


class QARequest(BaseModel):
    context: str = Field(..., min_length=1, max_length=2000)
    question: str = Field(..., min_length=1, max_length=200)


class QAResponse(BaseModel):
    answer: str
    confidence: float


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=400)
    max_length: int = Field(50, ge=10, le=200)
    temperature: float = Field(0.7, ge=0.1, le=1.2)


class GenerateResponse(BaseModel):
    generated_texts: List[str]
    model_info: str


def simple_sentiment(text: str) -> SentimentResponse:
    lowered = text.lower()
    positive = sum(lowered.count(tok) for tok in ["good", "great", "love", "happy", "excellent", "nice"])
    negative = sum(lowered.count(tok) for tok in ["bad", "hate", "sad", "angry", "terrible", "poor"])
    score = positive - negative
    if score > 0:
        label, confidence = "POSITIVE", min(0.5 + 0.1 * score, 0.99)
    elif score < 0:
        label, confidence = "NEGATIVE", min(0.5 + 0.1 * abs(score), 0.99)
    else:
        label, confidence = "NEUTRAL", 0.55
    return SentimentResponse(label=label, confidence=confidence)


def simple_qa(context: str, question: str) -> QAResponse:
    sentences = [s.strip() for s in context.replace("\n", " ").split(".") if s.strip()]
    answer = sentences[0] if sentences else "No answer found."
    return QAResponse(answer=answer, confidence=0.35)


def simple_generate(prompt: str, max_length: int, temperature: float) -> GenerateResponse:
    # Deterministic stub for demo purposes
    continuation = " ..." + " generated text"[: max_length // 4]
    text = (prompt + continuation)[: max_length]
    return GenerateResponse(
        generated_texts=[text],
        model_info=f"stub-generator (temp={temperature})",
    )


app = FastAPI(title="AMALEA Demo API", version="0.1.0")
iris_service = IrisService.create()
NLP_STUB_NOTE = "Sentiment/QA/Generate sind keyword-basierte Stubs (Demo)"


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_version": iris_service.version,
        "model_loaded": True,
        "target_classes": iris_service.target_names,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "nlp_endpoints_stub": True,
        "stub_note": NLP_STUB_NOTE,
    }


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    return iris_service.predict(
        [req.sepal_length, req.sepal_width, req.petal_length, req.petal_width]
    )


@app.post("/sentiment", response_model=SentimentResponse)
def sentiment(req: SentimentRequest):
    return simple_sentiment(req.text)


@app.post("/qa", response_model=QAResponse)
def qa(req: QARequest):
    return simple_qa(req.context, req.question)


@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    return simple_generate(req.prompt, req.max_length, req.temperature)


@app.get("/")
def root():
    return {
        "message": "AMALEA demo API running",
        "endpoints": ["/health", "/predict", "/sentiment", "/qa", "/generate"],
        "nlp_endpoints_stub": True,
        "stub_note": NLP_STUB_NOTE,
    }
