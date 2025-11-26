
import numpy as np
from scipy.stats import ttest_ind



m_mean = float(input().strip())
m_sd = float(input().strip())
m_n = int(input().strip())
f_mean = float(input().strip())
f_sd = float(input().strip())
f_n = int(input().strip())

np.random.seed(42)

m_data = np.random.normal(m_mean, m_sd, m_n)
f_data = np.random.normal(f_mean, f_sd, f_n)

t_val, p_val = ttest_ind(m_data, f_data, equal_var=True)

print("Two-Sample T-Test Result (Male vs Female Fit Ratings)")
print(f"T-statistic: {t_val:.4f}")
print(f"P-value: {p_val:.4f}")
if p_val < 0.05:
    print("Reject the null hypothesis: Significant difference in fit ratings between male and female respondents.")
else:
    print("Fail to reject the null hypothesis: No significant difference in fit ratings between male and female respondents.")







------------------------------------------ C3 - 2 ------------------------------------------


import numpy as np
from scipy import stats

def main():
    # Read inputs
    try:
        mean_before = float(input())
        std_before = float(input())
        mean_after = float(input())
        std_after = float(input())
        n = int(input())
    except ValueError:
        return

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate synthetic paired data
    # Note: To simulate paired data based on separate means/stds, we generate two independent
    # normal distributions. While real paired data often has correlation, this is the standard 
    # approach for synthetic generation when no correlation coefficient is provided.
    before_ratings = np.random.normal(mean_before, std_before, n)
    after_ratings = before_ratings + np.random.normal((mean_after - mean_before), 1e-1, n)

    # Perform paired t-test (ttest_rel)
    # We compare After vs Before. 
    # ttest_rel(a, b) calculates a - b. We use (after, before) to align with the intervention logic.
    t_stat, p_val = stats.ttest_rel(after_ratings, before_ratings)

    # Output results
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_val:.4f}")

    # Determine conclusion based on significance level 0.05
    if p_val < 0.05:
        print("Reject the null hypothesis. There is a significant difference in fit ratings before and after the intervention.")
    else:
        print("Fail to reject the null hypothesis. There is no significant difference in fit ratings before and after the intervention.")

if __name__ == "__main__":
    main()