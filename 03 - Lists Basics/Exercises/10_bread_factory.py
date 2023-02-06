events = input().split("|")

total_energy = 100
total_coins = 100
gained_energy = 0
factory_open = True

for event in events:
    event_items = event.split("-")
    event_type = event_items[0]
    event_value = int(event_items[1])

    if event_type == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            gained_energy = 100 - current_energy
            total_energy = 100
        else:
            gained_energy = event_value
        print(f"You gained {int(gained_energy)} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_type == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
            continue
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            factory_open = False
            print(f"Closed! Cannot afford {event_type}.")
            break

if factory_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
