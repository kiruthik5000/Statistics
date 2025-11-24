import pandas as pd
import os, sys
from scipy.stats import chi2_contingency


def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
df = load(input().strip())

contigency_table = df[['Electronics Sales', 'Clothing Sales', 'Home Goods Sales']].values

print("Contingency Table (Observed Frequencies):")
print(contigency_table)
chi, p, dof, e = chi2_contingency(contigency_table)


print(f"Chi-square Statistic: {round(chi, 2)}")
print(f"p-value: {p}")
print(f"Degrees of Freedom: {dof}")

print("Expected Frequencies:")
print(e)

if p < 0.01:
    print("Reject the null hypothesis.")
    print("There is enough evidence to suggest that product sales depend on months (they are related).")
else:
    print("No error")