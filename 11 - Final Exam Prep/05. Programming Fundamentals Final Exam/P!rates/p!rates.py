import re

targeted_cities = {}

while True:
    command = input()
    if command == "Sail":
        break

    city_info = command.split("||")
    city_name = city_info[0]
    population = int(city_info[1])
    gold = int(city_info[2])

    if city_name in targeted_cities:
        targeted_cities[city_name]["population"] += population
        targeted_cities[city_name]["gold"] += gold
    else:
        targeted_cities[city_name] = {"population": population, "gold": gold}

while True:
    command = input()
    if command == "End":
        break

    event = command.split("=>")
    event_type = event[0]
    city_name = event[1]

    if event_type == "Plunder":
        population = int(event[2])
        gold = int(event[3])
        targeted_cities[city_name]["population"] -= population
        targeted_cities[city_name]["gold"] -= gold
        print(f"{city_name} plundered! {gold} gold stolen, {population} citizens killed.")

        if targeted_cities[city_name]["population"] <= 0 or targeted_cities[city_name]["gold"] <= 0:
            del targeted_cities[city_name]
            print(f"{city_name} has been wiped off the map!")
    elif event_type == "Prosper":
        gold = int(event[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        targeted_cities[city_name]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {city_name} now has {targeted_cities[city_name]['gold']} gold.")

if targeted_cities:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for city, info in targeted_cities.items():
        print(f"{city} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")

