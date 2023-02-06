money_for_beggars = [int(number) for number in input().split(", ")]

number_of_beggars = int(input())

index_of_beggar = 0

earned_money = []

while index_of_beggar < number_of_beggars:
    total = 0
    for beggar in range(index_of_beggar, len(money_for_beggars), number_of_beggars):
        total += money_for_beggars[beggar]
    earned_money.append(total)
    index_of_beggar += 1

print(earned_money)
