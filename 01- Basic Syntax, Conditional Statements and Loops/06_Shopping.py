budget = int(input())

command = input()

while command != "End":
    current_price = int(command)
    budget -= current_price
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")

"""

6. Shopping

Write a program that reads an integer number representing a budget. On the following lines, it reads integer numbers
representing the prices of each product you should buy until it receives the command "End".
During the iterations, if there is not enough budget left to buy the next product, it prints
"You went in overdraft!" and end the program.
Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."

Example

Input                   Output
100
5
End                     You bought everything needed.
______________________________________________________
50
25
20
10                      You went in overdraft!

"""