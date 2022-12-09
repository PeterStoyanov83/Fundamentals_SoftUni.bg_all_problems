import  math
sentury = int(input())
years = sentury * 100
days = math.floor(years * 365.2422)
hours = math.floor(days * 24)
minutes = math.floor(hours * 60)

print(f"{sentury:.0f} centuries = {years:.0f} years = "
      f"{days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")