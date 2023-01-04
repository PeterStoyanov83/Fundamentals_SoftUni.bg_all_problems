import re

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d+)\!(\d+)'

total_cost = 0

bought_furniture = []

command = input()

while command != "Purchase":

    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += int(quantity) * float(price)

    command = input()

print(f'Bought furniture:')
for furn in bought_furniture:
    print(furn)

print(f"Total money spend: {total_cost:.2f}")
