import re

pattern = r"(?P<surr>(@|#))(?P<word_1>[A-Za-z]{3,})(?P=surr)(?P=surr)(?P<word_2>[A-Za-z]{3,})(?P=surr)"
text = input()
mirror_words = []
count = 0

result = re.finditer(pattern, text)
for match in result:
    current_words = match.groupdict()
    if current_words["word_1"] == current_words["word_2"][::-1]:
        mirror_words.append(current_words["word_1"])
    count += 1

if count == 0:
    print(f"No word pairs found!")
else:
    print(f"{count} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join([f"{word} <=> {word[::-1]}" for word in mirror_words]))