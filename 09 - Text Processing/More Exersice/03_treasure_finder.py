import re


def decrypt(key, text):
    # Initialize the decrypted text
    decrypted = ""

    # Decrypt the text by decreasing the ASCII code of each character with a corresponding number of the key sequence
    for i, ch in enumerate(text):
        decrypted += chr(ord(ch) - int(key[i % len(key)]))

    return decrypted


# Read the key
key = input().split()

# Initialize the message
message = ""

# Read the message lines until the "find" command
while True:
    line = input()
    if line == "find":
        break
    message += line

# Decrypt the message
    decrypted = decrypt(key, message)

# Find the treasure type and coordinates
    treasure_type = re.search(r'&(.+?)&', decrypted).group(1)
    coordinates = re.search(r"<(.+?)>", decrypted).group(1)

# Print the result
    print("Found {} at {}".format(treasure_type, coordinates))