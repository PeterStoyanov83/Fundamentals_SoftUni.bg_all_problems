number_of_orders = int(input())
total_amount = 0
amount_per_order = 0

for i in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())
    amount_per_order = price_per_capsule * days * caps_per_day

    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= caps_per_day <= 2000 and amount_per_order != 0:
        print(f"The price for the coffee is: ${amount_per_order:.2f}")
        total_amount += amount_per_order
        amount_per_order = 0
    else:
        continue
print(f"Total: ${total_amount:.2f}")
