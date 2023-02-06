items_and_prices = input().split("|")
budget = float(input())
items_bought = []
items_sold = []
profit = 0

for item in items_and_prices:
    item_list = item.split("->")
    price_of_item = float(item_list[1])
    category_of_item = item_list[0]
    if budget >= price_of_item:
        if category_of_item == "Clothes" and price_of_item <= 50 or category_of_item == "Shoes" and price_of_item \
                <= 35 or category_of_item == "Accessories" and price_of_item <= 20.5:
            budget -= price_of_item
            items_bought.append(price_of_item)
for price in items_bought:
    profit += price * 0.40
    items_sold.append(price + (price * 0.4))
for price in items_sold:
    print(f"{price:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if sum(items_sold) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
