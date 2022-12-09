divisor = int(input())
boundry =  int(input())
max_multiple = 0
for i in range(1, boundry+1):
    if i % divisor == 0:
        max_multiple = i
print(max_multiple)


"""
4. Maximum Multiple

On the first line, you will be given a positive number, which will serve as a divisor.
On the second line, you will receive a positive number that will be the boundary.
You should find the largest integer N, that is:

· divisible by the given divisor
· less than or equal to the given bound
· greater than 0

Note: it is guaranteed that N is found.

Examples:
Input               Output

2
7                   6
____________________________________
10
50                  50
____________________________________
37
200                 185
"""