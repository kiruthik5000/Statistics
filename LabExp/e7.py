import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import sys
file_name = input().strip()
file_path = os.path.join(sys.path[0], file_name)

df = pd.read_csv(file_path)

x = df[['x']]  
y = df['y']

model = LinearRegression()
model.fit(x, y)

intercept = model.intercept_
estimated_value = model.predict(np.array([[10]]))[0]
print(f"Intercept: {intercept:.4f}")
print(f"Estimated value at x=10: {estimated_value:.4f}")

