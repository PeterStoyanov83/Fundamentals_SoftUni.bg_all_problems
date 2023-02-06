budget = float(input())

price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk_liter = price_flour * 1.25
coloured_eggs = 0
current_bread_count = 0
budget_per_loaf = price_eggs + (price_milk_liter / 4) + price_flour

while budget >= budget_per_loaf:
    budget -= budget_per_loaf
    coloured_eggs += 3
    current_bread_count += 1
    if current_bread_count % 3 == 0:
        coloured_eggs -= (current_bread_count - 2)

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {coloured_eggs}"
      f" eggs and {budget:.2f}BGN left.")
