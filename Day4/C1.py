import pandas as pd
import os, sys
import numpy as np
from scipy.stats import chisquare

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
df = load(input().strip())

obs = df['Electronics Sales']

freq_sum = df['Electronics Sales'].sum()

avg_val = freq_sum / df.shape[0]

exp = np.full(df.shape[0], avg_val)

print(f"Observed Frequency: {obs.values}")
print(f"Expected Frequency: {exp}")


chi, p = chisquare(obs.values, exp)

print(f"\nChi-square Statistic: {round(chi, 2)}")
print(f"p-value: {p:.1f}")
print()

if p < 0.05:
    print("Reject the null hypothesis. There is not enough evidence to suggest that sales of electronics are evenly distributed across months.")
else:
    print("Fail to Reject the null hypothesis. There is not enough evidence to suggest that sales of electronics are evenly distribute across months.")
