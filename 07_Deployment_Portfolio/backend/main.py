from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from functools import lru_cache
from typing import List

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from transformers import pipeline


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


SENTIMENT_MODEL_ID = "distilbert-base-uncased-finetuned-sst-2-english"
QA_MODEL_ID = "distilbert-base-cased-distilled-squad"
GEN_MODEL_ID = "sshleifer/tiny-gpt2"


@lru_cache(maxsize=1)
def get_sentiment_pipeline():
    return pipeline("sentiment-analysis", model=SENTIMENT_MODEL_ID)


@lru_cache(maxsize=1)
def get_qa_pipeline():
    return pipeline("question-answering", model=QA_MODEL_ID)


@lru_cache(maxsize=1)
def get_generate_pipeline():
    # Tiny GPT-2 keeps CPU footprint small
    return pipeline("text-generation", model=GEN_MODEL_ID)


app = FastAPI(title="AMALEA Demo API", version="0.1.0")
iris_service = IrisService.create()
# Preload NLP models to avoid cold-start penalties on first request
sentiment_pipe = get_sentiment_pipeline()
qa_pipe = get_qa_pipeline()
generate_pipe = get_generate_pipeline()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_version": iris_service.version,
        "model_loaded": True,
        "target_classes": iris_service.target_names,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "nlp_models": {
            "sentiment": SENTIMENT_MODEL_ID,
            "qa": QA_MODEL_ID,
            "generate": GEN_MODEL_ID,
        },
    }


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    return iris_service.predict(
        [req.sepal_length, req.sepal_width, req.petal_length, req.petal_width]
    )


@app.post("/sentiment", response_model=SentimentResponse)
def sentiment(req: SentimentRequest):
    result = sentiment_pipe(req.text, truncation=True)[0]
    label = result["label"]
    # HF pipelines sometimes use LABEL_0/1; map to POSITIVE/NEGATIVE if needed
    if label == "LABEL_1":
        label = "POSITIVE"
    elif label == "LABEL_0":
        label = "NEGATIVE"
    return SentimentResponse(label=label, confidence=float(result["score"]))


@app.post("/qa", response_model=QAResponse)
def qa(req: QARequest):
    result = qa_pipe(question=req.question, context=req.context)
    return QAResponse(answer=result.get("answer", ""), confidence=float(result.get("score", 0.0)))


@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    outputs = generate_pipe(
        req.prompt,
        max_new_tokens=req.max_length,
        do_sample=True,
        temperature=req.temperature,
        num_return_sequences=1,
        return_full_text=True,
    )
    texts = [out["generated_text"] for out in outputs]
    return GenerateResponse(generated_texts=texts, model_info=GEN_MODEL_ID)


@app.get("/")
def root():
    return {
        "message": "AMALEA demo API running",
        "endpoints": ["/health", "/predict", "/sentiment", "/qa", "/generate"],
        "nlp_models": {
            "sentiment": SENTIMENT_MODEL_ID,
            "qa": QA_MODEL_ID,
            "generate": GEN_MODEL_ID,
        },
    }
