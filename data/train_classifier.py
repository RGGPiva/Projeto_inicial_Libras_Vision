import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
DATA_FILE = os.path.join(ARTIFACTS_DIR, "data.pickle")
MODEL_FILE = os.path.join(ARTIFACTS_DIR, "model.p")

with open(DATA_FILE, "rb") as f:
    data_dict = pickle.load(f)

data = np.asarray(data_dict["data"])
labels = np.asarray(data_dict["labels"])

x_train, x_test, y_train, y_test = train_test_split(
    data,
    labels,
    test_size=0.2,
    shuffle=True,
    stratify=labels,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features="sqrt",
    bootstrap=True,
    criterion="gini",
    random_state=42
)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy * 100:.2f}%")
print("\nRelatório de classificação:")
print(classification_report(y_test, y_pred))

with open(MODEL_FILE, "wb") as f:
    pickle.dump({"model": model}, f)

print(f"Modelo salvo em: {MODEL_FILE}")