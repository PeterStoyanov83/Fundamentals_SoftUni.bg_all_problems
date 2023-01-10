import re

class Food:
    def __init__(self, name, expiration_date, calories):
        self.name = name
        self.expiration_date = expiration_date
        self.calories = calories

food_string = input()

# using regex to match the pattern of the food information
food_pattern = r"#(.+)#(.+)#(\d+)#|\|(.+)\|(.+)\|(\d+)\|"
foods = re.finditer(food_pattern, food_string)

total_calories = 0
food_list = []

for food in foods:
    name = food.group(1) or food.group(4)
    expiration_date = food.group(2) or food.group(5)
    calories = int(food.group(3) or food.group(6))

    total_calories += calories

    new_food = Food(name, expiration_date, calories)
    food_list.append(new_food)

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for food in food_list:
    print(f"Item: {food.name}, Best before: {food.expiration_date}, Nutrition: {food.calories}")