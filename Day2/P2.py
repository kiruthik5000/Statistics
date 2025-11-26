import pandas as pd
import os, sys
from scipy.stats import skew, kurtosis

def load(file):
    return pd.read_csv(os.path.join(sys.path[0], file))
    
f1 = input().strip()
f2 = input().strip()

pop = load(f1)
sam = load(f2)

def fmt(x):
    """Format x to 2 decimals, trimming trailing zero in 2nd decimal place."""
    s = f"{x:.2f}"
    if s[-1] == "0":      # if second decimal = 0
        return s[:-1]     # remove last zero (e.g., 5.40 → 5.4)
    return s

def printer(df, types):
    if(types=='pop'):
        print("Population Stats:\n")
    else:
        print("Sample Stats:\n")

    mean = df['Delivery_Time_Hours'].mean()
    median = df['Delivery_Time_Hours'].median()
    mode = df['Delivery_Time_Hours'].mode()[0]
    var = df['Delivery_Time_Hours'].var()
    std = df['Delivery_Time_Hours'].std()
    skw = skew(df['Delivery_Time_Hours'])
    kurt = kurtosis(df['Delivery_Time_Hours'])

    print("{" +
          f"'Mean': {fmt(mean)}, 'Median': {fmt(median)}, 'Mode': {fmt(mode)}, "
          f"'Variance': {fmt(var)}, 'Std Dev': {fmt(std)}, "
          f"'Skewness': {skw:.3f}, 'Kurtosis': {kurt:.3f}"
          + "}")

printer(pop, 'pop')
printer(sam, 'sam')



--------------------------------------------------------P3 - q 2-------------------------------------------------------
import pandas as pd
import os, sys
import numpy as np
import math
np.random.seed(42)
filename = input().strip()

df = pd.read_csv(os.path.join(sys.path[0], filename))

population = df['Delivery_Time_Hours']

population_mean = population.mean()
population_std = population.std()

num_samples = 1000
sample_size = 30

sample_means = []

for _ in range(num_samples):
    sample = np.random.choice(population, sample_size, replace=True)
    sample_means.append(sample.mean())

sample_means = np.array(sample_means)

mean_of_sample_means = sample_means.mean()
std_of_sample_means = sample_means.std()

theoretical_se = population_std / math.sqrt(sample_size)

print(f"Population Mean: {population_mean:.2f}")
print(f"Mean of Sample Means: {mean_of_sample_means:.2f}")
print(f"Standard Deviation of Sample Means: {std_of_sample_means:.4f}")
print(f"Population Std Dev / √n: {theoretical_se:.4f}")
