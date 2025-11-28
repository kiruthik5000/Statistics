import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import sys, os


filename = input().strip()
file = os.path.join(sys.path[0], filename)
df = pd.read_csv(file)


X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

coeffs = model.coef_
intercept = model.intercept_
r2 = r2_score(y_test, y_pred)

print("Coefficients:")
print(f"TV: {coeffs[0]}")
print(f"Radio: {coeffs[1]}")
print(f"Newspaper: {coeffs[2]}")
print(f"Intercept: {intercept}")
print(f"R2 Score: {r2}")

