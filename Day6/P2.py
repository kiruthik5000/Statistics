import pandas as pd
import numpy as np
import os, sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


def iqr(df, c):
    Q1 = df[c].quantile(0.25)
    Q3 = df[c].quantile(0.75)

    IQR = Q3 - Q1

    low = Q1 - 1.5 * IQR
    high = Q3 + 1.5 * IQR

    df[c] = df[c].clip(lower=low, upper=high)

    return df


filename = input().strip()
df = pd.read_csv(os.path.join(sys.path[0], filename))

cols = ['Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Revenue']
df = df[cols]

for c in cols:
    df[c] = df[c].fillna(df[c].mean())

for c in cols:
    df = iqr(df, c)

scaler = StandardScaler()
df[cols] = scaler.fit_transform(df[cols])

X = df[['Unit_Cost']]
y = df['Revenue']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=200
)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")
