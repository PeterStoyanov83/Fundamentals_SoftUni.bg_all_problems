import re

data = input()

pattern = r"(=|\/)[A-Z][A-z]{2,}\1"

result = re.finditer(pattern, data)

points = 0

destinations = []

for destination in result:
    current_destination = re.split('[/=]', destination.group())[1]
    points += len(current_destination)
    destinations.append(current_destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")