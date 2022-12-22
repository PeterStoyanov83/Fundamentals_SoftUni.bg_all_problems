def calculate(price_calc, num):
    if order == "coffee":
        price_calc = num * 1.50
    elif order == "water":
        price_calc = num * 1.0
    elif order == "coke":
        price_calc = num * 1.40
    elif order == "snacks":
        price_calc = num * 2.00
    print(f"{price_calc:.2f}")


order = input()
n = float(input())

calculate(order, n)
