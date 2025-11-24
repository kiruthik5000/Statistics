import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(42)
import os, sys

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))

file = input().strip()
df = load(file)
print(f"Enter the dataset filename (with .csv or .xlsx extension): File loaded successfully: {file}")
print(f"Data shape: {df.shape}\n")
print("Preview of Loaded Data:")
print(df.head())

print("\n1.1: Simple Random Sample of 50 deliveries:")

simple_sample = df.sample(n=50, random_state=42).reset_index(drop=True)
print(simple_sample.head())

print("\n1.2: Stratified Sample by Zone (proportional to dataset):")

if 'Zone' not in df.columns:
    print("Error")
else:
    train, test = train_test_split(df,test_size=0.2,stratify=df["Zone"],random_state=42)
    print(train.head())

print("\n1.3: Systematic Sample (every 10th order):")

step = 10
if len(df) < step:
    print("Dataset too small for systematic sampling.")
else:
    systematic_sample = df.iloc[::step].reset_index(drop=True)
    print(systematic_sample.head())
# import os
# import pandas as pd
# import sys
# from sklearn.model_selection import train_test_split

# def load_csv(filename):
#     path = os.path.join(sys.path[0], filename)
#     return pd.read_csv(path)

# inp = input().strip()
# df = load_csv(inp)
# print("File loaded successfully:",inp)
# print("Data shape:",df.shape)
# print("Preview of Loaded Data:")
# print(df.head())

# print("Simple Random Sampling (50 students):")
# if df.shape[0] < 50 :
#     print("Not enough rows to sample 50 rows. Total rows:",df.shape[0])
# else :
#     sample = df.sample(n=50,random_state=42)
#     print(sample.head())
    
# print("Stratified Sampling (by Gender):")
# try:
#     if "Gender" not in df.columns:
#         print("Gender is missing")
#     else :
#         train, test = train_test_split(df,test_size=0.2,stratify=df["Gender"],random_state=42)
#         print(train.head())
# except:
#     print('Stratified sampling failed: The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.')
    
# print("Systematic Sampling (every 10th student):")
# step = 10
# if df.shape[0] < step :
#     print("Dataset is too small")
# else :
#     print(df.iloc[::step])