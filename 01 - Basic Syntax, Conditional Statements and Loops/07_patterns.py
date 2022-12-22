
num = int(input())
for i in range (1, num +1, 1 ):
    for j in range( 0, i):
        print("*", end="")
    print()
for i in range(num - 1, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()


"""
7. Patterns

Write a program that receives a number and creates the following pattern. 
The number represents the largest count of stars on one row.

Example

Input   Output

3       * 
        ** 
        *** 
        ** 
        *

5       * 
        ** 
        *** 
        **** 
        ***** 
        **** 
        *** 
        ** 
        *

"""

