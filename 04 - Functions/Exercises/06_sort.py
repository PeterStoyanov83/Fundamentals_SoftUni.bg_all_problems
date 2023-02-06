def sort_function(n):
    n.sort()
    return n


list_of_numbers = list(map(int, input().split(" ")))

print(sort_function(list_of_numbers))
