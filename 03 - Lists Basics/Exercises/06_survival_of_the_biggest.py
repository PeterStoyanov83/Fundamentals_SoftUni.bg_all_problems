
list_of_int = list(map(int, input().split()))

n = int(input())


for i in range(1, n + 1):
    min_int = min(list_of_int)
    list_of_int.remove(min_int)

list_of_int = list(map(str, list_of_int))
print(*list_of_int, sep=", ")

""""
6. Survival of the Biggest

Write a program that receives a list of integer numbers and a number n. The number n represents the amount of
numbers to remove from the list. You should remove the smallest ones

Input

On the first line you will receive a string (numbers separated by a space),
on the second line you will receive a number n (count of numbers to remove)

Output
Print all the numbers that are left in the list

Example

Input                       Output

10 9 8 7 6 5
3                           [10, 9, 8]
____________________________________________
1 10 2 9 3 8
2                           [10, 9, 3, 8]
"""