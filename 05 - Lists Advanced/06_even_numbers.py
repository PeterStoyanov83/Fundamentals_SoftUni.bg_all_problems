numbers = list(map(int, input().split(', ')))

indexes = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]

print(indexes)
