def positives(numbers):
    return [(number) for number in numbers if number >= 0]


def negatives(numbers):
    return [(number) for number in numbers if number < 0]


def even(numbers):
    return [(number) for number in numbers if number % 2 == 0]


def odd(numbers):
    return [(number) for number in numbers if number % 2 != 0]


numbers = [int(number) for number in input().split(", ")]

print(f' Positive: {positives(numbers)}')
print(f' Negative: {negatives(numbers)}')
print(f' Even: {even(numbers)}')
print(f' Odd: {odd(numbers)}')
