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

"""
10. * Gladiator Expenses

As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a helmet,
a sword, a shield, and an armor.
You will receive Peter's lost fights count.
Every second lost game, his helmet is broken.
Every third lost game, his sword is broken.
When both his sword and helmet are broken in the same lost fight, his shield also breaks.
Every second time his shield brakes, his armor also needs to be repaired.
You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.

Input / Constraints
The input will consist of 5 lines:
· On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
· On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
· On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
· On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
· On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].

Output
· As output, you must print Peter`s total expenses for newhealth equipment: "Gladiator expenses: {expenses} aureus"

Examples:
    
Input          Output                                  Comment

7              Gladiator expenses: 16.00 aureus        Trashed helmet -> 3 times
2                                                      Trashed sword -> 2 times
3                                                      Trashed shield -> 1 time
4
5                                                      total: 6 + 6 + 4 = 16.00 aureus;
__________________________________________________________________________________________
23
12.50
21.50
40
200               Gladiator expenses: 608.00 aureus
"""