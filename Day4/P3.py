
import pandas as pd
import numpy as np
import os, sys
from scipy.stats import chi2_contingency
filename = input().strip()

try:
    df = pd.read_csv(os.path.join(sys.path[0], filename))

    df = df[['Date', 'Day.Of.Week', 'Page.Loads']].dropna()

    df['Page.Loads'] = pd.to_numeric(df['Page.Loads'], errors='coerce')
    df = df.dropna()

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna()

    df['Year'] = df['Date'].dt.year

    df['WeekType'] = df['Day.Of.Week'].apply(lambda x: 'Weekend' if x in [1, 7] else 'Weekday')

    contingency = df.pivot_table(
        index='Year',
        columns='WeekType',
        values='Page.Loads',
        aggfunc='sum',
        fill_value=0
    )

    print("Contingency Table:")
    print(contingency, "\n")

    chi2, p, dof, expected = chi2_contingency(contingency)

    print(f"Chi-Square Statistic: {chi2:.2f}")
    print(f"p-value: {p:.4f}\n")

    if p < 0.01:
        print("Reject H0: Distribution of Page Loads differs between weekdays and weekends across years.")
    else:
        print("Fail to Reject H0: No significant difference in Page Load distributions across years.")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)

