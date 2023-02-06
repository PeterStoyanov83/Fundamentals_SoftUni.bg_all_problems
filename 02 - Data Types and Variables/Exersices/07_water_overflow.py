
tank_capacity = 255
n = int(input())

filled_liters = 0
for i in range(1, n+1):
    current_liters = int(input())

    if filled_liters + current_liters <= tank_capacity:
        filled_liters += current_liters
        continue
    print("Insufficient capacity!")

print(filled_liters)
