from itertools import permutations

n = int(input())
m = int(input())

cnt = 0
for i in permutations(range(0, n), m):
    cnt += 1
print(f"Total permutations (P({n},{m})) without replacement: {cnt} ")