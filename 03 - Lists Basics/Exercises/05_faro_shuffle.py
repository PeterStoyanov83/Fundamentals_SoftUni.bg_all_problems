deck_of_cards = input()
shuffles = int(input())
final_deck = []

for shuffle in range(shuffles):

    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0 : middle_of_deck]
    right_part = deck_of_cards[middle_of_deck::]

    for card_index in range(len(left_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    deck_of_cards = final_deck

print(final_deck)
