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
