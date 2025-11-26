from itertools import combinations

n, m = int(input()), int(input())

cnt = 0
for i in combinations(range(0, n), m):
    cnt += 1

print(f"Total combinations (C({n},{m})) without replacement: {cnt}")