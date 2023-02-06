countries = input().split(", ")
capitals = input().split(", ")

# result = {countries[index]: capitals[index] for index in range(len(countries))}
result = dict(zip(countries, capitals))  # zip method
for country, capital in result.items():
    print(f"{country} -> {capital}")
