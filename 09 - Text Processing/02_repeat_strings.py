text = input().split()
result = ""

for word in text:
    result += word * len(word)

print(result)


# [print(s * len(s))for s in input().split()]

