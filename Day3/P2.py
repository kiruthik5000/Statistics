import pandas as pd
import os, sys
from scipy.stats import norm
import numpy as np

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))

df = load(input().strip())

sigma = 1.41

north = df[df['Zone'] == 'North']['Delivery_Time_Hours']
south = df[df['Zone'] == 'South']['Delivery_Time_Hours']

n_sample = min(50, len(north), len(south))

north_sample = north.sample(n=n_sample, random_state=42)
south_sample = south.sample(n=n_sample, random_state=42)

mean1 = north_sample.mean()
mean2 = south_sample.mean()
# z_val = 0;
z_val = (mean1 - mean2) / np.sqrt(2 * (sigma ** 2) / n_sample)

p_val = 2 * (1 - norm.cdf(abs(z_val)))

print(f"Sample Size per Group: {n_sample}")
print(f"Mean Delivery Time (North): {mean1:.2f}")
print(f"Mean Delivery Time (South): {mean2:.2f}")
print(f"Z-Statistic: {z_val:.4f}")
print(f"P-value: {p_val:.4f}")

alpha = 0.05
if p_val < alpha:
    print("Reject the null hypothesis: There IS a significant difference in delivery times.")
else:
    print("Fail to reject the null hypothesis: No significant difference in delivery times.")
    