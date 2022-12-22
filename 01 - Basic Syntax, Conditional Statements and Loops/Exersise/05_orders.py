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



"""
5. Orders

You work at a coffee shop, and your job is to place orders to the distributors. Thus, you want to know the price of
each order. On the first line, you will receive integer N - the number of orders the shop will receive.
For each order, you will receive the following information:

· Price per capsule - a floating-point number in the range [0.01…100.00]
· Days - integer in the range [1…31]
· Capsules, needed per day - integer in the range [1…2000]
For each order, you should print a single line in the following format:
· "The price for the coffee is: ${price}"

If you do not receive a correct order (one or more of the values are not in the given range), you should ignore it and
move to the next one.
After you go through all orders, you need to print the total price in the following format:
· "Total: ${total_price}"
Both the price of a coffee and the total price must be formatted to the second decimal place.

Examples

Input               Output
1
1.53
30
8                   The price for the coffee is: $367.20 Total: $367.20
_________________________________________
2
4.99
31
3
0.35
31
5                   The price for the coffee is: $464.07 The price for the coffee is: $54.25 Total: $518.32
_________________________________________________
2
9.223
31
0
0.05
10
30                  The price for the coffee is: $15.00 Total: $15.00
"""