import os
import pandas as pd
import sys
from sklearn.model_selection import train_test_split

def load_csv(filename):
    path = os.path.join(sys.path[0], filename)
    return pd.read_csv(path)

inp = input().strip()
df = load_csv(inp)
print("File loaded successfully:",inp)
print("Data shape:",df.shape)
print("Preview of Loaded Data:")
print(df.head())

print("Simple Random Sampling (50 students):")
if df.shape[0] < 50 :
    print("Not enough rows to sample 50 rows. Total rows:",df.shape[0])
else :
    sample = df.sample(n=50,random_state=42)
    print(sample.head())
    
print("Stratified Sampling (by Gender):")
try:
    if "Gender" not in df.columns:
        print("Gender is missing")
    else :
        train, test = train_test_split(df,test_size=0.2,stratify=df["Gender"],random_state=42)
        print(train.head())
except:
    print('Stratified sampling failed: The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.')
    
print("Systematic Sampling (every 10th student):")
step = 10
if df.shape[0] < step :
    print("Dataset is too small")
else :
    print(df.iloc[::step])