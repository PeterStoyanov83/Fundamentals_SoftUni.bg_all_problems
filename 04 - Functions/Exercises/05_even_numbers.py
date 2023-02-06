def filter_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = list(map(int, input().split()))

result = list(filter(filter_even, num))
print(result)
