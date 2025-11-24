import pandas as pd
from scipy.stats import skew, kurtosis 
import os, sys


def load(file):
    print(f"File loaded successfully: {file}")
    return pd.read_csv(os.path.join(sys.path[0], file))


df = load(input().strip())

print(f"Data shape: {df.shape}")
print("Preview of Loaded Data:")
print(df.head())

print("Simple Random Sampling (50 students):")

sample = df.sample(n=50, random_state=42).reset_index(drop=True)
print(sample.head())
print("Summary Statistics of the Population data")

print(round(df['Height_cm'].describe(), 1))
med = df['Height_cm'].median()
mode = df['Height_cm'].mode()[0]

print(f"median: {med} mode: {mode}")
sk = skew(df['Height_cm'])
kurt = kurtosis(df['Height_cm'])

print(f"skewness: {sk:.3f} kurtosis: {kurt:.3f}")
print("Summary Statistics of the Sample data")
print(round(sample['Height_cm'].describe(), 1))
med = sample['Height_cm'].median()
mode = sample['Height_cm'].mode()[0]

print(f"median: {med} mode: {mode}")
sk = skew(sample['Height_cm'])
kurt = kurtosis(sample['Height_cm'])

print(f"skewness: {sk:.3f} kurtosis: {kurt:.3f}")