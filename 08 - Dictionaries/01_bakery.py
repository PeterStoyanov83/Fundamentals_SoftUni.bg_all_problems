elements = input().split(" ")
bakery_dict = {}

# # no 1 ** FOR LOOP **
# for i in range(0, len(elements), 2):
#     bakery_dict[elements[i]] = int(elements[i + 1])

# no 2  - Comprehension
bakery_dict = {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}

print(bakery_dict)
