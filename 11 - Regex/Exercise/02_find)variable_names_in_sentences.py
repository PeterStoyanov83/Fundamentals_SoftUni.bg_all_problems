import re

sentences = input()

pattern = r"\b_([A-Za-z0-9]+)\b"

result = re.findall(pattern, sentences)

print(",".join(result))
