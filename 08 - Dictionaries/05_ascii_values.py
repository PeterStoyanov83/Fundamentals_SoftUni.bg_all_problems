
list_of_characters = input().split(", ")

# characters = {}
# for key in list_of_characters:
#     characters[key] = ord(key)

characters = {key: ord(key) for key in list_of_characters}
print(characters)