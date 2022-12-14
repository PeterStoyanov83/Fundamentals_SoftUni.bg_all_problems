def ascii_in_range(a, b):
    list_of_char = []
    for char in range(ord(a) + 1, ord(b)):
        list_of_char.append(chr(char))
    return list_of_char

beginning = input()
end = input()

print(*ascii_in_range(beginning, end), end=" ")

"""
3. Characters in Range

Write a function that receives two characters and returns a single string with all the characters in between them 
(according to the ASCII code), separated by a single space. Print the result on the console.

Examples:
Input       Output

a
d           b c
________________________
#
:           $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9
________________________
#
C           $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A
"""