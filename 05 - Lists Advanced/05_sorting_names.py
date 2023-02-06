names = input().split(', ')

result = sorted(names, key=lambda item: (-len(item), item))  # sorting by len ad alphabetically

print(result)
