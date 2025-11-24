import numpy as np
from scipy.stats import norm
from statsmodels.stats.weightstats import ztest

# create populated data 



b_mean = float(input().strip())
b_sd = float(input().strip())
b_size = int(input().strip())

g_mean = float(input().strip())
g_sd = float(input().strip())
g_size = int(input().strip())

np.random.seed(42)

p_boys = np.random.normal(b_mean, b_sd, b_size);
p_girls = np.random.normal(g_mean, g_sd, g_size);

print("Two-Sample Z-Test Result (Boys > Girls)")

z_val , p_value = ztest(p_boys, p_girls, alternative='larger')
print(f"Z-statistic: {z_val:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject the null hypothesis: Boys are significantly taller than girls.")
else:
    print("Fail to reject the null hypothesis: No significant evidence that boys are taller than girls.")   