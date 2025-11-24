import pandas as pd
import os, sys
from sklearn.preprocessing import StandardScaler

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
def iqr(df, column):
    
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    
    IQR = Q3 - Q1
    
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR
    
    df[column] = df[column].clip(lower=lower_fence, upper=upper_fence)
    df[column] = df[column].astype('float')
        
    return df

def preprocess(df):
    
    contains = ['Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Revenue']
    
    print("First 5 rows of selected data:")
    
    print(df[contains].reset_index(drop=True).head())

    print("Missing values before treatment:")
    print(df[contains].isnull().sum())
    
    for c in contains:
        df[c] = df[c].fillna(df[c].mean())
    print("Missing values after treatment:")
    print(df[contains].isnull().sum())
    
    for c in contains:
        df = iqr(df, c)
    print("Outlier treatment done. DataFrame with capped outliers:")
    print(df[contains].head())
    scaler = StandardScaler()
    df[contains] = scaler.fit_transform(df[contains])
    
    print("First 5 rows after scaling:")
    print(df[contains].head())
    
    print("Correlation of features with Revenue (sorted):")
    
    corr = df[contains].corr()[['Revenue']].sort_values(by='Revenue')
    
    print(corr)
    
    return df
df = load(input().strip())

df = preprocess(df)
