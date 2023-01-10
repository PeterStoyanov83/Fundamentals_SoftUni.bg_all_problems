message = input()

while True:
    command = input()
    if command == "Decode":
        break

    command = command.split("|")
    if command[0] == "Move":
        n = int(command[1])
        message = message[n:] + message[:n]


    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
