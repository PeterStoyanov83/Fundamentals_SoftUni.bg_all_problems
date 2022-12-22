def min_max_sum_function(a):
    min_int = min(a)
    max_int = max(a)
    sum_of_int = sum(a)
    return f'The minimum number is {min_int}\n The maximum number is {max_int}\n The sum number is: {sum_of_int}'


numbers = list(map(int, input().split(" ")))
print(min_max_sum_function(numbers))
"""
7. Min Max and Sum

Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print the min and max values of the given numbers and the sum of all the numbers in the list.
Use min(), max() and sum().

The output should be as follows:

· On the first line: "The minimum number is {minimum number}"
· On the second line: "The maximum number is {maximum number}"
· On the third line: "The sum number is: {sum of all numbers}"

Example

Input                   Output

2 4 6                   The minimum number is 2 The maximum number is 6 The sum number is: 12

12 52 11 53 2 8 45      The minimum number is 2 The maximum number is 53 The sum number is: 183
"""