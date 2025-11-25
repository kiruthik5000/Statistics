import pandas as pd
import numpy as np
import os, sys
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))

def preprocess(df):
    replace_map = {'?': np.nan}
    
    df = df.replace(replace_map)
    
    for c in df.columns:
        df[c].fillna(df[c].mode()[0])
    
    
    for c in df.columns[2:]:
        if df[c].dtype == object:
            df[c] = df[c].astype('category')
            
    for c in df.columns:
        if str(df[c].dtype) == 'category':
            if c == 'Income_Bracket': 
                continue
            le = LabelEncoder()
            df[c] = df[c].astype(str)
            df[c+'_encode'] = le.fit_transform(df[c])
            
    return df
    
df = load(input().strip())

df = preprocess(df)
train_size = int(df.shape[0] * 0.7)

manual_train = df[:train_size]
manual_test = df[train_size:]

print("Manual Row Split:")
print(f"Train shape: {manual_train.shape}")
print(f"Test shape: {manual_test.shape}")

X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

print("\ntrain_test_split:")
print(f"X_Train shape: {X_train.shape}")
print(f"X_test  shape:{X_test.shape}")
print(f"y_train shape:{Y_train.shape}")
print(f"y_test  shape:{Y_test.shape}")
print("\nFirst 5 rows of X_train:")