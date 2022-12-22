unpure_symbols = {
    "forbitten symbols": [",", ".", "_"]
}
number_of_strings = int(input())

for word  in range(number_of_strings):
    string_input = input()
    for letter in string_input:
        if letter in unpure_symbols["forbitten symbols"]:
            print(f"{string_input} is not pure!")
            break

    else:
        print(f"{string_input} is pure.")


"""
6. String Pureness

You will be given number n. After that, you'll receive different strings n times. Your task is to check if the given 
strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":

· If a string is pure, print "{string} is pure."

· Otherwise, print "{string} is not pure!"

Examples:

Input               Output
2
pure string
not_pure_string     pure string is pure. not_pure_string is not pure!
_________________________________________________
3
SoftUni
12345
string.pureness     SoftUni is pure. 12345 is pure. string.pureness is not pure!"""