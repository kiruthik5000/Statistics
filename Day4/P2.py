import pandas as pd
import os, sys
import numpy as np
from scipy.stats import chi2_contingency

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
df = load(input().strip())

print("Null Hypothesis (H0): First-Time Visits are equally distributed across days of the month.")
print("Alternative Hypothesis (H1): First-Time Visits are not equally distributed across days of the month.\n")

print("Contingency Table (Page Loads vs Day of the Week):\n")

bins = [0, 2500, 3500, float('inf')]
labels = ['Low', 'Medium', 'High']

df['Page_Loads_Bin'] = pd.cut(df['Page.Loads'], bins=bins, labels=labels)

contigency = pd.crosstab(df['Day'], df['Page_Loads_Bin'])


chi2, p, dof, expected = chi2_contingency(contigency)
