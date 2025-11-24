import pandas as pd
import numpy as np
import os, sys
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
def preprocess(df):
    print("First 5 rows of dataset:")
    print(df.head())
    
    if {'global_radiation', 'temperature'}.issubset(df.columns):
        print('\nAvailable Columns:')
        print(['global_radiation', 'temperature'])
    
    X = df[['global_radiation']]
    Y = df['temperature']
    
    return X, Y, df


df = load(input().strip())

X, Y, df = preprocess(df)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=200)

model = LinearRegression()

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

r2_train = model.score(X_train, Y_train)

r2_test = r2_score(Y_test, Y_pred)

mse = mean_squared_error(Y_test, Y_pred)

mae = mean_absolute_error(Y_test, Y_pred)

rmse = np.sqrt(mse)

slope = model.coef_[0]

intercept = model.intercept_


print("\nModel Trained")
print(f"R² Score (Train): {r2_train:.4f}")
print(f"Intercept        : {intercept:.4f}")
print(f"Slope           : {slope:.4f}")
print("\nEvaluation Metrics:")
print(f"Mean Squared Error (MSE) : {mse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error  : {rmse:.4f}")
print(f"R² Score (Test)          : {r2_test:.4f}")