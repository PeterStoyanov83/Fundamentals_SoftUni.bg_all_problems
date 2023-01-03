# Read the two characters from the input
char1 = input()
char2 = input()

# Read the string from the input
string = input()

# Find the ASCII values of the characters
ascii1 = ord(char1)
ascii2 = ord(char2)

# Find the sum of the ASCII values of all characters between the two given characters in the string
total = 0
for ch in string:
    ascii = ord(ch)
    if ascii1 < ascii < ascii2:
        total += ascii

# Print the result
print(total)
