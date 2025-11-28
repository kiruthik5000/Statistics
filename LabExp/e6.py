import os
import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

file_name = input().strip()
file_path = os.path.join(sys.path[0], file_name)
df = pd.read_csv(file_path)

missing_data = df.isnull().sum()
print("Missing Data:")
print(missing_data)
print()

df_dropna = df.dropna()
print("Dataset after dropping missing values:")
print(df_dropna)
print()

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

mean_imputer = SimpleImputer(strategy='mean')
df_mean_filled = df.copy()
df_mean_filled[numeric_cols] = mean_imputer.fit_transform(df_mean_filled[numeric_cols])

median_imputer = SimpleImputer(strategy='median')
df_median_filled = df.copy()
df_median_filled[numeric_cols] = median_imputer.fit_transform(df_median_filled[numeric_cols])

scaler = StandardScaler()
standardized_values = scaler.fit_transform(df_mean_filled[['LoanAmount']])
df_standardized = pd.DataFrame(standardized_values, columns=['LoanAmount_Standardized'])

print("Standardized LoanAmount:")
print(df_standardized)
print()

minmax_scaler = MinMaxScaler()
normalized_values = minmax_scaler.fit_transform(df_mean_filled[['LoanAmount']])
df_normalized = pd.DataFrame(normalized_values, columns=['LoanAmount_Normalized'])

print("Normalized LoanAmount:")
print(df_normalized)

