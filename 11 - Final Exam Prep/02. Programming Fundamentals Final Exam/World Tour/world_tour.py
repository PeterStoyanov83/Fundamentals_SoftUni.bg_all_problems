stops = input()

while True:
    command = input().split(":")
    if command[0] == "Travel":
        break

    elif command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index <= len(stops):
            stops = stops[:index] + string + stops[index:]
            print(stops)
        else:
            print(stops)

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + "" + stops[end_index + 1:]
            print(stops)
        else:
            print(stops)

    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
            print(stops)
        else:
            print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
