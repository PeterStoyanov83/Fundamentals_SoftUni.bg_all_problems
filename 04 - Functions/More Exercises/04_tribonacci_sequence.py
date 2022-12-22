starting_number = int(input())
last_three = [1, 1]


def show_tribonacci(num):
    for number in range(1, num + 1):
        if number == 1 or number == 2:
            print(last_three[number - 1], end=" ")
            continue
        else:
            add_last_number = 0
            if len(last_three) > 2:
                add_last_number = last_three.pop(0)
        print(sum(last_three) + add_last_number, end=" ")
        last_three.append(sum(last_three) + add_last_number)


show_tribonacci(starting_number)

"""
4. Tribonacci Sequence

In the Tribonacci sequence, every number is formed by the sum of the previous 3.

Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting
from 1. You will receive a positive integer number as input.

Examples

Input   Output          Input   Output

4       1 1 2 4         8       1 1 2 4 7 13 24 44
"""