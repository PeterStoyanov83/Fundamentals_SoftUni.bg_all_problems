
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



"""
7. Water Overflow

You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines,
which will follow. On the following n lines, you will receive liters of water (integers), which you should pour into
your tank.

If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line,
print the liters in the tank.

Input           Output              

5
20
100             Insufficient capacity!                  
100             240
100
20             
"""