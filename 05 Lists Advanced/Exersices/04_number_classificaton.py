def positives(numbers):
    return [(number) for number in numbers if number >=0]


def negatives(numbers):
    return [(number) for number in numbers if number < 0]


def even(numbers):
    return [(number) for number in numbers if number % 2 == 0 ]


def odd(numbers):
    return [(number) for number in numbers if number % 2 != 0 ]


numbers = [int(number) for number in input().split(", ")]

print(f' Positive: {positives(numbers)}')
print(f' Negative: {negatives(numbers)}')
print(f' Even: {even(numbers)}')
print(f' Odd: {odd(numbers)}')


"""
4. Number Classification

Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints
all the positive, negative, even, and odd numbers on separate lines as shown below.

Note: Zero is counted for a positive number

Examples

Input                                                           Output

1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33                       Positive: 1, 0, 5, 3, 4, 12, 19
                                                                Negative: -2, -100, -20, -33
                                                                Even: -2, 0, 4, -100, -20, 12
                                                                Odd: 1, 5, 3, 19, -33

1, 2, 53, 2, 21                                                 Positive: 1, 2, 53, 2, 21
                                                                Negative:
                                                                Even: 2, 2
                                                                Odd: 1, 53, 21
"""
