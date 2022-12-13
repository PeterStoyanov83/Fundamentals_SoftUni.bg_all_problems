fire_with_cells = input().split("#")
current_water = int(input())
putted_out_fire_cells = []
effort = 0
for cell in fire_with_cells:
    is_valid = False
    list_with_cells = cell.split()
    water_needed = int(list_with_cells[2])
    if current_water >= water_needed:
        if "High" in list_with_cells and water_needed in range(81, 126) or \
         "Medium" in list_with_cells and water_needed in range(51, 81) or \
         "Low" in list_with_cells and water_needed in range(1, 51):
            is_valid = True
    if is_valid:
        putted_out_fire_cells.append(water_needed)
        effort += water_needed * 0.25
        current_water -= water_needed

print("Cells:")
for cell in putted_out_fire_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}\nTotal Fire: {sum(putted_out_fire_cells)}")


"""
8. * Seize the Fire

The group of adventurists have gone on their first task. Now they have to walk through fire - literally.
They have to use all of the water they have left. Your task is to help them survive.Create a program that calculates
the water that is needed to put out a "fire cell", based on the given information
about its "fire level" and how much it gets affected by water. First, you will be given the level of fire inside the
cell with the integer value of the cell, which represents the needed water to put out the fire.
They will be given in the following format:

"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"

Afterwards you will receive the amount of water you have for putting out the fires. There is a range of fire for each
of the fire types, and if a cell’s value is below or exceeds it, it is invalid and you don’t need to put it out.

        Type of Fire        Range
            High            81 - 125
            Medium          51 - 80
            Low             1 - 50

If a cell is valid, you have to put it out by reducing the water with its value. Putting out fire also takes effort
and you need to calculate it. Its value is equal to 25% of the cell’s value. In the end you will have to print the
total effort. Keep putting out cells until you run out of water. If you don’t have enough water to put out a given cell
 – skip it and try the next one. In the end, print the cells you have put out in the following format:
"Cells:
- {cell1}
- {cell2}
- {cell3}
……
- {cellN}"
"Effort: {effort}"
In the end, print the total fire you have put out from all of the cells in the following format:
"Total Fire: {totalFire}"

Input / Constraints
· On the 1st line you are going to receive the fires with their cells in the format described above – integer
    numbers in the range [1…500]
· On the 2nd line, you are going to be given the water – an integer number in the range [0….100000]

Output
· Print the cells, which you have put out in the following format:

"Cells:
- {cell}
- {cell2}
- {cell3}
- {cell5}
……
- {cellN}"
· Print the effort, rounded 2 digits after the decimal separator in the following format:
"Effort: {effort}"
· Print the total fire put out
"Total Fire: {totalFire}"

Examples
Input                                       Output
High = 89#Low = 28#Medium = 77#Low = 23
1250                                        Cells: - 89 - 28 - 77 - 23 Effort: 54.25 Total Fire: 217

Comments:
After reading the output, we start checking the level of the fire and its validity. The first is valid, so we
subtract the 89 from the amount of water – 1250, and the water becomes 1161. We need to calculate the
effort, which is 25% of 89. We will add 89 to the total fire we have put out. In the end the effort is 54.22 and
the total fire: 217
"""