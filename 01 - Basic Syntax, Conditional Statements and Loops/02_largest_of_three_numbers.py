first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)


'''
2. Largest of Three Numbers
Write a program that receives three whole numbers and prints the largest one.


Example:
Input       Output
 3       |
-1       |   
 5       |   5
___________________
 0       |
-1       |
-2       |   0
'''