# list_of_numbers = list(map(int, input().split(", ")))
# upper_boundary = 10
# lower_boundary = 0
# result = []
# sorted_list = sorted(list_of_numbers)
# sorted_list = reversed(sorted_list)
#
# for num in range(sorted_list, 0, -1):
#     current_list = []
#     for num in list_of_numbers:
#         if (num) >= lower_boundary and (num) <= upper_boundary:
#             current_list.append(num)
#             sorted_list.remove(num)
#     result.append(current_list)
#     print(f"Group of {upper_boundary}'s: {current_list}")
#     lower_boundary = upper_boundary
#     upper_boundary += 10
# print(f"Group of {upper_boundary}'s: {sorted_list}")


numbers = list(map(int, input().split(", ")))
tens = 0

while numbers:
    tens += 10
    current_list = list(filter(lambda n: n <= tens, numbers))
    numbers = [num for num in numbers if num not in current_list]
    print(f"Group of {tens}'s: {current_list}")
