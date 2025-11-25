import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import os, sys

filename = input().strip()

try:
    df = pd.read_csv(os.path.join(sys.path[0], filename))

    df = df[['Day', 'Page.Loads']].dropna()

    df['Page.Loads'] = pd.to_numeric(df['Page.Loads'], errors='coerce')
    df = df.dropna()

    bins = pd.qcut(df['Page.Loads'], q=3, labels=['Low', 'Medium', 'High'])
    df['Page_Loads_Bin'] = bins

    contingency_table = pd.crosstab(df['Day'], df['Page_Loads_Bin'])

    chi2, p_value, dof, expected = chi2_contingency(contingency_table)

    print("Null Hypothesis (H0): Page Loads are independent of the Day of the Week.")
    print("Alternative Hypothesis (H1): Page Loads depend on the Day of the Week.\n")

    print("Contingency Table (Page Loads vs Day of the Week):\n")
    print(contingency_table)
    print()

    print(f"Chi-Square Statistic: {chi2:.2f}")
    print(f"p-value: {p_value:.4f}\n")

    if p_value < 0.05:
        print("Conclusion: Reject H0. Page Loads depend on the Day of the Week.")
    else:
        print("Conclusion: Fail to Reject H0. Page Loads are independent of the Day of the Week.")

except FileNotFoundError:
    print("Error: File not found. Please check the filename.")
except Exception as e:
    print("An error occurred:", e)
