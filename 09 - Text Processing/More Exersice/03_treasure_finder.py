def decrypt(key, text):
    # Initialize the result string
    result = ""

    # Iterate through the characters of the text
    for i, ch in enumerate(text):
        # Decrypt the character by decreasing its ASCII code with the corresponding key number
        result += chr(ord(ch) - int(key[i % len(key)]))

    return result


# Read the input key
key = input().split()

# Initialize the decrypted message
message = ""

# Read the input lines until the "find" command is encountered
while True:
    line = input()
    if line == "find":
        break
    message += line

# Decrypt the message
decrypted = decrypt(key, message)

# Extract the treasure type and coordinates from the decrypted message
type_start = decrypted.index("&") + 1
type_end = decrypted.index("<")
type = decrypted[type_start:type_end]

coordinates_start = type_end + 1
coordinates_end = decrypted.index(">")
coordinates = decrypted[coordinates_start:coordinates_end]

# Print the result
print(f"Found {type} at {coordinates}")
