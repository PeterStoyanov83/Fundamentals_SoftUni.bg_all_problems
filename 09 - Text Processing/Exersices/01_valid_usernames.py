def is_valid_username(username):
    # Check that the username is between 3 and 16 characters long
    if len(username) < 3 or len(username) > 16:
        return False

    # Check that the username contains only letters, numbers, hyphens, and underscores
    for ch in username:
        if not ch.isalnum() and ch != '-' and ch != '_':
            return False

    # Check that the username has no redundant symbols
    if username[0] == '-' or username[0] == '_' or username[-1] == '-' or username[-1] == '_':
        return False
    for i in range(1, len(username) - 1):
        if (username[i] == '-' and username[i - 1] == '-') or (username[i] == '_' and username[i - 1] == '_'):
            return False

    return True


# Read the usernames from the input
usernames = input().split(", ")

# Print the valid usernames
for username in usernames:
    if is_valid_username(username):
        print(username)

"""
This program reads a list of usernames from the input, splits it into individual usernames using the split() 
function, and checks each username using the is_valid_username() function. If the username is valid, it is printed to
the output.
"""

"using regex"

import re


def extract_person_info(line):
    # Use a regular expression to find the name and age in the string
    name_regex = r"@(.+?)\|"
    age_regex = r"#(.+?)\*"
    name = re.search(name_regex, line).group(1)
    age = re.search(age_regex, line).group(1)

    # Print the extracted information
    print(f"{name} is {age} years old.")


# Read N lines of input from the user
N = int(input())
for i in range(N):
    line = input()
    extract_person_info(line)
