string_to_list_input = input().split()
inverted = []
for string in string_to_list_input:
    inverted.append(-int(string))

print(inverted)


"""
1. Invert Values

Write a program that receives a single string containing positive and negative numbers separated by a single space.
Print a list containing the opposite of each number.
"""