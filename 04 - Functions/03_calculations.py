def solve(a, b, op):
    result = None
    if op == "multiply":
        result = a * b
    elif op == "divide":
        result = int(a / b)
    elif op == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


operator = input()
num_1 = int(input())
num_2 = int(input())

print(solve(num_1, num_2, operator))
