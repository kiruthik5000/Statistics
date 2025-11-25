import pandas as pd
import numpy as np
import os, sys
np.random.seed(42)
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
def iqr(df, c):
    Q1 = df[c].quantile(0.25)
    Q3 = df[c].quantile(0.75)
    
    IQR = Q3 - Q1
    
    low = Q1 - 1.5 * IQR
    high = Q3 + 1.5 * IQR
    
    df[c] = df[c].clip(lower=low, upper=high)
    
    return df
    
def preprocess(df):
    
    cols = ['Customer_Age', 'Order_Quantity', 'Unit_Price', 'Unit_Cost', 'Revenue']
    
    for c in cols:
        df[c] = df[c].fillna(df[c].mean())
        
    for c in cols:
        df = iqr(df, c)
    
    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    
    X = df[['Unit_Cost']]
    Y = df['Revenue']
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=200)
    
    model = LinearRegression()
    
    model.fit(X_train, Y_train)
    
    Y_pred = model.predict(X_test)
    
    mse = mean_squared_error(Y_test, Y_pred)
    mae = mean_absolute_error(Y_test, Y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(Y_test, Y_pred)
    
    print(f"Mean Squared Error (MSE): {round(mse, 4):.4f}")
    print(f"Mean Absolute Error (MAE): {round(mae, 4):.4f}")
    print(f"Root Mean Squared Error (RMSE): {round(rmse, 4):.4f}")
    print(f"R2 Score: {round(r2, 4)}")
    
     
    return df

df = load(input().strip())

df = preprocess(df)