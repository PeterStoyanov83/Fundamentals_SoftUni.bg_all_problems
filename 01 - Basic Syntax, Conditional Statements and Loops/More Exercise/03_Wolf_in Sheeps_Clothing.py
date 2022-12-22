text = input()

check_for_wolf = text.split(", ")
check_for_number = len(check_for_wolf) - 1

for wolf in check_for_wolf:

    if wolf == "wolf" and check_for_number == 0:
        text_to_print = "Please go away and stop eating my sheep"

    elif wolf == "wolf":
        text_to_print = f"Oi! Sheep number {check_for_number}! You are about to be eaten by a wolf!"

    check_for_number -= 1

print(text_to_print)


"""
3. Wolf in Sheep's Clothing

Wolves have been reintroduced to Great Britain. You are a sheep farmer and are now plagued by wolves who pretend to be
sheep. Fortunately, you are good at spotting them. Warn the sheep in front of the wolf that it is about to be eaten.
Remember that you are standing at the front of the queue, which is at the end of the list:

[sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)

4 3 2 1

If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". Otherwise, return
"Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

Note: there will always be exactly one wolf on the list.

Input
The input will be a single string containing the animals separated by a comma and a single space ", "

Examples

Input                       Output

sheep, sheep, wolf          Please go away and stop eating my sheep

wolf, sheep, sheep,
sheep, sheep, sheep         Oi! Sheep number 5! You are about to be eaten by a wolf!

"""