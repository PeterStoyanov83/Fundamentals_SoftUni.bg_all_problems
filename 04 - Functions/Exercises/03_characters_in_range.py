def ascii_in_range(a, b):
    list_of_char = []
    for char in range(ord(a) + 1, ord(b)):
        list_of_char.append(chr(char))
    return list_of_char


beginning = input()
end = input()

print(*ascii_in_range(beginning, end), end=" ")
