"""Flask backend for the AI-Powered Email Spam Detection System."""

from __future__ import annotations

import os
import pickle
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"
VECTORIZER_PATH = BASE_DIR / "vectorizer.pkl"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model = None
vectorizer = None


def load_artifacts() -> None:
    """Load model artifacts on startup."""
    global model, vectorizer

    if not MODEL_PATH.exists() or not VECTORIZER_PATH.exists():
        raise FileNotFoundError(
            "model.pkl or vectorizer.pkl not found. Run train_model.py before starting the API."
        )

    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)

    with open(VECTORIZER_PATH, "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)


@app.get("/")
def root():
    return jsonify(
        {
            "service": "AI-Powered Email Spam Detection System",
            "status": "online",
            "version": "1.0.0",
        }
    )


@app.get("/health")
def health():
    artifacts_ready = bool(model is not None and vectorizer is not None)
    return jsonify({"status": "healthy" if artifacts_ready else "degraded", "artifactsReady": artifacts_ready})


@app.post("/predict")
def predict():
    if model is None or vectorizer is None:
        return (
            jsonify(
                {
                    "error": "Model artifacts are missing.",
                    "details": "Run train_model.py to generate model.pkl and vectorizer.pkl.",
                }
            ),
            500,
        )

    payload = request.get_json(silent=True) or {}
    message = (payload.get("email") or payload.get("message") or "").strip()

    if not message:
        return jsonify({"error": "Email content is required."}), 400

    transformed = vectorizer.transform([message])
    prediction = model.predict(transformed)[0]

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(transformed)[0]
        spam_probability = float(probabilities[1])
        ham_probability = float(probabilities[0])
    else:
        spam_probability = 0.5 if int(prediction) == 1 else 0.49
        ham_probability = 1 - spam_probability

    label = "spam" if int(prediction) == 1 else "ham"
    confidence = spam_probability if label == "spam" else ham_probability

    phishing_terms = [
        term
        for term in ["urgent", "verify", "account", "password", "lottery", "free", "click", "bank"]
        if term in message.lower()
    ]

    return jsonify(
        {
            "prediction": label,
            "confidence": round(confidence, 4),
            "scores": {
                "spam": round(spam_probability, 4),
                "ham": round(ham_probability, 4),
            },
            "insights": {
                "messageLength": len(message),
                "suspiciousTerms": phishing_terms,
                "riskLevel": (
                    "critical"
                    if spam_probability >= 0.85
                    else "high"
                    if spam_probability >= 0.65
                    else "moderate"
                    if spam_probability >= 0.45
                    else "low"
                ),
            },
        }
    )


if __name__ == "__main__":
    load_artifacts()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
else:
    load_artifacts()
