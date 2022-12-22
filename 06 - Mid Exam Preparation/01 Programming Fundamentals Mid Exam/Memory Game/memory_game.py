list_of_elements = list(input().split(' '))

number_of_moves = 1

while True:
    command = input()
    if command == "end":
        break
    first_index, second_index = [int(x) for x in command.split()]

    if first_index == second_index or \
            first_index >= len(list_of_elements) or first_index < 0 or \
            second_index >= len(list_of_elements) or second_index < 0:
        mid_index = len(list_of_elements) // 2
        list_of_elements.insert(mid_index, f'-{number_of_moves}a')
        list_of_elements.insert(mid_index, f'-{number_of_moves}a')
        print("Invalid input! Adding additional elements to the board")
    elif first_index != second_index and list_of_elements[first_index] == list_of_elements[second_index]:
        removed_element = list_of_elements[first_index]
        list_of_elements.remove(removed_element)
        list_of_elements.remove(removed_element)
        print(f"Congrats! You have found matching elements - {removed_element}!")
    elif list_of_elements[first_index] != list_of_elements[second_index]:
        print("Try again!")

    if len(list_of_elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break
    number_of_moves += 1

if len(list_of_elements) > 0:
    if list_of_elements:
        print("Sorry you lose :(")
        print(' '.join(list_of_elements))

