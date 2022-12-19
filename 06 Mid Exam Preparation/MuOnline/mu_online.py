health = 100
bitcoins = 0
dungeon = list(map(str, input().split('|')))
hero_is_dead = False

for room in dungeon:
    command = room.split()
    current_command = command[0]
    current_value = command[1]

    if current_command == "potion":
        new_health = health + int(current_value)
        if new_health > 100:
            new_health = 100
        healed = abs(100 - health)


        print(f"You healed for {healed} hp.")
        print(f"Current health: {new_health} hp.")
        health = new_health

    elif current_command == "chest":
        bitcoins += int(current_value)
        print(f"You found {current_value} bitcoins.")

    else:
        monster = current_command
        attack = current_value
        health -= int(attack)
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {len(room) - 1}")
            hero_is_dead = True
            break

if hero_is_dead == False:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
