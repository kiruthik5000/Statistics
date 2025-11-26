import os
import sys
import pandas as pd
import numpy as np

file_name=input()
df =pd.read_csv(os.path.join(sys.path[0],file_name))
print("Enter the dataset filename (with .csv or .xlsx extension): File loaded successfully:",file_name)
print("Data shape:",df.shape)
print("\nPreview of Loaded Data:")
print(df.head())

print("\n1.1: Simple Random Sample of 50 deliveries:")

simple_sample=df.sample(n=50, random_state=42).reset_index(drop=True)
print(simple_sample.head())
print("\n1.2: Stratified Sample by Zone (proportional to dataset):")

largest_zone=df['Zone'].value_counts().idxmax()
df_largest=df[df['Zone']== largest_zone]

if len(df_largest) >= 5:
 strat_sample=df_largest.sample(n=5, random_state=42).reset_index(drop=True)
else: 
   strat_sample=df_largest.reset_index(drop=True)

print(strat_sample)

print("\n1.3: Systematic Sample (every 10th order):")
step=10

systematic_sample=df.iloc[::step].reset_index(drop=True)
print(systematic_sample.head())