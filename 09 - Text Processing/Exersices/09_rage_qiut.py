import re

# Read the input
input_data = input()

# Extract the string-number sequences
matches = re.findall(r'\D+\d+', input_data)

# Calculate the number of unique symbols
unique_symbols = set()
for match in matches:
    string = match[:-1]
    unique_symbols.update(string.upper())

# Print the number of unique symbols
print(f'Unique symbols used: {len(unique_symbols)}')

# Build the rage message
rage_message = ''
for match in matches:
    string = match[:-1].upper()
    repeat_count = int(match[-1])
    rage_message += string * repeat_count

# Print the rage message
print(rage_message)