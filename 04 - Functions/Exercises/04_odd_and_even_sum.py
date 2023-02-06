def sum_of_odd_and_even(n):
    sum_of_odd = 0
    sum_of_even = 0
    for i in n:
        if int(i) % 2 == 0:
            sum_of_even += int(i)
        else:
            sum_of_odd += int(i)
    return f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}"


number = input()

print(sum_of_odd_and_even(number))
