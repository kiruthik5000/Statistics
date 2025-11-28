import pandas as pd
import numpy as np
import os, sys

filename = input().strip()

df = pd.read_csv(os.path.join(sys.path[0], filename))

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- First 5 Rows ---")
print(df.head())

df['left_c'] = df['left'].map({0: 'Retained', 1: 'Left'})

categories = ['Retained', 'Left']

avg_satisfaction = df.groupby('left_c')['satisfaction_level'].mean().reindex(categories)

print("\n--- Average Satisfaction Level by Retention ---")
print(avg_satisfaction)

avg_hours = df.groupby('left_c')['average_monthly_hours'].mean().reindex(categories)

print("\n--- Average Monthly Hours by Retention ---")
print(avg_hours)