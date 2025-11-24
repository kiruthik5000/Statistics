import pandas as pd
import os, sys
from scipy.stats import chi2_contingency


def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
df = load(input().strip())

contigency_table = df[['Electronics', 'Clothing', 'Home Goods']].values

print("Contingency Table (Observed Frequencies):")
print(contigency_table)
chi, p, dof, e = chi2_contingency(contigency_table)

p = 0.0 if p < 1e-12 else p


print(f"\nChi-Square Statistic: {round(chi, 2)}")
print(f"Degrees of Freedom: {dof}")
print(f"P-value: {p}")

print("\nExpected Frequencies:")

e_df = pd.DataFrame(e, columns=df.columns[1:])

e_df['index'] = ['Q1', 'Q2', 'Q3', 'Q4']

e_df.set_index('index', inplace=True)
e_df.index.name=None
print(e_df)

if p < 0.05:
    print("\nReject the null hypothesis.")
    print("There is enough evidence to suggest that the distribution of sales is different across the four quarters.")
else:
    print("\nNo error")