def sum_numbers(a, b):
    result = a + b
    return result


def substract(d):
    result = sum_numbers(num_a, num_b) - d
    return result


num_a = int(input())
num_b = int(input())
num_c = int(input())

print(substract(num_c))


"""
2. Add and Subtract

You will receive three integer numbers.
Write functions named:

· sum_numbers() that returns the sum of the first two integers
· subtract() that returns the difference between the returned result of the first function and the third integer

Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters. 
Print the result of the subtract() function on the console.

Examples

Input   Output

23
6
10      19

1
17
30      -12

42      0
58 
100
"""