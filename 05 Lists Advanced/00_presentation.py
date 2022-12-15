"""
LIST COMPREHENSION
plus:
    - comprehension is much faster and takes less memory
    - very short - one line code

minus:
    - used for very specific exact tasks not a universal tool
    - not suitable for large number operations
    -

structure :

[ output expression (result) | for cycle | optional parameters (conditions)]
[       x**2                   for x in num        if num x > 0 ]

 examples :

 nums =  [1, 2, 3, 4, 5, 6]
 filtered = [True if x % 2 == 0 else False for x in nums]
 ___________________________

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                              " only if all the conditions return True"
result = [num for num in nums if num % 2 == 0 if num > 5 if num != 10]
                                condition 1    cond 2       cond 3
_______________________________________________________
nested comprehension :

matrix =  [[x for x in range(3)] for _ in range(3)]

result - [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
____________________________________________________


.append()
.extend()
.insert( index, value)
.pop(value)
.remove(value)
.shift()
.sort()
.clear()
.set() - extract unique elements from a list


count()
    Calculates total occurrence of a given element of List.

del[a : b]
    This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
.sorted(list) - in accending order

        .sorted(list, key=(can be function or other operation) , reverse = True)


difference between map and filter  map returns everything and filter - only True values

____________________________________________
SWAPPING


nums = [1, 2, 3]

nums[0], nums[1], nums[2] = nums[2], nums[0], nums[1]

# 1 swaps with 3

# 2 swaps with 1

# 3 swaps with 2



"""

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

x= [num for num in range(5)]

print(x)

# the result is [0, 1, 2, 3, 4]

list