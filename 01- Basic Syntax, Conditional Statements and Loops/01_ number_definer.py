
number = float(input())

if number == 0:
    print("zero")
if number > 0:
    if 0 < number < 1:
        print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("positive")
elif number < 0:
    if 0 > number > -1:
        print("small negative")
    elif number < -1000000:
        print("large negative")
    else:
        print("negative")


'''

1. Number Definer

Write a program that reads a floating-point number and:
    - prints "zero" if the number is zero
    - prints "positive" or "negative"
    - adds "small" if the absolute value of the number is less than 1 and it is not 0, 
    or "large" if it exceeds 1 000 000

Example :


Input                   Output

25                      positive

0.7                     small positive

435247392.921           large positive

-0.005                  small negative

-103.21                 negative

-358583355123.001       large negative

'''