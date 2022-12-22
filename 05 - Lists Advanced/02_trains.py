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
"""
2. Trains

You will receive a number representing the number of wagons a train has. Create a list (train) with the given length
containing only zeros. Until you receive the command "End", you will receive some of the following commands:

· "add {people}" – you should add the number of people in the last wagon
· "insert {index} {people}" - you should add the number of people at the given wagon
· "leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which
the people will be more than the count in the wagon.

There will be no case in which the index is invalid!

After you receive the "End" command print the train.

Example

Input           Output

3
add 20
insert 0 15
leave 0 5
End             [10, 0, 20]
______________________________
5
add 10
add 20
insert 0 16
insert 1 44
leave 1 12
insert 2 100
insert 4 61
leave 4 1
add 15
End             [16, 32, 100, 0, 105]
"""