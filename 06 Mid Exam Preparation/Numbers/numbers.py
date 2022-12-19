<<<<<<< HEAD
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
=======
def sorted_func(greater_numbers):
    top_five_num = []
    for num in sorted(greater_numbers)[::-1]:
        if len(top_five_num):
            top_five_num.append(num)
        else:
            break
    return ' '.join([str(num) for num in top_five_num])


def numbers_func(numbers):
    average = sum(numbers)/ len(numbers)
    # print(average)
    greater_numbers = [num for num in numbers if num > average]

    if greater_numbers:
        print(sorted_func(greater_numbers))
    else:
        print("No")

list_of_numbers = list(map(int, input().split(" ")))
print(numbers_func(list_of_numbers))
>>>>>>> origin/main
