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

"""
5. Faro Shuffle

A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards 
in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original 
top card is still on top.

For example, faro shuffling the list
['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six' ]

Write a program that receives a single string (cards separated by a space) and on the second line receives a number of 
faro shuffles that have to be made. Print the state of the deck after the shuffle

Note: The length of the deck of cards will always be an even number

Example
Input                       Output
a b c d e f g h
5                           ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

one two three four
3                           ['one', 'three', 'two', 'four']
"""