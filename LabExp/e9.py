
import sys
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

input_file = input().strip()
filename = os.path.join(sys.path[0], input_file)
df = pd.read_csv(filename)



le = LabelEncoder()
df["species"] = le.fit_transform(df["species"])


X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
def evaluate_model(model, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="macro")
    rec = recall_score(y_test, y_pred, average="macro")
    f1 = f1_score(y_test, y_pred, average="macro")
    cm = confusion_matrix(y_test, y_pred)

    report = classification_report(
        y_test,
        y_pred,
        target_names=["setosa", "versicolor", "virginica"],
        digits=3,
        zero_division=0
    )

 
    print(f"{model_name}")
    print(f"Accuracy: {acc:.2f}")
    print(f"Precision (macro): {prec:.2f}")
    print(f"Recall (macro): {rec:.2f}")
    print(f"F1-score (macro): {f1:.2f}")
    print("Confusion Matrix:")
    print(cm)
    print("Classification Report:")
    print(report.strip())


evaluate_model(KNeighborsClassifier(), "KNN")


evaluate_model(LogisticRegression(max_iter=1000, random_state=42), "Logistic Regression")