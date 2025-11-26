import pandas as pd
from sklearn.model_selection import train_test_split
import os, sys

df = pd.read_csv(os.path.join(sys.path[0], input().strip()))

print(f"Shape of dataset: {df.shape}")

x_train, x_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df[df.columns[-1]], test_size=0.2, random_state=42)
print(f"Size of training dataset: {x_train.reset_index().shape}")
print(f"Size of test dataset: {x_test.reset_index().shape}")


print("\nShapes:")
print(f"X_train: {x_train.shape} Y_train: {y_train.shape}")
print(f"X_test: {x_test.shape} Y_test: {y_test.shape}")