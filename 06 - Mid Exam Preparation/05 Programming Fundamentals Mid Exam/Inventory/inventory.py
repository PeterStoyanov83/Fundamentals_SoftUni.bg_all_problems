
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
            # print(inventory)
            if item1 in inventory:
                index = inventory.index(item1) + 1
                inventory.insert(index, item2)

            # print(inventory)
        elif action == "Renew":
            # print(inventory)
            if item in inventory:
                inventory.remove(item)
                inventory.append(item)
            # print(inventory)

print(", ".join(inventory))
#
# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!
