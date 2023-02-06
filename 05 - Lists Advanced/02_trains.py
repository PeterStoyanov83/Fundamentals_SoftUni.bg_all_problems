number_of_wagons = int(input())
wagons = [0] * number_of_wagons


def adding_people(command):
    data = command.split(" ")
    people_to_add = int(data[1])
    wagons[-1] += int(people_to_add)  # adding the value in the last wagon [-1]
    return wagons


def inserting_people(command):
    data = command.split(" ")
    index = int(data[1])
    number_of_people = int(data[2])
    wagons[index] += number_of_people
    return wagons


def leaving_people(command):
    data = command.split(" ")
    index = int(data[1])
    number_of_people = int(data[2])
    wagons[index] -= number_of_people
    return wagons


while True:
    command = input()

    if command == "End":
        break

    data = command.split(" ")

    current_command = data[0]

    if current_command == "add":
        adding_people(current_command)

    elif current_command == "insert":
        inserting_people(current_command)

    elif current_command == "leave":
        leaving_people(current_command)

print(wagons)

# ________________________________________________


# number_of_wagons = int(input())
# wagons = [0] * number_of_wagons
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     data = command.split(" ")
#
#     current_command = data[0]
#
#     if current_command == "add":
#         people_to_add = data[1]
#         wagons[-1] += int(people_to_add)  # adding the value in the last wagon [-1]
#
#
#     elif current_command == "insert":
#         index = int(data[1])
#         number_of_people = int(data[2])
#         wagons[index] += number_of_people      #adding people in the indexed wagon
#
#
#     elif current_command == "leave":
#         index = int(data[1])
#         number_of_people = int(data[2])
#         wagons[index] -= number_of_people        #removing people from the indexed wagon
#
# print(wagons)
