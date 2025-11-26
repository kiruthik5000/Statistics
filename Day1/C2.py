import os
import sys
import pandas as pd
def get_int_input(prompt):
    try:
        value = int(input(prompt))
        if value < 0:
            print("Please enter a non-negative integer.")
            sys.exit(1)
        return value
    except ValueError:
        print("Invalid input! Please enter an integer.")
        sys.exit(1)


age_groups = ['18–25', '26–40', '40+']
coffee_types = ['Latte', 'Black Coffee']

data = {coffee: [] for coffee in coffee_types}

for age in age_groups:
    print(f"\nAge group: {age}")
    for coffee in coffee_types:
        count = get_int_input(f"Number of customers who prefer {coffee}: ")
        data[coffee].append(count)

# Create DataFrame
df = pd.DataFrame(data, index=age_groups)

total_customers = df.values.sum()
if total_customers == 0:
    print("No data provided (total customers = 0). Exiting.")
    sys.exit(1)

print("\nData Summary:")
print(df)

joint_prob_older_black = df.loc['40+', 'Black Coffee'] / total_customers
print(f"\nJoint Probability P(Age 40+ and Black Coffee): {joint_prob_older_black:.4f}")

total_40plus = df.loc['40+'].sum()
if total_40plus == 0:
    print("No customers in the 40+ age group, conditional probability undefined.")
    sys.exit(1)

black_40plus = df.loc['40+', 'Black Coffee']
cond_prob_black_given_40plus = black_40plus / total_40plus
print(f"Conditional Probability P(Black Coffee | Age 40+): {cond_prob_black_given_40plus:.4f}")

overall_prob_black = df['Black Coffee'].sum() / total_customers
print(f"\nOverall Probability P(Black Coffee): {overall_prob_black:.4f}")
print(f"Conditional Probability P(Black Coffee | Age 40+): {cond_prob_black_given_40plus:.4f}")

if abs(cond_prob_black_given_40plus - overall_prob_black) < 1e-4:
    print("Age (being 40 or older) does NOT influence preference for Black Coffee.")
else:
    print("Age (being 40 or older) influences preference for Black Coffee.")
