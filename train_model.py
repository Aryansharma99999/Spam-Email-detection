"""Train and save a demo spam detection model without pandas."""

from __future__ import annotations

import csv
import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "spam.csv"
MODEL_PATH = BASE_DIR / "model.pkl"
VECTORIZER_PATH = BASE_DIR / "vectorizer.pkl"


def load_dataset() -> tuple[list[str], list[int]]:
    texts: list[str] = []
    labels: list[int] = []

    with open(DATA_PATH, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            texts.append(row["text"])
            labels.append(1 if row["label"].strip().lower() == "spam" else 0)

    return texts, labels


def main() -> None:
    texts, labels = load_dataset()

    x_train, x_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.2,
        random_state=42,
        stratify=labels,
    )

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)
    x_train_vec = vectorizer.fit_transform(x_train)
    x_test_vec = vectorizer.transform(x_test)

    model = LogisticRegression(max_iter=250)
    model.fit(x_train_vec, y_train)

    accuracy = model.score(x_test_vec, y_test)

    with open(MODEL_PATH, "wb") as model_file:
        pickle.dump(model, model_file)

    with open(VECTORIZER_PATH, "wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    print(f"Model trained successfully. Validation accuracy: {accuracy:.2%}")
    print(f"Saved model to: {MODEL_PATH}")
    print(f"Saved vectorizer to: {VECTORIZER_PATH}")


if __name__ == "__main__":
    main()
