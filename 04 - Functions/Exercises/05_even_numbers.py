def filter_even (n):
   if n % 2 == 0:
       return True
   else:
       return False

num = list(map(int, input().split()))

result = list(filter(filter_even, num))
print(result)


"""
5. Even Numbers

Write a program that receives a sequence of numbers (integers) separated by a single space. 
It should print a list of only the even numbers. Use filter().

Example

Input           Output

1 2 3 4         [2, 4]

1 2 3 -1 -2 -3  [2, -2]
"""