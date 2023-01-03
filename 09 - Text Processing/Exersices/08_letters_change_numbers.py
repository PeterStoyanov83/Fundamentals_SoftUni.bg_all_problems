def process_string(string):
    # Extract the number and the letters from the string
    number = int(string[0])
    first_letter = string[1]
    second_letter = string[2]

    # Perform the first operation based on the case of the first letter
    if first_letter.isupper():
        number /= ord(first_letter) - 64
    else:
        number *= ord(first_letter) - 96

    # Perform the second operation based on the case of the second letter
    if second_letter.isupper():
        number -= ord(second_letter) - 64
    else:
        number += ord(second_letter) - 96

    return number

# Read the input strings
strings = input("Enter the strings: ").split()

# Process the strings and sum the results
result = sum(process_string(string) for string in strings)

# Print the result
print(f"{result:.2f}")
