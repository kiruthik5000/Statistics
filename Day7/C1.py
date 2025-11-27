import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

cleaned_file = input().strip()
new_file = input().strip()

cleaned_df = pd.read_csv(os.path.join(sys.path[0], cleaned_file))
new_df = pd.read_csv(os.path.join(sys.path[0], new_file))


for col in ['DATE', 'MONTH']:
    if col in new_df.columns:
        new_df = new_df.drop(columns=[col])

scaler = StandardScaler()
scaled_cleaned = pd.DataFrame(
    scaler.fit_transform(cleaned_df),
    columns=cleaned_df.columns
)

new_sample = scaled_cleaned.tail(1)
scaled_cleaned = scaled_cleaned.iloc[:-1]  

corr_matrix = scaled_cleaned.corr()

temp_corr = corr_matrix['temperature']

high_corr_features = temp_corr[abs(temp_corr) >= 0.7].index.tolist()

print(f"Features highly correlated with temperature (|corr| >= 0.7): {high_corr_features}")

if "sunshine" in scaled_cleaned.columns:
    scaled_cleaned = scaled_cleaned.drop(columns=["sunshine"])
    temp_corr = scaled_cleaned.corr()["temperature"]

print("\nSorted correlation with temperature:")
print(temp_corr.sort_values(ascending=False).to_frame())
