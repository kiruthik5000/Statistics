import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, ttest_ind, norm
import os
import sys


input_file = input().strip()
filename = os.path.join(sys.path[0], input_file)
df = pd.read_csv(filename)

sales = df["Sales"]
tv = df["TV"]

# Read inputs
mu0_sales = float(input().strip())   # for one-sample Z-test
mu0_tv = float(input().strip())      # for one-sample t-test

alpha = 0.05

# --------
mean_sales = np.mean(sales)
std_sales = np.std(sales, ddof=1)
n_sales = len(sales)

z_stat_1 = (mean_sales - mu0_sales) / (std_sales / np.sqrt(n_sales))
p_value_1 = 2 * (1 - norm.cdf(abs(z_stat_1)))
conclusion_1 = "Reject H0" if p_value_1 < alpha else "Fail to Reject H0"

print("One-Sample Z-Test (Sales):", end=" ")
print(f"Z-Statistic: {z_stat_1} p-Value: {p_value_1} Conclusion: {conclusion_1}", end="  ")


sales_A = sales[:100]
sales_B = sales[100:200]

mean_A = np.mean(sales_A)
mean_B = np.mean(sales_B)
std_A = np.std(sales_A, ddof=1)
std_B = np.std(sales_B, ddof=1)

z_stat_2 = (mean_A - mean_B) / np.sqrt((std_A**2 / len(sales_A)) + (std_B**2 / len(sales_B)))
p_value_2 = 2 * (1 - norm.cdf(abs(z_stat_2)))
conclusion_2 = "Reject H0" if p_value_2 < alpha else "Fail to Reject H0"

print("Two-Sample Z-Test (Sales Groups):", end=" ")
print(f"Z-Statistic: {z_stat_2} p-Value: {p_value_2} Conclusion: {conclusion_2}", end="  ")


t_stat_3, p_value_3 = ttest_1samp(tv, mu0_tv)
conclusion_3 = "Reject H0" if p_value_3 < alpha else "Fail to Reject H0"

print("One-Sample T-Test (TV):", end=" ")
print(f"T-Statistic: {t_stat_3} p-Value: {p_value_3} Conclusion: {conclusion_3}", end="  ")

tv_A = tv[:100]
tv_B = tv[100:200]

t_stat_4, p_value_4 = ttest_ind(tv_A, tv_B)
conclusion_4 = "Reject H0" if p_value_4 < alpha else "Fail to Reject H0"

print("Two-Sample T-Test (TV Groups):", end=" ")
print(f"T-Statistic: {t_stat_4} p-Value: {p_value_4} Conclusion: {conclusion_4}", end=" ")
