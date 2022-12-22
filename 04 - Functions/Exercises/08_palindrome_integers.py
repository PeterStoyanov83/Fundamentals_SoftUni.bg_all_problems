
def is_palindrome(i):
    for num in i:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


list_int = input().split(", ")

is_palindrome(list_int)

"""
8. Palindrome Integers

A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that receives 
a list of positive integers, separated by comma and space ", ". The function should check if each integer is a 
palindrome - True or False. Print the result.

Examples

Input               Output                              Input                   Output

123, 323, 421, 121  False True False True               32, 2, 232, 1010        False True True False

Hints · You can read more about palindromes here: https://en.wikipedia.org/wiki/Palindrome
"""