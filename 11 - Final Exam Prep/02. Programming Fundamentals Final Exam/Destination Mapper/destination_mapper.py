import re

pattern = re.compile(r'([\\|#])(?P<product>[A-Za-z ]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1')

food = input()

matches = pattern.finditer(food)

food = []
calories = 0


for match in matches:
    #creating a nested list
    food.append(f"Item: {match['product']}, Best before: {match['date']}, Nutrition: {match['calories']}")
    #calculating total calories
    calories += int(match['calories'])


food_for_n_days = calories // 2000

print(f"You have food to last you for: {food_for_n_days} days!")

[print(item) for item in food]
