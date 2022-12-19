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