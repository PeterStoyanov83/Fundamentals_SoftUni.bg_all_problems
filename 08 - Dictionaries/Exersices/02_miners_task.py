miners_dictionary = {}

while True:
    current_resource = input()

    if current_resource == "stop":
        break
    current_quantity = int(input())

    if current_resource not in miners_dictionary.keys():
        miners_dictionary[current_resource] = 0
    miners_dictionary[current_resource] += current_quantity

for current_resource, current_quantity in miners_dictionary.items():
    print(f"{current_resource} -> {current_quantity}")
