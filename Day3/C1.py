import math
from scipy.stats import norm

# --- Get user input ---
try:
    s_mean = float(input())
    p_mean = float(input())
    p_sd = float(input())
    n = int(input())

    test_type = input().strip().lower()
    alpha_input = input().strip()
    alpha = float(alpha_input) if alpha_input else 0.05

    if test_type not in ['greater', 'less', 'two-sided']:
        raise ValueError("Invalid test type. Must be 'greater', 'less', or 'two-sided'.")
except Exception as e:
    print(f"Input error: {e}")
    exit(1)

# --- Calculate z-statistic ---
z_value = (s_mean - p_mean) / (p_sd / math.sqrt(n))

# --- Calculate p-value ---
if test_type == 'greater':
    p_value = 1 - norm.cdf(z_value)
elif test_type == 'less':
    p_value = norm.cdf(z_value)
else:  # two-sided
    p_value = 2 * (1 - norm.cdf(abs(z_value)))

# --- Output ---
print(f"Z-statistic: {round(z_value, 4)}")
print(f"P-value: {round(p_value, 4)}")

if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
