-------------------------------- 2 --------------------------------------

import os
import sys
import pandas as pd
import numpy as np
import os,sys

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

filename = input().strip()

df = pd.read_csv(os.path.join(sys.path[0], filename))

required_cols = ['global_radiation', 'temperature'] 

df = df[required_cols]
df = df.apply(pd.to_numeric, errors='coerce')
df = df.fillna(df.mean())  

X = df[['global_radiation']].values   # reshape for sklearn
y = df['temperature'].values


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=200
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Linear Regression Model Results")
print(f"Intercept: {model.intercept_:.4f}")
print(f"Slope: {model.coef_[0]:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R2 Score: {r2:.4f}")

-------------------------------- 3 --------------------------------------

import os
import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


filename = input().strip()
df = pd.read_csv(os.path.join(sys.path[0], filename))


required_cols = ['global_radiation','humidity', 'pressure', 'temperature']


df = df[required_cols]
df = df.apply(pd.to_numeric, errors='coerce')
df = df.fillna(df.mean())   # fill missing values with column means

X = df[['global_radiation', 'humidity', 'pressure']].values   # reshape for sklearn
y = df['temperature'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=200
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Multiple Linear Regression (3 features) Results")
print(f"Intercept: {model.intercept_:.4f}")
print(f"Slopes (coefficients):")
print(f"  global_radiation: {model.coef_[0]:.4f}")
print(f"  humidity: {model.coef_[1]:.4f}")
print(f"  pressure: {model.coef_[2]:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R2 Score: {r2:.4f}")

-------------------------------- 4 --------------------------------------

import os
import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


filename = input().strip()
df = pd.read_csv(os.path.join(sys.path[0], filename))


required_cols = ['global_radiation','humidity', 'temperature']


df = df[required_cols]
df = df.apply(pd.to_numeric, errors='coerce')
df = df.fillna(df.mean())   # fill missing values with column means

X = df[['global_radiation', 'humidity']].values   # reshape for sklearn
y = df['temperature'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=200
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Multiple Linear Regression Model Results")
print(f"Intercept: {model.intercept_:.4f}")
print(f"Slopes (coefficients): global_radiation = {model.coef_[0]:.4f}, humidity = {model.coef_[1]:.4f}")
# print(f"  global_radiation: {model.coef_[0]:.4f}")
# print(f"  humidity: {model.coef_[1]:.4f}")
# print(f"  pressure: {model.coef_[2]:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R2 Score: {r2:.4f}")

--------------------------------- 5 --------------------------------------
import os
import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


filename = input().strip()
df = pd.read_csv(os.path.join(sys.path[0], filename))


required_cols = ['global_radiation','humidity', 'pressure', 'cloud_cover','temperature']


df = df[required_cols]
df = df.apply(pd.to_numeric, errors='coerce')
df = df.fillna(df.mean())   # fill missing values with column means

X = df[['global_radiation', 'humidity', 'pressure', 'cloud_cover']].values   # reshape for sklearn
y = df['temperature'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=200
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Multiple Linear Regression (4 features) Results")
print(f"Intercept: {model.intercept_:.4f}")
print(f"Slopes (coefficients):")
print(f"  global_radiation: {model.coef_[0]:.4f}")
print(f"  humidity: {model.coef_[1]:.4f}")
print(f"  pressure: {model.coef_[2]:.4f}")
print(f"  cloud_cover: {model.coef_[3]:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R2 Score: {r2:.4f}")