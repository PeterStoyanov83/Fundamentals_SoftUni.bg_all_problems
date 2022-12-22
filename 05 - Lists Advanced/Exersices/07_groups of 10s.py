# list_of_numbers = list(map(int, input().split(", ")))
# upper_boundary = 10
# lower_boundary = 0
# result = []
# sorted_list = sorted(list_of_numbers)
# sorted_list = reversed(sorted_list)
#
# for num in range(sorted_list, 0, -1):
#     current_list = []
#     for num in list_of_numbers:
#         if (num) >= lower_boundary and (num) <= upper_boundary:
#             current_list.append(num)
#             sorted_list.remove(num)
#     result.append(current_list)
#     print(f"Group of {upper_boundary}'s: {current_list}")
#     lower_boundary = upper_boundary
#     upper_boundary += 10
# print(f"Group of {upper_boundary}'s: {sorted_list}")


numbers = list(map(int, input().split(", ")))
tens = 0

while numbers:
    tens += 10
    current_list = list(filter(lambda n: n <= tens, numbers))
    numbers = [num for num in numbers if num not in current_list]
    print(f"Group of {tens}'s: {current_list}")


"""
7. Group of 10's

Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".

Examples:

· The numbers 2, 8, 4, and 10 fall into the group of 10's.
· The numbers 13, 19, 14, and 15 fall into the group of 20's.

For more clarification, see the examples below.

Example

Input                                       Output

8, 12, 38, 3, 17, 19, 25, 35, 50            Group of 10's: [8, 3]
                                            Group of 20's: [12, 17, 19]
                                            Group of 30's: [25]
                                            Group of 40's: [38, 35]
                                            Group of 50's: [50]

1, 3, 3, 4, 34, 35, 25, 21, 33              Group of 10's: [1, 3, 3, 4]
                                            Group of 20's: []
                                            Group of 30's: [25, 21]
                                            Group of 40's: [34, 35, 33]

Hints
· Keep track of the group using a variable to store its max value.
· Create a loop and filter the elements that are less than or equal to the group boundary and remove them
from the original list.
· Increase the boundary by 10.
· Loop until the given list is empty.
"""