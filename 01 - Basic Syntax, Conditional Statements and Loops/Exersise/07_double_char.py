command = input()

while command != "End":
    if command != "SoftUni":
        current_string = ""
        for i in command:
            current_string += i * 2
        print(current_string)

    command = input()
