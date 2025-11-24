print("BuyBloom Probability Calculator")

# 1. Order Return Probability
total_orders = int(input("Enter total number of orders shipped: "))
returned_orders = int(input("Enter number of orders returned: "))

prob_not_returned = (total_orders - returned_orders) / total_orders
print(f"Probability a randomly selected order was NOT returned: {prob_not_returned:.4f}\n")

# 2. Delivery Partner On-Time Probability (without replacement)
total_partners = int(input("Enter total number of delivery partners: "))
delayed_partners = int(input("Enter number of delayed partners: "))

on_time = total_partners - delayed_partners

# P(first on time) * P(second on time | first on time)
prob_two_on_time = (on_time / total_partners) * ((on_time - 1) / (total_partners - 1))

print(f"Probability both randomly chosen partners are on time: {prob_two_on_time:.4f}\n")

# 3. Flash Sale Discount Probability
p_discount = float(input("Enter probability of a product getting a discount (0 to 1): "))
num_products = int(input("Enter number of products chosen: "))

prob_all_discount = p_discount ** num_products

print(f"Probability all {num_products} randomly chosen products get discount: {prob_all_discount:.4f}\n")

# 4. Flash Deal Day Probability
total_days = int(input("Enter total number of days in the period (e.g., 7): "))
deal_days = int(input(f"Enter number of days with deals (out of {total_days}): "))

prob_deal_day = deal_days / total_days

print(f"Probability of finding a deal on a random day: {prob_deal_day:.4f}")
