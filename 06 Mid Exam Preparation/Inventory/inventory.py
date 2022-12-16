
inventory = list(map(str, input().split(", ")))


while True:
    command = input()
    if command == "Craft!":
        break

    else:
        command = command.split(" - ")
        action = command[0]
        item = command[1]
        if action == "Collect":
            if item not in inventory:
                inventory.append(item)
            else:
                continue
        elif action == "Drop":
            if item in inventory:
                inventory.remove(item)
            else:
                continue
        elif action == "Combine Items":
            items = item.split(":")
            item1 = items[0]
            item2 = items[1]
            for i in range(len(inventory)):
                if item1 in inventory:
                    inventory.insert(i + 1, items[1])
        elif action == "Renew":
            if item in inventory:
                inventory.remove(item)
                inventory.insert(-1, item)

print(", ".join(inventory))
#
# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!
