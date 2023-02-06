to_do_notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    data = command.split("-")

    priority = int(data[0]) - 1
    note = str(data[1])
    to_do_notes.pop(priority)
    to_do_notes.insert(priority, note)

final_to_do_list = [element for element in to_do_notes if element != 0]

print(final_to_do_list)
