initial_list = list(map(str, input().split("!")))

while True:
    command = input()
    if command == "Go Shopping!":
        break

    commands = command.split(" ")

    if commands[0] == "Urgent":
        if commands[1] in initial_list:
            continue
        else:
            initial_list.remove(commands[1])
            initial_list.insert(0, commands[1])


    elif commands[0] == "Unnecessary":
        if commands[1] in initial_list:
            initial_list.remove(commands[1])


    elif commands[0] == "Correct":
        old_item = commands[1]
        new_item = commands[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list.insert(index, new_item)
            del initial_list[index + 1]


    elif commands[0] == "Rearrange":
        if commands[1] in initial_list:
            initial_list.remove(commands[1])
            initial_list.insert(len(initial_list), commands[2])

print(*initial_list, sep=", ")

#
# def urgent(item):
#     if item not in products:
#         products.insert(0, item)
#
#
# def unnecessary(item):
#     if item in products:
#         products.remove(item)
#
#
# def correct(old_item, new_item):
#     if old_item in products:
#         index = products.index(old_item)
#         products.insert(index, new_item)
#         del products[index + 1]
#
#
# def rearrange(item):
#     if item in products:
#         products.remove(item)
#         products.insert(len(products), item)
#
#
# products = input().split("!")
# command = input()
# while command != "Go Shopping!":
#     command = command.split()
#     event = command[0]
#     product = command[1]
#     if event == "Urgent":
#         urgent(product)
#     elif event == "Unnecessary":
#         unnecessary(product)
#     elif event == "Correct":
#         old_item = command[1]
#         new_item = command[2]
#         correct(old_item, new_item)
#     elif event == "Rearrange":
#         rearrange(product)
#     command = input()
#
# print(*products, sep=", ")