from itertools import permutations, product
print("PIN Permutation Generator")
arr = list(map(int, input("Enter digits to use for PIN separated by commas (e.g., 0,1,2,3,4): ").split(',')))

n = int(input("Enter the length of the PIN (e.g., 3): \n"))

print("PIN Permutations")
perms = permutations(arr, n)
pr = product(arr, repeat=n)
cnt = 0
for i in perms: 
    cnt += 1
print(f"Total PINs without replacement (unique digits): {cnt}")
cnt = 0
for i in pr:
    cnt += 1

print(f"Total PINs with replacement (digits can repeat): {cnt}")
