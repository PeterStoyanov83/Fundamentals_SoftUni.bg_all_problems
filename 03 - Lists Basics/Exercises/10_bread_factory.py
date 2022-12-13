events = input().split("|")

total_energy = 100
total_coins = 100
gained_energy = 0
factory_open = True

for event in events:
    event_items = event.split("-")
    event_type = event_items[0]
    event_value = int(event_items[1])

    if event_type == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy >= 100:
            total_energy = 100
            gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_type == "order":
        if total_energy >= event_value:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
            continue
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            factory_open = False
            print(f"Closed! Cannot afford {event_type}.")
            break

if factory_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")


"""
10. * Bread Factory

As a young baker, you are baking the bread out of the bakery.
You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. 
Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")

· If the event is "rest":
o You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: 
"You gained {gained_energy} energy.".
o After that, print your current energy: "Current energy: {current_energy}.".
· If the event is "order":
o You've earned some coins (the number in the second part).
o Each time you get an order, your energy decreases by 30 points.
§ If you have the energy to complete the order, print: "You earned {earned} coins.".
§ Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!"
· In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend.
o If you have enough money, you should buy the ingredient and print:
"You bought {ingredient}."
o Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
If you managed to handle all events throughout the day, print on the following 3 lines:
"Day completed!"
"Coins: {coins}"
"Energy: {energy}"
Input / Constraints

You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
"event1|event2| … eventN".

Each event contains an event name or an ingredient and a number, separated by a dash in the format: 
"{event/ingredient}-{number}"

Output

Print the corresponding messages described above.
Examples
Input                                       Output

rest-2|order-10|eggs-100|rest-10            You gained 0 energy. Current energy: 100. You earned 10 coins. You bought eggs. You gained 10 energy. Current energy: 80. Day completed!

Coins: 10 Energy: 80

order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000 You earned 10 coins. You earned 10 coins. You earned 10 coins. You bought flour. You had to rest! Closed! Cannot afford oven.
"""
