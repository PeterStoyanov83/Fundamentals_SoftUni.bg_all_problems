n = int(input())
numbers = []
filtered_num = []


for i in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered_num.append(number)

elif command == "odd":
    for number in numbers:
        if number % 2!= 0:
            filtered_num.append(number)

elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered_num.append(number)

elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered_num.append(number)

print(filtered_num)
"""
On the first line, you will receive a single number n. On the following n lines, you will receive integers. 
After that, you will be given one of the following commands:

· even
· odd
· negative
· positive

Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
"""