import pandas as pd
import os, sys
import numpy as np
from scipy.stats import chisquare

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
df = load(input().strip())

print("Null Hypothesis (H0): First-Time Visits are equally distributed across days of the month.")
print("Alternative Hypothesis (H1): First-Time Visits are not equally distributed across days of the month.\n")

print("Observed Frequencies (First-Time Visits per Day):")

df['Dom'] = pd.to_datetime(df['Date']).dt.day

total_first_time = df.groupby('Dom')['First.Time.Visits'].sum().reset_index()

obs = total_first_time['First.Time.Visits'].values

print(obs)

print()
print("Expected Frequencies (assuming equal distribution):")
mean_val = total_first_time['First.Time.Visits'].mean()

expected = np.full(total_first_time.shape[0], mean_val)
print(expected)

chi, p = chisquare(obs, expected)

print(f"Chi-Square Statistic: {round(chi, 2)}")
print(f"p-value: {p}")

print("Conclusion: ",end='')

if p < 0.05:
    print("Reject H0. First-Time Visits are not equally distributed across days of the month.")
else:
    print("error")
