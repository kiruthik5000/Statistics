import numpy as np

n = int(input())

np.random.seed(42)

die1 = np.random.randint(1, 7, n)
die2 = np.random.randint(1, 7, n)

sums = die1 + die2

simple_prob = np.mean(sums > 8)

joint_prob = np.mean((die1 % 2 == 0) & (die2 > 3))

condition = (die1 == 4)
if np.sum(condition) == 0:
    conditional_prob = 0.0
else:
    conditional_prob = np.mean(sums[condition] == 7)

print("Simple Probability (Sum > 8):")
print(simple_prob)

print("\nJoint Probability (First even AND Second > 3):")
print(joint_prob)

print("\nConditional Probability (Sum = 7 | First die = 4):")
print(conditional_prob)
