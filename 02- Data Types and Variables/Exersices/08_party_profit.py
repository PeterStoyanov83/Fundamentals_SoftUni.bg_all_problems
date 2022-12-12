from math import floor
party_size = int(input())
days_of_adventure = int(input())
total_coins = 0
for day in range(1, days_of_adventure + 1):

    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5

    total_coins += 50
    total_coins -= 2 * party_size  #party is spnding for food

    if day % 3 == 0:
        total_coins -= 3 * party_size    # party is spending for drinking water
    if day % 5 == 0:
        total_coins += 20 * party_size
        if day % 3 == 0:
            total_coins -= 2 * party_size    #party is spending more for drinking water

coins_per_person = floor(total_coins / party_size)
print(f"{party_size} companions received {coins_per_person} coins each.")



"""
8. * Party Profit

As a young adventurer, you travel with your group worldwide, seeking for gold and glory. But you need to split the
profit among your companions.

You will receive a group size. After that, you receive the days of the adventure.
    Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
    Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
    Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion. But if you have a motivational
        party the same day, you spend additional 2 coins per companion.
    Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15th (fifteenth)
        day 5 (five) new companions are joined at the beginning of the day.

You should calculate how many coins gets each companion at the end of the adventure.

Input / Constraints

The input will consist of exactly 2 lines:

        · group size – integer in the range [1…100]
        · days – integer in the range [1…100]

Output

Print the following message: "{companions_count} companions received {coins} coins each."
Note: You cannot split a coin, so you should round down the coins to an integer number.

Examples

Input       Output

3
5           3 companions received 90 coins each.
___________________________________________________________
15
30          19 companions received 102 coins each.

"""