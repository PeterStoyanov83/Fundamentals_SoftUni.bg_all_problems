def is_palindrome(i):
    for num in i:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


list_int = input().split(", ")

is_palindrome(list_int)
