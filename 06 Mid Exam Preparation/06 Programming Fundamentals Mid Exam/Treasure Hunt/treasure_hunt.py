def loot_treasure(current_treasure_chest, *items_to_loot):
    for item in items_to_loot:
        if item not in current_treasure_chest:
            current_treasure_chest.insert(0, item)
    return current_treasure_chest


def drop_item(current_treasure_chest, index_of_item):
    if 0 <= index_of_item < len(current_treasure_chest):
        current_treasure_chest.append(current_treasure_chest.pop(index_of_item))
    return current_treasure_chest


def steal_treasure(current_treasure_chest, count_of_stolen_items):
    stolen_items = current_treasure_chest[-count_of_stolen_items:]
    current_treasure_chest = current_treasure_chest[:-count_of_stolen_items]
    print(', '.join(stolen_items))
    return current_treasure_chest


dict_operations = {
    "Loot": loot_treasure,
    "Drop": drop_item,
    "Steal": steal_treasure
}
treasure_chest = input().split("|")
command = input()
while command != "Yohoho!":
    operation, *data = [item if item.isalpha() else int(item) for item in command.split()]
    if operation in dict_operations:
        treasure_chest = dict_operations[operation](treasure_chest, *data)
    command = input()
if treasure_chest:
    average_treasure_gained = sum([len(item) for item in treasure_chest]) / len(treasure_chest)
    print(f"Average treasure gain: {average_treasure_gained:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

