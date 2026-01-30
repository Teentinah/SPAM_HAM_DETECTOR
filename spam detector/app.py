import os
import joblib
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS


MODELS_DIR = "models"
MODEL_PATH = os.path.join(MODELS_DIR, "spam_model.pkl")
VECTORIZER_PATH = os.path.join(MODELS_DIR, "vectorizer.pkl")


def load_artifacts():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError(
            "Modèle ou vectorizer introuvable. "
            "Lance d'abord: python train_model.py"
        )
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer


app = Flask(__name__)
CORS(app)

model, vectorizer = load_artifacts()


@app.route("/")
def index():
    """Page d'accueil - Interface web"""
    return send_from_directory("static", "index.html")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    message = data.get("message")
    if not message:
        return jsonify({"error": "Champ 'message' manquant"}), 400

    X = vectorizer.transform([message])
    proba = model.predict_proba(X)[0]
    pred = int(model.predict(X)[0])

    spam_proba = float(proba[1]) * 100.0
    ham_proba = float(proba[0]) * 100.0

    return jsonify(
        {
            "prediction": "spam" if pred == 1 else "ham",
            "label": int(pred),
            "confidence_spam": spam_proba,
            "confidence_ham": ham_proba,
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

