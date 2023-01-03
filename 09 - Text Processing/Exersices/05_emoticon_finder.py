# Read the input text
text = input()

# Initialize a string to store the emoticons
emoticons = ""

# Find all emoticons in the text
for i, ch in enumerate(text):
    if ch == ":":
        if i + 1 < len(text):
            emoticons += f"{text[i:i+2]}\n"

# Print the emoticons
print(emoticons)



# +++++++++++++++++++++++++++++++++++++++++++


# using regex

import re

def find_emoticons(text):
    # Use a regular expression to find all emoticons in the text
    emoticons = re.findall(r":\S", text)

    return emoticons

# Read the input text
text = input("Enter the text: ")

# Find the emoticons in the text
emoticons = find_emoticons(text)

# Print the emoticons
print("Emoticons:", emoticons)
