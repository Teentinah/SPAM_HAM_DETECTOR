import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib


DATA_PATH = os.path.join("data", "spam_dataset.csv")
MODELS_DIR = "models"
MODEL_PATH = os.path.join(MODELS_DIR, "spam_model.pkl")
VECTORIZER_PATH = os.path.join(MODELS_DIR, "vectorizer.pkl")


def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Fichier de données introuvable: {DATA_PATH}. "
            "Assure-toi que le CSV existe dans le dossier 'data/'."
        )
    df = pd.read_csv(DATA_PATH)
    # On suppose les colonnes 'text' et 'label'
    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError("Le CSV doit contenir les colonnes 'text' et 'label'.")
    return df["text"].astype(str), df["label"].astype(int)


def train():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer(stop_words=None)),
            ("clf", MultinomialNB()),
        ]
    )

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Précision du modèle: {acc * 100:.2f}%")
    print("\nRapport de classification:\n")
    print(classification_report(y_test, y_pred))

    os.makedirs(MODELS_DIR, exist_ok=True)

    # Sauvegarder séparément modèle et vectorizer pour l'API
    vectorizer = pipeline.named_steps["tfidf"]
    model = pipeline.named_steps["clf"]

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    print(f"\nModèle sauvegardé dans: {MODEL_PATH}")
    print(f"Vectorizer sauvegardé dans: {VECTORIZER_PATH}")


if __name__ == "__main__":
    train()

