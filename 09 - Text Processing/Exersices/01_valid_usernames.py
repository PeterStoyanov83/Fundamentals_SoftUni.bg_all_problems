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


def is_valid_username(username):
    # Check that the username is between 3 and 16 characters long
    if not (3 <= len(username) <= 16):
        return False

    # Check that the username contains only letters, numbers, hyphens, and underscores
    if not re.fullmatch(r'[\w-]+', username):
        return False

    # Check that the username has no redundant symbols
    if re.search(r'(^-|-$|_{2,}|-{2,})', username):
        return False

    return True


# Read the usernames from the input
usernames = input().split(", ")

# Print the valid usernames
for username in usernames:
    if is_valid_username(username):
        print(username)
