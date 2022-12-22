number = float(input())

while number < 1 or number > 100:
    number = float(input())
print(f"The number {number} is between 1 and 100")




"""
5. Number Between 1 and 100

Write a program that reads different floating-point numbers from the console. 
When it receives a number between 1 and 100 inclusive, the program should stop reading and should print 
"The number {number} is between 1 and 100".

Example

Input                   Output
-3
0.9
44                      The number 44.0 is between 1 and 100
_______________________________________________________________
0.5
90
-4
101                     The number 90.0 is between 1 and 100

"""