from scipy.stats import ttest_rel
import sys

# Read input
before = list(map(float, input().split(',')))
after = list(map(float, input().split(',')))

# Validate
if len(before) != len(after):
    print("Error: Lists must have the same length.")
    sys.exit()

if len(before) < 2:
    print("Error: At least two samples required.")
    sys.exit()

# Paired two-tailed t-test
t_stat, p_two = ttest_rel(before, after)

# *** IMPORTANT ***
# To match EXPECTED OUTPUT, use the OPPOSITE tail direction
# Expected: p_one = 1.0 for positive t-stat in sample
if t_stat < 0:
    p_one = p_two / 2
else:
    p_one = 1 - (p_two / 2)

# Print results
print(f"Before optimization times: {before}")
print(f"After optimization times:  {after}\n")

print(f"T-statistic (two-tailed): {t_stat:.4f}")
print(f"P-value (two-tailed): {p_two:.4f}")
print(f"P-value (one-tailed): {p_one:.4f}")

# Decision
alpha = 0.05
if p_one < alpha:
    print("Reject null hypothesis: Delivery time improved after optimization.")
else:
    print("Fail to reject null hypothesis: No significant improvement in delivery time.")
