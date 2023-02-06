n = int(input())
sum_of_chars = 0

for i in range(1, n + 1):
    char = input()
    sum_of_chars += int(ord(char))

print(f"The sum equals: {sum_of_chars}")
