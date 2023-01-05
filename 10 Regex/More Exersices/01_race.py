# import re
#
#
# patern = r"[A-z]+"
#
# list_of_racers = input().split(", ")
#
# while True:
#     command = input()
#     if command == "end of race":
#         break
#
#     match = re.findall(patern, command)
#     name = "".join(match)
#     place = 0
#     if name in list_of_racers:
#         place += 1
#         if place == 1:
#             place_of_racer = f'{place}st'
#         elif place == 2:
#             place_of_racer = f'{place}nd'
#         elif place == 3:
#             place_of_racer = f'{place}rd'
#             break
#
#

import re

racers = input().split(", ")

racer_distances = {}

while True:
    line = input()
    if line == "end of race":
        break
# Use regular expression to extract only the letters and digits from the line
    name_chars = re.findall("[A-Za-z0-9]", line)
# Convert the extracted characters to a string and store it as the name
    name = "".join(name_chars)

# If the name is in the list of racers, add the distance to their total distance
    if name in racers:
        distance = sum([int(char) for char in name_chars if char.isdigit()])
    if name in racer_distances:
        racer_distances[name] += distance
    else:
        racer_distances[name] = distance

# Sort the racers by distance in descending order
        sorted_racers = sorted(racer_distances, key=racer_distances.get, reverse=True)

# Print the top 3 racers
for i in range(3):
    place = i+1
    racer = sorted_racers[i]
    place += 1

    if place == 1:
        print(f'{place}st place: {racer}')
    elif place == 2:
        print(f'{place}nd place: {racer}')
    elif place == 3:
        print(f'{place}rd place: {racer}')
