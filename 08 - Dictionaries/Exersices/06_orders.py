orders = {}

while True:
    current_input = input()
    if current_input == 'buy':
        break
    name, price, qty = current_input.split(' ')
    if name not in orders:
        orders[name] = [float(price), int(qty)]
    else:
        orders[name][0] = float(price)
        orders[name][1] += int(qty)

for name in orders:
    total_price = orders[name][0] * orders[name][1]
    print(f"{name} -> {total_price:.2f}")
