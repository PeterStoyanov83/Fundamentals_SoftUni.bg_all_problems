command = input()

while command != "End":
    if command !="SoftUni":
        current_string = ""
        for i in command:
            current_string += i * 2
        print(current_string)

    command = input()

"""
7. Double Char

You will be given strings until you receive the command "End". For each string given, you should print a string in
which each character (case-sensitive) is repeated twice. Note that if you receive the string "SoftUni",
you should NOT print it!

Examples
Input               Output
Hello World
Repeat
End                 HHeelllloo WWoorrlldd RReeppeeaatt

1234!
SoftUni
softuni
End                 11223344!! ssooffttuunnii
"""