import pandas as pd
import os, sys

filename = input("Enter the CSV file name (e.g., income_data.csv): ").strip()

df = pd.read_csv(os.path.join(sys.path[0], filename))

replace_map = {'?':'Unknown'}
for c in df.columns:
    df[c] = df[c].replace(replace_map)

print("First 5 Rows:")
print(df.head(), "\n")

print("Column Names:")
print(list(df.columns), "\n")

rows, cols = df.shape
print("Dataset Shape:")
print(f"Rows: {rows}, Columns: {cols}\n")
print("Column Data Types and Non-Null Counts:")
for col in df.columns:
    print(f"{col:22} Non-Null: {df[col].count():<6} Type: {df[col].dtype}")
print()

print("Summary Statistics (Numerical Columns):")
print(df.describe(), "\n")

print("Categorical Columns and Value Counts:\n")

categorical_columns = df.select_dtypes(include=["object"]).columns

for col in categorical_columns:
    print(f"Column: {col}")
    print(df[col].value_counts(), "\n")

print("Gender Distribution:")

if "Gender" in df.columns:
    print(df["Gender"].value_counts(), "\n")
else:
    print("Gender column not found in the dataset.\n")
