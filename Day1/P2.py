def read_counts(product_name):
    while True:
        try:
            counts = list(map(int, input(f"Enter counts for {product_name}: ").split(",")))
            if len(counts) != 4 or any(c < 0 for c in counts):
                print("Error: Enter exactly 4 non-negative integers separated by commas.")
                continue
            return counts
        except:
            print("Invalid input. Try again.")

# ---- Input ----
A = read_counts("Product A")
B = read_counts("Product B")
C = read_counts("Product C")
D = read_counts("Product D")

# Combine all product data into a matrix
data = [A, B, C, D]

# Total purchases
total = sum(sum(row) for row in data)

# ----- (1) P(Product A and age <25) -----
p_A_under25 = A[0] / total

# ----- (2) P(age 25-40 | Product C) -----
total_C = sum(C)
p_age2540_given_C = C[1] / total_C if total_C > 0 else 0

# ----- (3) P(age 41-60) -----
total_age_41_60 = sum(row[2] for row in data)
p_age_41_60 = total_age_41_60 / total

# ----- (4) Independence check: Product B and Age 60+ -----
joint_B_60plus = B[3] / total
p_B = sum(B) / total
p_60plus = sum(row[3] for row in data) / total
product_of_marginals = p_B * p_60plus

# ---- Output ----
print(f"\nProbability of Product A by someone aged < 25: {p_A_under25:.4f}")
print(f"Probability of age 25-40 given Product C purchase: {p_age2540_given_C:.4f}")
print(f"Overall probability of buyer from 41-60 age group: {p_age_41_60:.4f}\n")

print(f"P(Product B and Age 60+): {joint_B_60plus:.4f}")
print(f"    P(Product B): {p_B:.4f}")
print(f"    P(Age 60+): {p_60plus:.4f}")
print(f"    P(Product B) * P(Age 60+): {product_of_marginals:.4f}")

if abs(joint_B_60plus - product_of_marginals) < 1e-6:
    conclusion = "INDEPENDENT"
else:
    conclusion = "DEPENDENT"

print(f"Conclusion: Product B purchases and Age 60+ are {conclusion}.")
