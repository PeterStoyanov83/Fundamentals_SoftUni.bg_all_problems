list_of_numbers = list(map(int, input().split()))
list_of_numbers.sort()
list_of_numbers.reverse()
average_in_list = int(sum(list_of_numbers) / len(list_of_numbers))
list_of_greater = []
counter = 0

for num in list_of_numbers:
    if num > average_in_list:
        list_of_greater.append(num)
        counter += 1

    if counter == 5:
        break

# list_of_greater.reverse()
# list_of_greater.sort()
list_of_greater = list(map(str, list_of_greater))
if len(list_of_greater) == 0:
    print("No")
else:
    print(' '.join(list_of_greater))