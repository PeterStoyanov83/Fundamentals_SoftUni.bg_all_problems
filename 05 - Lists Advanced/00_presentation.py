import timeit


def even_numbers_comprehension():
    return [num for num in [1, 2, 3, 4, 5, 6]]


def even_numbers_loop():
    even_num = []
    for num in [1, 2, 3, 4, 5, 6]:
        if num % 2 == 0:
            even_num.append(num)
    return even_num


print(timeit.timeit(even_numbers_loop))
print(timeit.timeit(even_numbers_comprehension))

"""
Output : 
0.7964988000000001
0.4443957999999999
"""

x = [num for num in range(5)]

print(x)

# the result is [0, 1, 2, 3, 4]

list
