
def multiplication_identifier(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "zero"
    elif a < 0 or b < 0 or c < 0:
        return "negative"
    elif (a > 0 and b > 0 and c > 0) or (a > 0 and b < 0 and c < 0) or (b > 0 and a < 0 and c < 0) or (c > 0 and a < 0 and b < 0):
        return "positive"


num1, num2, num3 = int(input()), int(input()), int(input())

print(multiplication_identifier(num1, num2, num3))

