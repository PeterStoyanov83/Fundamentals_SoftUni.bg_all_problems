population = list(map(int, input().split(", ")))

minimum_welth = int(input())

average_welth = sum(population) / len(population)

# print(average_welth)
social_population = []

if average_welth > minimum_welth:
    for person in population:
        population.remove(person)
        population.append(int(average_welth))
    print(population)

else:
    print("No equal distribution possible")
