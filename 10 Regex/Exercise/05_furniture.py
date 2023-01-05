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




# __________________________________________________________

# import re

name = re.compile(r'(?<=\>{2})[a-zA-Z0-9]+(?=\<{2})')
price = re.compile(r'(?<=\<{2})\d+(\.\d+)?(?=\!)')
quantity = re.compile(r'(?<=\!)\d+\b')

all_furniture = []
end_price = 0

while True:
    purchase = input()
    if purchase == 'Purchase':
        break
    name_match = name.search(purchase)
    price_match = price.search(purchase)
    quantity_match = quantity.search(purchase)
    if name_match and price_match and quantity_match:
        all_furniture.append(name_match.group())
        end_price += (float(price_match.group()) * int(quantity_match.group()))

print('Bought furniture:')
if all_furniture:
    print('\n'.join(all_furniture))
print('Total money spend:', f'{end_price:.2f}')

# Furniture v2

# import re

name = re.compile(r'>>(?P<name>[A-Za-z\d]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)')

all_furniture = []
end_price = 0

while True:
    purchase = input()
    if purchase == 'Purchase':
        break
    match = name.search(purchase)
    if match:
        furniture = match.groupdict()
        all_furniture.append(furniture['name'])
        end_price += (float(furniture['price']) * int(furniture['quantity']))

print('Bought furniture:')
if all_furniture:
    print('\n'.join(all_furniture))
print('Total money spend:', f'{end_price:.2f}')