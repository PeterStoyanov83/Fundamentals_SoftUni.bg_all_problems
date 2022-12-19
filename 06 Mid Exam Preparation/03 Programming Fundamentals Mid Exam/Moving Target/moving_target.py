def shoot_func(index, power, targets):
    if 0 <= index < len(targets):
        if targets[index] - power <= 0:
            targets.pop(index)
        else:
            targets[index] -= power

    return targets


def add_func(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")

    return targets


def strike_func(index, radius, targets):
    validator_index = index - radius >= 0 and index + radius < len(targets)

    if validator_index:
        start_target_index = index - radius
        final_target_index = index + radius

# removing items in range in the middle of the list
        targets = [targets[i] for i in range(len(targets)) if i < start_target_index or i > final_target_index]
    else:
        print("Strike missed!")

    return targets


def moving_targets(targets):
    while True:
        command = input()

        if command == 'End':
            print('|'.join([str(num) for num in targets]))
            break

        command = command.split(' ')
        current_command = command[0]
        first_element = int(command[1])
        second_element = int(command[2])

        if current_command == 'Shoot':
            targets = shoot_func(first_element, second_element, targets)
        elif current_command == 'Add':
            targets = add_func(first_element, second_element, targets)
        elif current_command == 'Strike':
            targets = strike_func(first_element, second_element, targets)


data = list(map(int, input().split(' ')))
moving_targets(data)

# targets = input().split(" ")
#
# line = input()
#
# while line != "End":
#     command_list = line.split(' ')
#     command = command_list[0]
#     index = int(command_list[1])
#     value = int(command_list[2])
#
#     if command == "Shoot" and index >= 0 and index < len(targets):
#         current_target = int(targets[index])
#         current_target -= value
#         if current_target <= 0:
#             targets.pop(index)
#         else:
#             targets[index] = current_target
#
#     elif command == "Add":
#         if index >= 0 and index < len(targets):
#             targets.insert(index, value)
#         else:
#             print("Invalid placement!")
#     elif command == "Strike":
#         if index - value >= 0 and index + value < len(targets):
#             targets = targets[0:index - value] + targets[index + value + 1:]
#         else:
#             print("Strike missed!")
#     line = input()
#
# targets = list(map(str, targets))
# output = "|".join(targets)
# print(output)
