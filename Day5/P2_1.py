import pandas as pd
import os, sys
import numpy as np
from sklearn.preprocessing import LabelEncoder

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
df = load(input("Enter the CSV file name (e.g., income_data.csv): Initial missing values per column:\n").strip())
df = df.reset_index(drop=True)

print(df.isna().sum())

replace_map = {' ?': np.nan}

df = df.replace(replace_map)
print("\nMissing values per column after replacing ' ?' with NaN:")
print(df.isna().sum())

for c in df.columns:
    mode = df[c].mode()[0]
    df[c] = df[c].fillna(mode)
print("\nMissing values per column after filling with mode:")
print(df.isna().sum())

category_cols = ['WorkClass', 'Education', 'Occupation', 'Relationship', 'Gender', 'Native_Country', 'Income_Bracket']

for c in category_cols:
    if c in df.columns:
        df[c] = df[c].astype('category')
        
        

print("\nData types after conversion to categorical:")
for c in df.columns:
    print(f"{c:<15}{str(df[c].dtype):>10}")
print("dtype: object\n")

encoder = LabelEncoder()

for c in category_cols:
    if c != 'Income_Bracket':
        df[c+"_encode"] = encoder.fit_transform(df[c])

print("First 5 rows of the processed dataframe:")


print(df.head())

    
