deck = input().split()
shuffle_count = int(input())

for i in range(shuffle_count):
    left_half = deck[:len(deck) // 2]
    right_half = deck[len(deck) // 2:]

    deck = [None] * len(deck)  # creating the placeholders in a list with the leingh of the deck
    for j in range(len(deck) // 2):
        deck[2 * j] = left_half[j]
        deck[2 * j + 1] = right_half[j]

print(deck)
