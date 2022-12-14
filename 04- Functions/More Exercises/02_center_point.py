from math import floor
def coordinates_calc(a,b):
    result = a * a + b * b
    return abs(result)


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))


if coordinates_calc(x1, y1) <= coordinates_calc(x2, y2):
    print(f'({int(x1)}, {int(y1)})')
else:
    print(f'({int(x2)}, {int(y2)})')

"""
2. Center Point You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2
on separate lines. Write a function that prints the point which is closest to the center of the coordinate system (0, 0)
in the format: "({X}, {Y})"

If the points are at the same distance from the center, print only the first one.
The resulting coordinates must be formatted to the lower integer.

Examples

Input       Output
2
4
-1
2           (-1, 2)
______________________
10
14.5
-17.2
16          (10, 14)

"""