first_str = input()

second_str = input()

last_printed_str = first_str

for character in range( len(first_str)):
    left_part = second_str[:character+1]
    right_part = first_str[character+1:]
    current_str = left_part + right_part
    if current_str == last_printed_str:
        continue
    last_printed_str = current_str
    print(current_str)


"""
10. * Mutate Strings
You will be given two strings. Transform the first string into the second one, letter by letter, starting 
from the first one. After each interaction, print the resulting string only if it is unique.

Note: the strings will have the same length.

Examples
Input               Output

bubble gum
turtle hum          tubble gum 
                    turble gum 
                    turtle gum 
                    turtle hum

Kitty
Doggy               Ditty 
                    Dotty 
                    Dogty 
                    Doggy
"""