
""""
2 testcase does not passes
"""


import os, sys
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, f1_score, precision_score

df = pd.read_csv(os.path.join(sys.path[0], input().strip()))

print(f"Shape of dataset: {df.shape}")

x = df.drop(columns=['not.fully.paid'], axis=1)
y = df['not.fully.paid']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train.reset_index(inplace=True)
x_test.reset_index(inplace=True)
print(f"Size of training dataset: {x_train.shape}")
print(f"Size of test dataset: {x_test.shape}")


model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

if cm.shape == (2, 2):
    tn, fp, fn, tp = cm.ravel()
    print(f"TN: {tn}, FP: {fp}, FN: {fn}, TP: {tp}")

print("\nEvaluation Metrics:")
acc = accuracy_score(y_test, y_pred)
rec = recall_score(y_test, y_pred, zero_division=0)
pre = precision_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print(f"Accuracy : {acc}")
print(f"Recall   : {rec}")
print(f"Precision: {pre}")
print(f"F1-score : {f1}")
