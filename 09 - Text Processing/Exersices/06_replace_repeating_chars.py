def remove_duplicate_letters(text):
    # Initialize the result string
    result = ""

    # Iterate through the characters of the text
    for i in range(len(text)):
        # If the current character is different from the previous one, add it to the result
        if i == 0 or text[i] != text[i-1]:
            result += text[i]
    return result



# Read the input text
text = input()

# Remove the duplicate letters from the text
result = remove_duplicate_letters(text)

# Print the result
print(result)