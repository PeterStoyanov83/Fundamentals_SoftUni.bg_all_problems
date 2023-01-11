import re

date = input()

search_pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"

result = re.findall(search_pattern, date)

for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
   