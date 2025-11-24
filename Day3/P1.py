import pandas as pd
import numpy as np
import os, sys
from scipy.stats import norm

def load(file):
    print(f"File loaded successfully: {file}")
    return pd.read_csv(os.path.join(sys.path[0], file))

df = load(input().strip())
print(f"Data shape: {df.shape}")
h_mean = float(input())
p_sd = float(input())

sample = df['Delivery_Time_Hours']
n = len(sample)
sample_mean = sample.mean()


z_val = (sample_mean - h_mean) / (p_sd / (n ** 0.5))

p_val = 2 * (1 - norm.cdf(abs(z_val)))

print(f"\nZ-statistic: {z_val:.4f}")
print(f"P-value: {p_val:.4f}")

if p_val < 0.05:
    print("Reject the null hypothesis. There is enough evidence to suggest the delivery time differs from the hypothesized mean.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to suggest the delivery time differs from the hypothesized mean.")