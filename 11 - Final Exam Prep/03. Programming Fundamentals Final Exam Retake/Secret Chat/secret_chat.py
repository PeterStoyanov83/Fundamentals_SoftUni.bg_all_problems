def insert_space(index, data):
    # slicing and adding a space on the current index
    data = data[:index] + " " + data[index:]
    print(data)


def reverse(substring, data):

    if substring in data:
        data = data.replace(substring, "", 1)  # replace 1st match of the substring with nothing ("")
        data = data + substring[::-1]  # adding the reversed substring to the end of the data string
        print(data)
    else:
        print("error")


def change_all(substring, replacement, data):
    data = data.replace(substring, replacement)
    print(data)


data = str(input())


while True:
    command = input().split(':|:')
    if command == "Reveal":
        print(f"You have a new text message: {data}")
        break

    elif command[0] == "InsertSpace":
        index = int(command[1])
        insert_space(index, data)

    elif command[0] == "Reverse":
        substring = command[1]
        reverse(substring, data)

    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        change_all(substring, replacement, data)


# ______________________________________________________
# data = input()
#
# while True:
#
#     command = input().split(':|:')
#     current_command = command[0]
#
#     if current_command == 'Reveal':
#         print(f"You have a new text message: {data}")
#         break
#
#     elif current_command == 'InsertSpace':
#         index = int(command[1])
#         data = data[:index] + ' ' + data[index:]
#         print(data)
#
#     elif current_command == 'Reverse':
#         substring = command[1]
#         if substring in data:
#             data = data.replace(substring, '', 1)
#             data = data + substring[::-1]
#             print(data)
#         else:
#             print('error')
#
#     elif current_command == 'ChangeAll':
#         substring, replacement = command[1], command[2]
#         data = data.replace(substring, replacement)
#         print(data)
