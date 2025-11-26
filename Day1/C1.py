n = int(input("Enter the number of Kings in the deck: "))
kings = int(input("Enter the total number of cards in the deck: \n"))
print(f"Initial Kings in deck: {n}")
print(f"Initial total cards in deck: {kings}")

print(f"Probability of drawing the first King: {(n/kings):.4f}")
n = n - 1
kings = kings - 1
print(f"Kings remaining after first draw: {n}")
print(f"Total cards remaining after first draw: {kings}")
print(f"Probability of drawing the second King (given first was King and not replaced): {(n/ kings):.4f}")
p1 = (n + 1)/ (kings + 1)
p2 = (n / kings)
print(f"Probability of drawing two Kings consecutively without replacement: {(p1 * p2):.4f}")

