import pandas as pd
from scipy.stats import chisquare, chi2_contingency
import os, sys

file = input().strip()
filepath = os.path.join(sys.path[0], file)


df = pd.read_csv(filepath)

df = df.dropna()

exp_adelie = int(input())
exp_chinstrap = int(input())
exp_gentoo = int(input())

species_order = ["Adelie", "Chinstrap", "Gentoo"]
observed_counts = [
    sum(df["species"] == "Adelie"),
    sum(df["species"] == "Chinstrap"),
    sum(df["species"] == "Gentoo")
]

expected_counts = [exp_adelie, exp_chinstrap, exp_gentoo]

total_obs = sum(observed_counts)
total_exp = sum(expected_counts)

expected_scaled = [(e / total_exp) * total_obs for e in expected_counts]

chi_stat_gof, p_value_gof = chisquare(f_obs=observed_counts, f_exp=expected_scaled)
conclusion_gof = "Reject H0" if p_value_gof < 0.05 else "Fail to Reject H0"

print("Chi-Square Goodness of Fit:")
print(f"Chi-Square Statistic: {chi_stat_gof}")
print(f"p-Value: {p_value_gof}")
print(f"Conclusion: {conclusion_gof}\n")

# ------------------- Test of Independence -------------------
contingency_table = pd.crosstab(df["species"], df["island"])
chi_stat_ind, p_value_ind, _, _ = chi2_contingency(contingency_table)
conclusion_ind = "Reject H0" if p_value_ind < 0.05 else "Fail to Reject H0"

print("Chi-Square Test of Independence:")
print(f"Chi-Square Statistic: {chi_stat_ind}")
print(f"p-Value: {p_value_ind}")
print(f"Conclusion: {conclusion_ind}")


