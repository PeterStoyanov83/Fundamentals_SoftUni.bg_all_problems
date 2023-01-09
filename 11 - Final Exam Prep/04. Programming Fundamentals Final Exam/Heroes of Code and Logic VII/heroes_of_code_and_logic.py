def cast_spell(name, mana_points, spell_n, heroes_dict):
    if heroes_dict[name]["MP"] >= mana_points:
        heroes_dict[name]['MP'] -= mp_needed
        print(f"{name} has successfully cast {spell_n} and now has {heroes_dict[name]['MP']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_n}!")
    return heroes_dict


def take_damage(hero_name, damage, attacker, heroes_dict):
    if heroes_dict[hero_name]["HP"] - damage <= 0:
        del heroes_dict[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")
    else:
        heroes_dict[hero_name]["HP"] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")
    return heroes


def recharge(name, amount_to_charge, heroes_dict):
    if heroes_dict[name]["MP"] + amount_to_charge > 200:
        print(f"{name} recharged for {200 - heroes_dict[name]['MP']} MP!")
        heroes_dict[name]["MP"] = 200
    else:
        heroes_dict[name]["MP"] += amount_to_charge
        print(f"{name} recharged for {amount_to_charge} MP!")
    return heroes_dict


def heal(hero_name, amount, heroes_dict):
    if heroes_dict[hero_name]['HP'] + amount >= 100:
        hp_gained = 100 - heroes_dict[hero_name]['HP']
    elif heroes_dict[hero_name]['HP'] + amount < 100:
        hp_gained = amount
    heroes_dict[hero_name]['HP'] += hp_gained
    print(f"{hero_name} healed for {hp_gained} HP!")
    return heroes


n = int(input())

heroes = {}

for _ in range(n):
    hero_name, hp, mp = input().split(" ")
    heroes[hero_name] = {"HP": int(hp), "MP": int(mp)}
    """this creates a dictionary where each key is a hero name and the value is a dictionary 
    containing the hero's HP and MP. The inner dictionary is referred to as a nested dictionary."""

data = input()

while data != "End":
    split_data = data.split(" - ")
    if split_data[0] == "CastSpell":
        hero_name, mp_needed, spell_name = split_data[1:]
        mp_needed = int(mp_needed)
        heroes = cast_spell(hero_name, mp_needed, spell_name, heroes)

    elif split_data[0] == "TakeDamage":
        hero_name, damage, attacker = split_data[1:]
        damage = int(damage)
        heroes = take_damage(hero_name, damage, attacker, heroes)

    elif split_data[0] == "Recharge":
        hero_name, amount = split_data[1:]
        amount = int(amount)
        heroes = recharge(hero_name, amount, heroes)

    elif split_data[0] == "Heal":
        hero_name, amount = split_data[1:]
        amount = int(amount)
        heroes = heal(hero_name, amount, heroes)

    data = input()

for name, values in heroes.items():
    print(name)
    print(f"  HP: {values['HP']}")
    print(f"  MP: {values['MP']}")
