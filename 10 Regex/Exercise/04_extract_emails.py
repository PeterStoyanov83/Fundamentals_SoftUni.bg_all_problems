import re

mails = input()

pattern = r"(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b"

results = re.findall(pattern, mails)

for match in results:
    print(match[0])

