def factorial(n):
    for factorial in range(1, n):
        n *= factorial
    return n


first_n = int(input())
second_n = int(input())
result = factorial(first_n) / factorial(second_n)
print(f"{result:.2f}")
