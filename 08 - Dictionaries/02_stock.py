inventory = input().split(' ')

inventory_products = {inventory[i]: int(inventory[i + 1]) for i in range(0, len(inventory), 2)}

search_product = input().split(' ')

for product in search_product:
    if product not in inventory_products:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {inventory_products[product]} of {product} left")
