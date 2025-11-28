import pandas as pd
import os
import sys

filename = input().strip()

filepath = os.path.join(sys.path[0], filename)
df = pd.read_csv(filepath)

print("Loan Data Analysis Started.\n")

print("First 5 Rows")
print(df.head(), "\n")

print("Column Names")
print(list(df.columns), "\n")

print("Dataset Shape")
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}\n")

print("Column Data Types and Non-Null Counts")
for col in df.columns:
    non_null = df[col].count()
    dtype = df[col].dtype
    print(f"{col:20} Non-Null: {non_null:<5} Type: {dtype}")
print()

print("Summary Statistics")
print(df.describe(), "\n")

key_columns = ['purpose', 'credit.policy', 'not.fully.paid']

for col in key_columns:
    if col in df.columns:
        print(f"Value Counts for '{col}'")
        print(df[col].value_counts(), "\n")
