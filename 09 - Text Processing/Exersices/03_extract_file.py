
filename_with_extensions = input().split("\\")
filename, extension = filename_with_extensions[-1].split(".")

print(f"File name: {filename}")
print(f'File extension: {extension}')



# _____________________

import re

# Read the input filename with extensions
filename_with_extensions = input()

# Use a regular expression to extract the filename and extension from the input
match = re.match(r".*\\(.*)\.(.*)", filename_with_extensions)
filename = match.group(1)
extension = match.group(2)

# Print the filename and extension
print(f"File name: {filename}")
print(f'File extension: {extension}')