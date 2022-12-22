def lengh_check(a):
    if 6 <= len(a)<=10:
        return True
    print("Password must be between 6 and 10 characters")
    return False

def is_alpha_is_num_check(a):
    if a.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False

def min_2_digits_check(a):
    digits_counter = 0
    for i in a:
        if i.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


password = input()
validated = [lengh_check(password), is_alpha_is_num_check(password), min_2_digits_check(password)]
if all(validated):
    print("Password is valid")



"""
9. Password Validator

Write a function that checks if a given password is valid. Password validations are:

· It should be 6 - 10 (inclusive) characters long
· It should consist only of letters and digits
· It should have at least 2 digits

If a password is valid, print "Password is valid".
Otherwise, for every unfulfilled rule, print a message:

· "Password must be between 6 and 10 characters"
· "Password must consist only of letters and digits"
· "Password must have at least 2 digits"

Examples
Input                       Output

logIn                       Password must be between 6 and 10 characters
                            Password must have at least 2 digits
_______________________________________________
MyPass123                   Password is valid
_______________________________________________
Pa$s$s                      Password must consist only of letters and digits
                            Password must have at least 2 digits
"""