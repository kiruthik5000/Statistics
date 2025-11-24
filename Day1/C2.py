import pandas as pd

data = {'Latte':[], 'Black Coffee':[], 'total': []}

total_observation = 0
index = ['18-25', '26-40', '40+']
for i in index:
    print(f"\nAge group: {i}")
    lat, cof = int(input("Number of customers who prefer Latte: ")), int(input("Number of customers who prefer Black Coffee: "))
    total_observation += lat
    total_observation += cof
    data['Latte'].append(lat);
    data['Black Coffee'].append(cof)
    data['total'].append(lat+cof)

df = pd.DataFrame(data)
df['age_group'] = index;
df.set_index('age_group', inplace=True)
df.index.name=None

print('Data Summary:')
print(df[['Latte', 'Black Coffee']])
print()

p1 = df.loc['40+']['Black Coffee']
join_prob = p1 / total_observation

p2 = df.loc['40+']['total']
con_pro = p1 / p2 if p2 != 0 else 0

over_black = df['Black Coffee'].sum() / total_observation

print(f"Joint Probability p(Age 40+ and Black Coffee): {join_prob:.4f}")
print(f"Conditional Probability P(Black Coffee | Age 40+): {con_pro:.4f}")
print()


print(f"Overall Probability P(Black Coffee): {over_black:.4f}")
print(f"Conditional Probability P(Black Coffee | Age 40+): {con_pro:.4f}")

if abs(con_pro - over_black) < 1e-4:
    print(f"Age (being 40 or older) does NOT influences preference for Black Coffee.")
else:
    print(f"Age (being 40 or older) influences preference for Black Coffee.")
