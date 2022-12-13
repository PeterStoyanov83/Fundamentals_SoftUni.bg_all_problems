# numbers = input().split(' ')
#
# abs_numbers = []
#
# for num in numbers:
#     abs_numbers.append(abs(float(num)))
#
# print(abs_numbers)


# with a function

def absolute_num_f(nums):
    result= [abs(num) for num in nums]
    return result

numbers = list(map(float, input().split(' ')))

print(absolute_num_f(numbers))

"""
1. Absolute Values

Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute 
value as a list. Use abs().
"""
