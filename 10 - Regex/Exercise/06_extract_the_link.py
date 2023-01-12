import re

pattern = r"((w{3})\.([A-Za-z0-9]+)(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"

valid_urls = []

sentence = input()

while sentence:
    matches = re.search(pattern, sentence)
    if matches:

        valid_urls.append(matches.group(0))

    sentence = input()

for url in valid_urls:
    print(url)


# _________________________ with  re.finditer()

import re

pattern = r"((w{3})\.([A-Za-z0-9]+)(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"

valid_urls = []

sentence = input()

while sentence:
    matches = re.finditer(pattern, sentence) # iterable object
    for match in matches: # we make a cycle to go through all the matches
        valid_urls.append(match.group(1))

    sentence = input()

for url in valid_urls:
    print(url)
