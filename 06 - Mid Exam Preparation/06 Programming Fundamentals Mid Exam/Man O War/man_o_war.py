def fire(index, damage):
    if 0 <= index < len(war_ship):
        war_ship[index] -= damage
        if war_ship[index] <= 0:
            commands['sunken'] = True
            print("You won! The enemy ship has sunken.")


def defend(start_index, end_index, damage_received):
    if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
        for secion in range(start_index, end_index + 1):
            pirate_ship[secion] -= damage_received
            if pirate_ship[secion] <= 0:
                commands['sunken'] = True
                print("You lost! The pirate ship has sunken.")
                break


def repair(index, repair_value):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] += repair_value
        if pirate_ship[index] > max_health_capacity:
            pirate_ship[index] = max_health_capacity


def status():
    low_hp_border = commands['max_health'] * 0.2
    count_of_repaired_ships = [ship for ship in pirate_ship if ship < low_hp_border]
    print(f"{len(count_of_repaired_ships)} sections need repair.")


pirate_ship = [int(item) for item in input().split(">")]
war_ship = [int(item) for item in input().split(">")]
max_health_capacity = int(input())

'using commands in a dictionary form'
commands = {
    'Fire': fire,
    'Defend': defend,
    'Repair': repair,
    'Status': status,
    'max_health': max_health_capacity,
    'sunken': False
}
command = input()
while command != "Retire":
    operation, *data = [item if item.isalpha() else int(item) for item in command.split()]
    commands[operation](*data)
    if commands['sunken']:
        break
    command = input()
if not commands['sunken']:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
