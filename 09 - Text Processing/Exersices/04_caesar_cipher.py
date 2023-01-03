def encrypt(text):
    # Initialize the encrypted text
    encrypted = ""

    # Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table
    for ch in text:
        encrypted += chr(ord(ch) + 3)

    return encrypted

# Read the input text
text = input()

# Encrypt the text
encrypted = encrypt(text)

# Print the encrypted text
print(encrypted)
