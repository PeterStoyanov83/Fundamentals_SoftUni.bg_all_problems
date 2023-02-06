
list_of_int = list(map(int, input().split()))

n = int(input())


for i in range(1, n + 1):
    min_int = min(list_of_int)
    list_of_int.remove(min_int)

list_of_int = list(map(str, list_of_int))
print(*list_of_int, sep=", ")
