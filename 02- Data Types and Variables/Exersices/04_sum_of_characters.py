n = int(input())
sum_of_chars = 0

for i in range(1, n + 1):
    char = input()
    sum_of_chars += int(ord(char))

print(f"The sum equals: {sum_of_chars}")
"""
4. Sum of Chars

Write a program, which sums the ASCII codes of N characters and prints the sum on the console. On the first line, 
you will receive N – the number of lines. On the following N lines – you will receive a letter per line. 
Print the total sum in the following format: "The sum equals: {total_sum}".

Note: n will be in the interval [1…20].

Examples

Input           Output 

5
A
b
C
d
E               The sum equals: 399 
_____________________________________________
12 
S 
o 
f 
t 
U 
n 
i 
R 
u 
l 
z 
z               The sum equals: 1263

"""