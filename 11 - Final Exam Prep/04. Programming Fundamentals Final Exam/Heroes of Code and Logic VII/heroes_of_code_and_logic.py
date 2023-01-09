n = int(input())

heroes = {}

for _ in range(n):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {"HP": int(hp), "MP": int(mp)}
    """this creates a dictionary where each key is a hero name and the value is a dictionary 
    containing the hero's HP and MP. The inner dictionary is referred to as a nested dictionary."""

data = input()

while data != "End":
    split_data = data.split(" - ")
    if split_data[0] == "CastSpell":
        hero_name, mp_needed, spell_name = split_data[1:]
        mp_needed = int(mp_needed)
        if heroes[hero_name]["MP"] >= mp_needed:
            heroes[hero_name]['MP'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif split_data[0] == "TakeDamage":
        hero_name, damage, attacker = split_data[1:]
        damage = int(damage)

        if heroes[hero_name]["HP"] - damage <= 0:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")

    elif split_data[0] == "Recharge":
        hero_name, amount = split_data[1:]
        amount = int(amount)
        if heroes[hero_name]['MP'] + amount >= 200:
            mp_gained = 200 - heroes[hero_name]['MP']
        elif heroes[hero_name]['MP'] + amount < 200:
            mp_gained = amount
        heroes[hero_name]['MP'] += mp_gained
        print(f"{hero_name} recharged for {mp_gained} MP!")

    elif split_data[0] == "Heal":
        hero_name, amount = split_data[1:]
        amount = int(amount)

        if heroes[hero_name]['HP'] + amount >= 100:
            hp_gained = 100 - heroes[hero_name]['HP']
        elif heroes[hero_name]['HP'] + amount < 100:
            hp_gained = amount
        heroes[hero_name]['HP'] += hp_gained
        print(f"{hero_name} healed for {hp_gained} HP!")

    data = input()

for name, values in heroes.items():
    print(name)
    print(f"  HP: {values['HP']}")
    print(f"  MP: {values['MP']}")

# _________________solution by open AI ______________________
# n = int(input())
#
# heroes = {}
#
# for i in range(n):
#     hero_info = input().split()
#     name = hero_info[0]
#     hp = int(hero_info[1])
#     mp = int(hero_info[2])
#     heroes[name] = {'HP': hp, 'MP': mp}
#
# while True:
#     command = input().split(" - ")
#     if command[0] == "End":
#         break
#     elif command[0] == "CastSpell":
#         hero = command[1]
#         mp_needed = int(command[2])
#         spell = command[3]
#         if heroes[hero]['MP'] < mp_needed:
#             print(f"{hero} does not have enough MP to cast {spell}!")
#         else:
#             heroes[hero]['MP'] -= mp_needed
#             print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['MP']} MP!")
#     elif command[0] == "TakeDamage":
#         hero = command[1]
#         damage = int(command[2])
#         attacker = command[3]
#         heroes[hero]['HP'] -= damage
#         if heroes[hero]['HP'] <= 0:
#             print(f"{hero} has been killed by {attacker}!")
#             heroes.pop(hero)
#         else:
#             print(f"{hero} was hit for {damage}")
