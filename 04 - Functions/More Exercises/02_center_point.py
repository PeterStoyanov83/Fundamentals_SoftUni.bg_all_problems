from math import floor


def coordinates_calc(a, b):
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
