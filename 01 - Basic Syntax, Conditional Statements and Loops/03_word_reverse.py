word = input()
reversed_w = ""

for i in range(len(word) -1, -1, -1):
    reversed_w += word[i]
print(reversed_w)

