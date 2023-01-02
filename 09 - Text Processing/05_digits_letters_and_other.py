string = input()
digits = ''
chars = ''
other = ''

for character in string:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        chars += character
    else:
        other += character

print(digits)
print(chars)
print(other)