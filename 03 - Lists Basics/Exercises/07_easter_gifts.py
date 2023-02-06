
gifts = input().split()

command = input()

while command != "No Money":
    command = command.split()
    action, current_gift = command[0], command[1]

    if action == "OutOfStock":
        for word in range(len(gifts)):
            if gifts[word] == current_gift:
                gifts[word] = "None"

    elif action == "Required":
        index = command[2]
        for item in range(len(gifts)):
            if item == int(index):
                gifts[item] = current_gift

    elif action == 'JustInCase':
        gifts[-1] = current_gift

    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
