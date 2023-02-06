lost_battles = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_broken = lost_battles // 2
swords_broken = lost_battles // 3
shields_broken = lost_battles // 6
armomrs_broken = shields_broken // 2

total_expences = helmet_price * helmets_broken + \
                 sword_price * swords_broken + \
                 shield_price * shields_broken + \
                 armor_price * armomrs_broken

print(f'Gladiator expenses: {total_expences:.2f} aureus')
