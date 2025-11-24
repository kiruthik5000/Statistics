import pandas as pd
import os, sys

# Read filename
filename = input("Enter the CSV file name (e.g., income_data.csv): ").strip()

# Load CSV
df = pd.read_csv(os.path.join(sys.path[0], filename))

print("First 5 Rows:")
print(df.head(), "\n")

# Column Names
print("Column Names:")
print(list(df.columns), "\n")

# Shape
rows, cols = df.shape
print("Dataset Shape:")
print(f"Rows: {rows}, Columns: {cols}\n")

# Column data types
print("Column Data Types and Non-Null Counts:")
for col in df.columns:
    print(f"{col:22} Non-Null: {df[col].count():<6} Type: {df[col].dtype}")
print()

# Summary statistics
print("Summary Statistics (Numerical Columns):")
print(df.describe(), "\n")

# Categorical Columns
print("Categorical Columns and Value Counts:\n")

categorical_columns = df.select_dtypes(include=["object"]).columns

for col in categorical_columns:
    print(f"Column: {col}")
    print(df[col].replace({'?': 'Unknown'}).value_counts(), "\n")

# Gender distribution
print("Gender Distribution:")

if "Gender" in df.columns:
    print(df["Gender"].value_counts(), "\n")
else:
    print("Gender column not found in the dataset.\n")
