
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

"""
4. Odd and Even Sum

You will receive a single number. You should write a function that returns the sum of all even and all odd digits in 
a given number. The result should be returned as a single string in the format:

"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

Print the result of the function on the console.

Examples
Input               Output

1000435             Odd sum = 9, Even sum = 4

3495892137259234    Odd sum = 54, Even sum = 22
"""