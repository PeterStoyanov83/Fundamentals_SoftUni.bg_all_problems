import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

numbers = input()

result = re.finditer(pattern, numbers)

for match in result:
    print(match.group(), end=" ")


