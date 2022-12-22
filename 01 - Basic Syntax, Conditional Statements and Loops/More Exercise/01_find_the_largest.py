number = input()


list_of_numbers = []
for i in number:
    digit = int(i)
    list_of_numbers.append(digit)
list_of_numbers.sort()
list_of_numbers.reverse()
print(*list_of_numbers, sep="")
