from itertools import combinations, combinations_with_replacement

print("Ice Cream Flavor Combination Calculator")
arr = list(input("Enter ice cream flavors separated by commas (e.g., Vanilla, Chocolate, etc.): ").split(','))
n = int(input(f"How many flavors do you want to choose (out of {len(arr)} available)?: \n"))
print("Flavor Combinations")

cnt = 0
p = combinations(arr, n)
for i in p:
    cnt += 1

print(f"Total combinations without replacement: {cnt}")

pr = combinations_with_replacement(arr, n)

cnt = 0
for i in pr:
    cnt += 1
print(f"Total combinations with replacement: {cnt}")
