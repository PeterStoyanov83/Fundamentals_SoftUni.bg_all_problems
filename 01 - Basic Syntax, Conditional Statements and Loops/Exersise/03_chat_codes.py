
number = int(input())

for i in range(number):
    message = int(input())
    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message != 88 and message != 86 and message < 88:
        print("GREAT!")
    elif message > 88:
        print("Bye.")

"""
3. Chat Codes

Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes.
He starts by creating a program for only four messages.
Create a program that receives the n number of messages sent. On the following n lines, it will receive integer numbers.
 For each number, the program should print a different message:

· If the number is 88 - "Hello"
· If the number is 86 - "How are you?"
· If the number is not 88 nor 86, and it is below 88 - "GREAT!"
· If the number is over 88 - "Bye."

Examples:
Input               Output

4
88
86
2
105                 Hello How are you? GREAT! Bye.

3
88
88
89                  Hello Hello Bye.
"""