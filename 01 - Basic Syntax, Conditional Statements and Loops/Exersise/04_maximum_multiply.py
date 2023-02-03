divisor = int(input())
boundry =  int(input())
max_multiple = 0
for i in range(1, boundry+1):
    if i % divisor == 0:
        max_multiple = i
print(max_multiple)
