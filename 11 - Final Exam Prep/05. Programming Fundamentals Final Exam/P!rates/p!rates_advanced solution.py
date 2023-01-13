class City:
    def __init__(self, name, population, gold):
        self.name = name
        self.population = population
        self.gold = gold

    def __str__(self):
        return f"{self.name} -> Population: {self.population} citizens, Gold: {self.gold} kg"


class Pirate:
    def __init__(self):
        self.targeted_cities = {}

    def add_city(self, command):
        city_info = command.split("||")
        city_name = city_info[0]
        population = int(city_info[1])
        gold = int(city_info[2])

        if city_name in self.targeted_cities:
            self.targeted_cities[city_name].population += population
            self.targeted_cities[city_name].gold += gold
        else:
            self.targeted_cities[city_name] = City(city_name, population, gold)

    def plunder_city(self, command):
        event = command.split("=>")
        event_type = event[0]
        city_name = event[1]

        if city_name not in self.targeted_cities:
            print(f"{city_name} not found")
            return
        if event_type == "Plunder":
            population = int(event[2])
            gold = int(event[3])
            self.targeted_cities[city_name].population -= population
            self.targeted_cities[city_name].gold -= gold
            print(f"{city_name} plundered! {gold} gold stolen, {population} citizens killed.")

            if self.targeted_cities[city_name].population <= 0 or self.targeted_cities[city_name].gold <= 0:
                del self.targeted_cities[city_name]
                print(f"{city_name} has been wiped off the map!")
        elif event_type == "Prosper":
            gold = int(event[2])
            if gold < 0:
                print("Gold added cannot be a negative number!")
                return
            self.targeted_cities[city_name].gold += gold
            print(
                f"{gold} gold added to the city treasury. {city_name} now has {self.targeted_cities[city_name].gold} gold.")

    def end(self):
        if self.targeted_cities:
            print(f"Ahoy, Captain! There are {len(self.targeted_cities)} wealthy settlements to go to:")
            for city, info in self.targeted_cities.items():
                print(str(info))
        else:
            print("Ahoy, Captain! All targets have been plundered and destroyed!")


pirate = Pirate()

while True:
    command = input()
    if command == "Sail":
        break
    pirate.add_city(command)

while True:
    command = input()
    if command == "End":
        break
    pirate.plunder_city(command)

pirate.end()