data = input()

while True:

    command = input().split(':|:')
    current_command = command[0]

    if current_command == 'Reveal':
        print(f"You have a new text message: {data}")
        break

    elif current_command == 'InsertSpace':
        index = int(command[1])
        data = data[:index] + ' ' + data[index:]
        print(data)

    elif current_command == 'Reverse':
        substring = command[1]
        if substring in data:
            data = data.replace(substring, '', 1)
            data = data + substring[::-1]
            print(data)
        else:
            print('error')

    elif current_command == 'ChangeAll':
        substring, replacement = command[1], command[2]
        data = data.replace(substring, replacement)
        print(data)

