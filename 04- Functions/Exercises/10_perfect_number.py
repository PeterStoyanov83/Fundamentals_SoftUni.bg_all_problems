def perfect_number(n):
    sum = 0
    for divior in range(1, n):
        if n % divior == 0:
            sum += divior
    if n == sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())

print(perfect_number(number))
