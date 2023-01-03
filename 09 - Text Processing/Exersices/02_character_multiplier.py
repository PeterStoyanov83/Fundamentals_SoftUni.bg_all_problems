# Read the input strings
str1, str2 = input().split()

# Initialize the total sum
total = 0

# Calculate the sum of the multiplied character codes
for i in range(min(len(str1), len(str2))):
    total += ord(str1[i]) * ord(str2[i])

# Add the remaining character codes to the total sum
for i in range(min(len(str1), len(str2)), max(len(str1), len(str2))):
    if len(str1) > len(str2):
        total += ord(str1[i])
    else:
        total += ord(str2[i])

# Print the result
print(total)
