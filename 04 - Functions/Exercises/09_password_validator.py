def leingh_check(a):
    if 6 <= len(a) <= 10:
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
validated = [leingh_check(password), is_alpha_is_num_check(password), min_2_digits_check(password)]
if all(validated):
    print("Password is valid")
