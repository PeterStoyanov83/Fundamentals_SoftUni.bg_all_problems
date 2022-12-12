a = int(input())
b = int(input())
exchange_a = b
exchange_b = a


print(f"Before:\n"
      f"a = {a}\n"
      f"b = {b}\n"
      f"After:\n"
      f"a = {exchange_a}\n"
      f"b = {exchange_b}")

"""
1. Exchange Integers
Read two integer numbers and, after that, exchange their values. 
Print the variable values before and after the exchange, as shown below:

Examples
Input               Output

5

10                  Before: a = 5 b = 10 After: a = 10 b = 5

________________________________________________________________
10

20                  Before: a = 10 b = 20 After: a = 20 b = 10

Hints

You may use a temporary variable to remember the old value of a, then assign the value of b to a, then assign 
the value of the temporary variable to b.

"""