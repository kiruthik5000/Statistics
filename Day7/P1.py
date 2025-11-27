import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

filename = input().strip()


df = pd.read_csv(os.path.join(sys.path[0], filename))

print("First 5 Rows:")
print(df.head())
print()

print("Dataset Info:")
print(df.info())
print()

print("Missing Values:")
print(df.isnull().sum())
print()

df = df.apply(pd.to_numeric, errors='coerce')
df = df.fillna(df.mean())

for col in df.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR
    df[col] = np.where(df[col] < lower_fence, lower_fence,
                       np.where(df[col] > upper_fence, upper_fence, df[col]))

print("Outlier treatment (IQR Winsorization) done.")
print()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

print("First 5 Rows After Scaling:")
print(scaled_df.head())
print()

corr_matrix = df.corr().abs() >= 0.7

print("Correlation matrix (absolute values >= 0.7):")
print(corr_matrix)
print()
if "PremiumPrice" in df.columns:
    print("Features sorted by absolute correlation with 'PremiumPrice':")
    corr_with_premium = pd.DataFrame(df.corr()["PremiumPrice"].abs().sort_values())
    print(corr_with_premium)
else:
    print("'PremiumPrice' column not found. Skipping correlation ranking.")
