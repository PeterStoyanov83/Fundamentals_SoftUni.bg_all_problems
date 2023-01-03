"""
this is unfinished
"""
# Read the input data
data = input()
string = input() # read the input
unique_symbols = set() # set to store unique symbols
result = "" # string to store the result

# loop through the input string
for i in range(len(string)):
    # check if the current character is a digit
    if string[i].isdigit():
        # if it is a digit, convert the previous characters to uppercase and repeat them N times
        result += string[i - 1:i].upper() * int(string[i])
    # add the current character to the set of unique symbols
        unique_symbols.add(string[i - 1].upper())

# print the number of unique symbols used
print(f"Unique symbols used: {len(unique_symbols)}")

# print the result
print(result)