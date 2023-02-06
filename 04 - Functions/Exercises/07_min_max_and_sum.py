def min_max_sum_function(a):
    min_int = min(a)
    max_int = max(a)
    sum_of_int = sum(a)
    return f'The minimum number is {min_int}\n The maximum number is {max_int}\n The sum number is: {sum_of_int}'


numbers = list(map(int, input().split(" ")))
print(min_max_sum_function(numbers))
