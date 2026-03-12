import os
import csv
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, ParameterGrid, cross_val_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
DATA_FILE = os.path.join(ARTIFACTS_DIR, "data.pickle")
CSV_FILE = os.path.join(ARTIFACTS_DIR, "hyperparameter_results.csv")

with open(DATA_FILE, "rb") as f:
    data_dict = pickle.load(f)

data = np.asarray(data_dict["data"])
labels = np.asarray(data_dict["labels"])

x_train, _, y_train, _ = train_test_split(
    data,
    labels,
    test_size=0.2,
    shuffle=True,
    stratify=labels,
    random_state=42
)

param_grid = {
    "n_estimators": [100, 250],
    "max_depth": [None, 10, 50],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2],
    "max_features": ["sqrt", "log2"],
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"]
}

results = []

for i, params in enumerate(ParameterGrid(param_grid), start=1):
    model = RandomForestClassifier(
        **params,
        random_state=42,
        n_jobs=-1
    )

    scores = cross_val_score(
        model,
        x_train,
        y_train,
        cv=5,
        scoring="accuracy",
        n_jobs=-1
    )

    result = params.copy()
    result["mean_accuracy"] = scores.mean()
    result["std_accuracy"] = scores.std()
    results.append(result)

    print(f"{i}: {params} -> {scores.mean():.4f}")

results.sort(key=lambda x: (-x["mean_accuracy"], x["std_accuracy"]))

with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"Resultados salvos em: {CSV_FILE}")