import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os, sys

# --------------------------
# Read CSV file
# --------------------------
filename = input().strip()
df = pd.read_csv(os.path.join(sys.path[0], filename))

# --------------------------
# 1. Encoding Text Columns
# --------------------------
print("Salary classes:", df['salary'].unique())
print("Department classes:", df['Department'].unique())

le_salary = LabelEncoder()
le_dept = LabelEncoder()

df['salary_enc'] = le_salary.fit_transform(df['salary'])
df['Department_enc'] = le_dept.fit_transform(df['Department'])

# --------------------------
# Show updated dataset info
# --------------------------
print(df.info())

# --------------------------
# 2. Missing Value Treatment
# --------------------------
print("\nMissing values per column:")
print(df.isna().sum())

# --------------------------
# 3. Feature Scaling
# --------------------------
scaler = StandardScaler()

# All independent features except target 'left'
features = ['satisfaction_level', 'last_evaluation', 'number_project',
            'average_monthly_hours', 'time_spend_company',
            'Work_accident', 'promotion_last_5years',
            'salary_enc', 'Department_enc']

df_scaled = df.copy()
df_scaled[features] = scaler.fit_transform(df[features])

# --------------------------
# 4. Multicollinearity Check
# --------------------------
corr = df_scaled[features].corr()

# Detect highly correlated features (≥ 0.7)
high_corr = corr.abs() >= 0.7

print("\nHighly correlated features (cutoff >= 0.7):")
print(high_corr)
